# CCAR-P: Claude Certified Architect - Professional

> **[📖 The Complete CCAR-P Study Guide](./guide.md)**: the full preparation guide with 8 chapters, per-domain exam notes, worked questions, the twelve trap answers, and exam-day strategy. This page is the summary; the guide is the study material.
>
> **Practice:** [30 practice questions](./practice-questions.md) · [Full CCAR-P practice tests on Preporato](https://preporato.com/certificates/claude-certified-architect-professional)
>
> **Download:** [PDF](../downloads/ccar-p-study-guide.pdf) · [EPUB](../downloads/ccar-p-study-guide.epub), with the practice questions included
>
> **At a glance:** 8 chapters · 7 code examples · 15 worked questions · 30 practice questions · ~10,800 words

The architect's Professional-level credential. CCAR-P certifies the person accountable for a Claude solution across its whole life: translating a vague business request into an architecture, selecting integration mechanisms, designing evaluation and governance into the system from day one, managing stakeholder expectations, and enabling the teams who build and operate the result. Its sibling at the same level, [CCDV-P](../ccdv-p/), certifies the engineer who runs such systems in production.

> **The exam changes on December 7, 2026.** From that date CCAR-P has 70 questions (60 scored) and new domain weights, and the guide and practice questions here follow that version. Testing on or before December 6? The earlier blueprint is summarized in [the guide](./guide.md#taking-ccar-p-before-december-7).

## Quick facts

| | |
|---|---|
| Price | $175 per attempt |
| Questions | 70: 60 scored and 10 unscored (63, all scored, through December 6) |
| Duration | 120 minutes to answer, about 135 minutes of seat time |
| Question style | Scenario-based; each item states how many responses to select |
| Passing score | 720 on a 100-1000 scaled score |
| Delivery | Pearson VUE, test center or online proctored |
| Languages | English or Japanese |
| Who can register | People who work at Claude Partner Network organizations, with a company email; you pay at Pearson's checkout |
| Validity | 12 months, free renewal assessment before expiration |
| Prerequisites | None formally; CCA-F is optional, and most candidates benefit from the Foundations vocabulary first |
| Recommended experience | 3+ years systems architecture or platform engineering, 6+ months delivering production Claude or LLM solutions |
| Partner tier | Counts toward Claude Partner Network tier eligibility |

## Exam domains (from December 7, 2026)

| Domain | Weight |
|--------|--------|
| 1. Solution Design and Architecture | 18% |
| 2. Claude Models, Prompting, and Context Engineering | 13% |
| 3. Integration | 21% |
| 4. Evaluation, Testing, and Optimization | 17% |
| 5. Governance, Safety, and Risk Management | 16% |
| 6. Stakeholder Communication and Lifecycle Management | 7% |
| 7. Developer Productivity and Operational Enablement | 8% |

## What the exam actually tests

The blueprint reads like an enterprise engagement:

- **Integration (the largest domain, now 21%)**: MCP versus direct API versus agent-to-agent connections, least-privilege tool access, retrieval architecture, and the reliability controls around every connection.
- **Evaluation and governance together are a third of the exam**: coverage gaps, judge bias, experiment design and model migrations on one side; guardrails, human-in-the-loop placement, injection surfaces and compliance controls on the other.
- **Stakeholder communication shrinks to 7% but doesn't vanish.** Discovery, commitments a probabilistic system can actually keep, decision records with their residual risk, and handoff to the team that runs the system still show up, and technically strong candidates still lose points there.

The scenario questions demand judgment that is hard to cram. This is deliberate: the exam certifies solution ownership rather than implementation skill, which the Foundations tier already covers.

## Study path (~6 weeks part-time)

1. **Weeks 1-2: official baseline plus gap map.** Check that your employer is in the [Claude Partner Network](https://claude.com/partners) (registration needs your company email), read the exam guide that matches your exam date, complete the Partner Academy architect courses, and map your experience against all seven domains. Most candidates find their gap in governance or evaluation rather than technology.
2. **Weeks 3-4: deepen the enterprise domains.** Work through [the Claude Developer Platform docs](https://platform.claude.com/docs) and [the Claude Code docs](https://code.claude.com/docs) on integration patterns, evaluation design, guardrails, and deployment surfaces, and study how compliance regimes map onto LLM systems. If you have never run discovery or written an architecture decision record for a real stakeholder, practice on a hypothetical engagement end to end.
3. **Weeks 5-6: calibrate.** Full-length, timed practice tests on the blueprint that matches your date. Use the per-domain breakdown ruthlessly; with seven domains, a comfortable overall average can hide a failing one.

## Common mistakes

- Preparing as if it were a harder CCA-F. The Professional exam spends most of its questions above the code, at the architecture, evaluation, governance, and communication level.
- Studying the old weights. From December 7, integration, evaluation, and governance grow, and stakeholder communication halves.
- Confusing zero data retention with data residency, or assuming every feature is available on every cloud platform.
- Letting the credential lapse: renewal is free before the 12-month mark and a full-price proctored exam after it.
- Booking a retake on impulse: every attempt costs the full fee, and the wait grows from 14 to 30 to 90 days after each failed attempt.

## Resources

**Official (free):**
- [Claude Certified Architect - Professional](https://anthropic-partners.skilljar.com/claude-certified-architect-professional-certification) on the Anthropic Partner Academy: both exam guides, courses, and registration
- [Claude Developer Platform docs](https://platform.claude.com/docs) and [Claude Code docs](https://code.claude.com/docs)

**Free articles:**
- [What changes on December 7](https://preporato.com/blog/ccar-p-exam-changes-december-2026)
- [CCAR-P complete guide](https://preporato.com/blog/claude-certified-architect-professional-complete-guide-2026)
- [6-week study plan](https://preporato.com/blog/ccar-p-study-plan-6-week-preparation-2026)
- [CCA-F vs CCAR-P: which to take](https://preporato.com/blog/cca-f-vs-ccar-p-which-claude-certification-2026)
- [Developer - Professional vs Architect - Professional](https://preporato.com/blog/claude-developer-professional-vs-architect-professional-2026)

**Practice:**
- [30 practice questions with explanations](./practice-questions.md) in this repo (free)
- [The CCAR-P page on Preporato](https://preporato.com/certificates/claude-certified-architect-professional): free sample questions, then (paid) full-length timed practice tests on both blueprints, a 500-card flashcard deck, and auto-graded build-and-submit projects
