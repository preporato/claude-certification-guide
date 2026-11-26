# Claude Certified Associate - Foundations (CCAO-F): The Complete Study Guide

A full preparation guide for Anthropic's non-technical certification. Part I teaches the material by topic, one chapter per exam domain. Part II re-indexes it by the official skills for revision. Part III covers trap answers, worked questions, and a final checklist.

Maintained by [preporato.com](https://preporato.com). Facts checked in November 2026 against the official exam guide (version 1.1, effective December 7, 2026) and Anthropic's program pages.

> **Which version this guide covers.** CCAO-F changes on December 7, 2026: 70 questions instead of 60, and six domains instead of seven. This guide follows the new blueprint. Testing on or before December 6? Read [Taking CCAO-F before December 7](#taking-ccao-f-before-december-7) first; almost everything here still applies.

---

## Contents

- [Introduction](#introduction)
- [Exam format](#exam-format)
- [Taking CCAO-F before December 7](#taking-ccao-f-before-december-7)
- **Part I: The material**
  - [Chapter 1: Defining the task and prompting](#chapter-1-defining-the-task-and-prompting)
  - [Chapter 2: Evaluating outputs and controlling quality](#chapter-2-evaluating-outputs-and-controlling-quality)
  - [Chapter 3: Choosing capabilities, models, and context](#chapter-3-choosing-capabilities-models-and-context)
  - [Chapter 4: Designing workflows](#chapter-4-designing-workflows)
  - [Chapter 5: Projects, knowledge, Skills, and memory](#chapter-5-projects-knowledge-skills-and-memory)
  - [Chapter 6: Responsible use, data protection, and governance](#chapter-6-responsible-use-data-protection-and-governance)
- **Part II: Exam domain notes**
  - [All six domains](#part-ii-exam-domain-notes)
- **Part III: Exam preparation**
  - [The preparation ladder](#the-preparation-ladder)
  - [The eight trap answers](#the-eight-trap-answers)
  - [Exam-day strategy](#exam-day-strategy)
  - [Worked questions](#worked-questions)
  - [3-week study plan](#3-week-study-plan)
  - [Pre-exam checklist](#pre-exam-checklist)
  - [Resources](#resources)

---

## Introduction

CCAO-F (Claude Certified Associate - Foundations) is the one Claude certification requiring no code, no API knowledge, and no engineering background. It validates that a professional can use Claude as a core productivity tool in a business role: turning objectives into well-specified requests, judging outputs before acting on them, choosing the right capability and model, setting Claude up for repeatable work, and applying data-protection and governance judgment every day.

Do not mistake non-technical for easy. The heaviest domain is **evaluating outputs**, and governance is the second heaviest after workflow design. Questions describe a work situation and ask what a careful professional does next: catch a fabricated citation before it reaches a client, decide which workflow step a person must keep, de-identify a dataset before analysis, or trace a quality drop to the configuration layer that changed. Candidates who prepare only on features routinely get caught by exactly those questions.

**Who should take it:** business analysts, project managers, operations leads, consultants, and professionals in marketing, communications, HR, and education who use claude.ai (web, desktop, or mobile) regularly and build Projects for their own work. Anthropic recommends regular hands-on professional use; there is no formal prerequisite.

The official guide builds every domain on Anthropic's **AI Fluency Framework** and its four competencies: **Delegation** (what to hand to Claude and what to keep), **Description** (specifying the work), **Discernment** (judging the output), and **Diligence** (owning the result). If a question feels ambiguous, ask which of the four it is testing.

## Exam format

| | |
|---|---|
| Questions | 70: 60 scored and 10 unscored trial items you cannot tell apart |
| Duration | 120 minutes to answer, about 135 minutes of seat time |
| Question style | Scenario-based; each item states how many responses to select, and multi-select items get no partial credit |
| Passing score | 720 on a 100-1000 scaled score; the score report adds percent correct per domain |
| Delivery | Pearson VUE, online proctored (OnVUE) or at a test center |
| Price | $99 per attempt, the lowest in the program |
| Registration | Anthropic Partner Academy, open to people who work at Claude Partner Network organizations (sign in with a company email); you pay at Pearson's checkout |
| Languages | English or Japanese, chosen when you schedule |
| Rescheduling | Free up to 1 hour before an OnVUE appointment, 48 hours before a test center one |
| Retakes | Full fee for every attempt; waits of 14, 30 and 90 days after the first, second and third failed attempts; at most 4 attempts in any 12 months |
| Validity | 12 months; free non-proctored renewal before expiration, full proctored exam after a lapse |
| Scope | claude.ai as a business tool. Programming and API topics are excluded, and no item asks you to recall prices, context-window sizes, or rate limits |

### Exam domains

| Domain | Weight | ~Scored questions | Core focus |
|--------|--------|-------------------|------------|
| 1. Task Definition and Prompting | 15% | ~9 | Prompt structure, staged deliverables, diagnosing weak prompts |
| 2. Output Evaluation and Quality Control | 20% | ~12 | Fitness for purpose, hallucinations, review depth, output format |
| 3. Capability, Model, and Context Selection | 15% | ~9 | Capabilities, model tier and effort, context and memory |
| 4. Workflow Design and Integration | 18% | ~11 | Deliverable workflows, delegation, repeatable workflows, honest expectations |
| 5. Configuration and Knowledge Management | 15% | ~9 | Projects, connectors, persistent instructions, configuration that degrades |
| 6. Responsible Use, Data Protection, and Governance | 17% | ~10 | Use-case appropriateness, sensitive data, policy and Diligence |

No domain falls below 15%, so none can be skipped.

## Taking CCAO-F before December 7

Exams through December 6, 2026 follow the earlier guide: **60 questions, all scored**, in 120 minutes, across seven domains.

| Domain (until December 6) | Weight | Where it lives in this guide |
|---|---|---|
| Output Evaluation and Validation | 21% | Chapter 2 |
| Workflow Integration and Solution Design | 16% | Chapter 4 |
| Governance, Risk, and Responsible Use | 15% | Chapter 6 |
| Prompting and Task Execution | 14% | Chapter 1 |
| Product and Model Selection | 12% | Chapter 3 |
| Configuration and Knowledge Management | 12% | Chapter 5 |
| Troubleshooting and Optimization | 10% | The diagnosis table in Chapter 1 and the degradation playbook in Chapter 5 |

The judgment rules are the same in both versions. What the new version adds is breadth: Skills, memory and incognito chats, code-executed analysis, effort levels, delegation labels for every workflow step, and configuration that degrades over time. On the earlier exam those appear rarely or not at all, and product questions center on chat, Projects, research, Artifacts, connectors, and the three model tiers. For the earlier exam, also practice streamlining a process that already works: fewer prompts, stable background moved into a Project, a saved template the team reuses.

---

# Part I: The material

## Chapter 1: Defining the task and prompting

### 1.1 The business prompt

A strong prompt names five things, plus whatever Claude cannot know by default:

1. **Role or context:** "You are helping a project manager prepare a stakeholder update"
2. **Task:** what to produce
3. **Source material:** the notes, report, or data to work from
4. **Constraints:** audience, length, tone, what to leave out
5. **Output format:** bullets, table, one-pager, email

The sixth ingredient is **the context Claude does not have**: your client's history, your internal terms, the decision the output will feed. Claude knows a great deal about the world and nothing about your organization unless you say it.

Before and after, on the same task:

> **Weak:** "Summarize these meeting notes."

> **Strong:** "You are helping a project manager prepare a stakeholder update. Summarize the attached meeting notes for the executive team in five bullet points. Each bullet names the decision made, the owner, and the deadline. Formal tone, no jargon, nothing that was only discussed without a decision. The executives already know the project; they need to know what changed."

Every improvement in the output traces back to one of those additions, which is how the exam expects you to diagnose weak prompts in reverse.

### 1.2 Task decomposition and sequencing

Split a deliverable that is too large or too varied for one request into **staged prompts**, each producing something you check before moving on. A quarterly report becomes: agree an outline, draft one section at a time from its source material, then a final pass for tone and consistency. The **checkpoints between steps** are part of the skill: an error caught at the outline stage costs one minute, the same error found in the finished report costs an afternoon. Decomposition is the tested answer whenever one giant prompt returned a shallow or partial result. For recurring multi-step work, the stages can live in a Project (Chapter 5).

Strategy also changes by task type:

| Task type | Adjust the prompt to |
|-----------|---------------------|
| Analysis | Provide the data, name the criteria to weigh, ask for reasoning before conclusions |
| Research | Use research for current information and require sources you can check |
| Drafting | Specify audience, tone, length, and format; share an example of good work |
| Brainstorming | Ask for volume and variety first, evaluate and narrow in a second step |

### 1.3 Diagnosing a weak prompt

Diagnose before you fix. The official guide names four specification gaps, and each has a first fix:

| Symptom | Specification gap | First fix |
|---------|------------------|-----------|
| Generic output that could fit any company | Missing context | Add the audience, source material, and an example of good output |
| Two runs read the request differently | Ambiguous instruction | Say exactly what to produce and what to leave out |
| Too long, wrong tone, or a different structure each time | Absent constraint | State length, tone, and structure, or show a concrete sample |
| A list of facts when you needed options | Wrong strategy for the task type | Switch strategy: brainstorm, analysis, drafting, or research |
| Instructions ignored late in a long chat | The conversation history has become noise | Restart with a summary; move standing rules into the Project |
| Half of a multi-part request ignored | Too many asks in one prompt | Decompose and run the steps in sequence |

Then choose the remedy:

- **Iterate** when the output is close: give specific feedback ("cut this to half the length, make the tone more direct, keep the three statistics"). Regenerating and hoping gives Claude nothing to act on.
- **Restart** when the conversation has drifted or filled with abandoned drafts.
- **Change approach** when the task needs a different capability or a staged workflow.

And change **one thing at a time**. Change the prompt, the model, and the knowledge together, and you learn nothing about which change mattered.

## Chapter 2: Evaluating outputs and controlling quality

The heaviest domain, and one habit underneath it: **every output is a draft that must earn trust before it leaves your screen.** The official guide asks you to classify an output as **ready to use**, **requiring revision**, or **requiring human correction**, judged against its requirements, its source material, or professional standards: accuracy, completeness, relevance, and fitness for its purpose.

### 2.1 What a hallucination looks like

A hallucination is a confident, plausible statement that is wrong or unsupported. The exam expects recognition from symptoms alone:

- **Highly specific numbers, dates, or statistics with no source.** Precision signals confidence and says nothing about accuracy.
- **Named studies, publications, or quotations you have not checked.** Fabricated citations read exactly like real ones until you look them up.
- **Details beyond the material you provided.** If the summary of a report mentions figures the report never contains, Claude filled the gap itself.
- **Uniform confidence across every claim.** The weakest guesses arrive in the same fluent tone as established facts.
- **Inconsistencies and bias:** figures that disagree between sections, one-sided analysis, or two people described in different language for the same performance.

A worked example, in the form the exam uses. You attached this excerpt from a quarterly report:

> Q2 revenue was $4.2M, up from Q1. The Enterprise segment led growth. We closed 14 new enterprise accounts during the quarter.

Claude's summary reads:

> Revenue grew 18% quarter-over-quarter to $4.2M, driven by the Enterprise segment, which closed 14 new accounts including two Fortune 500 logos. According to a Gartner study, this growth rate places the company in the top decile of its peer group.

Three hallucinations, each matching a red flag: **"18%"** is a figure the source never states (it says only "up from Q1"), **"two Fortune 500 logos"** goes beyond the material, and **the Gartner study** is a citation you will not locate. The revenue figure, the segment, and the account count are grounded. The tone is identical across all six claims, which is why tone can never be the filter.

### 2.2 Verification

Check every name, number, date, and quotation against the original source or an authoritative reference, and remove or flag anything you cannot confirm. Two rules the exam leans on:

- **Asking Claude to confirm its own output is not independent verification.** You can ask Claude to point to the passage that supports a claim, but then read that passage yourself.
- **Citations prove nothing until checked.** Their presence makes an output look trustworthy without making it so.

Watch for bias as well as error: one-sided analysis, stereotyped examples, and missing counterarguments are evaluation failures too.

### 2.3 Review depth and escalation

How hard you review depends on two things: **the consequence of an error** and **where the output goes**. An internal brainstorm can go after a skim. These need a qualified person to verify, correct, or escalate before use:

- anything external-facing (client emails, published copy, press material)
- anything with legal, financial, medical, or contractual consequences
- anything feeding a decision about people (hiring, performance, vendor selection)
- anything in a regulated workflow

You stay accountable for whatever you ship, however good it looks.

### 2.4 Adapting the output and choosing its format

A raw output is rarely the deliverable. Edit and adapt it for its audience and channel, and pick the format by what happens next:

| Format | Fits |
|--------|------|
| Inline response | A quick answer or short summary you read once |
| Artifact | A document, table, or page you will revise, export, and share |
| Structured data | Output someone will sort, compare, or feed into another step |
| Code-executed result | Totals, percentages, and forecasts that must be exact |
| Skill-produced document | A deliverable that must follow a team format or template |

The code-executed row matters: arithmetic written out in prose is an estimate. When figures must be exact, have Claude compute them with code execution on the data, and still sanity-check anything that leaves the building.

## Chapter 3: Choosing capabilities, models, and context

### 3.1 Capability selection

| Capability | What it is | Reach for it when |
|------------|-----------|-------------------|
| Chat | A single conversation | A one-off question or quick draft, no saved setup |
| Projects | A workspace with instructions, knowledge, Skills, and its own memory | The same context, documents, or standards recur across sessions |
| Artifacts | A side panel holding a standalone, editable deliverable | A document or table to refine over rounds and share |
| Research | Claude searches many sources and returns a cited report | You need current, verifiable information |
| Code-executed analysis | Claude writes and runs code on your uploaded files | You must analyze a data file or compute exact numbers |
| Skills | Packaged instructions and templates Claude applies when relevant | A procedure or format should be applied the same way every time |
| Connectors | Links to sources such as Google Drive, Gmail, and calendar | Material lives in those tools and changes often |
| Memory | Context Claude carries from past chats | Background should follow you without being pasted again |

Many scenarios need a **combination**: a Project with a connector and a Skill, plus code execution for the figures. Pick what the task needs and leave out the rest; more capabilities is not a better answer.

### 3.2 Model and effort selection

| Model | Optimizes for | Pick it for |
|-------|--------------|-------------|
| Haiku | Speed and low cost | Quick, well-defined tasks at volume: reformatting, short summaries, first-pass triage |
| Sonnet | Balance of quality, speed, and cost | The everyday default: drafting, analyzing reports, synthesizing notes |
| Opus | Deepest reasoning, highest quality | Complex, high-stakes work: multi-document strategy, plans where an error is expensive |

**Effort** works the same way: more effort means more thinking before the answer, which helps hard problems and slows simple ones. Match tier and effort to the task's complexity and stakes, and recognize when the faster, cheaper option is the right one. The most powerful setting for every task is a recurring wrong answer, and the exam asks you to **defend** a choice against the alternatives, so know why the other options lose. A model upgrade cannot fix missing context or stale knowledge; it only changes reasoning quality.

### 3.3 Context and memory management

The context window is how much conversation and attached material Claude can consider at once, and long sessions strain it. Four moves:

- **Restart** a fresh chat when a long conversation drifts or ignores instructions.
- **Summarize** the decisions so far and carry the summary into the new chat.
- **Persist** durable reference material to a Project, so no single conversation has to hold it.
- **Rely on memory** for background that should follow you across chats.

Memory needs upkeep. **Review** what Claude remembers, **edit or delete** memories that are wrong or outdated, and keep unrelated work apart (each Project has its own memory). For work that should stay out of your history and memory altogether, use an **incognito chat**. Know its limit: incognito controls what is *kept*. Anything you typed or uploaded in it has still been shared.

## Chapter 4: Designing workflows

### 4.1 End-to-end deliverables

Design questions start from the requirements: the deliverable, the audience, the source material, the quality bar, and the deadline. An answer that jumps straight to prompting without defining the task is wrong at this level. A full research or planning deliverable then runs through stages Claude supports: requirements, research with cited sources, data analysis through code execution, and synthesis into a plan someone can act on, with your checks between stages.

| Strong fit | Weak fit |
|-----------|----------|
| First drafts of emails, briefs, reports, plans | Final authority on factual accuracy |
| Summarizing meetings, long documents, research | Decisions requiring human accountability (hiring, legal, spend) |
| Reformatting and repurposing content across channels | Exact figures estimated in prose instead of computed with code execution |
| Brainstorming options, angles, counterarguments | Current events and live data, unless research or a connector grounds them |

### 4.2 Delegation: who does each step?

The Delegation competency gives four criteria for every step of a workflow: **reversibility**, **stakes**, the need for **human judgment or empathy**, and **accountability**. Each step gets one of three labels:

| Assignment | Use when | Example |
|------------|----------|---------|
| AI-executed | Easily reversed, low stakes, no judgment or empathy needed | Consolidating team updates into a first draft |
| Human-reviewed | Claude does it well, but errors would matter | A client email Claude drafts and a person checks before sending |
| Human-retained | Irreversible, high stakes, needs empathy or a named owner | Telling an employee about a layoff, approving spend, a hiring decision |

**Over-delegation** is a tested failure: Claude sending, deciding, or approving a consequential step with nobody checking. A workflow redesign that hands a human-retained step to Claude is wrong however efficient it looks.

### 4.3 Repeatable workflows

A recurring task done by retyping prompts gives different results every week and dies when its owner goes on leave. Turn it into a setup: a **Project** for the standing context, a **Skill** for the procedure and format, a **connector** for sources that change, and **code-executed steps** for the numbers. The tests of a good repeatable workflow are consistency across runs and across users, and whether a colleague can own it after handoff without asking you how it works.

### 4.4 Communicating capability

Stakeholders new to AI need an honest picture. Pair a concrete outcome ("about three hours saved each week on meeting summaries") with an honest limit ("outputs can contain errors, so a person reviews anything external"), and say what human oversight stays in place. **Overstating** sets up disappointment and misuse; **understating** loses a sound use case. Both are wrong answers. And **pilot before rollout**: one workflow, measured before and after, then expand. Big-bang adoption loses to a measured pilot.

## Chapter 5: Projects, knowledge, Skills, and memory

### 5.1 Configuring a Project

A Project has four configurable parts:

- **Instructions:** standing directions for every chat (role, tone, required formats)
- **Knowledge:** uploaded or connected documents Claude draws on
- **Skills:** packaged procedures and templates applied the same way each time
- **Scoped memory:** what Claude remembers within that Project

The classic question is knowing which layer a requirement belongs in:

| You want to... | Put it in |
|----------------|-----------|
| Apply a tone, role, or format rule to every chat | Project instructions |
| Make reference documents available to every chat | Project knowledge |
| Apply a step-by-step procedure or document template the same way each time | A Skill |
| Give details that matter only for today's task | The individual prompt |
| Use files or email that change often | A connector (Google Drive, Gmail) |
| Keep one client's context away from another's | Separate Projects, each with its own memory |

### 5.2 Persistent instructions

Persistent instructions hold what must stay uniform; the per-request prompt holds what changes. Good Project instructions anticipate the use cases and constraints the team will hit, so outputs stay consistent without each person restating rules. An example for a marketing team's content workspace:

> You are a content editor for Meridian Software's marketing team. In every chat:
> - Follow the brand voice guide in Project knowledge; flag any request that conflicts with it
> - Audience is IT decision-makers; avoid consumer-marketing tone
> - All statistics must come from the attached fact sheet; if a claim is not there, say so instead of estimating
> - Default deliverable format: headline options first, then body copy, then a three-line summary for approvals

Standing role, standards, a guardrail against invented statistics, and a default format. The documents those instructions name (the voice guide, the fact sheet) live in knowledge; today's campaign brief goes in the chat.

### 5.3 Uploads versus connectors

An **upload** is a fixed snapshot you curate: stable, controlled, and stale the day the source changes. A **connector** stays current but can pull in noise. Either way, keep knowledge **current, relevant, and uncluttered**: two versions of a price list in the same Project will eventually produce an answer from the wrong one.

### 5.4 When a working setup gets worse

A configuration that produced good work for months can degrade. Find the layer that changed before you change anything:

| Symptom | Likely layer | Fix |
|---------|-------------|-----|
| Cites a retired price list or old product name | Stale knowledge | Replace or remove the outdated document |
| Uses another client's terms or details | Memory accumulated across work streams | Delete those memories and separate the work streams |
| Formatting changed after a template update | Skill version | Check and fix the Skill version the Project uses |
| Rules applied inconsistently after an edit | Instructions | Review the recent instruction change |

Rewriting instructions nobody edited, or switching to a stronger model, cannot explain a sudden drop in a setup that used to work. And if you changed three things at once and quality fell, undo them and change one at a time.

## Chapter 6: Responsible use, data protection, and governance

One habit carries most of this domain: **check the policy before you paste.** When unsure whether data is sensitive, treat it as sensitive.

### 6.1 Is this use case appropriate?

Classify a proposed use as **appropriate**, **appropriate with safeguards**, or **inappropriate**, and write down why. The criteria:

- **Task suitability:** is this something Claude does reliably?
- **Delegation limits:** does it hand Claude a human-retained decision?
- **Trust in third-party Skills and connectors:** who built it, and what can it reach? Vet them like any software that touches company data.
- **The Anthropic Usage Policy:** some uses are off-limits whatever your internal policy says.

### 6.2 Data protection in practice

| Area | Do | Don't |
|------|----|-------|
| Data sensitivity | Check your organization's AI policy and data classification before sharing | Paste customer records, financials, or trade secrets for convenience |
| Personal data | De-identify first: remove names and addresses, replace identifiers with codes, screen free-text fields | Upload identifiable data and ask Claude to anonymize it afterwards |
| Code-executed analysis | Prepare the dataset to policy before you upload it | Treat a spreadsheet as safer than a document because it is "just numbers" |
| Incognito and memory | Use incognito chats and memory settings to control what is kept | Treat incognito as permission to share what policy forbids |
| Appropriate use | Draft, summarize, analyze, and brainstorm with review | Let Claude be the sole decision-maker on hiring, legal, or medical questions |
| Transparency | Follow your organization's rules on disclosing AI assistance | Present AI-generated work as independently verified when it is not |

Free-text fields deserve their own line: exit-interview comments, support tickets, and meeting notes carry names and identifying details that a column-by-column check misses.

### 6.3 Policy, ethics, and Diligence

When usage goes wrong, name the gap before choosing the fix:

- **Policy gap:** no rule covers the situation (a new connector, a new kind of data). Fix the policy, and escalate to its owner in the meantime.
- **Training gap:** the rule exists and people miss it. Fix the training, not the policy.

Ethical risks include **bias** (disparate treatment in outputs about people) and **transparency failures** (AI-assisted work presented as independent). **Diligence** means you own AI-assisted work: skipping the checks the stakes require is a Diligence lapse, whatever the tool produced.

Two decision rules cover most scenarios: if an output affects people's **rights, money, health, or legal standing**, a qualified person owns the final call. If data would cause harm were it **leaked**, the policy check comes before any productivity benefit.

---

# Part II: Exam domain notes

## Domain 1: Task Definition and Prompting (15%)

**Skills tested:** Prompt Construction; Task Decomposition and Sequencing; Prompt Diagnosis and Iteration.

**Know:** the five-part prompt plus the context Claude does not have; decomposition triggers and checkpoints; strategy by task type; the four specification gaps (missing context, ambiguous instruction, absent constraint, wrong strategy).

**Be able to:** rewrite "summarize this" into a complete prompt; stage a large deliverable with checks between steps; attribute a weak output to its gap and choose iterate, restart, or change approach.

**Anti-patterns:** one giant prompt; regenerate-and-hope; changing several variables at once.

## Domain 2: Output Evaluation and Quality Control (20%)

**Skills tested:** Output Evaluation and Fitness for Purpose; Hallucination Detection and Verification; Review Depth and Escalation; Output Adaptation and Format Selection.

**Know:** the five red flags; the ready / revision / human-correction classification; the mandatory-review list; the five output formats, including code-executed results for exact figures and Skill-produced documents.

**Be able to:** spot a fabricated citation or ungrounded figure from symptoms; verify against the source rather than against Claude; set review depth from the consequence of an error and the destination.

**Anti-patterns:** trusting fluency or the presence of citations; asking Claude to confirm itself; deleting every specific instead of verifying them.

## Domain 3: Capability, Model, and Context Selection (15%)

**Skills tested:** Capability Selection; Model and Effort Selection; Context and Memory Management.

**Know:** the eight capability triggers; the three model tiers and what effort changes; the four context moves (restart, summarize, persist, rely on memory); what incognito does and does not do.

**Be able to:** pick the capability combination a scenario needs; defend a tier and effort choice against the alternatives; keep memory clean by reviewing, editing, and deleting.

**Anti-patterns:** strongest-setting-everywhere; rebuilding context by hand every session; letting stale memories steer new work.

## Domain 4: Workflow Design and Integration (18%)

**Skills tested:** End-to-End Deliverable Workflows; Delegation and Workflow Redesign; Repeatable Workflow Design; Capability Communication.

**Know:** the strong-fit / weak-fit table; the four delegation criteria and three labels; what makes a workflow repeatable and handoff-ready; value-plus-limits stakeholder framing; pilot-then-expand.

**Be able to:** define requirements before prompting; label each step AI-executed, human-reviewed, or human-retained; spot over-delegation; turn a manual recurring task into a Project, Skill, connector, and code-executed setup.

**Anti-patterns:** Claude as final factual authority; Claude approving or sending consequential output unchecked; big-bang rollouts; overstating or understating capability.

## Domain 5: Configuration and Knowledge Management (15%)

**Skills tested:** Project Configuration; Connector and Knowledge Management; Persistent-Instruction Design; Configuration Lifecycle and Degradation.

**Know:** instructions vs knowledge vs Skill vs prompt vs connector; upload-versus-connector trade-offs; separate Projects for separate work streams; the degradation playbook.

**Be able to:** place any requirement in its layer; keep knowledge current and uncluttered; trace a quality drop to stale knowledge, accumulated memory, a Skill version, or an instruction edit.

**Anti-patterns:** standing rules retyped per chat; static uploads of fast-changing sources; rewriting unchanged instructions or upgrading the model to fix a stale document.

## Domain 6: Responsible Use, Data Protection, and Governance (17%)

**Skills tested:** Use-Case Appropriateness; Data Protection in Practice; Policy, Ethics, and Diligence.

**Know:** the three-way use-case classification and its four criteria; the do / don't matrix; de-identification steps, free-text fields included; policy gap vs training gap; the two decision rules.

**Be able to:** de-identify a dataset before upload; vet a third-party Skill or connector; escalate a case the policy does not cover; pick the corrective action that closes the gap you identified.

**Anti-patterns:** paste-first; anonymize-after-upload; incognito-makes-it-safe; Claude as sole decision-maker; presenting AI work as independently verified.

---

# Part III: Exam preparation

## The preparation ladder

Four layers, in order. Each builds on the previous, and the free layers take you surprisingly far. Anthropic retired its official practice exam when the exams moved to Pearson VUE; the three sample questions in the official exam guide are what remains.

| Step | Resource | Cost |
|------|----------|------|
| 1. Learn the vocabulary | The official exam guide and Partner Academy prep courses, plus the [Anthropic Academy courses](https://anthropic.skilljar.com/) mapped in Resources | Free |
| 2. Go to the source | The claude.ai Help Center (Projects, Skills, research, code-executed analysis, connectors, memory and incognito) and the Anthropic Usage Policy | Free |
| 3. First calibration | [30 practice questions with explanations](./practice-questions.md) in this repo | Free |
| 4. Full calibration | [Full-length timed practice tests and a 500-card flashcard deck](https://preporato.com/certificates/claude-certified-associate-foundations) on Preporato, including 70-question tests on the December 7 blueprint; the page has free sample questions to try first | Paid |

Steps 1-3 cost nothing and tell you honestly where you stand. Step 4 is how you close the gap they reveal.

## The eight trap answers

| Trap | Why it fails |
|------|-------------|
| Trust-the-output | Fluency and citations are not verification; consequential output gets checked |
| Self-verification | Claude confirming its own figures is not an independent check |
| Strongest-setting-everywhere | The top model or highest effort for every task ignores speed and cost |
| One-giant-prompt | Multi-part deliverables get staged into checkable steps |
| Incognito-makes-it-safe | Incognito controls what is kept; what you shared is still shared |
| Fix-what-did-not-change | A quality drop comes from the layer that changed, usually knowledge or memory |
| Paste-first | The policy check precedes the productivity win |
| Over-delegation | A consequential step needs a person reviewing or deciding |

On items that ask for more than one response, test each option on its own: one trap option among your picks costs the whole question, because there is no partial credit.

## Exam-day strategy

70 questions in 120 minutes is about 1.7 minutes each. Ten are unscored trial items you cannot spot, so give every question full attention. Stems are short scenarios, and the risk is pattern-matching on a feature when the question is about judgment. Before answering, ask which domain this is; if the scenario involves facts, people, or sensitive data, expect the right answer to include a safeguard. Read how many responses the item asks for before you read the options. Flag long deliberations, return at the end, and change an answer only when you find a definite error.

## Worked questions

Twelve fresh questions in the exam's style. (Written for this guide; timed full-length practice is linked in Resources.)

**Q1.** Claude summarizes your attached quarterly report and includes a revenue growth percentage. The report contains no such percentage. What happened, and what is the correct response?

- A) A hallucination filled a gap in the source; remove the figure or check it against the original
- B) Claude calculated it from the report's figures, so it can go into the summary as it stands
- C) The model used more recent data than the report had, so the newer number is worth keeping
- D) A formatting error moved the figure; regenerate the summary and see whether it comes back again

**Answer: A.** Details beyond the provided material are a named red flag. Option B assumes a calculation nobody verified, C invents a data source Claude does not have in this chat, and D rerolls without addressing the accuracy problem.

**Q2.** A manager wants Claude to rank the team's five sales reps for a promotion decision, using performance notes. The correct guidance?

- A) Fine, as long as the performance notes are anonymized before they go into the chat
- B) Fine, as long as Opus is used, since the decision needs the deepest reasoning available
- C) Refuse to use Claude anywhere near performance data, for this decision or any other one
- D) Claude can organize the notes, but a decision about people stays with the manager

**Answer: D.** Decisions about people sit on the human-retained list: Claude can summarize and organize, and the manager owns the judgment and the final call. Option A solves a privacy slice of the problem and misses the accountability core, B upgrades the model without changing who decides, and C overcorrects past the uses that remain fine.

**Q3.** A colleague pastes a customer list with emails and contract values into a chat "to save time formatting it." What should have happened first?

- A) Switching to a more capable model, so the formatting of the contract values comes out accurate
- B) Turning on research, so that Claude can verify each of the customer records against the web
- C) Checking the AI data policy, and de-identifying the sensitive fields if the task allows
- D) Nothing in particular, since formatting a list is a low-risk task with no decisions in it

**Answer: C.** Paste-first is the trap: leak-harmful data (customer records, financials) triggers the policy check before any convenience. The task being "just formatting" (D) changes nothing about what was shared, and options A and B change tools without asking whether the data should be there.

**Q4.** Your prompt "write a blog post about our new product" returned something generic enough to describe any company's product. The most effective fix?

- A) Regenerate the response a few times until a more specific version of the post appears
- B) Add role, audience, tone, length, the product sheet, and an example post you like
- C) Switch to the most capable model at the highest effort, so the post has more depth
- D) Split the request across three chats: one for the intro, one for the body, one for the close

**Answer: B.** Generic output means missing context and constraints; the five-part prompt is the fix. Option A is regenerate-and-hope, C is strongest-setting-everywhere, and D decomposes without adding the missing context.

**Q5.** Every week you produce the same client status update: same tone rules, same format, drawing on the same background documents. Today you retype the instructions and re-upload the files. The better setup?

- A) A saved text file of the prompts and file names, pasted into each new chat every week
- B) One very long chat, reused every week, so that Claude remembers the earlier updates
- C) Research mode, which remembers the sources it used and brings them back each week
- D) A Project, with tone and format in instructions and the documents in knowledge

**Answer: D.** Recurring context is the Projects trigger, and the instructions/knowledge split matches standing rules versus reference material. Option A still rebuilds by hand, B walks into context drift, and C misdescribes research.

**Q6. (Select TWO)** Which two situations make human review mandatory rather than optional?

- A) A response to a customer complaint about billing, sent under the company's name
- B) A draft agenda for an internal team meeting next week
- C) A brainstorm of taglines for an internal workshop on teamwork
- D) A reformatted version of your own notes from yesterday's call
- E) A summary feeding a decision on which vendor contract to terminate

**Answer: A and E.** External-facing communication with financial context (A) and input to a consequential decision about money and vendors (E) both require review. Options B, C, and D are low-stakes internal drafts.

**Q7.** Twenty exchanges into a long chat, Claude starts ignoring the formatting rules you set at the beginning. Best response?

- A) Repeat the rules more forcefully in the next message, in capitals, so they stand out
- B) Switch to a faster model, since the slowdown in a long chat is what causes the lapses
- C) Restart with a summary of decisions, and move the standing rules into Project instructions
- D) Ask Claude why it is ignoring the rules, and carry on once it has explained the reason to you

**Answer: C.** Late-chat instruction loss is context drift; restart, summarize, and persist is the fix, and standing rules belong in the layer that survives across chats. Option A treats a structural problem as an emphasis problem, B changes speed rather than context, and D asks Claude to explain something it can't observe.

**Q8.** You need current pricing for three competitors, announced within the last month, for a comparison table you will present. Which approach fits?

- A) Use research for current sources with citations, then check the pages cited
- B) Ask Claude directly and trust its training knowledge for all three of the prices
- C) Use Opus, whose training knowledge is the most recent of the models
- D) Ask the same question three times and keep the answers that agree

**Answer: A.** Recent, verifiable information is the research trigger, and the citations still get checked before an external deliverable. Options B and C rely on training data for recent facts (a more capable model does not change what it was trained on), and D mistakes consistency for accuracy.

**Q9.** Your team's five analysts produce weekly client reports with Claude, and quality varies wildly: different tones, different structures, statistics of unclear origin. Which single change addresses all three symptoms?

- A) Have the strongest analyst review everyone's reports before they are sent out to the clients
- B) Standardize all five analysts on the most capable model, at the highest effort level
- C) A shared document of good prompt examples that each analyst can copy from each week
- D) A shared Project: tone and structure in instructions or a Skill, sources in knowledge

**Answer: D.** Variance across teammates on the same task means there is no shared setup, and a shared Project fixes tone and structure (instructions, or a Skill for the report format) and data provenance (knowledge) in one move. Option A adds a bottleneck without fixing the source, B changes quality but not consistency, and C depends on five people copying correctly forever.

**Q10.** A colleague asks Claude for your company's Q3 market share, gets "23.4%, per IDC's industry tracker," and pastes it into a board slide. No source was attached. What should have happened?

- A) Nothing more, since the named source and the precise figure together make the number credible
- B) Treat it as unverified and check it against the actual IDC data before it reaches the board
- C) Ask Claude to double-check its own number in the same chat, and keep it if it agrees
- D) Rephrase the question in a new chat and compare the two answers before using either

**Answer: B.** Specific number, named source, no grounding: two red flags at once, headed for a high-stakes audience (research with checkable citations is the other route). Option A trusts the tell that most needs checking, C is self-verification, and D mistakes consistency for accuracy.

**Q11.** Three months after your company's AI policy banned uploading customer contracts, a review finds several account managers still upload them to summarize renewal terms. The policy wording is clear and was circulated by email. What closes the gap?

- A) Rewrite the policy in stronger language, and circulate it again with a read receipt
- B) Block Claude for the whole sales team until the contract uploads stop across every account
- C) Train them on what the rule covers and why, and give them a compliant way to do the task
- D) Allow the uploads from now on, since the practice has become common across the team

**Answer: C.** The rule exists and is clear, so this is a training gap, and the fix is training plus a compliant path, such as working from a de-identified extract. Option A rewrites a policy that is not the problem, B removes legitimate uses to fix a behavior, and D turns a compliance failure into policy.

**Q12.** An operations lead redesigns the weekly supplier-payment process so that Claude reads incoming invoices, matches them to purchase orders, and approves payment on any match, emailing the finance team a summary afterwards. What is wrong with the design?

- A) Over-delegation: Claude can match and flag, but a person approves the payments
- B) Nothing, because matching invoices to purchase orders is a well-defined task
- C) Claude should email the summary to finance before approving each payment instead of after
- D) The matching step should run on Opus, since payments are high-stakes work

**Answer: A.** Matching is a good AI-executed step; approving money is high-stakes, hard to reverse, and human-retained. Option B ignores stakes and reversibility, C changes the order of notification without putting a person in the decision, and D upgrades the model without fixing who decides.

## 3-week study plan

- **Week 1: official baseline.** Check that your employer is in the [Claude Partner Network](https://claude.com/partners) (registration needs your company email). Read the exam guide that matches your exam date, complete the Partner Academy prep course, and take the AI Fluency course. Map yourself against the six domains and their skills.
- **Week 2: deliberate product practice.** Use every capability the blueprint names on your own work: configure a Project with instructions, knowledge, and a Skill for a recurring task; connect a workplace source; run research and verify its citations; analyze a de-identified spreadsheet with code execution; review, edit, and delete memories; try an incognito chat. Practice the judgment side deliberately: classify three real outputs as ready, needing revision, or needing human correction, and label every step of one of your team's workflows AI-executed, human-reviewed, or human-retained.
- **Week 3: calibrate.** Start with the [30 practice questions](./practice-questions.md) in this repo, then take [full-length timed practice tests](https://preporato.com/certificates/claude-certified-associate-foundations) with per-domain review, and a final pass on the two judgment-heavy domains (output evaluation and governance). The night before: Part III here plus the [cheat sheet](https://preporato.com/blog/claude-certified-associate-foundations-cheat-sheet-2026).

Expanded version: [3-week CCAO-F study plan](https://preporato.com/blog/ccao-f-study-plan-3-week-preparation-2026).

## Pre-exam checklist

- [ ] I can write a business prompt with role, task, source, constraints, format, and the context Claude lacks
- [ ] I can stage a large deliverable with checkpoints between steps
- [ ] I can match a weak output to its specification gap and choose iterate, restart, or change approach
- [ ] I can name five hallucination red flags and verify claims against the source, not against Claude
- [ ] I can classify an output as ready, needing revision, or needing human correction
- [ ] I can set review depth from the consequence of an error and internal versus external use
- [ ] I can choose inline, Artifact, structured data, a code-executed result, or a Skill document
- [ ] I can choose the capability combination a scenario needs, and leave out what it doesn't
- [ ] I can choose a model tier and effort level and defend the choice against the alternatives
- [ ] I can restart, summarize, persist, or rely on memory, and keep memory clean
- [ ] I can explain what an incognito chat does and does not do
- [ ] I can label workflow steps AI-executed, human-reviewed, or human-retained, and spot over-delegation
- [ ] I can turn a manual recurring task into a repeatable, handoff-ready setup
- [ ] I can present Claude to stakeholders with a concrete benefit and an honest limit
- [ ] I can place any requirement into instructions, knowledge, a Skill, a prompt, or a connector
- [ ] I can trace a quality drop to stale knowledge, memory, a Skill version, or an instruction edit
- [ ] I can classify a use case as appropriate, appropriate with safeguards, or inappropriate
- [ ] I can de-identify a dataset before upload, free-text fields included
- [ ] I can tell a policy gap from a training gap
- [ ] I have the eight traps down cold and apply them per option on multi-select items
- [ ] I have taken at least two full-length timed practice tests and reviewed every miss

## Resources

**Official (free):**
- [Claude Certified Associate - Foundations](https://anthropic-partners.skilljar.com/claude-certified-associate-foundations-certification) on the Anthropic Partner Academy: both exam guides (testing through December 6, and from December 7), the prep course, and registration
- [Certification FAQ](https://anthropic-partners.skilljar.com/page/faq-certifications): registration, Pearson checkout, rescheduling, retakes, and renewal
- The claude.ai Help Center: the primary source for this exam, and the Anthropic Usage Policy
- Anthropic Academy courses, mapped to this exam's domains:
  - [Claude 101](https://anthropic.skilljar.com/claude-101): the product tour this exam assumes
  - [AI Fluency: Framework & Foundations](https://anthropic.skilljar.com/ai-fluency-framework-foundations): Delegation, Description, Discernment, and Diligence, which underpin every domain
  - [AI Capabilities and Limitations](https://anthropic.skilljar.com/ai-capabilities-and-limitations): the judgment layer behind hallucination spotting and appropriate use
  - Audience variants exist too ([small businesses](https://anthropic.skilljar.com/ai-fluency-for-small-businesses), [educators](https://anthropic.skilljar.com/ai-fluency-for-educators), [students](https://anthropic.skilljar.com/ai-fluency-for-students)) if one matches your role

**Free articles (preporato.com):**
- [What changes on December 7](https://preporato.com/blog/ccao-f-exam-changes-december-2026) · [CCAO-F complete guide](https://preporato.com/blog/claude-certified-associate-foundations-complete-guide-2026) · [Cheat sheet](https://preporato.com/blog/claude-certified-associate-foundations-cheat-sheet-2026) · [Domains breakdown](https://preporato.com/blog/ccao-f-exam-domains-complete-breakdown-2026) · [How to pass first attempt](https://preporato.com/blog/how-to-pass-ccao-f-first-attempt-2026) · [CCAO-F vs CCDV-F](https://preporato.com/blog/ccao-f-vs-ccdv-f-which-claude-certification-2026)

**Practice:**
- [30 practice questions with explanations](./practice-questions.md) in this repo (free)
- [The CCAO-F page on Preporato](https://preporato.com/certificates/claude-certified-associate-foundations): free sample questions, then (paid) full-length timed practice tests on both blueprints and a 500-card flashcard deck

---

*Not affiliated with Anthropic. Exam details reflect the program as of November 2026; the Partner Academy is authoritative. Found an error? [Open an issue](https://github.com/preporato/claude-certification-guide/issues).*
