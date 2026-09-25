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

## The findings, stated before the evidence

**On the measure that actually compares two businesses with different capital intensities — return
on assets — Silex beats listed software.** Its 22.67% operating margin at an asset turnover of
0.6167 gives a 13.98% return on assets (16.38% on the group's own operating profit). That is the
**92.4th percentile** of SIC 7372 (94.8th on the group figure), and it clears the return on assets
of the entire listed prepackaged-software industry taken in aggregate (11.33%). **To match that
aggregate, a fab with Silex's balance sheet would need an operating margin of 18.38%. It has 22.67%.**

**On operating margin alone Silex is at the 89.1st percentile of SIC 7372** (91.0th on the group
figure) — better than Salesforce, ServiceNow, Shopify, Amazon, Workday, Twilio, HubSpot, Datadog,
Atlassian, MongoDB and Snowflake, and worse than Microsoft, Adobe, Oracle, Intuit, SAP and Zoom.
Eleven of the seventeen named comparators in `SWM-4` are below it; six are above.

**Software's famous margins are three things stacked on top of each other, and only one of them is
real.** (1) The quoted number is usually **non-GAAP**: across eight companies' own full-year
reconciliations the gap between GAAP and non-GAAP operating margin runs from 9.6 to 41 points, median
**22.6 points** (`SWM-5`). (2) The quoted number is usually the **revenue-weighted aggregate**
(27.22% for SIC 7372), not a typical company: the **median** listed prepackaged-software filer has an
operating margin of **−4.5%** (`SWM-2`). (3) What is left — a genuinely better business at the top
of the industry — is real: Adobe, Microsoft and AWS beat Silex on operating margin *and* on return on
assets, which is the combination that matters. They do not beat it on asset turnover (Microsoft's is
0.455 against Silex's 0.617) or on capital intensity; they beat it on margin by enough to win anyway.

**The finding that cuts hardest against this project's own framing is `SWM-7`.** The argument for an
API-first foundry leans on the cloud analogy, and the cloud analogy assumes software needs no
factory. For the median software filer that is still true — median capex is **0.9%** of revenue and
median net plant **4.3%**. But **AWS spent 74.96% of its 2025 revenue on property and equipment and
carries net plant worth 147.64% of a year's revenue**; Oracle's net plant is **148.40%** of revenue
and Microsoft's capex **34.94%**. All three are more capital-hungry per dollar of revenue than TSMC
(33.03% and 111.77%), and AWS is **5.32× more capex-intensive than the MEMS fab**. A company the SEC
classifies as "Services-Prepackaged Software", CoreWeave, spent **200.92% of its revenue** on plant
in one year. **If the pitch is "the AWS of silicon", the honest version of that sentence now includes
AWS's balance sheet, and it is a fab's balance sheet at ten times the scale.**

**A low SaaS margin and a low fab margin are not the same fact — but the reason usually given is
wrong about two-thirds of the time.** Among *growing* software filers, faster growth does go with a
lower margin (`SWM-8`). But of the 111 SIC 7372 filers with a negative operating margin, only 33%
grew by 20% or more, while 32% were shrinking outright. Of the bottom quintile by margin, **70% are
in the bottom two quintiles by growth.** "They're buying growth" describes about a third of
loss-making listed software.

## How to read the tables

Every distribution figure is a **median and quartiles, never a mean.** These populations have tails
that make a mean meaningless: one SIC 7372 filer in CY2025 has an operating margin of −889.6%,
another a return on assets of +821.0%. Where a
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
| `SWM-6` | The DuPont decomposition, and the two questions answered: what a fab would need to match software, and by how much software wins at equal margin |
| `SWM-7` | Amazon's AWS segment — and the finding that AWS is a heavier fab than Silex |
| `SWM-8` | The Rule of 40: a low SaaS margin and a low fab margin do not mean the same thing |
| `SWM-9` | Listed wafer foundries on the same basis, for the other side of the comparison |

---

### SWM-1. The method: the SEC publishes every filer's tagged financials as free JSON, so the distribution can be measured rather than sampled

- **Sources:**
  - Frames API (every filer, one concept, one period):
    `https://data.sec.gov/api/xbrl/frames/us-gaap/<tag>/USD/<period>.json`
  - Company facts (one filer, every concept):
    `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`
  - Submissions (the SIC code): `https://data.sec.gov/submissions/CIK##########.json`
  - Example of a single response used here:
    <https://data.sec.gov/api/xbrl/frames/us-gaap/OperatingIncomeLoss/USD/CY2025.json>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Context.** This entry exists so that every number in `SWM-2`, `SWM-3`, `SWM-6` and
  `SWM-8` can be reproduced or contradicted.
- **How it was counted.** Scripts, all committed:
  [`tools/sec_margins/fetch_sec.py`](../../tools/sec_margins/fetch_sec.py) (fetch and cache),
  [`tools/sec_margins/sic_distribution.py`](../../tools/sec_margins/sic_distribution.py)
  (the distribution, the DuPont decomposition and the growth regression) and
  [`tools/sec_margins/comparators.py`](../../tools/sec_margins/comparators.py) (the named companies).
  Rate limit 10 requests/second, honoured with a 0.15 s pause; every response cached so a re-run is
  free. User-Agent `foundry-api-research/1.0` — **a generic string; no e-mail address of any kind
  was placed in a header, URL or payload.**

  1. **One frame per concept per period** gives every filer that reported that concept. For CY2025,
     `OperatingIncomeLoss` returns **4,643** filers in a single response.
  2. **The fiscal-year trap.** A `CY2025` duration frame is *not* "the year ended 31 December 2025".
     It is whichever annual period of the filer's own best aligns with calendar 2025: Microsoft
     appears with 2024-07-01 → 2025-06-30, Salesforce with 2025-02-01 → 2026-01-31. That is what
     makes the sample usable — January and June year-ends are normal in software and would otherwise
     be silently dropped — but the frame's `end` field has to be read, never assumed.
  3. **The balance-sheet join.** Because of (2), assets cannot be taken from `CY2025Q4I`. Every
     instantaneous frame from `CY2022Q1I` to `CY2026Q4I` was indexed by `(cik, end date)` and looked
     up at the income statement's own end date. Balance-sheet figures are therefore **ending**, not
     average.
  4. **SIC** comes from the submissions API, one call per filer, reading only the first 4 kB.
     All **7,066** CIKs in the frame universe were resolved and every one returned a
     SIC code, so **no filer was dropped for want of one.**
  5. **Fallbacks, because most software filers do not tag the obvious element.** Gross profit falls
     back to `Revenues − CostOfRevenue` (or `− CostOfGoodsAndServicesSold`), refused when the cost
     element is tagged negative. SG&A falls back to `SellingAndMarketingExpense +
     GeneralAndAdministrativeExpense`, because software companies overwhelmingly report those two
     lines rather than the combined one. Revenue prefers `Revenues`, then
     `RevenueFromContractWithCustomerExcludingAssessedTax`, then the "including assessed tax"
     variant; in SIC 7372 that resolves to `RevenueFromContractWithCustomerExcludingAssessedTax` for 147 filers, `Revenues` for
     54 and the “including assessed tax” variant for 10.
- **What it says — the population, and what was dropped.**

  | | CY2025 | CY2024 |
  |---|---:|---:|
  | Filers reporting `OperatingIncomeLoss` for the period | 4,643 | 4,977 |
  | **Usable: operating income, revenue and total assets at the same fiscal year end** | **3,598** | **3,832** |
  | Dropped — no `OperatingIncomeLoss` (reported revenue only) | 655 | 707 |
  | Dropped — no revenue element at the same period end | 615 | 671 |
  | Dropped — revenue ≤ 0 | 127 | 130 |
  | Dropped — revenue < US$1,000,000 | 297 | 316 |
  | Dropped — no `Assets` fact at that fiscal year end | 6 | 7 |
  | Dropped — no SIC code | 0 | 0 |

  **Nothing was dropped for being unprofitable, small, foreign or oddly classified.** The only
  filters are: the filer must have tagged an operating income, a revenue, and total assets at the
  same fiscal year end; revenue must be positive; and revenue must be at least **US$1,000,000**,
  because below that a ratio is noise (a filer with $40,000 of revenue and a $2m loss is a −5,000%
  operating margin and would otherwise set the minimum of every table).

- **End-to-end check against a primary filing.** Workiva Inc. (CIK 1445305) appears in the CY2025
  data with revenue **$884,568,000** and operating income **−$42,441,000**, sourced to accession
  **0001445305-26-000016**. Reading that filing's own income statement rendering
  (<https://www.sec.gov/Archives/edgar/data/1445305/000144530526000016/R5.htm>) gives, in thousands:

  | | 2025 | 2024 | 2023 |
  |---|---:|---:|---:|
  | Total revenue | 884,568 | 738,680 | 630,039 |
  | Gross profit | 694,138 | 566,625 | 475,817 |
  | Loss from operations | (42,441) | (76,534) | (94,527) |

  The pipeline's figures match the filing exactly, and the accession number it carries is the right
  one (Workiva's FY2025 Form 10-K, filed 2026-02-19).
- **Caveats.**
  - **US SEC registrants only.** Private software companies — the great majority of the industry —
    are absent, and so is every non-US software company that does not file with the SEC. SAP is in
    because it files a 20-F.
  - **Most recent complete year.** CY2025 is the most recent calendar-aligned annual frame that is
    substantially filed as at 2026-09-25. A few filers have a later fiscal year in `companyfacts`
    (Microsoft's FY2026, Intuit's FY2026, Atlassian's FY2026); those are reported in `SWM-4` and are
    **not** mixed into the distribution.
  - **Tagging errors survive.** Two are visible in SIC 7372 CY2025: one filer's `GrossProfit`
    exceeds its `Revenues` (a gross margin of 151.3%) and one tags a cost of revenue five times its
    revenue (−400.0%). They are left in, named in `SWM-2`, and are why the file reports quartiles
    rather than a mean.
  - **`www.sec.gov` returns HTTP 403** to a scripted request, so the DERA Financial Statement Data
    Sets — which would have given SIC and every tag in one download — were unreachable. The
    frames-plus-submissions route used instead costs about 7,000 requests. See `search-log.md` §20.

### SWM-2. The distribution: the median listed prepackaged-software company does not make an operating profit, while the median *dollar* of its revenue earns about 28%. Both are true and they answer different questions

- **Source:** the population built in `SWM-1`, from
  `https://data.sec.gov/api/xbrl/frames/us-gaap/...`, fetched 2026-09-25. Script:
  [`tools/sec_margins/sic_distribution.py`](../../tools/sec_margins/sic_distribution.py).
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Context**, and the denominator for everything else in this file.
- **How it was counted:** medians and quartiles only, never means. Every metric is computed per
  filer and then the percentiles are taken across filers, so a metric's `n` is the number of filers
  that tagged the inputs, which differs by metric and is printed.
- **What it says.** Every cell is a percentage of the stated denominator except the asset-turnover
  rows, which are also shown as percentages (a turnover of 0.546 prints as 54.6%).

  **Operating margin and return on assets, every group, CY2025**

  | SIC group | n | p10 | p25 | **median op margin** | p75 | p90 | **median ROA** |
  |---|---:|---:|---:|---:|---:|---:|---:|
  | 7372 Services-Prepackaged Software | 211 | −131.4% | −26.1% | **−4.5%** | 9.1% | 24.1% | **−2.2%** |
  | 7370 Services-Computer Programming, Data Processing, Etc. | 66 | −109.5% | −26.9% | **−3.1%** | 8.2% | 29.3% | **−1.3%** |
  | 7371 Services-Computer Programming Services | 27 | −318.6% | −20.8% | **−2.4%** | 13.4% | 36.0% | **−1.2%** |
  | 7373 Services-Computer Integrated Systems Design | 36 | −388.6% | −102.1% | **−9.1%** | 9.7% | 20.3% | **−7.1%** |
  | 7374 Services-Computer Processing & Data Preparation | 71 | −231.3% | −45.6% | **−0.2%** | 8.4% | 17.7% | **−0.1%** |
  | 7389 Services-Business Services, NEC (catch-all) | 96 | −82.7% | −10.0% | **3.6%** | 13.7% | 25.1% | **1.6%** |
  | ALL software & computer services (737x) | 411 | −155.5% | −32.2% | **−3.3%** | 9.5% | 23.9% | **−1.9%** |
  | 3674 Semiconductors & Related Devices | 86 | −51.4% | −21.0% | **1.0%** | 12.6% | 27.9% | **0.4%** |
  | 3559 Special Industry Machinery, NEC | 14 | −44.9% | −23.0% | **3.0%** | 13.2% | 16.7% | **1.7%** |
  | ALL filers with the tags | 3598 | −158.7% | −23.9% | **2.1%** | 12.8% | 25.1% | **1.4%** |
  | 7372, revenue < $100m | 61 | −469.1% | −166.2% | **−49.1%** | −11.0% | 5.0% | **−29.5%** |
  | 7372, revenue $100m-$1bn | 82 | −25.6% | −15.1% | **−3.0%** | 4.4% | 15.5% | **−2.1%** |
  | 7372, revenue > $1bn | 68 | −25.4% | −2.1% | **10.7%** | 22.2% | 30.9% | **5.3%** |

  **SIC 7372 Services-Prepackaged Software, CY2025** (n = 211)

  | Metric | n | min | p10 | p25 | **median** | p75 | p90 | max |
  |---|---:|---:|---:|---:|---:|---:|---:|---:|
  | Operating margin | 211 | −889.6% | −131.4% | −26.1% | **−4.5%** | 9.1% | 24.1% | 209.7% |
  | Asset turnover | 211 | 5.5% | 20.4% | 38.5% | **54.6%** | 77.4% | 114.9% | 391.4% |
  | Return on assets | 211 | −607.5% | −55.0% | −15.8% | **−2.2%** | 5.5% | 11.7% | 821.0% |
  | Turnover ex cash & goodwill | 211 | 7.4% | 33.4% | 64.6% | **98.2%** | 157.9% | 220.9% | 631.9% |
  | Return ex cash & goodwill | 211 | −711.3% | −84.3% | −28.4% | **−4.3%** | 9.7% | 23.1% | 1,028.4% |
  | Gross margin | 194 | −400.0% | 28.8% | 49.3% | **70.9%** | 78.5% | 84.6% | 151.3% |
  | R&D ÷ revenue | 186 | 0.0% | 8.1% | 14.0% | **21.6%** | 29.3% | 51.3% | 376.8% |
  | SG&A ÷ revenue | 194 | 7.2% | 21.1% | 33.8% | **49.2%** | 64.7% | 105.4% | 680.2% |
  | Stock comp ÷ revenue | 194 | 0.0% | 2.8% | 5.1% | **10.5%** | 18.0% | 26.1% | 168.6% |
  | Capex ÷ revenue | 176 | 0.0% | 0.2% | 0.4% | **0.9%** | 2.2% | 6.0% | 200.9% |
  | Net PP&E ÷ revenue | 187 | 0.0% | 0.7% | 1.6% | **4.3%** | 8.0% | 17.6% | 595.5% |
  | Operating cash flow ÷ revenue | 208 | −734.6% | −68.0% | −3.3% | **15.2%** | 26.1% | 36.1% | 59.6% |

  **SIC 7372 Services-Prepackaged Software, CY2024** (n = 231)

  | Metric | n | min | p10 | p25 | **median** | p75 | p90 | max |
  |---|---:|---:|---:|---:|---:|---:|---:|---:|
  | Operating margin | 231 | −1,345.7% | −104.9% | −33.0% | **−5.4%** | 8.3% | 22.1% | 221.4% |
  | Asset turnover | 231 | 1.9% | 25.1% | 37.4% | **57.1%** | 86.3% | 139.7% | 728.4% |
  | Return on assets | 231 | −843.2% | −49.8% | −16.0% | **−2.4%** | 4.9% | 11.3% | 472.4% |
  | Turnover ex cash & goodwill | 231 | 3.6% | 39.3% | 67.0% | **106.1%** | 163.0% | 242.9% | 1,005.4% |
  | Return ex cash & goodwill | 231 | −855.1% | −96.7% | −33.1% | **−5.1%** | 8.2% | 24.7% | 901.8% |
  | Gross margin | 213 | −73.6% | 36.3% | 51.9% | **69.8%** | 79.3% | 84.8% | 95.2% |
  | R&D ÷ revenue | 201 | 0.0% | 6.9% | 13.6% | **22.1%** | 30.9% | 47.2% | 314.5% |
  | SG&A ÷ revenue | 211 | 6.2% | 21.3% | 35.2% | **48.7%** | 65.5% | 91.9% | 1,331.0% |
  | Stock comp ÷ revenue | 204 | −1.2% | 2.5% | 5.2% | **11.0%** | 19.0% | 28.9% | 126.5% |
  | Capex ÷ revenue | 195 | 0.0% | 0.2% | 0.3% | **0.9%** | 1.9% | 5.0% | 454.4% |
  | Net PP&E ÷ revenue | 208 | 0.0% | 0.6% | 1.6% | **4.3%** | 8.5% | 19.8% | 622.2% |
  | Operating cash flow ÷ revenue | 230 | −530.5% | −33.6% | −5.3% | **12.5%** | 24.7% | 32.7% | 226.2% |

  **All software and computer services, SIC 737x, CY2025** (n = 411)

  | Metric | n | min | p10 | p25 | **median** | p75 | p90 | max |
  |---|---:|---:|---:|---:|---:|---:|---:|---:|
  | Operating margin | 411 | −30,033.3% | −155.5% | −32.2% | **−3.3%** | 9.5% | 23.9% | 236.3% |
  | Asset turnover | 411 | 0.1% | 15.2% | 37.6% | **57.8%** | 87.1% | 139.3% | 1,216.6% |
  | Return on assets | 411 | −2,813.4% | −54.2% | −16.2% | **−1.9%** | 6.5% | 14.0% | 821.0% |
  | Turnover ex cash & goodwill | 410 | 0.1% | 28.5% | 64.2% | **105.9%** | 169.1% | 260.8% | 3,281.0% |
  | Return ex cash & goodwill | 410 | −2,813.4% | −89.3% | −28.6% | **−2.5%** | 11.6% | 24.3% | 1,028.4% |
  | Gross margin | 367 | −466.7% | 21.7% | 39.3% | **64.3%** | 77.0% | 84.4% | 8,890.6% |
  | R&D ÷ revenue | 334 | 0.0% | 4.9% | 10.5% | **18.6%** | 27.9% | 56.7% | 24,833.3% |
  | SG&A ÷ revenue | 375 | 0.0% | 15.9% | 27.8% | **44.4%** | 64.0% | 123.3% | 4,733.3% |
  | Stock comp ÷ revenue | 364 | −1.7% | 1.2% | 3.5% | **8.5%** | 17.5% | 30.6% | 6,266.7% |
  | Capex ÷ revenue | 330 | 0.0% | 0.1% | 0.4% | **0.9%** | 2.6% | 7.7% | 1,033.3% |
  | Net PP&E ÷ revenue | 363 | 0.0% | 0.3% | 1.2% | **3.8%** | 9.2% | 20.3% | 3,433.3% |
  | Operating cash flow ÷ revenue | 403 | −19,366.7% | −107.7% | −7.2% | **10.8%** | 24.4% | 35.6% | 400.8% |

  **SIC 7372, revenue $100m-$1bn, CY2025** (n = 82)

  | Metric | n | min | p10 | p25 | **median** | p75 | p90 | max |
  |---|---:|---:|---:|---:|---:|---:|---:|---:|
  | Operating margin | 82 | −199.2% | −25.6% | −15.1% | **−3.0%** | 4.4% | 15.5% | 48.8% |
  | Asset turnover | 82 | 14.3% | 30.9% | 41.0% | **58.8%** | 76.3% | 114.5% | 164.7% |
  | Return on assets | 82 | −81.4% | −17.2% | −9.0% | **−2.1%** | 2.2% | 9.8% | 30.5% |
  | Turnover ex cash & goodwill | 82 | 21.8% | 55.9% | 79.1% | **115.8%** | 174.6% | 210.2% | 512.2% |
  | Return ex cash & goodwill | 82 | −87.7% | −36.6% | −17.4% | **−3.4%** | 4.6% | 16.9% | 250.2% |
  | Gross margin | 73 | 10.3% | 39.2% | 57.1% | **71.5%** | 76.9% | 82.4% | 94.9% |
  | R&D ÷ revenue | 76 | 2.1% | 7.2% | 14.4% | **21.4%** | 26.6% | 36.4% | 91.5% |
  | SG&A ÷ revenue | 80 | 7.2% | 25.2% | 35.6% | **47.9%** | 59.9% | 70.0% | 134.2% |
  | Stock comp ÷ revenue | 81 | 0.0% | 2.2% | 5.1% | **9.4%** | 17.5% | 20.6% | 105.4% |
  | Capex ÷ revenue | 74 | 0.0% | 0.3% | 0.4% | **0.9%** | 2.6% | 4.2% | 14.9% |
  | Net PP&E ÷ revenue | 69 | 0.1% | 1.1% | 2.4% | **4.9%** | 9.1% | 14.6% | 62.5% |
  | Operating cash flow ÷ revenue | 81 | −76.0% | −4.4% | 7.4% | **14.1%** | 23.7% | 26.7% | 46.2% |

  **Revenue-weighted aggregates — the same populations, summed rather than ranked**

  | Group | n | revenue-weighted op margin | asset turnover | ROA | turnover ex cash+goodwill | ROA ex cash+goodwill |
  |---|---:|---:|---:|---:|---:|---:|
  | 7372 Services-Prepackaged Software | 211 | **27.22%** | 0.416 | **11.33%** | 0.649 | 17.66% |
  | 7370 Services-Computer Programming, Data Processing, Etc. | 66 | **30.92%** | 0.596 | **18.44%** | 0.715 | 22.10% |
  | 7371 Services-Computer Programming Services | 27 | **14.38%** | 0.882 | **12.69%** | 1.507 | 21.67% |
  | 7373 Services-Computer Integrated Systems Design | 36 | **8.25%** | 0.697 | **5.75%** | 1.417 | 11.73% |
  | 7374 Services-Computer Processing & Data Preparation | 71 | **6.50%** | 0.583 | **3.79%** | 0.890 | 5.78% |
  | 7389 Services-Business Services, NEC (catch-all) | 96 | **16.77%** | 0.523 | **8.76%** | 0.791 | 13.27% |
  | ALL software & computer services (737x) | 411 | **26.91%** | 0.505 | **13.59%** | 0.711 | 19.14% |
  | 3674 Semiconductors & Related Devices | 86 | **33.06%** | 0.523 | **17.29%** | 0.766 | 25.32% |
  | 3559 Special Industry Machinery, NEC | 14 | **30.98%** | 0.846 | **26.20%** | 1.218 | 37.74% |
  | ALL filers with the tags | 3598 | **11.56%** | 0.656 | **7.59%** | 0.839 | 9.70% |

- **DERIVED (arithmetic written out).**
  - **The median filer and the median dollar are different animals, and the gap is the finding.**
    In SIC 7372 CY2025 the **median filer's** operating margin is **−4.5%**, while the
    **revenue-weighted aggregate** — total operating income of all 7372 filers ÷ their total
    revenue — is **+27.22%**. The second number is what people mean when they say "software runs at
    30%"; the first is what a randomly chosen listed software company actually earns. Quoting either
    one alone against a fab is misleading, so this file quotes both everywhere.
  - **Size explains most of it.** The median SIC 7372 filer with revenue **under $100m** has an operating margin of
    **−49.1%**; between **$100m and $1bn**, **−3.0%**; **above $1bn**, **+10.7%**. The population's
    negative median is a fact about how many very small loss-making software companies are listed
    in the United States, not a fact about software as a business.
  - **Capital intensity is where the two industries genuinely differ, and the gap is an order of
    magnitude.** Median SIC 7372 capex is **0.9%** of revenue and median net PP&E is
    **4.3%** of revenue, against Silex's **14.08%** and **68.02%** (`SWM-6`). That is
    **15.6×** on capex (14.08 ÷ 0.9) and **15.8×** on net plant (68.02 ÷ 4.3) on capex intensity. **This, and not the margin, is the real structural
    difference** — and `SWM-7` shows that it has stopped applying to the largest software
    businesses.
  - **Stock-based compensation is the population-level version of `SWM-5`.** Median SIC 7372 stock
    compensation is **10.5%** of revenue, upper quartile **18.0%**, top decile
    **26.1%**. A fab's equivalent line is a rounding error: Silex's prospectus discloses a
    warrant programme, not a material annual share-based charge. **Adding the median filer's stock
    compensation back to its operating margin moves it from **−4.5%** to
    **+6.0%** (−4.5 + 10.5)** — which is roughly the adjustment `SWM-5` measures directly for eight
    named companies.
  - **Two years, not one.** The CY2024 tables above are the stability check. SIC 7372's median operating margin was −5.4% in CY2024 against −4.5% in CY2025;
    median asset turnover 57.1% against 54.6%; median net PP&E 4.3% of revenue in both years;
    median stock compensation 11.0% against 10.5%; median capex 0.9% in both years. **Nothing in
    the picture is a one-year artefact.**
- **Named outliers, so the tails can be checked rather than trusted.**
  - **CoreWeave, Inc.** (CIK 1769628) is classified **SIC 7372, Services-Prepackaged Software**, and
    in CY2025 reported revenue of **$5,131m**, capex of **$10,309m** and net property and equipment
    of **$30,557m**, on a **−0.90%** operating margin and an asset turnover of **0.104**. Its capex
    is **200.92% of revenue** and its net plant **595.54%** — the maximum of both columns. Accession
    0001769628-26-000104. A "prepackaged software" company with six years of revenue tied up in
    plant is the single clearest illustration of `SWM-7`'s point.
  - The gross-margin maximum of **151.3%** is **TAOPING INC.**, which tags a `GrossProfit` of
    $3,368,706 against `Revenues` of $2,227,000 — a filer tagging error, left in and flagged.
  - The gross-margin minimum of **−400.0%** is **Zedge, Inc.**, whose tagged cost of revenue is
    $147.0m against $29.4m of revenue — almost certainly an impairment landing in the wrong element.
  - The operating-margin minimum of **−889.6%** is **authID Inc.**, $2,040,660 of revenue against a
    $18,153,520 operating loss. It is a real figure, and it is why no mean appears in this file.
- **Caveats.** SIC codes are self-reported on registration and are frequently stale: `7389
  Services-Business Services, NEC` is a catch-all that holds both software companies and businesses
  with nothing to do with software, and is reported above for completeness rather than as a software
  group. **SIC 7375, 7376, 7377, 7378 and 7379 have no filers at all** — not merely none that passed
  the filters, but none anywhere in the 7,066-CIK universe of `SWM-1` — so the "information
  retrieval" and "computer rental" rows cannot be produced. The SEC appears no longer to assign
  them. The five software-and-computer-services codes that are in use are 7370, 7371, 7372, 7373
  and 7374. Percentiles are unweighted across filers, so a
  $2m company counts as much as Microsoft — which is the point of also reporting the aggregate row.

### SWM-3. Where Silex's 22.7% actually falls: the 89th percentile of listed prepackaged software on operating margin, and higher still on return on assets

- **Source:** `SWM-2` (the distribution) and `SWM-6` (Silex's figures).
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Supports** H6. It is the direct answer to the question `LNI-17` raised.
- **How it was counted:** the percentile is the share of filers in the group whose value is at or
  below Silex's. Both Silex figures are carried — the parent-company 22.67% of `LNI-17` and the
  group 26.57% of the prospectus — and the return-on-assets percentile pairs each with the group's
  total assets of SEK 2,246m, which is conservative for the parent figure.

  Percentiles are the share of filers in the group at or below Silex's value, CY2025.

  | Group | n | Silex 22.67% (parent) margin pctile | Silex 26.57% (group) margin pctile | Silex ROA 13.98% pctile | Silex ROA 16.38% pctile |
  |---|---:|---:|---:|---:|---:|
  | 7372 Services-Prepackaged Software | 211 | 89.1 | **91.0** | 92.4 | **94.8** |
  | 7370 Services-Computer Programming, Data Processing, Etc. | 66 | 83.3 | **87.9** | 86.4 | **86.4** |
  | 7371 Services-Computer Programming Services | 27 | 81.5 | **85.2** | 77.8 | **81.5** |
  | 7373 Services-Computer Integrated Systems Design | 36 | 91.7 | **100.0** | 91.7 | **97.2** |
  | 7374 Services-Computer Processing & Data Preparation | 71 | 93.0 | **93.0** | 88.7 | **91.5** |
  | 7389 Services-Business Services, NEC (catch-all) | 96 | 86.5 | **90.6** | 89.6 | **92.7** |
  | ALL software & computer services (737x) | 411 | 88.6 | **91.2** | 89.8 | **92.2** |
  | 3674 Semiconductors & Related Devices | 86 | 82.6 | **88.4** | 88.4 | **89.5** |
  | 3559 Special Industry Machinery, NEC | 14 | 92.9 | **92.9** | 85.7 | **85.7** |
  | ALL filers with the tags | 3598 | 87.8 | **91.0** | 90.1 | **93.0** |
  | 7372, revenue < $100m | 61 | 96.7 | **96.7** | 96.7 | **96.7** |
  | 7372, revenue $100m-$1bn | 82 | 95.1 | **95.1** | 92.7 | **93.9** |
  | 7372, revenue > $1bn | 68 | 75.0 | **80.9** | 88.2 | **94.1** |

- **DERIVED (arithmetic written out).** 
  - Against **SIC 7372** (n = 211): the parent-company 22.67% sits at the **89.1st percentile** and
    the group 26.57% at the **91.0th**. Its return on assets of 13.98% is at the **92.4th** and
    16.38% at the **94.8th**.
  - Against the whole **737x** union (n = 411): **88.6** and **91.2** on margin; **89.8** and
    **92.2** on return on assets.
  - Against **every SEC filer with the tags** (n = 3,598), software or not: **87.8** and **91.0** on
    margin; **90.1** and **93.0** on return on assets.
  - Against its own **size peer group** — SIC 7372 filers with revenue between $100m and $1bn
    (n = 82). Silex's SEK 1,385m converts to roughly **US$125–150m** across the range of SEK/USD
    rates seen in 2025, so it lands in that band on any of them, and the conversion affects only
    which band is chosen, never a computed ratio. There it is at the **95.1st percentile** on margin
    and the **93.9th** on return on assets.
  - Against **SIC 3674, semiconductors and related devices** (n = 86): **82.6** and **88.4** on
    margin. Silex is a better business than most listed semiconductor companies too.
  - **The one group where it looks ordinary is SIC 7372 filers above $1bn of revenue** (n = 68),
    where 22.67% is only the **75.0th** percentile and 26.57% the **80.9th**. Even there, its
    return on assets is at the **94.1st** percentile — which is the whole argument of `SWM-6` in one
    line: the big software companies out-earn Silex on margin and lose to it on capital.
- **Caveats.** A percentile against listed US filers is not a percentile against the industry: the
  loss-making tail of SIC 7372 is a listed-company phenomenon (a private company with those numbers
  would not exist for long), and the profitable head is under-represented because the most
  profitable software businesses of all — the private ones and the divisions inside larger groups —
  never appear. The comparison is also across different reporting regimes: Silex is IFRS, most of
  the population is US GAAP, and IFRS 16 puts Silex's leased assets on its balance sheet in a way
  that **lowers** its measured asset turnover relative to a US GAAP filer with operating leases.

### SWM-4. The named comparators, GAAP, from their own XBRL: operating margins run from −30.6% (Snowflake) to +45.6% (Microsoft), and the median of the seventeen is 12.7%

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
    Zoom's 23.08% — **12th of 18**, i.e. above 11 of the other 17. Its group figure of 26.57% would
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

### SWM-5. GAAP against the headline: eight software companies' own full-year reconciliations, and the gap runs from 9.6 to 41 percentage points, median 22.6

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

### SWM-6. The decomposition that makes the comparison fair: a fab at 22.7% clears the software industry's aggregate return on assets, and is beaten only at the very top — by AWS, Microsoft and Adobe

- **Sources:** `SWM-2` (the distribution), `SWM-4` (the named companies), `LNI-17` and `LNI-18`
  (Silex). Silex's balance sheet and cash flow were read from the prospectus itself, which
  `LNI-18` had not needed: Silex Microsystems AB (publ), *Invitation to acquire ordinary shares*,
  approved by Finansinspektionen 2026-04-27, diary number 25-37533,
  <https://www.fi.se/sv/vara-register/prospektregistret/details?id=25-37533> (document:
  `GetFile?id=25-37533`), "Selected historical financial information", pp. 103–110.
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Supports** H6, and it is the entry this whole file exists to produce.
- **Why an operating margin on its own is not a comparison.** A fab earns its margin *after*
  depreciating a cleanroom; a SaaS company earns it on almost no fixed assets. Comparing the two
  percentages directly rewards whichever business happens to rent rather than own. The standard
  correction is the DuPont identity:

  > **operating margin × asset turnover = return on assets**

  which is an arithmetic identity, not a model: (operating income ÷ revenue) × (revenue ÷ assets) =
  operating income ÷ assets.

- **What it says — Silex's own numbers, from the prospectus.** Consolidated, IFRS, MSEK:

  | Year to 31 December | 2025 | 2024 | 2023 |
  |---|---:|---:|---:|
  | Net sales | 1,385 | 1,226 | 1,095 |
  | Operating profit (group) | 368 | 339 | 276 |
  | Depreciation and amortisation | 125 | 117 | 108 |
  | Total assets | 2,246 | 2,265 | 2,349 |
  | Cash and cash equivalents | 266 | 434 | 311 |
  | Property, plant and equipment (excl. right-of-use) * | 942 | 825 | 821 |
  | Right-of-use assets | 369 | 415 | 412 |
  | Investment in tangible fixed assets (capex) | 195 | 78 | 111 |
  | Net cash flows from operating activities | 353 | 377 | 352 |
  | Personnel expenses | 383 | 353 | 336 |

  \* **DERIVED**, as the sum of the four printed lines: 2025 buildings and land 439 + machinery and
  other technical facilities 314 + equipment, tools, fixtures and fittings 20 + construction in
  progress 169 = **942**. 2024: 426 + 348 + 15 + 36 = **825**. 2023: 401 + 368 + 17 + 35 = **821**.
  The prospectus prints no combined "property, plant and equipment" subtotal.

- **DERIVED (arithmetic written out) — Silex.**
  - **Operating margin.** 2025: 368 ÷ 1,385 = **26.57%**. 2024: 339 ÷ 1,226 = **27.65%**. 2023:
    276 ÷ 1,095 = **25.21%**. The parent-company figure `LNI-17` carries is 314 ÷ 1,385 = **22.67%**.
  - **The two Silex figures, and why both are quoted.** The group's operating profit is SEK 368m and
    the aggregator's parent-company figure is SEK 314m on identical net sales. The difference is
    SEK 54m; the group's *other operating income* is SEK 58m, and 368 − 58 = **310**, within SEK 4m
    of 314. That is **consistent with** the parent figure being struck before other operating
    income. It is recorded as an observation, not as a reconciliation — the group boundary is still
    not established (`LNI-17` caveat). **Every comparison below is given on both.**
  - **Asset turnover.** 1,385 ÷ 2,246 = **0.6167**. 2024: 1,226 ÷ 2,265 = 0.5413. 2023: 0.4662.
  - **Return on assets.** Group: 368 ÷ 2,246 = **16.38%**. Check: 0.2657 × 0.6167 = 0.1639.
    Parent EBIT over group assets: 314 ÷ 2,246 = **13.98%** (a deliberately conservative pairing).
  - **On assets less cash.** Silex holds SEK 266m of cash and no goodwill (intangible assets are
    tagged 0), so operating assets are 2,246 − 266 = **1,980**. Turnover 1,385 ÷ 1,980 = **0.6995**;
    return 368 ÷ 1,980 = **18.59%** (parent: 314 ÷ 1,980 = **15.86%**).
  - **Capital intensity.** Capex 195 ÷ 1,385 = **14.08%**. Net PP&E 942 ÷ 1,385 = **68.02%**;
    including right-of-use assets (942 + 369) ÷ 1,385 = **94.66%**.
  - **EBITDA margin.** (368 + 125) ÷ 1,385 = **35.60%**. Operating cash flow 353 ÷ 1,385 = **25.49%**.
  - **Personnel.** 383 ÷ 1,385 = **27.65%** of net sales, which reproduces `LNI-17`'s 27.9% for 2024
    from the group accounts (353 ÷ 1,226 = 28.79%).

- **DERIVED (arithmetic written out) — Q1. At equal operating margin, how much better is a software
  business than a fab?** The answer is the **ratio of asset turnovers and nothing else**, because
  margin × turnover = return on assets and the margins are equal by assumption. Silex's turnover is
  1,385 ÷ 2,246 = **0.6167**.

  | Software benchmark, SIC 7372 CY2025 | Asset turnover | ÷ Silex 0.6167 | At equal operating margin, software earns |
  |---|---:|---:|---|
  | median filer | 0.546 | **0.885×** | **11.5% _less_** on its assets |
  | upper quartile (p75) | 0.774 | **1.255×** | 25.5% more |
  | top decile (p90) | 1.149 | **1.864×** | 86.4% more |
  | median filer above $1bn of revenue | 0.505 | **0.818×** | 18.2% _less_ |
  | median filer in Silex's $100m–$1bn band | 0.588 | **0.953×** | 4.7% _less_ |
  | **revenue-weighted aggregate of all 211** | **0.416** | **0.675×** | **32.5% _less_** |

  On **assets less cash and goodwill**, where Silex's turnover is 1,385 ÷ 1,980 = 0.6995: the SIC
  7372 median is 0.982, a ratio of **1.404×**, and the 7372 aggregate is 0.649, a ratio of
  **0.928×**.

  **So the answer is not "software wins by 3×". It is between 0.68× and 1.86× depending on which
  software you mean, and on the reading most people intend — the industry in aggregate — a software
  company at Silex's operating margin would earn about a third _less_ on its assets than Silex
  does.** The reason is not that software is capital-intensive. It is that a software balance sheet
  is mostly cash, marketable securities and the goodwill of past acquisitions, none of which produce
  revenue. Strip cash and goodwill out and software's turnover advantage reappears at the median
  (1.404×) but still not in aggregate (0.928×), because the biggest holders of cash and goodwill are
  the biggest companies.

- **DERIVED (arithmetic written out) — Q2. What operating margin would a fab need to match the
  software company's return on assets?** Required margin = software's return on assets ÷ the fab's
  asset turnover of 0.6167.

  | Software benchmark | Its return on assets | ÷ 0.6167 = margin the fab would need | Silex at 22.67% / 26.57% |
  |---|---:|---:|---|
  | SIC 7372 median filer | −2.16% | **−3.50%** | clears it |
  | SIC 7372 median, revenue $100m–$1bn | −2.10% | **−3.41%** | clears it |
  | SIC 7372 median, revenue > $1bn | 5.32% | **8.62%** | clears it |
  | SIC 7372 upper quartile | 5.47% | **8.87%** | clears it |
  | **SIC 7372 revenue-weighted aggregate** | **11.33%** | **18.38%** | **clears it on both figures** |
  | SIC 7372 top decile | 11.73% | **19.02%** | clears it on both figures |
  | Intuit (`SWM-4`) | 13.32% | **21.60%** | clears it on both figures |
  | SAP (`SWM-4`) | 13.67% | **22.17%** | clears it on the group figure; 22.67% clears it by 0.50 pp |
  | AWS segment (`SWM-7`) | 18.06% | **29.29%** | **does not clear it** |
  | Microsoft (`SWM-4`) | 20.76% | **33.66%** | does not clear it |
  | Adobe (`SWM-4`) | 29.52% | **47.87%** | does not clear it |

  Worked, for the four that matter: 11.33% ÷ 0.6167 = **18.38%**; 11.73% ÷ 0.6167 = **19.02%**;
  18.06% ÷ 0.6167 = **29.29%**; 29.52% ÷ 0.6167 = **47.87%**.

  **Stated plainly, and this is the answer the file was built to produce: a fab at 22.7% is not
  merely competitive on return on assets — it clears the bar set by the entire listed
  prepackaged-software industry in aggregate (18.38%) and by the top decile of that industry
  (19.02%), on the lower of its two published operating margins.** What it does not clear is AWS
  (29.29%), Microsoft (33.66%) and Adobe (47.87%). The honest summary is that **software is not, as
  a class, a better business than a good specialty fab. The three or four best software businesses
  in the world are.**

- **The gross-margin comparison is the one that must not be made.** Silex's prospectus prints a
  "Gross margin 1" of **86.3%** for 2025, which is higher than all but a handful of SaaS companies.
  It is not the same quantity. The prospectus defines it:

  > "Gross profit 1  Net sales less raw materials and consumables."

  That is net sales less **materials only** — no labour, no depreciation, no utilities, no
  cleanroom. A software gross margin is struck after hosting, support and the amortisation of
  capitalised software. **1,385 − 190 = 1,195; 1,195 ÷ 1,385 = 86.28%**, and the 190 is the entire
  "raw materials and consumables" line. Quoting 86.3% against SIC 7372's median gross margin of
  **70.9%** would be a straightforward error, and it is recorded here so nobody makes it.
- **Caveats.**
  - Ending assets, not average assets, throughout — for Silex and for every filer. Silex's assets
    fell slightly in 2025 (2,265 → 2,246) so the effect on its figure is negligible; for a
    fast-growing software company ending assets inflate the denominator and therefore
    **understate** its return, which is conservative against the fab.
  - `LNI-17`'s 22.67% is a parent-company operating result from a commercial re-publisher of Swedish
    filings; the group figure of 26.57% is from a regulator-approved prospectus. Where one number
    has to be chosen, the group figure is the better-sourced one.
  - The "assets less cash and goodwill" correction removes only cash and equivalents, because no
    short-term-investments element is tagged consistently. Microsoft, Oracle and Salesforce hold
    large marketable-securities portfolios that stay in their denominators, so the correction
    **understates** software's operating-asset turnover and is conservative against the fab.

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

### SWM-8. The Rule of 40, tested: among *growing* software companies a low margin really is bought growth — but most low-margin software companies are not growing, they are shrinking

- **Source:** the CY2025 and CY2024 populations of `SWM-1`, joined by CIK. Script:
  [`tools/sec_margins/sic_distribution.py --rule40`](../../tools/sec_margins/sic_distribution.py).
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Context**, and a direct qualification of `SWM-2`. It is the reason a −20% SaaS
  margin and a −20% fab margin are not the same fact — and also the reason that equivalence is
  claimed far too freely.
- **How it was counted.** Revenue growth is CY2025 revenue ÷ CY2024 revenue − 1, for filers present
  in both years with the same SIC. Growth outside (−90%, +500%) is dropped as a reverse merger or a
  restatement artefact. Operating margins are winsorised at the 1st and 99th percentile **for the
  OLS only**, so that one −889% filer does not set the slope; the rank statistics use the raw data.

- **What it says — the summary statistics.**

  | | SIC 7372 | all 737x |
  |---|---:|---:|
  | filers with both years and a usable growth rate | **202** | **381** |
  | Pearson *r* (revenue growth, operating margin) | +0.206 | +0.023 |
  | Spearman ρ | **+0.184** (t = +2.64) | **+0.205** (t = +4.08) |
  | OLS slope, margins winsorised at 1st/99th pct | +47.76 pp per 1.00 of growth (t = +2.86) | +7.53 pp (t = +0.65) |
  | Rule-of-40 score (growth + GAAP margin): p25 / median / p75 / p90 | −13.1% / **12.5%** / 27.7% / 43.9% | −18.2% / **10.9%** / 28.1% / 47.1% |
  | share of filers clearing a score of 40% | **13.9%** | **14.4%** |

  **Medians by revenue-growth quintile, SIC 7372 (n = 202):**

  | Growth quintile | n | median growth | **median operating margin** | median R&D ÷ rev | median stock comp ÷ rev |
  |---|---:|---:|---:|---:|---:|
  | Q1 slowest | 40 | −12.2% | **−36.3%** | 17.7% | 6.7% |
  | Q2 | 40 | +2.7% | **+2.5%** | 24.2% | 8.1% |
  | Q3 | 40 | +12.1% | **+4.8%** | 20.1% | 9.2% |
  | Q4 | 40 | +18.5% | **+0.9%** | 22.3% | 10.9% |
  | Q5 fastest | 42 | +30.5% | **−8.8%** | 22.6% | 17.3% |

  **The same, all 737x (n = 381):**

  | Growth quintile | n | median growth | **median operating margin** | median R&D ÷ rev | median stock comp ÷ rev |
  |---|---:|---:|---:|---:|---:|
  | Q1 slowest | 76 | −15.9% | **−34.1%** | 17.2% | 6.4% |
  | Q2 | 76 | +1.4% | **+1.6%** | 16.4% | 5.0% |
  | Q3 | 76 | +9.7% | **+4.8%** | 18.2% | 7.0% |
  | Q4 | 76 | +17.8% | **+3.5%** | 20.9% | 10.2% |
  | Q5 fastest | 77 | +38.7% | **−8.1%** | 19.1% | 15.2% |

  **Split at zero growth, because the two halves are opposite stories:**

  | Subset | SIC 7372 | all 737x |
  |---|---|---|
  | shrinking (growth < 0) | n = 44, median growth −9.2%, median margin −29.0%, **Spearman +0.526 (t = +4.01)** | n = 96, median growth −10.4%, median margin −24.1%, **Spearman +0.503 (t = +5.64)** |
  | growing (growth ≥ 0) | n = 158, median growth +16.2%, median margin +0.4%, **Spearman −0.154 (t = −1.95)** | n = 285, median growth +14.5%, median margin +2.2%, **Spearman −0.166 (t = −2.84)** |
  | growing fast (growth ≥ 20%) | n = 54, median growth +29.4%, median margin −7.8%, Spearman −0.025 (t = −0.18) | n = 92, median growth +32.5%, median margin −5.8%, Spearman −0.133 (t = −1.27) |

- **What it says.**
  - **The pooled correlation between revenue growth and operating margin is positive, which looks
    like the opposite of the Rule of 40 until you split the sample.** It is positive because the
    shrinking filers have catastrophic margins, and they are shrinking, not investing.
  - **Split at zero growth, the two halves are opposite.** Among filers that grew, the rank
    correlation between growth and operating margin is **negative** — faster growth, lower margin,
    which is exactly the trade-off the Rule of 40 describes. It is significant at conventional
    levels across all of 737x (ρ = −0.166, t = −2.84, n = 285) and marginal in SIC 7372 alone
    (ρ = −0.154, t = −1.95, n = 158), so it is reported as a real but modest effect, not a strong
    one. Among filers that **shrank** it is **strongly positive** (ρ = +0.526 and +0.503, t = +4.01
    and +5.64) — the more revenue you lose, the worse your margin, which is operating leverage
    running backwards and is not a choice anybody made.
  - **The quintile table shows the same thing as an inverted U.** Margin is worst in the slowest
    quintile, rises through the middle quintiles, and falls again in the fastest. **R&D and
    stock-based compensation rise monotonically with growth**, which is the mechanism: the
    fast-growing quintile is spending the margin on engineers and equity.
- **What it means for the comparison with a fab.**
  - A software company at −20% may be buying a business that will exist in five years. **A fab at
    −20% is not**: its cost base is depreciation and a cleanroom's utilities, which do not convert
    into future revenue the way a sales force does. So a like-for-like margin comparison between a
    loss-making SaaS company and a loss-making fab is genuinely unfair to the fab.
  - **But the premise is only half true, and the half that is false is the half usually assumed.**
    **DERIVED:** of the 40 SIC 7372 filers in the **bottom quintile by operating margin**, **28
    (70%)** are in the bottom two quintiles by revenue growth and only **7 (18%)** are in the
    fastest-growing quintile. Of the **111** SIC 7372 filers with a negative operating margin,
    **35 (32%) were shrinking** and **37 (33%) grew by 20% or more**. So the sentence "a low SaaS
    margin means they are buying growth" describes about a third of the cases, and a roughly equal
    third are companies whose revenue is going backwards. **A low SaaS margin is evidence of
    nothing on its own.**
  - **Silex is in neither position.** Its net sales grew **+12.96%** in 2025 (1,385 ÷ 1,226 − 1) at
    a 26.57% operating margin, giving a Rule-of-40 score of **12.96 + 26.57 = 39.53%** — against the
    SIC 7372 distribution of the same score in the table above. Its 2024 score was
    11.96% + 27.65% = **39.61%** (1,226 ÷ 1,095 − 1 = 11.96%). **It has run at essentially the same
    Rule-of-40 score two years running, and that score sits at the **86.1st percentile** of listed
    prepackaged software** (and the 85.6th of all 737x). On the parent-company margin the score is
    12.96 + 22.67 = **35.63%**, the **83.2nd** percentile.
- **Caveats.** One year of growth is a noisy measure and acquisitions are not stripped out, so an
  acquisitive filer shows as "growing" while its margin falls for reasons of purchase accounting.
  The Rule of 40 is conventionally computed on **non-GAAP** margins and often on ARR rather than
  revenue; computed on GAAP, as here, the scores are far lower than the ones quoted in the industry,
  and `SWM-5` says by how much. The relationship reported here is a cross-sectional association in
  one year, not a causal claim about what any company chose.

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

---

## What I could not get, and why

Recorded so nobody repeats the attempt. The access-level detail is in
[`search-log.md`](search-log.md) §20.

1. **Private software companies — the great majority of the industry.** Everything here is US SEC
   registrants. The loss-making tail of SIC 7372 is partly a listing artefact (a private company
   with those numbers would be wound up, not reported), and the profitable head is under-represented
   because the best software businesses of all — the private ones, and the divisions inside larger
   groups — never file. There is no public data source that fixes this, and no estimate is offered.
2. **Non-US software companies that do not file with the SEC.** SAP is in because it files a 20-F.
   Sage, Dassault Systèmes, Xero, Constellation Software and the rest are not, so "the distribution
   of software margins" means "of US-listed software margins" throughout.
3. **A population-level non-GAAP figure.** Non-GAAP operating margin is **not** an XBRL concept, so
   it cannot be pulled from the frames. `SWM-5`'s eight companies were read one at a time out of
   their 8-K exhibits and are a deliberate spread, not a sample. The nearest population-level proxy
   is `ShareBasedCompensation ÷ revenue`, which `SWM-2` reports in full.
4. **Short-term investments.** The "assets less cash and goodwill" correction removes only
   `CashAndCashEquivalentsAtCarryingValue`, because no element for marketable securities is tagged
   consistently across filers. Microsoft, Oracle, Salesforce and Alphabet-scale balance sheets keep
   tens of billions of Treasuries in the denominator. The correction is therefore **partial and
   conservative against software** — the true software operating-asset turnover is higher than the
   figure used in `SWM-6`, and by an unknown amount.
5. **The SEC's DERA Financial Statement Data Sets**, which carry SIC and every tag in one quarterly
   download, are on `www.sec.gov` and return **HTTP 403** to a scripted request under every
   User-Agent tried. The frames-plus-submissions route used instead needed about 7,000 requests and
   an hour. Not solved.
6. **TSMC's and UMC's FY2025 Form 20-F facts** were not in `companyfacts` on 2026-09-25, so `SWM-9`
   reports FY2024 for both against FY2025 for everyone else. **Nothing is asserted about their FY2025
   figures in either direction.**
7. **AWS's share of Amazon's unallocated corporate assets.** Amazon carries $247,818m of 2025 assets
   in "Corporate", so AWS's 18.06% return on segment assets is computed on a denominator that
   excludes whatever part of that belongs to it. The true figure is lower, by an amount Amazon does
   not disclose.
8. **Amazon's research and development** is not tagged as `ResearchAndDevelopmentExpense`; it reports
   "Technology and infrastructure", which mixes R&D with running the data centres. The R&D column is
   blank for Amazon rather than filled with a non-comparable number.
9. **Silex's R&D as a line item.** IFRS lets process-development cost sit inside personnel and other
   external expenses, and Silex does not break it out. The prospectus states only that Silex "invests
   approximately 8–10 percent of its annual net sales in the development of its manufacturing
   processes and technologies", which is a company statement, not a measured line.
10. **Silex's parent-versus-group boundary** is still not established — `LNI-17`'s caveat stands.
    Both figures (22.67% and 26.57%) are carried through every comparison rather than one being
    chosen.
11. **Average rather than ending assets.** Computing DuPont on average assets would need two
    balance-sheet dates per filer per year; the frames make that possible but it doubles the join
    and was not done. Ending assets flatter a fast-growing company's denominator, so the software
    return on assets reported here is, if anything, **understated** for the fastest growers.
12. **Employment and output per head** were not attempted for the software population. Employee
    counts are in the `dei` taxonomy only sporadically and `EntityNumberOfEmployees` is not a
    required tag.
