# Design starts and mature nodes (`TRAD`)

Evidence on **population 1** of the demand split: traditional commercial chip demand, counted as
"design starts", and the one series that cuts against the simple declining story — the growth of
products in production at mature nodes.

## Read this before you use anything here

> [!IMPORTANT]
> **Never plot a design start and a Tiny Tapeout (or Efabless, or Google MPW) submission on one
> axis.** A Gartner or Semico "design start" is a commercial product intended for production — in
> Gartner's own definition "a unique tapeout" of an ASIC or ASSP by a company that expects to sell
> the part. A Tiny Tapeout submission is a one-tile experiment on a shared shuttle die that mostly
> will never be sold at all. They count different objects, under different definitions, from
> different populations. **Only the direction of each series may be compared, never the level, the
> ratio, or the difference.** Anything that puts the two on a common axis is wrong, however it is
> labelled.

> [!WARNING]
> **The two halves of the owner's design-starts chart cannot be joined.** See TRAD-3 and TRAD-6.
> The step from Gartner's ~11,000 in 2012 to Semico's ~6,200 in 2015 is not a measured collapse: it
> crosses two research houses whose published definitions of "ASIC design start" differ in scope
> (Semico counts FPGAs and PLDs as ASIC product types; Gartner treats FPGA/PLD as a separate,
> oppositely-moving series), and Semico's own public statements for the Section B window say design
> starts were *growing*, not falling. The *within-section* Gartner trend survives scrutiny. Section
> B, as drawn, does not.

## Contents

| Entries | Covers |
|---|---|
| TRAD-1 … TRAD-3 | The Gartner half of the design-starts chart: the report, the published levels, the definition |
| TRAD-4 … TRAD-6 | The Semico half, the definitional mismatch, and the verdict on the splice |
| TRAD-7 … TRAD-9 | ASML's mature-node chart, verified, and what it does and does not say |
| TRAD-10 … TRAD-13 | The mature-node complication tested: capacity, utilisation, pricing, subsidy |
| TRAD-14 … TRAD-16 | Related corroboration: leading-edge manufacturer count, and evidence *against* the declining story |

---

## The Gartner half

### TRAD-1. The Gartner report named on the chart exists, and its own headline is a 2.9%/yr decline, not a collapse

- **Source:** Ganesh Ramamoorthy and Bryan Lewis, "Market Trends: Worldwide, ASIC and ASSP Design
  Starts Continue Declining Trend, 2012", Gartner, published 2012-02-27, ID G00229088.
  <https://www.gartner.com/en/documents/1934119>
- **Verification:** Verified 2026-09-18 — of the report's *existence, title, authors, date, ID,
  summary and table of contents only*. The live Gartner page returns HTTP 403 to automated fetch; the
  metadata was read from the Internet Archive capture
  <http://web.archive.org/web/20210308074719/https://www.gartner.com/en/documents/1934119>
  (captured 2021-03-08). **The report body is paywalled and was not obtained, and no attempt was made
  to obtain it.** No figure in this entry comes from inside the report.
- **What it says** (all quoted from the public abstract/contents page):
  - Summary, in full: "The rising cost of designing in leading-edge process nodes has slowed growth
    in 45- and 32-nanometer designs starts in 2011. On the other hand, design starts in 90 nm and 65
    nm are holding up firmly." (the misspelling "designs starts" is the source's)
  - Section heading: "Market: Overall ASIC and ASSP Design Starts Set to Decline 2.9% Through 2016"
  - Section heading: "Overall ASIC and ASSP Design Starts Continue to Decline"
  - Section heading: "ASIC Design Value, Complexity and Production Units Are Growing"
  - Section heading: "Contrarian View: ASIC and ASSP Design Starts Slow; FPGA/PLD Design Starts Set
    to Grow in 2012 and 2013"
  - Section heading: "Technology: Leading-Edge Design Start Growth Slows as 90 and 65 nm Designs Hold
    Steady"
- **Bears on:**
  - **H5 (mixed).** The direction is down, which challenges a large pent-up reservoir. But Gartner's
    own stated rate is **-2.9% a year through 2016** — a slow drift, not the exponential collapse the
    chart's dashed fit implies. And Gartner's own contrarian section says FPGA/PLD design starts were
    *rising* over the same period, i.e. the custom-function demand did not vanish, it moved.
  - **H1 (supports).** Gartner's stated cause is "the rising cost of designing in leading-edge
    process nodes" — the doom-spiral mechanism, named by the analyst house itself.
- **Used in:** not yet.
- **Caveats:**
  - Two of the four headings above cut *against* a simple "demand is dying" reading: design *value,
    complexity and production units* were growing while starts fell, and FPGA/PLD starts were
    forecast to grow. Do not cite the title without them.
  - -2.9%/yr through 2016 is a **forecast made in 2012**, not an outcome. Nothing here confirms it
    happened.
  - The chart's Section A implies about **-9.0%/yr** over 2000–2012 (`DERIVED`:
    (11,000 / 34,000)^(1/12) − 1 = −0.0898). That is three times Gartner's own forward rate. The
    steep part of the chart is the early-2000s telecom bust, not a constant exponential.

### TRAD-2. Gartner's publicly quoted ASIC design-start levels are in the low **thousands**, not tens of thousands

- **Sources:**
  - Sean Murphy, "ASIC Design Starts Dropping: Implications for EDA", SKMurphy Inc., 2007-04-11.
    <https://www.skmurphy.com/blog/2007/04/11/asic-design-starts-dropping-implications-for-eda/>
    Reproduces a chart attributed to Bryan Lewis and John Barber of Gartner, presented to the Santa
    Clara Valley chapter of the IEEE Components, Packaging & Manufacturing Technology Society, and
    sourced onward to the EE Times article "Sockets scant for costly ASICs".
  - Peter Clarke, "ASIC design starts to fall 4% in 2007, says Gartner", *EE Times*, 2007-12-03.
    <https://www.eetimes.com/asic-design-starts-to-fall-4-in-2007-says-gartner/>
- **Verification:** Partial, 2026-09-18.
  - The SKMurphy page was fetched directly and read (HTTP 200); the table and the definition below
    are as that page gives them. **Verified** for what SKMurphy published.
  - The EE Times page was read through `WebFetch` only; a direct HTTPS fetch to `www.eetimes.com`
    timed out after 120 s. Its figures are therefore **Partial**.
  - Neither the underlying Gartner tables nor the original EE Times "Sockets scant for costly ASICs"
    article were obtained. Both are second-hand reproductions of Gartner data.
- **What it says:**
  - SKMurphy's reproduced Gartner table, worldwide ASIC design starts:

    | Year | Design starts |
    |---|---|
    | 2000 | 7,749 |
    | 2005 | 3,623 |
    | 2006 | 3,391 |
    | 2007 | 3,196 |
    | 2008 | 3,048 |

  - **Gartner's definition, as SKMurphy gives it:** "A design start is equal to a unique tapeout, but
    the IC may or may not go into production."
  - EE Times 2007-12-03, attributed to Gartner: 3,408 ASIC design starts in 2006; 3,275 projected for
    2007, a fall of 4%; roughly 200 of the 2007 starts at 65 nm or below.
- **Bears on:**
  - **H5 (context).** Fixes the order of magnitude of the commercial series: **thousands per year**,
    worldwide, for ASICs.
  - **Method (critical).** Gives the only explicit published Gartner definition found: a unique
    tapeout, production not required.
- **Used in:** not yet.
- **Caveats:**
  - The two 2006 figures disagree: 3,391 (SKMurphy's reproduced table) versus 3,408 (EE Times). A
    0.5% gap; both are "about 3,400". The 2007 figures disagree by more: 3,196 (table, apparently a
    forecast made in 2007) versus 3,275 (EE Times, December 2007). Record both; quote neither as
    "the" figure.
  - This is **ASIC only**. The chart's Section A is labelled "ASIC and ASSP". See TRAD-3.
  - Cross-checks against `DEM-11` in [`latent-demand-challenges.md`](latent-demand-challenges.md):
    that entry records Gartner Dataquest in 2002 putting design starts "closer to 5,000 this year,
    declining to just over 3,000 in 2006". The table's 3,391 for 2006 is "just over 3,000" — the two
    independent quotations of Gartner agree. DEM-11 marks the SKMurphy table as **Lead**; this entry
    upgrades it to **Partial** (page fetched and read; Gartner's own tables still not seen).

### TRAD-3. The chart's Section A is a near-constant **4.4×–4.7× multiple** of Gartner's published ASIC figures, and the multiple is unexplained

- **Source:** derived from TRAD-1, TRAD-2 and the owner-supplied chart "Number of design starts for
  commercial sectors".
- **Verification:** the arithmetic is `DERIVED` and written out below. The Section A values are
  **read off a chart, not from a table**, and are approximate to roughly ±500.
- **What it says:**

  | Year | Gartner published ASIC starts (TRAD-2) | Chart Section A (read off, approx.) | Ratio `DERIVED` |
  |---|---|---|---|
  | 2000 | 7,749 | ~34,000 | 34,000 / 7,749 = 4.39 |
  | 2005 | 3,623 | ~16,000 | 16,000 / 3,623 = 4.42 |
  | 2006 | 3,391 (alt. 3,408) | ~15,000 | 15,000 / 3,391 = 4.42 (alt. 4.40) |
  | 2007 | 3,196 (alt. 3,275) | ~15,000 | 15,000 / 3,196 = 4.69 (alt. 4.58) |
  | 2008 | 3,048 | ~14,000 | 14,000 / 3,048 = 4.59 |

  Mean of the five primary ratios = 4.50; range 4.39 to 4.69.

  The *shapes* match closely. `DERIVED`: Gartner's published series falls at
  (3,048 / 7,749)^(1/8) − 1 = −11.01%/yr over 2000–2008; Section A falls at
  (14,000 / 34,000)^(1/8) − 1 = −10.50%/yr over the same span. A difference of half a percentage
  point a year.
- **Bears on:**
  - **Method (critical).** Two readings are consistent with this, and we cannot currently choose
    between them:
    1. **Section A is ASIC + ASSP and Gartner's ASSP starts ran about 3.4× its ASIC starts**, with
       almost exactly the same trend. Gartner does publish an ASIC *and ASSP* series (TRAD-1), so
       this is entirely possible. We found **no public figure for Gartner ASSP design starts** to
       test it.
    2. **Section A is Gartner's ASIC series rescaled**, i.e. the chart's vertical axis is wrong by a
       factor of about 4.5 and the shape is the only real information in it.
  - **H5 (context).** Under *either* reading the *direction and rate* of Section A are corroborated
    by independently published Gartner figures. The **levels are not corroborated by anything**.
- **Used in:** not yet.
- **Caveats:**
  - **Do not quote any absolute number from Section A.** The trend is supported; the level is not.
  - The near-constant ratio is suggestive but is computed against only five years, two of which
    (2006, 2007) have two competing source values.
  - **Open question:** what does Gartner count as an ASSP design start, and how many were there? A
    single public Gartner ASSP figure would settle this. Not found.

---

## The Semico half, and the splice

### TRAD-4. Semico's own public statements say ASIC design starts **grew** through the whole of Section B's window

- **Sources** (Semico Research Corp. press material; `semico.com` now redirects every page to
  `/lander` and appears to be parked, so all four were read from the Internet Archive or a trade
  mirror):
  - "Mixed signal and IoT driving ASIC design starts growth, says Semico Research", *Semiconductor
    Digest*, March 2016, on report *ASIC Design Starts for 2016 by Key End Market Applications*
    (SC106-16, March 2016).
    <https://sst.semiconductor-digest.com/2016/03/mixed-signal-and-iot-driving-asic-design-starts-growth-says-semico-research/>
  - "ASIC Design Starts: Automotive on a Fast Track" (SC107-16, April 2016), Semico Research.
    <https://web.archive.org/web/2020/https://semico.com/content/asic-design-starts-automotive-fast-track>
  - "ASIC Design Starts 2022: New Applications and AI Become Market Drivers" (SC107-22), Semico
    Research.
    <https://web.archive.org/web/20230927043658/https://semico.com/content/asic-design-starts-2022-new-applications-and-ai-become-market-drivers>
  - "ASIC Design Starts by Major Market Applications" (SC106-23), Semico Research.
    <https://web.archive.org/web/20240221130711/https://semico.com/content/asic-design-starts-major-market-applications>
- **Verification:** Verified 2026-09-18. The Semiconductor Digest page was fetched directly (HTTP
  200). The three Semico pages were fetched from the Internet Archive (captures 2023-09-27,
  2024-02-21, and a 2020 capture of the automotive page) after the live site was found to redirect to
  a parking page. Quotes below are copied from those pages. **The reports themselves are paid
  products and were not obtained.**
- **What it says**, in Semico's own published words:
  - SC106-16 (March 2016): "the total ASIC design start market is expected to grow 5.0% in 2016 on
    top of a 4.5% growth rate in 2015."
  - SC107-16 (April 2016): "this will drive ASIC design starts in transportation to increase by 7.1%
    in 2016 and 6.5% CAGR over the next five years." Rich Wawrzyniak, Principal Analyst, adds the
    qualifier: "Although, slower growth in the traditional markets will act to moderate the overall
    design start growth rate over the forecast period, the innovations in automotive, communication
    and consumer markets continue to grow above the industry average."
  - SC107-22: "forecasts that total ASIC design starts will grow at a 3.7% CAGR from 2021 through
    2025."
  - SC106-23: "ASIC design starts increased 3.1% in 2022." Jim Feldhan, President, Semico Research,
    is quoted on the pressure: "These metrics are well known:  rising design and mask set costs,
    increasing device complexity, rising design cycle times and shrinking market windows" (the double
    space is the source's).
  - For context, the earlier SC101-12 (February 2012), the report immediately after Gartner's
    Section A ends: "Total ASIC design starts increased 11.1% in 2011 on top of a 9.8% growth in
    2010. Semico is forecasting continued growth with an increase of 10.2% in 2012." and "Total ASIC
    design starts are forecast to show a CAGR of 6.6% from 2012 - 2016."
    <https://web.archive.org/web/20230922085307/https://semico.com/content/asic-design-starts-key-end-market-application-0>
- **Bears on:**
  - **The chart (challenges, hard).** Section B is drawn falling from ~6,200 in 2015 to ~5,700 in
    2022, i.e. `DERIVED` (5,700 / 6,200)^(1/7) − 1 = **−1.19%/yr**. Semico's own published numbers
    for that window are **+4.5% (2015), +5.0% (2016 forecast), +3.1% (2022), +3.7% CAGR
    (2021–2025)**. Semico says up; the chart drawn from Semico says down.
  - **H5 (challenges the challenge).** The best-attested public statement from the house named on
    Section B is that commercial design starts were *growing* at 3–5% a year right through the period
    in which the project's thesis says traditional demand was flat or falling.
- **Used in:** not yet.
- **Caveats:**
  - These are press-release growth *rates*. **No absolute Semico level was found in public** — see
    TRAD-5. So we cannot say whether Semico's level was ~6,000, ~600 or ~60,000.
  - Semico's growth rates are not all outcomes: +5.0% (2016), +3.7% CAGR (2021–2025) and +6.6% CAGR
    (2012–2016) are forecasts. The measured ones are +9.8% (2010), +11.1% (2011), +4.5% (2015) and
    +3.1% (2022).
  - It is possible the owner's Section B is a *sub-series* (one product type, or one region, or
    excluding FPGA/PLD) that genuinely fell while Semico's headline grew. If so, the chart is
    mislabelled rather than wrong. We cannot tell without the report.
  - Semico's press releases have an obvious commercial interest in a growing market, just as an EDA
    vendor's have in a shrinking one. Weigh accordingly.

### TRAD-5. Semico and Gartner count different things: Semico's "ASIC design starts" **include FPGAs and PLDs**; Gartner's exclude them and move the opposite way

- **Sources:** the Semico report descriptions in TRAD-4, and the Gartner table of contents in TRAD-1.
- **Verification:** Verified 2026-09-18 from the same pages as TRAD-4 and TRAD-1.
- **What it says:**
  - Every Semico ASIC-design-starts report description found lists the product types counted. SC106-16
    (2016): "Nine ASIC product types (including Mixed Signal), three SoC types, FPGAs and PLDs are
    analyzed by design starts with unit shipments for each." SC106-23 (2023): "Nine ASIC product types
    including Mixed-Signal, Analog, Advanced Performance Multicore, Value Multicore and Basic SoCs,
    FPGAs and PLDs, Gate Array and Structured ASICs." SC101-12 (2012) names all nine: "Analog, Mixed
    Signal, Gate Array, Advanced Performance Multicore SoCs, Value Multicore SoCs, Basic SoCs, PLDs,
    FPGAs and Structured ASICs".
  - Gartner's report is "ASIC **and ASSP**" and carries a separate section: "Contrarian View: ASIC and
    ASSP Design Starts Slow; FPGA/PLD Design Starts Set to Grow in 2012 and 2013". Gartner therefore
    (i) excludes FPGA/PLD from the headline series and (ii) records it as moving in the *opposite*
    direction.
  - Gartner includes ASSPs — application-specific standard products, sold to many customers. Semico's
    nine product types do **not** name ASSP.
- **Bears on:**
  - **Method (critical).** The two series differ in scope in at least two ways, and the two
    disagreements push in opposite directions: Semico adds a category Gartner says was *growing*
    (FPGA/PLD); Gartner adds a category Semico does not list (ASSP). There is no reason to expect the
    levels to be comparable and no way to reconcile them from public material.
- **Used in:** not yet.
- **Caveats:**
  - Neither house publishes a full methodology. Gartner's "a unique tapeout" (TRAD-2) is the only
    explicit definition found on either side; **no Semico definition of a design start was found**.
    An FPGA "design start" plainly cannot be a tapeout, which is itself evidence the definitions
    differ.

### TRAD-6. Verdict: the splice is not legitimate, and the industry itself says the metric is ill-defined

- **Sources:**
  - Clive Maxfield, "What's the number of ASIC versus FPGA design starts?", *EE Times*, 2011-03-20.
    <https://www.eetimes.com/whats-the-number-of-asic-versus-fpga-design-starts/>
  - TRAD-1 to TRAD-5 above.
- **Verification:** Partial, 2026-09-18. The Maxfield article was read through `WebFetch` only; a
  direct HTTPS fetch to `www.eetimes.com` timed out after 120 s (two attempts, different tools).
  `WebFetch` returned, as quotations from the article, the phrases "I'm just making this number up",
  "I'm just pulling these numbers out of thin air" and "no one has a clue what a design start
  actually is", and reported that the example figures "2,500 ASIC design starts versus 90,000 FPGA
  design starts" are explicitly invented by the author for illustration. **Because these came through
  a summarising fetch rather than a direct read, treat the wording as unconfirmed** until someone
  opens the page in a browser.
- **What it says:** the article's argument is that published ASIC-versus-FPGA design-start statistics
  lack clear sourcing and a standard definition — is a start a cancelled architecture study, an RTL
  spec, an FPGA prototype of an ASIC, a derivative of a platform? It names Rich Wawrzyniak of Semico
  as someone who does track both.
- **The verdict on the owner's chart:**
  1. **Section A (Gartner, 2000–2012) is sound as a trend.** Two independent public quotations of
     Gartner figures (TRAD-2) give the same shape and almost the same rate of decline. The *levels*
     drawn are unexplained and about 4.5× the published ASIC figures (TRAD-3).
  2. **Section B (Semico, 2015–2022) is contradicted as a trend** by Semico's own published growth
     rates (TRAD-4). As drawn it falls ~1.2%/yr; Semico says it rose 3–5%/yr.
  3. **The step between them is not a measurement.** `DERIVED`: 11,000 → 6,200 is a fall of
     1 − 6,200/11,000 = **43.6%**, which over the three unmeasured years 2013–2014 would be
     (6,200 / 11,000)^(1/3) − 1 = **−17.4%/yr**, twice the steepest rate anywhere in Section A. There
     is no data point in 2013 or 2014 on the chart. Given TRAD-5, the most likely explanation is
     **definitional, not real**.
  4. **Therefore: do not present the blue line as one series, do not fit one exponential across both
     halves, and do not quote any level from either half.** Use Section A's *direction* (commercial
     ASIC/ASSP design starts fell through the 2000s, at roughly 9–11%/yr early and slowing) as
     evidence. Do not use Section B at all until the Semico contradiction in TRAD-4 is resolved.
- **Bears on:** **H5 (context)**, and the honesty of any chart built on this.
- **Used in:** not yet.
- **Caveats:** none that soften the above.

---

## The mature-node complication

### TRAD-7. ASML's mature-node chart, verified word for word — and it has **no numbers on the y-axis**

- **Source:** ASML Investor Day 2022, "Demand and capacity", Peter Wennink, 2022-11-11, page 24.
  PDF published by ASML at
  <https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/investors/investor-days/2022/2_asml-investor-day-2022_demand-and-capacity---peter-wennink.pdf>
  (linked from <https://www.asml.com/en/investors/investor-days/2022>). The same deck was filed with
  the SEC as Exhibit 99.2 to ASML Holding N.V.'s Form 6-K:
  <https://www.sec.gov/Archives/edgar/data/937966/000119312522283523/d369368dex992.htm>
- **Verification:** Verified 2026-09-18. The PDF was downloaded from `media.asml.com` (HTTP 200,
  2,531,829 bytes) and its text extracted; every string below is copied from page 24 of that
  extraction. The SEC exhibit was additionally read through `WebFetch` and returns the same slide
  title and figure; a direct fetch of the SEC URL returns HTTP 403 to a plain browser user-agent.
- **What it says** — page 24 in full, as extracted:
  - Section banner: "DUV growth drivers"
  - Slide title: "Significant increase in mask sets or products for ≥ 28 nm Logic nodes"
  - Chart title: "Products ≥ 28 nm technology in production (300 mm)"
  - Y-axis label: "# of mask sets (products) in production"
  - Callout: "Over 40% increase in products in past few years, meaning more applications"
  - Series labels: "90-130 nm", "65 nm", "40 nm", "28 nm"
  - X-axis labels: "2015", "2012", "2018", "2021" (the extractor returns them in that order; the
    chart plots 2012, 2015, 2018, 2021)
  - Right-hand panel: "Technology nodes require DUV", with a matrix "Technology Nodes / ArFi / ArF /
    KrF / i-line" against "90-130 nm / 65 nm / 40 nm / 28 nm", headed "DUV litho required"
  - Attribution: "Source: ASML analysis and external analysts"
  - Footer: "November 11, 2022  Page 24"
- **Bears on:**
  - **H5 (challenges).** The number of *distinct products* in production at mature nodes rose
    materially over 2012–2021, at the same time as the commercial design-start series was said to be
    falling. Any story that says "fewer and fewer chips get made" has to account for this.
- **Used in:** not yet.
- **Caveats — these matter:**
  - **The chart is unlabelled in magnitude.** No y-axis values are printed. It shows a shape and one
    percentage, nothing more. Do not derive a count of products from it.
  - **ASML's wording is "Over 40% increase in products in past few years", not "40% increase in new
    products since 2015".** The owner's caption — "Mature nodes have also demonstrated significant
    growth in the past 5+ years (40% increase in new products since 2015) and has necessitated
    capacity expansions through major CapEx investments" — **does not appear in this deck**, and was
    not found in the Investor Day 2021 deck (SEC Exhibit 99.2 to the 2021 Form 6-K,
    <https://www.sec.gov/Archives/edgar/data/937966/000119312521287742/d133133dex992.htm>, dated
    2021-09-29) either. Treat it as a third-party or in-house gloss, not as an ASML quotation, and do
    not put it in quotation marks attributed to ASML. Note also that ASML says "products", the gloss
    says "**new** products" — a substantive difference (see TRAD-8).
  - **"300 mm" is a real restriction.** The chart counts 300 mm products only. A great deal of mature
    and legacy production is on 200 mm, and is excluded.
  - "≥ 28 nm Logic". Memory, analog-only and sub-28 nm products are excluded.
  - The source line is "ASML analysis and external analysts" — ASML's own construction, partly from
    unnamed third parties. It is not an audited or reproducible count.
  - ASML sells the lithography tools that mature-node capacity expansion buys. It has a direct
    commercial interest in this slide.

### TRAD-8. Reading (a): a "mask set in production" and a "design start" count different populations, and the stock can rise while the flow falls

- **Source:** reasoning over TRAD-2 (Gartner's definition), TRAD-7 (ASML's axis label), and the
  Gartner headings in TRAD-1.
- **Verification:** this entry is **analysis, not a source**. The inputs are verified; the argument
  is ours. Marked **Lead** as a claim about the world.
- **What it says:** the owner asks how mature-node products in production can grow >40% while
  commercial design starts fall. The two series are not in conflict, because:
  1. **Stock versus flow.** A design start is a *flow*: new tapeouts begun this year. "# of mask sets
     (products) **in production**" is a *stock*: every product currently being manufactured,
     regardless of when it was designed. A stock can grow for years on a shrinking inflow, provided
     the outflow (products retired) shrinks faster. This alone is sufficient to reconcile the two,
     and it is the explanation that requires the fewest extra assumptions.
  2. **Products live longer.** Automotive and industrial parts have service lives measured in
     decades, and qualification cost discourages retiring or re-spinning them. Longer lives raise the
     stock without raising the flow.
  3. **Migration down, not up.** ASML's own page 22 says the opposite is happening at the top: "More
     products moving from mature to advanced Nodes". So the mature-node stock is *not* being topped
     up by aging leading-edge designs migrating down — ASML says traffic runs the other way. This
     weakens the "designs migrate down as they age" candidate explanation.
  4. **Different populations.** Gartner counts ASIC/ASSP tapeouts. ASML counts 300 mm mask sets at
     ≥ 28 nm logic, which includes many parts that no one would call an ASIC — standard products,
     microcontrollers, power and analog logic.
  5. **Genuine new demand at mature nodes.** ASML page 23, verbatim: "Mature market is growing faster,
     driven by smart grids and automotive"; "After being stable for years, we now see proliferation of
     mature applications, and growing wafer demand"; "Customers such as TSMC confirm mature
     applications are growing, in segments such as smartphone (driven by sensors, camera, etc) and
     automotive (driven by electrification)."
- **Bears on:**
  - **H5 (mixed).** Point 5 is real new demand and supports the idea that cheap, mature capacity
    finds new applications. Points 1–2 mean the >40% figure is **not** evidence of >40% more design
    activity, and must never be used as if it were.
- **Used in:** not yet.
- **Caveats:**
  - **The decisive test is not available.** If ASML's chart counted *new* mask sets per year rather
    than mask sets *in production*, it would be a flow and directly comparable in direction to design
    starts. It does not — the axis says "in production". The owner's caption says "new products",
    which is the flow reading; ASML's slide says the stock. **Do not use the caption's reading.**
  - Point 1 is a sufficiency argument, not a measurement. We have no public data on mature-node
    product retirement rates, so we cannot say how much of the >40% is longer lives and how much is
    new designs.

### TRAD-9. Reading (b), first half: mature nodes are growing and attracting capex — ASML's own forecast

- **Source:** ASML Investor Day 2022, "Demand and capacity", Peter Wennink, 2022-11-11, pages 17–19
  and 26–27 (same PDF as TRAD-7).
- **Verification:** Verified 2026-09-18 from the downloaded PDF text.
- **What it says:**
  - Page 19, "Advanced and mature nodes drive investments in wafer capacity", subtitle "~780k
    wafers/month per year 2020-2030, CAGR ~6.5%". The table, in 300 mm-equivalent thousands of wafer
    starts per month added per year:

    | Segment | CMD 2021, 2020–2025 | Growth 2020–2030 | CAGR 2020–2030 |
    |---|---|---|---|
    | NAND | +100 | +100 | 4.9% |
    | DRAM | +80 | +80 | 4.7% |
    | Advanced Logic | +125 | +220 | 12.0% |
    | Mature | +200 | +380 | 6.0% |
    | Total | +505 | +780 | 6.5% |

    with the footnote "Source: ASML analysis, Advanced Logic ≤2  nm, Mature >2  nm" (the extraction
    drops a digit from each node figure; in context these are ≤28 nm and >28 nm).
  - Bullet, page 19: "Mature markets driven primarily by strong automotive and industrial demand,
    mainly in 300 mm but 200 mm also growing".
  - Page 22: "TSMC June 2022 symposium: to add 50% on mature (including 28 nm)/ specialized capacity
    by 2025", sourced to "TSMC, Anandtech June16, 2022".
- **Bears on:**
  - **H1 / the "leading edge is always economically superior" claim (challenges it).** In ASML's own
    2022 planning numbers, **mature nodes account for the single largest block of added wafer
    capacity to 2030** — `DERIVED`: 380 / 930 = 40.9% of the total 2020–2030 addition including the
    geopolitical block (see TRAD-10), versus 220 / 930 = 23.7% for advanced logic. A leading edge
    that were always and everywhere economically superior would not leave the biggest capacity block
    to the nodes it replaced twelve years earlier.
  - **H5 (supports, weakly).** Cheap, depreciated, mature capacity is where new applications keep
    appearing.
- **Used in:** not yet.
- **Caveats:**
  - Mature grows at 6.0%/yr against advanced logic's 12.0%/yr. **Advanced logic is growing twice as
    fast.** Mature is the larger *absolute* addition only because it starts from a much larger base.
    Anyone using this entry must state both numbers; quoting the +380 without the 6.0% versus 12.0%
    is misleading.
  - These are forecasts made in November 2022, at the top of the post-shortage capex cycle. See
    TRAD-11 for what happened to mature-node economics afterwards.
  - ASML is the supplier. Its forecasts of how much equipment the industry will buy are not
    disinterested.

### TRAD-10. ASML itself attributes a sixth of the capacity growth to geopolitics, not demand

- **Source:** ASML Investor Day 2022, "Demand and capacity", Peter Wennink, 2022-11-11, pages 26–27
  (same PDF as TRAD-7).
- **Verification:** Verified 2026-09-18 from the downloaded PDF text.
- **What it says:**
  - Page 27 slide title: "Technological sovereignty and foundry competition create additional
    capacity", subtitle "Resulting in ~10% inefficiency of the total wafer installed capacity by
    2030".
  - The capacity table gains a row: "+ Technological Sovereignty & Competition — +150 — 0.8%",
    taking "Total capacity" from +780 to **+930** kwspm/yr over 2020–2030.
  - Bullets: "Tech sovereignty leading to less efficient use of the installed capacity as
    countries/regions aim to (re)gain fab footprint."; "Fab base becomes more spread in ownership and
    geography and load balancing will become more difficult"; "Intensified foundry competition could
    lead to period with overcapacity as players try to capture market share".
  - Right-hand note: "~10% inefficiency or an additional 18 million wafer capacity by 2030".
  - Page 26 demand-bucket table lists "Geopolitical and competitive driven growth — Technological
    sovereignty / Foundry competition — 150" against variables "Geopolitical driven self-sufficiency"
    and "Foundry competition uncertainty".
- **Bears on:**
  - **Reading (b) (challenges it, from the most sympathetic possible source).** ASML — which profits
    from every wafer of it — explicitly separates **150 of the 930** kwspm/yr of 2020–2030 capacity
    addition as driven by technological sovereignty and foundry competition rather than end demand,
    and calls the result "inefficiency". `DERIVED`: 150 / 930 = **16.1%** of the total addition.
  - **Context.** ASML also foresees "a period with overcapacity" from foundry competition. That is
    exactly what happened (TRAD-11).
- **Used in:** not yet.
- **Caveats:**
  - The +150 is not broken down by node, so we cannot say how much of the *mature* +380 is
    subsidy-driven. The qualitative case that most sovereignty capacity is mature-node is strong (new
    national fabs are overwhelmingly not leading-edge) but **is not established by this document**.
  - The 0.8% figure attached to the +150 row is a CAGR contribution, not a share.

---

## Changes needed in other files

*(Do not apply these here — this file owns none of them.)*

1. **`resources/demand/README.md`** — add a row to the "How the entries are organised" table:

   | [`design-starts-and-mature-nodes.md`](design-starts-and-mature-nodes.md) | `TRAD-1` … | Commercial ASIC/ASSP design-start series (Gartner, Semico), the definitional problems with them, and the growth of products in production at mature nodes |

2. **`resources/demand/latent-demand-challenges.md`, DEM-11** — the last caveat says a current
   design-start count was "**not found**". That is now partly superseded. Suggested replacement for
   that caveat:

   > This is a 2002 article. For the later series, and for why the commonly circulated
   > 2000–2025 design-starts chart cannot be read as one series, see
   > [`design-starts-and-mature-nodes.md`](design-starts-and-mature-nodes.md), TRAD-1 to TRAD-6.

   Also, the SKMurphy aggregation recorded there as **Lead** can be upgraded to **Partial**: the page
   was fetched and read on 2026-09-18 (see TRAD-2). The figures it gives are 2000: 7,749; 2005: 3,623;
   2006: 3,391; 2007: 3,196; 2008: 3,048 — note the 2008 figure 3,048 matches what DEM-11 records.

3. **`resources/references/costs-and-consolidation.md`, COST-3** — add the IBS figure recorded in
   TRAD-14 of this file as a second, independent data point on the same decline.

4. **`resources/hypotheses.md`, H5** — the evidence in this file is genuinely two-sided and the H5
   status line should say so. Suggested addition to H5's evidence list:
   "Commercial design starts: TRAD-1 to TRAD-6 (the widely used 2000–2025 chart is two incompatible
   series; the Gartner half supports a decline, the Semico half is contradicted by Semico's own
   published growth rates). Mature nodes: TRAD-7 to TRAD-13 (products in production at ≥28 nm grew
   >40%, but it is a stock not a flow)."

## Open questions

- What is Gartner's count of **ASSP** design starts? A single public figure would decide between the
  two readings in TRAD-3.
- What is **Semico's definition** of a design start, and what absolute level does it report? Neither
  was found in public.
- Does any public source give **new mask sets per year** (a flow) at mature nodes, rather than mask
  sets in production (a stock)? That would be the series directly comparable in direction to design
  starts.
- Where does the owner's caption on the ASML chart come from? It is not ASML's wording in either the
  2021 or 2022 Investor Day deck.
