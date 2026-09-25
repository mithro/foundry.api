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
