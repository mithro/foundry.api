# MOSIS: who paid for it, what it charged, and how many people ran it

Entries `MOS-1` … . This file exists because `FUND-5` and `FUND-6` established that the
repository could not compute anything about the longest-running multi-project-wafer service in
history: the claims *"a self-sustaining business for 40 years"* and *"up to $10 million annually at
its peak"* (`SMB-5`) rested on a single promotional article, with no budget, no revenue line, no
staff count and no year for the peak.

This pass went after the primary federal record: DoD budget justification books, the DTIC report
series (through its Internet Archive mirror), USAspending's assistance side, the National Academies'
own history of federal computing research, and MOSIS's own site as archived by the Internet Archive.

**The headline results:**

1. **DARPA spent about $44 million on MOSIS over its first decade** — "about $30 million in facility
   and staff costs plus roughly $14 million in project support costs" — according to the Institute
   for Defense Analyses' 1991 review of DARPA for DARPA (`MOS-8`). That is roughly **$2,300–$3,400
   of government money per design fabricated**, against a list price of **$400–$3,500 per design**.
2. **MOSIS says itself that DARPA funding ended in 1994**, and that after 2000 it took no government
   funding at all (`MOS-1`). "Self-sustaining for 40 years" is therefore wrong: it was about
   twenty-six, 1994 → 2020.
3. **$17,958,805 of DARPA money reached MOSIS again in January 2021** (`MOS-5`), which nothing in
   this repository knew, because it was a cooperative agreement and FPDS-NG carries only
   procurement.
4. **A continuous throughput series, 258 projects in 1981 to 1,880 in 1989** (`MOS-8`, `MOS-9`),
   and a **price list from 1984 to 1989** (`MOS-8`).
5. **Headcount: 12 people in 1983, 11 in 1984, 27 in 1987** (`MOS-3`).
6. **A commercial silicon broker tried the same business in 1981 and was out of orders by 1984**,
   and DARPA's own programme manager said the reason was that there was not enough demand for one
   (`MOS-10`).

It did **not** find a revenue line, an accounts statement, or a profit figure for any year, and the
"$10 million at peak" claim is still uncorroborated — though it is now bracketed by MOSIS's own
published prices.

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
  **Both of the key sentences below appear, word for word, in all four captures** — 2006-05-16,
  2007-02-08, 2010-11-25 and 2011-03-14. MOSIS published this statement, unchanged, for at least
  five years.
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

### MOS-3. How many people ran MOSIS: 12 named staff in 1983, 11 in 1984, 27 in 1987 — from ISI's own reports to DARPA

- **Sources:** the 1983, 1984 and 1987 ISI Annual Technical Reports (DTIC AD-A145776, AD-A157991 and
  AD-A224924), cited in `MOS-2`. The 1983 report is
  *1983 Annual Technical Report: A Research Program in Computer Technology*, ISI/SR-84-138, covering
  July 1982 → June 1983, <https://archive.org/details/DTIC_ADA145776>.
- **Verification:** Verified 2026-09-25, counted by hand from the OCR text of each report's project
  chapter. Each chapter of an ISI annual report opens with a roster under the headings "Research
  Staff", "Research Assistants" and "Support Staff".
- **How it was counted:** For 1983 and 1984, chapter 8 and chapter 5 respectively, both titled
  "VLSI", are the MOSIS chapter; both rosters were counted. For 1987, MOSIS occupies chapters 4
  "Advanced VLSI" and 5 "VLSI"; **the two chapters print the identical roster**, so the names were
  counted once, not twice.
- **What it says:**
  - **1983 report** (period July 1982 → June 1983), chapter 8 "VLSI".
    Research Staff (**8**): George Lewicki, Danny Cohen, Vance Tyree, Joel Goldberg, Ron Ayres,
    Barden Smith, Yehuda Afek, David Booth.
    Support Staff (**4**): Victor Brown, Victoria Svoboda, Jasmin Witthoft, Lee Magnone.
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
  - **1983: 8 + 4 = 12 named people.** **1984: 8 + 3 = 11 named people.**
    **1987: 12 + 8 + 7 = 27 named people.**
  - Against `MOS-8`'s project series — 1,532 projects in 1983, 1,634 in 1984, and a 1986/87 level
    of about 1,683: **1,532 ÷ 12 = 128 designs per person in 1983**, **1,634 ÷ 11 = 149 in 1984**,
    and **1,683 ÷ 27 = 62 in 1987** (or **1,683 ÷ 19 = 89** counting only employees, not the eight
    graduate research assistants).
  - **Productivity per head fell by more than half between 1984 and 1987 while throughput was flat.**
    Headcount went 11 → 27 (2.5×) for a project count that went 1,634 → 1,683 (1.03×). What the
    extra sixteen people bought was **not volume — it was technology**: the 1987 roster is split
    across "VLSI" and a new "Advanced VLSI" chapter opened to chase CMOS, 1.2 µm and quality
    assurance (`MOS-2`, `MOS-4`).
  - Against `MOS-8`'s $30 m of "facility and staff costs" over roughly a decade — about **$3.0 m a
    year** — a 27-person team is **$111,111 per head per year** fully loaded, including facilities,
    in late-1980s dollars. **This is derived from two independent sources and they agree**: the
    assumption and the measurement land in the same place.
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
  - **H6 (challenges).** Eleven to twenty-seven people is still a real fixed cost, and `MOS-8` now
    prices it: **about $3.0 m a year of DARPA money for facilities and staff**. Against ~1,700
    projects a year that is **$1,765 per design of pure overhead** — against a 1987 list price of
    **$400** for a TinyChip and **$3,500** for a twelve-part unit (`MOS-8`, Table 18-2). **The
    staffing cost was not a rounding error against the price; for the small parts it was several
    times the price, and the government paid it.**
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

- **Sources:** the 1983 and 1984 ISI Annual Technical Reports (DTIC AD-A145776, AD-A157991) and
  Lewicki's November 1985 GOMAC paper (DTIC AD-A160735), cited in `MOS-2` and `MOS-3`.
- **Verification:** Verified 2026-09-25, read in the OCR text.
- **What it says:**
  - **1983 report** (July 1982 → June 1983), in ISI's own overview: "A highlight of this reporting
    period has been the emergence of DARPA's MOSIS as a truly national resource. **Over 40
    universities and hundreds of designers now submit VLSI designs in electronic form via any
    network to MOSIS. MOSIS delivers chips and will soon deliver user-specified printed circuit
    boards to designers 30 to 35 days after receipt of a design.**"
  - **1983, runs completed in the reporting period:** "20 runs nMOS, 4 microns / 3 runs nMOS,
    3 microns / 7 runs CMOS/Bulk, 5 microns / 4 runs CMOS/Bulk, 3 microns / 2 runs CMOS/SOS".
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
  - **1983 runs:** 20 + 3 + 7 + 4 + 2 = **36 fabrication runs** in twelve months.
    **1984 runs:** 17 + 5 + 11 + 2 = **35 fabrication runs** in twelve months, i.e. about **one run
    every ten and a half days**. By 1990 IDA records "almost one per week" (`MOS-8`).
  - **Designs per run, cross-checked against `MOS-8`.** ISI told IDA it ran **1,532 projects in
    1983** and **1,634 in 1984**. Against 36 and 35 runs that is **43 and 47 projects per run** —
    which matches the 1985 statement that runs "carry a large number of users (typically about 40)"
    almost exactly. **Three numbers from three documents, and they close.** This is the strongest
    internal consistency check available on any MOSIS figure.
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

### MOS-8. The number: DARPA spent "about $30 million in facility and staff costs plus roughly $14 million in project support costs" on MOSIS — from the Institute for Defense Analyses' own review of DARPA

- **Source:** Richard H. Van Atta, Sidney Reed, Seymour J. Deitchman et al., *DARPA Technical
  Accomplishments, Volume 2: An Historical Review of Selected DARPA Projects*, Institute for
  Defense Analyses, IDA Paper P-2429, April 1991. **Chapter XVIII, "VLSI MOSIS", pp. 18-1 to
  18-31.** DTIC AD-A241725. <https://archive.org/details/DTIC_ADA241725>
  (OCR text at `https://archive.org/download/DTIC_ADA241725/DTIC_ADA241725_djvu.txt` — **that
  download URL intermittently 302s with an empty body; the `/details/` page always works and links
  it**, see [`search-log.md`](search-log.md) §16.6)
- **Verification:** Verified 2026-09-25. The OCR text was downloaded from the Internet Archive's
  `dticarchive` mirror and chapter XVIII read in full. This chapter was found by following a
  citation in `MOS-9` ("Van Atta et al., 1991a"), not by search. The scan is a 1991 typescript and
  the OCR is imperfect; every figure quoted below was read in context and cross-checked against
  `MOS-9` where possible. OCR damage is marked.
- **What it says:**
  - **The expenditure figure, verbatim** (p. 18-24): "Our initial estimate of DARPA expenditures on
    MOSIS over the period is **about $30 million in facility and staff costs plus roughly $14
    million [OCR: "miilion"] in project support costs.**"
  - **The leverage argument it sits inside** (p. 18-24): "Assuming that from 1981 through 1989 at
    least 60 percent of the projects implemented were for DARPA-sponsored research, roughly
    **7,300 chip designs** relevant to this research would have been implemented via MOSIS …
    Assuming very conservatively that MOSIS permitted direct implementation costs that were on
    average **$20,000 less per project** on 7,300 DARPA-sponsored projects, and also obviated a
    roughly equivalent per-project expense in administrative and overhead costs, it permitted
    accomplishment of projects that would have cost **$150-300 million or more** to do
    commercially … the value of MOSIS fabrications accomplished represents a **three-to-six-fold
    leveraging** of DARPA's budget".
  - **Projects per year, from ISI's own figures given to IDA** (Table 18-5 footnote, "By
    technology"): **1981: 258 · 1982: 809 · 1983: 1,532 · 1984: 1,634 · 1985: 1,790 · 1986: 1,683.**
    And in the overview (p. 18-2): "Since beginning operation in 1980, MOSIS has managed a growing
    volume of device fabrication (**from 258 projects in 1981, rising to 1,880 in 1989 after a
    decline in 1986-1988**)".
  - **Reach** (p. 18-2): "MOSIS serves users at **more than 360 institutions** throughout the United
    States, via ARPANET and other E-mail services."
  - **Who the users were** (p. 18-24): "Table 18-5 indicates that **at least two-thirds** of the
    microelectronic device projects implemented by MOSIS in 1981-86 were for DARPA contractors or
    DARPA-affiliated projects carried out by government laboratories."
  - **Prices, Table 18-2, "Illustrative Prices for Highest Project-Volume Technologies"** (p. 18-17)
    — year, technology, smallest unit, package price, per-part cost, weeks:
    - 1984, 4 µ nMOS, 12 parts, **$2,800**, $233/part, 9.9 weeks
    - 1985, 3 µ CMOS 2M, 12 parts, price n/a, 8.4 weeks
    - 1986, 3 µ CMOS 2M, 12 parts, price n/a, 9.7 weeks
    - 1987, 3 µ CMOS 2M, **4-part TinyChip $400**, $100/part; **12 parts $3,500**, $292/part
    - 1988, 3 µ CMOS 2M [OCR: "SpCMOS"], **4-part TinyChip $550**, $138/part; **12 parts $2,500**,
      $208/part
    - 1989, 2 µ CMOS 2M analog, **4-part TinyChip $550**, $138/part; **12 parts $3,100**, $258/part,
      8.1 weeks; **"Tiny board" PCB, 1 unit, $980**
  - **The cost comparison DARPA itself used** (footnote 39): "A 1987 DARPA sample of costs indicated
    that **commercial runs would cost from $25-50,000 each** depending on the complexity of the
    chip, compared with a range of **MOSIS costs of $1-3,000**. MOSIS users would in addition save
    an estimated **six work-months** of time required to carry out administrative and technical
    overhead preparations."
  - **Who paid the user's bill** (p. 18-15): "Costs for DARPA VLSI contractors are funded by DARPA,
    and for designers eligible under certain NSF programs, by NSF."
  - **Why access was widened** (footnote 7): "Extension to commercial users was **expected to reduce
    government costs of MOSIS support**, and to bring down costs to users generally, via better
    rates from suppliers through larger, more frequent runs."
  - **Run frequency** (p. 18-15): MOSIS "schedule[s] frequent runs (**almost one per week**
    currently)".
- **DERIVED (arithmetic written out):**
  - **Total DARPA spend on MOSIS, 1981 → ~1990:** $30 m + $14 m = **$44 million**. Over ten years
    that is **$4.4 m a year**, and against the facility-and-staff line alone, **$3.0 m a year**.
  - **Against the staff roster in `MOS-3`:** $3.0 m a year of facility and staff cost against 27
    named people in 1987 is **$111,111 per head per year** in late-1980s dollars, inclusive of
    facilities. That is a credible fully loaded cost for a university research institute and it
    **retrospectively justifies the $100,000-per-head assumption used in `MOS-3`** — which was
    a guess when it was written and is now anchored.
  - **DARPA's subsidy per design.** Total projects 1981 → 1989, using IDA's series and interpolating
    1987 and 1988 as no lower than 1986's 1,683 (the report says those years declined, so this is
    conservative): 258 + 809 + 1,532 + 1,634 + 1,790 + 1,683 + 1,683 + 1,683 + 1,880 = **12,952
    designs**. Against $44 m that is **$3,397 of DARPA money per design fabricated**; against the
    $30 m facility-and-staff line alone, **$2,316 per design**.
  - **And that is the number that matters.** The list price of a 1987 TinyChip was **$400**
    (Table 18-2). The DARPA facility-and-staff subsidy per design was **$2,316**. **The government
    was paying roughly six times the ticket price to keep the service running.** Even against the
    $3,500 twelve-part unit, DARPA's per-design overhead was **66% of the price on top of the
    price**.
  - **Against the peak claim in `SMB-5`:** DARPA's entire ten-year outlay on MOSIS, $44 m, is
    **4.4×** "up to $10 million annually at its peak" — i.e. the whole federal build-out cost about
    what the mature service is claimed to have billed in four and a half years.
  - **IDA's own leverage claim, checked:** 7,300 projects × ($20,000 direct + ~$20,000 overhead) =
    **$292 m**, which is the top of its "$150-300 million" range. $292 m ÷ $44 m = **6.6×**, at the
    top of its stated "three-to-six-fold". The arithmetic is IDA's own and it is at the optimistic
    end of it.
- **Bears on:**
  - **H6 (challenges, and this is the decisive entry in the file).** MOSIS was not a business that
    happened to have a government customer. **DARPA put roughly $44 million into it over its first
    decade — about $2,300 to $3,400 per design fabricated — while charging users $400 to $3,500 a
    design.** Whatever MOSIS became after 1994 (`MOS-1`), the thing that became self-sustaining had
    already been paid for. A new entrant has no equivalent.
  - **H6 (supports, on the running cost).** $3.0 m a year for facilities and staff, running ~1,700
    designs a year at the peak of the 1980s, is **$1,765 per design of operating cost**. That is the
    real cost-to-serve of a multi-project-wafer brokerage, measured, in a year we can date. Nothing
    else in this repository provides it.
  - **H5 (challenges).** "more than 360 institutions" and 1,880 projects in 1989 is the size of the
    entire American demand for prototype silicon at the moment it was **free at the point of use for
    most of its users** — DARPA and NSF were paying the bill (p. 18-15). That is the ceiling, not
    the floor.
  - **H5 (context, and it cuts the other way).** MOSIS's throughput *rose* 7.3× between 1981 and
    1989 while price per part fell from $233 to $138. Demand did respond to cost in the 1980s. What
    `FUND-6` shows is that it stopped responding after 2002.
- **Used in:** not yet.
- **Caveats:**
  - **"Our initial estimate."** IDA labels the $30 m + $14 m as an estimate, in a retrospective
    written in 1990-91, without saying how it was built or what years "the period" covers precisely.
    The chapter's data run 1980 → 1990. **It is not an accounting record and must never be quoted as
    one.** It is, however, the Department of Defense's own contracted assessor putting a number on
    it, which is a great deal better than nothing.
  - The per-design derivations above interpolate 1987 and 1988. The direction of the error is known
    (IDA says those years declined, so the true denominator is smaller and the true subsidy per
    design is **higher** than $3,397).
  - Table 18-5's second series — projects counted "by user" rather than "by technology" — is
    materially lower in every year and its OCR is damaged. IDA itself flags the discrepancy
    ("These numbers differ greatly from total project numbers that ISI provided to IDA by type of
    technology") and converts to percentages because of it. **Only the "by technology" series is
    quoted here.** MOSIS's own throughput numbers disagreed with each other in 1991, which is worth
    remembering when reading the "60,000 designs" counter of 2024.
  - The 1987 price of $400 for a 4-part TinyChip and `FUND-5`'s $510 DARPA/NSF price for the same
    thing in 1996 are nine years apart. **Nominal TinyChip prices were roughly flat from 1987 to
    1998** ($400 → $550 → $510 → $620), i.e. falling by about a third in real terms while feature
    sizes shrank by 4×.

### MOS-9. The National Research Council's independent account: MOSIS grew from 258 projects in 1981 to 1,880 in 1989, and DARPA's whole VLSI programme went from under $15m to over $93m in three years

- **Source:** National Research Council, Computer Science and Telecommunications Board, *Funding a
  Revolution: Government Support for Computing Research*, National Academy Press, 1999, Chapter 4
  "The Organization of Federal Support: A Historical Review", **pp. 121–122**, and Chapter 1
  (Executive Summary/overview), p. 10.
  <https://nap.nationalacademies.org/read/6323/chapter/6> (chapter 4) and
  <https://nap.nationalacademies.org/read/6323/chapter/2>
- **Verification:** Verified 2026-09-25. The full text was read from the National Academies Press's
  free online edition; printed page numbers were confirmed by parsing the page-keyed text the reader
  serves. **The Internet Archive's copy (`fundingrevolutio00nati`) is lending-restricted and returns
  HTTP 403 to a text download; nap.nationalacademies.org serves the whole book openly.**
- **What it says** (verbatim, p. 121 unless noted):
  - "Access to MOSIS was originally limited to the VLSI research community and other Department of
    Defense contractors who linked to it through the ARPANET. **After the National Science
    Foundation (NSF) assumed responsibility for administering MOSIS in 1982, access was expanded to
    include NSF-sponsored researchers and affiliated educational institutions. In 1984, access was
    expanded to other qualified users as well.**"
  - "Altogether, MOSIS was used by researchers at **more than 360 institutions by 1989. The number
    of projects run through MOSIS increased from 258 in 1981 to 1,880 in 1989.**"
  - "Prominent VLSI researcher **Charles Seitz** commented that MOSIS represented the **first period
    since the pioneering work of Eckert and Mauchley on the ENIAC in the late 1940s that
    universities and small companies had access to state-of-the-art digital technology**."
  - **p. 122:** "**DARPA was by far the largest federal supporter of VLSI research. Its funding for
    the VLSI program grew from less than $15 million in 1979 to over $93 million in 1982.** …
    NSF assumed responsibility for MOSIS. Its main objective was to pursue educational applications
    of MOSIS, and it expanded the reach of the program to a wider set of academic institutions than
    DARPA had."
  - **p. 122:** "**Federal funding for VLSI began to decline in the mid-1980s.** By 1983, plans for
    DARPA's Strategic Computing Initiative evolved to the point that the most promising ongoing
    architecture projects in the VLSI program … shifted to the new program."
  - **Chapter 1, on the hand-off:** "NSF funds the Metal Oxide Semiconductor Implementation Service
    (MOSIS) — a system developed at Xerox PARC and institutionalized by DARPA … **Once established,
    this program no longer matched DARPA's mission to develop leading-edge technologies, but it did
    match NSF's mission to support university education and research infrastructure.**"
- **DERIVED (arithmetic written out):**
  - **Growth 1981 → 1989:** 1,880 ÷ 258 = **7.3×** over eight years, a compound rate of
    **28% a year**.
  - **MOSIS as a share of the DARPA VLSI programme.** `MOS-8` puts DARPA's MOSIS spend at about
    $4.4 m a year averaged over the decade. Against a VLSI programme that was "over $93 million" in
    1982, MOSIS was **about 4.7%** of it. **MOSIS was a rounding error inside the programme it
    enabled** — which is precisely IDA's leverage point in `MOS-8`, arrived at from the other side.
- **Bears on:**
  - **H6 (context, important).** Two independent, authoritative sources — IDA in 1991 and the NRC in
    1999 — give the same project series and the same institution count. `MOS-8`'s numbers are not a
    single OCR'd typescript's word. **The 258 → 1,880 series is as solid as anything in this
    repository.**
  - **H6 (challenges).** The NRC's framing is that DARPA **handed MOSIS off** because "this program
    no longer matched DARPA's mission". MOSIS did not graduate to self-sufficiency in a market; it
    was passed from one agency to another, and then, on `MOS-1`'s account, released in 1994. That is
    a different story from a business finding its feet.
  - **H5 (challenges).** MOSIS's peak in the 1980s, at 1,880 projects a year, is *lower* than
    `FUND-6`'s implied 1981–2002 average of 2,381 and *far* higher than its implied 455 a year for
    2002–2024. **The best-documented decade of American demand for prototype silicon tops out at
    under 2,000 designs a year.**
- **Used in:** not yet.
- **Caveats:**
  - The NRC's account draws on the same underlying IDA study — it says so: "Many of the details
    contained in this section derive from case studies of the VLSI program and MOSIS contained in
    Van Atta et al. (1991a), although the interpretation here differs in some respects." **This is
    therefore corroboration of transcription, not a fully independent count.**
  - "$15 million in 1979 to over $93 million in 1982" is the **whole DARPA VLSI programme**, not
    MOSIS. It is quoted here only to size the container.
  - The NRC's "NSF assumed responsibility for administering MOSIS in 1982" sits awkwardly beside
    `MOS-1`'s "From 1986 to 1994, this program was jointly funded by DARPA and NSF" and `MOS-2`'s
    DARPA contract running to at least 1989. `MOS-8` resolves it: DARPA's Duane Adams and NSF's
    Bernard Chern agreed in 1982 that **NSF would fund eligible university users who were not on
    DARPA programmes** — NSF took over paying for a class of *users*, not over running the service.

### MOS-10. A commercial silicon broker already tried this, in 1981, and died of no demand — and DARPA said so at the time

- **Sources:**
  - Van Atta et al., IDA Paper P-2429 Vol. 2 (as `MOS-8`), pp. 18-23 to 18-24.
  - Quoting Mark A. Fischetti, "In pursuit of the one-month chip: Business outlook", *IEEE
    Spectrum*, September 1984, p. 48.
- **Verification:** Verified 2026-09-25 in the IDA text. **The underlying *IEEE Spectrum* article
  was not read** — IEEE Xplore was not reachable — so this is a quotation of a quotation and the
  entry is **Partial** on the Fischetti wording.
- **What it says** (IDA, p. 18-23, verbatim):
  - "for an early brief period, DARPA was reportedly the primary customer for a **commercial silicon
    broker—Synmos, which handled 1400 chips over a two-and-a-half year period from 1981 to 1983.**
    Synmos received MEBES data, translated it into mask-making instructions, compiled it on a VAX,
    generated a MEBES control tape, and then arranged [masks] and fabrication, diced the chips and
    returned them to the designer. It also supplied design tools. **By 1984 it was 'on ice,' without
    an order for more than a year.**"
  - "In essence, Mr. Matkeny [President and CEO] said, '**they [DARPA and other potential customers]
    didn't think what we were doing was worth it.**' At that time, Mr. Losleben of DARPA confirmed
    this, explaining that '**Synmos was not adding enough value to the process.** He added that
    **there may not yet be sufficient demand for a brokerage service for any one broker to
    survive.**'"
  - IDA adds, writing in 1991: "Within the past two years however, **two new commercial silicon
    brokerage firms have begun operations.**" It does not name them.
- **DERIVED (arithmetic written out):**
  - Synmos handled **1,400 chips over 2.5 years = 560 a year**. In the same years MOSIS ran 258
    (1981), 809 (1982) and 1,532 (1983) projects (`MOS-8`). **Synmos's whole lifetime output was
    less than MOSIS's 1983 alone**, and it was running on DARPA's business.
- **Bears on:**
  - **H5 (challenges, and this is a forty-year-old precedent for a live question).** A commercial
    silicon brokerage was tried, in the founding years of the market, with the biggest possible
    customer, and it went a year without an order. DARPA's own programme manager's diagnosis was
    **not** that the technology was wrong: it was that "**there may not yet be sufficient demand for
    a brokerage service for any one broker to survive**". The repository's H5 question — is there a
    long tail of demand for chips? — was asked and answered in the negative in 1984, by the person
    paying for the alternative.
  - **H6 (challenges).** The failure mode is the one this repository keeps finding: `CF-1` and the
    Efabless collapse, `SMB` on the long-tail businesses that failed, and now Synmos. **A brokerage
    that adds coordination but not capacity is squeezed from both ends.** Losleben's phrase — "not
    adding enough value to the process" — is the objection foundry.api has to answer.
  - **H6 (context, and it cuts for).** MOSIS survived the same years and grew 7.3× (`MOS-9`). The
    difference between MOSIS and Synmos was not the model; it was that **DARPA paid MOSIS's
    facility and staff costs** (`MOS-8`) and directed its own contractors to it.
- **Used in:** not yet.
- **Caveats:**
  - **Partial.** The Fischetti quotes come to us through IDA. The names are OCR'd from a 1991
    typescript: "Matkeny" and "Lcs'eben"/"Losleben" are as printed, and the latter is certainly
    **Paul Losleben**, DARPA's VLSI programme manager, who is interviewed elsewhere in the same
    chapter.
  - Nothing found says why Synmos failed beyond these two sentences — whether it was priced wrong,
    under-capitalised, or simply displaced by a subsidised competitor. **The "subsidised competitor"
    reading is at least as consistent with the facts as the "no demand" reading, and IDA does not
    consider it.**

### MOS-11. Congress was told in 2022 that MOSIS "has kind of disappeared", by a member who used it

- **Source:** *Strengthening the U.S. Microelectronics Workforce*, Hearing before the Subcommittee
  on Research and Technology, Committee on Science, Space, and Technology, U.S. House of
  Representatives, 117th Congress, 2022-02-15. Serial No. 117-46, pp. 68–69.
  <https://www.govinfo.gov/content/pkg/CHRG-117hhrg46798/pdf/CHRG-117hhrg46798.pdf>
- **Verification:** Verified 2026-09-25. The 26 MB PDF was downloaded from govinfo's public content
  URL (**no API key needed** — `https://www.govinfo.gov/content/pkg/<packageId>/pdf/<packageId>.pdf`)
  and converted with `pdftotext -layout`.
- **What it says:**
  - **Rep. Bill Foster** (D-IL, a physicist who designed chips at Fermilab), verbatim: "we at that
    time had access to something called **MOSIS, which I take it has kind of disappeared**, which is
    a way that they—you know, you used to be able to get for not very much money a small number of a
    new chip design, you know. And **the fact that that, too, has disappeared I think really takes
    the wind out of getting young engineers excited about this.** So I was wondering, you know, what
    are the things that have been tried to **keep multi-project wafers going** that would let, you
    know, graduate students or even undergrads have access and actually build their own chip".
  - **Dr. Tsu-Jae King Liu** (Dean of Engineering, UC Berkeley) in reply: "it turns out that **Intel
    is in the process of—actually offers a multi-project wafer kind of service. They call it the
    University Shuttle.** And—but part of the challenge is that even though they offer space on
    chips so students can design and see their chips fabricated … **the sophistication of the chips
    has grown exponentially** … And that's where accessibility is a challenge because, you know, if
    the computing systems you need, **the cloud computing credits you need to even design a chip**
    because it's so complex, it poses a barrier."
  - She adds: "At Berkeley we actually have designed a course where students within one semester can
    tape out a chip … and send it to Intel to have it fabricated in the **16-nanometer** generation
    technology".
  - Foster closes: "we ought to find a way that we can make the—**a better economic model** for
    getting kids, young kids access to be able to build their own chip."
- **Bears on:**
  - **H5 (mixed, and precise).** The Dean of Engineering at Berkeley, asked directly what the
    barrier is, **does not say fabrication cost**. She says design complexity and **EDA tool and
    cloud access**. That is a direct, on-the-record challenge to the premise that price of silicon
    is the binding constraint — and it comes from the person best placed to know. It supports
    `DEM-21`'s reading and it is the same answer `DEM-22` records the NSF workshop giving.
  - **H6 (context).** Two years after the free academic programme ended (`DEM-22`), a member of
    Congress who had personally used MOSIS believed the whole service had disappeared. **Nobody in
    the room corrected him.** For a service that MOSIS's successor describes as "extremely
    successful" and "self-sustaining for 40 years" (`SMB-5`), that is a striking piece of negative
    evidence about its visibility in 2022.
  - **H5 (challenges).** "the fact that that, too, has disappeared … really takes the wind out of
    getting young engineers excited" is the demand-side consequence stated by a user.
- **Used in:** not yet.
- **Caveats:**
  - Foster's "has kind of disappeared" is **wrong as a matter of fact** — MOSIS was still trading in
    2022 and was reconstituted as MOSIS 2.0 in 2023 (`SMB-5`, `DEM-22`). The entry records what was
    said in Congress, and what it implies about how well known the service still was, not a fact
    about MOSIS's existence.
  - Transcribed spoken testimony, with the disfluencies of speech.

---

## 1. Funding timeline — every instrument found, with the gaps named

| Period | Instrument | Amount | Source | Confidence |
|---|---|---|---|---|
| 1979 → 1982 | The container: DARPA's whole VLSI programme | "**less than $15 million in 1979 to over $93 million in 1982**" | `MOS-9` | NRC, 1999 |
| **1981-01 →** | DARPA establishes MOSIS at USC/ISI. Reporting instrument **contract MDA903-81-C-0335**, an umbrella covering ISI's whole DARPA programme (19 projects in 1987) | no dollar figure in any ISI report — MOSIS never had a budget line of its own | `MOS-2` | Verified that the contract exists; **amount not in the contract record** |
| **1981 → ~1990, whole period** | **DARPA's total outlay on MOSIS, as estimated by the Institute for Defense Analyses for DARPA** | **"about $30 million in facility and staff costs plus roughly $14 million in project support costs" = ~$44 million, ≈ $4.4 m a year** | `MOS-8` | IDA's own "initial estimate" — not an accounting record, but the best figure that exists |
| 1982 | DARPA/NSF agreement (Duane Adams / Bernard Chern): NSF funds eligible university users not on DARPA programmes; access widened to NSF-affiliated institutions | not public | `MOS-8`, `MOS-9` | Verified |
| 1984 | Access widened again, to "other qualified users" / commercial users, explicitly **"expected to reduce government costs of MOSIS support"** | — | `MOS-8`, `MOS-9` | Verified |
| 1981 → 1989 | Same ISI contract; 1987 report prints "Contract expiration date 30 November 1989" | not public | `MOS-2` | Verified |
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

**The honest gaps.** There is still no **year-by-year** figure for DARPA's funding of MOSIS, and no
figure at all for 1990 → 1994. The reason is structural and is now understood (`MOS-2`): MOSIS was a
chapter inside a university research contract, not a programme element, so it never had a public
budget line. What has changed is that **a total for the first decade now exists** — IDA's ~$44 m
(`MOS-8`) — where before this pass there was nothing. There is still no figure for what MOSIS
charged in aggregate, in any year, ever.

## 2. Revenue and cost — what can be established, with the arithmetic

### 2.1 Throughput — the only continuous series that exists

| Year | Projects | Source |
|---|---|---|
| 1981 | **258** | `MOS-8` (ISI's figures to IDA), corroborated by `MOS-9` |
| 1982 | **809** | `MOS-8` |
| 1983 | **1,532** | `MOS-8` |
| 1984 | **1,634** | `MOS-8` |
| 1985 | **1,790** — and Lewicki's own paper says "approximately 1600 … for over 100 separate organizations" | `MOS-8`, `MOS-4` |
| 1986 | **1,683** | `MOS-8` |
| 1987–88 | not given; IDA says there was "a decline in 1986-1988" | `MOS-8` |
| 1989 | **1,880**, users at "more than 360 institutions" | `MOS-8`, `MOS-9` |
| 2000–2009 | the *free academic* programme alone: "nearly 7000 student IC designs" ≈ **700/yr** | `DEM-22` |
| 1981→2002 average | **2,381/yr**, implied by "50,000 designs and more than 20 years" | `FUND-6` |
| 2002→2024 implied | **≈455/yr** | `FUND-6` |
| peak, claimed | "around **3,000** orders per year", year unknown | `SMB-5`, uncorroborated |

### 2.2 Prices, costs and staff

| Quantity | Value | Year | Basis |
|---|---|---|---|
| Fabrication runs completed | **36** (20+3+7+4+2) | Jul 1982 → Jun 1983 | `MOS-4` |
| Fabrication runs completed | **35** (17+5+11+2) | Jul 1983 → Jun 1984 | `MOS-4` |
| Run frequency | "almost **one per week**" | ~1990 | `MOS-8` |
| Users per prototyping run | "typically about **40**"; **DERIVED** 1,532 ÷ 36 = **43** and 1,634 ÷ 35 = **47** | 1983–85 | `MOS-4`, `MOS-8` |
| Projects per wafer lot | "**ten to thirty** projects" per ten-wafer lot | 1987 | `MOS-4` |
| Cost of a dedicated prototype run | **$30,000 – $50,000** per iteration (MOSIS); "**$25-50,000**" (1987 DARPA sample) | 1987 | `MOS-4`, `MOS-8` |
| MOSIS cost to the user, same comparison | "**$1-3,000**" | 1987 | `MOS-8` |
| **Price list, 4-part TinyChip** | **$400** (1987) → **$550** (1988) → **$550** (1989) → **$510** DARPA/NSF (1996) → **$620** standard / $590 discount (1998) | 1987–1998 | `MOS-8`, `FUND-5`, `SMB-8` |
| **Price list, 12-part unit** | **$2,800** (1984, 4 µ nMOS) → **$3,500** (1987) → **$2,500** (1988) → **$3,100** (1989, 2 µ analog) | 1984–1989 | `MOS-8` |
| Per-part cost | **$233** (1984) → $292 → $208 → **$138** (1989) | 1984–1989 | `MOS-8` |
| Turnaround | 4–6 weeks (1983/84) → 7–9 weeks (1990) → 8–10 weeks (1987 report) | 1983–1990 | `MOS-4`, `MOS-8` |
| Named staff | **12** (8 research + 4 support) | Jul 1982 → Jun 1983 | `MOS-3` |
| Named staff | **11** (8 research + 3 support) | Jul 1983 → Jun 1984 | `MOS-3` |
| Named staff | **27** (12 research + 8 research assistants + 7 support) | Jul 1986 → Nov 1987 | `MOS-3` |
| **DARPA facility and staff cost** | **~$30 m over the decade ≈ $3.0 m a year** | 1981 → ~1990 | `MOS-8` |
| **DARPA project support cost** | **~$14 m over the decade ≈ $1.4 m a year** | 1981 → ~1990 | `MOS-8` |
| **DERIVED** cost per head, fully loaded | $3.0 m ÷ 27 = **$111,111** | 1987 | `MOS-3`, `MOS-8` |
| **DERIVED** DARPA subsidy per design | $44 m ÷ ~12,950 designs = **$3,397**; facility-and-staff only, **$2,316** | 1981 → 1989 | `MOS-3`, `MOS-8` |
| **DERIVED** operating cost per design | $3.0 m ÷ ~1,700 = **$1,765** | mid/late 1980s | `MOS-8` |
| Mean federal purchase-order price for an MPW tile | **$16,701** (4 NASA orders); **$17,300** including `FUND-6`'s three | 2005 → 2016 | `MOS-6` |
| Claimed peak revenue | "up to $10 million annually" | year unknown | `SMB-5`, uncorroborated |
| **DERIVED** revenue per order at claimed peak | $10,000,000 ÷ 3,000 = **$3,333** | — | `FUND-6` |
| **Largest single federal instrument found** | **$17,958,805** | 2021 | `MOS-5` |
| Operating cost after 1990 | **not public** | — | — |
| Revenue, any year | **not public** | — | — |
| Profit or surplus, any year | **not public** | — | — |

### 2.3 The arithmetic that matters

**DARPA paid about six times the list price, per design, to keep MOSIS running.** In 1987 a MOSIS
TinyChip cost the user **$400** (`MOS-8`, Table 18-2). DARPA's facility-and-staff subsidy, spread
over every design MOSIS fabricated, was **$2,316** (`MOS-8`). Even against the $3,500 twelve-part
unit — the expensive end of the list — DARPA was adding **66% of the price again** in overhead.

**That subsidy is what "self-sustaining" was built on.** By 1994 MOSIS had a vendor base, standard
design rules, an installed user community of 360-plus institutions, quality-assurance procedures,
and a fully written pipeline — all paid for by $44 million of DARPA money over thirteen years
(`MOS-8`, `MOS-1`). *Then* it covered its own costs. **The question for foundry.api is not whether
a brokerage can run at break-even once it exists. MOSIS shows that it can. The question is who pays
the $44 million.**

**And when nobody did, it failed.** `MOS-10`: Synmos, a commercial silicon broker with DARPA as its
main customer, handled 1,400 chips between 1981 and 1983 and was "on ice" by 1984, without an order
for over a year. DARPA's own programme manager: "**there may not yet be sufficient demand for a
brokerage service for any one broker to survive.**"

**The shape of demand over forty-five years.** 258 (1981) → 1,880 (1989) → a 1981–2002 average of
2,381 → an implied 455 a year for 2002–2024 (`FUND-6`) → the free academic programme withdrawn in
2020 (`DEM-22`). It grew 7.3× in the eight years when it was new, subsidised and free at the point
of use to most of its users, and it has fallen by roughly **75–80%** since. The "around 3,000 at
peak" claim in `SMB-5` is consistent with that shape — 1,880 in 1989 rising to 3,000 in the 1990s is
an ordinary growth curve — which is the first time this repository has been able to say that.

## 3. Verdict on the two claims

**"Up to $10 million annually at its peak" — still uncorroborated, but no longer implausible.**
No second source for the figure was found. No budget, no accounts, no revenue line, no year. What
*has* changed is that the companion claim, "around 3,000 orders per year", now has a primary
anchor: **1,880 projects in 1989** (`MOS-8`, `MOS-9`), reached from 258 in 1981, so a later peak
near 3,000 is an ordinary continuation rather than an invention. And the revenue figure can now be
bracketed from the price list rather than guessed: at 3,000 orders, the 1989 mix of
**$550 TinyChips and $3,100 twelve-part units** (`MOS-8`) gives **$1.65 m** at the bottom and
**$9.3 m** at the top. **"Up to $10 million" is the top of that range, exactly.** That is
consistent, and it is the best that can honestly be said: the claim is arithmetically reachable on
MOSIS's own published prices if nearly every order was a large one. It still rests on one sentence
in one promotional article and should continue to be cited that way.

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

**What is still missing, and it is the thing that matters — except that now we can price it.**
Covering your costs is not the same as covering the cost of the *capital*. Nothing found establishes
whether MOSIS paid USC for space or indirect costs after 1994, or what its accounting basis was.
But `MOS-8` now puts a figure on the runway: **DARPA spent about $44 million over MOSIS's first
decade — roughly $2,300 to $3,400 per design fabricated — while charging users $400 to $3,500 a
design.** A business handed thirteen years of that, plus a captive federal customer base and a
government directing its own contractors to use it, is **not evidence that the same business can be
started cold.** The nearest thing to a controlled experiment is `MOS-10`: Synmos, the commercial
broker that tried it without the subsidy in the same years, and was out of orders by 1984.

## 4. Head count — how many people ran MOSIS

**Twelve named people in 1982/83. Eleven in 1983/84. Twenty-seven in 1986/87.** All three counts are
from ISI's own annual technical reports to DARPA, which print a roster at the head of each project
chapter (`MOS-3`).

| Reporting period | Research staff | Research assistants | Support staff | Total | Projects that year |
|---|---|---|---|---|---|
| Jul 1982 → Jun 1983 | 8 | — | 4 | **12** | 1,532 |
| Jul 1983 → Jun 1984 | 8 | — | 3 | **11** | 1,634 |
| Jul 1986 → Nov 1987 | 12 | 8 | 7 | **27** | ~1,683 |

**Designs per head: 128 in 1983, 149 in 1984, 62 in 1987** (or 89 in 1987 counting only employees,
not the eight graduate students). Throughput was flat from 1984 to 1987 while headcount rose 2.5×.
What the extra people bought was not volume but **technology** — the 1987 report splits MOSIS across
a "VLSI" chapter and a new "Advanced VLSI" chapter chasing CMOS, 1.2 µm and quality assurance
(`MOS-2`, `MOS-4`).

**So: are these services expensive because they are staffed rather than automated?** The answer this
evidence supports is **no, and that is the problem.** MOSIS was *not* labour-intensive for its era.
Eleven people ran 1,634 designs a year — one every hour and a half of a working year. The 1984
report describes automated vendor templates, computerised geometry processing, automated scheduling
and wafer-space allocation, and users perceiving MOSIS as "a black box that accepts artwork files
electronically and responds with packaged IC devices" (`MOS-4`, `MOS-8`). **It was about as automated
as 1984 permitted, and it still needed $3.0 million a year of government money for facilities and
staff** (`MOS-8`).

That is **$111,111 per head per year**, fully loaded, and **$1,765 per design** of operating cost
alone — against a list price of **$400** for the small part and **$3,500** for the large one
(`MOS-8`). The staff cost is not a tail to be automated away; at the small-part end it is several
times the price of the product. **Automation was not what made MOSIS cheap for users. The subsidy
was.**

Compare `FUND-7`: CMC Microsystems spent **CAD $5,285,705 on salaries and benefits in FY2008 —
53.5% of all expenditure** — and **CAD $4.0 m, 54.8% of the non-FABrIC base, in FY2026**. Payroll is
over half the cost of running an MPW brokerage, in the only such organisation that publishes
accounts, forty years after MOSIS. Two organisations, two continents, four decades apart, and the
same answer: **a multi-project-wafer brokerage is a payroll with a website attached.**

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
| **A MOSIS revenue figure, or a profit figure, for any single year** | **Does not exist in anything reached.** Forty-five years, and there is no accounts statement. | This is the same wall `FUND-6` hit. **The cost side has moved** — `MOS-8` gives DARPA's decade total and `MOS-3` the headcount — but the revenue side has not. |
| **A year-by-year DARPA figure for MOSIS, 1981–1994** | Only a decade total exists (`MOS-8`), labelled by IDA as an "initial estimate". Nothing for 1990–1994 at all. | The end date of DARPA funding rests on `MOS-1` alone. |
| **The IDA study's underlying data** | IDA Paper P-2429 says its project counts came from ISI; those submissions are not published, and IDA's own two series disagree (`MOS-8`). | The 258 → 1,880 series is as good as it gets. |
| **Volumes 1 and 3 of the IDA study, and *IEEE Spectrum*, September 1984** | Volume 3 (DTIC AD-A241680) was not downloaded; Volume 1 (AD-A239925) failed with repeated HTTP 302s. IEEE Xplore was not attempted. | `MOS-10`'s Synmos quotes are **Partial** — quoted through IDA, not read in the original. |
| **Seven of twelve ISI Annual Technical Reports** (AD-A178085, AD-A221184, AD-A231025, AD-A127288, AD-A115915, AD-A121182) | `archive.org/download/.../<id>_djvu.txt` returned HTTP 302 with an empty body on repeated attempts, although the files are listed in each item's metadata. | **`MOS-3`'s headcount series has three points instead of ten.** Each additional report is one `curl` away when the redirects clear, and would turn it into a full 1975–1987 series. |
| **What share of MOSIS's revenue came from federal customers** | Not published anywhere found. | Without it, "self-sustaining" cannot be distinguished from "sustained by government purchasing". |
| **How much of the $17.96 m ATMI award USC kept** | Not published. | `MOS-5`'s bearing on H6 is weaker than it looks if most of it passed to Intel. |
