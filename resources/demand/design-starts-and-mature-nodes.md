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
> B, as drawn, does not. **And no level on either half can be used:** Gartner's own published ASIC
> design-start series never exceeds about 11,150 in any year between 1994 and 2013 (TRAD-19), while
> Section A starts at ~34,000. Cite TRAD-19's figures, not the chart's.

## Contents

| Entries | Covers |
|---|---|
| TRAD-1 … TRAD-3 | The Gartner half of the design-starts chart: the report, the published levels, the definition |
| TRAD-4 … TRAD-6 | The Semico half, the definitional mismatch, and the verdict on the splice |
| TRAD-7 … TRAD-9 | ASML's mature-node chart, verified, and what it does and does not say |
| TRAD-10 … TRAD-13 | The mature-node complication tested: capacity, utilisation, pricing, subsidy |
| TRAD-14 … TRAD-18 | Related corroboration, and evidence *against* the declining-demand story |
| TRAD-19, TRAD-20 | A full Gartner ASIC design-start series 1994–2013, found late, which settles the scale question; and an NRE-cost and long-tail assertion from the same document |
| Verdict | Where readings (a) and (b) land once all of it is weighed |

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

### TRAD-3. The chart's Section A is a near-constant **4.4×–4.7× multiple** of Gartner's published ASIC figures over 2000–2008, and the multiple is unexplained

- **Source:** derived from TRAD-1, TRAD-2 and the owner-supplied chart "Number of design starts for
  commercial sectors".
- **Verification:** Partial, 2026-09-18. This entry is arithmetic over TRAD-1, TRAD-2 and the
  owner's chart, not a source of its own; every input carries its own status. All arithmetic is
  `DERIVED` and written out below. The Section A values are **read off a chart, not from a table**,
  and are approximate to roughly ±500.

> [!NOTE]
> **Read TRAD-19 with this entry.** A Gartner chart of 1994–2013 ASIC design starts, reproduced in a
> Xilinx corporate fact sheet, was found after this entry was written. It shows the series never
> exceeding about 11,150 in any year of that twenty-year span. That makes reading 2 below — a
> mis-scaled axis — much more likely than it appears here, though it does not rule out reading 1.
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
  - "ASIC Design Starts: Growing Applications and AI Drive the Market" (SC107-23), Semico Research.
    <https://web.archive.org/web/2023/https://semico.com/content/asic-design-starts-growing-applications-and-ai-drive-market>
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
  - SC107-23: "forecasts that ASIC design starts will continue to increase to meet the demand for
    more evolved, better performing products in all markets with automotive/transportation having the
    highest CAGR at 4.8% from 2022 through 2027."
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
  - **The exact report named on the owner's chart was not located.** The chart credits "Semico
    Research, ASIC Design Starts for 2022 by Key End Market Applications", which is Semico's SKU
    SC106-22. No page for SC106-22 was found in the Internet Archive; the sibling reports above
    (SC106-16, SC107-22, SC106-23, SC107-23) were. The figures in this entry are therefore from the
    same report families and the same analysts, but **not from the report the chart cites**.
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
  1. **Section A (Gartner, 2000–2012) is sound as a trend and wrong in its levels.** Three
     independent public reproductions of Gartner figures (TRAD-2, TRAD-19) give the same shape and
     almost the same rate of decline — `DERIVED` −10.27%/yr for Gartner 2000–2012 against Section A's
     −8.98%/yr. But Gartner's ASIC design starts never exceed about 11,150 in any year from 1994 to
     2013 (TRAD-19), while Section A starts at ~34,000. The levels drawn are between 3× and 5× the
     published figures and are unexplained (TRAD-3).
  2. **Section B (Semico, 2015–2022) is contradicted as a trend** by Semico's own published growth
     rates (TRAD-4). As drawn it falls ~1.2%/yr; Semico says it rose 3–5%/yr.
  3. **The step between them is not a measurement.** `DERIVED`: 11,000 → 6,200 is a fall of
     1 − 6,200/11,000 = **43.6%**, which over the three unmeasured years 2013–2014 would be
     (6,200 / 11,000)^(1/3) − 1 = **−17.4%/yr**, twice the steepest rate anywhere in Section A. There
     is no data point in 2013 or 2014 on the chart. Given TRAD-5, the most likely explanation is
     **definitional, not real**.
  4. **Fitting an exponential is itself misleading.** Gartner's own series *rose* from 1994 to 1997
     and its two big falls are 2001 and 2009, both recessions, with mild single-digit declines
     in between (TRAD-19). A single exponential fitted from 2000 attributes to a secular trend what
     is substantially two downturns, and it hides the 1994–1997 hump by starting after it.
  5. **Therefore: do not present the blue line as one series, do not fit one exponential across both
     halves, and do not quote any level from either half.** Use Section A's *direction* (commercial
     ASIC design starts fell through the 2000s, hard in 2001 and 2009 and mildly in between) as
     evidence. Do not use Section B at all until the Semico contradiction in TRAD-4 is resolved.
     Prefer citing TRAD-19's figures directly to citing the chart.
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

### TRAD-11. Reading (b), the hard test: in 2024–25 mature-node utilisation, margins and prices all fell

- **Sources:**
  - Alan Patterson, "Mature-Node Foundries Face Overcapacity from China", *EE Times*, 2025-01-02.
    <https://www.eetimes.com/mature-node-foundries-face-overcapacity-from-china/>
  - "[News] Taiwan's UMC Reportedly to Slash Supplier Prices 15% in 2026—Mature Node Shake-Up Ahead",
    TrendForce, 2025-10-02.
    <https://www.trendforce.com/news/2025/10/02/news-taiwans-2nd-largest-foundry-umc-reportedly-to-slash-supplier-prices-15-in-2026-mature-node-shake-up-ahead/>
- **Verification:** Partial, 2026-09-18. Both pages were read through `WebFetch`, which returned the
  figures below as quotations. The underlying analyst products (SemiAnalysis, TechInsights) are paid
  and were **not** obtained; the TrendForce piece is itself reporting *Commercial Times* and *Economic
  Daily News*, so several figures are third-hand. Company gross margins are checkable against filings
  and were not independently checked here.
- **What it says:**
  - EE Times, attributed to Sravan Kundojjala of SemiAnalysis: mature-node foundry utilisation
    "dropped to a low 70% in 2024"; global mature-node operating profit excluding TSMC and Samsung
    "plunged by 23% from the previous year"; mature-node average selling prices "declined 5% on
    average"; China's logic and foundry capex "soared in 2024 by about 30% from the previous year".
  - EE Times, attributed to Dan Hutcheson of TechInsights: "China's capacity can address well over
    half of mature- and essential-node chip demand"; global fab utilisation for mature and
    essential-node chips is "well below 80%".
  - TrendForce/*Commercial Times*: UMC told suppliers "all supply contracts must see a price
    reduction of at least 15%" from 2026-01-01; "UMC's gross margin has fallen from 45.12% in 2022 to
    27.72% in H1 this year"; "Chinese foundries, led by SMIC and Hua Hong, are continuing to expand
    28nm to 90nm capacities".
  - TrendForce/*Economic Daily News*: mature-node utilisation "could fall from around 70% in the
    first half to 60% or lower in the second half" of 2025; Q3 orders "dropped 20–30% from Q2 levels".
- **Bears on:**
  - **Reading (b) (challenges it hard).** If mature-node growth showed that the economics at the
    trailing edge are durably good, 2024–25 should not have looked like this: utilisation in the 60s
    and 70s, prices down 5%, operating profit down 23%, a 15% supplier price cut, and UMC's gross
    margin down 17 percentage points from 2022. That is the profile of a **subsidised capacity glut**,
    not of healthy demand.
  - **Context.** ASML predicted exactly this in 2022 (TRAD-10: "Intensified foundry competition could
    lead to period with overcapacity as players try to capture market share").
- **Used in:** not yet.
- **Caveats:**
  - 2022 was the peak of the shortage. Measuring 2024–25 against it exaggerates the fall. UMC's
    45.12% gross margin in 2022 was a shortage margin, not a normal one.
  - "Utilisation fell" is not the same as "demand fell": capacity was added very fast. Both the
    numerator and denominator moved.
  - Every figure here is attributed to a paid analyst product we did not read.

### TRAD-12. …and by 2026 it had turned round again, which is why neither year settles the question

- **Sources:**
  - "Capacity Cuts and Surging Demand for AI Power ICs Set Stage for Mature-Node Foundry Price
    Increases, Says TrendForce", TrendForce, 2026-05-07.
    <https://www.trendforce.com/presscenter/news/20260507-13036.html>
  - "AI Component Capacity Squeeze and Foundry Output Cuts to Extend Mature-Node Price Increases in
    2027, Says TrendForce", TrendForce, 2026-06-30.
    <https://www.trendforce.com/presscenter/news/20260630-13127.html>
- **Verification:** Partial, 2026-09-18. Both TrendForce press releases were read through `WebFetch`,
  which returned the quoted strings below. TrendForce's underlying research reports are paid products
  and were not obtained.
- **What it says:**
  - 2026-05-07: "average 8-inch capacity utilization rate among the world's top 10 foundries is
    projected to approach 90% in 2026", up from "around 80% in 2025", and to "remain above 80% through
    1H27". "TSMC and Samsung Foundry have been reducing 8-inch capacity since the second half of
    2025". On 12-inch mature nodes, "nearly 70% of capacity expansion is being driven by Chinese
    foundries". Foundries have "begun successfully passing through price increases to customers".
  - 2026-06-30: 8-inch utilisation "recovered to 88% in 2026 and is expected to reach 90% in the
    second half of the year"; "Foundry prices have risen across the board between the first and second
    quarters of 2026, with average increases ranging from 5% to 15%"; further increases of "5–10%
    between the second and third quarters of 2026"; increases expected "to extend through to 2027".
- **Bears on:**
  - **Reading (b) (restores some of it, but not on the original grounds).** Mature-node economics in
    2026 are tight and prices are rising — but the stated reasons are (i) **leading-edge players
    withdrawing capacity** (TSMC and Samsung cutting 8-inch) and (ii) **AI-server power management and
    interposer demand**. That is not "mature nodes are intrinsically well-priced"; it is a supply cut
    plus an AI-driven demand shock.
  - **Method (critical).** Taken together, TRAD-11 and TRAD-12 show the mature-node series swinging
    from glut to shortage in about eighteen months. **No single year of mature-node utilisation or
    pricing can be used to settle an argument about long-run economics.**
- **Used in:** not yet.
- **Caveats:** TrendForce forecasts. The 2026 figures for the second half of 2026 and for 2027 are
  projections, not outcomes.

### TRAD-13. The best counter-argument to the "Chinese subsidy glut" reading

- **Source:** Paul Triolo, "Legacy Chip Overcapacity in China: Myth and Reality", *Trustee China Hand*,
  Center for Strategic and International Studies, 2024-04-30.
  <https://www.csis.org/blogs/trustee-china-hand/legacy-chip-overcapacity-china-myth-and-reality>
- **Verification:** Partial, 2026-09-18. Read through `WebFetch`; the quoted strings below are as
  returned. The industry study it cites for the 90%/37% figures is not named in what we retrieved.
- **What it says:** the argument is that the overcapacity panic is overstated and that semiconductors
  do not behave like photovoltaics or EVs. Specific points returned:
  - Chinese share is "around 27 percent for 28-65 nm process node production, falling to around 20
    percent for 90-180 nm".
  - An industry study projecting that "by 2030 domestic capacity will be able to cover around 90% of
    domestic demand", against 37% in 2020.
  - SMIC "has gone from having 60 percent of its production for foreign customers 5 years ago to
    nearly 80 percent of capacity now used for domestic customers".
  - Leading Chinese foundries' "margins, capex, and depreciation compare favorably with industry
    averages", making it hard to attribute price cuts solely to subsidy.
  - Fabs normally run at 70–90% utilisation; the 99% of the shortage was the anomaly.
- **Bears on:**
  - **Reading (b) (mixed).** If Chinese mature-node expansion is mostly *import substitution for
    Chinese domestic demand*, then it is demand-driven after all — just demand that used to be served
    from outside China. That weakens "the growth is purely subsidy" without supporting "the trailing
    edge is intrinsically better economics".
  - **TRAD-11 (challenges it).** Triolo's point that 70–90% is normal utilisation undercuts reading
    the 2024 "low 70%" as evidence of a glut.
- **Used in:** not yet.
- **Caveats:**
  - Written 2024-04-30, before the 2024–25 margin and price deterioration in TRAD-11. It is a
    forecast that has since been partly tested and did not do well on the near term.
  - CSIS is a think tank with funders and a policy position; this is advocacy as well as analysis.

---

## Related corroboration, and evidence against the declining-demand story

### TRAD-14. A second, independent count of leading-edge manufacturers: 18 at 130 nm in 2001

- **Source:** Mark LaPedus, "Foundry Wars Begin", *Semiconductor Engineering*, 2021-04-19.
  <https://semiengineering.com/foundry-wars-begin/>
- **Verification:** Partial, 2026-09-18. Read through `WebFetch`, which returned the quoted strings
  below. The IBS data behind the 18 figure is a paid product and was not obtained.
- **What it says:**
  - "In 2001, there were 18 chipmakers with fabs that could process 130nm chips, which was the
    leading-edge process at the time", attributed to IBS.
  - "Today, Samsung and TSMC are the only two foundry vendors capable of providing processes at the
    most advanced logic nodes, namely 7nm and 5nm", with Intel re-entering foundry in March 2021.
- **Bears on:**
  - **H1 (supports).** A second, independently published data point on the same consolidation already
    recorded in [`../references/costs-and-consolidation.md`](../references/costs-and-consolidation.md)
    COST-3.
  - **H5 (context).** Fewer manufacturers is a *supply-side* count. It says who will serve you, not
    how many people want a chip.
- **Used in:** not yet.
- **Caveats:**
  - COST-3 records "more than two dozen in 1998; three by 2020"; this gives 18 in 2001. **These are
    not the same count** — different years, and "chipmakers with fabs that could process 130nm"
    includes IDMs making their own parts, whereas "two foundry vendors" counts merchant foundries
    only. Do not blend them into one series.
  - The often-quoted "18–28 in 2001–2002 down to 3" is therefore at least two different counts
    stitched together. Anyone using it must say which definition they mean at each end.

### TRAD-15. Against the story: the designs did not disappear, they got bigger — Gartner's own figures

- **Source:** Kurt Shuler, "The Three Consequences Of Fewer Design Starts", *Semiconductor
  Engineering*, 2012-03-22.
  <https://semiengineering.com/the-three-consequences-of-fewer-design-starts/>
  The author was Vice President of Marketing at Arteris; the post is labelled "SPONSOR BLOG". It
  reports figures from the Gartner report in TRAD-1 and from "Gartner Webinar Semiconductor Forecast:
  1Q12 Update", 2012-03-08 (analysts named as Bryan Lewis, Peter Middleton and Jim Walker).
- **Verification:** Verified 2026-09-18 — the page was fetched directly (HTTP 200) and the strings
  below are copied from it. **Verified for what Shuler published**; the underlying Gartner report and
  webinar are paywalled and were not obtained.
- **What it says**, verbatim:
  - "Bryan and Ganesh found that as the number of design starts in our semiconductor industry
    continues its slow, inexorable decline, the value, complexity and chip units per design are
    increasing."
  - "ASIC and ASSP design starts decreased by 2.3% from 2010 to 2011."
  - "Design starts are expected to decrease an average of 2.9% per year through 2016."
  - "ASICs earning greater than $30 million through their product life cycle increased to 11% in 2011,
    from 8 % in 2010." (the space in "8 %" is the source's)
  - "ASIC designs with a product run of over 5 million units increased to 17% of all ASIC design
    starts in 2011, from 12% in 2010."
  - "ASICs with a gate count greater than 60 million gates were 15% of the total in 2011, an increase
    from 12% in 2010."
- **Bears on:**
  - **H5 (challenges the way the design-starts series is usually read).** This is the strongest public
    support for "design starts fell partly because designs got bigger and absorbed what used to be
    several chips". The same Gartner data that gives the falling count gives rising revenue per
    design, rising units per design and rising gate count per design. A falling count of starts is
    therefore **not** by itself evidence that less custom silicon is wanted.
  - **H1 (supports).** It also shows the bar rising: by 2011 a larger share of designs needed >5m
    units and >$30m lifetime revenue to make sense. That is the exclusion mechanism the project's
    thesis is about, measured.
  - **Both at once.** The same four bullets support the thesis's *mechanism* and undercut its
    *headline metric*. Use them together or not at all.
- **Used in:** not yet.
- **Caveats:**
  - A vendor sponsor blog. Arteris sells SoC interconnect IP and benefits from the "fewer, bigger
    chips" narrative. The figures are nonetheless specific, attributed and dated.
  - The year-on-year changes (8%→11%, 12%→17%, 12%→15%) are one year's movement, not a trend.
  - -2.3% from 2010 to 2011 is a far milder number than the chart's Section A slope (TRAD-1).

### TRAD-16. Against the story: TSMC's own count of distinct products has grown, not shrunk, 2019–2025

- **Sources:** TSMC annual reports and business overviews, `investor.tsmc.com`:
  - 2019: <https://investor.tsmc.com/static/annualReports/2019/english/pdf/2019_tsmc_ar_e_ch5.pdf>
  - 2020: <https://investor.tsmc.com/sites/ir/annual-report/2020/2020_Business_Overview_E.pdf>
  - 2021: <https://investor.tsmc.com/sites/ir/annual-report/2021/2021_Business_Overview_E.pdf>
  - 2022: <https://investor.tsmc.com/sites/ir/annual-report/2022/2022_Business_Overview_E.pdf>
  - 2023: <https://investor.tsmc.com/sites/ir/annual-report/2023/2023_Business_Overview_E.pdf>
  - 2024: <https://investor.tsmc.com/sites/ir/annual-report/2024/2024%20Business%20Overview_0.pdf>
  - 2025: <https://investor.tsmc.com/sites/ir/annual-report/2025/2025%20Annual%20Report_E.pdf>
- **Verification:** Verified 2026-09-18. Each PDF was downloaded and its text extracted; each figure
  below comes from the sentence quoted from that year's own document. (The 2020 and 2022 PDFs return
  HTTP 403 to a plain scripted request and were retrieved through `WebFetch`, which saved the PDF
  locally; the text was then extracted from the saved file.)
- **What it says:**

  | Year | Different products | Distinct technologies | Different customers |
  |---|---|---|---|
  | 2019 | 10,761 | — | 499 |
  | 2020 | 11,617 | 281 | 510 |
  | 2021 | 12,302 | 291 | 535 |
  | 2022 | 12,698 | 288 | 532 |
  | 2023 | 11,895 | 288 | 528 |
  | 2024 | 11,878 | 288 | 522 |
  | 2025 | 12,682 | 305 | 534 |

  Sample sentences, verbatim: "TSMC manufactured 10,761 different products for 499 customers in
  2019."; "The Company manufactured 11,617 different products using 281 distinct technologies for 510
  different customers in 2020."; "In 2025, the Company manufactured 12,682 different products using
  305 distinct technologies for 534 different customers."
- **Bears on:**
  - **H5 (challenges).** This is the only *long, primary, audited-company* public series on the number
    of distinct chip products found anywhere in this work. At the largest foundry in the world the
    number of distinct products rose 17.9% from 2019 to 2025 (`DERIVED`: 12,682 / 10,761 − 1 =
    0.1785), and the number of customers rose from 499 to 534. It did not fall.
  - **H5 (also supports, on the customer count).** 534 customers, essentially flat across seven years
    despite the product count moving, is a strikingly small and stable number for the world's largest
    foundry. The set of organisations that can buy from TSMC is not growing.
- **Used in:** not yet. Overlaps
  [`../references/customer-concentration.md`](../references/customer-concentration.md) CONC-2, which
  records the 2024 sentence.
- **Caveats:**
  - **One company.** TSMC gained foundry share over this period, so its product count can rise while
    the industry total falls. This is not an industry series.
  - A "different product" here is a part TSMC manufactured in that year — a **stock**, like ASML's
    mask sets (TRAD-7), not a flow of new designs. It includes long-running parts. Do not compare it
    to a design-start count as a level or as a rate.
  - The 2019 figure is from a different sentence form and does not state a technology count.
  - The 2023–24 dip and 2025 rebound track the industry cycle, not a structural change.

### TRAD-17. Against the story: semiconductor revenue set records through the whole period

- **Source:** "Global Annual Semiconductor Sales Increase 25.6% to $791.7 Billion in 2025",
  Semiconductor Industry Association, 2026-02-06.
  <https://www.semiconductors.org/global-annual-semiconductor-sales-increase-25-6-to-791-7-billion-in-2025/>
  Monthly sales are compiled by World Semiconductor Trade Statistics (WSTS).
- **Verification:** Verified 2026-09-18. The page was fetched directly (HTTP 200) and the strings
  below are copied from it. The live page returns HTTP 403 to `WebFetch`; a scripted request with an
  ordinary browser user-agent succeeds.
- **What it says**, verbatim:
  - "global semiconductor sales hit $791.7 billion in 2025, an increase of 25.6% compared to the 2024
    total of $630.5 billion"
  - "Sales of logic products increased by 39.9%, totaling $301.9 billion in 2025, making it the
    largest product category by sales."
  - John Neuffer, SIA president and CEO: "The global semiconductor industry posted its highest-ever
    annual sales in 2025, nearly hitting $800 billion, and global sales in 2026 are projected to reach
    roughly $1 trillion".
- **Bears on:**
  - **H5 (challenges, but only in one direction).** Any claim that "traditional chip demand is
    declining" has to be stated carefully: **revenue is at record highs and accelerating.** What is
    claimed to be declining is the *number of distinct commercial design projects*, which is a
    different quantity and can move the opposite way (TRAD-15). Never let the two be conflated.
- **Used in:** not yet.
- **Caveats:**
  - **Revenue, not units.** No public unit-shipment series was found in the SIA material retrieved;
    the 2025 SIA Factbook charts "Annual Semiconductor Shipments ($ Billion)", i.e. dollars. An
    industry unit series remains **not found**.
  - The 2025 number is heavily AI- and memory-driven and is not representative of the broad market.
  - The release contains an apparent error in its own text: "Memory products were second in terms of
    sales, increasing by 34.8% **in 2024** to a total of $223.1 billion" appears in the paragraph about
    2025. Quoted here exactly as published; do not silently correct it.

### TRAD-18. Against the story: chip startup funding is at record levels

- **Source:** Jesse Allen, "Startup Funding: Q1 2026", *Semiconductor Engineering*, 2026-04-13.
  <https://semiengineering.com/startup-funding-q1-2026/>
- **Verification:** Partial, 2026-09-18. Read through `WebFetch`; the quoted strings below are as
  returned. Not read directly.
- **What it says:** "80 startups raise $8.4B" in the first quarter of 2026; 18 companies raised rounds
  above $100 million; Rapidus and Cerebras each reached $1 billion; the majority of the large rounds
  are for chips "designing chips primarily for AI inference workloads or attempting to overcome
  bandwidth limitations".
- **Bears on:**
  - **H5 (challenges).** If the up-front cost of a chip were an absolute barrier, one would not expect
    80 private companies to raise $8.4bn in a quarter to design chips. Money is not the binding
    constraint at the top of the market.
  - **H5 (supports, on reflection).** $8.4bn across 80 companies is `DERIVED` an average of
    8,400 / 80 = **$105m each**. That is the *entry ticket*, and it is consistent with the project's
    claim that a chip project is out of reach of anyone without nine figures of capital. The evidence
    cuts both ways and must be quoted with both readings.
- **Used in:** not yet.
- **Caveats:**
  - Highly skewed: two of the 80 took $1bn each, so the mean above is not a typical round. A median
    would be far lower and was not published.
  - One quarter, at the top of an AI capital cycle.
  - "Semiconductor startups" here includes equipment, materials and EDA companies, not only chip
    designers.

### TRAD-19. A full Gartner ASIC design-start series, 1994–2013, published in a Xilinx fact sheet — and it never exceeds ~11,150

- **Source:** Xilinx, Inc., *Corporate Fact Sheet*, December 2009, page 3. Chart headed "ASIC
  Landscape Continues to Deteriorate: 22% Decline in 2009", y-axis "Number of Annual Design Starts",
  x-axis "Calendar Year" 1994–2013, attribution line "Source: Gartner (March 2009)".
  <http://media.corporate-ir.net/media_files/irol/21/212763/XilinxPR_factsheet_December2009_v2.pdf>
- **Verification:** Verified 2026-09-18. The PDF was downloaded directly (HTTP 200, 456,555 bytes),
  its text extracted, and page 3 rendered to an image and read. Every string quoted below is from that
  page. **The bar heights are read off a chart and are approximate**; the growth percentages are
  printed labels and are exact as printed. The Gartner data behind it is a paid product and was not
  obtained.
- **What it says:**
  - The chart's y-axis runs 0 to 12,000. **The tallest bar, 1997, is about 11,150.** The series rises
    1994–1997 and falls from 1998 onward — it is a hump, not a pure exponential decay.
  - Bar heights read off the chart, approximate, to the nearest 50: 1994 ~9,850; 1995 ~10,050;
    1996 ~10,900; 1997 ~11,150; 1998 ~9,950; 1999 ~8,950; **2000 ~7,750**; 2001 ~4,950; 2002 ~4,000;
    thereafter the bars sit between ~3,800 and ~2,050.
  - Printed growth labels, exact: 2003 **-4.3%**, 2004 **-1.8%**, 2005 **-2.4%**, 2006 **-5.9%**,
    2007 **-7.1%**, 2008 **-9.5%**, 2009 **-21.7%** (bar highlighted in red, with the callout "22%
    Decline in 2009"), 2010 **0.2%**, 2011 **-2.8%**, 2012 **-3.4%**, 2013 **-3.8%**.
  - Bryan Lewis, Gartner Analyst, quoted on the chart: "More likely, we will see a large percentage of
    these questionable designs not hit any production and die a slow death by indefinite push-outs."
- **`DERIVED` reconstruction of the series.** Anchoring on 2005 = 3,623 (TRAD-2, SKMurphy's reproduced
  Gartner table) and applying the printed growth labels in turn:

  | Year | Growth label | Derived level |
  |---|---|---|
  | 2005 | — (anchor) | 3,623 |
  | 2006 | −5.9% | 3,623 × 0.941 = **3,409** |
  | 2007 | −7.1% | 3,409 × 0.929 = 3,167 |
  | 2008 | −9.5% | 3,167 × 0.905 = 2,866 |
  | 2009 | −21.7% | 2,866 × 0.783 = 2,244 |
  | 2010 | +0.2% | 2,244 × 1.002 = 2,249 |
  | 2011 | −2.8% | 2,249 × 0.972 = 2,186 |
  | 2012 | −3.4% | 2,186 × 0.966 = **2,112** |
  | 2013 | −3.8% | 2,112 × 0.962 = 2,031 |

  **The 2006 cross-check is decisive for the label-to-year assignment:** the derived 3,409 matches the
  3,408 that EE Times published for Gartner's 2006 figure in December 2007 (TRAD-2) to within one
  unit, from two entirely independent documents. The 2007 and 2008 derived values (3,167 and 2,866)
  sit below SKMurphy's 3,196 and 3,048, which is expected — SKMurphy's table is a 2007 Gartner
  forecast, this chart is Gartner's March 2009 revision after the crash.
- **Bears on:**
  - **TRAD-3 (resolves most of it).** Gartner's ASIC design starts, on Gartner's own chart, **never
    reach 12,000 in any of the twenty years 1994–2013**. The owner's Section A begins at ~34,000 in
    2000. `DERIVED`: 34,000 / 11,150 = **3.0×** the highest value the Gartner series ever reaches. At
    2012 the gap is `DERIVED` 11,000 / 2,112 = **5.2×**. Section A's *levels* are therefore certainly
    not Gartner ASIC design starts. Either they are ASIC + ASSP with ASSP starts several times ASIC
    starts, or the axis is mis-scaled.
  - **H5 (challenges, and sharpens the challenge).** The underlying decline is real and large:
    `DERIVED` 7,749 (2000) → 2,112 (2012) is −10.27%/yr over twelve years, close to Section A's
    −8.98%/yr. **The shape of Section A is right. Its numbers are not.**
  - **H5 (also complicates it).** The 1994–1997 rise and the −21.7% in 2009 show the series is
    strongly cyclical. The mid-2000s declines are mild single digits (−1.8% to −7.1%); the collapses
    are 2001 and 2009, both recessions. Fitting a single exponential across 2000–2012 attributes to a
    secular trend what is substantially two recessions.
- **Used in:** not yet.
- **Caveats:**
  - **This is a Xilinx marketing document.** Xilinx sold FPGAs and the page is headed "Today's Global
    Economics Favor Programmable Chips". It has every reason to show ASIC design starts falling. The
    *attribution* to Gartner (March 2009) and the printed growth labels are nonetheless specific and
    checkable, and one of them reproduces an independently published Gartner figure exactly.
  - 2009–2013 on this chart are **forecasts made in March 2009**, at the trough of the financial
    crisis. Do not present 2012 = ~2,112 as an outcome. It is a 2009 forecast of 2012.
  - The chart is headed "ASIC Landscape"; the surrounding text discusses ASICs *and* ASSPs. Whether
    the bars are ASIC-only or ASIC+ASSP is **not stated**. If they are ASIC+ASSP, then Section A of
    the owner's chart is definitively mis-scaled, because there is then nothing left for ASSP to add.
  - Bar heights are read off a chart. Only the growth percentages and the axis maximum are printed.
  - The host `media.corporate-ir.net` is a legacy investor-relations CDN. Archive the PDF if it is to
    be cited.

### TRAD-20. The same Xilinx fact sheet gives an NRE cost escalation figure, and draws the long tail explicitly

- **Source:** Xilinx, Inc., *Corporate Fact Sheet*, December 2009, page 3 (same document as TRAD-19).
- **Verification:** Verified 2026-09-18 from the rendered page.
- **What it says:**
  - Verbatim: "Application-specific devices can take 12 to 24 months to design, and the fixed costs
    associated with semiconductor manufacturing have risen to an exorbitant $60 million on the most
    advanced 40nm chip-making technology from $20 million on 90nm technology, just three years ago.
    Even the tiniest mistake in implementation can result in a multimillion dollar mask re-spin,
    leading to time-to-market delays and a potentially devastating "domino effect" on a company's
    business."
  - The second chart on the page is headed "ASIC/ASSP Application Gap is Growing", sub-headed "Growing
    Number of Underserved Applications". Its axes are "Market Size" (vertical) and "Application Market
    Segments" (horizontal), with no numbers on either. The bars are labelled in three bands:
    "ASIC/ASSP Class Applications" (the tall left-hand bars), "Underserved Applications" (the middle),
    "Traditional FPGA Class Applications" (the long right-hand tail), with "+ 100s More" at the far
    right.
- **Bears on:**
  - **H1 (supports).** A dated, primary, corporate statement of NRE escalation: `DERIVED` 60 / 20 =
    **3×** in about three years, 90 nm to 40 nm. Complements the IBS design-cost figures in
    [`../references/costs-and-consolidation.md`](../references/costs-and-consolidation.md) COST-1 and
    COST-2 with a different metric ("fixed costs associated with semiconductor manufacturing") and a
    different, non-analyst source.
  - **H5 (supports, weakly but notably).** In 2009 a major semiconductor vendor published a **long-tail
    diagram of chip demand** and asserted a *growing* band of "Underserved Applications" sitting
    between what justifies an ASIC/ASSP and what a traditional FPGA serves. That is the project's H5
    claim, drawn by a chip company, sixteen years before this repository.
- **Used in:** not yet.
- **Caveats:**
  - **The long-tail chart has no numbers on either axis and no source line.** It is an illustration of
    a marketing argument, not data. It establishes that the claim was made, not that it is true. Cite
    it as an *assertion by Xilinx*, never as evidence of the tail's size.
  - Xilinx's commercial interest here is direct: the "underserved" band is exactly what it wanted to
    sell FPGAs into.
  - "$60 million" is not defined — it is "fixed costs associated with semiconductor manufacturing",
    which may or may not mean the mask set, and may or may not include design. Do not present it as a
    mask-set cost. `../references/costs-and-consolidation.md` COST-1 puts total 7 nm *design* cost at
    about $249m, which is a different and much larger quantity; the two are not comparable.
  - December 2009. Superseded by a decade and a half of further escalation.

---

## Verdict on the two readings

**Reading (a) — how can mature-node products grow >40% while design starts fall?** They can, easily,
and the reconciliation is not interesting: ASML counts a **stock** ("# of mask sets (products) **in
production**", TRAD-7) and Gartner counts a **flow** ("a unique tapeout", TRAD-2). A stock of products
in production rises whenever products are retired more slowly than they are added, which is exactly
what long automotive and industrial lifetimes produce. Three further points are established:
ASML says the migration is *upward*, from mature to advanced (TRAD-8, page 22), so the mature stock is
not being fed by aging leading-edge designs; there is genuine new mature-node demand from automotive
electrification, sensors and smart grids, in ASML's words and TSMC's (TRAD-8, TRAD-9); and the two
series count different populations anyway. **The >40% is not evidence of >40% more design activity and
must never be used as if it were.** The owner's caption phrasing "40% increase in **new** products" is
the flow reading and is not what ASML's slide says.

**Reading (b) — does mature-node growth show the leading edge is not always economically superior?**
*Partly, and much more weakly than it looks.*

- **For it:** ASML's own 2020–2030 planning puts the largest single block of added wafer capacity at
  mature nodes, +380 of +930 kwspm/yr, `DERIVED` 40.9% (TRAD-9). Products in production at ≥28 nm grew
  >40% over 2012–2021 (TRAD-7). New applications keep appearing at nodes twelve to twenty years old
  (TRAD-8). None of that is what one would see if the leading edge dominated on economics everywhere.
- **Against it:** ASML itself carves out +150 of the +930, `DERIVED` **16.1%**, as driven by
  "Technological sovereignty and foundry competition" rather than demand, and calls the resulting
  capacity "~10% inefficiency" (TRAD-10). Advanced logic grows at **12.0%/yr against mature's 6.0%/yr**
  — mature is bigger only in absolute terms, off a much larger base (TRAD-9). And when the shortage
  ended, mature-node economics were poor: utilisation in the 60s–70s, ASPs down 5%, operating profit
  ex-TSMC/Samsung down 23%, a 15% supplier price cut at UMC (TRAD-11).
- **The honest answer:** the ASML chart is drawn across 2012–2021 and its "past few years" callout
  starts at 2015. That window **ends at the peak of the worst semiconductor shortage in the industry's
  history.** It is a shortage-flattered window. When the 2024–25 data arrived, mature nodes behaved
  like a subsidised glut, not like a structurally superior business (TRAD-11); by 2026 they had
  tightened again, but for reasons — leading-edge players *withdrawing* mature capacity, plus AI power
  ICs — that are not about mature-node economics being intrinsically good (TRAD-12). The best
  counter-argument to the subsidy reading is that Chinese expansion is import substitution for real
  Chinese domestic demand (TRAD-13), which is demand-driven but says nothing about relative node
  economics.
- **What survives:** a narrow, defensible claim. *Mature nodes are not dying, they attract real
  investment, and new applications keep appearing there.* That is enough to refute "the leading edge is
  always and everywhere the right place to be". It is **not** enough to claim that mature-node
  economics are good, or improving, or that the market would reward a new entrant there. The 2024–25
  evidence points the other way.

**What contradicts the "traditional demand is declining" story, in order of force:**

1. **TRAD-15.** Gartner's own data says the count fell while value, units and gate count *per design*
   rose. The metric may be measuring integration, not demand.
2. **TRAD-4.** Semico — the house named on half the owner's chart — publicly said ASIC design starts
   *grew* 3–5% a year through the period that half covers.
3. **TRAD-16.** TSMC's distinct product count rose 17.9% from 2019 to 2025 and its customer count rose.
4. **TRAD-17.** Semiconductor revenue is at record highs, $791.7bn in 2025, up 25.6%.
5. **TRAD-7 to TRAD-9.** Mature-node products in production grew >40%; mature nodes are the largest
   block of planned capacity addition to 2030.
6. **TRAD-18.** 80 chip startups raised $8.4bn in one quarter of 2026.
7. **TRAD-1.** Even Gartner's own report contains a "Contrarian View" that FPGA/PLD design starts were
   set to *grow* while ASIC/ASSP starts slowed — the custom-function demand moved, it did not vanish.

The strongest surviving version of the project's own claim is therefore **not** "fewer chips are
wanted". It is: *the number of organisations for whom a commercial custom chip is economically
possible has shrunk, the bar per design has risen, and the foundries serve a small and stable set of
customers.* TRAD-14, TRAD-15 and TRAD-16 (the flat 499→534 customer count) all support that narrower
claim. The broad "design starts are collapsing" claim, as drawn on the owner's chart, does not
survive.

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
   TRAD-14 of this file as a second, independent data point on the same decline, **with the warning
   in TRAD-14's caveats**: "18 chipmakers with fabs that could process 130nm in 2001" and "three
   foundries by 2020" are not the same count and must not be drawn as one line.

4. **`resources/references/customer-concentration.md`, CONC-2** — CONC-2 records TSMC's 2024 sentence
   in isolation. The 2019–2025 series is in TRAD-16 of this file and shows the count *rising*
   (10,761 → 12,682 products; 499 → 534 customers). Suggested added caveat for CONC-2:

   > The 522 customers of 2024 is a cyclical low, not a trend: TSMC reported 499 (2019), 510 (2020),
   > 535 (2021), 532 (2022), 528 (2023), 522 (2024) and 534 (2025). See
   > [`../demand/design-starts-and-mature-nodes.md`](../demand/design-starts-and-mature-nodes.md)
   > TRAD-16.

5. **`resources/hypotheses.md`, H5** — the evidence in this file is genuinely two-sided and the H5
   status line should say so. Suggested addition to H5's evidence list:
   "Commercial design starts: TRAD-1 to TRAD-6 (the widely used 2000–2025 chart is two incompatible
   series; the Gartner half supports a decline, the Semico half is contradicted by Semico's own
   published growth rates). Mature nodes: TRAD-7 to TRAD-13 (products in production at ≥28 nm grew
   >40%, but it is a stock not a flow)."

## Open questions

- What is Gartner's count of **ASSP** design starts? A single public figure would decide between the
  two readings in TRAD-3. TRAD-19 narrows it: if the Xilinx chart is already ASIC+ASSP, the question
  is closed and Section A is simply mis-scaled. The chart does not say which it is.
- **Is the owner's Section A perhaps not a Gartner series at all?** Its levels match nothing Gartner
  published. Someone should ask where the chart's numbers were actually taken from before the chart
  is used anywhere.
- What is **Semico's definition** of a design start, and what absolute level does it report? Neither
  was found in public.
- Does any public source give **new mask sets per year** (a flow) at mature nodes, rather than mask
  sets in production (a stock)? That would be the series directly comparable in direction to design
  starts.
- Where does the owner's caption on the ASML chart come from? It is not ASML's wording in either the
  2021 or 2022 Investor Day deck.
- Is there a public **unit-shipment** series for the industry, as opposed to a revenue series? The
  2025 SIA Factbook charts dollars only. WSTS holds the unit data and sells it.
- **Mask-set cost by node was not verified.** TRAD-20 gives one dated primary figure for "fixed costs
  associated with semiconductor manufacturing" ($20m at 90 nm rising to $60m at 40 nm), but that is
  not a mask-set cost and stops at 2009. Searching for a modern per-node mask-set cost produced only
  secondary marketing and
  aggregator pages quoting incompatible figures (e.g. 7 nm variously "$3–$5M" and "$15 million"),
  with no primary source. The best-known primary-ish figures are IBS's, which are a paid product;
  SemiAnalysis's treatment is behind a paid newsletter. Neither was obtained and neither should be
  quoted from a search summary. `../references/costs-and-consolidation.md` COST-1 and COST-2 already
  hold the IBS *design*-cost figures with their provenance; a mask-set-cost entry should be added
  only when a citable primary figure is found.
- Does Gartner still publish an ASIC/ASSP design-starts series after 2015? Gartner document
  2967017, "Forecast: ASIC and ASSP Chip Design Starts, Worldwide, 2015 Update", exists in Gartner's
  public catalogue; nothing later was found. If the series was discontinued, that is itself worth
  recording.

## Sources that could not be reached, and why

| Source | Blocker |
|---|---|
| Gartner G00229088 report body (TRAD-1) | Paid product. Live page returns HTTP 403 to automated fetch; only the archived abstract and contents page was used. No attempt made to obtain the body. |
| Gartner "Forecast: ASIC and ASSP Chip Design Starts, Worldwide, 2015 Update" (doc 2967017) | Paid product; not obtained. |
| Semico SC101-12 / SC106-16 / SC107-16 / SC107-22 / SC106-23 report bodies (TRAD-4) | Paid products. `semico.com` now redirects every page to `/lander`; only Internet Archive captures of the public press pages were used. |
| IBS leading-edge manufacturer counts (TRAD-14) and IBS mask-cost figures | Paid product; not obtained. |
| SemiAnalysis mature-node analysis (TRAD-11) | Paid newsletter; only the EE Times report of it was used. |
| TechInsights capacity figures (TRAD-11) | Paid product; only the EE Times report of it was used. |
| TrendForce research reports behind TRAD-12 | Paid products; only the free press releases were used. |
| `www.eetimes.com` direct fetch (TRAD-2, TRAD-6) | Two scripted HTTPS requests timed out after 120 s each. Those pages were read only through a summarising fetch tool, so their entries are Partial. |
| `www.sec.gov` direct fetch | Returns HTTP 403 to an ordinary browser user-agent. SEC asks requesters to identify themselves in the User-Agent; we do not put personal details in headers, so SEC URLs were read through a fetch tool instead. The ASML deck was obtained from `media.asml.com` directly in any case. |
| EE Times, "Sockets scant for costly ASICs" (the origin of the Gartner table in TRAD-2) | Not located; only SKMurphy's reproduction of the chart was found. |
