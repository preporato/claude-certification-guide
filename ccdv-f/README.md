# CCDV-F: Claude Certified Developer - Foundations

The developer credential. CCDV-F validates that an engineer can build real applications on the Claude platform: choosing between a workflow and an agent, calling the Messages API correctly, wiring in tools and MCP, controlling cost, grounding answers in documents, and shipping systems that are secure, tested, and debuggable.

> **[📖 The Complete CCDV-F Study Guide](./guide.md)**: the full preparation guide with 8 technology chapters (one per exam domain), per-domain exam notes, worked questions, trap answers, and exam-day strategy. This page is the summary; the guide is the study material.
>
> **Practice:** [30 practice questions](./practice-questions.md) · [Full CCDV-F practice tests on Preporato](https://preporato.com/certificates/claude-certified-developer-foundations)
>
> **Download:** [PDF](../downloads/ccdv-f-study-guide.pdf) · [EPUB](../downloads/ccdv-f-study-guide.epub), with the practice questions included
>
> **At a glance:** 8 chapters · 11 code examples · 15 worked questions · 30 practice questions · ~10,600 words

> **The exam changes on December 7, 2026.** From that date CCDV-F has 70 questions (60 scored) and new domain weights, and the guide and practice questions here follow that version. Testing on or before December 6? The earlier blueprint is summarized in [the guide](./guide.md#taking-ccdv-f-before-december-7).

## Quick facts

| | |
|---|---|
| Price | $125 per attempt |
| Questions | 70: 60 scored and 10 unscored (53, all scored, through December 6) |
| Duration | 120 minutes to answer, about 135 minutes of seat time |
| Question style | Scenario-based; each item states how many responses to select |
| Passing score | 720 on a 100-1000 scaled score |
| Delivery | Pearson VUE, online proctored or at a test center |
| Languages | English or Japanese |
| Who can register | People who work at Claude Partner Network organizations, with a company email; you pay at Pearson's checkout |
| Validity | 12 months, free renewal assessment before expiration |
| Recommended experience | 1-5 years software engineering, 6+ months hands-on Claude or LLM work, fluency in Python or TypeScript, REST APIs, command line |
| Partner tier | Counts toward Claude Partner Network tier eligibility |

## Exam domains (from December 7, 2026)

| Domain | Weight |
|--------|--------|
| 1. Agents and Workflows | 17% |
| 2. Applications and Integration | 20% |
| 3. Claude Code | 8% |
| 4. Eval, Testing, and Debugging | 10% |
| 5. Model Selection and Optimization | 12% |
| 6. Prompt and Context Engineering | 15% |
| 7. Security and Safety | 8% |
| 8. Tools and MCP | 10% |

The new blueprint spreads the weight. API mechanics fall from a third of the exam to a fifth, while Claude Code, evaluation, and prompt and context engineering grow. Items are engineering judgments: read a trace, an error body, a request, or usage numbers, and pick the change that fixes the cause. Agents are built with the Claude Agent SDK, your own loop, or Managed Agents; tools connect through the Model Context Protocol (MCP), the open protocol that standardizes how models discover and call external tools and data.

## Study path (~4 weeks part-time)

1. **Week 1: official baseline.** Check that your employer is in the [Claude Partner Network](https://claude.com/partners) (registration needs your company email), read the exam guide that matches your exam date, and complete the Partner Academy prep course.
2. **Weeks 2-3: build against the platform.** The official guide asks for one shipped, tool-using agent with a custom tool or MCP server, structured outputs, prompt caching, an evaluation against a golden set, and a deterministic guardrail. Build exactly that, then spend a day in Claude Code with a Rules file, a Skill, a hook, and headless mode.
3. **Week 4: calibrate.** Full-length timed practice tests, then per-domain review. No domain is above 20%, so even coverage decides the result.

## Common mistakes

- Treating the small domains as optional. Claude Code, security, and evaluation together are over a quarter of the new exam.
- Relying on habits from older models: temperature 0 for determinism, `budget_tokens` for thinking, prefill for JSON, and forced tool choice are all rejected by the newest models.
- Knowing the API but not the economics: cache breakpoints placed by change cadence, batching, and effort come before any tier downgrade.
- Letting the credential lapse: renewal is free before the 12-month mark and a full-price proctored exam after it.

## Resources

**Official (free):**
- [Claude Certified Developer - Foundations](https://anthropic-partners.skilljar.com/claude-certified-developer-foundations-certification) on the Anthropic Partner Academy: both exam guides, the prep course, and registration
- [Claude Developer Platform docs](https://platform.claude.com/docs) and [Claude Code docs](https://code.claude.com/docs)

**Free articles:**
- [What changes on December 7](https://preporato.com/blog/ccdv-f-exam-changes-december-2026)
- [CCDV-F complete guide](https://preporato.com/blog/claude-certified-developer-foundations-complete-guide-2026)
- [4-week study plan](https://preporato.com/blog/ccdv-f-study-plan-4-week-preparation-2026)
- [CCDV-F vs CCA-F: which to take](https://preporato.com/blog/ccdv-f-vs-cca-f-which-claude-certification-2026)

**Practice:**
- [30 practice questions with explanations](./practice-questions.md) in this repo (free)
- [The CCDV-F page on Preporato](https://preporato.com/certificates/claude-certified-developer-foundations): free sample questions, then (paid) full-length timed practice tests on both blueprints, a 500-card flashcard deck, and auto-graded hands-on projects
