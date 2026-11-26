# Practice question banks

One JSON file per exam. These files are the single source for the practice pages (`<exam>/practice-questions.md`), the practice test in `docs/index.html` (one self-contained HTML file), and the question appendix in the PDF and EPUB downloads.

After editing a bank, rebuild with `python3 scripts/build.py` (no dependencies) and commit the regenerated files with your change.

## Format

```json
{
  "domain": "d2",
  "scenario": "support",
  "stem": "The question. Use `backticks` for code, file names and API fields.",
  "code": { "lang": "python", "text": "optional code shown under the question" },
  "options": {
    "a": "The correct option",
    "b": "A distractor",
    "c": "A distractor",
    "d": "A distractor"
  },
  "answer": ["a"],
  "explanation": "{a} is right because ... {b} fails because ... Refer to every option as {a}, {b}, {c} ..."
}
```

- Write the options with keys `a` to `e` and the correct ones first. The build shuffles them with a fixed seed, spreads correct answers evenly across the letters, and replaces each `{a}`-style reference in the explanation with the option's final letter.
- `domain` is an id from the bank's `domains` list. `scenario` is optional and refers to the bank's `scenarios` list (CCA-F groups some of its questions under two practice scenarios, the way the exam groups its questions).
- Multiple-response questions have two or three letters in `answer` and say so in the stem: "(Select TWO)".
- Keep the options about the same length. If the correct option is always the longest, or the only one with a reason attached, the question gives itself away; give distractors the same level of detail.
- Explain every option in the explanation, the wrong ones included.

## Rules for new questions

- Write them yourself. Never copy questions from the real exams, from paid question banks, or from anyone else's materials.
- Check technical facts against Anthropic's documentation ([platform.claude.com/docs](https://platform.claude.com/docs) and [code.claude.com/docs](https://code.claude.com/docs)) and program facts against the Partner Academy.
- Keep the domain spread close to the exam's official weights.
