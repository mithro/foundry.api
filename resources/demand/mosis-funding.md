# MOSIS: who paid for it, what it charged, and how many people ran it

Entries `MOS-1` … . This file exists because `FUND-5` and `FUND-6` established that the
repository could not compute anything about the longest-running multi-project-wafer service in
history: the claims *"a self-sustaining business for 40 years"* and *"up to $10 million annually at
its peak"* (`SMB-5`) rested on a single promotional article, with no budget, no revenue line, no
staff count and no year for the peak.

This pass went after the primary federal record: DoD budget justification books, the DTIC report
series (through its Internet Archive mirror), USAspending's assistance side, and MOSIS's own site as
archived by the Internet Archive. It found the **dates** of MOSIS's federal funding, the **contract
number** it ran on, **two hard throughput numbers from 1984 and 1985**, a **named headcount for
1984 and 1987**, and an **$17.96 million DARPA cooperative agreement in 2021** that nobody in this
repository knew about. It did **not** find a budget, an accounts statement, or a revenue line, and
the "$10 million at peak" figure is still uncorroborated.

Format and conventions: [`../README.md`](../README.md). Searches and dead ends:
[`search-log.md`](search-log.md) §16.

---

### MOS-1. MOSIS says, in its own words, when its DARPA funding ended (1994) and that after 2000 it took no government funding at all

- **Sources** (Internet Archive copies of `mosis.com`, which is gone from the live web):
  - "History of the MOSIS Educational Program", archived 2010-11-25:
    <https://web.archive.org/web/20101125133617id_/http://www.mosis.com/products/mep/mep-history.html>
  - The same page archived 2006-05-16, 2007-02-08 and 2011-03-14:
    <https://web.archive.org/web/20060516155123id_/http://www.mosis.com/products/mep/mep-history.html>,
    <https://web.archive.org/web/20070208073221id_/http://www.mosis.com/products/mep/mep-history.html>,
    <https://web.archive.org/web/20110314042516id_/http://www.mosis.com/products/mep/mep-history.html>
- **Verification:** Verified 2026-09-25. All four captures were fetched with `curl` in the Wayback
  raw-content `id_` form (`WebFetch` refuses `web.archive.org`; see `search-log.md` §1) and read in
  full. The URL was found by walking the Wayback CDX index for `mosis.com`, not by search.
- **What it says** (verbatim, from the 2010-11-25 capture):
  - "The MOSIS Service has been conducting an educational program since 1986. **From 1986 to 1994,
    this program was jointly funded by DARPA and NSF. In 1994, the DARPA funding for MOSIS and for
    the educational program ended.**"
  - "From 1994 until 1998 the educational program was funded jointly by NSF and MOSIS. When the NSF
    funding ended in 1998, additional funding was obtained from the SIA/SRC and some industrial
    firms to supplement the MOSIS contribution. **This additional funding ended in 2000.** Since
    2000, the funding for the educational program has been provided by MOSIS."
  - And, flatly: "**The MOSIS Service does not receive funding from NSF or any other government
    agency. MOSIS sole source of revenue is derived from its commercial operations.**"
  - On what the free programme covered: the MEP had "an instructional component for support of
    scheduled classes in VLSI design" and "a research component to support unfunded research
    conducted by graduate students and faculty". "Both of these MEP components were offered at no
    cost to the universities."
- **Bears on:**
  - **H6 (supports).** This is the **corroboration `FUND-6` said did not exist**. It is not a
    promotional news item written forty years after the fact: it is MOSIS's own operational page,
    published while the service was running, saying in the present tense that it took no government
    funding and lived on commercial revenue. It is still an unaudited self-description, but it is
    contemporaneous and it is specific.
  - **H6 (qualifies "40 years", hard).** The claim in `SMB-5` is "a self-sustaining business for
    40 years". MOSIS's own page dates the end of DARPA funding to **1994** — thirteen years after
    the service started in January 1981 (`MOS-3`). On MOSIS's own account the self-sustaining period
    is about **1994 → 2020**, roughly **26 years**, not 40, and even that is qualified by NSF money
    to 1998 and SIA/SRC and industry money to 2000 for the educational half. And it ends: `MOS-5`
    records **$17.96 million** of DARPA money arriving in 2021.
  - **H5 (context).** The subsidy chain for the free academic programme — DARPA+NSF, then NSF+MOSIS,
    then SIA/SRC+industry+MOSIS, then MOSIS alone, then nothing after 2020 (`DEM-22`) — is a
    thirty-four-year record of funders leaving one at a time.
- **Used in:** not yet.
- **Caveats:**
  - **This conflicts, mildly, with `FUND-5`.** `FUND-5` records NSF award 9809025 to USC, PI Herbert
    Schorr, running **1998-10-01 → 1999-09-30**, $199,726, explicitly "The MOSIS service, through
    this award, provides low-cost custom and semi-custom VLSI prototyping … to educational
    institutions." MOSIS's history page says NSF funding "ended in 1998". Both can be true if the
    page means the *recurring* NSF programme ended in calendar 1998 and 9809025 was a last, separate
    award; but the page is a summary written years later and should not be treated as a ledger.
  - "Does not receive funding from NSF or any other government agency" is a statement about
    **funding**, not about sales. `FUND-5` shows DARPA and NSF buying fabrication at a published
    "DARPA/NSF PRICE", and `FUND-6` and `MOS-6` show NASA and others buying MPW slots. MOSIS could
    truthfully say it took no funding while a large share of its revenue came from federal
    customers. **Nothing found anywhere states that share.**
  - The sentence appears on the *educational programme's* history page. It is written as a statement
    about the MOSIS Service as a whole, and it reads that way, but it is not on a financial page.

### MOS-2. The DARPA instrument MOSIS ran on: contract MDA903-81-C-0335 to USC/ISI — the number is public, the dollar amount is not

- **Sources** (Internet Archive's mirror of the DTIC technical-report collection, `dticarchive`):
  - George Lewicki, "Prototyping and Small-Volume Parts through MOSIS", USC/ISI Reprint Series
    ISI/RS-85-160, November 1985, reprinted from the GOMAC-85 Digest. DTIC AD-A160735.
    <https://archive.org/details/DTIC_ADA160735> (OCR text:
    <https://archive.org/download/DTIC_ADA160735/DTIC_ADA160735_djvu.txt>)
  - USC/ISI, *1987 Annual Technical Report: A Research Program in Computer Technology*, ISI/SR-88-255,
    covering 1986-07-01 → 1987-11-30. DTIC AD-A224924.
    <https://archive.org/details/DTIC_ADA224924>
  - USC/ISI, *1984 Annual Technical Report: A Research Program in Computer Technology*, ISI/SR-85-150,
    covering July 1983 → June 1984. DTIC AD-A157991. <https://archive.org/details/DTIC_ADA157991>
- **Verification:** Verified 2026-09-25. The OCR text of all three was downloaded from
  `archive.org/download/<id>/<id>_djvu.txt` and read. **`apps.dtic.mil` itself is blocked to
  automated fetching** — every path returns an Azure WAF page reading "The request is blocked." The
  Internet Archive's `dticarchive` collection is a complete, OCR'd, fully fetchable mirror and is
  the route that worked. Quotations below are from OCR of 1980s typescript; obvious OCR damage is
  marked `[sic]`.
- **What it says:**
  - **The contract.** Every one of these ISI reports carries, on its report-documentation page, the
    same procurement instrument: "**8a. NAME OF FUNDING/SPONSORING ORGANIZATION: DARPA … 9.
    PROCUREMENT INSTRUMENT IDENTIFICATION NUMBER: MDA903 81 C 0335**", sponsor address "Defense
    Advanced Research Projects Agency, 1400 Wilson Boulevard, Arlington, VA 22209". The 1987 report
    also prints "Contract expiration date 30 November 1989" and "Contract No. MDA 903 81 C 0335".
  - **The founding date and founder.** 1984 report, §5.1: "**Recognizing this need. DARPA established
    the MOSIS (MOS Implementation Service) system at ISI in January 1981.**" The 1987 report repeats
    it word for word. The 1985 GOMAC paper: "Since 1980, the Information Sciences Institute of the
    University of Southern California has been managing the MOS Implementation System (MOSIS) for
    DARPA's VLSI design research community."
  - **The contract is an umbrella, not a MOSIS line.** MDA903-81-C-0335 funds ISI's whole DARPA
    research programme. In the 1987 report it covers nineteen numbered projects, of which MOSIS is
    two (chapter 4 "Advanced VLSI" and chapter 5 "VLSI") and a third is related (chapter 6 "KITSERV
    VLSI Kit Design Service"). The other sixteen are LISP, expert systems, internet protocols,
    multimedia conferencing, natural language, and DARPA HQ computer support. **No report in this
    series prints a dollar figure, for MOSIS or for the contract.**
  - The 1987 report describes MOSIS's own funding in the past tense: "Under this **completed
    contract**, MOSIS has accomplished the following …" and "MOSIS (**through this now completed
    contract**) has drastically reduced the cost of prototyping".
- **Bears on:**
  - **H6 (context, and it is the missing plumbing).** MOSIS was a *line inside a university
    research contract*, not a programme element with its own budget. That is why `FUND-6` could not
    find it in FPDS and why `MOS-4` cannot find it in DARPA's budget books: **it never had a public
    budget line of its own.** The absence of a number is a structural fact about how it was funded,
    not a gap in the searching.
  - **H6 (challenges the strong reading of "self-sustaining").** For at least 1981 → 1989 MOSIS's
    staff were paid out of a DARPA cost-reimbursement contract. Whatever "self-sustaining" means, it
    does not mean the first decade.
- **Used in:** not yet.
- **Caveats:**
  - The contract number is the *reporting* instrument. There may have been separate DARPA task
    orders or follow-on contracts for MOSIS specifically; none was found.
  - "Contract expiration date 30 November 1989" is the expiry printed in the 1987 report, which is
    dated July 1990. It does not establish what replaced it. `MOS-1` puts the end of DARPA money at
    1994, five years later, so at least one further instrument existed and was not found.

### MOS-3. How many people ran MOSIS: 11 named staff in 1984, 27 in 1987 — from ISI's own reports to DARPA

- **Sources:** the 1984 and 1987 ISI Annual Technical Reports cited in `MOS-2`
  (DTIC AD-A157991 and AD-A224924).
- **Verification:** Verified 2026-09-25, counted by hand from the OCR text of each report's project
  chapter. Each chapter of an ISI annual report opens with a roster under the headings "Research
  Staff", "Research Assistants" and "Support Staff".
- **How it was counted:** For 1984, chapter 5 "VLSI" is the MOSIS chapter; its two rosters were
  counted. For 1987, MOSIS occupies chapters 4 "Advanced VLSI" and 5 "VLSI"; **the two chapters
  print the identical roster**, so the names were counted once, not twice.
- **What it says:**
  - **1984 report** (period July 1983 → June 1984), chapter 5 "VLSI".
    Research Staff (**8**): George Lewicki, Ron Ayres, Danny Cohen, Joel Goldberg, Lee Richardson,
    Barden Smith, Victoria Svoboda, Vance Tyree.
    Support Staff (**3**): Kathie Fry, Terri Lewis, Jasmin Witthoft.
  - **1987 report** (period 1986-07-01 → 1987-11-30), chapters 4 and 5, identical roster.
    Research Staff (**12**): George Lewicki, Ron Ayres, Jeff Deifik, Joel Goldberg, Wes Hansford,
    Lee Richardson, Craig Rogers, Carl Service, Bing Sheu, Barden Smith, Jeff Sondeen, Vance Tyree.
    Research Assistants (**8**): David Hollenberg, Ming Hsu, Wen-Jay Hsu, Shih-Lien Lu, Mahesh Patil
    [OCR: "Mahesb"], Vijay Sharma, Je-Hurn Shieh, Eric Shih.
    Support Staff (**7**): Barbara Brockschmidt, Mike Curry, Sam Delatorre, Terry Dosek, Kathie Fry,
    Terri Lewis, Christine Tomovich.
- **DERIVED (arithmetic written out):**
  - **1984: 8 + 3 = 11 named people.** **1987: 12 + 8 + 7 = 27 named people.**
  - Against `MOS-4`'s throughput: at "approximately 1600 design projects per year" (1985) and a
    headcount between 11 and 27, that is **1600 ÷ 11 = 145** to **1600 ÷ 27 = 59 design projects per
    person per year**. Take the midpoint headcount of 19: **1600 ÷ 19 ≈ 84 designs per person per
    year**, or about **one design per person every three working days**.
  - Against the peak claim in `SMB-5` — "around 3,000 orders per year", "up to $10 million" — a
    27-person service at $10m of revenue is **$10,000,000 ÷ 27 = $370,370 of revenue per head**.
    That is a plausible figure for a 1990s technical service business but it is **a derivation
    across two sources twenty years apart and should not be quoted as a MOSIS number.**
- **Bears on:**
  - **H6 (supports, and this is the point the task asked for).** The question was whether services
    like this are expensive because they are **staffed** rather than automated. On the only two
    dated rosters that exist, MOSIS ran **1,600 design projects a year with a double-digit
    headcount**. That is not a labour-intensive concierge operation; it is a small team running a
    pipeline. Compare `FUND-7`: CMC Microsystems spent **CAD $5.29 m on salaries in FY2008, 53.5% of
    all spending**, to deliver far fewer designs. MOSIS's cost structure, to the extent it can be
    inferred at all, looks lighter.
  - **H6 (challenges).** Eleven to twenty-seven people is still a real fixed cost. At, say,
    $100k fully loaded per head in the late 1980s, 27 heads is **$2.7 m a year** before a single
    wafer is bought. Against `MOS-4`'s 1,600 projects that is **$1,688 per design of pure overhead**
    — the same order as the whole DARPA/NSF TinyChip price of **$510** in `FUND-5` and as
    `FUND-6`'s derived **$3,333** per order at peak. **The staffing cost is not a rounding error
    against the price; it is most of it.** The $100k figure is our assumption, not a source.
- **Used in:** not yet.
- **Caveats:**
  - These are **named people on a project roster in an annual report**, not full-time equivalents
    and not a payroll. Several names (Danny Cohen, Bing Sheu) are senior ISI figures who almost
    certainly split time across projects, and the eight "Research Assistants" in 1987 are graduate
    students.
  - Only two years were recovered. Fourteen ISI Annual Technical Reports exist in the DTIC series
    (1975 through 1987); the OCR text of seven of the twelve requested came down on the first
    attempt and the rest failed silently (see [`search-log.md`](search-log.md) §16.2). **If those
    are read, this becomes a time series rather than two points**, and it is cheap to do.
  - The 1987 chapters 4 and 5 sharing one roster could mean one team served both, or could be an
    editing shortcut in the report. The reading here is the conservative one — count once.

### MOS-4. What MOSIS actually did, in its own numbers, in 1984 and 1985: 35 fabrication runs a year, then ~1,600 design projects a year for 100+ organisations

- **Sources:** the 1984 ISI Annual Technical Report (DTIC AD-A157991) and Lewicki's November 1985
  GOMAC paper (DTIC AD-A160735), both cited in `MOS-2`.
- **Verification:** Verified 2026-09-25, read in the OCR text.
- **What it says:**
  - **1985, verbatim:** "**MOSIS currently handles approximately 1600 design projects per year for
    over 100 separate organizations.** All communication between MOSIS and its design community is
    conducted over the ARPANET, a government-sponsored computer communications network."
  - **1985, on run size:** prototyping runs "carry a large number of users (**typically about 40**)".
    Small-volume production runs "are initiated on request and **typically serve from one to three
    users**".
  - **1984, runs completed in the reporting period** (July 1983 → June 1984): "17 runs nMOS.
    4 microns / 5 runs nMOS, 3 microns / 11 runs CMOS/Bulk, 3 microns / 2 runs CMOS/SOS".
  - **1987, the economics MOSIS claimed:** a dedicated prototype iteration "means paying on the order
    of **$30K to $50K** for each iteration of a prototype design … to generate masks and to buy a
    minimum lot of ten wafers". MOSIS instead bought "Minimum lots of ten wafers … but these ten
    wafers hold **ten to thirty projects** instead of only one. This means that the $30K to $50K run
    cost can be apportioned among those ten to thirty users." And: "A cost reduction of **one to two
    orders of magnitude** has been achieved by sharing a single fabrication run among many users."
  - **1984, turnaround:** "four to six weeks for standard technology runs". **1987:** "eight to ten
    weeks" — it got *slower*.
- **DERIVED (arithmetic written out):**
  - **1984 runs:** 17 + 5 + 11 + 2 = **35 fabrication runs** in twelve months, i.e. about **one run
    every ten and a half days**.
  - **Designs per run, 1984:** if 35 runs carried the 1985 figure of ~40 users each, that is
    35 × 40 = **1,400 projects** — consistent with the 1,600 stated a year later, and a check that
    the two numbers are describing the same service.
  - **Against MOSIS's own cumulative counter (`FUND-6`).** 1,600 designs a year in 1985 against
    "50,000 designs and more than 20 years of experience" by 2002 (50,000 ÷ 21 = **2,381/yr**) and
    an implied **455/yr** for 2002 → 2024. So: **1,600 a year in 1985, ~2,400 a year average over
    1981–2002, ~455 a year over 2002–2024.** The 1985 figure is the first *dated, primary,
    contemporaneous* throughput number this repository has for MOSIS, and it sits below the
    1981–2002 average, which is what you would expect if the peak came later.
  - **Against the "3,000 orders at peak" claim (`SMB-5`):** 1985's 1,600 is **53%** of the claimed
    peak. The claim is therefore not absurd — but the peak year is still unknown.
  - **Against `DEM-22`'s free-programme number:** the MEP ran "nearly 7000 student IC designs" over
    2000–2009, about **700 a year**. If total throughput in that decade was near the 455/yr implied
    by the cumulative counter, then **the free academic programme was larger than the whole paying
    business** — which cannot both be true, and is a strong hint that the "more than 50,000" counter
    was stale, exactly as `FUND-6`'s caveat warned.
- **Bears on:**
  - **H5 (challenges).** The aggregated American long tail for prototype chips reached roughly
    1,600 designs a year across "over 100 separate organizations" **in 1985**, when a chip design
    was a heroic act requiring ARPANET access. Forty years of cheaper EDA, open PDKs and the
    internet did not multiply that; `FUND-6` shows the rate falling. **The demand curve for
    prototype silicon did not respond to cost the way the latent-demand story requires.**
  - **H5 (context).** "over 100 separate organizations" is the size of the customer base of the
    only game in town, in the country that invented the technology, at the height of its DARPA
    funding.
  - **H6 (supports).** "the $30K to $50K run cost can be apportioned among those ten to thirty
    users" is the shuttle arithmetic stated by the operator, in period, with numbers.
- **Used in:** not yet.
- **Caveats:**
  - "Design projects" is not the same unit as "orders" (`SMB-5`), "designs" (the cumulative
    counter), or "tape-outs". A single design project may generate several fabrication orders.
    **The three series in this file are not strictly commensurable** and are compared above only for
    order of magnitude.
  - "approximately" and "over 100" are the source's own hedges.
  - The 1984 run count is for a **twelve-month reporting period**, not a calendar year.

### MOS-5. $17,958,805 of DARPA money reached MOSIS in January 2021 — an Air Force cooperative agreement for Intel 22FFL access

- **Sources:**
  - USAspending award `ASST_NON_FA86502121010_097`, FAIN **FA86502121010**:
    <https://www.usaspending.gov/award/ASST_NON_FA86502121010_097>
    (read through the public API, `https://api.usaspending.gov/api/v2/awards/ASST_NON_FA86502121010_097/`
    and `https://api.usaspending.gov/api/v2/transactions/`)
- **Verification:** Verified 2026-09-25. The award record and all four transactions were read from
  USAspending's public JSON API. **`search-log.md` §13 recorded USAspending as unreachable because
  its award-search endpoints are POST-only and that session was GET-only. `curl -X POST` works
  perfectly well; the blocker was the tool, not the site.** See `search-log.md` §16.
- **What it says:**
  - Recipient **University of Southern California**, UEI G88KLJR3KYT5, 3720 S Flower St, Los Angeles.
  - Description, verbatim: "**ACCESS TO INTELS 22FFL TECHNOLOGY THROUGH THE MOSIS-INTEL ALLIANCE
    (ATMI)**" (later modifications correct it to "INTEL'S").
  - Instrument type **05, "COOPERATIVE AGREEMENT (B)"** — assistance, not a purchase.
  - **CFDA 12.910**, whose agency is given as "**DEFENSE ADVANCED RESEARCH PROJECTS AGENCY (DARPA),
    DEPT OF DEFENSE**". Awarding and funding office: "FA8650 USAF AFMC AFRL PZL AFRL/PZL" and
    "F4FBBL AFRL RYD" — i.e. **DARPA money placed through the Air Force Research Laboratory.**
  - Transactions: **2021-01-08, action type "NEW", federal action obligation $17,958,805.00**;
    2022-12-16 continuation $0; 2023-10-30 continuation $0; **2025-01-24, "ADJUSTMENT TO COMPLETED
    PROJECT", −$151,534.47**. Period of performance as recorded: 2021-01-08 → 2022-04-08, last
    modified 2025-01-31.
- **DERIVED (arithmetic written out):**
  - Net obligated: 17,958,805.00 − 151,534.47 = **$17,807,270.53**, which is the total USAspending
    reports.
  - Against the peak-revenue claim in `SMB-5`: **$17.81 m is 1.78× "up to $10 million annually at
    its peak"**. A single federal instrument, in one year, was larger than MOSIS's claimed best
    commercial year.
  - Against everything `FUND-6` could find in FPDS-NG — **$54,300 across three USC actions** — this
    one award is **328×** that total. `FUND-6`'s conclusion that "FPDS-NG knows almost nothing about
    MOSIS" was right; the reason is that **the money was assistance, not procurement**, and FPDS
    does not carry assistance at all.
- **Bears on:**
  - **H6 (challenges, hard).** This is the single most damaging fact in this file for the
    "self-sustaining business" story. Whatever was true from 1994 to 2020, in **January 2021** MOSIS
    took an eighteen-million-dollar DARPA cooperative agreement — and it did so in the same period
    in which its free academic programme was being withdrawn for lack of funding (`DEM-22`, 2020)
    and two years before MOSIS 2.0 was set up under CA DREAMS with a stated goal of "achieve
    self-sustainability within the next few years" (`SMB-5`).
  - **H6 (context).** The instrument type matters and cuts against `FUND-5`'s clean story. `FUND-5`
    showed federal money arriving as **pre-paid purchases at a published discount** — a business
    selling to a government. ATMI is a **cooperative agreement**: assistance, with the government
    as a partner in the work, not a customer at a price list. **Both mechanisms are real, and they
    are not the same mechanism.**
  - **H5 (context).** What the money bought was *access to one company's process node* — Intel
    22FFL. The binding constraint being relieved was not designer demand; it was a foundry
    relationship.
- **Used in:** not yet.
- **Caveats:**
  - USAspending's period of performance (2021-01-08 → 2022-04-08) is plainly not the whole story:
    there are continuation modifications in 2022 and 2023 and a closeout in 2025. The dates in the
    record should be treated as the record's, not as the project's.
  - **Nothing found says how much of the $17.96 m USC kept.** An access agreement of this kind
    plausibly passes most of the money to the foundry. If so it says nothing about MOSIS's operating
    cost — the same ambiguity `FUND-6` flagged for the "$10 million" figure.
  - This is one award found by a keyword search on "MOSIS" in the award description. **Awards to USC
    that do not spell "MOSIS" in the description would not appear**, and USAspending's assistance
    data does not reach before FY2008 at all.

### MOS-6. Federal agencies were still buying MOSIS shuttle slots as ordinary purchases — four NASA orders, $14k–$21k each

- **Sources:** USAspending contract awards, read through the public API keyword search on
  "multi-project wafer":
  - `NNG16PE06P`, 2016-03-15 → 2016-07-01, **$21,261**: "ACQUISITION OF 40 SQ-MM AREA SILICON TILE
    IN A 0.25UM BULK-CMOS PROCESS MULTI-PROJECT WAFER (MPW) FABRICATION RUN FOR 80 PARTS."
  - `NNG14LL77P`, 2014-07-14 → 2014-08-18, **$17,610**: "BULK-CMOS MULTI-PROJECT-WAFER (MPW); LOT OF
    40 TSMC MIXED-MODE MS, QTY., 1 EACH."
  - `NNG13LD02P`, 2012-12-18 → 2012-12-30, **$14,110**: "A 25MM2 AREA (MINIMUM) SILICON TILE IN A
    0.25UM TSMC BULK-CMOS PROCESS MULTI-PROJECT-WAFER (MPW) FABRICATION RUN FOR 40 PARTS (MINIMUM).
    SHIPPING"
  - `NNG16LI06P`, 2016-06-20 → 2020-12-31, **$13,822**: "APPROXIMATELY 32.2 SQ-MM AREA SILICON TILE
    IN A 0.25UM TSMC BULK-CMOS WITH EPITAXIAL (EPI) SUBSTRATE PROCESS MULTI-PROJECT-WAFER (MPW)"
  - All four name **UNIVERSITY OF SOUTHERN CALIFORNIA** as recipient and NASA as awarding agency.
- **Verification:** Verified 2026-09-25 from the USAspending API.
- **DERIVED (arithmetic written out):**
  - Four orders, 2012 → 2016, total 21,261 + 17,610 + 14,110 + 13,822 = **$66,803**, mean
    **$16,701** per order.
  - Add `FUND-6`'s three FPDS actions ($27,000 + $6,500 + $20,800 = $54,300) and the visible federal
    **purchasing** of MOSIS slots over roughly 2005 → 2016 is **$121,103 across seven actions**,
    mean **$17,300**. (Two of `FUND-6`'s three are also NASA; the sets may overlap and the total
    should be treated as an order of magnitude, not a ledger.)
  - **$16,701 mean order against `FUND-6`'s derived $3,333 revenue per order at peak** is **5.0×**.
    These are 0.25 µm tiles of 25–40 mm² with 40–80 packaged parts, i.e. the big end of the product,
    not the TinyChip end.
- **Bears on:**
  - **H6 (supports).** Federal agencies bought MOSIS slots the way any customer would: fixed-price
    purchase orders, at prices that look like a price list. This is the `FUND-5` mechanism still
    running thirty years later.
  - **H5 (challenges).** Seven visible federal purchase actions over roughly a decade, totalling
    about $121k, is **not a market**. If NASA — an agency that designs radiation-hard custom silicon
    for a living — bought four MPW tiles in five years, the "latent demand" from organisations with
    a genuine need for small-volume custom chips is very thin indeed.
- **Used in:** not yet.
- **Caveats:**
  - Keyword search on award descriptions finds only awards whose description happens to say
    "multi-project wafer" or "MOSIS". Purchases described as "integrated circuit fabrication" would
    be missed entirely, and **most purchase orders are described badly**. This is a floor, and
    probably a low one.
  - USAspending's contract data does not reach before FY2008 in this API; `FUND-6`'s FPDS query
    covers roughly 2004 onward. **Neither reaches the 1980s or 1990s.**

### MOS-7. DARPA's own budget justification books, FY2000 → FY2012, name MOSIS exactly once — and never as a funded line

- **Sources:** the Defense-wide RDT&E justification books ("J-books") for the Defense Advanced
  Research Projects Agency, downloaded from the DoD Comptroller:
  `https://comptroller.defense.gov/BudgetMaterials/fy<YEAR>budgetjustification.aspx` → the
  `03_RDT_and_E` DARPA PDF for each of FY2000, FY2001, FY2002, FY2003, FY2004, FY2005, FY2006,
  FY2007, FY2008, FY2009 (two parts), FY2010, FY2011 and FY2012. Example:
  <https://comptroller.defense.gov/Portals/45/Documents/defbudget/fy2001/budget_justification/pdfs/03_RDT_and_E/fy01pb_darpa.pdf>
- **Verification:** Verified 2026-09-25. All fourteen PDFs (about 38 MB, 211,000 lines of extracted
  text) were downloaded with `curl`, converted with `pdftotext -layout`, and searched
  **case-sensitively** for `MOSIS`. A case-insensitive search is useless here: it matches
  "reverse **osmosis**", which appears in the Biological Warfare Defense programme element in
  FY2004, FY2005 and FY2006 and produced three false hits on the first pass.
- **What it says:**
  - **Case-sensitive `MOSIS` hit count by book:** FY2000 **0**, FY2001 **0**, FY2002 **0**,
    FY2003 **0**, FY2004 **0**, FY2005 **0**, FY2006 **0**, FY2007 **0**, FY2008 **0**,
    FY2009 **0**, FY2010 **0**, FY2011 **0**, FY2012 **1**.
  - `Information Sciences Institute`: **0** in all fourteen books.
  - The single FY2012 mention is not a MOSIS budget line. It is inside PE 0603739E "Advanced
    Electronics Technologies", project MT-15 "Mixed Technology Integration", under the heading
    "Compound Semiconductor Materials on Silicon (COSMOS) Multi-Project Wafer (MPW)", FY2010
    **$10.445 million**, and reads, verbatim: "Initiated mask aggregation and support functions for
    eventual transition to the Trusted Access Program Office (TAPO) or **MOSIS** (**a production
    service for chip fabrication**) to facilitate future regular offerings of the technology
    following the early access program."
  - Same entry, on why DARPA ran an MPW at all: "The COSMOS MPW program established a foundry
    capability in order to provide broad access to the DoD and commercial RF/mixed-signal design
    community. This program introduced early access multiproject wafer effort and will support **4
    MPW runs** of increasing sophistication."
- **Bears on:**
  - **H6 (supports `MOS-1`).** Thirteen consecutive years of DARPA's complete public budget
    justification contain no MOSIS funding line. That is exactly what `MOS-1` says should be the
    case: DARPA funding ended in 1994. **Two independent sources now agree, one of them the
    government's own budget.**
  - **H6 (context).** By 2011 DARPA describes MOSIS in the third person as "a production service for
    chip fabrication" it might hand technology *to* — a vendor, not a programme.
  - **H5 (context).** DARPA's own MPW line, COSMOS, cost **$10.445 m in FY2010 alone** to support
    **four runs**. **DERIVED:** $10,445,000 ÷ 4 = **$2.61 m per MPW run**, for a compound-
    semiconductor process. That is what a government pays to stand up shuttle access in a process
    nobody else offers, and it is a useful upper bound against the $30k–$50k-per-run figures in
    `MOS-4`.
- **Used in:** not yet.
- **Caveats:**
  - **These books do not reach the years that matter.** The DoD Comptroller publishes budget
    materials back to FY1998, but the FY1998 and FY1999 pages carry no justification PDFs at all,
    and the FY2000 book is the earliest DARPA J-book available. **MOSIS's DARPA funding ran 1981 →
    1994 (`MOS-1`), entirely before the first available book.** The silence of FY2000–FY2012 is
    consistent with `MOS-1` but cannot confirm it for the funded years — there is nothing to look at.
  - A negative result from text extraction is only as good as the extraction. The books are
    born-digital PDFs with a clean text layer (211,000 lines extracted, "Trusted Access Program
    Office" and "multi-project wafer" both found), so this is a reliable negative, but it is still a
    negative.

---

## 1. Funding timeline — every instrument found, with the gaps named

| Period | Instrument | Amount | Source | Confidence |
|---|---|---|---|---|
| **1981-01 →** | DARPA establishes MOSIS at USC/ISI. Reporting instrument **contract MDA903-81-C-0335**, an umbrella covering ISI's whole DARPA programme (19 projects in 1987) | **not public — no dollar figure in any ISI report, and MOSIS never had a budget line of its own** | `MOS-2` | Verified that the contract exists; **amount not found** |
| 1981 → 1989 | Same contract; 1987 report prints "Contract expiration date 30 November 1989" | not public | `MOS-2` | Verified |
| 1986 → 1994 | MOSIS Educational Program "jointly funded by DARPA and NSF" | not public | `MOS-1` | MOSIS's own statement |
| **1994** | **"In 1994, the DARPA funding for MOSIS and for the educational program ended."** | — | `MOS-1` | MOSIS's own statement, uncorroborated except by the J-book silence |
| 1994 → 1998 | MEP "funded jointly by NSF and MOSIS" | not public | `MOS-1` | MOSIS's own statement |
| 1996-07 → 1997-03 | "MOSIS DIRECT-FUNDING PRICE LIST", column headed "DARPA/NSF PRICE" — agencies pre-paying for fabrication at a discount | per-item prices only; **no total** | `FUND-5` | Verified |
| FY1999 | NSF award **9809025**, USC, PI Herbert Schorr, 1998-10-01 → 1999-09-30 | **$199,726** | `FUND-5` | Verified |
| 1998 → 2000 | MEP supplemented by "SIA/SRC and some industrial firms"; AMI and HP donating wafers | not public; **wafers donated in kind** | `MOS-1`, `FUND-5` | MOSIS's own statement |
| 2000 → 2020 | "the funding for the educational program has been provided by MOSIS"; "MOSIS sole source of revenue is derived from its commercial operations" | — | `MOS-1` | MOSIS's own statement |
| FY2000 → FY2012 | **DARPA RDT&E budget justification: no MOSIS line, in any of thirteen books** | **$0 identifiable** | `MOS-7` | Verified |
| ~2005 → 2016 | Federal agencies (mostly NASA) **buying** MPW slots as purchase orders | **~$121,103 across 7 visible actions**, mean ~$17,300 | `MOS-6`, `FUND-6` | Verified; a floor |
| **2021-01-08** | **DARPA (CFDA 12.910) via AFRL, cooperative agreement FA86502121010, "ACCESS TO INTEL'S 22FFL TECHNOLOGY THROUGH THE MOSIS-INTEL ALLIANCE (ATMI)"** | **$17,958,805 obligated; net $17,807,270.53 after a 2025 closeout adjustment** | `MOS-5` | Verified |
| 2020 | Free academic tape-out programme discontinued | — | `DEM-22` | Verified |
| 2023 → 2028 | MOSIS 2.0 under the CA DREAMS Microelectronics Commons hub; stated goal "achieve self-sustainability within the next few years and generate $20 million in annual revenue" | not public | `SMB-5` | Institutional statement |

**The honest gaps.** There is no dollar figure, anywhere in the public record this pass could reach,
for DARPA's funding of MOSIS in any year between 1981 and 1994 — the years that matter. The reason
is structural and is now understood (`MOS-2`): MOSIS was a chapter inside a university research
contract, not a programme element. There is also no figure for what MOSIS charged in aggregate, in
any year, ever.

## 2. Revenue and cost — what can be established, with the arithmetic

| Quantity | Value | Year | Basis |
|---|---|---|---|
| Design projects handled | **~1,600 per year**, for "**over 100 separate organizations**" | **1985** | `MOS-4`, primary and contemporaneous |
| Fabrication runs completed | **35** (17 + 5 + 11 + 2) | Jul 1983 → Jun 1984 | `MOS-4` |
| Users per prototyping run | "typically about **40**" | 1985 | `MOS-4` |
| Projects per wafer lot | "**ten to thirty** projects" per ten-wafer lot | 1987 | `MOS-4` |
| Cost of a dedicated prototype run, as MOSIS described it | **$30,000 – $50,000** per iteration | 1987 | `MOS-4` |
| **DERIVED** cost per user on a shared run | $30,000 ÷ 30 = **$1,000** to $50,000 ÷ 10 = **$5,000** | 1987 | arithmetic on `MOS-4` |
| Named staff | **11** | Jul 1983 → Jun 1984 | `MOS-3` |
| Named staff | **27** (12 research + 8 research assistants + 7 support) | Jul 1986 → Nov 1987 | `MOS-3` |
| **DERIVED** designs per head per year | 1600 ÷ 11 = **145**; 1600 ÷ 27 = **59**; midpoint ≈ **84** | 1985 vs 1984/1987 rosters | arithmetic on `MOS-3`, `MOS-4` |
| DARPA/NSF TinyChip price | **$510** per project, lot of 4, 2.0 µm, packaging included | 1996-07 → 1997-03 | `FUND-5` |
| Mean federal purchase-order price for an MPW tile | **$16,701** (4 NASA orders); **$17,300** including `FUND-6`'s three | 2005 → 2016 | `MOS-6` |
| Claimed peak orders | "around 3,000 orders per year" | year unknown | `SMB-5`, uncorroborated |
| Claimed peak revenue | "up to $10 million annually" | year unknown | `SMB-5`, uncorroborated |
| **DERIVED** revenue per order at claimed peak | $10,000,000 ÷ 3,000 = **$3,333** | — | `FUND-6` |
| **Largest single federal instrument found** | **$17,958,805** | 2021 | `MOS-5` |
| Operating cost, any year | **not public** | — | — |
| Revenue, any year | **not public** | — | — |
| Profit or surplus, any year | **not public** | — | — |

**The one new cross-check.** `MOS-4` gives 1,600 designs a year in 1985 from a primary source.
`FUND-6` derives 2,381 a year as the 1981–2002 average and 455 a year for 2002–2024 from MOSIS's own
cumulative counter. 1,600 in 1985 sits **below** the early-period average and **3.5×** above the late
one. That is the shape of a service that grew through the late 1980s and 1990s, peaked somewhere in
between, and then fell by roughly **70–80%**. The "around 3,000 at peak" claim in `SMB-5` is
**consistent with** that shape — 1,600 in 1985 rising to 3,000 at some later point is an ordinary
growth curve — which is the first time anything in this repository has been able to say that.

## 3. Verdict on the two claims

**"Up to $10 million annually at its peak" — still uncorroborated, but no longer implausible.**
No second source for the figure was found. No budget, no accounts, no revenue line, no year. What
*has* changed is that the companion claim, "around 3,000 orders per year", now has a primary
anchor: MOSIS handled ~1,600 design projects a year in 1985 (`MOS-4`), so a later peak near 3,000 is
an ordinary doubling rather than an invention. At 3,000 orders and the $16,701 mean federal order
price of `MOS-6`, revenue would be $50 m — far above the claim; at the $510 TinyChip price of
`FUND-5` it would be $1.5 m — far below. **The claim sits between two defensible bounds, which is
all that can honestly be said.** It rests on one sentence in one promotional article and should
continue to be cited that way.

**"A self-sustaining business for 40 years" — corroborated in substance, refuted in its arithmetic.**
`FUND-6` could find no support for this beyond the 2024 article. It now has contemporaneous support
from MOSIS itself: "**The MOSIS Service does not receive funding from NSF or any other government
agency. MOSIS sole source of revenue is derived from its commercial operations**" (`MOS-1`, page
live on `mosis.com` through at least 2011). Thirteen years of DARPA budget books with no MOSIS line
(`MOS-7`) are consistent with it.

But **"40 years" is wrong on MOSIS's own numbers.** By its own history page, DARPA funded MOSIS from
January 1981 until 1994 — **thirteen years**. NSF money continued to 1998 and SIA/SRC and industry
money to 2000, for the educational half. And the period ends at the other end too: in January 2021
MOSIS took a **$17.96 million DARPA cooperative agreement** (`MOS-5`), and from 2023 it has been
inside a federally funded Microelectronics Commons hub whose stated goal is to *become*
self-sustaining (`SMB-5`).

The defensible statement is: **MOSIS was set up and paid for by DARPA for its first thirteen years,
covered its own costs from sales for roughly the twenty-six years from 1994 to 2020, and returned to
federal funding in 2021.** That is a genuinely remarkable record and it is the strongest single piece
of evidence in this repository for H6. It is not what `SMB-5` says.

**What is still missing, and it is the thing that matters.** Covering your costs is not the same as
covering the cost of the *capital*. Nothing found establishes whether MOSIS paid USC for space,
overhead, or the ISI infrastructure it sat on; whether its "self-sustaining" accounting included
university indirect costs; or what it would have cost to start the service without DARPA paying for
the first thirteen years. **A business that was handed thirteen years of runway and a captive
federal customer base is not a proof that the same business can be started cold.**

## 4. Head count — how many people ran MOSIS

**Eleven named people in 1983/84. Twenty-seven in 1986/87.** Both counts are from ISI's own annual
technical reports to DARPA, which print a roster at the head of each project chapter (`MOS-3`).

The 1987 figure splits as 12 research staff, 8 research assistants (graduate students) and 7 support
staff. Removing the students leaves **19 employees** running a service that handled **~1,600 design
projects a year** — about **84 designs per employee per year**, or one every three working days.

This bears directly on the question the task asked: **are these services expensive because they are
staffed rather than automated?** On this evidence, MOSIS was *not* especially labour-intensive for
its era. It was a small team running a highly automated pipeline over the ARPANET — the 1984 report
describes automated vendor templates, computerised geometry processing, and users perceiving MOSIS
as "a black box that accepts artwork files electronically and responds with packaged IC devices"
(`MOS-4`).

But the fixed cost is still real and still large relative to the price. At an assumed $100,000 fully
loaded per head in the late 1980s — **our assumption, not a source** — 27 heads is $2.7 m a year,
which against 1,600 designs is **$1,688 per design of overhead alone**. The DARPA/NSF price for a
TinyChip a decade later was **$510** (`FUND-5`). Those two numbers cannot both be right unless either
throughput was much higher by the mid-1990s, or the TinyChip was cross-subsidised by the large parts,
or the staff cost was carried somewhere other than the price. **Which of those it was is exactly
what no public source says**, and it is the single most valuable unanswered question about MOSIS.

Compare `FUND-7`: CMC Microsystems spent **CAD $5,285,705 on salaries and benefits in FY2008 —
53.5% of all expenditure** — and **CAD $4.0 m, 54.8% of the non-FABrIC base, in FY2026**. Payroll is
over half the cost of running an MPW brokerage, in the only such organisation that publishes
accounts. There is no reason to think MOSIS was different.

## 5. Blocked, and not found

| Source | What happened | Consequence |
|---|---|---|
| **`apps.dtic.mil`** — the Defense Technical Information Center | **Blocked outright to automated fetching.** Every path (`/sti/citations/…`, `/sti/tr/pdf/…`, `/dtic-search/api/v1/search`, `/dtic/tr/fulltext/u2/…`) returns an Azure WAF page: "**The request is blocked.**" `discover.dtic.mil` returns 200 but is a JavaScript application. | **Worked around.** The Internet Archive's `dticarchive` collection is a complete, OCR'd mirror: `https://archive.org/advancedsearch.php?q=collection:dticarchive+AND+<term>&output=json` searches it and `https://archive.org/download/DTIC_AD<number>/DTIC_AD<number>_djvu.txt` returns full text. Everything in `MOS-2`, `MOS-3` and `MOS-4` came through this route. |
| **DARPA J-books before FY2000** | The DoD Comptroller lists budget-material pages back to FY1998, but `budget1998.aspx` and `budget1999.aspx` carry **no justification PDFs**, and there is no `fy1998budgetjustification.aspx`. | **The 1981–1994 DARPA funding years are not covered by any available budget book.** This is the largest single gap in this file. |
| **`crsreports.congress.gov`** | Returns **HTTP 403** to `curl`. | CRS reports were not searched. Some are mirrored in govinfo's GOVPUB collection, which was searched. |
| **`api.govinfo.gov` with `DEMO_KEY`** | Works, and full-text-searches the Congressional Record, hearings, committee prints, the Serial Set and GOVPUB. **But it rate-limits after four or five requests**, returning HTTP 429 for the rest of the hour. | Searched successfully; document downloads were slow. A registered API key would remove this, but **registration requires a form and an email address, which the rules forbid.** |
| **`www.osti.gov/api/v1/records`** | Connection failed outright (curl exit before any HTTP status). | OSTI not searched. |
| **NTRL / NTIS** (`ntrl.ntis.gov`) | Front page returns 200 but the search is a JavaScript application; no public JSON endpoint was found. | Not searched. |
| **USAspending POST endpoints** | **Not blocked.** `search-log.md` §13 recorded them as unreachable because that session was GET-only. `curl -X POST` works. Note two traps: `award_type_codes` must come from **one** group, and `time_period.start_date` **cannot be earlier than 2007-10-01**. | This is how `MOS-5` and `MOS-6` were found. **`search-log.md` §13's blocked-source entry should be corrected.** |
| **Local and trade press** (*Electronic News*, *EE Times* 1980s–90s, Los Angeles and Marina del Rey outlets, USC student and alumni press) | **Not reached.** Every general web search engine remains blocked to automated queries (`search-log.md` §12.1, §13). Without a search engine there is no way to find a 1992 trade-press article. | The owner's "local news is a gold mine" lead is **unworked**. It is the largest unexplored surface. |
| **Oral histories** (Computer History Museum, IEEE History Center) | Not reached, same reason — their catalogues were not locatable without search, and neither site's sitemap was tried. | Conway/Mead-era first-hand accounts of MOSIS's funding are unread. |
| **A MOSIS revenue figure, a budget, an operating cost, or a profit figure for any single year** | **Does not exist in anything reached.** Forty-five years, and there is no accounts statement. | This is the same wall `FUND-6` hit, and it has not moved. |
| **What share of MOSIS's revenue came from federal customers** | Not published anywhere found. | Without it, "self-sustaining" cannot be distinguished from "sustained by government purchasing". |
| **How much of the $17.96 m ATMI award USC kept** | Not published. | `MOS-5`'s bearing on H6 is weaker than it looks if most of it passed to Intel. |
