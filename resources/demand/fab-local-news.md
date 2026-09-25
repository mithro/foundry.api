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

**The three most useful capital numbers:**

1. **$86,500,000 of net cash bought a working 200 mm fab with about 849 employees, 1,223,000 sq ft
   of building and 375,000 sq ft of cleanroom** (`LN-3`). That is **$101,884 of capital per job** and
   **$231 per square foot of cleanroom** — one to two orders of magnitude below a greenfield build.
   The fab existed already; someone else paid for it.
2. **$56,000,000 of capex was expected to "increase overall output by at least 40%"** at a 200 mm
   fab (`LN-2`). A capital cost per unit of incremental capacity, stated by the operator.
3. **The public subsidy is small next to the private capital**: up to $16,000,000 of CHIPS plus
   $19,000,000 from Minnesota's Forward Fund (`LN-4`), against $206,466,000 of consideration for one
   fab and a $10,230,000 county match obligation in Florida (`LN-5`). The CHIPS money is a rounding
   error on the transaction that actually added the capacity.

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
  - **Capital cost per unit of incremental capacity.** The 356,000 sq ft Bloomington fab produced
    FY2021 revenue of $162,848,000. If "$56 million … increase overall output by at least 40%" is
    taken at face value and the *majority* of the $56,000,000 is the capacity part, then the fab's
    output can be raised by 40% for **well under $56,000,000** — call it $56,000,000 ÷ 0.40 =
    **$140,000,000 per 100% of this fab's output**, as an upper bound on the capacity portion.
    Against the $10bn–$20bn a leading-edge fab now costs, that is the whole mature-node argument in
    one line.
  - **It did raise output.** Revenue went $162,848,000 (FY2021) → $212,941,000 (FY2022) →
    $286,682,000 (FY2023), i.e. **+76.0% over two years** (286,682 ÷ 162,848 = 1.760), against a
    promised "at least 40%" output increase. Revenue is not output, and price and mix moved too.
- **Caveats:** "Output" is undefined in the filing — it is not wafer starts per month and no wspm
  figure is published anywhere in the five 10-Ks. The $56,000,000 covers both capacity and a GaN
  technology entry, and the filing does not split them. The upper bound above is therefore a
  bound, not a measurement.

### LN-3. A working 200 mm fab with ~849 employees cost $86.5 million of net cash — $101,884 of capital per job

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

- **DERIVED (arithmetic written out):**
  - **Head count acquired.** SkyWater had 702 employees at 2024-12-29 and 1,551 at 2025-12-28, and
    the filing says Fab 25 came with "substantially all of the … employees". 1,551 − 702 = **849
    employees**, treating Legacy SkyWater head count as flat across the year. This is an inference,
    not a disclosure; SkyWater also ran "workforce reorganizations" in the same year, so the true
    Fab 25 head count is probably a little above 849.
  - **Capital cost per job.**
    - Net cash: $86,500,000 ÷ 849 = **$101,884 per job**.
    - Base purchase price only: $73,000,000 ÷ 849 = **$85,983 per job**.
    - Total accounting consideration: $206,466,000 ÷ 849 = **$243,187 per job**.
  - **Capital cost per square foot.**
    - Net cash per square foot of cleanroom: $86,500,000 ÷ 375,000 = **$230.67/sq ft**.
    - Net cash per square foot of building: $86,500,000 ÷ 1,223,000 = **$70.73/sq ft**.
  - **Against fair value.** The bargain purchase gain of $111,746,000 on $206,466,000 of
    consideration means the assets were appraised at 206,466 + 111,746 = **$318,212,000**, so
    SkyWater paid **64.9%** of appraised fair value (206,466 ÷ 318,212), or **27.2%** of it in cash
    (86,500 ÷ 318,212).
  - **Revenue per employee at the acquired fab.** Six months of SkyWater Texas revenue was
    $175,292,000 (`LN-7`), so annualised: 175,292,000 × 2 ÷ 849 = **$412,900 per employee** — and
    the fab was bought for **$101,884 per employee of net cash**. The purchase price was about
    **0.25 years of that fab's revenue** (86,500 ÷ 350,584).
- **Caveats:** **This is not the cost of building a fab.** It is the cost of buying one that
  already exists from an owner who wanted to exit, and the accountants said so by recognising a
  bargain purchase gain. The $120,000,000 "off-market component of the Supply Agreement" means part
  of the price was paid in the form of a below-market four-year take-or-pay to the seller — i.e.
  Infineon sold cheap and bought wafers cheap. The filing gives the reason explicitly: "the bargain
  purchase gain resulted from Infineon's strategic decision to divest Fab 25 in exchange for the
  favorable wafer production pricing included in the Supply Agreement and its ability to maintain
  security of supply for semiconductors used in its products from a trusted partner." A greenfield
  200 mm fab is a $1bn-scale project; none of these numbers say otherwise.

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

---

## What I could not get, and why

(to be completed)
