# Changelog

All notable changes to this list are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/) loosely: a major version for a rebuild or a change to the entry format, a minor version for each twice-yearly sweep, a patch for fixes between sweeps.

## [Unreleased]

### Changed

- Link previews: every page now carries Open Graph and Twitter card metadata with a description and a preview image in the AB//LABS style, and the favicon is the AB//LABS mark.
- The website moved to <https://library.ab-labs.io/osint-tools/>. The old atlas-bear.github.io address redirects there, so existing links keep working.
- Ownership wording, contacts and names now reflect AB//LABS, which began as Atlas|Bear Labs and spun off from Atlas|Bear; the connection is explained in About. Copyright lines read AB//LABS (formerly Atlas|Bear Labs); contact is `support@ab-labs.io`.
- The website is now built with Quarto instead of MkDocs Material, with the same pages, a Browse page (a filterable card grid of every tool, generated from the entries) and the shared theme. The pages in `docs/` now carry a front-matter title instead of a top heading; the README is unchanged.

## [2.0.0] - 2026-10-12

A full rebuild. Every entry was re-verified, the list grew from 45 to well over a hundred tools, and the repository gained a website, data exports and continuous checks.

### Added

- Pages for vessel tracking, vessel identity and inspections, ownership and sanctions, satellite imagery, ports and infrastructure, cargo and trade data, security incidents, maps and weather, commercial platforms, utilities and code, and learning, each with a short introduction and a `Last checked` date.
- A note on who owns the AIS data (Kpler, S&P Global and the others) and what remains open, with sources.
- Open government AIS sources (NOAA MarineCadastre, Norway, Denmark, Finland, Australia), raw feeds (aisstream.io, AISHub) and self-hosted receiving (AIS-catcher, OpenCPN).
- Port state control databases, class registers, flag registries, sanctions lists, shadow fleet trackers and IUU vessel lists.
- Free imagery and detection sources: Copernicus Browser, Global Fishing Watch radar detections, SkyTruth Cerulean, Skylight, VIIRS boat detection, and the Vantor, Umbra and Capella open data programmes.
- IMF PortWatch, the NGA World Port Index, TeleGeography's cable map, Marine Regions and OpenInfraMap.
- Trade statistics and shipment records (UN Comtrade, ITC Trade Map, WITS, Eurostat, USA Trade Online, ImportYeti, Open Supply Hub) and freight indices.
- Reporting centres and advisories (UKMTO, ReCAAP, IMB, MDAT-GoG, MSCHOA, NGA MSI, ONI) and conflict maps.
- A commercial platforms page that flags enterprise products and names the free alternative for each group.
- Our own tools: equasis-cli, cue-kit and MARA, marked as ours.
- ArcNautical (proposed by SaltyTaro in #3) and Phantom Tide (proposed by tg12 in #2).
- From our own bookmark review: MarineRadar, Tradlinx, Ships IO, OpenAerialMap, the Maritime Cyber Attack Database, GDELT, Worldwide AIS Network, bbox finder, the VESSA dataset, the ODIS catalogue, the Allianz Safety and Shipping Review, the Organized Crime Index, Shipmap.org, Kaggle AIS datasets, the World Factbook Archive, Rendezvous and two guides.
- A glossary, an archive of retired tools, written inclusion criteria, issue forms and a pull request template.
- A website at atlas-bear.github.io/osint-tools built with MkDocs Material from the pages in `docs/`.
- `tools.json` and `tools.csv`, generated from the pages, for anyone who wants the list as data.
- Continuous checks: the generated files match `docs/`, the site builds, Markdown lints, and links are checked on every pull request and monthly.

### Changed

- Every tool is now one line: name, access, owner, description. Access uses a fixed vocabulary (Free, Free account, Freemium, Paid, Enterprise quote, Share-to-get, On application).
- The pages in `docs/` are the source of truth; `README.md` is generated from them.
- Corrected URLs for Google Earth, the ITU ship station search, MarineCadastre, the UN AIS Handbook, PeakFinder, GeoNames, the SubTel Forum cable map, Shodan and the Centre for Information Resilience's Ukraine map.
- Maxar is now Vantor; Maritime Optima is now ShipAtlas; MARA links to maraiq.com rather than a private repository.
- The general-purpose map entries were cut to those with a maritime reason, with a pointer to Bellingcat's toolkit for the rest.
- The MIT licence year and the community guidelines date were updated.

### Removed

- Dead or repurposed: Sourcemap Free Edition, Travel With Drone (both to the archive).
- Off-topic or redundant: CrewLinker, DuckDuckGo Maps, Satellites.pro, F4map, HERE WeGo (to the archive).
- The separate Supply Chain Management Tools repository was folded in and retired; its five ERP packages are recorded in the archive rather than listed, because they are operations software rather than intelligence sources.

### Fixed

- The "Active Links" claim is now backed by a link checker.
- The community guidelines no longer carry a placeholder date.

## [1.1] - 2025-10-20

### Changed

- Revised the Equasis entry and standardised entry formatting.

## [1.0] - 2025-07-15

### Added

- Related resources, the Atlas Bear ecosystem table, badges and community guidelines.
- MARA under supply chain risk management.

### Changed

- Reorganised the table of contents and rewrote tool descriptions.

## [0.1] - 2024-07-16

### Added

- First public version of the list, with MIT licence.
