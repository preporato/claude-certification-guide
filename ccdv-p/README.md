# CCDV-P: Claude Certified Developer - Professional

The operator's credential, and the newest exam in the program (open since November 17, 2026). CCDV-P validates that an engineer can run Claude applications and agents in production at scale: keep them reliable under load, instrument and monitor them, diagnose failures and lead incident response, gate releases with evaluation, control cost and latency across a fleet, harden tool-using agents against hostile input, and supervise fleets of coding agents.

> **[📖 The Complete CCDV-P Study Guide](./guide.md)**: the full preparation guide with 8 chapters (one per exam domain), per-domain exam notes, worked questions, trap answers, and exam-day strategy. This page is the summary; the guide is the study material.
>
> **Practice:** [30 practice questions](./practice-questions.md) · [Full CCDV-P practice tests on Preporato](https://preporato.com/certificates/claude-certified-developer-professional)
>
> **Download:** [PDF](../downloads/ccdv-p-study-guide.pdf) · [EPUB](../downloads/ccdv-p-study-guide.epub), with the practice questions included
>
> **At a glance:** 8 chapters · 12 worked questions · 30 practice questions · ~8,500 words

## Quick facts

| | |
|---|---|
| Price | $175 per attempt |
| Questions | 70: 60 scored and 10 unscored |
| Duration | 120 minutes to answer, about 135 minutes of seat time |
| Question style | Scenario-based multiple choice and multiple response; each item states how many responses to select |
| Passing score | 720 on a 100-1000 scaled score, with percent correct per domain on the report |
| Delivery | Pearson VUE, online proctored or at a test center |
| Languages | English or Japanese |
| Who can register | People who work at Claude Partner Network organizations, with a company email; you pay at Pearson's checkout |
| Prerequisites | None; CCDV-F is recommended preparation and its scope is assumed knowledge |
| Validity | 12 months, free renewal assessment before expiration |
| Exam guide | Version 1.0, November 2026 |
| Partner tier | Counts toward Claude Partner Network tier eligibility |

## Exam domains

| Domain | Weight |
|--------|--------|
| 1. Advanced Agent Architecture and Orchestration | 17% |
| 2. Production Integration, Reliability, and Knowledge Grounding | 20% |
| 3. Observability and Production Monitoring | 12% |
| 4. Advanced Debugging and Incident Response | 10% |
| 5. Evaluation Engineering and Quality Assurance | 12% |
| 6. Cost and Latency Optimization at Scale | 8% |
| 7. Runtime Guardrails and Production Security | 11% |
| 8. Agent Fleet Operations for Software Delivery | 10% |

Most items hand you evidence from a running system (an error mix, usage numbers, a trace cohort, a judge's agreement rate, a red-team finding) and ask what explains it and what fixes it. The three sample questions in the official guide set the tone: branch retries on the stop condition instead of retrying everything, withhold gating from a position-biased judge until it agrees with people, and close an exfiltration path with a deterministic control rather than a stronger prompt.

## CCDV-P or CCAR-P?

Both are $175 professional exams that touch integration, evaluation, and safety. The architect exam ([CCAR-P](../ccar-p/)) asks which design to choose, what to commit to stakeholders, and how to govern it. The developer exam asks how to run the system once it is live: measure it, debug it, release changes safely, and keep it secure and affordable. If your job is on-call for a Claude system, this is the one.

## Study path (~6 weeks part-time)

1. **Week 1: official baseline.** Check that your employer is in the [Claude Partner Network](https://claude.com/partners) (registration needs your company email), read the exam guide in full, take the free Developer - Professional prep courses, and review the CCDV-F scope.
2. **Weeks 2-5: operate something.** The official guide asks for at least one tool-using agent in production with distributed tracing and cost telemetry, SLIs and SLOs, an evaluation suite that gates releases, layered guardrails, and an incident and postmortem practice. Build or adopt exactly that, red-team it, and run parallel and unattended Claude Code jobs against it.
3. **Week 6: calibrate.** Full-length timed practice tests, then per-domain review. The largest domain is 20%, so even coverage decides the result.

## Common mistakes

- Preparing on features instead of evidence. Almost every item is "here is what the system did; what is the cause?"
- One retry path for everything. Rate limits, length stops, refusals, and context-window stops each need their own handling.
- Trusting a judge, a gate, or an AI reviewer before calibrating it against people.
- Treating prompt instructions or logging as security controls where a deterministic block is needed.
- Unattended runs without a permission mode, tool list, or budget: they hang on prompts or run up a bill.
- Letting the credential lapse: renewal is free before the 12-month mark and a full-price proctored exam after it.

## Resources

**Official (free):**
- [Claude Certified Developer - Professional](https://anthropic-partners.skilljar.com/claude-certified-developer-professional-certification) on the Anthropic Partner Academy: the exam guide, the free prep courses, and registration
- [Claude Developer Platform docs](https://platform.claude.com/docs) and [Claude Code docs](https://code.claude.com/docs)

**Free articles:**
- [What is CCDV-P?](https://preporato.com/blog/what-is-claude-developer-professional-ccdv-p)
- [Exam guide explained](https://preporato.com/blog/claude-certified-developer-professional-exam-guide-2026)
- [Cheat sheet](https://preporato.com/blog/claude-developer-professional-cheat-sheet-2026)
- [6-week study plan](https://preporato.com/blog/claude-developer-professional-study-plan-2026)
- [CCDV-F vs CCDV-P](https://preporato.com/blog/ccdv-f-vs-claude-certified-developer-professional-2026)

**Practice:**
- [30 practice questions with explanations](./practice-questions.md) in this repo (free)
- [The CCDV-P page on Preporato](https://preporato.com/certificates/claude-certified-developer-professional): free sample questions, then (paid) full-length timed practice tests and a 500-card flashcard deck
