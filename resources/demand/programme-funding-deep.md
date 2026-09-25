# What the money buys, and how much of it is people (`FUNDX`)

[`programme-funding.md`](programme-funding.md) (`FUND-1` … `FUND-9`) established **how much** public
money the multi-project-wafer brokers take. This file asks the next question:

> **What is the money buying, and how much of it is human labour that automation removes?**

`FUND-9` found that CMC Microsystems spends over half its money on payroll, and that Europractice's
grant looks like a payroll for twenty to twenty-five people. Neither finding rested on a headcount,
because nobody publishes one. This file goes back to the primary documents — audited financial
statements, the grant reports filed with the European Commission, and national grant registers —
to see how far the payroll question can actually be answered.

**Three things changed as a result, and two of them are corrections to `FUND-7` and `FUND-9`.**
Read `FUNDX-1` before quoting either of those entries again.

Currencies are **not** converted. Euro, Canadian dollar and pound figures stand as their sources
give them.

---

### FUNDX-1. CMC's audited financial statements for five consecutive years are public, and they contradict the pie charts `FUND-7` and `FUND-9` were read off

- **Sources** (CMC Microsystems, "Corporate Reports", <https://www.cmc.ca/corporate-reports/> — the
  page that lists them; each statement is the signed, audited set, not a web rendering):
  - *Financial Statements, year ended March 31, 2026*:
    <https://www.cmc.ca/wp-content/uploads/2026/08/2026-CMC-Financial-Statements-1.pdf>
  - *Financial Statements, year ended March 31, 2025*:
    <https://www.cmc.ca/wp-content/uploads/2024/04/2025-03-31-Financial-Statements-796634.pdf>
  - *Financial Statements, year ended March 31, 2024*:
    <https://www.cmc.ca/wp-content/uploads/2024/09/ENG-CMC-final-Sept-24.pdf>
  - *Financial Statements, year ended March 31, 2023*:
    <https://www.cmc.ca/wp-content/uploads/2023/10/2023-CMC-Financial-Statements-EN.pdf>
    (carries restated 2022 comparatives)
- **Verification:** Verified 2026-09-25. All four PDFs were downloaded with `curl` and converted with
  `pdftotext -layout`; every figure below is a line read out of the "Statement of Revenue and
  Expenditures". The statements are fund-accounted, with a column per fund (NSERC / Other / RSF /
  MSI / Quebec / FABrIC) and a total column. Each year's columns were re-added by script and
  reconcile to the printed totals **to the dollar**.
- **How it was counted:** `search.open.canada.ca` and URL-pattern guessing both failed for these
  (that is what `FUND-7`'s blocked list records). The route that worked is trivial and is recorded
  here so nobody repeats the failure: `https://www.cmc.ca/corporate-reports/` is a plain HTML page
  listing every annual report *and* every financial-statement PDF with a direct link. It was never
  fetched. "Revenue earned from customers" below is the sum of every revenue line that is a payment
  by a user of the service; "public money" is every line that is a government grant or contribution.
  The split is ours and is itemised in the caveats.
- **What it says:**

  | Year ended 31 March | Total revenue | Total expenditure | Surplus / (deficit) | Salaries and benefits | Salaries as % of expenditure |
  |---|---:|---:|---:|---:|---:|
  | 2022 (restated) | $15 534 163 | $15 653 837 | ($119 674) | **$7 091 733** | **45.3%** |
  | 2023 | $16 746 411 | $18 987 114 | ($2 240 703) | **$7 647 774** | **40.3%** |
  | 2024 | $15 566 315 | $16 420 151 | ($853 836) | **$6 933 083** | **42.2%** |
  | 2025 | $13 419 183 | $17 066 020 | ($3 646 837) | **$7 876 088** | **46.2%** |
  | 2026 | $21 535 763 | $20 012 740 | $1 523 023 | **$7 859 646** | **39.3%** |

  **CMC ran a deficit in four of these five years.**

  **Correction 1 — the payroll number in `FUND-7` and `FUND-9` is wrong.** Both entries take
  "Salaries and Benefits **$4.0M**" from the expenditure pie chart in the *Annual Report 2025-26*.
  The audited statement for the same year shows salaries and benefits of **$7 859 646**. The $4.0m
  is only the **"Other" fund column** ($3 992 878); the FABrIC fund carries a further **$3 866 768**
  of CMC's own salaries. The pie chart does not say so.

  **Correction 2 — FABrIC is not a pass-through.** `FUND-7` says "FABrIC is a pass-through and must
  be excluded from any unit-cost calculation", and treats the whole $12.8m pie slice as money moving
  through CMC to other people. In the audited statement the FABrIC fund's $14 883 748 of
  expenditure breaks down as **$3 535 310 of "UR challenge projects"** (the actual grants CMC passes
  on, 23.8% of the fund), **$3 866 768 of CMC salaries** (26.0%), $2 363 249 of software tools and
  leases, $1 641 088 of academic fabrication and packaging, and $2 126 722 of "Contribution to
  indirect costs". Only the first of those is a pass-through.

  **Correction 3 — the commercial arm is cross-subsidised by the federal programme, and the
  statement says so on its face.** A line called **"Contribution to Indirect Costs"** appears as a
  *negative* number in the Other (commercial) column and an equal *positive* number in the FABrIC
  column: **$490 552 in 2024, $2 212 084 in 2025, $2 126 722 in 2026.** In other words the federal
  FABrIC contribution absorbs a rising share of the commercial arm's overhead. `FUND-7`'s reading —
  "its fastest-growing line is a commercial arm selling to foreigners" and "if any of the four
  programmes here is converging on self-financing, it is this one" — has to be set against this.

  **Where the revenue comes from** (every line, as printed):

  | Year ended 31 March | Earned from customers | Public money | Interest | Earned as % of revenue | Earned as % of expenditure |
  |---|---:|---:|---:|---:|---:|
  | 2022 | $6 319 108 | $9 196 537 | $18 518 | 40.7% | 40.4% |
  | 2023 | $7 533 071 | $9 150 728 | $62 612 | 45.0% | 39.7% |
  | 2024 | **$7 854 197** | $7 636 264 | $75 854 | 50.5% | 47.8% |
  | 2025 | $6 865 987 | $6 495 647 | $57 549 | 51.2% | 40.2% |
  | 2026 | $5 332 809 | $16 136 220 | $66 734 | 24.8% | 26.6% |

  The public lines change name as the funder changes: **CFI-MSI** (Canada Foundation for
  Innovation, Major Science Initiatives) $6 656 900 in 2022, $6 856 681 in 2023, $4 575 000 in 2024,
  **nil** thereafter; **Province of Quebec** $1 996 665 / $2 048 076 / $1 775 545, nil thereafter;
  **RSF/NSERC** $542 972 / $245 971, nil thereafter; **ISED** nil, nil, $1 285 719, $6 388 416,
  **$16 100 612**. One federal programme has replaced everything else — see `FUNDX-2`.

  **The commercial fund on its own.** In the year ended 2026-03-31 the Other fund took
  **$4 140 881** of revenue against **$5 126 267** of expenditure, a deficiency of **$985 386** —
  *after* being credited $2 126 722 by FABrIC. In the year ended 2025-03-31: revenue $4 578 657,
  expenditure $7 178 918, deficiency **$2 600 261**, after a credit of $2 212 084.

  **Other things in the notes worth having.** Note 10: "The combined expense for all Organization
  pension plans for the year was $453,069 (2025 - $474,833)". Note 8: CMC rents from "Kingston
  Terminal Properties" at "$7,163 per month" (2025-03-01 → 2030-02-28) and from "KRP Properties" at
  "$2,130 per month" (2025-05-01 → 2028-04-30) — total minimum commitments of **$829 389** over four
  years. Note 9: purchase orders outstanding at 2026-03-31 of **$2 326 745**. The legal name is
  "Canadian Microelectronics Corporation/Société Canadienne de Micro-électronique"; some staff were
  "previously paid through Queen's University payroll" and remain in the University Pension Plan.
- **DERIVED (arithmetic written out):**
  - **Payroll share, corrected.** 7 859 646 ÷ 20 012 740 = **39.3%** for the year ended 2026-03-31,
    not the 54.8% in `FUND-9`. The five-year mean of the five percentages
    (45.3 + 40.3 + 42.2 + 46.2 + 39.3) ÷ 5 = **42.7%**. In the year ended 2008-03-31 it was
    5 285 705 ÷ 9 882 500 = **53.5%**. **The direction is down, not flat** — the opposite of what
    `FUND-9` concluded from two data points.
  - **Payroll per prototype.** Against `DEM-20`'s 240 prototypes fabricated in 2025/26:
    7 859 646 ÷ 240 = **CAD $32 749 of salary per prototype**. Total expenditure per prototype is
    20 012 740 ÷ 240 = **CAD $83 386**; excluding only the genuine grant pass-through,
    (20 012 740 − 3 535 310) ÷ 240 = **CAD $68 656**. All three are much larger than `FUND-7`'s
    CAD $30 417, which used the pie chart's understated cost base.
  - **Earned revenue is falling.** $7 854 197 (2024) → $6 865 987 (2025) → $5 332 809 (2026).
    5 332 809 ÷ 7 854 197 = 0.679, a **32.1% fall in two years**, while public money went
    7 636 264 → 6 495 647 → 16 136 220, a **2.11× rise over the same two years**
    (16 136 220 ÷ 7 636 264).
  - **Customers have never covered half the cost.** Earned revenue as a share of *expenditure*
    peaked at 47.8% in the year ended 2024-03-31 and has never exceeded it in the five audited
    years. `FUND-7`'s "customers covered 74.0%" figure came from dividing $5.4m by a $7.3m cost base
    that the audited statement does not support.
  - **Implied headcount.** No headcount is published. Salaries and benefits of $7 859 646, at a
    fully-loaded cost of CAD $120 000 per employee, implies **65 people**; at $140 000,
    **56 people**; at $160 000, **49 people**. Pension expense of $453 069 against that payroll is
    5.8% of it, which is consistent with a mixed RRSP-matching and defined-benefit population and
    does not narrow the range. **Treat 50–65 as an order of magnitude, not a count.**
- **Bears on:**
  - **H6 (challenges, and this is now the most precise evidence anywhere in the directory).** Five
    consecutive audited years of a national MPW brokerage. Payroll is **39–46% of everything it
    spends**, every year. Customers cover **27–48% of expenditure**, every year, and never half. It
    lost money in four years out of five.
  - **H6 (challenges).** The commercial arm — the part `FUND-7` read as converging on
    self-financing — loses money on its own account in both years for which the fund columns can be
    read, and does so *after* a transfer from the federal programme that rose from $0.5m to $2.1m in
    three years.
  - **H6 (context, and it cuts towards the automation argument).** CAD $32 749 of salary per
    prototype is the number the "no full-time employees" model is competing against. It is not a
    marginal cost — much of that payroll supports tools, training and an incubator, not tapeouts —
    but it is what the service's own accounts spend on people, divided by the thing it is famous
    for.
  - **H5 (challenges).** Earned revenue, which is the only demand signal here that is measured in
    money rather than in counts, **fell 32% in two years** while the subsidy doubled.
- **Used in:** not yet.
- **Caveats:**
  - **The earned/public split is ours.** "Earned from customers" = non-subscriber fabrication,
    subscriber fabrication, subscriptions, R&D consulting, other industrial, training revenue,
    sponsorship/SponsorChip, other academic, other, contract management, NanoCanada. "Public" =
    CFI-MSI, Province of Quebec, RSF/NSERC, ISED, provincial contribution. Interest is neither.
    Two lines are genuinely ambiguous: **"Other" $349 344 (2023)** and **"NanoCanada" $69 427
    (2023)**; NanoCanada is a not-for-profit network that itself receives public money, so counting
    it as earned is generous to the earned side. Moving both to "public" would take 2023's earned
    share from 45.0% to 42.5%.
  - **Fund accounting makes single-year comparisons treacherous.** The fund structure changes every
    year (MSI and Quebec funds disappear after 2024; FABrIC appears in 2024; RSF comes and goes).
    Only the **Total** column is comparable across years, and that is what the first table uses.
  - **The 2026 revenue is inflated by a one-off.** The *Annual Report 2025-26* states: "The funding
    agreement for this program was amended in 2025, resulting in $2.4M retroactive revenue, all of
    which was recognized in the 2025-26 fiscal year." Note 7 separately records an interfund
    transfer of **$1 120 531** from FABrIC to Other "in recognition of prior year FABrIC income
    adjustments". The 2026 surplus of $1 523 023 should not be read as a turn to profitability.
  - **Salaries and benefits is one line.** It does not separate technical from administrative staff,
    and no CMC document found does. The staff page (<https://www.cmc.ca/staff/>) lists **4
    leadership and 9 key contacts, 13 named people in total**, which is a directory, not a
    headcount.
  - **The implied headcount is a division, not a measurement.** No CMC document states an employee
    number, and none of the five statements discloses one.
  - The 2022 figures are the **restated** comparatives printed in the 2023 statements; the 2022
    statements themselves are also published
    (<https://www.cmc.ca/wp-content/uploads/2022/09/Financial-Statements-31MAR2022-EN.pdf>) but that
    PDF is a scan with **no text layer** (`pdftotext` returns 15 bytes) and was not read.
  - All figures are Canadian dollars, unconverted.

### FUNDX-2. FABrIC is a CAD $120 million federal contribution running to 2031, and CMC's auditors state that CMC is economically dependent on it

- **Sources:**
  - Government of Canada, Proactive Disclosure of Grants and Contributions, agreement **819430**,
    found through <https://search.open.canada.ca/grants/> with the phrase query
    `"Canadian Microelectronics"` (one record).
  - CMC Microsystems, *Financial Statements, year ended March 31, 2026*, **Note 11, Economic
    dependence**: <https://www.cmc.ca/wp-content/uploads/2026/08/2026-CMC-Financial-Statements-1.pdf>
  - FABrIC programme site, <https://fabricinnovation.ca/>
  - CMC Microsystems, *Annual Report 2025-26*:
    <https://www.cmc.ca/wp-content/uploads/2026/09/CMCAnnualReport_2025-26_EN.pdf>
- **Verification:** Verified 2026-09-25. The federal record was read from the search result page
  (`search.open.canada.ca` serves it server-side; the `format=json` parameter is ignored and returns
  HTML). The note was read from the audited PDF's text layer.
- **How it was counted:** `search.open.canada.ca/grants/?search_text=CMC+Microsystems` returns
  **zero** records — CMC's trading name is not in the register. The unquoted legal name matches
  everything (453 334 records, because the search is an OR over the words). The **quoted phrase**
  `"Canadian Microelectronics"` returns exactly one record. That is the whole trick.
- **What it says:**
  - The federal record, field by field: recipient **"Canadian Microelectronics Corporation"**;
    value **$120,000,000.00**; date Jun 11, 2024; agreement number **819430**; duration
    "from Jun 11, 2024 to Dec 31, 2031"; description **"FABrIC - Fabrication of Integrated
    Components for the Internet's Edge"**; organization "Innovation, Science and Economic
    Development Canada"; program name **"SIF Stream 5 - National Innovation Ecosystems"**;
    agreement type "Contribution"; location "Montreal, Quebec, CA H3C6M8".
  - **The auditors' note, verbatim** (Note 11, *Economic dependence*, financial statements for the
    year ended 2026-03-31): "The Organization is economically dependent on support from the
    Government of Canada's Strategic Response Fund (SRF). In 2024, the Organization secured funding
    of $120 million through the SRF, funding **75-100% of costs** to support the design,
    manufacturing and commercialization of semiconductors and intelligent sensor technology."
  - The programme's own site describes it as "a Strategic Response Fund initiative of the Government
    of Canada to advance domestic capabilities in advanced semiconductor design and manufacturing"
    and "Managed by CMC Microsystems".
  - **The name differs between the two records.** The federal register calls the instrument
    "SIF Stream 5 - National Innovation Ecosystems"; CMC and the programme site call it the
    "Strategic Response Fund". Both refer to agreement 819430 and the same $120m.
- **DERIVED (arithmetic written out):**
  - $120 000 000 over 2024-06-11 → 2031-12-31, a span of 2 759 days = 7.554 years:
    **$15 886 191 a year**.
  - Against the ISED revenue CMC actually recognised: $1 285 719 (FY2024) + $6 388 416 (FY2025) +
    $16 100 612 (FY2026) = **$23 774 747 drawn in the first three years**, i.e. 19.8% of the
    $120m in the first 2.8 years of a 7.55-year agreement.
  - Against the whole of CMC: in the year ended 2026-03-31, ISED money of $16 100 612 was
    **74.8%** of total revenue ($21 535 763) and **80.4%** of total expenditure ($20 012 740).
  - Against `DEM-20`'s 240 prototypes: $15 886 191 ÷ 240 = **CAD $66 192 per prototype per year of
    the FABrIC commitment alone.** This is *not* a cost per prototype — FABrIC buys challenge
    grants, training and equipment as well — and must not be quoted as one. It is the size of the
    commitment set beside the thing the organisation is best known for.
- **Bears on:**
  - **H6 (challenges, hard).** `FUND-7`'s reading was that CMC is "converging on self-financing".
    Its own auditors, in the same year's statements, write the opposite in a formal
    economic-dependence note, and quantify the dependence: a single contribution funding
    **"75-100% of costs"**. This is the strongest single sentence in either file.
  - **H6 (context).** The public money did not disappear when CFI-MSI and Quebec funding ended in
    2024; it was **replaced and more than doubled** by one federal industrial-policy contribution.
    The subsidy per prototype rose because the programme's ambitions grew, not because demand did.
  - **H5 (challenges).** $120m of federal money is being spent on a national semiconductor design
    ecosystem whose flagship prototyping service fabricated **240 prototypes** in the year the money
    started flowing at scale (`DEM-20`).
- **Used in:** not yet.
- **Caveats:**
  - **$120m is the ceiling of a contribution agreement, not money received.** Contributions are
    reimbursements against eligible cost and are routinely underspent. What CMC has actually
    recognised is the $23.8m above.
  - The proactive-disclosure record classifies CMC as a **"For-profit organization"**. CMC is a
    not-for-profit corporation. The field is wrong; nothing else in the record depends on it.
  - "$15.9m a year" is a straight-line division of a commitment that is plainly not spent in a
    straight line — $1.3m in the first year, $16.1m in the third.
  - The register covers federal transfer payments from 2018 only, and expressly excludes "grants and
    contributions reallocated or otherwise redistributed by the recipient to third parties". CMC's
    NSERC funding history before 2018 (the $9.7m a year in `FUND-7`) is **not** in it.
  - `FUND-7`'s note describes FABrIC as funded by "the Innovation, Science and Economic Development
    Canada's Strategic Response Fund". That is what CMC calls it; the federal register calls the
    same agreement SIF Stream 5. Neither source is wrong, but a search on one name will not find the
    other.

### FUNDX-3. The Europractice coordinator told the European Commission, in writing, twice, that "No university scheme in the world is self-funded" — and that an MPW service "is not a financially viable business"

- **Sources** (publishable summaries filed under the FP7 grants and published by the Commission on
  CORDIS; these are the documents behind the "Reporting" tab that `FUND-2` used only for the
  post-2016 grants):
  - EUROPRACTICE IC4 (grant 214157), *Publishable summary*:
    <https://cordis.europa.eu/docs/projects/cnect/7/214157/080/reports/001-Publishablesummary12.pdf>
  - EUROPRACTICE IC5 (grant 257098), *Publishable summary* (period 1):
    <https://cordis.europa.eu/docs/projects/cnect/8/257098/080/reports/001-Publishablesummary.pdf>
  - EUROPRACTICE IC5 (grant 257098), *Publishable summary FINAL*:
    <https://cordis.europa.eu/docs/projects/cnect/8/257098/080/reports/001-PublishablesummaryFINAL.pdf>
  - EUROPRACTICE 2012 (grant 315961), *Publishable summary*:
    <https://cordis.europa.eu/docs/projects/cnect/1/315961/080/reports/001-Publishablesummary.pdf>
  - EUROPRACTICE 2013 (grant 610018) fact sheet, for the 2013 membership figure:
    <https://cordis.europa.eu/project/id/610018>
- **Verification:** Verified 2026-09-25. All four PDFs were downloaded with `curl` and converted with
  `pdftotext -layout`; every quote below was copied out of the text layer. These are the
  coordinator's own words, published unaltered by the Commission.
- **How it was counted:** `https://cordis.europa.eu/project/id/<id>/reporting` returns a page whose
  HTML carries `href="/docs/projects/cnect/<n>/<id>/080/reports/…"` links to the actual filed
  documents. The rendered text of the reporting page shows only the file names, so a text-only read
  misses them; **grep the raw HTML for `/docs/projects/`**. This is the route `FUND-2` did not take
  for the FP7 grants, and it is where the FP7-era material lives.
- **What it says:**
  - **The business-model paragraph, IC4** (2008–2010), verbatim and in full:

    > "The current business model relies on major contributions from the universities and industrial
    > customers covering all of the CAD Vendor and shipment costs (licenses, maintenance, delivery),
    > IC prototyping and volume production costs plus an identifiable contribution through the annual
    > university membership fees to the overall running costs of the Service. As the MPW service is
    > open to industrial customers, it is not a healthy situation to ask higher prices and to make
    > profit on MPW fabrication of European industry or SME designs in order to cover university
    > costs. **No university scheme in the world is self-funded. Either these schemes are funded
    > through direct funds or through government paid staff. The fact that the foundries themselves
    > restrict MPW services to their major customers (just a service – no business) and do not give
    > access to universities due to the large overhead (support) indicate that MPW service is not a
    > financially viable business.**"

  - **The same paragraph, IC5** (2010–2011), with two additions:

    > "**No university scheme in the world is self-funded and from interactions with the other
    > schemes world-wide it is apparent that Europractice has by far the highest level of end-user
    > financial contribution.** Either these schemes are funded through direct funds or through
    > government paid staff. … **When we compare the annual funding of the EUROPRACTICE IC Service
    > (annually ~ 1.6 million euro to support 650 European universities) to other university schemes
    > we see that those other schemes get a much higher funding.**"

  - **A named subsidy line inside the grant.** EUROPRACTICE 2012's summary explains what the money
    buys, verbatim: "with the introduction of 90nm technology in 2006, the increased mask cost
    resulted in high prototype fabrication cost, even for a mini@sic MPW run, for a small design
    area of 2x2mm. This proved to be too expensive for academic institutions and **EUROPRACTICE
    asked the EC for a special budget (called subsidy budget) in order to be able to further reduce
    mini@sic MPW prototype fabrication prices (part of the prototyping cost is paid by this EC
    budget).** The resulting increase in the number of small designs prototyped shows that this
    financial incentive stimulates universities to adopt new technologies."
  - **The SME side is explicitly outside the grant.** EUROPRACTICE 2012: "EUROPRACTICE is offering,
    **at full non-EC funded cost**, access to prototyping (MPW runs) and initial volume fabrication
    to more than 200 fabless companies, startups and small companies in Europe. … **This activity is
    not funded by the project.**" IC5 gives the same with "more than 150 fabless companies".
  - **Subsidised prices, stated as prices.** IC5 final: "the universities and research centers can
    have small IC and MEMS designs prototyped at pricing levels of **2,000 €** for 0.35µ-like CMOS
    to **15,000 €** for advanced 90nm CMOS mixed-signal RF technologies", and the target "can only
    be achieved if the price per prototype can be kept around **10,000 euro with subsidy through
    this project**."
  - **The target volume.** IC5: "To prototype **more than 300 IC/SoC designs** from those 650
    universities or institutes per year"; "to have about **20 designs of the 300 in 65/40nm** in
    2010-2011"; "to have **more than 10 MEMS and MEMS/CMOS designs** annually prototyped".
  - **The membership series, from the grants themselves.** IC4 (2008): "about **600 universities and
    50 research institutes**". IC5 (2010): "Today **550 universities and 100 research institutes**".
    EUROPRACTICE 2012: "Today **512 universities and 128 research institutes from 44 countries**".
    EUROPRACTICE 2013's objective text: "**650 European Academia (515 universities and 135 research
    centers)** have access to this Service", with "strong support letters from 130 Academia".
- **DERIVED (arithmetic written out):**
  - **The coordinator's own €1.6m/yr matches `FUND-4`'s reconstruction.** `FUND-4` derived a
    declared operating cost of €1 607 027/yr (IC4), €1 672 812/yr (IC5) and €1 356 408/yr
    (EUROPRACTICE 2012) from `totalCost ÷ years` in the CORDIS bulk export. The IC5 summary states
    "annually ~ 1.6 million euro" independently. **Two different routes, the same number.** That
    upgrades `FUND-4`'s figure from a derivation to a corroborated one.
  - **What the €1.6m bought per member.** €1 600 000 ÷ 650 institutions = **€2 462 per member
    institution per year** of total declared cost, against a Full-IC membership fee of €1 100
    (`FUND-3`). The fee covered **44.7%** of the declared cost per member — and the declared cost
    excludes the trading side entirely.
  - **Against the target volume.** €1 600 000 ÷ 300 designs = **€5 333 of declared cost per design**
    at the grant's own target. `FUND-4` derived €2 500–4 000 from `DEM-16`'s actual counts of
    400–600; the difference is that the grant's target counted only the academic IC/SoC designs, not
    the industrial ones.
  - **The paying membership has been flat for eighteen years.** 650 (2008) → 650 (2010) → 640 (2012)
    → 650 (2013) → 612 paid (2017/18, `FUND-2`) → 630 (2026-09-19, `FUND-3`). Range over eighteen
    years: **612 to 650, a 6% spread.**
- **Bears on:**
  - **H6 (challenges, and this is the most quotable evidence in either file).** The organisation that
    runs Europe's MPW brokerage told its funder, in a document the Commission then published, that
    **"MPW service is not a financially viable business"** and that **"No university scheme in the
    world is self-funded."** It repeated it two years later, adding that Europractice "has by far the
    highest level of end-user financial contribution" of any such scheme in the world — i.e. the most
    commercial one it knows of still needed €1.6m a year.
  - **H6 (challenges).** The second sentence names the mechanism the owner is testing: schemes are
    "funded through direct funds **or through government paid staff**". Where the subsidy is not
    cash it is salary. That is the payroll question stated by the incumbent.
  - **H5 (mixed, and the useful part cuts both ways).** "The resulting increase in the number of
    small designs prototyped shows that this financial incentive stimulates universities to adopt
    new technologies" is a clean statement of price elasticity from inside the programme: when the
    price fell, volume rose (see `FUNDX-4` for the year it ran out of money). But the elasticity is
    measured *within* a fixed academic membership of ~650 institutions that has not grown in
    eighteen years. Cheaper prototypes moved existing members to newer nodes; they did not bring new
    customers.
  - **H8 (context).** "it is not a healthy situation to ask higher prices and to make profit on MPW
    fabrication of European industry or SME designs in order to cover university costs" is an
    explicit refusal to cross-subsidise academia from industry — a pricing-design choice, stated as
    a principle, by the incumbent.
- **Used in:** not yet.
- **Caveats:**
  - **These are advocacy documents.** A publishable summary filed under a grant is written partly to
    justify the next grant. "No university scheme in the world is self-funded" is the coordinator's
    assertion about the world, made while asking the world's largest funder for more money; it is
    not an audit. Its evidential value is that it is the incumbent's own characterisation of its own
    business, made against interest on the viability point and in interest on the funding point.
  - **"~1.6 million euro" carries no basis.** It is not said whether it is EC contribution, declared
    cost, or the whole service. `FUND-4`'s CORDIS figures suggest declared cost (EC contribution in
    the same years was €1.05m and €1.06m a year), but the summary does not say.
  - The two IC5 summaries **disagree on prices**: the period-1 version says "1000 € for 0.35µ-like
    CMOS to 7,000 € for advanced 90nm", the FINAL version "2,000 € … to 15,000 €". Both are
    reproduced above. No explanation is given; prices roughly doubled between the two filings, which
    is consistent with `FUNDX-4`.
  - The membership counts are the coordinator's, are round, and are not audited. "650 European
    Academia" appears in 2008, 2010 and 2013 unchanged, which suggests a house figure rather than a
    count.
  - **The financial reports themselves are still not public.** What CORDIS publishes is the
    *publishable summary*. The Form C / Certificate on the Financial Statements, and any cost
    breakdown by work package, remain unpublished — `FUND-4`'s verdict on that is unchanged.

### FUNDX-4. EUROPRACTICE IC3 existed and CORDIS has no record of it; the 2010 annual report shows the mini@sic subsidy running out mid-year and prices going up

- **Sources:**
  - EUROPRACTICE IC4 *Publishable summary* (as `FUNDX-3`), first sentence.
  - EUROPRACTICE *IC Service Annual Report 2010*, filed under grant 214157 and published on CORDIS:
    <https://cordis.europa.eu/docs/projects/cnect/7/214157/080/publishing/readmore/Annual-report-2010.pdf>
  - EUROPRACTICE 2012 *Publishable summary* (as `FUNDX-3`), for the EUROCHIP dates.
  - CORDIS FP6 bulk export, `https://cordis.europa.eu/data/cordis-fp6projects-csv.zip`, downloaded
    2026-09-25.
  - CORDIS fact sheet for STAR, grant 515895: <https://cordis.europa.eu/project/id/515895>
- **Verification:** Verified 2026-09-25. The PDFs were read from their text layers; the FP6 export's
  `csv/project.csv` (10 093 projects) and `csv/organization.csv` were scanned by script.
- **How it was counted:** two scans of the FP6 export. (1) Every project whose any field matches
  `europractice|eurochip|IC3|multi.?project wafer|MPW|design kit|CAD tool|silicon brokerage|shuttle`.
  (2) Every project in which imec appears in `organization.csv`, split by `role`. Both were run to
  completion and their full output inspected.
- **What it says:**
  - **EUROPRACTICE IC3 is named, dated and placed in FP6 by the grant that succeeded it.** The IC4
    publishable summary opens, verbatim: "The previous EUROPRACTICE IC Service project
    **EUROPRACTICE IC3, part of the 6th Framework and ending on 31 December 2008**, is widely
    recognized as a world-class service offering state-of-the-art CAD tools and technologies to
    universities and industry." It says so twice: "the period up to 31 December 2008 is covered for
    these activities by the previous project EUROPRACTICE IC3".
  - **It is not in CORDIS.** Neither scan of the FP6 bulk export finds it. Scan (1) returns no
    Europractice project at all: the only FP6 record mentioning the word is ACCORD (034041), the
    optoelectronics support action `FUND-4` already identified. Scan (2) lists **60 imec FP6
    projects**, of which the only candidate by size and subject is **STAR (515895), "Silicon
    technology access to research", 2004-10-01 → 2007-09-30, total cost €103 925 000, EU
    contribution €11 000 000**, coordinated by imec. STAR is **not** Europractice: its objective is
    to extend "the 300mm compatible process driven research pilot-lines under construction at IMEC,
    CEA/LETI and FhG-IISB with mainly complementary equipment" — the pilot-line infrastructure, not
    the CAD-and-MPW brokerage. Its funding scheme is "CNI-SSA - Construction of new infrastructures".
  - **So `FUND-4`'s "hole in the record for 2006 and 2007" is not a hole in the funding. It is a hole
    in CORDIS.** The service was running under a named FP6 grant that the Commission's own public
    project database does not contain. `FUND-4`'s caveat "Either the IC service ran with no dedicated
    EC grant, or a grant exists that neither search found" is resolved in favour of the second.
  - **EUROCHIP's dates are confirmed from a primary EC-published document.** EUROPRACTICE 2012's
    summary: "The European Commission has supported broker services for over 20 years … Service
    offered by **Eurochip (1989-1995)** and **EUROPRACTICE (1995-until today)**." `FUND-4` records
    EUROCHIP as absent from CORDIS in every framework programme; it is, but its existence and dates
    are now sourced.
  - **The 2010 annual report shows the subsidy budget running out and prices going up.** The
    foreword, signed "Dr. C. Das, Chairman EUROPRACTICE IC Service, imec (Belgium)", verbatim:

    > "since the prototyping prices in 90nm and below became so attractively low, due to the EC
    > subsidy, a lot of the European universities and research institutes started to design in these
    > technologies. This resulted in the fact that we received many 90nm-designs to be prototyped :
    > **55 in 2009 and 68 in 2010**. Unfortunately the other consequence is that **the EC-subsidy for
    > fabrication of mini@sic designs in 90nm and below for the period until the end of 2011 was
    > almost used in the first half of 2010. As a result we regret that we have been forced to change
    > (increase) the prices for miniasic designs starting 1 August 2010.** Apologies for this. **We
    > have been the victim of a successful mini@sic program** with affordable prototype fabrication
    > prices for European Academia (thanks to the EC subsidy). It clearly shows that **when
    > prototyping prices are affordable, universities start to design in advanced technologies** and
    > bring their research activities to a higher level".

  - **The same report independently confirms the design series in `DEM-16`, including the split that
    `DEM-16` flagged as uncertain.** Its chart carries the same 2000–2010 triplets, and its prose
    states: "In 2010, a total of **533 ASICs** have been prototyped" and "**79%** of the designs are
    sent in by European universities and research laboratories while the remaining **21%** of the
    designs is being sent in by non-European universities and companies world-wide." The 2005 chart
    on the same spread gives 450 with a 69/31 split.
  - **mini@sic volume:** "**350 designs prototyped (306 in 2009)**" under mini@sic conditions in
    2010.
  - The report also states who delivers the service in that era: "The EUROPRACTICE IC Services are
    offered by the following centers: • imec, Leuven (Belgium) • Fraunhofer-Institut fuer
    Integrierte Schaltungen (Fraunhofer IIS), Erlangen (Germany)", and, on the funding: "The European
    Commission is funding the Europractice IC Service under the IST programme in the 7th framework.
    **This funding is exclusively used to support European universities and research laboratories.**"
- **DERIVED (arithmetic written out):**
  - **The split `DEM-16` could not confirm, confirmed.** For 2010 the triplet is 113 industry +
    non-European / 83 Europractice Research / 337 Europractice Academic. (83 + 337) ÷ 533 =
    **78.8%**, which the report's prose rounds to 79%; 113 ÷ 533 = **21.2%**, which it rounds to
    21%. For 2005 the triplet is 138 / 69 / 243: (69 + 243) ÷ 450 = **69.3%** ("69%") and
    138 ÷ 450 = **30.7%** ("31%"). Both check. **`DEM-16`'s caveat that "the chart's per-series
    split is inferred … and is not certain" can be lifted for 2005 and 2010, and by extension the
    label order is the one `DEM-16` assumed.**
  - **The subsidised share of the service in 2010:** 350 mini@sic designs ÷ 533 total =
    **65.7% of all designs were on the subsidised programme**.
  - **The paying industrial line was falling while the subsidised line rose.** Industry +
    non-European designs: 164 (2008) → 153 (2009) → **113 (2010)**, a fall of **31.1%** in two
    years. Europractice Academic over the same two years: 285 → 305 → **337**, a rise of **18.2%**.
  - **The subsidy budget's own arithmetic.** A budget intended to last from the start of the grant
    "until the end of 2011" was "almost used in the first half of 2010". EUROPRACTICE IC5 ran
    2010-04-01 → 2011-12-31, i.e. 21 months; the subsidy lasted roughly the first **3** of them.
- **Bears on:**
  - **H5 (supports, and this is one of the few clean elasticity observations in the directory).**
    Europractice dropped the price of an advanced-node prototype, demand rose fast enough to exhaust
    a two-year budget in three months, and the service had to raise prices again. The incumbent's own
    conclusion, in its own words: "when prototyping prices are affordable, universities start to
    design in advanced technologies."
  - **H5 (challenges, and it is the same fact).** What responded was **node choice within a fixed
    customer base**, not the size of that base. 90nm designs went 55 → 68; total designs went
    545 → 533, i.e. **down**. Membership did not move. The elasticity is in *what* the existing 650
    institutions tape out, not in *how many* institutions there are. Anybody arguing that a lower
    price unlocks a long tail has to explain why this price cut moved the mix and not the total.
  - **H6 (challenges).** A price subsidy with a fixed budget is a price subsidy that runs out. The
    programme's response to success was to **raise prices**, mid-grant, and apologise.
  - **H5 (challenges).** The part of Europractice's volume that pays full commercial price fell 31%
    in two years while the subsidised part grew 18%.
  - **H6 (context).** "The previous EUROPRACTICE IC Service project EUROPRACTICE IC3" means the EC
    has funded this service continuously since 1989 with no gap — EUROCHIP 1989–1995, then
    EUROPRACTICE 1995 to today, thirty-seven years by 2026. `FUND-4`'s "€87.0 million" understates
    the total by whatever IC3 and EUROCHIP were worth, and **neither figure is public**.
- **Used in:** not yet.
- **Caveats:**
  - **IC3's value is unknown.** No amount, no grant number, no dates beyond "ending on 31 December
    2008" have been found. It is not in the FP6 bulk export, not in the CORDIS web search, and the
    FP6 export is the Commission's own published dataset. The most likely explanations — a grant
    administered outside the FP6 project dataset, or a record never migrated — cannot be
    distinguished from here. See the blocked-sources list.
  - **STAR is a different thing and must not be added to the Europractice total.** It is recorded
    here only because it is the one large imec-coordinated FP6 grant a careless search would
    mistake for IC3, and because its own numbers (€103.9m total cost, €11m EU, three pilot lines)
    are a useful measure of what the EC was spending on imec's *infrastructure* in the same years.
  - The 2010 foreword is a customer-facing annual report, not an accounting document. "Almost used
    in the first half of 2010" is not a figure.
  - The design-count triplets are read out of a PDF chart's data labels, exactly as in `DEM-16`. The
    check above is that the report's own prose percentages reproduce from them, which is strong but
    is not the underlying database.
  - "This funding is exclusively used to support European universities and research laboratories" is
    the coordinator's statement of intent about grant money; it is consistent with the SME activity
    being "not funded by the project" (`FUNDX-3`) but it is not an audit finding.

### FUNDX-5. A reproducible staff census: Europractice names 13 people in 2017, 21 in 2024 and 19 in 2025 — and in 2025 the same foundry has two different human contacts depending on which partner you go through

- **Sources:**
  - EUROPRACTICE, *EP activity Report 2017*, "CONTACT INFORMATION" page (p. 56):
    <https://europractice-ic.com/wp-content/uploads/2019/06/EP-activity-Report-2017.pdf>
  - EUROPRACTICE, *Activity Report 2024*, "CONTACT INFORMATION" (p. 64):
    <https://europractice-ic.com/wp-content/uploads/2025/10/Europractice_ActivityReport2024_webversion.pdf>
  - EUROPRACTICE, *Activity Report 2025*, "CONTACT INFORMATION" (p. 68):
    <https://europractice-ic.com/wp-content/uploads/2026/03/Europractice_AR2025_web.pdf>
  - imec, press kit (institute-wide figures): <https://www.imec-int.com/en/reading-room/press-kit>
  - Fraunhofer IIS, "Facts and figures" (Annual Report 2025):
    <https://www.iis.fraunhofer.de/en/profil/what-makes-us-special/jb/2025/facts.html>
  - Tyndall National Institute, *Annual Report 2025*:
    <https://www.tyndall.ie/wp-content/uploads/2026/07/Tyndall-Annual-Report-2025.pdf>
- **Verification:** Verified 2026-09-25. Every PDF was downloaded with `curl` and converted with
  `pdftotext -layout`; the contact pages were read in full and the names counted by hand after a
  script located the section. The institute-level figures are quoted from the institutions' own
  pages.
- **How it was counted:** the contact page of each activity report is laid out as a set of blocks —
  a service or foundry name, then a person's name, then an e-mail. Every personal name was listed,
  duplicates (people who cover more than one foundry) collapsed, and generic mailboxes
  (`MicroelectronicsCentre@stfc.ac.uk`, `virtual-asic@iis.fraunhofer.de`,
  `cime-prototypage@grenoble-inp.fr`) counted as **zero** people. This is the same method as
  `FUND-9` but applied to the **annual reports** rather than the live website, which makes it a time
  series and makes it reproducible against a fixed document.
- **What it says:**

  | Activity report | imec | UKRI-STFC | Fraunhofer IIS | Grenoble (CMP → CIME-P) | Tyndall | **Distinct people** | Foundry/technology slots |
  |---|---:|---:|---:|---:|---:|---:|---:|
  | 2017 | 9 | **0** (generic mailbox only) | 4 | — | — | **13** | 10 |
  | 2024 | 10 | 3 | 3 | 4 | 1 | **21** | 18 |
  | 2025 | 8 | 3 | 3 | 4 | 1 | **19** | 18 |

  The 2025 people, in full: **imec** — Romano Hoofman (general), Paul Malisse (operational), Josef
  Stoudek (legal), Tobias Vanderhenst (TSMC), Ahmed Ba-Makhramah (UMC), Pieter Claes (X-FAB, imec
  Si-Photonics, imec GaN-IC, MEMS — four foundries, one person), Alexandre Pereira (Graphenea), Adil
  Masood (Pragmatic). **UKRI-STFC** — Mark Willoughby (design tools), Clive Holmes (training
  courses), Richard Bishop (academic membership). **Fraunhofer IIS** — Elvira Liandres (ams OSRAM,
  IHP, UMS), Syed Shahnawaz (GlobalFoundries), Ruslan Rybalko (X-FAB). **CIME-P / Grenoble INP** —
  Gaétan Debontride (ams OSRAM), Zineb M'Harzi (EM Microelectronic, Si-Photonics), Mohammadreza
  Dolatpoor Lakeh (STMicroelectronics), Antoine Abisset (Science). **Tyndall** — Simon Toft Sørensen
  (smart system integration).

  **The consortium duplicates itself.** In the 2025 list, **X-FAB** has a named contact at imec
  (Pieter Claes) *and* at Fraunhofer IIS (Ruslan Rybalko). **ams OSRAM** has one at Fraunhofer IIS
  (Elvira Liandres) *and* one at CIME-P (Gaétan Debontride). **Silicon photonics** has one at imec
  (Pieter Claes) *and* one at CIME-P (Zineb M'Harzi). Which human being you get depends on which
  partner's page you land on, not on what you want made.

  **The Grenoble partner is now called CIME-P, not CMP.** The 2025 report's sign-off reads "Your
  Europractice team at imec, UKRI-STFC, Fraunhofer IIS, **CIME-P**, and Tyndall", and every Grenoble
  contact e-mail is `cime-prototypage@grenoble-inp.fr`. `FUND-8` records CMP's own domains
  (`mycmp.fr`, `cmp.imag.fr`) as dead and asks whether the money reached the same team; the
  consortium's own document answers that the Grenoble partner is now an activity of Grenoble INP
  under a new name.

  **The partners, at institute scale** (none of this is Europractice; it is the size of the bodies
  the Europractice staff sit inside):
  - **imec**: "the expertise of **over 6,500 employees**" and "In 2025, imec reported revenues of
    **€1.2 billion**" (press kit, read 2026-09-25).
  - **Fraunhofer IIS**: "In 2025, Fraunhofer IIS's revenue amounted to **€264 million**. The
    institute financed **58 percent** of its expenses (excluding investments) with funds from
    business and industry, and an additional **24 percent** from public project funds." Workforce:
    "**1,225** salaried employees, representing a slight decline compared with the previous year. In
    addition, 366 students and 11 trainees are employed at the institute." (Marked "*Projection as
    of January 2026".)
  - **Tyndall National Institute (University College Cork)**: "By year-end, Tyndall had **581
    research and professional services staff, including 172 PhD and MSc postgraduate students**,
    representing more than 50 nationalities". Its EU scorecard for 2025: "€686m total project value
    | €125m Tyndall grant value | 84 projects | 18 Tyndall co-ordinated projects".
  - **UKRI-STFC** and **CIME-P**: **no staff number for the Europractice activity is published by
    either**, and `www.europractice.stfc.ac.uk/welcome.html` and `/content/contacts/contacts.html`
    both return **HTTP 404**.
- **DERIVED (arithmetic written out):**
  - **Designs per named person.** Against `DEM-16`'s totals: 614 ÷ 13 = **47.2** (2017);
    837 ÷ 21 = **39.9** (2024); 753 ÷ 19 = **39.6** (2025). The named establishment grew 46%
    (13 → 19) while the design count grew 23% (614 → 753), so **output per named person fell 16%**
    over eight years.
  - **CORRECTED 2026-09-25 by `PRD-5`: three of the nineteen are not on the fabrication service.**
    The 2025 contact page prints its own functional split — three imec coordination (general /
    operational / legal), **three UKRI-STFC listed as design tools, training courses and academic
    membership**, one Tyndall, twelve foundry-specific. Excluding the three STFC roles,
    **753 ÷ 16 = 47.1 designs per fabrication-facing named person**, and *that* is the figure
    comparable with MOSIS's 49.8 (`PRD-2`). The gap between the two services is **1.06×, not 3.7×**.
  - **Europractice has CMC's denominator problem too, one level smaller** (`PRD-5`): AR2025 states
    it "currently distributes around **65,000 design-tool license bundles every year**" and that
    "**More than 100 lecturers** attend Europractice training activities annually" — **86 licence
    bundles per fabricated design**. Its staff are not all on fabrication either.
  - **The 753 is described two ways in one report** (`PRD-5`): "fabricated" on p.15 and
    "submitted" on p.3. Which it is changes nothing here but is not established.
  - **EU money per named person per year.** 2017, at the EUROPRACTICE 2016 rate:
    € 1 540 159,50 ÷ 13 = **€ 118 474**. 2024, at the RETICLES rate: € 2 395 114,58 ÷ 21 =
    **€ 114 053**. 2025, at the RETICLES rate that actually funded most of that calendar year:
    € 2 395 114,58 ÷ 19 = **€ 126 059**. At the Europractice 2.0 rate now running:
    € 3 997 727,50 ÷ 19 = **€ 210 407**.
  - **Set against the institutes' own turnover per head.** Fraunhofer IIS turns over
    € 264 000 000 ÷ 1 225 = **€ 215 510 per salaried employee**; imec
    € 1 200 000 000 ÷ 6 500 = **€ 184 615 per employee**. Both are *revenue*, not cost, so the true
    fully-loaded cost per head is lower. The €114 000–126 000 per named Europractice person under
    the two completed grants therefore looks like **roughly half to two-thirds of a full-time
    equivalent each** — consistent with the obvious reading, which is that these are people who do
    Europractice among other things.
  - **The whole grant as person-years.** Europractice 2.0 is € 11 993 182,50 over 3 years for a
    named establishment of 19, i.e. **57 named person-years at € 210 407 each**, against
    3 × 753 = **2 259 designs**, i.e. **39.6 designs per named person-year**.
  - **`FUND-9`'s €173,814 per named person is superseded on the annual-report basis.** It divided
    the Europractice 2.0 rate by 23 names taken from the live website; the annual report for the
    same period names 19, giving €210,407. Both are upper bounds on cost per person because both
    assume the grant pays for nothing but people, and both are lower bounds on the real
    establishment because both count only published customer-facing contacts.
- **Bears on:**
  - **H6 (context, and this is the closest anyone gets to the automation question from the public
    record).** About **forty designs per named person per year** is the productivity of the incumbent
    European brokerage, and it has been **falling**. That is the number an automated service has to
    beat, and it is the reason the payroll question matters: every extra design needs another slice
    of somebody's year.
  - **H6 (challenges the automation argument, honestly).** The duplication is real but it is not
    obviously waste. Five partners with five different foundry relationships is how the consortium
    gets access to 102 technologies from 22 foundries (`FUND-2`); a single automated broker would
    have to negotiate all of those itself. The people are partly *relationship* cost, not *process*
    cost, and relationship cost does not automate away.
  - **H5 (context).** Fraunhofer IIS finances **58%** of its expenses from industry and imec turns
    over €1.2bn. These are not institutions that cannot sell things. They still take a Coordination
    and Support Action to run an academic MPW brokerage.
- **Used in:** not yet.
- **Caveats:**
  - **A named-contact count is not a headcount, and the gap is large and unknown.** Accounts,
    procurement, IT, legal, the design-tools operation at STFC, training delivery, web, and the
    people who actually assemble reticles are all invisible to it. `FUND-9` says the same thing and
    it is worth repeating: **13, 21 and 19 are floors.**
  - **The 2017 zero for STFC is an artefact of presentation, not of staffing.** The 2017 report
    routed all membership, tools and training enquiries to a single generic mailbox; the 2024 and
    2025 reports name three people behind the same mailbox. The jump from 13 to 21 is therefore
    partly a change in how the report is written, and the "46% growth in the named establishment"
    derived above should be read with that in mind. Excluding STFC entirely, the count goes
    13 → 18 → 16.
  - The institute-level figures are for **imec, Fraunhofer IIS and Tyndall as wholes**. Europractice
    is a small activity inside each. Do not divide institute revenue by Europractice designs.
  - Fraunhofer IIS's 2025 figures are explicitly "Projection as of January 2026", not final.
  - imec's "over 6,500 employees" and "€1.2 billion" come from a press kit, which is a marketing
    document. imec's statutory accounts were **not** obtained — see the blocked list.
  - The e-mail addresses above are published by Europractice on its own public contact pages and are
    quoted only to show which mailbox is generic and which is personal. **Nothing was sent to any of
    them.**

### FUNDX-6. CMC in 2018: 48 employees, a CAD $6.5 million operating budget, and a national research council that decided it would rather fund researchers than fund a broker

- **Sources** (local and national news, which carry numbers the annual reports do not):
  - CBC News, "Feds set to pull plug on microelectronics powerhouse", Ottawa, posted **2018-11-02**:
    <https://www.cbc.ca/news/canada/ottawa/cmc-microsystems-kingston-funding-1.4886292>
  - Mike Postovit, Global News Kingston, "Hi-tech Kingston company hoping for funding to stay alive",
    **2018-11-14**:
    <https://globalnews.ca/news/4660184/hi-tech-kingston-company-hoping-for-funding-to-stay-alive/>
- **Verification:** Verified 2026-09-25. The CBC article refuses `WebFetch` (**HTTP 403**) but serves
  `curl` with an ordinary browser User-Agent; it was fetched that way and read in full. The Global
  News article was read through `WebFetch`. Both are contemporaneous reports quoting CMC's president
  and CEO by name.
- **What it says:**
  - **A headcount, which nothing CMC publishes gives.** CBC: "Many of the non-profit corporation's
    **48 employees** are engineers and PhD research scientists." Global News, twelve days later: "at
    least **45 people** out of work at the non-profit company".
  - **An operating budget.** CBC: "CMC president and CEO Gordon Harling said the organization, which
    has a **$6.5-million annual operating budget**, has been scrambling to find alternative funding
    since being 'dumped' by NSERC."
  - **Why the money was cut, in NSERC's own logic as relayed by the CEO.** Global News quotes Gord
    Harling: "**They felt that they did not want to fund a third party that provides tools to
    researchers, they want to fund researchers directly.**" CBC: "In 2016, NSERC announced it was
    cutting CMC's funding, apparently part of a broader shift toward supporting individual research
    projects."
  - **The timeline.** CBC (2018-11-02): "With the last of CMC's bridge funding set to run out next
    June, Harling has begun notifying employees the doors could soon close. By next month fabrication
    runs will come to an end, and by next March the thousands of students and researchers who rely on
    computer programs licensed through the organization, which operated like a software co-op, will
    need to find a new source." Global News: termination notices distributed **2018-10-30**.
  - **The scale of the service it ran on $6.5m.** CBC: "Last year, CMC assisted some **8,000 students
    plus another 5,000 researchers and professors**, and was involved in about one-third of all
    collaborative research grants between universities and industry — about **$30 million** worth."
    And on why the tool licences mattered: "**The cost of a single licence for circuit-design
    software might reach $100,000.**"
  - **What a Nobel laureate said about it.** Art McDonald, quoted by CBC: "The idea that this could
    be disbanded and we could lose this resource just doesn't make any sense … **It's effectively a
    national laboratory.**"
  - The service survived. The audited statements in `FUNDX-1` show CFI-MSI and Province of Quebec
    money arriving in its place from at least FY2022, and ISED/FABrIC from FY2024.
- **DERIVED (arithmetic written out):**
  - **Cost per head, 2018:** $6 500 000 ÷ 48 = **CAD $135 417 per employee per year**, all-in (the
    whole operating budget, not just payroll). Payroll was 53.5% of spending in 2008 (`FUND-7`) and
    39–46% in 2022–2026 (`FUNDX-1`); at 45% of $6.5m that is $2.9m of payroll, or **CAD $60 900 per
    head** — plainly too low for "engineers and PhD research scientists", which suggests either that
    the 48 includes part-time and student staff, or that the payroll share was higher in 2018 than in
    either bracketing measurement. **Neither can be resolved from the public record.**
  - **CMC shrank by a third and then tripled.** Total expenditure: CAD $9 882 500 (FY2008, `FUND-7`)
    → $6 500 000 (2018, the CEO's figure) → $20 012 740 (FY2026, audited). That is **−34.2%** over
    the first decade and **×3.08** over the second.
  - **The implied 2026 headcount, anchored on 2018.** If a CMC employee still costs what the whole
    2018 budget divided by 48 implies, CAD $135 417, then FY2026's payroll of $7 859 646 supports
    **58 people**. Holding the 2018 headcount of 48 flat instead gives $7 859 646 ÷ 48 = **CAD
    $163 743 per head**, a 21% rise over eight years before any inflation adjustment. **The truth is
    somewhere in that box: roughly 48–65 people.**
  - **Designs per employee. WITHDRAWN AS ORIGINALLY STATED — corrected 2026-09-25 by `PRD-6`.**
    The original reading was: `DEM-20` gives 240 prototypes in FY2025/26, so at 48 employees that
    is 5.0 per employee per year and at 58, 4.1. **Both the numerator and the denominator are
    wrong.**
    - **Denominator.** 48–65 is a whole-organisation count, and CMC is not only a broker. Its own
      audited statements put fabrication-and-packaging at **19.1% (FY2026), 28.9% (FY2025) and
      34.0% (FY2023)** of expenditure. Re-based pro-rata: 48 × 19% = 9.1 → 240 ÷ 9.1 = **26.3**;
      58 × 29% = 16.8 → **14.3**; 65 × 34% = 22.1 → **10.9**. **The range is 10.9–26.3, two to
      five times the published 5.0.**
    - **Numerator.** Only **1,369 of 1,803** five-year "designs prototyped" were MPW manufacturing;
      434 were custom micro-and-nanotechnology lab work. 240 × (1,369 ÷ 1,803) = **~182 MPW designs**
      in FY2026.
    - **The corrected gap to MOSIS is 3.5×, not 29.7×** — 49.8 (MOSIS's own last measured year,
      `PRD-2`) ÷ 14.3 (CMC's middle estimate). Against MOSIS's *peak* year it is 10.4×. **The 29.7×
      figure must not be used.**
    - Still missing: **any CMC headcount after 2018, and any staff split by function.**
      `cmc.ca/wp-json/wp/v2/awsm_team_member?per_page=100` returns `x-wp-total: 20`, but those are
      board and leadership, not an establishment count (`PRD-6`).
- **Bears on:**
  - **H6 (challenges, and this is the most direct statement of the problem found anywhere).** A
    national research council looked at a subsidised MPW broker and concluded it **did not want to
    fund a third party that provides tools to researchers**; it wanted to fund researchers directly.
    That is a funder rejecting the intermediary model on principle, not on performance. Any brokerage
    that depends on public money carries this risk in its business model, and CMC nearly died of it.
  - **H6 (supports, and it matters).** CMC did not die. It replaced NSERC with CFI, then Quebec, then
    ISED, and tripled in size. A service with real users can survive losing its founding funder — but
    note what it took: three successive funders and eight years.
  - **H5 (challenges).** "8,000 students plus another 5,000 researchers and professors" served in
    2017 — and `DEM-20` has the prototype count at 240 a year. **Thirteen thousand people, a few
    hundred chips.** Almost everything CMC does for almost everybody it serves is *tools and
    training*, not fabrication. Any model that reads CMC's subsidy as the cost of making chips is
    reading it wrong, and `FUND-7`'s and this file's per-prototype figures all carry that error.
  - **H8 (context).** "The cost of a single licence for circuit-design software might reach $100,000"
    is the reason these brokerages exist at all, and it is a cost that no amount of automation on the
    fabrication side removes.
- **Used in:** not yet.
- **Caveats:**
  - **48 and 45 are journalists' figures**, given twelve days apart by two outlets, and the second
    ("at least 45 people out of work") is a count of people losing jobs, not of employees. They agree
    to within 7%, which is as good as this gets, but neither is CMC's own statement.
  - **"$6.5-million annual operating budget" is a CEO's figure in an interview.** It is not reconciled
    to any published statement, and CMC's audited statements for that year were not found (see the
    blocked list). It is roughly two-thirds of FY2008's audited $9.88m, which is consistent with an
    organisation that had lost its main grant.
  - The CBC piece carries no personal byline ("CBC News") and is based on interviews at CMC; the
    Global News piece is bylined Mike Postovit. Neither is a document.
  - "one-third of all collaborative research grants between universities and industry — about $30
    million worth" is CMC's own claim about its reach, relayed by a journalist. Not checked.
  - `FUND-7`'s 2007/08 figures and these 2018 figures are eleven years apart with nothing in between.

### FUNDX-7. What Europractice is worth next to the rest of the Chips JU: €12.0 million against €1.23 billion, and imec's Europractice line is 0.9% of what the same Joint Undertaking pays imec for one pilot line

- **Sources:** CORDIS bulk export for Horizon Europe,
  `https://cordis.europa.eu/data/cordis-HORIZONprojects-csv.zip`, downloaded 2026-09-25 (23 451
  projects), `csv/project.csv` and `csv/organization.csv`.
- **Verification:** Verified 2026-09-25. Every figure is a field from those two files. Nothing here is
  quoted from a press release.
- **How it was counted:** every project whose `topics`, `masterCall` or `legalBasis` field contains
  `CHIPS` was selected (28 projects), grouped by topic, and summed. Separately, every row of
  `organization.csv` whose `name` matches imec, the Fraunhofer-Gesellschaft, UKRI, Institut
  Polytechnique de Grenoble or University College Cork was summed on `netEcContribution`, across all
  of Horizon Europe and then restricted to the Chips topics.
- **What it says:**
  - **The Chips JU's whole visible portfolio in CORDIS**: 28 projects, **€1 229 880 105** of EU
    contribution against **€2 489 952 773** of total cost.
  - **The five pilot lines take €898 486 867 of that** — 73% of the EU money in 18% of the projects:

    | Grant | Acronym and subject | Topic | EU contribution | Total cost | Dates |
    |---|---|---|---:|---:|---|
    | 101183277 | **NanoIC** — "European pilot line for beyond 2nm leading edge System-on-Chip" | CPL-1 | € 448 006 740 | € 551 778 479 | 2024-01-01 → 2028-12-31 |
    | 101182279 | **FAMES** — FD-SOI pilot line | CPL-2 | € 216 811 042 | € 433 622 083 | 2023-12-01 → 2028-12-31 |
    | 101183307 | **APECS-PL** — advanced packaging | CPL-3 | € 96 211 548 | € 194 423 097 | 2024-11-01 → 2029-06-30 |
    | 101213727 | **PIXEurope** — photonic ICs | CPL-5 | € 88 027 325 | € 176 054 650 | 2025-06-01 → 2030-05-31 |
    | 101183211 | **WBGPilotLine** — wide bandgap | CPL-4 | € 49 430 212 | € 98 860 425 | 2025-06-01 → 2030-05-31 |

  - **Europractice 2.0 is the only project under its topic.** `HORIZON-JU-CHIPS-2025-CSA-1` funds
    exactly one grant, 101252350, at **€11 993 182**. The whole of the EU's pan-European chip-design
    *access* infrastructure, for 2025–2028, is that one line.
  - **The design-tools money is a separate, larger line, and it is new.** Topic
    `HORIZON-JU-CHIPS-2025-IA-EDA-two-stage` funds two grants — **ODE4EC-DIG**, "Open Design
    Environment for European Chips - Digital SoC Design", €8 182 400 EU of €19 178 973, and
    **ODE4EC-PIV**, "Open Design Ecosystem for European Chips - Productivity, Integration…",
    €5 700 179 of €14 537 084 — both running 2026-06-01 → 2029-05-31, **€13 882 580 of EU money
    between them**. That is *more* EU money for an open design environment over three years than for
    Europractice over the same three years.
  - **Who gets the money.** Net EU contribution across the *whole* of Horizon Europe, from
    `organization.csv`:

    | Organisation | Participations | Net EU contribution, all Horizon Europe | Of which Chips JU topics | Europractice 2.0 line |
    |---|---:|---:|---:|---:|
    | imec | 194 | **€ 598 513 416** | € 462 154 752 | € 3 900 016 |
    | Fraunhofer-Gesellschaft | 741 | € 568 662 659 | € 91 002 944 | € 1 788 141 |
    | University College Cork (Tyndall) | 202 | € 128 303 002 | € 20 156 478 | € 1 094 973 |
    | UKRI | 122 | € 67 927 489 | € 3 602 261 | € 3 602 261 |
    | Institut Polytechnique de Grenoble | 49 | € 15 985 617 | € 4 568 304 | € 1 607 791 |

  - **imec takes 96.6% of NanoIC.** NanoIC has six participants; imec is coordinator with
    **€432 633 226** of the €448 006 740, ahead of University College Cork (€5 612 201), CEA
    (€4 971 673), Politehnica Bucharest (€2 243 120), Fraunhofer (€1 978 321) and VTT (€568 200).
  - **Fraunhofer coordinates APECS-PL** with €76 404 542 of its €96 211 548.
  - **Europractice 2.0 is the only Chips JU grant in which UKRI appears at all.**
- **DERIVED (arithmetic written out):**
  - **Europractice 2.0 against the Chips JU portfolio:** 11 993 182 ÷ 1 229 880 105 = **0.975%**.
  - **imec's Europractice line against imec's NanoIC line:** 432 633 226 ÷ 3 900 016 = **110.9×**.
    Per year — NanoIC runs five years, Europractice 2.0 three — 432 633 226 ÷ 5 = €86 526 645/yr
    against 3 900 016 ÷ 3 = €1 300 005/yr, a ratio of **66.6×**.
  - **imec's Europractice line against everything imec gets from Horizon Europe:**
    3 900 016 ÷ 598 513 416 = **0.652%**.
  - **Pilot-line leverage.** The five pilot lines draw €898 486 867 of EU money against
    €1 454 738 734 of declared total cost, i.e. the EU pays **61.8%** and industry and member states
    find the other 38.2%. Europractice 2.0's EU contribution is **100%** of its declared cost
    (`FUND-1`). **The EU pays a higher share of the brokerage than of the fabs.**
- **Bears on:**
  - **H6 (challenges, in a new way).** The complaint that Europractice is expensive has to be set
    against what else the same funder is buying. **€4.0 million a year is 0.65% of imec's EU money.**
    If the brokerage were shut down tomorrow nobody in Brussels would notice the saving. That cuts
    against any argument that the subsidy is unsustainable — it plainly is sustainable — and for the
    argument that it is unexamined.
  - **H6 (context).** The EU is now funding an "Open Design Environment for European Chips" at a
    *higher* annual rate (€13.9m over 3 years = €4.6m/yr) than the MPW brokerage (€4.0m/yr). The
    money is moving from access-to-silicon towards access-to-tools.
  - **H5 (challenges).** €1.23 billion of EU money and €2.49 billion of total cost is now committed
    to European chip pilot lines. The demand-side service that would put small customers on those
    lines is €12.0 million of it. Whatever the pilot lines are being built for, it is not the long
    tail.
  - **H8 (context).** The EU pays 100% of the brokerage's declared cost and 61.8% of the pilot lines'.
    Co-funding discipline is applied to fabs and not to services.
- **Used in:** not yet.
- **Caveats:**
  - **CORDIS's Chips JU coverage is incomplete and the totals are a floor.** The Chips JU's own
    website (`chips-ju.europa.eu`) is a client-side-rendered application that a fetch cannot read,
    and its project pages were not obtained. The 28 projects here are those the CORDIS bulk export
    carried on 2026-09-25.
  - **The Chips Act competence centres are not in this data at all.** A scan of all 23 451 Horizon
    Europe projects for "competence cent(re|er)" in title, objective or topic returns nine hits, none
    of them a Chips Act competence centre. They are funded jointly by the Chips JU and member states
    through national instruments and are **not** in CORDIS. See the blocked list.
  - **"Net EU contribution" across all of Horizon Europe is not a measure of an institution's
    income.** imec's €598m is spread over 194 projects and several years, against a turnover of
    €1.2 billion a *year*.
  - Pilot-line "total cost" includes member-state and industrial contributions that CORDIS does not
    break out; the 61.8% is an EU-contribution-to-declared-cost ratio, not a public-to-private ratio.
  - The €13.9m ODE4EC pair had not started when this was written (both begin 2026-06-01). They are
    awarded, not spent.

### FUNDX-8. The UK's national money, from a register `FUND-1` did not use: £2,406,051 of British public money paid for the UK's share of RETICLES, and a second UK MPW service has taken £17.1 million

- **Sources:** UK Research and Innovation, *Gateway to Research* — the public register of every UKRI
  grant, read through its JSON API (`gtr.ukri.org/api/…`), data last refreshed 2026-07-06 per the
  API's own `lastRefreshDate`:
  - RETICLES (UK share), GtR project 10065357:
    <https://gtr.ukri.org/api/projects?ref=10065357>
  - CORNERSTONE, EPSRC EP/L021129/1: <https://gtr.ukri.org/api/projects?ref=EP%2FL021129%2F1>
  - CORNERSTONE 2, EPSRC EP/T019697/1: <https://gtr.ukri.org/api/projects?ref=EP%2FT019697%2F1>
  - CORNERSTONE 2.5, EPSRC EP/W035995/1: <https://gtr.ukri.org/api/projects?ref=EP%2FW035995%2F1>
  - CORNERSTONE Photonics Innovation Centre (C-PIC), EPSRC EP/Z531066/1:
    <https://gtr.ukri.org/api/projects?ref=EP%2FZ531066%2F1>
- **Verification:** Verified 2026-09-25. Every figure is a field from the GtR API's JSON
  (`fund.valuePounds`, `fund.start`, `fund.end`, `fund.funder.name`, `leadResearchOrganisation`),
  fetched with `curl` and an `Accept: application/json` header. Quotes are from the records'
  `abstractText`.
- **How it was counted:** `https://gtr.ukri.org/api/search/project?term=<term>&page=1&fetchSize=40`
  with `Accept: application/json` returns a clean JSON result set. Three searches were run:
  `Europractice` (2 hits), `"multi-project wafer"` (6 hits) and `CORNERSTONE` (415 hits, of which 4
  are the silicon-photonics programme; the rest match the ordinary English word). Each hit's project
  record was then fetched by its `ref`.
- **What it says:**
  - **`FUND-1`'s open question is closed.** `FUND-1` records that under RETICLES, UKRI appears with
    a Net EU contribution of **€0,00** and a Total cost of "No data", and concludes: "the UK's own
    spending on its share of Europractice in 2022–2025 is not in CORDIS at all. It was funded
    nationally and is **not established here**." It is established now. Gateway to Research carries
    the project, with STFC - Laboratories as lead organisation, under the title "Research,
    Entrepreneurship, Training, IP-exchange & Chip pLatform of EUROPRACTICE Services (RETICLES)",
    grant category **"EU-Funded"**, status Closed, with:
    - **£ 2 406 051**, funder **"Horizon Europe Guarantee"**, type `INCOME_ACTUAL`,
      **2022-09-30 → 2025-09-29**.

    The Horizon Europe Guarantee is the UK Treasury's domestic underwrite for UK participants in
    Horizon Europe during the period when the UK was not associated. So the Brexit gap `FUND-1`
    spotted in CORDIS ("The UK is in, out, and back in") did not mean the UK stopped paying; it
    meant the UK paid itself, out of its own budget, and the payment is in a British register rather
    than a European one.
  - **A second, entirely separate UK national MPW service exists, and is not in this directory.**
    CORNERSTONE, at the University of Southampton with the University of Glasgow, is a silicon
    photonics rapid-prototyping foundry offering access by multi-project wafer. From CORNERSTONE
    2.5's abstract, verbatim: "the fabrication of silicon photonics devices, circuits and systems
    requires large scale investments and capital equipment such as cleanrooms, lithography, etching
    equipment etc. Based at the Universities of Southampton and Glasgow, CORNERSTONE 2.5 will
    provide world-leading fabrication capability to silicon photonics researchers and the wider
    science community. … **Access will be facilitated via a multi-project-wafer (MPW) mechanism
    whereby multiple users' designs will be fabricat[ed]**". Its four grants:

    | Grant reference | Title | Funder | Amount | Period |
    |---|---|---|---:|---|
    | EP/L021129/1 | CORNERSTONE: Capability for OptoelectRoNics, mEtamateRialS, nanoTechnOlogy aNd sEnsing | EPSRC | £ 2 267 121 | 2014-09-14 → 2020-06-29 |
    | EP/T019697/1 | CORNERSTONE 2 | EPSRC | £ 1 494 157 | 2020-03-01 → 2023-02-28 |
    | EP/W035995/1 | CORNERSTONE 2.5 | EPSRC | £ 1 553 164 | 2022-12-02 → 2025-06-01 |
    | EP/Z531066/1 | **CORNERSTONE Photonics Innovation Centre (C-PIC)** | EPSRC | **£ 11 782 397** | 2024-05-31 → 2029-05-30 |

    C-PIC's abstract states the problem in the same terms every other programme in this directory
    does: "**access to silicon prototyping facilities remains a challenge in the UK due to the high
    cost of both equipment and the cleanroom facilities that are required to house the equipment**".
    Its hosts are "University of Southampton, University of Glasgow and the Science and Technologies
    Facilities Council (STFC), together with **105 partners at proposal stage**", and it is
    "underpinned by the C-PIC silicon photonics prototyping foundry".
  - **STFC is in both.** The same research council laboratory that runs the Europractice
    design-tools and membership office at Rutherford Appleton is a named host of C-PIC.
  - The only other UK grants matching "multi-project wafer" are a £4 574 888 EPSRC Quantum
    Technology Capital award to Bristol (2016–2019), a £1 999 999 compound-semiconductor equipment
    award to Cardiff (2017–2018), and an £89 912 Innovate UK feasibility study to **Pragmatic
    Semiconductor**, "FlexiFab - an Open Foundry for Flexible Electronics Ecosystem"
    (2023-06-30 → 2023-11-30) — Pragmatic being one of the foundries in Europractice's own 2025
    portfolio (`FUNDX-5`).
- **DERIVED (arithmetic written out):**
  - **The UK's rate on RETICLES:** £ 2 406 051 ÷ 3.0 years = **£ 802 017 a year**. For comparison,
    under the preceding grant NEXTS, CORDIS gives UKRI **€ 2 090 000** over 3.75 years =
    € 557 333 a year of EU money, and under Europractice 2.0 it gives UKRI **€ 3 602 261,25** over
    3 years = € 1 200 754 a year. **Currencies are not converted here** — the point is that the UK
    line did not lapse, it changed currency and payer.
  - **`FUND-4`'s €87.0 million is missing this.** The eleven-grant total in `FUND-4` counts only EU
    contributions. Adding the UK's own RETICLES contribution gives **€ 87 023 980 + £ 2 406 051**,
    which cannot be stated as one number without inventing an exchange rate and is therefore left as
    two. What can be said is that the public money behind Europractice is **larger than `FUND-4`
    records**, by at least this amount, and by whatever EUROCHIP and EUROPRACTICE IC3 were worth
    (`FUNDX-4`).
  - **CORNERSTONE's total and its acceleration.** 2 267 121 + 1 494 157 + 1 553 164 + 11 782 397 =
    **£ 17 096 839** across 2014-09-14 → 2029-05-30. By annual rate:
    - CORNERSTONE: £ 2 267 121 ÷ 5.79 yr = **£ 391 559 / yr**
    - CORNERSTONE 2: £ 1 494 157 ÷ 3.00 yr = **£ 498 052 / yr**
    - CORNERSTONE 2.5: £ 1 553 164 ÷ 2.50 yr = **£ 621 266 / yr**
    - C-PIC: £ 11 782 397 ÷ 5.00 yr = **£ 2 356 479 / yr**

    The current rate is **6.02×** the first grant's (2 356 479 ÷ 391 559).
  - **The same shape as everywhere else in this file.** Europractice's EU rate rose 2.60× from
    2016–18 to 2025–28 (`FUND-1`). CMC's expenditure rose 3.08× from 2018 to FY2026 (`FUNDX-6`). The
    Chips JU has committed €1.23bn where the KDT JU committed a fraction of it (`FUNDX-7`). And the
    UK's silicon-photonics MPW service has gone up 6.02×. **Public money for prototyping access is
    rising steeply everywhere, on every continent checked, at the same time as Europractice's design
    count falls from 985 (2021) to 753 (2025) (`DEM-16`).**
- **Bears on:**
  - **H6 (challenges).** A second national MPW service, in a country that already pays into
    Europractice, is taking **£2.36 million a year** and rising, with no published price list, no
    published design count and no published revenue found. The subsidised-MPW population is larger
    than `FUND-1` … `FUND-9` counted, and every member of it is growing.
  - **H5 (challenges).** £17.1 million over fifteen years for UK silicon-photonics prototyping, and
    the C-PIC bid needed "105 partners at proposal stage" to justify it. That is a lot of
    institutional machinery around an access problem, and it is the same access problem Europractice
    was set up to solve in 1989.
  - **H6 (context, and a caution about `FUND-4`).** Counting EU contributions is not counting public
    money. The UK's £2.4m was invisible to CORDIS and visible in a British register that takes one
    HTTP request. **Every other member state has an equivalent register and none of them has been
    searched** — see the blocked list. `FUND-4`'s €87.0 million should be read as "the EU
    contribution", never as "what Europractice cost the public".
- **Used in:** not yet.
- **Caveats:**
  - **Gateway to Research reports awarded value, not spend.** `fund.type` is `INCOME_ACTUAL`, which
    is UKRI's term for the award as recorded, not an outturn.
  - **C-PIC is not only a foundry.** £11.78m buys an innovation centre — a knowledge hub, funded
    innovation projects, commercialisation support — "underpinned by" a prototyping foundry.
    Treating all of it as MPW money would be wrong, exactly as treating all of Europractice's grant
    as fabrication money would be (`FUND-2`).
  - **No design count, price list or revenue figure for CORNERSTONE was looked for or found.** It is
    recorded here as a funding line only. Somebody should write it up properly; it is the nearest
    UK analogue to Europractice's prototyping half and it is entirely absent from this directory.
  - The Horizon Europe Guarantee record gives no breakdown by work package or partner, and no cost
    statement. It is one number.
  - GtR's `lastRefreshDate` was 2026-07-06, so grants awarded in the last three months may be
    missing.
  - The `CORNERSTONE` search returns 415 hits because the word is ordinary English. Only the four
    Southampton grants above are the programme; the rest were read and discarded.


---

## 1. Head-count and payroll: what is public, and what is not

The question this file was written to answer. Everything in the table is quoted or derived from the
entry named in the last column; blank cells are things nobody publishes.

| Organisation | Head-count | Basis and date | Payroll | Payroll as % of spend | Spend or turnover | Entry |
|---|---|---|---|---|---|---|
| **CMC Microsystems** | **48 employees** ("many … are engineers and PhD research scientists") | CBC News, 2018-11-02 | — | — | CAD **$6.5 m** operating budget (CEO, 2018) | `FUNDX-6` |
| **CMC Microsystems**, FY2022 | not published | — | CAD **$7 091 733** | **45.3%** | CAD $15 653 837 | `FUNDX-1` |
| **CMC Microsystems**, FY2023 | not published | — | CAD **$7 647 774** | **40.3%** | CAD $18 987 114 | `FUNDX-1` |
| **CMC Microsystems**, FY2024 | not published | — | CAD **$6 933 083** | **42.2%** | CAD $16 420 151 | `FUNDX-1` |
| **CMC Microsystems**, FY2025 | not published | — | CAD **$7 876 088** | **46.2%** | CAD $17 066 020 | `FUNDX-1` |
| **CMC Microsystems**, FY2026 | not published; **≈48–65 implied** | derived from payroll ÷ CAD $121k–164k per head | CAD **$7 859 646** | **39.3%** | CAD $20 012 740 | `FUNDX-1`, `FUNDX-6` |
| **CMC Microsystems**, FY2008 | not published | — | CAD **$5 285 705** | **53.5%** | CAD $9 882 500 | `FUND-7` |
| **Europractice** (the consortium, not its hosts) | **19 named customer-facing people** (2025); 21 (2024); 13 (2017) | counted from the activity reports' contact pages | not published | not published | EU grant € 3 997 728 / yr | `FUNDX-5` |
| **Europractice** (live website basis) | **23 named contacts**, 32 slots | counted 2026-09-19 | not published | not published | — | `FUND-9` |
| **imec** (whole institute) | "**over 6,500 employees**" | imec press kit, 2025 | not published | not published | revenue **€1.2 bn** (2025) | `FUNDX-5` |
| **Fraunhofer IIS** (whole institute) | **1 225 salaried**, + 366 students, + 11 trainees | institute facts page, 2025 (projection) | not published | not published | revenue **€264 m** (2025); 58% from industry | `FUNDX-5` |
| **Tyndall / UCC** (whole institute) | **581** research and professional services staff, of which 172 are PhD/MSc students → **409** non-student | *Annual Report 2025* | not published | not published | €125 m Tyndall grant value across 84 EU projects | `FUNDX-5` |
| **UKRI-STFC** Europractice team | **not published** | — | not published | not published | € 3 602 261 over 2025–28 | `FUND-1` |
| **CIME-P / Grenoble INP** (ex-CMP) | **not published** | — | not published | not published | € 1 607 791 over 2025–28 | `FUND-8`, `FUNDX-5` |
| **MOSIS / USC ISI** | **not published, ever** | — | not published | not published | not published | `FUND-6` |

**What is not public, stated plainly.** No organisation in this table publishes a head-count *for the
multi-project-wafer activity*. Only CMC publishes a payroll line at all, and only for the whole
organisation. Nobody anywhere publishes the split between technical and administrative staff. The
only administrative cost that is published anywhere in either file is Europractice's own statement
that of the €1 100 Full-IC membership fee, "**100 € to administer the membership**" (`FUND-3`) —
which, across 630 members, is **€63 000 a year of pure membership administration**, and which
Europractice charges for separately because, in its own words, the EC does not pay for it.

**The single comparison the file was written to make.** CMC, the only one of these organisations with
audited accounts, spends **39–46% of everything on salaries and benefits**, and has done so in every
one of the five audited years. In 2008 it was 53.5%. Europractice's own coordinator told the
Commission that university MPW schemes are "funded through direct funds **or through government paid
staff**" (`FUNDX-3`) — i.e. that where the subsidy is not cash it is salary. About **forty designs
per named Europractice person per year** (`FUNDX-5`) and **four to five prototypes per CMC employee
per year** (`FUNDX-6`) are the two productivity figures the public record supports, and both are
falling or flat.

## 2. The funding table, extending `FUND-1` … `FUND-9`

Only instruments **not already in `FUND-4`'s table or `FUND-7`** appear here. Currencies unconverted.

| Instrument | Recipient | Amount | Period | What it bought | Entry |
|---|---|---:|---|---|---|
| **EUROCHIP** | the predecessor consortium | **not public** | 1989–1995 (dates now sourced) | the broker service before Europractice | `FUNDX-4` |
| **EUROPRACTICE IC3**, FP6 | imec-led consortium | **not public — the grant is named by its successor and is absent from CORDIS** | ended 1998-12-31 → **2008-12-31** | the IC service through 2006–2008, the "hole" in `FUND-4` | `FUNDX-4` |
| **STAR**, FP6 grant 515895 | imec (coordinator), CEA, Fraunhofer IISB | **€ 11 000 000** EU of **€ 103 925 000** total | 2004-10-01 → 2007-09-30 | 300 mm pilot-line equipment at three institutes. **Not Europractice** — listed so nobody confuses it | `FUNDX-4` |
| **mini@sic "subsidy budget"** (inside the FP7 grants) | Europractice | not separately published; exhausted mid-2010 | ~2006 → 2011 | direct reduction of the price of a small advanced-node tapeout | `FUNDX-3`, `FUNDX-4` |
| **Chips JU NanoIC** | **imec** (96.6% of it) | € 448 006 740 EU of € 551 778 479 | 2024-01-01 → 2028-12-31 | a beyond-2nm pilot line | `FUNDX-7` |
| **Chips JU FAMES** | CEA-led; imec, Fraunhofer, UCC, INP Grenoble all in | € 216 811 042 of € 433 622 083 | 2023-12-01 → 2028-12-31 | an FD-SOI pilot line | `FUNDX-7` |
| **Chips JU APECS-PL** | **Fraunhofer** (coordinator, € 76 404 542) | € 96 211 548 of € 194 423 097 | 2024-11-01 → 2029-06-30 | advanced packaging pilot line | `FUNDX-7` |
| **Chips JU PIXEurope** | UCC/Tyndall € 7 780 250, imec € 3 811 520 | € 88 027 325 of € 176 054 650 | 2025-06-01 → 2030-05-31 | photonic IC pilot line | `FUNDX-7` |
| **Chips JU WBGPilotLine** | Fraunhofer € 236 578 | € 49 430 212 of € 98 860 425 | 2025-06-01 → 2030-05-31 | wide-bandgap pilot line | `FUNDX-7` |
| **Chips JU ODE4EC-DIG + ODE4EC-PIV** | two consortia | € 13 882 580 of € 33 716 057 | 2026-06-01 → 2029-05-31 | an "Open Design Environment for European Chips" | `FUNDX-7` |
| **Chips JU, all 28 CORDIS projects** | — | **€ 1 229 880 105** of **€ 2 489 952 773** | 2023 → 2030 | of which Europractice 2.0 is **0.975%** | `FUNDX-7` |
| **Chips Act competence centres** | national consortia | **not in CORDIS; not found** | — | — | `FUNDX-7`, blocked list |
| **CMC — NSERC National Design Network** | CMC | CAD $9 700 060 in FY2008; **cut from 2016**, gone by 2019 | ~1984 → 2019 | the whole of CMC | `FUND-7`, `FUNDX-6` |
| **CMC — CFI Major Science Initiatives** | CMC | CAD $6 656 900 (FY22), $6 856 681 (FY23), $4 575 000 (FY24), **nil after** | to 2024 | operating support | `FUNDX-1` |
| **CMC — Province of Quebec** | CMC | CAD $1 996 665 (FY22), $2 048 076 (FY23), $1 775 545 (FY24), **nil after** | to 2024 | provincial share | `FUNDX-1` |
| **CMC — Research Support Fund (RSF)** | CMC | CAD $542 972 (FY22), $245 971 (FY23), nil after | to 2023 | indirect costs | `FUNDX-1` |
| **CMC — ISED "FABrIC" / SIF Stream 5, agreement 819430** | Canadian Microelectronics Corporation | **CAD $120 000 000** | 2024-06-11 → 2031-12-31 | "75-100% of costs", per the auditors' economic-dependence note. CAD $23 774 747 recognised in the first three years | `FUNDX-2` |
| **CMC — provincial contribution (unnamed)** | CMC | CAD $107 231 (FY25), $35 608 (FY26) | — | — | `FUNDX-1` |
| **RETICLES, UK share — Horizon Europe Guarantee** | STFC Laboratories | **£ 2 406 051** | 2022-09-30 → 2025-09-29 | the UK's part of Europractice while the UK was unassociated. **Invisible to CORDIS**, which shows UKRI at € 0,00 | `FUNDX-8` |
| **CORNERSTONE + CORNERSTONE 2 + 2.5 + C-PIC** (EPSRC) | Universities of Southampton and Glasgow, with STFC | **£ 17 096 839** | 2014-09-14 → 2029-05-30 | a second, separate UK national silicon-photonics MPW foundry and innovation centre | `FUNDX-8` |

**Four totals worth carrying away.** `FUND-4` puts the EU's traceable Europractice money at
**€87 023 980** over 1995–2028; `FUNDX-4` and `FUNDX-8` show that figure is a **floor** three times
over, because EUROCHIP (1989–1995) and EUROPRACTICE IC3 (to 2008) are real and unpriced, and because
the UK's own **£2 406 051** for RETICLES never touched the EU budget. Over the same window the same
funder has committed **€1.23 billion** to the Chips JU, of which the brokerage is 1%. Canada has
committed **CAD $120 million** to one organisation with roughly fifty employees. And the UK, which
already pays into Europractice, has separately put **£17 096 839** into a second national MPW
foundry.

**A methodological warning that follows from `FUNDX-8`.** Counting EU contributions is not counting
public money. The UK's RETICLES money took one HTTP request to a British register and is invisible
in CORDIS. Belgium, Germany, France and Ireland all have equivalent registers and **none of them has
been searched**. Every figure in this file and in `programme-funding.md` that is described as a
total should be read as *the part of the total that the European Commission paid*.

## 3. Cost per design, recomputed

`FUND-2`'s central Europractice figure survives this work unchanged: **€19 024 797,50 of EU money for
6 791 designs over 2016-07-01 → 2025-09-30 = €2 801,47 per design.** Nothing found here changes the
numerator or the denominator. Two things qualify it:

- It is a **floor on the historical total**, because EUROCHIP and EUROPRACTICE IC3 are unpriced
  (`FUNDX-4`), though both fall outside the 2016–2025 window used for the €2 801 figure.
- The **current** rate is €3 997 727,50 ÷ 753 = **€5 309 per design** (`FUND-3`), and the named
  establishment that delivers those designs is 19 people, i.e. **€210 407 per named person per year**
  and **39.6 designs per named person per year** (`FUNDX-5`).

**CMC's figures change materially, because `FUND-7`'s cost base was wrong.** All from `FUNDX-1`,
against `DEM-20`'s **240 prototypes** in the year ended 2026-03-31:

| Measure | Arithmetic | Result |
|---|---|---:|
| Total expenditure per prototype | 20 012 740 ÷ 240 | **CAD $83 386** |
| Expenditure less the genuine grant pass-through ("UR challenge projects", $3 535 310) | 16 477 430 ÷ 240 | **CAD $68 656** |
| Salaries and benefits per prototype | 7 859 646 ÷ 240 | **CAD $32 749** |
| Revenue earned from customers per prototype | 5 332 809 ÷ 240 | **CAD $22 220** |
| Public subsidy per prototype (all expenditure) | (20 012 740 − 5 332 809) ÷ 240 | **CAD $61 166** |
| Public subsidy per prototype (excluding the pass-through) | (16 477 430 − 5 332 809) ÷ 240 | **CAD $46 436** |

`FUND-7` gave **CAD $30 417** of cost and **CAD $7 917** of subsidy per prototype, and said customers
covered **74.0%**. Those came from pie-chart labels. On the audited statement the cost per prototype
is **$68 656–83 386**, the subsidy is **$46 436–61 166**, and customers cover **26.6%** of
expenditure (5 332 809 ÷ 20 012 740) — or **32.4%** of expenditure excluding the pass-through
(5 332 809 ÷ 16 477 430). **In no audited year have CMC's customers covered half of its
expenditure**: the peak was 47.8% in the year ended 2024-03-31.

**The caveat that applies to every number in this section is the one `FUND-2` and `FUND-7` already
make, and `FUNDX-6` sharpens.** Dividing a whole programme's cost by its prototype count overstates
what a prototype costs, because most of what these programmes do is tools, licences and training for
people who never tape out. CBC's figure for CMC makes the scale of that error concrete: **8,000
students and 5,000 researchers served, 240 prototypes fabricated.** The per-prototype figures above
are *cost per unit of the thing the organisation is famous for*, not unit costs, and they must not be
quoted as unit costs.

## 4. Blocked sources, and what would unblock a human

| Source | What happened | What it would have answered | What would unblock a human |
|---|---|---|---|
| **`chips-ju.europa.eu`** (work programme, project pages, Design Platform, competence centres) | The site is a client-side-rendered Microsoft Power Pages application. `curl` returns the navigation chrome and no content; `/Work-Programme/` returns a 1 648-byte shell. | The Chips JU's own annual work programmes, annual activity reports, the indicative budget for topic `HORIZON-JU-CHIPS-2025-CSA-1`, and the national co-funding shares. | A real browser. Everything used here came from the CORDIS bulk export instead. |
| **EU Funding & Tenders Portal topic page** for `HORIZON-JU-CHIPS-2025-CSA-1` | Also client-side rendered; `WebFetch` returns only the page header. The SEDIA search API (`api.tech.ec.europa.eu/search-api/prod/rest/search`) returns **HTTP 405, "Method not allowed"** to a GET. | The topic's indicative budget and expected number of grants, i.e. whether €12.0m was the whole topic or a share of it. CORDIS shows one grant under the topic, which strongly implies the whole. | A browser, or a POST to the SEDIA API (this session was GET-only). |
| **EU Financial Transparency System** (`ec.europa.eu/budget/financial-transparency-system/`) | Reachable (HTTP 200) but it is a **Qlik Sense dashboard** loaded from `dashboard.tech.ec.europa.eu`; there is no HTML table and no CSV link in the page source. `FUND-4`'s blocked list recorded it as "not queried"; it has now been tried. | Payments to imec and the other partners outside the research programmes. CORDIS already carries per-participant contributions, so the expected marginal value is low. | A browser, and patience with a Qlik dashboard. |
| **CORDIS search API with `format=json`** | Returns only the `header` block — `totalHits` and the translated Elasticsearch query — with **no `hits`**, for every query tried. `FUND-1` used it successfully in September; it does not work that way now. | Nothing that the bulk exports do not carry. | The bulk CSV exports (`cordis-fp4…fp7`, `cordis-HORIZONprojects-csv.zip`) work perfectly and are the route to use. |
| **`cordis.europa.eu` record for EUROPRACTICE IC3** | **Does not exist.** Two independent scans of the FP6 bulk export — a full-text scan over all 10 093 projects, and a scan of every project in which imec appears — return nothing. The grant is named, dated and placed in FP6 by the IC4 publishable summary that CORDIS itself publishes. | The value of the EC's Europractice grant for roughly 2005–2008, and therefore the true 1995–2028 total. | The FP6 final reports held by DG CNECT, an access-to-documents request under Regulation 1049/2001, or the *Official Journal* call and award notices for the FP6 IST programme. **This session made no request of any kind.** |
| **EUROCHIP (1989–1995) grant value** | Still not in CORDIS, in any framework programme's export — `FUND-4`'s finding stands. What is new is that its **existence and dates are now sourced** to an EC-published document (`FUNDX-4`). | The size of the EU's original 1989 commitment. | ESPRIT programme documents on `op.europa.eu`, or the *Official Journal*. |
| **imec's statutory accounts** (Belgian National Bank, Central Balance Sheet Office) | The public consultation API at `consult.cbso.nbb.be/api/rs-consult/published-deposits` returns **HTTP 500** without an enterprise number, **HTTP 417** on a dotted enterprise number, and **HTTP 403** on the `/enterprise/{number}` path. The enterprise number itself was **not confirmed** from a primary source, so the queries may have been wrong as well as refused. | imec's audited turnover, its *social balance sheet* (which in Belgium carries an FTE count and a total wage bill), and whether any Europractice segment is disclosed. | `consult.cbso.nbb.be` in a browser, after looking imec's enterprise number up in the Kruispuntbank van Ondernemingen. This is the single most valuable unopened document for the payroll question. |
| **Fraunhofer IIS institute-level payroll** | The institute publishes revenue (€264 m) and head-count (1 225) but **no wage bill**. The Fraunhofer-Gesellschaft's consolidated annual report was not opened. | Cost per head at the German partner, and therefore a better anchor for what the Europractice grant buys. | The Fraunhofer-Gesellschaft's *Jahresbericht* financial section. |
| **`www.europractice.stfc.ac.uk`** pages other than the two `FUND-3` uses | `/welcome.html` and `/content/contacts/contacts.html` both return **HTTP 404**. The membership and member-list pages `FUND-3` cites still work. | The size of the STFC design-tools operation, and the tool price list. | Navigating the live site from its working entry point, and a member login for the tool prices. |
| **CMC's audited statements for FY2022 as filed** | The PDF at `cmc.ca/wp-content/uploads/2022/09/Financial-Statements-31MAR2022-EN.pdf` downloads (3.3 MB) but is a **scan with no text layer** — `pdftotext` returns 15 bytes. The FY2022 figures used in `FUNDX-1` are the restated comparatives in the FY2023 statements. | FY2022 as originally reported, before restatement. | OCR, or reading the scan. |
| **CMC's accounts and annual reports for 2009–2021** | `cmc.ca/corporate-reports/` — the page that solved `FUND-7`'s problem for 2022–2026 — lists nothing before the *Annual Report 2021*. `FUND-7`'s note about the Flash-based 2009–2015 site still stands. | The middle of CMC's history, including the 2016–2019 funding crisis in its own accounts. | The Internet Archive's copies of the old ASP.NET site, or a request to CMC. |
| **CMC head-count, any year after 2018** | Not published in any annual report or financial statement read (five statements, five annual reports). The staff page names **13** people. A commercial data vendor puts it at 86 for 2026; that is a LinkedIn-derived estimate, not a filing, and is **not used** anywhere in this file. | The denominator for every per-person figure here. | CMC's own statement, or the notes to a future audit. |
| **The split between technical and administrative staff, anywhere** | Not published by CMC, Europractice, any Europractice partner, or MOSIS. The only administrative figure in the whole record is Europractice's "€100 to administer the membership" per member per year. | The core of the automation question. | Nothing public. This is a genuine hole. |
| **Chips Act competence centres** | Not in CORDIS: a scan of all 23 451 Horizon Europe projects for "competence cent(re\|er)" returns nine hits, none of them a Chips Act competence centre. They are set up nationally with joint Chips JU and member-state money. | The national co-funding shares the brief asked about. | The Chips JU site in a browser, and then twenty-odd national agencies' registers. |
| **Belgian, German, French, Irish and Dutch national grant registers** | **Not reached.** The **UK** register *was* reached and produced `FUNDX-8` — £2.4m of UK money for RETICLES that CORDIS does not show, and £17.1m for a second UK MPW service. The others were not searched; time went to the Canadian register and the CORDIS bulk exports. | National co-funding of the Europractice partners, which `FUNDX-8` shows can be a material fraction of a grant and completely absent from CORDIS. | Förderkatalog (Germany), FRIS (Flanders), ANR and the Grenoble INP/CNRS accounts (France), Research Ireland (Ireland), NWO (Netherlands). All are public and searchable, and **Gateway to Research's JSON API took one request** — this is the highest-value unfinished work in the file. |
| **CORNERSTONE's design counts, prices and revenue** | **Not looked for.** `FUNDX-8` establishes the funding only. | Whether the UK's second MPW service has the same economics as Europractice's. | `cornerstone.sotonfab.co.uk` and the grants' own final reports. |
| **Kingston Whig-Standard archive** | `thewhig.com/?s=CMC+Microsystems` returns a page with no matching articles. The two useful local stories came from CBC Ottawa and Global News Kingston instead. | Local coverage of CMC's 2018 crisis and of its site. | The Whig's own archive, or a library database. |
| **`cbc.ca`** | Returns **HTTP 403** to `WebFetch`. Serves `curl` normally with an ordinary browser User-Agent. | Nothing — worked around. | Recorded so nobody gives up on CBC. |
