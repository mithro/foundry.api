# Shuttle and multi-project wafer programmes (`DEM`)

How many people actually submit a chip design when the price of trying falls to a few hundred
dollars, or to nothing. These are the closest thing that exists to a direct test of H5.

A **multi-project wafer** (MPW), or **shuttle**, run puts many customers' designs onto one set of
masks and one wafer lot, so they share the mask cost. It is how universities and small companies
have made prototype chips since the 1980s. Submission counts, acceptance rates and how full each run
is are therefore a direct measure of how many people want to make a chip at a given price.

---

### DEM-1. Tiny Tapeout publishes a design count for every shuttle it has ever run

- **Source:** Tiny Tapeout, "Tiny Tapeout Chips": <https://tinytapeout.com/chips/>
- **Verification:** Verified 2026-09-18. Fetched and read the page itself; the page's own
  `dateModified` metadata reads `2026-09-15T20:16:23+01:00`.
- **What it says:** a table headed "Current chips" with the columns "Run", "Launched", "Closed",
  "Shuttle", "Designs", "Chips expected", "Estimated delivery date". Transcribed in full, the
  "Designs" column reads:

  | Run | Launched | Closed | Foundry shuttle | Designs |
  |---|---|---|---|---|
  | TTIHP26b | 2026-07-27 | 2026-09-21 | IHP-2609 | Open |
  | TTSKY26c | 2026-05-26 | 2026-09-07 | CI-2609 | 242 |
  | TTGF0p3 | 2026-06-01 | 2026-07-07 | WS-2606 | 32 |
  | TTGF26b | 2026-06-05 | 2026-06-22 | WS-2606 | 90 |
  | TTGF26a | 2026-04-17 | 2026-06-22 | WS-2606 | 95 |
  | TTSKY26b | 2026-04-25 | 2026-05-18 | CI-2605 | 273 |
  | TTSKY26a | 2026-02-27 | 2026-05-11 | CI-2605 | 289 |
  | TTIHP0p4 | 2026-03-27 | 2026-03-28 | IHP-2603 | 40 |
  | TTIHP26a | 2025-11-25 | 2026-03-23 | IHP-2603 | 283 |
  | TTGF0p2 | 2025-11-06 | 2025-11-24 | WS-2512 | 52 |
  | TTSKY25b | 2025-09-18 | 2025-11-10 | CI-2511 | 316 |
  | TTSKY25a | 2025-06-27 | 2025-09-15 | CI-2509 | 237 |
  | TTIHP25b | 2025-04-20 | 2025-09-01 | IHP-2509 | 81 |
  | TTIHP25a | 2025-03-12 | 2025-03-28 | IHP-2504 | 547 |
  | TT10 | 2024-11-11 | Cancelled | - | - |
  | TT09 | 2024-09-07 | 2024-11-10 | CI-2411 | 369 |
  | TTIHP0p2 | 2024-10-22 | 2024-11-04 | IHP-2504 | 95 |
  | TT08 | 2024-06-10 | 2024-09-06 | CI-2409 | 135 |
  | TT07 | 2024-04-22 | 2024-06-01 | CI-2406 | 120 |
  | TT06 | 2024-01-30 | 2024-04-19 | CI-2404 | 238 |
  | TT05 | 2023-09-11 | 2023-11-04 | CI-2311 | 174 |
  | TT04 | 2023-07-01 | 2023-09-08 | CI-2309 | 143 |
  | TT03 | 2023-03-01 | 2023-04-23 | CI-2304C | 100 * |
  | TT02 | 2022-11-09 | 2022-12-02 | CI-2211Q | 165 |
  | TT01 | 2022-08-17 | 2022-09-01 | MPW7 | 152 |

  - **DERIVED:** summing the "Designs" column over the 23 rows that print a number gives
    **4,268 designs** across all Tiny Tapeout shuttles from TT01 (closed 2022-09-01) to TTSKY26c
    (closed 2026-09-07). TTIHP26b prints "Open" and TT10 prints "Cancelled", so neither is in the
    sum. Arithmetic: 242 + 32 + 90 + 95 + 273 + 289 + 40 + 283 + 52 + 316 + 237 + 81 + 547 + 369 +
    95 + 135 + 120 + 238 + 174 + 143 + 100 + 165 + 152 = 4,268.
  - The page also says: "Tiles and PCBs for open shuttles can be prepurchased at
    app.tinytapeout.com/prepurchase ." and lists two future runs, "TTGF26c" (submission deadline
    "Dec 2026") and "TTSKY26d" ("Nov 2026").
- **Bears on:**
  - H5 (supports): between four and five thousand separate chip designs were submitted by paying
    customers in four years, on three different foundry processes, at a price of a few hundred
    dollars. These are people who would not otherwise have made a chip at all.
  - H4 (supports).
- **Used in:** not yet.
- **Caveats:**
  - A "design" here is a tile on a shared die — roughly 160 × 100 µm on SKY130, about a thousand
    logic gates (Tiny Tapeout's own FAQ, checked 2026-09-18: "For TT04 to TT10, the standard tile
    size is about 160x100 um. This is enough for about 1000 digital logic gates, depending on their
    size."). These are experiments and teaching exercises, not products.
  - Design counts are not customer counts. One person can submit many designs, and university
    courses submit in bulk. See DEM-2 for a count of distinct projects.
  - The TT03 figure carries an asterisk with no footnote anywhere on the page. DEM-4 explains it.
  - The table is Tiny Tapeout's own; DEM-2 is an independent count from its API that agrees.

### DEM-2. Counting Tiny Tapeout's submissions from its public API, and how full each run was

- **Source:** Tiny Tapeout submission-statistics API:
  <https://app.tinytapeout.com/api/shuttles/submission-stats>. This is the endpoint that
  <https://tinytapeout.com/chips/> links to under its "Stats" heading, where the page says "Graphs
  created by tt-shuttle-stats using data from the API ." (tool repository:
  <https://github.com/TinyTapeout/tt-shuttle-stats>).
- **Verification:** Verified 2026-09-18 by fetching the JSON and counting it.
- **How it was counted** (so that anyone can reproduce it):
  1. `curl -sL https://app.tinytapeout.com/api/shuttles/submission-stats -o tt-stats.json`
     (fetched 2026-09-18).
  2. The JSON has two top-level keys, `shuttles` (28 objects: `id`, `slug`, `name`, `deadline`,
     `tiles_total`, `tiles_used`, `tiles_reserved`) and `submissions` (4,314 objects: `shuttle_id`,
     `project_id`, `top_module`, `tile_count`, `first_submission_time`).
  3. Submissions were grouped by `shuttle_id` and counted; distinct `project_id` values were counted
     per shuttle and overall; `tiles_used / tiles_total` was computed per shuttle.
- **What it says:**
  - **4,314 submission records in total, with 4,308 distinct `project_id` values**, across 24
    shuttles that have any submissions. The API's records begin with TT04 (deadline 2023-09-08); it
    holds nothing for TT01, TT02 or TT03.
  - **Submissions by calendar year of `first_submission_time`:** 2023 → 317; 2024 → 970;
    2025 → 1,632; 2026 → 1,395. No record lacks a timestamp. Both 2023 (the API's records start
    mid-year) and 2026 (fetched 2026-09-18) are partial years.
  - **Tile capacity used, per shuttle**, sorted by deadline (`tiles_used` / `tiles_total`, and the
    submission count):

    | Shuttle | Deadline | Tiles total | Tiles used | % used | Submissions | Distinct projects |
    |---|---|---|---|---|---|---|
    | tt04 | 2023-09-08 | 350 | 227 | 64.9% | 143 | 143 |
    | tt05 | 2023-11-04 | 380 | 283 | 74.5% | 174 | 174 |
    | tt06 | 2024-04-19 | 512 | 512 | 100.0% | 238 | 238 |
    | tt07 | 2024-06-01 | 512 | 301 | 58.8% | 119 | 119 |
    | tt08 | 2024-09-06 | 512 | 236 | 46.1% | 135 | 135 |
    | ttihp0p2 | 2024-11-04 | 240 | 240 | 100.0% | 95 | 95 |
    | tt09 | 2024-11-10 | 512 | 480 | 93.8% | 369 | 369 |
    | tt10 | 2025-03-12 | 512 | 240 | 46.9% | 112 | 112 |
    | ttihp25a | 2025-03-12 | 560 | 560 | 100.0% | 546 | 540 |
    | ttihp0p3 | 2025-05-19 | 32 | 31 | 96.9% | 23 | 23 |
    | ttcad25a | 2025-06-10 | 512 | 483 | 94.3% | 257 | 257 |
    | ttihp25b | 2025-09-01 | 240 | 176 | 73.3% | 81 | 81 |
    | ttsky25a | 2025-09-15 | 512 | 505 | 98.6% | 237 | 237 |
    | ttsky25b | 2025-11-10 | 512 | 506 | 98.8% | 316 | 316 |
    | ttgf0p2 | 2025-11-24 | 160 | 160 | 100.0% | 52 | 52 |
    | ttihp26a | 2026-03-23 | 560 | 540 | 96.4% | 283 | 283 |
    | ttihp0p4 | 2026-03-28 | 240 | 138 | 57.5% | 40 | 40 |
    | ttsky26a | 2026-05-11 | 512 | 512 | 100.0% | 289 | 289 |
    | ttsky26b | 2026-05-18 | 512 | 512 | 100.0% | 273 | 273 |
    | ttgf26b | 2026-06-22 | 160 | 155 | 96.9% | 90 | 90 |
    | ttgf26a | 2026-06-22 | 160 | 160 | 100.0% | 95 | 95 |
    | ttgf0p3 | 2026-07-03 | 160 | 115 | 71.9% | 32 | 32 |
    | ttsky26c | 2026-09-07 | 512 | 510 | 99.6% | 242 | 242 |
    | ttihp26b | 2026-09-21 | 240 | 143 | 59.6% | 73 | 73 |

    Four further shuttles (ttsky26d, ttboat26, ttgf26c, ttgf26d) had deadlines after the fetch date
    and two tiles used each.
  - **Cross-check against DEM-1.** For the 22 shuttles that appear both on the chips page and in the
    API, 20 agree exactly. Two differ by one: TTIHP25a is 547 on the page and 546 records in the API
    (540 distinct projects), and TT07 is 120 on the page and 119 in the API. Two shuttles with
    submissions in the API — `ttcad25a` (257) and `ttihp0p3` (23) — have no row in the chips-page
    table at all, and `tt10`, printed as "Cancelled" on the page, holds 112 submissions in the API.
- **Bears on:**
  - H5 (supports): demand grew from 317 submissions in the API's partial first year to 1,632 in
    2025, and **7 of the 24 runs with any submissions filled 100% of their tiles** — tt06,
    ttihp0p2, ttihp25a, ttgf0p2, ttsky26a, ttsky26b and ttgf26a.
  - H5 (**challenges**): demand is *not* uniformly ahead of supply. Once Tiny Tapeout raised
    capacity to 512 tiles, TT07 filled 58.8%, TT08 filled 46.1% and TT10 filled 46.9%. On the IHP
    process, ttihp25b filled 73.3%, ttihp0p4 57.5% and ttihp26b 59.6%. **9 of the 24 runs with any
    submissions came in below 75% of capacity** (ttgf0p3 71.9%, ttihp26b 59.6%, ttihp0p4 57.5%,
    ttihp25b 73.3%, tt10 46.9%, tt08 46.1%, tt07 58.8%, tt05 74.5%, tt04 64.9%). Capacity of this
    size is not automatically absorbed.
- **Used in:** not yet.
- **Caveats:**
  - `tiles_used` is Tiny Tapeout's own bookkeeping field; the entry takes it at face value.
  - Some runs are explicitly labelled test shuttles on the chips page ("None - test shuttle"), and a
    low fill on a test run means less.
  - A `project_id` is a project, not a person. Course and workshop submissions arrive in batches;
    ttihp25a (546 submissions closing 2025-03-28) and ttcad25a (257) look like organised group runs.
  - The API gives no price, no revenue and no information on who submitted, so it says nothing
    directly about H6.

### DEM-3. Tiny Tapeout's TT03 run was 100 new submissions plus 149 carried over from TT02

- **Source:** Tiny Tapeout, "Tiny Tapeout 3": <https://tinytapeout.com/chips/tt03/>
- **Verification:** Verified 2026-09-18.
- **What it says:**
  - Under "Launch stats": "Launched: 1 March 2023", "Submission closed: 24 April 2023", "Submitted
    to Efabless 2304C chipIgnite shuttle using Skywater 130nm open source PDK".
  - Under "Project statistics": "100 projects submitted, 149 projects added from TT02", "build time
    for all projects 22.68 hours", "total cells 79674", "94 used Wokwi, 135 Verilog, 1 myhdl, 7
    Amaranth, spade 1, xls 2, migen 1, systemverilog 3, mixed radix circuit synthesis (mrcs) 1,
    chisel 1."
- **Bears on:**
  - H5 (context): explains the unfootnoted asterisk on the TT03 row in DEM-1. The TT03 die carried
    249 projects but only 100 were new submissions, so summing the "Designs" column does not
    double-count the 149 re-runs.
  - H5 (context, weakly supporting): the language breakdown shows most submitters used a hardware
    description language rather than the graphical tool, i.e. they were not all complete beginners.
- **Used in:** not yet.
- **Caveats:** the page's "Submission closed: 24 April 2023" and the chips table's "2023-04-23"
  disagree by a day. Neither matters for the counts.

### DEM-4. The first Google-sponsored open MPW shuttle was oversubscribed, and 60% of designs came from people who were not IC designers

- **Source:** SkyWater Technology and Efabless, "First Google-Sponsored MPW Shuttle Launched at
  SkyWater with 40 Open Source Community Submitted Designs", press release dated in the text
  "BLOOMINGTON, Minn. and SAN JOSE, Calif. – April 6, 2021":
  <https://www.skywatertechnology.com/first-google-sponsored-mpw-shuttle-launched-at-skywater-with-40-open-source-community-submitted-designs/>
- **Verification:** Verified 2026-09-18, fetched and read in full.
- **What it says:**
  - "The design submission process was open for 30 days, generating 1700 downloads in the first two
    weeks and filling all 40 available slots. Additional designs will be accommodated starting in
    the next MPW shuttle run which is anticipated in mid-2021."
  - "The Open MPW Shuttle Program attracted designers from both academia and commercial
    organizations. Approximately 60% of the designs were submitted by software, FPGA and hardware
    developers (non-IC experts) — demonstrating a significant untapped underlying interest generated
    by putting IC design in the hands of users."
  - Mohamed Kassem, Efabless chief technology officer and co-founder: "We have seen fantastic
    community engagement with almost 1100 members," and "On this first MPW, this project empowered
    and enabled dozens of new designers to bring their ideas to silicon."
  - John Kent, SkyWater executive vice president of technology development and design enablement:
    "With design tools and open source design IP, engineers from around the world are collaborating
    and creating new content while accessing design and fabrication resources in a revolutionary
    way."
- **Bears on:**
  - H5 (supports): the strongest single sentence found for H5 is the press release's own —
    "demonstrating a significant untapped underlying interest generated by putting IC design in the
    hands of users" — and it is backed by the fact that the run filled and overflowed into the next.
  - H4 (supports).
- **Used in:** not yet. `OPEN-1` covers the earlier announcement of the same programme, and its
  "To find" note asked for exactly these numbers.
- **Caveats:**
  - Manufacturing was free, paid for by Google. Demand at a price of zero is an upper bound on
    demand at a price above zero, and says nothing about H6.
  - This is a vendor press release, not an independent count. It gives the accepted number (40) in
    its own headline but not the submitted number; DEM-6 supplies that (45) from Efabless's own
    programme page, and DEM-5 cross-checks the 45.
  - "60%" is stated without a method.

### DEM-5. Google's own count: "around 250" projects manufactured, and 75 submitted to MPW-5 from 19 countries

- **Source:** Johan Euphrosine, "Build Open Silicon with Google", Google Open Source Blog, dated on
  the page "Wednesday, June 1, 2022":
  <https://opensource.googleblog.com/2022/05/Build%20Open%20Silicon%20with%20Google.html>
- **Verification:** Verified 2026-09-18, fetched and read in full.
- **What it says:**
  - "Towards this goal, we've been sponsoring a series of Open MPW shuttles on the Efabless platform,
    allowing around 250 open source projects to manufacture their own silicon."
  - "With the last MPW-5 shuttle that closed up in March this year, we've seen a record level of
    engagement with 75 open silicon projects submitted for inclusion from 19 different countries."
  - "Together we've built a community of more than 3,000 members, where hardware designers and
    software developers alike, can all contribute in their own way to advance the state of the art of
    open silicon design."
  - "Each project gets a fixed 2.92mm x 3.52mm user area and 38 I/O pins in a predefined harness to
    harden their design."
  - On the kinds of design submitted: "Group submissions like the Zero to ASIC course , often
    packing as many as 14 subprojects in the shared user area".
  - "Our partner, Efabless announced that the next MPW-6 shuttle will accept open source project
    submissions until Monday, June 8, 2022."
- **Bears on:**
  - H5 (supports): submissions per shuttle rose from 45 (MPW-1, DEM-4/DEM-6) to a "record" 75 by
    MPW-5, against a fixed 40 slots — so the programme was running at roughly 1.9× oversubscription
    by its fifth run.
- **Used in:** not yet.
- **Caveats:**
  - **Conflicts with DEM-7.** Google's blog says 75 projects for MPW-5; the *Hackster.io* report of
    the very same announcement says 78. Both numbers are recorded; neither has been reconciled.
  - "around 250" is Google's own rounded figure for projects manufactured across all shuttles up to
    that date, not a filing-grade count.
  - Free manufacturing again. This is demand at price zero.

### DEM-6. Efabless's own programme page: eight shuttles, 40 slots each; MPW-1 45 designs, MPW-2 56

- **Source:** Efabless Corporation, "Efabless Open MPW Program" (`efabless.com/open_shuttle_program`),
  as archived by the Internet Archive on 2025-09-09:
  <https://web.archive.org/web/20250909130522/https://efabless.com/open_shuttle_program>
- **Verification:** Verified 2026-09-18 from the archived copy. The live page is gone — every
  Wayback capture from 2025-12-05 onwards returns 404 — because Efabless shut down (`OPEN-7`). The
  archived page's footer reads "© 2024 Efabless Corporation".
- **What it says:**
  - "Make Your Own Chips for Free" / "Design and fabricate your own open-source design for free with
    the Open MPW Program".
  - "Eight shuttles, 40 slots per shuttle, free to designers of fully open-source IC and IP designs."
  - "The shuttle provides opportunities for designers to experiment and push the state-of-the-art
    without having to reconcile the risk associated with the cost of fabrication."
  - "Costs for fabrication, packaging, evaluation boards and shipping are covered by Google for this
    program."
  - Under "Previous Shuttle Projects": "MPW-1 — 45 designs submitted in 30 days!" followed by a
    breakdown ("9 x Open processor cores", "9 x SoC's", "Crypto-currency Miner", "Robotic App
    Processor", "Amateur Satellite Radio Transceiver", "7 x Analog/RF", "5 eFPGA's"); and "MPW-2 —
    56 designs submitted in 30 days!" ("11 x Open processor cores", "11 x SoC's", "Crypto-router",
    "Time to Digital Converter - LIDAR", "Multi-project harness for Caravel", "17 x Analog/RF",
    "3 eFPGA's").
  - Of OpenLane: "It opens the door for every software developer to generate hardware representation
    without the need for details. That's at least a 1000x more potential designers!"
- **Bears on:**
  - H5 (supports): 45 and 56 designs submitted against 40 slots. Every one of MPW-1, MPW-2 and MPW-5
    (DEM-5) was oversubscribed. **DERIVED** acceptance rates, if 40 were taken each time:
    40/45 = 89%, 40/56 = 71%, 40/75 = 53%.
  - H5 (context): the programme ran eight shuttles at 40 slots — **DERIVED** 8 × 40 = 320 slots —
    which is consistent with Google's "around 250" (DEM-5) part-way through the series.
- **Used in:** not yet.
- **Caveats:**
  - The page mixes states: the schedule section still shows the MPW-6 dates ("April 11, 2022:
    Project submission is OPEN", "June 8, 2022: Project submission is CLOSED"), while the banner says
    "MPW-7 Submission Deadline is September 12". It was not kept current, so the "Eight shuttles"
    line may be a plan rather than a count of runs completed.
  - Only MPW-1 and MPW-2 submission counts are given. MPW-3, MPW-4, MPW-6, MPW-7 and MPW-8
    submission counts were **not found anywhere** — see [`search-log.md`](search-log.md).
  - Efabless is the vendor and the numbers are marketing copy.
  - "That's at least a 1000x more potential designers!" is a vendor's assertion with no method. It is
    quoted here because it is exactly the claim H5 makes, made by an interested party, and it is not
    evidence.

### DEM-7. A secondary report of the same announcement gives 78, not 75, for MPW-5

- **Source:** Gareth Halfacree, "Google Launches Open Silicon Developer Portal for Its Skywater,
  Efabless Open MPW Program", *Hackster.io*, published 2022-06-03 (page metadata
  `"datePublished":"2022-06-03T14:52:50+0000"`):
  <https://www.hackster.io/news/google-launches-open-silicon-developer-portal-for-its-skywater-efabless-open-mpw-program-31743e472cb8>
- **Verification:** Verified 2026-09-18 for the quoted text. The underlying figures are the Google
  blog's (DEM-5) and Efabless's, not independently gathered, so as evidence this is **Partial**.
- **What it says:**
  - "The first MPW shuttle saw 45 designs submitted in 30 days , of which 60 per cent came from
    first-time designers with no prior silicon tape-out experience. 40 of those were selected to form
    the first chips to come out of the program, and while issues with the toolchain meant
    difficulties getting the finished parts fully functional the program has been attracting users
    ever since with a record 78 projects submitted for the latest shuttle, MPW-5."
  - Standfirst: "Company boasts of 250 designs produced so far, but aims to get even more chip-design
    beginners on-board for free fabrication."
- **Bears on:**
  - H5 (supports): independently repeats the 45-submitted / 40-selected split, which no single
    primary page states in one sentence.
  - H5 (context): records the **disagreement with DEM-5** — 78 here against Google's own 75. We have
    not resolved it and do not pick one.
- **Used in:** not yet.
- **Caveats:**
  - Halfacree also restates the 60% figure as "first-time designers with no prior silicon tape-out
    experience", where the SkyWater press release (DEM-4) says "software, FPGA and hardware
    developers (non-IC experts)". Those are not the same claim. DEM-4's wording is the primary one.
  - "issues with the toolchain meant difficulties getting the finished parts fully functional" is
    asserted without a source, and is a real caveat on what a submission count means: a submitted
    design is not a working chip.

### DEM-8. Google capped each GlobalFoundries open shuttle at 40 projects, chosen on stated criteria

- **Source:** Ethan Mahintorabi, Johan Euphrosine and Aaron Cunningham, "Google funds open source
  silicon manufacturing shuttles for GlobalFoundries PDK", Google Open Source Blog, dated on the page
  "Monday, October 31, 2022":
  <https://opensource.googleblog.com/2022/10/announcing-globalfoundries-open-mpw-shuttle-program.html>
- **Verification:** Verified 2026-09-18, fetched and read in full. Byline as printed: "By Ethan
  Mahintorabi, Software Engineer and Johan Euphrosine, Developer Programs Engineer – Hardware
  Toolchains Team, and Aaron Cunningham, Technical Program Manager – Google Open Source Programs
  Office".
- **What it says:**
  - "Following the announcement about GlobalFoundries joining Google's open source silicon
    initiative , we are now sponsoring a series of no-cost OpenMPW shuttle runs for the GF180MCU PDK
    in the coming months."
  - "Each shuttle run will select 40 projects based on the following criteria:" — design sources
    released publicly under an open source licence; reproducible from source and the GF180MCU PDK;
    "Projects must be submitted within the shuttle deadline (projects submitted earlier get
    additional chances to be selected)"; must pass the pre-manufacturing checks.
  - "The first shuttle GF-MPW-0 will be a test shuttle, with submissions open from Oct. 31, 2022 to
    Dec. 5, 2022."
- **Bears on:**
  - H5 (context): confirms that the supply side was a hard cap of 40 per run, set by the sponsor's
    budget and not by demand. Any submission count above 40 is therefore a floor on demand, not a
    measure of it.
  - H5 (context): "projects submitted earlier get additional chances to be selected" implies the
    organisers expected to have to choose.
- **Used in:** not yet. This resolves the Lead recorded under `OPEN-2`.
- **Caveats:** the post announces a programme; it reports no submission counts. How many were
  actually submitted to the GF180MCU shuttles was **not found** — see [`search-log.md`](search-log.md).

### DEM-9. Google's own total for the SkyWater programme: 240 designs manufactured from "over 364 community submissions" across six shuttles

- **Source:** Johan Euphrosine and Ethan Mahintorabi, Hardware Toolchains Team, "SkyWater and Google
  expand open source program to new 90nm technology", Google Open Source Blog, dated on the page
  "Thursday, July 28, 2022":
  <https://opensource.googleblog.com/2022/07/SkyWater-and-Google-expand-open-source-program-to-new-90nm-technology.html>
- **Verification:** Verified 2026-09-18 by fetching the page, but through `WebFetch` rather than
  `curl`: `curl` to `opensource.googleblog.com` returned HTTP 429 (rate limited) and we backed off
  rather than retrying. The quotes are as `WebFetch` returned them from the page.
- **What it says:**
  - "Google has sponsored six shuttles on the Efabless platform, manufacturing 240 designs from over
    364 community submissions."
  - "The latest MPW-6 shuttle received 90 submissions from a diverse community across 24 different
    countries"
- **Bears on:**
  - **H5 (supports):** MPW-6's 90 submissions is the highest per-shuttle figure recorded for the
    programme, up from 45 at MPW-1 (DEM-4, DEM-6) and 75 at MPW-5 (DEM-5). Submissions grew
    monotonically across the series as far as the record goes.
  - **H5 (challenges, and this is the important reading).** Take the sentence at face value and it
    is the cleanest natural experiment available: manufacturing, the process design kit and the tool
    flow were **free**, promoted worldwide by Google, and the total global response over six
    shuttles and roughly eighteen months was **364 submissions**. If a large population of would-be
    chip designers were held back only by up-front cost, this is where it should have appeared. Four
    hundred people is a real community; it is not a market.
  - **DERIVED:** 240 manufactured ÷ 364 submitted = **66% accepted**; 364 ÷ 6 shuttles = **61
    submissions per shuttle** on average.
- **Used in:** not yet. Together with DEM-4 to DEM-8, this closes the "To find" note on `OPEN-1`.
- **Caveats:**
  - "over 364" is Google's own wording and is approximate; the "240" is likely 6 × 40 slots.
  - Selection was capped at 40 per shuttle by the sponsor (DEM-8), so 364 is a floor on interest at a
    price of zero, not a measurement of demand.
  - This counts *submissions*, not people: the same designer could submit to several shuttles, and
    the Zero to ASIC course submitted group projects "packing as many as 14 subprojects" into one
    slot (DEM-5).
  - It also says nothing about willingness to pay, which is the part H6 needs.

### DEM-10. After Efabless failed, Tiny Tapeout's industrial share rose to 38%, and its new fab partner reserves the right to delay a shuttle under 50% full

- **Source:** Nick Flaherty, "Tiny Tapeout sees industrial boost as it recovers from eFabless
  closure", *eeNews Europe*, dated on the page "May 16, 2025":
  <https://www.eenewseurope.com/en/tiny-tapeout-sees-industrial-boost-as-it-recovers-from-efabless-closure/>
- **Verification:** Verified 2026-09-18, fetched and read.
- **What it says:**
  - "The Tiny Tapeout programme is bouncing back from recent problems with a survey that shows a
    dramatic increase in industrial engagements."
  - "It had partnered with eFabless which closed in March, resulting in the the TT08 and 09 runs
    being delayed and TT10 cancelled. This hit 500 chip designs." (The doubled "the the" is in the
    source.)
  - "However Efabless founders Jeff DiCorpo and Mohammed Kassem have launched ChipFoundry.io,
    re-enabling access to the 130nm process at Skywater Technology in the US using the open source
    process development kit (PDK)."
  - "The main differences are a price increase from $10k to $15k for 100 chips, and they reserve the
    right to delay a shuttle if it's less than 50% full. 'They are going to support Tiny Tapeout, and
    we plan to open our next SKY130 shuttle in July, taping out in September. Prices are to be
    determined, but will likely be €300 for a devkit and €70 for a tile,' said Tiny Tapeout founder
    Matt Venn."
  - "A recent survey also showed more companies taking advantage of the open source programme. The
    industrial customers now represent 38%, up from 14% in 2023, with 20% from hobbyists."
- **Bears on:**
  - **H5 (supports).** A shift from 14% to 38% industrial users in two years is the single best
    indication found that low-cost shuttle demand is not purely hobbyist. Companies, not just
    enthusiasts, are using the cheapest route to silicon.
  - **H5 (challenges).** "they reserve the right to delay a shuttle if it's less than 50% full" is a
    supplier writing undersubscription risk into its terms. It corroborates the fill rates counted
    directly in DEM-2, where 9 of the 24 runs with submissions came in below 75% of capacity.
  - **H6 (context).** "a price increase from $10k to $15k for 100 chips" cross-checks the published
    chipIgnite prices in [`pricing-and-cost-to-serve.md`](pricing-and-cost-to-serve.md) (SMB-9), where
    the 2021 launch price was $9,750 and the current price is $14,950. The two agree.
- **Used in:** not yet.
- **Caveats:**
  - The 38% / 14% / 20% figures come from an unnamed "recent survey" with no published method,
    sample size or date, reported second-hand. **The survey itself was not found**; see
    [`search-log.md`](search-log.md). Treat those three percentages as **Partial** even though the
    article quoting them was read in full.
  - "This hit 500 chip designs" is the journalist's figure. Our own count from the Tiny Tapeout API
    (DEM-2) gives TT08 135 + TT09 369 + TT10 112 = 616 submissions across the three affected runs,
    or 504 for TT08 and TT09 alone — which is presumably what the 500 refers to.

### DEM-16. Europractice's annual design count, 2000–2025: a twenty-year plateau, a step up, then a decline

- **Sources:** EUROPRACTICE annual activity reports, all at `europractice-ic.com`:
  - *EP activity Report 2017*: <https://europractice-ic.com/wp-content/uploads/2019/06/EP-activity-Report-2017.pdf>
  - *Activity Report 2021*: <https://europractice-ic.com/wp-content/uploads/2022/03/europractice_ar2021_web_150dpi.pdf>
  - *Activity Report 2022*: <https://europractice-ic.com/wp-content/uploads/2023/03/2023-03-22_europractice_ar2022_web.pdf>
  - *Activity Report 2024*: <https://europractice-ic.com/wp-content/uploads/2025/10/Europractice_ActivityReport2024_webversion.pdf>
  - *Activity Report 2025*: <https://europractice-ic.com/wp-content/uploads/2026/03/Europractice_AR2025_web.pdf>
- **Verification:** **Mixed, and the entry says which part is which.**
  - **Verified 2026-09-18** by us, from the PDFs downloaded and their text layers extracted and read:
    the 2000–2017 series (the data labels on the 2017 report's chart), and the totals for 2016 (575),
    2017 (614), 2021 (985), 2022 (731), 2024 (837) and 2025 (753).
  - **Partial:** the totals for 2014 (544), 2015 (569), 2018 (624), 2019 (884), 2020 (896) and 2023
    (813). These were reported to us with quotes and document URLs, but we did not open those six
    PDFs ourselves.
- **What it says:**
  - **The series.** The 2017 report's chart, captioned "MPW designs in 2017" with the three-series
    legend "Industry + non-European univ/research / Europractice Research / Europractice Academic",
    carries data labels for every year from 2000. Read out of the PDF text, the label triplets are:
    2000 140/27/313; 2001 159/46/281; 2002 155/13/237; 2003 115/48/200; 2004 128/52/234;
    2005 138/69/243; 2006 134/84/215; 2007 154/87/298; 2008 164/85/285; 2009 153/87/305;
    2010 113/83/337; 2011 143/96/321; 2012 139/105/301; 2013 144/87/307; 2014 153/80/311;
    2015 169/72/328; 2016 145/128/301; 2017 182/109/323.
  - **DERIVED**, summing each triplet: 2000 → 480; 2001 → 486; 2002 → 405; 2003 → 363; 2004 → 414;
    2005 → 450; 2006 → 433; 2007 → 539; 2008 → 534; 2009 → 545; 2010 → 533; 2011 → 560; 2012 → 545;
    2013 → 538; 2014 → 544; 2015 → 569; 2016 → 574; 2017 → 614.
  - **Later years, from the reports' prose:** 2018 → 624; 2019 → 884; 2020 → 896; 2021 → 985;
    2022 → 731; 2023 → 813; 2024 → 837; 2025 → 753.
  - Quotes for the years we read ourselves:
    - 2017: "In 2017, a total of 614 designs have been prototyped, a significant increase compared to
      2016, when already a record-high number of 575 designs were noted. 70% of the designs are sent
      in by European universities and research institutes while the remaining 30% of the designs is
      accorded for by non-European universities (20%) and commercial companies world-wide (10%)."
    - 2021: "In 2021, EUROPRACTICE customers submitted 985 designs. We are very pleased to see that
      this is a ten-percent growth compared to the previous year, despite the supply shortages. Most
      of the designs (74%) were prototyped by European academia and industry."
    - 2024: "Our users submitted a total of 837 designs for prototyping, marking a slight
      three-percent increase compared to the previous year. … As in previous years, the majority of
      designs (78%) were submitted by European users. Within Europe, universities and research
      institutes contributed 69% of the total submissions, while the industry, primarily SMEs and
      startups, accounted for 9%."
    - 2025: "In line with this focus, 753 designs were fabricated through Europractice MPW services
      in 2025 by users from academic and research institutions worldwide. The majority came from
      Europe: 85% of all designs originated from Europractice member institutions in the EU and the
      rest of the EMEA region."
- **Bears on:**
  - **H5 (challenges, and this is the most important single series in the directory).** Europe's MPW
    broker ran between **363 and 614 designs a year for the whole of 2000 to 2017** — eighteen years,
    essentially flat, through the entire period in which design tools, IP reuse and the internet were
    supposed to be lowering the barrier to making a chip. It stepped up to 884–985 in 2019–2021 and
    has since fallen back to 753. There is no sign here of a dam waiting to burst.
  - **H5 (challenges).** The users are overwhelmingly academic. In 2024, 69% of submissions came from
    European universities and research institutes and only 9% from European industry.
  - **H5 (supports, weakly).** Demand has been *continuous* for a quarter of a century and has never
    collapsed, and the 2019–2021 step is real growth even allowing for the scope change below.
- **Used in:** not yet.
- **Caveats:**
  - **The series is not on a consistent basis, and Europractice says so itself.** The 2019 report
    reads: "In 2019, a total of 884 submitted designs have been prototyped on EUROPRACTICE MPW runs.
    This number is much higher than for previous years, since it includes MPW prototypes in TSMC
    technologies and all prototypes from MPW runs organized by CMP. Therefore, any comparison with
    previous years will be difficult." (Reported to us; **Partial**.) So the 2019 step is at least
    partly a merger of Europractice's and CMP's counts, not new demand. Likewise the 2025 fall is
    partly definitional: European SMEs and start-ups moved to a separate service, EuroCDP.
  - The chart's per-series split is inferred from the order in which the labels extract and is **not**
    certain. Only the totals should be cited. The 2016 total from the chart (574) and from the 2017
    report's prose (575) differ by one.
  - Europractice is subsidised (`SMB-6`), so this is not demand at an unsubsidised price.
  - **Europractice does not publish the number of MPW runs it offers per year** in any activity report
    we or the search covered. See [`search-log.md`](search-log.md).

### DEM-17. A Europractice stimulation programme: 98 applications, 50 designs selected

- **Source:** EUROPRACTICE, *EP activity Report 2017*, section "RESULTS — MPW PROTOTYPING SERVICE":
  <https://europractice-ic.com/wp-content/uploads/2019/06/EP-activity-Report-2017.pdf>
- **Verification:** Verified 2026-09-18 from the PDF text.
- **What it says, verbatim:** "Overall a total of 98 applications were submitted to 6 First User
  Stimulation Programmes by 73 universities from 23 countries. These design proposals were and judged
  by 5 independent expert committees and 50 designs were selected for fabrication." (The "were and
  judged" is in the source.)
- **DERIVED:** 50 ÷ 98 = a **51% acceptance rate**; 98 applications from 73 universities is 1.3
  applications per institution.
- **Bears on:**
  - **H5 (supports).** One of very few published rejection rates for a chip-fabrication programme.
    When Europractice offered subsidised first-time fabrication, twice as many applications arrived as
    there were places. That is the same shape as the Google Open MPW shuttles (DEM-4 to DEM-9):
    whenever the price approaches zero, applications exceed the slots on offer.
  - **H5 (context).** 98 applications across 23 countries is, in absolute terms, small.
- **Used in:** not yet.
- **Caveats:** a subsidised, promoted, one-off programme aimed at first-time users. Oversubscription
  at a price near zero says nothing about demand at a price that covers costs.

### DEM-18. Europractice's own price list says several TSMC shuttles are "extremely loaded" and a waiting list may be created

- **Source:** EUROPRACTICE IC Service, "Schedules & Prices 2025", TSMC sections, under "Important
  notes": <https://europractice-ic.com/schedules-prices-2025/>
- **Verification:** Verified 2026-09-18, read directly from the page text. The wording appears twice
  on the page, once in the standard TSMC block and once in the TSMC mini@sic block.
- **What it says, verbatim:** "Dates are GDS submission deadlines. Several TSMC shuttles are extremely
  loaded. For any technology, please make your design registration as early as possible. We will work
  with you and do our best to get your design on the run. If required, a waiting list will be
  created."
- **Bears on:**
  - **H5 (supports).** A live, current statement from a broker that demand for particular shuttle
    slots exceeds supply, made in the one place where saying it costs the broker something: its own
    price list.
- **Used in:** not yet.
- **Caveats:**
  - It is about **TSMC** shuttles specifically — the most advanced and most capacity-constrained
    technologies in the portfolio — not about chip fabrication generally. Contrast DEM-2, where about
    a third of Tiny Tapeout's own runs went materially undersubscribed.
  - "If required, a waiting list will be created" is conditional: it does not say one exists.
  - No numbers.

### DEM-19. CMP (Grenoble) fabricated 100–400 circuits a year for thirty years, and no more

- **Source:** CMP (Circuits Multi-Projets), *CMP Annual Report 2011*, history section, report
  pp. 11–14. CMP's own site is gone (see caveats); read from the Internet Archive:
  <https://web.archive.org/web/20210404130708if_/https://mycmp.fr/IMG/pdf/cmp_annual-report-2011_full_version.pdf>
- **Verification:** Verified 2026-09-18 from the archived PDF, text extracted and read. (`WebFetch`
  refuses `web.archive.org` outright, so the Wayback work was done with `curl` and the `if_`/`id_`
  raw-content forms.)
- **What it says** — quoted from the report's year-by-year history, with the spacing artefacts of the
  PDF's text layer closed up:
  - 1993: "25 runs have been organized… Nearly 200 circuits coming from 55 Institutions were
    fabricated"
  - 1994: "In total 32 runs gathered 251 circuits, from 75 Institutions"
  - 1995: "95 Institutions (Universities, Research Laboratories and Industrial Companies) submitted
    298 circuits for education, research and industrial purposes. … In total 34 runs totalizing
    3817 mm 2 took place."
  - 1996: "a total of 107 Institutions … submitted 354 circuits"
  - 1998: "a total of 90 Institutions … submitted 259 circuits"
  - 2006: "a total of 329 circuits … for 93 organizations … (22 countries). Compared to 2005 the
    number of circuits increased by 25%."
  - 2007: "a total of 401 circuits were fabricated for 105 organizations (Universities, Research
    Laboratories and Industrial Companies) all over the world (23 countries). Compared to 2006 the
    number of circuits increased by 22% and the number of participants increased by 13%."
  - 2008: "a total of 375 circuits were fabricated for 89 organizations"
  - 2009: "a total of 391 circuits were fabricated for 104 organizations"
  - 2010: "a total of 354 circuits were fabricated for 122 Universities, Research Laboratories and
    Companies from 23 countries."
  - 2011: "a total of 273 circuits were fabricated for 96 Universities, Research Laboratories and
    Companies from 19 countries."
- **Bears on:**
  - **H5 (challenges).** France's national MPW service peaked at 401 circuits a year in 2007 and was
    back to 273 by 2011. Thirty years of continuous operation produced a service that never exceeded
    about 400 designs a year from about 100 institutions.
  - **H5 (context).** CMP published the run count where most services do not: 25 runs (1993), 32
    (1994), 34 (1995) — roughly 8 to 10 circuits per run.
- **Used in:** not yet.
- **Caveats:**
  - **CMP no longer exists as an operating service.** Its domain `mycmp.fr` now resolves to a
    domain-parking page and `cmp.imag.fr` is dead. The Europractice 2022 activity report (verified for
    DEM-20) records that CMP "had to stop fabrication activities at STMicroelectronics, ams and
    CEA-Leti due to administrative reasons" and that "a new French MPW service, CIME-P, was created in
    October 2022 and joined the consortium". That is a supply-side failure, not a demand one, but it
    removed a thirty-year-old MPW service from Europe.
  - The counts are CMP's own, in a promotional annual report, and the wording alternates between
    "submitted" and "fabricated" from year to year.
  - A 2015 figure — "A total of 265 circuits were fabricated for 90 Institutions, Research
    Laboratories and Companies from 25 countries" — was reported to us from
    <https://web.archive.org/web/20210404130708if_/https://mycmp.fr/IMG/pdf/cmp_annual-report-2015_full_version.pdf>
    but we did not open that PDF: **Partial**.
  - CMP's cumulative counters are internally inconsistent about runs — "1029 runs" (2017 web
    snapshot), "1043 MPW runs" (2019 snapshot), "1142 manufacturing runs" (2021, via a conference
    company profile). Fourteen runs in twenty-seven months followed by ninety-nine in eighteen months
    is not a credible run rate; either the definition changed or a counter was stale. All three are
    **Partial** — reported to us from archived pages we did not open — and no run-rate argument should
    be built on them.
