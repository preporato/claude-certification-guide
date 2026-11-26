# Claude Certified Developer - Professional (CCDV-P): The Complete Study Guide

A full preparation guide for Anthropic's Professional-tier developer exam. Part I teaches the material by topic, one chapter per exam domain. Part II re-indexes it by the official skills for revision. Part III covers trap answers, worked questions, and a final checklist.

Maintained by [preporato.com](https://preporato.com). Facts checked in November 2026 against the official exam guide (version 1.0, November 2026), Anthropic's program pages, and the current Claude API and Claude Code documentation.

---

## Contents

- [Introduction](#introduction)
- [Exam format](#exam-format)
- **Part I: The material**
  - [Chapter 1: Advanced agent architecture and orchestration](#chapter-1-advanced-agent-architecture-and-orchestration)
  - [Chapter 2: Production integration, reliability, and grounding](#chapter-2-production-integration-reliability-and-grounding)
  - [Chapter 3: Observability and production monitoring](#chapter-3-observability-and-production-monitoring)
  - [Chapter 4: Advanced debugging and incident response](#chapter-4-advanced-debugging-and-incident-response)
  - [Chapter 5: Evaluation engineering and quality assurance](#chapter-5-evaluation-engineering-and-quality-assurance)
  - [Chapter 6: Cost and latency at scale](#chapter-6-cost-and-latency-at-scale)
  - [Chapter 7: Runtime guardrails and production security](#chapter-7-runtime-guardrails-and-production-security)
  - [Chapter 8: Agent fleet operations for software delivery](#chapter-8-agent-fleet-operations-for-software-delivery)
- **Part II: Exam domain notes**
  - [All eight domains](#part-ii-exam-domain-notes)
- **Part III: Exam preparation**
  - [The preparation ladder](#the-preparation-ladder)
  - [The ten trap answers](#the-ten-trap-answers)
  - [Exam-day strategy](#exam-day-strategy)
  - [Worked questions](#worked-questions)
  - [6-week study plan](#6-week-study-plan)
  - [Pre-exam checklist](#pre-exam-checklist)
  - [Resources](#resources)

---

## Introduction

CCDV-P (Claude Certified Developer - Professional) is the newest Claude certification, live since November 17, 2026. It certifies the engineer who **operates** Claude systems in production: keeps them reliable under load, instruments and monitors them, diagnoses failures that only show up across thousands of traces, gates releases with evaluation, controls cost and latency across a fleet, hardens tool-using agents against adversarial input, and increasingly runs fleets of coding agents that do engineering work under supervision.

The exam assumes everything [CCDV-F](../ccdv-f/) covers (the Messages API, tools, the Agent SDK, Claude Code) and asks what happens after launch. Most items show evidence from a running system (an error mix, usage numbers, a trace, a judge's agreement rate, a red-team finding) and ask what explains it and what fixes it. Wrong options are usually things that help a little or help later; the right one addresses the cause the evidence points to.

**Who should take it:** senior and staff engineers, platform and site reliability engineers extending their practice to LLM systems, and solutions engineers accountable for live Claude applications. Anthropic's guide expects daily work with the Claude APIs and SDKs (Messages API, Agent SDK, Claude Managed Agents), Claude Code and MCP, an understanding of how first-party API deployments differ from cloud-platform ones, and at least one tool-using agent built and deployed in production. CCDV-F is recommended preparation but not a prerequisite.

**How it differs from [CCAR-P](../ccar-p/):** the architect exam asks which design to choose and what to commit to stakeholders; the developer exam asks how to run it, measure it, and fix it once it is live.

## Exam format

| | |
|---|---|
| Questions | 70: 60 scored and 10 unscored trial items you cannot tell apart |
| Duration | 120 minutes to answer, about 135 minutes of seat time |
| Question style | Scenario-based multiple choice and multiple response; each item states how many responses to select, with no partial credit |
| Passing score | 720 on a 100-1000 scaled score, with per-domain percent correct on the report |
| Delivery | Pearson VUE, online proctored (OnVUE) or at a test center |
| Price | $175 per attempt |
| Registration | Anthropic Partner Academy, open to people who work at Claude Partner Network organizations (sign in with a company email); you pay at Pearson's checkout |
| Languages | English or Japanese, chosen when you schedule |
| Prerequisites | None; CCDV-F is recommended |
| Rescheduling | Free up to 1 hour before an OnVUE appointment, 48 hours before a test center one |
| Retakes | Full fee for every attempt; waits of 14, 30 and 90 days after the first, second and third failed attempts; at most 4 attempts in any 12 months |
| Validity | 12 months; free non-proctored renewal before expiration, full proctored exam after a lapse |
| Partner tier | Counts toward Claude Partner Network tier eligibility |

### Exam domains

Numbered as in the official guide:

| Domain | Weight | ~Scored questions | Core focus |
|--------|--------|-------------------|------------|
| 1. Advanced Agent Architecture and Orchestration | 17% | ~10 | Multi-agent patterns, durable execution, architecture at scale, context and memory |
| 2. Production Integration, Reliability, and Knowledge Grounding | 20% | ~12 | Failure-class handling, throughput and quotas, MCP and change management, retrieval at scale |
| 3. Observability and Production Monitoring | 12% | ~7 | Telemetry, SLIs and SLOs, drift detection, trace analysis at scale |
| 4. Advanced Debugging and Incident Response | 10% | ~6 | Complex failure diagnosis, incident response, learning loops |
| 5. Evaluation Engineering and Quality Assurance | 12% | ~7 | Offline eval systems and gates, judge engineering, online quality |
| 6. Cost and Latency Optimization at Scale | 8% | ~5 | Fleet cost architecture, routing, caching diagnostics, latency engineering |
| 7. Runtime Guardrails and Production Security | 11% | ~7 | Layered guardrails, threat defense and red-teaming, identity and audit |
| 8. Agent Fleet Operations for Software Delivery | 10% | ~6 | Parallel coding agents, AI code review, unattended runs, organization-wide configuration |

---

# Part I: The material

## Chapter 1: Advanced agent architecture and orchestration

### 1.1 Multi-agent orchestration in production

| Pattern | How it works | Watch for |
|---------|-------------|-----------|
| Supervisor / worker | An orchestrator plans, dispatches subtasks, and synthesizes results | The supervisor's context filling with raw worker output; return compact summaries |
| Parallel dispatch | Independent subtasks run at once in isolated contexts | Hidden dependencies between "independent" tasks; conflicting results with no merge rule |
| Delegation with context isolation | A subagent gets only what its task needs and returns a result | Over-sharing context (cost, leakage) or under-sharing (the subagent guesses) |
| Approval flow | A step pauses for a person before a consequential action | Approvals on every step (reviewer fatigue) or none on the irreversible one |

Inter-agent failures are the tested part: a worker that fails silently and the supervisor that treats its empty result as "nothing found"; two workers editing the same resource; an orchestrator that retries a whole fan-out because one worker timed out. Design each hand-off with an explicit contract: what goes in, what comes back, how failure is reported.

### 1.2 Durable execution and state

Long-running agents must survive interruption, restart, and a **model version change** mid-task:

- **Session persistence:** the conversation and the agent's state live in durable storage that outlives any one process.
- **Checkpointing:** after each completed step, record what was done and what comes next, so a restart resumes instead of starting over.
- **Resumability with idempotent steps:** a resumed step that already ran must not run its side effect twice.
- **Memory architecture:** durable facts and decisions go into a memory store the agent reads at start; the transcript is not a memory system.
- **Version changes:** a checkpoint should be meaningful to the next model version. Opaque, model-bound artifacts (such as thinking blocks, which current models tie to the model and conversation that produced them) don't carry across; your recorded state and summaries do.

### 1.3 Architecture selection at scale

A running system produces the evidence for its own redesign. Move a **workflow toward an agent** when quality data shows the fixed path can't handle the variety of real inputs; move an **agent toward a workflow** when cost and reliability data show it takes the same few paths every time, at agent prices and agent variance. Team-level decisions include standardizing the **agent harness** (custom loop, Agent SDK, or Managed Agents), any framework, and reusable patterns, so that every team doesn't solve tracing, retries, and approvals differently.

### 1.4 Context and memory architecture

For agents approaching context limits or cost ceilings:

| Technique | What it does | Fits |
|-----------|-------------|------|
| Context editing | Clears old tool results (or old thinking blocks) past a threshold | Tool-heavy loops where old results are dead weight |
| Compaction | Summarizes earlier history into a shorter form | Long conversations where the thread of decisions matters |
| Persistent memory | The agent writes and reads durable notes outside the window | Knowledge that must outlive a session |
| Mid-conversation system messages | Appends an operator instruction to the conversation (on models that support it) instead of editing the cached system prompt | Changing instructions mid-session without invalidating the cache |
| Tool search with deferred loading | Keeps large tool catalogs out of context until a search finds the right tool | Dozens to hundreds of tools |
| Programmatic tool calling | Claude calls tools from code execution, so intermediate results don't flow through the context | Many calls whose intermediate output the model doesn't need to read |

The trap is a bigger context window for a context problem: it moves the cliff instead of managing what fills it.

## Chapter 2: Production integration, reliability, and grounding

### 2.1 Reliability engineering: branch on the failure class

A production client must tell failure classes apart, because each needs different handling:

| Signal | Class | Handling |
|--------|-------|---------|
| 429 `rate_limit_error` | Capacity | Back off honoring `retry-after`, queue, shed low-priority load |
| 500 `api_error`, 529 `overloaded_error` | Transient service error | Retry with exponential backoff and jitter, capped; circuit-break on sustained failure |
| 400 `invalid_request_error` | Your bug | Fix the request; never retry unchanged |
| `stop_reason: "refusal"` (HTTP 200) | Safety decline | A safety-handling path: rephrase, route, or a documented fallback model; never blind retry |
| `stop_reason: "max_tokens"` | Output budget | Raise the budget or continue; a retry reproduces the truncation |
| `stop_reason: "model_context_window_exceeded"`, or 400 "prompt is too long" | Context | Trim, compact, or split the input |

One undifferentiated retry path for all of these is a classic root cause: it multiplies cost on refusals and truncations while doing nothing for them.

Around the client:

- **Circuit breakers** stop calling a failing dependency for a cooling-off period, so a degraded model or region doesn't pile up timeouts.
- **Graceful degradation** keeps the product useful when the model isn't: a cached answer, a simpler path, an honest "try again later".
- **Fallbacks** across models, regions, or platforms keep traffic flowing, but respect **feature parity**: a fallback platform or model may not support a feature the primary request uses (a tool type, a beta, a parameter), so test the fallback path with the same requests.

The official SDKs already retry connection errors, 429s, and 5xx errors with exponential backoff (twice by default, configurable); your layer decides policy above that. Log the `request-id` header of every response: it is how Anthropic support finds a request.

### 2.2 Scale and throughput

Rate limits are measured in **requests per minute**, **input tokens per minute**, and **output tokens per minute**. On most models, input-token limits count only uncached input: cache reads don't count, cache writes do. So caching raises effective throughput as well as cutting cost. Identify the **binding constraint** before acting:

| Evidence | Binding constraint | Lever |
|----------|-------------------|-------|
| 429s with low token volume | Request rate | Batch requests, fewer and larger calls |
| 429s on input-token limits with large repeated prefixes | Input tokens | Caching, trimming context |
| Bulk work nobody waits on competing with live traffic | Wrong lane | Move it to the Message Batches API (50% off, asynchronous) |
| One tenant's spike exhausting everyone's quota | Isolation | Per-tenant quotas, queues, and workspaces |

Production patterns: **queueing with backpressure** (accept work at the rate you can serve, signal "slow down" upstream instead of failing randomly), **separate workspaces** per environment or product so limits and spend caps apply to each, and **capacity planning** from measured tokens per task times forecast volume.

### 2.3 Production MCP and change management

- **Remote MCP servers** need real authentication (OAuth or scoped tokens), versioning of tools and schemas (a renamed field is a breaking change for every client), and monitoring like any production service.
- **Gateways and routing** centralize authentication, logging, quotas, and policy for model and MCP traffic, and keep **configuration parity** across platforms (the same model settings, tools, and limits wherever the request goes).
- **Model version migrations** are tested against breaking behavior changes with the regression suite before cutover.
- **Prompt updates** are versioned and released like code: **progressive rollout** (a small share of traffic first, watching quality and cost) with a fast **rollback** path.

### 2.4 Retrieval and grounding at scale

| Choice | Prefer it when |
|--------|---------------|
| Agentic search with tools | Exploratory, multi-hop questions; constantly changing corpora; correctness over latency |
| RAG pipeline (chunk, embed, index, retrieve) | Large corpora, lookup-style questions, tight latency |
| Hybrid keyword + semantic search, then re-ranking | Exact identifiers mixed with natural language; many near-matches |

Grounding practices: **cite sources** (the API's citations feature or search-result content blocks return the passages behind each claim), **declare uncertainty** ("the documents don't cover this" is an allowed answer), and expose **confidence signals** downstream (retrieval scores, citation coverage) rather than the model's self-assessment.

Diagnose retrieval-quality failures **by stage**: was the query built well, did retrieval return the right candidates, did re-ranking keep them, did generation use them? A wrong answer with the right passage retrieved is a generation or grounding failure; a wrong answer without it is a retrieval failure.

## Chapter 3: Observability and production monitoring

### 3.1 Telemetry and instrumentation

Instrument for debuggability and privacy at the same time:

- **Distributed traces** for agent loops: one trace per task, a span per model call and per tool call, with parent-child links across subagents. The Claude SDKs can emit OpenTelemetry spans in your process, and the API can deliver its own server-side spans to your backend (both in beta at the time of writing), with a content mode that decides whether prompts and responses are exported.
- **Token and cost metrics** from every response's `usage` (`input_tokens`, `output_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`), tagged with model, tenant, and feature, so cost per task and per tenant is a sum you control.
- **Cache diagnostics:** cache hit rate (cache reads over total input); a sudden drop after a deploy usually means the cached prefix changed.
- **Grounding and reasoning traceability:** which passages and tool results each answer drew on.
- **Structured log events** (stop reason, error type, request ID, latency, retries) rather than free text.
- **Content capture under privacy constraints:** capture metadata by default, redact or sample content, restrict who can read it, and honor zero-data-retention commitments in your own logs as well as at the provider.

For organization-level reporting, the Usage and Cost API reports usage and spend; Claude Code can export OpenTelemetry metrics and events, which an organization can enforce through managed settings.

### 3.2 SLIs, SLOs, and alerting

LLM services need indicators beyond uptime:

| SLI | Why |
|-----|-----|
| Availability and error rate by class | 429s, 5xx, and 400s mean different things |
| Latency: time to first token and total | Users feel the first; pipelines feel the second |
| Refusal rate and truncation rate | Spikes signal a prompt, model, or budget change |
| Quality score from sampled online evaluation | The only signal that catches confident wrong answers |
| Cost per task and per tenant | Runaway loops and abuse show up here first |

Set SLOs on them, alert on burn rate rather than single blips, and watch specifically for **drift after model updates**: a behavioral regression often shows up as a shift in length, refusal rate, tool-call count, or quality score rather than as errors. Anomalous usage (a tenant's token use jumping tenfold) is both a cost and a security signal.

### 3.3 Trace analysis at scale

At thousands of traces a minute, no one reads traces one by one:

- **Sampling:** keep every error and every slow or expensive trace (tail-based), plus a random sample of the rest.
- **Aggregation:** group by model version, prompt version, tool, tenant, and input type.
- **Failure-cohort analysis:** find what the failing traces share (a document format, a tool, a time window, a tenant) and quantify how much of the failure it explains. A systemic issue is invisible in any single trace and obvious in the cohort.

## Chapter 4: Advanced debugging and incident response

### 4.1 Complex failure diagnosis

Isolate where a failure originates: **model output**, the **agent harness** (your loop, hooks, state handling), a **tool**, or the **data** (retrieved content, inputs).

- **Multi-turn failures:** find the first turn where the trace diverges from a good run; the visible failure is often several turns later.
- **Multi-agent failures:** check each hand-off: did the worker fail, or did the supervisor misread its result?
- **Non-deterministic failures:** reproduce with several runs of the same input before concluding anything; a 1-in-20 failure needs 20+ runs to see.
- **Refusals** are a failure class of their own (`stop_reason: "refusal"`, with a category in `stop_details`): look for what in the input triggers them before changing anything else.
- **Retrieval-grounding failures:** see Chapter 2.4's stage diagnosis.
- **A server-tool loop that pauses** (`stop_reason: "pause_turn"`) isn't an error: send the response back as it is and the turn continues.

### 4.2 Incident response and learning loops

During an outage or quality regression:

1. **Triage:** scope (which models, tenants, features), severity, and the change that preceded it.
2. **Mitigate:** roll back the prompt or model version, switch to a fallback, disable the feature, or shed load. Restore service before root-causing.
3. **Communicate:** status to users and stakeholders, with honest scope.
4. **Learn:** a blameless postmortem whose outputs are concrete: **a regression eval case** for the failure, **monitoring coverage** that would have caught it sooner, and fixes to the process that let it ship.

An incident that doesn't become an eval case and a monitor is likely to recur unnoticed.

## Chapter 5: Evaluation engineering and quality assurance

### 5.1 Offline evaluation systems

- **Golden sets** drawn from real traffic, including rare and hard cases in known proportions.
- **Regression suites** run on every prompt, model, tool, or agent change.
- **Behavioral checks:** schema validity, the right tool called, citations present, refusals where expected.
- **Retrieval metrics:** retrieval precision and recall, and **groundedness** of answers.
- **CI/CD gates** with explicit **release criteria**: no slice may regress beyond a threshold, whatever the average does.
- **Suite validity over time:** **contamination** (test cases leaking into prompts or examples), **saturation** (everything scores 100%, so the suite no longer discriminates), and **coverage gaps** (new features and input types with no cases). Refresh and extend the suite as the product changes.

### 5.2 LLM-as-judge engineering

A judge is a measuring instrument; calibrate it before trusting it:

- **Agreement with human labels** on a sampled set, measured with an inter-rater reliability statistic such as Cohen's kappa, which corrects for chance agreement.
- **Rubric design:** specific criteria, an explicit scale, a required evidence sentence per score, and a grader that reasons before scoring.
- **Bias and position effects:** in pairwise comparisons, randomize or swap the order and keep only consistent verdicts; control for verbosity; prefer a judge from a different model than the one being graded.
- **Judge drift across versions:** re-calibrate when the judge model changes.
- **Gating authority** waits until agreement is acceptable. A gate driven by an uncalibrated judge passes everything or nothing for the wrong reasons.

### 5.3 Online quality measurement

Offline suites miss what real users do. Measure live: **sample production traffic** for grading, run **A/B tests** with a predefined metric and sample size, and wire **feedback loops** (thumbs, corrections, escalations) into the eval set. Match the metric to the task: field-level accuracy for extraction, rubric scores for generation, task success and steps for agents, groundedness for retrieval-grounded answers.

## Chapter 6: Cost and latency at scale

### 6.1 Cost architecture

- **Model costs and forecast them** from tokens per task times volume, split by route and tenant.
- **Routing and cascades:** a cheap model handles what it can and escalates the rest; route by task type, based on measurements. Before building a cascade, measure the simpler option: a more capable model at lower effort can match an older model at high effort.
- **Caching strategy:** stable content first, breakpoints by change cadence (up to 4 per request), and diagnostics through `cache_read_input_tokens` and hit rates. Cache writes cost 1.25x (5-minute) or 2x (1-hour) the input price; reads cost a tenth or less. Caches are scoped to a model, so a cascade across models gives up reuse between them.
- **Batch vs realtime:** the Message Batches API halves the price of everything nobody waits on.
- **Per-tenant budgets:** enforce spend caps per tenant or workspace in your gateway, and cap autonomous runs with a token or dollar budget.

### 6.2 Latency engineering

Distinguish **time to first token** (TTFT, what a user waiting on a chat feels) from **total latency** (what a pipeline waiting on the full result feels):

| Lever | Improves |
|-------|---------|
| Streaming | Perceived latency (TTFT for the user); total time unchanged |
| Cache checkpoints on long stable prefixes | TTFT and cost |
| Parallel tool execution | Total time of tool-heavy turns |
| Lower effort on routes that don't need deep reasoning | Total time and cost |
| A faster tier, or fast mode where offered | Output speed, at a quality or price trade-off |

Measure the latency profile before choosing: a slow TTFT on a long prompt points to caching; a slow total with many sequential tool calls points to parallelism.

## Chapter 7: Runtime guardrails and production security

### 7.1 Runtime guardrail systems

Layer controls by the agent's risk profile:

- **Input and output filtering**, and **PII redaction** before content reaches the model and the logs
- **Hook-based policy enforcement** (Claude Code and Agent SDK hooks) and **destructive-action prevention** enforced in code
- **Sandboxing** that gives the agent tool and web access without exposing production systems or credentials
- **Approval gates** for irreversible actions, with **deterministic enforcement**: the model can't talk its way past them
- **Refusal handling and safety fallbacks:** a refusal routes to a defined path instead of a retry loop
- **False-positive / false-negative tuning:** a filter that blocks legitimate work gets bypassed; measure both error types on real traffic and tune

In Claude Code, permission rules evaluate **deny, then ask, then allow**: an allow rule can't carve an exception out of a deny. Managed settings sit above project and user settings, and organizations can cap things like effort or allowed MCP servers centrally.

### 7.2 Threat defense and adversarial testing

The highest-risk combination for a tool-using agent is **private data access + untrusted input + an external communication channel**. With all three, injected instructions can turn the agent into an exfiltration path. Threats to know:

- **Prompt injection** through tickets, emails, web pages, documents, and tool results
- **Tool and memory poisoning:** a compromised tool description or a planted memory that steers later behavior
- **Data exfiltration paths:** email, web requests, links with data in the URL, file writes to shared places
- **Unsafe autonomy:** consequential actions with no gate, at machine speed

Defense in depth breaks the combination with **deterministic** controls: scope data access to the task (the ticket's own account), allowlist recipients and domains or require approval for external sends, keep untrusted content in tool results as data, and vet and pin MCP servers. A system prompt warning is not an enforceable boundary. **Red-team** exercises target the high-risk paths specifically and become regression tests. Frameworks the guide names: the **OWASP Top 10 for LLM Applications** and the **NIST AI Risk Management Framework** with its **Generative AI Profile**.

### 7.3 Identity, secrets, and audit

- **Agent identity:** each agent or service has its own identity and permissions, distinct from the users it acts for, so actions are attributable.
- **Workload identity federation** replaces long-lived static API keys: workloads exchange their platform identity for short-lived credentials, so there is no key to leak or rotate.
- **Secrets management:** remaining secrets live in a secret manager, never in prompts, code, or images.
- **Least-privilege tool permissions** per agent and per task.
- **Audit logging** of security-relevant actions: tool calls with side effects, approvals, permission changes, who acted on whose behalf.

## Chapter 8: Agent fleet operations for software delivery

### 8.1 Parallel coding agents

For large engineering tasks, fan out: decompose into independent units (per module, per service, per failing test), run **parallel agents on isolated git worktrees** so they don't trample each other's files, and plan the **merge and conflict strategy** up front (small, separable changes; a merge order; an integration agent or person resolving conflicts). Fleet telemetry surfaces fleet-level failure modes: many agents failing on the same flaky test, duplicated work on overlapping tasks, cost concentrated in a few runaway sessions.

### 8.2 Verification and AI code review

When generation outpaces human review, verification becomes the bottleneck:

1. Introduce AI code review in **shadow mode**: it comments, but nothing is blocked.
2. **Calibrate** it against human review on the same pull requests: what does it catch, what does it miss, how often is it wrong?
3. Only then let it **gate merges**, for the categories where it proved reliable.
4. Keep **human oversight** where it matters: a person owns and approves changes; AI review raises the floor, it doesn't replace accountability.

### 8.3 Unattended and event-driven runs

Agents run toward a goal, on a schedule, or in response to events (for example, **CI/CD incident first response**: an agent triages a failing pipeline and proposes a fix). Unattended runs need:

- **Explicit permissions:** a run that hangs until the CI timeout is usually waiting on a permission prompt nobody can answer. Set the permission mode (for example `dontAsk`, which denies anything not pre-approved) and the allowed tools explicitly.
- **Budgets:** a spend or token cap per run (`claude -p` accepts a maximum budget), so a loop can't run up a bill overnight.
- **Checkpointing** so long runs resume, **notification** when they finish or fail, and **escalation** to a person for anything outside their mandate.
- **Clean configuration:** scripted runs should load only the configuration the pipeline intends (`claude -p --bare` skips locally discovered hooks, plugins, MCP servers, and CLAUDE.md files).

### 8.4 Organization-wide coding agent configuration

- **Managed settings and policies** (deployed centrally; users can't override them): denied commands, permission defaults, effort caps, sandbox requirements, telemetry.
- **MCP allowlists:** only approved servers can be connected.
- **Telemetry** enforced for every developer, so the organization sees usage, cost, and errors.
- **Gateway routing** of model traffic for authentication, logging, and quotas.
- **Governance for sharing:** a quality and safety bar (review, tests, owners, versions) before a prompt, Skill, or MCP server is shared across teams, usually distributed as versioned plugins through an internal marketplace.

---

# Part II: Exam domain notes

## Domain 1: Advanced Agent Architecture and Orchestration (17%)

**Skills tested:** Multi-Agent Orchestration; Durable Execution and State Management; Architecture Selection at Scale; Context and Memory Architecture.

**Know:** supervisor/worker, parallel dispatch, isolation, and approval flows and how each fails; persistence, checkpointing, idempotent resumption, memory, and surviving model changes; evidence for evolving workflow vs agent; the six context and memory techniques.

**Be able to:** find the failing hand-off in a multi-agent trace; make a long-running agent restartable; decide from production data whether to change patterns; pick a context policy for an agent near its limits.

**Anti-patterns:** raw worker output flooding the supervisor; restarts that redo side effects; a bigger window for a context problem; editing the cached system prompt mid-session.

## Domain 2: Production Integration, Reliability, and Knowledge Grounding (20%)

**Skills tested:** Reliability Engineering for Claude Services; Scale and Throughput Management; Production MCP and Change Management; Retrieval and Knowledge Grounding at Scale.

**Know:** the failure-class table; circuit breakers, degradation, fallbacks with feature parity; RPM, ITPM, OTPM and how caching affects them; queueing, backpressure, batches, workspaces; remote MCP auth, schema versioning, gateways, progressive rollout; agentic search vs RAG, hybrid search and re-ranking, citations and uncertainty, stage-by-stage diagnosis.

**Be able to:** split one retry path into per-class handling; name the binding throughput constraint; roll out a prompt or model change safely; locate a grounding failure by stage.

**Anti-patterns:** retrying refusals and truncations; fallbacks never tested with real requests; unversioned tool schemas; more retrieved chunks for a precision problem.

## Domain 3: Observability and Production Monitoring (12%)

**Skills tested:** Telemetry and Instrumentation; Production Monitoring and Alerting; Trace Analysis at Scale.

**Know:** traces with spans per model and tool call; usage fields and cache hit rate; structured events with request IDs; privacy-aware content capture; LLM-specific SLIs; burn-rate alerting; drift signals after model updates; tail-based sampling and failure cohorts.

**Be able to:** instrument an agent loop end to end within privacy limits; define SLIs and SLOs; detect a behavioral regression that produces no errors; quantify a systemic issue from trace cohorts.

**Anti-patterns:** logging full content by default; uptime-only monitoring; reading individual traces to find systemic issues.

## Domain 4: Advanced Debugging and Incident Response (10%)

**Skills tested:** Complex Failure Diagnosis; Incident Response and Learning Loops.

**Know:** the four origins (model output, harness, tools, data); multi-turn, multi-agent, and non-deterministic diagnosis; refusal and pause_turn handling; triage, mitigation, rollback, communication; postmortems that produce eval cases and monitors.

**Be able to:** isolate a failure's origin from a trace; reproduce a rare failure; restore service before root-causing; turn an incident into regression coverage.

**Anti-patterns:** concluding from one run; treating pause_turn as an error; fixing forward during an outage when a rollback exists; postmortems with no eval or monitor.

## Domain 5: Evaluation Engineering and Quality Assurance (12%)

**Skills tested:** Evaluation System Design; LLM-as-Judge Engineering; Online Quality Measurement.

**Know:** golden sets, regression suites, behavioral checks, retrieval metrics, CI gates and release criteria; contamination, saturation, and coverage gaps; judge calibration, inter-rater reliability, position and verbosity bias, judge drift; live sampling, A/B tests, feedback loops, metrics by task type.

**Be able to:** design a release gate for prompt, model, and agent changes; keep a suite valid over time; calibrate a judge and withhold gating until it agrees with people; measure quality on live traffic.

**Anti-patterns:** gating on an uncalibrated judge; a saturated suite that always passes; averages that hide a failing slice.

## Domain 6: Cost and Latency Optimization at Scale (8%)

**Skills tested:** Cost Architecture at Scale; Latency Engineering.

**Know:** cost modeling and forecasting; routing and cascades; caching strategy, prices, and diagnostics; batch economics; per-tenant budgets; TTFT vs total latency; streaming, parallel tools, cache checkpoints, effort.

**Be able to:** find where spend concentrates and pick the lever; enforce tenant budgets; pick the latency lever that matches the profile.

**Anti-patterns:** a cascade before measuring a single model at lower effort; streaming to fix a pipeline's total latency; unlimited budgets on autonomous runs.

## Domain 7: Runtime Guardrails and Production Security (11%)

**Skills tested:** Runtime Guardrail Systems; Threat Defense and Adversarial Testing for Agentic Systems; Identity, Secrets, and Audit at Scale.

**Know:** the guardrail layers; deny-ask-allow and managed settings; the high-risk combination of private data, untrusted input, and external communication; injection, poisoning, exfiltration, unsafe autonomy; red-teaming; OWASP Top 10 for LLM Applications and NIST AI RMF; agent identity, workload identity federation, audit logging.

**Be able to:** close an exfiltration path with a deterministic control; tune a filter's false positives and negatives; design a red-team exercise; replace static keys with federated identity.

**Anti-patterns:** prompt warnings as security boundaries; detection (logging) where prevention is needed; shared static keys; allow rules to escape a deny.

## Domain 8: Agent Fleet Operations for Software Delivery (10%)

**Skills tested:** Parallel Agent Orchestration for Engineering Work; Verification and AI Code Review Operations; Unattended and Event-Driven Agent Operations; Organization-Wide Coding Agent Configuration.

**Know:** worktree isolation and merge strategy; fleet telemetry; shadow mode, calibration, then gating for AI review; permission modes, budgets, checkpoints, notification, and escalation for unattended runs; managed settings, MCP allowlists, telemetry, gateways, and sharing governance.

**Be able to:** fan out a large change safely; introduce AI review without losing human ownership; make a CI agent run unattended without hanging or overspending; set organization-wide policy.

**Anti-patterns:** parallel agents in one working tree; AI review gating merges before calibration; unattended runs waiting on prompts; sharing unreviewed Skills and MCP servers.

---

# Part III: Exam preparation

## The preparation ladder

Five layers, in order. Anthropic's practice exam was retired when the exams moved to Pearson VUE; the three sample questions in the official exam guide are what remains.

| Step | Resource | Cost |
|------|----------|------|
| 1. Learn the vocabulary | The official exam guide and the free Developer - Professional prep courses on the Anthropic Academy; the CCDV-F guide as assumed knowledge | Free |
| 2. Go to the source | [The Claude Developer Platform docs](https://platform.claude.com/docs) (errors, rate limits, caching, context management, observability, security) and [the Claude Code docs](https://code.claude.com/docs) (settings, permissions, hooks, plugins, headless) | Free |
| 3. First calibration | [30 practice questions with explanations](./practice-questions.md) in this repo | Free |
| 4. Full calibration | [Full-length timed practice exams and a 500-card flashcard deck](https://preporato.com/certificates/claude-certified-developer-professional) on Preporato, written to the guide's domains and skills; the page has free sample questions to try first | Paid |
| 5. Operate something | Run one tool-using agent with tracing, cost telemetry, SLOs, a gating eval suite, layered guardrails, and a postmortem practice, as the official guide recommends | Free |

## The ten trap answers

| Trap | Why it fails |
|------|-------------|
| Retry-everything | Refusals, truncations, and 400s need their own paths; retries multiply their cost |
| Bigger-window | A larger context window moves the cliff; manage what fills it |
| Prompt-as-boundary | A system prompt warning can't stop exfiltration; deterministic controls can |
| Detect-instead-of-prevent | Logging and alerts don't stop an irreversible action |
| Uncalibrated-gate | A judge that disagrees with people can't gate releases |
| One-run-conclusion | Non-deterministic failures need repeated runs |
| Fix-forward-in-an-incident | Restore service first; rollback before root cause |
| Untested-fallback | A fallback that lacks a feature the request uses fails when you need it |
| Unattended-without-limits | No permission mode, budget, or escalation means hangs and runaway cost |
| Allow-overrides-deny | Deny wins; managed settings sit above project and user settings |

On multi-select items, test each option on its own: one trap among your picks costs the question.

## Exam-day strategy

70 questions in 120 minutes is about 1.7 minutes each, and ten are unscored items you can't spot. Most stems hand you evidence: read it first and name what it shows (a mixed failure class, a position bias, a missing control, a binding constraint) before reading the options. Prefer the option that addresses the cause the evidence shows over options that help in general. Read how many responses the item asks for, flag anything over three minutes, and change an answer only when you find a definite error.

## Worked questions

Twelve fresh questions in the exam's style. (Written for this guide; timed full-length practice is linked in Resources.)

**Q1.** A document-processing service sends each request through one retry wrapper: any non-success is retried up to five times with backoff. After a prompt change, cost jumps 40% with no gain in completed documents. Logs show most retries follow `stop_reason: "max_tokens"`. What should change?

- A) Raise the retry limit from five to ten so that more of the long documents eventually get through
- B) Remove every retry from the wrapper so the duplicated spending stops at once
- C) Give length stops their own path (a bigger output budget or a split input); keep backoff for 429 and 5xx
- D) Move the service to a smaller, cheaper model so that each of the retries costs less than it does today

**Answer: C.** A length stop reproduces on retry, so each retry pays again for the same truncation; it needs a budget or input change. Option A multiplies the waste, B loses the retries that do help on transient errors, and D changes quality to make a broken loop cheaper.

**Q2.** A multi-tenant assistant's 429 rate-limit errors cluster during one large customer's nightly sync, and other tenants' interactive requests fail at the same time. Which design fixes the cause?

- A) Move the nightly sync to the Message Batches API and give each tenant its own quota and queue
- B) Raise the retry count in every client so interactive requests outlast the nightly spike
- C) Ask the large customer to schedule its sync for a quieter hour of the night
- D) Upgrade every tenant to a faster model so that requests finish before the per-minute limits are reached

**Answer: A.** Bulk work nobody waits on belongs in batches, and per-tenant isolation stops one tenant's spike from exhausting shared limits. Option B adds load during the spike, C moves the problem without preventing the next one, and D doesn't change rate limits.

**Q3.** A research agent runs for hours across hundreds of tool calls. Late in each run it repeats searches it already did and costs climb sharply. The context is mostly old search results. Which policy fits?

- A) Move the agent to a model with a larger context window so old results stay visible
- B) Restart the agent from scratch every hour so each run begins with an empty context
- C) Raise the effort level so the model reasons harder about which searches it already ran
- D) Clear old tool results with context editing, and keep findings in persistent memory

**Answer: D.** Old tool results are dead weight, and findings belong in durable memory rather than in a transcript that is about to be trimmed. Option A moves the cliff, B throws away progress, and C can't recover context that was never managed.

**Q4.** After a model version update, error rates and latency are unchanged, but average response length drops 30% and the share of answers citing a source falls from 92% to 71%. Nobody was alerted. What monitoring was missing?

- A) Uptime checks on the API endpoint from several regions, alerting the on-call engineer within a minute
- B) Behavioral drift signals such as length, citation rate, and sampled quality, by model version
- C) Error logging at a more detailed level, with the full request body on each failure
- D) A daily cost report per feature, sent to the team that owns the assistant

**Answer: B.** The regression produced no errors, so only behavioral and quality indicators could catch it, compared before and after the version change. Options A and C watch errors that never happened, and D doesn't measure quality.

**Q5.** A failure affects about 3% of support conversations: the agent applies the wrong refund policy. No single trace explains it. What is the most efficient next step?

- A) Read the failing traces one at a time until a pattern becomes clear to the team
- B) Raise the logging level on every request so the next failures carry more detail
- C) Group failing traces by region, document version, tool path, and model, against passing ones
- D) Roll back the most recent prompt change right away, since it is the likeliest cause of the failures

**Answer: C.** A systemic issue at 3% shows up in the cohort and in no single trace. Option A doesn't scale, B adds volume without analysis, and D acts on a guess the data could confirm or rule out.

**Q6.** A quality regression hits a customer-facing assistant 20 minutes after a prompt release. Traces suggest the new prompt causes it, but the exact cause isn't clear. What comes first?

- A) Roll back to the previous prompt version, confirm recovery, and tell users what happened
- B) Debug the new prompt directly in production until the exact cause of the regression has been found
- C) Wait for a full day of traffic so the regression can be measured with confidence
- D) Switch every request to the fallback model until the team has finished its review

**Answer: A.** Restore service first when a rollback exists; then root-cause it and add the failure as a regression eval case. Option B extends the outage, C leaves users on a known-bad version, and D changes a variable that isn't implicated.

**Q7.** A team's eval suite has passed every release for four months with scores of 99-100%. Users report new failure types on recently launched features. What is wrong with the suite?

- A) Nothing is wrong: four months of near-perfect scores show that quality is high
- B) The pass threshold is set too high, so small regressions are hidden by rounding
- C) The judge model is too capable, so it grades the outputs more generously than human reviewers do
- D) It is saturated and lacks cases for the new features, so it no longer measures quality

**Answer: D.** A suite that always passes and lacks cases for new features measures the past; refresh it with harder cases and cases drawn from new traffic. Option A trusts a broken instrument, B misreads what the threshold does, and C blames the grader when the cases are the problem.

**Q8. (Select TWO)** A chat product's users wait 9 seconds before seeing any text, while a downstream pipeline built on the same model must cut its total processing time. Which two changes address each need correctly?

- A) Stream responses in the pipeline as well, so that it finishes each document sooner
- B) Stream responses in the chat product so users see text sooner
- C) Raise effort in the chat product so that its answers are worth the wait
- D) Run the pipeline's independent tool calls in parallel instead of one by one
- E) Move the chat product onto the Message Batches API to lower its cost

**Answer: B and D.** Streaming fixes perceived latency (time to first token) for waiting users; parallel tool execution cuts total time for pipelines. Option A confuses time to first token with total time, C slows the chat further, and E puts a waiting user on an asynchronous lane.

**Q9.** An internal agent reads incoming vendor emails, can query the finance database, and can send email. Which control most directly prevents an injected email from making it send invoices to an attacker?

- A) A system prompt rule telling the agent never to follow any instructions that it finds inside emails
- B) A log of every email the agent sends, reviewed by the finance team each morning
- C) A recipient allowlist or approval on the email tool, and database access scoped to this vendor
- D) A lower effort level, so the agent is less likely to carry out multi-step embedded instructions

**Answer: C.** The agent combines private data, untrusted input, and external communication; deterministic limits on the send channel and the data scope break that combination. Option A isn't enforceable, B detects after the damage, and D doesn't remove the capability.

**Q10.** A company's CI agents authenticate to the Claude API with one static API key stored in the pipeline's secrets, shared by every repository. Which change most improves identity and audit?

- A) Rotate the shared key every week and announce each new key to the repository owners
- B) Use workload identity federation, so each pipeline gets short-lived credentials of its own
- C) Commit the key to each repository in encrypted form, so that every team holds a copy of its own
- D) Issue each developer a personal key and have the CI jobs run with the committer's key

**Answer: B.** Federated identity removes the static secret and makes each workload's actions attributable in audit logs. Option A shortens the exposure window but keeps one shared identity, C still distributes a secret, and D ties automated jobs to individuals.

**Q11.** A platform team wants AI code review on every pull request, because human reviewers can't keep up with agent-written changes. What is the right rollout?

- A) Let AI review block merges from the first day, since agents write most of the changes
- B) Replace human review entirely, because the code under review was written by AI anyway
- C) Run AI review only on pull requests written by people, and merge agent changes after tests pass
- D) Start in shadow mode, compare with human reviews, then gate only where it proved reliable

**Answer: D.** AI review earns gating authority through calibration against human review on the same pull requests, and a person still owns approval. Option A gates before anyone knows its error rate, B removes ownership, and C skips the changes that most need verification.

**Q12.** A nightly unattended Claude Code job in CI sometimes runs until the 6-hour pipeline timeout without finishing, and once ran up an unexpected bill. Which configuration addresses both problems?

- A) An explicit permission mode and tool list, a spend budget, and a notification when it ends
- B) A longer pipeline timeout, so that the job has the time it needs to finish its work
- C) The `bypassPermissions` mode on the CI runner, so no tool call ever waits for approval
- D) A developer on call who watches the job each night and stops it by hand when it runs long

**Answer: A.** Hangs in unattended runs usually come from permission prompts nobody answers, and a budget caps runaway cost. Option B just makes the hang longer, C removes every safety check on a machine with access to the code, and D defeats the point of an unattended run.

## 6-week study plan

- **Week 1: baseline.** Read the official exam guide and the free Developer - Professional prep courses. Re-read the [CCDV-F guide](../ccdv-f/guide.md) as assumed knowledge and map yourself against the 25 skills.
- **Weeks 2-3: reliability, observability, and evaluation.** Build per-class error handling and fallbacks for an agent you run; add traces, usage metrics, and cache hit rate; define three SLIs with SLOs; build a regression suite and calibrate an LLM judge against human labels.
- **Week 4: security and cost.** Red-team your agent against the private data + untrusted input + external communication combination and close what you find with deterministic controls; model its cost per task and test caching, routing, and effort changes.
- **Week 5: fleets.** Run parallel Claude Code agents on worktrees, configure an unattended CI job with a permission mode and a budget, and write managed settings for a hypothetical organization.
- **Week 6: calibrate.** Start with the [30 practice questions](./practice-questions.md) in this repo, then take [full-length timed practice exams](https://preporato.com/certificates/claude-certified-developer-professional) and review every miss by domain. The night before: Part III here and the [cheat sheet](https://preporato.com/blog/claude-developer-professional-cheat-sheet-2026).

Expanded version: [6-week Developer - Professional study plan](https://preporato.com/blog/claude-developer-professional-study-plan-2026).

## Pre-exam checklist

- [ ] I can find the failing hand-off in a multi-agent trace and design hand-off contracts
- [ ] I can make a long-running agent checkpoint and resume without repeating side effects
- [ ] I can use production data to decide between workflow and agent patterns
- [ ] I can choose context editing, compaction, memory, mid-conversation system messages, tool search, or programmatic tool calling
- [ ] I handle 429, 5xx, 400, refusal, max_tokens, and context stops on separate paths
- [ ] I can add circuit breakers, degradation, and fallbacks that respect feature parity
- [ ] I can name the binding throughput constraint and use batches, queues, quotas, and workspaces
- [ ] I can roll out prompt, model, and MCP changes progressively with rollback
- [ ] I can choose agentic search or RAG and diagnose a grounding failure by stage
- [ ] I can instrument an agent loop with traces, usage metrics, and cache hit rate within privacy limits
- [ ] I can define LLM-specific SLIs and SLOs and detect drift after a model update
- [ ] I can find a systemic issue through sampling and failure cohorts
- [ ] I can isolate a failure to model output, harness, tool, or data, and reproduce non-deterministic failures
- [ ] I restore service before root-causing and turn incidents into eval cases and monitors
- [ ] I can design release gates and keep a suite free of contamination, saturation, and coverage gaps
- [ ] I can calibrate a judge, measure inter-rater reliability, and control position bias
- [ ] I can measure quality on live traffic with the metric that fits the task
- [ ] I can model fleet cost and choose routing, caching, batching, effort, and tenant budgets
- [ ] I can tell time to first token from total latency and pick the matching lever
- [ ] I can layer guardrails and tune their false positives and negatives
- [ ] I can break the private data + untrusted input + external communication combination deterministically
- [ ] I can replace static keys with workload identity federation and audit agent actions
- [ ] I can run parallel coding agents on worktrees with a merge strategy
- [ ] I can introduce AI code review through shadow mode and calibration
- [ ] I can configure unattended runs with permissions, budgets, checkpoints, and escalation
- [ ] I can set organization-wide managed settings, MCP allowlists, telemetry, and sharing governance
- [ ] I have the ten traps down cold and apply them per option on multi-select items
- [ ] I have taken at least two full-length timed practice exams and reviewed every miss

## Resources

**Official (free):**
- [Claude Certified Developer - Professional](https://anthropic-partners.skilljar.com/claude-certified-developer-professional-certification) on the Anthropic Partner Academy: the exam guide, the free prep courses, and registration
- [Claude Developer Platform docs](https://platform.claude.com/docs) and [Claude Code docs](https://code.claude.com/docs)
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) and the [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), both named in the official guide

**Free articles (preporato.com):**
- [Exam guide explained](https://preporato.com/blog/claude-certified-developer-professional-exam-guide-2026) · [Exam domains](https://preporato.com/blog/claude-certified-developer-professional-exam-domains-2026) · [Cheat sheet](https://preporato.com/blog/claude-developer-professional-cheat-sheet-2026) · [20 practice questions](https://preporato.com/blog/claude-developer-professional-practice-questions-2026) · [6-week study plan](https://preporato.com/blog/claude-developer-professional-study-plan-2026) · [CCDV-F vs CCDV-P](https://preporato.com/blog/ccdv-f-vs-claude-certified-developer-professional-2026) · [Developer vs Architect - Professional](https://preporato.com/blog/claude-developer-professional-vs-architect-professional-2026)

**Practice:**
- [30 practice questions with explanations](./practice-questions.md) in this repo (free)
- [The CCDV-P page on Preporato](https://preporato.com/certificates/claude-certified-developer-professional): free sample questions, then (paid) full-length timed practice exams and a 500-card flashcard deck

---

*Not affiliated with Anthropic. Exam details reflect the program as of November 2026; the Partner Academy is authoritative. Found an error? [Open an issue](https://github.com/preporato/claude-certification-guide/issues).*
