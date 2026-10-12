<!-- GENERATED FILE. Do not edit README.md. Edit the matching page in docs/ and run: python scripts/build_readme.py. CI rejects pull requests where they differ. -->

# Maritime and Supply Chain OSINT Tools

![Tools](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatlas-bear%2Fosint-tools%2Fmain%2Ftools.json&query=%24.count&label=tools&color=blue)
![Last checked](https://img.shields.io/badge/last%20checked-2026--10-blue)
![Check list](https://github.com/atlas-bear/osint-tools/actions/workflows/check.yml/badge.svg)
![Check links](https://github.com/atlas-bear/osint-tools/actions/workflows/links.yml/badge.svg)
![License](https://img.shields.io/github/license/atlas-bear/osint-tools)

> Part of the [Atlas Bear Labs](https://github.com/atlas-bear) intelligence toolkit. Read this list as a website at [atlas-bear.github.io/osint-tools](https://atlas-bear.github.io/osint-tools/), or download it as [tools.json](tools.json) or [tools.csv](tools.csv).

**Related resources:**

- [AI-Enhanced OSINT](https://github.com/atlas-bear/osint-ai-guide): our guide to using AI in intelligence work, with the OPSEC practice that applies to every tool here.
- [Recommended Reading](https://github.com/atlas-bear/recommended-reading): books for intelligence professionals working on illicit trade.
- [MARA](https://maraiq.com): our maritime security intelligence platform. Feedback and the public roadmap live at [mara-roadmap](https://github.com/atlas-bear/mara-roadmap).

---

Atlas Bear Labs created this repository to share the tools we use in our own research. We hope they are useful to others doing maritime and supply chain work. The list covers applications, sites, data sets and code for tracking ships, cargo and trade, finding out who owns and runs a vessel, and checking what you find against imagery, inspection records and sanctions lists.

Every entry was opened and checked on the date at the bottom of its page. Each one names who runs the tool and what it costs, because both have changed a lot since we started the list, and because the market for vessel data has consolidated into a few owners. There is a short [note on that](#who-owns-the-ais-data) after the tracking page.

This is not an exhaustive list, and it is not meant to be. We list what works for the questions we and the people we train actually ask. If a tool you rely on is missing, or an entry is wrong, please [propose a change](#contributing). We reply to every proposal.

## Table of Contents

<!-- TOC -->
- [How to read an entry](#how-to-read-an-entry)
- [How this list is maintained](#how-this-list-is-maintained)
- [Vessel tracking (AIS)](#vessel-tracking-ais)
  - [Live maps with a free tier](#live-maps-with-a-free-tier)
  - [Open government AIS data](#open-government-ais-data)
  - [Raw feeds and your own receiver](#raw-feeds-and-your-own-receiver)
- [Who owns the AIS data](#who-owns-the-ais-data)
  - [Why it matters](#why-it-matters)
  - [What is still open](#what-is-still-open)
- [Vessel identity and inspections](#vessel-identity-and-inspections)
  - [Identity and registration](#identity-and-registration)
  - [Port state control](#port-state-control)
  - [Photos and yachts](#photos-and-yachts)
- [Ownership, sanctions and shadow fleet](#ownership-sanctions-and-shadow-fleet)
  - [Corporate and beneficial ownership](#corporate-and-beneficial-ownership)
  - [Sanctions lists and screening](#sanctions-lists-and-screening)
  - [Shadow fleet trackers](#shadow-fleet-trackers)
  - [Fishing and IUU](#fishing-and-iuu)
- [Satellite imagery and detection](#satellite-imagery-and-detection)
  - [Free imagery browsers and archives](#free-imagery-browsers-and-archives)
  - [Dark vessel and anomaly detection](#dark-vessel-and-anomaly-detection)
  - [Open commercial imagery](#open-commercial-imagery)
- [Ports, chokepoints and infrastructure](#ports-chokepoints-and-infrastructure)
  - [Ports and chokepoints](#ports-and-chokepoints)
  - [Cables, pipelines and boundaries](#cables-pipelines-and-boundaries)
- [Cargo, containers and trade data](#cargo-containers-and-trade-data)
  - [Container tracking](#container-tracking)
  - [Bills of lading and facilities](#bills-of-lading-and-facilities)
  - [Trade statistics](#trade-statistics)
  - [Freight rates](#freight-rates)
- [Security incidents and warnings](#security-incidents-and-warnings)
  - [Reporting centres and advisories](#reporting-centres-and-advisories)
  - [Conflict maps and event databases](#conflict-maps-and-event-databases)
- [Maps, weather and charts](#maps-weather-and-charts)
  - [Maps and street-level imagery](#maps-and-street-level-imagery)
  - [Weather and sea state](#weather-and-sea-state)
  - [Charts and bathymetry](#charts-and-bathymetry)
- [Commercial platforms](#commercial-platforms)
  - [Vessel tracking and maritime intelligence](#vessel-tracking-and-maritime-intelligence)
  - [Radar, optical and RF detection](#radar-optical-and-rf-detection)
  - [Ownership, sanctions and risk](#ownership-sanctions-and-risk)
  - [Trade and shipment data](#trade-and-shipment-data)
  - [Security and risk advisories](#security-and-risk-advisories)
- [Utilities, code and our tools](#utilities-code-and-our-tools)
  - [Our tools](#our-tools)
  - [Libraries and code](#libraries-and-code)
- [Learning and reference](#learning-and-reference)
  - [Guides and handbooks](#guides-and-handbooks)
  - [Data and reference](#data-and-reference)
  - [Training](#training)
  - [Other lists](#other-lists)
- [Glossary](#glossary)
- [Archive](#archive)
  - [Shut down, merged or gone](#shut-down-merged-or-gone)
  - [Renamed or moved](#renamed-or-moved)
  - [Dropped as off-topic](#dropped-as-off-topic)
- [Contributing](#contributing)
  - [What earns a place](#what-earns-a-place)
  - [The entry format](#the-entry-format)
  - [Generated files](#generated-files)
  - [Reviews and releases](#reviews-and-releases)
- [About, licence and contact](#about-licence-and-contact)
  - [Licence](#licence)
  - [Disclaimer](#disclaimer)
  - [Contact and support](#contact-and-support)
  - [Acknowledgments](#acknowledgments)
  - [Atlas Bear ecosystem](#atlas-bear-ecosystem)
<!-- /TOC -->

---

## How to read an entry

Each tool is one line: **name**, then **access**, then **owner**, then what it does and its main catch.

- **Free**: open to anyone. **Free account**: free after registering. **Freemium**: a useful free tier plus paid tiers.
- **Paid**: no free tier; prices carry the month we saw them. **Enterprise quote**: sold to organisations on contract, no published price.
- **Share-to-get**: you contribute data (usually an AIS receiver feed) to get access. **On application**: free or discounted for eligible organisations.

Tools we built ourselves are marked **(ours)** after the owner. The [commercial platforms](#commercial-platforms) page groups the enterprise products and says what free source answers the same question. Terms are explained once in the [glossary](#glossary). Dead tools go to the [archive](#archive) rather than vanishing.

[↑ Back to top](#maritime-and-supply-chain-osint-tools)

---

## How this list is maintained

We sweep the whole list twice a year, in spring before the Summer School on Illicit Trade and again in autumn, and re-date each page when we do. A link checker runs on every pull request and on the first of each month, and opens an issue when a link breaks. Each sweep ends with a GitHub release and a [CHANGELOG](CHANGELOG.md) entry. The pages in `docs/` are the source; `README.md`, `tools.json` and `tools.csv` are generated from them.

[↑ Back to top](#maritime-and-supply-chain-osint-tools)

---

## Vessel tracking (AIS)

Where is a ship now, and where has it been? The commercial maps answer the first question for free and charge for the second. The free route to history is the government and NGO data below. It covers more than most people expect: the whole US coast since 2009, Norway since 2005 with satellite AIS included, and Global Fishing Watch's global record since 2012. For a live feed to build on, aisstream.io costs nothing, and a receiver of your own costs about the price of a textbook.

One OPSEC point. Searching a named vessel on a commercial site while logged in ties your interest in that ship to your account. The open feeds and your own receiver do not.

### Live maps with a free tier

- **[MarineTraffic](https://www.marinetraffic.com/)** · Freemium · Kpler · The largest crowd-sourced AIS map, with vessel pages, port calls and photos. Free accounts see about a day of track and no port calls or ownership; Kpler has owned it since March 2023 and the free tier has narrowed since.
- **[VesselFinder](https://www.vesselfinder.com/)** · Freemium (Basic from €9/yr, 2026-10) · VesselFinder Ltd, Bulgaria · Live map and vessel particulars with the cheapest paid route to longer tracks (3, 7 or 90 days by tier). Its terms forbid scraping and building datasets.
- **[MyShipTracking](https://www.myshiptracking.com/)** · Freemium · MyShipTracking · Terrestrial AIS map with a credit-based API and a free trial key. Coverage is near-shore only.
- **[ShipAtlas](https://www.maritimeoptima.com/shipatlas)** · Freemium (from €10/month, 2026-10) · Maritime Optima, Norway · Satellite AIS positions, recent port calls and a sea-route calculator. The free tier is capped at ten satellite position views.
- **[ShipXplorer](https://www.shipxplorer.com/)** · Freemium · AirNav Systems · AIS map fed by hobbyist receivers, from the company behind ShipSpotting. Hosting a receiver earns a premium account.
- **[MarineRadar](https://www.marineradar.com/)** · Freemium · Lascade, Dubai · Live terrestrial and satellite AIS for more than 100,000 vessels with route playback, on the web and in mobile apps. Subscription prices are not published.
- **[Tradlinx vessel tracking](https://www.tradlinx.com/vessel-tracking/)** · Free · Tradlinx Inc., Seoul · Latest position, destination and identifiers for a ship by name, MMSI, IMO or call sign, with no account. Near-shore receivers only; satellite coverage is in the paid Ocean Visibility product.
- **[Shipinfo.net](https://shipinfo.net/)** · Freemium · STELS A LLC, Russia · AIS map with waterway and port-congestion analytics and Northern Sea Route ice layers. Operated from Russia, so think about what you query from a case machine.
- **[Global Fishing Watch map](https://globalfishingwatch.org/map)** · Free account · Global Fishing Watch · Tracks from 2012, port visits, encounters, loitering, AIS gaps and radar detections for the whole world. Built around fishing and carrier vessels, and about three days behind live.

### Open government AIS data

- **[MarineCadastre vessel traffic](https://hub.marinecadastre.gov/pages/vesseltraffic)** · Free · NOAA and BOEM · Bulk US-waters AIS from 2009 to the previous year, filtered to one position a minute, with GeoParquet files from 2024 onward. The deepest free raw AIS archive anywhere, but US waters only.
- **[Kystverket AIS](https://www.kystverket.no/en/sea-transport-and-ports/ais/access-to-ais-data/)** · Free (NLOD open licence) · Norwegian Coastal Administration · A live API for the Norwegian economic zone with no registration, plus historical files back to 2005 that include Norway's own satellite AIS. Small fishing and leisure craft are excluded, and full history needs an application.
- **[BarentsWatch AIS API](https://developer.barentswatch.no/)** · Free account · BarentsWatch, Norway · Developer API over the Norwegian AIS feed with about two weeks of history. Norway only.
- **[Danish AIS data](https://www.dma.dk/safety-at-sea/navigational-information/ais-data)** · Free · Danish Maritime Authority · Daily files of AIS for Danish waters, the approach to the Baltic. The shore network moved to the Danish Emergency Management Agency; historical files are supplied on application.
- **[Digitraffic Marine](https://www.digitraffic.fi/en/marine-traffic/)** · Free (CC BY 4.0) · Fintraffic, Finland · Live AIS over REST and MQTT plus Portnet port-call schedules, with commercial use allowed. Finland and the northern Baltic only; requests need a `Digitraffic-User` header.
- **[AMSA vessel traffic data](https://www.operations.amsa.gov.au/Spatial/DataServices/DigitalData)** · Free · Australian Maritime Safety Authority · Monthly AIS shapefiles for the Australian search-and-rescue region, at roughly hourly positions. Good free history for the Indo-Pacific approaches.
- **[Global Fishing Watch APIs](https://globalfishingwatch.org/our-apis/)** · Free account (non-commercial) · Global Fishing Watch · Vessel search, events, presence grids from 2012 to about four days ago, and radar detections through a documented API with a Python client. No commercial licence is offered.

### Raw feeds and your own receiver

- **[aisstream.io](https://aisstream.io/)** · Free account · aisstream.io (community project) · A live global WebSocket feed of AIS messages, filtered by bounding box or MMSI, with GitHub sign-in. No history, three connections per account, and connections must come from a server rather than a browser.
- **[AISHub](https://www.aishub.net/)** · Share-to-get · AISHub · A pooled raw AIS feed and API that you get access to by contributing a live feed from your own receiver. Live data only.
- **[AIS-catcher](https://github.com/jvde-github/AIS-catcher)** · Free (open source, GPL-3.0) · jvde-github · Turns an RTL-SDR or similar dongle and a small computer into an AIS receiver with a web map, and feeds AISHub or the commercial networks. Range is line of sight, a few tens of nautical miles.
- **[OpenCPN](https://opencpn.org/)** · Free (open source, GPL-2.0) · OpenCPN project · A chart plotter that shows AIS from your receiver over real charts and keeps a local log. Useful for offline analysis of your own feed.

*Last checked 2026-10-12.*

[↑ Back to top](#maritime-and-supply-chain-osint-tools)

---

## Who owns the AIS data

Most of the commercial vessel-tracking data that analysts use now belongs to two companies, and it is worth knowing how that happened before you build a workflow on a free tier.

**Kpler**, a commodities data firm, [bought MarineTraffic and FleetMon](https://www.kpler.com/blog/kpler-acquires-marinetraffic-and-fleetmon-for-maritime-sector-expansion) in March 2023, then [phased FleetMon out](https://support.marinetraffic.com/en/articles/9552991-fleetmon-and-marinetraffic-merge-process-for-former-fleetmon-ais-partners-from-january-2024) from January 2024 and asked its volunteer receiver hosts to redirect their feeds to MarineTraffic. In November 2024 it agreed to buy Spire's maritime business, including the exactEarth satellite constellation data, for [about $241 million](https://www.satellitetoday.com/finance/2024/11/13/spire-to-sell-maritime-business-to-kpler-in-241m-deal/). The deal [closed on 25 April 2025](https://kpler.com/blog/kpler-completes-acquisition-of-spire-maritime-strengthening-maritime-intelligence-capabilities) after Spire sued over the delay. The UK competition regulator [decided in July 2025](https://www.gov.uk/cma-cases/kpler-slash-spire-global-merger-inquiry) that it did not qualify for review. In September 2025 Kpler launched [Kpler AIS](https://support.marinetraffic.com/en/articles/12495052-19-september-2025-announcing-the-launch-of-kpler-ais), one feed from more than 13,000 receivers that replaces MarineTraffic AIS, and in June 2026 it took a [$1 billion investment](https://maritime-executive.com/article/kpler-secures-1-billion-investment-from-sixth-street) at a valuation near $4 billion.

**S&P Global** merged with IHS Markit on [28 February 2022](https://press.spglobal.com/2022-02-28-S-P-Global-Completes-Merger-with-IHS-Markit,-Creating-a-Global-Leader-to-Power-the-Markets-of-the-Future). That brought it the ship database that began life as Lloyd's Register-Fairplay (sold today as Sea-web and the Maritime Portal) and the Panjiva trade data. S&P Global also [assigns IMO ship numbers](https://www.imo.org/en/OurWork/IIIS/Pages/IMO-Identification-Number-Schemes.aspx) on the IMO's behalf, free of charge, and on 10 November 2025 it [completed the purchase of ORBCOMM's satellite AIS business](https://press.spglobal.com/2025-11-10-S-P-Global-Announces-Successful-Completion-of-its-Acquisition-of-ORBCOMMs-Automatic-Identification-System-Business). Of the other names you will meet, Lloyd's List Intelligence was [sold by Informa to Montagu Private Equity](https://montagu.com/montagu-acquires-maritime-intelligence-from-informa-plc/) in 2022, and Windward was [taken private by FTV Capital](https://www.uktech.news/ai/maritime-ai-firm-windward-bought-by-ftv-capital-in-216m-deal-20241224) in early 2025.

### Why it matters

Terrestrial AIS is collected by thousands of receivers, many of them run by volunteers who are [rewarded with subscriptions](https://support.marinetraffic.com/en/articles/9552976-what-benefits-do-i-get-as-an-ais-partner) rather than paid. The aggregated data is then sold back, and the free tiers have narrowed. A free MarineTraffic account shows about a day of track and no port calls or ownership, and the [Density plan was retired in 2025](https://support.marinetraffic.com/en/articles/13456094-mobile-pro-plan-faq). History, which is what an investigation needs, sits behind the paywall. Even the main NGO dataset depends on these companies: Global Fishing Watch [buys its AIS](https://globalfishingwatch.org/faqs/data-source-updates) from Spire (since 2023) and MarineTraffic (since 2024), and both now belong to Kpler.

None of this is a complaint about the companies. Collecting, cleaning and serving AIS at global scale costs money. It is a reason to know the open sources, to keep copies of what you download, and to say in your reports which source and date range you used.

### What is still open

- **United States**: NOAA and BOEM publish every year of US-waters AIS since 2009 through MarineCadastre, free and without an account.
- **Norway**: the Coastal Administration publishes a live feed under an open licence and historical files back to 2005 that include satellite AIS, with full history on application.
- **Denmark, Finland and Australia**: daily, live and monthly files respectively, for their own waters.
- **Global Fishing Watch**: tracks and events worldwide from 2012, free for non-commercial use, about four days behind live.
- **Live feeds**: aisstream.io is free and global but keeps no history; AISHub gives you the pool if you contribute a receiver.
- **Your own receiver**: a software-defined radio dongle and AIS-catcher give you ground truth for the stretch of coast you can see, and feed the pools above.

A [2025 study](https://arxiv.org/abs/2511.23016) rebuilt Baltic Sea vessel activity from open AIS alone and landed within 20 percent of results from proprietary data. Open data is thinner than the commercial feeds, but for coastal questions it is often enough. The entries are on the [vessel tracking](#vessel-tracking-ais) page.

*Sources checked 2026-10-12.*

[↑ Back to top](#maritime-and-supply-chain-osint-tools)

---

## Vessel identity and inspections

Who is this ship, who runs it, and has anyone inspected it lately? Start from the IMO number, because names, flags, MMSIs and call signs all change and the IMO number does not. Equasis and GISIS give the registered owner and the managers for free. The port state control databases give detention and deficiency histories. The class registers tell you whether a recognised society still stands behind the hull. Beneficial ownership, the person behind the one-ship company, takes the corporate records on the [next page](#ownership-sanctions-and-shadow-fleet).

Equasis and GISIS need an account and log your searches to it. If you query many ships at once, our [equasis-cli](#utilities-code-and-our-tools) does it from the command line.

### Identity and registration

- **[Equasis](https://www.equasis.org/)** · Free account · EMSA and a consortium of maritime administrations · Particulars, registered owner and managers, class, P&I cover and port state inspections for most merchant ships, and from 2026 a record of ship-to-ship transfers. The first stop for any vessel.
- **[IMO GISIS](https://gisis.imo.org/Public/SHIPS/Default.aspx)** · Free account · International Maritime Organization · The IMO's own ship and company records: name and flag history, IMO company numbers and registered addresses. The public modules need a free IMO web account.
- **[ITU MARS ship station search](https://mmsapp.itu.int/mmsapp/shipstation/list)** · Free · International Telecommunication Union · Looks up a ship by MMSI, call sign, name or distress-beacon identity and returns the administration that registered it. The quickest check that an MMSI matches a flag.
- **[Ships IO](https://shipsio.com/ships)** · Paid (30-day free trial, from $19.99/yr, 2026-10) · ShipVault LLC, Hawaii · Crowd-sourced database of about 160,000 large ships with technical and commercial details, linked companies, yards and parts. Cheap enough for individuals, but check its claims against Equasis.
- **[DNV Vessel Register](https://vesselregister.dnv.com/)** · Free · DNV · Class status, surveys and certificates for ships classed by DNV.
- **[ABS Record](https://www.eagle.org/portal/#/absrecord/search)** · Free · American Bureau of Shipping · Class records for ABS-classed ships.
- **[ClassNK Register of Ships](https://www.classnk.or.jp/register/regships/regships.aspx)** · Free · Nippon Kaiji Kyokai · Class records for the Japanese society's large fleet.
- **[Panama Maritime Authority](https://www.amp.gob.pa/)** · Free · Autoridad Marítima de Panamá · The world's largest flag registry; its public pages hold registry notices and verification services.
- **[Liberian Registry](https://www.liscr.com/)** · Free · LISCR · Public vessel and certificate lookups for the Liberian flag.
- **[Marshall Islands Registry](https://www.register-iri.com/)** · Free · International Registries, Inc. · Public information and lookups for the Marshall Islands flag.

### Port state control

- **[THETIS (Paris MoU)](https://portal.emsa.europa.eu/web/thetis/inspections)** · Free · EMSA for the Paris MoU · Inspection and detention records for ships calling in Europe, Canada and Russia's European ports.
- **[Tokyo MoU APCIS](https://www.tokyo-mou.org/inspections-detentions/psc-database/)** · Free · Tokyo MoU · Asia-Pacific inspection records in near real time. The database is hosted in Vladivostok.
- **[Indian Ocean MoU](https://www.iomou.org/)** · Free · Indian Ocean MoU · Inspection and detention data for the Indian Ocean region.
- **[Black Sea MoU](https://bsmou.org/)** · Free · Black Sea MoU · Inspection records for the Black Sea states. The public database is developed and hosted by the Russian Federation, and may not load from every network.
- **[USCG PSIX](https://cgmix.uscg.mil/PSIX/PSIXSearch.aspx)** · Free · US Coast Guard · Weekly snapshot of Coast Guard records: particulars, inspections, deficiencies and detentions for ships in US waters.

### Photos and yachts

- **[ShipSpotting](https://www.shipspotting.com/)** · Free account · AirNav Systems · Dated, crowd-sourced ship photos, useful for confirming a hull, a livery or a name change. Browsing is free; uploading needs an account.
- **[Superyachts.com Top 100](https://www.superyachts.com/top-100/)** · Free · Superyachts.com Ltd · Rankings and owner searches for the largest yachts, useful in sanctions and asset-tracing work.

*Last checked 2026-10-12.*

[↑ Back to top](#maritime-and-supply-chain-osint-tools)

---

## Ownership, sanctions and shadow fleet

The registered owner on a ship's papers is usually a one-ship company. Finding who stands behind it means corporate records, leaks databases and sanctions lists, and the free sources here are the same ones the big platforms build on. The fishing lists sit at the bottom because illegal fishing uses the same tricks (reflagging, renaming, dark periods) and the same tools find it. Tracking data for fishing vessels is on the [vessel tracking](#vessel-tracking-ais) page.

Two cautions. Sanctions screening by name alone misses most ships; screen by IMO number. And a tool run by an advocacy group is a lead to confirm against the official list, not a finding.

### Corporate and beneficial ownership

- **[OpenCorporates](https://opencorporates.com/)** · Freemium · OpenCorporates · The largest open database of companies and officers, with searches free on the web and the API and bulk data paid. Free API access is available to public-benefit projects on application.
- **[GLEIF LEI search](https://search.gleif.org/)** · Free · Global Legal Entity Identifier Foundation · Legal entity identifiers with registered addresses and parent relationships for companies that have one. Good for banks, traders and larger shipowners.
- **[ICIJ Offshore Leaks Database](https://offshoreleaks.icij.org/)** · Free · International Consortium of Investigative Journalists · Companies, officers and addresses from the Panama Papers, Paradise Papers, Pandora Papers and related leaks. The usual way into offshore shipowning structures.
- **[OCCRP Aleph](https://aleph.occrp.org/)** · Free account · Organized Crime and Corruption Reporting Project · Searchable archive of company registries, leaks and documents. Some collections are open only to journalists.

### Sanctions lists and screening

- **[OpenSanctions](https://www.opensanctions.org/)** · Freemium (free for non-commercial use) · OpenSanctions · Consolidated sanctions and politically exposed person data from more than a hundred sources, with vessels as entities matched to IMO numbers, flag histories and shadow-fleet tags. Commercial use needs a licence.
- **[OFAC Sanctions List Search](https://sanctionssearch.ofac.treas.gov/)** · Free · US Treasury · The official search of US designations, including vessels by IMO number.
- **[EU Sanctions Map](https://www.sanctionsmap.eu/)** · Free · European Union · Every EU sanctions regime with the legal acts and the listed persons, entities and vessels.
- **[UK Sanctions List](https://www.gov.uk/government/publications/the-uk-sanctions-list)** · Free · UK Foreign, Commonwealth and Development Office · The UK's consolidated designations, including ships specified under the Russia regime.
- **[UN Security Council Consolidated List](https://main.un.org/securitycouncil/en/content/un-sc-consolidated-list)** · Free · United Nations Security Council · All individuals, entities and vessels listed by the Council's sanctions committees.
- **[ArcNautical](https://arcnautical.com/check)** · Free · ArcNautical · Screens one IMO number against the OFAC, EU, UK and UN lists without an account, states which lists it could reach, and offers a keyless JSON endpoint. Launched in 2026; cross-check its result against OpenSanctions and the official lists.

### Shadow fleet trackers

- **[KSE Institute Shadow Fleet Tracker](https://sanctions.kse.ua/)** · Free · Kyiv School of Economics Institute · Monthly reports on Russian seaborne oil exports and the tankers carrying them. Reports and data downloads rather than a vessel search.
- **[Rendezvous](https://www.rdzvs.com/technology)** · Free account (early access; terms not yet published, 2026-10) · Rendezvous (an independent team working on the Baltic shadow fleet) · Scores vessels for shadow-fleet behaviour with a calibrated machine-learning model over AIS silences, encounters, flag history and port calls, and gives analysts a ranked triage console with the reasons for each score. Early-stage, with deployments around the Gulf of Finland and the Kerch Strait.
- **[UANI tanker tracker](https://www.unitedagainstnucleariran.com/)** · Free · United Against Nuclear Iran · A running list of several hundred tankers linked to Iranian oil. UANI is an advocacy group, so confirm against the official lists before you rely on an entry.

### Fishing and IUU

- **[Combined IUU Vessel List](https://iuu-vessels.org/)** · Free · Trygg Mat Tracking · Every regional fisheries organisation's list of vessels caught fishing illegally, merged with Interpol notices, with name and flag history, alerts and a spreadsheet download.
- **[FAO Global Record](https://globalrecord.fao.org/)** · Free · UN Food and Agriculture Organization · The Global Record of Fishing Vessels, with a unique vessel identifier and quick search by IMO, MMSI or call sign.
- **[WCPFC Record of Fishing Vessels](https://vessels.wcpfc.int/)** · Free · Western and Central Pacific Fisheries Commission · Public search and CSV download of vessels authorised to fish in the western and central Pacific, with photos and the option to include deleted records.
- **[IOTC vessel records](https://iotc.org/vessels)** · Free · Indian Ocean Tuna Commission · Authorised and IUU vessel lists for the Indian Ocean.
- **[ICCAT Record of Vessels](https://www.iccat.int/en/VesselsRecord.asp)** · Free · International Commission for the Conservation of Atlantic Tunas · Authorised vessels and the Atlantic IUU list.

*Last checked 2026-10-12.*

[↑ Back to top](#maritime-and-supply-chain-osint-tools)

---

## Satellite imagery and detection

Imagery is how you test what AIS tells you. Radar (SAR) sees ships through cloud and at night and is the main free way to find a vessel that has stopped transmitting; optical imagery confirms what the radar return is. The European Sentinel satellites make both free, with a revisit of a few days. Sentinel Hub's EO Browser, which many guides still link, was retired on 20 March 2026; the Copernicus Browser is its free replacement. Commercial high-resolution imagery is sold per scene, but two operators publish open samples and Vantor releases free imagery after major disasters.

### Free imagery browsers and archives

- **[Copernicus Browser](https://browser.dataspace.copernicus.eu/)** · Free account · European Space Agency for the European Commission · Sentinel-1 radar and Sentinel-2 optical imagery with search, time-lapse and download. Sentinel-1 is back to a six-day revisit since the 1C and 1D satellites came into service in 2025 and 2026.
- **[Copernicus Data Space](https://dataspace.copernicus.eu/)** · Free account · European Space Agency · The APIs behind the browser (STAC, OData and processing) for pulling Sentinel data into your own tools.
- **[NASA Worldview](https://worldview.earthdata.nasa.gov/)** · Free · NASA · Same-day, low-resolution global imagery from MODIS and VIIRS, enough to see weather, smoke, ice and large slicks.
- **[NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/)** · Free · NASA · Active fire and thermal anomaly detections, including flaring at offshore platforms and fires at sea.
- **[OpenAerialMap](https://map.openaerialmap.org/)** · Free (open licences) · Humanitarian OpenStreetMap Team · Openly licensed aerial and drone imagery uploaded by mappers and responders, much of it very high resolution and much of it after disasters. Patchy, but where it exists it beats satellite imagery.
- **[EOS LandViewer](https://eos.com/landviewer/)** · Freemium · EOS Data Analytics · Browser for Sentinel, Landsat and some commercial imagery with analysis tools; the free tier allows a small number of scenes a month.

### Dark vessel and anomaly detection

- **[Bellingcat Ship Detection Tool](https://ollielballinger.users.earthengine.app/view/ship-detection-tool)** · Free · Ollie Ballinger for Bellingcat · Counts and plots ships in Sentinel-1 radar imagery for any area and date range, including ships with AIS off. Runs in Google Earth Engine; Bellingcat's 2023 guide explains the method.
- **[Global Fishing Watch data portal](https://globalfishingwatch.org/data-download/)** · Free account (non-commercial) · Global Fishing Watch · Downloads of radar vessel detections matched to AIS (from 2017), fishing effort and other derived datasets. The radar layer is the simplest global view of unmatched, likely dark, vessels.
- **[SkyTruth Cerulean](https://cerulean.skytruth.org/)** · Free · SkyTruth · Oil slicks detected in Sentinel-1 radar, with the likely source vessel or platform suggested from AIS, through a map and an API. Vessel attribution runs a few days behind.
- **[Skylight](https://www.skylight.global/)** · On application · Allen Institute for AI (Ai2) · Maritime monitoring platform that fuses AIS, radar and optical detections into alerts, free to governments, regional bodies and NGOs working on illegal fishing and maritime security.
- **[VIIRS Boat Detection](https://eogdata.mines.edu/products/vbd/)** · Free · Earth Observation Group, Colorado School of Mines · Nightly detections of lit fishing boats from the VIIRS day-night band, useful for squid and other light-attracting fleets.

### Open commercial imagery

- **[Vantor Open Data Program](https://vantor.com/company/open-data-program/)** · Free (CC BY-NC 4.0) · Vantor (formerly Maxar Intelligence) · High-resolution before-and-after imagery released for major disasters as a catalogue on AWS. Event-driven rather than on demand, and non-commercial use only.
- **[Vantor Discover](https://xpress.maxar.com/)** · Freemium · Vantor · Browse previews of the commercial high-resolution archive for free; buying a scene is quote-based. The portal kept its Maxar address after the 2025 rename.
- **[Umbra Open Data](https://umbra.space/open-data/)** · Free (CC BY 4.0) · Umbra · Very high-resolution radar imagery of about twenty fixed sites, some of them ports, with no sign-up. A good way to learn what commercial SAR can show.
- **[Capella Open Data](https://registry.opendata.aws/capella_opendata/)** · Free (CC BY 4.0) · Capella Space · Sample high-resolution radar scenes on AWS. Capella has been owned by IonQ since July 2025.
- **[SkyFi](https://skyfi.com/)** · Paid · SkyFi · Marketplace for buying archive imagery or new tasking from several satellite operators by the scene, for people who need one picture rather than a contract.

*Last checked 2026-10-12.*

[↑ Back to top](#maritime-and-supply-chain-osint-tools)

---

## Ports, chokepoints and infrastructure

What is normal for this port or strait, and what has changed? The IMF's PortWatch is the free answer for traffic volumes at ports and chokepoints; the NGA's World Port Index tells you what a port can physically handle. The rest of this page is the fixed geography of the sea: cables, pipelines, terminals and the boundaries that decide whose rules apply.

### Ports and chokepoints

- **[IMF PortWatch](https://portwatch.imf.org/)** · Free · International Monetary Fund with the University of Oxford · Daily port calls and trade volume estimates for about 1,800 ports and transit counts for the main chokepoints, updated weekly, with an ArcGIS API. The figures are modelled from AIS and get revised.
- **[NGA World Port Index](https://msi.nga.mil/Publications/WPI)** · Free · US National Geospatial-Intelligence Agency · Publication 150: location, depths, facilities and services for several thousand ports, as a spreadsheet or GIS layer.
- **[UNCTAD Liner Shipping Connectivity Index](https://unctadstat.unctad.org/datacentre/)** · Free · UN Trade and Development · Quarterly index of how well each country and port is connected to container shipping networks, inside the UNCTADstat data centre.
- **[Container Port Performance Index](https://www.worldbank.org/en/topic/transport/publication/cppi)** · Free · World Bank and S&P Global Market Intelligence · Annual ranking of about 400 container ports by time in port, built from AIS, with the report and the data file for download.
- **[Port Optimizer](https://www.portoflosangeles.org/business/supply-chain/port-optimizer)** · Free account · Port of Los Angeles with Wabtec · Volumes, forecasts and container tracking for the port of Los Angeles. One of the few ports that publishes forward-looking data.

### Cables, pipelines and boundaries

- **[TeleGeography Submarine Cable Map](https://www.submarinecablemap.com/)** · Free · TeleGeography · The standard interactive map of submarine cables and landing stations, covering 694 systems in its 2026 edition.
- **[SubTel Forum Cable Map](https://subtelforum.com/submarine-cable-map/)** · Free · Submarine Telecoms Forum · A second cable map that also shows the cable-ship fleet and planned systems.
- **[Global Gas Infrastructure Tracker](https://globalenergymonitor.org/projects/global-gas-infrastructure-tracker/)** · Free (CC BY 4.0) · Global Energy Monitor · LNG terminals and gas pipelines worldwide, with ownership and status, downloadable after a short form.
- **[Marine Regions](https://www.marineregions.org/)** · Free · Flanders Marine Institute (VLIZ) · Exclusive economic zones, territorial seas and other maritime boundaries as downloadable geodata. The reference layer for "whose waters is this ship in".
- **[OpenInfraMap](https://openinframap.org/)** · Free · Russ Garrett · Power lines, telecoms, oil and gas infrastructure drawn from OpenStreetMap, including offshore platforms and pipelines.

*Last checked 2026-10-12.*

[↑ Back to top](#maritime-and-supply-chain-osint-tools)

---

## Cargo, containers and trade data

What is in the box, who shipped it, and does the trade flow make sense? Container tracking is free as long as you have a container or booking number. Shipment records come from customs releases of bills of lading, which are public in the United States and sold everywhere else. Trade statistics from the UN, the World Bank and national agencies are free and are the quickest way to check whether a claimed flow is plausible at all.

The commercial shipment databases (Panjiva, ImportGenius, Datamyne, Volza and others) are on the [commercial platforms](#commercial-platforms) page; ImportYeti covers the free part of the same US data.

### Container tracking

- **[Track-Trace](https://www.track-trace.com/container)** · Free · Webfokus, Norway · Sends a container number to the right page of about 170 carriers. Nothing stored, nothing to sign up for.
- **[SeaRates container tracking](https://www.searates.com/container/tracking/)** · Freemium · DP World · Tracks by container, bill of lading or booking number across most carriers and shows the carrying vessel's position. Free lookups are limited without an account.
- **[ShipsGo](https://www.shipsgo.com/)** · Freemium · ShipsGo · Multi-carrier container tracking with a few free lookups, then per-shipment credits and an API.
- **[BIC container owner codes](https://www.bic-code.org/bic-codes)** · Free · Bureau International des Containers · The register behind the first three letters of every container number: who owns or operates the box.

### Bills of lading and facilities

- **[ImportYeti](https://www.importyeti.com/)** · Freemium · ImportYeti · US import bills of lading searchable by company, supplier and product, free with limits on how much detail you see. The free way into the data Panjiva and ImportGenius sell.
- **[Open Supply Hub](https://opensupplyhub.org/)** · Free (API from $225/month, 2026-10) · Open Supply Hub · An open database of production facilities with names, addresses and the brands that list them. Search and downloads are free; the API is paid.

### Trade statistics

- **[UN Comtrade](https://comtradeplus.un.org/)** · Free account · UN Statistics Division · Bilateral trade by product code for almost every country, with a free API key subject to daily limits.
- **[ITC Trade Map](https://www.trademap.org/)** · Free account · International Trade Centre · Trade flows, tariffs and market indicators by product and country, with company directories for some markets.
- **[WITS](https://wits.worldbank.org/)** · Free · World Bank · Trade and tariff data with bulk download and an API, drawing on Comtrade and tariff databases.
- **[Eurostat Comext](https://ec.europa.eu/eurostat/web/international-trade-in-goods/database)** · Free · Eurostat · EU trade in goods at eight-digit product detail by partner country and month.
- **[USA Trade Online](https://usatrade.census.gov/)** · Free account · US Census Bureau · US imports and exports at ten-digit detail by country, district and port.
- **[OEC](https://oec.world/)** · Freemium · Datawheel · Visual explorer of trade flows by country and product, built on Comtrade and national data. Good for a first picture; check the numbers at source.
- **[Resource Trade Earth](https://resourcetrade.earth/)** · Free · Chatham House · Trade in natural resources (fuels, metals, agricultural goods) by country pair, with maps and downloads.

### Freight rates

- **[Drewry World Container Index](https://www.drewry.co.uk/supply-chain-advisors/supply-chain-expertise/world-container-index-assessed-by-drewry)** · Free (headline) · Drewry · Weekly spot container rates on the main east-west routes. The headline figures are free; the detail is a subscription.
- **[Freightos Baltic Index](https://fbx.freightos.com/)** · Freemium · Freightos · Daily container spot index by lane; headline rates are free and the full series is paid.

*Last checked 2026-10-12.*

[↑ Back to top](#maritime-and-supply-chain-osint-tools)

---

## Security incidents and warnings

What has happened in this stretch of water, and what are the authorities warning about? The reporting centres below are where ships report attacks and suspicious approaches, and most publish their incident records and advisories for free. The NGA's anti-shipping activity messages go back decades and are the best free historical series of attacks with coordinates. Conflict maps round out the picture where war, rather than crime, is the hazard.

Our own platform, MARA, is on this page too. It is a commercial product and we say so; the free sources above it are what it builds on.

### Reporting centres and advisories

- **[UKMTO](https://www.ukmto.org/)** · Free · UK Maritime Trade Operations (Royal Navy) · Advisories and incident reports for the Red Sea, Gulf of Aden, Arabian Sea and the Gulf, and the voluntary reporting scheme ships use there.
- **[Maritime Security Centre Indian Ocean](https://www.mscio.eu/)** · Free account · EU Naval Force · Threat assessments, incident updates and voluntary registration for ships transiting the Red Sea, Gulf of Aden and western Indian Ocean. The successor to MSCHOA, the Horn of Africa centre.
- **[ReCAAP ISC](https://www.recaap.org/)** · Free account · ReCAAP Information Sharing Centre, Singapore · Incident reports, weekly and annual statistics and a searchable map for piracy and armed robbery in Asia. The dashboard needs a free account.
- **[IMB](https://www.icc-ccs.org/icc/imb)** · Free · ICC International Maritime Bureau · Runs the 24-hour Piracy Reporting Centre that collects attack reports worldwide and publishes quarterly statistics and an incident map.
- **[MICA Center](https://www.mica-center.org/)** · Free · French Navy · The Brest centre that hosts MDAT-GoG, the French and British reporting and advisory service for the Gulf of Guinea, and publishes annual and weekly maritime security reports.
- **[NGA Maritime Safety Information](https://msi.nga.mil/)** · Free · US National Geospatial-Intelligence Agency · Navigation warnings, broadcast warnings and the Anti-Shipping Activity Messages (ASAM) database, a geocoded record of attacks and suspicious approaches going back to the 1980s.
- **[ONI Worldwide Threat to Shipping](https://www.oni.navy.mil/news/shipping-threat-reports/)** · Free · US Office of Naval Intelligence · Weekly summary of threats and incidents by region, compiled from the reporting centres and open sources.
- **[MARA](https://maraiq.com/)** · Paid (contact us) · Atlas Bear (ours) · Our maritime security intelligence platform: round-the-clock monitoring of security incidents with alerts, intelligence reports, daily hot spots and country and port indices. Feedback and the public roadmap are on GitHub.
- **[Phantom Tide](https://phantom.labs.jamessawyer.co.uk/)** · Free account (Starter tier; higher tiers exist, prices not published, 2026-10) · James Sawyer · Analyst dashboard that ranks hotspots where vessel tracks, aircraft, navigation warnings, weather, satellite detections and GNSS interference overlap, with a notebook and area reports. A hosted app with closed source; the public repository holds the docs and release notes.

### Conflict maps and event databases

- **[Maritime Cyber Attack Database](https://maritimecybersecurity.nl/)** · Free · NHL Stenden University of Applied Sciences, Netherlands · About 300 cyber incidents against ships, ports and maritime companies since 2001, with a map filterable by victim, attacker, country and year.
- **[GDELT](https://www.gdeltproject.org/data.html)** · Free · The GDELT Project · Machine-coded records of news events and mentions worldwide, downloadable in bulk or through BigQuery. Noisy, but a quick way to see what was reported about a port or sea area on a given day.

- **[Liveuamap](https://liveuamap.com/)** · Freemium · Liveuamap · Geolocated news events, including strikes on shipping and ports in the Black Sea and the Red Sea. Ad-supported, with an optional ad-free subscription.
- **[Eyes on Russia map](https://eyesonrussia.org/)** · Free · Centre for Information Resilience · Verified, geolocated incidents from the war in Ukraine, including Black Sea and port events, built with C4ADS.
- **[ACLED](https://acleddata.com/)** · Free account (non-commercial) · Armed Conflict Location and Event Data · Coded political violence and protest events worldwide, including attacks on ports and shipping, downloadable after registration.

*Last checked 2026-10-12.*

[↑ Back to top](#maritime-and-supply-chain-osint-tools)

---

## Maps, weather and charts

The general mapping tools every OSINT analyst uses are covered well by [Bellingcat's toolkit](https://bellingcat.gitbook.io/toolkit) and we do not repeat them. The ones here earn a maritime sentence. Historical imagery shows a port changing. Russian and Chinese maps cover ports the Western providers cover thinly. Weather and currents test whether a claimed track is physically possible, and charts check draught against depth.

### Maps and street-level imagery

- **[Google Earth](https://www.google.com/earth/about/versions/)** · Free · Google · The desktop Pro version has a historical imagery slider, the easiest way to watch a berth, a terminal or a shipyard change over years.
- **[OpenStreetMap](https://www.openstreetmap.org/)** · Free · OpenStreetMap Foundation · Community-mapped berths, terminals, piers and port infrastructure with tags you can query.
- **[OpenSeaMap](https://www.openseamap.org/)** · Free · OpenSeaMap · A nautical overlay on OpenStreetMap: buoys, lights, harbours and anchorages.
- **[Bing Maps](https://www.bing.com/maps)** · Free · Microsoft · A second aerial imagery source, often from a different date than Google's, with bird's-eye views of many ports.
- **[Yandex Maps](https://yandex.com/maps)** · Free · Yandex · The best coverage and street panoramas for Russian and Central Asian ports.
- **[Baidu Maps](https://map.baidu.com/)** · Free · Baidu · Coverage and street views of Chinese ports. It uses its own shifted coordinate system, so convert before you compare positions.
- **[DualMaps](https://data.mapchannels.com/dualmaps8/map.htm)** · Free · MapChannels · Road map, aerial view and Street View side by side for one point.
- **[WikiMapia](https://wikimapia.org/)** · Free · WikiMapia · Crowd-labelled places, including industrial sites, terminals and naval facilities that official maps leave blank.
- **[KartaView](https://kartaview.org/)** · Free · Grab · Crowd-sourced street-level photos, useful where Street View has nothing.
- **[PeakFinder](https://www.peakfinder.com/)** · Free · PeakFinder GmbH · Draws the mountain skyline from any viewpoint, which geolocates many coastal photographs.
- **[GeoNames](https://www.geonames.org/)** · Free · GeoNames · Gazetteer of place names with coordinates and alternate spellings, for matching ports named in several languages.

### Weather and sea state

- **[Windy](https://www.windy.com/)** · Freemium · Windyty SE · Wind, wave, swell and current forecasts and recent history from several models. A quick check on whether a claimed speed or route makes sense.
- **[earth.nullschool](https://earth.nullschool.net/)** · Free · Cameron Beccario · Animated global wind, ocean current and wave fields, with a time slider.
- **[Zoom Earth](https://zoom.earth/)** · Freemium · Neave Interactive · Near-real-time weather satellite imagery and storm tracks that affect shipping routes.
- **[Copernicus Marine](https://marine.copernicus.eu/)** · Free account · Mercator Ocean International · Ocean current, wave, temperature and sea-ice datasets, for drift and feasibility analysis.

### Charts and bathymetry

- **[GEBCO](https://www.gebco.net/)** · Free · GEBCO (IHO and IOC) · The global bathymetry grid. Can a ship of this draught be where its AIS says it is?
- **[NOAA ENC Viewer](https://www.nauticalcharts.noaa.gov/enconline/enconline.html)** · Free · NOAA Office of Coast Survey · US electronic navigational charts in the browser.
- **[Navionics ChartViewer](https://webapp.navionics.com/)** · Free · Garmin · Worldwide nautical charts with depths and anchorages in the browser.
- **[EMODnet](https://emodnet.ec.europa.eu/)** · Free · European Commission · European marine data: bathymetry, human activities (cables, pipelines, wind farms, dredging) and more as map layers and downloads.

*Last checked 2026-10-12.*

[↑ Back to top](#maritime-and-supply-chain-osint-tools)

---

## Commercial platforms

> **Read this first.** The platforms on this page are enterprise products priced for shipping companies, insurers, banks and governments. Most publish no price; expect a contract rather than a credit card. We list them because readers ask what the big names do, and because reports and news stories cite them. For most investigations the free sources on the earlier pages answer the same question, more slowly. Each group below names the free page to start from.

Ownership changes fast in this market. Kpler owns MarineTraffic, FleetMon and the former Spire Maritime; S&P Global owns the Sea-web ship database and Panjiva; Lloyd's List Intelligence belongs to Montagu; Windward to FTV Capital. The [AIS data note](#who-owns-the-ais-data) has the details and dates.

### Vessel tracking and maritime intelligence

Free alternatives: [vessel tracking](#vessel-tracking-ais) and [vessel identity](#vessel-identity-and-inspections).

- **[Kpler](https://www.kpler.com/)** · Enterprise quote · Kpler · Commodity flows, cargo tracking and the combined MarineTraffic, FleetMon and Spire AIS feeds, sold as a platform and as data.
- **[S&P Global Market Intelligence](https://www.spglobal.com/market-intelligence/en/)** · Enterprise quote · S&P Global · Sea-web and the Maritime Portal (the ship database descended from Lloyd's Register-Fairplay), satellite AIS from the former ORBCOMM business, and Panjiva trade data.
- **[Lloyd's List Intelligence](https://www.lloydslistintelligence.com/)** · Enterprise quote · Lloyd's List Intelligence (Montagu) · Seasearcher vessel database, risk and compliance screening, casualty records and the Lloyd's List news service.
- **[Windward](https://www.windward.ai/)** · Enterprise quote · Windward (FTV Capital) · AI risk scores for vessels and companies, dark activity and sanctions compliance workflows.
- **[Pole Star Global](https://www.polestarglobal.com/)** · Enterprise quote · Pole Star Global · PurpleTRAC sanctions screening and fleet monitoring, widely used by banks and traders.
- **[Vortexa](https://www.vortexa.com/)** · Enterprise quote · Vortexa · Cargo-level tracking of oil, gas and refined products, with analytics on floating storage and shadow fleet flows.
- **[Starboard Maritime Intelligence](https://starboard.nz/)** · Enterprise quote · Starboard, New Zealand · Vessel risk and dark activity analytics aimed at governments and fisheries agencies in the Pacific and beyond.
- **[TankerTrackers.com](https://www.tankertrackers.com/)** · Paid (Corporate Lite $12,000/yr, 2026-10) · TankerTrackers.com · Tanker movements, floating storage and sanctioned oil flows from imagery and AIS. Retail tiers are closed to new subscribers.
- **[Worldwide AIS Network](https://www.worldwideais.org/)** · Enterprise quote · Worldwide AIS Network ApS, Copenhagen · Live and regional AIS feeds over REST, WebSocket and raw NMEA, with a free data sample for evaluation. A smaller alternative to the Kpler and S&P feeds.
- **[Datalastic](https://datalastic.com/)** · Paid (from about €199/month, 2026-10) · Datalastic · A developer-oriented AIS and vessel data API, one of the cheaper paid routes to programmatic positions. The site refuses some automated and overseas requests.

### Radar, optical and RF detection

Free alternatives: [satellite imagery and detection](#satellite-imagery-and-detection).

- **[ICEYE](https://www.iceye.com/)** · Enterprise quote · ICEYE · Tasked high-resolution radar imagery and dark vessel detection products.
- **[Unseenlabs](https://unseenlabs.space/)** · Enterprise quote · Unseenlabs · Geolocation of ships from their radio-frequency emissions, independent of AIS.
- **[HawkEye 360](https://www.he360.com/)** · Enterprise quote · HawkEye 360 · Radio-frequency geolocation and maritime domain awareness products for governments.
- **[SynMax](https://www.synmax.com/)** · Enterprise quote · SynMax · Theia, a dark vessel detection platform combining radar and optical imagery with AIS.
- **[Planet](https://www.planet.com/)** · Enterprise quote · Planet Labs · Daily optical imagery of the whole land surface and coasts, plus the Sentinel Hub APIs under the Planet Insights Platform.

### Ownership, sanctions and risk

Free alternatives: [ownership, sanctions and shadow fleet](#ownership-sanctions-and-shadow-fleet).

- **[Sayari](https://sayari.com/)** · Enterprise quote · Sayari · Corporate ownership graph built from public records in many jurisdictions, with trade and sanctions risk screening.
- **[Kharon](https://www.kharon.com/)** · Enterprise quote · Kharon · Research and data on sanctions, export controls and the networks around designated parties.
- **[Altana](https://altana.ai/)** · Enterprise quote · Altana · Supply chain network mapping across shipment and corporate records.
- **[Sourcemap](https://www.sourcemap.com/)** · Enterprise quote · Sourcemap · Supplier mapping and traceability for regulatory due diligence. The free edition we once listed is gone.

### Trade and shipment data

Free alternatives: [cargo, containers and trade data](#cargo-containers-and-trade-data).

- **[Panjiva](https://panjiva.com/)** · Enterprise quote · S&P Global · Bills of lading and shipment records for many countries, with company profiles and network views.
- **[ImportGenius](https://www.importgenius.com/)** · Paid · ImportGenius · US and other customs shipment records with published subscription plans.
- **[Descartes Datamyne](https://www.datamyne.com/)** · Enterprise quote · Descartes · Import and export records for the Americas and beyond.
- **[Volza](https://www.volza.com/)** · Paid · Volza · Export and import shipment data for a large set of countries, sold by subscription.
- **[Linerlytica](https://www.linerlytica.com/)** · Paid · Linerlytica · Container shipping market analysis and port congestion tracking.
- **[Sea-Intelligence](https://www.sea-intelligence.com/)** · Paid · Sea-Intelligence · Liner schedule reliability and container market research.

### Security and risk advisories

Free alternatives: [security incidents and warnings](#security-incidents-and-warnings).

- **[Ambrey](https://ambrey.com/)** · Enterprise quote · Ambrey · Maritime security advisories, intelligence and armed guarding.
- **[Dryad Global](https://dryadglobal.com/)** · Enterprise quote · Dryad Global · Maritime risk intelligence and advisories, with some free weekly commentary.
- **[Risk Intelligence](https://riskintelligence.eu/)** · Enterprise quote · Risk Intelligence, Denmark · The MaRisk system of port and sea-area threat assessments.

*Last checked 2026-10-12.*

[↑ Back to top](#maritime-and-supply-chain-osint-tools)

---

## Utilities, code and our tools

Once you are looking at more than a handful of ships, you need code. It queries Equasis in batches, decodes AIS messages, plots a million positions, and archives what you found before it changes. These are the libraries and small tools we reach for, starting with the two we wrote ourselves.

### Our tools

- **[equasis-cli](https://github.com/rhinonix/equasis-cli)** · Free (open source, PolyForm Noncommercial) · Atlas Bear (ours) · Looks up vessels, port state inspections, ownership history and company fleets in Equasis from the command line, an interactive shell or Python, handles batches of hundreds of ships, and flags renames, reflagging, detentions and missing P&I cover. Needs your own free Equasis account; install from PyPI or this repository only.
- **[cue-kit](https://github.com/atlas-bear/cue-kit)** · Free (open source, AGPL-3.0) · Atlas Bear (ours) · Turns a video URL or file into extracted frames and a timestamped transcript that a language model can actually read, with a bundled Claude Code skill for asking questions about footage. Alpha, and useful for port and vessel videos.

### Libraries and code

- **[pyais](https://github.com/M0r13n/pyais)** · Free (open source, MIT) · Leon Morten Richter · Python library that decodes and encodes AIS NMEA sentences, the first thing you need to read a raw feed or a receiver log.
- **[gfw-api-python-client](https://github.com/GlobalFishingWatch/gfw-api-python-client)** · Free (open source, Apache-2.0) · Global Fishing Watch · Official Python client for the Global Fishing Watch APIs: vessel search, events and presence grids straight into pandas.
- **[Bellingcat auto-archiver](https://github.com/bellingcat/auto-archiver)** · Free (open source, MIT) · Bellingcat · Archives web pages, posts and media from a spreadsheet of URLs, with hashes and timestamps, so that a vessel page or a port notice is preserved before it changes.
- **[QGIS](https://qgis.org/)** · Free (open source, GPL-2.0) · QGIS project · Desktop GIS for laying AIS points, EEZ boundaries, bathymetry and satellite imagery on one map. Plugins pull Copernicus and Vantor open data in directly.
- **[Kepler.gl](https://kepler.gl/)** · Free (open source, MIT) · OpenJS Foundation · Browser tool that plots millions of points from a CSV or GeoParquet file with a time slider, which is how we first look at a bulk AIS download.
- **[bbox finder](https://bboxfinder.com/)** · Free (open source) · CUGOS · Draw a box on a map and get its coordinates in the format an API wants, which is the quickest way to set up an aisstream.io or Copernicus filter.
- **[VESSA dataset](https://zenodo.org/records/17246832)** · Free (GPL-3.0) · Pablo Rangel and colleagues, Brazilian Navy Research Institute and UFRJ · More than 200,000 labelled vessel images in 25 categories for training detectors and classifiers, published on Zenodo in November 2025.
- **[SunCalc](https://www.suncalc.org/)** · Free · Torsten Hoffmann · Sun position and shadow length for any place and time, for dating or placing a photograph of a ship or a port.
- **[Shodan](https://www.shodan.io/)** · Freemium · Shodan · Search engine for internet-exposed devices, including ships' satellite terminals and port systems. Its old AIS ship tracker is gone and AIS data is now sold only as a bulk dataset.
- **[Hunchly](https://hunch.ly/)** · Paid · Hunchly · Browser extension that captures and hashes every page you visit during an investigation, which is the evidence trail you want when a vessel page changes after you cite it.

*Last checked 2026-10-12.*

[↑ Back to top](#maritime-and-supply-chain-osint-tools)

---

## Learning and reference

The method matters more than the tool. These are the guides we point students to, the training we run or take part in, and the general OSINT lists that cover everything this list leaves out on purpose.

### Guides and handbooks

- **[UN AIS Handbook](https://unstats.un.org/wiki/spaces/AIS/overview)** · Free · UN Committee of Experts on Big Data, AIS Task Team · The method handbook for cleaning and analysing AIS data for statistics, with worked examples. Most pages date from 2020 to 2023, but the fundamentals have not moved.
- **[Peering Beyond the Clouds](https://www.bellingcat.com/resources/2023/05/11/peering-beyond-the-clouds-a-guide-to-bellingcats-ship-detection-tool/)** · Free · Bellingcat · The 2023 guide to finding ships in Sentinel-1 radar imagery with the Ship Detection Tool, and the best short introduction to SAR for analysts.
- **[Bellingcat Online Investigation Toolkit](https://bellingcat.gitbook.io/toolkit)** · Free · Bellingcat · Hundreds of tool pages with cost, requirements, limitations and ethical notes, including a maritime section updated in 2026. Our pointer for general OSINT tools.
- **[GIJN: Tracking Ships at Sea](https://gijn.org/resource/tracking-ships-at-sea/)** · Free · Global Investigative Journalism Network · A reporter's guide to vessel tracking, ownership and imagery, with case examples.
- **[Deep Dive by Rae Baker](https://deepdive.raebaker.net/)** · Free · Rae Baker · Maritime OSINT guides from the author of *Deep Dive*, including a maritime patterning framework, port analysis and a Raspberry Pi AIS receiver build.
- **[C4ADS](https://c4ads.org/)** · Free · C4ADS · Reports on illicit networks, sanctions evasion and the shadow fleet, with the data-driven method laid out in each one.
- **[Setting up an SDR AIS receiver with AIS-catcher](https://www.worldwideais.org/post/how-to-set-up-sdr-ais-receiver-ais-catcher)** · Free · Worldwide AIS Network ApS · A step-by-step guide to building your own AIS receiver from a software-defined radio dongle, written by a commercial feed provider.
- **[Free government nautical charts](https://blog.anchorages.co/tools/free-nautical-charts/)** · Free · Anchorages · A maintained list of the national hydrographic offices that give their charts away, with links.

### Data and reference

- **[World Factbook Archive](https://worldfactbookarchive.org/)** · Free (open source, MIT) · MilkMp, a community project not affiliated with the CIA · Every edition of the CIA World Factbook from 1990 to 2025 as a searchable site, a database and a free offline app, after the CIA discontinued the Factbook on 4 February 2026. Its Intelligence Atlas layers submarine cables, shipping routes, chokepoints and EEZ boundaries over the country data.
- **[ODIS Catalogue of Sources](https://catalogue.odis.org/)** · Free · UNESCO/IOC Project Office for IODE · A searchable catalogue of more than 3,000 ocean data and information sources, for finding the agency that holds the dataset you need.
- **[Allianz Safety and Shipping Review](https://commercial.allianz.com/news-and-insights/reports/shipping-safety.html)** · Free · Allianz Commercial · The annual review of ship losses, casualties and risk trends, the standard open reference on what goes wrong at sea and where.
- **[The Organized Crime Index](https://ocindex.net/)** · Free · Global Initiative Against Transnational Organized Crime · Country scores for criminal markets and actors, from arms and drugs to human trafficking, with the methodology published. Useful context for any illicit trade case.
- **[Shipmap.org](https://www.shipmap.org/)** · Free · Kiln and the UCL Energy Institute · An animated map of the world's merchant shipping over one year, built from 2012 AIS data. Old, but the best single picture of how trade moves for a classroom.
- **[AIS datasets on Kaggle](https://www.kaggle.com/datasets?search=ais)** · Free account · Kaggle (Google) · Practice datasets of AIS positions uploaded by users, mostly copies of public releases such as MarineCadastre and the Danish files, for learning to clean and plot tracks.

### Training

- **[Summer School on Illicit Trade](https://www.rug.nl/education/summer-winter-schools/illicit-trade)** · Paid (fee published per edition) · University of Groningen · The annual summer school where this list gets used and tested each year, with sessions on maritime and supply-chain OSINT.
- **[Atlas Bear Academy](https://www.atlasbear.academy/)** · Paid (contact us) · Atlas Bear (ours) · Our professional development programmes in maritime security and supply chain intelligence.

### Other lists

- **[awesome-osint](https://github.com/jivoi/awesome-osint)** · Free · jivoi and contributors · The largest general OSINT list, with about 1,450 entries. Its maritime section is three lines long, which is why this list exists.
- **[OSINT Framework](https://osintframework.com/)** · Free · Justin Nordine · A categorised tree of general OSINT tools with registration and pricing markers and a weekly link check.

*Last checked 2026-10-12.*

[↑ Back to top](#maritime-and-supply-chain-osint-tools)

---

## Glossary

Short definitions of the terms the entries use. The [UN AIS Handbook](https://unstats.un.org/wiki/spaces/AIS/overview) and the IMO's [identification number page](https://www.imo.org/en/OurWork/IIIS/Pages/IMO-Identification-Number-Schemes.aspx) go deeper.

**IMO number.** A seven-digit identifier (the last digit is a check digit) that stays with a ship's hull for life, through renames, reflaggings and sales. It is mandatory for most seagoing merchant ships under SOLAS. S&P Global assigns the numbers free of charge on behalf of the IMO. There is also an IMO company number for owners and managers. Start every vessel search from the IMO number if you have it.

**MMSI.** The nine-digit Maritime Mobile Service Identity that a ship's radio and AIS transmit. The first three digits (the MID) identify the flag state. An MMSI changes when a ship reflags, so it is not a permanent identifier, and shadow-fleet ships sometimes transmit MMSIs that do not match their flag or that belong to another ship.

**Call sign.** The radio identifier assigned by the flag state. It also changes on reflagging. The ITU MARS database maps call signs and MMSIs to ships and administrations.

**AIS.** The Automatic Identification System, a VHF broadcast of position, course, speed and identity. Class A transponders are compulsory for ships of 300 gross tonnage and up on international voyages and for all passenger ships. Class B units are cheaper, transmit less often and at lower power, and are what most small craft carry. Terrestrial AIS is picked up by shore receivers (many of them volunteer-run) within a few tens of nautical miles. Satellite AIS fills the gaps at sea, at a cost.

**AIS gap, or dark activity.** A period with no AIS positions. Causes range from poor coverage and a switched-off transponder to deliberate concealment. A gap is a lead, not proof, and the free government and NGO sources on the tracking page are where to check coverage before drawing conclusions.

**Spoofing.** Transmitting false AIS data, most often a false position (a ship appears somewhere it is not) or a false identity. Radar imagery and port records are the usual ways to test a suspected spoof.

**STS transfer.** A ship-to-ship transfer of cargo at sea or at anchor, used legitimately for lightering and illegitimately to obscure the origin of sanctioned oil. Equasis began carrying STS data in 2026.

**Port state control (PSC).** Inspections of foreign ships in national ports. Results, including detentions and deficiencies, are published by regional agreements called MoUs (Paris, Tokyo, Indian Ocean, Black Sea and others) and by the US Coast Guard. A detention history is one of the strongest free risk signals.

**Flag state and open registries.** The country whose flag a ship flies sets its rules and issues its documents. Open registries (often called flags of convenience) register ships owned elsewhere. Several publish searchable registers; some do not.

**Registered owner, beneficial owner and ISM manager.** The registered owner is the company on the papers, often a one-ship shell. The beneficial owner is the person or group who controls and profits from the ship, and is usually what an investigation wants. The ISM manager (or DOC company) runs the ship day to day under the International Safety Management Code. Equasis and GISIS show registered owners and managers; beneficial ownership takes corporate records.

**Classification society.** An organisation that sets technical standards and surveys ships against them. Class status and class history are public in several registers. A class withdrawal is a warning sign.

**P&I club.** A mutual insurer covering a shipowner's liabilities. Ships outside the main International Group clubs, or with no cover listed, are worth a second look.

**Bill of lading.** The shipping document that names shipper, consignee, cargo and route. Customs releases of bills of lading (in the United States, for example) are the backbone of trade-data tools.

**EEZ.** The exclusive economic zone, extending up to 200 nautical miles from a coast, in which the coastal state controls resources. EEZ boundaries matter for fishing and for where a flag state's open AIS data stops.

**Chokepoint.** A narrow passage that a large share of trade must pass through, such as Hormuz, Bab el-Mandeb, Malacca, Suez, Panama or the Turkish Straits. Transit counts for the main chokepoints are published weekly by the IMF.

**Shadow fleet.** Ships used to move sanctioned oil and goods while hiding their ownership and movements: old tonnage, opaque owners, flags that change often, uncertain insurance, and AIS gaps and spoofing. The term is informal; the lists on the sanctions page use their own criteria.

**IUU fishing.** Illegal, unreported and unregulated fishing. Regional fisheries management organisations (RFMOs) publish lists of vessels caught doing it, and the Combined IUU Vessel List merges them.

**SAR imagery.** Synthetic aperture radar from satellites such as Sentinel-1, which sees ships through cloud and at night. It is the main free way to find a ship that is not transmitting AIS.

[↑ Back to top](#maritime-and-supply-chain-osint-tools)

---

## Archive

Tools that were on this list and no longer are. We keep them here, with a date and a reason, so that people who remember a tool can see what happened to it, and so that nobody adds it back by mistake. Dead sites are named without links.

### Shut down, merged or gone

| Tool | What it was | Retired | Why |
| --- | --- | --- | --- |
| FleetMon | AIS tracking site with a free tier | January 2024 | Kpler [phased it into MarineTraffic](https://support.marinetraffic.com/en/articles/9552991-fleetmon-and-marinetraffic-merge-process-for-former-fleetmon-ais-partners-from-january-2024); the domain no longer resolves (checked 2026-10-12). |
| Spire Maritime | Satellite AIS provider (including the exactEarth constellation data) | 25 April 2025 | Sold to Kpler for about $241 million and absorbed into Kpler AIS. |
| Sentinel Hub EO Browser | Free browser for Sentinel imagery | 20 March 2026 | Planet retired the EO Browser and the Sentinel Hub dashboard; the APIs continue under the Planet Insights Platform. Use the Copernicus Browser. |
| Copernicus Open Access Hub | The original Sentinel download portal | October 2023 | Replaced by the Copernicus Data Space Ecosystem. |
| Planet NICFI basemaps | Free monthly tropical imagery | 24 January 2025 | The programme ended; access remained only for existing users for a period. |
| Global Fishing Watch API v2 | Earlier API version | 30 April 2024 | Switched off in favour of v3; the Python client tracks the current version. |
| Sourcemap Free Edition | Free supply-chain mapping tool | By 2026 | The site's certificate now points at an abandoned development host; Sourcemap sells enterprise traceability only. |
| Shodan Ship Tracker | Shodan's AIS map | By 2026 | The site stopped responding; AIS is now a paid bulk dataset at Shodan. |
| Travel With Drone | Map of drone videos | By 2026 | The domain was repurposed for a generic products page. |
| MarineTraffic Density plan | Low-cost plan with density maps | 2025 | Decommissioned; some features moved to the paid Mobile Pro plan. |
| TankerTrackers retail tiers | Individual subscriptions | By 2026 | Closed to new subscribers; corporate plans only. |
| Bing Maps for Enterprise | Developer API behind many map mashups | Free keys June 2025, paid June 2028 | Microsoft is retiring the API. The consumer Bing Maps site is unaffected. |

### Renamed or moved

| Tool | Was | Now |
| --- | --- | --- |
| Maxar Discover | discover.maxar.com | Vantor Discover, after Maxar Intelligence became Vantor in October 2025. |
| Maritime Optima | One app | Split into ShipAtlas (individuals) and ShipIntel (companies). |
| ITU ship station search | itu.int | mmsapp.itu.int |
| MarineCadastre AIS | marinecadastre.gov/ais | hub.marinecadastre.gov |
| Russia-Ukraine Monitor | maphub.net page | eyesonrussia.org, maintained by the Centre for Information Resilience. |
| PeakFinder | peakfinder.org | peakfinder.com |
| SubTel Forum cable map | /online-map/ | /submarine-cable-map/ |
| MSCHOA | Maritime Security Centre Horn of Africa (mschoa.org) | Maritime Security Centre Indian Ocean (mscio.eu), run by EU Naval Force. |
| Supply Chain Management Tools | A separate Atlas Bear repository of open-source ERP software (Apache OFBiz, OpenBoxes, OpenLMIS, Odoo, xTuple) | Folded into this list in October 2026 and retired. They are operations software, not intelligence sources. xTuple has been closed source since 2019 and was bought by CAI Software in 2022; the other four are alive and well for people who need an ERP. |

### Dropped as off-topic

Removed in the October 2026 rebuild because they are general tools with no maritime use beyond what the maps page covers, or because they add nothing. They are CrewLinker (a seafarer job board), DuckDuckGo Maps (a wrapper around Apple Maps), Satellites.pro (repackaged imagery from an unnamed operator), F4map (3D city views) and HERE WeGo (a general map).

[↑ Back to top](#maritime-and-supply-chain-osint-tools)

---

## Contributing

Know of a tool we left off, or spotted one that has died, moved or lost its free tier? Please tell us. The easiest route is the [issue form](https://github.com/atlas-bear/osint-tools/issues/new/choose), which needs no Markdown. If you prefer a pull request, edit one page in `docs/` and follow the format below. We reply to every proposal, whether or not we add the tool.

### What earns a place

A tool or data source goes on the list when it:

1. Answers a question about ships, cargo, ports, sea routes, owners or trade flows.
2. Is live and open to the public, or gated only by a stated condition that anyone can meet and that the entry names (an account, a shared receiver feed, an application open to eligible organisations).
3. States its access terms: free, free with an account, freemium with the free part clear, or paid with a published price or an honest "quote-based".
4. Adds something a listed source does not, such as history, an API, coverage, or a different way of collecting the data.
5. Has an identifiable operator with a contact page.
6. Has been public for at least six months, or is an open-source project with a licence and tagged releases.

We do not list tools whose purpose is tracking individuals, or tools that work by breaking another site's terms. We stay inside maritime OSINT and maritime supply-chain analysis. Good general OSINT lists already exist, and we point to them on the learning page rather than copying them.

Self-submissions are welcome. Say so in the pull request or the issue form. We verify every entry ourselves before it goes in, and we treat a disclosed self-submission exactly like any other proposal.

Dead tools are not deleted. They move to the [archive](#archive) with a date and a reason, so that people who remember them can see what happened.

### The entry format

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

### Generated files

`README.md`, `tools.json` and `tools.csv` are built from the pages in `docs/` by `scripts/build_readme.py`. Please do not edit them directly; the check on every pull request will fail if they differ from `docs/`. If you can run Python, run the script and commit all three files. If not, tick "Allow edits by maintainers" and we will regenerate them on your branch.

```bash
python scripts/build_readme.py          # rebuild README.md, tools.json and tools.csv
python scripts/build_readme.py --check  # what CI runs
```

The script also checks the entry format, the access words, duplicate URLs and the `Last checked` line, and it refuses em dashes, because we try to keep the writing plain.

### Reviews and releases

We sweep the whole list twice a year, in spring before the [Summer School on Illicit Trade](https://www.rug.nl/education/summer-winter-schools/illicit-trade) and again in autumn. A link checker runs on every pull request and once a month, and opens an issue when something breaks. Each sweep ends with a release and a [CHANGELOG](CHANGELOG.md) entry.

The list and the data files are MIT licensed. The "awesome list" community prefers Creative Commons licences for lists like this one; we may revisit that. Please keep to our [community guidelines](https://github.com/atlas-bear/osint-tools/blob/main/COMMUNITY_GUIDELINES.md) in issues and pull requests.

[↑ Back to top](#maritime-and-supply-chain-osint-tools)

---

## About, licence and contact

### Licence

The list, the text and the data files (`tools.json`, `tools.csv`) are released under the [MIT License](LICENSE). Every tool on the list has its own licence and terms of use, and several of the free sources are free for non-commercial use only. Read the terms before you build on a source, and before you redistribute its data.

### Disclaimer

Listing a tool is not an endorsement. We check that each tool is live, that we can name who runs it, and that its access terms are what the entry says. We do not audit the accuracy of the data a tool returns. Prices and free tiers change without notice, so treat every price here as a snapshot from the date next to it.

A few entries are hosted in jurisdictions you may not want a case machine to connect to, and several require an account that logs what you search. Where we know this, the entry says so. The [OPSEC parts of our AI guide](https://atlas-bear.github.io/osint-ai-guide/05-opsec/) cover the general practice.

### Contact and support

- Corrections, dead links and proposals: the [issue forms](https://github.com/atlas-bear/osint-tools/issues/new/choose).
- Questions and discussion: [GitHub Discussions](https://github.com/atlas-bear/osint-tools/discussions).
- Anything else: [support@atlasbear.co](mailto:support@atlasbear.co).

### Acknowledgments

Thanks to everyone who has proposed tools, reported dead links and corrected us. Thanks in particular to the maintainers of the open AIS feeds and the public registries listed here, who keep this field open at all. Thanks also to the organisers and participants of the Summer School on Illicit Trade, where much of this list is put to work each year.

### Atlas Bear ecosystem

| Repository | Purpose | Status |
| --- | --- | --- |
| [osint-tools](https://github.com/atlas-bear/osint-tools) | This list, also at [atlas-bear.github.io/osint-tools](https://atlas-bear.github.io/osint-tools/) | ![Last commit](https://img.shields.io/github/last-commit/atlas-bear/osint-tools) |
| [osint-ai-guide](https://github.com/atlas-bear/osint-ai-guide) | AI-Enhanced OSINT: a practical guide, also at [atlas-bear.github.io/osint-ai-guide](https://atlas-bear.github.io/osint-ai-guide/) | ![Last commit](https://img.shields.io/github/last-commit/atlas-bear/osint-ai-guide) |
| [recommended-reading](https://github.com/atlas-bear/recommended-reading) | Reading list for intelligence professionals | ![Last commit](https://img.shields.io/github/last-commit/atlas-bear/recommended-reading) |
| [equasis-cli](https://github.com/rhinonix/equasis-cli) | Equasis from the command line, in batches | ![Last commit](https://img.shields.io/github/last-commit/rhinonix/equasis-cli) |
| [cue-kit](https://github.com/atlas-bear/cue-kit) | Turn video into frames and transcripts for analysis | ![Last commit](https://img.shields.io/github/last-commit/atlas-bear/cue-kit) |
| [mara-roadmap](https://github.com/atlas-bear/mara-roadmap) | Public roadmap and feedback for [MARA](https://maraiq.com), our maritime security intelligence platform | ![Last commit](https://img.shields.io/github/last-commit/atlas-bear/mara-roadmap) |

**Learn more:** [Atlas Bear Academy](https://www.atlasbear.academy), [atlasbear.co](https://atlasbear.co) and [Waterline](https://maraiq.substack.com/), our newsletter. **Contact:** [support@atlasbear.co](mailto:support@atlasbear.co).

[↑ Back to top](#maritime-and-supply-chain-osint-tools)

---
