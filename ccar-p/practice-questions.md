# CCAR-P practice questions

30 practice questions for **Claude Certified Architect - Professional** (CCAR-P), written for this repo and spread across the exam's seven domains by their official weights. 6 of them ask for more than one answer, as some of the real exam's questions do (each item says how many to pick); those count only when every choice is right.

Choose your answer before you open the explanation.

**Want a timed run?** The [CCAR-P page on Preporato](https://preporato.com/certificates/claude-certified-architect-professional) has free sample questions and full-length timed practice tests in the exam's format, with a score for every domain.

| Domain | Exam weight | Questions here |
|---|---|---|
| Solution Design and Architecture | 18% | 5 |
| Claude Models, Prompting, and Context Engineering | 13% | 4 |
| Integration | 21% | 6 |
| Evaluation, Testing, and Optimization | 17% | 5 |
| Governance, Safety, and Risk Management | 16% | 5 |
| Stakeholder Communication and Lifecycle Management | 7% | 2 |
| Developer Productivity and Operational Enablement | 8% | 3 |

---

### Question 1

*Solution Design and Architecture*

A support team wants answers to product questions grounded in a 300-page manual. Questions are single-turn, and the manual is updated monthly. What is the simplest sufficient architecture?

- **A.** Retrieval over the manual feeding one model call that cites the passages it used
- **B.** An autonomous agent that browses the manual page by page until it finds the answer
- **C.** A multi-agent research system with a planner and three specialist agents for the manual
- **D.** A model fine-tuned on the manual every month, so the answers always reflect the latest version

<details>
<summary>Answer</summary>

**A.** One well-scoped, grounded call meets the requirement, so retrieval plus a single call is the simplest sufficient pattern (A). C and B add autonomy the task doesn't need, with the cost and latency to match. Monthly fine-tuning (D) is heavy, slower to update than re-indexing, and gives no citations.

</details>

### Question 2

*Solution Design and Architecture*

Which architecture proposal for an invoice-processing assistant is complete?

- **A.** Extraction with schema validation; posting to the ERP with an exceptions queue; a dashboard of monthly invoice volume
- **B.** Intake and OCR; extraction with schema validation; ERP posting with an exceptions queue; evals and corrections fed back
- **C.** Email intake and OCR; extraction with the most capable model at high effort; posting straight into the ERP system
- **D.** Email intake and OCR; a multi-agent extraction team with a reviewer agent; posting to the ERP; a launch announcement

<details>
<summary>Answer</summary>

**B.** A complete architecture has input, processing, output and a feedback loop that turns evals, user corrections and monitoring into design changes (B). C has no feedback loop. A has no input stage, and a volume dashboard measures activity without feeding quality back. D adds complexity and still has no feedback loop.

</details>

### Question 3

*Solution Design and Architecture*

Two designs meet the accuracy target. Design 1 uses the top tier: p95 latency 6 seconds, \$0.09 per request. Design 2 routes between the fast and balanced tiers: p95 latency 2 seconds, \$0.02 per request. The client's stated constraint is a 3-second p95 SLA at 2 million requests a month. Which design, and why?

- **A.** Run both designs in production indefinitely and let the traffic decide over time
- **B.** Postpone the decision until a newer model is released, since prices keep falling
- **C.** Design 1, because the top tier leaves quality headroom for harder requests later on
- **D.** Design 2, because it meets the latency SLA and the cost pillar at the same accuracy

<details>
<summary>Answer</summary>

**D.** When both options meet accuracy, the stated business constraint decides, and only Design 2 meets the 3-second SLA, at about \$40,000 a month against \$180,000 (D). C breaks the SLA. A doubles cost and complexity for no reason. B ignores a decision the data already supports.

</details>

### Question 4

*Solution Design and Architecture*

A due-diligence system must analyze each target company's financials, legal filings and press coverage. The three analyses are independent, and each needs different tools and sources. Which design fits?

- **A.** Three separate systems, one per analysis, each delivering its own report to the client
- **B.** One agent holding all the tools for all three analyses, so a single context sees everything
- **C.** An orchestrator with three scoped subagents running in parallel, then a synthesis step
- **D.** One agent doing the three analyses in sequence, finishing each before it starts the next

<details>
<summary>Answer</summary>

**C.** Independent subtasks with different tool needs are what justifies decomposition: each subagent gets a narrow toolset and its own context, and the orchestrator merges the results (C). B is capability bloat. D gives up parallelism and mixes three contexts. A skips the synthesis the client actually needs.

</details>

### Question 5

*Solution Design and Architecture*

A global retailer's policy assistant covers 14 regions. Each region's policies differ and are owned by different teams. Answers mix rules from different regions. What is the best design change?

- **A.** Put all 14 regions' policies in every request, so that the model always has the complete set to work from
- **B.** Tag documents with their region and filter retrieval by the user's region before semantic search
- **C.** Fourteen regional agents that negotiate with each other on every question until they agree
- **D.** Ask users to mention their region in each question, and change nothing else in the system

<details>
<summary>Answer</summary>

**B.** The data has a clean partition, so filtering on region metadata keeps other regions' rules out of the context (B). C adds coordination machinery to a retrieval problem. A is context stuffing. D leaves the mixed retrieval in place.

</details>

### Question 6

*Claude Models, Prompting, and Context Engineering*

Which TWO workloads benefit most from prompt caching? (Select TWO)

- **A.** Single requests shorter than the minimum cacheable length, sent thousands of times a day
- **B.** Requests whose first line is the current timestamp, followed by a long, stable policy text that never changes
- **C.** An agent loop that resends the same 12,000-token system prompt and tool definitions on every turn
- **D.** An endpoint where many users ask questions about the same 50-page policy within minutes of each other
- **E.** A weekly job that sends one unique 3,000-token prompt, different every time it runs

<details>
<summary>Answer</summary>

**C and D.** Caching pays off when a long, stable prefix repeats within the cache lifetime (C, D). A weekly unique prompt (E) never repeats in time. A timestamp at the start (B) breaks the prefix on every request. Prompts under the minimum length (A) are never cached.

</details>

### Question 7

*Claude Models, Prompting, and Context Engineering*

An eligibility step must apply six interacting rules. Accuracy is the priority, and the latency budget is generous. Which prompting approach fits?

- **A.** A lower effort level, so that the model commits to an answer before it overthinks the interacting rules
- **B.** Few-shot examples alone, with no stated rules, so the model infers the logic from the cases
- **C.** Have the model reason through each rule, stated as an explicit criterion, before deciding, then validate the result
- **D.** A zero-shot prompt kept as short as possible, so that the model isn't distracted by the detail of the six rules

<details>
<summary>Answer</summary>

**C.** Multi-step logic benefits from explicit reasoning before the answer, and the generous latency budget covers its cost (C). Zero-shot (D) suits simple, unambiguous tasks. Examples (B) teach format and edge cases, and six interacting rules still need to be stated. Lower effort (A) cuts the reasoning the task needs.

</details>

### Question 8

*Claude Models, Prompting, and Context Engineering*

An enterprise assistant's system prompt has grown to 60,000 tokens of procedures for 40 business processes, and most requests need one or two of them. Latency and cost are high, and instruction-following has slipped. What is the best restructuring?

- **A.** Build 40 separate assistants, one per business process, and make users choose the right one
- **B.** Move to a model with a larger context window, so that all 40 procedures fit with plenty of room to spare
- **C.** Mark the most important procedures in capitals so the model gives them priority over the rest
- **D.** Keep the system prompt to the core role and rules, and load each procedure as a Skill only when relevant

<details>
<summary>Answer</summary>

**D.** Loading procedures on demand keeps the context small and focused, which improves attention, cost and latency together (D). Emphasis (C) doesn't shrink the prompt. A bigger window (B) holds more of the same dilution. A moves the routing problem onto users.

</details>

### Question 9

*Claude Models, Prompting, and Context Engineering*

Downstream systems consume the assistant's JSON, and occasional schema violations cause failed transactions. Which change addresses this at the source, and what still needs checking?

- **A.** Structured outputs with the integration schema, plus semantic checks and handling of refusal and length stops
- **B.** A stronger instruction to follow the schema exactly, repeated at the end of the system prompt
- **C.** A retry loop that resends any request whose JSON fails validation, until a valid response arrives
- **D.** A regex step that repairs broken JSON before it is passed on to the downstream systems

<details>
<summary>Answer</summary>

**A.** Constrained decoding removes schema violations at the source, and semantic checks plus stop-reason handling cover what it doesn't guarantee (A). Retries (C) and instructions (B) reduce failures without eliminating them. Regex repair (D) guesses at intent and can corrupt data quietly.

</details>

### Question 10

*Integration*

A procurement agent must get quotes from a supplier's own AI agent, which runs on the supplier's systems with its own tools, policies and reasoning. Which integration mechanism fits?

- **A.** Agent-to-agent delegation over a defined protocol, with request and response contracts and auth
- **B.** A direct API call to Claude with the supplier's price list pasted into the prompt for each quote
- **C.** An MCP server that gives your agent direct access to the supplier's database of current prices
- **D.** A shared system prompt that both companies edit, so the two agents follow the same instructions

<details>
<summary>Answer</summary>

**A.** Two autonomous systems with separate owners, tools and policies call for delegation between agents, with contracts and isolation so either side can fail independently (A). C bypasses the supplier's agent and policies and assumes access you won't get. B works only if you already have current prices, which is what you're asking for. D merges two organizations' control into one prompt.

</details>

### Question 11

*Integration*

One internal app sends support tickets to Claude for tagging. One team owns it, and no reuse is planned. A platform engineer proposes building an MCP server first. What is the right assessment?

- **A.** Fine-tune a tagging model instead, so the app no longer needs to call Claude at all
- **B.** Build the MCP server now, since every integration should go through MCP as a matter of standard
- **C.** Use a direct API integration now, and revisit MCP if other surfaces later need the capability
- **D.** Use agent-to-agent delegation between the ticketing app and a dedicated tagging agent

<details>
<summary>Answer</summary>

**C.** MCP pays off when one capability serves many clients or surfaces, and one app with one owner is the direct-API case (C). B adds maintenance for a benefit that doesn't exist yet. D adds autonomous-system machinery to a single call. A skips a simpler option that works.

</details>

### Question 12

*Integration*

Which TWO observations are signs of capability bloat in a production agent? (Select TWO)

- **A.** Two tools have overlapping descriptions, and both plausibly handle 'find a customer'
- **B.** Each subagent's tools are scoped to the single responsibility it has in the system
- **C.** The reporting agent uses read-only credentials for the databases it queries
- **D.** It exposes 45 tools, and invocation logs show only 9 ever used
- **E.** Tool descriptions state when not to use each tool

<details>
<summary>Answer</summary>

**A and D.** Unused tools that ship with every request (D) and overlapping tools that blur selection (A) are classic signs of bloat. Scoped toolsets (B), read-only credentials for a read-only job (C) and boundary statements in descriptions (E) are the cure.

</details>

### Question 13

*Integration*

An agent connects to six MCP servers exposing 300 tools, and every request front-loads all of their definitions. Tool selection is poor and costs are high. What is the best fix?

- **A.** Add more examples to the system prompt showing which tool to pick for each of the common kinds of request
- **B.** Shorten every tool description to a single line, so the definitions take up fewer tokens
- **C.** Move to a model with a larger context window, so that all 300 definitions fit comfortably
- **D.** Load tool definitions on demand, such as with tool search, and give each agent only the servers it needs

<details>
<summary>Answer</summary>

**D.** Loading tools as the agent narrows in cuts tokens and improves selection accuracy, and scoping servers per responsibility removes tools that never belonged (D). A bigger window (C) holds the same noise. One-line descriptions (B) make selection worse. Examples (A) add tokens without reducing the tool count.

</details>

### Question 14

*Integration*

A company assistant answers questions over the document store using a service account that can read every folder, including HR and legal. A contractor asked about salaries and got an answer. What is the root fix?

- **A.** Remove the HR documents from the index, so that the assistant can no longer retrieve them
- **B.** Run retrieval and tools with the calling user's identity and permissions, and log each access
- **C.** Add a system-prompt rule, 'Never discuss salaries', and repeat it at the start of each turn
- **D.** Filter out any response that contains the word 'salary' before it reaches the contractor's screen

<details>
<summary>Answer</summary>

**B.** The shared over-privileged account erased per-user authorization and made every access unattributable, so the fix is acting as the caller (B). C is a probabilistic patch, A breaks legitimate HR use, and D is easy to get around and blocks legitimate answers.

</details>

### Question 15

*Integration*

Engineers search an internal knowledge base with exact error codes such as 'E-4031.' Semantic search returns conceptually similar documents about other errors. What is the best fix?

- **A.** A larger embedding model, which captures the meaning of each individual error code more precisely
- **B.** Hybrid search: keyword matching for exact identifiers plus semantic search, then re-ranking
- **C.** Retrieve more chunks per query, so that the right document is more likely to be included
- **D.** Fine-tune the generation model on the error codes, so that it recognizes each one on sight

<details>
<summary>Answer</summary>

**B.** Exact identifiers such as error codes and SKUs need keyword matching, which hybrid search adds alongside semantic retrieval (B). Better embeddings (A) still treat codes as fuzzy meaning. More chunks (C) add noise. The generation model (D) can't fix documents that were never retrieved.

</details>

### Question 16

*Evaluation, Testing, and Optimization*

A contract-extraction service has three complaints: wrong values, slow responses at peak hours, and a rising monthly bill. Which THREE metrics should the monitoring plan track? (Select THREE)

- **A.** Field-level accuracy against a labeled dataset
- **B.** Average response length
- **C.** p95 and p99 latency
- **D.** Number of prompt revisions per month
- **E.** Cost per document and tokens per task

<details>
<summary>Answer</summary>

**A, C, E.** Each complaint maps to a metric: wrong values to accuracy (A), slowness to tail latency (C), and the bill to cost per unit of work (E). Prompt revision counts (D) and response length (B) measure activity, and neither shows whether the complaints are fixed.

</details>

### Question 17

*Evaluation, Testing, and Optimization*

A team tuned its prompt against the same 200 examples it uses to report accuracy. Testing shows 98%, and production shows 84%. What went wrong, and what is the fix?

- **A.** The eval set leaked into tuning; tune on a development set and report on a held-out set like production
- **B.** The model is too small for the variety in production, so the system should move up a tier
- **C.** Production traffic is lower quality than the test examples, so it should be filtered before the model sees it
- **D.** 200 examples is too few to be reliable, so the team should add 20 more of the same kind

<details>
<summary>Answer</summary>

**A.** Tuning against the test set overfits to it, so the score stops predicting production (A). C blames the data the system has to handle. B changes the model without fixing the measurement. D keeps the same leak with a slightly bigger set.

</details>

### Question 18

*Evaluation, Testing, and Optimization*

A team wants to ship a new prompt, new retrieval settings and a tier change together, because 'it felt better in 15 spot checks.' What is the correct approach?

- **A.** Run 15 more spot checks with a different reviewer to confirm the first impression
- **B.** Ask the stakeholders which version they prefer after a short demo of both versions
- **C.** Test one variable at a time, with a metric and sample size set in advance, and ship on a significant result
- **D.** Ship all three changes together, since the spot checks were positive and it saves a release

<details>
<summary>Answer</summary>

**C.** A clean experiment changes one variable and decides on a metric chosen in advance (C). With three changes at once (D), a win or a loss can't be attributed to anything. Preference (B) and more spot checks (A) are still the feels-better method.

</details>

### Question 19

*Evaluation, Testing, and Optimization*

Traces show the correct policy passages are retrieved, yet answers still state the wrong refund window. Where is the failure, and what is the first fix?

- **A.** Too few passages: raise the number retrieved per question so the model has more to go on
- **B.** The index is stale, so it should be rebuilt from the latest version of every policy document
- **C.** Retrieval: re-chunk and re-embed the whole corpus, so the passages match questions more closely
- **D.** Generation: answer only from the retrieved passages, cite them, and evaluate faithfulness

<details>
<summary>Answer</summary>

**D.** When the right documents arrive and the answer is still wrong, the failure sits in generation and grounding (D). C and B fix retrieval, which the traces show is working. A adds noise to a context that already contains the answer.

</details>

### Question 20

*Evaluation, Testing, and Optimization*

Answers about leave policies leave out exceptions. Traces show the retrieved chunks contain the rule sentence, while the exception sits in the next paragraph, which isn't retrieved. What is the best fix?

- **A.** Retrieve 30 chunks instead of 5, so the paragraph with the exception is more likely to be included
- **B.** Move to a more capable model, which is better at inferring exceptions from the rule sentence
- **C.** Tell the model in the system prompt to remember that most policies have exceptions
- **D.** Re-chunk along the document's structure, with some overlap, so rules and exceptions stay together

<details>
<summary>Answer</summary>

**D.** Chunks smaller than the unit of meaning split rules from their qualifiers, so structure-aware chunking fixes the retrieval unit (D). More chunks (A) might catch the exception along with plenty of noise. No model (B) can use a paragraph it never receives, and an instruction (C) can't supply the missing text.

</details>

### Question 21

*Governance, Safety, and Risk Management*

An agent reads inbound customer emails and can issue refunds. Which TWO controls are deterministic, as opposed to prompt-based? (Select TWO)

- **A.** An output filter that blocks any reply containing a full account number
- **B.** Few-shot examples of the agent declining suspicious requests
- **C.** A system-prompt rule, 'Never issue large refunds', placed at the top of the agent's instructions
- **D.** A persona instruction, 'You are a careful agent', repeated before each tool call
- **E.** Tool permissions that cap a refund at \$100 per call and send larger amounts for human approval

<details>
<summary>Answer</summary>

**A and E.** Permission limits (E) and output filtering (A) are enforced in code, whatever the model decides. C, D and B shape behavior probabilistically, and a cleverly written email can talk the model past them.

</details>

### Question 22

*Governance, Safety, and Risk Management*

A moderation pipeline handles 500,000 low-risk comments a day and occasionally receives legal threats. Which human-in-the-loop design fits?

- **A.** Have a human review every comment before it is published, so nothing slips through
- **B.** Automate routine decisions with sampled QA; send legal threats and low-score cases to reviewers
- **C.** Remove humans from the pipeline entirely, since the comments are low risk on the whole
- **D.** Let the model escalate to a human whenever its self-reported confidence is low

<details>
<summary>Answer</summary>

**B.** Humans go where the risk is high, and sampling covers the routine volume (B). Reviewing everything (A) destroys the efficiency case. C leaves legal threats unhandled. Self-reported confidence (D) is poorly calibrated, so the thresholds that route cases to people have to be set by the system.

</details>

### Question 23

*Governance, Safety, and Risk Management*

A US telehealth company with patients in the US and Germany plans to use Claude to summarize clinical notes. Which TWO frameworks apply? (Select TWO)

- **A.** FedRAMP
- **B.** HIPAA, for US patients' health information
- **C.** GDPR, for the personal data of patients in the EU
- **D.** None, since Claude is a third-party service
- **E.** Only HIPAA, since the company is based in the US

<details>
<summary>Answer</summary>

**B and C.** The framework follows the data type and the jurisdiction: US health data brings HIPAA (B), and processing EU residents' personal data brings GDPR wherever the company is based (C). FedRAMP (A) covers cloud services for US federal agencies. E ignores the German patients, and D confuses using a vendor with being exempt.

</details>

### Question 24

*Governance, Safety, and Risk Management*

Your observability stack stores full prompts and responses, including customer personal data, in a log platform that 300 engineers can read. What is the risk, and what is the fix?

- **A.** Data leakage through logs: redact personal data first, restrict access, and set a retention limit
- **B.** Ask the model in the system prompt to leave personal data out of every one of its responses
- **C.** Encrypt the stored logs at rest and leave the access as it is for the 300 engineers
- **D.** No real risk, because the logs are internal and every one of the 300 engineers works for the company

<details>
<summary>Answer</summary>

**A.** Logs and traces are a leakage channel, so the fix minimizes what's stored and who can see it (A). Internal access (D) still exposes customer data to hundreds of people. Encryption with unchanged access (C) protects the storage while every reader still sees the data. B leaves the personal data in the prompts, and the model can't be relied on to keep it out of responses.

</details>

### Question 25

*Governance, Safety, and Risk Management*

A resume-screening assistant ranks candidates for interviews. An audit finds that applicants from two universities abroad are ranked lower than equally qualified applicants. The candidate pool is balanced, and the system prompt tells the model to favor 'polished communication and familiarity with US business norms.' What is the source of the bias, and the right mitigation?

- **A.** Evaluation design: change the audit's test set until the gap between the groups disappears
- **B.** Data bias: collect more resumes from the two universities so the model sees more of their graduates
- **C.** Prompt framing: use job-related criteria applied identically to everyone, then re-measure by group
- **D.** Model choice: move to a more capable tier, which judges candidates from abroad more fairly

<details>
<summary>Answer</summary>

**C.** The pool is balanced and the prompt itself encodes criteria that disadvantage the group, so the bias comes from prompt framing and the fix is neutral, job-related criteria, checked per group (C). More data (B) treats a data problem the audit didn't find. Changing the test set (A) hides the gap without fixing it. A stronger model (D) follows the same loaded instructions.

</details>

### Question 26

*Stakeholder Communication and Lifecycle Management*

Stakeholders ask for a guarantee that the assistant 'never gives a wrong answer.' What is the appropriate response?

- **A.** Commit only to 99.9% uptime, which the platform can guarantee, and leave accuracy out of the SLA
- **B.** Promise 100% accuracy to secure approval, then work toward it during the first months in production
- **C.** Refuse to set any accuracy target, since no LLM system can promise a specific level of quality
- **D.** Commit to measured targets: accuracy per slice, an error budget, escalation paths, and a remediation plan

<details>
<summary>Answer</summary>

**D.** Probabilistic systems get SLAs built on measured rates, such as at least 96% accuracy per slice on a held-out set, with error budgets, escalation paths and remediation, and stakeholders should hear that LLM outputs have a measurable error rate (D). B sets up a broken promise. C leaves stakeholders nothing to hold the system to. Uptime (A) says nothing about answer quality.

</details>

### Question 27

*Stakeholder Communication and Lifecycle Management*

Which TWO artifacts belong in the handoff to the team that will operate the system? (Select TWO)

- **A.** Eval baselines and an inventory of prompts and their versions
- **B.** The architect's personal working notes from the design phase
- **C.** A raw export of the project chat channel from start to finish
- **D.** Runbooks covering escalation paths and known failure modes
- **E.** The kickoff slide deck that set out the project's goals and scope

<details>
<summary>Answer</summary>

**A and D.** Operators need to know how to respond to problems (D) and what normal looks like, along with what is deployed (A). Personal notes (B), kickoff slides (E) and raw chat (C) aren't operational documentation.

</details>

### Question 28

*Developer Productivity and Operational Enablement*

Claude Code runs in your CI pipeline, and the team agrees it must never run git push or curl anywhere the repository is used. Where should this restriction live?

- **A.** A wiki page listing the commands that Claude Code must never run in any pipeline
- **B.** Each developer's `~/.claude/settings.json`, set up during onboarding for the team
- **C.** Deny rules in the committed project settings, such as `Bash(git push *)` and `Bash(curl *)`
- **D.** A `CLAUDE.md` instruction at the top of the repository saying never to run git push or call curl

<details>
<summary>Answer</summary>

**C.** Permission rules in version-controlled project settings apply everywhere the repository runs, CI included, and the client enforces them (C). User settings (B) don't reach CI or other developers. `CLAUDE.md` (D) is guidance the model weighs. A wiki (A) is invisible to the tooling.

</details>

### Question 29

*Developer Productivity and Operational Enablement*

A platform team built a code-review subagent and a release-notes skill that every repository in the company should use, in the same version. What is the best way to distribute them?

- **A.** Post the prompt text in a chat channel for developers to copy into their own setups
- **B.** Package them as a plugin, or deploy them through managed settings, so everyone gets one version
- **C.** Paste both definitions into every repository's `CLAUDE.md`, so each project carries them
- **D.** Ask each developer to copy the files into their own `~/.claude/` folder during onboarding

<details>
<summary>Answer</summary>

**B.** Plugins bundle skills and subagents for distribution, and managed settings can push them to the whole organization, which keeps one maintained version (B). Copy-and-paste distribution (A, D) drifts as soon as the originals change. `CLAUDE.md` (C) holds always-on instructions and can't define a subagent or an on-demand skill.

</details>

### Question 30

*Developer Productivity and Operational Enablement*

A team adopting Claude Code configured its repository so that pull requests written by Claude merge automatically once CI passes. A production incident traces back to one of those merges, and nobody on the team can explain the change. Which control restores human ownership of the code?

- **A.** Require a named human reviewer to approve every pull request, AI-written ones included
- **B.** Have a second Claude session review each pull request before it merges into the main branch
- **C.** Raise the test coverage threshold for AI-written pull requests before they can merge
- **D.** Label AI-written pull requests so that they are easy to find after any later incident

<details>
<summary>Answer</summary>

**A.** Ownership means a person approves and answers for each change before it merges (A). An AI reviewer (B) adds a check without adding accountability. More coverage (C) catches more defects but still leaves nobody owning the change. A label (D) helps after an incident and does nothing before one.

</details>

---

## Where to go next

- **Review by domain.** If your misses cluster, re-read those domains in Part II of the [CCAR-P study guide](./guide.md):
  - [Solution Design and Architecture](./guide.md#domain-1-solution-design-and-architecture-18)
  - [Claude Models, Prompting, and Context Engineering](./guide.md#domain-2-claude-models-prompting-and-context-engineering-13)
  - [Integration](./guide.md#domain-3-integration-21)
  - [Evaluation, Testing, and Optimization](./guide.md#domain-4-evaluation-testing-and-optimization-17)
  - [Governance, Safety, and Risk Management](./guide.md#domain-5-governance-safety-and-risk-management-16)
  - [Stakeholder Communication and Lifecycle Management](./guide.md#domain-6-stakeholder-communication-and-lifecycle-management-7)
  - [Developer Productivity and Operational Enablement](./guide.md#domain-7-developer-productivity-and-operational-enablement-8)
- **Practice at full length.** The [CCAR-P page on Preporato](https://preporato.com/certificates/claude-certified-architect-professional) has free sample questions and full-length timed practice tests (paid) in the exam's format, with a score for every domain.

Found a mistake in a question? [Open an issue](https://github.com/preporato/claude-certification-guide/issues/new?template=outdated-fact.yml) and we'll fix it.

*These questions were written for this repo and are not taken from the exam. Not affiliated with Anthropic.*
