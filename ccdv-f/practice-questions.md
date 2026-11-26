# CCDV-F practice questions

30 practice questions for **Claude Certified Developer - Foundations** (CCDV-F), written for this repo and spread across the exam's eight domains by their official weights. 7 of them ask for more than one answer, as some of the real exam's questions do (each item says how many to pick); those count only when every choice is right.

Choose your answer before you open the explanation.

**Want a timed run?** The [CCDV-F page on Preporato](https://preporato.com/certificates/claude-certified-developer-foundations) has free sample questions and full-length timed practice tests in the exam's format, with a score for every domain.

| Domain | Exam weight | Questions here |
|---|---|---|
| Agents and Workflows | 17% | 5 |
| Applications and Integration | 20% | 6 |
| Claude Code | 8% | 2 |
| Eval, Testing, and Debugging | 10% | 3 |
| Model Selection and Optimization | 12% | 4 |
| Prompt and Context Engineering | 15% | 4 |
| Security and Safety | 8% | 3 |
| Tools and MCP | 10% | 3 |

---

### Question 1

*Agents and Workflows*

A team wants an autonomous agent to convert CSV exports into a fixed JSON layout. The column mapping never changes. What is the best approach?

- **A.** A manager agent with three subagents that each convert a third of the columns
- **B.** An orchestration framework with a state graph that tracks each file's progress
- **C.** An Agent SDK agent with file tools, so that it can read each export and write out the JSON
- **D.** A deterministic script, or one model call with a schema where a field needs interpretation

<details>
<summary>Answer</summary>

**D.** Apply the four-question test: the task isn't complex, its path is fully known, and code can avoid errors cheaply, so autonomy only adds cost and unpredictability (D). C, A and B each add machinery the problem doesn't need.

</details>

### Question 2

*Agents and Workflows*

Which TWO things does the Claude Agent SDK give you that you would otherwise build yourself in a custom loop? (Select TWO)

- **A.** A hosted vector database for retrieval over your project's own documents
- **B.** A visual drag-and-drop designer for building the agent's workflow
- **C.** Automatic fine-tuning of the model on your agent's traces
- **D.** The agent loop with built-in tools for files, shell commands and search
- **E.** Context management, plus hooks and permissions for deterministic control

<details>
<summary>Answer</summary>

**D and E.** The Agent SDK packages the same harness Claude Code runs on: the loop and built-in tools (D), plus context management, hooks, permissions and subagents (E). It doesn't host a vector database (A), fine-tune models (C) or provide a visual designer (B).

</details>

### Question 3

*Agents and Workflows*

A bank's agent must keep all code execution and data inside its own network for data-residency rules. A startup wants the fastest path to production. Which deployment fits each?

- **A.** Self-hosted for both
- **B.** Self-hosted for the bank, managed for the startup
- **C.** Managed for the bank, self-hosted for the startup
- **D.** Managed for both

<details>
<summary>Answer</summary>

**B.** Residency and custom-runtime requirements point to self-hosted execution, and speed to production points to a managed deployment where the provider runs the loop and the sandbox (B). D puts the bank's data outside its network. A slows the startup down for a requirement it doesn't have. C reverses both.

</details>

### Question 4

*Agents and Workflows*

An agent must summarize 12 long PDFs independently, then write a comparison across them. The single-agent version runs out of context. What is the best design?

- **A.** One agent reads all 12 PDFs in sequence in a single context, summarizing each one before moving to the next
- **B.** Raise `max_tokens` on the single agent so it has room for all twelve summaries and the comparison
- **C.** Give each PDF to a parallel subagent with its own context, and compare their summaries in an orchestrator
- **D.** Twelve agents, one per PDF, that send their findings to each other directly and agree on the comparison

<details>
<summary>Answer</summary>

**C.** The summaries are independent subtasks, so isolated subagent contexts fit, and only compact reports return to the orchestrator (C). A is the design that already failed. `max_tokens` (B) limits output, and the problem is input. Agents talking to each other directly (D) remove the coordinator that merges results and isolates failures.

</details>

### Question 5

*Agents and Workflows*

A coding agent built on the Claude Agent SDK must run the project's linter after every file edit. The system prompt says 'Always run the linter after you edit a file.' Traces show it skips the linter in about one run in ten, mostly late in long sessions. Which change makes the requirement hold?

- **A.** A hook that runs the linter after every edit tool call, so it runs as code, not at the model's discretion
- **B.** Add few-shot examples to the prompt that show the agent running the linter after each edit
- **C.** Raise the effort level so the agent plans more carefully and follows its instructions more closely
- **D.** Repeat the instruction in capitals at the end of the system prompt, which is where the model reads it last

<details>
<summary>Answer</summary>

**A.** A required action shouldn't depend on the model remembering it; a post-edit hook runs every time (A). Emphasis (D), examples (B) and more reasoning (C) all make the step more likely, and none makes it certain, which is what the requirement asks for.

</details>

### Question 6

*Applications and Integration*

A chatbot sends only the newest user message to the API on each turn. Users complain that it forgets what they said two messages earlier. What fixes this?

- **A.** Send the conversation history, alternating user and assistant turns, with every request
- **B.** Switch to a model with a larger context window that can hold more of the conversation
- **C.** Raise `max_tokens` so there is room in each response to refer back to earlier messages
- **D.** Enable prompt caching, so the earlier turns of the conversation are remembered between requests

<details>
<summary>Answer</summary>

**A.** The Messages API is stateless: the history you send is the model's entire memory of the conversation (A). Caching (D) makes repeated prefixes cheaper and faster, and it only applies to content you actually send. `max_tokens` (C) limits output length. A larger window (B) is useless when the earlier turns are never included.

</details>

### Question 7

*Applications and Integration*

Which `stop_reason` tells you the response ended because it filled the model's context window, as opposed to hitting the `max_tokens` value you set?

- **A.** `max_tokens`
- **B.** `end_turn`
- **C.** `model_context_window_exceeded`
- **D.** `pause_turn`

<details>
<summary>Answer</summary>

**C.** C means the response ran into the model's context window limit. A means it hit your own `max_tokens` cap. D means a server-side tool loop paused and should be continued, and B means Claude finished naturally. The first two both mean the output may be incomplete and shouldn't be parsed as a finished answer.

</details>

### Question 8

*Applications and Integration*

Which TWO problems does streaming solve? (Select TWO)

- **A.** Users waiting several seconds for the first words of a chat reply
- **B.** HTTP timeouts on requests with very large `max_tokens` values
- **C.** Answers that contain factual errors
- **D.** High token prices on long outputs, since streamed tokens are billed at a lower rate
- **E.** Rate-limit errors during traffic peaks

<details>
<summary>Answer</summary>

**A and B.** Streaming sends tokens as they're generated, which shortens perceived latency (A) and keeps long-running requests alive instead of waiting on one large response (B). It doesn't change token pricing (D), accuracy (C) or rate limits (E).

</details>

### Question 9

*Applications and Integration*

Your app sends a different subset of 30 tools on each request depending on the user's plan, and the order of the tool list varies between requests. The system prompt is identical every time, yet the cache hit rate is near zero. Why?

- **A.** Requests that include tool definitions can't be cached, so only the messages after them are stored
- **B.** The system prompt must be placed before the tools in the request, or the system prompt can't be cached at all
- **C.** The 5-minute cache lifetime is too short for this traffic and needs to move to the 1-hour option
- **D.** Tools lead the cache prefix, so a changing tool list or order breaks it; send one stable, ordered list per plan

<details>
<summary>Answer</summary>

**D.** The cache is a prefix match in a fixed order (tools, then system, then messages), so a changing tool list breaks the prefix at its very start (D). The order of those sections isn't yours to choose (B), tools are cacheable (A), and a longer lifetime (C) doesn't help a prefix that never repeats.

</details>

### Question 10

*Applications and Integration*

Your batch job writes results to the database in the order they come back, pairing each with the input at the same position. Some records end up with another record's classification. Why?

- **A.** Sampling makes the classifications non-deterministic, so some labels change between runs
- **B.** Results can come back in any order; match each one to its request by `custom_id`
- **C.** The batch expired before all of its requests finished, so later results shifted position
- **D.** Results are only kept for 29 days, after which older records lose their labels

<details>
<summary>Answer</summary>

**B.** Results aren't guaranteed to follow request order, which is why every request carries a `custom_id` (B). An expired batch (C) produces 'expired' results, which wouldn't swap labels between records. Non-determinism (A) can change a label but doesn't explain systematic mismatches. Retention (D) is unrelated.

</details>

### Question 11

*Applications and Integration*

A downstream parser broke after your model outputs changed format overnight. Nobody touched the code. Which TWO practices prevent this kind of silent change? (Select TWO)

- **A.** Always call the newest model alias, so production picks up every improvement automatically
- **B.** Pin a specific model version in production and upgrade on purpose after running evals
- **C.** Keep prompts under version control (or in a prompt registry) and run evals before changing them
- **D.** Edit prompts directly in production for speed, so that fixes reach users the same day
- **E.** Add retries around the parser

<details>
<summary>Answer</summary>

**B and C.** Pinning (B) keeps model behavior fixed until you choose to move, and versioned prompts (C) make every behavior change reviewable and revertible. A floating alias (A) and direct production edits (D) are how silent changes happen. Retries (E) repeat the same broken output.

</details>

### Question 12

*Claude Code*

Which files should hold a team's shared Claude Code permission rules (for example, allowing `Bash(npm run test *)`) and one developer's personal overrides for the same project?

- **A.** `~/.claude/settings.json` for the team; the project's `.claude/settings.json` for the developer's own overrides
- **B.** `CLAUDE.md` for both, with the developer's overrides in a section at the end
- **C.** Committed `.claude/settings.json` for the team; gitignored `.claude/settings.local.json` for the developer
- **D.** `.mcp.json` for the team, and `CLAUDE.local.md` in the project root for the developer

<details>
<summary>Answer</summary>

**C.** The project settings file is shared through version control, and the local settings file holds personal overrides for that project without being committed (C). User-level settings (A) apply to one person across all projects. `CLAUDE.md` files (B, D) hold instructions, while permissions are enforced from settings files, and `.mcp.json` configures MCP servers.

</details>

### Question 13

*Claude Code*

A platform team has a proven Claude Code setup: a code-review Skill, a security-review subagent, a hook that blocks pushes to main, and an internal MCP server. Forty product teams in separate repositories should install it and receive updates. What is the best way to distribute it?

- **A.** Document the setup on the wiki and let each team rebuild it to suit its own repository
- **B.** A versioned plugin in an internal marketplace, so teams install it once and receive updates
- **C.** Copy the files into each repository's `.claude/` folder, so every team has its own setup
- **D.** Put the files in each developer's user-level `~/.claude/` folder through an onboarding script

<details>
<summary>Answer</summary>

**B.** A plugin bundles skills, subagents, hooks and MCP servers as one installable unit with versions, and a marketplace handles distribution and updates (B). Copies in forty repositories (C) drift apart with every change. A wiki (A) depends on forty teams rebuilding it correctly. User-level folders (D) reach one machine at a time and nothing in the repository.

</details>

### Question 14

*Eval, Testing, and Debugging*

Your test suite checks that the model's summary exactly equals a stored 'golden' string, and the tests keep flaking. What is a better approach?

- **A.** Assert on structure and key facts (valid schema, required fields, must-have figures) or grade with a rubric
- **B.** Retry each test until the output matches the golden string, then record a pass
- **C.** Delete the flaky tests and rely on manual review of a few outputs before each release
- **D.** Set temperature to 0 and keep exact string matching, since that makes the model's outputs fully deterministic

<details>
<summary>Answer</summary>

**A.** Sampled outputs vary between runs, so tests should check what matters about an output instead of its exact wording (A). Temperature 0 (D) is not a plan: the newest models reject sampling parameters with a 400, and where temperature 0 was accepted it reduced variation without guaranteeing identical text. Retrying until a pass (B) hides real regressions, and deleting tests (C) removes the safety net.

</details>

### Question 15

*Eval, Testing, and Debugging*

After you add a new tool named `get order status`, every request returns 400 `invalid_request_error`. What is the first move?

- **A.** Retry with exponential backoff, since a newly added tool can take a few minutes to register
- **B.** Rewrite the system prompt to explain the new tool and when the agent should call it
- **C.** Switch to a different model that supports more flexible tool names in its requests
- **D.** Fix the request: tool names can't contain spaces, so rename it (for example, `get_order_status`)

<details>
<summary>Answer</summary>

**D.** A 400 is a client error caused by the request itself, and a tool name with spaces breaks the documented pattern `^[a-zA-Z0-9_-]{1,128}$` (D). Retries (A) repeat the same invalid request. The model (C) and the prompt (B) play no part in request validation.

</details>

### Question 16

*Eval, Testing, and Debugging*

A team grades chatbot replies with an LLM judge on a 1-5 helpfulness rubric. Compared with 200 human-labeled replies, the judge agrees with people on short replies but rates long replies about a point higher than they do. What should the team do before trusting the scores?

- **A.** Average the judge's scores with those of a second judge model, so that the length bias is diluted
- **B.** Switch the judge to a larger, more capable model and start using its scores in the release gate right away
- **C.** Revise the rubric and judge prompt to score what matters regardless of length, then re-measure agreement
- **D.** Replace the rubric with an exact-match comparison against stored reference answers

<details>
<summary>Answer</summary>

**C.** The human labels expose a length bias, so the fix is a calibrated judge: change the rubric, then check agreement again (C). Averaging two judges (A) can average the same bias. A larger model (B) may still be biased, and skipping the re-measure means nobody knows. Exact match (D) can't grade helpfulness, because good replies vary in wording.

</details>

### Question 17

*Model Selection and Optimization*

A team's monthly API bill doubled, and evals show quality is fine. Which TWO levers should they try before downgrading the model tier? (Select TWO)

- **A.** Raise `max_tokens` so fewer responses get cut off
- **B.** Send all traffic, live chat included, through the Batch API
- **C.** Cache the stable prefix (tools and system prompt)
- **D.** Trim context: drop stale tool outputs and history the model no longer needs
- **E.** Move all traffic to the fast tier today

<details>
<summary>Answer</summary>

**C and D.** Trimming (D) and caching (C) cut cost without touching the model, so they come before a tier change, which should only happen with eval evidence (E). Batch (B) fits only work nobody is waiting for. A higher `max_tokens` (A) can raise spend.

</details>

### Question 18

*Model Selection and Optimization*

A coding agent on a model that supports the effort parameter works well but runs slowly and uses many tokens on routine refactors. Evals show quality holds at a lower effort level for those tasks. What should change?

- **A.** Raise effort to `max` on every request so refactors finish in fewer turns
- **B.** Lower `output_config.effort` for routine refactors; keep a higher level for hard tasks
- **C.** Set `max_tokens` to 512 for every request so no response can run long
- **D.** Switch to a smaller model for every task without testing it, since refactors are simple

<details>
<summary>Answer</summary>

**B.** Effort controls how many tokens Claude spends across the whole response, thinking and tool calls included, without changing models, and the evals already show the lower level holds (B). D skips the evidence step. A hard cap (C) truncates work midway. Maximum effort (A) adds tokens and latency, the opposite of the goal.

</details>

### Question 19

*Model Selection and Optimization*

A team runs its chatbot with adaptive thinking at high effort on every request, including one-line greetings. Latency and cost rose, with no measurable quality gain on those replies. What is the best response?

- **A.** Disable thinking for the whole application, since it adds latency and cost to every single reply it sends
- **B.** Move to the most capable model, which answers simple turns quickly even at high effort
- **C.** Raise effort to `max` everywhere, so every turn gets the most careful answer possible
- **D.** Decide per workload: keep deeper reasoning where evals show gains, and route simple turns at low effort

<details>
<summary>Answer</summary>

**D.** Reasoning buys accuracy on multi-step problems and costs output tokens and latency everywhere else, so depth is a per-workload choice backed by evals (D). A gives up the gains where they exist (and on some current models thinking can't be disabled at all). C and B spend more on replies that didn't need it.

</details>

### Question 20

*Model Selection and Optimization*

An autocomplete feature must return short suggestions within a few hundred milliseconds, and the quality bar is modest. Which setup fits?

- **A.** A fast-tier (Haiku-class) model with streaming and a small `max_tokens`
- **B.** A top-tier model with extended thinking, so the suggestions are as good as possible
- **C.** A balanced-tier model with `max_tokens` of 32,000
- **D.** The Batch API, which halves the cost of each suggestion request

<details>
<summary>Answer</summary>

**A.** Latency-critical, high-volume, bounded tasks are the fast tier's case (A). B adds the most latency of all the options. Batch (D) is asynchronous. C misses the latency target, and a huge output budget is pointless for short suggestions.

</details>

### Question 21

*Prompt and Context Engineering*

You pass a 50-page contract and ask detailed questions about it. Answers sometimes miss relevant clauses. Which prompt structure follows Anthropic's long-context guidance?

- **A.** The contract twice, once before and once after the question, so that no clause in it is missed
- **B.** The question first, so Claude knows what to look for, then the contract
- **C.** The question in the middle of the contract, next to the clauses it is about
- **D.** The contract first, in tags such as `<contract>`, then the instructions and question at the end

<details>
<summary>Answer</summary>

**D.** Anthropic recommends putting long documents at the top and the query at the end, and reports up to 30% better responses in tests with complex inputs; the tags keep the document separate from the instructions (D). B and C go against that guidance, and A doubles the cost and the noise. Asking Claude to quote the relevant clauses before answering also helps it focus.

</details>

### Question 22

*Prompt and Context Engineering*

Your code forced JSON output by prefilling the assistant turn with an opening brace. After moving to a newer model, requests with the prefilled last assistant turn return a 400 error. What is the recommended replacement?

```python
messages = [
    {"role": "user", "content": f"Extract the fields from: {doc}"},
    {"role": "assistant", "content": "{"},   # prefill
]
```

- **A.** Stay on the older model permanently
- **B.** Structured outputs: put the JSON schema in `output_config.format` and drop the prefill
- **C.** Add 'respond only in JSON' to the prompt and extract the first {...} block with a regex
- **D.** Prefill with an opening square bracket instead, which the newer models still accept

<details>
<summary>Answer</summary>

**B.** Starting with the Claude 4.6 models, a prefilled last assistant turn is rejected, and Anthropic's migration guidance for format control points to structured outputs (B). D is still a prefill. C goes back to probabilistic formatting with fragile parsing. A blocks every future upgrade.

</details>

### Question 23

*Prompt and Context Engineering*

Which TWO practices make a few-shot prompt for a tricky classification more reliable? (Select TWO)

- **A.** Examples wrapped in tags such as `<example>`, clearly separated from the input to classify
- **B.** Examples that contradict the instructions, to test robustness
- **C.** Examples that all share the same label
- **D.** Fifty near-identical examples, so that the model sees the same pattern many times over
- **E.** Two to four varied examples, including one the model should correctly reject

<details>
<summary>Answer</summary>

**A and E.** A small, varied set with a negative case teaches the boundary (E), and clear separation keeps the model from mixing examples with the real input (A). Near-identical examples (D) and single-label sets (C) teach a narrow pattern. Contradictory examples (B) teach the model to ignore your instructions.

</details>

### Question 24

*Prompt and Context Engineering*

A benefits assistant receives three HR policy documents in every request. When employees ask about benefits the policies don't mention, it still answers with confident specifics. Which request design fixes this?

- **A.** Ask the model to add a confidence score to each answer, and show low-confidence answers with a warning
- **B.** Switch to structured outputs with a required `answer` field, so every reply has the same shape
- **C.** Use cited policy documents, require a cited passage per answer, and allow 'not covered in the policies'
- **D.** Add the whole company intranet to the context, so that far more of the employees' questions are covered

<details>
<summary>Answer</summary>

**C.** Grounding needs a source to cite and permission to say the answer isn't there (C). More context (D) moves the boundary without teaching the model to stop at it. A self-reported confidence score (A) isn't verification. A required `answer` field (B) forces an answer even when there isn't one, and citations can't be combined with structured outputs in one request.

</details>

### Question 25

*Security and Safety*

A research agent reads web pages. One page hides text telling the agent to email the user's files to an outside address, and the agent has a `send_email` tool. Which TWO controls most directly reduce this risk? (Select TWO)

- **A.** A lower effort level, so the agent carries out fewer multi-step instructions
- **B.** A system-prompt line telling the agent to ignore malicious instructions, as the only defense it relies on
- **C.** Least-privilege tools: no `send_email` tool for the research agent, or human approval on outbound email
- **D.** A deterministic gate in code that blocks or holds any action sending data to an external address
- **E.** A larger model, which is better at spotting hidden instructions in web pages

<details>
<summary>Answer</summary>

**C and D.** Content the agent reads is an untrusted channel, so the strongest controls limit what an injected instruction can do: no dangerous capability (C) and a programmatic check on risky actions (D). A prompt instruction on its own (B) is probabilistic. Model size (E) and effort (A) aren't security controls.

</details>

### Question 26

*Security and Safety*

A developer put the production API key into a system-prompt template in the repository 'so the agent can call internal APIs.' Which TWO steps fix this? (Select TWO)

- **A.** Have your tool code authenticate to the internal APIs, so the model never sees the credential
- **B.** Move the key to the end of the prompt, where users are less likely to see it
- **C.** Tell the model in the system prompt never to reveal the key to anyone who asks for it
- **D.** Base64-encode the key in the template so it isn't readable in plain text
- **E.** Rotate the key, and store secrets in environment variables or a secret manager

<details>
<summary>Answer</summary>

**A and E.** A key in a repository and a prompt is already exposed, so it gets rotated and stored properly (E), and credentials belong in the code that executes tools, outside the model's context (A). Encoding (D) is trivially reversed, an instruction (C) is probabilistic, and moving the key (B) keeps it in the prompt.

</details>

### Question 27

*Security and Safety*

An internal HR assistant answers every employee's questions using one service account that can read all employee records. A junior employee asked about a colleague's salary and got an answer. What is the root fix?

- **A.** Run lookups with the calling user's identity and permissions, and log each call against that user
- **B.** Add a system-prompt rule, 'Never reveal salaries', and repeat it to the model at the start of every turn
- **C.** Remove salary data from the HR system that the assistant's service account can read
- **D.** Filter out any response that contains the word 'salary' before it reaches the employee

<details>
<summary>Answer</summary>

**A.** The shared over-privileged account erased per-user authorization and the audit trail, and acting as the caller restores both (A). B is a probabilistic patch. C breaks legitimate HR work. A keyword filter (D) is easy to get around and blocks legitimate answers.

</details>

### Question 28

*Tools and MCP*

Which statement about server-side tools such as web search is correct?

- **A.** They're available only through MCP, so each one needs an MCP server configured for it
- **B.** Your application must implement and execute them, then return their results as `tool_result` blocks
- **C.** They work only in the Batch API, because their results take longer to produce than a normal request allows
- **D.** They run on Anthropic's infrastructure, so your code doesn't execute them or return `tool_result` blocks

<details>
<summary>Answer</summary>

**D.** Server tools execute on Anthropic's side, and their results come back inside the response (D). Client tools are the ones your code runs (B). Server tools are declared in the tools parameter like any other tool (A), and they work in regular requests (C).

</details>

### Question 29

*Tools and MCP*

Your company's quarterly-report procedure is 12 steps with templates and formatting rules. Teams want Claude to follow it in claude.ai, Claude Code and the API. No new external system is involved. Which mechanism fits?

- **A.** A custom tool that returns the procedure's steps when Claude calls it
- **B.** An MCP server that serves the templates to Claude, claude.ai, and the API
- **C.** A Skill: packaged instructions and templates that load when the task matches
- **D.** A fine-tuned model trained on the past quarterly reports and on their templates

<details>
<summary>Answer</summary>

**C.** The need is know-how and workflow steps, which is what Skills package (C). Tools (A) and MCP servers (B) add actions or data access, and nothing here needs a new action or data source. Fine-tuning (D) is heavy machinery for a procedure that fits in a document.

</details>

### Question 30

*Tools and MCP*

An agent calls `create_shipment` with inputs that sometimes have the wrong type (weight as a string) or miss required fields, which breaks your handler. Which API feature addresses this at the source?

- **A.** `strict: true` on the tool definition, so tool inputs follow the `input_schema`
- **B.** `tool_choice` set to `auto`, so the model decides when to call the tool
- **C.** A longer, more detailed tool description that explains each of the fields and its type
- **D.** A higher effort level, so the model checks its tool inputs more carefully

<details>
<summary>Answer</summary>

**A.** Strict tool use applies schema validation to the tool's inputs (A). A better description (C) helps the model pick and fill the tool and still guarantees nothing. `auto` (B) is the default and changes nothing. More effort (D) changes how much the model reasons and still can't guarantee types.

</details>

---

## Where to go next

- **Review by domain.** If your misses cluster, re-read those domains in Part II of the [CCDV-F study guide](./guide.md):
  - [Agents and Workflows](./guide.md#domain-1-agents-and-workflows-17)
  - [Applications and Integration](./guide.md#domain-2-applications-and-integration-20)
  - [Claude Code](./guide.md#domain-3-claude-code-8)
  - [Eval, Testing, and Debugging](./guide.md#domain-4-eval-testing-and-debugging-10)
  - [Model Selection and Optimization](./guide.md#domain-5-model-selection-and-optimization-12)
  - [Prompt and Context Engineering](./guide.md#domain-6-prompt-and-context-engineering-15)
  - [Security and Safety](./guide.md#domain-7-security-and-safety-8)
  - [Tools and MCP](./guide.md#domain-8-tools-and-mcp-10)
- **Practice at full length.** The [CCDV-F page on Preporato](https://preporato.com/certificates/claude-certified-developer-foundations) has free sample questions and full-length timed practice tests (paid) in the exam's format, with a score for every domain.

Found a mistake in a question? [Open an issue](https://github.com/preporato/claude-certification-guide/issues/new?template=outdated-fact.yml) and we'll fix it.

*These questions were written for this repo and are not taken from the exam. Not affiliated with Anthropic.*
