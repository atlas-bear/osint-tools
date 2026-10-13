---
title: "Vessel tracking (AIS)"
description: "Where a ship is now and where it has been: live AIS maps, the free government and NGO archives, and feeds to build on."
---

Where is a ship now, and where has it been? The commercial maps answer the first question for free and charge for the second. The free route to history is the government and NGO data below. It covers more than most people expect: the whole US coast since 2009, Norway since 2005 with satellite AIS included, and Global Fishing Watch's global record since 2012. For a live feed to build on, aisstream.io costs nothing, and a receiver of your own costs about the price of a textbook.

One OPSEC point. Searching a named vessel on a commercial site while logged in ties your interest in that ship to your account. The open feeds and your own receiver do not.

## Live maps with a free tier

- **[MarineTraffic](https://www.marinetraffic.com/)** · Freemium · Kpler · The largest crowd-sourced AIS map, with vessel pages, port calls and photos. Free accounts see about a day of track and no port calls or ownership; Kpler has owned it since March 2023 and the free tier has narrowed since.
- **[VesselFinder](https://www.vesselfinder.com/)** · Freemium (Basic from €9/yr, 2026-10) · VesselFinder Ltd, Bulgaria · Live map and vessel particulars with the cheapest paid route to longer tracks (3, 7 or 90 days by tier). Its terms forbid scraping and building datasets.
- **[MyShipTracking](https://www.myshiptracking.com/)** · Freemium · MyShipTracking · Terrestrial AIS map with a credit-based API and a free trial key. Coverage is near-shore only.
- **[ShipAtlas](https://www.maritimeoptima.com/shipatlas)** · Freemium (from €10/month, 2026-10) · Maritime Optima, Norway · Satellite AIS positions, recent port calls and a sea-route calculator. The free tier is capped at ten satellite position views.
- **[ShipXplorer](https://www.shipxplorer.com/)** · Freemium · AirNav Systems · AIS map fed by hobbyist receivers, from the company behind ShipSpotting. Hosting a receiver earns a premium account.
- **[MarineRadar](https://www.marineradar.com/)** · Freemium · Lascade, Dubai · Live terrestrial and satellite AIS for more than 100,000 vessels with route playback, on the web and in mobile apps. Subscription prices are not published.
- **[Tradlinx vessel tracking](https://www.tradlinx.com/vessel-tracking/)** · Free · Tradlinx Inc., Seoul · Latest position, destination and identifiers for a ship by name, MMSI, IMO or call sign, with no account. Near-shore receivers only; satellite coverage is in the paid Ocean Visibility product.
- **[Shipinfo.net](https://shipinfo.net/)** · Freemium · STELS A LLC, Russia · AIS map with waterway and port-congestion analytics and Northern Sea Route ice layers. Operated from Russia, so think about what you query from a case machine.
- **[Global Fishing Watch map](https://globalfishingwatch.org/map)** · Free account · Global Fishing Watch · Tracks from 2012, port visits, encounters, loitering, AIS gaps and radar detections for the whole world. Built around fishing and carrier vessels, and about three days behind live.

## Open government AIS data

- **[MarineCadastre vessel traffic](https://hub.marinecadastre.gov/pages/vesseltraffic)** · Free · NOAA and BOEM · Bulk US-waters AIS from 2009 to the previous year, filtered to one position a minute, with GeoParquet files from 2024 onward. The deepest free raw AIS archive anywhere, but US waters only.
- **[Kystverket AIS](https://www.kystverket.no/en/sea-transport-and-ports/ais/access-to-ais-data/)** · Free (NLOD open licence) · Norwegian Coastal Administration · A live API for the Norwegian economic zone with no registration, plus historical files back to 2005 that include Norway's own satellite AIS. Small fishing and leisure craft are excluded, and full history needs an application.
- **[BarentsWatch AIS API](https://developer.barentswatch.no/)** · Free account · BarentsWatch, Norway · Developer API over the Norwegian AIS feed with about two weeks of history. Norway only.
- **[Danish AIS data](https://www.dma.dk/safety-at-sea/navigational-information/ais-data)** · Free · Danish Maritime Authority · Daily files of AIS for Danish waters, the approach to the Baltic. The shore network moved to the Danish Emergency Management Agency; historical files are supplied on application.
- **[Digitraffic Marine](https://www.digitraffic.fi/en/marine-traffic/)** · Free (CC BY 4.0) · Fintraffic, Finland · Live AIS over REST and MQTT plus Portnet port-call schedules, with commercial use allowed. Finland and the northern Baltic only; requests need a `Digitraffic-User` header.
- **[AMSA vessel traffic data](https://www.operations.amsa.gov.au/Spatial/DataServices/DigitalData)** · Free · Australian Maritime Safety Authority · Monthly AIS shapefiles for the Australian search-and-rescue region, at roughly hourly positions. Good free history for the Indo-Pacific approaches.
- **[Global Fishing Watch APIs](https://globalfishingwatch.org/our-apis/)** · Free account (non-commercial) · Global Fishing Watch · Vessel search, events, presence grids from 2012 to about four days ago, and radar detections through a documented API with a Python client. No commercial licence is offered.

## Raw feeds and your own receiver

- **[aisstream.io](https://aisstream.io/)** · Free account · aisstream.io (community project) · A live global WebSocket feed of AIS messages, filtered by bounding box or MMSI, with GitHub sign-in. No history, three connections per account, and connections must come from a server rather than a browser.
- **[AISHub](https://www.aishub.net/)** · Share-to-get · AISHub · A pooled raw AIS feed and API that you get access to by contributing a live feed from your own receiver. Live data only.
- **[AIS-catcher](https://github.com/jvde-github/AIS-catcher)** · Free (open source, GPL-3.0) · jvde-github · Turns an RTL-SDR or similar dongle and a small computer into an AIS receiver with a web map, and feeds AISHub or the commercial networks. Range is line of sight, a few tens of nautical miles.
- **[OpenCPN](https://opencpn.org/)** · Free (open source, GPL-2.0) · OpenCPN project · A chart plotter that shows AIS from your receiver over real charts and keeps a local log. Useful for offline analysis of your own feed.

*Last checked 2026-10-12.*
