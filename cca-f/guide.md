# Claude Certified Architect - Foundations (CCA-F): The Complete Study Guide

A full preparation guide for Anthropic's CCA-F exam. Part I teaches the technology the exam draws from, organized by topic. Part II re-indexes the same material by exam domain for revision. Part III covers exam strategy, worked questions, and a pre-exam checklist.

Maintained by [preporato.com](https://preporato.com). Facts checked in November 2026 against the official exam guide (version 1.1, November 2026), Anthropic's program pages, and the current Claude API and Claude Code documentation.

---

## Contents

- [Introduction](#introduction)
- [Exam format](#exam-format)
- [The six production scenarios](#the-six-production-scenarios)
- **Part I: Technology**
  - [Chapter 1: The Claude API and the agentic loop](#chapter-1-the-claude-api-and-the-agentic-loop)
  - [Chapter 2: Tools and tool_use](#chapter-2-tools-and-tool_use)
  - [Chapter 3: Multi-agent orchestration](#chapter-3-multi-agent-orchestration)
  - [Chapter 4: Model Context Protocol (MCP)](#chapter-4-model-context-protocol-mcp)
  - [Chapter 5: Claude Code](#chapter-5-claude-code)
  - [Chapter 6: Prompt engineering and structured output](#chapter-6-prompt-engineering-and-structured-output)
  - [Chapter 7: Context management in production](#chapter-7-context-management-in-production)
  - [Chapter 8: Reliability, escalation, and recovery](#chapter-8-reliability-escalation-and-recovery)
- **Part II: Exam domain notes**
  - [Domain 1: Agentic Architecture & Orchestration (27%)](#domain-1-agentic-architecture--orchestration-27)
  - [Domain 2: Tool Design & MCP Integration (18%)](#domain-2-tool-design--mcp-integration-18)
  - [Domain 3: Claude Code Configuration & Workflows (20%)](#domain-3-claude-code-configuration--workflows-20)
  - [Domain 4: Prompt Engineering & Structured Output (20%)](#domain-4-prompt-engineering--structured-output-20)
  - [Domain 5: Context Management & Reliability (15%)](#domain-5-context-management--reliability-15)
- **Part III: Exam preparation**
  - [The preparation ladder](#the-preparation-ladder)
  - [The Golden Rule and five mental models](#the-golden-rule-and-five-mental-models)
  - [The seven anti-patterns](#the-seven-anti-patterns)
  - [Critical distinctions](#critical-distinctions)
  - [Exam-day strategy](#exam-day-strategy)
  - [Worked questions](#worked-questions)
  - [30-day study plan](#30-day-study-plan)
  - [Pre-exam checklist](#pre-exam-checklist)
  - [Resources](#resources)

---

## Introduction

CCA-F (Claude Certified Architect - Foundations) is Anthropic's certification for people who build production-grade Claude systems end to end: agentic architectures, multi-agent orchestration, prompt and context engineering for reliability, and the tools and MCP servers agents depend on. It launched on March 12, 2026 as the program's first exam and now sits inside a five-certification program (see the [repo root](../README.md) for the full comparison). Anthropic's current exam guide (version 1.1, November 2026) gives the exam code as **CCAR-F**; this guide keeps CCA-F, the name most candidates know it by.

The exam is written from production judgment. Questions describe running systems with logs, failures, and constraints, and ask what a competent architect would do. Memorizing definitions is necessary but never sufficient; the exam repeatedly asks you to choose between two plausible approaches, and the difference is always an engineering principle this guide teaches explicitly.

**Who should take it:** engineers and technical leads who have moved past making individual API calls and now design the systems those calls live in. Anthropic recommends hands-on experience building Claude or agent systems before sitting it.

## Exam format

| | |
|---|---|
| Exam code | CCAR-F in the official guide (version 1.1); widely known as CCA-F |
| Questions | 60 |
| Duration | 120 minutes to answer, about 135 minutes of seat time |
| Passing score | 720 on a 100-1000 scaled score, with percent correct per domain on the report |
| Question style | Multiple choice and multiple response; each item states how many responses to select |
| Structure | Scenario-based: 4 of the 6 scenarios below, picked at random for each sitting |
| Delivery | Pearson VUE, test center or online proctored. No Claude, no docs, no browser during the exam |
| Price | $125 per attempt |
| Registration | Anthropic Partner Academy, open to people who work at Claude Partner Network organizations (sign in with a company email); you pay at Pearson's checkout |
| Rescheduling | Free up to 1 hour before an OnVUE appointment, 48 hours before a test center one |
| Languages | English or Japanese |
| Retakes | Full fee for every attempt; waits of 14, 30 and 90 days after the first, second and third failed attempts; at most 4 attempts in any 12 months |
| Validity | 12 months; free non-proctored renewal assessment before expiration, full-price proctored exam after it lapses |
| Partner tier | Counts toward Claude Partner Network tier eligibility |

### Exam domains

| Domain | Weight | ~Questions |
|--------|--------|-----------|
| 1. Agentic Architecture & Orchestration | 27% | ~16 |
| 2. Tool Design & MCP Integration | 18% | ~11 |
| 3. Claude Code Configuration & Workflows | 20% | ~12 |
| 4. Prompt Engineering & Structured Output | 20% | ~12 |
| 5. Context Management & Reliability | 15% | ~9 |

## The six production scenarios

The exam is scenario-based: each scenario sets up a production context and frames a set of questions. Every sitting presents 4 of the 6 scenarios below, picked at random, so prepare for all six. The names and primary domains are from the official exam guide (version 1.1); the "expect" lines are this guide's reading of where each scenario's questions tend to go.

1. **Customer Support Resolution Agent.** An Agent SDK agent handling returns, billing disputes, and account issues through custom MCP tools (`get_customer`, `lookup_order`, `process_refund`, `escalate_to_human`), aiming for 80%+ first-contact resolution. *Primary domains:* agentic architecture, tool design and MCP, context management and reliability. *Expect:* escalation rules (ambiguity escalates, sentiment alone does not), programmatic gates before refunds, structured tool errors, structured handoffs.
2. **Code Generation with Claude Code.** A team using Claude Code for generation, refactoring, debugging, and documentation, with custom slash commands and CLAUDE.md configuration. *Primary domains:* Claude Code configuration and workflows, context management. *Expect:* the CLAUDE.md hierarchy, path-scoped rules, Skills and commands, Plan Mode versus direct execution, `--resume` and `fork_session`.
3. **Multi-Agent Research System.** A coordinator delegating to subagents that search the web, analyze documents, synthesize findings, and write cited reports. *Primary domains:* agentic architecture, tool design and MCP, context management. *Expect:* hub-and-spoke rules, explicit context passing, parallel `Task` calls, partial-failure handling, provenance and conflicting sources.
4. **Developer Productivity with Claude.** An Agent SDK tool that explores unfamiliar codebases, explains legacy systems, generates boilerplate, and automates chores with the built-in tools (Read, Write, Bash, Grep, Glob) and MCP servers. *Primary domains:* tool design and MCP, Claude Code configuration, agentic architecture. *Expect:* built-in tool choice, incremental investigation, MCP scopes and secrets, tool scoping.
5. **Claude Code for Continuous Integration.** Claude Code in a CI/CD pipeline running code reviews, generating tests, and commenting on pull requests, with feedback that must be actionable and low in false positives. *Primary domains:* Claude Code configuration, prompt engineering and structured output. *Expect:* `-p` and output flags, hooks, explicit review criteria, independent review sessions, batch versus real-time for pipeline jobs.
6. **Structured Data Extraction.** A system that extracts data from unstructured documents, validates it against JSON schemas, and feeds downstream systems. *Primary domains:* prompt engineering and structured output, context management and reliability. *Expect:* schema design with nullable and "unclear" values, `tool_use` with schemas and `tool_choice`, validation-retry loops, the Batch API, stratified sampling.

---

# Part I: Technology

## Chapter 1: The Claude API and the agentic loop

### 1.1 Requests, roles, and statelessness

A Claude API call sends a `messages` array of alternating `user` and `assistant` turns, an optional `system` prompt, and configuration (model, `max_tokens`, `tools`). The single most important fact underneath every exam question: **the API is stateless**. Claude has no memory between calls. The conversation history you send IS the memory. Every request must carry the full history the model needs, including every prior tool result.

### 1.2 stop_reason controls everything

Each response carries a `stop_reason` that tells your code what Claude intends:

- `"end_turn"`: Claude considers the task complete. Terminate the loop.
- `"tool_use"`: Claude wants a tool executed. Run it, append the result, continue the loop.
- `"max_tokens"`: the response was truncated by the output limit. Handle explicitly; treating truncation as completion silently corrupts results.

The API has a few more values worth knowing: `"refusal"` (Claude declined), `"stop_sequence"` (one of your stop sequences was hit), `"pause_turn"` (a server-side tool loop such as web search paused; send the response back as-is to let Claude continue) and `"model_context_window_exceeded"` (the response filled the context window). Branch on them explicitly instead of treating every unknown value as completion.

The canonical agentic loop:

```python
while True:
    response = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=4096,
        messages=messages,
        tools=tools,
    )
    if response.stop_reason == "end_turn":
        break  # task complete
    if response.stop_reason == "tool_use":
        tool_result = execute_tool(response.content)
        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_result})
```

**Anti-pattern (heavily tested):** parsing Claude's natural-language output to decide whether to continue ("check if the response contains 'I'm done'"). Natural language parsing is fragile. `stop_reason` is the contract. Similarly, an arbitrary iteration cap (`max_loops = 10`) is a safety net, never the primary termination mechanism; semantic completion via `stop_reason` is.

### 1.3 Token budgets

Long-running loops need a budget enforced from outside the model:

- Track cumulative input plus output tokens from each response's `usage` field. Note that history grows every iteration, so later calls cost more.
- At ~80% of budget, inject an instruction to wrap up within the next iteration or two (a soft warning).
- At 100%, break the loop programmatically (a hard stop). Never rely on Claude to self-terminate.

```python
MAX_TOKENS = 100_000
total = 0
while True:
    response = client.messages.create(...)
    total += response.usage.input_tokens + response.usage.output_tokens
    if total > MAX_TOKENS:
        break  # hard stop, enforced outside the model
    if total > MAX_TOKENS * 0.8:
        messages.append({"role": "user",
                         "content": "TOKEN BUDGET WARNING: summarize findings and conclude."})
```

### 1.4 Handling truncation and refusal

Two `stop_reason` values break naive response handling, and both appear in exam scenarios. `"max_tokens"` means the response was cut off by the output cap; treating it as a complete answer silently corrupts downstream processing. A refusal means Claude declined the request; code that reads the first content block unconditionally crashes or mishandles it.

```python
response = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=2048,
    messages=messages,
)

match response.stop_reason:
    case "end_turn":
        # complete answer; find the text block (a thinking block can come first)
        result = next(b.text for b in response.content if b.type == "text")
    case "max_tokens":
        # Truncated: never parse as complete. Retry with a higher cap,
        # stream, or split the task.
        handle_truncation(response)
    case "tool_use":
        run_tool_loop(response)                     # continue the loop
    case "refusal":
        handle_refusal(response)                    # a decline, not an answer
    case _:
        log_and_escalate(response)                  # anything new
```

**Anti-pattern:** `text = response.content[0].text` with no `stop_reason` check. It works in every demo and fails in production the first time an output hits the cap, a request is declined, or thinking puts another block first.

### 1.5 Model selection

Reason by tier, and anchor production answers to the mid tier:

| Model | Tier | Pick it when |
|-------|------|--------------|
| Claude Haiku | Fastest, cheapest | Simple, high-volume, latency-sensitive tasks (classification, routing) |
| Claude Sonnet | Balance of speed and intelligence | The default production workhorse; the safe exam answer for standard workloads |
| Claude Opus | Most capable | The hardest reasoning and long-horizon agentic work where capability beats cost |

When a question describes a routine production workload and offers a top-tier model as an answer, cost discipline usually makes the mid-tier model correct. When it describes genuinely hard multi-step reasoning, capability wins.

## Chapter 2: Tools and tool_use

### 2.1 How tool selection actually works

Claude selects tools by reading their **descriptions**. Not the tool name, and not hints buried in the system prompt: the description is the primary routing mechanism. A well-written description contains:

- A one-sentence purpose statement ("Searches a PostgreSQL database for customer records matching the given criteria.")
- Parameter documentation with type, format, and constraints ("customer_id: string, UUID format, required")
- A boundary statement naming what the tool does NOT do and which tool to use instead ("This tool searches existing records. To create records, use create_customer.")
- One or two example invocations
- Error behavior ("Returns { error: 'not_found' } if no records match.")

A complete tool definition puts that description to work alongside a JSON Schema for the inputs:

```json
{
  "name": "search_customers",
  "description": "Searches existing customer records in the CRM by name, email, or region. Returns up to 20 matches with id, name, email, and account status. Use this to FIND existing customers. To create a new customer record, use create_customer instead. Returns {\"matches\": []} when no records match; returns {\"error\": \"permission_denied\"} if the caller lacks CRM read access.",
  "input_schema": {
    "type": "object",
    "properties": {
      "query":  { "type": "string", "description": "Name, email, or partial match" },
      "region": { "type": "string", "enum": ["NA", "EMEA", "APAC"], "description": "Optional region filter" },
      "limit":  { "type": "integer", "minimum": 1, "maximum": 20, "default": 10 }
    },
    "required": ["query"]
  }
}
```

Notice what the description carries: purpose, the boundary against the neighboring tool, and the exact shape of both empty and error results. That last part is what lets the agent distinguish "no customers found" from "not allowed to look", the distinction Section 2.5 tests.

### 2.2 How many tools

**4-5 tools per agent is the reliable range.** Selection accuracy degrades significantly as the count grows, and by around 18+ tools Claude begins misrouting calls. When a system needs more capability than five tools can express, the answer is splitting into subagents with scoped tool sets, never loading everything into one agent.

### 2.3 tool_choice

| Value | Behavior | Use when |
|-------|----------|----------|
| `"auto"` | Claude may answer in text OR call a tool | Default; let Claude decide |
| `"any"` | Claude MUST call some tool | You need tool use but the choice can vary |
| `{"type": "tool", "name": "extract_data"}` | Claude MUST call that specific tool | Forcing structured extraction through a schema |

Exam pattern: "How do you ensure Claude always returns structured JSON?" The answer is a schema-enforced mechanism: a tool defined with the JSON schema and forced through `tool_choice`, or structured outputs (the schema in `output_config.format`, or `strict: true` on the tool), which guarantee schema-valid JSON through constrained decoding. A system-prompt instruction to "always respond in JSON" is the trap option.

Current API note: some of the newest models reject forced tool use (`any` or a named `tool`) with a 400 error, and Anthropic points to structured outputs or `auto` plus strict tools instead. The exam's principle stays the same: format guarantees come from a mechanism, never from an instruction.

### 2.4 Syntax errors versus semantic errors

Schema-enforced output through `tool_use` eliminates **syntax errors**: malformed JSON, missing fields, wrong types. It does nothing about **semantic errors**: wrong values, hallucinated data, misclassifications. Schema validation plus retry handles the first class. Only evaluation and human review catch the second. Questions that blur this line are testing whether you know validation's limits.

### 2.5 Designing error responses

Tools fail, and how they report failure decides whether an agent can recover:

| Error type | isRetryable | Examples |
|-----------|------------|----------|
| Transient | true | Timeout, service unavailable, rate limit |
| Validation | false | Invalid input format, missing required field |
| Business logic | false | Insufficient balance, policy violation |
| Permission | false | Unauthorized, forbidden resource |
| Not found | false | Resource does not exist |

Rules the exam tests directly:

- **Distinguish access failures from valid empty results.** "Permission denied" and "no results found" demand different agent behavior; collapsing them into an empty list poisons downstream reasoning.
- Return structured error context: failure type, what was attempted, partial results, suggested alternatives.
- Silently returning empty results as success is an anti-pattern because it forecloses recovery.

```json
{
  "status": "partial_failure",
  "completed": ["repo_scan", "dependency_check"],
  "failed": {
    "tool": "security_scan",
    "error_type": "timeout",
    "attempted": "Full repository security scan",
    "partial_results": "Scanned 47 of 120 files before timeout",
    "alternatives": ["Retry with reduced scope", "Queue for batch processing"]
  }
}
```

## Chapter 3: Multi-agent orchestration

### 3.1 Hub-and-spoke

The primary multi-agent architecture on this exam. The rules, cold:

- A **coordinator** (hub) manages all communication. Subagents never talk to each other directly.
- Subagents run with **isolated context windows**. They do not inherit the coordinator's history; anything a subagent needs must be passed explicitly in its prompt.
- The coordinator can emit multiple subagent invocations in one response for **parallel** execution, or wait on dependencies for **sequential** execution.
- Failure is **isolated**: one subagent crashing does not take down the coordinator or its siblings.

| Aspect | Hub-and-spoke | Flat (all-in-one) |
|--------|--------------|-------------------|
| Context | Each subagent gets only what it needs | One agent holds everything |
| Failure blast radius | One subagent | The whole system |
| Tools per agent | 4-5 scoped | Everything loaded, selection degrades |
| Scaling | Add subagents independently | Refactor the monolith |
| Fits | Complex multi-domain work | Simple single-domain tasks |

### 3.2 Subagent design principles

- **Single responsibility** per subagent (security scanning, dependency analysis, code quality).
- **Scoped tools**: only the 4-5 tools that subagent's job requires.
- **Explicit contracts**: define what the coordinator passes in and what comes back.
- **Timeouts** per subagent; the coordinator never waits indefinitely.
- **Result normalization**: subagents return one standardized format so the coordinator merges without per-agent parsing.

### 3.3 Parallel, sequential, hybrid

| Pattern | Use when | Example |
|---------|----------|---------|
| Sequential | Step N's output feeds step N+1 | Research → Analyze → Recommend |
| Parallel | Steps are independent | Scan five repositories simultaneously |
| Hybrid | Mixed dependencies | Parallel scans → sequential merge → final report |

### 3.4 Task decomposition

Two families:

- **Fixed pipelines**: a predetermined sequence of stages. Predictable, testable, right when the workflow is known in advance.
- **Dynamic decomposition**: the coordinator plans subtasks at runtime based on what it discovers. Right for open-ended investigations; costs more tokens and needs tighter budgets.

Over-decomposition is a tested trap: splitting trivially small work across subagents adds orchestration overhead without any isolation benefit.

### 3.5 State machines and session management

Complex workflows model cleanly as state machines: states like planning, executing, waiting_for_tool, reviewing, escalating, complete, failed; transitions driven by `stop_reason` values, tool results, and validation outcomes; guards as programmatic preconditions. The payoff is crash recovery: persist the state, resume from it.

Session mechanics that appear in questions:

- `--resume <session>` continues a prior session with full history intact.
- `fork_session` branches an independent copy from a shared baseline; changes in the fork never propagate back.

### 3.6 Orchestration in code

The coordinator patterns above, as they actually look. Parallel fan-out means emitting several delegations in one turn and merging when all return; sequential means awaiting each dependency:

```python
# Parallel: independent subtasks, spawned together, merged once
scan_prompts = [scanner_prompt(repo, findings_schema) for repo in repos]
results = run_subagents_parallel(scan_prompts, timeout_s=300)   # isolated contexts
merged = merge_findings([r for r in results if r is not None])  # tolerate failures

# Sequential: B needs A's output, so A completes first
outline = run_subagent(outline_prompt(document))
draft   = run_subagent(draft_prompt(document, outline))          # outline passed explicitly
```

The two rules the exam checks are visible right in the shape of the code: every subagent receives its inputs **explicitly in its prompt** (nothing is inherited), and a failed subagent becomes a `None` to tolerate rather than an exception that destroys its siblings' work.

A structured handoff, whether subagent-to-coordinator or agent-to-human, carries state rather than prose:

```json
{
  "handoff_reason": "policy_ambiguity",
  "conversation_summary": "Customer requests refund of $840 for order 19384, outside the 30-day window by 3 days",
  "attempted": ["standard_refund_policy_check", "manager_exception_lookup"],
  "blocking_question": "Does the loyalty-tier exception apply to window overruns under 7 days?",
  "customer_sentiment": "calm",
  "urgency": "normal"
}
```

## Chapter 4: Model Context Protocol (MCP)

### 4.1 What MCP is

MCP is the open protocol standardizing how models discover and call external tools and data sources. An MCP server exposes capabilities; any MCP-capable client (Claude Code, the API via connectors, other vendors' agents) can consume them without custom integration.

### 4.2 The three capability types

The exam expects you to keep these apart:

- **Tools**: functions Claude can call, with parameters and results (`create_issue`, `search_documents`).
- **Resources**: read-only content catalogs Claude can browse. Data, never actions (GitHub issues, documentation, database schemas).
- **Prompts**: reusable prompt templates the server provides, encapsulating domain-specific prompt engineering.

The three primitives in server code, using the Python SDK's FastMCP style:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("support-kb")

@mcp.tool()
def search_tickets(query: str, status: str = "open") -> str:
    """Search support tickets by keyword. Use status='closed' for resolved tickets."""
    return json.dumps(ticket_store.search(query, status))

@mcp.resource("kb://articles/{article_id}")
def get_article(article_id: str) -> str:
    """A knowledge-base article, addressable by id, browsable by the client."""
    return kb.fetch(article_id)

@mcp.prompt()
def triage_ticket(ticket_text: str) -> str:
    """Reusable triage prompt with the team's severity rubric baked in."""
    return f"Classify severity using the P1-P4 rubric...\n\nTicket:\n{ticket_text}"

mcp.run()
```

One server, three capability types: the tool is an **action** the model invokes, the resource is **data** the client can browse and attach, and the prompt is packaged **know-how**. Exam questions describe a requirement and ask which primitive fits; the answer follows from whether the requirement is an action, data, or a reusable instruction set.

### 4.3 Configuration and scope

| File | Scope | Version controlled | Use |
|------|-------|--------------------|-----|
| `.mcp.json` | Project | Yes | Team-wide tool configuration |
| `~/.claude.json` | User | No | Personal preferences, experiments |

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_TOKEN": "${GITHUB_TOKEN}" }
    }
  }
}
```

Two rules with exam weight: secrets go in via `${ENV_VAR}` expansion and are never committed raw, and project-level config is the answer whenever a whole team needs the same servers.

## Chapter 5: Claude Code

The most heavily configured surface on the exam (20% as its own domain, and it reappears inside scenarios).

### 5.1 The CLAUDE.md hierarchy

| Location | Scope | Version controlled | Loaded |
|----------|-------|--------------------|--------|
| `~/.claude/CLAUDE.md` | User (personal) | No | Always, for this user only |
| `PROJECT_ROOT/CLAUDE.md` or `.claude/CLAUDE.md` | Project (team) | Yes | Always, for everyone |
| `subdirectory/CLAUDE.md` | Directory | Yes | Only when working in that directory |

**The trap the exam loves:** a developer puts team standards in `~/.claude/CLAUDE.md` and wonders why teammates ignore them. User-level config is personal and never ships with the repo. Team instructions belong in the project-level file, committed to version control.

Content guidance: coding standards, test commands, architectural decisions, review criteria. Keep rules specific and actionable ("Run `npm test` before committing"), put the most important ones at the top, and never put secrets in it.

### 5.2 Path-specific rules

`.claude/rules/` holds rule files with a `paths:` glob list in frontmatter; each loads only when Claude edits matching files:

```yaml
---
paths:
  - "src/api/**/*.ts"
---
All API endpoints must validate input using zod schemas.
```

### 5.3 Skills and slash commands

Skills are reusable prompt-based extensions with YAML frontmatter. The fields that get tested:

```yaml
---
name: "review-security"
description: "Performs a security-focused code review"
context: fork          # runs in an isolated subagent
allowed-tools: [Read, Grep, Glob]
argument-hint: "file path or directory to review"
---
```

`context: fork` isolates the skill in a subagent so verbose output does not pollute the main conversation. `allowed-tools` applies least privilege.

### 5.4 Hooks

Hooks run shell commands at lifecycle events. They are the exam's canonical example of programmatic enforcement. The core events:

| Event | Fires | Typical use |
|-------|-------|-------------|
| PreToolUse | Before a tool executes | Block dangerous operations, gate compliance requirements |
| PostToolUse | After a tool completes | Linters, formatters, output validation |
| UserPromptSubmit | When the user submits a prompt | Inject context, screen inputs |
| Stop | When Claude is about to finish | Verify required steps actually ran |
| PreCompact | Before history compaction | Preserve critical state |
| SessionStart / SessionEnd | Session lifecycle | Setup, logging |
| SubagentStop | A subagent finishes | Validate subagent output |

Configuration in `settings.json` nests event → matcher group → hook handlers. The matcher filters by tool name (exact, `|`-separated, or regex), and an `if` field narrows to specific invocations:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "if": "Bash(rm *)",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/block-rm.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [ { "type": "command", "command": "npx eslint --fix" } ]
      }
    ]
  }
}
```

A hook script controls the outcome through its exit code and output: **exit 0** allows (and can return structured JSON for fine-grained decisions), **exit 2 blocks the action**, with the stderr text or a JSON `permissionDecision` explaining why:

```bash
#!/bin/bash
# .claude/hooks/block-rm.sh: deny recursive deletes, allow everything else
COMMAND=$(jq -r '.tool_input.command')
if echo "$COMMAND" | grep -q 'rm -rf'; then
  jq -n '{ hookSpecificOutput: {
    hookEventName: "PreToolUse",
    permissionDecision: "deny",
    permissionDecisionReason: "Destructive command blocked by policy"
  } }'
else
  exit 0
fi
```

Two details worth having cold: there is no dedicated commit event, so "always run tests before committing" is a `PreToolUse` hook matching `Bash` with an `if` on `git commit`, and hooks defined in the committed project `settings.json` reach the whole team while `~/.claude/settings.json` hooks are personal.

Whenever a question asks how to **guarantee** a behavior (tests always run before commit, `rm -rf` never executes), the answer is a hook. A CLAUDE.md instruction is guidance the model probably follows; a hook is a mechanism it cannot bypass.

### 5.5 Imports, local files, and session commands

Four mechanics round out the configuration surface, and each has appeared in scenario questions:

- **`@path` imports.** A CLAUDE.md can pull in other files with `@path/to/file` syntax: `See @README for the project overview and @docs/git-instructions.md for the git workflow.` Imports resolve relative to the importing file, recurse up to four hops deep, and are skipped inside backticks and code blocks. Imported files load at launch, so imports organize content without saving context.
- **`CLAUDE.local.md`.** Personal, project-specific instructions that load alongside the project CLAUDE.md and belong in `.gitignore`: sandbox URLs, preferred test data, anything true for you and wrong for the team. This completes the placement question: team-wide → committed project file; personal-everywhere → `~/.claude/CLAUDE.md`; personal-this-project → `CLAUDE.local.md`.
- **`/compact` and what survives it.** Compaction summarizes conversation history to reclaim context. The project-root CLAUDE.md survives: it is re-read from disk and re-injected afterward. Instructions given only in conversation do not survive, which is exactly why durable rules belong in files rather than chat.
- **`/init`, `/memory`, `/context`.** `/init` generates a starting CLAUDE.md by analyzing the codebase, `/memory` opens the memory files for editing, and `/context` shows which files actually loaded into the current session, the first debugging step when Claude ignores an instruction.

### 5.6 Plan Mode versus direct execution

| Plan Mode | Direct execution |
|-----------|-----------------|
| Multi-file coordinated changes | Single-file fixes |
| Multiple valid architectural approaches | A clear stack trace pointing at the bug |
| Unfamiliar codebase exploration | Simple additions to known files |
| Cross-cutting refactors | Typos and small edits |

### 5.7 Built-in tools

| Tool | Purpose | Detail with exam weight |
|------|---------|------------------------|
| Grep | Search file contents | Regex, ripgrep-based |
| Glob | Match file paths | Patterns like `**/*.ts` |
| Read | Read files | Line ranges, images, PDFs |
| Edit | Targeted modification | Needs a unique text anchor to match |
| Write | Create or overwrite | Edit for changes, Write for new files |
| Bash | Shell commands | Working directory resets between calls |

Investigate incrementally: Grep/Glob to locate, Read the relevant region, then Edit. Reading entire large files into context when a search would do is the anti-pattern being probed.

### 5.8 CI/CD and headless mode

- `-p` / `--print`: non-interactive mode; without it the pipeline hangs waiting for input. The essential flag.
- `--output-format json`: machine-parseable output.
- `--tools "Read,Grep,Glob"`: limit the run to those built-in tools (least privilege in automation).
- `--allowedTools` is a different flag: it pre-approves tools so they run without a permission prompt, and `--disallowedTools` removes or denies specific tools. A CI job that needs both restriction and no prompts uses `--tools` for the first and `--allowedTools` for the second.

```bash
claude -p "Review this PR for security issues" --output-format json --tools "Read,Grep,Glob"
```

Two principles ride along: include prior findings in the prompt so repeated reviews report only new issues, and separate generation from review. A model reviewing code it just wrote, in the same session, retains the reasoning that produced it and is biased toward approving it. Independent review sessions fix this.

## Chapter 6: Prompt engineering and structured output

### 6.1 Explicit criteria beat vague guidance

"Be conservative" does not reduce false positives, and "be thorough" does not improve coverage. Working instructions name the criteria: "Only flag issues with severity high or above that have a direct security impact." "Check for SQL injection, XSS, CSRF, and authentication bypass." The test for a good criterion: someone reading the output can verify whether it was met.

System prompt shape: role first, then numbered explicit criteria, then boundary statements ("Do NOT suggest style changes"), then the exact output format.

### 6.2 Few-shot examples: what they can and cannot do

Use 2-4 targeted examples that demonstrate classification reasoning and output format, including at least one example of what NOT to flag and one tricky edge case.

What few-shot cannot do, and the exam checks: **enforce ordering or compliance**. Examples showing tools called in the correct order do not guarantee that order. Ordering is a compliance requirement, and compliance requirements get programmatic enforcement (hooks, gates, orchestration).

### 6.3 Prompt chaining

Complex work splits into focused chained prompts, each doing one job: extract → validate → enrich → format. Each stage gets its own instructions and its own validation. One giant prompt doing everything at once is less reliable and much harder to debug.

### 6.4 The interview pattern and self-correction

Two named patterns extend chaining and both show up in scenario questions:

- **The interview pattern** inverts the flow: instead of guessing what the model needs, you instruct it to ask. "Before drafting the migration plan, ask me up to five questions about constraints you need and cannot infer from the repository." This fits tasks where requirements live in a human's head, and it beats a long speculative prompt that guesses wrong.
- **Self-correction as a separate pass.** After generation, a follow-up prompt asks the model to check its own output against explicit criteria: "Review the extraction above against the schema. List any field where the value is not directly supported by the source text, then output the corrected JSON." A self-correction pass with named criteria catches real errors; the same instruction folded into the original prompt ("double-check your work") mostly does not. Note the boundary from Section 6.7: self-correction against *criteria* helps, while self-*review* of open-ended quality in the same context stays biased, which is why independent review instances exist.

### 6.5 Schema design for structured output

Force extraction through a schema (structured outputs, or a tool defined with the schema and forced with `tool_choice` on models that allow forcing), and design the schema for the real world:

- **Nullable fields** for data that may not exist in the source.
- **`"unclear"` enum values** for genuinely ambiguous fields.
- **`"other"` plus a detail string** for categories outside the predefined enum.

Every field should have a graceful "I don't know" path. A required, non-nullable field for information that is sometimes absent guarantees validation failures no retry can fix.

### 6.6 Validation and retry

When extraction fails validation, the retry prompt carries three things: the original document, the failed output, and the specific validation errors, with an instruction to fix only those errors.

The boundary that gets tested: **retries fix execution errors, never information gaps.** If Claude misformatted a date, a retry fixes it. If the source document simply lacks the revenue figure, no number of retries will produce it; the nullable schema absorbs it instead.

### 6.7 Batch API

| Aspect | Batch API | Real-time API |
|--------|-----------|---------------|
| Cost | 50% cheaper | Standard |
| Processing | Up to 24 hours | Seconds |
| Latency SLA | None | Yes |
| Tool loops | No: a request can't run tools and continue mid-request | Yes |
| Correlation | `custom_id` per request | Conversation/session |
| Fits | Overnight reports, weekly audits, bulk extraction | User-facing, interactive |

The all-time trap: proposing Batch for anything a user is waiting on. No SLA means possibly 24 hours. The reverse trap also appears: paying real-time prices for overnight bulk work that Batch would halve.

### 6.8 Multi-instance review

Self-review in the same context is biased: the model retains the reasoning that produced the output and tends to confirm it. Production review uses independent instances that see only the artifact, not the conversation that generated it. For code, split per-file passes (local issues) from a cross-file integration pass (systemic issues).

## Chapter 7: Context management in production

### 7.1 Lost-in-the-middle

Models attend well to the beginning and end of the context window and poorly to the middle. Consequences the exam builds questions on:

- Critical information belongs at the **beginning** (or end), never buried mid-context.
- "Increase the context window" is not a fix for attention problems and is a marked trap answer. Restructure instead: extract key facts into a block at the top, or split into focused passes.

### 7.2 Keeping context lean

- **Trim tool outputs** to the fields the next step needs before appending them to history.
- **Prune ceremony**: "file saved successfully" messages and other irrelevant successes.
- **Progressive summarization**: every N tool calls, replace detailed history with a summary.
- **Key-fact extraction**: pull names, numbers, dates, and decisions into a persistent structured block at the prompt's top.
- **Scratchpad files**: persist findings outside the window entirely, and read back only what is needed.
- **Subagent offloading**: ten files to analyze means ten focused subagent contexts returning summaries, never one context holding all ten.

### 7.3 Position-aware input and scratchpads

Position-aware input applies the attention curve deliberately. The same facts, restructured so the critical block leads:

```python
prompt = f"""CASE FACTS (authoritative, extracted from prior steps):
- Customer: {facts['customer_id']}, tier: {facts['tier']}
- Order {facts['order_id']}: ${facts['amount']}, delivered {facts['delivered']}
- Policy window: 30 days; request is {facts['days_over']} days past it

TASK: {task}

SUPPORTING MATERIAL (reference only):
{long_tool_outputs}"""
```

A scratchpad moves state out of the window entirely. The agent appends findings to a file as it works and reads back only what the next step needs:

```python
def note(finding: dict):
    with open("scratchpad.jsonl", "a") as f:
        f.write(json.dumps(finding) + "\n")

def recall(topic: str) -> list[dict]:
    return [json.loads(l) for l in open("scratchpad.jsonl")
            if topic in l]          # selective read-back, never the whole file
```

The pattern's point is the selective read-back: a scratchpad that gets dumped wholesale into every prompt has just reinvented the bloated context it was meant to prevent.

### 7.4 Detecting context degradation

Signals that the model has lost the thread:

- Inconsistent answers to the same question within one session
- References to "typical patterns" instead of specific findings from this conversation
- Re-running tools whose results are already in history
- Citing information never provided

Remediation: scratchpads, subagent offloading, and compaction of the conversation while preserving essentials.

## Chapter 8: Reliability, escalation, and recovery

### 8.1 Escalation and human-in-the-loop

Escalate when:

- The customer explicitly asks for a human
- Policy is **ambiguous** and no clear rule applies
- The agent has made no progress after multiple attempts (deterministic loop detection)
- The action is irreversible (deletions, refunds above threshold)
- Sources conflict in a way that cannot be resolved programmatically

Do NOT escalate merely because:

- The customer sounds frustrated (sentiment is not a trigger)
- The model's self-reported confidence is low (**confidence scores are poorly calibrated**, and the exam tests this trap by name)
- The task is complex but sits inside clear policy

The mental model: **complexity is the agent's job; ambiguity is a human's.** Handoffs are structured: state, history summary, what was attempted, why escalation fired.

### 8.2 Error propagation in chains

Covered mechanically in Chapter 2.5; the orchestration-level rules: preserve partial results (three of four successful scans are still valuable), give the coordinator structured context to make recovery decisions, and never let one failure cascade into unrelated subagents.

### 8.3 Crash recovery

Long-running agents checkpoint to a **manifest file**: completed steps, pending steps, intermediate results, timestamp. On restart, the coordinator loads the manifest into the new prompt and resumes from the checkpoint. Two supporting properties:

- **Idempotency**: tool calls safe to replay without duplicate side effects, so re-executing from a checkpoint is harmless.
- **Circuit breaker**: after N consecutive failures of a tool, stop retrying, switch to a fallback, reset after cooldown.
- **Graceful degradation**: a non-critical tool failing should narrow the output ("results exclude the security scan, which was unavailable"), never abort the workflow.

### 8.4 Coverage annotations

When an agent reports on work spanning many items (files reviewed, repos scanned, documents processed), require an explicit coverage annotation rather than trusting silence:

```json
{
  "reviewed": ["auth.py", "sessions.py", "tokens.py"],
  "skipped": [
    { "file": "legacy_crypto.py", "reason": "exceeds single-pass size; queued for focused pass" }
  ],
  "coverage": "3 of 4 files"
}
```

Without the annotation, "no issues found in the audit" and "no issues found in the 60% of the audit that actually ran" are indistinguishable, which is the failure the exam probes. The same principle produced the structured partial-failure responses in Chapter 2.5; coverage annotations extend it from errors to normal operation.

### 8.5 Provenance

When synthesizing from multiple sources: map every claim to its source (URL, document, excerpt, date). When sources conflict, annotate BOTH values with attribution and surface the conflict; silently picking one is the tested anti-pattern. Distinguish quotes, paraphrases, and inferences, and track recency.

### 8.6 Quality assurance beyond the average

A 97% aggregate accuracy can conceal complete failure on a rare document type: if 90% of inputs are easy, the hard 10% can be failing entirely behind a comfortable average. The tested answer is **stratified sampling**: sample by document type AND by field, set thresholds per stratum, and route low-confidence extractions to human review rather than accepting them silently.

---

# Part II: Exam domain notes

Revision-oriented summaries. Each domain lists what you must know (facts) and what you must be able to do (judgment), then the domain's anti-patterns.

## Domain 1: Agentic Architecture & Orchestration (27%)

**Know:** the agentic loop and `stop_reason` semantics; hub-and-spoke rules (isolated contexts, explicit data passing, coordinator-mediated communication); parallel vs sequential vs hybrid execution; fixed vs dynamic decomposition; state-machine modeling; `--resume` vs `fork_session`; token budget mechanics (soft warning ~80%, programmatic hard stop).

**Be able to:** design a loop that terminates on semantics rather than iteration caps; decide what context a subagent genuinely needs; choose parallel or sequential from data dependencies; recognize over-decomposition; place a token budget outside the model's control.

**Anti-patterns:** parsing prose for termination; iteration caps as primary stop; sharing full coordinator context with subagents; few-shot examples to enforce tool ordering; letting one subagent failure cascade.

## Domain 2: Tool Design & MCP Integration (18%)

**Know:** descriptions are the routing mechanism; the 4-5 tool sweet spot and degradation at ~18+; the three `tool_choice` values; the isRetryable error taxonomy; `.mcp.json` (project, committed) vs `~/.claude.json` (user, personal); `${ENV_VAR}` secret expansion; MCP tools vs resources vs prompts; built-in tool purposes.

**Be able to:** write a description with purpose, parameters, boundaries, examples, and error behavior; classify an error's retryability; design a structured error response with partial results; distinguish access failure from empty result; choose the correct MCP capability type for a requirement.

**Anti-patterns:** routing by tool name; the everything-agent with 18+ tools; raw secrets in committed config; generic "error occurred" responses; empty-result-as-success.

## Domain 3: Claude Code Configuration & Workflows (20%)

**Know:** the CLAUDE.md hierarchy and which levels are version controlled; the team-standards-in-user-config trap; `.claude/rules/` path scoping; skill frontmatter (`context: fork`, `allowed-tools`, `argument-hint`); hook events and their `settings.json` syntax; Plan Mode criteria; headless flags (`-p`, `--output-format json`, `--tools` to restrict, `--allowedTools` to pre-approve).

**Be able to:** place a rule at the correct hierarchy level; convert a "Claude must always/never" requirement into the right hook; scope a skill's tools to least privilege; decide Plan Mode vs direct execution from the change's shape; wire a CI review that stays non-interactive and reports only new findings.

**Anti-patterns:** team standards in `~/.claude/CLAUDE.md`; CLAUDE.md guidance where a hook is required; skills with unrestricted tools; CI invocations without `-p`; self-review in the generation session.

## Domain 4: Prompt Engineering & Structured Output (20%)

**Know:** explicit-testable-criteria doctrine; few-shot's scope (format and reasoning yes, compliance no); prompt chaining stages; nullable/unclear/other schema design; the validation-retry loop's inputs; execution errors vs information gaps; the full Batch vs real-time table; multi-instance review rationale.

**Be able to:** rewrite vague guidance into testable criteria; build a 2-4 example few-shot set including negative examples; design a schema that survives missing and ambiguous data; construct a retry prompt; route a workload correctly between Batch and real-time; set up unbiased review.

**Anti-patterns:** "be conservative/thorough" as instructions; few-shot for ordering; retrying to conjure absent data; Batch behind a waiting user; prompt-only JSON formatting; enums with no escape value.

## Domain 5: Context Management & Reliability (15%)

**Know:** lost-in-the-middle and its mitigations; trimming, pruning, progressive summarization, key-fact blocks, scratchpads, subagent offloading; degradation signals; escalation triggers and non-triggers; manifest-based crash recovery; idempotency, circuit breakers, graceful degradation; claim-source provenance and conflict annotation; stratified vs random sampling.

**Be able to:** restructure a prompt so critical facts lead; detect degradation from behavioral signals; write an escalation policy that fires on ambiguity and irreversibility, never on sentiment or self-confidence; design a checkpoint manifest; expose a per-stratum quality view that an aggregate metric hides.

**Anti-patterns:** "bigger context window" as an attention fix; no state persistence in long workflows; aggregate accuracy without stratification; discarding partial results; silent conflict resolution between sources.

---

# Part III: Exam preparation

## The preparation ladder

Five layers, in order. Each builds on the previous, and the free layers take you surprisingly far. Anthropic retired its official practice exam when the exams moved to Pearson VUE; the sample questions in the official exam guide are what remains.

| Step | Resource | Cost |
|------|----------|------|
| 1. Learn the vocabulary | [Anthropic Partner Academy courses](https://claude.com/partners), the official exam guide, and the [Anthropic Academy courses](https://www.anthropic.com/learn) mapped in Resources | Free |
| 2. Go to the source | [The Claude Developer Platform docs](https://platform.claude.com/docs) (API, tool use, Agent SDK, MCP) and [the Claude Code docs](https://code.claude.com/docs) | Free |
| 3. First calibration | [30 practice questions with explanations](./practice-questions.md) in this repo | Free |
| 4. Full calibration | [Six full-length scenario-format practice tests and a 500-card flashcard deck](https://preporato.com/certificates/claude-certified-architect) on Preporato, built on the exact domain weights; the page has free sample questions to try first | Paid |
| 5. Prove it hands-on | [12 auto-graded build-and-submit projects](https://preporato.com/certificates/claude-certified-architect): agentic loops, hub-and-spoke systems, MCP servers, extraction pipelines | Paid |

Steps 1-3 cost nothing and tell you honestly where you stand. Steps 4-5 are how you close the gap they reveal.

## The Golden Rule and five mental models

**The Golden Rule: programmatic enforcement beats prompt-based guidance.** On any question where both appear, the mechanism (hook, gate, schema validation, retry loop, hard stop) beats the instruction. Prompts are probabilistic; mechanisms are deterministic. If a behavior must ALWAYS happen, the answer is never "add it to the system prompt."

Five mental models for evaluating answer choices:

1. **The Determinism Test.** Can this solution fail silently? Then it needs programmatic enforcement.
2. **The Isolation Principle.** Does this subagent need all this context? Minimum necessary context is almost always the right answer.
3. **The Recovery Question.** If this fails at 3 AM with nobody watching, can the system recover? Prefer answers with structured errors, partial results, and checkpoints.
4. **The Attention Budget.** Is the critical information buried mid-context? "Process everything in one pass" loses to focused passes with an integration step.
5. **The Calibration Check.** Does this rely on Claude assessing its own confidence or quality? Replace with external validation and deterministic thresholds.

## The seven anti-patterns

| Anti-pattern | Why wrong | Correct approach |
|--------------|-----------|------------------|
| Few-shot examples for tool ordering | Ordering is compliance; few-shot is probabilistic | Hooks, gates, orchestration |
| Self-reported confidence for escalation | Poorly calibrated | Deterministic thresholds and rule triggers |
| Batch API for user-facing blocking flows | No SLA, up to 24h | Real-time API with streaming |
| Bigger context = better attention | Lost-in-the-middle persists | Focused passes, key facts up front |
| Silent empty results on failure | Forecloses recovery | Structured error context with partials |
| All tools on one agent | Selection degrades from ~18 tools | 4-5 scoped tools, split into subagents |
| Prompt-only JSON formatting | Probabilistic, malformed output possible | Schema-enforced output (structured outputs or a schema-defined tool) plus validation of the values |

## Critical distinctions

| A | B | The difference |
|---|---|----------------|
| `stop_reason: end_turn` | `stop_reason: tool_use` | Done vs continue the loop |
| `tool_choice: any` | `tool_choice: auto` | Must call some tool vs may answer in text |
| `~/.claude/CLAUDE.md` | `.claude/CLAUDE.md` | Personal vs team (version controlled) |
| `context: fork` | Default skill context | Isolated subagent vs main conversation |
| Syntax errors | Semantic errors | Schemas fix the first; review catches the second |
| `isRetryable: true` | `isRetryable: false` | Transient vs validation/permission/logic |
| Batch API | Real-time API | 50% cheaper, up to 24h, no SLA vs instant |
| Plan Mode | Direct execution | Multi-file/architectural vs single-file/obvious |
| Hooks | CLAUDE.md instructions | Deterministic vs probabilistic |
| Stratified sampling | Random sampling | Catches per-type failures vs masks them |
| `--resume` | `fork_session` | Continue same session vs independent branch |
| Access failure | Valid empty result | Different failures demanding different recovery |
| Token hard stop | Token soft warning | Programmatic break vs wrap-up instruction |

## Exam-day strategy

**Time.** 120 minutes, 60 questions, so 2 minutes average. The four scenarios are picked for you at random, so there is nothing to choose: give each about 25 minutes, read the scenario introduction once properly before its first question, and keep the last 15 minutes for flagged items. Change an answer only on a definite error.

**Per question**, check how many responses it asks for, then identify three things before reading the choices: which domain is being tested, whether it asks for the right approach or the anti-pattern, and whether the Golden Rule applies.

**Named trap patterns.** "Update the system prompt to always..." when a mechanism exists. "Increase the context window" for attention problems. "Use Claude's confidence score" for escalation. "Add more few-shot examples" for ordering compliance. "97% accuracy proves it works" without stratification.

## Worked questions

Twelve fresh questions in the exam's style, with reasoning. (These are written for this guide; timed full-length practice is linked in Resources.)

**Q1.** Your agentic loop sometimes runs forever on ambiguous tasks. A teammate proposes `max_iterations = 15` as the fix. What is the strongest objection?

- A) 15 iterations is too low for complex tasks, so the cap should be set a lot higher
- B) The loop should check whether Claude's reply text says the task is finished
- C) Token budgets already make iteration caps redundant in any production loop like this
- D) A cap treats the symptom; `stop_reason` should end the loop, with the cap as a net

**Answer: D.** The loop's primary contract is `stop_reason`. An iteration cap is a legitimate backstop but a poor primary mechanism. Option A argues about the number and misses the principle, B is the prose-parsing anti-pattern, and C confuses two complementary safety nets.

**Q2.** A support agent must hand off to a human whenever a refund exceeds $500. Where does this rule live?

- A) In a programmatic gate that checks the amount before the refund tool runs
- B) In the system prompt: "Always escalate any refund above $500 to a human agent"
- C) In a few-shot example that shows a $600 refund being escalated correctly
- D) In the refund tool's description, next to the parameters it accepts

**Answer: A.** "Whenever" means compliance, and compliance is enforced by mechanism (a check in code before the refund tool runs, the same idea as a `PreToolUse` hook). Options B and C are probabilistic, and D improves selection but cannot enforce a threshold.

**Q3.** Claude must return valid JSON matching a strict schema for every extraction. Which combination guarantees the format?

- A) A system prompt with the schema pasted in and an instruction to follow it exactly
- B) Few-shot examples of correctly formatted output, one for each type of document
- C) Schema-enforced output, such as structured outputs, plus validation of the values
- D) A higher effort level, so that the model checks its JSON before it answers

**Answer: C.** Schema enforcement (structured outputs, or an extraction tool defined with the JSON schema and forced on models that allow it) eliminates syntax errors, and validation catches what a schema can't, such as wrong values. Options A, B, and D are probabilistic.

**Q4.** A document-extraction pipeline keeps failing validation on the `revenue` field for a minority of documents. Investigation shows those documents genuinely contain no revenue figure. The fix?

- A) Retry the failed documents up to five times before marking them as failed
- B) Make `revenue` nullable, and let downstream logic handle its absence
- C) Add few-shot examples that show revenue being extracted correctly
- D) Route those documents to a more capable model that can find the figure

**Answer: B.** This is an information gap. Retries (A) and examples (C) cannot create data absent from the source, and a stronger model (D) cannot either. The schema must absorb reality.

**Q5.** Your coordinator spawns four repository scanners in parallel. One times out. Which return value from the failed scanner best serves the system?

- A) An empty findings list, so that the merge step is not disrupted by the failure
- B) A raised exception that halts the whole audit so someone can investigate it
- C) The message "Scan failed" with a null result in place of the findings
- D) A structured error: the timeout, what was tried, the files done, retry options

**Answer: D.** Partial results plus context (say, the 47 of 120 files it did scan) enable an informed recovery decision. Option A is empty-as-success, C is context-free failure, and B throws away three successful scans.

**Q6. (Select TWO)** Which placements make a team-wide "always run tests before commit" requirement actually binding for everyone?

- A) The project's committed `.claude/CLAUDE.md`
- B) Each developer's own `~/.claude/CLAUDE.md`
- C) A note about testing in the repository README
- D) A few-shot example in each developer's personal config
- E) A `PreToolUse` hook in committed project settings, on `git commit`

**Answer: A and E.** Project-level, version-controlled placement reaches the team (A), and the hook makes it enforcement rather than guidance (E). The hook is the stronger of the two; the CLAUDE.md line alone is probabilistic but at least correctly scoped. Options B and D are personal scope, and C is invisible to Claude in most workflows.

**Q7.** A nightly compliance job summarizes 40,000 support transcripts. Cost is the concern; nobody reads results before morning. Which delivery mechanism?

- A) The Batch API, with a `custom_id` for each transcript
- B) The real-time API with prompt caching on the instructions
- C) The real-time API with streaming, to finish sooner overnight
- D) An agentic loop that works through the transcripts in order

**Answer: A.** Overnight, bulk, no one waiting: Batch's 50% saving with no SLA fits exactly, and `custom_id` maps results back. Options B and C pay real-time prices for latency nobody uses, and D adds orchestration where none is needed.

**Q8.** After 30 minutes of a long code investigation, Claude begins re-running searches it already ran and describing "common patterns in codebases like this" instead of citing files it read. What is happening, and what is the right response?

- A) The model is hallucinating, so the session should move to a larger model
- B) The context window is too small, so it should be raised for this session
- C) Context degradation: use a scratchpad, compact the history, and offload work
- D) The tools are misconfigured, so the search tools should be registered again from scratch

**Answer: C.** Repeated tool calls and generic-pattern language are the named degradation signals; persist key findings to a scratchpad and offload the remaining subtasks to focused subagents. Option B is the bigger-context trap, and A and D misread the signals.

**Q9.** Your extraction system reports 97% accuracy overall, but a customer complains that purchase orders in one regional format are consistently wrong. What does the QA process need?

- A) A higher overall accuracy target for the whole system, such as 99% from now on
- B) A second model that votes on every extraction before it is accepted
- C) Larger random samples, so the regional errors show up more often
- D) Stratified sampling by document type and field, with thresholds per stratum

**Answer: D.** The aggregate hides a per-type failure; only stratification exposes it. Options A and C keep measuring the same masked average, and B adds cost without changing what is measured.

**Q10.** A reviewer agent should evaluate code that a generator agent just produced. Which setup yields the most trustworthy review?

- A) A fresh session that sees only the code, with per-file passes and a cross-file pass
- B) The generator reviews its own output in the same session, since it has the context
- C) The generator reviews in the same session, with a prompt telling it to be fully objective
- D) An independent session that receives the code and the generator's full reasoning

**Answer: A.** Independence requires not inheriting the generation reasoning, and per-file plus integration passes catch both local and systemic issues. Options B and C keep the bias, and D reintroduces it through the transcript.

**Q11.** A compliance team requires that Claude Code can never execute a shell command containing `curl` against production hosts, for any developer, with no exceptions. Which implementation meets the requirement?

- A) A rule in the committed project CLAUDE.md: "Never run curl against production hosts"
- B) A `PostToolUse` hook that reports each violation to the security channel afterwards
- C) A `PreToolUse` hook on Bash in committed project settings that blocks violations
- D) A note in each developer's own `~/.claude/CLAUDE.md`, set up during onboarding

**Answer: C.** "Never, for any developer, no exceptions" is enforcement, and only a blocking `PreToolUse` hook in *committed project* settings delivers it: its script inspects the command and exits 2 (or returns a deny decision), deterministically and before execution. Option A is probabilistic guidance, B fires after the damage, and D is personal scope that reaches nobody else.

**Q12.** A developer keeps personal sandbox URLs and test credentials paths in the project's committed CLAUDE.md "so Claude remembers them", and teammates complain about the noise. Where does that content belong?

- A) A CLAUDE.md in a subdirectory of the project, near the code it concerns
- B) `CLAUDE.local.md` at the project root, listed in `.gitignore`
- C) The system prompt of each session, typed in when the session starts
- D) An `@import` from the committed CLAUDE.md to the developer's home folder

**Answer: B.** Personal, project-specific content has a dedicated home: `CLAUDE.local.md`, loaded alongside the project file and kept out of version control. Option A still ships to the team, C does not persist, and D commits a reference to one person's home directory into the shared file, which breaks for everyone else.

## 30-day study plan

- **Days 1-7: official baseline.** Check that your employer is in the [Claude Partner Network](https://claude.com/partners) (registration needs your company email), complete the Partner Academy architect courses, read the official exam guide, and map your experience against the five domains.
- **Days 8-21: build.** Work through [the Claude Developer Platform docs](https://platform.claude.com/docs) and [the Claude Code docs](https://code.claude.com/docs) with a project open: an agent with tools and a real loop, an MCP server, a Claude Code setup with CLAUDE.md hierarchy, one hook, one skill, and a headless CI invocation. Part I of this guide is your reading companion; the exam rewards people who have hit these failure modes personally. If you want these builds checked, the [hands-on projects](https://preporato.com/certificates/claude-certified-architect) (paid) cover the same ground with automatic rubric grading.
- **Days 22-30: calibrate.** Start with the [30 practice questions](./practice-questions.md) in this repo to see the format, then take [full-length, timed, scenario-format practice tests](https://preporato.com/certificates/claude-certified-architect). Review per-domain results, re-read the matching Part II notes, and spend the final days on your two weakest domains. The night before, review Part III's tables and the [cheat sheet](https://preporato.com/blog/claude-certified-architect-cheat-sheet-2026).

The expanded week-by-week version: [30-day CCA-F study plan](https://preporato.com/blog/cca-f-study-plan-30-day-preparation).

## Pre-exam checklist

You are ready when every line is true:

- [ ] I can explain the agentic loop and why `stop_reason` (never prose parsing or iteration caps) controls termination
- [ ] I know the hub-and-spoke rules: isolated contexts, explicit data passing, coordinator-mediated communication, isolated failure
- [ ] I can choose parallel vs sequential vs hybrid execution from data dependencies
- [ ] I know escalation triggers (ambiguity, irreversibility, explicit request, no progress) and non-triggers (sentiment, self-reported confidence)
- [ ] I know tool descriptions route selection, and 4-5 scoped tools is the reliable range
- [ ] I can state all three `tool_choice` values and their use cases
- [ ] I can classify errors by retryability and design a structured partial-failure response
- [ ] I know the CLAUDE.md hierarchy, what is version controlled, and the team-config trap
- [ ] I know `.mcp.json` vs `~/.claude.json` and `${ENV_VAR}` secret expansion
- [ ] I can distinguish MCP tools, resources, and prompts
- [ ] I know hook events and why hooks beat CLAUDE.md for guarantees
- [ ] I know `context: fork`, `allowed-tools`, and path-scoped rules
- [ ] I know the headless flags: `-p`, `--output-format json`, `--tools` (restrict) and `--allowedTools` (pre-approve)
- [ ] I can rewrite vague prompt guidance into explicit, testable criteria
- [ ] I know few-shot teaches format and reasoning but cannot enforce ordering
- [ ] I know schemas fix syntax errors, review catches semantic errors
- [ ] I can design nullable/unclear/other schemas and a validation-retry prompt
- [ ] I know retries fix execution errors, never information gaps
- [ ] I know the full Batch vs real-time table and both trap directions
- [ ] I know why independent review sessions beat self-review
- [ ] I can explain lost-in-the-middle and its mitigations
- [ ] I can detect context degradation and remediate with scratchpads, compaction, and offloading
- [ ] I can design manifest-based crash recovery with idempotent tools
- [ ] I know why aggregate accuracy masks per-type failures and how stratified sampling fixes it
- [ ] I have the seven anti-patterns and five mental models down cold
- [ ] I have taken at least two full-length timed practice tests and reviewed every miss

## Resources

**Official (free):**
- [Claude Certified Architect - Foundations](https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification) on the Anthropic Partner Academy: the exam guide, prep courses, and registration
- [Claude Developer Platform docs](https://platform.claude.com/docs) (API, agents, tool use, MCP) and [Claude Code docs](https://code.claude.com/docs)
- Anthropic Academy courses, mapped to this exam's domains:
  - [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) and [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action): the 20% Claude Code domain
  - [Introduction to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol) and [MCP: Advanced Topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics): the 18% tool design and MCP domain
  - [Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents) and [Introduction to agent skills](https://anthropic.skilljar.com/introduction-to-agent-skills): orchestration and Claude Code configuration
  - [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api): the API foundation everything else builds on

**Free articles (preporato.com):**
- [CCA-F complete guide](https://preporato.com/blog/claude-certified-architect-complete-guide-2026) · [Cheat sheet](https://preporato.com/blog/claude-certified-architect-cheat-sheet-2026) · [Domains breakdown](https://preporato.com/blog/cca-f-exam-domains-complete-breakdown-2026) · [Exam format](https://preporato.com/blog/cca-f-exam-format-structure-what-to-expect) · [How to pass first attempt](https://preporato.com/blog/how-to-pass-cca-f-first-attempt-2026) · [Hardest topics by attempt data](https://preporato.com/blog/hardest-cca-f-exam-topics-practice-attempt-data-2026)
- Technical guides: [hooks](https://preporato.com/blog/claude-code-hooks-explained-cca-f-guide) · [subagent orchestration](https://preporato.com/blog/claude-code-subagents-orchestration-patterns-cca-f) · [MCP tool design](https://preporato.com/blog/mcp-tool-design-best-practices-cca-f) · [MCP architecture](https://preporato.com/blog/model-context-protocol-mcp-architecture-guide-2026) · [structured output](https://preporato.com/blog/structured-output-prompt-engineering-claude-cca-f) · [CLAUDE.md context management](https://preporato.com/blog/claude-md-context-management-best-practices-2026) · [permissions precedence](https://preporato.com/blog/claude-code-permissions-settings-precedence-guide)

**Practice:**
- [30 practice questions with explanations](./practice-questions.md) in this repo (free)
- [The CCA-F page on Preporato](https://preporato.com/certificates/claude-certified-architect): free sample questions to start, then the full tests below
- (Paid) [Six full-length scenario-format practice tests and a 500-card flashcard deck](https://preporato.com/certificates/claude-certified-architect) built on the exact domain weights
- (Paid) [12 hands-on projects](https://preporato.com/certificates/claude-certified-architect): build-and-submit work (agentic loops, hub-and-spoke systems, MCP servers, extraction pipelines) graded automatically against a rubric

---

*Not affiliated with Anthropic. Exam details reflect the program as of November 2026; the Partner Academy is authoritative. Found an error? [Open an issue](https://github.com/preporato/claude-certification-guide/issues).*
