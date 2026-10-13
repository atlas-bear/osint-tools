---
title: "Satellite imagery and detection"
description: "Testing what AIS tells you with free radar and optical imagery, and the detection tools that find ships that stopped transmitting."
---

Imagery is how you test what AIS tells you. Radar (SAR) sees ships through cloud and at night and is the main free way to find a vessel that has stopped transmitting; optical imagery confirms what the radar return is. The European Sentinel satellites make both free, with a revisit of a few days. Sentinel Hub's EO Browser, which many guides still link, was retired on 20 March 2026; the Copernicus Browser is its free replacement. Commercial high-resolution imagery is sold per scene, but two operators publish open samples and Vantor releases free imagery after major disasters.

## Free imagery browsers and archives

- **[Copernicus Browser](https://browser.dataspace.copernicus.eu/)** · Free account · European Space Agency for the European Commission · Sentinel-1 radar and Sentinel-2 optical imagery with search, time-lapse and download. Sentinel-1 is back to a six-day revisit since the 1C and 1D satellites came into service in 2025 and 2026.
- **[Copernicus Data Space](https://dataspace.copernicus.eu/)** · Free account · European Space Agency · The APIs behind the browser (STAC, OData and processing) for pulling Sentinel data into your own tools.
- **[NASA Worldview](https://worldview.earthdata.nasa.gov/)** · Free · NASA · Same-day, low-resolution global imagery from MODIS and VIIRS, enough to see weather, smoke, ice and large slicks.
- **[NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/)** · Free · NASA · Active fire and thermal anomaly detections, including flaring at offshore platforms and fires at sea.
- **[OpenAerialMap](https://map.openaerialmap.org/)** · Free (open licences) · Humanitarian OpenStreetMap Team · Openly licensed aerial and drone imagery uploaded by mappers and responders, much of it very high resolution and much of it after disasters. Patchy, but where it exists it beats satellite imagery.
- **[EOS LandViewer](https://eos.com/landviewer/)** · Freemium · EOS Data Analytics · Browser for Sentinel, Landsat and some commercial imagery with analysis tools; the free tier allows a small number of scenes a month.

## Dark vessel and anomaly detection

- **[Bellingcat Ship Detection Tool](https://ollielballinger.users.earthengine.app/view/ship-detection-tool)** · Free · Ollie Ballinger for Bellingcat · Counts and plots ships in Sentinel-1 radar imagery for any area and date range, including ships with AIS off. Runs in Google Earth Engine; Bellingcat's 2023 guide explains the method.
- **[Global Fishing Watch data portal](https://globalfishingwatch.org/data-download/)** · Free account (non-commercial) · Global Fishing Watch · Downloads of radar vessel detections matched to AIS (from 2017), fishing effort and other derived datasets. The radar layer is the simplest global view of unmatched, likely dark, vessels.
- **[SkyTruth Cerulean](https://cerulean.skytruth.org/)** · Free · SkyTruth · Oil slicks detected in Sentinel-1 radar, with the likely source vessel or platform suggested from AIS, through a map and an API. Vessel attribution runs a few days behind.
- **[Skylight](https://www.skylight.global/)** · On application · Allen Institute for AI (Ai2) · Maritime monitoring platform that fuses AIS, radar and optical detections into alerts, free to governments, regional bodies and NGOs working on illegal fishing and maritime security.
- **[VIIRS Boat Detection](https://eogdata.mines.edu/products/vbd/)** · Free · Earth Observation Group, Colorado School of Mines · Nightly detections of lit fishing boats from the VIIRS day-night band, useful for squid and other light-attracting fleets.

## Open commercial imagery

- **[Vantor Open Data Program](https://vantor.com/company/open-data-program/)** · Free (CC BY-NC 4.0) · Vantor (formerly Maxar Intelligence) · High-resolution before-and-after imagery released for major disasters as a catalogue on AWS. Event-driven rather than on demand, and non-commercial use only.
- **[Vantor Discover](https://xpress.maxar.com/)** · Freemium · Vantor · Browse previews of the commercial high-resolution archive for free; buying a scene is quote-based. The portal kept its Maxar address after the 2025 rename.
- **[Umbra Open Data](https://umbra.space/open-data/)** · Free (CC BY 4.0) · Umbra · Very high-resolution radar imagery of about twenty fixed sites, some of them ports, with no sign-up. A good way to learn what commercial SAR can show.
- **[Capella Open Data](https://registry.opendata.aws/capella_opendata/)** · Free (CC BY 4.0) · Capella Space · Sample high-resolution radar scenes on AWS. Capella has been owned by IonQ since July 2025.
- **[SkyFi](https://skyfi.com/)** · Paid · SkyFi · Marketplace for buying archive imagery or new tasking from several satellite operators by the scene, for people who need one picture rather than a contract.

*Last checked 2026-10-12.*
