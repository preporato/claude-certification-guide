# CCAO-F practice questions

30 practice questions for **Claude Certified Associate - Foundations** (CCAO-F), written for this repo and spread across the exam's six domains by their official weights. 6 of them ask for more than one answer, as some of the real exam's questions do (each item says how many to pick); those count only when every choice is right.

Choose your answer before you open the explanation.

**Want a timed run?** The [CCAO-F page on Preporato](https://preporato.com/certificates/claude-certified-associate-foundations) has free sample questions and full-length timed practice tests in the exam's format, with a score for every domain.

| Domain | Exam weight | Questions here |
|---|---|---|
| Task Definition and Prompting | 15% | 5 |
| Output Evaluation and Quality Control | 20% | 6 |
| Capability, Model, and Context Selection | 15% | 4 |
| Workflow Design and Integration | 18% | 5 |
| Configuration and Knowledge Management | 15% | 5 |
| Responsible Use, Data Protection, and Governance | 17% | 5 |

---

### Question 1

*Task Definition and Prompting*

Your prompt 'Write an email about the new expense tool' produced something generic. Which TWO additions would improve it most? (Select TWO)

- **A.** A switch to the most capable model at the highest effort level
- **B.** A request for ten versions so that you can pick the best one of them
- **C.** The tool's key facts, pasted in: launch date, how to get access, where to get help
- **D.** An instruction to 'make it amazing' and to be as creative and engaging as it can
- **E.** Who the email is for and what it should get them to do

<details>
<summary>Answer</summary>

**C and E.** Generic output comes from missing context, and the audience and goal (E) and the source material (C) are two of the five parts of a complete business prompt. Enthusiasm (D) adds no information. More versions (B) of an underspecified email are more generic emails. A stronger model (A) still can't know facts you didn't give it.

</details>

### Question 2

*Task Definition and Prompting*

You need a 20-page market analysis with competitor profiles, a pricing comparison and recommendations. One big prompt produced a shallow result. What is the best approach?

- **A.** Ask for 'much more detail' in every section of the same single prompt
- **B.** Break it into steps: agree on an outline, draft each section from its sources, then do a final pass
- **C.** Regenerate the same prompt until a deeper version of the analysis appears
- **D.** Rewrite the single prompt with every requirement in capitals, so that Claude can't skip any of them

<details>
<summary>Answer</summary>

**B.** Multi-part deliverables work better as a sequence of smaller steps you can check (B). A and D keep the one-giant-prompt problem. C is regenerate-and-hope.

</details>

### Question 3

*Task Definition and Prompting*

Claude's first draft of a customer apology is too long and too formal. Which follow-up works best?

- **A.** 'Please improve this draft and make it much better than the first one you wrote.'
- **B.** Start a new chat and paste in the same prompt you used the first time
- **C.** Regenerate the response and pick whichever of the versions reads better
- **D.** 'Cut this to about 120 words, warmer and more direct; keep the refund details and open with the apology.'

<details>
<summary>Answer</summary>

**D.** Specific feedback gives Claude concrete changes to make (D). A gives it nothing to act on, and C and B roll the dice again on an unchanged request.

</details>

### Question 4

*Task Definition and Prompting*

You want campaign ideas for a product launch. Which prompting strategy fits brainstorming?

- **A.** Ask for many varied ideas first (say, 20), then narrow them with your criteria in a follow-up
- **B.** Ask for the single best idea, so you don't have to sort through a long list of them
- **C.** Give no context at all, so Claude is unconstrained and free to surprise you
- **D.** Ask for a short list of ideas with final budgets and timelines already attached to each one of them

<details>
<summary>Answer</summary>

**A.** Brainstorming works best as volume and variety first, then judgment (A). Asking for one best idea (B) skips the exploration. Budgets (D) belong to a later planning step. With no context (C), the ideas won't fit your product or audience.

</details>

### Question 5

*Task Definition and Prompting*

You asked for 'a table comparing vendors,' and each time the columns come out different. What is the most effective fix?

- **A.** Regenerate until the columns happen to come out the way you want them
- **B.** Ask for 'a better, more professional table' with clearer columns
- **C.** Show the exact structure: list the columns in order or paste a sample row to follow
- **D.** Switch to Opus, which keeps its formatting far more consistent from one run to the next

<details>
<summary>Answer</summary>

**C.** A wrong format every time means the format was described vaguely, and a concrete example fixes that (C). A is regenerate-and-hope, D changes the model without clarifying the request, and B is still vague.

</details>

### Question 6

*Output Evaluation and Quality Control*

Claude summarized a 30-page vendor contract you attached and wrote: 'The contract auto-renews for 24 months unless cancelled 90 days before expiry.' This line is going into an email to your director. What is the most efficient way to check it?

- **A.** Regenerate the summary and check whether the same line comes back a second time
- **B.** Ask Claude to quote the exact clause with its section number, then read that clause yourself
- **C.** Send it as is, because the contract was attached, so Claude worked from the actual contract text
- **D.** Ask Claude whether it's sure, and send the summary if it confirms the line

<details>
<summary>Answer</summary>

**B.** A grounded claim can point to its evidence, so asking for the clause and reading it yourself is fast and conclusive (B). Asking for reassurance (D) gets a fluent answer either way. Consistency across regenerations (A) doesn't prove accuracy. An attached source (C) lowers the risk of errors without removing it, and this line describes a contract commitment.

</details>

### Question 7

*Output Evaluation and Quality Control*

Claude drafted a job ad for a software engineer that uses phrases like 'young, energetic team' and 'digital native.' What is the issue, and what should you do?

- **A.** Nothing; phrases like these are standard in technology job ads and help the company attract a good cultural fit
- **B.** The tone is too casual for a technical role; ask for a formal rewrite that sounds more professional
- **C.** The ad is too long for job boards; ask for a shorter version that keeps the key requirements
- **D.** It signals an age preference, which can deter qualified applicants and create legal risk; ask for inclusive wording

<details>
<summary>Answer</summary>

**D.** Evaluating output covers bias as well as factual errors, and age-coded language in a job ad is a real fairness and compliance problem (D). B and C change the style and keep the biased phrases. A confuses a common phrase with an acceptable one.

</details>

### Question 8

*Output Evaluation and Quality Control*

Claude built a pricing comparison table with totals calculated from 40 line items you pasted in. The table is going into a client proposal. What validation is needed?

- **A.** Nothing, because you supplied the numbers and Claude only added them up
- **B.** Round the totals so that any small differences in the arithmetic won't matter to the client
- **C.** Recompute the totals independently, for example in a spreadsheet, before it goes out
- **D.** Ask Claude to double-check its own math in the same chat, and fix anything it finds

<details>
<summary>Answer</summary>

**C.** Precise arithmetic over many figures is a weak fit to accept unchecked, and a client-facing proposal makes the numbers consequential, so they get verified independently (C). Next time, have Claude compute totals with code execution on the line items rather than in prose. The same process checking itself (D) isn't an independent check. Correct inputs (A) don't guarantee correct sums. Rounding (B) hides errors.

</details>

### Question 9

*Output Evaluation and Quality Control*

Claude wrote a market summary with no sources attached. Which TWO details are hallucination red flags? (Select TWO)

- **A.** 'According to a 2025 McKinsey survey, 73% of retailers...' with no source attached
- **B.** A suggestion to verify the figures with the original sources before publishing
- **C.** A general explanation of what market share means and how analysts measure it
- **D.** A note that Claude can't see your internal sales data
- **E.** A precise figure for next quarter's market size, stated as fact

<details>
<summary>Answer</summary>

**A and E.** A named study with a precise statistic and no source (A), and a confident, specific figure about the future (E), fit the red-flag profile: precision and authority without grounding. A general definition (C) is low risk, and B and D are signs of honest, calibrated output.

</details>

### Question 10

*Output Evaluation and Quality Control*

Claude summarized a customer interview and wrote: 'The customer is frustrated with onboarding and plans to cancel.' The transcript mentions onboarding friction but says nothing about cancelling. What is the problem?

- **A.** It presents an inference as fact; edit it to what the transcript supports, or label it as interpretation
- **B.** The summary needs a more formal, neutral tone before it is shared with the product team
- **C.** The summary is too short to capture everything the customer said about onboarding
- **D.** Nothing; it's a reasonable reading of the frustration that the customer described at length in the interview

<details>
<summary>Answer</summary>

**A.** Details beyond the source are a hallucination red flag, and a cancellation claim could trigger real business decisions, so the output has to match its evidence (A). A plausible reading (D) still isn't supported by the transcript. C and B are style issues.

</details>

### Question 11

*Output Evaluation and Quality Control*

Research mode returns a summary of a new data regulation with eight cited sources. Your compliance team will base a plan on it. Which TWO steps are needed before anyone uses it? (Select TWO)

- **A.** Nothing; eight citations from different sources prove that the summary is accurate
- **B.** Have the compliance owner review the conclusions before the plan is built on them
- **C.** Ask Claude to rate the reliability of each source
- **D.** Run research mode again and keep only the claims that appear in both of the summaries
- **E.** Open the cited sources and confirm each key claim matches them, and that they're current and authoritative

<details>
<summary>Answer</summary>

**B and E.** Citations make claims checkable, which helps only if someone checks them (E), and regulatory content goes through a qualified reviewer (B). Citations alone (A) don't prove the summary represents its sources correctly. Repeated claims (D) show consistency, which isn't accuracy. Claude grading its own sources (C) is no independent check.

</details>

### Question 12

*Capability, Model, and Context Selection*

Every month you turn a 9,000-row sales export into a two-page summary for regional managers, with exact totals by region and a short commentary. Which setup fits?

- **A.** Research mode, so that every figure in the summary comes with a citation you can check
- **B.** The most capable model at the highest effort, so the arithmetic in the prose is accurate every month
- **C.** Paste all 9,000 rows into a chat and ask Claude to add up each region and then write the short commentary
- **D.** Code execution on the uploaded export for exact totals, with the summary as an Artifact you can revise

<details>
<summary>Answer</summary>

**D.** Exact figures from a data file are the code-execution trigger, and a document you will revise and share is the Artifact trigger (D). Totals written out in prose (C) are estimates. Research (A) searches outside sources and has nothing to do with your export. A stronger setting (B) still produces arithmetic in prose; computation that must be exact belongs in code.

</details>

### Question 13

*Capability, Model, and Context Selection*

Which TWO tasks justify Opus over Sonnet? (Select TWO)

- **A.** Writing a two-line reply to a colleague who asked whether the quarterly report will be ready on time
- **B.** A strategy recommendation synthesizing six long reports, where an error would be expensive
- **C.** Reformatting a list of 30 names and email addresses into a sortable table
- **D.** Working out how obligations interact across five related contracts before a negotiation
- **E.** Summarizing the notes from a short weekly team meeting

<details>
<summary>Answer</summary>

**B and D.** Opus is for complex, high-stakes reasoning across a lot of material (B, D). Sonnet is the everyday default, and quick, simple tasks like C, A and E suit Sonnet or Haiku.

</details>

### Question 14

*Capability, Model, and Context Selection*

You need to sort 400 short customer comments into five well-defined themes today. Speed matters more than nuance. Which approach fits?

- **A.** Haiku with the five themes clearly defined, then a spot-check of a sample
- **B.** Opus at the highest effort, for maximum quality on every one of the comments
- **C.** Research mode, so each theme is backed by sources from outside the company
- **D.** One comment per chat, so each of the 400 comments gets Claude's full attention

<details>
<summary>Answer</summary>

**A.** Quick, well-defined tasks at volume are Haiku's case, and a sample check keeps the quality honest (A). Opus (B) spends time and cost on a task that doesn't need deep reasoning. Research mode (C) searches for current sources, which this task doesn't need. D wastes hours.

</details>

### Question 15

*Capability, Model, and Context Selection*

A long chat about a proposal has become slow, and Claude has started mixing up details from early drafts with the current version. What is the best move?

- **A.** Keep going in the same chat and correct each mistake as soon as it appears in a draft
- **B.** Paste the entire chat history into a new chat, so that nothing from any of the earlier drafts is lost along the way
- **C.** Start fresh with a summary of current decisions and the latest draft, and keep references in Project knowledge
- **D.** Switch to Haiku for speed, since the slowdown is the main problem with the long chat

<details>
<summary>Answer</summary>

**C.** Restart, summarize and persist is the fix for an overloaded chat: a fresh context with only what matters (C). A keeps the overload, B moves it to a new chat, and D changes speed without fixing the mix-ups.

</details>

### Question 16

*Workflow Design and Integration*

Your manager wants to roll Claude out to all 200 employees next week for every kind of task. What do you recommend?

- **A.** Wait until AI tools stop making mistakes, so no one has to check the outputs they produce
- **B.** Pilot one or two well-defined workflows with a small group, measure time and errors before and after, then expand
- **C.** Let each employee figure out their own uses without guidance, since everyone's work is different
- **D.** Roll it out to all 200 employees at once next week, to build momentum and show that leadership supports it

<details>
<summary>Answer</summary>

**B.** A measured pilot shows the real value and the limits on a small scale before the whole company depends on it (B). A big-bang rollout (D) spreads untested habits everywhere at once. A waits for something that won't happen. C produces uneven quality and no evidence.

</details>

### Question 17

*Workflow Design and Integration*

Which TWO tasks are strong fits for Claude in a marketing team's workflow? (Select TWO)

- **A.** Turning a webinar transcript into a blog draft and three social posts
- **B.** Reconciling 5,000 ad-spend transactions with no independent check
- **C.** Deciding which agency gets a \$200,000 contract
- **D.** Drafting five subject-line variants for an A/B test
- **E.** Reporting a competitor's announcement from yesterday, from memory

<details>
<summary>Answer</summary>

**A and D.** Drafting variants (D) and repurposing content across channels (A) are classic strong fits, with a person reviewing the output. A spending decision (C) needs human accountability, precise reconciliation at volume (B) belongs in a spreadsheet or finance system, and yesterday's news (E) is beyond the model's knowledge unless research mode grounds it.

</details>

### Question 18

*Workflow Design and Integration*

You're presenting a Claude pilot to leadership. Which framing is most appropriate?

- **A.** 'Claude will replace the operations team by next year, which will save the company its entire annual salary budget.'
- **B.** 'The benefits are real, but they can't really be measured in time or in quality.'
- **C.** 'Summaries take 10 minutes instead of 45; the owner still reviews each one, since outputs can contain errors.'
- **D.** 'Claude eliminates errors from our summaries, so they no longer need anyone to review them.'

<details>
<summary>Answer</summary>

**C.** Good stakeholder communication pairs a concrete, measured benefit with an honest limitation (C). D promises something no probabilistic system delivers. A overstates the role and invites resistance. B gives leadership nothing to decide with.

</details>

### Question 19

*Workflow Design and Integration*

A colleague opens Claude and types 'help me with the Q3 board deck.' The results are unfocused. What should be defined before prompting?

- **A.** The deliverable, its audience, the source material, and what a good result looks like
- **B.** The slide color scheme, the fonts, the template, and how many slides the deck should have
- **C.** Nothing; Claude should infer it from the name of the deck and the quarter
- **D.** Which model to use, and whether to turn on extended thinking for it

<details>
<summary>Answer</summary>

**A.** Solution design starts from the task: what you need, for whom, from which sources, and how you'll judge it (A). Model choice (D) comes later and won't rescue an undefined task. Claude can't infer goals nobody has stated (C). Colors (B) are a detail of the deliverable.

</details>

### Question 20

*Workflow Design and Integration*

A legal team handles NDAs in five steps: intake, first-pass review against the team's playbook, negotiation, approval and signature. Where does Claude add the most value with the right safeguards?

- **A.** Negotiating directly with the other party, unsupervised, so that each deal closes faster
- **B.** Signing on the company's behalf once the NDA has been reviewed and approved
- **C.** Final approval, since Claude can check the whole NDA faster than a lawyer can
- **D.** First-pass review: compare each NDA with the playbook and flag deviations for a lawyer

<details>
<summary>Answer</summary>

**D.** First-pass review is a good human-reviewed step: Claude compares and flags, and a lawyer decides on each deviation (D). Approval (C), signature (B) and negotiation with the other party (A) are human-retained steps that carry legal accountability, and handing them to Claude is over-delegation.

</details>

### Question 21

*Configuration and Knowledge Management*

In a team Project, where should each of these go: (1) 'Always write in British English and use our headline format'; (2) the 40-page brand guidelines PDF; (3) the team's seven-step procedure for turning a brief into a campaign one-pager in the standard template; (4) the brief for this week's campaign?

- **A.** (1) Project instructions, (2) a Skill, (3) Project instructions, (4) Project knowledge
- **B.** (1) Project instructions, (2) Project knowledge, (3) a Skill, (4) the chat prompt
- **C.** (1) Project knowledge, (2) Project instructions, (3) the chat prompt, (4) a Skill
- **D.** (1) The chat prompt, (2) the chat prompt, (3) Project knowledge, (4) Project instructions

<details>
<summary>Answer</summary>

**B.** Standing rules go in instructions, reference documents in knowledge, a repeatable procedure with a template in a Skill, and details for one task in the chat (B). C swaps rules and documents, retypes the procedure every time and makes a one-week brief permanent. D retypes standing rules in every chat and stores a temporary brief as a permanent rule. A packages a reference PDF as a procedure and stores the temporary brief permanently.

</details>

### Question 22

*Configuration and Knowledge Management*

Your weekly report draws on a Google Doc of sales notes that the team updates daily. You've been uploading a copy every Monday, and sometimes it's out of date. What is the better setup?

- **A.** Paste the notes in from memory at the start of each week's report
- **B.** Upload a fresh copy twice a week instead of once, on Mondays and Thursdays
- **C.** Copy the notes into the Project instructions, which Claude reads in every chat
- **D.** Connect Google Drive so Claude reads the current version of the document

<details>
<summary>Answer</summary>

**D.** Connectors suit material that lives in another tool and changes often, so Claude reads the current version (D). More frequent uploads (B) shrink the gap without closing it. Memory (A) adds errors. Instructions (C) hold standing rules, and pasted notes there go stale just as fast.

</details>

### Question 23

*Configuration and Knowledge Management*

A Project keeps quoting last year's prices. Both the 2025 and the 2026 price sheets are in Project knowledge. What fixes this?

- **A.** Remove or replace the outdated sheet; if both must stay, say in the instructions which one is current
- **B.** Use research mode for prices, so that Claude searches the web for the current figures each time it needs one
- **C.** Correct Claude in every chat whenever it quotes one of last year's prices
- **D.** Switch to Opus, which is better at telling which of two documents is newer

<details>
<summary>Answer</summary>

**A.** Stale knowledge produces confidently outdated answers, so the fix is maintaining the knowledge itself (A). Correcting every chat (C) never ends. A stronger model (D) still reads both sheets. Your prices are internal, so searching for them (B) won't find the right ones.

</details>

### Question 24

*Configuration and Knowledge Management*

A consultant runs all client work in one Project with memory on. This week, a draft for Client A mentioned the internal codename of Client B's project. The instructions and knowledge files haven't changed. What is the right fix?

- **A.** Remove Client B's files from Project knowledge, so that Claude can no longer read them
- **B.** Switch to a more capable model that keeps different clients' details apart more reliably
- **C.** Delete the memories about Client B, and give each client its own Project so memory stays scoped to one client
- **D.** Add an instruction telling Claude never to mention other clients' names, codenames, or projects in any of its drafts

<details>
<summary>Answer</summary>

**C.** Details from another work stream are the signature of memory accumulated across clients, so the fix is to clean that memory and separate the work streams (C). An instruction (D) papers over context that shouldn't be shared at all. A stronger model (B) doesn't change what Claude remembers. The knowledge files (A) haven't changed, so they can't explain the new behavior.

</details>

### Question 25

*Configuration and Knowledge Management*

On Monday you changed a Project's instructions, switched the model and uploaded new knowledge files. Since then, the outputs are worse. What should you do?

- **A.** Ask Claude what went wrong, since it can see its own instructions and knowledge
- **B.** Roll back, then reapply one change at a time, comparing results on the same test inputs
- **C.** Delete the Project and start over with a fresh setup built from scratch this week
- **D.** Change everything again until the outputs are as good as they were before Monday

<details>
<summary>Answer</summary>

**B.** With three changes at once, you can't tell which one hurt quality, so change one variable at a time against the same inputs (B). D adds more confusion, A asks Claude to explain configuration changes it can't observe, and C throws away a setup that worked before Monday.

</details>

### Question 26

*Responsible Use, Data Protection, and Governance*

You want Claude to summarize an internal incident report that contains customers' names and email addresses. Your company's AI policy allows internal documents and prohibits customer personal data. What do you do?

- **A.** Paste it in, because the policy allows internal documents and this report is an internal one
- **B.** Paste it in and ask Claude to ignore the names
- **C.** De-identify the customer details first, since the summary doesn't need them, then summarize
- **D.** Paste it into an incognito chat, since incognito chats aren't saved to history or memory

<details>
<summary>Answer</summary>

**C.** Check the policy before pasting: the report is allowed, the customer data isn't, and the task works without it (C). Being internal (A) doesn't change the personal-data rule. Incognito (D) controls what is kept afterwards, but the data has still been shared. Asking Claude to ignore data (B) comes after you've already shared it.

</details>

### Question 27

*Responsible Use, Data Protection, and Governance*

A sales rep wants to upload a prospect's RFP, marked confidential, so Claude can help draft the response. Your AI policy says nothing about third-party confidential documents. What is the best action?

- **A.** Ask the policy owner or legal before uploading, and treat the RFP as sensitive until they answer
- **B.** Rewrite the RFP from memory in your own words and upload that version instead of the file
- **C.** Upload it, since the policy doesn't forbid it and the prospect wants a fast response
- **D.** Upload only the pages that look less sensitive, and keep the pricing pages out of it

<details>
<summary>Answer</summary>

**A.** When the policy doesn't cover a case, escalate to the policy owner and stay on the cautious side in the meantime (A). Silence in the policy (C) doesn't amount to approval. Partial uploads (D) and paraphrasing from memory (B) still share confidential content, and the rewrite adds errors.

</details>

### Question 28

*Responsible Use, Data Protection, and Governance*

Your organization requires disclosure when AI helps produce external content. You drafted a customer newsletter with Claude and then edited it heavily. What applies?

- **A.** Describe the newsletter as written and fact-checked by the team without help from AI
- **B.** Skip disclosure, because your heavy edits have made the newsletter substantially your own original work
- **C.** Disclose AI involvement only if a customer asks how the newsletter was written
- **D.** Follow the disclosure rule as written, since your edits don't change how the draft was produced

<details>
<summary>Answer</summary>

**D.** Transparency rules apply as written (D). Editing (B) doesn't remove the requirement, disclosure on request (C) isn't what the policy says, and A misrepresents how the work was made.

</details>

### Question 29

*Responsible Use, Data Protection, and Governance*

Which TWO uses make Claude the decision-maker in a situation where a qualified person must own the call? (Select TWO)

- **A.** Using Claude's ranking alone to decide which employees are laid off
- **B.** Brainstorming names for a team offsite
- **C.** Summarizing your own meeting notes
- **D.** Drafting three versions of an internal FAQ for a manager to choose from
- **E.** Sending Claude's answer about a customer's legal rights to the customer without legal review

<details>
<summary>Answer</summary>

**A and E.** Decisions that affect people's livelihoods (A) or legal standing (E) need a qualified human to own them, however good the draft looks. D, B and C are drafting and organizing work where a person still chooses what to use.

</details>

### Question 30

*Responsible Use, Data Protection, and Governance*

A colleague found a free third-party Skill online that promises to summarize any contract, and wants to add it to the legal team's Project, which has the Google Drive connector enabled. What should happen first?

- **A.** Install it, but turn off the Google Drive connector while the team is testing it on a few contracts
- **B.** Vet it like any software touching company data: publisher, what it does with files, policy; then get approval
- **C.** Install it if its reviews are good and other legal teams have used it without any problems
- **D.** Install it, since Skills only change how Claude formats output and can't reach the connected files

<details>
<summary>Answer</summary>

**B.** Trust in third-party Skills and connectors is part of judging whether a use is appropriate, so it gets vetted and approved before it touches legal files (B). Skills can carry instructions and code, so they do more than format output (D). Turning the connector off for a test (A) skips the question of what happens when it is on. Reviews (C) say nothing about your organization's policy or data.

</details>

---

## Where to go next

- **Review by domain.** If your misses cluster, re-read those domains in Part II of the [CCAO-F study guide](./guide.md):
  - [Task Definition and Prompting](./guide.md#domain-1-task-definition-and-prompting-15)
  - [Output Evaluation and Quality Control](./guide.md#domain-2-output-evaluation-and-quality-control-20)
  - [Capability, Model, and Context Selection](./guide.md#domain-3-capability-model-and-context-selection-15)
  - [Workflow Design and Integration](./guide.md#domain-4-workflow-design-and-integration-18)
  - [Configuration and Knowledge Management](./guide.md#domain-5-configuration-and-knowledge-management-15)
  - [Responsible Use, Data Protection, and Governance](./guide.md#domain-6-responsible-use-data-protection-and-governance-17)
- **Practice at full length.** The [CCAO-F page on Preporato](https://preporato.com/certificates/claude-certified-associate-foundations) has free sample questions and full-length timed practice tests (paid) in the exam's format, with a score for every domain.

Found a mistake in a question? [Open an issue](https://github.com/preporato/claude-certification-guide/issues/new?template=outdated-fact.yml) and we'll fix it.

*These questions were written for this repo and are not taken from the exam. Not affiliated with Anthropic.*
