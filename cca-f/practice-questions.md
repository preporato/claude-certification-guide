# CCA-F practice questions

30 practice questions for **Claude Certified Architect - Foundations** (CCA-F), written for this repo and spread across the exam's five domains by their official weights. 7 of them ask for more than one answer, as some of the real exam's questions do (each item says how many to pick); those count only when every choice is right.

The first 8 questions are grouped under two practice scenarios written for this repo, the way the real exam groups its questions; the exam itself presents four of the six scenarios in its official guide, picked at random.

Choose your answer before you open the explanation.

**Want a timed run?** The [CCA-F page on Preporato](https://preporato.com/certificates/claude-certified-architect) has free sample questions and full-length timed practice tests in the exam's format, with a score for every domain.

| Domain | Exam weight | Questions here |
|---|---|---|
| Agentic Architecture & Orchestration | 27% | 8 |
| Tool Design & MCP Integration | 18% | 5 |
| Claude Code Configuration & Workflows | 20% | 6 |
| Prompt Engineering & Structured Output | 20% | 6 |
| Context Management & Reliability | 15% | 5 |

---

## Scenario 1: Retail support coordinator

> A retailer's support system uses a coordinator agent that receives each customer conversation and delegates to three subagents: an order-lookup agent with read-only order tools, a refund agent that can issue refunds, and a policy agent that searches the returns-policy knowledge base. Company policy: refunds above \$250 need a human's approval, and customers can come back to an open conversation within 7 days.

### Question 1

*Agentic Architecture & Orchestration*

The refund agent needs the order total, the purchase date and the customer's stated reason to decide eligibility. What should the coordinator include when it delegates the task?

- **A.** An instruction for the refund agent to ask the customer to repeat the details of the order
- **B.** The full raw transcript plus every earlier tool output, so that the refund agent misses nothing at all in its decision
- **C.** The specific facts it needs, written into the delegation prompt: order id, total, purchase date, stated reason
- **D.** Nothing extra, because subagents can read the coordinator's conversation history directly

<details>
<summary>Answer</summary>

**C.** Subagents in a hub-and-spoke design start with their own context window and see only what the coordinator passes to them, so C is the working design: the minimum necessary context, stated explicitly. D assumes an inheritance that doesn't exist. B spends tokens and attention on material the decision doesn't need, which is where lost-in-the-middle errors start. A makes the customer pay for a gap the coordinator could close with facts it already has.

</details>

### Question 2

*Context Management & Reliability*

Which TWO events should trigger a handoff to a human agent? (Select TWO)

- **A.** Answering the customer's question takes three tool calls
- **B.** The customer asks to speak to a person
- **C.** The model reports a confidence score of 0.62 on its eligibility decision
- **D.** The customer writes in capital letters and says they are furious about a covered \$90 refund
- **E.** The customer requests a \$400 refund for an order the policy covers

<details>
<summary>Answer</summary>

**B and E.** An explicit request for a human (B) is a standing escalation trigger, and the \$400 refund (E) crosses the \$250 approval threshold, which makes the handoff mandatory under policy. Sentiment alone (D) is no trigger when the request sits inside clear policy; the agent can resolve it while acknowledging the frustration. Self-reported confidence (C) is poorly calibrated and makes an unreliable trigger. Task complexity (A) is the agent's job.

</details>

### Question 3

*Tool Design & MCP Integration*

The policy agent's knowledge-base search sometimes fails because the search service times out, and sometimes finds nothing because no policy covers the case. Both situations currently return an empty list. How should the tool respond instead?

- **A.** Keep returning an empty list in both cases, and let the agent keep retrying the search until a result finally comes back
- **B.** A structured error for the timeout (type, retryable: true, what was tried), and a successful empty result for no match
- **C.** Return the closest-matching policy in both cases, so that the agent always has something it can cite
- **D.** Raise an exception in both cases, so that the coordinator ends the conversation and a person follows up

<details>
<summary>Answer</summary>

**B.** B separates a transient failure from a valid empty result, and the two need different recovery: retry the search, or tell the customer no policy applies. With A, the agent can't tell an outage from a real answer and may report that no policy covers the case during an outage. D ends conversations over a recoverable timeout. C invents relevance, which leads the agent to cite a policy that doesn't apply.

</details>

### Question 4

*Agentic Architecture & Orchestration*

A customer returns four days later to continue a conversation about a pending refund. Separately, a supervisor wants to test a different resolution on a copy of that conversation without changing what the customer sees. Which pairing fits?

- **A.** Start fresh sessions for both, and paste the last assistant message into each one's system prompt to carry the context
- **B.** Fork the session for the customer, and resume the original session for the supervisor's experiment
- **C.** Resume the same session for both, so that the customer and the supervisor see the same history
- **D.** Resume the customer's session to restore the full history, and fork a separate copy for the supervisor

<details>
<summary>Answer</summary>

**D.** Resuming continues a session with its history intact, which is what the returning customer needs. Forking creates an independent branch from the same history, and changes in the fork never flow back, which is what the supervisor needs. D matches both. B swaps the two. C lets the supervisor's experiment change the customer's conversation. A throws away most of the context and relies on one message to carry it.

</details>

## Scenario 2: Nightly multi-repository audit

> A security team runs a nightly audit across 40 repositories. A coordinator spawns one scanner subagent per repository. Each scanner has `Read`, `Grep` and `Glob` plus a dependency-check tool. The coordinator merges the findings into one report for the morning stand-up and opens tickets for new critical issues.

### Question 5

*Agentic Architecture & Orchestration*

Which execution pattern fits the scanning stage and the report stage?

- **A.** Fan out the 40 independent scans in parallel, then one merge step builds the report from normalized results
- **B.** Run the scans in parallel, then several report writers in parallel, and concatenate their outputs
- **C.** Use one agent that scans all 40 repositories in a single context so it can spot cross-repository patterns
- **D.** Scan sequentially so each scanner can learn from the previous one's findings, then write the report in parallel sections

<details>
<summary>Answer</summary>

**A.** Independent work runs in parallel and dependent work runs in sequence, so the hybrid in A matches the data dependencies: the scans don't need each other, and the report needs all of them. D serializes independent work and slows the audit for no gain. C pushes 40 repositories into one context, which degrades attention and turns one failure into a total failure. B produces a report with no single view of the findings, which is what the merge step exists for.

</details>

### Question 6

*Context Management & Reliability*

Last night the audit crashed at repository 27. The rerun started again from repository 1 and opened duplicate tickets for findings already reported. Which TWO changes fix this? (Select TWO)

- **A.** Checkpoint progress to a manifest (repositories done, pending, results so far) and resume from it after a crash
- **B.** Give the scanners larger context windows, so that they remember everything that happened in the previous night's run
- **C.** Run the audit weekly instead of nightly
- **D.** Make ticket creation idempotent, keyed by repository and finding id, so a replay can't create duplicates
- **E.** Ask the coordinator at startup which repositories it had already finished before the crash last night

<details>
<summary>Answer</summary>

**A and D.** A manifest (A) lets the restarted coordinator continue from repository 27, and idempotent side effects (D) make any replayed step harmless; together they turn a crash into a delay. Context windows (B) don't survive a process crash, and the coordinator has no memory of the previous run to ask about (E), because the API is stateless. Running less often (C) leaves the failure in place.

</details>

### Question 7

*Tool Design & MCP Integration*

An engineer proposes giving every scanner the full tool set, including `Write`, `Bash` and the ticketing tool, 'in case they need it.' What is the best response?

- **A.** Replace the scanner tools with Bash alone, since Bash can do everything the other tools do
- **B.** Give the scanners every tool, and add a system-prompt rule that forbids them from writing anything
- **C.** Keep each scanner on the read-only tools its job needs, and let only the coordinator open tickets
- **D.** Accept the proposal, because more tools make the scanners more capable of handling unusual repositories

<details>
<summary>Answer</summary>

**C.** Least privilege scopes each agent to what its responsibility requires. C also keeps tool selection accurate and stops a misbehaving scanner from changing code or opening tickets. D widens the blast radius and adds selection noise for capabilities nobody uses. B relies on a probabilistic instruction to restrain a capability that should never be there. A hands the scanners the broadest tool of all.

</details>

### Question 8

*Context Management & Reliability*

The morning report said 'No critical issues found across all repositories.' The team later learns that six scanners hit their token budgets and skipped their largest files. What should the report format have required?

- **A.** Nothing in the report; the scanners needed a more capable model to finish within their budgets
- **B.** A longer narrative summary from each scanner, describing in detail what it looked at and what it concluded
- **C.** A confidence score from each scanner, shown next to its findings in the merged report
- **D.** A coverage annotation from every scanner (files reviewed, files skipped and why) carried into the report

<details>
<summary>Answer</summary>

**D.** Without explicit coverage, 'no issues found' can't be told apart from 'no issues found in the part that ran.' D makes the gap visible so the skipped files can be queued for a focused pass. Self-reported confidence (C) is poorly calibrated and says nothing about what was skipped. A longer summary (B) adds words without the counts. A stronger model (A) can still hit a budget, and the report would still hide it.

</details>

## Standalone questions

### Question 9

*Agentic Architecture & Orchestration*

After the first tool call, every follow-up request in your agent loop fails with a 400 error. Here is how the loop builds the next request. What is wrong?

```python
response = client.messages.create(model=MODEL, max_tokens=1024,
                                  tools=tools, messages=messages)
if response.stop_reason == "tool_use":
    call = next(b for b in response.content if b.type == "tool_use")
    result = run_tool(call.name, call.input)
    messages.append({"role": "user", "content": [{
        "type": "tool_result",
        "tool_use_id": call.id,
        "content": result,
    }]})
```

- **A.** The loop should set `tool_choice` to `any` after the first call, so the model keeps using tools
- **B.** The assistant turn with the `tool_use` block is never appended, so the `tool_result` has no matching call
- **C.** `tool_result` blocks belong in the system prompt, where the model reads them before it reads any of the messages
- **D.** `max_tokens` is too low for a tool loop, so the second request runs out of room for its result

<details>
<summary>Answer</summary>

**B.** The API is stateless, so each request must carry the whole exchange: the assistant message with the `tool_use` block comes first, then the user message with the matching `tool_result` (B). Without it, the `tool_use_id` points at nothing. C misplaces tool results, which go in a user turn. D and A change settings that have nothing to do with a malformed history.

</details>

### Question 10

*Agentic Architecture & Orchestration*

Your research agent uses the server-side web search tool. Some responses come back with `stop_reason` `pause_turn`, and the loop treats them as finished, returning half-done research. What is the correct handling?

- **A.** Send a follow-up request with the paused response appended as-is, so Claude continues the server-side work
- **B.** Raise `max_tokens` and send the original request again, so the search finishes in one response
- **C.** Treat `pause_turn` the same as `end_turn`, since the paused response already contains the search results it found
- **D.** Run the web search locally and return a `tool_result` for it, so the loop can move to the next step

<details>
<summary>Answer</summary>

**A.** `pause_turn` means a server-side tool loop reached its iteration limit mid-task. The documented handling is A: return the response as the latest assistant turn, and Claude picks up where it stopped. C is the bug in the question. D treats a server tool like a client tool; there is no `tool_use` for your code to answer. B restarts the work and pays for it twice.

</details>

### Question 11

*Agentic Architecture & Orchestration*

A team answers one-line FAQ questions from a two-page policy with a six-subagent pipeline: retriever, reader, drafter, tone checker, fact checker and formatter. Answers take 25 seconds and cost far more than expected. What is the best change?

- **A.** Collapse it to one model call with the policy in context, plus a light validation step if needed
- **B.** Move every subagent to the most capable model, to cut the retries that slow the pipeline down
- **C.** Run the six subagents in parallel under a coordinator, so that the steps no longer wait on each other
- **D.** Cache each subagent's output, so that repeated questions skip the whole pipeline

<details>
<summary>Answer</summary>

**A.** This is over-decomposition: the task is small, single-domain and fits in one context, so the subagents add orchestration cost without any isolation benefit, and A removes the overhead. Parallelizing (C) doesn't fit a chain where each step needs the previous step's output. B raises the cost of a design that shouldn't exist. D helps only with repeated identical questions and leaves the latency of the chain in place.

</details>

### Question 12

*Agentic Architecture & Orchestration*

A payments service's error rate spiked. The cause could be in code, configuration, infrastructure or a third-party API, and what to check next depends on what each check finds. How should the coordinator decompose the investigation?

- **A.** One prompt asking Claude for the root cause, with the error-rate graph attached
- **B.** A fixed pipeline that runs the four checks in a set order, from the code through to the third-party API at the end
- **C.** Dynamic decomposition: plan next steps from each finding, with a token budget and iteration cap in code
- **D.** Run every conceivable check in parallel, with no coordinator, so that nothing is missed

<details>
<summary>Answer</summary>

**C.** Open-ended investigations, where the next step depends on what you just learned, call for dynamic decomposition. Because that pattern costs more and can wander, C pairs it with limits enforced outside the model. A fixed pipeline (B) suits workflows that are known in advance. D wastes effort and leaves nobody to connect the findings. A asks for an answer without giving the model any way to gather evidence.

</details>

### Question 13

*Agentic Architecture & Orchestration*

Long research tasks sometimes use ten times the expected tokens. Which TWO belong in a reliable token-budget design? (Select TWO)

- **A.** Setting `max_tokens` to 50 on every call
- **B.** Asking Claude each turn how many tokens it has used so far
- **C.** A system-prompt instruction asking Claude to keep each research task under 50,000 tokens in total
- **D.** Track cumulative input and output tokens from each response's usage field inside the loop
- **E.** Stop the loop in code when the budget is reached, with a wrap-up instruction at about 80% of it

<details>
<summary>Answer</summary>

**D and E.** Budgets are enforced from outside the model: measure from the usage field (D) and act on the measurement with a soft warning and a hard stop (E). An instruction (C) and the model's own estimate (B) are probabilistic and unmeasured. A tiny `max_tokens` (A) truncates every response, so turns end at the cap before they finish.

</details>

### Question 14

*Tool Design & MCP Integration*

A team's MCP server should (1) let Claude create Jira tickets, (2) expose the team's API schema files so a user can attach them as context, and (3) provide a reusable 'triage this incident' template with the team's severity rubric. Which MCP primitives fit, in that order?

- **A.** Tool, tool, tool
- **B.** Resource, tool, prompt
- **C.** Prompt, resource, tool
- **D.** Tool, resource, prompt

<details>
<summary>Answer</summary>

**D.** Creating a ticket is an action, so it's a tool. Schema files are read-only data for the client to browse and attach, so they're a resource. The packaged triage template is a prompt. D matches action, data and know-how in that order. A turns data and a template into callable functions. B and C put the action in the wrong primitive.

</details>

### Question 15

*Tool Design & MCP Integration*

Every developer on a team should get the same internal MCP server in Claude Code, and the server needs an API token. Which TWO choices are correct? (Select TWO)

- **A.** Put the token in `CLAUDE.md` so Claude can pass it to the server
- **B.** Paste the raw token into `.mcp.json`, so that setup is a single step for every developer on the team
- **C.** Define the server in the project's `.mcp.json` and commit it to the repository
- **D.** Reference the token as `${INTERNAL_API_TOKEN}` in `.mcp.json`, set by each developer in their environment
- **E.** Have each developer add the server with local scope by following a wiki page

<details>
<summary>Answer</summary>

**C and D.** Project scope (C) is the configuration that reaches the whole team through version control, and environment variable expansion (D) keeps the secret out of the repository. B commits a credential. E relies on every developer repeating a manual step, and local scope never propagates. A puts a secret into the model's context, where it can leak through outputs or logs.

</details>

### Question 16

*Tool Design & MCP Integration*

When users ask to change their email address, Claude often calls `get_customer` instead of `update_customer`, then tells the user the change is done. Both tools exist. What is the first fix?

- **A.** Add a system-prompt line telling Claude to use `update_customer` whenever a user asks for an update
- **B.** Rewrite both descriptions: what each does, when to use it, when to use the other, with `get_customer` read-only
- **C.** Rename `get_customer` to `fetch_customer`, so that its name no longer sounds like it could change a customer record
- **D.** Remove `get_customer` from the agent, so that `update_customer` is the only customer tool left

<details>
<summary>Answer</summary>

**B.** Claude selects tools mainly from their descriptions, so overlapping or vague descriptions are the first thing to fix (B), and the boundary statements ('to change a record, use `update_customer`') are what resolve this confusion. A rename (C) changes little while the descriptions stay vague. A system-prompt patch (A) is weaker than fixing the routing signal itself. Removing the read tool (D) breaks every legitimate lookup.

</details>

### Question 17

*Claude Code Configuration & Workflows*

Your team wants every file Claude edits to be formatted with Prettier immediately after each edit, for everyone working in the repository. Which configuration does that?

- **A.** A `PostToolUse` hook in each developer's own `~/.claude/settings.json` that runs Prettier
- **B.** A `CLAUDE.md` line, 'Run Prettier after every edit', committed so the whole team gets it
- **C.** A `PostToolUse` hook matching `Edit|Write` in the committed `.claude/settings.json`, running Prettier
- **D.** A `PreToolUse` hook on `Edit` in the committed `.claude/settings.json` that runs Prettier on the file

<details>
<summary>Answer</summary>

**C.** Formatting has to run after the file changes, which is `PostToolUse`, and the committed project settings file shares the hook with the whole team, so C covers both requirements. D runs before the edit exists. B is guidance Claude may skip, while a hook runs every time. A works only for developers who set it up themselves.

</details>

### Question 18

*Claude Code Configuration & Workflows*

A team requires that Claude never ends its work while the test suite is failing. Which hook enforces this?

- **A.** A `SessionEnd` hook that runs the test suite and prints any failures to stderr as the session is closing
- **B.** A `Stop` hook that runs the tests and, when any fail, exits with code 2 and prints them to stderr
- **C.** A `PostToolUse` hook that runs the whole test suite after every file that Claude reads
- **D.** A `UserPromptSubmit` hook that runs the tests before each prompt reaches Claude

<details>
<summary>Answer</summary>

**B.** Exit code 2 from a `Stop` hook prevents Claude from stopping and feeds the stderr text back, so Claude keeps working on the failures (B). `SessionEnd` (A) fires as the session closes and can't block anything. D tests before the work happens. C runs constantly at the wrong moment and can't stop Claude from finishing.

</details>

### Question 19

*Claude Code Configuration & Workflows*

A `PostToolUse` hook on `Write` scans each file Claude writes. It finds an API key in a file Claude just wrote and exits with code 2. What happens?

- **A.** The file is already written; Claude receives the hook's stderr message and can act on it
- **B.** Claude Code shuts down the session, because a secret was written to the repository
- **C.** Nothing happens, because exit code 2 is ignored for `PostToolUse` hooks on `Write`
- **D.** The write is cancelled and the file is never created, and Claude receives the hook's message

<details>
<summary>Answer</summary>

**A.** `PostToolUse` fires after the tool has run, so it can't undo the write; exit code 2 shows its stderr to Claude (A). To stop the write itself, the check belongs in a `PreToolUse` hook, where exit code 2 blocks the call, which is the behavior D describes. B and C describe behaviors that don't exist.

</details>

### Question 20

*Claude Code Configuration & Workflows*

A developer asks Claude Code to migrate 40 files from a callback-based API client to async/await. The change touches shared types, and there are two reasonable migration strategies. What is the best way to start?

- **A.** One prompt for the whole change, then a careful review of the final diff across all 40 files
- **B.** Direct execution, file by file, fixing each problem as it appears and running the tests as it goes
- **C.** A `CLAUDE.md` rule saying 'use async/await', so Claude converts each file it touches
- **D.** Plan Mode: Claude explores the codebase and proposes a migration plan to review before any change

<details>
<summary>Answer</summary>

**D.** Multi-file, cross-cutting changes with more than one valid approach are Plan Mode's case (D): the strategy gets agreed before 40 files move. B and A commit to an approach before anyone has compared the options, and a wrong choice is expensive to unwind. C states a preference without planning the migration.

</details>

### Question 21

*Claude Code Configuration & Workflows*

A team's dependency-audit skill prints thousands of lines of output, and teammates complain it floods the main conversation. Which frontmatter change fixes this?

- **A.** `context: fork`, so the skill runs in an isolated subagent and returns its result
- **B.** `disable-model-invocation: true`, so the skill only runs when someone calls it
- **C.** `allowed-tools: Read`, so the skill can only read files while it runs
- **D.** `model: haiku`, so the skill's work is done by a faster, cheaper model

<details>
<summary>Answer</summary>

**A.** `context: fork` (A) runs the skill in its own subagent context, so the verbose work stays out of the main conversation. B only stops Claude from invoking the skill automatically; the output still floods the conversation whenever someone runs it. C changes which tools are pre-approved and D changes the model, and neither moves the output.

</details>

### Question 22

*Claude Code Configuration & Workflows*

In a monorepo, files under `services/payments/` follow strict rules (all amounts in integer cents, no floats). The rules confuse Claude when it works on the frontend. Which TWO placements load these rules only when Claude works in the payments code? (Select TWO)

- **A.** A section titled 'Payments only' in the root `CLAUDE.md`
- **B.** A `CLAUDE.md` file inside `services/payments/`
- **C.** A file in `.claude/rules/` with `paths: ["services/payments/**"]` in its frontmatter
- **D.** Each developer's `~/.claude/CLAUDE.md`
- **E.** The project's `.mcp.json`

<details>
<summary>Answer</summary>

**B and C.** A path-scoped rule (C) loads when Claude reads or edits a matching file, and a subdirectory `CLAUDE.md` (B) loads on demand when Claude works with files in that directory. The root `CLAUDE.md` (A) loads in every session, frontend work included. D is personal and reaches nobody else. E configures MCP servers and holds no instructions.

</details>

### Question 23

*Prompt Engineering & Structured Output*

A code-review prompt says 'Be thorough but avoid nitpicks.' Reviews flag style issues inconsistently and miss SQL injection. Which rewrite fixes the cause?

- **A.** 'You are a world-class senior security engineer reviewing production code for a large bank.'
- **B.** 'Be extremely thorough, never miss anything, and comment on every issue you see, however small it seems.'
- **C.** 'Be conservative with your comments, and only raise issues that a senior reviewer would raise.'
- **D.** 'Report only SQL injection, XSS, authentication bypass and secrets in code, at high or critical severity; skip formatting and naming.'

<details>
<summary>Answer</summary>

**D.** Vague instructions produce inconsistent behavior because the model has to guess the threshold. D names the categories, the severity floor and the exclusions, and anyone reading a review can check whether it followed them. B and C push the same vague guidance in two directions. A role line (A) without criteria leaves the same guesswork.

</details>

### Question 24

*Prompt Engineering & Structured Output*

A classifier should flag support tickets that mention a physical safety risk. In testing it flags every ticket containing the word 'fire', including 'firewall rules reset after update.' What is the best few-shot improvement?

- **A.** An instruction in the prompt: 'Don't be fooled by keywords; read the whole ticket and judge the actual risk first.'
- **B.** Two to four examples: the firewall ticket labeled not-safety with a reason, a real safety ticket, an ambiguous one
- **C.** Twenty examples of genuine safety tickets, so the model sees many cases of what to flag
- **D.** A higher effort level, so the model thinks harder about each ticket before labeling it

<details>
<summary>Answer</summary>

**B.** Few-shot examples teach reasoning and edge cases best when they include something the model should leave alone, so the tricky negative in B is the example that matters. C piles on positives and teaches nothing about the false positives. A is vague guidance. More effort (D) leaves the misunderstanding in place, because nothing shows the model where the boundary is.

</details>

### Question 25

*Prompt Engineering & Structured Output*

Your team plans to use structured outputs (a JSON schema in `output_config.format`) for invoice extraction. Which TWO statements about this feature are true? (Select TWO)

- **A.** It also guarantees that every extracted value is correct for the source document it came from
- **B.** It works only when `tool_choice` forces a specific tool
- **C.** It removes the need to validate business rules in your own code, such as totals matching the line items
- **D.** Constrained decoding makes the response valid JSON that matches the schema's structure and types
- **E.** A refusal or a `max_tokens` cutoff can still produce output that doesn't match the schema, so check `stop_reason`

<details>
<summary>Answer</summary>

**D and E.** Structured outputs guarantee format: valid, schema-compliant JSON (D), with the documented exceptions of refusals and truncation (E). Format says nothing about whether the values are right, so semantic checks such as totals and dates stay in your pipeline, which rules out A and C. B confuses the feature with forced tool use; structured outputs are requested through `output_config.format`.

</details>

### Question 26

*Prompt Engineering & Structured Output*

An extraction fails validation because `invoice_date` came back as 2026-04-31, a date that doesn't exist. What should the retry request contain?

- **A.** The failed output and the words 'try again', so the model knows its first answer was rejected
- **B.** The original document again with no other changes, since the model gets the date right on most of its other attempts
- **C.** The original document, the failed output, and the specific error, with an instruction to correct only that field
- **D.** The same request sent to a more capable model, which is less likely to produce an invalid date

<details>
<summary>Answer</summary>

**C.** A useful retry tells the model exactly what failed ('`invoice_date` 2026-04-31 is not a valid date') and gives it the source to fix it against (C). B repeats the conditions that produced the error. A removes the source the model needs to correct the date. D changes the model without telling it what went wrong.

</details>

### Question 27

*Prompt Engineering & Structured Output*

A product team wants to move its live chat assistant to the Message Batches API to cut costs in half. What is the right assessment?

- **A.** Reject it, because batch requests can't include a system prompt or the conversation history
- **B.** Approve it: users get the same quality at half the price, and the savings fund other features
- **C.** Approve it, provided the app polls for results every second so replies appear without delay
- **D.** Reject it: batches have no latency guarantee (up to 24 hours), so cut costs with caching or a cheaper tier

<details>
<summary>Answer</summary>

**D.** The batch discount comes with asynchronous processing and no latency guarantee, which rules it out for anyone waiting on an answer: most batches finish within an hour, but some take up to 24 (D). B ignores the latency. Polling (C) doesn't speed up processing. A is false: batch requests take the same parameters as regular Messages requests.

</details>

### Question 28

*Prompt Engineering & Structured Output*

One prompt asks Claude to extract 30 fields from a contract, normalize every currency, classify the risk clauses and write an executive summary. Results vary from run to run, and errors are hard to trace. What is the best restructuring?

- **A.** A chain of focused prompts (extract, validate, normalize, classify, summarize), each with its own checks
- **B.** The same single prompt on a more capable model, which can hold all four jobs in mind at once
- **C.** Ask for the executive summary first, then the fields, so the summary frames the extraction
- **D.** The same single prompt with each requirement marked IMPORTANT in capitals, so that none of the four jobs is skipped

<details>
<summary>Answer</summary>

**A.** Prompt chaining gives each stage one job and a validation point, so a failure shows up in the stage that caused it (A). Emphasis (D) doesn't reduce the number of jobs in one prompt. A stronger model (B) may help a little and leaves errors untraceable. Reordering (C) builds the summary on fields nobody has checked yet.

</details>

### Question 29

*Context Management & Reliability*

A knowledge-base Q&A agent receives 40 retrieved passages per question. The passage with the answer usually lands near the middle, and answers often miss it. Which TWO changes address this? (Select TWO)

- **A.** Retrieve 80 passages instead of 40, so the answer is never left out
- **B.** Re-rank the passages and pass only the most relevant few
- **C.** Raise the effort level so the model reads each passage more carefully
- **D.** Put the passages first and the question and instructions at the end
- **E.** Switch to a model with a larger context window for the passages

<details>
<summary>Answer</summary>

**B and D.** Attention is weakest in the middle of long contexts, so the fixes shrink the middle and move what matters to the edges: fewer, better passages (B), and long material first with the question last, which Anthropic's long-context guidance recommends (D). A bigger window (E) and more passages (A) make the middle longer. More effort (C) changes how much the model reasons and does nothing about where the answer sits.

</details>

### Question 30

*Context Management & Reliability*

Two internal documents disagree about the warranty period: a 2024 policy says 12 months and a 2026 update says 24 months. What should the agent's answer do?

- **A.** Decline to answer until someone in the policy team fixes the conflicting documents
- **B.** State 24 months without mentioning the conflict, because the newer document always takes precedence over the older one
- **C.** Answer with attribution: both values, their documents and dates, the newer one as likely current, and a flag
- **D.** Average the two values and state 18 months, so the answer reflects both of the documents

<details>
<summary>Answer</summary>

**C.** Provenance keeps each claim tied to its source and flags the conflict for review instead of settling it silently (C). Silently picking one value (B) is the tested anti-pattern even when the choice happens to be right, because nobody learns that the documents disagree. D produces a number neither source supports. A withholds an answer the agent can give with a caveat.

</details>

---

## Where to go next

- **Review by domain.** If your misses cluster, re-read those domains in Part II of the [CCA-F study guide](./guide.md):
  - [Agentic Architecture & Orchestration](./guide.md#domain-1-agentic-architecture--orchestration-27)
  - [Tool Design & MCP Integration](./guide.md#domain-2-tool-design--mcp-integration-18)
  - [Claude Code Configuration & Workflows](./guide.md#domain-3-claude-code-configuration--workflows-20)
  - [Prompt Engineering & Structured Output](./guide.md#domain-4-prompt-engineering--structured-output-20)
  - [Context Management & Reliability](./guide.md#domain-5-context-management--reliability-15)
- **Practice at full length.** The [CCA-F page on Preporato](https://preporato.com/certificates/claude-certified-architect) has free sample questions and full-length timed practice tests (paid) in the exam's format, with a score for every domain.

Found a mistake in a question? [Open an issue](https://github.com/preporato/claude-certification-guide/issues/new?template=outdated-fact.yml) and we'll fix it.

*These questions were written for this repo and are not taken from the exam. Not affiliated with Anthropic.*
