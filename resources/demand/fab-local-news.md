# What a small US fab actually costs: filings, county agreements and local news (`LN`)

Entries `LN-1` … . This file goes after one specific shape of datum:

> "*SkyWater invests $10M USD and brings 200 new jobs to [town nobody has heard of]*"

— the **capital-cost-per-job** and **capital-cost-per-unit-of-capacity** pair, for US
small/specialty/MEMS/mature-node fabs. National trade press prints the headline; the county
commission agenda, the state economic-development press room and the SEC filing print the number.

The priority order is: (1) capital cost per unit of capacity and per job; (2) the public subsidy
attached; (3) head count, wafer-start capacity, wafer size, cleanroom area, node; (4) who the
customers are and whether small/prototype customers are served.

All currency is US dollars unless stated. Where a filing reports in thousands, this file writes the
figure out in full and says so.

---

## Summary, including what cuts against the thesis

**Read `LN-7` before quoting anything else in this file.** It is the single strongest number here
and it points the wrong way for the project.

SkyWater is the one US pure-play specialty foundry in this directory that has had to publish segment accounts,
and in the one year it reported two segments separately the result is unambiguous:

| FY2025 segment | What it is | Revenue | Operating income | Margin |
|---|---|---:|---:|---:|
| **Legacy SkyWater** (Bloomington MN + Kissimmee FL) | low-volume, high-mix, "highly customized projects in a low-volume research and development environment" | $266,847,000 | **$(34,496,000)** | **−12.93%** |
| **SkyWater Texas** (Fab 25, Austin) | high-volume 200 mm, one anchor customer on a take-or-pay | $175,292,000 | **$31,920,000** | **+18.21%** |

The high-mix, many-customer half loses money at the operating line. The single-anchor-customer,
high-volume half makes money. That is the JLC-versus-Porton question from
[`demand/other-industry-margins.md`](other-industry-margins.md) answered, for one year, in a wafer
fab, and it lands against **H6**. The caveats are real and are stated in `LN-7` — the Texas segment
is six months, its revenue contains amortisation of a $120,000,000 off-market supply contract, and
corporate SG&A sits entirely in the Legacy column — but they do not make a −12.93% operating margin
into a positive one.

**And the second-strongest finding, `LN-9`, points the same way.** Osceola County, Florida built a
$75,000,000, 109,000 sq ft fab at Kissimmee in the mid-2010s on exactly this project's thesis —
shared cleanroom access sold to many companies on a membership model. Florida Trend's account of
what happened is one sentence long:

> "The project’s creators expected the fab to draw interest from private companies who’d pay membership fees to use its clean room and share in intellectual property developed there. But that interest never materialized"

Nine years later the whole 500-acre NeoCity campus employed "roughly 90 people" against about
$200,000,000 of county and local money — **$2,222,222 of county capital per realised job**. That is
a third independent instance of the failure mode already recorded at MEMSCAP (`IHF-8`) and Efabless
(`OPEN-7`).

**The cleanest single comparison in the file is `LN-15`, and it is the same company doing both
things.** In July 2022 SkyWater announced a $1,800,000,000, 600,000 sq ft fab at Purdue with 750
jobs and $71,500,000 of Indiana state incentives — **$2,400,000 of capital per job**. It cancelled
it in April 2024. In June 2025 it spent **$86,500,000 of net cash** buying an operating 200 mm fab
in Austin and got **approximately 1,000 employees** and **400,000 wafer starts a year** —
**$86,500 of capital per job**. More jobs, for **4.81% of the announced capital**; the state
incentive per job on the plan that failed ($95,333) is **larger than the whole capital cost per job
of the deal that worked**.

**The three most useful capital numbers:**

1. **$86,500,000 of net cash bought a working 200 mm fab with approximately 1,000 employees,
   1,223,000 sq ft of building and 400,000 wafer starts a year of capacity** (`LN-3`). That is
   **$86,500 of capital per job**, **$2,595 per wafer-start-per-month** and **$216 per wafer of
   annual capacity** — one to two orders of magnitude below a greenfield build. The fab existed
   already; someone else paid for it.
2. **$56,000,000 of capex was expected to "increase overall output by at least 40%"** at a 200 mm
   fab (`LN-2`). A capital cost per unit of incremental capacity, stated by the operator.
3. **Capital cost per job splits by verb, not by company size** (`LN-14`). Across eleven US sites
   the range is **71×**, from $75,000 to $5,357,143 a job. The four cheapest are all *purchases of
   an operating fab from a seller who wanted out* — Bloomington **$75,000** (2017), San Antonio
   **$80,000** (2016), Fab 25 **$86,500** (2025), Canandaigua **$98,214** (2017): a 31% band across
   nine years, four states and two wafer sizes, mean **$84,929**. Everything that *builds or tools
   new capacity* averages **$1,300,816 a job**, **15.3×** as much.
4. **The same split, measured in capacity instead of jobs, gives 8.8×** (§ "Capital per wafer
   start"). Buying averages **$2,110 per wafer-start-per-month** across three transactions that
   agree to within 1.8× ($1,429 Tower, $2,308 Bloomington, $2,595 Fab 25); building or expanding
   averages **$18,510 per wspm** ($10,769 SkyWater debottleneck, $26,250 Polar). Two independent
   metrics on two overlapping sets of sites bracket the buy-versus-build gap at **roughly an order
   of magnitude**.

**And the answer to "can a long tail pay for it" is now computable, and it is a qualified no**
(§ "Capital per wafer start", part 4). The whole worldwide unsubsidised open-shuttle sector took
$931,158 in 2025 (`PAY-8`). That is **564 years** of revenue to fund Polar's $525,000,000 build and
**32 years** to fund the $30,000,000 purchase of the cheapest fab here. The reason is not price —
the long tail pays **$9,333 per 200 mm wafer equivalent** through wafer.space and on the order of
**€65,000** through a Tiny Tapeout shuttle, against the **$1,200 per wafer** SkyWater's Bloomington
fab actually earned. The reason is volume: the entire recorded die area of that sector, over its
whole existence, is **about two hours of one small fab's capacity**. What pays for a fab is
**1,560 customers buying 100 wafers a year** — at which size the capital is only **$19,231 per
customer if bought** and **$218,750 if built**, 6.4% and 72.9% of one year of that customer's
spend. **The capital is not the obstacle. Finding customers who buy wafers rather than tape-outs
is.**

And on the public money: it is a third to a half of a small fab's capital, not a rounding error.
Rogue Valley Palm Bay took $6,700,000 of CHIPS against $25,000,000 of project (26.8%, or 39.6%
counting other grants, `LN-12`); Polar took $198,000,000 of federal and state money against
$525,000,000 (37.71%, `LN-11`); X-FAB took up to $50,000,000 against $200,000,000 (25.0%, `LN-8`).
SkyWater is the outlier at the low end: up to $16,000,000 of CHIPS plus $19,000,000 from Minnesota's
Forward Fund (`LN-4`), against $206,466,000 of consideration for one fab and a $10,230,000 county
match obligation in Florida (`LN-5`).

And the structural fact behind all of it: **SkyWater no longer exists as an independent company**
(`LN-6`). It was bought by IonQ on 2026-07-31 for $15.00 cash plus 0.4883 IonQ shares per share. The
US-listed pure-play specialty foundry this directory has been tracking is now the captive fab of a
quantum-computing company.

---

### LN-1. SkyWater's head count, revenue and facilities, five years, from its own 10-Ks

- **Sources** (SEC EDGAR, SkyWater Technology, Inc., CIK 0001819974):
  - FY2021 Form 10-K, filed 2022-03-10:
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997422000013/skyt-20220102.htm>
  - FY2022 Form 10-K, filed 2023-03-15:
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997423000011/skyt-20230101.htm>
  - FY2023 Form 10-K, filed 2024-03-15:
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
  - FY2024 Form 10-K, filed 2025-03-14:
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997425000010/skyt-20241229.htm>
  - FY2025 Form 10-K, filed 2026-03-11:
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997426000009/skyt-20251228.htm>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** Context for H1, H5 and H6; the segment split in `LN-7` is what actually bears on H6.
- **How it was counted:** Each 10-K was fetched with `curl` using an ordinary browser user-agent
  (`data.sec.gov` and `www.sec.gov/Archives` both return a "Your Request Originates from an
  Undeclared Automated Tool" interstitial to a plain scripted user-agent; a browser user-agent plus
  the usual `Sec-Fetch-*` headers is served normally), converted to text with a local script, and
  the head-count sentence and the revenue line read directly. Revenue is the "Total revenue" line of
  the consolidated statements of operations, in thousands as printed.
- **What it says:**

  The head-count sentence is formulaic and appears once per filing under "Human Capital Resources":

  > "As of January 2, 2022, we had 590 employees. All employees reside in the United States of America."

  > "As of January 1, 2023, we had 706 employees. All employees reside in the United States of America."

  > "As of December 31, 2023, we had 731 employees. All employees reside in the United States of America."

  > "As of December 29, 2024, we had 702 employees. All employees reside in the United States of America."

  > "As of December 28, 2025, we had 1,551 employees. All employees reside in the United States of America."

  | Fiscal year end | Employees | Total revenue | Capital expenditure |
  |---|---:|---:|---:|
  | (FY2020) | not stated in these filings | $140,438,000 | $89,900,000 |
  | 2022-01-02 (FY2021) | 590 | $162,848,000 | $32,000,000 |
  | 2023-01-01 (FY2022) | 706 | $212,941,000 | $18,600,000 |
  | 2023-12-31 (FY2023) | 731 | $286,682,000 | $12,800,000 |
  | 2024-12-29 (FY2024) | 702 | $342,269,000 | $14,300,000 |
  | 2025-12-28 (FY2025) | 1,551 | $442,139,000 | $27,200,000 |

  The properties, from Item 2 of the FY2025 10-K:

  > "Our corporate headquarters and a fabrication facility are located in Bloomington, Minnesota, a 356,000 square foot facility."

  > "We utilize the 109,000 square foot facility, with approximately 36,000 square feet of cleanroom space, to address emerging commercial and government agency needs for U.S.-sourced electronics."

  > "This facility is approximately 1,223,000 square feet in size, with approximately 375,000 of the square footage being specific to cleanroom space."

  Who the customers are, from Item 1:

  > "We serve a diverse array of customers ranging from designers producing near-commodity volume chips to those requiring highly specialized next-generation technology solutions. Infineon accounted for 43% and 7% of our revenue for fiscal years ended December 28, 2025 and December 29, 2024, respectively. Two customers, other than Infineon, represented 21% and 10% of our revenue for the fiscal year ended December 28, 2025."

  And the company's own statement of why it exists, which is the long-tail argument in a foundry's
  own risk factor:

  > "As a result of our smaller manufacturing footprint, we target opportunities that larger competitors are unable to fulfill efficiently. These contracts are typically lower volume but require higher levels of customization and engineering expertise."

  The FY2021 10-K states the same positioning positively:

  > "Expertise in highly customized projects in a low-volume research and development environment ."

- **DERIVED (arithmetic written out):**
  - **Revenue per employee.** FY2021: $162,848,000 ÷ 590 = **$276,014**. FY2022:
    $212,941,000 ÷ 706 = **$301,616**. FY2023: $286,682,000 ÷ 731 = **$392,178**. FY2024:
    $342,269,000 ÷ 702 = **$487,563**. FY2025 blended: $442,139,000 ÷ 1,551 = **$285,067** — but
    FY2025 mixes half a year of a much larger fab, so the blended figure is not comparable; see
    `LN-7`.
  - **Capital intensity over five years.** Capex FY2021–FY2025 totals
    32.0 + 18.6 + 12.8 + 14.3 + 27.2 = **$104,900,000**, against FY2025 revenue of $442,139,000 —
    i.e. the whole five-year capital programme of an operating US specialty foundry is about
    **0.24× one year's revenue**. Capex as a share of revenue fell from 19.7% (FY2021,
    32.0 ÷ 162.848) to 4.2% (FY2024, 14.3 ÷ 342.269) before the Texas year.
  - **Customer concentration.** FY2025: 43% + 21% + 10% = **74% of revenue in three customers**, up
    from 40% + 20% = **60% in two** in FY2024. This is CONC-shaped evidence from a *small* foundry,
    not a leading-edge one — see the caveat.
- **Caveats:** The head-count figures are total employees, not fab operators, and include corporate
  staff at three sites. The FY2025 jump from 702 to 1,551 is almost entirely the Fab 25 acquisition
  (`LN-3`), not organic hiring. Capex figures are the MD&A "we spent approximately" line, which
  includes software; the cash-flow-statement "Purchases of property and equipment" line differs
  slightly (FY2021 $30,762,000 against the MD&A's $32.0 million). SkyWater is a *specialty*
  foundry, not an open-entry shuttle service — its customers are mostly funded programmes and
  established fabless firms, not the long tail this project is about. It does host the SKY130 open
  PDK, which is why it is here at all.

### LN-2. $56 million of capital was expected to raise a 200 mm fab's output "by at least 40%"

- **Source:** SkyWater Technology, Inc., FY2021 Form 10-K, filed 2022-03-10, "Capital Expenditures"
  in Item 7 and Note 1.
  <https://www.sec.gov/Archives/edgar/data/1819974/000181997422000013/skyt-20220102.htm>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** Context for H1; mildly **Supports** the project's premise that mature-node capacity is
  cheap to add relative to leading-edge capacity.
- **What it says:**

  > "On July 26, 2021, we announced that our board of directors approved $56 million in strategic capital investments for expanding manufacturing capacity and technology capabilities at our Minnesota facility. The majority of this investment is targeted to expand capacity and capabilities at our Minnesota fab which is expected to increase overall output by at least 40% and to enable accelerated revenue growth. The remainder is focused on expediting our entry into the gallium nitride, or GaN, market, a promising technology for electric vehicles, 5G and consumer electronics, among others due to its properties that enable higher charging efficiencies, smaller ship size, and lighter weight for many applications."

  The same programme is described in Note 1 with the first-year spend attached:

  > "The strategic capital investment is a multi-year strategy and we invested approximately $ 13,800 during the year ended January 2, 2022."

  (Note 1 is stated in thousands, so $13,800 thousand = $13,800,000.)

- **DERIVED (arithmetic written out):**
  - **Capital cost per unit of incremental capacity — now computable.** The same FY2021 10-K states
    the fab's capacity (`LN-18`): *"Our fab's throughput capacity is up to 156,000 wafers per year
    (device mix dependent)."* 156,000 ÷ 12 = **13,000 wafer starts per month**. A 40% increase is
    13,000 × 0.40 = **5,200 wspm**, or 156,000 × 0.40 = **62,400 wafers a year**. Therefore:
    - $56,000,000 ÷ 5,200 wspm = **$10,769.23 per wafer-start-per-month**.
    - $56,000,000 ÷ 62,400 = **$897.44 of capital per wafer of annual capacity**.
    Against Polar's $26,250/wspm for doubling a neighbouring fab (`LN-11`), debottlenecking is
    **2.4× cheaper** per unit of capacity than a doubling (26,250 ÷ 10,769 = 2.44); against the
    $2,110/wspm mean for *buying* a fab (§ "Capital per wafer start" below) it is **5.1× dearer**.
  - **Upper bound on the whole-fab cost, for scale.** $56,000,000 ÷ 0.40 = **$140,000,000 per 100%
    of this fab's output**. Against the $10bn–$20bn a leading-edge fab now costs, that is the whole
    mature-node argument in one line.
  - **It did raise output.** Revenue went $162,848,000 (FY2021) → $212,941,000 (FY2022) →
    $286,682,000 (FY2023), i.e. **+76.0% over two years** (286,682 ÷ 162,848 = 1.760), against a
    promised "at least 40%" output increase. Revenue is not output, and price and mix moved too.
- **Caveats:** "Output" is undefined in the filing and is not explicitly wafer starts — the 40% is
  converted above by applying it to the throughput figure printed elsewhere in the same document,
  which is an assumption, not a statement. The $56,000,000 covers both capacity *and* a GaN
  technology entry, and the filing does not split them, so the true capacity spend is below
  $56,000,000 and **$10,769/wspm is therefore an upper bound**. The whole-fab bound is a bound, not
  a measurement.

### LN-3. A working 200 mm fab with ~1,000 employees and 400,000 wafer starts a year cost $86.5 million of net cash — $86,500 of capital per job

- **Source:** SkyWater Technology, Inc., FY2025 Form 10-K, filed 2026-03-11, Note 3 (Business
  Combination) and Item 1.
  <https://www.sec.gov/Archives/edgar/data/1819974/000181997426000009/skyt-20251228.htm>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Supports** H1's mature-node half and the project's premise that a fab of useful
  size is within reach of ordinary capital — with the large caveat that this was a *used* fab.
- **What it says:**

  > "On June 30, 2025, the Company completed the acquisition of all of the issued and outstanding membership interests of Spansion Fab 25, LLC (“Fab 25”) a newly formed limited liability company that received, pursuant to a pre-closing restructuring, substantially all of the property, plant and equipment, employees and certain other assets and liabilities related to Infineon Technologies AG’s (“Infineon”) 200 mm fab in Austin, Texas (the “Transaction”)"

  > "The total purchase consideration exchanged on the Transaction was $206.5 million , consisting of the $120.0 million fair value of the off-market component of the Supply Agreement and net cash payments of $86.5 million ."

  > "Net cash paid consisted of the base purchase price of $73.0 million paid at closing, plus $19.9 million paid at closing for estimated"

  > "We funded the net cash purchase price for the Transaction of approximately $86.5 million with net borrowings under our Loan Agreement (as defined below), which materially increased our indebtedness."

  What was bought:

  > "SkyWater Texas is a high-volume manufacturer that provides Wafer Services product offerings focused on 200 mm semiconductor fabrication, copper processing, high-voltage technology services and 65 nm node infrastructure support. This facility is approximately 1,223,000 square feet in size, with approximately 375,000 of the square footage being specific to cleanroom space."

  And SkyWater booked a gain for buying it below fair value:

  > "The excess of the estimated fair value of assets acquired and liabilities assumed over the estimated fair value of the total purchase consideration exchanged was recognized as a bargain purchase gain pursuant to Topic 805 in the amount of $ 111,746 ."

  ($111,746 thousand = $111,746,000.)

  **CORRECTION, added 2026-09-25 on a second pass.** The head count and the capacity are both
  published, in SkyWater's own completion press release of 2025-06-30, which was not read when this
  entry was first written:

  > "By adding approximately 400,000 wafer starts per year in capacity, Fab 25 brings meaningful scale to SkyWater's exclusively U.S.-based, pure-play foundry operation"

  > "Approximately 1,000 Fab 25 employees have now joined SkyWater."

  > "SkyWater’s acquisition of Fab 25 consists of a $73 million payment at close plus an additional approximately $20 million payment at close for working capital"

  (<https://www.skywatertechnology.com/skywater-completes-acquisition-of-fab-25/>, verified
  2026-09-25.) **The 849 originally derived here was an undercount; use 1,000.** Every figure below
  has been recomputed on 1,000, and the superseded 849-based figures are shown struck through in
  words so the correction is traceable.

- **DERIVED (arithmetic written out):**
  - **Head count acquired: ~1,000, stated by the buyer.** The derivation that produced 849
    (1,551 at 2025-12-28 minus 702 at 2024-12-29) was an inference that assumed Legacy SkyWater head
    count was flat; it was not — SkyWater ran "workforce reorganizations" in the same year, so
    Legacy shrank and the difference understated the acquisition. **The figures previously published
    in this entry on a base of 849 — $101,884, $85,983 and $243,187 per job — are superseded.**
  - **Capital cost per job (on ~1,000).**
    - Net cash: $86,500,000 ÷ 1,000 = **$86,500 per job**.
    - Base purchase price only: $73,000,000 ÷ 1,000 = **$73,000 per job**.
    - Total accounting consideration: $206,466,000 ÷ 1,000 = **$206,466 per job**.
  - **Capital cost per unit of capacity.** 400,000 wafer starts a year ÷ 12 = **33,333 wafer starts
    per month**.
    - $86,500,000 ÷ 33,333 wspm = **$2,595.03 per wafer-start-per-month**.
    - $86,500,000 ÷ 400,000 = **$216.25 of capital per wafer of annual capacity**.
  - **Capital cost per square foot.**
    - Net cash per square foot of cleanroom, on SkyWater's 375,000: $86,500,000 ÷ 375,000 =
      **$230.67/sq ft**. On Spansion's own long-standing 114,000 (see caveats):
      $86,500,000 ÷ 114,000 = **$758.77/sq ft**.
    - Net cash per square foot of building: $86,500,000 ÷ 1,223,000 = **$70.73/sq ft**.
  - **Against the seller's book value.** The abbreviated financial statements of the Fab 25 business
    filed as Exhibit 99.2 to SkyWater's Form 8-K of 2025-11-05 show **property, plant and equipment
    of $148,019 thousand** at 2025-06-30 (and $154,658 thousand a year earlier)
    (<https://www.sec.gov/Archives/edgar/data/1819974/000181997425000037/skyt-20250912xex9902.htm>,
    verified 2026-09-25). SkyWater paid $86,500,000 of cash for PP&E carried at **$148,019,000** —
    **58.4%** of the seller's own book value (86,500 ÷ 148,019).
  - **Against fair value.** The bargain purchase gain of $111,746,000 on $206,466,000 of
    consideration means the assets were appraised at 206,466 + 111,746 = **$318,212,000**, so
    SkyWater paid **64.9%** of appraised fair value (206,466 ÷ 318,212), or **27.2%** of it in cash
    (86,500 ÷ 318,212).
  - **Revenue per employee, and revenue per wafer.** Six months of SkyWater Texas revenue was
    $175,292,000 (`LN-7`), so annualised $350,584,000: ÷ 1,000 employees = **$350,584 per
    employee**, and ÷ 400,000 wafers of capacity = **$876.46 of revenue per wafer of capacity** (at
    whatever utilisation ran in those six months, so this is a lower bound on price per wafer
    shipped). The purchase price was **0.25 years of that fab's revenue** (86,500 ÷ 350,584).
- **Caveats:** **This is not the cost of building a fab.** It is the cost of buying one that
  already exists from an owner who wanted to exit, and the accountants said so by recognising a
  bargain purchase gain. The $120,000,000 "off-market component of the Supply Agreement" means part
  of the price was paid in the form of a below-market four-year take-or-pay to the seller — i.e.
  Infineon sold cheap and bought wafers cheap. The filing gives the reason explicitly: "the bargain
  purchase gain resulted from Infineon's strategic decision to divest Fab 25 in exchange for the
  favorable wafer production pricing included in the Supply Agreement and its ability to maintain
  security of supply for semiconductors used in its products from a trusted partner." A greenfield
  200 mm fab is a $1bn-scale project; none of these numbers say otherwise.

  **The cleanroom area is disputed between two filings and both are quoted above.** SkyWater's
  FY2025 10-K says "approximately 375,000 of the square footage being specific to cleanroom space".
  Spansion's FY2014 Form 10-K, written by the people who ran the fab, says: *"We own and operate one
  wafer fabrication facility, Fab 25, which is located in Austin, Texas and has approximately
  114,000 square feet of clean room space."*
  (<https://www.sec.gov/Archives/edgar/data/1322705/000143774915002287/code20141231_10k.htm>,
  verified 2026-09-25.) The two differ by **3.3×**. The most likely reconciliation is that
  SkyWater's figure counts sub-fab, chase and support space and Spansion's counts only classed
  production cleanroom, but neither filing says so. **Any per-square-foot-of-cleanroom comparison in
  this file that uses Fab 25 should be read with that 3.3× uncertainty attached**, and the
  per-square-foot-of-*building* and per-wafer-start figures preferred, since those are unambiguous.

### LN-4. The CHIPS money attached to a small fab: up to $16 million federal plus $19 million from Minnesota's Forward Fund, and a $10.23 million refundable tax credit

- **Source:** SkyWater Technology, Inc., FY2025 Form 10-K, filed 2026-03-11, Item 1A and Note 1.
  <https://www.sec.gov/Archives/edgar/data/1819974/000181997426000009/skyt-20251228.htm>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** Context for H1 and H6 — it sizes the public subsidy available to a *small* US fab
  against the private capital it has to raise anyway.
- **What it says:**

  > "In December 2023, we submitted an application for CHIPS and Science Act funding for modernization and equipment upgrades to enhance production at our Minnesota fab. In December 2024, we signed a preliminary memorandum of terms that provides for up to $16 million in funding pursuant to the CHIPS and Science Act, which will be combined with $19 million in incentives from the State of Minnesota’s Forward Fund. However, there is no guarantee that we will receive any such CHIPS and Science Act funding pursuant to the preliminary memorandum of terms or otherwise"

  Separately, the Section 48D refundable investment tax credit:

  > "The Company receives government assistance in the form of refundable investment tax credits available under Section 48D of the Creating Helpful Incentives to Produce Semiconductors for America Act of 2022 (“CHIPS Act”) for eligible capital expenditures. Upon completing all necessary registrations, the Company has a recognized income tax receivable of $ 10,230 for eligible capital expenditures arising from its 2023, 2024 and 2025 tax years as of December 28, 2025."

  > "For the fiscal years ended December 28, 2025, and December 29, 2024, $ 967 and $ 449 of deferred gain was recognized as a reduction of depreciation expense in cost of revenues"

  And the rate change:

  > "changes increasing the Section 48D refundable tax credit for semiconductor manufacturing facilities from 25% to 35% for property placed in service after 2025"

- **DERIVED (arithmetic written out):**
  - **Eligible capital implied by the credit.** $10,230,000 at the 25% rate implies
    10,230,000 ÷ 0.25 = **$40,920,000 of eligible capital expenditure** across tax years 2023, 2024
    and 2025. Total reported capex over fiscal 2023–2025 was 12.8 + 14.3 + 27.2 =
    **$54,300,000**, so **75.4%** of the capital programme qualified (40.92 ÷ 54.3). Tax years and
    fiscal years are not identical, so this is approximate.
  - **Subsidy against private capital.** $16,000,000 + $19,000,000 = **$35,000,000** of announced
    grant money, against $86,500,000 of cash and $206,466,000 of total consideration spent on one
    acquisition in the same period, and $104,900,000 of five-year organic capex. Grants are
    **25.0%** of the five-year organic capex (35 ÷ 104.9) and **16.9%** of the acquisition
    consideration.
  - **Subsidy per job.** If the $35,000,000 is read against SkyWater's whole 1,551-person workforce:
    35,000,000 ÷ 1,551 = **$22,566 per existing job**. No job-creation target is disclosed in the
    filing, so a per-*new*-job figure cannot be computed from this source.
- **Caveats:** A preliminary memorandum of terms is not an award; the filing says so twice. The
  Minnesota Forward Fund figure of $19,000,000 is SkyWater's characterisation and was not verified
  against a Minnesota DEED document (see "What I could not get"). The 48D receivable is a credit
  against eligible equipment already bought, not new money for new capacity.

### LN-5. Osceola County, Florida gave SkyWater a fab to operate for free — and SkyWater owes a 20% match of about $10.23 million

- **Source:** SkyWater Technology, Inc., FY2025 Form 10-K, filed 2026-03-11, Note 13 (Commitments
  and Contingencies), and Item 1A.
  <https://www.sec.gov/Archives/edgar/data/1819974/000181997426000009/skyt-20251228.htm>
  The underlying agreement is Exhibit 10.13, "Technology and Economic Development Agreement, dated
  January 25, 2021, by and between Osceola County, Florida and SkyWater Florida, Inc., and joined
  for limited purposes by ICAMR, Inc.", filed with the Form S-1 of 2021-03-22.
- **Verification:** Verified for the 10-K text quoted; **Partial** for the underlying county
  numbers, which are not in the filing (see "What I could not get").
- **Date checked:** 2026-09-25
- **Bearing:** **Context** for H6, and a direct **Challenge** to any claim that a small fab's
  economics can be read off its own accounts: the building, its cleanroom and its wastewater plant
  were paid for by a county and a water authority, and never appear as SkyWater capital at all.
- **What it says:**

  > "On January 25, 2021, the Company entered into a technology and economic development agreement (the “TED Agreement”), and a lease agreement (the “CfN Lease”) with the government of Osceola County, Florida (“Osceola”) and ICAMR, Inc., a Florida non-profit corporation doing business as BRIDG (“BRIDG”), to lease and operate the Center for NeoVation (the “CfN”), a semiconductor research and development and manufacturing facility in Kissimmee, Florida. Under the CfN Lease, the Company agrees to bring the plant to full production capacity within five years , and then to operate the plant at full capacity for an additional 15 years. At the end of the lease, SkyWater will take ownership of the facility. The Company is responsible for taxes, utilities, insurance, maintenance, operation of the assets, and making capital investments in the facility to bring the facility to its full production capacity. Investments and costs required to bring the facility to its full capacity will be substantial. The Company may terminate the TED Agreement and CfN Lease with 18 months’ notice. In the event the Company terminates the agreements, it is required to continue to operate the CfN until the earlier of either a replacement operator is found, or the 18 months’ notice period expires, and it may be required to make a payment of up to $ 15,000 to Osceola upon termination."

  (Note 13 is in thousands: the termination payment is up to **$15,000,000**.)

  The wastewater plant was paid for by the water authority:

  > "the advanced wastewater treatment facility (“AWT Facility”), a separate building located on the same leased premise as the CfN and subject to the CfN Lease. The AWT Facility was financed in substantial part by funds provided by the Tohopekaliga Water Authority (“TWA”) to house the acid waste neutralization, pH adjustment, and reverse osmosis water treatment systems."

  > "As of December 28, 2025, the Company expects future payments on these commitments of approximately $ 3,600 which the Company expects will be paid in full by the first quarter of 2028."

  And the federal money went to the *county*, not to SkyWater:

  > "In the third quarter of 2022, the U.S. Department of Commerce Economic Development Administration granted funds to Osceola and BRIDG for continued development of Central Florida’s Semiconductor Cluster for Broad-Based Prosperity through the Build Back Better Regional Challenge, a portion of which is committed to the expansion of the CfN and purchase, installation, and qualification of equipment in the CfN. In February 2023, the Company committed to Osceola a 20 % matching share contribution of the project costs, including any project overages, which was estimated as a total commitment of approximately $ 10,230 as of December 28, 2025. The Company’s commitment to fund this matching contribution is limited to $ 1,000 in any single calendar quarter. Of this total commitment, and as of December 28, 2025, the Company has paid a total of $ 2,000 and has an unpaid obligation accrued of $ 4,900"

  The facility itself:

  > "We utilize the 109,000 square foot facility, with approximately 36,000 square feet of cleanroom space, to address emerging commercial and government agency needs for U.S.-sourced electronics. We also lease office space adjacent to the Center for NeoVation in Kissimmee, Florida, which consists of approximately 6,000 square feet and our agreement for such office space expires in January 2039."

- **DERIVED (arithmetic written out):**
  - **Implied size of the federal grant portion.** A 20% match of $10,230,000 implies a project of
    10,230,000 ÷ 0.20 = **$51,150,000** total, of which the non-SkyWater 80% is
    51,150,000 − 10,230,000 = **$40,920,000**. (Coincidentally the same figure as the 48D-implied
    capex in `LN-4`; they are unrelated.)
  - **Cleanroom share.** 36,000 ÷ 109,000 = **33.0%** of the Kissimmee building is cleanroom,
    against 375,000 ÷ 1,223,000 = **30.7%** at Fab 25. Two independent US fabs land within
    2.3 points of each other, which is a usable planning ratio.
  - **What the county's capital is worth to SkyWater.** SkyWater pays no purchase price for a
    109,000 sq ft building with 36,000 sq ft of cleanroom and an advanced wastewater plant, and
    takes ownership at the end of a 20-year lease. Applying the Fab 25 cleanroom rate from `LN-3`
    ($230.67/sq ft of cleanroom, itself a distressed-sale number), 36,000 × 230.67 =
    **$8,304,120** — which is plainly far too low for a purpose-built 200 mm advanced-packaging
    line, and is the best evidence available here that the Fab 25 price was exceptional rather than
    typical.
- **Caveats:** The county's own outlay is not in this filing. Osceola County and the State of
  Florida built the facility as ICAMR/BRIDG from about 2015 and the reported public cost runs into
  the low hundreds of millions; **that number is not verified here** and must not be quoted from
  this entry. The "$15,000" termination payment and "$1,000 in any single calendar quarter" are
  thousands, per the note's header.

### LN-6. SkyWater no longer exists as an independent company — IonQ bought it on 2026-07-31

- **Sources:**
  - SkyWater Technology, Inc., Form 8-K filed 2026-01-26 (event 2026-01-25), Item 1.01:
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312526022750/d32015d8k.htm>
  - SkyWater Technology, LLC, Form 8-K filed 2026-07-31 (event 2026-07-31), Items 1.02, 2.01, 3.01:
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312526327137/d49031d8k.htm>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Supports** H2 and H1. A specialty foundry serving many small, high-mix customers
  could not stand alone; it ended as a captive fab inside a customer.
- **What it says:**

  From the January announcement:

  > "On January 25, 2026, SkyWater Technology, Inc., a Delaware corporation (the “Company” or “SkyWater”), entered into an Agreement and Plan of Merger (the “Merger Agreement”) with IonQ, Inc., a Delaware corporation (“Parent” or “IonQ”)"

  > "will be converted into the right to receive (i) $15.00 in cash (the “Per Share Cash Consideration”) plus (ii) a number of shares of Parent common stock"

  > "The “Exchange Ratio” means the quotient obtained by dividing (i) $20.00 by (ii) the volume weighted average price of the Parent Shares for the 20 full consecutive trading days prior to, but not including, the third business day before the closing date of the Mergers"

  From the closing 8-K:

  > "On July 31, 2026 (the “Closing Date”), pursuant to the Merger Agreement, (i) Merger Subsidiary 1 merged with and into the Company, with the Company surviving as a wholly-owned subsidiary of Parent (the “First Merger”), and (ii) immediately following the effective time of the First Merger (the “Effective Time”), the Company, as the surviving entity of the First Merger, merged with and into Merger Subsidiary 2 (the “Surviving Company”), which survived the merger as a wholly-owned subsidiary of Parent under the name SkyWater Technology, LLC"

  > "automatically converted into the right to receive (i) $15.00 in cash (the “Per Share Cash Consideration”) and (ii) 0.4883 shares of the common stock of IonQ, par value $0.0001 per share"

  > "On the Closing Date, the Company notified the Nasdaq Capital Market (“Nasdaq”) of the consummation of the Mergers and requested that Nasdaq file a notification of removal from listing and registration on Form 25"

- **DERIVED (arithmetic written out):**
  - **Headline per-share value.** $15.00 cash + $20.00 of stock (the exchange ratio is defined to
    deliver $20.00 of IonQ stock within a collar) = **$35.00 per SkyWater share** at announcement.
  - **Implied per-job value of the whole company.** SkyWater had 1,551 employees. The 8-K does not
    state an equity value, and the share count is not quoted here, so a per-job figure is *not*
    computed. See "What I could not get".
  - **The practical consequence for this project.** After 2026-07-31 there is no further SkyWater 10-K, no
    further head-count sentence and no further segment disclosure for this US pure-play specialty
    foundry. `LN-1` and `LN-7` are the end of that series.
- **Caveats:** The exchange ratio was collared: "if the Parent Trading Price is greater than or
  equal to $60.13, then the Exchange Ratio shall be equal to 0.3326 shares … or (ii) if the Parent
  Trading Price is less than or equal to $37.99, then the Exchange Ratio shall be equal to 0.5265
  shares." The realised 0.4883 is inside the collar. IonQ is a quantum-computing company, so the
  strategic logic is captive supply, not foundry consolidation.

### LN-7. The high-mix segment loses money; the anchor-customer segment makes money — in the same company, in the same year

- **Source:** SkyWater Technology, Inc., FY2025 Form 10-K, filed 2026-03-11, Note 18 (Segment
  Information).
  <https://www.sec.gov/Archives/edgar/data/1819974/000181997426000009/skyt-20251228.htm>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Challenges** H6, hard. Also **Challenges** the "small customers pay for the
  capital" reading of H5.
- **What it says:**

  The two segments are defined as:

  > "Legacy SkyWater: A pure-play technology foundry that offers advanced semiconductor development and manufacturing services from its fabrication facility in Bloomington, Minnesota and advanced packaging services from its Kissimmee Florida facility. Legacy SkyWater provides ATS and Wafer Services product offerings."

  > "SkyWater Texas is a high-volume manufacturer that provides Wafer Services product offerings focused on 200 mm semiconductor fabrication, copper processing, high-voltage technology services and 65 nm node infrastructure support."

  The segment table, as printed (in thousands), fiscal year ended 2025-12-28:

  | Line | Legacy SkyWater | SkyWater Texas | Total FY2025 | Total FY2024 |
  |---|---:|---:|---:|---:|
  | Revenue | 266,847 | 175,292 | 442,139 | 342,269 |
  | Cost of revenue — labor | 79,978 | 53,005 | 132,983 | 79,430 |
  | Cost of revenue — direct expenses | 93,503 | 64,252 | 157,755 | 102,597 |
  | Cost of tool revenue | 30,655 | — | 30,655 | 73,281 |
  | Cost of revenue — depreciation and amortization | 15,815 | 18,003 | 33,818 | 17,335 |
  | **Total cost of revenue** | 219,951 | 135,260 | 355,211 | 272,643 |
  | **Gross profit** | 46,896 | 40,032 | 86,928 | 69,626 |
  | Research and development expense | 14,621 | — | 14,621 | 15,040 |
  | Total selling, general and administrative expense | 66,771 | 8,112 | 74,883 | 48,026 |
  | **Operating income (loss)** | **(34,496)** | **31,920** | (2,576) | 6,560 |
  | Bargain purchase gain | — | 111,746 | 111,746 | — |
  | Interest expense | (13,713) | — | (13,713) | (8,837) |
  | **Net income (loss)** | **(14,268)** | **137,714** | 123,446 | (2,517) |

  Total assets by segment: Legacy SkyWater $518,540 thousand, SkyWater Texas $215,367 thousand.

- **DERIVED (arithmetic written out):**
  - **Gross margin.** Legacy: 46,896 ÷ 266,847 = **17.57%**. Texas: 40,032 ÷ 175,292 = **22.84%**.
  - **Operating margin.** Legacy: −34,496 ÷ 266,847 = **−12.93%**. Texas:
    31,920 ÷ 175,292 = **+18.21%**.
  - **The gap is mostly SG&A, and that is the point.** Legacy SG&A is
    66,771 ÷ 266,847 = **25.02%** of revenue; Texas SG&A is 8,112 ÷ 175,292 = **4.63%**. A high-mix
    foundry selling to many customers spends five times as much of each revenue dollar on selling
    and administering as a fab selling almost all its output to one customer on a take-or-pay. That
    is the cost-to-serve that H6 assumes away.
  - **R&D falls entirely on the high-mix segment.** $14,621,000 against $0 — 5.48% of Legacy
    revenue.
  - **Labour intensity.** Legacy cost-of-revenue labour is 79,978 ÷ 266,847 = **29.97%** of
    revenue; Texas is 53,005 ÷ 175,292 = **30.24%**. Almost identical, so the difference between the
    two businesses is *not* direct fab labour — it is overhead and R&D.
  - **Return on segment assets.** Legacy: −34,496 ÷ 518,540 = **−6.65%**. Texas:
    31,920 ÷ 215,367 = **+14.82%** for six months.
  - **Whole-company reality check.** Excluding the one-off bargain purchase gain of $111,746,000,
    the consolidated FY2025 result is an operating loss of $2,576,000 on $442,139,000 of revenue
    (**−0.58%**), and consolidated FY2024 was an operating profit of $6,560,000 on $342,269,000
    (**+1.92%**). **In four of the five years covered by `LN-1` SkyWater did not make money.**
- **Caveats, stated at full strength because they matter:**
  - SkyWater Texas is **six months** (2025-06-30 to 2025-12-28), not a full year, and its first six
    months are the honeymoon of a take-or-pay contract.
  - Texas revenue includes the unwinding of the **$120,000,000 off-market component** of the
    Infineon supply agreement — revenue that is, in substance, part of the purchase price coming
    back as margin. The 10-K says the off-market component is "presented net of Supply Agreement
    specific contract assets which total $ 32,492 as of December 28, 2025". **The +18.21% Texas
    operating margin is therefore not a clean merchant-foundry margin and should not be quoted as
    one.**
  - **Corporate SG&A appears to sit entirely in the Legacy column.** Texas's $8,112,000 of SG&A on
    $175,292,000 of revenue is implausibly low for a standalone business, so some of Legacy's
    25.02% is group cost that a standalone Legacy would not carry in full.
  - Legacy's FY2025 also carries $30,655,000 of "cost of tool revenue" against a tool-revenue
    business that shrank sharply (FY2024: $73,281,000), and $2,108,000 of related-party consulting
    expense for brokering the Fab 25 deal.
  - Even after all of that: a −12.93% operating margin does not become positive under any of these
    adjustments, and the direction of the comparison — high-mix loses, anchor-customer wins — is
    the same one `PCB-11` and `IHF-8` found elsewhere in this directory.

### LN-8. X-FAB Lubbock: $200 million and "up to 250 additional jobs" — $800,000 of capital per job

- **Sources:**
  - Joshua Ramirez, "X-Fab announces $200 million expansion, creates 250 new jobs", KCBD NewsChannel
    11 (Lubbock, Texas), 2023-05-11.
    <https://www.kcbd.com/2023/05/12/x-fab-announces-200-million-expansion-creates-250-new-jobs/>
  - "X-FAB Texas Unveils Expansion in Lubbock, TX", Lubbock Economic Development Alliance, May 2023.
    <https://lubbockeda.org/x-fab-texas-announces-expansion-in-lubbock-tx/>
  - "X-Fab (Texas)", NIST CHIPS Program Office project page (preliminary memorandum of terms dated
    2024-12-06). <https://www.nist.gov/chips/x-fab-texas-lubbock>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Challenges** H5 and H6 on the capital side. $800,000 of capital per job is the cost
  of a job at a modern specialty fab, and no plausible number of $300 tape-outs pays for it.
- **What it says:**

  KCBD (the Lubbock CBS affiliate — this is the local-news version of the story):

  > "The $200 million expansion will help X-Fab keep pace with the demand for these lucrative semiconductors."

  > "This expansion will create up to 250 new jobs in Lubbock."

  > "The silicon-carbide market right now is forecasted to grow by roughly 35% per year over the next decade."

  The Lubbock Economic Development Alliance release:

  > "Phase one amounts to $200 million and is expected to create up to 250 additional jobs."

  > "X-FAB employs approx. 4,200 people worldwide."

  And, for scale on what a regional development body actually delivers:

  > "Since its inception in 2004, LEDA has assisted 249 companies with their expansion or relocation to Lubbock. These companies committed to creating 12,388 jobs and investing more than $2.2 billion in new capital improvements that have resulted in $2.0 billion in value-added impact to the Lubbock area."

  NIST, on the federal share:

  > "up to $50 million in proposed direct funding under the CHIPS and Science Act"

  > "The proposed CHIPS investment would create an estimated 150 jobs"

  NIST also describes the site as "the only high-volume SiC foundry in the U.S."

- **DERIVED (arithmetic written out):**
  - **Capital cost per job.** $200,000,000 ÷ 250 = **$800,000 per job**.
  - **Federal money per job.** $50,000,000 ÷ 150 = **$333,333 per job**, and the CHIPS share of the
    announced private investment is 50 ÷ 200 = **25.0%**.
  - **LEDA's whole twenty-year book, as a benchmark.** $2,200,000,000 ÷ 12,388 =
    **$177,591 of committed capital per committed job** across 249 companies in every industry. A
    semiconductor fab job costs **4.5×** the Lubbock average (800,000 ÷ 177,591).
- **Caveats:** "Up to 250" is a commitment, not a delivery, and KCBD's 250 and NIST's 150 are
  different counts on different bases (total expansion versus CHIPS-attributable). $200,000,000 is
  "phase one"; the company said further phases would follow "based on market demands". SiC is a
  capital-heavy specialty, not a general mature-node line.

### LN-9. NeoCity, Kissimmee: a $75 million purpose-built fab, ~$200 million of county money, and about 90 jobs — and the shared-access business model that "never materialized"

- **Sources:**
  - "Osceola County lands promising new business partner at high-tech hub NeoCity", Florida Trend,
    2022-03-09 (no byline shown).
    <https://www.floridatrend.com/article/33244/osceola-county-lands-promising-new-business-partner-at-high-tech-hub-neocity/>
  - Natalia Jaramillo, "NeoCity nabbed a half-billion in federal funds. But its impact on Osceola
    County is years away.", Orlando Sentinel, 2024-02-19 (read via the Yahoo Finance syndication).
    <https://finance.yahoo.com/news/neocity-nabbed-half-billion-federal-120000216.html>
  - "Soto Applauds U.S. Department of Defense 'Cornerstone' Award of $289 Million to Osceola
    County", Office of Rep. Darren Soto, 2023-11-21.
    <https://soto.house.gov/media/press-releases/soto-applauds-us-department-defense-cornerstone-award-289-million-osceola>
- **Verification:** Verified for the quoted text of all three; **Partial** for the "over $500
  million" total, which the Orlando Sentinel attributes to an interviewee rather than a document.
- **Date checked:** 2026-09-25
- **Bearing:** **Challenges** H5 directly. This is the closest thing in the record to somebody
  building a shared-access fab on the long-tail thesis and finding no tail.
- **What it says:**

  Florida Trend, on the original design of the thing — **this is the single most on-point sentence
  found in this whole pass**:

  > "Imec was to provide circuit design work and consult on the project’s centerpiece, a $75-million, 109,000-sq.-ft. wafer fabrication facility — a “fab” in industry parlance — on 20 acres. The plan called for UCF to run the clean-room facility and fund its operations."

  > "The project’s creators expected the fab to draw interest from private companies who’d pay membership fees to use its clean room and share in intellectual property developed there. But that interest never materialized, and by the time the chip-making facility opened in early 2017, the effort was rebranded as BRIDG (Bridging the Innovation Development Gap) — and had a new strategy based on securing military contracts."

  What the pivot to defence work then delivered, against the running cost:

  > "BRIDG succeeded in snagging a $20-million contract from the U.S. Department of Defense and a $7.5-million contract from the Air Force Research Laboratory. But the government work didn’t generate enough revenue to cover the facility’s $25-million annual operating costs. Meanwhile, state financial backing — $22.5 million as of 2020 — never reached the $25 million a year the initiative’s organizers had anticipated."

  > "BRIDG’s woes deepened during the pandemic. In 2020, Gov. Ron DeSantis vetoed $10 million in appropriations BRIDG had hoped to get. Shortly thereafter, UCF ended its contract with the organization and laid off more than two dozen BRIDG employees who’d been on its payroll"

  The county's own investment and the physical plant, from Florida Trend's fact box:

  > "Investment: $200 million from the county and local groups"

  > "Location: The master-planned district is on 500 acres near downtown Kissimmee."

  > "The Center for NeoVation — A 109,000-sq.-ft. semiconductor manufacturing facility operated by SkyWater Florida. The two-story building has 35,000 square feet of clean room space with additional laboratory/manufacturing space and has ultra-purified water and air systems as well as anti-vibration technology to guard against contamination and defects that could hamper wafer production."

  SkyWater's early spend and hiring at the site:

  > "Since inheriting the facility, SkyWater has spent nearly $1 million installing equipment and hiring employees, according to the public company’s financial reports. As of January, it had more than 30 employees at the site and was looking to hire nine more. It expects to create 220 jobs in Florida by 2026."

  And the precedent the same region set twenty years earlier:

  > "Between 1996 and 2003, Central Florida and state officials gave Agere Systems and its predecessors more than $40 million in incentives to expand a microchip plant in south Orange County, hoping to create an industry cluster with high-paying jobs. By 2002, however, Agere had followed industry trends and moved most of its chip production overseas."

  Two years later, the Orlando Sentinel counted the federal money and the people:

  > "Since late 2022, NeoCity — a collection of multiple, fledgling tech firms — has laid claim to an impressive half-billion dollars in federal funding."

  > "Beginning in mid-2022, NeoCity has received $50.8 million from the Biden administration’s American Rescue Plan, $120 million from the Department of Defense, $15 million from the National Science Foundation and more."

  > "Today, NeoCity overall employs roughly 90 people across its nearly 500-acre campus, Miller said."

  > "It’s created nearly 100 jobs and is on pace for 200+ within its first five years of operation."

  > "Osceola County residents can apply for the roughly 20 new positions SkyWater is hiring for this year, Miller said."

  > "In Osceola County, where the median household income is roughly $64,000, one of the lowest in Central Florida, work at NeoCity will be among the highest paying jobs you can get, Rasgon noted."

  The DoD award, from the congressional office:

  > "The county was awarded a five-year Cornerstone award with an initial funding allocation of $3.65 million and a spending ceiling of $120 million."

  > "Notably, the contract offers options for an additional $169 million, potentially resulting in a total award of $289 million."

  > "SkyWater will enter into an agreement for SkyWater to execute all aspects of the initial award of up to $120 million."

- **DERIVED (arithmetic written out):**
  - **What a purpose-built small fab costs per square foot, and how far that is from a used one.**
    $75,000,000 ÷ 109,000 sq ft = **$688.07 per square foot of building**;
    $75,000,000 ÷ 35,000 sq ft = **$2,142.86 per square foot of cleanroom**. Against `LN-3`'s
    distressed purchase of Fab 25 at $70.73 and $230.67 respectively, **building new cost 9.7× and
    9.3× as much per square foot as buying used** (688.07 ÷ 70.73 = 9.73;
    2,142.86 ÷ 230.67 = 9.29). Two ratios, computed independently, agreeing within 5%.
  - **County capital per job realised.** $200,000,000 ÷ ~90 people on the campus at 2024-02-19 =
    **about $2,222,222 of county and local money per job**, nine years after ICAMR was launched in
    2014. Against the 220 Florida jobs SkyWater said it expected by 2026:
    200,000,000 ÷ 220 = **$909,091 per planned job**.
  - **The shortfall that killed the original model.** BRIDG needed $25,000,000 a year. Its two
    named contracts, $20,000,000 and $7,500,000, total $27,500,000 — **but those are contract
    values, not annual revenue**, and the article says explicitly they "didn't generate enough
    revenue to cover" one year of operating cost. State backing was $22,500,000 *cumulative* to
    2020 against $25,000,000 *a year* hoped for: over the six years 2015–2020 that is a shortfall of
    about 6 × 25,000,000 − 22,500,000 = **$127,500,000**.
  - **Federal money per job at the campus.** $50,800,000 + $120,000,000 + $15,000,000 =
    $185,800,000 of named awards, against ~90 jobs = **$2,064,444 per job**; on the Sentinel's "over
    $500 million", 500,000,000 ÷ 90 = **$5,555,556 per job**. These are programme spends, much of
    it multi-year R&D rather than capital, and should be read as an upper bound on cost per job,
    not as capital intensity.
- **Caveats, and they matter:**
  - The $500,000,000 is *committed federal funding* across a 500-acre campus with several
    organisations on it, most of it R&D programme money and award *ceilings* (the DoD Cornerstone
    award had an "initial funding allocation of $3.65 million" against a "$120 million" ceiling and
    a $289,000,000 theoretical maximum). Dividing it by a head count is a rhetorical calculation,
    not a capital-intensity measurement, and is labelled as such above.
  - Florida Trend prints 35,000 sq ft of cleanroom; SkyWater's own 10-K (`LN-1`) prints
    "approximately 36,000 square feet". Use the filing.
  - The "$75-million" fab cost is Florida Trend's figure for the original ICAMR build and was not
    traced to a county document (see "What I could not get").
  - **The strongest part of this entry is the qualitative finding, not the arithmetic.** A
    public-private consortium built a small fab explicitly to sell shared cleanroom access to many
    companies on a membership model — precisely the demand this project assumes — and the interest
    "never materialized". That is the same failure mode as `IHF-8` (MEMSCAP) and `OPEN-7`
    (Efabless), at a third site, with a third funding model.

### LN-10. An operating 150 mm MEMS wafer fab, 120,000 sq ft on 57 acres, changed hands for $2.75 million

- **Sources:**
  - "Akoustis Receives Incentive Package Providing Up to $8 Million in Tax Credits Related to Its
    Planned Expansion into Upstate New York", Akoustis Technologies, Inc., 2017-03-31.
    <https://www.globenewswire.com/news-release/2017/03/31/947547/0/en/Akoustis-Receives-Incentive-Package-Providing-Up-to-8-Million-in-Tax-Credits-Related-to-Its-Planned-Expansion-into-Upstate-New-York.html>
  - "Akoustis Technologies Completes Strategic Acquisition of New York Wafer Manufacturing Facility
    and Operation", Akoustis Technologies, Inc., 2017-06-27.
    <https://www.globenewswire.com/news-release/2017/06/27/1029440/0/en/Akoustis-Technologies-Completes-Strategic-Acquisition-of-New-York-Wafer-Manufacturing-Facility-and-Operation.html>
  - "Akoustis Successfully Completes Sale of Assets to SpaceX", press release of 2025-05-15 filed as
    Exhibit 99.1 to the Form 8-K of ATECH (Parent) Resolution Corp. (formerly Akoustis
    Technologies, Inc.), CIK 0001584754.
    <https://www.sec.gov/Archives/edgar/data/1584754/000121390025044032/ea024225601ex99-1_atech.htm>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Supports** the project's premise on capital cost — this is the cheapest real fab in
  the record. **Challenges** it on viability: the buyer went bankrupt seven years later and the fab
  is now captive inside SpaceX.
- **What it says:**

  From the March 2017 incentive release:

  > "up to $8 million in performance-based incentives under the Excelsior Jobs Program"

  > "acquire a 120,000 Sq. Ft. Wafer Manufacturing Facility"

  > "57-acres of real estate associated with the facility"

  > "create 214 new jobs in Canandaigua, N.Y."

  > "retaining the 31 existing employees currently working in the STC-MEMS facility"

  > "invest up to $20 million in the project over the next 5 years"

  From the June 2017 closing release:

  > "Akoustis paid $2.75 million in cash at closing, plus conventional closing costs"

  > "Successfully Transitions 28 Employees - Expanding the Akoustis Team to 55 Employees"

  > "150-mm wafer fab business, including all semiconductor manufacturing tools"

  > "Class 100/Class 1000 cleanroom space"

  And how it ended, from the 8-K exhibit of 2025-05-15:

  > "Tune Holdings has acquired substantially all of Akoustis’s assets, with the exception of those owned by debtor Grinding and Dicing Services, Inc. (“GDSI”), for approximately $30.2 million in cash and the assumption of certain liabilities."

  > "Following completion of the Court-approved auction process on April 25, 2025, the Company selected Tune Holdings as the winning bidder for substantially all of its assets, except those owned by GDSI."

  > "We are pleased to close this strategic transaction, which will maximize value for our creditors and preserve the vast majority of our employees’ jobs,"

  Tune Holdings Corp. is described in the same release as "a wholly owned subsidiary of Space
  Exploration Technologies Corp. (“SpaceX”)".

- **DERIVED (arithmetic written out):**
  - **Purchase price per square foot.** $2,750,000 ÷ 120,000 sq ft = **$22.92 per square foot** of
    wafer-manufacturing building, tools included, on 57 acres. Against `LN-9`'s purpose-built
    $688.07/sq ft, that is **1/30th of the cost** (22.92 ÷ 688.07 = 3.3%).
  - **Purchase price per existing job.** $2,750,000 ÷ 28 transitioned employees = **$98,214**;
    ÷ 31 existing employees = **$88,710**.
  - **Planned capital per new job.** $20,000,000 ÷ 214 = **$93,458 per new job** — which includes
    "the initial real estate acquisition, construction and renovations, plant infrastructure
    enhancements, semiconductor manufacturing equipment purchases, employee training and software".
  - **Public money per new job.** $8,000,000 ÷ 214 = **$37,383**, and the state's incentive is
    8 ÷ 20 = **40.0%** of the private plan.
  - **What the same assets fetched eight years later.** $30,200,000 for substantially all assets
    against $2,750,000 for the fab in 2017 — but the 2025 figure includes eight years of tool
    investment, the BAW patent estate (reported as 40 US patents) and the RFMi subsidiary, so the
    two are not comparable as a return. What *is* comparable: a distressed, court-supervised
    auction of a US specialty fab business cleared at **$30.2 million**.
- **Caveats:** The March release says 31 existing employees and the June release says 28
  transitioned; both are quoted. Akoustis was an IDM building its own product, not a merchant
  foundry selling to a long tail, so the fab's *use* is not the project's model even though its
  *price* is the most relevant one here. The company filed Chapter 11 on 2024-12-16 following a
  circa-$59,000,000 trade-secret judgment in favour of Qorvo — the bankruptcy was caused by
  litigation, not by the fab economics, which is an important distinction and is why this entry does
  not treat the Chapter 11 as evidence against small-fab viability. The **pattern** it completes,
  though, is the same as `LN-6`: **two US specialty fabs in two years both ended up owned by a large
  customer** (IonQ; SpaceX).

### LN-11. Polar Semiconductor, Bloomington MN: $525 million for +20,000 wafer starts per month and 98 manufacturing jobs

- **Sources:**
  - Estelle Timar-Wilcox, "Minnesota semiconductor manufacturer awarded nearly $200 million in
    state, federal funding for expansion", MPR News, 2024-05-13.
    <https://www.mprnews.org/story/2024/05/13/minnesota-polar-semiconductor-manufacturer-millions-funding-expansion>
  - "Polar Semiconductor (Minnesota)", NIST CHIPS Program Office project page.
    <https://www.nist.gov/chips/polar-semiconductor-minnesota-bloomington>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Challenges** H5/H6 on capital cost per job — this is the most expensive job in the
  file. **Context** for capital cost per unit of capacity, where it gives the cleanest number
  anywhere in this directory.
- **What it says:**

  MPR News (Minnesota Public Radio — the local outlet):

  > "Polar Semiconductor in Bloomington plans to use $120 million in federal funding announced Monday to expand its facility, creating 160 new jobs and doubling its output of semiconductor chips."

  > "Bloomington’s Polar Semiconductor is beginning a $525 million expansion that it says will double its output and create 160 new jobs."

  > "Polar is getting another $75 million in state funding for the project, and has secured private funding as well."

  > "In Minnesota, semiconductor production is a fast-growing industry; the state’s more than 150 semiconductor manufacturers added nearly 2,000 jobs over the last two years."

  NIST, with the capacity and the job split:

  > "Up to $123 million in total direct funding under the CHIPS and Science Act"

  > "Investment of more than $525 million from private, state, and federal sources"

  > "from roughly 20,000 to roughly 40,000 wafer starts per month"

  > "Over 160 manufacturing and construction jobs in Minnesota"

  with "98 manufacturing jobs and 68 construction jobs", and an R&D condition:

  > "Committed to use commercially reasonable efforts to allocate 7% of its total U.S.-based revenue each year to R&D that is conducted in the United States for a period of 5 years"

- **DERIVED (arithmetic written out):**
  - **Capital cost per unit of capacity — the cleanest such figure found.** The expansion adds
    40,000 − 20,000 = 20,000 wafer starts per month.
    $525,000,000 ÷ 20,000 wspm = **$26,250 of capital per wafer-start-per-month**.
    Annualised: 20,000 × 12 = 240,000 added wafers a year, so
    $525,000,000 ÷ 240,000 = **$2,187.50 of capital per wafer of annual capacity**. Over a
    ten-year asset life that is **$218.75 of capital per wafer produced**, before any operating
    cost.
  - **Capital cost per job.** $525,000,000 ÷ 98 permanent manufacturing jobs = **$5,357,143 per
    job** — the highest in this file. Counting construction jobs too:
    $525,000,000 ÷ 160 = **$3,281,250**. Counting the 166 that 98 + 68 actually sums to:
    $525,000,000 ÷ 166 = **$3,162,651**.
  - **Public share.** $123,000,000 + $75,000,000 = $198,000,000, which is
    198 ÷ 525 = **37.71%** of the project. Per permanent job:
    $198,000,000 ÷ 98 = **$2,020,408 of public money per manufacturing job**.
  - **Against SkyWater next door.** Polar is expanding a 200 mm fab in the same town as SkyWater's
    Bloomington fab. SkyWater's entire five-year organic capex was $104,900,000 (`LN-1`); Polar's
    single expansion is **5.0×** that (525 ÷ 104.9).
- **Caveats:** MPR reports "up to $120 million" federal (the preliminary announcement); NIST's page
  says "up to $123 million" (the final award). Both are quoted. "160 new jobs" in the MPR headline
  conflates 98 permanent with 68 construction. The $525,000,000 is "from private, state, and
  federal sources", so it is a project total, not private capex. The capital-per-wspm figure is for
  *doubling an existing fab*, which is cheaper per unit than greenfield and more expensive than the
  debottlenecking in `LN-2`.

### LN-12. Rogue Valley Microdevices, Palm Bay FL: a pure-play MEMS foundry for $25 million and 75 jobs — and the public purse covers 40% of it

- **Sources:**
  - "EDC announces Oregon-based Rogue Valley Microdevices, Inc. to open microfabrication facility in
    Palm Bay", Economic Development Commission of Florida's Space Coast, 2023-06-28.
    <https://spacecoastedc.org/roguevalley/>
  - "Rogue Valley Microdevices (Florida)", NIST CHIPS Program Office project page (preliminary
    memorandum of terms dated 2024-07-01).
    <https://www.nist.gov/chips/rogue-valley-microdevices-florida-palm-bay>
- **Verification:** Verified for the two sources quoted; **Partial** for the $5,000,000 Florida
  Department of Commerce loan and $3,200,000 of "other incentives", which came from a search summary
  and were not read in a primary document.
- **Date checked:** 2026-09-25
- **Bearing:** **Mixed** on H6. This is the closest company in the file to foundry.api's own model —
  a pure-play MEMS foundry whose customers are small — and the numbers are within reach. But 40%
  of the capital is public.
- **What it says:**

  The Space Coast EDC (the local development commission):

  > "The company’s acquisition of a 50,000-square-foot commercial building at 2301 Commerce Drive in Palm Bay will result in a capital investment of $25 million."

  > "adding 30 jobs over 3 years with an average wage of $59,900, with anticipation of hiring 75 new employees over 5 years with an average wage of $65,267."

  > "The space will be reconfigured for a state-of-the-art cleanroom and office space, with initial production of its first MEMS devices slated for 2024."

  NIST:

  > "up to $6.7 million in proposed direct funding under the CHIPS and Science Act"

  > "creating over 75 jobs in the state of Florida"

  > "reliable, domestic supply of MEMS devices manufactured on 300mm wafers"

  and the investment is "estimated to nearly triple RVM's manufacturing capacity".

- **DERIVED (arithmetic written out):**
  - **Capital cost per job.** $25,000,000 ÷ 75 = **$333,333 per job** on the five-year plan;
    $25,000,000 ÷ 30 = **$833,333 per job** on the three-year plan.
  - **Capital cost per square foot.** $25,000,000 ÷ 50,000 sq ft = **$500 per square foot** of
    building, retrofitting an existing commercial shell. That sits between the used-fab prices
    ($22.92 and $70.73 per sq ft, `LN-10` and `LN-3`) and the purpose-built fab ($688.07,
    `LN-9`) — which is where a retrofit should sit, and is a useful confirmation that the three
    figures are measuring the same thing.
  - **Capital against payroll.** 75 jobs × $65,267 = **$4,895,025 of annual payroll**. The
    $25,000,000 of capital is therefore **5.11 years of the payroll it supports**
    (25,000,000 ÷ 4,895,025).
  - **Public share.** CHIPS $6,700,000 alone is 6.7 ÷ 25 = **26.8%** of the project. Adding the
    reported $3,200,000 of other grants: 9,900,000 ÷ 25,000,000 = **39.6%**. The reported
    $5,000,000 state loan is debt, not a grant, and is excluded from that fraction; including it,
    14,900,000 ÷ 25,000,000 = **59.6%** of the capital comes from the public sector in some form.
  - **Federal money per job.** $6,700,000 ÷ 75 = **$89,333**.
- **Caveats:** The wage figures are the EDC's incentive-application numbers, which are targets. A
  "capital investment of $25 million" in an EDC release usually means the total announced project
  value including the building purchase, not cleanroom tooling alone. "300 mm capable" for a MEMS
  foundry is a marketing claim about the largest wafer the tools can accept, not a statement of
  300 mm volume production. Rogue Valley's original fab is in Medford, Oregon; no comparable
  capital figure for the Medford site was found (see "What I could not get").

### LN-13. WestGate@Crane, Odon, Indiana: four small semiconductor companies, $277–300 million, and a capital-per-job spread of 7×

- **Sources:**
  - Alex Brown, "Ground broken on $84M semiconductor campus at WestGate", Inside INdiana Business,
    2022-11-21.
    <https://www.insideindianabusiness.com/articles/ground-broken-on-84m-semiconductor-campus-at-westgate>
  - "WestGate@Crane welcomes new $84 million collaborative microelectronics campus", Regional
    Opportunity Initiatives, 2022-11-21.
    <https://regionalopportunityinc.org/2022/11/21/microelectronics-campus/>
- **Verification:** Verified for the Inside INdiana Business figures; **Partial** for the Regional
  Opportunity Initiatives figures, which were read only through a search summary.
- **Date checked:** 2026-09-25
- **Bearing:** **Context** for H1 and H6. It is the only place found where four *different* small
  semiconductor companies announce capital and jobs on the same day at the same site, so the
  capital-per-job spread between them is measured under near-identical conditions.
- **What it says:**

  > "$84 million microelectronics campus at WestGate@Crane Technology Park"

  > "create nearly 550 jobs"

  > "invest more than $236 million to build and equip a 100,000-square-foot fabrication facility"

  > "create up to 413 jobs by the end of 2028"

  > "average salaries higher than 250% of the Daviess County average"

  The other three tenants:

  > "10,000-square-foot fabrication and R&D facility" and "create up to 35 high-wage jobs by the end of 2027" (Everspin Technologies)

  > "invest more than $34 million to lease and equip a 10,000-square-foot space" and "create up to 40 jobs by the end of 2027" (Trusted Semiconductor Solutions)

  > "invest $7.3 million to expand to Indiana" and "plans to add 61 jobs" (Reliable MicroSystems)

  The incentives:

  > "up to $11 million in conditional tax credits and training grants for NHanced Semiconductors"

  > "up to $10 million in redevelopment tax credits"

  > "up to $10 million in matching funds from the Indiana Regional Economic Acceleration and Development Initiative"

- **DERIVED (arithmetic written out):**
  - **Capital per job, four companies, one site, one day:**

    | Company | Announced capital | Jobs | Capital per job |
    |---|---:|---:|---:|
    | Reliable MicroSystems | $7,300,000 | 61 | **$119,672** |
    | NHanced Semiconductors | $236,000,000 | 413 | **$571,429** |
    | Trusted Semiconductor Solutions | $34,000,000 | 40 | **$850,000** |
    | Everspin Technologies | not stated | 35 | — |

    The spread between the cheapest and dearest is 850,000 ÷ 119,672 = **7.1×**, at the same site
    in the same week. **Capital cost per job is not a property of "a fab"** — it is a property of
    what the company is doing, and it varies by an order of magnitude.
  - **Capital per square foot.** NHanced: $236,000,000 ÷ 100,000 sq ft = **$2,360 per square
    foot** — the highest in this file, and 3.4× the purpose-built fab in `LN-9` ($688.07), because
    the money is advanced-packaging tooling rather than building. Trusted Semiconductor:
    $34,000,000 ÷ 10,000 = **$3,400 per square foot**, higher still, for a leased space.
  - **Public share of NHanced.** $11,000,000 + $10,000,000 = $21,000,000 of state tax credits
    against $236,000,000 = **8.9%** — much the lowest public share in this file. Per job:
    $21,000,000 ÷ 413 = **$50,847**.
  - **The campus shell.** $84,000,000 of campus against ~550 jobs = **$152,727 per job** for the
    buildings alone, before any tenant's tooling.
- **Caveats:** Every figure is an announcement with a target date (2027, 2028), not a delivery.
  "Up to" appears on every job number. Tax credits described as "conditional" and "performance-
  based" are only earned if the jobs appear. Advanced packaging is not wafer fabrication; NHanced's
  $2,360/sq ft should not be compared to a front-end fab's cost per square foot without that
  caveat. No follow-up reporting on whether these targets were met was found (see "What I could not
  get").

### LN-14. The capital-cost-per-job table, assembled

- **Sources:** every entry above; no new source.
- **Verification:** Verified — each row is arithmetic on figures verified in the entry cited.
- **Date checked:** 2026-09-25
- **Bearing:** **Mixed** on H5 and H6, and the most useful single thing in this file after `LN-7`.
- **How it was counted:** Each row divides the announced or paid capital by the announced or
  actual job count, exactly as computed in the cited entry. Rows are not adjusted to a common year;
  they span 2017 to 2025 in nominal dollars.
- **What it says:**

  | Site | What happened | Capital | Jobs | **Capital per job** | Entry |
  |---|---|---:|---:|---:|---|
  | Bloomington MN | **bought** an operating 200 mm fab from Cypress | $30,000,000 | 400 | **$75,000** | `LN-18` |
  | San Antonio TX | **bought** an operating 200 mm analog fab, paid in shares | $40,000,000 | ~500 | **$80,000** | `LN-17` |
  | Austin TX (Fab 25) | **bought** an operating 200 mm fab, net cash | $86,500,000 | ~1,000 | **$86,500** | `LN-3` |
  | Canandaigua NY | **bought** an operating 150 mm MEMS fab | $2,750,000 | 28 | **$98,214** | `LN-10` |
  | Odon IN (Reliable) | small expansion into a shared campus | $7,300,000 | 61 | **$119,672** | `LN-13` |
  | Odon IN (campus shell) | buildings only, four tenants | $84,000,000 | ~550 | **$152,727** | `LN-13` |
  | Palm Bay FL | **retrofitted** a commercial shell into a MEMS fab | $25,000,000 | 75 | **$333,333** | `LN-12` |
  | Odon IN (NHanced) | built out and tooled advanced packaging | $236,000,000 | 413 | **$571,429** | `LN-13` |
  | Lubbock TX | **expanded** an operating SiC fab | $200,000,000 | 250 | **$800,000** | `LN-8` |
  | Odon IN (Trusted) | leased and tooled a small space | $34,000,000 | 40 | **$850,000** | `LN-13` |
  | Kissimmee FL | **built** a new fab + campus (county money only) | $200,000,000 | ~90 realised | **$2,222,222** | `LN-9` |
  | Bloomington MN | **doubled** an operating 200 mm fab | $525,000,000 | 98 permanent | **$5,357,143** | `LN-11` |

  *(Updated 2026-09-25: Fab 25's head count corrected from the derived 849 to the ~1,000 SkyWater
  states in its own completion release, and Bloomington added from `LN-18`. The table now has
  eleven sites plus the Odon campus shell.)*

- **DERIVED (arithmetic written out):**
  - **The range is 71-fold**: 5,357,143 ÷ 75,000 = **71.4×** between the cheapest and dearest job
    in the table.
  - **The split is not by company size or by state. It is by verb.** The four rows under $100,000 a
    job are all *purchases of an existing fab from a seller who wanted out*. Everything that
    involves *building or tooling new capacity* is $119,000 a job or more, and the two rows over
    $2,000,000 a job are both *new capacity at a site that was already running*.
  - **Mean of the eight "build/expand" rows** (119,672 + 152,727 + 333,333 + 571,429 + 800,000 +
    850,000 + 2,222,222 + 5,357,143) ÷ 8 = 10,406,526 ÷ 8 = **$1,300,816 per job**. **Mean of the
    four "buy" rows** = (75,000 + 80,000 + 86,500 + 98,214) ÷ 4 = 339,714 ÷ 4 = **$84,929 per
    job**. The ratio is **15.3×** (1,300,816 ÷ 84,929).
  - **What this means for the project, stated plainly.** If foundry.api intends to *build*
    capacity, the planning number is on the order of **$0.1m–$5m of capital per job**, and the long
    tail has to pay for that. If it intends to *buy* a fab somebody else is exiting, the planning
    number is **about $85,000 per job** — and the four independent observations of that, spanning
    **2016 to 2025, four states and two wafer sizes**, fall in a 31% band ($75,000, $80,000,
    $86,500, $98,214). **That convergence is the most useful number in this file.**
  - **The same split shows up in capital per unit of capacity, and at a similar ratio.** Three
    "buy" transactions average **$2,110.43 per wafer-start-per-month** against **$18,509.62** for
    two "build/expand" projects — **8.77×**, against the 15.3× found on the per-job measure. The
    two measures bracket the answer at roughly an order of magnitude. See the section "Capital per
    wafer start, and how many customers it takes to pay for it" below for the full table and for
    what it means for customer counts.
- **Caveats:** Nominal dollars across 2017–2025; no inflation adjustment. Job counts mix realised
  head count (Canandaigua, Fab 25, Kissimmee) with announced targets (everywhere else), and targets
  are systematically optimistic, which pushes the announced rows' cost per job *down* relative to
  what will be realised. "Capital" mixes purchase price, capex commitments and project totals
  including public money. The two "buy" rows are both distressed or strategic exits and are not a
  market price for a fab; there is no liquid market for fabs.

### LN-15. The same company, two routes: $1.8 billion and 750 jobs announced in Indiana and cancelled, then $86.5 million and ~1,000 jobs bought in Texas

- **Sources:**
  - "Indiana's Economic Development Momentum Continues with State's First Microelectronics Fab,
    $1.8B Planned Investment from SkyWater Technology", Indiana Economic Development Corporation,
    2022-07-22.
    <https://www.iedc.in.gov/events/news/details/2022/07/22/indiana-s-economic-development-momentum-continues-with-state-s-first-microelectronics-fab-1.8b-planned-investment-from-skywater-technology>
  - Alex Brown, "Chip maker SkyWater cancels plans for Indiana plant—at least for now", Inside
    INdiana Business, 2024-04-05.
    <https://www.insideindianabusiness.com/articles/skywater-semiconductor-plant-no-longer-planned-for-west-lafayette>
  - SkyWater Technology, Inc., Forms 10-K for FY2023, FY2024 and FY2025 (`LN-1` for URLs).
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Supports** the project's premise on how to get capacity cheaply, and
  **Challenges** the assumption that CHIPS-scale public money makes a greenfield small fab viable.
  It is the cleanest natural experiment in this file: one company, two routes, three years apart.
- **What it says:**

  The announcement, from the state's own development corporation:

  > "$1.8 billion state-of-the-art semiconductor R&D and production facility"

  > "750 new high-wage jobs in Tippecanoe County"

  > "600,000-square-foot semiconductor research and development and production facility in partnership with Purdue University in West Lafayette"

  > "Founded in 2017, Skywater employs 600 associates in Minnesota and Florida."

  The incentive package, itemised:

  > "up to $29 million in the form of conditional tax credits and $1 million in training grants"

  > "$20 million in redevelopment tax credits"

  > "up to $20 million in conditional structured performance payments"

  > "up to $500,000 in innovation vouchers"

  > "$1 million in Manufacturing Readiness Grants"

  Twenty-one months later, Inside INdiana Business reported the cancellation. SkyWater:

  > "While we don't have a definitive plan targeting new fab construction in Indiana, we remain committed to growing the microelectronics ecosystem in the U.S."

  Purdue University:

  > "SkyWater has released its option on the land but remain a valued partner with research opportunities in the works."

  The Indiana Economic Development Corporation:

  > "While we understand that businesses' plans and timelines can change for a variety of reasons, Indiana's microelectronics industry continues to grow at a rapid pace."

  The filings track the same arc. The FY2023 10-K still says:

  > "In addition, in 2022, we announced our plans to build a production and research and development facility in West Lafayette, Indiana through a public-private partnership with the State of Indiana and Purdue University."

  The FY2024 10-K repeats it. **The FY2025 10-K does not mention Indiana or Purdue anywhere.**

- **DERIVED (arithmetic written out):**
  - **Announced Indiana capital per job.** $1,800,000,000 ÷ 750 = **$2,400,000 per job**.
  - **Announced Indiana capital per square foot.** $1,800,000,000 ÷ 600,000 sq ft = **$3,000 per
    square foot** — 4.4× the purpose-built Kissimmee fab's $688.07 (`LN-9`) and 42× the used Fab 25
    at $70.73 (`LN-3`).
  - **The state's share.** 29,000,000 + 1,000,000 + 20,000,000 + 20,000,000 + 500,000 + 1,000,000 =
    **$71,500,000** of state incentives, which is 71.5 ÷ 1,800 = **3.97%** of the project and
    $71,500,000 ÷ 750 = **$95,333 per job**. **The state incentive per job is about the same size as
    the entire capital cost per job of buying a fab** ($75,000 to $98,214 in `LN-14`) — and
    **larger than all four of them**.
  - **How far beyond the company the plan was.** SkyWater's FY2022 revenue was $212,941,000
    (`LN-1`), so the Indiana plan was 1,800 ÷ 212.941 = **8.45× one year's revenue**. Its whole
    five-year organic capex was $104,900,000, so the plan was 1,800 ÷ 104.9 = **17.2× everything it
    actually spent on capital in five years**. It had 600 associates and proposed to add 750.
  - **What it did instead.** In June 2025 it bought an operating 200 mm fab for **$86,500,000 of
    net cash** and got **approximately 1,000 employees** and 400,000 wafer starts a year of
    capacity (`LN-3`). Against the Indiana plan:
    - Cash: 86.5 ÷ 1,800 = **4.81%** of the announced capital.
    - Jobs: 1,000 ÷ 750 = **133%** of the announced jobs.
    - Capital per job: $86,500 against $2,400,000 = **27.7× cheaper**
      (2,400,000 ÷ 86,500 = 27.75).
  - **The whole finding in one line:** the same company got **more jobs for one twenty-third of the
    capital** by buying an existing fab instead of building one, and the difference was not
    marginal — it was the difference between a project that happened and a project that did not.
- **Caveats:** The Indiana facility and Fab 25 are not the same thing: Indiana was to be a new R&D
  and production facility with unspecified technology, Fab 25 is an existing 65 nm-support 200 mm
  line with a four-year take-or-pay to its former owner. A greenfield fab buys capability the
  buyer chooses; a used fab buys the capability that is there. The $1,800,000,000 was contingent on
  CHIPS funding that SkyWater never received for Indiana — the company's own statement blames "the
  details of the CHIPS initiative" unfolding. The IEDC incentives were performance-based and, as
  far as could be determined, none was paid. Neither the SkyWater cancellation statement nor the
  Purdue statement was read on a page that loaded for an automated fetch; both are quoted from
  Inside INdiana Business, which is a trade outlet, not the local Lafayette paper (`wlfi.com`,
  `jconline.com` and `wthr.com` all refused — see "What I could not get").

### LN-16. MOSIS 2.0 and CA DREAMS: $85.8 million of Department of Defense money against a $20 million-a-year revenue target

- **Sources:**
  - Stephanie Lee, "The vision of MOSIS 2.0", USC Information Sciences Institute / USC Viterbi,
    2024-06-05. <https://www.isi.edu/news/68892/the-vision-of-mosis-2-0/>
  - "MOSIS 2.0's First Year: Bridging Research and Production", USC Information Sciences Institute,
    2025-02-21. <https://www.isi.edu/news/972800/mosis-2-0s-first-year-bridging-research-and-production/>
  - "USC's CA DREAMS Hub secures additional $27 million in DoD funding", USC Viterbi School of
    Engineering, 2024-12-10.
    <https://viterbischool.usc.edu/news/2024/12/uscs-ca-dreams-hub-secures-additional-27-million-in-dod-funding-from-chips-science-act/>
  - "MOSIS 2.0", CA DREAMS. <https://ca-dreams.org/mosis-2-0/>
- **Verification:** Verified for every quote below.
- **Date checked:** 2026-09-25
- **Bearing:** **Context** for H5 and **Challenges** the "self-sustaining" reading of `SMB-5`. It
  also fills two of the gaps `mosis-funding.md` records as unfilled: `ca-dreams.org` had not been
  crawled, and MOSIS 2.0's scale was known only from marketing.
- **What it says:**

  The size of the public programme behind MOSIS 2.0, from USC Viterbi:

  > "The Department of Defense has awarded an additional $27 million from the CHIPS & Science Act to the California Defense Ready Electronics"

  > "a $16.2 million project to advance gallium nitride (GaN) technology and a $15.7 million project to develop 5G/6G-relevant prototypes"

  > "The CA DREAMS workforce development initiative will receive $1.5 million to lead the development of nationally recognized microcredentials"

  > "these awards bring CA DREAMS' total 2024 Department of Defense investment to $58.9 million"

  > "The total funding since the launch of the project, in 2023, is $85.8 million"

  > "another portion of the funding will be devoted specifically to the CA DREAMS Hub and its 16 partners from industry"

  What MOSIS 2.0 is trying to become, from ISI's own first-year piece:

  > "Over four decades, MOSIS delivered more than 60,000 integrated circuit designs and generated up to $10 million annually at its peak."

  > "MOSIS 2.0 began accepting external customers in summer 2024 and launched its storefront in October."

  > "The goal is ambitious: achieve self-sustainability within the next few years and generate $20 million in annual revenue."

  > "What would normally require months of legal agreements and process setup was completed in two weeks."

  From the 2024 piece:

  > "At its peak, MOSIS fulfilled around 3,000 orders per year, generating up to $10 million in sales."

  > "MOSIS has been extremely successful. Even though it was run by a university, it was a self-sustaining business for 40 years."
  > — Mike Haney, Deputy Director

  > "The ultimate goal is to transform MOSIS 2.0 into a self-sustaining platform by the end of the five-year Microelectronics Commons program in 2028."

  > "The 16 funded partners work like one organization"

  And **the customer-count breakdown, which is new to this directory**, from `ca-dreams.org`:

  > "MOSIS has supported 50+ US government laboratories and agencies, 800+ colleges and universities, and 100+ companies."

  > "been financially self-sustaining for over 35 years."

  The named manufacturing partners on that page are **Northrop Grumman, Teledyne and HRL**, and the
  service covers "compound semiconductors and Si".

- **DERIVED (arithmetic written out):**
  - **Average order value at MOSIS's peak.** $10,000,000 ÷ 3,000 orders = **$3,333 per order**.
    That is the realised average ticket of the longest-running multi-project-wafer service there
    has ever been, and it sits between Tiny Tapeout's $100–$300 and ChipFoundry's $14,950.
  - **The subsidy is about the size of the target revenue.** $85,800,000 since 2023, spread over
    the five-year Microelectronics Commons programme to 2028, is 85.8 ÷ 5 = **$17,160,000 a year of
    public money** — **85.8%** of the $20,000,000 annual revenue MOSIS 2.0 hopes to earn
    (17.16 ÷ 20). Against the historical peak of $10,000,000 a year, the current public funding rate
    is **1.72×** the best year the service ever had.
  - **The tail MOSIS actually served was academic, 8 to 1.** 800+ colleges and universities against
    100+ companies is a ratio of **8:1**, with 50+ government laboratories on top. Adding them,
    **at least 950 institutional customers over 44 years** — about **21.6 new institutions a year**
    (950 ÷ 44). That is the realised, all-time institutional customer count of the service most
    often cited as proof that a long tail exists, and 84% of it is universities.
  - **Designs per customer.** 60,000 designs ÷ 950 institutions = **63 designs per institution**
    over 44 years, or **1.4 designs per institution per year**.
- **Caveats and one discrepancy that must be flagged:**
  - **The $27,000,000 does not reconcile with its own itemisation.** $16,200,000 + $15,700,000 +
    $1,500,000 = **$33,400,000**, against a headline of "an additional $27 million". The most
    likely explanation is that the GaN and 5G/6G projects are shared with other hubs and only part
    of each lands at CA DREAMS, but the article does not say so. **Do not quote the $27,000,000 and
    the itemisation together as if they add up.** The $58,900,000 and $85,800,000 totals are stated
    directly and are the safer figures.
  - "Financially self-sustaining for over 35 years" on `ca-dreams.org` conflicts with the
    finding already in this directory (`MOS-1`, `MOS-8`) that DARPA funded MOSIS through 1994 and
    that it took $17,958,805 of DARPA money again in January 2021. `mosis-funding.md` should be
    read before either claim is used; **this entry does not endorse the "self-sustaining"
    framing**, it records that CA DREAMS still publishes it.
  - "$20 million in annual revenue" is a goal stated in a university news item, not a plan filed
    anywhere. The 2028 date is the end of the funding programme, not a commitment.
  - The customer counts ("50+", "800+", "100+") are cumulative over MOSIS's whole history and are
    the service's own marketing figures; no register of them was found.

### LN-17. Tower/Maxim, San Antonio: 28,000 wafers a month and nearly 500 employees for $40 million — paid in shares, no cash

- **Sources:**
  - "TowerJazz to Expand its Worldwide Manufacturing Capabilities with Proposed Acquisition of Maxim
    Integrated's Wafer Manufacturing Plant in Texas, US", press release of 2015-11-18, furnished as
    Tower Semiconductor Ltd. Form 6-K, SEC CIK 0000928876.
    <https://www.sec.gov/Archives/edgar/data/928876/000117891315003493/zk1517623.htm>
  - Tower Semiconductor Ltd. Form 6-K of 2016-02-02 announcing completion.
    <https://www.sec.gov/Archives/edgar/data/928876/000117891316004110/zk1617923.htm>
- **Verification:** Verified for the 2015 release, every quote read in the filed document;
  **Partial** for the fifteen-year term of the supply agreement, which appears in the completion
  release on Tower's investor site rather than in the 6-K read here.
- **Date checked:** 2026-09-25
- **Bearing:** **Supports** the project's premise on capital cost, and gives the **third
  independent observation of what buying a fab costs per job**. Also **Context** for H2: this is
  the same trade as Fab 25 — an IDM sells its fab to a foundry and becomes its anchor customer.
- **What it says:**

  > "TowerJazz, (NASDAQ/TASE:TSEM) the global specialty foundry leader, announced today it has signed an agreement with Maxim Integrated Products, Inc. (NASDAQ:MXIM) to purchase Maxim’s 8-inch fabrication facility in San Antonio, Texas, United States."

  > "The proposed purchase will expand TowerJazz’s current worldwide manufacturing capacity, cost-effectively increasing production by approximately 28,000 wafers per month."

  > "As part of the transaction, the companies have also signed a long-term supply agreement for TowerJazz to manufacture products for Maxim in the San Antonio facility. The transaction is to be paid with TSEM ordinary shares with a total value of approximately 40 million US dollars."

  > "All of the site’s nearly 500 employees will be retained. The headcount consists of production operators, highly experienced production support personnel and process and integration engineers, the majority of which possess graduate degrees."

  > "The facility can support the advanced analog platforms using geometries down to 130nm and can be used also to manufacture third party products using TowerJazz specialty process technologies."

  The buyer's own framing of *why* it is cheap:

  > "We are very excited about this fab purchase. It will provide a quick solution for our significantly growing customer demand, while gaining additional high quality manufacturing capabilities and global flexibility with the incremental capacity,"
  > — Dr. Itzhak Edrei, TowerJazz's President

  And the seller's, which is the same trade Infineon made nine years later (`LN-3`):

  > "We needed a trusted partner to manage our proprietary process technology who also shared our commitment to the employees in San Antonio. Tower Jazz has a proven track record with Maxim and similar beliefs about employees, so this is a natural fit. I look forward to our continued partnership over the coming years,"
  > — Vivek Jain, Senior Vice President of Maxim Integrated's Technology and Manufacturing Group

  > "With this arrangement, we will continue to support our customers for years to come, improve utilization in our Oregon fab, and advance our manufacturing flexibility."

- **DERIVED (arithmetic written out):**
  - **Capital per job.** $40,000,000 ÷ 500 = **$80,000 per job**. Against the two other purchases
    in `LN-14` — $75,000 (Bloomington 2017, `LN-18`), $86,500 (Fab 25 2025) and $98,214
    (Canandaigua 2017) — the four land at **$75,000, $80,000, $86,500 and $98,214**, a spread of
    **31%** across **nine years, four states and two wafer sizes**. Mean:
    (75,000 + 80,000 + 86,500 + 98,214) ÷ 4 = **$84,929 per job**.
  - **Capital per unit of capacity — and the comparison that matters.**
    $40,000,000 ÷ 28,000 wspm = **$1,428.57 per wafer-start-per-month**. Polar's new capacity in
    `LN-11` cost $26,250 per wspm. **Buying capacity cost 1/18th of building it**
    (26,250 ÷ 1,428.57 = 18.4×).
    Annualised: 28,000 × 12 = 336,000 wafers a year, so $40,000,000 ÷ 336,000 = **$119.05 of
    capital per wafer of annual capacity**, against Polar's $2,187.50 — the same 18.4× ratio,
    computed two different ways.
  - **Cash cost: zero.** The consideration was TSEM ordinary shares. A specialty foundry acquired a
    130 nm-capable 200 mm fab with 500 staff **without spending a dollar of cash**, in exchange for
    about 3% dilution and a long-term supply commitment to the seller.
- **Caveats:** Paying in stock is not free — it is dilution, and the $40,000,000 is the share value
  at announcement, not a cash price. The purchase came bundled with a long-term supply agreement
  under which Maxim keeps buying from the fab, which is what made the price low; a buyer without an
  anchor customer attached would not get this price. Tower is an Israeli company, so this is not a
  US small fab's own capital decision, but the fab and its 500 jobs are in San Antonio. "Nearly 500
  employees" is the seller's figure at announcement. No local San Antonio coverage with a county or
  city incentive figure was found (see "What I could not get").

### LN-18. Cypress sold the Bloomington fab for $30 million with 400 jobs and 156,000 wafers a year of capacity — and the capacity figure was printed once and then withdrawn

- **Sources:**
  - "Cypress Closes Sale of Minnesota Wafer Fabrication Facility", Cypress Semiconductor
    Corporation, PR Newswire, 2017-03-01.
    <https://www.prnewswire.com/news-releases/cypress-closes-sale-of-minnesota-wafer-fabrication-facility-300416287.html>
  - "SkyWater Technology Foundry Acquires Twin-Cities Semiconductor Manufacturing Facility from
    Cypress Semiconductor Corporation", SkyWater Technology Foundry, 2017-03-27 (PDF on the
    company's own site).
    <https://www.skywatertechnology.com/wp-content/uploads/2017/03/SkyWater_Acquisition_3_27_17.pdf>
  - SkyWater Technology, Inc., FY2021 Form 10-K, filed 2022-03-10, Item 1.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997422000013/skyt-20220102.htm>
  - "SkyWater Technology (Minnesota)", NIST CHIPS Program Office project page.
    <https://www.nist.gov/chips/skywater-technology-minnesota-bloomington>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Supports** the project's premise on capital cost — a **fourth** independent
  observation of what buying an operating fab costs per job, and the **first** one where capacity,
  jobs and price are all published for the same fab.
- **What it says:**

  Cypress, on the price:

  > "sold the subsidiary...to SkyWater Technology Foundry for $30 million"

  > "The sale of Fab 4 in Minnesota allows us to reduce our manufacturing costs as we exit the fab while using the proceeds to pay down debt."
  > — Hassane El-Khoury, President and CEO

  The same statement contains the sentence that closes the circle on `LN-3`, eight years early:

  > "We will also be able to improve the utilization and efficiency of Fab 25 in Texas, into which we have been transitioning products over the last 18 months."

  SkyWater, on the jobs, four weeks later:

  > "Carrying forward Minnesota’s high-tech legacy, SkyWater Technology Foundry keeps 400 manufacturing jobs in the Twin Cities"

  > "With funding from Oxbow Industries, a Minnesota-based private equity firm and diversified holding company, the acquisition ensures the manufacturing facilities’ future and keeps 400 high-tech manufacturing jobs in Minnesota."

  > "Originally commissioned by Control Data Corporation in the 1980s, the facility has been a cornerstone of Minnesota’s high-tech community"

  And the capacity, from the FY2021 10-K — **the only SkyWater annual report that prints it**:

  > "Our Bloomington, Minnesota-based fab can produce up to 156,000 wafers per year (depending on the product mix) and has at least 517 well-maintained fab and sort tools, enabling high volume production for highly customized products. Our utilization rate for the year ended January 2, 2022 was approximately 87%."

  > "Our fab’s throughput capacity is up to 156,000 wafers per year (device mix dependent)."

  **That sentence does not appear in the FY2022, FY2023, FY2024 or FY2025 10-K.** All four were
  searched for "156,000", "throughput capacity", "wafers per year" and "wafer starts"; the only
  hits are unrelated uses of "utilization rate". The disclosure was made once, at IPO, and
  withdrawn.

  What the CHIPS money would have added, from NIST:

  > "increasing the production capacity of 90nm and 130nm wafers by approximately 30%"

  > "This proposed CHIPS Investment is expected to create approximately 70 jobs"

  > "the State of Minnesota’s Forward Fund would provide $19 million in dedicated funding to support this proposed project"

- **DERIVED (arithmetic written out):**
  - **Capital cost per job.** $30,000,000 ÷ 400 = **$75,000 per job** — the cheapest job in this
    file, and the fourth "buy" observation. With Tower ($80,000), Fab 25 ($86,500) and Canandaigua
    ($98,214) the four run **$75,000 / $80,000 / $86,500 / $98,214**, a **31% spread across nine
    years, four states and two wafer sizes**. Mean: (75,000 + 80,000 + 86,500 + 98,214) ÷ 4 =
    339,714 ÷ 4 = **$84,929 per job**.
  - **Capital cost per unit of capacity.** 156,000 ÷ 12 = **13,000 wafer starts per month**.
    - $30,000,000 ÷ 13,000 wspm = **$2,307.69 per wafer-start-per-month**.
    - $30,000,000 ÷ 156,000 = **$192.31 of capital per wafer of annual capacity**.
  - **Capital per tool.** $30,000,000 ÷ 517 tools = **$58,027 per fab or sort tool**, buildings and
    land included. A single new 200 mm process tool lists well into seven figures.
  - **Realised revenue per wafer — the number the customer arithmetic needs.** At 87% utilisation
    the fab ran 156,000 × 0.87 = **135,720 wafers** in FY2021, against total revenue of
    $162,848,000 (`LN-1`). $162,848,000 ÷ 135,720 = **$1,199.88 of revenue per wafer produced**,
    call it **$1,200**. This is a *blended* figure: it divides all revenue, including $111,691,000
    of Advanced Technology Services, by all wafers, so it is what a wafer of this fab's capacity
    earned, not a wafer price. Splitting it the other way, Wafer Services revenue alone was
    $51,157,000, so 51,157,000 ÷ 135,720 = **$376.92** — which is far too low for a 200 mm wafer
    and shows that most of the fab's wafer starts were consumed by development work billed as
    services, not by wafers sold by the wafer.
  - **Payback, as a sanity check on the purchase price.** $30,000,000 of purchase price against
    $162,848,000 of FY2021 revenue is **0.18 years of revenue** (30 ÷ 162.848) — the same order as
    Fab 25's 0.25 years.
  - **The CHIPS modernisation, in the same units.** +30% of 13,000 wspm = **+3,900 wspm**, or
    +46,800 wafers a year. The announced public money is $16,000,000 + $19,000,000 =
    **$35,000,000**, so $35,000,000 ÷ 3,900 = **$8,974.36 of public money per added
    wafer-start-per-month**, and $35,000,000 ÷ 70 jobs = **$500,000 of public money per job**.
    **That is public money only** — SkyWater's own share is not disclosed, so the true cost per
    wspm is higher and this is a lower bound.
- **Caveats:** The $30,000,000 is Cypress's figure for the sale of the capital stock of a
  subsidiary, so it is an equity price and may sit over undisclosed debt or working capital; the
  SkyWater release names no price at all. "400 manufacturing jobs" is SkyWater's number in a
  jobs-focused release and may exclude staff. "156,000 wafers per year" is explicitly
  "device mix dependent" and is a *capability*, not a run rate; the 87% utilisation is for one year.
  The 13,000 wspm conversion assumes twelve equal months. This fab is a 90–350 nm 200 mm line, so
  its wafers are not comparable to a 300 mm wafer or to a MEMS thin-film wafer without adjusting
  for mask count. The CHIPS award was a **preliminary memorandum of terms**, not an award, and is
  labelled as such in `LN-4`.

---

## Capital per wafer start, and how many customers it takes to pay for it

*Added 2026-09-25 on a second pass, after the capacity figures that `LN-14` was missing were found.
No new entry IDs: everything here is arithmetic on figures verified in `LN-1` … `LN-18` and on
entries elsewhere in this directory. Where an input comes from outside this file it is cited.*

### 1. Dollars of capital per wafer-start-per-month

| Site | Verb | Capital | wspm | **$ / wspm** | **$ / wafer-yr** | Source |
|---|---|---:|---:|---:|---:|---|
| Tower / Maxim, San Antonio TX, 2016 | **buy** | $40,000,000 | 28,000 | **$1,428.57** | **$119.05** | `LN-17` |
| SkyWater / Cypress, Bloomington MN, 2017 | **buy** | $30,000,000 | 13,000 | **$2,307.69** | **$192.31** | `LN-18` |
| SkyWater / Infineon, Fab 25 Austin TX, 2025 | **buy** | $86,500,000 | 33,333 | **$2,595.03** | **$216.25** | `LN-3` |
| SkyWater Bloomington 2021 debottleneck | **expand** | $56,000,000 | +5,200 | **$10,769.23** | **$897.44** | `LN-2` |
| SkyWater Bloomington CHIPS modernisation | **expand** | $35,000,000 *(public only)* | +3,900 | **$8,974.36** *(lower bound)* | **$747.86** | `LN-18` |
| Polar Semiconductor, Bloomington MN, 2024 | **build** | $525,000,000 | +20,000 | **$26,250.00** | **$2,187.50** | `LN-11` |
| Rogue Valley, Palm Bay FL, 2023–25 | **retrofit** | $25,000,000 – $30,000,000 | 21,000 | **$1,190 – $1,429** | **$99 – $119** | `LN-12`, below |
| X-FAB Texas, Lubbock, existing site | *(base, for scale)* | — | >19,000 | — | — | below |

**Two new primary sources support the last two rows.**

X-FAB publishes its Lubbock throughput on its own careers site
(<https://www.xfabulous.com/our-locations/lubbock-usa/>, verified 2026-09-25):

> "Currently the site is averaging over 19,000 wafer starts/month (Production and Engineering)."

> "The focus is on the production of 6-inch wafers in the CMOS area as well as SiC technologies."

> "X-FAB Texas has a total of 400 employees."

Peter Clarke reported Rogue Valley's Palm Bay capacity twice for *eeNews Europe*, on 2023-06-29 and
again on 2024-07-02:

> "21,000 wafer starts per month"

> "US$30 million capex"

> "equipped to run wafers of 200mm and 300mm diameter"

> "expected to employ about 75 people and begin production in 2025"

(<https://www.eenewseurope.com/en/rogue-valley-selects-florida-for-mems-wafer-fab/> and
<https://www.eenewseurope.com/en/rogue-valley-set-to-receive-chips-funding-for-300mm-mems-fab/>,
both verified 2026-09-25.) Note that eeNews says **US$30 million capex** where the Space Coast EDC
said "a capital investment of $25 million" (`LN-12`); both are shown, and the range is carried
through.

**DERIVED:**
- **Mean of the three "buy" rows:** (1,428.57 + 2,307.69 + 2,595.03) ÷ 3 = 6,331.29 ÷ 3 =
  **$2,110.43 per wspm**, i.e. **$175.87 per wafer of annual capacity** (2,110.43 ÷ 12).
- **Mean of the two clean "expand/build" rows** (excluding the public-only CHIPS row and the
  non-comparable MEMS row): (10,769.23 + 26,250.00) ÷ 2 = **$18,509.62 per wspm**, i.e.
  **$1,542.47 per wafer of annual capacity**.
- **Ratio: 18,509.62 ÷ 2,110.43 = 8.77×.** Buying capacity costs about **one ninth** of building
  it. On the per-job measure in `LN-14` the same split was 13.9×; the two measures bracket the
  answer at **roughly an order of magnitude**, which is the honest way to state it.
- **The three "buy" rows agree far better than they have any right to.** $1,428.57, $2,307.69 and
  $2,595.03 — a 1.82× spread across nine years, three states, three sellers and two wafer sizes,
  with no two transactions sharing a buyer except SkyWater's own two.

**Caveat, and it is a large one: the Rogue Valley row is not comparable and must not be averaged
in.** A MEMS thin-film wafer start is a handful of deposition and etch steps; a 200 mm BCD or CMOS
wafer start at Polar or SkyWater is tens of masks and hundreds of steps. SkyWater's own historical
framing of its Bloomington capacity is "12,000 wafer starts a month, assuming 200-mm diameter
wafers and 30 mask layers". Comparing $1,190/wspm of MEMS capacity with $26,250/wspm of CMOS
capacity compares two different things, and the apparent result that a MEMS retrofit is cheaper per
wafer start than *buying* a CMOS fab is an artefact of that. **Mask-layer-normalised capacity is the
right unit and nobody publishes it.**

### 2. What a wafer of that capacity earns

One fab publishes both capacity and utilisation, so one realised figure exists (`LN-18`):

- SkyWater Bloomington, FY2021: 156,000 × 0.87 utilisation = **135,720 wafers**;
  $162,848,000 of revenue ÷ 135,720 = **$1,199.88 of revenue per wafer produced**.

Against the capital numbers above:

| | $ capital per wafer of annual capacity | Years of revenue at $1,200/wafer to repay the capital |
|---|---:|---:|
| **Buy** (mean of three) | $175.87 | **0.15 years** |
| **Expand/build** (mean of two) | $1,542.47 | **1.29 years** |

Capital is not what makes a fab hard. Even a built fab repays its *capital* out of about fifteen
months of revenue at full utilisation. What kills small fabs in this directory is operating cost and
utilisation — `LN-7`'s −12.93% operating margin, `LN-9`'s $25,000,000-a-year running cost against
$27,500,000 of total contracts, `IHF-8`'s audited losses. **Nothing in this section contradicts
that; it narrows where the difficulty is.**

### 3. How many customers does it take?

Take the cheapest real fab in the file, Bloomington at **156,000 wafers a year for $30,000,000**,
and the dearest capacity, Polar at **$2,187.50 per wafer of annual capacity**. Then price the
customers from this directory's own evidence.

| Customer type | What they pay | Source |
|---|---|---|
| Tiny Tapeout design | **$199.62 lifetime average** — $0.85m central dollar-equivalent lifetime revenue ÷ 4,258 designs | `PAY-6` |
| wafer.space slot | **$7,000 – $8,500**, for "1,000 bare dies" of 19.67 mm² | `PAY-9` |
| ChipFoundry shuttle slot | **$14,950** | `CF-8`, `SMB-9` |
| "Real" production customer | **100 wafers a year**, ≈ $300,000 a year at $3,000/wafer | `customers-needed-to-fill-a-fab.md` |

**(a) Filling the fab, in customers.**
156,000 wafers a year ÷ 100 wafers per customer = **1,560 customers**. For Fab 25:
400,000 ÷ 100 = **4,000 customers**. Both are numbers the repository's own long-tail evidence can
imagine; neither is a million.

**(b) Capital per such customer.**
- Bought: $30,000,000 ÷ 1,560 = **$19,231 of capital per customer**, which is
  19,231 ÷ 300,000 = **6.4% of one year of that customer's spend**.
- Built at Polar's rate: 156,000 × $2,187.50 = $341,250,000; ÷ 1,560 = **$218,750 per customer**,
  which is **72.9% of one year of that customer's spend**.

**Both are financeable.** A business whose capital cost is 6% — or even 73% — of one year of
customer revenue is an ordinary business. **If the tail contains 1,560 customers who each buy 100
wafers a year, the capital is not the problem, and buying rather than building makes it eleven times
less of a problem.**

**(c) But the tail this directory has actually measured does not buy wafers.** Price the same
capital against what the observed long tail actually pays:

- **Tiny Tapeout, at $199.62 a design.** $30,000,000 ÷ 199.62 = **150,285 designs** to cover the
  purchase price of the cheapest fab here, before a dollar of operating cost. Tiny Tapeout has done
  **4,258 designs in five years** (`PAY-6`) and its record year was **1,455 designs** (2025). At the
  record rate: 150,285 ÷ 1,455 = **103 years**. For Fab 25: $86,500,000 ÷ 199.62 = 433,323 designs
  = **298 years**. For Polar's $525,000,000: 2,629,997 designs = **1,807 years**.
- **ChipFoundry shuttle slots, at $14,950.** $30,000,000 ÷ 14,950 = **2,007 slots**. ChipFoundry's
  completed runs committed 21, 23 and 29 slots at two to three runs a year (`CF-6`, `CF-7`) — call
  it 75 slots a year at its best. 2,007 ÷ 75 = **27 years** for the cheapest fab, **77 years** for
  Fab 25, **468 years** for Polar.
- **The whole unsubsidised sector's money at once.** Tiny Tapeout, chipIgnite/ChipFoundry and
  wafer.space together took **$931,158 in 2025** (`PAY-8`). $30,000,000 ÷ 931,158 = **32.2 years**
  of the entire worldwide unsubsidised open-shuttle sector's revenue, spent on nothing but the
  purchase price, to buy the cheapest fab in this file. Against Polar's $525,000,000:
  **563.8 years**.

**(d) The reason is a unit mismatch of four orders of magnitude, and it cuts the project's way on
price.** A wafer.space slot is "1,000 bare dies" of 19.67 mm² = **19,670 mm² of die area**. A
200 mm wafer is π × 100² = **31,415.9 mm²** gross, of which perhaps 28,000 mm² is usable die area
after edge exclusion, so **one wafer.space slot is roughly three-quarters of one 200 mm wafer**. At
$7,000 a slot that is about **$9,333 of revenue per 200 mm wafer equivalent** — against the
**$1,200 per wafer** SkyWater's whole Bloomington fab earned in FY2021. A Tiny Tapeout shuttle is
one purchased slot resold up to 512 ways: `CF-9` records Tiny Tapeout putting **1,357 designs onto
ChipFoundry silicon in five runs while buying five slots**, and `PAY-6`'s per-shuttle revenue runs
€63,750–€73,420 on a single slot — i.e. **on the order of €65,000 of revenue per wafer
equivalent**, fifty times what the fab earns per wafer from everybody else.

**So the long tail does not pay too little per wafer. It pays 8× to 54× too much per wafer, and
consumes almost no wafers.** The binding constraint is volume, and it is not close:

- 6,218 Tiny Tapeout tiles over five years, at 512 tiles to a slot, is **12.1 slot-equivalents**
  (6,218 ÷ 512) ≈ **about a dozen wafers of die area in five years**.
- wafer.space's thirty orders across three runs is **30 slots** ≈ **23 wafers of die area**
  (30 × 0.75).
- Together: **≈ 35 wafers of die area** for the whole recorded output of both programmes.
- Bloomington's capacity is **156,000 wafers a year**, or 156,000 ÷ 365 = **427 wafers a day**.
- 35 ÷ 427 = **0.08 days — about two hours.**

**The entire recorded die area of the unsubsidised open-shuttle sector, over its whole existence, is
about two hours of one small fab's capacity.** The *actual* wafers consumed are more than that,
because a multi-project run is a minimum lot — typically about 25 wafers — whether you use a
512th of the reticle or all of it: wafer.space's three runs alone would be ~75 wafers on that
basis, and the two programmes together plausibly a few hundred wafers, i.e. **of the order of one
day** of the fab. Either way the conclusion is the same and is not sensitive to the assumption.

### 4. The answer, plainly

> **No plausible number of tape-out customers pays for a built fab, and none pays for a bought one
> either — but the gap is 18× narrower, and the shape of the gap is volume, not price.**

Stated as the three findings the coordinator asked for:

1. **Built fab: unreachable.** Polar's $525,000,000 is **563.8 years** of the current worldwide
   unsubsidised open-shuttle sector's annual revenue (525,000,000 ÷ 931,158), or **1,807 years** of
   Tiny Tapeout at its record rate. The fastest series in this directory is Tiny Tapeout's
   **+156%/yr** over 2022–2025 (`PAY-6`), i.e. ×2.56 a year. Growing $931,158 to $525,000,000 at
   that rate takes ln(563.8) ÷ ln(2.56) = 6.3346 ÷ 0.9400 = **6.7 years of unbroken ×2.56 growth**
   — and the same entry records that the sector's money **fell 46% in 2025**. Treat 6.7 years as
   the arithmetic floor under the most favourable assumption in the directory, not as a forecast.
2. **Bought fab: not reachable today, but arguably reachable.** $30,000,000 is **32.2 years** of the
   sector's current revenue — or, the more useful framing, **about nineteen months** of the revenue
   of a sector 20× its present size (20 × 931,158 = $18,623,160/yr; 30,000,000 ÷ 18,623,160 = 1.61
   years). Twenty times wafer.space's thirty orders is 600 orders. That is a number this directory
   can imagine; 150,285 Tiny Tapeout designs is not.
3. **What actually pays for either is wafer customers, and the capital per wafer customer is
   small.** 1,560 customers at 100 wafers a year fills the Bloomington fab, and the capital works
   out at **$19,231 per customer bought** or **$218,750 per customer built** — 6.4% and 72.9% of one
   year of that customer's spend. **The capital is not the obstacle. Finding 1,560 customers who buy
   wafers rather than tape-outs is the obstacle**, and `DEM-15` (TSMC's non-top-ten customers
   average US$41m a year each), `PAY-9` (thirty orders worldwide in thirteen months) and the
   retention analysis (a recurring core of about 1,250 Tiny Tapeout designers, of whom 73.6% make
   exactly one design ever) are the evidence on whether they exist. **They say: not yet.**

**A correction to an assumption used in commissioning this section.** The tiles-per-design ratio is
**1.46**, not 1.76: `PAY-6` gives 6,218 tiles and 4,258 designs, and 6,218 ÷ 4,258 = **1.4603**. The
figure 1.76 in `PAY-6` is the 2025→2026 revenue growth ratio (341,710 ÷ 194,670), not a tile count.
Nothing above depends on it — the arithmetic here uses revenue per design, not tiles — but it should
not propagate.

---

## What I could not get, and why

Blocked items with the blocker named are recorded here on purpose. None of these was abandoned for
lack of trying, and none was worked around by defeating a bot check.

1. **`fltimes.com` (Finger Lakes Times) — HTTP 429, no Wayback snapshot.** The Ontario County deed
   transactions column for May 2025 carries the exact recorded price at which the Canandaigua fab's
   land and buildings transferred from Akoustis to Tune Holdings (SpaceX) — reportedly
   **$8,965,720** for 5450 and 5440 Campus Drive, Town of Canandaigua. This is the single best
   available split of the $30.2m total sale into real property versus everything else, and it is
   exactly the county-record-in-the-local-paper datum this task was looking for. The article URL
   returned HTTP 429 on three attempts with a browser user-agent, and
   `archive.org/wayback/available` reports **no archived snapshot** of it. The figure is therefore
   recorded in `LN-10` only as reported, not as verified, and the underlying Ontario County deed
   record was not retrieved.
2. **`eda.gov` — HTTP 403.** The Economic Development Administration's own Build Back Better
   Regional Challenge finalist page for the Osceola County Board of County Commissioners
   (<https://www.eda.gov/funding/programs/american-rescue-plan/build-back-better/finalists/osceola-county-board-of-county-commissioners>)
   returns 403 to an automated fetch. That page has the component-project breakdown of the
   $50,800,000 award, which would have converted `LN-9`'s single federal number into a
   capital-versus-programme split.
3. **Osceola County's own capital outlay on ICAMR/BRIDG was never traced to a county document.**
   The `$200 million from the county and local groups` in `LN-9` is Florida Trend's figure and
   `$273 million` appears in the Orlando Economic Partnership's material. Neither was matched to a
   Board of County Commissioners agenda item, a bond issue or a CAFR line. The county's
   **revenue-bond issues** for NeoCity, which would give the exact principal, par value and pledged
   revenue, were not located.
4. ~~**No wafer-start capacity (wspm) is published anywhere in SkyWater's five 10-Ks.**~~
   **WRONG, corrected 2026-09-25.** It is published, in the FY2021 10-K: *"Our fab's throughput
   capacity is up to 156,000 wafers per year (device mix dependent)"*, with an 87% utilisation rate
   alongside it. The first pass searched for "wafer starts" and "wspm" and missed "wafers per
   year". The sentence was then **dropped from the FY2022, FY2023, FY2024 and FY2025 10-Ks** —
   which is itself recorded in `LN-18`. With it, `LN-2`'s "$56 million … at least 40%" converts to
   **$10,769/wspm**, and Fab 25's capacity turned out to be in SkyWater's own completion press
   release ("approximately 400,000 wafer starts per year"), which also corrected the Fab 25 head
   count from a derived 849 to a stated ~1,000. **What remains missing is mask-layer-normalised
   capacity**: a MEMS thin-film wafer start and a 30-mask CMOS wafer start are not the same unit,
   nobody publishes the normalisation, and that is why the Rogue Valley row is excluded from the
   averages in the capacity section.
4b. **Still no capacity figure at all for six of the eleven sites** — Kissimmee (CfN), Canandaigua,
   the four Odon tenants, or the Indiana plan that was cancelled. Akoustis published a *filter*
   capacity ("approximately 500 million XBAW filters per year" at the New York fab, as of 2022,
   found but not verified against a primary document) and never, so far as could be found, a wafer
   capacity.
4c. **No published utilisation for any site except SkyWater Bloomington in FY2021 (87%).** Every
   $/wspm figure in this file is therefore capital per unit of *nameplate* capacity. Polar's
   neighbour SkyWater ran at 87% in a good year; `PCB-2` records a Chinese PCB plant at 41.55%.
   Nameplate is the optimistic end.
5. **The Lubbock tax-abatement file could not be opened.** The City of Lubbock's Laserfiche
   WebLink instance has a "Notice Of Intent To Enter Tax Abatement Agreement - X-Fab TX"
   (<https://weblink.ci.lubbock.tx.us/WebLink/DocView.aspx?id=226922&dbid=5&repo=Lubbock&cr=1>) but
   serves only a JavaScript viewer shell to `curl`; the document pages are not exposed at a plain
   URL and the WebLink REST endpoints return 404. So the *abated* value, the term and the clawback
   terms behind `LN-8`'s $200,000,000 are not in this file. A Texas Tax Code Chapter 313 value
   limitation agreement for X-FAB Texas was searched for and **not found** — the company may simply
   not have one.
6. **No follow-up on whether any of the announced job targets were met.** Every row in `LN-14`
   except Canandaigua, Fab 25 and Kissimmee is an announcement. Nothing was found that reports
   actual head count against target for X-FAB Lubbock, Rogue Valley Palm Bay, or any of the four
   Odon tenants. Targets are systematically optimistic and this is a known weakness of the table.
7. **Rogue Valley Microdevices' Medford, Oregon fab.** No capital figure, head count, cleanroom
   area or wafer-start figure was found for the original site, so the Palm Bay numbers in `LN-12`
   cannot be checked against the company's existing operation.
8. **The Florida Department of Commerce loan and the "other incentives" in `LN-12`** ($5,000,000
   and $3,200,000) were not read in a primary document and are marked Partial in that entry.
9. **Three of the four Indiana local outlets refused an automated fetch.** `wthr.com` (Indianapolis
   NBC), `fox59.com` (Indianapolis Fox) and `wlfi.com` (Lafayette CBS — the actual local station
   for West Lafayette) all returned **HTTP 403**. The SkyWater and Purdue statements in `LN-15` are
   therefore quoted from Inside INdiana Business, a trade outlet, and the genuinely local
   Lafayette coverage (`wlfi.com`, `jconline.com` — the Journal & Courier) was not read. Nothing
   was found on what the *county* had committed, as opposed to the state.
10. **No count of MOSIS 2.0's actual customers, tape-outs, prices or staff.** `ca-dreams.org` and
    `isi.edu` publish a $20,000,000 revenue *goal* and the historical MOSIS customer breakdown, and
    nothing about the present. The gap `mosis-funding.md` records ("MOSIS 2.0's actual headcount,
    revenue or order book") is still open; `LN-16` narrows it only on the public-funding side.
11. **The $27,000,000 CA DREAMS award does not reconcile with its own published itemisation**
    ($33,400,000 of named projects). No reconciling document was found, and the discrepancy is
    flagged in `LN-16` rather than resolved.
12. **Nothing was found for several named targets.** No capital-cost-per-job or capacity figure was
    located for Micross, Teledyne's Thousand Oaks operation, Global Circuit Innovations, Silicon
    Valley Microelectronics, Norcada, MEMSIC, Qorvo Richardson or Coherent/II-VI within the time
    available. These are absences of searching, not verified absences of data. Tower's San Antonio
    fab *was* found (`LN-17`) but **no local San Antonio coverage** — no city or Bexar County
    incentive, abatement or Chapter 380/381 agreement — was located for it; the numbers in `LN-17`
    are all from the company's SEC filings.

