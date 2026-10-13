---
title: "Who owns the AIS data"
description: "How most commercial AIS data came to belong to two companies, and what that means before you build on a free tier."
---

Most of the commercial vessel-tracking data that analysts use now belongs to two companies, and it is worth knowing how that happened before you build a workflow on a free tier.

**Kpler**, a commodities data firm, [bought MarineTraffic and FleetMon](https://www.kpler.com/blog/kpler-acquires-marinetraffic-and-fleetmon-for-maritime-sector-expansion) in March 2023, then [phased FleetMon out](https://support.marinetraffic.com/en/articles/9552991-fleetmon-and-marinetraffic-merge-process-for-former-fleetmon-ais-partners-from-january-2024) from January 2024 and asked its volunteer receiver hosts to redirect their feeds to MarineTraffic. In November 2024 it agreed to buy Spire's maritime business, including the exactEarth satellite constellation data, for [about $241 million](https://www.satellitetoday.com/finance/2024/11/13/spire-to-sell-maritime-business-to-kpler-in-241m-deal/). The deal [closed on 25 April 2025](https://kpler.com/blog/kpler-completes-acquisition-of-spire-maritime-strengthening-maritime-intelligence-capabilities) after Spire sued over the delay. The UK competition regulator [decided in July 2025](https://www.gov.uk/cma-cases/kpler-slash-spire-global-merger-inquiry) that it did not qualify for review. In September 2025 Kpler launched [Kpler AIS](https://support.marinetraffic.com/en/articles/12495052-19-september-2025-announcing-the-launch-of-kpler-ais), one feed from more than 13,000 receivers that replaces MarineTraffic AIS, and in June 2026 it took a [$1 billion investment](https://maritime-executive.com/article/kpler-secures-1-billion-investment-from-sixth-street) at a valuation near $4 billion.

**S&P Global** merged with IHS Markit on [28 February 2022](https://press.spglobal.com/2022-02-28-S-P-Global-Completes-Merger-with-IHS-Markit,-Creating-a-Global-Leader-to-Power-the-Markets-of-the-Future). That brought it the ship database that began life as Lloyd's Register-Fairplay (sold today as Sea-web and the Maritime Portal) and the Panjiva trade data. S&P Global also [assigns IMO ship numbers](https://www.imo.org/en/OurWork/IIIS/Pages/IMO-Identification-Number-Schemes.aspx) on the IMO's behalf, free of charge, and on 10 November 2025 it [completed the purchase of ORBCOMM's satellite AIS business](https://press.spglobal.com/2025-11-10-S-P-Global-Announces-Successful-Completion-of-its-Acquisition-of-ORBCOMMs-Automatic-Identification-System-Business). Of the other names you will meet, Lloyd's List Intelligence was [sold by Informa to Montagu Private Equity](https://montagu.com/montagu-acquires-maritime-intelligence-from-informa-plc/) in 2022, and Windward was [taken private by FTV Capital](https://www.uktech.news/ai/maritime-ai-firm-windward-bought-by-ftv-capital-in-216m-deal-20241224) in early 2025.

## Why it matters

Terrestrial AIS is collected by thousands of receivers, many of them run by volunteers who are [rewarded with subscriptions](https://support.marinetraffic.com/en/articles/9552976-what-benefits-do-i-get-as-an-ais-partner) rather than paid. The aggregated data is then sold back, and the free tiers have narrowed. A free MarineTraffic account shows about a day of track and no port calls or ownership, and the [Density plan was retired in 2025](https://support.marinetraffic.com/en/articles/13456094-mobile-pro-plan-faq). History, which is what an investigation needs, sits behind the paywall. Even the main NGO dataset depends on these companies: Global Fishing Watch [buys its AIS](https://globalfishingwatch.org/faqs/data-source-updates) from Spire (since 2023) and MarineTraffic (since 2024), and both now belong to Kpler.

None of this is a complaint about the companies. Collecting, cleaning and serving AIS at global scale costs money. It is a reason to know the open sources, to keep copies of what you download, and to say in your reports which source and date range you used.

## What is still open

- **United States**: NOAA and BOEM publish every year of US-waters AIS since 2009 through MarineCadastre, free and without an account.
- **Norway**: the Coastal Administration publishes a live feed under an open licence and historical files back to 2005 that include satellite AIS, with full history on application.
- **Denmark, Finland and Australia**: daily, live and monthly files respectively, for their own waters.
- **Global Fishing Watch**: tracks and events worldwide from 2012, free for non-commercial use, about four days behind live.
- **Live feeds**: aisstream.io is free and global but keeps no history; AISHub gives you the pool if you contribute a receiver.
- **Your own receiver**: a software-defined radio dongle and AIS-catcher give you ground truth for the stretch of coast you can see, and feed the pools above.

A [2025 study](https://arxiv.org/abs/2511.23016) rebuilt Baltic Sea vessel activity from open AIS alone and landed within 20 percent of results from proprietary data. Open data is thinner than the commercial feeds, but for coastal questions it is often enough. The entries are on the [vessel tracking](01-vessel-tracking.md) page.

*Sources checked 2026-10-12.*
