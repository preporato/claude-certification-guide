# CCA-F: Claude Certified Architect - Foundations

The original Anthropic certification (launched March 12, 2026) and the credential for people who build production-grade Claude systems end to end: agentic architectures, multi-agent orchestration, prompt and context engineering for reliability, and the tools and MCP servers agents depend on. Anthropic's current exam guide (version 1.1, November 2026) gives its exam code as **CCAR-F**; most candidates still know it as CCA-F.

Where [CCDV-F](../ccdv-f/) certifies platform mechanics, CCA-F certifies the assembly of those mechanics into working systems.

> **[📖 The Complete CCA-F Study Guide](./guide.md)**: the full preparation guide with 8 technology chapters, per-domain exam notes, worked questions, anti-patterns, and exam-day strategy. This page is the summary; the guide is the study material.
>
> **Practice:** [30 practice questions](./practice-questions.md) · [Full CCA-F practice tests on Preporato](https://preporato.com/certificates/claude-certified-architect)
>
> **Download:** [PDF](../downloads/cca-f-study-guide.pdf) · [EPUB](../downloads/cca-f-study-guide.epub), with the practice questions included
>
> **At a glance:** 8 chapters · 17 code examples · 12 worked questions · 30 practice questions · ~10,100 words

## Quick facts

| | |
|---|---|
| Exam code | CCAR-F in the official guide (version 1.1, November 2026) |
| Price | $125 per attempt |
| Questions | 60 |
| Duration | 120 minutes to answer, about 135 minutes of seat time |
| Question style | Scenario-based multiple choice and multiple response; each item states how many responses to select |
| Structure | 4 of 6 published scenarios, picked at random for each sitting |
| Passing score | 720 on a 100-1000 scaled score |
| Delivery | Pearson VUE, test center or online proctored |
| Languages | English or Japanese |
| Who can register | People who work at Claude Partner Network organizations, with a company email; you pay at Pearson's checkout |
| Validity | 12 months, free renewal assessment before expiration |
| Recommended experience | 6+ months building with the Claude API, Agent SDK, Claude Code, and MCP |
| Partner tier | Counts toward Claude Partner Network tier eligibility |

## Exam domains

| Domain | Weight |
|--------|--------|
| 1. Agentic Architecture & Orchestration | 27% |
| 2. Tool Design & MCP Integration | 18% |
| 3. Claude Code Configuration & Workflows | 20% |
| 4. Prompt Engineering & Structured Output | 20% |
| 5. Context Management & Reliability | 15% |

The domains and weights did not change in the November 2026 guide, and CCA-F is not part of the December 7, 2026 update that changes CCAO-F, CCDV-F, and CCAR-P.

Two things stand out in this blueprint:

- **The 20% Claude Code weight makes CCA-F one of the most Claude-Code-intensive exams in the program.** Expect working fluency with the configuration hierarchy, subagents, hooks, and Skills, well beyond "I have used it once".
- **Agentic architecture is the center of gravity.** Systems where the model plans and executes multi-step work using tools, and the orchestration of multiple agents, carry more than a quarter of the exam.

## The scenario format

The official guide publishes six scenarios, and each sitting presents four of them at random: a customer support resolution agent, code generation with Claude Code, a multi-agent research system, developer productivity tooling, Claude Code in continuous integration, and structured data extraction. Questions arrive inside these running systems, so a question about a context-management failure or a tool-design flaw comes with a concrete architecture around it. The [guide](./guide.md#the-six-production-scenarios) describes each one and what it tends to test.

You can't choose your scenarios, so prepare for all six. Practicing only with isolated flashcard-style questions leaves you unprepared for reasoning inside a running system; make sure some of your practice mirrors the scenario format.

## Study path (~30 days part-time)

1. **Week 1: official baseline.** Check that your employer is in the [Claude Partner Network](https://claude.com/partners) (registration needs your company email), complete the Partner Academy architect-track courses, and read the official exam guide, including its six scenarios and sample questions.
2. **Weeks 2-3: build.** Work through [the Claude Developer Platform docs](https://platform.claude.com/docs) and [the Claude Code docs](https://code.claude.com/docs) while building something real: an agent with tools, an MCP server, a Claude Code workflow with subagents and hooks. The exam writes questions from production judgment, and building is how you acquire it.
3. **Week 4: calibrate.** Take full-length, timed practice tests in the scenario format, review the per-domain breakdown, and spend the remaining days on your weakest two domains.

## Common mistakes

- Underestimating the Claude Code domain. Engineers who build agents through the API alone routinely lose most of a fifth of the exam here.
- Preparing with definitions instead of systems. The scenario format punishes memorization-first preparation.
- Mixing up what the exam tests with what the newest models accept. The guide tests `tool_choice` values such as `"any"` for structured extraction, while some of the newest models reject forced tool choice; know both, and the study guide notes where they differ.
- Letting the credential lapse after passing: the renewal assessment is free before the 12-month mark, and a full-price proctored exam after it.
- Booking a retake on impulse: every attempt costs the full fee, and the wait grows from 14 to 30 to 90 days after each failed attempt.

## Resources

**Official (free):**
- [Claude Certified Architect - Foundations](https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification) on the Anthropic Partner Academy: the exam guide, courses, and registration
- [Claude Developer Platform docs](https://platform.claude.com/docs) and [Claude Code docs](https://code.claude.com/docs)

**Free articles:**
- [CCA-F complete guide](https://preporato.com/blog/claude-certified-architect-complete-guide-2026)
- [30-day study plan](https://preporato.com/blog/cca-f-study-plan-30-day-preparation)
- [CCA-F vs CCAR-P: which to take](https://preporato.com/blog/cca-f-vs-ccar-p-which-claude-certification-2026)

**Practice:**
- [30 practice questions with explanations](./practice-questions.md) in this repo (free)
- [The CCA-F page on Preporato](https://preporato.com/certificates/claude-certified-architect): free sample questions to start, then the full tests below
- (Paid) [Six full-length scenario-format practice tests and a 500-card flashcard deck](https://preporato.com/certificates/claude-certified-architect) built on the exact domain weights
- (Paid) [12 hands-on projects](https://preporato.com/certificates/claude-certified-architect): build-and-submit work (agentic loops, hub-and-spoke systems, MCP servers, extraction pipelines) graded automatically against a rubric
