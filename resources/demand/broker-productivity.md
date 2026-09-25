# Designs per staff-member per year at the MPW brokers: is the collapse real?

Entries `PRD-1` … . This file exists to test one number. The repository had established a table —
MOSIS **149** designs per head in 1983/84, Europractice **39.6** in 2025, CMC **5.0** in FY2026 —
and the obvious reading is that a 1984 service running on 1984 computers shipped **30×** more
designs per person than a 2026 service does.

## Verdict on the comparison itself: it does not survive in the form stated

**The 30× gap is mostly a measurement artefact. Three separate errors push in the same direction,
and correcting all three leaves a gap of roughly 1.3× against Europractice and about 10× against
CMC — not 30×.**

1. **1984 is the maximum of a violently noisy MOSIS series, and the series was four points long
   because five of twelve source documents had not been recovered. All five are now recovered**
   (`PRD-1`). On the full 1982–1987 run the figure goes **62 → 128 → 149 → 90 → 62 → 50**. Picking
   1984 as "MOSIS" and 2025 as "Europractice" compares the best year of one service with the latest
   year of another. MOSIS's own last measured year is **49.8 designs per named person**
   (`PRD-2`) — which is *below* Europractice's 2025 figure of 39.6–47.1.
2. **Europractice's 19 and CMC's ~48–65 include people who are not on the fabrication service at
   all; MOSIS's 11 excludes people who were.** Three of Europractice's 19 named contacts are
   design-tools, training and membership, not fabrication (`PRD-4`), and the service distributes
   **65,000 design-tool licence bundles a year** (`PRD-5`). CMC's audited statements put fabrication
   and packaging at **19–34% of expenditure** and fabrication at **18–39% of revenue** (`PRD-6`) —
   the 5.0 figure is a denominator artefact and should be withdrawn in that form. Meanwhile
   MOSIS's roster is a *project-chapter roster inside a university institute*, which excluded the
   **37-person ISI computer centre** that ran MOSIS's machines (`PRD-3`).
3. **The unit is the same, and that part of the comparison is sound.** MOSIS "projects", Europractice
   "designs fabricated" and CMC "prototypes fabricated" all mean *one design placed on a shared
   mask set and manufactured*. This was the thing most likely to kill the comparison and it does
   not (`PRD-2`, `PRD-4`, `PRD-6`).

**What is left after the correction is still a real effect, and the evidence points at one cause
above all the others: batch size.** MOSIS in 1986/87 put **32.8 designs on every fabrication run**
(`PRD-2`). Europractice's 2026 schedule offers **248 distinct technology-and-date submission slots**
for 753 designs a year — **3.0 designs per slot** (`PRD-8`). The per-run labour did not get more
expensive; it got divided among roughly eleven times fewer designs. Portfolio fragmentation, not
headcount bloat, is what the numbers actually show.

Two further causes are documented and both cut in the same direction: **MOSIS refused to check its
customers' designs and Europractice checks every one** (`PRD-7`), and **advancing the node cut
MOSIS's own projects-per-run by 1.9–3.0× and nearly doubled its turnaround, in period, measured by MOSIS**
(`PRD-9`). The "it is all mature nodes anyway" counter is only about one-third true (`PRD-10`).

The legal/NDA hypothesis (H8) is **supported but thinly evidenced**: MOSIS distributed *published,
non-proprietary* design rules and libraries and had no legal function on its roster in any of the
six years recovered; Europractice names a **legal** contact among nineteen (`PRD-11`). No broker
publishes a count of agreements processed, and nothing was found that sizes the cost.

Format and conventions: [`../README.md`](../README.md). Errata against `MOS-*` and `FUNDX-*` are in
the final report to the owner of those files, not applied here.

---

### PRD-1. All five missing ISI Annual Technical Reports are recovered, and the MOSIS staff series is now six consecutive years, 1982–1987 — with 1984's 149 exposed as the peak of a noisy series

- **Source:** the Internet Archive's `dticarchive` mirror of the DTIC technical-report collection.
  The five reports `mosis-funding.md` §16.2 recorded as failed downloads:
  - AD-A127288 — USC/ISI, *1982 Annual Technical Report: A Research Program in Computer Technology*,
    ISI/SR-83-23, covering 1981-07-01 → 1982-06-30. <https://archive.org/details/DTIC_ADA127288>
  - AD-A221184 — USC/ISI, *1986 Annual Technical Report*, ISI/SR-87-178, covering
    1985-07-01 → 1986-06-30. <https://archive.org/details/DTIC_ADA221184>
  - AD-A115915 — USC/ISI, *1980 Annual Technical Report, Volume 1*, ISI/SR-81-19, covering
    1979-10-01 → 1980-09-30. <https://archive.org/details/DTIC_ADA115915>
  - AD-A231025 — USC/ISI, *Final Technical Report*, covering 1981-07-01 → 1989-11-30, dated
    1990-12-31. <https://archive.org/details/DTIC_ADA231025>
  - AD-A121182 — Stanford University Integrated Circuits Laboratory, *Research in VLSI Systems*,
    1982-11. <https://archive.org/details/DTIC_ADA121182> — **not an ISI report at all.**
  Plus the four already read (AD-A145776, AD-A157991, AD-A178085, AD-A224924).
- **Verification:** Verified 2026-09-25. **The recorded workaround is not needed.** Fetching
  `https://archive.org/metadata/DTIC_<id>` returns JSON whose `d1` and `dir` fields give the storage
  node and path directly; `https://<d1><dir>/DTIC_<id>_djvu.txt` then serves the OCR text with no
  redirect and no empty body. All five came down on the first attempt this way, 51 kB to 450 kB
  each. `archive.org/services/search/v1/scrape?q=collection:dticarchive AND title:("Research Program
  in Computer Technology")` returns the whole series — **fourteen items, and no others exist**;
  `archive.org/advancedsearch.php` was returning HTTP 502 "Sorry, we're kinda busy" at the time and
  the `scrape` endpoint is the one that works. Rosters were counted by hand from the OCR of each
  report's VLSI project chapter, exactly as `MOS-3` did.
- **What it says.** Each ISI annual report opens every project chapter with a roster under
  "Research Staff", "Research Assistants" and "Support Staff". The MOSIS chapter is titled "VLSI"
  (and, from 1985, also "Advanced VLSI").
  - **1982 report**, chapter 4 "VLSI--SERVICES AND RESEARCH". Research Staff (**10**): Danny Cohen,
    Yehuda Afek, Ron Ayres, David Booth, Joel Goldberg, George Lewicki, Lee Magnone, Lee Richardson,
    Barden Smith, Vance Tyree. Support Staff (**3**): Victor Brown, Victoria Svoboda, Sharyn Brache.
  - **1986 report**, chapters 5 "ADVANCED VLSI" and 6 "VLSI". **The two chapters print the identical
    roster**, so it is counted once. Research Staff (**12**): George Lewicki, Ron Ayres, Jeff Deifik,
    Joel Goldberg, Wes Hansford, Lee Richardson, Craig Rogers, Carl Service, Bing Sheu, Barden Smith,
    Jeff Sondeen, Vance Tyree. Research Assistants (**8**): David Hollenberg, Ming Hsu, Wen-Jay Hsu,
    Shih-Lien Lu, Mahesh Patil, Vijay Sharma, Je-Hurn Shieh, Eric Shih. Support Staff (**7**):
    Barbara Brockschmidt, Mike Curry, Sam Delatorre, Terry Dosek, Kathie Fry, Terri Lewis, Christine
    Tomovich.
  - **The 1986 and 1987 rosters are the same twenty-seven names in the same order.** `MOS-3` reads
    the 27 as a 1987 figure; it is first printed in the report covering **1985-07-01 → 1986-06-30**
    and repeated verbatim a year later.
  - **1980 report**: no VLSI or MOSIS chapter. MOSIS "became operational in January 1981" (1982
    report, §4.2.1), after the 1980 report's period closed. **There is no 1981 Annual Technical
    Report in the series**, so 1980-10 → 1981-06 is a genuine gap in the record, not a failure to
    find it.
  - **The Final Technical Report (AD-A231025) contains no MOSIS material.** Despite covering
    1981-07-01 → 1989-11-30, it is thirty-one pages holding one chapter, "Computer Research Support".
    A case-insensitive search of its full text for `mosis` and `vlsi` returns **zero** hits.
  - AD-A121182 is Stanford's, not ISI's: "RESEARCH IN VLSI SYSTEMS HEURISTIC PROGRAMMING PROJECT AND
    VLSI THEORY PR..(U) STANFORD UNIV CA INTEGRATED CIRCUITS LAB J HENNESSY ET AL. NOV 82
    MDA903-79-C-0680". It was in the list by mistake.
- **DERIVED (arithmetic written out).** Named people on the MOSIS chapter roster, by reporting
  period, against the IDA calendar-year project series from `MOS-8` (258 · 809 · 1,532 · 1,634 ·
  1,790 · 1,683 for 1981–1986):

  | ISI report | Period | Research | Assistants | Support | **Named** | Projects, calendar yr | **Designs per named person** |
  |---|---|---:|---:|---:|---:|---:|---:|
  | 1982 ATR | 1981-07 → 1982-06 | 10 | 0 | 3 | **13** | 809 (1982) | 809 ÷ 13 = **62.2** |
  | 1983 ATR | 1982-07 → 1983-06 | 8 | 0 | 4 | **12** | 1,532 (1983) | 1,532 ÷ 12 = **127.7** |
  | 1984 ATR | 1983-07 → 1984-06 | 8 | 0 | 3 | **11** | 1,634 (1984) | 1,634 ÷ 11 = **148.5** |
  | 1985 ATR | 1984-07 → 1985-06 | 12 | 0 | 8 | **20** | 1,790 (1985) | 1,790 ÷ 20 = **89.5** |
  | 1986 ATR | 1985-07 → 1986-06 | 12 | 8 | 7 | **27** | 1,683 (1986) | 1,683 ÷ 27 = **62.3** |
  | 1987 ATR | 1986-07 → 1987-11 | 12 | 8 | 7 | **27** (same names) | see `PRD-2` | **49.8** |

  - **The series is 62 → 128 → 149 → 90 → 62 → 50.** It rises by 2.4× in two years and falls by 3.0×
    in three. **1984 is its single highest point.** Quoting 149 as "MOSIS" and comparing it with the
    latest year of any other service is not a like-for-like comparison; it is max against last.
  - **A like-for-like comparison uses last against last.** MOSIS's last measured year is **49.8**
    (`PRD-2`). Europractice's 2025 figure on its published contacts is **39.6**, or **47.1** counting
    only the sixteen who are on the fabrication side (`PRD-4`). **49.8 ÷ 47.1 = 1.06×.** On the
    numbers, the incumbent European brokerage in 2025 is doing roughly what MOSIS did in 1987.
  - **Fabrication runs per reporting period** — counted from each report's own run list or
    technology breakdown: 1982 **19** runs (named list, M17M … M26L), 1983 **36** (20+3+7+4+2),
    1984 **35** (17+5+11+2), 1985 **39** (18+19+2), 1986 **50** (21+22+2+5), 1986/87 **58 over
    seventeen months** = 58 × 12 ÷ 17 = **40.9 a year** (see `PRD-2` on why 58 and not 44). Run
    cadence rose to 1985/86 and then fell back.
- **Bearing: Challenges H6, and challenges the repository's own headline finding.** The claim that
  a subsidised 1980s brokerage was an order of magnitude more productive per head than a modern one
  rests on one year of a six-year series, and that year is the maximum. **This is the most valuable
  single result in this file and it cuts against the thesis.**
- **Bearing: Context for H6 (the part that survives).** Headcount went 13 → 12 → 11 → 20 → 27 → 27
  while projects went 809 → 1,532 → 1,634 → 1,790 → 1,683 → ~1,345. **MOSIS's own productivity per
  head fell by a factor of three between 1984 and 1987, inside one organisation, with one funder,
  one contract and one technology family.** Whatever caused the decline was already operating in
  1985, forty years before Europractice's 2025 report.
- **Used in:** not yet.
- **Caveats:**
  - These are **named people in a project chapter of an annual report**, not FTEs. Victoria Svoboda
    is "Support Staff" in 1983 and "Research Staff" in 1984 — the same person reclassified — which
    is a direct demonstration that the categories are loose.
  - The IDA project series is calendar-year; the rosters are July-to-June. Each row pairs a roster
    with the calendar year its period mostly covers. Shifting the pairing by one year changes 1984's
    148.5 to 1,532 ÷ 11 = 139.3 or 1,790 ÷ 11 = 162.7 — it does not change the shape.
  - 1980-10 → 1981-06 and calendar 1988–1989 have no roster. The 1,880 projects IDA reports for 1989
    cannot be divided by anything.
  - The 1986 and 1987 rosters being identical could mean a stable team or an editing shortcut. The
    conservative reading is taken: 27 in both.

### PRD-2. MOSIS's own contemporaneous count for its last measured year: 1,905 projects in seventeen months — 32.8 designs per run, and 49.8 designs per named person per year

- **Source:** USC/ISI, *1987 Annual Technical Report: A Research Program in Computer Technology*,
  ISI/SR-88-255, covering 1986-07-01 → 1987-11-30, DTIC AD-A224924, §5.3.1 "Completed Fabrication
  Runs". <https://archive.org/details/DTIC_ADA224924>
- **Verification:** Verified 2026-09-25. This table is in a report `MOS-2` and `MOS-3` already cite;
  it was not previously read out. It is the **only place in the whole ISI series where MOSIS prints
  its own project count**, and it prints it per technology, with projects-per-run and measured
  turnaround. **The OCR was not trusted: page 28 of the PDF was rendered at 250 dpi with `pdftoppm`
  and read as an image, and the three lines below are exactly what is printed.** They are also
  internally inconsistent — see the derivation.
- **What it says** (verbatim, confirmed against the page image):

  > "The following is a categoric breakdown by technology of the fabrication runs completed during
  > this reporting period:
  > 12 runs CMOS/Bulk, 2 u 245 projects (20.4 per run) avg T/A 16.6 weeks
  > 22 runs CMOS/Bulk, 3 u 1363 projects (37.9 per run) avg T/A 8.8 weeks
  > 10 runs NMOS, 3 u 297 projects (29.7 per run) avg T/A 7.3 weeks"

  And, on what a "project" is (1986 report, §6.2, identical wording in 1987): "Designers use any
  available design tools to create artwork (layout) files, which are sent to MOSIS via the ARPANET
  or other computer networks. MOSIS compiles a multiproject wafer and contracts with the
  semiconductor industry for mask making, wafer fabrication, and packaging. **MOSIS then delivers
  packaged IC devices to the user.**"
- **DERIVED (arithmetic written out):**
  - **The table does not close, and this has to be dealt with before anything is derived from it.**
    Line 1: 245 ÷ 12 = 20.4 ✓. Line 3: 297 ÷ 10 = 29.7 ✓. **Line 2: 1,363 ÷ 22 = 62.0, not 37.9.**
    Two of the three reproduce exactly, so one number in the middle line is wrong. There are exactly
    two ways to fix it:
    - **Reading C — the run count is wrong.** 1,363 ÷ 37.9 = **36 runs**. Then total runs
      12 + 36 + 10 = **58**, projects **1,905**.
    - **Reading B — the project count is wrong.** 22 × 37.9 = **834 projects**. Then total runs
      **44**, projects 245 + 834 + 297 = **1,376**.
  - **Reading C is the right one, on two independent checks.** First, the same report says the 3 µm
    double-level-metal process had "runs **every other week**" — 26 a year, i.e. 17 ÷ 12 × 26 =
    **37 runs** in this period, for that process alone, before the single-metal double-poly 3 µm
    process is counted. Twenty-two is impossible; thirty-six is exactly right. Second, IDA (`MOS-8`)
    gives 1,683 projects for calendar 1986 and 1,880 for 1989 "after a decline in 1986-1988".
    Reading C annualises to 1,345 a year, a modest decline; Reading B annualises to 971, which would
    require a 42% collapse and a 94% recovery in three years.
  - **Runs (reading C):** **58**. **Projects:** **1,905**.
  - **Period length:** 1986-07-01 → 1987-11-30 is **17 months**. Annualised throughput:
    1,905 × 12 ÷ 17 = **1,345 projects a year**.
  - **Against the roster of 27 (`PRD-1`):** 1,345 ÷ 27 = **49.8 designs per named person per year**.
    **This is the last measured MOSIS productivity figure that exists**, and it is the same under
    reading A (the run counts as printed) because the project total does not change; only reading B
    moves it, to 971 ÷ 27 = 36.0.
  - **Designs per run:** 1,905 ÷ 58 = **32.8** (reading C); 1,905 ÷ 44 = 43.3 (reading A);
    1,376 ÷ 44 = 31.3 (reading B). **All three readings land between 31 and 44, and 32.8 is used
    throughout this file as the conservative figure.** It is consistent with the 1985 GOMAC statement
    in `MOS-4` that runs "carry a large number of users (typically about 40)".
  - **Annualised run cadence:** 58 × 12 ÷ 17 = **40.9 runs a year**, one every 8.9 days —
    consistent with IDA's "almost one per week" (`MOS-8`) and with 50 runs in 1985/86 (`PRD-1`).
- **Bearing: Challenges H6 (against the 30× reading).** 49.8 designs per named person is
  **0.33× the 1984 figure of 148.5** and **1.06× Europractice's 2025 fabrication-side figure of
  47.1** (`PRD-4`). The "1984 versus 2026" comparison compares MOSIS at its peak with a modern
  service at its trough; MOSIS at its own end-point is not more productive than Europractice now.
- **Bearing: Supports H6 (on where the productivity actually lives).** 32.8 designs per run is the
  number that matters. It is the denominator the per-run fixed labour — reticle assembly, vendor
  interface, wafer acceptance, sawing, packaging, distribution — gets divided by. See `PRD-8`.
- **Used in:** not yet.
- **Caveats:**
  - **The source table is internally inconsistent** and the resolution above, though well supported,
    is a reconstruction. Anyone quoting this entry must quote the inconsistency with it.
  - The seventeen-month period is unusual and stated in the report ("Contract expiration date 30
    November 1989"; the reporting period is printed on the title page). Annualising assumes a flat
    rate within it.
  - "Projects" here counts *projects placed on completed runs*, not orders, not customers, and not
    parts delivered. A user who iterated twice in the period is two projects.
  - The three lines do not include SOS or wafer-scale integration, which the 1986 report lists
    separately. If those ran in 1986/87 and are omitted, the true total is **higher** and 49.8 is a
    floor.

### PRD-3. MOSIS's 11 people were a project-chapter roster inside a 200-person institute — the 37-person computer centre that ran MOSIS's machines was a different chapter, and at least one person is on both

- **Sources:** USC/ISI *1986 Annual Technical Report* (AD-A221184), chapter 6 "VLSI" and chapter 11
  "Computer Research Support"; USC/ISI *Final Technical Report* (AD-A231025), chapter 1 "Computer
  Research Support"; USC/ISI *1985 Annual Technical Report* (AD-A178085), §10.3.2.
- **Verification:** Verified 2026-09-25 from the OCR text of all three. Names counted by hand.
- **What it says:**
  - The 1986 report's **chapter 11, "Computer Research Support"**, names Director Ronald Ohlander
    plus Software (**10**), Hardware (**7**), Operations and Network Services (**16**) and Support
    Staff (**3**) — **37 people**.
  - That group ran the machines MOSIS ran on. The 1985 report, §10.3.2, verbatim: "**A substantial
    effort was made in this reporting period to transition the computing support for MOSIS from
    operating on two KLs to a number of clustered VAX-11/750s.** The transition is almost entirely
    complete; all that remains on the KLs is the MOSIS message service."
  - **Christine Tomovich is listed in both chapters of the same report** — in the MOSIS Support Staff
    roster and in Computer Research Support, Operations and Network Services. The rosters are
    allocations of named people to projects, and they overlap.
  - MDA903-81-C-0335 was an umbrella contract covering nineteen numbered projects, of which MOSIS
    was two (`MOS-2`). Accounting, contracts, procurement, personnel and facilities at USC and ISI
    appear in **no** chapter roster.
  - **Both sides subcontract the fab.** The 1986 report lists MOSIS's components as including
    "fabrication of E-beam mask sets (**via subcontract**)", "fabrication of wafer lots (**via
    subcontract**)" and "wafer sawing, die packaging, and bonding (**via subcontract**)". Europractice
    and CMC do the same. On this point the comparison is symmetric and fair.
- **DERIVED (arithmetic written out):**
  - If even a quarter of the 37-person computer centre's effort was MOSIS's — a guess, and flagged as
    one — the 1986 denominator is 27 + 9 = **36**, and 1,683 ÷ 36 = **46.8** rather than 62.3.
    Applying the same quarter-share to 1984's eleven: 11 + 9 = 20, and 1,634 ÷ 20 = **81.7** rather
    than 148.5. **Nothing in the record apportions the computer centre**, and this arithmetic is
    shown only to size the direction of the error, which is that **MOSIS's published headcount is a
    floor and the productivity figures derived from it are ceilings.**
- **Bearing: Challenges H6.** The MOSIS side of the comparison is systematically understated by an
  unknown amount, and the modern side (a named-contacts count for Europractice, a whole-organisation
  count for CMC) is overstated by an unknown amount. **The two errors point the same way and both
  inflate the gap.**
- **Used in:** not yet.
- **Caveats:** the 25% figure above is illustrative and is **not evidence**. No document apportions
  ISI shared services to projects.

### PRD-4. Europractice's 753 means designs *fabricated*, the same unit as MOSIS's "projects" — but three of the nineteen named people are design tools, training and membership, not fabrication

- **Source:** EUROPRACTICE, *Activity Report 2025*, §"RESULTS 2025: MPW PROTOTYPING" (p. 15) and
  "CONTACT INFORMATION" (p. 68).
  <https://europractice-ic.com/wp-content/uploads/2026/03/Europractice_AR2025_web.pdf>
- **Verification:** Verified 2026-09-25. Downloaded with `curl`, converted with `pdftotext -layout`,
  both pages read in full.
- **What it says:**
  - The unit, verbatim: "**In line with this focus, 753 designs were fabricated through Europractice
    MPW services in 2025 by users from academic and research institutions worldwide.** The majority
    came from Europe: 85% of all designs originated from Europractice member institutions in the EU
    and the rest of the EMEA region."
  - The coordinator's letter uses the submission wording instead: "Our users submitted 753 designs
    across 14 foundries" — **the same number is described once as submitted and once as fabricated
    in the same document.**
  - Also in the same units: "Germany (**175 prototypes**), France (80), Switzerland (78), and Italy
    (62) leading in the number of fabricated prototypes", and "**172 prototypes fabricated**" at
    65 nm.
  - **The contact page splits the nineteen by function, and the split is printed on the page.** Three
    blocks: "For general information or enquiries about Europractice, please contact the project
    coordination team at imec" — Romano Hoofman (general), Paul Malisse (operational), **Josef
    Stoudek (legal)**; "For enquiries about Europractice **academic membership, design tools or
    training courses**, please contact the Microelectronics Support Centre, STFC Rutherford Appleton
    Laboratory" — Mark Willoughby (design tools), Clive Holmes (training courses), Richard Bishop
    (academic membership); "For enquiries about Europractice smart system integration" — Simon Toft
    Sørensen. Then: "For more specific enquiries **concerning technology access, MPW schedules, and
    related customer support**" — twelve foundry-specific contacts across imec, Fraunhofer IIS and
    CIME-P.
- **DERIVED (arithmetic written out):**
  - **Fabrication-facing named people, 2025:** 19 total − 3 UKRI-STFC (design tools, training,
    membership, all three behind one generic mailbox and none of them on the fabrication side) =
    **16**.
  - 753 ÷ 16 = **47.1 designs per fabrication-facing named person per year**, against `FUNDX-5`'s
    753 ÷ 19 = **39.6**. The correction is **+19%**.
  - Against MOSIS's last measured year (`PRD-2`, 49.8): **49.8 ÷ 47.1 = 1.06×.**
  - Against MOSIS's best year (`PRD-1`, 148.5): **148.5 ÷ 47.1 = 3.2×**, not 3.8× and not 30×.
- **Bearing: Challenges H6 (on the comparison).** Once the unit and the denominator are matched,
  Europractice in 2025 is within 6% of MOSIS in 1987. The order-of-magnitude claim does not hold
  against Europractice at all.
- **Bearing: Context for H8.** One of nineteen named Europractice people has the single word
  **"legal"** after their name. Six years of MOSIS rosters (`PRD-1`) contain no legal, contracts or
  compliance role of any kind.
- **Used in:** not yet.
- **Caveats:**
  - **16 is still a named-contacts count, not a headcount**, and `FUNDX-5`'s caveat stands in full:
    accounts, procurement, IT, reticle assembly and the people who actually run the runs are
    invisible to it. **If the true fabrication establishment is 30 rather than 16, the figure is
    25.1 and MOSIS 1987 beats it 2.0×.** This is the single largest unresolved uncertainty in the
    whole comparison and **no document that gives a Europractice FTE count was found** — see the
    blockers section.
  - Removing STFC entirely assumes none of its three people touch fabrication. The 2017 report routed
    every STFC enquiry to one generic mailbox, so the function has always been presented as
    tools-and-training.
  - "Submitted" and "fabricated" being used for the same 753 means at least one of the two sentences
    is loose. If 753 is submissions and some fraction was not fabricated, Europractice's real figure
    is lower still.

### PRD-5. Europractice is not mainly a fabrication service: it distributes around 65,000 design-tool licence bundles a year

- **Source:** EUROPRACTICE, *Activity Report 2025*, interview with John McLean (UKRI-STFC, retired
  2020, OBE), pp. 22–24, same PDF as `PRD-4`.
- **Verification:** Verified 2026-09-25 from the PDF text.
- **What it says** (the interviewer's question, which states the figure as Europractice's own):

  > "Europractice currently distributes around **65,000 design-tool license bundles every year** — an
  > impressive scale. How did you manage this in practice?"

  McLean's answer: "Each Europractice member institution typically needs many different tools, often
  for large groups of students and researchers. Once you start serving hundreds of institutions, you
  quickly learn that individually tailoring licenses for each one is impossible."

  And on training: "**More than 100 lecturers attend Europractice training activities annually.**"

  And on the split of the service across two organisations: the portal "will redirect you to: Design
  Tool & Training website **europractice.stfc.ac.uk** … Technology & Fabrication website
  **europractice-ic.com**". The service publishes itself as two halves.

  On the institutional scale: "a pan-European chip infrastructure for design innovation, used by
  **more than 600 academic and research institutions**", and "In 2025, we were present at **more
  than 20 events**."
- **DERIVED (arithmetic written out):**
  - **65,000 licence bundles ÷ 753 fabricated designs = 86 licence bundles per design.** Even at one
    minute of human attention per bundle per year that is 65,000 minutes = **1,083 hours ≈ 0.6 of a
    full-time person**; at ten minutes it is six people. **Nothing in the record says which.** The
    point is only that the denominator of "designs per head" is being asked to carry an activity
    two orders of magnitude larger in unit count than fabrication.
  - 600 institutions ÷ 753 designs = **1.3 designs per member institution per year**. Most members
    are there for the tools, not the silicon.
- **Bearing: Challenges H6 (on the comparison).** Europractice's staff are not a fabrication
  brokerage's staff. Dividing 753 designs by any count of Europractice people overstates the cost of
  a design by whatever share of their time goes to tools, training, membership and outreach. This is
  the same error as CMC's (`PRD-6`), one level smaller.
- **Bearing: Context for H8.** MOSIS's users brought their own tools — the 1986 report says "Designers
  use **any available design tools** to create artwork (layout) files". MOSIS never distributed a
  licence. The tool-distribution function is a *response to closed, expensive EDA*, and it is a large
  part of what the modern brokers spend their people on.
- **Used in:** not yet.
- **Caveats:** the 65,000 figure is in the interviewer's question, i.e. Europractice describing
  itself in its own report, not an audited count. "Bundle" is not defined; a bundle may be one tool
  or fifty, and one institution may take many.

### PRD-6. CMC's 5.0 designs per head is a denominator artefact: its own audited statements put fabrication at 19–34% of expenditure and 18–39% of revenue

- **Sources:** Canadian Microelectronics Corporation / Société Canadienne de Micro-électronique,
  audited financial statements, Statement of Revenue and Expenditures:
  - Year ended 2026-03-31 (with 2025 comparatives):
    <https://www.cmc.ca/wp-content/uploads/2026/08/2026-CMC-Financial-Statements-1.pdf>
  - Year ended 2023-03-31 (with 2022 comparatives):
    <https://www.cmc.ca/wp-content/uploads/2023/10/2023-CMC-Financial-Statements-EN.pdf>
  - CMC Microsystems, *Annual Report 2025-26*:
    <https://www.cmc.ca/wp-content/uploads/2026/09/CMCAnnualReport_2025-26_EN.pdf>
- **Verification:** Verified 2026-09-25. All three downloaded with `curl` from the index page
  `https://www.cmc.ca/corporate-reports/` and converted with `pdftotext -layout`. The FY2026
  statement is fund-accounted across four columns (National Design Network, Other, RSF, FABrIC); the
  figures below are the total column.
- **What it says.** FY2026 (year ended 2026-03-31), total column, in Canadian dollars:

  | Line | FY2026 | FY2025 |
  |---|---:|---:|
  | Revenue — non-subscriber fabrication | 3,124,872 | 4,144,356 |
  | Revenue — subscriber fabrication | 726,323 | 1,104,028 |
  | Revenue — subscriptions | 1,001,062 | 979,644 |
  | Revenue — training | 185,057 | 209,154 |
  | Revenue — ISED (grant) | 16,100,612 | 6,388,416 |
  | **Total revenue** | **21,535,763** | **13,419,183** |
  | Expense — salaries and benefits | 7,859,646 | 7,876,088 |
  | Expense — fabrication and packaging, industrial | 2,176,337 | 3,265,455 |
  | Expense — fabrication and packaging, academic | 1,641,088 | 1,672,397 |
  | Expense — **software tools and annual leases** | 2,744,135 | 2,437,108 |
  | Expense — **UR challenge projects** | 3,535,310 | — |
  | Expense — professional fees | 883,951 | 492,296 |
  | Expense — outreach | 462,278 | 289,274 |
  | **Total expenditure** | **20,012,740** | **17,066,020** |

  FY2023, same statement: fabrication and packaging **6,452,356**; software tools and annual leases
  **1,452,722**; salaries and benefits **7,647,774**.

  And what the fabrication number counts, from the annual report: "In 2025/26, **240 advanced
  technology prototypes were fabricated through CMC** … In this five-year period, **MPW manufacturing
  accounted for 1,369 designs, and custom MNT labs were accessed through CMC to manufacture an
  additional 434 designs**" out of 1,803.

  And the scale of everything else CMC does, from the same report: "an international network of
  **over 11,000 researchers and more than 1,200 companies**"; "**Over 50 CAD tools**"; "**40+**
  Canadian Micro-nanotechnology (MNT) Labs"; "In 2025/26, FABrIC delivered **14 training courses**";
  "**110,000 Trained HQP**"; "**8,400 Academic-industry collaborations supported**".
- **DERIVED (arithmetic written out):**
  - **Fabrication share of expenditure.** FY2026: (2,176,337 + 1,641,088) ÷ 20,012,740 =
    3,817,425 ÷ 20,012,740 = **19.1%**. FY2025: (3,265,455 + 1,672,397) ÷ 17,066,020 =
    4,937,852 ÷ 17,066,020 = **28.9%**. FY2023: 6,452,356 ÷ 18,987,114 = **34.0%** (the FY2023 total
    is the sum of the thirteen printed expenditure lines: 7,647,774 + 6,452,356 + 1,452,722 +
    779,199 + 695,294 + 574,255 + 427,055 + 382,353 + 271,628 + 244,298 + 126,126 + 77,702 −
    143,648 = 18,987,114).
  - **Fabrication share of revenue.** FY2026: (3,124,872 + 726,323) ÷ 21,535,763 =
    3,851,195 ÷ 21,535,763 = **17.9%**. FY2025: (4,144,356 + 1,104,028) ÷ 13,419,183 =
    5,248,384 ÷ 13,419,183 = **39.1%**.
  - **Software-tool distribution is growing as a share of the business:** 1,452,722 ÷ 18,987,114 =
    **7.7%** in FY2023 → 2,744,135 ÷ 20,012,740 = **13.7%** in FY2026.
  - **Re-basing the productivity figure.** `FUNDX-6` divides 240 prototypes by 48–65 whole-
    organisation staff to get 5.0 or 4.1. Apportioning staff to the fabrication service in proportion
    to direct fabrication spend gives, for the plausible corners:
    48 × 19% = 9.1 → 240 ÷ 9.1 = **26.3**; 58 × 29% = 16.8 → 240 ÷ 16.8 = **14.3**;
    65 × 34% = 22.1 → 240 ÷ 22.1 = **10.9**.
    **The whole range is 10.9 to 26.3, i.e. two to five times the published 5.0.**
  - **And the numerator is too large as well.** Only 1,369 of 1,803 five-year "designs prototyped"
    were MPW manufacturing: 1,369 ÷ 1,803 = **75.9%**. Applied to FY2026, 240 × 0.759 = **182 MPW
    designs**, with the other 58 made in university cleanrooms CMC brokered access to. Using 182
    and the middle denominator: 182 ÷ 16.8 = **10.8**.
  - **The corrected gap.** MOSIS 1984 at 148.5 against CMC at a middle estimate of 14.3 is
    **10.4×**, not 30×. Against MOSIS's last measured year, 49.8 ÷ 14.3 = **3.5×**.
- **Bearing: Challenges H6, hard, and the published 5.0 should be withdrawn.** CMC's own audited
  accounts say four-fifths of what it spends is not fabrication. A figure that divides its
  fabrication output by its whole payroll measures nothing.
- **Bearing: Supports H6 (the part that survives).** Even re-based, CMC is the outlier: 11–26 designs
  per fabrication-side head against Europractice's 47 and MOSIS's 50. Canada's programme is
  genuinely the least productive per head of the three, by a factor of two to four.
- **Bearing: Context for H5.** CMC serves "over 11,000 researchers and more than 1,200 companies" and
  fabricates 240 prototypes a year. **Forty-six people served for every chip made.** `FUNDX-6` says
  the same thing from the 2018 figures and it is worth repeating with FY2026 numbers.
- **Used in:** not yet.
- **Caveats:**
  - **Apportioning staff pro-rata to direct programme spend is an assumption, not a measurement.**
    Fabrication brokerage may be more or less labour-intensive per dollar than tool distribution.
    CMC publishes no staff split by function, and searching five annual reports and five audited
    statements for one found nothing (`FUNDX` §16.4 records the same negative).
  - **No CMC headcount has been published since 2018.** The 48–65 box is `FUNDX-6`'s, inherited
    whole. `https://www.cmc.ca/wp-json/wp/v2/awsm_team_member?per_page=100` returns
    `x-wp-total: 20` — twenty published team members, but they are board and leadership (Yvon
    Savaria, Bozena Kaminska, Paul Chow and Gord Harling are among them), not an establishment list.
  - "UR challenge projects", CAD $3,535,310 in FY2026 and nil in FY2025, is a new line that is
    neither fabrication nor tools. CMC's activity mix is still moving.
  - Fund accounting means the "total" column mixes restricted and unrestricted money. The ratios
    above are of the totals as printed.

### PRD-7. The job changed: MOSIS explicitly refused to check its customers' designs; Europractice checks every one

- **Sources:**
  - USC/ISI, *1986 Annual Technical Report* (AD-A221184), §6.2 — wording identical in the 1987
    report (AD-A224924), §5.2.
  - EUROPRACTICE, *Activity Report 2025*, §"MULTI PROJECT WAFER AND MINI@SIC RUNS" (p. 7).
- **Verification:** Verified 2026-09-25 from the OCR text and the PDF text respectively.
- **What it says.** MOSIS, 1986, verbatim:

  > "Though MOSIS may be instrumental in providing cells and design tools to the user, **it is the
  > sole responsibility of the user to see that the submitted patterns yield working designs.** One
  > may compare MOSIS to a publisher of conference proceedings compiled from papers submitted in
  > 'camera-ready' form, where the publisher's responsibility is to produce the exact image on the
  > right kind of paper using the appropriate ink and binding — **but not to address the spelling,
  > grammar, syntax, ideas, or concepts of the various papers.**"

  And: "The user perceives MOSIS as a '**black box**' that accepts artwork files electronically and
  responds with packaged IC devices."

  Europractice, 2025, verbatim:

  > "Only prototypes from fully qualified wafers are taken to ensure that the chips delivered will
  > function 'right first time'. To achieve this, **extensive Design Rule and Electrical Rule
  > Checkings are performed on all designs submitted to the Service.**"
- **DERIVED:** none — this is a qualitative difference in scope, and the whole point is that it is
  not quantified anywhere. **Per-design DRC and ERC by the broker is, by construction, labour that
  scales with the number of designs and cannot be amortised over a run.** It is the one cost in this
  file that has to rise one-for-one with throughput.
- **Bearing: Supports H6 (and it is the cleanest causal finding in the file).** The two operators
  describe opposite policies on the same task, forty years apart, each in its own words. MOSIS's
  productivity per head was measured on a service that did *not* do this work. Any comparison of
  designs per head between the two is comparing different jobs.
- **Bearing: Context for H8.** MOSIS could refuse because its design rules were published and
  vendor-independent (`PRD-11`) — a user could run the checks themselves with the same public rule
  set MOSIS used. A modern broker cannot hand the user the sign-off deck, because the sign-off deck
  is the foundry's confidential property. **Closed PDKs move the checking labour from the customer
  to the broker.** That is a mechanism by which openness reduces cost to serve, and it is stated by
  both operators without either of them meaning to say it.
- **Used in:** not yet.
- **Caveats:**
  - MOSIS did do *parametric* quality assurance — it inserted its own test strip on every wafer and
    probed it ("MOSIS's extensive quality-assurance program is aimed primarily at the parametric
    level"). It checked the *fabrication*, not the *design*. The distinction is the point, but it
    means MOSIS was not doing nothing.
  - Europractice says DRC/ERC is performed; it does not say by whom, with how much automation, or at
    what cost. It may be largely a scripted batch job.
  - MOSIS's policy in 1981 or 1994 may not have been its policy in 1986. Only the 1986 and 1987
    reports were checked for this wording; both carry it.

### PRD-8. Batch size, not headcount: MOSIS put 32.8 designs on every run; Europractice's 2026 schedule offers 248 technology-and-date slots for 753 designs — 3.0 per slot

- **Sources:**
  - MOSIS: `PRD-2` (1,905 projects on 58 runs) and `MOS-4` (1985: runs "carry a large number of
    users (typically about 40)").
  - EUROPRACTICE, "Schedules 2026", <https://europractice-ic.com/schedules-prices-2026/>, the full
    year's MPW submission-date grid for every technology.
  - EUROPRACTICE, *Activity Report 2025*, p. 7: "Today, Europractice provides access to **nearly 90
    technologies from more than 20 foundries**, pilot lines, and other manufacturers."
- **Verification:** Verified 2026-09-25. The schedule page was fetched with `curl` (1.2 MB of
  server-rendered HTML) and parsed with a Python script: each technology row carries twelve month
  columns and a day-of-month number in each month that has a submission deadline. The script counted
  rows, filled cells and distinct calendar dates. It is reproducible from the saved HTML.
- **What it says:**
  - **124 technology lines** carry at least one 2026 MPW date. **307 filled month-cells** in total;
    de-duplicating technology lines that appear twice leaves **248 distinct (technology, date)
    submission slots** on **154 distinct calendar dates**.
  - The distribution of run dates per technology: 29 technologies get **one** run date in the whole
    year, 50 get **two**, 28 get **three**, and only ten get six or more. Mean **2.48**.
  - MOSIS in 1985/86 ran **50** fabrication runs across four technology families (nMOS 3/4 µm,
    CMOS/Bulk 3 µm, CMOS/SOS 4 µm, wafer-scale integration), and the 1986 report says its 3 µm
    double-metal CMOS process had "runs **every other week**" while 1.2 µm was "a regular (**once a
    month**) 1.2-micron fabrication run".
- **DERIVED (arithmetic written out):**
  - **MOSIS 1986/87:** 1,905 projects ÷ 58 runs = **32.8 designs per run** (`PRD-2`; 43.3 on the
    alternative reading of the same table).
  - **Europractice 2025/26:** 753 designs ÷ 248 slots = **3.04 designs per slot**; ÷ 154 distinct
    calendar dates = **4.9**; ÷ 307 filled cells = **2.45**.
  - **Ratio:** 32.8 ÷ 3.04 = **10.8×**. Even on the most generous denominator (154 distinct dates),
    32.8 ÷ 4.9 = **6.7×**.
  - **Put the two together.** Designs per head = (designs per run) × (runs per head). MOSIS 1986/87:
    32.8 × (58 × 12 ÷ 17 ÷ 27 = 1.52 runs per head per year) = **49.8** ✓ Europractice 2025:
    3.04 × (248 ÷ 16 = 15.5 slots per fabrication-facing head) = **47.1** ✓ **The modern service
    runs ten times as many shuttle events per person and puts eleven times fewer designs on each.
    The two effects almost exactly cancel.** That identity is the finding: the modern broker is not
    slower per event, it is running far more, far emptier events.
- **Bearing: Supports H6 (and it identifies the mechanism).** The cost of a multi-project-wafer
  brokerage is per-*run*, not per-*design*: one vendor negotiation, one reticle assembly, one
  acceptance test, one packaging lot, one distribution per run. MOSIS amortised that over 43
  customers. Europractice amortises it over three. **Fragmentation of the technology portfolio — 90
  technologies from 20+ foundries instead of four processes from a handful of vendors — is what
  destroyed the productivity, and it happened because customers now want ninety different things.**
- **Bearing: Challenges H5.** Ninety technologies chasing 753 designs a year is a demand curve so
  thin that the average offering runs 2.5 times a year for three customers. That is not a market
  with a long tail of unmet demand; it is a market whose remaining demand is spread too thin to
  batch.
- **Bearing: Context for H11.** This is a queueing result. A service that could hold designs and
  batch them aggressively — rather than publishing 248 fixed slots a year — would move up MOSIS's
  curve without hiring anybody.
- **Used in:** not yet.
- **Caveats:**
  - **A scheduled slot is not a run that happened.** Some 2026 dates will be cancelled or merged, and
    some technology lines share one physical run (an ams OSRAM 0.35 µm CMOS date and its OPTO variant
    on the same day are almost certainly one reticle). **The true run count is lower than 248 and
    the true designs-per-run is higher than 3.04.** The 154-distinct-dates figure of 4.9 is the
    conservative bound and even that is 6.7× below MOSIS.
  - 753 is calendar 2025 and the schedule is calendar 2026. Europractice's portfolio has been growing,
    so using the 2026 schedule against 2025 designs slightly overstates the fragmentation.
  - MOSIS's 32.8 counts only three technology lines in a seventeen-month window, from a table whose
    middle row does not close (`PRD-2`'s caveats).
  - The identity in the last derivation is arithmetic, not causation: it decomposes the difference,
    it does not prove which factor moved first.

### PRD-9. Complexity, measured by MOSIS itself in 1987: going from 3 µm to 2 µm cut projects per run by roughly half and nearly doubled turnaround

- **Source:** USC/ISI, *1987 Annual Technical Report* (AD-A224924), §5.3.1, the table quoted in
  `PRD-2`.
- **Verification:** Verified 2026-09-25 from the OCR text.
- **What it says** (verbatim, again):

  > "12 runs CMOS/Bulk, 2 u 245 projects (20.4 per run) avg T/A 16.6 weeks
  > 22 runs CMOS/Bulk, 3 u 1363 projects (37.9 per run) avg T/A 8.8 weeks
  > 10 runs NMOS, 3 u 297 projects (29.7 per run) avg T/A 7.3 weeks"

  And the service-level turnaround MOSIS advertised, from its own reports, year by year: 1982 "a
  design-to-packaged VLSI device turnaround time of **a few weeks**"; 1983, 1984 and 1985 "**four to
  six weeks** for standard technology runs"; 1986 and 1987 "**eight to ten weeks** for standard
  technology runs".
- **DERIVED (arithmetic written out):**
  - **Projects per run, 3 µm against 2 µm:** the report's own figures, **37.9 against 20.4**, give
    37.9 ÷ 20.4 = **1.86×**. `PRD-2` shows the 3 µm line's run count is misprinted; the *per-run*
    figure 37.9 is the one that reconciles with the project count, so it is the one used here. On
    the alternative reading the ratio is 62.0 ÷ 20.4 = 3.04×. **The direction is identical under
    every reading and the size is between 1.9× and 3.0×.**
  - **Turnaround, 3 µm against 2 µm:** 16.6 ÷ 8.8 = **1.89×**.
  - **Advertised turnaround over the life of the service:** "a few weeks" (1982) → 4–6 weeks
    (1983–85) → 8–10 weeks (1986–87). Taking the midpoints, 5 → 9 weeks is **1.8× slower** in three
    years, on the same service, while headcount went 12 → 27.
- **Bearing: Supports H6 (complexity is real, and it was real in 1987).** The advanced-node penalty
  is not a FinFET-era phenomenon. One step of node advance, at 2 µm, inside MOSIS, on MOSIS's own
  numbers, cost it between half and two-thirds of its batch size and nearly doubled its cycle time. **This is the
  best-measured complexity datum in the repository, and it is from 1987.**
- **Bearing: Challenges H6 (against blaming modern nodes specifically).** If a 3 µm → 2 µm step did
  this, then the productivity collapse is a property of *chasing the leading edge*, not of the
  leading edge being at 3 nm. MOSIS's own decline from 149 to 50 (`PRD-1`) coincides exactly with
  its 1985 decision to open an "Advanced VLSI" chapter and chase 2 µm and 1.2 µm (`MOS-3`).
- **Used in:** not yet.
- **Caveats:**
  - Fewer projects per run at 2 µm partly reflects **demand**: fewer users were ready to design at
    2 µm in 1987. Batch size and appetite are confounded here and the report does not separate them.
  - Longer turnaround at 2 µm is partly the vendors' cycle time, not MOSIS's labour.
  - The internal inconsistency in the 3 µm line is noted above and is not resolved.

### PRD-10. The node mix Europractice actually ships: about a third mature, but 22–28 nm is the second-largest group and four universities taped out at 7 nm FinFET in 2025

- **Source:** EUROPRACTICE, *Activity Report 2025*, §"UNPARALLELED TECHNOLOGY MIX" (p. 16).
- **Verification:** Verified 2026-09-25 from the PDF text. The two bar charts on that page
  ("Number of fabricated designs in 2025 per foundry", "…per technology (node)") are raster images
  with no extractable data labels; only the prose figures below could be read.
- **What it says** (verbatim):

  > "**One third of Europractice users still rely on mature, cost-effective technologies with nodes
  > between 0.11µm and 0.35µm.**
  > The second most frequently used group includes nodes from 28 nm to 22 nm. The strong growth in
  > 22-nm uptake is driven not only by GlobalFoundries' 22FDX technology (**95 submitted designs**)
  > but also by the introduction of CEA-Leti's MAD300 … (**39 submitted designs**) …
  > Between these two categories, the 65 nm technology and its associated nodes remain an important
  > option, with **172 prototypes fabricated**.
  > … In 2025, four universities prototyped for the first time in the smallest node offered by
  > Europractice: TSMC's 7nm FinFET."
- **DERIVED (arithmetic written out):**
  - **Mature (0.11–0.35 µm): about one third of 753 ≈ 251 designs.**
  - **65 nm and associates: 172 designs = 172 ÷ 753 = 22.8%.**
  - **22 nm identified by name: 95 + 39 = 134 designs = 17.8%**, before the rest of the 28 nm band.
  - **Residual:** 753 − 251 − 172 − 134 = **196 designs (26%)** across 28 nm, 40 nm, 90 nm, the
    More-than-Moore platforms, photonics, MEMS and 7 nm.
  - **So the mature share is 33%, not the great majority.** Two-thirds of Europractice's designs are
    at 65 nm or below, and the fastest-growing band is 22 nm.
- **Bearing: Mixed on H6.** The brief's counter-argument — "Europractice and CMC ship mostly
  mature-node designs, so complexity is a weak explanation" — is **one-third right and two-thirds
  wrong**. The complexity hypothesis survives, in the weakened form that `PRD-9` supports: it is not
  about FinFET, it is about the number of *different* nodes and the drag each new one imposes.
  Europractice's biggest growth is into a node (22FDX) that did not exist when its staff count was
  13.
- **Bearing: Context for H5.** Four universities taping out at 7 nm in one year, in the whole of
  Europe, is the size of the academic leading-edge demand.
- **Used in:** not yet.
- **Caveats:**
  - "One third of **users**" is not "one third of **designs**"; the derivation above treats them as
    the same and they need not be. The residual of 196 carries the whole of that error.
  - 95 and 39 are "submitted designs"; 172 is "prototypes fabricated". The report mixes the two
    units on one page.
  - CMC's node mix was **not** established. Its annual report says only that "photonics and silicon
    photonics technologies outpace microelectronics designs at 40% of the total" — a materials split,
    not a node split.

### PRD-11. MOSIS's design rules were published and vendor-independent, and no MOSIS roster in six years contains a legal or contracts role; Europractice names a legal contact among nineteen

- **Sources:**
  - USC/ISI, *1987 Annual Technical Report* (AD-A224924), §4.1, and the identical passage in the
    *1986 Annual Technical Report* (AD-A221184), §5.1.
  - USC/ISI *1986 Annual Technical Report*, §6.3.1, on which published rule set MOSIS used.
  - EUROPRACTICE, *Activity Report 2025*, "CONTACT INFORMATION" (p. 68) — quoted in `PRD-4`.
  - EUROPRACTICE, *Activity Report 2025*, p. 7, on open-source PDKs.
- **Verification:** Verified 2026-09-25 from the OCR text and the PDF text.
- **What it says.** MOSIS, 1987, verbatim:

  > "Such an interface is possible, and MOSIS has developed it by defining a standard interface
  > through which many fabricators can be accessed. **This interface includes a set of
  > non-proprietary design rules applicable to a multiple vendor base and scalable with the decreases
  > in feature size expected over the next several years.** … By using the MOSIS Service, a large
  > number of designers are able to develop their designs **with little or no investment of the
  > fabricators' engineering time. Fabricators become involved in a project only when a designer is
  > ready to go into production.**"

  And: "**MOSIS acquires and maintains non-proprietary design libraries fabricable by a multiple
  vendor base and distributes those libraries to its users and to commercial CAD vendors**, who
  install them on their systems and make them available to users."

  Which rules: "MOSIS routinely supports NMOS at 3-micron and 4-micron feature sizes, with buried,
  rather than butting, contacts, **in accordance with the Mead-Conway design rules**" and
  "CMOS/SOS fabrication with 4.0 micron feature size **in accordance with the Caltech design rules.
  All of the SOS vendors support these design rules.**"

  Europractice, 2025: the coordination team at imec is three people — "Romano Hoofman (general),
  Paul Malisse (operational), **Josef Stoudek (legal)**".

  And, on the return of open rule sets: "Europractice now supports the fabrication of designs created
  with open source PDKs. Users can prototype using platforms such as **GlobalFoundries' 180 nm MCU
  and IHP's SG13C and SG13G2**, available through the Europractice service." The 2025 report also
  names IHP, "whose open-source PDKs continue to gain traction", among its **top three foundries by
  number of submitted designs**.
- **DERIVED (arithmetic written out):**
  - **Named legal/contracts roles on the MOSIS chapter roster, 1982 through 1987: zero, in all six
    years, out of 13 + 12 + 11 + 20 + 27 + 27 = 110 name-years** (`PRD-1`).
  - **Named legal roles at Europractice 2025: one of nineteen = 5.3%.**
  - **One of the top three Europractice foundries by design count is an open-PDK foundry (IHP).**
- **Bearing: Supports H8, but weakly, and the honest statement is that the cost is not sized.** The
  1980s service ran on a published, scalable, vendor-independent rule set that any user could hold,
  and it needed no lawyer on the roster. The 2025 service runs on ninety per-foundry confidential
  PDKs and names a lawyer in its top three. That is a genuine structural difference and it is
  consistent with H8. It is **not** proof that legal gating is a large share of the cost: one named
  contact out of nineteen is a thin reed, and **no broker publishes a count of agreements processed,
  a legal or compliance headcount, or a cost line for it.** CMC's audited "professional fees" of
  CAD $883,951 in FY2026 (`PRD-6`) is the closest thing to a number and it is not broken out by
  purpose.
- **Bearing: Supports H8 (the stronger form).** IHP's open-PDK processes are, by Europractice's own
  account, in the **top three** technologies by submitted designs in 2025 — ahead of every other
  European foundry. Where the gate is removed, the volume goes.
- **Bearing: Context for H6.** "Fabricators become involved in a project only when a designer is
  ready to go into production" is the 1987 statement of exactly the interface an API-first service
  needs, and it was possible because the rules were public.
- **Used in:** not yet.
- **Caveats:**
  - A named contact's parenthetical job label is not a staffing statement. Josef Stoudek may be
    part-time on Europractice, and other partners may have legal staff who are not named.
  - MOSIS operated before ITAR's modern semiconductor controls and before foundry PDKs existed in
    their current form; the absence of a legal role in 1984 partly reflects an absent problem, not a
    solved one.
  - No document was found that states how many NDAs, licence agreements or export declarations any
    of the three brokers processes per year. This was searched for and is recorded as a blocker.

### PRD-12. Interfaces multiplied: MOSIS named four wafer vendors and three mask houses in 1982; Europractice offers nearly 90 technologies from more than 20 manufacturers

- **Sources:**
  - USC/ISI, *1982 Annual Technical Report* (AD-A127288), §4.3, "Fabrication runs completed between
    July 1981 and June 1982" — a named list of nineteen runs with mask house, wafer vendor and
    feature size for each.
  - EUROPRACTICE, *Activity Report 2025*, p. 7 and p. 16.
- **Verification:** Verified 2026-09-25 from the OCR text and the PDF text.
- **What it says:**
  - The 1982 run list names, across all nineteen runs, **three mask houses** — MicroMask, UltraTech,
    Sierracin — and **four wafer fabricators** — AMI, ZyMos, HP, ComDial — at 3, 4 and 5 µm.
  - By 1986/87 MOSIS says only that "The MOSIS vendor base has expanded substantially during this
    reporting period" and that "**a single vendor often provides several fabrication
    technologies**"; **it never prints a vendor count again in the series.**
  - Europractice 2025: "Today, Europractice provides access to **nearly 90 technologies from more
    than 20 foundries**, pilot lines, and other manufacturers. A strong focus is placed on
    European-based suppliers, as **17 of them have manufacturing facilities in Europe**." And: "In
    2025, Europractice users fabricated designs in **14 different foundries**."
  - Europractice distributes the vendor relationships across five partner institutions, and
    **duplicates some of them**: `FUNDX-5` establishes that X-FAB has a named contact at imec *and*
    at Fraunhofer IIS, ams OSRAM at Fraunhofer IIS *and* at CIME-P, and silicon photonics at imec
    *and* at CIME-P.
- **DERIVED (arithmetic written out):**
  - **Technologies per fabrication-facing named person.** Europractice: ~90 ÷ 16 = **5.6**;
    on the schedule count, 124 technology lines ÷ 16 = **7.8**. MOSIS 1986/87: four technology
    families ÷ 27 = **0.15**. **A modern Europractice person carries 37 to 52 times as many
    technology relationships as a MOSIS person did.**
  - **Designs per technology.** Europractice: 753 ÷ 90 = **8.4 designs per technology per year**.
    MOSIS 1986/87: 1,905 ÷ 3 = **635**.
- **Bearing: Supports H6, and it answers the question the brief asked not to assume.** More
  foundries means **more** integration work, not less, and the evidence is the designs-per-technology
  ratio: MOSIS's average process carried 635 designs, Europractice's carries 8.4. Each relationship
  has a fixed cost — qualification, PDK version tracking, price negotiation, schedule, a named human
  — and it is now being paid 90 times over for a total volume less than half of MOSIS's.
- **Bearing: Challenges H6 (the fair counter, and `FUNDX-5` states it too).** Breadth is the product.
  Users want 22FDX *and* 0.35 µm high-voltage *and* silicon photonics *and* SiGe BiCMOS, and no
  single-process service would serve them. The cost is not waste; it is what the customers asked for.
- **Used in:** not yet.
- **Caveats:**
  - The 1982 vendor list is one year, and MOSIS's base grew after it. **No later MOSIS vendor count
    was found in any of the ten reports read**, so the comparison is 1982 against 2025 and the
    1986 MOSIS number is unknown.
  - "Nearly 90 technologies" and "124 technology lines on the schedule" count different things
    (process offerings against schedule rows including variants and packaging options).
  - CMC was not counted: its annual report says "100+ Global supply chain vendors; includes 50+
    located in Canada", which is a supply-chain count, not a foundry count.

---

## What I could not get, and why

Named blockers, in rough order of how much they would change the conclusions.

1. **A Europractice FTE count for the service.** This is the single most valuable missing number in
   the whole comparison: everything in `PRD-4` rests on sixteen *named contacts* being a usable proxy
   for the fabrication establishment, and it may be half the truth. Searched: the 2017, 2024 and 2025
   activity reports in full; imec's press kit; Fraunhofer IIS's facts page; Tyndall's annual report;
   the CORDIS reporting tabs for the Europractice grants. **All give institute-wide figures and none
   gives a Europractice figure.** `www.europractice.stfc.ac.uk/welcome.html` and
   `/content/contacts/contacts.html` still return HTTP 404, as `FUNDX` §16.3 records. The Chips JU
   grant 101252350 (Europractice 2.0) would carry a person-month budget in its Annex 1, and Annex 1
   is not published.
2. **A CMC headcount after 2018, and any staff split by function.** `https://www.cmc.ca/wp-json/wp/v2/awsm_team_member?per_page=100`
   works and returns `x-wp-total: 20`, but the twenty are board and leadership. Five annual reports
   and four audited financial statements contain no employee count; the pension note in the FY2026
   statements describes two plans without numbers. **The 10.9–26.3 range in `PRD-6` would collapse to
   a point if CMC published one number.** Ontario's public-sector salary disclosure was not checked;
   CMC is a not-for-profit corporation hosted by Queen's University and may or may not be in scope,
   and that is the next thing to try.
3. **A count of NDAs, PDK licence agreements or export declarations processed per year, by anyone.**
   Searched across Europractice's three activity reports, CMC's annual reports and audited statements,
   and the FP7 reporting documents. **Nothing.** This is the evidence H8 most needs and it does not
   appear to exist in public. CMC's "professional fees" line is the only adjacent number and it is
   undifferentiated.
4. **A quantitative DRC-rule-count or mask-layer comparison across nodes.** Attempted: the Magic
   technology files are fetchable (`http://opencircuitdesign.com/magic/archive/scmos.tech` is the
   real MOSIS SCMOS deck, 131 kB, description "MOSIS Scalable CMOS Technology for Standard Rules";
   `open_pdks`' `sky130/magic/sky130.tech` and `gf180mcu/magic/gf180mcu.tech` fetch from
   `raw.githubusercontent.com`). **They were not counted**, because a Magic tech-file DRC section is
   a tool-specific subset of a sign-off deck and comparing the two would have been a false precision.
   The honest version of this measurement needs the foundry sign-off decks, which are under NDA —
   which is itself the finding. `PRD-9` is the substitute and it is better evidence anyway, because
   it is a measurement of throughput, not of rule counts.
5. **Per-node design counts for Europractice 2025.** The two bar charts on p. 16 of the activity
   report are raster images with no data labels and no underlying table. `PRD-10`'s residual of 196
   designs is the cost of that.
6. **CMC's node mix.** Not published in any form. Only the materials split (40% photonics) is given.
7. **MOSIS project counts for calendar 1987, 1988 and 1989 disaggregated, and any roster for those
   years.** The ISI series ends with the 1987 report; the Final Technical Report (AD-A231025) covers
   1981–1989 but contains only the Computer Research Support chapter and no MOSIS material at all.
   IDA's 1,880 for 1989 therefore has no denominator and never will from this source.
8. **The 1980-10 → 1981-06 gap.** There is no 1981 ISI Annual Technical Report. The
   `archive.org` scrape of the whole `dticarchive` collection for this title returns fourteen items
   and that is the complete series, so this is a gap in what ISI filed, not in what was found.

**Nothing was blocked by a CAPTCHA, a paywall, a login wall or a bot check in this pass.** No
browser was needed; no VNC server was started; no form was submitted, no account created and no
person contacted by any channel. Every fetch was a GET. `archive.org/advancedsearch.php` returned
HTTP 502 "Sorry, we're kinda busy" twice and was replaced by
`archive.org/services/search/v1/scrape`, which is faster and complete.
