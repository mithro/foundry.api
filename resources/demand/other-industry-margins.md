# Margin split by order size, outside PCBs (`OIM`)

## What this file is for

[`long-tail-businesses.md`](long-tail-businesses.md) `SMB-1` and
[`../analyses/long-tail-pays-for-the-capital.md`](../analyses/long-tail-pays-for-the-capital.md)
rest on **one table in one filing**. JLC's IPO prospectus splits the same PCB factories by order
area and prints the gross margin of each half: 36.24% on sample and small-batch work against 2.76%
on medium and large batch, which decomposes to **97.60% of gross profit coming from the long tail**.
[`pcb-industry-comparables.md`](pcb-industry-comparables.md) then searched the PCB industry for a
second such table and found none — the best-placed peer, Fastprint, splits its margin four ways and
never by batch size.

This file searches **outside PCBs** for the same shape of disclosure: a capital-owning manufacturer
or process business that reports margin, or revenue and cost, **broken down by order size, batch
size, customer size or channel**, in a way that lets the small end be compared with the bulk end.

It is deliberately not a hunt for long-tail analogies in general. That work is
[`../analyses/industry-parallels.md`](../analyses/industry-parallels.md) (`PAR-1`…`PAR-39`).
A business that merely has many customers is not evidence here. The entry has to show the split.

Entries are graded by what they actually contain:

| Grade | What it means |
|---|---|
| **1. Printed table** | Margin by order or batch size, from the same plant, printed by the issuer. The JLC shape. |
| **2. Stated comparison** | "Our short-run work earns X% against Y% on volume", in a filing, prospectus or transcript. |
| **3. Segment reporting** | Segments that happen to correspond to long tail versus bulk, with margins, even if not labelled that way. |
| **4. Reverse finding** | The small end is *less* profitable. Recorded with equal care and no softening. |

---

### OIM-1. Cimpress publishes gross margin by reportable segment for seven years, and its
micro-business segment earns 55% against 32% in its wholesale segment — grade 3, and the closest
thing to JLC found outside PCBs

- **Sources:**
  - Cimpress plc (Nasdaq: CMPR), CIK 0001262976, Annual Report on Form 10-K for the fiscal year
    ended 2025-06-30, filed 2025-08-08, accession 0001628280-25-039200:
    <https://www.sec.gov/Archives/edgar/data/1262976/000162828025039200/cmpr-20250630.htm>
  - Cimpress plc, Form 8-K exhibit 99.1, "Q4 FY2025 Quarterly Earnings" investor letter, furnished
    2025-07-29, accession 0001262976-25-000084:
    <https://www.sec.gov/Archives/edgar/data/1262976/000126297625000084/q4_fy25quarterlyearnings.htm>
  - Cimpress plc, Form 10-K for the fiscal year ended 2024-06-30, filed 2024-08-09, accession
    0001262976-24-000064:
    <https://www.sec.gov/Archives/edgar/data/1262976/000126297624000064/cmpr-20240630.htm>
- **Verification:** Verified 2026-09-25. `www.sec.gov/Archives/...` returns **HTTP 403** to `curl`
  under every User-Agent tried, including a declared non-browser one — the body is SEC's "Your
  Request Originates from an Undeclared Automated Tool" page. The FY2025 10-K and the Q4 FY2025
  earnings exhibit were therefore opened in an ordinary browser and their text read directly; every
  quote below was copied from that text. The FY2024 figures were read through `WebFetch`, which
  does reach `www.sec.gov`, and are marked where they appear.
- **What it says:**
  - **Cimpress is a print business built on small orders and says so in its first sentence.**
    "Cimpress is a strategically focused collection of businesses that specialize in print mass
    customization, through which we deliver large volumes of individually small-sized customized
    orders of printed materials and promotional products."
  - **It names the long tail.** Among its scale advantages it lists "the ability to systematically
    and automatically sort through the voluminous "long tail" of diverse and uncommon orders in
    order to group them into more homogeneous categories, and to route them to production nodes
    that are specialized for that category of operations".
  - **It states the cost-versus-volume trade-off the whole project is about.** "Traditionally, the
    only way to manufacture at a low unit cost was to produce a large volume of that product …
    Custom-made products (i.e., those produced in small volumes for a very specific purpose)
    historically incurred very high unit costs … Mass customization breaks this trade off, enabling
    low-volume, low-cost production of individually unique products."
  - **The long-tail segment, Vista.** "Our Vista business helps about 11 million small businesses
    annually to create attractive, professional-quality marketing and branding products at
    affordable prices and low volumes." And: "VistaPrint represents the vast majority of the
    revenue in this segment where, during fiscal year 2025, average order value (AOV) was more than
    $90 and customers spent, on average, a bit more than $150 for the year; **gross margins were
    about 55%** and advertising spend as a percent of revenue was about 15%."
  - **The bulk/wholesale segments, Upload & Print.** "Our Upload & Print businesses are organized in
    two reportable segments: PrintBrothers and The Print Group, both of which focus on serving
    graphic professionals such as local printers, print resellers, graphic artists, advertising
    agencies, and other customers with professional desktop publishing skill sets. Average order
    values and annual spend per customer vary by business, with AOVs, on average, of about €100 -
    €175 and annual spend per customer of about €300 - €900 in fiscal year 2025. **Gross margins
    vary by business but averaged about 32% in fiscal year 2025 due to wholesale-like pricing** and
    the wide variety of products produced both in owned facilities as well as via third-party
    fulfillers. Advertising spend as a percent of external revenue was about 5% in fiscal year
    2025, although it also varies by business."
  - **The third segment, National Pen**, sits between them: "National Pen serves more than a
    million small businesses annually … During fiscal year 2025, National Pen's average order value
    was about $300 - $350, and annual spend per customer was about $470. Gross margins were about
    51% in fiscal year 2025 with highly seasonal profits driven in the December quarter.
    Advertising spend as a percent of revenue (excluding inter-segment revenue) was about 20% in
    fiscal year 2025."
  - **It owns plant.** "Our businesses operate production facilities throughout the geographies
    listed above, with approximately 3 million square feet of production space in the aggregate
    across our owned and operated facilities." Property, plant and equipment, net, was
    **$302,494 thousand** at 2025-06-30 ($265,177 thousand a year earlier); purchases of property,
    plant and equipment were **$89,024 thousand** in FY2025 and capitalised software a further
    $64,093 thousand.
  - **The numbers are printed, per segment, for seven years.** The Q4 FY2025 earnings document
    prints, for each reportable segment, an annual chart captioned "Gross Profit ($M) & Gross
    Margin (%) Annual" running FY2019 to FY2025, and a revenue table by segment. Transcribed:

    | Segment | FY2025 revenue ($000) | FY2025 gross profit ($M) | FY2025 gross margin, as printed | FY2025 segment EBITDA ($000) |
    |---|---|---|---|---|
    | Vista (≈11m micro-businesses, AOV >$90) | 1,824,271 | 1,006 | **55%** | 347,693 |
    | PrintBrothers (graphic professionals, resellers) | 669,151 | 193 | **29%** | 83,351 |
    | The Print Group (graphic professionals, resellers) | 378,075 | 143 | **38%** | 71,071 |
    | National Pen (>1m small businesses, AOV $300–350) | 406,764 | 207 | **51%** | 31,433 |
    | All Other Businesses | 227,363 | 96 | **42%** | 21,883 |
    | Inter-segment eliminations | (102,545) | — | — | (28,857) |
    | **Total revenue** | **3,403,079** | — | 47.5% consolidated | — |

    And the seven-year series of printed annual segment gross margins:

    | Segment | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
    |---|---|---|---|---|---|---|---|
    | Vista | 58% | 60% | 58% | 57% | 55% | 57% | **55%** |
    | PrintBrothers | 24% | 24% | 25% | 26% | 26% | 29% | **29%** |
    | The Print Group | 34% | 33% | 34% | 35% | 35% | 37% | **38%** |
    | National Pen | 57% | 53% | 49% | 53% | 52% | 53% | **51%** |
    | All Other Businesses | 40% | 46% | 50% | 46% | 44% | 44% | **42%** |

  - **The company explains its own consolidated margin decline by order mix, in the same direction.**
    "Gross margin was impacted by the continued product mix shift to product categories that
    generally have higher gross profit per order and higher customer lifetime value but lower gross
    margins than many of our legacy products including business cards". And at segment level:
    "gross margins contracted (down 160 basis points) this quarter as a result of product mix
    shifting to lower gross margin but higher gross profit orders".
  - **FY2024 says the same thing with the same numbers** (read via `WebFetch`, 2026-09-25): Vista
    "gross margins were about 56%", "average order value was more than $86 and customers spent, on
    average, a bit more than $145 for the year"; Upload & Print "Gross margins vary by business but
    averaged about 32% in fiscal year 2024", "AOVs, on average, of about €95 - €160 and annual spend
    per customer of about €300 - €700 in fiscal year 2024".
- **DERIVED (arithmetic written out):** script `tmp/cimpress_decomp.py` in the working tree at the
  time of writing (project-local `tmp/`, deleted after use). Inputs are only the printed figures
  above.
  - Segment gross margins recomputed from printed revenue ÷ printed gross profit, which checks the
    printed percentages: Vista 1,006,000 ÷ 1,824,271 = **55.15%** (printed 55%); PrintBrothers
    193,000 ÷ 669,151 = **28.84%** (printed 29%); The Print Group 143,000 ÷ 378,075 = **37.82%**
    (printed 38%); National Pen 207,000 ÷ 406,764 = **50.89%** (printed 51%); All Other 96,000 ÷
    227,363 = **42.22%** (printed 42%). All five agree to the rounding.
  - **Upload & Print combined**, FY2025: revenue 669,151 + 378,075 = 1,047,226; gross profit
    193 + 143 = 336; margin 336,000 ÷ 1,047,226 = **32.08%**, which reproduces the 10-K's "about
    32%" exactly. This is the check that the two halves of the disclosure are the same numbers.
  - **The two-way split, Vista against Upload & Print.** Of their combined $2,871,497 thousand of
    revenue and $1,342M of gross profit: Vista is **63.53% of revenue and 74.96% of gross profit**;
    Upload & Print is **36.47% of revenue and 25.04% of gross profit**.
  - **Across all five segments** (revenue $3,505,624 thousand before eliminations, gross profit
    $1,645M): Vista is **52.04% of revenue and 61.16% of gross profit**; the two Upload & Print
    segments together are 29.87% of revenue and 20.42% of gross profit.
  - **Revenue needed per $1 of gross profit:** Vista 1 ÷ 0.5515 = **$1.81**; Upload & Print
    1 ÷ 0.3208 = **$3.12**. The wholesale business must turn over **1.72×** the revenue of the
    long-tail business to service the same capital. (JLC's equivalent ratio was 13.1× in 2025 and
    3.6× in 2023 — see `../analyses/long-tail-pays-for-the-capital.md`.)
  - **The gap is closing, not widening.** Vista's printed annual margin against Upload & Print's,
    recomputed from the printed annual revenue and gross-profit series:

    | | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
    |---|---|---|---|---|---|---|---|
    | Vista | 58% | 60% | 58% | 57% | 55% | 57% | 55% |
    | Upload & Print (computed) | 28.44% | 27.56% | 28.22% | 29.64% | 29.50% | 32.16% | 32.09% |
    | **Gap (pp)** | **29.56** | **32.44** | **29.78** | **27.36** | **25.50** | **24.84** | **22.91** |

    Over six years (FY2019 to FY2025) the long-tail premium narrowed by
    29.56 − 22.91 = **6.65 percentage points**, because the long-tail margin fell 3 points and the
    wholesale margin rose 3.6 points. This runs **opposite** to JLC, where the two segments diverged.
  - **The advertising offset, which is the most important number in this entry.** Segment EBITDA
    margins: Vista 347,693 ÷ 1,824,271 = **19.06%**; PrintBrothers 83,351 ÷ 669,151 = **12.46%**;
    The Print Group 71,071 ÷ 378,075 = **18.80%**; National Pen 31,433 ÷ 406,764 = **7.73%**; All
    Other 21,883 ÷ 227,363 = **9.62%**. A 23-point gross-margin advantage becomes a **0.26-point**
    EBITDA advantage against The Print Group, because Vista spends about 15% of revenue on
    advertising and Upload & Print about 5%. National Pen, at 51% gross margin and 20% advertising,
    ends at 7.73% EBITDA — the *worst* of the five.
- **Bears on:**
  - **H6 (supports, moderately).** A second capital-owning manufacturer, in a second industry, on a
    second continent, reports a much higher gross margin on the small-order half of its business
    than on the bulk half — 55% against 32% — and says in its own words that the bulk half's margin
    is lower because of "wholesale-like pricing". The mechanism JLC describes is not unique to PCBs
    or to China.
  - **H6 (challenges, and this is the honest half).** The gross-margin advantage does not survive
    to the operating line. Vista's segment EBITDA margin is 19.06% against The Print Group's
    18.80% — a difference of a quarter of a percentage point. The long tail's margin is bought with
    advertising: 15% of revenue against 5%. **In Cimpress's accounts, the cost of acquiring a long
    tail eats almost the whole of the long tail's gross-margin premium.** JLC's disclosure does not
    let this be tested for JLC; Cimpress's does, and the answer is uncomfortable.
  - **H6 (challenges).** The gap is *narrowing*, by 6.65 pp in six years, the reverse of JLC's
    direction of travel.
  - **H7 (context).** Cimpress gives no customer-concentration figure, but "about 11 million small
    businesses annually" in one segment and "more than a million" in another is a scale of
    fragmentation comparable to JLC's 1.36 million paying users.
- **Used in:** not yet.
- **Caveats:**
  - **This is not the same plant.** JLC's table splits one set of factories. Cimpress's segments are
    separate acquired businesses (Vista is organic; PrintBrothers is druck.at, Printdeal and
    WIRmachenDRUCK; The Print Group is Easyflyer, Exaprint, Pixartprinting and Tradeprint) with
    their own plants, their own countries and their own cost structures. Part of the 23-point gap
    could be German and Italian wage rates rather than order size. That is a real weakening and it
    is why this is graded 3 and not 1.
  - **Upload & Print is not "bulk" in the JLC sense.** Its average order is €100–175, not a
    20 m² production run. The segments differ by *customer type* — micro-business buying for itself
    versus a print reseller buying wholesale — with "wholesale-like pricing" as the stated cause.
    The order-size difference shows up in annual spend (€300–900 against ~$150), not in the single
    order. The split is closer to "retail versus trade" than to "sample versus batch".
  - **Upload & Print uses third-party fulfillers** for part of its production, so its cost of goods
    includes bought-in manufacture. Cimpress says the gross margin reflects both "wholesale-like
    pricing and the wide variety of products produced both in owned facilities as well as via
    third-party fulfillers", and does not separate the two causes.
  - **Printing is not chipmaking.** $302m of net PP&E across 3 million square feet is a rounding
    error next to a fab. The capital-intensity argument that `long-tail-pays-for-the-capital.md`
    makes for JLC is weaker here, not stronger.
  - The seven-year gross-margin series is read off charts in an investor letter (an 8-K exhibit,
    furnished not filed, and not audited), printed to whole percentage points. The FY2025 revenue,
    segment EBITDA and balance-sheet figures in the same document are to the thousand. The FY2025
    segment gross margins were independently reproduced from revenue and gross profit, which is why
    they can be relied on; the FY2019–FY2022 ones cannot be checked the same way beyond the printed
    revenue and gross-profit dollars, which are themselves chart labels.
  - Cimpress restated its segment results in Q1 FY2025 for a change in inter-segment transfer
    pricing, recast back to Q1 FY2023. Figures before FY2023 are on the old basis.

### OIM-2. Reliance: 4.6 million orders a year at an average of $3,120, a largest customer worth
0.6% of sales, and a printed statement that the small orders are what earns the margin — grade 2

- **Source:** Reliance, Inc. (NYSE: RS), CIK 0000861884, Annual Report on Form 10-K for the year
  ended 2025-12-31, filed 2026-02-26, accession 0001104659-26-020651:
  <https://www.sec.gov/Archives/edgar/data/861884/000110465926020651/rs-20251231x10k.htm>
- **Verification:** Partial, 2026-09-25. The Item 1 quotes below were read through `WebFetch`,
  which reaches `www.sec.gov` where `curl` gets HTTP 403, and were returned identically on the
  queries that produced them. **The consolidated gross-profit-margin percentages were not
  retrieved** — the MD&A sits beyond the point at which the fetch tool truncates the document — so
  no margin figure is asserted here. That is the missing half of this entry and it is listed in the
  blocked-sources table.
- **What it says:**
  - **The long tail, quantified.** "we service more than 125,000 customers"; the company "wrote and
    delivered over 4.6 million orders during 2025" at an "average price of approximately $3,120 per
    order". "In 2025, our average order size was $3,120 and we delivered approximately 40% of orders
    within 24 hours."
  - **Who the customers are.** "most of our sales are to small machine shops and fabricators, in
    small quantities with frequent and often just-in-time deliveries".
  - **The stated comparison.** "a focus on as-needed inventory management and small orders with
    quick turnaround and increasing levels and types of value-added processing generates higher
    gross profit margins".
  - **Why the bulk channel cannot serve them.** "Many customers deal exclusively with service
    centers because the quantities of metal products that they purchase are smaller than the
    minimum order sizes specified by mills."
  - **Customer concentration.** "customer concentration is not significant"; "Our largest customer
    represented 0.6% of our net sales in 2025"; "over 90% of the sales orders we serviced were from
    repeat customers".
  - 2025 net sales were "$14.29 billion".
- **DERIVED (arithmetic written out):**
  - Revenue per customer, 2025: $14,290,000,000 ÷ 125,000 = **$114,320**. Two orders of magnitude
    above JLC's CNY 7,571 (≈US$1,050) per paying user. These are small *businesses*, not hobbyists.
  - Orders per customer, 2025: 4,600,000 ÷ 125,000 = **36.8**.
  - Implied revenue from the order count: 4,600,000 × $3,120 = **$14.352 billion**, against reported
    net sales of $14.29 billion — a 0.43% overshoot, consistent with "over 4.6 million" being a
    rounded floor. The two disclosures reconcile, which is a reason to trust both.
- **Bears on:**
  - **H6 (supports, weakly).** A capital-owning processor with 125,000 customers and a $3,120
    average order states in an audited annual report that small orders with quick turnaround are
    what generate the higher gross profit margin. It is the mechanism JLC's prospectus describes,
    asserted by a company on another continent in another material.
  - **H7 (supports).** A largest customer at 0.6% of sales, from 125,000 customers, is the second
    audited example found of the fragmentation that removes buyer power. JLC's was 0.28%.
  - It is **grade 2, not grade 1**: the company says small orders earn more, but publishes no
    margin split by order size. The comparison it invites — service centre against mill — is a
    comparison between companies, not inside one set of accounts.
- **Used in:** not yet.
- **Caveats:**
  - **Reliance is a distributor with processing, not a manufacturer.** It buys metal from mills and
    cuts, slits and shapes it. Its capital is inventory and processing equipment across hundreds of
    sites, not one indivisible plant. The fab analogy is weaker than JLC's.
  - "Higher gross profit margins" is stated without a counterfactual: higher than what is not
    defined in the sentence. The surrounding text implies "than mills", but the filing does not say
    so in those words and does not print a number for either side.
  - The consolidated gross margin for 2025 is not in this entry. Until it is, the size of the
    premium is unknown.

### OIM-3. Asymchem prints exactly the JLC table for pharmaceutical contract manufacturing — and
it points the other way: small clinical batches 39.42%, large commercial batches 53.32% — grade 1,
grade 4

- **Sources:** 凯莱英医药集团（天津）股份有限公司 (Asymchem Laboratories (Tianjin) Co., Ltd.,
  SZSE: 002821), annual reports, all fetched from the exchange's own document server at
  `static.cninfo.com.cn`:
  - 2025 年年度报告 (FY2025 annual report), published 2026-03-31:
    <http://static.cninfo.com.cn/finalpage/2026-03-31/1225053960.PDF>
  - 2024 年年度报告 (FY2024 annual report), published 2025-03-29:
    <http://static.cninfo.com.cn/finalpage/2025-03-29/1222941173.PDF>
  - 2023 年年度报告 (FY2023 annual report), published 2024-03-29:
    <http://static.cninfo.com.cn/finalpage/2024-03-29/1219441324.PDF>
  - 2022 年年度报告 (FY2022 annual report), published 2023-03-31:
    <http://static.cninfo.com.cn/finalpage/2023-03-31/1216273048.PDF>
- **Verification:** Verified 2026-09-25. Each PDF was downloaded (a browser User-Agent plus
  `-H "Referer: http://www.cninfo.com.cn/"` is required, per the note already in
  [`search-log.md`](search-log.md) §8), its text extracted with `pdftotext -layout`, and every
  figure below located and read in place. Both printed margins in every year were **independently
  recomputed** from the printed revenue and printed cost in the same row; all six reproduce to the
  second decimal.
- **Note on language:** these are Chinese-language filings. Chinese is quoted in the original so a
  reader can check it; **the English renderings are ours**, not the source's, including the table
  headings and row labels.
- **How it was counted:** the table is §三、"主营业务分析" / "2、收入与成本" / "（2）占公司营业收入或
  营业利润 10%以上的行业、产品、地区、销售模式的情况" — "(2) Industries, products, regions and sales
  models accounting for more than 10% of the Company's operating revenue or operating profit" — whose
  columns are 营业收入 / 营业成本 / 毛利率 ("operating revenue / operating cost / gross margin"),
  broken down 分产品 ("by product").
- **What it says:**
  - **The company defines the two halves in its own glossary** (释义, "definitions"):
    "临床阶段 指 与商业化阶段相对应，新药获批前的研究开发阶段" and
    "商业化阶段 指 与新药临床阶段相对应的，药物正式获批上市后的阶段"
    — "**clinical stage**: corresponding to the commercial stage, the research-and-development stage
    before a new drug is approved"; "**commercial stage**: corresponding to the clinical stage of a
    new drug, the stage after the drug is formally approved for marketing." In a CDMO this is a
    batch-size distinction: clinical-stage work is kilograms for trials, commercial-stage work is
    repeat production runs of an approved medicine.
  - **The table, transcribed in full** (CNY; 毛利率 = gross margin):

    | Year | Product line (分产品) | Operating revenue (营业收入) | Operating cost (营业成本) | Gross margin (毛利率) |
    |---|---|---|---|---|
    | 2022 | 临床阶段 CDMO 解决方案 (clinical-stage CDMO solutions) | 1,666,325,421.25 | 978,386,888.02 | **41.28%** |
    | 2022 | 商业化阶段 CDMO 解决方案 (commercial-stage CDMO solutions) | 7,586,807,240.02 | 3,752,539,786.68 | **50.54%** |
    | 2023 | 临床阶段 CDMO 解决方案 (clinical-stage) | 1,507,098,338.18 | 893,098,773.91 | **40.74%** |
    | 2023 | 商业化阶段 CDMO 解决方案 (commercial-stage) | 5,112,480,745.14 | 2,041,367,918.54 | **60.07%** |
    | 2024 | 临床阶段 CDMO 解决方案 (clinical-stage) | 1,766,779,126.83 | 1,070,280,234.84 | **39.42%** |
    | 2024 | 商业化阶段 CDMO 解决方案 (commercial-stage) | 2,803,949,393.96 | 1,308,953,865.20 | **53.32%** |

    The FY2022 report also prints the year-on-year change in each margin — clinical
    "0.53%", commercial "2.95%" — which gives 2021 as well (see DERIVED).
  - **The disclosure stopped in 2025.** The FY2025 report collapses the two rows into one,
    "小分子 CDMO 解决方案" ("small-molecule CDMO solutions"), revenue 4,734,651,275.52, cost
    2,517,242,168.72, margin **46.83%**. There is no clinical/commercial split anywhere in the
    FY2025 report. The four-year series is therefore closed, and a reader in 2027 would not find
    this table at all.
  - **It is a physical-goods business sold by weight.** The FY2025 report's 实物销售 ("physical
    sales") table gives 销售量 ("sales volume") of **250,603.66 Kg** in 2025 and 286,469.58 Kg in
    2024, 生产量 ("production volume") 273,066.38 Kg and 288,105.65 Kg.
  - **It owns and is building plant.** "2024 年末多肽固相合成产能约 21,000L，预计 2025 下半年多肽固相
    合成总产能将达 30,000L" — "at the end of 2024 solid-phase peptide synthesis capacity was about
    21,000 L, and total solid-phase peptide synthesis capacity is expected to reach 30,000 L in the
    second half of 2025"; "500L GMP 发酵车间和 5,000L GMP 车间已于 2025 年第一季度正式投入使用" —
    "a 500 L GMP fermentation workshop and a 5,000 L GMP workshop were formally brought into use in
    the first quarter of 2025."
  - **The company states the utilisation mechanism itself**, about its newer lines: "业务处于爬坡期，
    产能利用率相对较低……导致新兴业务毛利率较低" — "the business is in a ramp-up period and capacity
    utilisation is relatively low … which causes the gross margin of the emerging businesses to be
    low."
- **DERIVED (arithmetic written out):** script `tmp/cdmo_decomp.py` in the working tree at the time
  of writing (project-local `tmp/`, deleted after use).
  - **Every printed margin reproduces.** 2024 clinical: (1,766,779,126.83 − 1,070,280,234.84) ÷
    1,766,779,126.83 = 696,498,891.99 ÷ 1,766,779,126.83 = **39.42%**. 2024 commercial:
    (2,803,949,393.96 − 1,308,953,865.20) ÷ 2,803,949,393.96 = 1,494,995,528.76 ÷
    2,803,949,393.96 = **53.32%**. The same check passes for 2022 (41.28% / 50.54%) and 2023
    (40.74% / 60.07%).
  - **2021, from the FY2022 report's own year-on-year changes:** clinical 41.28 − 0.53 =
    **40.75%**; commercial 50.54 − 2.95 = **47.59%**. Commercial was already ahead.
  - **The gap, every year:** 2021 **+6.84 pp**, 2022 **+9.25 pp**, 2023 **+19.33 pp**, 2024
    **+13.90 pp** — in favour of the *large* batches, in all four years the company disclosed.
  - **The gross-profit decomposition, the JLC calculation run on this table:**

    | Year | Clinical (small batch) share of revenue | Clinical share of gross profit |
    |---|---|---|
    | 2022 | 18.01% | **15.21%** |
    | 2023 | 22.77% | **16.66%** |
    | 2024 | 38.65% | **31.78%** |

    In every year the small-batch half takes a *smaller* share of gross profit than of revenue —
    the mirror image of JLC, where the long tail was 75.57% of revenue and 97.60% of gross profit.
  - **Revenue needed per CNY 1 of gross profit, 2024:** clinical 1 ÷ 0.3942 = **CNY 2.54**;
    commercial 1 ÷ 0.5332 = **CNY 1.88**. The *large-batch* business services capital more
    efficiently, by a factor of 1.35×. At JLC the same calculation gives CNY 2.76 against CNY 36.23
    the other way.
- **Bears on:**
  - **H6 (challenges, strongly).** This is the reverse finding, and it is the single most important
    entry in this file. It is the same disclosure shape as JLC's — one company, one set of GMP
    plants, revenue and cost printed side by side for a small-batch line and a large-batch line,
    audited, four consecutive years — and it says the opposite. In pharmaceutical contract
    manufacturing the **large** batches carry the margin, by 6.8 to 19.3 percentage points, every
    year. Any argument that "small orders are where the gross profit is" has to be stated as a
    claim about *particular* industries, not about small orders in general. `SMB-1`'s finding is
    not a law.
  - **H6 (context).** The likely mechanism is not mysterious and it matters for a fab. A
    clinical-stage batch is a first-of-a-kind process run once: process development, analytical
    method development, technology transfer and regulatory documentation are consumed by a few
    kilograms of output. A commercial batch runs a validated process repeatedly. That is the
    **learning-curve and NRE argument**, and it is exactly the structure a chip shuttle has —
    every long-tail chip is a first-of-a-kind. Where the long tail is *repetitive* (JLC: a
    five-board order runs the same panelised process as every other order) the long tail wins; where
    the long tail is *novel* (a clinical molecule; arguably a one-off chip design) it loses. This
    is the sharpest fault line the search found, and PCB-versus-CDMO is the natural experiment for
    it.
- **Used in:** not yet.
- **Caveats:**
  - **The clinical/commercial split is a batch-size proxy, not a batch-size measurement.** Asymchem
    does not print batch sizes or an order-size band the way JLC prints 1 m² and 20 m². The
    inference that clinical means small batches rests on the glossary and on how CDMOs work, not on
    a disclosed threshold.
  - **Clinical work is partly sold by the hour, not by the kilogram.** The FY2024 report says
    "临床前及临床阶段新药化合物的发现及合成一般以 FTE 方式进行收费(Full Time Equivalent 按工时计费模式)"
    — "the discovery and synthesis of pre-clinical and clinical-stage new-drug compounds is
    generally charged on an FTE basis (Full Time Equivalent, a model charged by working hours)".
    Part of the clinical line is therefore a labour-services margin, not a manufacturing margin, so
    the two rows are not purely like for like.
  - **2023 was distorted by one enormous order.** Commercial revenue fell from CNY 7.59bn (2022) to
    5.11bn (2023) to 2.80bn (2024), and the FY2025 report refers to "2023 年大订单已全部执行完毕" —
    "the 2023 large order has been fully executed". The company's COVID-era antiviral contract sits
    inside the commercial line and inflates both its scale and, probably, its 60.07% margin in 2023.
    The 2024 figure (53.32%) is the cleanest of the four.
  - The 2021 figures are derived from printed percentage-point changes, not read from the FY2021
    report. They are one decimal place of precision and should be re-read before being cited.
  - The disclosure no longer exists. See the FY2025 note above.

### OIM-4. Porton, a second and independent CDMO, prints the same split and the same direction —
early-clinical 19.69% against 44.70% for late-clinical and commercial — grade 1, grade 4

- **Sources:** 重庆博腾制药科技股份有限公司 (Porton Pharma Solutions Ltd., SZSE: 300363), annual
  reports from `static.cninfo.com.cn`:
  - 2025 年年度报告 (FY2025 annual report), published 2026-04-04:
    <http://static.cninfo.com.cn/finalpage/2026-04-04/1225080083.PDF>
  - 2024 年年度报告 (FY2024 annual report), published 2025-03-29:
    <http://static.cninfo.com.cn/finalpage/2025-03-29/1222950027.PDF>
- **Verification:** Verified 2026-09-25, by the same method as `OIM-3`. All six printed margins
  were recomputed from the printed revenue and cost in the same row and reproduce to the second
  decimal.
- **Note on language:** Chinese-language filings; the English renderings are ours.
- **What it says:**
  - **The company defines the bands by trial phase** (释义, "definitions"):
    "临床早期 指 临床二期及以前阶段" — "**early clinical**: phase II and earlier stages";
    "临床后期 指 临床三期至新药申请阶段" — "**late clinical**: phase III through to the new-drug
    application stage."
  - **The table, transcribed** (CNY). The FY2024 report changed the reporting basis and restates
    2023 on the new basis; both versions of 2023 are given by the company, and the restated one is
    used here because it is the comparable basis:

    | Year | Product line (分产品) | Operating revenue (营业收入) | Operating cost (营业成本) | Gross margin (毛利率) |
    |---|---|---|---|---|
    | 2023 (restated) | 临床早期业务 (early-clinical business) | 602,913,229.03 | 561,651,031.61 | **6.84%** |
    | 2023 (restated) | 临床后期及商业化业务 (late-clinical and commercial business) | 2,863,763,715.36 | 1,332,307,247.80 | **53.48%** |
    | 2024 | 临床早期业务 (early-clinical) | 729,544,523.70 | 624,782,629.95 | **14.36%** |
    | 2024 | 临床后期及商业化业务 (late-clinical and commercial) | 2,010,067,122.51 | 1,217,914,335.26 | **39.41%** |
    | 2025 | 临床早期业务 (early-clinical) | 779,947,429.45 | 626,391,396.21 | **19.69%** |
    | 2025 | 临床后期及商业化业务 (late-clinical and commercial) | 2,311,946,059.16 | 1,278,553,253.36 | **44.70%** |

  - **The company names the idle-plant mechanism explicitly**, explaining its 2024 loss:
    "1、随着前期收到的重大订单于 2023 年陆续完成交付，公司营业收入同比减少约 18%；2、公司产能利用率不足，
    单位固定成本分摊增加，导致整体毛利率下降；3、随着公司前期运营规模扩大，公司相关的运营费用及固定资产折旧
    持续保持在高位水平，对净利润产生负面影响"
    — "1. as the major orders received earlier were delivered in turn during 2023, the Company's
    operating revenue fell about 18% year on year; 2. **the Company's capacity utilisation was
    insufficient, the unit fixed-cost allocation increased, and the overall gross margin therefore
    fell**; 3. as the Company's operating scale had previously expanded, its related operating
    expenses and fixed-asset depreciation have stayed at a high level, which has had a negative
    effect on net profit." It also reports 销售量 ("sales volume") of **889,154.36 KG** of
    self-produced product in 2024 (796,741.12 KG in 2023).
- **DERIVED (arithmetic written out):** same script as `OIM-3`.
  - **Every printed margin reproduces.** 2025 early-clinical: (779,947,429.45 − 626,391,396.21) ÷
    779,947,429.45 = 153,556,033.24 ÷ 779,947,429.45 = **19.69%**. 2025 late+commercial:
    (2,311,946,059.16 − 1,278,553,253.36) ÷ 2,311,946,059.16 = 1,033,392,805.80 ÷
    2,311,946,059.16 = **44.70%**. Same check passes for 2023 restated (6.84% / 53.48%) and 2024
    (14.36% / 39.41%).
  - **The gap:** 2023 **+46.63 pp**, 2024 **+25.05 pp**, 2025 **+25.01 pp**, all in favour of the
    larger batches.
  - **The gross-profit decomposition:**

    | Year | Early-clinical share of revenue | Early-clinical share of gross profit |
    |---|---|---|
    | 2023 (restated) | 17.39% | **2.62%** |
    | 2024 | 26.63% | **11.68%** |
    | 2025 | 25.23% | **12.94%** |

    **In 2023 the small-batch line was 17.39% of revenue and 2.62% of gross profit.** That is
    almost precisely JLC's 2025 picture with the two segments exchanged: at JLC the bulk line was
    24.43% of revenue and 2.40% of gross profit.
  - **Revenue needed per CNY 1 of gross profit, 2025:** early-clinical 1 ÷ 0.1969 = **CNY 5.08**;
    late+commercial 1 ÷ 0.4470 = **CNY 2.24**. The small-batch business must turn over **2.27×** the
    revenue to service the same capital — the opposite sign to JLC's 13.1×.
- **Bears on:**
  - **H6 (challenges, strongly).** A second company, independently owned, on a different exchange
    board, with a different product mix and a different reporting basis, publishes the same kind of
    table and the same direction over three years. `OIM-3` is not a one-company artefact. In
    small-molecule pharmaceutical manufacturing the small-batch end is reliably and substantially
    the worse business.
  - **H6 (context, and this is the part that bears most directly on a fab).** Porton's own
    explanation for why its margins move is capacity utilisation and fixed-cost absorption — the
    same argument `../analyses/long-tail-pays-for-the-capital.md` tests as the "idle-plant"
    objection. At JLC the test came out for the long tail (the *big-batch* plant was written down
    for idleness). At Porton it comes out the other way. Whether a long tail fills a plant is an
    empirical question per industry, and it has now been answered both ways.
- **Used in:** not yet.
- **Caveats:**
  - **The split is by trial phase, not by batch size**, exactly as in `OIM-3`, and the same
    FTE-versus-product caveat applies: early-clinical CDMO work is partly charged by the hour.
  - **Porton was loss-making in 2024** (net loss attributable to shareholders of CNY 288 million on
    the company's own statement) and its new businesses ran at a **−71.87%** gross margin. It is
    not a healthy company in these years, and a distressed company's segment margins should be read
    with that in mind. The direction of the early-versus-late gap is nevertheless stable across all
    three years and across the restatement.
  - The 2023 row used here is the FY2024 report's **restated** figure. On the original basis the
    FY2023 report gave different product categories; the restatement is the company's own and its
    reason is printed ("为更为科学、准确地反映公司的当前实际业务情况" — "in order to reflect the
    Company's current actual business situation more scientifically and accurately").
  - Two Chinese CDMOs are not the world CDMO industry. Lonza, Siegfried, Recipharm and Catalent
    were not read for a comparable split; see the blocked-sources list.

---

*(Continued below: further entries, the comparison table, the verdict and the blocked-sources list.)*
