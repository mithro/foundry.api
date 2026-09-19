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
company.** `PAY-9` is our own numbers, and `PAY-5` shows that Tiny Tapeout buys from it.

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

---

## Efabless chipIgnite and ChipFoundry.io

### PAY-7. chipIgnite's price never changed: $9,750 from May 2021 to the day the company died

- **Sources:** Internet Archive captures of Efabless's own chipIgnite pages, fetched in raw (`id_`)
  form where available and in rendered form where not:
  - <https://web.archive.org/web/20210520000214/https://efabless.com/chipignite/2106q> (2021-05-20)
  - <https://web.archive.org/web/20211219031133/https://efabless.com/chipignite/2110C> (2021-12-19)
  - <https://web.archive.org/web/20220202204841/https://efabless.com/chipignite/2204C> (2022-02-02)
  - <https://web.archive.org/web/20240521021124id_/https://efabless.com/chipignite> (2024-05-21)
  - <https://web.archive.org/web/20241216140400id_/https://efabless.com/chipignite> (2024-12-16)
  - <https://web.archive.org/web/20250901050905id_/https://efabless.com/chipignite> (2025-09-01)
  - <https://web.archive.org/web/20250829062705id_/https://efabless.com/chipignite-mini> (2025-08-29)
  - <https://web.archive.org/web/20250826233607id_/https://efabless.com/chipignite-ml> (2025-08-26)
  - <https://web.archive.org/web/20250302002325id_/https://efabless.com/chipignite-university-program> (2025-03-02)

  and, for the successor, <https://chipfoundry.io/chipignite> and <https://chipfoundry.io/faqs>.
- **Verification:** **Verified 2026-09-19.** Nineteen archived Efabless pages and both live
  ChipFoundry pages were fetched with `curl --compressed` and read.
- **What it says**, verbatim, in date order:
  - **2021-05-20** (the launch page, four weeks before the first tapeout): "Two pricing options:
    **$9,750 for 100 QFN or 300 WCSP parts** / 1000 parts for $20 each", "Private shuttle -- no
    open-source requirement", "Make a reservation with a **$200 deposit**", "**$200 reservation fee
    (fully refundable if minimum projects not met)**", "Note: Schedule depends on meeting minimum
    project capacity". The identical wording is on every capture through **2022-02-02**.
  - **2024-05-21, 2024-12-16, 2025-09-01** (the site stayed up, frozen, after the shutdown): "Create
    your own chip with our rapid IC creation platform for just **$9,750 per project**". The 2024
    page also lists what the price buys: "10 sq mm of project space", "38 programmable IO's",
    "100 QFN or Bare Die", "5 evaluation PCB boards", "Firmware and test tools".
  - **chipIgnite Mini**, a cheaper product that appears in captures from 2024-08-23: "chipIgnite Mini
    offers an affordable and efficient solution for bringing your ASIC designs to life. At just
    **$3,500 per project**, we divide our proven 'Caravel' design space into four independent
    projects".
  - **chipIgnite ML**, from 2024-11: "Proto-Only Option: … Pricing starts at **$14,750**.
    Proto + Production Option: … starting at **$30,000**."
  - **chipIgnite University Program**: "Tier I Pool of 5 projects **$48,750**", "Tier II Pool of 10
    projects **$87,750**".
  - **ChipFoundry, live on 2026-09-19:** "**$14,950 per tapeout**"; the FAQ states the change in its
    own words — "**Pricing: chipIgnite projects are priced at $14,950 compared to $9,750**" — and
    adds "There is an option for an additional 50 bare die for $3000", "We do not offer discounts
    for individual project submissions", and "If a shuttle does not meet the minimum customer
    commitment threshold required for launch, you will be offered: A full refund of your project
    fee, or The option to roll over your project to the next scheduled shuttle".
- **DERIVED (arithmetic written out):**
  - **The headline price was flat for four years.** $9,750 in May 2021 and $9,750 in December 2024.
    Against US CPI that is a real price *cut*; the repository does not deflate anywhere else, so it
    is left as a nominal observation.
  - Tier I is 5 × $9,750 = **$48,750 exactly — no discount at all**. Tier II is $87,750 ÷ 10 =
    **$8,775 per project, a 10% discount** (1 − 8,775 ÷ 9,750 = 0.10).
  - chipIgnite Mini is a quarter of the Caravel area for 35.9% of the price
    (3,500 ÷ 9,750 = 0.359), i.e. **1.44× the price per unit area** of a full slot.
  - ChipFoundry's rise: 14,950 ÷ 9,750 = **+53.3%**.
- **Bears on:**
  - **H6 (context, and it corrects an impression).** The repository has treated "$9,750 in 2021,
    $14,950 today" as a price series. It is not a series; it is **one price held flat for four
    years by one company, and then a 53% step change by a different company** after the first one
    failed. The flat price is itself evidence: Efabless never found it could charge more, and the
    successor immediately did.
  - **H6 (supports).** The $200 refundable deposit and the "minimum project capacity" clause are in
    the launch page from day one. **Both operators, four years apart, wrote undersubscription risk
    into their own published terms** — `OPG-9` records ChipFoundry's version and this is Efabless's.
    A programme that sells slots at a published price still cannot guarantee the run happens.
  - **`SMB-9` and `OPG-9` can both be upgraded.** `SMB-9` gives only the endpoints; the whole
    interior is now dated. `OPG-9`'s caveat marks the $14,950 price and the refund clause as
    **Partial**, read by a delegated agent; both were re-read directly on 2026-09-19 and are
    **Verified**.
- **Used in:** the price in `PAY-8`.
- **Caveats:**
  - The 2024–2025 efabless.com captures are of a site nobody was maintaining; the price on a dead
    company's page is not proof it was being charged.
  - chipIgnite Mini at $3,500 means **not every 2024 slot was sold at $9,750**, and no capture says
    how many Minis were sold. `PAY-8` therefore over-states 2024.
  - No capture gives a discount schedule for individuals, and ChipFoundry says there is none.

### PAY-8. DERIVED: chipIgnite and ChipFoundry revenue, 2021–2026 — and the peak was 2024

- **Sources:** the manufactured-slot counts in `OPG-1` and `OPG-3` (the repository owner's extract
  of Efabless's platform database), the archived platform pages re-read for this entry (URLs in the
  caveats), the prices in `PAY-7`, and ChipFoundry's live `all-metrics` API
  (<https://platform.chipfoundry.io/api/v1/shuttles/all-metrics>, re-fetched 2026-09-19).
- **Verification:** **DERIVED.** The slot counts are **Partial** (owner-supplied for four shuttles
  that no archive covers); the prices are Verified; ChipFoundry's `committed` counts were re-fetched
  on 2026-09-19 and are Verified as a reading of the API.
- **How it was counted:** `OPG-1`'s `Slots` column is the source spreadsheet's `Manufactured` field
  — the number of projects actually fabricated on that shuttle. **On chipIgnite, unlike the free
  Google Open MPW shuttles, being fabricated is what you pay for**, so a manufactured slot is taken
  here as a paid slot. Revenue = manufactured slots × the price in force. For ChipFoundry the
  equivalent field is `committed`, which `OPG-9` reads as "paid and locked in".
- **What it gives:**

  | Shuttle | Tapeout | Paid slots | Price | Revenue |
  |---|---|---:|---:|---:|
  | CI 2106Q | 2021-06-18 | 19 | $9,750 | $185,250 |
  | CI 2110C | 2021-11-26 | 13 | $9,750 | $126,750 |
  | CI 2204C | 2022-04-08 | 16 | $9,750 | $156,000 |
  | CI 2206Q | 2022-06-17 | 14 | $9,750 | $136,500 |
  | *CI 2209C* | *2022-09-19* | *8, status unconfirmed* | *$9,750* | *$78,000* |
  | CI 2211Q | 2022-12-05 | 22 | $9,750 | $214,500 |
  | CI 2304C | 2023-04-24 | 19 | $9,750 | $185,250 |
  | CI 2306Q | 2023-06-05 | 21 | $9,750 | $204,750 |
  | CI 2309 | 2023-09-11 | 20 | $9,750 | $195,000 |
  | CI 2311 | 2023-11-15 | 33 | $9,750 | $321,750 |
  | CI 2404 | 2024-04-24 | 40 | $9,750 | $390,000 |
  | CI 2406 | 2024-06-03 | 40 | $9,750 | $390,000 |
  | CI 2409 | 2024-09-16 | 40 | $9,750 | $390,000 |
  | CI 2411 | 2024-11-11 | 40 | $9,750 | $390,000 |
  | *CI 2504* | *never taped out* | *0 (20 projects had arrived)* | *$9,750* | *$0* |
  | CI 2509 | 2025-09-12 | 21 committed | $14,950 | $313,950 |
  | CI 2511 | 2025-11 | 23 committed | $14,950 | $343,850 |
  | CI 2605 | 2026, in fabrication | 29 committed | $14,950 | $433,550 |
  | CI 2609 | 2026, open | 16 committed so far | $14,950 | $239,200 |
  | CI 2612 | 2026, open | 0 so far | $14,950 | $0 |

  **By year of tapeout, CI 2209C excluded:**

  | Year | Paid slots | Revenue | Operator |
  |---|---:|---:|---|
  | 2021 | 32 | **$312,000** | Efabless |
  | 2022 | 52 | **$507,000** | Efabless |
  | 2023 | 93 | **$906,750** | Efabless |
  | 2024 | **160** | **$1,560,000** | Efabless |
  | 2025 | 44 | **$657,800** | ChipFoundry |
  | 2026 (to 2026-09-19) | 45 | **$672,750** | ChipFoundry |
  | **Total** | **426** | **$4,616,300** | |

  Including CI 2209C adds 8 slots and $78,000 to 2022.
- **DERIVED growth, and this is the answer to the question this file was written for:**
  - **Paid slots** 2021 → 2024: 32 → 52 → 93 → 160. Year on year ×1.63, ×1.79, ×1.72.
    CAGR = (160 ÷ 32)^(1/3) − 1 = 5^(1/3) − 1 = **+71.0%/yr**.
  - **Submissions** over the same years (`OPG-7`): 51 → 125 → 225 → 377. Year on year ×2.45, ×1.80,
    ×1.68. CAGR = (377 ÷ 51)^(1/3) − 1 = **+94.8%/yr**.
  - **Over the three years, submissions rose 7.39× and paid slots rose 5.00×.**
    **Revenue grew, but it grew more slowly than interest did**, and the reason is visible in the
    table: the shuttle was capped at 40 slots and hit the cap in 2024, while submissions kept
    climbing to 377.
  - **ChipFoundry**: 44 paid in 2025, 45 so far in 2026 — **+2.3%**, against `interest` of 129 and
    262 on the same shuttles, **+103%** (`OPG-9`). Two points is not a trend and must not be
    presented as one.
  - **The peak is 2024 and the programme has not recovered.** $1,560,000 in 2024 against $657,800 in
    2025 and $672,750 so far in 2026 — **57.8% down** on the peak
    (1 − 657,800 ÷ 1,560,000 = 0.578).
- **Bears on:**
  - **H5 (challenges, and this is the most important number in the file).** The repository's
    headline for the paid programme is `OPG-7`'s "about 1.7× a year". **On money it is about
    1.7× a year too — until 2024, when it stops, because the supplier ran out of slots and then ran
    out of money.** The submission series and the revenue series agree about *direction* and
    disagree about *ceiling*. Interest is uncapped; a 40-slot shuttle is not.
  - **H5 (challenges).** The gap between 377 submissions and 160 paid slots in 2024 is not all
    unmet demand. Efabless ran design contests on its own shuttles with **free fabrication as the
    prize** — its April 2024 release offers "The top ten winners will be awarded free fabrication
    of their designs" (`OPG-6`). An unknown share of chipIgnite "submissions" were contest entries
    competing for a sponsored slot, not customers who would have paid $9,750.
  - **H6 (context).** $1.56m of gross revenue in the best year, from a company that then failed to
    raise a Series B (`OPG-15`). Whatever a SkyWater shuttle costs, four a year at 40 slots was not
    enough to sustain the company.
  - **H6 (context).** ChipFoundry is running the same product at +53% price and about a quarter of
    the volume, with a published refund clause for shuttles that do not fill (`PAY-7`).
- **Used in:** the revenue table at the foot of this file.
- **Caveats — several, and two of them are serious:**
  - **"Manufactured slots = paid slots" is an inference, not a statement.** Nobody at Efabless ever
    said so. Free contest slots and sponsored academic slots are inside these counts and are not
    revenue. Ten free TinyML prizes alone would cut 2024 by $97,500.
  - **The 40s are suspicious.** All four 2024 shuttles show exactly 40 manufactured, which is also
    the nominal capacity Efabless's platform used for every shuttle. Either they all filled exactly,
    or 40 is a default. **We could not resolve this.** The archived platform pages carry a separate
    line, "*N* of 40 project slots reserved", and it reads **19** for CI 2106Q, **13** for CI 2110C,
    **16** for CI 2204C and **14** for CI 2206Q on captures taken after those shuttles closed — but
    **0** for CI 2211Q, CI 2404 and CI 2406 on captures taken while they were open, and the field is
    absent from the later page layout entirely. It behaves like a manually maintained field, not a
    live count, so it cannot serve as an independent check. Captures read on 2026-09-19:
    `https://web.archive.org/web/20240421145959id_/https://platform.efabless.com/shuttles/2106Q`,
    `…/20221206073015id_/…/2110C`, `…/20231114083445id_/…/2204C`,
    `…/20240519044142id_/…/2206Q?active_tab=summary`, `…/20221114235435id_/…/2211Q`,
    `…/20240227031436id_/…/CI%202404`, `…/20240413194415id_/…/CI%202406`,
    `…/20240718142010id_/…/CI%202409`, `…/20250124154327id_/…/CI%202411`,
    `…/20250125035816id_/…/CI%202504`.
  - **chipIgnite Mini at $3,500 (`PAY-7`) was on sale from about August 2024** and would cut $6,250
    off this table for every slot sold as a Mini.
  - Four of the Efabless-era rows (CI 2304C, CI 2306Q, CI 2311, CI 2209C) have **no Internet Archive
    capture at all** and rest entirely on the owner's spreadsheet.
  - ChipFoundry's fields are mutable and have been revised downwards (`OPG-9`); the counts here are
    as read on 2026-09-19, and CI 2609 and CI 2612 are still open, so 2026 will rise.
  - **Eight Efabless-era slots and at least five ChipFoundry-era slots are Tiny Tapeout's own
    purchases** (`PAY-5` maps them). That money is in this table as chipIgnite revenue and in
    `PAY-6` as Tiny Tapeout revenue. **Adding the two programmes double-counts it**; the combined
    table below nets it out.
  - Everything is gross revenue. The wafers, the masks, the packaging and the staff come out of it.

---

## wafer.space

### PAY-9. wafer.space: $55,500, then $175,000, then $125,000 so far — the only programme here that publishes the money itself

- **Sources:**
  - <https://www.crowdsupply.com/wafer-space/gf180mcu-run-1>
  - <https://www.crowdsupply.com/wafer-space/gf180mcu-run-2>
  - <https://www.crowdsupply.com/wafer-space/gf180mcu-run-3>
  - <https://wafer.space/> and <https://wafer.space/news/>
- **Verification:** **Verified 2026-09-19.** All five pages fetched with `curl --compressed` and a
  browser `User-Agent`, and read directly by the author of this entry. `OPG-12` recorded these
  figures **Partial**, from a delegated agent; this is the re-read it asked for, and **two of the
  numbers have moved**.
  **Conflict of interest: wafer.space is the repository owner's own company** (the campaign pages
  list Tim Ansell as founder; the site footer reads "© 2025 Wafer Space PTE. LTD." at
  "143 Cecil Street, #17-04, GB Building, Singapore 069542").
- **What it says**, verbatim, as read on 2026-09-19:

  | Campaign | Raised | Goal | Backers | Status |
  |---|---|---|---:|---|
  | GF180MCU Run 1 | "$ 55,500 raised" | "of $ 40,000 goal", "138 % Funded!" | **6** | "Nov 28 2025 funded on"; products "No Longer Available" |
  | GF180MCU Run 2 | "$ 175,000 raised" | "of $ 1 goal", "Funded!" | **18** | "Jun 29 funded on" (2026) |
  | GF180MCU Run 3 | "$ 125,000 raised" | "of $ 1 goal", "Funded!" | **6** | "91 days left"; "Funding ends on Dec 19, 2026 at 03:59 PM PST" |

  **Run 3 has moved since `OPG-12` was written**: `OPG-12` records "$121,500 raised" and "5 backers";
  the page now reads $125,000 and 6 backers. It is a live page and will move again.

  Prices, as printed:
  - **Run 1**: "GF180MCU Shuttle Slot, Bare Dies … Includes 1,000 bare dies delivered in a Gel-Pak"
    **$7,000**; "GF180MCU Shuttle Slot, Wire-Bonded … Includes 1,000 dies mounted to PCBs and wire
    bonded" **$8,500**; "Undiced Full Wafer … Can only be ordered with a design slot purchase"
    **$2,000**. Slot geometry: "Each slot consists of a 3.88 mm × 5.07 mm (19.67 mm²) fixed die
    area, replicated 1,000 times."
  - **Run 2**: 1×1 **$7,000** early bird / **$7,500** standard; 0.5×1 and 1×0.5 **$4,000** /
    **$4,500**. "Early bird pricing is available through 30 April 2026."
  - **Run 3**: 1×1 **$7,000** / **$8,000**; 0.5×1 and 1×0.5 **$4,000** / **$5,000**;
    0.5×0.5, new this run, **$2,000** / **$3,000**. Add-on: "Chip on Board Packaging $1,500 USD ·
    $1.50 per die". Early-bird deadline 30 September 2026, purchase deadline 9 December 2026,
    "Q2 2027 Bare dies and packaged parts shipped".
  - The site's own headline: "Get 1,000 custom silicon dies from just $2 per die".
- **DERIVED (arithmetic written out):**
  - **Revenue by year of campaign close:** 2025 → **$55,500** (Run 1, closed 2025-11-28);
    2026 → **$300,000 so far** (Run 2's $175,000, closed 2026-06-29, plus Run 3's $125,000 with
    three months still to run). **Total to date $355,500.**
  - Growth 2025 → 2026: 300,000 ÷ 55,500 = **×5.4**, on n = 2 and with 2026 incomplete. Two data
    points are not a growth rate and this must not be quoted as one.
  - **Revenue per backer:** Run 1 $55,500 ÷ 6 = **$9,250**; Run 2 $175,000 ÷ 18 = **$9,722**;
    Run 3 $125,000 ÷ 6 = **$20,833**. The first two sit just above the $7,000–$8,500 full-slot
    price, so the typical backer bought about one slot plus an add-on. Run 3's is 2.1× that, so its
    six backers are buying several slots each — a **different kind of customer**, or, on six orders,
    simply noise.
  - **Backers, not customers:** 6 + 18 + 6 = **30 orders in thirteen months**, worldwide.
- **Bears on:**
  - **H5 (supports).** $355,500 of unsubsidised, pre-paid orders in thirteen months, at a published
    flat price, with no sales process and no NDA. On revenue that is already about half of Tiny
    Tapeout's entire five-year total (`PAY-6`), reached in a year.
  - **H5 (challenges).** **Thirty orders.** That is the whole worldwide response. `OPG-12` makes
    this point and re-reading the pages does not soften it: the money is real and the customer count
    is tiny. A programme whose 2026 revenue rests on six orders has no law of large numbers
    protecting it.
  - **H6 (supports).** The money arrives before the wafer does, at a published price, with the
    buyers carrying the fill risk. That is the shape `PRINCIPLES.md` argues for, and wafer.space is
    the only programme here whose takings are published as a matter of course.
- **Used in:** the revenue table at the foot of this file.
- **Caveats:**
  - **Self-interested.** Our own company, our own numbers.
  - "Raised" is the platform's gross figure. **Crowd Supply takes a fee and it is not published on
    these pages**, so wafer.space's own receipts are lower than these numbers by an unknown margin.
  - "Backers" counts **orders**, not people, and includes non-slot pledges (the $2,000 undiced
    wafer, the $1,500 chip-on-board add-on).
  - Run 1's goal was restated mid-campaign from $68,012 to $40,000 (`OPG-12`), so its
    "138 % Funded!" badge should not be quoted. Runs 2 and 3 carry a $1 placeholder goal, so theirs
    should not be quoted either.
  - **Run 3 is open.** Its $125,000 and its 6 backers are both floors.
  - **Tiny Tapeout is one of the buyers.** `PAY-5` shows TTGF0p2 on WS-2512 and TTGF26a, TTGF26b and
    TTGF0p3 on WS-2606, so part of Run 1's and Run 2's money is Tiny Tapeout's, and part of
    wafer.space's backer count is one intermediary reselling tiles. `OPG-11` records the same
    pattern at IHP.
  - No campaign publishes how many slots were sold — only how much money and how many orders.

---

## Company filings

### PAY-10. Efabless's last financing was $2.5m of debt from one investor, five months before it shut down — and it declined to disclose its revenue

- **Source:** Efabless Corporation, Form D (notice of exempt offering of securities), filed with the
  US Securities and Exchange Commission on 2024-10-08.
  Accession number **0002039822-24-000001**, CIK **0002039822**, file number 021-526093.
  Document: <https://www.sec.gov/Archives/edgar/data/2039822/000203982224000001/xslFormDX01/primary_doc.xml>
  Company index: <https://data.sec.gov/submissions/CIK0002039822.json>
- **Verification:** **Verified 2026-09-19.** The filing was located through EDGAR full-text search
  (`https://efts.sec.gov/LATEST/search-index?q=efabless`, which serves automated requests and
  returned 21 hits, exactly one of them a Form D) and the document itself was read through
  `WebFetch`. **`curl` cannot fetch `www.sec.gov/Archives` at all** — every request returns HTTP 403
  "Your Request Originates from an Undeclared Automated Tool", under every `User-Agent` tried, and
  SEC's stated remedy is to put a contact e-mail address in the `User-Agent`, which this work does
  not do. `www.sec.gov/cgi-bin/browse-edgar` returns 403 for the same reason.
- **What it says**, field by field:
  - Issuer **efabless Corp**, incorporated in **Delaware**, "Over Five Years Ago", principal place
    of business **969 Industrial Road, Suite I, San Carlos, California 94070**.
  - Related persons: **Michael Wishart** (executive officer and director), **Mohamed Kassem**
    (executive officer and director), **Lucio Lanza**, **Jack Hughes**, **Jeremy Hitchcock**
    (directors).
  - Industry group: **Other Technology**.
  - **Issuer size / revenue range: "Decline to Disclose".**
  - Type of filing: **new notice**. Federal exemption: **Rule 506(b)**.
  - Securities offered: **Debt**.
  - **Date of first sale: 2024-09-27. Total offering amount $2,500,000. Total amount sold
    $2,500,000. Remaining to be sold $0. Number of investors: 1.** Sales commissions $0, finders'
    fees $0, minimum investment $0.
  - Signed by **Michael Wishart, Chief Executive Officer, 2024-10-05**.
  - **It is the only filing EDGAR holds for this issuer.** The submissions index lists one
    accession number and nothing else.
- **Bears on:**
  - **H6 (context, and it is the sharpest piece of context in the file).** **Money raised is not
    revenue and must never be presented as such.** But the shape of this raise is informative:
    five months before it shut down, and at the point `OPG-15` says it "was not able to close our
    Series B round", Efabless took **$2.5m of debt from a single investor** — a bridge, not a
    round. Set beside `PAY-8`'s $1.56m of 2024 chipIgnite gross revenue, a $2.5m bridge is roughly
    nineteen months of that revenue line, and it was not enough.
  - **H6 (context).** "Decline to Disclose" on the revenue box is a legal option, freely chosen. It
    is the closest thing to an Efabless revenue disclosure that exists, and it discloses nothing.
  - **H5 (context).** Lucio Lanza and Jack Hughes on the board are serious EDA and semiconductor
    names. This was not an unfunded hobby; it had the people who would know.
- **Used in:** context for `PAY-8`.
- **Caveats:**
  - **A Form D is a notice of an exempt offering. It is not audited and carries no revenue figure.**
    Nothing in it says what Efabless sold or earned.
  - "Over Five Years Ago" and the single-filing history mean **EDGAR does not hold Efabless's
    earlier venture rounds**. Either they were filed under a different registrant we did not find,
    or they were not filed on EDGAR. `OPG-15`'s account of the funding history is not corroborated
    here beyond this one filing.
  - The document was read through `WebFetch`, which summarises with a small model; the field values
    above were requested verbatim and are consistent across two separate reads of the raw XML and
    the XSL-rendered form, but **no human re-read the primary document**.

### PAY-11. Tiny Tapeout B.V.'s filed accounts would settle the question outright, and we could not reach them

- **Source:** Tiny Tapeout's own terms of service name the legal entity — "The Terms constitute a
  binding agreement between you and **Tiny Tapeout B.V.**" — and set jurisdiction: "These Terms
  shall be governed by the laws of the Netherlands … the competent court located in **Amsterdam,
  the Netherlands**" (<https://tinytapeout.com/terms/>, read from the site's public source
  repository on 2026-09-19).
- **Verification:** **Verified** for the entity name and jurisdiction. **Blocked** for the accounts.
- **What it says, and what it would say if it could be read:** a Dutch **besloten vennootschap**
  (B.V., a private limited company) is required to file annual accounts with the KvK (Kamer van
  Koophandel, the Chamber of Commerce). KvK's own page states the obligation and the retention
  period — in the original Dutch, "**Bv's en nv's zijn vrijwel altijd verplicht een jaarrekening te
  deponeren**" (*translated: "B.V.s and N.V.s are almost always required to file annual
  accounts"*) and "**Je kunt jaarrekeningen opvragen tot 7 jaar terug**" (*translated: "You can
  request annual accounts going back up to 7 years"*), at
  <https://www.kvk.nl/producten-bestellen/jaarrekeningen/> (read 2026-09-19).
  A small B.V. files an abbreviated balance sheet, which normally shows total assets, equity and
  sometimes turnover. **That single document would replace the whole of `PAY-6` with a measurement.**
- **What was tried, and what blocked it** (all on 2026-09-19):
  - `https://www.kvk.nl/zoeken/?zoekwoord=tiny%20tapeout` returns HTTP 200 but the trade-register
    results are rendered client-side; the served HTML contains only the CMS chrome. Read through
    `WebFetch` it comes back as "a generic landing/help page … no trade register entries".
  - `https://www.kvk.nl/zoeken/handelsregister/?handelsnaam=tiny+tapeout` returns **HTTP 404**.
  - `https://api.kvk.nl/api/v2/zoeken?naam=tiny%20tapeout` returns **HTTP 401**; the KvK API needs a
    key, which needs an account, and **this work does not create accounts**.
  - The ordering flow for a filed annual account is a paid product. **We did not enter it**, so we
    cannot state its price. KvK's published product list does not print a price on the
    jaarrekeningen page itself.
  - No KvK number appears anywhere on tinytapeout.com — not in the terms, not on the contact page,
    not in the site footer.
- **Bears on:**
  - **H6 (context).** This is the one document that would turn the largest estimate in this file
    into a fact, and it exists, and it is cheap for a human. **Recorded as the single highest-value
    open item in this file.**
- **Used in:** the blocked-sources list.
- **Caveats:**
  - We did not establish that Tiny Tapeout B.V. *has* filed. A company incorporated in 2023 or 2024
    may have filed once or not at all, and a micro-entity's filing may contain no turnover figure.
  - We did not establish the KvK number, so even the existence of the registration is, strictly,
    inferred from the company's own terms of service.
  - **What a human should do:** search `https://www.kvk.nl/zoeken/handelsregister/` for
    "Tiny Tapeout" in an ordinary browser, note the KvK number, then order the deposited
    jaarrekening for each available year. Everything after the search costs money.

---

## The revenue table

All three programmes, by calendar year. Tiny Tapeout on the **MID** assumption from `PAY-6`;
chipIgnite/ChipFoundry from `PAY-8`; wafer.space from `PAY-9`. Euro amounts are converted at the
**ECB euro reference rate for 2026-09-17, EUR 1 = USD 1.1481**, the same rate `SMB-9` uses.

| Year | Tiny Tapeout | chipIgnite → ChipFoundry | wafer.space | **Total (US$)** |
|---|---:|---:|---:|---:|
| 2021 | — | $312,000 | — | **$312,000** |
| 2022 | $11,650 | $507,000 | — | **$518,650** |
| 2023 | $42,400 | $906,750 | — | **$949,150** |
| 2024 | $166,925 | **$1,560,000** | — | **$1,726,925** |
| 2025 | $217,858 | $657,800 | $55,500 | **$931,158** |
| 2026 (to 2026-09-19) | $392,317 | $672,750 | $300,000 | **$1,365,067** |
| **Total** | **$831,150** | **$4,616,300** | **$355,500** | **$5,802,950** |

Tiny Tapeout's 2025 row is $38,100 + €156,570 = $38,100 + $179,758; its 2026 row is €341,710.
The **LOW** and **HIGH** Tiny Tapeout cases (`PAY-6`) move the 2026 total between $1,255,000 and
$1,505,000 and the six-year total between $5.6m and $6.1m — so **the Tiny Tapeout uncertainty,
large as it is in percentage terms, barely moves the sector total.** The sector total is
chipIgnite's number.

**Netting out the double count.** Tiny Tapeout buys its wafer space from the other two programmes
(`PAY-5`): at least one chipIgnite slot for each of TT02, TT03, TT04, TT05, TT06, TT07, TT08, TT09,
TTSKY25a, TTSKY25b, TTSKY26a/b and TTSKY26c, plus wafer.space slots for the TTGF runs.
**DERIVED:** one slot per shuttle at the price of the day is 1 × $9,750 (2022) + 3 × $9,750 (2023)
+ 4 × $9,750 (2024) + 2 × $14,950 (2025) + 2 × $14,950 (2026) = 9,750 + 29,250 + 39,000 + 29,900 +
29,900 = **$137,800**, about **2.4%** of the $5.80m total. It is small, but it is real, and the
combined total is a sector *gross* figure, not a sector *value-added* figure.

## Growth on revenue against growth on submissions

This is what the file was written to answer. **They do not tell the same story, and they diverge in
opposite directions for different programmes.**

| Programme | Window | Interest series | CAGR | Money series | CAGR | Which grew faster |
|---|---|---|---:|---|---:|---|
| **chipIgnite** | 2021–2024 | submissions 51 → 377 | **+94.8%** | paid slots 32 → 160 | **+71.0%** | **interest, by a wide margin** |
| **ChipFoundry** | 2025 → 2026 | `interest` 129 → 262 | **+103%** | `committed` 44 → 45 | **+2.3%** | **interest, overwhelmingly** |
| **Tiny Tapeout** | 2022–2025 | design records 166 → 1,530 | **+109.7%** | revenue $11,650 → $217,858 | **+156% to +165%** | **money** |
| **wafer.space** | 2025 → 2026 | orders 6 → 24 | ×4.0 | revenue $55,500 → $300,000 | ×5.4 | money, on n = 2 |
| **All three** | 2021–2024 | — | — | total $312k → $1.73m | **+76.9%** | — |
| **All three** | 2021–2025 | — | — | total $312k → $931k | **+31.4%** | — |

**Four findings, stated plainly.**

1. **On chipIgnite — the longest paid series in the record — revenue grew materially more slowly
   than submissions.** Submissions rose 7.39× over three years; paid slots rose 5.00×. The cause is
   not mysterious: **a 40-slot shuttle caps revenue and nothing caps interest.** Every
   "oversubscribed" figure in `OPG-1`, `OPG-2` and `shuttle-programmes.md` is measuring the
   uncapped side.
2. **On ChipFoundry the divergence is total.** Interest doubled; money did not move. `OPG-9`
   already said this and it survives re-reading the API. Two points is not a trend, and it is the
   only direct measurement of the gap anyone publishes.
3. **On Tiny Tapeout revenue grew *faster* than designs** — because the price rose. Revenue per
   design went $70 → $102 → $194 → $134 → €252 (`PAY-6`). This is the one place where the money
   series is *better* news than the unit series, and the reason is pricing power, not volume.
4. **The sector's money fell 46% in 2025, the year its unit counts hit a record.**
   $1,726,925 in 2024 → $931,158 in 2025 (1 − 931,158 ÷ 1,726,925 = 0.461), while
   `data-cuts-and-statistics.md` §3.2 records 2025 as Tiny Tapeout's largest year ever at 1,530
   design records. **A reader given only the submission series would not know that 2025 was the
   worst year the sector has had.** That is the strongest single argument in this repository for
   not quoting submission counts as demand.

   The cause is known and it is not a demand collapse: Efabless failed in March 2025, CI 2504 never
   taped out, and TT10 was cancelled. `OPG-3`, `OPG-7` and `PAY-5` all say so. But **"the operator
   died" is exactly the kind of risk a revenue series shows and a submission series hides**, and
   H6 is about whether serving these customers is a business, not about whether they want the
   product.

## Cross-check against the top-down estimate

`open-access-audit.md` §6.1 estimates the entire genuinely-open, genuinely-commercial sector at
**"plausibly one to three million dollars of annual revenue"** in 2026, and ChipFoundry alone at
"roughly $1M a year".

**DERIVED, bottom-up, for 2026:** $1,365,067 for the first 8.6 months. Annualised at the same rate,
1,365,067 × 12 ÷ 8.6 = **about $1.9m**. ChipFoundry alone: 672,750 × 12 ÷ 8.6 = **about $0.94m**.

**The two agree, and the bottom-up figure sits in the lower half of the top-down range.** Where they
differ I trust the bottom-up figure, because every one of its inputs is a dated published price
multiplied by a dated published unit count, and the top-down figure is an informed guess. Two things
qualify that:

- The bottom-up figure covers **only these three programmes**. It excludes IHP's paid Open-Silicon
  MPW. **DERIVED from `OPG-11`:** its SG13G2 run had 59.2 mm² registered at €2,800/mm² =
  **€165,760**, and its CMOS5L run 44.5 mm² at €1,500/mm² = **€66,750** — together about
  **€232,510, or $267,000**, though registered area is not a paid order and the CMOS5L run had not
  reached its 90 mm² minimum. It also excludes Cadence/SkyWater's $10,000 aggregation service
  (`OPG-19`) and anything we did not find. The true sector figure is higher than $1.9m.
- Two of the five open shuttles counted (CI 2609, CI 2612) and one wafer.space campaign (Run 3) are
  still taking orders, so 2026 will end higher than the annualisation implies.

**The honest statement is therefore: the whole open-and-commercial sector is running at roughly
$2m a year of gross revenue in 2026, its best year was 2024 at about $1.7m from three programmes,
and it has never been larger than that.** `open-access-audit.md` §6.1's comparison stands and gets
sharper: `SMB-5` records MOSIS at "up to $10 million annually at its peak" in 1990s money.

## Revenue per customer and per design

| Programme | Unit | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---:|---:|---:|---:|---:|---:|
| chipIgnite / ChipFoundry | per paid slot | $9,750 | $9,750 | $9,750 | $9,750 | $14,950 | $14,950 |
| wafer.space | per order | — | — | — | — | $9,250 | $9,722 / $20,833 |
| Tiny Tapeout | per design | — | $70 | $102 | $194 | $134 | €252 |
| Tiny Tapeout | per tile | — | $70 | $69 | $109 | $144 | €134 |

**DERIVED:** a chipIgnite customer was worth **50×** a Tiny Tapeout design in 2024
(9,750 ÷ 194 = 50.3), and a ChipFoundry customer is worth **52×** a Tiny Tapeout design in 2026
(14,950 ÷ (252 × 1.1481) = 14,950 ÷ 289 = 51.7).
Across the three programmes in 2026, **$972,750 of the $1,365,067 — 71% — came from roughly fifty
orders** (45 ChipFoundry commitments and about six wafer.space orders in the year), and the
remaining 29% came from 1,358 Tiny Tapeout designs.

**The reading for H6.** The long tail in this sector is real in *headcount* and almost absent in
*money*. Seven pounds in ten comes from a few dozen orders a year at $7,000–$15,000 each; three
pounds in ten comes from well over a thousand orders at €70–€400 each. Any business model built on
the thousand has to be almost entirely self-serve, because `data-cuts-and-statistics.md` §5.3's
lifetime value of €122–$521 per acquired designer leaves nothing for a sales motion — and this file
puts the same conclusion on the revenue side. Any business model built on the fifty is a business
with fifty customers, which is `CONC`-style concentration at the bottom of the market, exactly as
`OPG-11` found at IHP.

## Blocked sources

Everything that could not be reached, with the blocker, as `resources/README.md` requires.

| Source | What it would have given | Blocker |
|---|---|---|
| **KvK deposited annual accounts for Tiny Tapeout B.V.** | Filed turnover and balance sheet — would replace `PAY-6` with a measurement | Trade-register search is client-side and `…/zoeken/handelsregister/` returns HTTP 404; `api.kvk.nl` returns HTTP 401 without a key; a key needs an account and the accounts themselves are a paid product. **We create no accounts and pay for nothing.** Highest-value open item in this file. |
| **`www.sec.gov/Archives` and `cgi-bin/browse-edgar` via `curl`** | Efabless's Form D | HTTP 403, "Your Request Originates from an Undeclared Automated Tool", under every `User-Agent`. SEC's remedy is an e-mail address in the `User-Agent`, which this work will not do. **Worked around**: `efts.sec.gov` serves automated requests and `WebFetch` reached the document (`PAY-10`). |
| **Efabless's earlier venture rounds** | Amounts and dates before the 2024 bridge | EDGAR holds exactly one filing for CIK 0002039822. Earlier rounds are either under a registrant we did not find or were never filed on EDGAR. |
| **Keyword search of conference talks and slides** (FOSSi Dial-Up, ORConf, Supercon, FOSDEM) for Tiny Tapeout unit or revenue numbers | Possibly a founder-stated revenue figure | **The session's web-search budget was exhausted (200 of 200 calls) before this task reached that step.** Nothing was searched for. The task explicitly asked for it and it is **not done**. |
| **`platform.efabless.com` shuttle pages for CI 2304C, CI 2306Q, CI 2311, CI 2209C** | Independent check on four rows of `PAY-8` | The site is dead and the CDX API returns no captures for these URLs on any date (`OPG-2` records the same). |
| **Whether Efabless's four 2024 shuttles really manufactured 40 slots each** | Would fix the largest single number in `PAY-8` | The "*N* of 40 project slots reserved" field on the archived pages behaves like a manually maintained value (0 while open, a real number after close, absent from the later layout). No source resolves it. |
| **Tiny Tapeout's sponsored-versus-sold split per shuttle** | Would fix `PAY-6`'s largest uncertainty | Never published. The IEEE block booking on TTSKY26b ("Half the area and PCBs have been reserved for them") is the only quantified instance and even that gives no price. |
| **Crowd Supply's platform fee** | wafer.space's net receipts | Not printed on the campaign pages, and Crowd Supply does not publish a public rate card on them. |
| **Tiny Tapeout PCB attach rate after 2024** | Would replace the 0.50–0.70 assumption in `PAY-6` | Published for TT04 and TT06 only (`PAY-4`). |
| **`app.tinytapeout.com/prepurchase`** (prepaid credits for universities) | Institutional pricing | An empty single-page-application shell, like the calculator; the prices are not in the served HTML and we did not find a second price module. |
| **Internet Archive, intermittently** | — | The CDX API returned "Internet Archive services are temporarily offline" for part of 2026-09-19, and `web.archive.org` rate-limits after roughly twenty fetches. Every capture cited above was eventually retrieved, with backoff. |

## Changes this file implies for files it does not own

1. **`SMB-10`'s caveat is now wrong** and should be corrected. It says "The headline Tiny Tapeout
   price (tile + ASIC + board) is **not published as a number** anywhere we could read". It is:
   `PAY-3` reads the whole schedule out of the order application's own invoice module. `SMB-10`'s
   €3,900/mm² derivation can also be redone against that schedule.
2. **`OPG-9`'s caveat can be upgraded from Partial to Verified** for two items: ChipFoundry's
   "$14,950 per project" price and the minimum-commitment refund clause were both re-read directly
   from `https://chipfoundry.io/faqs` on 2026-09-19 (`PAY-7`).
3. **`OPG-12` is out of date on wafer.space Run 3.** It records "$121,500 raised" and "5 backers";
   the page read $125,000 and 6 backers on 2026-09-19 (`PAY-9`). `OPG-12`'s Partial status can also
   be upgraded — all three campaign pages have now been read directly.
4. **`SMB-9` should point at `PAY-7`** for the interior of the price history. Its "$9,750 in 2021,
   $14,950 today" reads as a series; `PAY-7` shows it is a flat price followed by a step change by
   a different company.
5. **`OPG-1`'s `Slots` column should carry the warning in `PAY-8`'s caveats** — that it is the
   spreadsheet's `Manufactured` field, that on chipIgnite it is the closest thing to a paid-customer
   count, and that the four 2024 shuttles' identical 40s are unverified.
6. **`hypotheses.md` needs H5 and H6 updating** with the divergence in the growth-rate table above.
   H5's Challenges list should gain "the sector's revenue fell 46% in 2025, the year its unit counts
   set a record"; H6's should gain "71% of the sector's money comes from about fifty orders a year".
7. **`data-cuts-and-statistics.md` §2.4** ("Free versus paid") now has a matched money series to sit
   beside its unit series, and §5.3's "€540,960 – $2,318,400" lifetime range can be narrowed to
   `PAY-6`'s $0.63m – $1.11m.
