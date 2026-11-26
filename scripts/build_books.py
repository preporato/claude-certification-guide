#!/usr/bin/env python3
"""Build the PDF and EPUB edition of each study guide into downloads/.

Each book is the exam's guide.md followed by its 30 practice questions and an answer
key, built from the same banks as the practice pages.

Needs pandoc 3 and Chrome or Chromium:
    PANDOC=/path/to/pandoc CHROME=/path/to/chrome python3 scripts/build_books.py
(both default to the names on PATH: pandoc and chromium)
"""
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402  (the practice-page builder: banks, option order, links)

ROOT = build.ROOT
REPO = build.REPO
PANDOC = os.environ.get("PANDOC", "pandoc")
CHROME = os.environ.get("CHROME", "chromium")
EDITION = "November 2026 edition"
OUT = ROOT / "downloads"
HERE = Path(__file__).resolve().parent


def run(cmd, **kw):
    subprocess.run(cmd, check=True, **kw)


def absolute_links(text, exam):
    """Rewrite repo-relative links so they work outside GitHub."""
    def fix(m):
        label, target = m.group(1), m.group(2)
        if target.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        if target.startswith("./practice-questions.md"):
            return f"[{label}](#practice-questions)"
        if target.startswith("./guide.md#"):
            return f"[{label}]({target[len('./guide.md'):]})"
        path = os.path.normpath(os.path.join(exam, target.split("#")[0]))
        anchor = "#" + target.split("#", 1)[1] if "#" in target else ""
        kind = "tree" if target.endswith("/") or "." not in os.path.basename(path) else "blob"
        return f"[{label}]({REPO}/{kind}/main/{path}{anchor})"
    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", fix, text)


def appendix(bank, questions):
    domains = {d["id"]: d["name"] for d in bank["domains"]}
    scenarios = {s["id"]: s for s in bank.get("scenarios", [])}
    md = build.md
    lines = [
        "# Practice questions",
        "",
        f"{len(questions)} questions for {bank['code']}, written for this guide in the exam's style and spread across its domains by the official weights. "
        "Questions that ask for more than one answer say how many. The answers and explanations follow in the next section.",
        "",
        f"For timed, full-length practice with a score for every domain, see [the {bank['code']} page on Preporato]({bank['cert_page']}).",
        "",
    ]
    seen = None
    for q in questions:
        if q["scenario"] and q["scenario"] != seen:
            seen = q["scenario"]
            s = scenarios[seen]
            lines += [f"## Scenario: {s['title']}", "", f"> {md(s['text'])}", ""]
        if not q["scenario"] and seen is not None and seen != "standalone":
            seen = "standalone"
            lines += ["## Standalone questions", ""]
        lines += [f"**Question {q['n']}** *({domains[q['domain']]})*", "", md(q["stem"]), ""]
        if q.get("code"):
            lines += [f"```{q['code']['lang']}", q["code"]["text"], "```", ""]
        for o in q["options"]:
            lines.append(f"- **{o['letter']}.** {md(o['text'])}")
        lines.append("")
    lines += ["# Answers and explanations", ""]
    for q in questions:
        answer = " and ".join(q["answer"]) if len(q["answer"]) == 2 else ", ".join(q["answer"])
        lines += [f"**Question {q['n']}: {answer}.** {md(q['explanation'])}", ""]
    lines += [
        "# Keep going",
        "",
        f"- **Full-length practice.** [The {bank['code']} page on Preporato]({bank['cert_page']}) has free sample questions and full-length timed practice tests (paid) in the exam's format, with a score for every domain.",
        f"- **Updates and corrections.** The latest edition and the guides for the other four exams are at [github.com/preporato/claude-certification-guide]({REPO}).",
        "",
    ]
    return "\n".join(lines)


def front_page(bank):
    return (
        '<section class="cover-page">\n'
        f'<p class="kicker">Claude Certification Guide · {EDITION}</p>\n'
        f'<p class="code">{bank["code"]}</p>\n'
        f'<p class="name">{bank["name"]}</p>\n'
        '<p class="what">The complete study guide, with 30 practice questions and an answer key</p>\n'
        '<div class="facts">\n'
        f'<p>Full-length timed practice tests: <a href="{bank["cert_page"]}">{bank["cert_page"].replace("https://", "")}</a></p>\n'
        f'<p>Updates and the guides for the other four exams: <a href="{REPO}">{REPO.replace("https://", "")}</a></p>\n'
        '</div>\n'
        '<p class="legal">MIT license. Maintained by Preporato. Not affiliated with, endorsed by, or sponsored by Anthropic; Claude is a trademark of Anthropic, PBC. '
        'Exam facts reflect the program in November 2026; the Anthropic Partner Academy is authoritative.</p>\n'
        '</section>\n\n'
    )


def build_pdf(exam, bank, body_md, tmp):
    src = tmp / f"{exam}.md"
    html = tmp / f"{exam}.html"
    css = (HERE / "book.css").read_text().replace("__FOOTER__", f"{bank['code']} study guide · Full practice tests: {bank['cert_page'].replace('https://', '')}")
    (tmp / "book.css").write_text(css)
    src.write_text(front_page(bank) + body_md)
    run([PANDOC, "-f", "gfm", "-t", "html5", "--standalone", "--embed-resources",
         "--metadata", f"title={bank['code']} study guide", "--metadata", "lang=en",
         "--css", str(tmp / "book.css"), "-o", str(html), str(src)])
    out = OUT / f"{exam}-study-guide.pdf"
    run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={out}", html.as_uri()], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return out


def build_cover(exam, bank, tmp):
    page = (HERE / "cover.html").read_text()
    page = page.replace("__CODE__", bank["code"]).replace("__NAME__", bank["name"]).replace("__EDITION__", EDITION)
    path = tmp / f"{exam}-cover.html"
    path.write_text(page)
    png = tmp / f"{exam}-cover.png"
    run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
         f"--screenshot={png}", "--window-size=1600,2400", path.as_uri()], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return png


def build_epub(exam, bank, body_md, tmp):
    src = tmp / f"{exam}-epub.md"
    src.write_text(body_md)
    out = OUT / f"{exam}-study-guide.epub"
    run([PANDOC, "-f", "gfm", "-t", "epub3", "--toc", "--toc-depth=2", "--split-level=1",
         "--epub-cover-image", str(build_cover(exam, bank, tmp)),
         "--css", str(HERE / "epub.css"),
         "--metadata", f"title={bank['code']} study guide: {bank['name']}",
         "--metadata", "author=Preporato",
         "--metadata", "lang=en-US",
         "--metadata", "rights=MIT license. Not affiliated with Anthropic.",
         "--metadata", f"description={EDITION}. The complete study guide with 30 practice questions and an answer key. Full practice tests: {bank['cert_page']}",
         "-o", str(out), str(src)])
    return out


def main():
    OUT.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        for exam in build.EXAMS:
            bank = build.load_bank(exam)
            questions = build.arrange(bank)
            guide = absolute_links((ROOT / exam / "guide.md").read_text(), exam)
            body = guide.rstrip() + "\n\n" + appendix(bank, questions)
            pdf = build_pdf(exam, bank, body, tmp)
            epub = build_epub(exam, bank, body, tmp)
            print(f"{pdf.relative_to(ROOT)} ({pdf.stat().st_size // 1024} KB), {epub.relative_to(ROOT)} ({epub.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
