#!/usr/bin/env python3
"""Build the generated files from the question banks in practice/*.json.

    <exam>/practice-questions.md   one page per exam, answers folded under each question
    docs/index.html                the practice test: one HTML file that runs offline in any browser

Run from anywhere, no dependencies:  python3 scripts/build.py

The banks are the source of truth. Options are written with keys a-e and the correct
one first; explanations refer to options as {a}, {b}, ... This script shuffles the
options with a fixed seed (so builds are reproducible and correct answers are spread
evenly across A-D) and replaces the {x} references with the final letters.
"""
import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMS = ["ccao-f", "ccdv-f", "ccdv-p", "cca-f", "ccar-p"]
LETTERS = "ABCDE"
REPO = "https://github.com/preporato/claude-certification-guide"
WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight"}


def load_bank(exam):
    return json.loads((ROOT / "practice" / f"{exam}.json").read_text())


def github_slug(heading):
    """The anchor GitHub generates for a Markdown heading."""
    s = heading.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def guide_domain_anchors(exam):
    """Anchors of the guide's Part II domain sections, in order."""
    text = (ROOT / exam / "guide.md").read_text()
    return [github_slug(h) for h in re.findall(r"^## (Domain \d+:.*)$", text, re.M)]


def arrange(bank):
    """Shuffle each question's options and resolve {x} references to letters."""
    rng = random.Random("claude-certification-guide/" + bank["id"])
    slots = []
    out = []
    for n, q in enumerate(bank["questions"], 1):
        keys = sorted(q["options"])
        correct = q["answer"]
        if len(correct) == 1 and len(keys) == 4:
            if not slots:
                slots = list(range(4))
                rng.shuffle(slots)
            target = slots.pop()
            others = [k for k in keys if k not in correct]
            rng.shuffle(others)
            order = others[:target] + correct + others[target:]
        else:
            order = keys[:]
            rng.shuffle(order)
        letter = {k: LETTERS[i] for i, k in enumerate(order)}
        explanation = re.sub(r"\{([a-e])\}", lambda m: letter[m.group(1)], q["explanation"])
        out.append({
            "n": n,
            "domain": q["domain"],
            "scenario": q.get("scenario"),
            "stem": q["stem"],
            "code": q.get("code"),
            "options": [{"letter": letter[k], "text": q["options"][k]} for k in order],
            "answer": sorted(letter[k] for k in correct),
            "explanation": explanation,
        })
    return out


def guide_url(exam, anchor=""):
    return f"{REPO}/blob/main/{exam}/guide.md" + (f"#{anchor}" if anchor else "")


def md(text):
    """Escape bank text for GitHub Markdown, leaving `code spans` untouched.

    GitHub would otherwise read '<tag>' as HTML, a pair of '$' signs as math, '*' as
    emphasis and '~' as strikethrough."""
    out = []
    for part in re.split(r"(`[^`]*`)", text):
        if part.startswith("`") and part.endswith("`") and len(part) > 1:
            out.append(part)
        else:
            out.append(part.replace("\\", "\\\\").replace("<", "&lt;").replace("$", "\\$")
                       .replace("*", "\\*").replace("~", "\\~"))
    return "".join(out)


# ---------------------------------------------------------------------------
# Markdown page per exam
# ---------------------------------------------------------------------------

def render_markdown(bank, questions):
    exam, code = bank["id"], bank["code"]
    domains = {d["id"]: d for d in bank["domains"]}
    count = {d["id"]: 0 for d in bank["domains"]}
    for q in questions:
        count[q["domain"]] += 1
    scenarios = {s["id"]: s for s in bank.get("scenarios", [])}
    multi = sum(len(q["answer"]) > 1 for q in questions)
    n_domains = len(bank["domains"])

    lines = [
        f"# {code} practice questions",
        "",
        f"{len(questions)} practice questions for **{bank['name']}** ({code}), written for this repo and spread across the exam's {WORDS.get(n_domains, n_domains)} domains by their official weights. "
        f"{multi} of them ask for more than one answer, as some of the real exam's questions do (each item says how many to pick); those count only when every choice is right.",
        "",
    ]
    if scenarios:
        lines += [
            f"The first {sum(1 for q in questions if q['scenario'])} questions are grouped under two practice scenarios written for this repo, the way the real exam groups its questions; the exam itself presents four of the six scenarios in its official guide, picked at random.",
            "",
        ]
    lines += [
        "Choose your answer before you open the explanation.",
        "",
        f"**Want a timed run?** The [{code} page on Preporato]({bank['cert_page']}) has free sample questions and full-length timed practice tests in the exam's format, with a score for every domain.",
        "",
        "| Domain | Exam weight | Questions here |",
        "|---|---|---|",
    ]
    for d in bank["domains"]:
        lines.append(f"| {d['name']} | {d['weight']}% | {count[d['id']]} |")
    lines += ["", "---", ""]

    current_scenario = None
    standalone_started = False
    for q in questions:
        if q["scenario"] and q["scenario"] != current_scenario:
            current_scenario = q["scenario"]
            s = scenarios[current_scenario]
            idx = list(scenarios).index(current_scenario) + 1
            lines += [f"## Scenario {idx}: {s['title']}", "", f"> {md(s['text'])}", ""]
        if not q["scenario"] and scenarios and not standalone_started:
            standalone_started = True
            lines += ["## Standalone questions", ""]
        lines += [
            f"### Question {q['n']}",
            "",
            f"*{domains[q['domain']]['name']}*",
            "",
            md(q["stem"]),
            "",
        ]
        if q.get("code"):
            lines += [f"```{q['code']['lang']}", q["code"]["text"], "```", ""]
        for o in q["options"]:
            lines.append(f"- **{o['letter']}.** {md(o['text'])}")
        answer = " and ".join(q["answer"]) if len(q["answer"]) == 2 else ", ".join(q["answer"])
        lines += [
            "",
            "<details>",
            "<summary>Answer</summary>",
            "",
            f"**{answer}.** {md(q['explanation'])}",
            "",
            "</details>",
            "",
        ]

    anchors = guide_domain_anchors(exam)
    lines += [
        "---",
        "",
        "## Where to go next",
        "",
        f"- **Review by domain.** If your misses cluster, re-read those domains in Part II of the [{code} study guide](./guide.md):",
    ]
    for i, d in enumerate(bank["domains"]):
        anchor = anchors[i] if i < len(anchors) else ""
        lines.append(f"  - [{d['name']}](./guide.md#{anchor})")
    lines += [
        f"- **Practice at full length.** The [{code} page on Preporato]({bank['cert_page']}) has free sample questions and full-length timed practice tests (paid) in the exam's format, with a score for every domain.",
        "",
        "Found a mistake in a question? [Open an issue](" + REPO + "/issues/new?template=outdated-fact.yml) and we'll fix it.",
        "",
        f"*These questions were written for this repo and are not taken from the exam. Not affiliated with Anthropic.*",
        "",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Practice test page
# ---------------------------------------------------------------------------

def render_app(banks):
    data = []
    for bank, questions in banks:
        anchors = guide_domain_anchors(bank["id"])
        data.append({
            "id": bank["id"],
            "code": bank["code"],
            "name": bank["name"],
            "certPage": bank["cert_page"],
            "guide": guide_url(bank["id"]),
            "exam": bank["exam"],
            "minutes": bank["minutes"],
            "domains": [
                {**d, "guide": guide_url(bank["id"], anchors[i] if i < len(anchors) else "")}
                for i, d in enumerate(bank["domains"])
            ],
            "scenarios": bank.get("scenarios", []),
            "questions": questions,
        })
    template = (ROOT / "scripts" / "practice-test.html").read_text()
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return template.replace("/*__BANKS__*/[]", payload)


def main():
    banks = []
    for exam in EXAMS:
        bank = load_bank(exam)
        questions = arrange(bank)
        (ROOT / exam / "practice-questions.md").write_text(render_markdown(bank, questions))
        banks.append((bank, questions))
        spread = {}
        for q in questions:
            if len(q["answer"]) == 1:
                spread[q["answer"][0]] = spread.get(q["answer"][0], 0) + 1
        print(f"{exam}: {len(questions)} questions, single-answer spread {dict(sorted(spread.items()))}")
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs" / "index.html").write_text(render_app(banks))
    (ROOT / "docs" / ".nojekyll").write_text("")
    print("docs/index.html written")


if __name__ == "__main__":
    main()
