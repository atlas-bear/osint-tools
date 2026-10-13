# Maritime and Supply Chain OSINT Tools

![Tools](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatlas-bear%2Fosint-tools%2Fmain%2Ftools.json&query=%24.count&label=tools&color=blue)
![Last checked](https://img.shields.io/badge/last%20checked-2026--10-blue)
![Check list](https://github.com/atlas-bear/osint-tools/actions/workflows/check.yml/badge.svg)
![Check links](https://github.com/atlas-bear/osint-tools/actions/workflows/links.yml/badge.svg)
![License](https://img.shields.io/github/license/atlas-bear/osint-tools)

> Part of the [Atlas Bear Library](https://atlas-bear.github.io/), where Atlas Bear Labs gathers its public guides, lists and tools. Read this list as a website at [atlas-bear.github.io/osint-tools](https://atlas-bear.github.io/osint-tools/), or download it as [tools.json](https://github.com/atlas-bear/osint-tools/blob/main/tools.json) or [tools.csv](https://github.com/atlas-bear/osint-tools/blob/main/tools.csv).

**Related resources:**

- [AI-Enhanced OSINT](https://github.com/atlas-bear/osint-ai-guide): our guide to using AI in intelligence work, with the OPSEC practice that applies to every tool here.
- [Recommended Reading](https://github.com/atlas-bear/recommended-reading): books for intelligence professionals working on illicit trade.
- [MARA](https://maraiq.com): our maritime security intelligence platform. Feedback and the public roadmap live at [mara-roadmap](https://github.com/atlas-bear/mara-roadmap).

---

Atlas Bear Labs created this repository to share the tools we use in our own research. We hope they are useful to others doing maritime and supply chain work. The list covers applications, sites, data sets and code for tracking ships, cargo and trade, finding out who owns and runs a vessel, and checking what you find against imagery, inspection records and sanctions lists.

Every entry was opened and checked on the date at the bottom of its page. Each one names who runs the tool and what it costs, because both have changed a lot since we started the list, and because the market for vessel data has consolidated into a few owners. There is a short [note on that](ais-data-note.md) after the tracking page.

This is not an exhaustive list, and it is not meant to be. We list what works for the questions we and the people we train actually ask. If a tool you rely on is missing, or an entry is wrong, please [propose a change](contributing.md). We reply to every proposal.

## How to read an entry

Each tool is one line: **name**, then **access**, then **owner**, then what it does and its main catch.

- **Free**: open to anyone. **Free account**: free after registering. **Freemium**: a useful free tier plus paid tiers.
- **Paid**: no free tier; prices carry the month we saw them. **Enterprise quote**: sold to organisations on contract, no published price.
- **Share-to-get**: you contribute data (usually an AIS receiver feed) to get access. **On application**: free or discounted for eligible organisations.

Tools we built ourselves are marked **(ours)** after the owner. The [commercial platforms](09-commercial-platforms.md) page groups the enterprise products and says what free source answers the same question. Terms are explained once in the [glossary](glossary.md). Dead tools go to the [archive](archive.md) rather than vanishing.

## How this list is maintained

We sweep the whole list twice a year, in spring before the Summer School on Illicit Trade and again in autumn, and re-date each page when we do. A link checker runs on every pull request and on the first of each month, and opens an issue when a link breaks. Each sweep ends with a GitHub release and a [CHANGELOG](https://github.com/atlas-bear/osint-tools/blob/main/CHANGELOG.md) entry. The pages in `docs/` are the source; `README.md`, `tools.json` and `tools.csv` are generated from them.
