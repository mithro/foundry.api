# Open programme growth (`OPG`)

Evidence on how many people submitted a design to an *open-PDK* shuttle programme, per run, over
time, and at what price. It extends [`shuttle-programmes.md`](shuttle-programmes.md) (`DEM-1`…`DEM-10`
cover Tiny Tapeout and the Google Open MPW shuttles) in four directions the repository did not have:

1. **The whole Efabless series, not the part Google published.** `DEM-9` records Google's own
   "over 364 community submissions" across six shuttles. That was the count as of 2022-07-28. Two
   more SkyWater shuttles and two GlobalFoundries shuttles followed. The series does not end at 364.
2. **The paid series.** chipIgnite was Efabless's commercial shuttle at a published fixed price,
   with no external funding behind it. It is the closest thing in the record to demand at a price
   that covers costs, which is what H6 needs and H5's free-shuttle evidence cannot supply.
3. **Successors.** ChipFoundry, IHP and wafer.space are running open-PDK shuttles now, and two of
   them publish live demand data.
4. **Paying customers counted individually.** Crowd Supply campaigns give backer counts for
   open-silicon hardware — including the ones that failed.

**A warning that applies to every series in this file.** Efabless shut down in early 2025
(`OPEN-7`). The Google Open MPW and chipIgnite series both stop there. They stop because the
operator died, not because demand fell: the last chipIgnite shuttle to close, CI 2411, was the
second-largest the programme ever ran, and a further shuttle (CI 2504) was open and taking
submissions when the company went under. **A series that ends because its operator failed is not a
series that declined.** `OPG-3`, `OPG-7` and `OPG-15` each say this again where the numbers are.

The deep dive that reads these entries together — including why the subsidised open programme grew
while the older subsidised programmes did not — is
[`efabless-and-the-open-shuttles.md`](efabless-and-the-open-shuttles.md).

---

### OPG-1. The complete Efabless shuttle table: 23 shuttles, 1,584 submissions against 726 slots

- **Source:** a spreadsheet of every Efabless-run shuttle, supplied by the repository owner and
  published read-only as CSV:
  <https://docs.google.com/spreadsheets/d/1rfEuEqolkQVyqDWOkrZNRI2C1IuSfmDA34QAcTb0V4I/export?format=csv&gid=2074606292>
  Columns: `Order, Date, Process, Name, URL, Manufactured` (slots), `Count` (submissions),
  `Participants` (distinct people), `Projects`, `New Users`.
- **Verification:** **Owner-supplied**, with the arithmetic **Verified 2026-09-18** — the CSV was
  downloaded and every total below was recomputed from it, not taken on trust. The *figures
  themselves* are the owner's compilation; they are not a published Efabless document. But eighteen
  of the twenty-three rows can be checked against Efabless's own platform pages in the Internet
  Archive, and `OPG-2` does exactly that.
- **How it was counted** (reproducible): `curl -sL "<the URL above>" -o shuttles.csv`, then a Python
  script that reads the 23 data rows (those with a non-empty `Order`), groups them by programme, and
  sums `Count`, `Manufactured` and `New Users`. The summary blocks lower down the same sheet were
  **not** used; see the caveats, they disagree with the row data.
- **What it says:**

  | # | Date (sheet) | Process | Shuttle | Slots | Submissions | Participants | Projects | New users |
  |---|---|---|---|---|---|---|---|---|
  | 1 | 2020-11-12 | SKY130 | MPW-1 | 40 | 37 | 32 | 37 | 0 |
  | 2 | 2021-06-18 | SKY130 | MPW-2 | 40 | 57 | 54 | 56 | 0 |
  | 3 | 2021-11-15 | SKY130 | MPW-3 | 40 | 53 | 45 | 53 | 23 |
  | 11 | 2021-11-26 | SKY130 | CI 2110C | 13 | 28 | 24 | 28 | 8 |
  | 4 | 2021-12-31 | SKY130 | MPW-4 | 40 | 52 | 47 | 52 | 12 |
  | 5 | 2022-03-21 | SKY130 | MPW-5 | 40 | 75 | 64 | 74 | 28 |
  | 12 | 2022-04-08 | SKY130 | CI 2204C | 16 | 13 | 11 | 13 | 6 |
  | 6 | 2022-04-11 | SKY130 | MPW-6 | 40 | 90 | 74 | 85 | 37 |
  | 13 | 2022-06-17 | SKY130 | CI 2206Q | 14 | 53 | 40 | 53 | 27 |
  | 14 | *(blank)* | SKY130 | CI 2209C | 8 | 8 | 8 | 8 | 3 |
  | 7 | 2022-07-08 | SKY130 | MPW-7 | 40 | 106 | 88 | 106 | 38 |
  | 8 | 2022-10-31 | GF180MCU | MPW-0 | 40 | 88 | 65 | 86 | 31 |
  | 9 | 2022-11-19 | SKY130 | MPW-8 | 40 | 147 | 94 | 144 | 43 |
  | 15 | 2022-12-05 | SKY130 | CI 2211Q | 22 | 59 | 40 | 59 | 20 |
  | 16 | 2023-04-24 | SKY130 | CI 2304C | 19 | 27 | 20 | 27 | 6 |
  | 17 | 2023-06-05 | SKY130 | CI 2306Q | 21 | 49 | 40 | 49 | 13 |
  | 18 | 2023-09-11 | SKY130 | CI 2309 | 20 | 49 | 35 | 47 | 9 |
  | 10 | 2023-10-28 | GF180MCU | MPW-1 | 40 | 116 | 95 | 114 | 40 |
  | 19 | 2023-11-15 | SKY130 | CI 2311 | 33 | 100 | 82 | 100 | 38 |
  | 20 | *(blank)* | SKY130 | CI 2404 | 40 | 109 | 83 | 109 | 49 |
  | 21 | *(blank)* | SKY130 | CI 2406 | 40 | 76 | 57 | 76 | 23 |
  | 22 | *(blank)* | SKY130 | CI 2409 | 40 | 73 | 59 | 73 | 29 |
  | 23 | *(blank)* | SKY130 | CI 2411 | 40 | 119 | 75 | 119 | 41 |

  All **DERIVED**, with the arithmetic written out:

  - **Google Open MPW on SKY130, MPW-1…MPW-8: 617 submissions against 320 slots = 1.93×.**
    37 + 57 + 53 + 52 + 75 + 90 + 106 + 147 = 617. 8 × 40 = 320. 617 ÷ 320 = 1.9281.
  - **Cumulative SKY130 submissions by shuttle:** 37, 94, 147, 199, 274, **364**, 470, 617.
    **The 364 is the figure Google published** (`DEM-9`, "over 364 community submissions" across six
    shuttles) and it is the figure `DEM-9` currently treats as the programme's total. It is the
    running total through MPW-6 and nothing more. MPW-7 (106) and MPW-8 (147) followed, and 253 of
    the programme's 617 SkyWater submissions — **41%** — arrived after the number Google published.
  - **Google Open MPW on GF180MCU, MPW-0 and MPW-1: 204 submissions against 80 slots = 2.55×.**
    88 + 116 = 204. 2 × 40 = 80. 204 ÷ 80 = 2.55.
  - **Google programme total: 821 submissions across 10 shuttles against 400 slots = 2.05×.**
    617 + 204 = 821. 320 + 80 = 400. 821 ÷ 400 = 2.0525.
  - **chipIgnite: 763 submissions across 13 shuttles against 326 slots = 2.34×.**
    28 + 13 + 53 + 8 + 59 + 27 + 49 + 49 + 100 + 109 + 76 + 73 + 119 = 763.
    13 + 16 + 14 + 8 + 22 + 19 + 21 + 20 + 33 + 40 + 40 + 40 + 40 = 326. 763 ÷ 326 = 2.3405.
    Excluding CI 2209C (see caveats): 755 ÷ 318 = 2.3742.
  - **chipIgnite submissions by calendar year**, taking the year from the shuttle's own `YYMM` name
    code: 2021 → **28**; 2022 → **133** (13 + 53 + 8 + 59); 2023 → **225** (27 + 49 + 49 + 100);
    2024 → **377** (109 + 76 + 73 + 119). Year on year: 133 ÷ 28 = 4.75×, 225 ÷ 133 = 1.69×,
    377 ÷ 225 = 1.68×. Excluding CI 2209C, 2022 is 125 and the ratios are 4.46×, 1.80×, 1.68×.
    **Roughly 1.7× a year, twice in a row, in the paid programme.**
  - **New users.** Google: 252 of 821 = **30.7%** new
    (0+0+23+12+28+37+38+31+43+40 = 252; 252 ÷ 821 = 0.3069). chipIgnite: 272 of 763 = **35.6%** new
    (8+6+27+3+20+6+13+9+38+49+23+29+41 = 272; 272 ÷ 763 = 0.3565). **So about two-thirds of all
    submissions — 69.3% for Google, 64.4% for chipIgnite — came from people who had submitted
    before.**
  - **Everything together:** 1,584 submissions, 726 slots, 2.18× (1584 ÷ 726 = 2.1818); 524 new
    users, 33.1% (524 ÷ 1584 = 0.3308).
- **Bears on:**
  - **H5 (supports).** Every programme total is more than 2× the slots offered, and the paid
    programme is *more* oversubscribed (2.34×) than the free one (2.05×).
  - **H5 (supports).** chipIgnite grew 1.7× a year for two consecutive years at a fixed $9,750–$14,950
    price with no external funding (`OPG-8`), and was still at a record when the company died
    (`OPG-7`).
  - **H5 (challenges, and this is the important reading of the same table).** Two-thirds of
    submissions came from returning users. The **Participants** column, summed, is 1,232 across 23
    shuttles — and those are not distinct people either, because the same person recurs across
    shuttles. The base is much narrower than the submission count suggests. A programme where a third
    of submissions are new is growing; it is not evidence of a large untapped population arriving.
  - **H6 (context).** The sheet has no revenue, no cost and no margin. It says how many people
    bought; it says nothing about whether selling to them paid.
- **Used in:** not yet.
- **Caveats — three known problems with the sheet, all stated honestly:**
  - **CI 2209C.** The sheet's own chipIgnite total (755) *excludes* the CI 2209C row, which carries
    8 submissions and 8 slots. The repository owner believes **CI 2209C was cancelled or
    rescheduled**; that is **unconfirmed** and we could not confirm it. Efabless's own platform
    listed a shuttle page for it (`OPG-3`) and the 2110C schedule table gave it a tapeout date of
    "September 19, 2022", but **no Internet Archive capture of that page exists** (the CDX API
    returns nothing for `platform.efabless.com/shuttles/2309C` or `…/2209C` on any date), so its
    final state is unverifiable. Both totals are given above.
  - **CI 2311 is listed twice, under two different processes.** In one of the sheet's summary tables
    CI 2311's 100 submissions sit in the SKY130 column and in another they sit in the chipIgnite
    column. This is a presentation error in the summary blocks, not a data error: **all chipIgnite
    shuttles were on SKY130**, and Efabless's own platform navigation lists CI 2311 under
    "chipIgnite Projects" (`OPG-3`). Treat it as chipIgnite.
  - **The sheet's own summary blocks are stale and should not be cited.** "ChipIgnite Manufactured
    158" is the slot total for CI 2110C through CI 2311 only (13+16+14+22+19+21+20+33 = 158); it
    omits the four 2024 shuttles (4 × 40 = 160) and CI 2209C. Recompute from the rows, as above.
  - Six rows have a blank `Date`. For CI 2404, CI 2406, CI 2409 and CI 2411 the tapeout dates are
    recoverable from the archived platform pages (2024-04-24, 2024-06-03, 2024-09-16, 2024-11-11);
    CI 2209C's is from the schedule table on the 2110C page (2022-09-19).
  - The `Date` column is the shuttle's **opening** date, not its close: MPW-1 is dated 2020-11-12,
    the day of the SkyWater announcement (`OPEN-1`), while the archived MPW-1 page gives
    "Open Nov 12, 2020".
  - **The sheet omits two chipIgnite shuttles that existed.** See `OPG-3`.

### OPG-2. Efabless's own platform printed an oversubscription percentage for every shuttle, and the Internet Archive kept it

- **Source:** Efabless's shuttle pages on `platform.efabless.com`, as archived by the Internet
  Archive. The live platform is gone (`OPEN-7`); captures from 2025-12-05 onwards return 404, and
  the late captures of the `?active_tab=summary` form return 503. The raw-content (`id_`) form of an
  earlier capture works. Examples:
  - MPW-8: <https://web.archive.org/web/20240613104249id_/https://platform.efabless.com/shuttles/MPW-8>
  - MPW-7: <https://web.archive.org/web/20221204010751id_/https://platform.efabless.com/shuttles/MPW-7>
  - GF MPW-1: <https://web.archive.org/web/20240227030244id_/https://platform.efabless.com/shuttles/GFMPW-1>
  - CI 2411: <https://web.archive.org/web/20250124154327id_/https://platform.efabless.com/shuttles/CI%202411>
- **Verification:** **Verified 2026-09-18.** Eighteen archived shuttle pages were fetched and their
  statistics blocks read directly. This is the strongest independent check on `OPG-1` available,
  because it is Efabless's own platform rather than anyone's compilation of it.
- **How it was done** (reproducible):
  1. `curl -s "https://web.archive.org/cdx/search/cdx?url=platform.efabless.com/shuttles*&output=text&limit=300&collapse=urlkey&fl=timestamp,original,statuscode"`
     lists every archived shuttle URL. 44 rows come back.
  2. For each shuttle, pick a capture **after** the tapeout date (the page's own "Tapeout:" line
     gives it) and fetch
     `https://web.archive.org/web/<timestamp>id_/<url>`. A capture taken during the submission
     window shows a partial count and must not be used — see the caveats, this matters a great deal.
  3. Strip tags and read the block that begins `Participants`. Every page prints, in order:
     participants, new users, projects, categories, and then `Capacity`, `N / 40`, a percentage, and
     the literal word `Oversubscribed` or `Undersubscribed`.
- **What it says.** Efabless's own final figures, and the sheet's, side by side:

  | Shuttle | sheet `Count` | sheet `Projects` | page `Projects` | page `Participants` (sheet) | page new users (sheet) | page capacity | page label |
  |---|---|---|---|---|---|---|---|
  | MPW-1 | 37 | 37 | **37** | 32 (32) | 0 (0) | 37/40 = 92.0% | Undersubscribed |
  | MPW-2 | 57 | 56 | 57 | 55 (54) | 0 (0) | 57/40 = 142.0% | Oversubscribed |
  | MPW-3 | 53 | 53 | **53** | 45 (45) | 23 (23) | 53/40 = 132.0% | Oversubscribed |
  | MPW-4 | 52 | 52 | **52** | 47 (47) | 12 (12) | 52/40 = 130.0% | Oversubscribed |
  | MPW-5 | 75 | 74 | 76 | 66 (64) | 29 (28) | 76/40 = 190.0% | Oversubscribed |
  | MPW-6 | 90 | 85 | 86 | 75 (74) | 37 (37) | 86/40 = 215.0% | Oversubscribed |
  | MPW-7 | 106 | 106 | 110 | 90 (88) | 38 (38) | 110/40 = 275.0% | Oversubscribed |
  | MPW-8 | 147 | 144 | **144** | 94 (94) | 43 (43) | 144/40 = 360.0% | Oversubscribed |
  | GF MPW-0 | 88 | 86 | **86** | 65 (65) | 31 (31) | 86/40 = 215.0% | Oversubscribed |
  | GF MPW-1 | 116 | 114 | 116 | 97 (95) | 41 (40) | 116/40 = 290.0% | Oversubscribed |
  | CI 2110C | 28 | 28 | **28** | 24 (24) | 8 (8) | 28/40 = 70.0% | **Undersubscribed** |
  | CI 2204C | 13 | 13 | **13** | 11 (11) | 6 (6) | 13/40 = 32.0% | **Undersubscribed** |
  | CI 2206Q | 53 | 53 | **53** | 40 (40) | 27 (27) | 53/40 = 132.0% | Oversubscribed |
  | CI 2309 | 49 | 47 | 48 | 36 (35) | 9 (9) | 48/40 = 120.0% | Oversubscribed |
  | CI 2404 | 109 | 109 | **109** | 83 (83) | 49 (49) | 109/40 = 272.0% | Oversubscribed |
  | CI 2406 | 76 | 76 | 78 | 58 (57) | 23 (23) | 78/40 = 195.0% | Oversubscribed |
  | CI 2409 | 73 | 73 | 70 | 53 (59) | 25 (29) | 70/40 = 175.0% | Oversubscribed |
  | CI 2411 | 119 | 119 | **119** | 75 (75) | 41 (41) | 119/40 = 298.0% | Oversubscribed |

  **Agreement, DERIVED by counting the table:** of the 18 shuttles checked, the archived page's
  `Projects` figure matches the sheet's `Projects` column **exactly for 10**; `Participants` matches
  exactly for 10; `New Users` matches exactly for **15**. Of the eight that differ on `Projects`,
  seven differ by +1, +2 or +4 in the page's favour and one (CI 2409) by −3.
  **The two sources agree.** The residual differences are consistent with the two being snapshots of
  a live database taken at different moments — projects were still being added, withdrawn or made
  public after tapeout — and no difference is large enough to change any conclusion.

  Verbatim examples of what the page prints, for the record:
  - MPW-7: `Participants 90 + 38 New Users`, `Projects 110`, `50 Categories`,
    `Capacity 110 / 40 275.0 % Oversubscribed`.
  - MPW-8: `Participants 94 + 43 New Users`, `Projects 144`, `Capacity 144 / 40 360.0 % Oversubscribed`.
  - CI 2204C: `Participants 11 + 6 New Users`, `Projects 13`, `Capacity 13 / 40 32.0 % Undersubscribed`.
- **Bears on:**
  - **H5 (supports).** The operator's own platform labelled sixteen of these eighteen runs
    **Oversubscribed**, in its own words, on its own page, computed by its own software. MPW-8 at
    360% and CI 2411 at 298% are the two largest.
  - **H5 (supports).** It independently confirms the part of `OPG-1` that matters most: the series
    did not end at 364. MPW-7 (110) and MPW-8 (144) are on Efabless's own pages.
  - **H5 (challenges).** It also confirms the two chipIgnite runs that **failed to fill**: CI 2110C
    at 70% and CI 2204C at 32%, both labelled `Undersubscribed` by the platform itself, both final
    (the captures are 2022-12-06 and 2023-11-14, long after their 2021-11-26 and 2022-04-08
    tapeouts). And the very first Google shuttle, MPW-1, came in at 92% — under its 40 slots. The
    paid programme's first two commercial runs did not fill. `OPG-7` reads this as the start of a
    curve, but it is a real hole in any story that says demand was always ahead of supply.
- **Used in:** not yet. It gives `DEM-6` the MPW-3 to MPW-8 submission counts its "not found
  anywhere" note asked for, and `DEM-8` the GF180MCU counts its "not found" note asked for.
- **Caveats:**
  - **The biggest trap in this source: a capture taken while the shuttle was open shows a partial
    count, and the page still prints the word `Undersubscribed`.** Worked examples, all read:
    MPW-8 on 2022-11-21, two days after opening, prints `6 / 40 15.0 % Undersubscribed` — the same
    shuttle finished at 144. GF MPW-0 on 2022-11-15 prints `4 / 40 10.0 % Undersubscribed` and
    finished at 86. CI 2406 on 2024-04-13 prints `9 / 40 22.0 %` and finished at 78. **Anyone
    quoting a percentage from one of these pages must state the capture date and show it is after
    the tapeout date.**
  - `N / 40` uses a nominal 40-slot shuttle throughout, including for the early chipIgnite runs
    whose actual reserved slots were 13, 16, 14 and so on. The chipIgnite pages print the real
    number separately: CI 2110C says "13 of 40 project slots reserved", CI 2204C "16 of 40".
  - `Projects` is the count of *public* project pages on the platform, which is why it drifts from
    the sheet's `Count`. Neither is a count of people.
  - These are the vendor's own numbers. `OPG-2` is an independent check on `OPG-1`'s
    *transcription*, not an independent measurement of demand.
  - CI 2304C, CI 2306Q, CI 2311 and CI 2209C have **no Internet Archive captures at all** — the CDX
    API returns an empty result for each. Their rows in `OPG-1` are unchecked.

### OPG-3. The spreadsheet omits two chipIgnite shuttles, and one of them was open when the company died

- **Source:** archived Efabless platform pages.
  - CI 2106Q: <https://web.archive.org/web/20240421145959id_/https://platform.efabless.com/shuttles/2106Q>
  - CI 2504: <https://web.archive.org/web/20250125035816id_/https://platform.efabless.com/shuttles/CI%202504>
- **Verification:** **Verified 2026-09-18**, both pages fetched and read.
- **What it says:**
  - **CI 2106Q** is the *first* chipIgnite shuttle and it is not in the spreadsheet, whose chipIgnite
    series starts at CI 2110C. The page header reads `2106Q` / `chipIgnite Shuttle Service`, the body
    `19 of 40 project slots reserved`, `Tapeout: Jun 18, 2021`, `Delivery: Oct 06, 2021`, and the
    statistics block `Participants 22 | 0 New Users | Projects 23 | Capacity 23 / 40 | 57.0 % |
    Undersubscribed`. The capture is 2024-04-21, three years after tapeout, so 23 is final.
  - **CI 2504** is the shuttle that was open when Efabless failed, and it is not in the spreadsheet
    either. The page reads `CI 2504` / `chipIgnite Shuttle Service`, `Tapeout: Apr 21, 2025 at 11:59
    PT`, `Delivery: Sep 2025`, `Status Open`, and `Participants 20 | + 14 New Users | Projects 20 |
    14 from new users | Capacity 20 / 40 | 50.0 % | Undersubscribed`. The capture is **2025-01-25**,
    about six weeks after the shuttle opened on 2024-12-13 and about five weeks before the shutdown.
    **Twenty projects, fourteen of them from people who had never submitted to Efabless before, had
    already arrived on a shuttle that still had three months to run.**
  - The CI 2504 page's own left-hand navigation lists the complete chipIgnite series as Efabless
    itself grouped it: `2106Q, 2110C, 2204C, 2206Q, 2209C, 2211Q, 2304C, 2306Q, CI 2309, CI 2311,
    CI 2404, CI 2406, CI 2409, CI 2411` under the heading "chipIgnite Projects", and `GFMPW-0,
    GFMPW-1, MPW-1 … MPW-8` under "Open MPW Projects". **CI 2311 is in the chipIgnite group**, which
    settles the sheet's double-listing of it. **CI 2209C has a page**, which shows it was at least
    set up, though it says nothing about whether it ran.
- **DERIVED:** adding CI 2106Q to `OPG-1`'s chipIgnite totals and keeping CI 2209C out gives
  **778 submissions across 13 shuttles against 337 slots = 2.31×** (755 + 23 = 778;
  318 + 19 = 337; 778 ÷ 337 = 2.3086), and makes 2021 **51** submissions rather than 28
  (23 + 28), so the 2021→2022 step becomes 125 ÷ 51 = **2.45×** rather than 4.46×.
- **Bears on:**
  - **H5 (context, and a correction).** The chipIgnite series is 15 shuttles, not 13 — and its first
    run, like its second and third, did not fill. A cleaner statement of the paid programme's
    history is: *three undersubscribed runs, then ten oversubscribed ones, then death.*
  - **H5 (supports) and the truncation point.** CI 2504 is the single clearest piece of evidence that
    the series was cut off rather than exhausted. Twenty paid projects with fourteen new customers,
    a quarter of the way through the window, on a shuttle that never taped out.
- **Used in:** not yet.
- **Caveats:**
  - CI 2106Q's final figure is 23 projects against a *nominal* 40 but only **19 slots reserved**, so
    whether it was "undersubscribed" depends which denominator you use. The platform used 40.
  - CI 2504's 20 is a snapshot on an open shuttle and would have grown. It is a floor, not a total.
  - We do not know what happened to CI 2504's customers. We did not find any public statement about
    refunds or roll-overs.

### OPG-4. Where Google's published numbers and the spreadsheet agree, and where they do not

- **Sources:** the two Google Open Source Blog posts already recorded as `DEM-5` and `DEM-9`, and
  the Efabless programme page recorded as `DEM-6`, compared against `OPG-1` and `OPG-2`.
- **Verification:** **Partial.** The Google and Efabless pages were verified for `DEM-5`, `DEM-6` and
  `DEM-9` by the author of those entries; what is verified here, on 2026-09-18, is the *comparison*
  and the arithmetic.
- **What it says:**

  | Claim | Published figure | Spreadsheet | Archived Efabless page | Agree? |
  |---|---|---|---|---|
  | MPW-5 submissions | 75 (`DEM-5`, Google) | 75 | 76 | **yes** |
  | MPW-6 submissions | 90 (`DEM-9`, Google) | 90 | 86 | **yes** (sheet), near (page) |
  | Cumulative through six shuttles | "over 364" (`DEM-9`) | **364** exactly | — | **yes, exactly** |
  | Designs manufactured, six shuttles | 240 (`DEM-9`) | 6 × 40 = 240 | — | **yes** |
  | MPW-1 submissions | **45** (`DEM-6`, Efabless; `DEM-7`, Hackster; and Google's own slides, `OPG-5`) | **37** | **37** | **no** |
  | MPW-2 submissions | 56 (`DEM-6`, Efabless) | 57 (`Projects` 56) | 57 | **yes**, on `Projects` |
  | MPW-5 submissions | 78 (`DEM-7`, Hackster) | 75 | 76 | **no** |

- **Bears on:**
  - **H5 (supports).** The cumulative-through-MPW-6 figure lands on Google's published 364 exactly,
    from a source that had no reason to be reverse-engineered to it. That is a strong sign the
    spreadsheet is a faithful extract of the platform database, and therefore that the 617 and 821
    totals in `OPG-1` can be relied on.
  - **H5 (context).** The **MPW-1 disagreement is real and unresolved**: 45 appears in Efabless's own
    marketing (`DEM-6`), in Hackster (`DEM-7`) *and* in Google's own conference slides (`OPG-5`),
    while 37 appears in the spreadsheet *and* on Efabless's own platform page. Both numbers are
    recorded. We have not reconciled them and do not pick one. The most likely explanation — and it
    is **our conjecture, not anyone's statement** — is that 45 counts submissions received and 37
    counts project records that survived on the platform, but nothing we read says so.
- **Used in:** not yet.
- **Caveats:** every figure on both sides of this comparison originates with Efabless or with
  Google-reporting-Efabless. It is a consistency check between two views of one vendor's database,
  not corroboration by an unrelated party. No unrelated party ever counted these shuttles.

### OPG-5. Google's own slides: "No NDA required, just clone", MPW-1 at 45 designs, and how much of a shuttle a single course occupied

- **Source:** Aaron Cunningham (Google), "Open source silicon ecosystem — New shuttles, PDK releases,
  and tools", slide deck presented at RISC-V Days Tokyo Autumn 2022, hosted by the RISC-V
  Association of Japan:
  <https://riscv.or.jp/wp-content/uploads/DAY1_Aaron_Google_RISC-V_Tokyo_Autumn_2022-Aaron_Slides_cp.pdf>
  (title slide byline: "Aaron Cunningham aacunningham@google.com").
- **Verification:** **Verified 2026-09-18.** PDF downloaded with `curl` and its text layer extracted
  and read (34 pages).
- **What it says**, quoted from the slides' text layer:
  - Slide 14, on the SkyWater PDK: "github.com/google/skywater-pdk **Open source, manufacturable
    130nm PDK No NDA required, just clone.** June 2020"
  - Slide 17: "Silicon Realization Program SKY130 'Open MPW Shuttle Program' is managed by efabless,
    sponsored by Google and manufactured by SkyWater."
  - Slide 18: "Silicon Realization Program No cost Open source design Reproducible User Project Area
    RISC-V Management Area"
  - Slide 19, on MPW-1: "MPW-ONE Manufacturing Test Area Manufacturing Test Area Experienced
    **45 designs in 30 days 60% by first time designers**"
  - Slide 22: "**Group submissions up to 16 projects in 1 slot MPW1: 8 MPW2: 9 MPW3: 16 MPW4: 13
    MPW5: 15 MPW6: 14** zerotoasiccourse.com github.com/mattvenn/multi_project_tools"
  - Slide 23: "**TinyTapeout 152 projects in 1 slot Submitted to MPW-7** tinytapeout.com"
  - Slide 24, on Japanese submissions: "MPW3: １ Jacaranda-8 (8-bit ISA) MPW5: １ PMU MPW6: 5 Marmot:
    Linux capable RISC-V SoC NNgen ML accelerator Ramen Timer HP35 RTL clone Color convertor"
  - Slide 33, the intended funnel: "Community ↓ Group submission ↓ Open MPW shuttles ↓ Private
    shuttles ↓ Full wafer ↓ Industry"
- **Bears on:**
  - **H4 and H5 (supports), and this is the cleanest sentence in the repository for the NDA
    question.** "No NDA required, just clone" is the sponsor's own one-line statement of what was
    different about this PDK. Every competing programme in `OPG-8`'s comparison requires an NDA.
  - **H5 (challenges, and it cuts hard).** Slide 22 says a single course — the Zero to ASIC course —
    packed 8, 9, 16, 13, 15 and 14 projects into **one slot** on MPW-1 through MPW-6. Slide 23 says
    Tiny Tapeout packed **152 projects into one slot** on MPW-7. So (a) a large share of the
    "designs" attributed to these shuttles were sub-tiles inside a single submission, not
    independent customers, and (b) the reverse also holds — an entire course of sixteen people
    counted as one submission. **The relationship between "submissions", "designs" and "people" in
    every one of these series is loose in both directions, and nobody publishes a reconciliation.**
    This is the strongest single caution against reading `DEM-1`'s 4,268 Tiny Tapeout designs or
    `OPG-1`'s 1,584 submissions as 4,268 or 1,584 customers.
  - **H5 (context).** Slide 24 shows what a national share looked like: Japan contributed 1, 1 and 5
    designs to MPW-3, MPW-5 and MPW-6. Against a global total in the dozens per shuttle, that is
    what "worldwide" meant in practice.
- **Used in:** not yet.
- **Caveats:**
  - Slide text extracted from a PDF loses layout; the groupings above are as the text layer orders
    them and the association of a number to a label was checked by eye but is not typographically
    guaranteed.
  - The deck is Google's, promoting Google's programme.
  - It gives 45 for MPW-1, which disagrees with the spreadsheet's and the platform's 37 (`OPG-4`).
  - It is dated autumn 2022 and so predates MPW-8, both GF180MCU shuttles, and all but the first
    four chipIgnite runs.

### OPG-6. Efabless's own press release, April 2024: "1300 designs and six hundred tapeouts"

- **Source:** Efabless Corporation, "Efabless Announces the Launch of the Tiny ML on Tiny Tapeout
  Contest", GlobeNewswire, dated in the text "PALO ALTO, Calif., April 23, 2024 (GLOBE NEWSWIRE)":
  <https://www.globenewswire.com/news-release/2024/04/23/2868104/0/en/Efabless-Announces-the-Launch-of-the-Tiny-ML-on-Tiny-Tapeout-Contest.html>
- **Verification:** **Verified 2026-09-18**, fetched with `curl` and read.
- **What it says**, verbatim from the "About Efabless" boilerplate: "Efabless offers a platform
  applying open source and community models to enable a global community of chip experts and
  non-experts to collaboratively design, share, prototype and commercialize special purpose chips.
  **Over the past three years, 1300 designs and six hundred tapeouts have been executed on
  Efabless.** The company's customers include startups, Fortune 500 companies, universities, and
  research institutions around the world."
  Also, on what Efabless itself paid for: "The top ten winners will be awarded free fabrication of
  their designs, offering a tangible pathway for bringing their innovative ideas to life."
- **DERIVED, as a cross-check on `OPG-1`:** summing the spreadsheet's `Count` over every shuttle
  whose date is on or before 2024-04-23 gives **1,207** submissions and **566** slots across 19
  shuttles. Adding CI 2106Q, which the sheet omits (`OPG-3`), gives **1,230** and **585**. CI 2404
  taped out the next day, 2024-04-24, and finished at 109, which would take the running total to
  **1,339**. Efabless's "1300 designs" therefore sits between the count excluding the in-flight
  shuttle (1,230) and the count including it (1,339); "six hundred tapeouts" sits just above the
  slot total (585). **The two agree to within the precision the press release offers.**
- **Bears on:**
  - **H5 (supports).** A public, dated, third-party-distributed statement of programme scale that
    matches the spreadsheet. It is the only such statement found for the combined programme.
  - **H6 (context).** "customers include startups, Fortune 500 companies, universities, and research
    institutions" is Efabless's own description of who paid. No proportions are given.
- **Used in:** not yet.
- **Caveats:**
  - Round numbers in marketing boilerplate ("1300", "six hundred"), with no method and no as-of date
    beyond "over the past three years".
  - It is the vendor describing itself, distributed on a paid newswire.
  - "designs" and "tapeouts" are not defined. Our mapping of them onto `Count` and `Manufactured` is
    **our inference**, not the release's.

### OPG-7. chipIgnite: the paid programme grew about 1.7× a year and was at a record when the company died

- **Sources:** `OPG-1` (the spreadsheet), `OPG-2` (Efabless's archived platform pages), `OPG-3`
  (CI 2106Q and CI 2504), and the chipIgnite pricing printed on the archived CI 2110C page.
- **Verification:** **Verified 2026-09-18** for the archived pages and the arithmetic;
  **owner-supplied** for the spreadsheet rows that no archive covers (CI 2304C, CI 2306Q, CI 2311,
  CI 2209C).
- **What it says:**
  - The price, printed on the archived CI 2110C page (capture 2022-12-06): "Two pricing options:
    **$9,750 for 100 QFN or 300 WCSP parts** / 1000 parts for $20 each", "Private shuttle -- no
    open-source requirement", "Guaranteed reservation with $200 deposit", and an "Includes" list of
    "Complete EDA design flow", "Pre-designed packaging and test board", "10 mm² user design area",
    "37 programmable IOs supporting digital and analog", "5 evaluation board assemblies". The
    current successor price is $14,950 (`OPG-9`), which matches `SMB-9`.
  - The full series, submissions per shuttle, in date order:
    **23** (2106Q), **28** (2110C), **13** (2204C), **53** (2206Q), *8 (2209C, status unconfirmed)*,
    **59** (2211Q), **27** (2304C), **49** (2306Q), **49** (2309), **100** (2311), **109** (2404),
    **76** (2406), **73** (2409), **119** (2411), **20 and still open** (2504).
  - **DERIVED**, by calendar year of the shuttle's name code, excluding CI 2209C and including
    CI 2106Q: 2021 → **51**; 2022 → **125**; 2023 → **225**; 2024 → **377**.
    125 ÷ 51 = 2.45×, 225 ÷ 125 = 1.80×, 377 ÷ 225 = 1.68×.
  - **The last shuttle to close, CI 2411, was the largest chipIgnite ever ran** at 119 submissions
    (Efabless's own page: `Capacity 119 / 40 298.0 % Oversubscribed`), and the next one was open and
    accumulating new customers when the company shut down.
- **Bears on:**
  - **H5 (supports), and this is the most load-bearing entry in the file.** Everything else in the
    repository about open shuttles is demand at a price of zero, paid for by Google
    (`DEM-4`…`DEM-9`, `OPEN-1`) or by a national research budget (`DEM-16`…`DEM-19`, `SMB-6`).
    chipIgnite is not: it is a fixed published price of $9,750–$14,950, run by a company the
    comparison document marks as the only programme not requiring external funding (`OPG-8`), and
    **it grew roughly 1.7× a year for three consecutive years**.
  - **H5 (challenges).** The first three runs did not fill — 23, 28 and 13 submissions against
    nominal 40-slot shuttles, two of them labelled `Undersubscribed` by Efabless's own software
    (`OPG-2`), and CI 2204C at 32% of nominal capacity. For its first eighteen months the paid
    programme was a failure by its own dashboard's standard. Whatever made it work later took
    eighteen months to appear, and none of our sources say what it was.
  - **H5 (challenges).** The series is lumpy, not a smooth curve: 100 (2311) → 109 (2404) → 76
    (2406) → 73 (2409) → 119 (2411). Two consecutive falls in 2024. The annual figures grow; the
    per-shuttle figures do not.
  - **H6 (context, and the limit of this entry).** A growing count of $10k–$15k orders is a revenue
    line, not a margin. `SMB-9` records the price; nothing anywhere records the cost to serve. The
    fact that the company then failed to raise money (`OPG-15`) is at least consistent with the
    growth not having been profitable, and one named industry figure says exactly that (`OPG-16`).
- **Used in:** not yet.
- **Caveats:**
  - **Where and why the series stops.** It stops at CI 2411 (closed 2024-11-11) and CI 2504
    (open, never taped out) because **Efabless shut down at the end of February 2025** (`OPEN-7`,
    `OPG-15`). There is no shuttle after that because there was no company after that. **Do not read
    the end of this series as a fall in demand.** The successor programme's numbers are `OPG-9`.
  - Assigning shuttles to calendar years by their `YYMM` name code is a convention; CI 2110C's
    tapeout was 2021-11-26 and CI 2411's was 2024-11-11, so the convention holds, but CI 2304C
    actually taped out 2023-04-24 and is counted in 2023 on both bases.
  - Four chipIgnite rows (2209C, 2304C, 2306Q, 2311) have no archived page and rest on the
    spreadsheet alone.
  - chipIgnite shuttles had no open-source requirement, so unlike the Google shuttles their designs
    are not publicly inspectable and cannot be counted from a repository.

### OPG-8. The 2022 programme comparison: chipIgnite was the only one marked as not needing external funding

- **Source:** "MPW Program Comparisons (2022)", a comparison table supplied by the repository owner
  and published read-only:
  <https://docs.google.com/document/d/1rGOHsDU8XALX7jKw31Q59y3njZ0865T2qZPzhHIjIYo/export?format=txt>
- **Verification:** **Owner-supplied.** The document itself was **Verified 2026-09-18** — downloaded
  and read in full — but it is an internal comparison with no byline, no method and no citations, so
  what is verified is *that the document says this*, not that the figures in it are right. Several
  of them are demonstrably rough; see the caveats. Two of its claims are independently confirmed
  elsewhere in this file and are marked below.
- **What it says.** Transcribed from the document, six programmes across the columns:

  | | Google OpenMPW | chipIgnite | EuroPractice | MUSE | MOSIS | CMC |
  |---|---|---|---|---|---|---|
  | Operated by | Efabless | Efabless | IMEC | MUSE | MOSIS | CMC |
  | Location | Worldwide | Worldwide | Europe | US | US | Canada |
  | Created | 2020 | 2021 | 1995 | 2018 | 1981 | |
  | Commercial Allowed | Yes | Yes | Restricted | ? | ? | Restricted |
  | **NDAs required** | **No** | **No** | **Yes** | **Yes** | **Yes** | **Yes** |
  | Number of Employees | <10 | <10 | >70 | <25 | | >100 |
  | Projects per year | 1,000 | >100 | <700 | ??? | | <500 |
  | Lifetime Projects | | | | | 60,000 | |
  | **Requires External Funding** | **Yes** | **No** | **Yes** | **Maybe?** | **Yes** | **Yes** |
  | Number of Foundries | 2 | 1 | >6? | 1 | | |
  | Foundries | SkyWater, GlobalFoundries | SkyWater | TSMC, IHP, GlobalFoundries, UMC, X-Fab, IMEC | TSMC | | |
  | Process Technologies | 2 (SKY130, GF180MCU) | 1 (SKY130) | >20 | 5? | >20 | >20 |
  | User Cost | Free | Fixed $10k | Per mm | Per mm | Per mm? | Per mm? |
  | **Cost for 10 mm² of 130 nm** | **Free** | **$10k USD** | **~$15k USD** | **~$24k USD** | | |
  | Packaging Included | Yes | Yes | No | ? | No | No |
  | Development Boards Included | Yes | Yes | No | ? | No | No |

  Its footnotes, verbatim:
  - [1] "25% of 2 employees at Google, ~50% of 5→10 employees at Efabless."
  - [2] "56 projects in 2022 (targeted at 80), up from 27 projects in 2021."
  - [3] "Google has provided the funding."
  - [4] "No 130nm process technology is offered. Closest option selected @ $1,500 USD per mm2"
  - [5] "€2,280 EUR per mm2 = €22,800 EUR ~= $24,000 USD"

  It also gives a "Project Types (Per Year)" split for chipIgnite — "37 academic / 19 commercial" —
  and for Europractice — "500 academic / 200 commercial".
- **Bears on:**
  - **H6 (supports, and this is why the document matters).** Of the six programmes, exactly one is
    marked "Requires External Funding: **No**", and it is the paid one. Google's own programme is
    marked "Yes", with the footnote naming Google as the funder. Europractice and MOSIS are marked
    "Yes" — and `SMB-6` has Europractice saying so in its own words. **If the comparison is right,
    chipIgnite is the only entry in this whole table that was a business rather than a subsidy.**
  - **H6 (supports).** <10 employees against >70 at Europractice and >100 at CMC, at a third to a
    sixth of the price, with packaging and boards included. That is the cost-to-serve claim the
    whole foundry.api argument rests on, stated as a comparison by someone who ran one of the
    programmes.
  - **H5 (context) and question C.** The NDA row — No, No, Yes, Yes, Yes, Yes — lines up exactly
    with which programmes grew. `OPG-5` confirms the "No" for the Google/Efabless side from Google's
    own slides, and `OPG-19` confirms the "Yes" for Europractice from Europractice's own access page.
- **Used in:** not yet.
- **Caveats, and they are substantial:**
  - **No author, no date beyond "2022", no method, no sources.** Treat every cell as a
    knowledgeable person's estimate.
  - **Several cells are wrong or misleading against better evidence.** "Google OpenMPW: 1,000
    projects per year" is not a count — the programme's *total* over its whole life was 821
    submissions across 10 shuttles (`OPG-1`). "Europractice: Operated by IMEC" is a simplification of
    a consortium. "Europractice <700 projects per year" is roughly right for that period against
    `DEM-16`'s 731 for 2022.
  - **Footnote [2]'s chipIgnite figures do not match `OPG-1`.** It says "56 projects in 2022 …
    up from 27 projects in 2021", where the shuttle data give 125–133 submissions in 2022 and 28–51
    in 2021. The most likely reading is that the footnote counts *accepted/manufactured* projects
    while `OPG-1` counts submissions — 2022's chipIgnite slot total is 60, or 52 excluding CI 2209C,
    which is the right order for "56" — but **the document does not say which it means** and this is
    our conjecture.
  - Blank cells are blank in the source. MOSIS and CMC are the least filled in.
  - The document carries an internal link (`bit.ly/goog-ic-edu`) and a link to
    `smartphotonics.nl/our-offering/mpw/`. Neither was followed.

### OPG-9. ChipFoundry, the successor, publishes live per-shuttle demand — and every completed run has come in under its slot count

- **Source:** ChipFoundry's shuttle-metrics API, which the client-side metrics page at
  <https://platform.chipfoundry.io/shuttle-metrics> calls. The page itself is a 483-byte Vite shell
  with no data in it; the API is public and unauthenticated:
  - <https://platform.chipfoundry.io/api/v1/shuttles/all-metrics>
  - <https://platform.chipfoundry.io/api/v1/shuttles/status>
- **Verification:** **Verified 2026-09-18**, both endpoints fetched with `curl` and the JSON read.
- **How it was found** (reproducible): fetch `https://platform.chipfoundry.io/shuttle-metrics`, note
  it is an empty SPA shell, fetch the JS bundle it references
  (`/assets/index-BxHOwEBh.js`) and grep it for quoted paths beginning `/api`. `/api/v1/shuttles/all-metrics`
  and `/api/v1/shuttles/status` are among them and both return HTTP 200 without credentials.
- **What it says.** `all-metrics`, verbatim, on 2026-09-18:

  `{"shuttles":[{"shuttle_name":"CI2612","slug":"ci2612","status_text":"Open for interest","interest":110,"planned":35,"reserved":3,"committed":0},{"shuttle_name":"CI2609","slug":"ci2609","status_text":"Open for interest","interest":79,"planned":35,"reserved":21,"committed":16},{"shuttle_name":"CI2605","slug":"ci2605","status_text":"In fabrication (55%)","interest":73,"planned":43,"reserved":32,"committed":29},{"shuttle_name":"CI2511","slug":"ci2511","status_text":"Shipped to customers","interest":53,"planned":37,"reserved":24,"committed":23},{"shuttle_name":"CI2509","slug":"ci2509","status_text":"Shipped to customers","interest":76,"planned":28,"reserved":22,"committed":21}]}`

  | Shuttle | status | interest | planned (slots) | reserved | committed |
  |---|---|---|---|---|---|
  | CI2509 | Shipped to customers | 76 | 28 | 22 | **21** |
  | CI2511 | Shipped to customers | 53 | 37 | 24 | **23** |
  | CI2605 | In fabrication (55%) | 73 | 43 | 32 | **29** |
  | CI2609 | Open for interest | 79 | 35 | 21 | 16 |
  | CI2612 | Open for interest | 110 | 35 | 3 | 0 |

  `status` gives each shuttle's process as `"process_node":"130nm"`, `"technology_pdk":"SkyWater
  SKY130"`, with nine dated milestones each (open, commit, tapeout, mask_release, lot_start,
  wafers_shipped, packaging_complete, board_assembly_complete, customer_shipped) and an
  `is_projected` flag on every one. CI2509 is described as `"September 2025 MPW Shuttle (formerly
  CC2509)"`, tapeout 2025-09-12, customer_shipped 2026-05-19.
- **Bears on:**
  - **H5 (challenges, and this is the most uncomfortable number in the file).** ChipFoundry reports
    `interest` two to three times its slot count on every shuttle — 76 against 28, 53 against 37,
    110 against 35 — **and yet not one completed shuttle has filled its planned slots**: 21 committed
    of 28 planned, 23 of 37, 29 of 43. **Interest is not demand.** Every "oversubscribed" figure in
    `OPG-1`, `OPG-2` and the whole of `shuttle-programmes.md` is a count of *submissions* or
    *expressions of interest*, and here is the one programme that publishes both sides of that gap.
    The gap is large and it goes the wrong way for H5.
  - **H5 (context).** It also shows the programme is continuing. Five shuttles from September 2025
    to December 2026, two already shipped. The Efabless series (`OPG-7`) ends because Efabless ended;
    the work did not.
  - **H6 (context).** `committed` is the number of customers who have paid. 21, 23 and 29 paying
    customers per shuttle at $14,950 is the clearest picture available of the size of this business.
    **DERIVED:** 21 × $14,950 = $313,950; 29 × $14,950 = $433,550 per shuttle, before any cost.
- **Used in:** not yet.
- **Caveats:**
  - **These fields are mutable and have been revised downwards.** Wayback captures of the same API
    show `ci2605` at `interest 95, planned 45, reserved 34, committed 29` on 2026-06-01 against
    `73 / 43 / 32 / 29` today. Any citation must carry the date it was read.
    (Capture: `https://web.archive.org/web/20260601170129if_/https://platform.chipfoundry.io/api/v1/shuttles/ci2605/metrics`
    — **Partial**: reported to us by a delegated agent in this session, not re-fetched by the author
    of this entry.)
  - ChipFoundry does not define `interest`, `reserved` or `committed` anywhere we found. Our reading
    of `committed` as "paid and locked in" is an **inference**.
  - The two open shuttles' numbers will move.
  - `planned` is not fixed either — CI2605 went from 45 to 43 between June and September 2026.
  - **Partial, not Verified:** the price, "$14,950 per project for standard shuttle participation",
    and the minimum-commitment clause, "If a shuttle does not meet the minimum customer commitment
    threshold required for launch, you will be offered: A full refund of your project fee, or The
    option to roll over your project to the next scheduled shuttle", were read from
    <https://chipfoundry.io/faqs> by a delegated agent in this session and quoted back; the author of
    this entry read `$14,950` on <https://chipfoundry.io/> but not the FAQ. That clause matters: it
    is a second supplier writing undersubscription risk into its own terms, alongside the one
    `DEM-10` records.

### OPG-10. IHP's free open MPW: eight runs in under two years, "60+ designs", and a submission process that runs entirely on GitHub

- **Sources:**
  - IHP Open DesignLib documentation: <https://ihp-open-designlib.readthedocs.io/en/latest/>
  - The run repositories under <https://github.com/IHP-GmbH>, indexed by
    <https://github.com/IHP-GmbH/IHP-Open-FMD_QNC-Tapeouts>
  - Krzysztof Herman, "One year of experience with IHP OpenMPW shuttles: a review", Free Silicon
    Conference 2025: <https://wiki.f-si.org/images/5/50/FSiC2025_TapeOut.pdf>
- **Verification:** **Partial.** Every item below was fetched and read by a delegated agent in this
  session, which reported the URLs, the commands and the extracted text; the author of this entry did
  **not** re-fetch them. The FSiC PDF in particular could not be read with the tools to hand
  (`WebFetch` returns raw PDF, poppler is not installed) and was recovered by inflating its
  FlateDecode streams, so its quotes are a **de-spaced reconstruction and are not character-exact**.
  Treat the counts as good and the wording as approximate. `OPEN-3` already covers the IHP PDK
  itself and is Verified.
- **What it says:**
  - **Who paid.** From the Open DesignLib docs: "It is also a central point for design fabrication
    under the concept of IHP Free MPW runs funded by a public German project FMD-QNC (16ME083).
    Project funds can be used exclusively to produce chip designs for non-commercial activities, such
    as university education, research projects, and others."
  - **Eight runs**, Dec 2023 to Sep 2025, recoverable as the eight submodules of
    `IHP-Open-FMD_QNC-Tapeouts` (`curl -sL https://raw.githubusercontent.com/IHP-GmbH/IHP-Open-FMD_QNC-Tapeouts/main/.gitmodules`):
    TO_Dec2023, TO_May2024, TO_Nov2024, TO_Dec2024, TO_Apr2025, TO_May2025, TO_July2025, TO_Sep2025.
  - **Designs per run**, from the FSiC 2025 slides: May-24 **5**, Nov-24 **11**, Dec-24 **9**,
    Apr-25 **22**, May-25 **14**, with a headline of "60+ designs submitted up to the moment" as of
    July 2025.
  - **A countable cross-check.** Each `TO_<Month><Year>` repository has one top-level directory per
    accepted design. Counting directories (excluding the fixed infrastructure directories `.github`,
    `.vscode`, `drc`, `symbol`, `ExampleDesign`, `IP-QualityAssesment`) gives Dec2023 2, May2024 5,
    Nov2024 11, Dec2024 1, Apr2025 17, May2025 14, July2025 18, Sep2025 19 — **87 in total**. It
    agrees exactly with IHP's own figures for May-24, Nov-24 and May-25 and **undercounts** Dec-24
    (1 against 9) and Apr-25 (17 against 22), because a few directories bundle several circuits
    (`RF_amplifiers`, `active_L_VCOs`). **The directory count is a lower bound.**
  - **Countries**, from the FSiC slides: "Germany, Swiss, Austria, France, Chile, Brasil, USA,
    Lithuania, Bangladesh, India, Pakistan, Japan, UK".
  - **Selection**, from the docs: "All designs, which have passed tests will be submitted for a
    selection process according to criteria presented below. The time window for evaluation &
    selection will be around 10 days"; the mandatory criteria include "provide design data together
    with open source license" and "The maximum area below 2 mm² preferred".
  - **No NDA is mentioned anywhere in the free-era documentation.** The mandatory condition is the
    opposite: an open-source licence.
- **Bears on:**
  - **H5 (supports, weakly).** A second foundry with an open PDK, a second free programme, a second
    worldwide response — and, again, applications arriving from more than a dozen countries within
    two years of the PDK appearing.
  - **H5 (challenges).** The absolute numbers are small: about **87 to 100 designs over eight runs
    in under two years**, against the Google programme's 821 over ten. `DEM-16`'s point stands — a
    real community, not a market.
  - **H4 (supports).** The submission process is a pull request against a public GitHub repository,
    which is about as close to self-service as chip fabrication has come.
- **Used in:** not yet. It extends `OPEN-3`.
- **Caveats:**
  - Partial throughout, as stated above.
  - The docs table omits the Dec 2023 run, which exists only as a repository; the run count of eight
    comes from the repository list, not from any IHP page that says "eight".
  - "60+ designs" is IHP's own rounded figure as of July 2025 and predates the last two runs.
  - **The free era has ended.** From 2026 the programme is paid: see `OPG-11`. Any statement that
    "IHP's open MPW is free" is now out of date.

### OPG-11. IHP's paid open-silicon MPW publishes who has registered how much area — and two customers are 71% of one run

- **Source:** IHP, "Open Source Request", the registration page for its Open-Silicon MPW programme:
  <https://dk.ihp-microelectronics.com/OpenSourceRequest.php> (the path
  `ihp-microelectronics.com/services/research-and-prototyping-service/mpw-prototyping-service/low-cost-open-source-mpw-access-1`
  307-redirects to it; `WebFetch` will not follow the cross-host redirect, so fetch the `dk.` URL
  directly).
- **Verification:** **Verified 2026-09-18.** Fetched with `curl` and the per-customer figures read
  straight out of the HTML — they are in `data-label` / `data-value` attributes on a stacked bar and
  need no JavaScript:
  `curl -sL https://dk.ihp-microelectronics.com/OpenSourceRequest.php | grep -o -E 'data-label="[^"]*"|data-value="[^"]*"'`
- **What it says:**
  - **The pricing mechanism**, verbatim: "The MPW run will only start once the total area requested
    by all customers exceeds the minimum required area. After this threshold is reached, the price
    per customer will decrease as the total requested area increases, until the lowest price level is
    reached." And: "Customers who choose to release their designs under the Apache License 2.0 can
    benefit from our lowest-cost MPW offering." And: "**Participation requires signing the Open
    Silicon MPW Program Participation Agreement.**" And, for those who will not publish:
    "For customers who do not wish to disclose their intellectual property, IHP offers participation
    in the same open-silicon MPW program at 20% off the standard MPW price."
  - **Two runs are open.** "Open Source SG13G2 29.09.2026", registration deadline "2026-09-21",
    price "SG13G2 - 2800€ per ㎟". And "Open Source MPW CMOS5L 09.11.2026", deadline "2026-10-26",
    price "SG13CMOS5L - 1500€ per ㎟", carrying the warning "**Minimal required area not reached yet**"
    with "Minimum area 90㎟" and "Lowest price 900€ per ㎟".
  - **Who has registered, and how much, read from the page:**

    *SG13G2 run closing 2026-09-29* — IHP_ext 2, Lund University 1, Navia Labs 9,
    **Tiny Tapeout B.V. 18**, NEBULA MICROSYSTEMS 3, Simra AI 1, Ulster University 1.2,
    **IEEE Circuits and Systems Society 24**. **DERIVED total: 59.2 mm²**
    (2 + 1 + 9 + 18 + 3 + 1 + 1.2 + 24 = 59.2).

    *SG13CMOS5L run closing 2026-11-09* — Universität Heidelberg – Kirchhoff Institut für Physik 28,
    Open Circuit Design 7.5, Heidelberg University (HeiChips) 9. **DERIVED total: 44.5 mm²**
    (28 + 7.5 + 9 = 44.5), against a stated minimum of 90 mm².
- **Bears on:**
  - **H5 (challenges, hard, on two separate counts.)**
    1. **Concentration.** On the SG13G2 run, two customers — IEEE CASS at 24 mm² and Tiny Tapeout at
       18 mm² — hold **42 of 59.2 mm², or 71%** (42 ÷ 59.2 = 0.7095). The other six customers
       between them hold 17.2 mm². This is the long-tail thesis's own showcase programme, and its
       demand is concentrated in two intermediaries. `CONC`-style customer concentration is visible
       at the very bottom of the market, not only at the top.
    2. **Undersubscription.** The CMOS5L run has reached 44.5 of the 90 mm² it needs, five weeks
       before its deadline, and IHP's own page says so in bold. A run that may not happen for want of
       demand, published live by the operator.
  - **H6 (supports, as a design).** The price falls as aggregate area rises and the run does not
    start until a threshold is met. That is a fab selling machine time at published prices and making
    the buyers, not itself, carry the fill risk — structurally close to what `AUCTIONS.md` proposes.
    Whether it works is exactly what the CMOS5L run is testing in public.
  - **H4 (context).** €2,800/mm² for the open route against IHP's standard €7,300/mm² for the same
    SG13G2 process — **DERIVED**, a 62% discount (1 − 2800 ÷ 7300 = 0.6164) — is the price of
    publishing your design. (**Partial**: the €6,300 / €7,300 standard prices were read from
    IHP's schedule and price list by a delegated agent, not by this entry's author.)
- **Used in:** not yet.
- **Caveats:**
  - **A live page.** These figures will change; 2026-09-18 is the date read, and the SG13G2 deadline
    is 2026-09-21, three days later.
  - The bar's full scale appears to be 180 mm² with the "minimum area" marker at 50% and the "lowest
    price" marker at 100%; that reading of the scale is an **inference** from the marker positions,
    not something the page states.
  - "Registered area" is not a paid order. We do not know how many of these registrations convert.
  - The participation agreement is a legal instrument, not an NDA, but it is not nothing: this is no
    longer "just clone" (`OPG-5`).
  - **Tiny Tapeout B.V. appearing as a customer here means the 18 mm² is one line in IHP's book and
    several hundred tiles in Tiny Tapeout's.** Do not add IHP's customer count to Tiny Tapeout's
    design count.

### OPG-12. Crowd Supply: wafer.space sold 6, then 18, then 5 slots at $2,000–$8,500 each

- **Source:** Crowd Supply campaign pages:
  - <https://www.crowdsupply.com/wafer-space/gf180mcu-run-1>
  - <https://www.crowdsupply.com/wafer-space/gf180mcu-run-2>
  - <https://www.crowdsupply.com/wafer-space/gf180mcu-run-3>
  and the Crowd Supply "Open Silicon" category: <https://www.crowdsupply.com/open-silicon>
- **Verification:** **Partial.** All pages were fetched and read by a delegated agent in this session
  on 2026-09-18, which reported the verbatim figures and the URLs; the author of this entry did not
  re-fetch them.
  **Conflict of interest, stated plainly: wafer.space is the repository owner's own company** (the
  campaign pages list Tim Ansell as founder). These are our own numbers and should be weighted
  accordingly.
- **What it says:**

  | Campaign | Raised | Goal | Backers | Closed |
  |---|---|---|---|---|
  | GF180MCU Run 1 | "$55,500 raised" | "of $40,000 goal", "138% Funded!" | **6** | "Nov 28 2025 funded on" |
  | GF180MCU Run 2 | "$175,000 raised" | "of $1 goal", "Funded!" | **18** | "Jun 29 funded on" (2026) |
  | GF180MCU Run 3 | "$121,500 raised" | "of $1 goal", "Funded!" | **5** | live, "Funding ends on Dec 19, 2026" |

  Prices, Run 3: full slot $7,000 early bird / $7,500–$8,000 standard; half slots $4,000/$4,500;
  quarter slot $2,000; undiced wafer $2,000; chip-on-board packaging +$1,500. Every slot delivers
  **1,000 dies**: "Each slot consists of a 3.88 mm × 5.07 mm (19.67 mm²) fixed die area, replicated
  1,000 times."

  Run 1's goal was **restated during the campaign**: Wayback captures show "$17,500 raised of $68,012
  goal, 26% Funded, 2 backers" on 2025-11-01, "$40,000 raised, 59% Funded, 5 backers" on 2025-11-26,
  and "$40,000, 100% Funded!" by 2025-12-15 — i.e. the goal was changed from $68,012 to $40,000
  after the money came in. Runs 2 and 3 carry a placeholder "$1 goal", so their "Funded!" badge
  means nothing.

  Run 2's own page says of Run 1: "GF180MCU Run 1 closed in November 2025 with a full reticle of many
  designs from universities, startups, hobbyists, and established engineers around the world. …
  29 of those designs are publicly available at github.com/wafer-space/ws-run1."
- **Bears on:**
  - **H5 (supports, weakly).** Backers went 6 → 18 between Run 1 and Run 2, a 3× rise, at $4,000 to
    $8,500 a slot with no subsidy of any kind. These are unambiguously paying customers, which is
    the population the repository's evidence is weakest on.
  - **H5 (challenges).** **Six. Then eighteen. Then five so far.** On the most permissive reading
    that is fewer than thirty distinct buyers in a year, worldwide, for a $2,000–$8,500 route to a
    thousand custom chips. Set beside `DEM-16`'s Europractice at 753–985 designs a year, these are
    tiny numbers. And one of the eighteen is Tiny Tapeout reselling tiles inside its slot (`OPG-11`
    shows the same pattern at IHP), so the count of *end* customers and the count of *slot buyers*
    are different things.
  - **H6 (context).** A published, flat, self-service price with no sales process, and the money
    arrives before the wafer does. That is the shape `PRINCIPLES.md` argues for. Whether $175,000 a
    run covers the run is not something these pages say.
- **Used in:** not yet.
- **Caveats:**
  - Partial and self-interested, as above.
  - "Backers" on Crowd Supply counts orders, not people, and includes non-slot pledges.
  - Run 1's moved goalpost means its "138% Funded!" badge should not be quoted as evidence of
    oversubscription.
  - Crowd Supply does not print campaign start dates; the dates above are inferred from the oldest
    project update on each campaign.
  - **Two percentages that a summarisation tool produced for Runs 2 and 3 — "17,500,000%" and
    "12,150%" — are not printed anywhere on those pages.** They are artefacts of the $1 placeholder
    goal. Do not quote them.

### OPG-13. The open-silicon crowdfunding campaigns that failed, and the one that was suspended

- **Sources:**
  - OnChip, "Open-V": <https://www.crowdsupply.com/onchip/open-v>
  - Chips4Makers, "Retro-uC": <https://www.crowdsupply.com/chips4makers/retro-uc>
  - RadioStack, "Maverick-603": <https://www.crowdsupply.com/radiostack/maverick-603>
  - Libre RISC-V M-Class: <https://www.crowdsupply.com/libre-risc-v/m-class>
- **Verification:** **Partial.** All four pages were fetched and read by a delegated agent in this
  session on 2026-09-18, which reported the verbatim figures; not re-fetched by this entry's author.
- **What it says:**
  - **Open-V** (an open-source RISC-V microcontroller): "$44,641 raised" "of $400,000 goal",
    **318 backers**, "Jun 30 2017 ended", every product "No Longer Available", and the page prints
    **no percentage and no "Funded!"**. **DERIVED: 44,641 ÷ 400,000 = 11.2% of goal.** Tiers ran from
    "Chip Pioneer — $49" to "Early Access Chip-on-Board + Design Review — $9,000".
  - **Retro-uC** (Chips4Makers): "$4,034 raised" "of $22,000 goal", **40 backers**, "Oct 21 2018
    ended", no "Funded!". **DERIVED: 4,034 ÷ 22,000 = 18.3% of goal.** Its foundry route was TSMC via
    the imec service centre — a closed PDK, not an open one.
  - **Maverick-603** (RadioStack), and this is the one that matters most here: "$16,142 raised" "of
    $15,000 goal", "107% Funded!", **62 backers** — and then "Apr 25 2023 suspended", banner
    "Campaign Suspended". Its chip was to be made through Efabless: "With the help of eFabless and
    their ChipIgnite Program, we were able to overcome these obstacles and make Maverick-603 a
    reality." and "Our custom, open source chip will be manufactured at the SkyWater Foundry in
    Minnesota through the eFabless ChipIgnite Program." It listed as a risk: "The tape-out timeline
    for our chip at eFabless could be delayed."
  - **Libre RISC-V M-Class**: "This project has been abandoned and will not launch." No goal, no
    money, no backers.
  - **Negative result, and a useful one:** Crowd Supply's "Open Silicon" category contains **four**
    projects in total — Dabao (Baochip) and wafer.space Runs 1, 2 and 3. There has **never been a
    Tiny Tapeout campaign on Crowd Supply**, nor on GroupGets; Tiny Tapeout sells direct. Searches of
    crowdsupply.com for `caravel`, `openlane`, `chipfoundry` and `zero to asic` return zero results;
    `efabless` returns only Maverick-603.
- **Bears on:**
  - **H5 (challenges, and this is the section a reviewer should check).** The repository's open-silicon
    evidence is drawn almost entirely from programmes that succeeded. Here is the other side.
    An open RISC-V microcontroller raised **11% of its goal** with 318 backers and died. Retro-uC
    raised **18%** with 40 backers and died. The one product that did fund, reached its goal and had
    62 paying backers — Maverick-603, the only consumer product on Crowd Supply built on chipIgnite —
    was **suspended**. Enthusiasm for open silicon converts into funded hardware products very
    poorly.
  - **H5 (challenges).** 318 backers for Open-V is *more* than any single open shuttle run has ever
    had participants, and it still failed, because wanting a chip and paying enough to make one are
    different things.
  - **H6 (context).** Maverick-603's own risk list named its dependence on Efabless's schedule. The
    intermediary's fragility was visible to its customers in 2022, two and a half years before it
    failed.
- **Used in:** not yet.
- **Caveats:**
  - Partial; not re-read by this entry's author.
  - Open-V (2016–17) and Retro-uC (2017–18) predate SKY130 and the open-PDK era entirely. They are
    evidence about open-silicon *products*, not about open-PDK shuttle demand, and the comparison
    should not be pushed too far.
  - Crowd Supply suspends campaigns for several reasons; the page does not say why Maverick-603 was
    suspended, and we did not find a statement. **Do not assert that Efabless caused it.**
  - A crowdfunding platform is a biased sample: it sees consumer-facing products, not the startups
    and universities that buy most shuttle slots.

### OPG-14. Tiny Tapeout's price history, and what Efabless actually sponsored

- **Sources:** Tiny Tapeout's own pages over time, via the Internet Archive:
  - <https://web.archive.org/web/20230308005142id_/https://tinytapeout.com/> (2023-03-08)
  - <https://web.archive.org/web/20230923173106id_/https://tinytapeout.com/> (2023-09-23)
  - <https://web.archive.org/web/20240225014649id_/https://tinytapeout.com/> (2024-02-25)
  - <https://web.archive.org/web/20250226081141id_/https://tinytapeout.com/faq/> (2025-02-26)
  - <https://web.archive.org/web/20250621202131id_/https://tinytapeout.com/> and `/faq/` (2025-06-21)
  and the live workshop page <https://tinytapeout.com/workshops/>.
- **Verification:** **Verified 2026-09-18.** Seven archived captures and the live workshops page were
  fetched with `curl` and read.
- **What it says**, verbatim, in date order:
  - **2023-03-08** (TT03 era): "Design + Physical PCB + ASIC = $100 + p&p" and "Design only = $25".
    **No sponsor is named anywhere on the page.**
  - **2023-09-23** (TT04 era): "Design (single tile) + Physical PCB + ASIC = $100 + shipping",
    "Design only (single tile): $50", "Extra tiles = $50 each". **Again no sponsor named.**
  - **2024-02-25** (TT06 era) — the first capture in which Efabless appears: "160 x 100 um tile +
    ASIC + demonstration board: **The standard price is $300 plus shipping.** However, **Efabless is
    sponsoring a special early bird offer of $150** (plus shipping), **limited to one order per
    person.** Each extra tile is $50, and extra analog pins start from $40 per pin."
  - **2025-02-26**, the FAQ, five days before Efabless shut down: "**The first 80 orders from
    individuals are sponsored by Efabless**, so you get 1 tile, 1 ASIC mounted on 1 demo board PCB for
    $150 + postage. **After those first 80 are gone, the price goes up to $300.**"
  - **2025-06-21**, after Efabless shut down: the sponsorship sentence is **gone** from the FAQ, and
    the home page reads "200 x 150 um tile + ASIC + demonstration board: **The price for the current
    open source IHP shuttle is 150 € plus shipping.** Each extra tile is 50 €."
  - The live workshops page lists its sponsors as image files, among them `sponsors/chip-ignite.png`
    and `sponsors/chip-foundry.png`, alongside IEEE, IEEE SSCS, IEEE Toronto, Synopsys, CMC, CHIMES,
    Chip Design Germany, DTU, Swiss Chips, the UK Electronics Skills Foundation, the University of
    Toronto and the University of Waterloo. The page also says: "We have run over 20 workshops in
    multiple countries and helped over 1,000 participants learn and design their own ASIC."
- **Bears on:**
  - **This corrects `OPEN-5`.** `OPEN-5`'s caveat currently reads "The prices were subsidised by
    Efabless at the time." That is **too broad and, as written, wrong**. What Tiny Tapeout's own
    pages say is narrower and quite different:
    1. The **standard price was not sponsored**. It was $300, printed as the standard price, from
       TT06 onward.
    2. Efabless sponsored **one capped tier** — an early-bird rate of $150, limited to one order per
       person, and limited to the **first 80 orders from individuals** (eeNews, quoted in `OPEN-5`,
       says the first 100 for TT06). Businesses and universities paid $300 throughout.
    3. The sponsorship **did not exist before about January 2024**. In 2023 the price was $100 for
       tile-plus-chip-plus-board with **no sponsor named on the page at all** — which is *lower* than
       the sponsored $150 that came later.
    4. When Efabless died, prices did **not** rise. The next shuttle was €150 for a tile, an ASIC and
       a board — the same as the old sponsored early-bird rate, and half the unsponsored $300.
  - **The owner's account and the public record, compared.** The owner states that Efabless did not
    subsidise Tiny Tapeout's prices but sponsored free places at specific workshops. The public
    record **partly** supports that and **partly** does not. It supports it on workshops: chipIgnite
    and ChipFoundry are both on Tiny Tapeout's workshop sponsor list. It does **not** support the
    stronger form of the claim, because Tiny Tapeout's own home page said in so many words, for more
    than a year, that "Efabless is sponsoring a special early bird offer of $150" against a standard
    price of $300 — that *is* a price subsidy, just a capped one aimed at individuals. **We found no
    page anywhere stating that Efabless sponsored free workshop places**, only that it is listed as a
    workshop sponsor.
  - **H5 (challenges, mildly).** The price a Tiny Tapeout customer actually paid varied by a factor
    of three depending on whether they were an individual and how early they ordered. Submission
    counts across shuttles therefore mix populations facing different prices, which weakens any
    reading of `DEM-1` and `DEM-2` as a demand curve.
  - **H5 (supports).** Prices *fell* after the sponsor disappeared, which is the opposite of what a
    subsidised-market story predicts.
- **Used in:** not yet. **`OPEN-5` needs editing; see the "Changes needed in other files" section of
  [`efabless-and-the-open-shuttles.md`](efabless-and-the-open-shuttles.md).**
- **Caveats:**
  - Archive captures are point samples. The sponsorship may have begun before 2024-02-25 and ended
    before 2025-06-21; we know only that it was absent on 2023-09-23, present on 2024-02-25 and
    2025-02-26, and absent on 2025-06-21.
  - The 2025-06 price is in euros for an IHP shuttle and the earlier ones in dollars for a SkyWater
    shuttle, on different tile sizes (160×100 µm against 200×150 µm). It is not a like-for-like
    comparison and should not be presented as one.
  - "over 20 workshops … over 1,000 participants" is Tiny Tapeout's own figure with no method, no
    date and no list.
  - Efabless *did* also sponsor fabrication directly, but as prizes: its 2024 TinyML contest offered
    "The top ten winners will be awarded free fabrication of their designs" (`OPG-6`). That is a
    third form of sponsorship, distinct from both a price subsidy and a workshop sponsorship.

### OPG-15. Mike Wishart's full statement: "we were not able to close our Series B round"

- **Source:** the Efabless shutdown thread on SemiWiki, "efabless just shut down", started by Daniel
  Payne on 2025-03-04; Mike Wishart's letter to the Efabless community posted in full by Daniel
  Nenni (SemiWiki's founder) on 2025-03-05:
  <https://semiwiki.com/forum/threads/efabless-just-shut-down.22217/>
- **Verification:** **Verified 2026-09-18**, fetched with `curl` and read. (`WebFetch` timed out on
  this URL; `curl` worked.)
- **What it says:**
  - The shutdown notice Efabless posted at `efabless.com/notice`, quoted in the thread's first post:
    "Due to funding challenges, Efabless has shut down operations until further notice. We regret
    any inconvenience and will provide updates as available."
  - Wishart's letter, signed "With kind regards / Mike Wishart", opening: "I confirm here what many
    of you have already heard; the sad news of the wind down of Efabless and the layoff of our
    wonderful team of smart, dedicated, selfless and inspired professionals. Efabless has been
    dedicated since its founding to making chip creation affordable, simple and accessible to
    everyone. Our pillars are community, business models based on sharing of risk and reward and open
    source. **On the brink of a wonderful next chapter, we were not able to close our Series B round
    and must now tend to the inevitable necessities.** Our customers and partners should now have
    received word and how to follow up."
  - "I am thrilled with what the Efabless team accomplished and saddened to think about what it could
    have been. Chips can now be created for thousands of dollars not millions, and, ultimately, by
    millions and not thousands of people."
  - "Without the support of GlobalFoundries, SkyWater, Synopsys, Google, XFAB, AFRL, Arm and many
    others, we would not have come this far."
  - "And the same to our **13K plus member community**."
- **Bears on:**
  - **H4 and H6 (challenges), extending `OPEN-7`.** `OPEN-7` has the trade-press paraphrase, "we were
    unable to complete our latest funding round". This is the primary text, and it is more specific:
    the round that failed was a **Series B**, and the CEO's own framing is "On the brink of a
    wonderful next chapter" — a company that believed it was about to succeed, not one winding down a
    failing product.
  - **H5 (context).** "13K plus member community" is Efabless's own final community figure, against
    the "almost 1100 members" Kassem gave for MPW-1 in 2021 (`DEM-4`) and Google's "more than 3,000
    members" in mid-2022 (`DEM-5`). **DERIVED:** roughly 1,100 → 3,000 → 13,000 over about four
    years. Community grew about 12× while submissions grew about 4× a year at the peak; the two are
    not the same thing and the gap between them is itself worth noting.
- **Used in:** not yet. It supplements `OPEN-7`.
- **Caveats and the open question:**
  - **The repository owner states that Efabless died because an early investor refused to be diluted,
    blocking the new round from closing.** That is recorded here as **owner-supplied** and
    **uncorroborated**. Wishart's letter is *consistent* with it — a round that was close and did not
    close — but says nothing about why, names no investor, and mentions no dispute. **We searched for
    corroboration and did not find any.** What was tried and what happened:
    - SemiWiki thread (above): read in full. No mention of an investor, dilution or a block.
    - Hackster.io's report (`OPEN-7`): `WebFetch` returned **HTTP 403**. The article was already read
      for `OPEN-7`, which records "sources suggest a grant on which the company had been banking did
      not materialize" — a *different* proposed cause, and also unattributed.
    - SEC EDGAR, to look for Form D filings that would show the rounds: `https://www.sec.gov/cgi-bin/browse-edgar?...`
      returned **HTTP 403** with the message "Your Request Originates from an Undeclared Automated
      Tool". SEC requires a declared User-Agent identifying the requester, and we will not put a
      personal identifier in a request header, so **this route is closed to us**. *A human could open
      EDGAR full-text search in a browser and look for Efabless Corporation Form D filings; that is
      the single most likely place a public record of the rounds exists.*
    - Web searches for the investor/dilution account, in several phrasings: nothing. Every result
      repeats "funding challenges" or the Series B sentence.
    - Matt Venn's own year-in-review (<https://www.zerotoasiccourse.com/post/year_update_2025/>,
      2026-01-04): read; it describes the impact but **does not explain the cause**.
  - **So the honest position is:** the cause of death is publicly unexplained beyond "the Series B
    did not close". The owner's account is a specific, plausible mechanism for that, supplied by
    someone with direct knowledge, and it remains owner-supplied. **It should not be written into
    `WHY.md` or `PRINCIPLES.md` as established.**
  - A forum thread is a secondary carrier. The letter is quoted by SemiWiki's founder, not posted by
    Wishart himself, and `efabless.com/notice` is gone.

### OPG-16. A named industry figure's verdict: "the revenue model just did not work"

- **Source:** Daniel Nenni, founder of SemiWiki, replying in the same thread on 2025-03-05:
  <https://semiwiki.com/forum/threads/efabless-just-shut-down.22217/> (post #5).
- **Verification:** **Verified 2026-09-18**, read in the thread.
- **What it says**, verbatim: "Yes, big foundries are not a fan of open source tools. TSMC silicon
  verifies EDA tools and IP so customers can be assured of success. The whole trusted foundry thing.
  We worked with eFabless when they first started. It was fun and very educational but **the revenue
  model just did not work. People who use open source tools do it mainly due to cost and that is a
  tough customer base to profit from.** My opinion."
  The question he was answering, from user `hist78`: "They seem to have a good business model in the
  semiconductor market. I'm wondering what went wrong. TSMC is not in the eFabless' partner list.
  Could that be one of the biggest problems?"
- **Bears on:**
  - **H5 and H6 (challenges), and this is the sharpest public statement against the thesis we have
    found.** It is exactly H6's negation, from someone who says he worked with the company: the
    customers exist, they are drawn by cost, and a customer base drawn by cost is hard to profit
    from. If that is right, the growth in `OPG-1` and `OPG-7` is real *and* commercially worthless,
    which is the one combination that would let both "demand grew" and "the company died" be true
    without either explaining the other.
  - **H4 (context).** The second claim — that large foundries dislike open-source tools because they
    qualify EDA and IP themselves — bears on `RISK` and on whether an open flow can reach a leading
    foundry at all.
- **Used in:** not yet.
- **Caveats:**
  - **It is explicitly an opinion** — he says "My opinion" — from a forum post, by someone who runs
    a site funded by the commercial EDA and IP industry that open tools compete with.
  - "We worked with eFabless when they first started" is asserted without detail; we have no way to
    check what the relationship was or when.
  - It is a claim about profitability made without access to Efabless's accounts.
  - The reply directly beneath it, from user `revsemi`, offers a different diagnosis again: "The
    problem with open-source currently is that it is hijacked by large software and cloud companies.
    … such an open source definition actually makes it very hard for small companies to survive."
    Three public explanations for one death — a grant that did not arrive, a revenue model that did
    not work, and an open-source model that favours large firms — and none of them is evidenced.

### OPG-17. Europractice's own access rules: members only, by country, by institution type, with NDAs and design-kit licences

- **Sources:**
  - EUROPRACTICE, "Foundry access & Membership":
    <https://europractice-ic.com/access-and-registration/foundry-access-and-membership/>
  - EUROPRACTICE, "Eligible Countries": <https://www.europractice.stfc.ac.uk/membership/eligible.html>
  - EUROPRACTICE, "EUROPRACTICE Membership": <https://www.europractice.stfc.ac.uk/membership/membership.html>
- **Verification:** **Verified 2026-09-18**, all three fetched with `curl` and read.
- **What it says**, verbatim:
  - On what a user must sign: "Here are quick links to the access information to particular foundries
    together with the **necessary NDAs (Non-Disclosure Agreements), DKLAs (Design Kit License
    Agreements)** and contact details".
  - On who may join: "Europractice membership is available to **academic institutions or publicly
    funded research laboratories primarily engaged in university-like activities** from Europe
    (European Union member States and European countries eligible to participate in EC projects) and
    other countries within EMEA (Europe, Middle East, and Africa)."
  - On everyone else: "Customers who are **not eligible** for Europractice membership can access
    **only** MPW and volume-production fabrication services. In this case, **Standard prices** would
    apply."
  - From the eligibility page: "EUROPRACTICE services are available to Academic Institutions or
    publicly funded Research Laboratories primarily engaged in University like activities from the
    European Union member States, European countries eligible to participate in Horizon Europe KDT JU
    Programme, and other countries in the EMEA (Europe, Middle East and Africa) region. **Eligible
    institutions must become a Member of EUROPRACTICE and pay the annual membership fee before they
    can make use of EUROPRACTICE services.**" It then lists the 27 EU member states plus Albania,
    Armenia, Azerbaijan, Bosnia-Herzegovina, Georgia, Iceland, Israel, Liechtenstein, Moldova,
    Montenegro, North Macedonia, Norway, Switzerland, Turkey, Serbia, Ukraine and the United Kingdom.
  - The fees, from the membership page: "**Full-IC annual membership, 1100 EURO**",
    "Software-only annual membership, 600 EURO", "FPGA-only annual membership, 200 EURO",
    "**MPW-only annual membership, 600 EURO**", and "The annual membership fee year runs from
    1 October to 30 September."
- **Bears on:**
  - **Question C directly** (see [`efabless-and-the-open-shuttles.md`](efabless-and-the-open-shuttles.md)).
    This is the primary text for the access-and-eligibility explanation. To put a design on a
    Europractice MPW at the member price in 2026 a person must: belong to a degree-awarding
    institution or a publicly funded lab; be in one of about 44 listed countries; pay €600 or €1,100
    a year before doing anything; and sign an NDA and a design-kit licence per foundry. To put a
    design on a Google Open MPW shuttle in 2022 a person had to clone a repository and open an
    account.
  - **H5 (context).** It also explains the shape of `DEM-16`'s series. A service whose membership is
    gated on institution type will grow with the number of qualifying institutions, which barely
    changes, not with the number of interested people.
- **Used in:** not yet. It supports `SMB-6`, `SMB-7` and `DEM-16`.
- **Caveats:**
  - The NDA/DKLA sentence is a link-list heading. It establishes that NDAs and design-kit licences
    are part of the access procedure; **it does not establish that every foundry in the portfolio
    requires one**, and Europractice tells users to go to the per-foundry pages. We did not read
    those pages.
  - Non-members *can* buy MPW fabrication at standard prices, so this is not an absolute bar to a
    non-European or commercial user — it is a price and paperwork barrier, not a wall. The
    comparison document's "Commercial Allowed: Restricted" (`OPG-8`) is the right characterisation.
  - Two Europractice web presences exist (`europractice-ic.com` and `europractice.stfc.ac.uk`) with
    overlapping and not identical text. Both were read.
  - The membership fee is small next to a mask set. Its effect is as a gate and an administrative
    step, not as a cost.

### OPG-18. Muse Semiconductor requires two or three signed agreements, and its prices cannot be read

- **Source:** Muse Semiconductor's FAQ, <https://www.musesemi.com/faq>, and its pricing and schedule
  pages <https://www.musesemi.com/shared-block-tapeout-pricing> and `/shared-block-tapeout-schedule`.
- **Verification:** **Partial.** The FAQ quotes were read by a delegated agent in this session on
  2026-09-18 and reported back; not re-read by this entry's author. The **pricing and schedule pages
  could not be read at all** — see the caveats.
- **What it says**, from the FAQ: "We require only two agreements: A Mutual Non-Disclosure Agreement
  (MNDA)…A TSMC 3-way NDA between Muse, TSMC, and the customer." (plus a Master Technology Usage
  Agreement for TSMC IP access). And: "Yes! We have several commercial customers. Semiconductor
  startups and semiconductor IP suppliers can access TSMC technology cost-effectively."
- **Bears on:**
  - **Question C.** Muse is the clean counter-example: a low-friction, well-run, US-based university
    shuttle service on a **closed** PDK, requiring **two or three NDAs** including a three-way NDA
    with the foundry. It corroborates `OPG-8`'s "NDAs required: Yes" for MUSE from Muse's own words.
  - **H4 (context).** It shows what the paperwork looks like when the PDK is not open, and therefore
    what "No NDA required, just clone" (`OPG-5`) was actually replacing.
- **Used in:** not yet.
- **Caveats:**
  - **Blocked, and worth recording precisely.** `musesemi.com/shared-block-tapeout-pricing` returns
    HTTP 200 but is entirely client-rendered (a Wix application); the ~494 KB response contains no
    prices, and the same is true of the schedule page. **The Internet Archive does not help** — the
    most recent capture (`https://web.archive.org/web/20260521111101if_/https://www.musesemi.com/shared-block-tapeout-pricing`)
    is the same JavaScript-only shell. Forty captures back to 2019-08-25 were listed; the older ones
    were not all checked, and a pre-Wix capture may well be readable. *What would unblock a human:
    opening either page in an ordinary browser, or working back through the 2019–2021 captures.*
  - `OPG-8`'s "~$24k USD for 10 mm² of 130 nm" for MUSE is therefore **unverified** and rests on the
    comparison document alone.

### OPG-19. Cadence and SkyWater are running a $10,000 SKY130 MPW aggregation service

- **Source:** SkyWater Technology, "Lowering Barriers to Silicon: Cadence Launches MPW Aggregation
  Service for SKY130":
  <https://www.skywatertechnology.com/lowering-barriers-to-silicon-cadence-launches-mpw-aggregation-service-for-sky130/>
- **Verification:** **Partial.** Read by a delegated agent in this session on 2026-09-18 and reported
  with quotes; not re-read by this entry's author.
- **What it says:** "USD $10,000 per design"; participants receive "40 bare die"; layout bounding box
  "3.588mm x 5.188mm"; verification uses "the Cadence® Pegasus™ Physical Verification Solution, based
  on the SKY130 design rules"; the audience is "students and researchers to entrepreneurs and
  early-stage teams"; each submission requires "an executed legal agreement"; "Cadence plans to offer
  multiple MPW runs per year". First run: DRC rules finalised "May 2, 2025", submissions "Mid-May
  2025", die delivery "September 2025".
- **Bears on:**
  - **H4 and H5 (supports).** A fourth independent route to SKY130 silicon, opened *after* Efabless
    died, run by the largest EDA vendor but for the **open** PDK. Open PDKs outlived the company that
    popularised them.
  - **Question C (context).** Its price sits between wafer.space ($2,000–$8,000 for 1,000 dies) and
    ChipFoundry ($14,950 for 100 packaged parts), and it requires "an executed legal agreement" —
    less than an NDA, more than "just clone".
- **Used in:** not yet.
- **Caveats:**
  - Partial. It is also a vendor press release.
  - **No slot count and no submission count are published**, so it cannot be added to any series
    here. If Cadence begins publishing run data it would be the first genuinely independent operator
    of an open-PDK shuttle whose numbers could be compared with Efabless's.
  - "40 bare die" against chipIgnite's "100 QFN packaged parts" makes the two prices not directly
    comparable.

### OPG-20. The Open MPW submission windows, read off Efabless's own shuttle pages — and the "30 days" everyone quotes for MPW-1 is not what the platform said

- **Sources:** the archived Efabless shuttle pages on `platform.efabless.com`, raw-content form. Each
  page prints its own schedule as two lines, "<date>: Project submission is OPEN" and
  "<date>: Project submission is CLOSED at 23:59 PT".
  - MPW-1: <https://web.archive.org/web/20240227030521id_/https://platform.efabless.com/shuttles/MPW-1>
  - MPW-7: <https://web.archive.org/web/20221204010751id_/https://platform.efabless.com/shuttles/MPW-7>
  - MPW-8: <https://web.archive.org/web/20221121184401id_/https://platform.efabless.com/shuttles/MPW-8>
  - GF MPW-0: <https://web.archive.org/web/20221115002500id_/https://platform.efabless.com/shuttles/GFMPW-0>
  - GF MPW-1: <https://web.archive.org/web/20240227030244id_/https://platform.efabless.com/shuttles/GFMPW-1>
  - MPW-6's window is not on a surviving page; it comes from `DEM-6` (Efabless's own programme page:
    "April 11, 2022: Project submission is OPEN", "June 8, 2022: Project submission is CLOSED") and is
    corroborated by Google's blog, `DEM-5`: "the next MPW-6 shuttle will accept open source project
    submissions until Monday, June 8, 2022."
- **Verification:** **Verified 2026-09-19.** The five platform pages were fetched with `curl` and
  their schedule lines read directly.
- **How it was counted** (reproducible): the Wayback CDX API lists every archived
  `platform.efabless.com/shuttles*` URL; for each shuttle, a capture was fetched in the
  `/web/<timestamp>id_/` raw form and the two schedule lines extracted.
- **What it says:**

  | Shuttle | Submission opened | Submission closed | **Window** | Submissions (`OPG-1` sheet) | Submissions (`OPG-2` page) | **Per day** (sheet) |
  |---|---|---|---|---|---|---|
  | MPW-1 | 2020-11-12 | 2021-02-19 | **99 d** | 37 | 37 (45 per `DEM-6`/`DEM-7`) | **0.37** (0.45 on 45) |
  | MPW-2 | *not recoverable* | 2021-06-18 (tapeout) | — | 57 | 57 | — |
  | MPW-3 | *not recoverable* | 2021-11-15 (tapeout) | — | 53 | 53 | — |
  | MPW-4 | *not recoverable* | 2021-12-31 (tapeout) | — | 52 | 52 | — |
  | MPW-5 | *not recoverable* | 2022-03-21 (tapeout) | — | 75 | 76 | — |
  | MPW-6 | 2022-04-11 | 2022-06-08 | **58 d** | 90 | 86 | **1.55** |
  | MPW-7 | 2022-07-08 | 2022-09-12 | **66 d** | 106 | 110 | **1.61** |
  | MPW-8 | 2022-11-19 | 2022-12-31 | **42 d** | 147 | 144 | **3.50** |
  | GF MPW-0 | 2022-10-31 | 2022-12-05 | **35 d** | 88 | 86 | **2.51** |
  | GF MPW-1 | 2023-10-28 | 2023-12-11 | **44 d** | 116 | 116 | **2.64** |

- **DERIVED (arithmetic written out; computed with `uv run python` in a throwaway script and
  reproducible from the figures shown):**
  - MPW-1: 2020-11-12 → 2021-02-19 = **99 days**; 37 ÷ 99 = **0.37/day**, 45 ÷ 99 = **0.45/day**.
  - MPW-6: 2022-04-11 → 2022-06-08 = **58 days**; 90 ÷ 58 = **1.55/day**.
  - MPW-7: 2022-07-08 → 2022-09-12 = **66 days**; 106 ÷ 66 = **1.61/day**.
  - MPW-8: 2022-11-19 → 2022-12-31 = **42 days**; 147 ÷ 42 = **3.50/day**.
  - GF MPW-0: 2022-10-31 → 2022-12-05 = **35 days**; 88 ÷ 35 = **2.51/day**.
  - GF MPW-1: 2023-10-28 → 2023-12-11 = **44 days**; 116 ÷ 44 = **2.64/day**.
- **Bears on:**
  - **`ACC-8`'s per-day comparison, which it destroys from the Google side as well as the AFRL side.**
    `ACC-8` divided MPW-1's 45 submissions by **30 days**. Efabless's own platform says the MPW-1
    submission window was **99 days**. The "30 days" in the SkyWater press release (`DEM-4`) and on
    Efabless's marketing page (`DEM-6`) is either how long it took to *fill the 40 slots* or an
    error; it is not the submission window the platform recorded. **Both denominators in `ACC-8` were
    wrong, in opposite directions.**
  - **H5 (supports), on the honest version of the comparison.** Against AFRL's 82 ÷ 78 = 1.05
    proposals a day (`ACC-15`), **four of the six Google shuttles with a recoverable window beat it**,
    and MPW-8 beat it by **3.3×** (3.50 ÷ 1.05). The one Google shuttle that loses is **MPW-1 — the
    one `ACC-8` chose**.
  - **H5 (context) on the metric itself.** Submissions per day of window is a bad measure for a
    programme with a hard 40-slot cap: MPW-8 looks fastest partly because its window was shortest and
    the community already knew the deadline. The reason to compute it is to show that it does not
    support the claim `ACC-8` made with it, not to make the opposite claim.
- **Used in:** [`../analyses/open-access-audit.md`](../analyses/open-access-audit.md) §6.5.
- **Caveats:**
  - **Four of the ten windows are not recoverable.** Every surviving capture of the MPW-2, MPW-3,
    MPW-4 and MPW-5 pages was taken *after* tapeout, and on those captures the template prints the
    same date for "OPEN" and "CLOSED" (both equal to the tapeout date). They are therefore left blank
    rather than guessed. The Wayback CDX API holds no pre-tapeout capture of any of them.
  - The submission counts are the ones already recorded and already disputed: `OPG-1` (the owner's
    sheet) and `OPG-2` (Efabless's own statistics block) disagree by a few on most shuttles and by 8
    on MPW-1, where `DEM-6` and `DEM-7` say 45 and both machine sources say 37. Both are shown.
  - A "window" here is a calendar span, not an exposure: MPW-1 was the first of its kind and had no
    audience; MPW-8 was the eighth and had a community of thousands. Dividing by days does not
    correct for that, which is the point.
