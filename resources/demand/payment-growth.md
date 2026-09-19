# Payment growth (`PAY`)

Everything else in `resources/demand/` counts **submissions**. A submission is interest. This file
tries to count **money paid**, over time, for the three programmes where a customer genuinely pays
a price that is not subsidised down to nothing: **Tiny Tapeout**, **Efabless chipIgnite** and its
successor **ChipFoundry.io**, and **wafer.space**.

**Read this warning before any number below.** Not one figure in this file is a measured revenue
figure. Nobody in this sector publishes revenue. Every total here is a **derivation**: a published
price list multiplied by a published unit count, with the price regime dated from Internet Archive
captures and the unit counts taken from the operators' own APIs and web pages. Where an input is
unknown — above all, how many customers bought a demonstration board, and how many tiles were
given away — a range is given and the assumption is named. A derivation is not a measurement, and
this file never calls one a measurement.

**Why this matters.** The repository's growth evidence has repeatedly been discounted on the
grounds that a free submission is not a paid order. `OPG-9` is the sharpest form of that objection:
ChipFoundry publishes both `interest` and `committed`, and the gap between them is large.
This file is the attempt to answer that objection with money. **It does not fully answer it.**
The headline result is in §"The revenue table" and §"Growth on revenue against growth on
submissions", and the second of those is the uncomfortable one.

Conflict of interest, stated once and plainly: **wafer.space is the repository owner's own
company.** `PAY-13` and `PAY-14` are our own numbers.

---

## Tiny Tapeout

### PAY-1. Tiny Tapeout's own API publishes, per shuttle, the deadline, the tiles available and the tiles used

- **Source:** `https://app.tinytapeout.com/api/shuttles/submission-stats`, the endpoint Tiny
  Tapeout's own published statistics tool reads
  (<https://github.com/TinyTapeout/tt-shuttle-stats>, whose README says: "Parses data from
  https://app.tinytapeout.com/api/shuttles/submission-stats to show the number of projects submitted
  and tile utilisation over time for the most recent Tiny Tapeout shuttles"). The graphs it produces
  are embedded on <https://tinytapeout.com/chips/>.
- **Verification:** **Verified 2026-09-19.** Fetched with `curl` and a browser `User-Agent` and the
  JSON parsed. 620 kB, 28 shuttles, 4,327 submission records.
- **How it was counted** (reproducible):
  `curl -sfL --compressed -A "<browser UA>" https://app.tinytapeout.com/api/shuttles/submission-stats`,
  then read `shuttles[]` (`slug`, `name`, `deadline`, `tiles_total`, `tiles_used`,
  `tiles_reserved`) and `submissions[]` (`shuttle_id`, `project_id`, `top_module`, `tile_count`,
  `first_submission_time`). Shuttles before TT04 are not in this API; their tile counts come from
  `https://index.tinytapeout.com/<id>.json` instead, summing each project's `tiles` field
  ("1x1" → 1, "2x2" → 4, and so on). **A browser `User-Agent` is required on `index.tinytapeout.com`
  or the request gets HTTP 403.**
- **What it says**, in deadline order (the four shuttles still open in December 2026 carry a
  placeholder `tiles_used` of 2 and are omitted):

  | Shuttle | Deadline | tiles_total | tiles_used | submissions |
  |---|---|---:|---:|---:|
  | tt04 | 2023-09-08 | 350 | 227 | 143 |
  | tt05 | 2023-11-04 | 380 | 283 | 174 |
  | tt06 | 2024-04-19 | 512 | **512** | 238 |
  | tt07 | 2024-06-01 | 512 | 301 | 119 |
  | tt08 | 2024-09-06 | 512 | 236 | 135 |
  | ttihp0p2 | 2024-11-04 | 240 | 240 | 95 |
  | tt09 | 2024-11-10 | 512 | 480 | 369 |
  | **tt10** | 2025-03-12 | 512 | 240 | 112 |
  | ttihp25a | 2025-03-12 | 560 | 560 | 546 |
  | ttihp0p3 | 2025-05-19 | 32 | 31 | 23 |
  | ttcad25a | 2025-06-10 | 512 | 483 | 257 |
  | ttihp25b | 2025-09-01 | 240 | 176 | 81 |
  | ttsky25a | 2025-09-15 | 512 | 505 | 237 |
  | ttsky25b | 2025-11-10 | 512 | 506 | 316 |
  | ttgf0p2 | 2025-11-24 | 160 | 160 | 52 |
  | ttihp26a | 2026-03-23 | 560 | 540 | 283 |
  | ttihp0p4 | 2026-03-28 | 240 | 138 | 40 |
  | ttsky26a | 2026-05-11 | 512 | **512** | 289 |
  | ttsky26b | 2026-05-18 | 512 | **512** | 273 |
  | ttgf26b | 2026-06-22 | 160 | 155 | 90 |
  | ttgf26a | 2026-06-22 | 160 | **160** | 95 |
  | ttgf0p3 | 2026-07-03 | 160 | 115 | 32 |
  | ttsky26c | 2026-09-07 | 512 | 510 | 242 |
  | ttihp26b | 2026-09-21 | 240 | 164 | 86 |

  Pre-TT04 tiles, from the shuttle indexes: tt01 152 tiles / 152 projects, tt02 166 / 166,
  tt03 249 / 249, tt03p5 29 / 29, ttihp0p1 61 / 24, ttgf0p1 63 / 24.
- **DERIVED:** `tiles_used` summed over the 24 closed shuttles in the API is **7,746**; adding the
  six pre-TT04 and off-API runs (152 + 166 + 249 + 29 + 61 + 63 = 720) gives **8,466 tiles ever
  placed on a Tiny Tapeout die**. This **checks the repository's existing "7,728 tiles" figure**
  in `data-cuts-and-statistics.md` §5.3: that figure was the same `tiles_used` field read on
  2026-09-18 and it is right for the shuttles it covers; it omits the pre-TT04 runs and one further
  shuttle has closed since.
- **Bears on:**
  - **H5 (context).** This is the unit base for every Tiny Tapeout revenue figure in this file. It
    is the operator's own count of *tiles allocated*, which is much closer to a billable quantity
    than a count of designs.
  - **H6 (context).** `tiles_used` reaches `tiles_total` exactly on six shuttles (tt06, ttihp0p2,
    ttihp25a, ttsky26a, ttsky26b, ttgf26a, ttgf0p2). Those are sell-outs. It falls well short on
    others — tt04 at 227/350, tt08 at 236/512, tt10 at 240/512.
- **Used in:** the derivation in `PAY-6`.
- **Caveats:**
  - **`tiles_used` is not the same as tiles paid for.** For TT04 the operator's own news post says
    "350 tiles total, 235 allocated and paid for" while the API says 227 used. The difference is
    tiles that were bought and then not filled. So the API slightly **under**-counts paid tiles.
  - The API starts at TT04. TT01–TT03 are reconstructed from the shuttle index, which counts what
    reached the die, not what was ordered.
  - `tt10` is in the API with 240 tiles and 112 submissions **and was cancelled** (`PAY-5`).
  - A large share of the tiles on some shuttles are re-runs of existing designs, not new orders;
    `data-cuts-and-statistics.md` §3.2 measures this and `PAY-5` uses it.

### PAY-2. Tiny Tapeout's published price, dated from the Internet Archive, from free in 2022 to a €70 tile plus a €300 board in 2026

- **Sources:** Internet Archive captures of `https://tinytapeout.com/` and `/faq/`. The captures
  quoted below, all fetched in the raw (`id_`) form:
  - <https://web.archive.org/web/20220901123539id_/http://tinytapeout.com/>
  - <https://web.archive.org/web/20221105134738id_/https://tinytapeout.com/>
  - <https://web.archive.org/web/20230305162858id_/https://tinytapeout.com/>
  - <https://web.archive.org/web/20230810110102id_/https://tinytapeout.com/>
  - <https://web.archive.org/web/20231004002753id_/https://www.tinytapeout.com/>
  - <https://web.archive.org/web/20240208041441id_/https://tinytapeout.com/>
  - <https://web.archive.org/web/20240302202057id_/https://tinytapeout.com/>
  - <https://web.archive.org/web/20241013102124id_/https://tinytapeout.com/faq/>
  - <https://web.archive.org/web/20241202145413id_/https://tinytapeout.com/>
  - <https://web.archive.org/web/20250403052837id_/https://tinytapeout.com/>
  - <https://web.archive.org/web/20250516165910id_/https://tinytapeout.com/>
  - <https://web.archive.org/web/20250703111652id_/https://tinytapeout.com/>
  - <https://web.archive.org/web/20250803141608id_/https://tinytapeout.com/>
  - <https://web.archive.org/web/20260909121226id_/https://www.tinytapeout.com/>
- **Verification:** **Verified 2026-09-19.** Twenty-four captures of the home page and nineteen of
  the FAQ were fetched with `curl --compressed` and a browser `User-Agent`, stripped of tags, and
  every currency amount extracted and read in date order. (`curl` without `--compressed` returns a
  gzip stream that looks like text and silently produces mojibake; several captures had to be
  refetched for this reason.)
- **What it says**, verbatim, in date order:

  | Capture | What the page printed |
  |---|---|
  | 2022-09-01 | **No price anywhere on the page.** "TinyTapeout is an educational project that aims to make it easier and cheaper than ever to get your digital designs manufactured on a real chip! … If you submit a design then there's a good chance we'll get it made and in your hands! … your design ready to be manufactured on the next Efabless shuttle run on the 1st of September." |
  | 2022-11-05 | "We will have: **190 ASIC + PCB packages at $100 + P&P** **250 Design only packages at $25**" and, in the order form, "Design slot + Physical PCB with the chip ($100)" / "Design slot only ($25)" |
  | 2023-03-05 | "**Design + Physical PCB + ASIC = $100 + p&p**" / "**Design only = $25**" |
  | 2023-08-10, 2023-09-23, 2023-10-04 | "**Design (single tile) + Physical PCB + ASIC = $100 + shipping**" / "**Design only (single tile): $50**" / "**Extra tiles = $50 each**" |
  | 2024-02-08 | "160 x 100 um tile + ASIC + demonstration board: **$150 + shipping with earlybird Efabless discount, $300 without.** Each extra tile: $50" |
  | 2024-03-02 → 2024-12-02 | "The standard price is **$300** plus shipping. However, **Efabless is sponsoring a special early bird offer of $150** (plus shipping), **limited to one order per person.** Each extra tile is $50, and extra analog pins start from $40 per pin." |
  | 2024-10-13 (FAQ) | "**The first 80 orders from individuals are sponsored by Efabless**, so you get 1 tile, 1 ASIC mounted on 1 demo board PCB for $150 + postage. After those first 80 are gone, the price goes up to $300." and "If you want more chips you have to order more of the PCBs at **$250 each** — the early bird price is only available once per person." |
  | 2025-04-03 | "The standard price is **$300** plus shipping. Each extra tile is $50, and extra analog pins start from $40 per pin." **The Efabless sponsorship sentence is gone** (Efabless shut down on 2025-03-01). |
  | 2025-05-16, 2025-07-03 | "200 x 150 um tile + ASIC + demonstration board: **The price for the current open source IHP shuttle is 150 € plus shipping. Each extra tile is 50 €.**" |
  | 2025-08-03 onward | **No price on the page at all.** "Pricing depends on the size of your design, the shuttle you use and whether its analog or digital. Use the calculator to check current prices. **Early bird prices are currently reserved for projects affected by the Efabless shutdown.**" |
  | 2026-09-09 | Still no price. "Early bird prices offer an opportunity for you to tapeout at a lower cost. **Early bird prices are limited per shuttle, and are only available to individuals.**" |

- **Bears on:**
  - **H5 and H8 (supports, on price).** The bundled price of a tile, a packaged chip and a
    demonstration board went $0 (TT01) → $100 (2022–2023) → $300 standard with a $150 sponsored
    tier (2024) → €150 (mid-2025) → €370 standard / €170 early-bird (2026, `PAY-3`). The **cheapest
    available route never rose above $150/€185** in four years.
  - **H5 (challenges).** The *standard* price rose from $100 to €370, a 3.4× rise at constant
    bundle, across exactly the period the repository reads as demand growth. Any "demand appears
    when the price falls" reading of Tiny Tapeout has to survive the fact that its list price rose.
  - **This tightens `OPG-14`.** `OPG-14` established that Efabless sponsored a capped tier rather
    than the whole price. `PAY-2` adds the dates, the cap size ("the first 80 orders from
    individuals"), the extra-board price ($250), and the fact that **from August 2025 Tiny Tapeout
    stopped printing any price on its website at all**, which is a real reduction in price
    transparency by the programme the repository holds up as the transparent one.
- **Used in:** the price regimes in `PAY-6`.
- **Caveats:**
  - Archive captures are point samples, roughly monthly. A change could fall up to a month before
    the capture that first shows it.
  - The 2022-11-05 page also contains the strings "Sorry, we are sold out!" and "available" next to
    both packages. These are **template elements shown conditionally by JavaScript**, not a
    statement of state at capture time, and must not be quoted as evidence that TT02 sold out.
  - The dollar prices are for a 160×100 µm SKY130 tile and the euro prices for a 200×150 µm IHP
    tile. **These are not the same good** and the sequence is not a like-for-like price series;
    `OPG-14` makes the same point.
  - No capture gives the exchange rate used, and Tiny Tapeout has billed in euros since 2025.

### PAY-3. The live price schedule, read straight out of Tiny Tapeout's own order application

- **Source:** the JavaScript module that computes every Tiny Tapeout invoice,
  <https://app.tinytapeout.com/_build/assets/invoice-BwELwELl.js>, referenced by
  <https://app.tinytapeout.com/calculator>.
- **Verification:** **Verified 2026-09-19.** Fetched with `curl` and read. This is the first time
  the repository has been able to read Tiny Tapeout's current prices at all: `SMB-10`'s caveat
  records that "The headline Tiny Tapeout price (tile + ASIC + board) is **not published as a
  number** anywhere we could read" because the calculator is client-side. **It is published — in
  the calculator's own source.**
- **How it was found** (reproducible): fetch `https://app.tinytapeout.com/calculator`, list the
  `/_build/assets/*.js` modules it preloads, and fetch `invoice-*.js`. It is 2 kB and contains the
  whole schedule as literals.
- **What it says**, verbatim from the module:

  ```js
  m={pcb:300,pcbDiscount:100,tile:70,analogPin:100,discountedAnalogPins:2,
     analogPinDiscount:40,shipping:15,currency:"EUR",chipsOnLoan:!1,maxAnalogPins:0},   // chipfoundry
  y={pcb:300,pcbDiscount:100,tile:70,analogPin:200,analogPinDiscount:40,
     discountedAnalogPins:0,shipping:15,currency:"EUR",chipsOnLoan:!1,maxAnalogPins:16},// ihp
  f={pcb:300,pcbDiscount:100,tile:70,analogPin:0,discountedAnalogPins:0,
     analogPinDiscount:0,shipping:15,currency:"EUR",chipsOnLoan:!1,maxAnalogPins:0},    // gf180
  C={ihp:y,chipfoundry:m,gf180:f}
  ```

  and the line labels it builds: `"DevKits (PCBs)"` / `"Tiny Tapeout DevKit PCBs"` /
  `"ASIC + carrier board + demo board"`, `"Tile Cost"` / `"Space for your design on the chip"`,
  `"Analog pins"`, and `"Worldwide Economy Shipping"`.
- **DERIVED (arithmetic written out), all in euros:**
  - One tile + one DevKit, standard: 70 + 300 = **€370**, plus €15 shipping = **€385**.
  - One tile + one DevKit at the early-bird PCB price: 70 + 100 = **€170**, plus €15 = **€185**.
    **This reproduces exactly the figure Tiny Tapeout published on 2025-10-01** — "thanks to
    ChipFoundry you can tape out a single-tile digital design and receive your own ASIC for just
    €185 including shipping" — which dates this schedule to **on or before 2025-10-01**.
  - The `pcbDiscount` is the sponsorship. It is worth **€200 per board**, 54% of the standard
    bundle (200 ÷ 370 = 0.5405).
  - Analog is charged per *customer*, not per project, and IHP analog pins are 2× ChipFoundry's
    (€200 against €100), with the first-two-pin discount switched off on IHP
    (`discountedAnalogPins:0`).
- **Bears on:**
  - **H6 (supports).** A complete, machine-readable, published price list with no quote, no login
    and no negotiation, differentiated by process. It is exactly the object `PRINCIPLES.md` argues
    a fab should publish.
  - **H6 (challenges).** The *headline* is no longer published in human-readable form on the
    website (`PAY-2`). A price you can only obtain by reading a bundled JavaScript module, or by
    starting an order, is published in a weak sense.
  - **`SMB-10` should be updated:** its caveat that the bundled price cannot be read is now wrong,
    and its €3,900/mm² derivation can be redone against the €70 tile and the real tile geometry.
- **Used in:** the P6 price regime in `PAY-6`.
- **Caveats:**
  - A minified bundle read on one day. The file name carries a content hash, so a price change
    produces a new file name; this snapshot is 2026-09-19.
  - It is the *default* schedule. Coupons exist (`applyCoupon`), prepaid credits are offered to
    universities, and `chipsOnLoan` and `subsidizedPCBs` are per-shuttle flags the module reads
    from elsewhere. **Actual billed prices are lower than this list for an unknown share of orders.**
  - The public teaching page <https://tinytapeout.com/teaching/> prices "Up to 5 Projects, 1 PCB
    kits" at €565, "25 Projects, 3 PCB kits" at €2,195 and "75 Projects, 5 PCB kits" at €5,325.
    **DERIVED:** solving the three simultaneously gives €50 per tile and €315 per PCB kit
    (5a + b = 565 and 25a + 3b = 2195 give a = 50, b = 315; 75 × 50 + 5 × 315 = 5,325 ✓). €315 is
    €300 + €15 shipping. **So that page is running on a superseded €50 tile price** and the two
    published schedules disagree. Both are recorded; neither is treated as authoritative for a
    specific shuttle.

### PAY-4. The only two shuttles where Tiny Tapeout published how many units were actually paid for

- **Sources:** Tiny Tapeout's own news posts, from the site's public source repository
  <https://github.com/TinyTapeout/tinytapeout_www> (`content/news/…/_index.en.md`), and live at
  <https://tinytapeout.com/news/>:
  - "TT04 submissions are closed", dated 2023-09-09
  - "TT06 sells out. TT07 open!", dated 2024-04-20
- **Verification:** **Verified 2026-09-19**, repository cloned and both files read.
- **What it says**, verbatim:
  - TT04: "The final numbers: **350 tiles total, 235 allocated and paid for, with 115 still
    available. 98 PCBs were allocated, 97 paid.** In total, 143 projects were submitted from over
    30 countries".
  - TT06: "We sold all the tiles on TT06 — 238 projects submitted from 30 countries. … **We sold
    100% of the Efabless-sponsored PCBs, plus another 60 at full price.**"
- **DERIVED (arithmetic written out):**
  - **TT04 revenue, and this one needs no assumption at all.** The price in force (`PAY-2`,
    captures 2023-08-10 and 2023-10-04) was $100 for a bundle of one tile + ASIC + PCB, $50 for a
    design-only tile and $50 for each extra tile. 97 bundles × $100 = $9,700. The remaining paid
    tiles, 235 − 97 = 138, at $50 = $6,900. **Total $16,600**, excluding shipping and analog pins
    (there were none on TT04). **This is the single most reliable revenue figure in this file.**
  - **TT06.** The sponsored tier was the first 80 orders from individuals (`PAY-2`, FAQ), so
    "100% of the Efabless-sponsored PCBs" is 80 boards at $150 and "another 60 at full price" is 60
    at $300. 80 × 150 = $12,000; 60 × 300 = $18,000; 140 bundles consume 140 of the 512 tiles, and
    512 − 140 = 372 tiles at $50 = $18,600. **Total $48,600**, again excluding shipping and analog.
  - **PCB attach rate**, the one quantity everything else in `PAY-6` needs: 97 ÷ 143 = **0.678** on
    TT04 and 140 ÷ 238 = **0.588** on TT06. Per tile it is 97 ÷ 235 = 0.413 and 140 ÷ 512 = 0.273.
    **Per design is the stabler of the two**, and 0.60 is used as the central assumption with a
    0.50–0.70 range.
- **Bears on:**
  - **H6 (challenges, hard).** **Tiny Tapeout's best-documented shuttle earned $16,600.** TT04 ran
    for ten weeks, drew 143 projects from over 30 countries, and sold $16,600 of tiles and boards.
    Its slot on the Efabless CI-2309 shuttle cost, at the chipIgnite list price of the day,
    $9,750 (`SMB-9`). That leaves about $6,850 before PCBs, packaging, shipping, fulfilment or
    anybody's time, on a shuttle that took a quarter of a year.
  - **H5 (supports, weakly).** TT06 is roughly 2.9× TT04 six months later (48,600 ÷ 16,600 = 2.93).
  - **H6 (context).** Only 41% of TT04's paid tiles and 27% of TT06's came with a board. **Most
    Tiny Tapeout customers do not buy the physical product**, which is where most of the price is.
- **Used in:** the anchor for `PAY-6`.
- **Caveats:**
  - Two shuttles out of twenty-eight. Every other shuttle's paid-unit count is inferred.
  - "98 PCBs were allocated, 97 paid" is the only place in the whole record where an open-silicon
    programme distinguishes allocated from paid. One of 98 did not pay.
  - The TT06 split assumes the sponsored tier was still 80 boards in April 2024; the FAQ capture
    that says "the first 80" is from October 2024, and `OPEN-5` quotes eeNews saying "the first 100"
    for TT06. If it was 100, TT06 is 100 × 150 + 40 × 300 + 372 × 50 = **$45,600**, $3,000 lower.

### PAY-5. What is not revenue: bring-up runs, port runs, sponsors, free tiles, and one cancelled shuttle

- **Sources:**
  - Shuttle-by-shuttle table at <https://tinytapeout.com/chips/> (site repo, `content/chips/_index.md`)
  - News posts "Efabless shuts down - Tiny Tapeout will continue" (2025-03-01), "TT08 is open!"
    (2024-08-09), "TTSKY26a sold out — TTSKY26b opens" (2026-04-26), "TTSKY25a submitted"
    (2025-10-01), "TTIHP26a wrap up!" (2026-03-26), "2025 Year in Review" (2026-01-08),
    "TTGF26a opens" (2026-04-23)
  - Re-run shares per shuttle: `data-cuts-and-statistics.md` §3.2
- **Verification:** **Verified 2026-09-19** for the site pages; **Partial** for the re-run shares,
  which are taken from the repository's own earlier analysis rather than recomputed here.
- **What it says:**
  - **The chip table names, for every run, which commercial shuttle Tiny Tapeout bought space on.**
    TT02 → CI-2211Q, TT03 → CI-2304C, TT04 → CI-2309, TT05 → CI-2311, TT06 → CI-2404,
    TT07 → CI-2406, TT08 → CI-2409, TT09 → CI-2411, TT01 → MPW7 (the free Google shuttle),
    TTIHP25a/0p2 → IHP-2504, TTIHP25b → IHP-2509, TTIHP26a/0p4 → IHP-2603, TTIHP26b → IHP-2609,
    TTSKY25a → CI-2509, TTSKY25b → CI-2511, TTSKY26a/b → CI-2605, TTSKY26c → CI-2609,
    TTGF0p2 → **WS-2512**, TTGF26a/26b/0p3 → **WS-2606**. **`WS-` is wafer.space**, so Tiny
    Tapeout's GF180 runs are wafer.space orders and Tiny Tapeout's SKY130 runs are chipIgnite /
    ChipFoundry orders. **Tiny Tapeout's revenue is gross, and a large part of it is another
    programme's revenue.**
  - **TT01 was free.** The 2022-09-01 capture carries no price (`PAY-2`), and the launch post says
    "Tiny Tapeout's very first chip submitted to the free Google MPW7 shuttle". 152 tiles, no money.
  - **TT10 was cancelled.** The chip table's row reads "TT10 | 2024-11-11 | Cancelled". The
    2025-03-01 post says "Current TT10 shuttle and future SkyWater Sky130 shuttles are paused" and
    "We are prepared to offer a refund to all affected customers if we aren't able to ship those
    chips." 240 tiles and 112 submissions were in it. From 2025-08 the website said "Early bird
    prices are currently reserved for projects affected by the Efabless shutdown", i.e. the money
    was made good in kind. **TT10 is counted as zero net revenue in `PAY-6`.**
  - **Nine runs are process bring-up or port runs, not sales:** tt03p5, ttihp0p1, ttihp0p2,
    ttihp0p3, ttihp0p4, ttgf0p1, ttgf0p2, ttgf0p3, and the Cadence-sponsored mass port ttcad25a.
    Their re-run shares are 73%, 39%, 83%, 69%, 56% and 92% respectively
    (`data-cuts-and-statistics.md` §3.2). **1,097 tiles sit in these runs.**
  - **ttihp25a is the make-good for Efabless.** 560 tiles, 546 submissions, **433 of 564 records
    re-runs (77%)**: it is the shuttle on which Tiny Tapeout re-taped the SKY130 back-catalogue and
    the stranded TT10 designs onto IHP. Only the 131 first-time designs are treated as sold.
  - **Every recent shuttle names a sponsor.** ChipFoundry sponsored TTSKY25a and TTSKY25b; SwissChips
    sponsored TTIHP26a; Tillitis and Wit funded the GF180MCU port; Synopsys sponsors workshops; and
    **"This shuttle is supported by the IEEE. Half the area and PCBs have been reserved for them,
    but there's still plenty of space… 40 non-subsidized PCBs are available for anyone to submit
    designs"** (TTSKY26b, 2026-04-26).
  - **Free tiles are given away.** TT08: "The demoscene competition is running alongside TT08. This
    is an opportunity for a free tapeout! **All entrants get 1 free tile.**"
- **Bears on:**
  - **H5 and H6 (challenges, and this is the most important paragraph in this file).** On the
    2026-04-26 statement, **half of TTSKY26b's area and half its boards were an IEEE block
    booking**, and only 40 boards were available at a non-subsidised price. Tiny Tapeout's tile
    count is therefore **not** a count of small buyers paying a market price: an unknown but large
    share of it is sponsorship, institutional block bookings, competition prizes and re-ports.
    `OPG-11` found the same shape at IHP — two customers holding 71% of a run.
  - **H6 (context).** The programme buys its slots from chipIgnite/ChipFoundry, IHP and wafer.space
    at $9,750–$14,950 a slot (`SMB-9`). Its revenue is gross and its margin is unpublished.
- **Used in:** the exclusions in `PAY-6`.
- **Caveats:**
  - **The split between sponsored and sold tiles is not published for any shuttle**, so `PAY-6`
    cannot net sponsorship out. It nets out only the runs that are wholly bring-up or port runs.
    Every Tiny Tapeout figure in this file is therefore an **over-estimate of money from ordinary
    customers**, and possibly a large one.
  - Treating ttihp25a's 433 re-runs as free is our inference from the refund/roll-over statement,
    not something Tiny Tapeout says.
  - "Sponsored" does not always mean the sponsor paid cash to Tiny Tapeout. It may mean the fab
    donated the slot. Either way it is not a small customer's money.

### PAY-6. DERIVED: Tiny Tapeout's revenue, per shuttle and per year, 2022–2026

- **Sources:** `PAY-1` (tiles and designs), `PAY-2` and `PAY-3` (dated price regimes), `PAY-4`
  (the PCB attach rate and the two exact shuttles), `PAY-5` (the exclusions).
- **Verification:** **DERIVED, not measured.** Every input is Verified; the combination is
  arithmetic performed here on 2026-09-19.
- **How it was computed** (reproducible). A price regime is assigned to each shuttle by its closing
  date from the table in `PAY-2`:

  | Regime | In force | Bundle (tile + ASIC + board) | Cheapest bundle | Extra tile |
  |---|---|---|---|---|
  | P1 | 2022-11 → 2023-05 | $100 | $100 | $25 |
  | P2 | 2023-07 → 2023-12 | $100 | $100 | $50 |
  | P3 | 2024-01 → 2025-03 | $300 | $150 (Efabless) | $50 |
  | P4 | 2025-03 → 2025-05 | $300 | $300 | $50 |
  | P5 | 2025-05 → ~2025-09 | €150 | €150 | €50 |
  | P6 | ~2025-09 → now | €370 | €170 | €70 |

  Then, per shuttle: `bundles = attach × designs` (capped at tiles), and
  `revenue = bundles × bundle_price + (tiles − bundles) × tile_price`.
  **LOW** = attach 0.50 and every bundle at the cheapest price. **MID** = attach 0.60 and bundles
  split half cheap, half standard. **HIGH** = attach 0.70 and every bundle at the standard price.
  Shipping and analog-pin charges are excluded throughout (both would raise the figures).
- **What it gives:**

  | Shuttle | Closed | Tiles counted as sold | Designs | Regime | LOW | MID | HIGH |
  |---|---|---:|---:|---|---:|---:|---:|
  | tt01 | 2022-09-01 | 0 (free MPW-7) | 152 | — | 0 | 0 | 0 |
  | tt02 | 2022-12-02 | 166 | 166 | P1 | $10,375 | $11,650 | $12,850 |
  | tt03 | 2023-04-23 | 100 | 100 | P1 | $6,250 | $7,000 | $7,750 |
  | tt03p5 | 2023-06-13 | 0 (bring-up) | 29 | — | 0 | 0 | 0 |
  | **tt04** | 2023-09-08 | **235** | 143 | P2 | $15,350 | $16,050 | $16,750 |
  | tt05 | 2023-11-04 | 283 | 174 | P2 | $18,500 | $19,350 | $20,250 |
  | **tt06** | 2024-04-19 | **512** | 238 | P3 | $37,500 | $50,625 | $67,350 |
  | tt07 | 2024-06-01 | 301 | 120 | P3 | $21,050 | $27,650 | $36,050 |
  | ttihp0p1 | 2024 | 0 (bring-up) | 24 | — | 0 | 0 | 0 |
  | tt08 | 2024-09-06 | 236 | 135 | P3 | $18,600 | $25,975 | $35,300 |
  | ttihp0p2 | 2024-11-04 | 0 (bring-up) | 95 | — | 0 | 0 | 0 |
  | tt09 | 2024-11-10 | 480 | 369 | P3 | $42,400 | $62,675 | $88,500 |
  | *tt10* | *cancelled* | *240* | *112* | *P3* | *$17,600* | *$23,725* | *$31,500* |
  | ttihp25a | 2025-03-28 | 127 (first-time only) | 564 | P4 | $38,100 | $38,100 | $38,100 |
  | ttihp0p3 | 2025-05-19 | 0 (bring-up) | 23 | — | 0 | 0 | 0 |
  | ttcad25a | 2025-06-10 | 38 (first-time only) | 257 | P5 | €5,700 | €5,700 | €5,700 |
  | ttihp25b | 2025-09-01 | 176 | 81 | P5 | €12,800 | €13,700 | €14,500 |
  | ttsky25a | 2025-09-15 | 505 | 237 | P6 | €47,150 | €63,750 | €85,150 |
  | ttsky25b | 2025-11-10 | 506 | 316 | P6 | €51,220 | €73,420 | €101,720 |
  | ttgf0p2 | 2025-11-24 | 0 (bring-up) | 52 | — | 0 | 0 | 0 |
  | ttihp26a | 2026-03-23 | 540 | 283 | P6 | €52,000 | €71,800 | €97,200 |
  | ttihp0p4 | 2026-03-28 | 0 (bring-up) | 40 | — | 0 | 0 | 0 |
  | ttsky26a | 2026-05-11 | 512 | 289 | P6 | €50,240 | €70,440 | €96,440 |
  | ttsky26b | 2026-05-18 | 512 | 273 | P6 | €49,440 | €68,640 | €93,140 |
  | ttgf26a | 2026-06-22 | 160 | 95 | P6 | €16,000 | €22,600 | €31,000 |
  | ttgf26b | 2026-06-22 | 155 | 90 | P6 | €15,350 | €21,650 | €29,750 |
  | ttgf0p3 | 2026-07-03 | 0 (bring-up) | 32 | — | 0 | 0 | 0 |
  | ttsky26c | 2026-09-07 | 510 | 242 | P6 | €47,800 | €64,700 | €86,400 |
  | ttihp26b | 2026-09-21 | 164 (still open) | 86 | P6 | €15,780 | €21,880 | €29,480 |

  **The method checks out against the two shuttles where the answer is known** (`PAY-4`). TT04's
  published figures give exactly **$16,600**; the model's MID is $16,050, **3.3% low**. TT06's give
  **$48,600**; the model's MID is $50,625, **4.2% high**. That is the only calibration available and
  it is a good one — but it is two points, both from the dollar era.

  **Per calendar year of the closing date, TT10 excluded. "Designs" counts only designs on
  revenue-bearing shuttles, so the free bring-up and port runs are not in it:**

  | Year | Tiles counted as sold | Designs | LOW | MID | HIGH |
  |---|---:|---:|---:|---:|---:|
  | 2022 | 166 | 166 | $10,375 | $11,650 | $12,850 |
  | 2023 | 618 | 417 | $40,100 | $42,400 | $44,750 |
  | 2024 | 1,529 | 862 | $119,550 | $166,925 | $227,200 |
  | 2025 | 1,352 | 1,455 | $38,100 + €116,870 | $38,100 + €156,570 | $38,100 + €207,070 |
  | 2026 (to 2026-09-21) | 2,553 | 1,358 | €246,610 | €341,710 | €463,410 |
  | **Lifetime** | **6,218** | **4,258** | **≈$572k** | **≈$757k** | **≈$993k** |

  The lifetime line adds dollars and euros as if they were the same unit; at the ECB reference rate
  used in `SMB-9` (EUR 1 = USD 1.1481) the euro part is about 15% larger in dollars, so the
  dollar-equivalent lifetime range is roughly **$0.63m – $1.11m**, central **$0.85m**.

  **A hard floor, for anyone who rejects the attach-rate assumption entirely:** 6,218 tiles, each
  at the extra-tile price of its own regime and no boards sold at all, is **$/€375,530**.
- **Bears on:**
  - **H5 (supports).** The revenue series rises every year: roughly $10k → $40k → $167k → $195k →
    €342k (nine months). **DERIVED growth on the MID series:** 2022→2023 ×3.64 (42,400 ÷ 11,650),
    2023→2024 ×3.94 (166,925 ÷ 42,400), 2024→2025 ×1.17 (194,670 ÷ 166,925), 2025→2026 ×1.76 on
    nine months of 2026 (341,710 ÷ 194,670). Over the three steps 2022→2025 the CAGR is
    (194,670 ÷ 11,650)^(1/3) − 1 = **+156%/yr**.
  - **H6 (challenges, and this is the finding).** **The whole programme, over five years, has taken
    in under a million dollars.** The best single year is 2026 at roughly €342k for nine months.
    That is one salary and a bit, gross, before the cost of the shuttle slots it buys, the boards,
    the packaging and the shipping. `data-cuts-and-statistics.md` §5.3 reached €0.54m–$2.3m by a
    cruder route; this derivation lands in the same place and narrows it.
  - **H6 (challenges).** **DERIVED, revenue per design on the MID series:** 2022 $70 (11,650 ÷ 166),
    2023 $102 (42,400 ÷ 417), 2024 $194 (166,925 ÷ 862), 2025 $134 (194,670 ÷ 1,455), 2026 €252
    (341,710 ÷ 1,358). **Revenue per tile:** 2022 $70, 2023 $69 (42,400 ÷ 618), 2024 $109
    (166,925 ÷ 1,529), 2025 $144 (194,670 ÷ 1,352), 2026 €134 (341,710 ÷ 2,553). Both roughly
    double across the period, which is the healthiest thing in the series — but the absolute level,
    **a design worth about €130–€250**, leaves no room at all for a sales motion, a support call or
    any customer acquisition beyond word of mouth. That is the same conclusion
    `data-cuts-and-statistics.md` §5.3 reached from lifetime value, now reached from revenue.
- **Used in:** the revenue table and growth comparison at the foot of this file.
- **Caveats — read all of these before quoting any figure above:**
  - **This is a derivation, not a measurement.** No Tiny Tapeout revenue figure has ever been
    published.
  - **The attach rate is the single biggest lever** and it is calibrated on two shuttles out of
    twenty-eight, both from 2023–2024, both under a dollar price list. The 2026 euro shuttles may
    have a completely different attach rate.
  - **The sponsorship problem (`PAY-5`) is not netted out and pushes every figure down, not up.**
    If half of TTSKY26b's tiles and boards were an IEEE block booking rather than individual sales,
    the *money* may still be real but the *customer count* is not, and if the IEEE block was
    donated rather than sold the money is not real either. **We do not know which.**
  - The 2026 row stops at 2026-09-21 and ttihp26b was still open, so 2026 is a partial year and a
    floor.
  - Dollar and euro figures are not converted except where stated.
  - `tiles_used` under-counts paid tiles (`PAY-1` caveat), pushing the figures down.
  - Shipping and analog-pin charges are excluded, pushing the figures down.
  - **Everything here is gross revenue.** Tiny Tapeout buys its wafer space from the very
    programmes in the rest of this file, at $9,750–$14,950 a slot, and pays for boards, packaging
    and shipping out of these numbers. Nothing here is margin, and nothing here says the programme
    is profitable or that it is not.
