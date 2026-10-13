---
title: "Contributing"
---

Know of a tool we left off, or spotted one that has died, moved or lost its free tier? Please tell us. The easiest route is the [issue form](https://github.com/atlas-bear/osint-tools/issues/new/choose), which needs no Markdown. If you prefer a pull request, edit one page in `docs/` and follow the format below. We reply to every proposal, whether or not we add the tool.

## What earns a place

A tool or data source goes on the list when it:

1. Answers a question about ships, cargo, ports, sea routes, owners or trade flows.
2. Is live and open to the public, or gated only by a stated condition that anyone can meet and that the entry names (an account, a shared receiver feed, an application open to eligible organisations).
3. States its access terms: free, free with an account, freemium with the free part clear, or paid with a published price or an honest "quote-based".
4. Adds something a listed source does not, such as history, an API, coverage, or a different way of collecting the data.
5. Has an identifiable operator with a contact page.
6. Has been public for at least six months, or is an open-source project with a licence and tagged releases.

We do not list tools whose purpose is tracking individuals, or tools that work by breaking another site's terms. We stay inside maritime OSINT and maritime supply-chain analysis. Good general OSINT lists already exist, and we point to them on the learning page rather than copying them.

Self-submissions are welcome. Say so in the pull request or the issue form. We verify every entry ourselves before it goes in, and we treat a disclosed self-submission exactly like any other proposal.

Dead tools are not deleted. They move to the [archive](archive.md) with a date and a reason, so that people who remember them can see what happened.

## The entry format

Every tool is one line, on one of the numbered pages in `docs/`:

```markdown
- **[Name](https://example.org/)** · Access · Owner · What it does and its main limit, in one or two plain sentences.
```

The parts are separated by a middle dot (`·`, U+00B7). **Access** is one of these words:

| Access | Meaning |
| --- | --- |
| Free | Open to anyone, no account needed. |
| Free account | Free after you register. |
| Freemium | A useful free tier plus paid tiers. Say what the free tier gives if it is not obvious. |
| Paid | No free tier. Give a published price and the month you saw it, or write "quote-based". |
| Enterprise quote | Sold to organisations on contract, no published price. |
| Share-to-get | You get access by contributing data, usually a receiver feed. |
| On application | Free or discounted for eligible organisations after an application. |

A qualifier in parentheses adds detail, for example `Free (non-commercial)`, `Free (open source, GPL-3.0)` or `Paid (from €9/yr, 2026-10)`. A price must carry a `YYYY-MM` date, because prices move.

**Owner** is the company, agency, project or maintainer. If nobody can tell who runs a site, it does not go on the list. Our own tools carry `(ours)` after the owner.

**Description** is one or two sentences in plain words. What does it do for an analyst, and what is the catch (coverage, delay, limits, where it is hosted)? No marketing language.

Each page ends with `*Last checked YYYY-MM-DD.*`. That date is the last time we swept the whole page, opened every link and re-read every claim. Adding one entry does not change it.

## Generated files

`README.md`, `tools.json` and `tools.csv` are built from the pages in `docs/` by `scripts/build_readme.py`. Please do not edit them directly; the check on every pull request will fail if they differ from `docs/`. If you can run Python, run the script and commit all three files. If not, tick "Allow edits by maintainers" and we will regenerate them on your branch.

```bash
python scripts/build_readme.py          # rebuild README.md, tools.json and tools.csv
python scripts/build_readme.py --check  # what CI runs
```

The script also checks the entry format, the access words, duplicate URLs and the `Last checked` line, and it refuses em dashes, because we try to keep the writing plain.

## Reviews and releases

We sweep the whole list twice a year, in spring before the [Summer School on Illicit Trade](https://www.rug.nl/education/summer-winter-schools/illicit-trade) and again in autumn. A link checker runs on every pull request and once a month, and opens an issue when something breaks. Each sweep ends with a release and a [CHANGELOG](https://github.com/atlas-bear/osint-tools/blob/main/CHANGELOG.md) entry.

The list and the data files are MIT licensed. The "awesome list" community prefers Creative Commons licences for lists like this one; we may revisit that. Please keep to our [community guidelines](https://github.com/atlas-bear/osint-tools/blob/main/COMMUNITY_GUIDELINES.md) in issues and pull requests.
