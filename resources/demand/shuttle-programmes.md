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
    2025, and eight of the twenty-four closed runs filled 100% of their tiles.
  - H5 (**challenges**): demand is *not* uniformly ahead of supply. Once Tiny Tapeout raised
    capacity to 512 tiles, TT07 filled 58.8%, TT08 filled 46.1% and TT10 filled 46.9%. On the IHP
    process, ttihp25b filled 73.3%, ttihp0p4 57.5% and ttihp26b 59.6%. Roughly a third of runs went
    materially undersubscribed. Capacity of this size is not automatically absorbed.
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
    directly in DEM-2, where about a third of runs came in well below capacity.
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
