# Published prices, and what it costs to serve a small customer (`SMB`)

H6 says that a fab which does no per-customer engineering and sells machine time at published prices
can make money from each small customer. Two things can be checked against public sources: whether
anyone actually publishes prices for small-volume chip fabrication, and what those prices look like
next to the underlying wafer and mask cost.

The short answer to the first question is **yes, several organisations have published MPW prices
openly for decades, and the commercial foundries do not.** The short answer to the second is that
almost the entire price a small customer pays is fixed cost per project, not silicon.

---

### SMB-7. Europractice publishes a full MPW price list, and every line has a minimum billable area

- **Source:** EUROPRACTICE IC Service, "Schedules & Prices 2025":
  <https://europractice-ic.com/schedules-prices-2025/>
- **Verification:** Verified 2026-09-18. The page was fetched and the price tables and their
  footnotes read directly out of the page text.
- **What it says:**
  - Two price columns throughout, "Standard EUR / mm²" and "Discounted EUR / mm²". The discount
    rule: "Customer is an academic institution or a research facility from one of the 27 EU
    countries together with Albania, Armenia, Azerbaijan, Bosnia-Herzegovina, Georgia, Iceland,
    Israel, Liechtenstein, North Macedonia, Moldova, Montenegro, Norway, Switzerland, Turkey,
    Serbia, the UK and Ukraine." … "Standard prices apply to all other customers."
  - **GlobalFoundries MPW price list** (Standard / Discounted, EUR per mm²), with the minimum
    billable area from the numbered footnotes:

    | Technology | Standard | Discounted | Minimum billable area |
    |---|---|---|---|
    | SiGe 8XP | 5,060 | 4,600 | 12 mm² |
    | 130 nm BCDlite | 1,760 | 1,600 | 12 mm² |
    | 55 nm BCDlite | 5,720 | 5,200 | 9 mm² |
    | 45RFE | 10,230 | 9,300 | 12 mm² |
    | 45RFSOI | 10,230 | 9,300 | 12 mm² |
    | 45 nm SPCLO Silicon Photonics | 242,000 | 220,000 | fixed 5 mm × 5 mm block |
    | 28 nm SLPe | 12,430 | 11,300 | 4 mm² |
    | 22 nm FDSOI | 18,975 | 17,250 | 4 mm² |
    | 12 nm LP+ | 31,240 | 28,400 | 4 mm² |
    | **180 MCU (Open PDK)** | **913** | **830** | **6 mm²** |

    Footnote 1, verbatim: "Price = area (mm²) * price/mm² with min. fabrication cost equivalent to
    12 mm². Any edge length between 1.0 mm to 11 mm is possible. The mentioned die size is referred
    to the Pre-Shrink die size."
  - **IHP price list** (EUR per mm², Standard / Discounted): SG13C SiGe:C RF CMOS 4,500 / 3,825;
    SG13G2 SiGe:C Bipolar/Analog 7,300 / 6,205; SG13G3 9,000 / 7,650. Footnote: "Price = area (mm 2 )
    * price/mm 2 with min. fabrication cost equivalent to 0.8mm 2 ."
  - **STMicroelectronics:** "All prices have a minimum charge of 1.25mm² including seal-ring."
  - **TSMC's full MPW prices are not in the table.** The page says only: "Prices for TSMC
    technologies can be calculated through the online Price Request Form:".
  - **An explicit charge for being small:** "When four or more independent sub-designs are registered
    in one MPW submission to optimize the minimum charged area, an additional verification charge of
    1,000 EUR will be applied." (An equivalent clause elsewhere on the page reads "1,000 USD is
    applicable. This is regardless of the request and charges for sub die sawing (6 USD per
    additional die obtained from the base MPW submission).")
  - A cancellation fee: "A cancellation fee is applicable if the registration is cancelled later
    than 2 weeks after the Registration deadline or if the customer is unable to provide a DRC-clean
    GDS before the Tapeout deadline."
- **DERIVED (arithmetic written out):** the cheapest ticket a commercial customer can buy on the
  open-PDK node is 6 mm² × €913/mm² = **€5,478**. On GF 130 nm BCDlite it is 12 × €1,760 =
  **€21,120**. On 12 nm LP+ it is 4 × €31,240 = **€124,960**.
- **Bears on:**
  - **H6 and H8 (supports).** Publishing prices for small-volume fabrication is not a novelty. A
    European broker has done it for thirty years, openly, with no login and no quote request.
  - **H6 (challenges).** Every technology carries a minimum billable area, and those minima are
    exactly what a fixed cost of serving a customer looks like when it is turned into a price. The
    "additional verification charge of 1,000 EUR" for four or more sub-designs in one submission is
    a vendor charging, in cash, for the extra handling of splitting one block among several small
    customers. H6 assumes that cost away; Europractice bills for it.
- **Used in:** not yet.
- **Caveats:**
  - Europractice is a subsidised broker, not a fab (see SMB-6). Its prices are not a foundry's costs.
  - The discounted column is for European academic and research users only; the standard column is
    the one relevant to a commercial small customer.
  - The prices exclude packaging and test unless a line says otherwise.
  - The 2026 list exists at `/schedules-prices-2026/` and was not read.

### SMB-8. MOSIS published its prices as a fixed fee plus a rate per mm², and the fixed fee dominated

- **Sources** (Internet Archive copies of `mosis.com`, whose live pages are gone):
  - MOSIS domestic price list, valid through 1998-12-31, archived 1998-12-02:
    <https://web.archive.org/web/19981202003231id_/http://www.mosis.com:80/New/Orders/Prices/price-list-domestic.html>
  - "How to Calculate 0.13 Micron Domestic Prices", archived 2003-03-01:
    <https://web.archive.org/web/20030301050415id_/http://www.mosis.com/Orders/Prices/13micron-price-example.html>
- **Verification:** Verified 2026-09-18 from the archived pages, fetched with `curl` using the
  Wayback `id_` raw-content form. (`WebFetch` refuses `web.archive.org` outright, so archived pages
  have to go through `curl`.)
- **What it says:**
  - **1998, Orbit 2.0 micron CMOS.** "Prices are per design, and prices are the same packaged or
    unpackaged." Part 10011: "2.30 x 2.30 mm 'TinyChip' (purchase add'l parts in lots of 4)", unit
    "Lot of 4", **standard price $620, discount price $590**. The next size up, 4.60 × 6.80 mm, first
    12 parts: $2,910 standard / $2,790 discount.
  - **2003, IBM 0.13 micron.** "The minimum area for 0.13 micron processes is 10.0 mm²." Worked
    example for a 32.081 mm² design, 40 parts in 84-PGA packages: "First lot of 40 parts (rounded to
    nearest whole dollar): **$17,500 + ($4,000/mm² * 32.081 mm²) = $145,824**"; "Assembly (rounded to
    nearest whole dollar): 40 parts x $40/part = $1,600".
- **DERIVED (arithmetic written out):**
  - At the 0.13 µm minimum area of 10 mm², the price is $17,500 + (10 × $4,000) = **$57,500**, of
    which **$17,500, or 30%, is the fixed per-project charge** that does not depend on area at all.
  - The 1998 TinyChip is 2.30 × 2.30 mm = 5.29 mm² for $620, i.e. about **$117/mm²** including four
    parts.
- **Bears on:**
  - **H5 and H4 (supports).** A $620 chip was on a public price list in 1998. "Anyone can buy a chip
    for a few hundred dollars" is not a new idea, and the argument that cost was the only barrier
    has to explain why the tail did not appear then (see SMB-5: MOSIS peaked at about 3,000 orders
    a year).
  - **H6 (challenges, usefully).** This is the clearest public decomposition found of the price of
    serving one small customer: a flat charge per project, plus silicon. The flat charge went from
    $2,500 at 0.35 µm to $19,000 at 0.18 µm to $17,500 at 0.13 µm. A foundry.api that sells machine
    time has the same fixed cost per customer to cover, and nothing in the model removes it.
- **Used in:** not yet.
- **Caveats:**
  - These are twenty-five- and twenty-year-old prices for obsolete nodes, useful for structure
    rather than level.
  - Archived pages: the figures are as MOSIS published them at the time, not audited.
  - The 0.18 µm figures ($19,000 + $1,640/mm², minimum 7.0 mm², archived 2001) and the 0.35 µm
    figures ($2,500 + $820/mm², minimum 4.0 mm², archived 2000) come from sibling pages in the same
    archive that were reported to us but that we did not open ourselves: treat those two as
    **Partial**.

### SMB-9. chipIgnite: a published, flat, all-in price for a 130 nm tape-out — $9,750 in 2021, $14,950 today

- **Sources:**
  - Efabless Corporation, "Efabless Launches chipIgnite with SkyWater to Bring Chip Creation to the
    Masses", GlobeNewswire, dateline "SAN JOSE, Calif. and BLOOMINGTON, Minn., May 20, 2021":
    <https://www.globenewswire.com/news-release/2021/05/20/2233541/0/en/Efabless-Launches-chipIgnite-with-SkyWater-to-Bring-Chip-Creation-to-the-Masses.html>
  - ChipFoundry (operated by UmbraLogic Technologies LLC), "chipIgnite" product page:
    <https://chipfoundry.io/chipignite>
- **Verification:** **Verified 2026-09-20.** Both prices were read on the pages cited, and the
  $14,950 figure was independently confirmed against ChipFoundry's own live metrics API and its
  April-2025 launch page (`CF-1`, `CF-11`). Note the correction below: **$9,750 → $14,950 is not one
  price rising.** ChipFoundry launched at $14,950 in April 2025, five months before it acquired
  Efabless's assets, so these are two flat prices set by two different companies.
- **Verification:**
  - The ChipFoundry page: **Verified 2026-09-18**, fetched and read directly.
  - The 2021 press release: **Verified 2026-09-18** by fetching the page itself, but through
    `WebFetch` rather than `curl` — the host refused the `curl` request (exit 92, no HTTP response).
    The quotes are as `WebFetch` returned them from the page.
- **What it says:**
  - 2021: "The starting price of $9750 per project includes 100 QFN or 300 WCSP packaged parts and
    five evaluation boards." / "The program provides users 10 mm2 of total project area with
    fabrication for projects using the SkyWater Open Source PDK." / "SkyWater's open source 130 nm
    CMOS platform will be used to fabricate chips for the chipIgnite program."
  - 2026, ChipFoundry's chipIgnite page, as headline bullets: "**$14,950 per tapeout**" / "Reserve
    space for your project on an upcoming shuttle" / "User Design Area — Up to 15mm² of die space
    with a standard I/O ring" / "Configurable IO — 38 fully -configurable I/Os supporting both
    digital and analog signaling" / "Predesigned Packaging — Option of 100 QFN-packaged parts or
    Bare Die" / "Open-source or Commercial EDA Tool Support — Includes complete RTL-to-GDSII
    open-source design flow". Page footer: "© 2026 UmbraLogic Technologies LLC".
- **DERIVED (arithmetic written out):**
  - 2021: $9,750 ÷ 10 mm² = **$975 per mm²**, packaging and 100 parts included.
  - 2026: $14,950 ÷ 15 mm² = **$997 per mm²** at full area; $14,950 ÷ 100 parts =
    **$149.50 per packaged chip**.
  - Price change 2021 → 2026: 14,950 ÷ 9,750 = **+53%** on the headline, though the area rose from
    10 mm² to "up to 15 mm²", so the per-mm² price is almost unchanged.
  - The comparison with Europractice's cheapest line (SMB-7) needs a rate, so here it is: at the
    **ECB euro reference rate for 2026-09-17, EUR 1 = USD 1.1481**
    (<https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml>), GF 180 MCU (Open PDK) at
    €913/mm² standard = **US$1,048/mm²**, against chipIgnite's $975/mm² (2021) and $997/mm² (2026).
    The margin is about 5%, so the comparison turns on the exchange rate: below roughly
    USD 1.09 per euro it reverses.
- **Bears on:**
  - **H6 and H8 (supports).** A flat, published, no-negotiation price for a complete 130 nm tape-out
    with packaged parts, sold to anyone. This is the closest existing thing to what foundry.api
    proposes, and at the exchange rate given above it is cheaper per mm² than any commercial MPW
    line in SMB-7 — but only just, and only at that rate.
  - **H6 (context).** The price survived the collapse of the company that invented it: Efabless shut
    down in March 2025 (`OPEN-7`) and the programme was restarted by its founders under a new company
    at a higher price. The product was viable enough for someone to pick up; the company was not.
- **Used in:** not yet.
- **Caveats:**
  - A published headline price is not a margin. Neither Efabless nor ChipFoundry publishes what it
    costs them, and Efabless's failure to raise money is the only signal we have about whether the
    price covered the cost.
  - "Up to 15mm²" is the ceiling, not the billed quantity; the per-mm² derivation is therefore a
    *best case* for the buyer.
  - **Corrected 2026-09-20.** This previously read "ChipFoundry's other prices are behind 'Request a
    Quote'; only the chipIgnite headline is public." That is wrong. ChipFoundry publishes a **36-block
    IP catalogue at $6,200–$33,900** (group tiers to $42,900), **SRAM at $2,500**, ML packages at
    **$22,250 / $45,000**, support at **$1,000 per 5 hours** and training at **$450 a seat**. See
    `CF-11` in [`chipfoundry.md`](chipfoundry.md). A Tier-1 IP licence is **2.9× a tapeout**, so any
    revenue estimate built on shuttle slots alone counts the razor and none of the blades.

### SMB-10. Tiny Tapeout publishes a per-tile price of €70, and charges per analog pin per customer

- **Source:** Tiny Tapeout, "Analog Specs": <https://tinytapeout.com/specs/analog/>
- **Verification:** Verified 2026-09-18, fetched and read.
- **What it says:**
  - "Projects with analog pins must be two tiles high. This means that the minimum price for the area
    of the project is 140€ (each tile is 70€)."
  - "In addition, there is a cost for each analog pin attributable to a given customer (rather than
    project) on a given shuttle. The price for analog pins is 40€ per pin for the first 2 pins you
    need on the Tiny Tapeout shuttle, and 100€ per pin for additional pins."
  - Worked examples given on the page: "You submit a design requiring 1x2 tiles and 2 analog pins.
    This costs you 220€ (140€ for the tiles, and 80€ for the analog pins)." and "You then submit
    another design on the same shuttle, itself requiring 2x2 tiles and 3 analog pins. This would cost
    you 580€ (280€ for the tiles, and 300€ for the analog pins)."
  - Scope: "This price is only for including the design in the shuttle, and does not include the cost
    of the ASIC, PCB, or shipping."
  - Geometry: "1x2 tiles = 160x225um", "2x2 tiles = 334x225um".
- **Bears on:**
  - **H6 and H8 (supports).** €70 is the smallest published unit of chip manufacturing we found
    anywhere. It is also a genuinely published price: no login, no quote.
  - **H6 (context, and a neat one).** The analog-pin charge is explicitly "attributable to a given
    customer (rather than project)", and the second pin pair costs 2.5× the first. That is a
    published price schedule in which the *customer*, not the design, is the billable unit — which
    is precisely the distinction H6 turns on.
- **Used in:** not yet.
- **Caveats:**
  - **DERIVED, and approximate:** if a 1×2 tile pair is 160 × 225 µm = 0.036 mm², then one tile is
    about 0.018 mm² and €70 per tile is roughly **€3,900 per mm²** on a 130 nm process — about twice
    Europractice's standard 130 nm BCDlite rate of €1,760/mm² (SMB-7). The single-tile height is not
    published; it is inferred by halving the 1×2 figure, so treat this number as indicative only.
  - The headline Tiny Tapeout price (tile + ASIC + board) is **not published as a number** anywhere
    we could read: the site's FAQ answers "What is the price?" with "You can use our handy calculator
    to check pricing", and <https://app.tinytapeout.com/calculator> is a client-side application
    that returns no price text to a fetch. Recorded as a blocker in [`search-log.md`](search-log.md).
  - Earlier published figures exist in trade press — `OPEN-5` quotes eeNews on "$150 for 1 tile, the
    ASIC and the demo board" rising to "$300" — but those bundle the chip and board and are in US
    dollars, so they are **not comparable** with the €70 shuttle-inclusion price and should not be
    presented as a price change.

### SMB-11. What a wafer actually costs: CSET's per-node table, derived from TSMC's own financials

- **Source:** Saif M. Khan and Alexander Mann, "AI Chips: What They Are and Why They Matter", Center
  for Security and Emerging Technology, Georgetown University, April 2020, Table 9 "Calculation of
  foundry sale price per chip in 2020 by node", pp. 44–45. doi:10.51593/20190014. PDF:
  <https://cset.georgetown.edu/wp-content/uploads/AI-Chips%E2%80%94What-They-Are-and-Why-They-Matter-1.pdf>
- **Verification:** Verified 2026-09-18. The PDF was downloaded and the text of pages 44 and 45
  extracted and read; the numbers below are line 7 of Table 9 as printed.
- **What it says:**
  - Method, in the authors' words: "Line 7 lists the foundry sale price per wafer, which is the sum
    of capital consumed per wafer (line 5) and other costs and markup per wafer (line 6)."
  - **Line 7, foundry sale price per 300 mm wafer, in 2020 US dollars:**

    | Node (nm) | 90 | 65 | 40 | 28 | 20 | 16/12 | 10 | 7 | 5 |
    |---|---|---|---|---|---|---|---|---|---|
    | Mass production | 2004 Q4 | 2006 Q4 | 2009 Q1 | 2011 Q4 | 2014 Q3 | 2015 Q3 | 2017 Q2 | 2018 Q3 | 2020 Q1 |
    | **$ per wafer** | 1,650 | 1,937 | 2,274 | 2,891 | 3,677 | 3,984 | 5,992 | 9,346 | 16,988 |
    | $ per chip (line 8) | 2,433 | 1,428 | 713 | 453 | 399 | 331 | 274 | 233 | 238 |
- **DERIVED (arithmetic written out):** a 300 mm wafer has a gross area of π × 150² = 70,686 mm².
  - 65 nm: $1,937 ÷ 70,686 mm² = **$0.027 per mm²**.
  - 28 nm: $2,891 ÷ 70,686 mm² = **$0.041 per mm²**.
  - Against SMB-7's Europractice standard price of €12,430/mm² at 28 nm, a small MPW customer pays
    roughly **300,000 times** the silicon's share of a wafer's sale price. Against the GF open-PDK
    180 MCU line at €913/mm², even taking the 90 nm wafer price as an upper bound for a mature node
    ($1,650 ÷ 70,686 = $0.023/mm²), the ratio is about **40,000 times**.
- **Bears on:**
  - **H6 (context, and it is the crucial context).** Essentially none of what a small chip customer
    pays is silicon. It is the amortised mask set, the fixed handling per project, and the
    programme's own overhead. A model that sells machine time at published prices has to attack
    those, not the wafer cost — and if it cannot, "sell it cheaper" does not follow from "silicon is
    cheap".
  - **H1 (context):** shows how steeply wafer price itself rises with node, independent of NRE.
- **Used in:** not yet.
- **Caveats:**
  - These are **modelled** figures, built from TSMC's published financials and a set of stated
    assumptions, not disclosed prices. The authors say so.
  - 2020 vintage. Wafer prices have risen since; a 22% year-on-year rise in TSMC's average wafer
    selling price in 2023 has been reported in trade press but we did not verify it.
  - The ratio derivation compares a *shared* MPW price (where one customer's mm² carries a share of a
    whole mask set and a whole lot) against a *full-wafer* price. It is an illustration of where the
    money goes, not a like-for-like comparison, and should never be quoted as "MPW customers are
    overcharged 300,000×".

### SMB-12. Mask-set cost at mature nodes has collapsed, per the Global Semiconductor Association's survey

- **Source:** Chris Edwards, "Democratising chip design", *New Electronics*, 2021-06-03. The live URL
  returns HTTP 403; read from the Internet Archive:
  <https://web.archive.org/web/20241214200533id_/https://www.newelectronics.co.uk/content/features/democratising-chip-design>
- **Verification:** Verified 2026-09-18 from the archived copy.
- **What it says, verbatim:**
  - "At introduction, a full mask set for the 180nm process could easily cost $300,000 and ran to
    more than half a million dollars for 130nm. Today the picture is quite different. The Global
    Semiconductor Association's industry survey found over the past two years, 180nm mask-set prices
    were no more than $60,000 and often below $80,000 for 130nm sets."
  - "The mask set is far from the only upfront engineering cost. Tools and IP are vital for any
    design, which at the higher end easily run into millions."
- **Bears on:**
  - **H4 and H5 (supports).** If a 130 nm mask set is well under $100,000, then a single small
    customer can in principle afford a dedicated run, not just a share of one — and the economic
    case for sharing masks weakens at mature nodes.
  - **H6 (supports, indirectly).** The fixed cost the fab has to recover per project on a mature node
    is tens of thousands of dollars, not millions, which is the regime in which many small customers
    can each be profitable.
- **Used in:** not yet.
- **Caveats:**
  - The quoted sentence is internally odd — "no more than $60,000 and often below $80,000" — and it
    is reproduced here exactly as printed. It is a journalist's paraphrase of a GSA survey, not the
    survey itself. **The GSA survey itself was not obtained**; see
    [`search-log.md`](search-log.md).
  - "over the past two years" is relative to 2021.
  - Leading-edge mask costs are a different world: figures of "beyond $1M" at 28 nm and "beyond
    $10M" at 7 nm are reported by Dylan Patel in SemiAnalysis, "The Dark Side Of The Semiconductor
    Design Renaissance" (2022-07-24), <https://newsletter.semianalysis.com/p/the-dark-side-of-the-semiconductor>.
    **Status: Partial** — reported to us from a fetch of that page but not read by us line by line,
    and the article attributes the figures to SPIE presentations generally rather than to a specific
    source.

### SMB-13. The commercial foundries do not publish shuttle prices at all

- **Sources** (all checked 2026-09-18):
  - **TSMC CyberShuttle**: <https://www.tsmc.com/english/dedicatedFoundry/services/cyberShuttle>
  - **TSMC via Europractice**: <https://europractice-ic.com/schedules-prices-2025/>
  - **Muse Semiconductor** (the TSMC university shuttle broker):
    <https://www.musesemi.com/shared-block-tapeout-pricing> and `/full-block-tapeout-pricing`
  - **CMC Microsystems** (Canada): <https://www.cmc.ca/en/WhatWeOffer/Make/FabPricing.aspx>
  - **AnySilicon**: <https://anysilicon.com/130nm-wafer-mpw-cost/>
- **Verification:** **Partial.** The TSMC CyberShuttle quote and the Europractice "Price Request
  Form" line were both read directly, on 2026-09-18. The Muse, CMC and AnySilicon results were
  obtained by fetching those URLs and finding no price; we did not open them in a graphical browser,
  and Muse in particular may well publish prices that only render with JavaScript. **We did not
  submit any quote-request form**, which is the only route several of these offer.
- **What it says:**
  - **TSMC CyberShuttle** — no prices. The page says: "If you are a TSMC customer, login to
    TSMC-Online or contact your local TSMC representative for the latest CyberShuttle® schedule."
    **On access:** this URL was reported to us as returning HTTP 403 to automated fetches. It does
    not, as of 2026-09-18: `curl` with a generic User-Agent returns **HTTP 200**, and so does
    `WebFetch`. The sentence is in the delivered page source, though inside an embedded
    JSON blob rather than in the rendered HTML, which is the kind of thing that makes a page look
    empty to a naive reader. No price string appears anywhere in the body. Recorded in
    [`search-log.md`](search-log.md) so the next person does not treat the page as blocked.
  - **TSMC via Europractice** — full MPW prices are not tabulated; only "Prices for TSMC technologies
    can be calculated through the online Price Request Form:" (SMB-7, verified directly).
  - **Muse Semiconductor** — pages titled "…Services and Price" that contain no readable price. The
    site renders client-side, and the archived copies carry no price text either.
  - **CMC Microsystems** — **HTTP 403** to an automated fetch.
  - **AnySilicon** — an article titled "130nm Wafer & MPW Cost Explained" that contains no figures
    and routes the reader to a quote-request form.
- **Bears on:**
  - **H8 (supports).** "Published prices, visible queues and public results" is a real
    differentiator, not a restatement of what the industry already does. The largest foundry in the
    world tells a prospective small customer to log in or call a representative.
  - **H5 (context).** Not publishing a price is itself a barrier to a small customer with an idea and
    no relationship — and it is invisible in any demand statistic, because someone who never asks
    never appears in a count.
- **Used in:** not yet.
- **Caveats:** absence of a price on a fetched page is weak evidence in a world of
  JavaScript-rendered sites. The finding is "we could not find a published price by reading", not
  "no price is published anywhere". A human with a browser could settle Muse and CMC in minutes.
