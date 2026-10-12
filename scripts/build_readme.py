#!/usr/bin/env python3
"""Build README.md, tools.json and tools.csv from the pages in docs/.

The files in docs/ are the source of truth for the list. This script joins
them in the order below into one README.md, converts cross-page links back to
in-page anchors, adds a table of contents and "back to top" links, checks that
every tool entry follows the one-line format, and exports the entries to
tools.json and tools.csv. Run it after editing anything in docs/:

    python scripts/build_readme.py          # rewrite README.md, tools.json, tools.csv
    python scripts/build_readme.py --check  # exit 1 if any of the three is out of date

Entry format (one line per tool, on the pages listed in ENTRY_PAGES):

    - **[Name](https://example.org/)** · Access · Owner · What it does, in one or two sentences.

Access is one of the words in ACCESS, with an optional qualifier in
parentheses. Owner is required. Atlas Bear tools carry "(ours)" in the owner
field. Each entries page ends with a line "*Last checked YYYY-MM-DD.*".
"""
import csv
import datetime as dt
import io
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
README = ROOT / "README.md"
TOOLS_JSON = ROOT / "tools.json"
TOOLS_CSV = ROOT / "tools.csv"

ORDER = [
    "index.md",
    "01-vessel-tracking.md",
    "ais-data-note.md",
    "02-vessel-identity.md",
    "03-ownership-sanctions.md",
    "04-satellite-imagery.md",
    "05-ports-infrastructure.md",
    "06-cargo-trade.md",
    "07-incidents-security.md",
    "08-maps-weather-charts.md",
    "09-commercial-platforms.md",
    "10-utilities-code.md",
    "11-learning.md",
    "glossary.md",
    "archive.md",
    "contributing.md",
    "about.md",
]
ENTRY_PAGES = [p for p in ORDER if re.match(r"^\d\d-", p)]

REPO_BLOB = "https://github.com/atlas-bear/osint-tools/blob/main/"
REPO_FILES = ["CHANGELOG.md", "LICENSE", "CONTRIBUTING.md", "tools.json", "tools.csv"]
BACK = "[↑ Back to top](#maritime-and-supply-chain-osint-tools)"
HEADER = (
    "<!-- GENERATED FILE. Do not edit README.md. Edit the matching page in docs/ "
    "and run: python scripts/build_readme.py. CI rejects pull requests where they differ. -->\n\n"
)

ACCESS = ["Free account", "Freemium", "Free", "Paid", "Enterprise quote", "Share-to-get", "On application"]
ENTRY = re.compile(
    r"^- \*\*\[(?P<name>[^\[\]]+)\]\((?P<url>https?://[^\s()]+(?:\([^\s()]*\)[^\s()]*)*)\)\*\* · "
    r"(?P<access>" + "|".join(re.escape(a) for a in ACCESS) + r")(?: \((?P<note>[^)]*)\))? · "
    r"(?P<owner>[^·]+?) · (?P<description>.+?)\s*$"
)
LAST_CHECKED = re.compile(r"^\*Last checked (\d{4}-\d{2}-\d{2})\.\*$")
COLUMNS = ["name", "url", "access", "access_note", "owner", "description",
           "category", "section", "page", "ours", "last_checked"]


class BuildError(Exception):
    pass


def slug(heading):
    s = heading.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"\s", "-", s)


def split_h2(text):
    """Yield chunks at H2 boundaries, ignoring code fences."""
    chunks, cur, fence = [], [], False
    for line in text.splitlines():
        if line.startswith("```"):
            fence = not fence
        if line.startswith("## ") and not fence:
            chunks.append(cur)
            cur = [line]
        else:
            cur.append(line)
    chunks.append(cur)
    return ["\n".join(c).strip("\n") for c in chunks if "\n".join(c).strip()]


def norm_url(url):
    url = url.split("#", 1)[0].rstrip("/")
    m = re.match(r"^(https?://)([^/]+)(.*)$", url)
    return (m.group(1) + m.group(2).lower() + m.group(3)) if m else url


def parse_entries(text, page, errors):
    entries, category, section, fence, last_checked = [], None, None, False, None
    today = dt.date.today()
    for n, line in enumerate(text.splitlines(), 1):
        where = f"docs/{page}:{n}"
        if line.startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        if line.startswith("## "):
            category, section = line[3:].strip(), None
            continue
        if line.startswith("### "):
            section = line[4:].strip()
            continue
        if line.startswith("#### "):
            errors.append(f"{where}: H4 headings are not allowed on entries pages")
            continue
        if "—" in line:
            errors.append(f"{where}: em dash")
        m = LAST_CHECKED.match(line.strip())
        if m:
            d = dt.date.fromisoformat(m.group(1))
            if d > today:
                errors.append(f"{where}: Last checked date is in the future")
            if (today - d).days > 365:
                print(f"warning: {where}: Last checked is more than a year old", file=sys.stderr)
            last_checked = m.group(1)
            continue
        if line.startswith("- **["):
            m = ENTRY.match(line)
            if not m:
                errors.append(f"{where}: entry does not match the one-line format")
                continue
            e = m.groupdict()
            note = e["note"] or ""
            if re.search(r"[€$£]", note) and not re.search(r"\d{4}-\d{2}", note):
                errors.append(f"{where}: a price in the access qualifier needs a YYYY-MM date")
            if category is None:
                errors.append(f"{where}: entry before the first H2 heading")
            desc = e["description"].strip()
            if len(re.findall(r"[.!?](\s|$)", desc)) > 2:
                print(f"warning: {where}: description longer than two sentences", file=sys.stderr)
            if re.search(r"(?<![(\[])https?://", desc):
                errors.append(f"{where}: bare URL in description")
            entries.append({
                "name": e["name"].strip(),
                "url": e["url"],
                "access": e["access"],
                "access_note": note,
                "owner": e["owner"].strip(),
                "description": desc,
                "category": category,
                "section": section,
                "page": page,
                "ours": e["owner"].strip().endswith("(ours)"),
                "last_checked": None,
            })
        elif line.startswith("- ") and "**[" in line:
            errors.append(f"{where}: entry does not start with '- **['")
    if last_checked is None:
        errors.append(f"docs/{page}: missing '*Last checked YYYY-MM-DD.*' line")
    for e in entries:
        e["last_checked"] = last_checked
    return entries


def build():
    out, all_entries, errors = [], [], []
    for name in ORDER:
        path = DOCS / name
        if not path.exists():
            errors.append(f"docs/{name}: missing")
            continue
        text = path.read_text(encoding="utf-8")
        if name in ENTRY_PAGES:
            all_entries.extend(parse_entries(text, name, errors))
        elif "—" in text:
            errors.append(f"docs/{name}: em dash")
        text = re.sub(r"\]\([0-9a-z-]+\.md#([^)]+)\)", r"](#\1)", text)       # cross-page -> in-page
        text = re.sub(r"\]\([0-9a-z-]+\.md\)", lambda m: "](#" + slug(first_h2(DOCS / m.group(0)[2:-1])) + ")", text)
        for f in REPO_FILES:
            text = text.replace(f"]({REPO_BLOB}{f})", f"]({f})")             # site URLs -> repo-relative
        for chunk in split_h2(text):
            is_front = not chunk.startswith("## ")
            if is_front:
                out.append(chunk + "\n\n## Table of Contents\n\n<!-- TOC -->\n<!-- /TOC -->\n\n---")
            else:
                out.append(chunk + "\n\n" + BACK + "\n\n---")
    # duplicates
    seen_url, seen_name = {}, {}
    for e in all_entries:
        u, nm = norm_url(e["url"]), e["name"].casefold()
        if u in seen_url:
            errors.append(f"duplicate URL {e['url']} ({seen_url[u]} and {e['page']})")
        if nm in seen_name:
            errors.append(f"duplicate name {e['name']} ({seen_name[nm]} and {e['page']})")
        seen_url[u], seen_name[nm] = e["page"], e["page"]
    if errors:
        raise BuildError("\n".join(errors))
    text = HEADER + "\n\n".join(out) + "\n"
    toc, fence = [], False
    for line in text.splitlines():
        if line.startswith("```"):
            fence = not fence
            continue
        m = re.match(r"^(##|###) (.+)$", line)
        if m and not fence and m.group(2).strip() != "Table of Contents":
            indent = "" if m.group(1) == "##" else "  "
            toc.append(f"{indent}- [{m.group(2).strip()}](#{slug(m.group(2))})")
    text = text.replace("<!-- TOC -->\n<!-- /TOC -->", "<!-- TOC -->\n" + "\n".join(toc) + "\n<!-- /TOC -->", 1)
    order = {p: i for i, p in enumerate(ORDER)}
    all_entries.sort(key=lambda e: (order[e["page"]], e["name"].casefold()))
    return text, all_entries


def first_h2(path):
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            return line[3:]
    raise BuildError(f"{path.name}: no H2 heading to link to")


def exports(entries):
    newest = max((e["last_checked"] for e in entries), default=None)
    data = {"count": len(entries), "last_checked": newest, "tools": [{k: e[k] for k in COLUMNS} for e in entries]}
    js = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(COLUMNS)
    for e in entries:
        w.writerow([e[k] if k != "ours" else ("yes" if e[k] else "no") for k in COLUMNS])
    return js, buf.getvalue()


def main():
    try:
        text, entries = build()
    except BuildError as err:
        print(f"build failed:\n{err}", file=sys.stderr)
        return 1
    js, cs = exports(entries)
    targets = [(README, text), (TOOLS_JSON, js), (TOOLS_CSV, cs)]
    if "--check" in sys.argv:
        stale = [p.name for p, want in targets
                 if not p.exists() or p.read_text(encoding="utf-8", newline="") != want]
        if stale:
            print(f"out of date: {', '.join(stale)}. Run: python scripts/build_readme.py", file=sys.stderr)
            return 1
        print(f"README.md, tools.json and tools.csv match docs/ ({len(entries)} tools)")
        return 0
    for p, want in targets:
        p.write_text(want, encoding="utf-8", newline="")
    print(f"wrote README.md ({len(text.splitlines())} lines), tools.json and tools.csv ({len(entries)} tools)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
