# Claude Certified Architect - Professional (CCAR-P): The Complete Study Guide

A full preparation guide for Anthropic's Professional-tier architect exam. Part I teaches the material by topic. Part II re-indexes it by exam domain and the official skills for revision. Part III covers trap answers, worked questions, and a final checklist.

Maintained by [preporato.com](https://preporato.com). Facts checked in November 2026 against the official exam guide (version 1.1, effective December 7, 2026), Anthropic's program pages, and the current Claude API and Claude Code documentation.

> **Which version this guide covers.** CCAR-P changes on December 7, 2026: 70 questions instead of 63, new domain weights, and rewritten skills in every domain. The seven domains keep their names. This guide follows the new blueprint. Testing on or before December 6? Read [Taking CCAR-P before December 7](#taking-ccar-p-before-december-7) first.

---

## Contents

- [Introduction](#introduction)
- [Exam format](#exam-format)
- [Taking CCAR-P before December 7](#taking-ccar-p-before-december-7)
- **Part I: The material**
  - [Chapter 1: Architecture patterns and solution design](#chapter-1-architecture-patterns-and-solution-design)
  - [Chapter 2: Models, prompting, and context engineering](#chapter-2-models-prompting-and-context-engineering)
  - [Chapter 3: Integration mechanisms](#chapter-3-integration-mechanisms)
  - [Chapter 4: Retrieval architecture and quality](#chapter-4-retrieval-architecture-and-quality)
  - [Chapter 5: Evaluation, testing, and optimization](#chapter-5-evaluation-testing-and-optimization)
  - [Chapter 6: Governance, safety, and compliance](#chapter-6-governance-safety-and-compliance)
  - [Chapter 7: Stakeholders and the solution lifecycle](#chapter-7-stakeholders-and-the-solution-lifecycle)
  - [Chapter 8: Team enablement](#chapter-8-team-enablement)
- **Part II: Exam domain notes**
  - [All seven domains](#part-ii-exam-domain-notes)
- **Part III: Exam preparation**
  - [The preparation ladder](#the-preparation-ladder)
  - [The twelve trap answers](#the-twelve-trap-answers)
  - [Exam-day strategy](#exam-day-strategy)
  - [Worked questions](#worked-questions)
  - [6-week study plan](#6-week-study-plan)
  - [Pre-exam checklist](#pre-exam-checklist)
  - [Resources](#resources)

---

## Introduction

CCAR-P (Claude Certified Architect - Professional) is the top of the architect track. It certifies the person accountable for a Claude solution across its whole life: turning a vague business request into an architecture, choosing where it runs and how it connects, designing evaluation and governance in from day one, committing only to what a probabilistic system can deliver, and enabling the teams who build and operate the result.

The exam reads like an enterprise engagement. Where the Foundations tier ([CCA-F](../cca-f/)) asks whether you can build a system correctly, the Professional tier asks whether you can own the solution. Most items name a binding constraint (a residency obligation, a latency ceiling, an audit requirement, a budget) and ask which option satisfies it and what trade-off it costs. Wrong options are usually true in some other context; the skill is noticing which constraint decides. Its sibling [CCDV-P](../ccdv-p/) is the Professional exam for engineers who operate Claude systems in production.

**Who should take it:** solution architects with 3+ years of systems architecture or platform engineering experience and 6+ months delivering production Claude or LLM solutions. There are no formal prerequisites; CCA-F first is recommended for the vocabulary but never required, and Foundations does not convert into Professional.

## Exam format

| | |
|---|---|
| Questions | 70: 60 scored and 10 unscored trial items you cannot tell apart |
| Duration | 120 minutes to answer, about 135 minutes of seat time |
| Question style | Scenario-based; each item states how many responses to select. **No partial credit**: every selected option must be defensible |
| Passing score | 720 on a 100-1000 scaled score, with per-domain percent correct on the report |
| Delivery | Pearson VUE, online proctored (OnVUE) or at a test center |
| Price | $175 per attempt |
| Registration | Anthropic Partner Academy, open to people who work at Claude Partner Network organizations (sign in with a company email); you pay at Pearson's checkout |
| Languages | English or Japanese, chosen when you schedule |
| Rescheduling | Free up to 1 hour before an OnVUE appointment, 48 hours before a test center one |
| Retakes | Full fee for every attempt; waits of 14, 30 and 90 days after the first, second and third failed attempts; at most 4 attempts in any 12 months |
| Validity | 12 months; free non-proctored renewal before expiration, full proctored exam after a lapse |

### Exam domains

| Domain | Weight | ~Scored questions | Core focus |
|--------|--------|-------------------|------------|
| 1. Solution Design and Architecture | 18% | ~11 | Delegation, pattern selection, decomposition, value, deployment surface and runtime |
| 2. Claude Models, Prompting, and Context Engineering | 13% | ~8 | Tiers, prompt diagnosis, techniques, token economics, caching, effort and context lifecycle |
| 3. Integration | 21% | ~13 | Least privilege, auth, binding constraints, monitoring, retrieval, connection mechanisms, reliability |
| 4. Evaluation, Testing, and Optimization | 17% | ~10 | Coverage gaps, business-derived evals, judge bias, experiments, root cause, cost, migration |
| 5. Governance, Safety, and Risk Management | 16% | ~10 | Guardrail placement, injection surface, risk ranking, HITL gates, compliance controls, bias |
| 6. Stakeholder Communication and Lifecycle Management | 7% | ~4 | Unsupportable commitments, ADRs, handoff completeness |
| 7. Developer Productivity and Operational Enablement | 8% | ~5 | Packaging workflows, Agent SDK and Claude Code configuration, accountability for AI code |

## Taking CCAR-P before December 7

Exams through December 6, 2026 follow the earlier guide: **63 questions, all scored**, in 120 minutes, across the same seven domains with different weights.

| Domain | Until December 6 | From December 7 |
|---|---|---|
| Solution Design and Architecture | 17% | 18% |
| Claude Models, Prompting, and Context Engineering | 13% | 13% |
| Integration | 19% | 21% |
| Evaluation, Testing, and Optimization | 16% | 17% |
| Governance, Safety, and Risk Management | 14% | 16% |
| Stakeholder Communication and Lifecycle Management | 14% | 7% |
| Developer Productivity and Operational Enablement | 7% | 8% |

On the earlier exam, give stakeholder work twice the time this guide's weighting suggests: discovery outputs, the lifecycle phases, SLAs with error budgets, and ADRs (all in Chapter 7). The newer skills in this guide (deployment surfaces and runtimes, idempotency, experimental design, model migration, plugin packaging) appear rarely or not at all on the earlier version.

---

# Part I: The material

## Chapter 1: Architecture patterns and solution design

### 1.1 Delegating between Claude and people

Before any pattern, decide who does what. Assign each step of the business process to **Claude**, to **a person**, or to **both together** (Claude drafts, a person decides), and justify each assignment against three criteria:

- **Reversibility:** can a mistake be undone cheaply?
- **Stakes:** what does a mistake cost, and to whom?
- **Accountability:** must a named person answer for the outcome (a regulator, a contract, an employment decision)?

Reversible, low-stakes steps go to Claude; irreversible or accountable steps stay with people or get a gate (Chapter 6.4). The answer the exam rewards is almost never "Claude does all of it" or "Claude does none of it".

### 1.2 The architecture patterns

| Pattern | What it is | Pick it when |
|---------|-----------|--------------|
| Augmented LLM | A single model call enriched with retrieval, tools, or memory | One well-scoped call solves the task; lowest cost and latency |
| Workflow | Several model calls in a fixed, developer-defined sequence | Steps are known in advance and predictability or auditability matters |
| Agentic | The model runs an open-ended loop, choosing its own tools and steps | The path can't be enumerated up front; exploration is required |
| Skills-based | Packaged procedures (Skills) the model loads when a task matches, on top of one of the above | The same know-how must be reused across teams and surfaces, governed and versioned in one place |

The governing principle: **start with the simplest pattern that meets the requirement.** When an augmented call satisfies the scenario, both workflow and agentic answers are wrong. A predictability or audit requirement points to a workflow; open-ended discovery points to an agent, accepting its cost and latency variance. A reuse-and-governance requirement points to Skills. The pattern you choose also draws the **delegation boundary**: a workflow keeps sequencing decisions with your code; an agent hands them to the model.

A complete architecture has four parts: **input, processing, output, and a feedback loop** (evals, user signals, monitoring feeding back into design). **End-to-end evaluation** questions ask which component fails first under a stated load or trust condition: the single shared retrieval index under 10x traffic, the tool with write access when inputs become untrusted, the session store when sessions get long. Find the weakest link against the stated requirement (scalability, maintainability, access control), not the most impressive component.

### 1.3 Orchestrator and subagent decomposition

- Go multi-agent only when decomposition is real: independent subtasks that can run in parallel justify an orchestrator with workers. A narrow single-domain task belongs to one agent.
- Decompose **by capability** (research, analysis, writing) or **by data domain** (per region, per product line).
- Sequential hand-off when outputs chain; parallel fan-out when subtasks are independent, merged in a synthesis step.
- Judge a proposed decomposition against **observability and error recovery**: can you see which subagent failed, and can one subtask be retried without rerunning the rest? Decompositions fail at **task boundaries** (overlapping or missing responsibilities), **control flow** (no owner for retries or timeouts), and **result synthesis** (the orchestrator merges conflicting reports without a rule).

### 1.4 Value-based decisions

Anchor every architecture answer to the value the scenario names: **efficiency** (throughput, automation rate), **transformation** (new capability the business didn't have), **productivity** (time saved per person), **solution cost** (per-transaction spend), and **performance SLAs** (latency, availability, accuracy floors). When two answers are technically valid, the one that maximizes the stated outcome under the stated cost or SLA ceiling wins. When competing feature proposals arrive, rank them by measurable business value, not by technical interest.

### 1.5 Deployment surface and agent runtime

Where the model runs is an architecture decision with consequences.

| Surface | Strengths | Trade-offs to accept |
|---------|----------|---------------------|
| Anthropic API (first party) | New models and features first | Data is processed outside your cloud account |
| Amazon Bedrock, Google Vertex AI, Microsoft Foundry | Inside your existing cloud boundary, billing, IAM, and compliance attestations | Features can arrive later or not at all; some runtimes aren't offered there |

| Agent runtime | Who owns the loop and session state | Fits |
|---------------|-------------------------------------|------|
| Messages API loop (your code) | You | Full control, any surface |
| Self-hosted Agent SDK or headless Claude Code | You, on your infrastructure | A capable agent harness inside your boundary |
| Claude Managed Agents | Anthropic hosts the loop and a per-session sandbox | Speed, no session state to own; available on Anthropic's platform rather than every cloud surface |

Rules the exam leans on:

- **A residency obligation is binding.** If model inputs must stay inside a cloud boundary, the cloud surface wins, and you accept its feature lag and own the agent runtime and session state yourself.
- **Zero data retention (ZDR) governs how long data is kept, not where it is processed.** It never satisfies a residency obligation on its own.
- **Surface choice constrains runtime choice.** An answer claiming every requirement is met with no trade-off is usually wrong.

## Chapter 2: Models, prompting, and context engineering

### 2.1 Model tiers

| Tier | Optimizes for | Pick it when |
|------|--------------|--------------|
| Opus class | Hardest reasoning, long-horizon agentic work | Failure is expensive and volume is low |
| Sonnet class | Capability, cost, and latency in balance | The production default for most enterprise workloads |
| Haiku class | Lowest cost and latency | High-volume, well-bounded tasks: classification, routing, extraction |

Choose the tier that satisfies **every** binding constraint (latency, cost, quality), and be ready to say why each rejected tier fails: too slow for the SLA, too expensive at the volume, below the quality floor. Default to balanced and move on evidence; at scale, **routing beats a single model**:

```python
def answer(query: str) -> str:
    triage = client.messages.create(
        model="claude-haiku-5-5", max_tokens=16,
        output_config={"effort": "low"},
        messages=[{"role": "user", "content": f"Reply SIMPLE or COMPLEX only:\n{query}"}],
    )
    label = next(b.text for b in triage.content if b.type == "text").strip()

    model = "claude-haiku-5-5" if label == "SIMPLE" else "claude-sonnet-5-5"
    response = client.messages.create(model=model, max_tokens=4000,
                                      messages=[{"role": "user", "content": query}])
    return next(b.text for b in response.content if b.type == "text")
```

### 2.2 Diagnosing and revising a system prompt

Degraded or inconsistent output usually traces to **underspecification**: the prompt never said what is in scope, what format to use, or what to do in the hard case. A good system prompt orders role, explicit **testable** criteria, boundary statements, and the output format. Revise toward precision, but don't **over-constrain**: rules so rigid that legitimate variation (a different but valid structure, a needed clarifying question) gets suppressed are a failure too. "Flag SQL injection and authentication bypass" is testable; "be careful" is not.

### 2.3 Choosing a prompting technique

| Technique | Use it for | Cost |
|-----------|-----------|------|
| Zero-shot | Simple, unambiguous tasks | Lowest |
| Few-shot (2-4 examples) | Teaching format and edge-case judgment; include a correct rejection | More input tokens |
| Prompted reasoning ("think step by step") | Visible reasoning on models without native thinking, or when you need the reasoning in the output | Output tokens |
| Native (adaptive) thinking with effort | Multi-step problems on current models; the model decides how much to think, effort sets the ceiling | Thinking tokens; tune effort per route |
| Structured output | Output another system parses | Schema design up front |

Pick the technique that addresses the **observed failure** at the lowest token cost: a format failure wants structured output, not more reasoning; a reasoning failure wants thinking, not more examples.

### 2.4 Token economics and caching

Analyze what fills the context against the token budget and the call volume: repeated system prompts, tool definitions loaded on every call, documents resent each turn, bloated tool outputs. Reduce what doesn't carry task-relevant information, and cache what must be resent.

Prompt caching stores the processed form of a stable prefix so repeated calls skip reprocessing it. Cache reads bill at a tenth of the base input rate or less, depending on the model; writes cost 1.25x for the default 5-minute cache and 2x for the 1-hour cache.

- **It is a prefix match.** Any byte change invalidates everything after it. The render order is tools, then system, then messages.
- **Breakpoints by change cadence.** One after content that never changes (tools, policies), another after content that changes a few times a day (a per-customer document), and the per-request content last. A breakpoint placed after the per-request question makes every prefix unique.
- **Rolling breakpoints** move with a growing conversation so each turn reads the history from cache.
- **Modular or Skill-based packaging** keeps reusable instructions in stable, versioned units instead of copy-pasted variants that differ by a word and never share a cache entry.
- **The classic breakers:** a timestamp or user ID early in the prefix, tool definitions reordered between calls, shuffled document order.
- **It doesn't pay off** for infrequent calls (the entry expires first) or prefixes below the minimum cacheable length.

```python
system=[
    {"type": "text", "text": POLICIES + OUTPUT_FORMAT,      # never changes
     "cache_control": {"type": "ephemeral"}},                # breakpoint 1: tools + policies
    {"type": "text", "text": customer_contract,             # changes per customer
     "cache_control": {"type": "ephemeral"}},                # breakpoint 2
],
messages=[{"role": "user", "content": per_request}]          # volatile, after both breakpoints
```

### 2.5 Reasoning effort and the context lifecycle

For long-running agents, allocate reasoning where it pays: higher effort for planning and hard judgment steps, lower effort for routine subagents and high-volume turns. Then choose how context survives a long session:

| Technique | What it does | Fits |
|-----------|-------------|------|
| Context editing | Clears old tool results (or thinking) from the history | Tool-heavy loops where old results are dead weight |
| Memory tool | The agent writes durable notes to a store it reads later | Knowledge that must outlive one session |
| Compaction | Summarizes earlier history into a shorter form | Long conversations where the thread of decisions matters |

Attention also concentrates at the edges of the window: critical instructions and key facts go at the beginning or end.

## Chapter 3: Integration mechanisms

The heaviest domain (21%). Expect a dozen questions.

### 3.1 Choosing the connection mechanism

| Mechanism | What it is | Pick it when |
|-----------|-----------|--------------|
| MCP | Open protocol exposing tools, resources, and prompts to any compliant client | One capability must be reused across many clients and surfaces |
| Direct API / CLI | A direct integration with the service | One application, low latency, full control, no reuse need |
| Agent-to-agent hand-off | Delegation between autonomous systems with their own tools and reasoning | Distinct responsibility domains that must operate, scale, and fail independently |

Weigh **latency** (every hop adds time; a direct call is fastest), **security** (who authenticates to what), and **statefulness** (does the other side keep state across calls?). "Multiple teams and clients need the same tool" means MCP; a one-off inside a single product means direct, and wrapping it in a protocol layer adds maintenance without benefit.

### 3.2 Least-privilege tool configuration

Capability bloat is an agent carrying more tools and permissions than its task requires. The signs: tool counts far beyond the task, overlapping descriptions, broad write permissions granted "just in case", and tools that never appear in invocation logs but ship in every request. For each tool connection, decide: **remove** it, **scope it down** (read-only, one resource, one tenant), or **replace it with a context-efficient access pattern**, such as one search tool instead of forty endpoint tools, or code execution over an API instead of a tool per operation. Oversized agents split into scoped subagents.

### 3.3 Progressive discovery versus monolithic context

Progressive discovery loads tool definitions, Skills, schemas, and reference data on demand as the agent narrows in (tool search with deferred loading, Skills whose full text loads only when used). Monolithic loading front-loads everything into every request. **Progressive discovery wins when the toolset or corpus is large**: lower token cost, better attention, higher selection accuracy, at the price of an extra discovery step. Monolithic loading is fine for a small, stable toolset in a latency-sensitive path.

### 3.4 Authentication and authorization

- **Agents act with the calling user's permissions.** One over-privileged service account shared by all users erases per-user boundaries and audit trails.
- **Look for credential exposure** (keys in prompts, code, client apps, logs, or committed config) and **privilege escalation** (a tool that lets a low-privilege user reach high-privilege data through the agent). Specify a mitigation for each: secrets in a secret manager, short-lived scoped tokens, per-user authorization checks in the tool itself.
- Every tool invocation should be attributable: who triggered it, with which permissions, against which resource.

### 3.5 Production reliability controls

Read the failure pattern in the traces, then pick the control:

| Pattern | Control |
|---------|---------|
| Bursts of 429 rate-limit errors | Client-side rate limiting and queueing; backoff honoring `retry-after` |
| Transient 500 / 529 errors | Retry with exponential backoff and jitter, capped |
| Duplicate side effects after retries (double payments, duplicate tickets) | **Idempotency keys** on side-effecting tools, so a retried request returns the original result |
| A model or region persistently unavailable | Fallback routing to another model or surface, with the quality trade-off accepted in advance |

The idempotency row is the one candidates miss: when a tool executed but the client timed out before seeing the result, every retry repeats a completed action. Fewer retries make it rarer; an idempotency key makes it safe. A prompt telling the model to "check first" can't fix it, because the retry happens in your client, where the model never sees the earlier result.

### 3.6 Relieving the binding constraint, and monitoring

When a system's dominant constraint is **accuracy** or **latency**, evaluate the candidate changes (retrieval depth, model tier, caching, call pattern such as parallel calls or streaming) and pick the one that relieves the binding constraint **at least cost to the other**. Re-ranking buys accuracy with latency; caching buys latency and cost with nothing; a tier upgrade buys accuracy with both.

At scale, failures go undetected when monitoring watches the wrong thing. A scenario where "nobody noticed for three weeks" asks which signal would have surfaced it: per-slice quality sampling, tool error rates per tool, refusal and truncation rates, cost per task, latency percentiles per step, or traces linking each answer to its retrieved sources.

## Chapter 4: Retrieval architecture and quality

### 4.1 Choosing the retrieval architecture

| Architecture | How it works | Fits |
|--------------|-------------|------|
| Full-corpus context | Put the whole corpus in the prompt (and cache it) | Small, stable corpora within the context budget |
| Pre-built RAG pipeline | Chunk, embed, and index ahead of time; retrieve top passages per query | Large corpora, predictable lookup-style queries, tight latency |
| Agentic search with tools | The agent searches, reads, and refines with tools (search, grep, fetch) | Exploratory, multi-hop questions; corpora that change constantly |

Decide on corpus size and change rate, the query pattern, and the latency and cost limits.

### 4.2 Index quality: chunking, contextual retrieval, and fallbacks

| Chunk size | Strength | Weakness |
|-----------|----------|----------|
| Small (sentence/paragraph) | Precise matching, less noise per chunk | Loses surrounding context; answers can miss qualifiers |
| Large (section/page) | Preserves context and cross-references | Dilutes relevance scoring, inflates token cost |

Chunk to the granularity of the questions. When you index, use **contextual retrieval**: before embedding, prepend each chunk with a short description of where it sits in its document (which contract, which section, which period), and index it for both embeddings and keyword (BM25) search, so a chunk that says "the fee rises 3%" is still found by a query about the 2026 vendor renewal. Then configure **fallbacks**: hybrid keyword-plus-semantic search for exact identifiers (error codes, SKUs), and a fallback to broader or agentic search when retrieval scores are low, rather than answering from weak passages.

### 4.3 The retrieval quality rules

- **Re-rank when first-stage retrieval has high recall but low precision.** A re-ranker reorders a broad candidate set so only the most relevant chunks reach the prompt.
- **Fix retrieval quality before stuffing context.** If top results are noisy, retrieving more feeds the model more noise at higher cost. "Retrieve more chunks" as a quality fix is a marked trap.
- **Filter by metadata before semantic search** when the corpus partitions cleanly (product, region, date, document status).

```python
def retrieve(query: str, region: str, k: int = 5) -> list[Chunk]:
    candidates = index.hybrid_search(                          # keyword + embeddings
        query=query,
        filter={"region": region, "doc_status": "current"},     # metadata first: shrink the space
        top_k=40,                                               # first stage: high recall
    )
    reranked = reranker.score(query, candidates)                # second stage: precision
    if not reranked or reranked[0].score < MIN_SCORE:
        return agentic_fallback(query)                          # weak retrieval: search wider
    return reranked[:k]                                         # only the best reach the prompt
```

When answers are wrong, the fix lives in this function (chunking, context, the filter, the re-ranker, the fallback), never in raising `k`.

## Chapter 5: Evaluation, testing, and optimization

### 5.1 Coverage gaps: metrics match failures

When a failure reached production, ask which dimension the eval suite never measured:

| Failure you care about | Metric |
|------------------------|--------|
| Wrong answers | Accuracy against a labeled dataset |
| Answers not supported by the sources | Groundedness (every claim traceable to retrieved text) |
| Slow responses | Latency percentiles (p95/p99), time to first token |
| Budget overruns | Cost per request, tokens per task |
| Harmful output | Safety violation rate on adversarial sets |
| Injection and leakage | Security test pass rate against known attacks |

A suite that scored only accuracy can't catch a fluent, ungrounded answer; one that never ran adversarial inputs can't catch an injection.

### 5.2 Deriving evaluations from the business process

An eval exists to support a decision: a model change, a prompt change, a release gate. Take the part of the business process that decision affects, derive the success criterion from the **business outcome** (claims processed correctly, tickets resolved without reopening), and mix methods so the test set covers the **deployed distribution**, including the hard and rare cases in known proportions. Hold the eval set out of prompt development, and refresh it as traffic drifts.

```json
{"id": "inv-0042", "input": "Invoice, EU format, scanned", "expected": {"total": 1840.00, "currency": "EUR"}, "slice": "eu-scanned"}
{"id": "inv-0043", "input": "Invoice, US format, digital", "expected": {"total": 220.50, "currency": "USD"}, "slice": "us-digital"}
{"id": "adv-0007", "input": "Invoice with handwritten injection attempt", "expected": {"refused_or_flagged": true}, "slice": "adversarial"}
```

Score per slice; an aggregate can hide a failing one.

### 5.3 Graders and judge bias

- **Code-based graders** for objective properties: schema validity, required fields, exact values, latency budgets.
- **LLM-as-judge** (a separate model call grading against a written rubric) for open-ended quality.
- **Human review calibrates the judge.** When judge scores disagree with people, name the bias and apply its correction:

| Bias | Symptom | Correction |
|------|---------|-----------|
| Position | Pairwise judge prefers whichever answer comes first | Evaluate both orders and keep only consistent verdicts |
| Verbosity | Longer answers score higher regardless of quality | Rubric criteria that don't reward length; length-matched comparisons |
| Self-preference | Judge favors outputs from its own model family | A judge from a different model or family, checked against human labels |
| Judge drift | Agreement with humans falls over time | Periodic recalibration on fresh human-labeled samples |

```python
JUDGE_RUBRIC = """Score the response 1-5 on each criterion, with one sentence of evidence per score.
Length is not a criterion: a short answer that meets the criteria scores as high as a long one.
1. Faithfulness: every claim is supported by the retrieved passages
2. Completeness: the answer addresses all parts of the question
3. Tone: professional, no speculation presented as fact
Output JSON: {"faithfulness": n, "completeness": n, "tone": n, "evidence": {...}}"""
```

### 5.4 Experimental design

Comparing two prompt or model configurations within a sample and cost budget:

- **One variable per experiment.** Change the prompt or the model, never both.
- **Same cases for both arms** (a paired comparison), drawn from the deployed distribution.
- **Several trials per case.** Outputs vary run to run, so a single run per case can't separate the configuration effect from noise. Run each case enough times (often 3-5) to see the spread, then compare the configurations by more than that spread.
- **Predefine the success metric and sample size** before starting. Choosing the variant that "feels better" after ten spot checks is a tested anti-pattern.

### 5.5 Root-cause isolation

| Symptom in logs or traces | Likely cause | First fix |
|---------------------------|-------------|-----------|
| Correct documents retrieved, answer still wrong | Hallucination / weak grounding | Tighten grounding, require citations to retrieved text |
| Wrong or missing documents retrieved | Retrieval failure | Fix chunking, context, query construction; add re-ranking |
| A tool or subagent returned an error the agent glossed over | Tool or subagent error | Fix the tool; surface errors instead of continuing |
| Fails only on complex multi-step reasoning | Model mismatch (tier too low, or wrong model for the task) | Test the same prompt on a higher tier |
| Fails uniformly across input types | Prompt failure | Rewrite criteria to be explicit and testable |

### 5.6 Cost, latency, and model migration

Read telemetry before optimizing: where is spend concentrated (which route, which step), what is the **cache hit rate** on routes that should cache, where does latency accumulate? Then apply the lever that reduces it without breaking the quality floor: caching for repeated input, batch for non-urgent bulk, lower effort or a cheaper tier for routes where evals hold, streaming and parallel calls for latency.

Models are deprecated on a published timeline. Given a deprecation date and regression results for a candidate version, choose the response:

| Regression results | Response |
|-------------------|----------|
| Candidate passes the suite | Migrate on schedule, pinned to the new version |
| Small, prompt-fixable regressions | Re-tune prompts, then re-baseline the evals on the new model |
| Large regressions, time remains | Stay pinned and defer, while fixing; plan the move before the retirement date |
| Retirement imminent | Migrate with mitigations (narrower rollout, more review) rather than run on a model that is about to fail |

## Chapter 6: Governance, safety, and compliance

### 6.1 Guardrail layers and placement

Defense in depth, in order:

1. **Input validation and injection screening** before anything reaches the model
2. **System prompt constraints**: role, boundaries, refusal behavior
3. **Tool permission scoping** so the agent can't act outside its mandate
4. **Output filtering and moderation** before responses reach users or systems
5. **Human review** for the high-stakes residue the earlier layers flag

Prompt instructions are probabilistic; permission scoping and output validation are deterministic, so compliance-critical controls include the programmatic layers. **Placement** questions describe a misuse path and ask for the control that closes it **without degrading a stated legitimate use**: block the export path, not the whole tool; restrict the recipient list, not the email feature.

```python
def handle(user_input: str, user: User) -> str:
    screened = injection_screen(user_input)            # 1. input validation
    if screened.blocked:
        return refusal(screened.reason)

    response = client.messages.create(
        model=MODEL, max_tokens=4000,
        system=CONSTRAINED_SYSTEM_PROMPT,               # 2. role, boundaries, refusal behavior
        tools=scope_tools_for(user),                    # 3. least-privilege tool set per caller
        messages=[{"role": "user", "content": screened.text}],
    )

    verdict = output_filter(response)                   # 4. moderation before delivery
    if verdict.requires_review:
        return queue_for_human(response, verdict)       # 5. human on the flagged residue
    return verdict.text
```

### 6.2 The injection surface

Anything that enters the model's context from outside your control is a channel for injected instructions: **retrieved documents, tool results, MCP server responses, and third-party Skills**. Controls that keep untrusted content from acting as instruction: mark and delimit it as data, keep privileged instructions in the system prompt, screen it, scope tools so a hijacked agent can do little, vet and pin third-party Skills and MCP servers, and require approval for actions triggered while processing untrusted content.

### 6.3 Risk assessment and ranking

For a proposed deployment, list risks by category and rank them by **exposure** (likelihood times impact, given this deployment's users, data, and tools):

- **Attack surface:** inputs from the public, documents from third parties, tools with write access
- **Failure modes:** hallucination in a consequential output, silent tool failures
- **Token and quota exhaustion:** runaway loops, abuse that burns the rate limit or the budget for everyone
- **Dependency and supply-chain risk:** third-party MCP servers, Skills, libraries, and a single model or region dependency

The top risk is the one this deployment is most exposed to, not the most dramatic one in the abstract.

### 6.4 Human-in-the-loop gates

- A human gate sits **before irreversible or high-stakes actions**: payments and charges, deletions, external communications, contract commitments.
- Reversible, auditable steps run without a gate, backed by the audit log and the ability to undo.
- Constrain an action deterministically where you can (send only to the address on file) instead of reviewing it.
- **A model's self-reported confidence is never the trigger** for a gate on an irreversible step; thresholds are set by the system.
- Gating every step destroys the efficiency case and trains reviewers to rubber-stamp. Gate where reversibility and stakes demand it; sample elsewhere.

### 6.5 Architectural controls for compliance

Match the control to the obligation, and pick the set that **evidences** it:

| Obligation | Control |
|-----------|---------|
| Data must be processed in a jurisdiction or cloud boundary | Data residency through the deployment surface (Chapter 1.5) |
| Data must not be retained by the provider | Retention settings and zero-data-retention arrangements where eligible |
| Personal data minimization | PII detection and redaction before the model sees it, and in logs |
| Demonstrable accountability | Audit logging of inputs, outputs, tool calls, and approvals |
| Customers' data kept apart | Tenant isolation in storage, retrieval indexes, caches, and credentials |

| Framework | One line | Triggered by |
|-----------|----------|--------------|
| GDPR | EU personal-data regulation: lawful basis, minimization, right to erasure | Processing EU residents' personal data, wherever you sit |
| HIPAA | US health-information law: safeguards and vendor BAAs | Patient and health data for US covered entities |
| FedRAMP | US federal cloud authorization program | Cloud services for US federal agencies |

Scenarios can trigger more than one framework, and more than one control.

### 6.6 Bias: find the source before the fix

When outputs or a dataset show disparate results across groups, the mitigation depends on where the bias comes from:

| Source | Evidence | Mitigation |
|--------|----------|-----------|
| Data | The training examples, retrieved documents, or historical decisions are skewed | Rebalance or correct the data; add counter-examples |
| Prompt framing | The prompt describes groups differently or uses loaded criteria | Neutral, criteria-based instructions applied identically |
| Evaluation design | The test set under-represents a group, or the rubric encodes a preference | Stratified test sets and rubrics reviewed for fairness |

Measure per group before and after; an aggregate can look fair while one group fails.

## Chapter 7: Stakeholders and the solution lifecycle

### 7.1 Lifecycle phases and discovery

**Discovery, design, handoff, monitoring, iteration.** Starting to build before discovery outputs exist is wrong at the professional level. Discovery produces:

- A business problem statement with **measurable success criteria**
- A **constraint inventory**: latency budgets, cost ceilings, compliance regimes, data residency
- A **data inventory and access map**: what exists, where it lives, who owns it, what the agent may touch
- A **stakeholder map with decision owners**, so trade-off calls have a named approver
- A **current-process baseline**, because improvement claims need a before number

### 7.2 Commitments a probabilistic system can't make

Read discovery notes and draft SLAs for commitments the architecture can't meet: "100% accuracy", "identical answers every time", "never makes a mistake on legal questions", "responds in under 200 ms" for a deep-reasoning route, "no human review needed" on a regulated decision. Resolve each by **clarifying the requirement** (a measured accuracy floor with an error budget, a review path) or **changing the architecture** (a faster tier on that route, a human gate). Commit to measured rates plus remediation, never to perfection:

| Commitment | Target | Measured by | On breach |
|-----------|--------|-------------|-----------|
| Latency | p95 under 4s | Per-request traces | Route review, capacity add |
| Accuracy floor | 96% on the held-out eval set, per slice | Weekly eval run | Error budget consumed; change freeze until recovered |
| Cost | Under $0.04 per transaction | Usage logs | Lever review (caching, routing, batch) |
| Escalation | 100% of flagged outputs reach human review in 4h | Queue metrics | Staffing or threshold adjustment |

### 7.3 Architecture decision records

An ADR is a short, version-controlled document capturing one consequential decision: context, options considered, decision, consequences. A good one makes the **trade-off and the residual risk explicit** and addresses every stakeholder constraint, without overstating certainty about model behavior ("the model will always..." is a red flag in an ADR).

```markdown
# ADR-007: Workflow pattern for contract summarization (not agentic)

## Status
Accepted, 2026-08-12

## Context
Legal requires identical five-section briefs with a reviewable processing
trail. Compliance sign-off depends on deterministic, auditable steps.

## Options considered
1. Agentic loop with document tools: flexible, but non-deterministic paths
   fail the auditability requirement
2. Fixed workflow, one model call per section, all inputs/outputs logged
3. Single augmented call: cheapest, but can't produce per-step trails

## Decision
Option 2. Auditability is the binding constraint and only fixed steps satisfy it.

## Consequences
Per-contract cost is ~5x a single call. New section types require a code
change rather than a prompt change. Section summaries still carry a measured
error rate (2.1% on the eval set); briefs for contracts over $1M get legal review.
Revisit if the audit requirement is relaxed or section count exceeds 10.
```

### 7.4 Handoff completeness

The team receiving a Claude system needs more than the code. Check the handoff package for the missing piece that would block them:

- **Assumptions:** expected input formats, volumes, languages, the model version pinned
- **Dependencies:** API keys and who owns them, MCP servers, indexes and how they refresh, quotas
- **Runbook:** how to tell the system is unhealthy, what to do on rate limits, outages, a quality regression, or a model deprecation, and who to escalate to
- **Baselines:** the eval suite, its current scores, and the prompt inventory

## Chapter 8: Team enablement

### 8.1 Packaging and distributing a proven workflow

A workflow proven on one team spreads as a **plugin**: a packaged bundle of Skills, hooks, subagents, commands, and MCP configuration with a manifest, published in an internal **marketplace** so teams install it once and receive versioned updates. Then decide what is **enforced centrally** and what is left to teams:

- **Managed settings** (deployed by IT, which users can't override) enforce what must hold everywhere, especially for runs nobody watches: denied tools and permissions, allowed marketplaces, required hooks, sandboxing.
- **The managed CLAUDE.md** carries organization-wide guidance such as coding standards.
- **Project configuration** (committed `.claude/settings.json`, CLAUDE.md, Rules files) carries each team's conventions.

| Platform | Managed CLAUDE.md location |
|----------|---------------------------|
| macOS | `/Library/Application Support/ClaudeCode/CLAUDE.md` |
| Linux / WSL | `/etc/claude-code/CLAUDE.md` |
| Windows | `C:\Program Files\ClaudeCode\CLAUDE.md` |

The rule: an enterprise scenario asking how to **prevent** an action everywhere wants managed settings (`permissions.deny`); one asking how to **standardize behavior** wants the managed CLAUDE.md. Instructions shape what the model does; settings are enforced by the client regardless of what the model decides.

### 8.2 Configuring the Agent SDK and Claude Code

- **Permission modes:** `default` (asks before edits and commands), `acceptEdits` (accepts file edits), `plan` (explores and plans without editing), `auto` (a classifier reviews actions instead of prompting), `dontAsk` (denies anything not pre-approved, useful for locked-down automation), `bypassPermissions` (skips prompts; isolated environments only).
- **Hooks** enforce required steps and block dangerous ones deterministically.
- **Subagent definitions** give a delegated task its own prompt, context, and minimal tool set.
- **Headless and CI operation** (`claude -p`, or the Agent SDK in a pipeline) runs with the repository's committed configuration and the narrowest permissions the job needs.

### 8.3 Accountability for AI-generated code

When a team adopts AI-assisted development, the control that preserves human ownership is a **named human reviewer who approves and answers for every change**, backed by tests and the normal review requirements. Watch for the gaps: AI-written code merged with no human approval, the same AI session reviewing its own output, reviews skipped because "the tests pass", or nobody able to explain the change after merge.

---

# Part II: Exam domain notes

## Domain 1: Solution Design and Architecture (18%)

**Skills tested:** Task Delegation Between Claude and Humans; End-to-End Architecture Evaluation; Architectural Pattern Selection; Orchestrator and Subagent Decomposition; Value-Based Architectural Decisions; Deployment Surface and Agent Runtime Selection.

**Know:** reversibility, stakes, and accountability for delegation; the four patterns and the delegation boundary each sets; the four-part architecture; where decompositions fail; the five value pillars; surfaces, runtimes, and their trade-offs; ZDR is not residency.

**Be able to:** assign each process step to Claude, a person, or both; find the component that fails first under a stated condition; pick the simplest sufficient pattern; choose the surface and runtime a binding constraint demands and name the trade-off.

**Anti-patterns:** agentic-by-default; architectures with no feedback loop; decomposition without independent subtasks; "all requirements met, no trade-off".

## Domain 2: Claude Models, Prompting, and Context Engineering (13%)

**Skills tested:** Model Tier Selection; System Prompt Diagnosis and Revision; Prompting Technique Selection; Context Composition and Token Economics; Cache Breakpoints and Reusable Packaging; Reasoning Effort and Context Lifecycle.

**Know:** the tiers and why each rejected tier fails; underspecification vs over-constraint; the technique table including native thinking with effort; caching economics, breakpoints by cadence, Skill packaging; context editing vs memory tool vs compaction.

**Be able to:** pick the tier that meets every binding constraint; revise a prompt without over-constraining; place breakpoints for a stated call pattern; allocate effort and a context strategy for a long-running agent.

**Anti-patterns:** flagship-everywhere; volatile content early in a cached prefix; more examples for a reasoning failure; vague criteria.

## Domain 3: Integration (21%)

**Skills tested:** Least-Privilege Tool Configuration; Authentication and Authorization Posture; Relieving the Binding Performance Constraint; Instrumentation and Monitoring Gaps; Retrieval Architecture Selection; Connection Mechanism Selection; Progressive Discovery vs. Monolithic Context Loading; Production Reliability Controls.

**Know:** remove, scope down, or replace a tool connection; credential exposure and privilege escalation; trade-offs among retrieval depth, tier, caching, and call pattern; the signals monitoring must cover; full-corpus vs RAG vs agentic search, contextual retrieval and fallbacks; MCP vs direct vs agent-to-agent; progressive discovery; rate limits, backoff, idempotency, fallback routing.

**Be able to:** trim a bloated tool configuration; fix an auth design; relieve accuracy or latency at least cost to the other; name the missing monitor; choose a retrieval architecture and configure it; make retries safe for side-effecting tools.

**Anti-patterns:** the mega-agent; shared service accounts; context-stuffing; protocol layers on one-off integrations; retries without idempotency.

## Domain 4: Evaluation, Testing, and Optimization (17%)

**Skills tested:** Evaluation Coverage Gaps; Deriving Evaluations from Business Processes; LLM-as-Judge Design and Bias; Experimental Design for Configuration Comparison; Root-Cause Isolation from Logs and Traces; Cost and Latency Optimization; Model Version Migration.

**Know:** the six metric dimensions; deriving criteria from business outcomes; the four judge biases and corrections; paired comparisons with several trials per case; the root-cause table; telemetry-first optimization; the migration responses.

**Be able to:** name the missing metric after a production failure; design an eval for a decision; correct a biased judge; size an experiment to separate signal from variance; isolate a root cause from a trace; choose pin, re-tune, re-baseline, or defer.

**Anti-patterns:** tuning on the test set; one run per case; multi-variable experiments; aggregate-only metrics; uncalibrated judges.

## Domain 5: Governance, Safety, and Risk Management (16%)

**Skills tested:** Guardrail Placement; Prompt Injection Surface and Controls; Risk Assessment and Ranking; Human-in-the-Loop Checkpoints; Architectural Controls for Compliance Obligations; Bias Source Identification and Mitigation.

**Know:** the five layers and placement against a misuse path; injection channels including MCP responses and third-party Skills; the four risk categories and ranking by exposure; gate placement by reversibility and stakes; the obligation-to-control table and the frameworks; the three bias sources.

**Be able to:** close a misuse path without breaking legitimate use; specify controls for an injection surface; rank risks for a specific deployment; gate only what must be gated; choose the control set that evidences an obligation; match a bias mitigation to its source.

**Anti-patterns:** single-layer guarantees; gates on everything; confidence-based gates; ZDR as residency; fixing data bias with a prompt.

## Domain 6: Stakeholder Communication and Lifecycle Management (7%)

**Skills tested:** Unsupportable Commitments in Requirements and SLAs; Architecture Decision Records; Operational Handoff Completeness.

**Know:** the lifecycle and discovery outputs; commitments a probabilistic system can't make and how to restate them; what a good ADR makes explicit; the four parts of a complete handoff.

**Be able to:** spot and fix an unsupportable commitment; revise an ADR to state the trade-off and residual risk; find the missing assumption, dependency, or runbook step.

**Anti-patterns:** promising determinism or perfection; ADRs that overstate certainty; handoff without runbooks and baselines.

## Domain 7: Developer Productivity and Operational Enablement (8%)

**Skills tested:** Packaging and Distributing Claude Code Workflows; Agent SDK and Claude Code Configuration; Accountability for AI-Generated Code.

**Know:** plugins and marketplaces; managed settings vs managed CLAUDE.md vs project configuration; the six permission modes; hooks, subagents, headless and CI; the human-ownership control.

**Be able to:** package a proven workflow for an organization; decide what to enforce centrally for unattended runs; configure a team workflow within safety limits; spot the accountability gap in a review process.

**Anti-patterns:** team standards in personal config; prevention by instruction instead of settings; `bypassPermissions` outside isolation; AI reviewing its own code.

---

# Part III: Exam preparation

## The preparation ladder

Five layers, in order. Each builds on the previous, and the free layers take you surprisingly far. Anthropic retired its official practice exam when the exams moved to Pearson VUE; the three sample questions in the official exam guide are what remains.

| Step | Resource | Cost |
|------|----------|------|
| 1. Learn the vocabulary | The official exam guide and Partner Academy prep course, plus the [Anthropic Academy courses](https://anthropic.skilljar.com/) mapped in Resources | Free |
| 2. Go to the source | [The Claude Developer Platform docs](https://platform.claude.com/docs) (integration, agents, evaluation, guardrails, cloud platforms) and [the Claude Code docs](https://code.claude.com/docs) | Free |
| 3. First calibration | [30 practice questions with explanations](./practice-questions.md) in this repo | Free |
| 4. Full calibration | [Full-length timed practice tests and a 500-card flashcard deck](https://preporato.com/certificates/claude-certified-architect-professional) on Preporato, including 70-question tests on the December 7 blueprint; the page has free sample questions to try first | Paid |
| 5. Prove it hands-on | [Auto-graded build-and-submit projects](https://preporato.com/certificates/claude-certified-architect-professional) at the architecture level | Paid |

Steps 1-3 cost nothing and tell you honestly where you stand. Steps 4-5 are how you close the gap they reveal.

## The twelve trap answers

Professional-level distractors are plausible and technically true in some context. These patterns mark an option wrong for the scenario at hand:

| Trap | Why it fails |
|------|-------------|
| Flagship-everywhere | Ignores cost and latency; the tier must meet every binding constraint |
| Agentic-by-default | Autonomy without a reason is a defect; the simplest sufficient pattern wins |
| No-trade-off | Real constraints conflict; an option claiming none is usually wrong |
| ZDR-as-residency | Retention and processing location are different obligations |
| Prompt-guarantee | Safety and compliance enforcement comes from permissions, validation, and layers |
| Context-stuffing | Retrieval precision and structure are the levers, not volume |
| Mega-agent | Capability bloat degrades selection and widens the blast radius |
| Retry-without-idempotency | Retrying a side-effecting call duplicates its effect |
| Gate-everything / confidence-gate | Gates go where reversibility and stakes demand, set by the system |
| Aggregate-metric | Per-slice evaluation is the professional answer |
| One-run-per-case | Run-to-run variance hides the configuration effect |
| Promise-perfection | SLAs commit to measured rates and remediation |

For multi-select items, apply the traps to each option independently: one bad pick costs the whole question, because there is no partial credit.

## Exam-day strategy

70 questions in 120 minutes is about 1.7 minutes each, and ten are unscored items you cannot spot, so treat every question as scored. The scenario stems are long, so read the **question line first**, then the scenario, so you know what to extract. Identify the domain, find the binding constraint (residency, latency, cost, audit, reversibility), and check each option against the trap table. Read how many responses the item asks for. Flag anything over three minutes, keep the last ten minutes for flagged items, and change an answer only when you find a definite error.

## Worked questions

Fifteen fresh questions in the exam's style. (Written for this guide; timed full-length practice is linked in Resources.)

**Q1.** A legal team needs contracts summarized into a fixed five-section brief, every time, with an auditable processing trail for compliance sign-off. Which pattern?

- A) An agentic loop with document tools, for flexibility across the many contract types
- B) A single augmented call with the whole contract in context and the brief template
- C) Multi-agent decomposition, with a router that picks a specialist per contract type
- D) A fixed workflow of model calls, one per section, with logged inputs and outputs

**Answer: D.** Fixed output structure plus auditability is the workflow tell. Options A and C add autonomy the requirement forbids, and B can't produce the per-step trail compliance wants.

**Q2.** A support assistant answers 50,000 queries daily. Evals show the Haiku-class tier handles 85% of traffic at target accuracy but fails on complex multi-policy questions. The architect's move?

- A) Route: the fast tier handles routine traffic and escalates the hard slice to a stronger tier
- B) Upgrade all of the traffic to the Opus-class tier, so that the hard questions are covered too
- C) Keep the fast tier for everything, and add more few-shot examples for the hard cases
- D) Fine-tune the fast tier on the failing multi-policy queries until it reaches the target

**Answer: A.** Routing keeps the cost of the easy 85% and the quality of the hard 15%. Option B pays flagship prices for solved traffic, C applies a prompting fix to a capability gap, and D proposes heavier machinery where routing solves it directly.

**Q3.** An agent's prompt begins with the current timestamp, then the system prompt, tool definitions, and reference documents. Prompt caching saves almost nothing. Why?

- A) The reference documents exceed the longest length that prompt caching can store
- B) Tool definitions can't be cached, so every request starts the prefix again after them
- C) The timestamp at the start changes on every request, so the prefix never matches
- D) The cache lifetime is shorter than the usual interval between two of the requests

**Answer: C.** A changing token early in the prefix breaks everything after it; order stable-first, variable-last. Option B is false, and A and D invent facts the scenario doesn't give.

**Q4.** Three product teams want the same internal knowledge-search capability from Claude Code, a desktop assistant, and a customer-facing agent. Integration mechanism?

- A) One MCP server that exposes the search capability to all three surfaces
- B) Each team builds its own direct API integration, for full control of its surface
- C) Agent-to-agent delegation from each surface to a dedicated search agent
- D) A shared prompt template that describes the search logic for each team to use

**Answer: A.** Build once, expose to many clients is MCP's defining case. Option B triples maintenance, C adds autonomous-system machinery for a shared tool, and D is a prompt where a protocol is required.

**Q5.** A RAG system's answers are frequently wrong. Traces show the top retrieved chunks are usually off-topic. The team proposes raising retrieval from 5 chunks to 20. Assessment?

- A) Correct, because more chunks raise the odds that the right one is included in the context
- B) Correct, but only together with a move to a model that has a larger context window
- C) Wrong, because the model tier should be upgraded first, before retrieval is changed at all
- D) Wrong: precision is the problem, so fix chunking and queries and consider re-ranking

**Answer: D.** Context-stuffing is the trap; when precision is low, volume amplifies noise and cost, so the fixes are chunking, query construction, chunk context, and re-ranking. Option C misdiagnoses: the wrong documents arrive, so retrieval is the failure.

**Q6. (Select TWO)** An underwriting assistant recommends loan approvals. Which two controls are required rather than optional?

- A) A system prompt instructing the model to be fair and unbiased in every case
- B) Human review before any final approval decision reaches a customer
- C) The Opus-class tier for all underwriting traffic, including routine applications
- D) Human review of every internal draft the model produces along the way
- E) Per-group evaluation of recommendation quality across demographic groups

**Answer: B and E.** A high-stakes, regulated decision needs a human gate (B), and fairness needs stratified evaluation (E). Option A is a prompt-guarantee, C is flagship-everywhere, and D is gate-everything on a low-risk internal step.

**Q7.** Two months after launch, an extraction system's judge scores drift upward while customer complaints rise. What most likely broke?

- A) The model was silently upgraded by the provider, which changed the extraction quality
- B) The eval dataset is too small to show the errors that customers are reporting now
- C) The judge no longer agrees with human standards; recalibrate it on fresh human labels
- D) Latency increased, so customers now notice and report more of the routine errors

**Answer: C.** Judge scores and human perception diverging is judge drift, the failure calibration exists to catch. Option A contradicts a pinned model, and B and D don't explain the divergence.

**Q8.** A pilot's stakeholders are unhappy: the system works but "isn't what we needed." A post-mortem finds no written success criteria, no constraint inventory, and no baseline of the process it replaced. Which phase failed?

- A) Discovery, whose outputs were never produced
- B) Design, for choosing the wrong pattern for the work
- C) Monitoring, for missing the quality regressions
- D) Handoff, for missing the operating documentation

**Answer: A.** All three missing artifacts (success criteria, constraints, baseline) are discovery outputs. A system that "works" while missing the need is what skipped discovery produces.

**Q9.** A draft ADR for choosing an agentic triage design states: "The model will always route tickets correctly, so no human review is needed." The support director's stated constraint is that no high-priority ticket may be misrouted without someone noticing within an hour. What revision does the ADR need?

- A) None, because the decision and its reason are both clearly documented already
- B) Remove the consequences section entirely, to keep the decision record short and easy to read
- C) Replace the agentic design with a fixed workflow, which never misroutes any ticket
- D) State the measured error rate and residual risk, and record the mitigation

**Answer: D.** An ADR must make the trade-off and residual risk explicit and address the stakeholder's constraint (for example a review queue for high-priority routes with a one-hour SLA), without overstating certainty about model behavior. Option A leaves a false certainty in a governing document, B deletes the part that matters, and C changes the decision when the problem is the record.

**Q10.** A platform team wants every engineer's Claude Code to follow the same review conventions and reach the same internal MCP servers. Where does the configuration live?

- A) Each engineer's `~/.claude/CLAUDE.md`, distributed through an onboarding document
- B) A shared service account whose settings every engineer inherits when they log in
- C) Committed project configuration with env-var secrets, or a plugin that bundles it
- D) A wiki page documenting the conventions and the MCP server addresses for everyone

**Answer: C.** Team-wide behavior lives in committed project configuration (CLAUDE.md and project-scoped MCP config), and a plugin packages it for many repositories. Option A depends on every individual complying forever, B is the shared-account anti-pattern, and D is invisible to the tooling.

**Q11.** An enterprise must guarantee that no developer's Claude Code session can ever call external network tools, on every machine and in every repository, and separately wants company coding standards applied everywhere. Which pairing is correct?

- A) The ban as deny rules in managed settings, and the standards in the managed CLAUDE.md
- B) Both in a managed CLAUDE.md deployed to every developer machine in the company
- C) Both in managed settings, deployed by IT so that no developer can override either one
- D) The ban in each project's committed settings, and the standards in each project's CLAUDE.md

**Answer: A.** Enforcement and guidance live in different layers: permission deny rules the client enforces, and guidance the model follows. Option B puts a hard requirement in a soft layer, C puts prose standards in a mechanism that can't express them, and D covers only repositories that adopt it.

**Q12.** Six months post-launch, the extraction system's weekly eval still scores 97%, but customers in one region report rising errors. The eval set was built from launch-week traffic and never refreshed, while that region's document formats changed. What failed?

- A) The model drifted over the six months, and it should be re-pinned to the version used at launch
- B) The accuracy target was set too low at launch, so the score hides the regional errors
- C) The judge rubric has drifted and needs recalibration against new human-labeled samples
- D) Eval maintenance: the set no longer mirrors production; refresh it with the new formats

**Answer: D.** An eval frozen at launch measures the past; refresh it and add the new formats as a scored slice. Option A invents drift against a pinned model, B tunes a number the measurement no longer supports, and C points at the judge when the dataset decayed.

**Q13.** A healthcare insurer's obligation requires that member data and all model inputs stay inside its Google Cloud environment, where its compliance attestations live. Its product team also wants Anthropic to host the agent loop so nobody has to manage session state. What should the architect recommend?

- A) The Anthropic API with Managed Agents, under a zero-data-retention arrangement
- B) Claude on Vertex AI, with the insurer's team owning the agent loop and session state
- C) The Anthropic API, with all member data copied into Google Cloud as a backup
- D) Vertex AI with Managed Agents, which satisfies both of the insurer's requirements at once

**Answer: B.** The residency obligation is binding, so the cloud surface wins and the team accepts owning the runtime, and that some features may arrive later there. Option A confuses retention with residency, C still sends inputs outside the boundary, and D assumes a hosted runtime exists on that surface and that no trade-off is needed.

**Q14.** A model your production system is pinned to retires in five weeks. The candidate replacement passes 94% of your regression suite; the failures are all in one output-format slice, and two prompt changes fixed half of them in a quick test. What is the right plan?

- A) Switch immediately, since 94% of the regression suite is close enough to ship
- B) Stay pinned to the old model indefinitely, since it is the only one that passes everything
- C) Re-tune prompts for the failing slice, re-baseline evals, and migrate before retirement
- D) Wait for the next model release, which may fix the format slice without any work

**Answer: C.** The regressions are concentrated and prompt-fixable, and the timeline allows a fix: re-tune, re-baseline, migrate on schedule. Option A ships known regressions, B runs into a hard retirement, and D bets the system on a release that may not come in time.

**Q15.** A team compares two prompt versions on 40 test cases, one run each. Version B wins 23 to 17, and they plan to ship it. Re-running version A alone on the same cases gives scores that vary by 5 points between runs. What should they do?

- A) Run each case several times for both versions, and compare against the run-to-run spread
- B) Ship version B now, since it won the comparison on the same 40 test cases
- C) Add more test cases to the comparison, but keep a single run for each one
- D) Change the model at the same time, so that the difference between the two versions grows larger

**Answer: A.** A 6-point win inside a 5-point run-to-run spread isn't evidence; several trials per case separate the configuration effect from noise. Option B ships noise, C still can't see variance within each case, and D adds a second variable.

## 6-week study plan

- **Weeks 1-2: baseline and gap map.** Check that your employer is in the [Claude Partner Network](https://claude.com/partners) (registration needs your company email). Read the exam guide that matches your exam date, complete the Partner Academy prep course, and map your experience against all seven domains and 39 skills honestly. Most candidates' gaps are governance, deployment surfaces, and evaluation design.
- **Weeks 3-4: the enterprise domains.** Work through the platform docs on integration, cloud deployment, and evaluation while practicing the judgment tables here (pattern and surface selection, reliability controls, root-cause isolation, migration). Run one experiment with several trials per case, calibrate one LLM judge against human labels, and write one ADR and one handoff runbook for a hypothetical engagement. The [hands-on projects](https://preporato.com/certificates/claude-certified-architect-professional) (paid) cover this ground with automatic grading.
- **Weeks 5-6: calibrate.** Start with the [30 practice questions](./practice-questions.md) in this repo, then take [full-length timed practice tests](https://preporato.com/certificates/claude-certified-architect-professional). With seven domains, a comfortable average can hide a failing domain, so read the per-domain breakdown ruthlessly and drill the weak two. Final week: Part III daily, the [cheat sheet](https://preporato.com/blog/claude-certified-architect-professional-cheat-sheet-2026) the night before.

Expanded week-by-week version: [6-week CCAR-P study plan](https://preporato.com/blog/ccar-p-study-plan-6-week-preparation-2026).

## Pre-exam checklist

- [ ] I can assign process steps to Claude, a person, or both by reversibility, stakes, and accountability
- [ ] I can choose augmented, workflow, agentic, or Skills-based, defaulting to the simplest sufficient pattern
- [ ] I can find the component that fails first under a stated load or trust condition
- [ ] I can judge a decomposition on observability and error recovery
- [ ] I can anchor a recommendation to the stated value pillar and ceiling
- [ ] I can choose a deployment surface and agent runtime and name the trade-off, and I know ZDR is not residency
- [ ] I can pick a tier that meets every binding constraint and say why the others fail
- [ ] I can diagnose an underspecified system prompt without over-constraining it
- [ ] I can match prompting technique to failure, including native thinking with effort
- [ ] I can place cache breakpoints by change cadence and use Skill-based packaging
- [ ] I can choose context editing, the memory tool, or compaction for a long-running agent
- [ ] I can trim a tool configuration to least privilege and fix an auth design
- [ ] I can relieve accuracy or latency at least cost to the other, and name the missing monitor
- [ ] I can choose full-corpus, RAG, or agentic search, and configure contextual retrieval and fallbacks
- [ ] I can select MCP, direct API, or agent-to-agent from reuse, latency, security, and state
- [ ] I can make retries safe with idempotency keys and add fallback routing
- [ ] I can name the missing metric after a production failure and derive an eval from the business outcome
- [ ] I can correct position, verbosity, self-preference, and drift bias in an LLM judge
- [ ] I can design a comparison with several trials per case
- [ ] I can isolate a root cause from traces and plan a model migration within a deprecation timeline
- [ ] I can place guardrails and gates without blocking legitimate use
- [ ] I can map an injection surface, rank deployment risks, and pick compliance controls that evidence an obligation
- [ ] I can trace bias to data, prompt framing, or evaluation design
- [ ] I can restate an unsupportable commitment, fix an ADR, and complete a handoff package
- [ ] I can package a workflow as a plugin and decide what managed settings enforce
- [ ] I know the six permission modes and the control that keeps humans accountable for AI-written code
- [ ] I have the twelve traps down cold and apply them per option on multi-select items
- [ ] I have taken at least two full-length timed practice tests and reviewed every miss

## Resources

**Official (free):**
- [Claude Certified Architect - Professional](https://anthropic-partners.skilljar.com/claude-certified-architect-professional-certification) on the Anthropic Partner Academy: both exam guides (testing through December 6, and from December 7), the prep course, and registration
- [Claude Developer Platform docs](https://platform.claude.com/docs) and [Claude Code docs](https://code.claude.com/docs)
- Anthropic Academy courses, mapped to this exam's domains:
  - [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api): prompting, tool use, RAG, agents, MCP, production patterns
  - [Introduction to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol) and [MCP: Advanced Topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics): the integration domain
  - [Claude with Amazon Bedrock](https://anthropic.skilljar.com/claude-in-amazon-bedrock) and [Claude on Google Cloud](https://anthropic.skilljar.com/claude-with-google-vertex): the deployment surfaces behind solution-design scenarios
  - [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action): the developer productivity and enablement domain

**Free articles (preporato.com):**
- [What changes on December 7](https://preporato.com/blog/ccar-p-exam-changes-december-2026) · [CCAR-P complete guide](https://preporato.com/blog/claude-certified-architect-professional-complete-guide-2026) · [Cheat sheet](https://preporato.com/blog/claude-certified-architect-professional-cheat-sheet-2026) · [Domains breakdown](https://preporato.com/blog/ccar-p-exam-domains-complete-breakdown-2026) · [Exam format](https://preporato.com/blog/ccar-p-exam-format-structure-what-to-expect-2026) · [How to pass first attempt](https://preporato.com/blog/how-to-pass-ccar-p-first-attempt-2026)
- Topic guides: [enterprise deployment (Bedrock/Vertex/Foundry)](https://preporato.com/blog/ccar-p-enterprise-deployment-bedrock-vertex-foundry-guide) · [governance, guardrails & HITL](https://preporato.com/blog/ccar-p-governance-guardrails-hitl-compliance-guide) · [cost & latency optimization](https://preporato.com/blog/ccar-p-cost-latency-optimization-prompt-caching-guide) · [evaluation strategy](https://preporato.com/blog/ccar-p-evaluation-strategy-eval-datasets-metrics-guide) · [CCAR-P vs Developer - Professional](https://preporato.com/blog/claude-developer-professional-vs-architect-professional-2026)

**Practice:**
- [30 practice questions with explanations](./practice-questions.md) in this repo (free)
- [The CCAR-P page on Preporato](https://preporato.com/certificates/claude-certified-architect-professional): free sample questions, then (paid) full-length timed practice tests on both blueprints, a 500-card flashcard deck, and auto-graded hands-on projects

---

*Not affiliated with Anthropic. Exam details reflect the program as of November 2026; the Partner Academy is authoritative. Found an error? [Open an issue](https://github.com/preporato/claude-certification-guide/issues).*
