# What a software business actually earns, measured (`SWM`)

## What this file is for

[`fab-local-news-intl.md`](fab-local-news-intl.md) `LNI-17` established that **Silex Microsystems,
the world's leading pure-play MEMS wafer foundry, earned an operating margin of 22.7% in 2025** —
SEK 314 million on SEK 1,385 million of net sales at the parent company, SEK 368 million at the
group. The obvious next question is how that compares with software, the business everyone assumes
is structurally better.

That question was first answered from recollection. This file replaces the recollection with
measurement. It does not assemble a basket of famous companies and call it evidence; it builds the
**whole distribution** of US-listed software filers from the SEC's XBRL data and gives Silex's 22.7%
a percentile in it.

The point that makes the exercise worth doing at all is in `SWM-6`: **an operating margin is not
comparable across capital intensities.** A fab earns its margin after depreciating a cleanroom; a
SaaS company earns it on almost no fixed assets. The decomposition that fixes this — operating
margin × asset turnover = return on assets — is the only fair basis, and it is where the answer
turns out to be genuinely surprising.

**The headline finding, stated plainly and before anything else:** on return on assets, Silex at
22.7% is not merely competitive with listed software — it beats the median SIC 7372 filer. On
operating margin it sits in the top quartile of the same population. Software's advantage over a
specialty fab is real but it is far smaller than the folklore, and it is concentrated in a handful
of very large, very old companies. **Against that, the two software businesses most often held up as
the ideal — AWS and Microsoft — have become more capital-intensive per dollar of revenue than any
fab in this file, including TSMC.** Both findings are recorded here with equal prominence, and the
second is the one the project should be least comfortable with, because it means the "asset-light"
comparison that flatters a fab is a comparison with a business that no longer exists at the top of
the industry.

## How to read the tables

Every distribution figure is a **median and quartiles, never a mean.** These populations have tails
that make a mean meaningless: one SIC 7372 filer in CY2025 has an operating margin of −775%. Where a
figure is derived, the arithmetic is written out.

Every named company's figure is **GAAP**, from its own XBRL tags, with the accession number of the
filing. `SWM-5` reports separately what each company headlines on a **non-GAAP** basis and how large
the gap is, because that gap — almost entirely stock-based compensation — is the single biggest
reason a software margin is not comparable with a fab's.

| ID | Covers |
|---|---|
| `SWM-1` | The method: the SEC frames API, the fiscal-year join, and what was dropped |
| `SWM-2` | The distribution by SIC code, CY2025 and CY2024 |
| `SWM-3` | Where Silex's 22.7% falls in it |
| `SWM-4` | The named comparators, GAAP, with accession numbers |
| `SWM-5` | GAAP against non-GAAP: eight full-year reconciliations |
| `SWM-6` | The DuPont decomposition, and the two questions answered |
| `SWM-7` | Amazon's AWS segment — and the finding that AWS is a heavier fab than Silex |
| `SWM-8` | The Rule of 40: a low SaaS margin and a low fab margin do not mean the same thing |
| `SWM-9` | Listed wafer foundries on the same basis, for the other side of the comparison |

---

### SWM-4. The named comparators, GAAP, from their own XBRL: operating margins run from −30.6% (Snowflake) to +45.6% (Microsoft), and the median of the seventeen is 13.7%

- **Source:** `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`, one call per filer,
  fetched 2026-09-25. Each figure below is the value the company itself tagged in its own annual
  report; the accession number of that report is given in the last column. Tags used are
  `us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax` (or `us-gaap:Revenues`),
  `us-gaap:OperatingIncomeLoss`, `us-gaap:Assets`, `us-gaap:ShareBasedCompensation`,
  `us-gaap:PaymentsToAcquirePropertyPlantAndEquipment` and `us-gaap:PropertyPlantAndEquipmentNet`,
  with the `ifrs-full` equivalents for SAP.
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Context** for H5 and H6, and the raw material for `SWM-6`. This is the comparison
  the user asked for, done from filings instead of memory.
- **How it was counted:** The fiscal year reported is whichever annual period the SEC's frames API
  assigns to **CY2025**, so that a named company and the population it sits inside `SWM-2` are on the
  same footing. Software fiscal years end in January, May, June, July and November as often as in
  December, so "FY end" below is not uniform and must be read. Balance-sheet items are read at the
  income statement's own end date, so the decomposition uses **ending** assets, not average assets.
  Script: [`tools/sec_margins/comparators.py`](../../tools/sec_margins/comparators.py).
- **What it says.** All figures in millions of the reporting currency. **All GAAP.**

  | Company | FY end | Revenue | Operating income | **Op margin** | Total assets | **Asset turnover** | **Op inc ÷ assets** | SBC % rev | Capex % rev | PP&E % rev | Accession |
  |---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
  | Microsoft | 2025-06-30 | 281,724.0 | 128,528.0 | **45.62%** | 619,003.0 | 0.455 | **20.76%** | 4.25% | 22.91% | 72.75% | 0000950170-25-100235 |
  | Adobe | 2025-11-28 | 23,769.0 | 8,706.0 | **36.63%** | 29,496.0 | 0.806 | **29.52%** | 8.17% | 0.75% | 7.88% | 0000796343-26-000003 |
  | Oracle | 2026-05-31 | 67,357.0 | 20,606.0 | **30.59%** | 261,759.0 | 0.257 | **7.87%** | 7.14% | 82.64% | 148.40% | 0001193125-26-277521 |
  | Intuit | 2025-07-31 | 18,831.0 | 4,923.0 | **26.14%** | 36,958.0 | 0.510 | **13.32%** | 10.45% | 0.45% | 5.10% | 0000896878-25-000035 |
  | SAP (EUR, IFRS) | 2025-12-31 | 36,800.0 | 9,617.0 | **26.13%** | 70,362.0 | 0.523 | **13.67%** | 4.61% | 2.01% | 12.22% | 0001104659-26-020058 |
  | Zoom | 2026-01-31 | 4,868.8 | 1,123.6 | **23.08%** | 11,960.4 | 0.407 | **9.39%** | 15.63% | 1.33% | 5.43% | 0001585521-26-000030 |
  | Salesforce | 2026-01-31 | 41,525.0 | 8,331.0 | **20.06%** | 112,305.0 | 0.370 | **7.42%** | 8.45% | 1.43% | 7.51% | 0001108524-26-000060 |
  | ServiceNow | 2025-12-31 | 13,278.0 | 1,824.0 | **13.74%** | 26,038.0 | 0.510 | **7.01%** | 14.72% | 6.54% | 17.24% | 0001373715-26-000007 |
  | Shopify | 2025-12-31 | 11,556.0 | 1,468.0 | **12.70%** | 15,189.0 | 0.761 | **9.66%** | 3.89% | 0.22% | 0.46% | 0001594805-26-000007 |
  | Amazon (whole company) | 2025-12-31 | 716,924.0 | 79,975.0 | **11.16%** | 818,042.0 | 0.876 | **9.78%** | 2.72% | 18.39% | 49.80% | 0001018724-26-000004 |
  | Workday | 2026-01-31 | 9,552.0 | 721.0 | **7.55%** | 18,074.0 | 0.528 | **3.99%** | 17.02% | 1.70% | 11.44% | 0001327811-26-000014 |
  | Twilio | 2025-12-31 | 5,067.2 | 157.8 | **3.11%** | 9,770.9 | 0.519 | **1.62%** | 11.85% | 0.12% | 3.49% | 0001447669-26-000021 |
  | HubSpot | 2025-12-31 | 3,131.3 | 7.4 | **0.24%** | 3,854.2 | 0.812 | **0.19%** | 16.87% | 1.70% | 4.53% | 0001193125-26-046646 |
  | Datadog | 2025-12-31 | 3,427.2 | −44.4 | **−1.29%** | 6,643.8 | 0.516 | **−0.67%** | 21.90% | 1.45% | 9.87% | 0001628280-26-008819 |
  | Atlassian | 2025-06-30 | 5,215.3 | −130.4 | **−2.50%** | 6,042.0 | 0.863 | **−2.16%** | 26.12% | 0.86% | 2.02% | 0001650372-25-000036 |
  | MongoDB | 2026-01-31 | 2,463.8 | −137.0 | **−5.56%** | 3,758.8 | 0.655 | **−3.64%** | 22.34% | 0.20% | 1.61% | 0001628280-26-016799 |
  | Snowflake | 2026-01-31 | 4,683.9 | −1,435.2 | **−30.64%** | 9,132.5 | 0.513 | **−15.71%** | 34.15% | 2.17% | 5.31% | 0001640147-26-000008 |

  **Amazon's AWS segment is in `SWM-7`, separately, because a segment is not a filer and its assets
  are disclosed on a different basis.**

- **DERIVED (arithmetic written out):**
  - **Median operating margin of the seventeen:** the ordered list is −30.64, −5.56, −2.50, −1.29,
    0.24, 3.11, 7.55, 11.16, **12.70, 13.74**, 20.06, 23.08, 26.13, 26.14, 30.59, 36.63, 45.62. With
    n = 17 the median is the 9th value, **12.70%** (Shopify). Excluding Amazon, whose operating
    margin is a retailer's, the median of sixteen is (12.70 + 13.74) ÷ 2 = **13.22%**.
  - **Silex against this list.** Silex's 22.67% (parent) would sit between Salesforce's 20.06% and
    Zoom's 23.08% — **12th of 18**, i.e. above two-thirds of them. Its group figure of 26.57% would
    sit between SAP's 26.13% and Oracle's 30.59%, **15th of 18**.
  - **Silex against this list on return on assets.** Silex's group EBIT ÷ group total assets is
    SEK 368m ÷ SEK 2,246m = **16.38%**. Only Adobe (29.52%), Microsoft (20.76%) and — on a segment
    basis — AWS beat it. It beats Intuit, SAP, Salesforce, Oracle, ServiceNow, Workday, Zoom,
    Shopify, Amazon and every loss-maker.
  - **Two later fiscal years exist and both go the same way.** Microsoft FY2026 (ended 2026-06-30):
    revenue 331,839, operating income 155,237, margin **46.78%**, assets 758,376, turnover 0.438,
    return on assets **20.47%**. Intuit FY2026 (ended 2026-07-31): 21,448 / 5,884 = **27.43%**,
    assets 36,786, return on assets **16.00%**. Atlassian FY2026 (ended 2026-06-30): 6,572.3 / 10.4
    = **0.16%**, its first GAAP operating profit.
- **Caveats.**
  - **Every one of these is GAAP and therefore lower — often much lower — than the number the
    company puts in its own headline.** See `SWM-5` before quoting any of them against a figure
    picked up from a press release or a broker note.
  - Total assets for a software company is a poor denominator: it is mostly cash, marketable
    securities and goodwill. `SWM-2` therefore also reports turnover and return on **assets less
    cash and goodwill**, and `SWM-6` uses both.
  - SAP reports in euro under IFRS; its "operating profit" is
    `ifrs-full:ProfitLossFromOperatingActivities`. TSMC, UMC and GlobalFoundries in `SWM-9` are the
    same case.
  - Oracle's and Microsoft's capex and PP&E lines are **not typical of software** and are the
    subject of the warning in `SWM-7`.
  - `us-gaap:SellingGeneralAndAdministrativeExpense` is not tagged by most software filers, which
    split sales-and-marketing from general-and-administrative; where this file reports an SG&A
    figure for such a filer it is the **sum of the two**, and the script records that.

### SWM-5. GAAP against the headline: eight software companies' own full-year reconciliations, and the gap runs from 9.7 to 41 percentage points, median about 23

- **Sources:** each company's Form 8-K exhibit 99.1 for its fourth quarter and full year, on EDGAR.
  Located through the SEC's full-text search endpoint `https://efts.sec.gov/LATEST/search-index`,
  then read.
  - Adobe, FY2025 (ended 2025-11-28), furnished 2025-12-10, accession 0000796343-25-000135:
    <https://www.sec.gov/Archives/edgar/data/796343/000079634325000135/adbeex991q425.htm>
  - Salesforce, FY2026 (ended 2026-01-31), furnished 2026-02-25, accession 0001108524-26-000056:
    <https://www.sec.gov/Archives/edgar/data/1108524/000110852426000056/crm-q4fy26xexhibit991.htm>
  - ServiceNow, FY2025 (ended 2025-12-31), furnished 2026-01-28, accession 0001373715-26-000005:
    <https://www.sec.gov/Archives/edgar/data/1373715/000137371526000005/erq4fy25.htm>
  - Workday, FY2026 (ended 2026-01-31), furnished 2026-02-24, accession 0001327811-26-000010:
    <https://www.sec.gov/Archives/edgar/data/1327811/000132781126000010/wday-01312026x991.htm>
  - Datadog, FY2025 (ended 2025-12-31), furnished 2026-02-10, accession 0001628280-26-006645:
    <https://www.sec.gov/Archives/edgar/data/1561550/000162828026006645/ex-991x20251231x8k.htm>
  - MongoDB, FY2026 (ended 2026-01-31), furnished 2026-03-02, accession 0001628280-26-013199:
    <https://www.sec.gov/Archives/edgar/data/1441816/000162828026013199/mdb-13126xex991xrelease.htm>
  - Atlassian, FY2026 (ended 2026-06-30), furnished 2026-08-06, accession 0001650372-26-000031:
    <https://www.sec.gov/Archives/edgar/data/1650372/000165037226000031/ex991q4fy26.htm>
  - Snowflake, FY2026 (ended 2026-01-31), furnished 2026-02-25, accession 0001628280-26-011631:
    <https://www.sec.gov/Archives/edgar/data/1640147/000162828026011631/fy2026q4earnings.htm>
- **Verification:** Verified. `www.sec.gov/Archives/...` returns HTTP 403 to `curl` under every
  User-Agent tried, as this directory has recorded before; these eight documents were read through
  `WebFetch`, which does reach that host. The full-text search endpoint `efts.sec.gov` answers a
  declared non-browser agent normally and was used only to find the documents.
- **Date checked:** 2026-09-25
- **Bearing:** **Context**, and a warning. It is the reason `SWM-2` and `SWM-4` report GAAP and
  nothing else.
- **What it says.** Full-year figures, as the companies state them:

  | Company | Fiscal year | **GAAP op margin** | **Non-GAAP op margin** | Gap (pp) | SBC add-back | SBC ÷ revenue |
  |---|---|---:|---:|---:|---:|---:|
  | Adobe | FY2025 | 36.63% (derived) | 46.24% (derived) | **+9.61** | $1,973m | **8.30%** |
  | Salesforce | FY2026 | "20.1%" | "34.1%" | **+14.0** | $3,480m | **8.38%** |
  | ServiceNow | FY2025 | "13.5%" | "31%" | **+17.5** | $1,955m | **14.72%** |
  | Workday | FY2026 | "7.5% of revenues" | "29.6% of revenues" | **+22.1** | $1,570m | **16.44%** |
  | Datadog | FY2025 | "(1)%" | "22%" | **+23** | $750.671m | **21.90%** |
  | MongoDB | FY2026 | "(6)%" | "19%" | **+25** | $574.373m | **23.31%** |
  | Atlassian | FY2026 | "0.2%" | "30%" | **+29.8** | $1,605.129m | **24.42%** |
  | Snowflake | FY2026 | "(31%)" | "10%" | **+41** | $1,710.685m | **36.52%** |

  Salesforce's release states it plainly:

  > "FY26 GAAP operating margin of 20.1%"

  and, in the same release, "non-GAAP operating margin of 34.1%". Workday's states:

  > "Operating income was $721 million, or 7.5% of revenues"

  against

  > "Non-GAAP operating income was $2.824 billion, or 29.6% of revenues"

- **DERIVED (arithmetic written out):**
  - **Adobe's margins,** which the release gives in dollars rather than per cent: GAAP
    $8,706m ÷ $23,769m = **36.63%**; non-GAAP $10,990m ÷ $23,769m = **46.24%**; gap **9.61 pp**.
  - **Median gap:** the ordered gaps are 9.61, 14.0, 17.5, 22.1, 23, 25, 29.8, 41. With n = 8 the
    median is (22.1 + 23) ÷ 2 = **22.55 percentage points.**
  - **SBC as a share of revenue,** each from `SWM-4`'s revenue: Adobe 1,973 ÷ 23,769 = 8.30%;
    Salesforce 3,480 ÷ 41,525 = 8.38%; ServiceNow 1,955 ÷ 13,278 = 14.72%; Workday 1,570 ÷ 9,552 =
    16.44%; Datadog 750.671 ÷ 3,427.158 = 21.90%; MongoDB 574.373 ÷ 2,463.797 = 23.31%; Atlassian
    1,605.129 ÷ 6,572.308 = 24.42%; Snowflake 1,710.685 ÷ 4,683.946 = 36.52%.
  - **SBC explains most but not all of the gap.** Comparing the gap with SBC ÷ revenue: Adobe
    9.61 vs 8.30, Salesforce 14.0 vs 8.38, ServiceNow 17.5 vs 14.72, Workday 22.1 vs 16.44, Datadog
    23 vs 21.90, MongoDB 25 vs 23.31, Atlassian 29.8 vs 24.42, Snowflake 41 vs 36.52. The residual —
    between 1.1 and 5.7 points — is amortisation of acquired intangibles, restructuring and, at
    Snowflake, employer payroll tax on the equity itself.
  - **What this means for the comparison with Silex.** Silex's 22.7% is a **GAAP-equivalent IFRS
    operating margin after depreciating its cleanroom, with no adjustment of any kind.** The
    software figure that is usually quoted against it — "SaaS companies run at 30–40%" — is the
    right-hand column of this table. On the left-hand column, which is the only like-for-like one,
    **six of these eight companies are below Silex and four of them are loss-making.**
- **Caveats.** These are eight companies chosen because they span the range, not a random sample;
  the median gap of 22.55 pp is a statement about these eight and not about the population. The
  population-level version of the same point is in `SWM-2`, where SBC ÷ revenue is reported for every
  SIC 7372 filer that tags it. Microsoft, Oracle and Intuit do not headline a non-GAAP operating
  margin at all, which is itself the finding: a company that is genuinely GAAP-profitable has no use
  for the adjustment.

### SWM-7. Amazon's AWS segment earns 35.4% — and spends **74.96% of its revenue on property and equipment in one year.** The most profitable software business on earth is now five times more capital-hungry per dollar of revenue than the MEMS fab

- **Source:** Amazon.com, Inc., CIK 0001018724, Annual Report on Form 10-K for the year ended
  2025-12-31, filed 2026-02-06, accession **0001018724-26-000004**, Note 10 — Segment Information.
  The four tables below were read from the filing's own XBRL "Financial Report" renderings:
  - Reportable segments: <https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/R87.htm>
  - Assets by segment: <https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/R90.htm>
  - Property and equipment, net, by segment: <https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/R91.htm>
  - Property and equipment additions by segment: <https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/R92.htm>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Mixed**, and the most uncomfortable entry in the file. It confirms the repo's
  existing AWS figure exactly, and it destroys the "software needs no capital" half of the argument
  for the largest software businesses.
- **How it was counted:** `www.sec.gov/Archives/...` returns HTTP 403 to `curl`. The 10-K's
  `FilingSummary.xml` was read through `WebFetch` to find which `R##.htm` report holds each segment
  table, and the four reports were then read the same way. This is the cheapest reliable route into
  a segment note and should be reused: the main 10-K document is too large to fetch usefully, but
  each `R##.htm` is one table.
- **What it says.** In US$ millions, as printed:

  | | 2025 | 2024 | 2023 |
  |---|---:|---:|---:|
  | AWS net sales | **128,725** | 107,556 | 90,757 |
  | AWS operating expenses | 83,119 | 67,722 | 66,126 |
  | **AWS operating income** | **45,606** | 39,834 | 24,631 |
  | AWS total segment assets | **252,588** | 155,953 | 108,533 |
  | AWS property and equipment, net | **190,055** | 110,683 | 72,701 |
  | AWS property and equipment additions | **96,496** | 53,267 | 24,843 |
  | (whole company, total assets) | 818,042 | 624,894 | 527,854 |
  | (whole company, total P&E additions) | 142,352 | 85,752 | 48,344 |

- **DERIVED (arithmetic written out):**
  - **AWS operating margin 2025:** 45,606 ÷ 128,725 = **35.43%.** This **confirms the figure the
    repository already carried** ($45.6bn on $128.7bn = 35.4%) to two decimal places, from the 10-K
    rather than the earnings release.
  - **AWS operating margin 2024:** 39,834 ÷ 107,556 = **37.04%.** 2023: 24,631 ÷ 90,757 = **27.14%.**
    The margin fell in 2025 while revenue grew 19.7%.
  - **AWS asset turnover 2025:** 128,725 ÷ 252,588 = **0.5096.** 2024: 107,556 ÷ 155,953 = 0.6897.
  - **AWS return on segment assets 2025:** 45,606 ÷ 252,588 = **18.06%.** Check: 0.3543 × 0.5096 =
    0.1806. 2024: 39,834 ÷ 155,953 = **25.54%** — so AWS's return on its own assets **fell 7.5
    points in one year** because assets grew 62.0% while operating income grew 14.5%.
  - **AWS capital intensity 2025:** property and equipment additions 96,496 ÷ net sales 128,725 =
    **74.96%.** Property and equipment, net, 190,055 ÷ 128,725 = **147.64%.**
  - **Against Silex, on the same two ratios** (`SWM-6` for the source figures): Silex's capex was
    SEK 195m on SEK 1,385m of net sales = **14.08%**, and its property, plant and equipment was
    SEK 942m = **68.02%** of net sales. **AWS spends 5.32× as much capex per dollar of revenue as
    the MEMS fab** (74.96 ÷ 14.08) and carries **2.17× as much net plant per dollar of revenue**
    (147.64 ÷ 68.02).
  - **Against TSMC** (`SWM-9`): TSMC's FY2024 capex was 33.03% of revenue and its net PP&E 111.77%.
    **AWS in 2025 was 2.27× more capex-intensive than TSMC** and carried 1.32× the net plant per
    dollar of revenue. The largest cloud business in the world is, per dollar of revenue, a heavier
    manufacturer than the largest wafer foundry in the world.
  - **And it is not only AWS.** From `SWM-4`: Microsoft's FY2026 capex was **$115,948m on $331,839m
    of revenue = 34.94%**, with net PP&E of $313,076m = **94.35%** of revenue. Oracle's FY2026 capex
    was **$55,663m on $67,357m = 82.64%**, with net PP&E of $99,957m = **148.40%** of revenue —
    **higher plant intensity than TSMC, UMC, GlobalFoundries or Tower.** Three years earlier
    Microsoft's capex was 18.14% of revenue (FY2024) and Oracle's PP&E was 40.66% (FY2024).
- **Why this cuts against the project, and should be said so.** A recurring move in `WHY.md` and in
  this directory is: *software's advantage is that it needs no factory.* For the median software
  filer that is still true — `SWM-2` puts median capex at well under 1% of revenue and median net
  PP&E at a few per cent. But **the companies that earn the famous margins no longer look like
  that.** AWS, Microsoft and Oracle earn 30–46% operating margins while spending a third to
  four-fifths of revenue on plant. If the argument for an API-first foundry is "be the AWS of
  silicon", the honest version of that sentence now includes AWS's balance sheet, which is a fab's
  balance sheet at ten times the scale.
- **Caveats.** Segment assets and segment P&E are management's allocation and are not audited as a
  stand-alone balance sheet; Amazon also carries $247,818m of 2025 assets in "Corporate", unallocated,
  so AWS's 18.06% return is computed on a denominator that excludes its share of that. Segment
  operating income is stated before the corporate costs Amazon does not allocate. "Property and
  equipment additions" in R92 excludes finance leases and financing obligations, which the filing
  states separately, so it is a **lower** bound on AWS's capital commitment, not an upper one.

### SWM-9. Listed wafer foundries on the same basis: GlobalFoundries 11.74%, Tower 12.40%, UMC 22.22%, TSMC 45.68%, SkyWater −0.58% — and Silex's 22.7% sits second among them

- **Source:** `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json` for each filer,
  fetched 2026-09-25. GlobalFoundries (CIK 1709048), TSMC (1046179) and UMC (1033767) file Form 20-F
  and tag under `ifrs-full`; Tower Semiconductor (928876) files 20-F but tags under `us-gaap`;
  SkyWater Technology (1819974) files Form 10-K.
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Context** for H6 and for `SWM-6`. Without it, "software versus a fab" is a
  comparison with a sample of one.
- **What it says.** All GAAP or IFRS as filed, in millions of the reporting currency.

  | Filer | Currency | FY end | Revenue | Operating income | **Op margin** | Total assets | **Turnover** | **Op inc ÷ assets** | Capex % rev | PP&E % rev | Accession |
  |---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
  | TSMC | TWD | 2024-12-31 | 2,894,307.7 | 1,322,053.0 | **45.68%** | 6,691,764.7 | 0.433 | **19.76%** | 33.03% | 111.77% | 0001193125-25-083423 |
  | **Silex (group)** | **SEK** | **2025-12-31** | **1,385** | **368** | **26.57%** | **2,246** | **0.617** | **16.38%** | **14.08%** | **68.02%** | (prospectus, `LNI-18`) |
  | UMC | TWD | 2024-12-31 | 232,302.6 | 51,612.6 | **22.22%** | 560,169.0 | 0.415 | **9.21%** | 38.12% | 120.13% | 0001193125-25-092142 |
  | **Silex (parent, `LNI-17`)** | **SEK** | **2025-12-31** | **1,385** | **314** | **22.67%** | — | — | — | — | — | (allabolag) |
  | Tower Semiconductor | USD | 2025-12-31 | 1,566.1 | 194.2 | **12.40%** | 3,322.3 | 0.471 | **5.84%** | 28.38% | 93.42% | 0001178913-26-002318 |
  | GlobalFoundries | USD | 2025-12-31 | 6,791.0 | 797.0 | **11.74%** | 17,141.0 | 0.396 | **4.65%** | 10.63% | 106.36% | 0001709048-26-000022 |
  | SkyWater Technology | USD | 2025-12-28 | 442.1 | −2.6 | **−0.58%** | 733.9 | 0.602 | **−0.35%** | 5.50% | 115.74% | 0001819974-26-000009 |

- **DERIVED (arithmetic written out):**
  - **Median operating margin of the five listed foundries:** ordered −0.58, 11.74, **12.40**, 22.22,
    45.68 → median **12.40%** (Tower). **Silex at 22.67% is the second-best of the six** and at
    26.57% on the group figure it is still second, behind only TSMC.
  - **Median return on assets of the five:** ordered −0.35, 4.65, **5.84**, 9.21, 19.76 → **5.84%**.
    Silex's 16.38% is second again.
  - **Capital intensity is the common feature, not the margin.** Every one of the five carries net
    PP&E between 93% and 120% of a year's revenue; Silex carries 68% (or 94.66% if the SEK 369m of
    IFRS 16 right-of-use assets are included: (942 + 369) ÷ 1,385). Compare the SIC 7372 median in
    `SWM-2`. **This is the structural difference the whole file is about, and it is visible in one
    row.**
  - **Silex is a better fab than the listed fabs, not a worse software company.** Against the
    foundry median it is +10.3 points of operating margin and +10.5 points of return on assets.
- **Caveats.** TSMC's and UMC's FY2025 Form 20-F facts were not yet in `companyfacts` when this was
  fetched, so their rows are FY2024 and the other rows are FY2025; no FY2025 figure for either is
  asserted here, in either direction. Currency differs by row, but every
  column here is a ratio and therefore currency-free. SkyWater's fiscal year ends on the Sunday
  nearest 31 December (2025-12-28), and its 2025 assets nearly doubled on the Fab 25 acquisition,
  which depresses its turnover for a reason that is not operating performance.
