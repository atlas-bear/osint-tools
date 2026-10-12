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
- **[SunCalc](https://www.suncalc.org/)** · Free · Torsten Hoffmann · Sun position and shadow length for any place and time, for dating or placing a photograph of a ship or a port.
- **[Shodan](https://www.shodan.io/)** · Freemium · Shodan · Search engine for internet-exposed devices, including ships' satellite terminals and port systems. Its old AIS ship tracker is gone and AIS data is now sold only as a bulk dataset.
- **[Hunchly](https://hunch.ly/)** · Paid · Hunchly · Browser extension that captures and hashes every page you visit during an investigation, which is the evidence trail you want when a vessel page changes after you cite it.

*Last checked 2026-10-12.*
