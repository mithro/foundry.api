# What it costs to run a multi-project-wafer service (`FUND`)

Every other file in this directory measures what a shuttle programme **charges**. This one tries to
measure what one **costs to run**, and how much of that cost the customers actually cover.

The project already holds two statements that point in opposite directions:

- `SMB-6`: Europractice says on its own "about" page that "European Union (EU) funding has
  significantly lowered the cost of participating in and using the Europractice service".
- `SMB-5`: MOSIS's host institution says it "was a self-sustaining business for 40 years" at "up to
  $10 million annually at its peak".

Neither is a budget. This file looks for the budgets.

The primary source for Europractice is **CORDIS** (`cordis.europa.eu`), the European Commission's
public project database, which publishes each grant's total cost, EU contribution, dates and the
contribution to every individual participant. The primary sources for MOSIS are USC ISI's own
material, NSF's public award search, and the federal contract feeds.

**Read the verdict at the end before quoting anything from the middle.** For one of the two
programmes the arithmetic can be done to the euro. For the other it cannot be done at all.

---

### FUND-1. Europractice's EU grants, 2016–2028: four contracts, €31.0 million, 100% EU-funded, every euro traceable to a named partner

- **Sources** (all CORDIS project fact sheets, European Commission, Publications Office of the EU):
  - EUROPRACTICE 2016, grant agreement 688226: <https://cordis.europa.eu/project/id/688226>
  - NEXTS, grant agreement 825121: <https://cordis.europa.eu/project/id/825121>
  - RETICLES, grant agreement 101096239: <https://cordis.europa.eu/project/id/101096239>
  - Europractice 2.0, grant agreement 101252350: <https://cordis.europa.eu/project/id/101252350>
- **Verification:** Verified 2026-09-19. All four fact sheets were fetched with `curl` and read
  directly; CORDIS serves them fully rendered server-side, so no browser is needed. The figures below
  are copied from the pages, not computed, except where marked DERIVED. A CORDIS full-text search for
  `contenttype='project' AND europractice` returns six projects; these four are the ones whose
  subject *is* the Europractice service.
- **How it was counted:** the CORDIS search API is public and returns JSON:
  `https://cordis.europa.eu/search?q=<query>&p=1&num=50&format=json`. Each project's participant
  contributions were then read from the fact-sheet HTML at
  `https://cordis.europa.eu/project/id/<grant id>`, whose participant blocks carry a "Net EU
  contribution" and a "Total cost" per organisation.
- **What it says:**

  | Grant | Acronym | Dates | Programme / scheme | Total cost | EU contribution |
  |---|---|---|---|---|---|
  | 688226 | EUROPRACTICE 2016 | 2016-07-01 → 2018-12-31 | H2020-EU.2.1.1, topic ICT-25-2015, **IA** | € 3 850 398,75 | € 3 850 398,75 |
  | 825121 | NEXTS | 2019-01-01 → 2022-09-30 | H2020-EU.2.1.1, topic ICT-07-2018, **IA** | € 7 989 055,00 | € 7 989 055,00 |
  | 101096239 | RETICLES | 2022-10-01 → 2025-09-30 | HORIZON.2.4.2 (Key Digital Technologies JU), topic HORIZON-KDT-JU-2021-3-CSA, **HORIZON-JU-CSA** | € 7 185 343,75 | € 7 185 343,75 |
  | 101252350 | Europractice 2.0 | 2025-10-01 → 2028-09-30 | HORIZON, topic HORIZON-JU-CHIPS-2025-CSA-1 "A Pan-European infrastructure for Chips Design Innovation", **HORIZON-JU-CSA** | € 11 993 182,50 | € 11 993 182,50 |

  **In all four, total cost equals EU contribution exactly.** CORDIS defines total cost as "The total
  amount of money invested in the project. The total cost includes EU contribution as well as other
  project costs not covered by EU funding." For these grants there is no such other cost recorded:
  the EU pays 100% of the project's declared cost.

  **Who gets the money** ("Net EU contribution" per participant, as printed on each fact sheet):

  | Organisation | EUROPRACTICE 2016 | NEXTS | RETICLES | Europractice 2.0 |
  |---|---:|---:|---:|---:|
  | INTERUNIVERSITAIR MICRO-ELECTRONICA CENTRUM (imec, Belgium) — **coordinator throughout** | € 1 790 398,75 | € 2 173 740,00 | € 3 237 596,25 | € 3 900 016,25 |
  | UNITED KINGDOM RESEARCH AND INNOVATION (UKRI, UK) | € 1 406 000,00 | € 2 090 000,00 | **€ 0,00** (listed as "Partner", not beneficiary) | € 3 602 261,25 |
  | FRAUNHOFER GESELLSCHAFT ZUR FORDERUNG DER ANGEWANDTEN FORSCHUNG EV (Germany) | € 654 000,00 | € 1 245 665,00 | € 1 408 146,25 | € 1 788 141,25 |
  | ASSOCIATION POUR LE DEVELOPPEMENT DES RECHERCHES AUPRES DES UNIVERSITES DE L ACADEMIE DE GRENOBL (Grenoble, France — the CMP host) | — | € 1 228 025,00 | — | — |
  | INSTITUT POLYTECHNIQUE DE GRENOBLE (INP Grenoble, France — the CMP host) | — | — | € 1 455 625,00 | € 1 607 791,25 |
  | UNIVERSITY COLLEGE CORK (Ireland — Tyndall National Institute) | — | € 1 251 625,00 | € 1 083 976,25 | € 1 094 972,50 |
  | **Sum** | **€ 3 850 398,75** | **€ 7 989 055,00** | **€ 7 185 343,75** | **€ 11 993 182,50** |

  The sums reconcile to the cent against the headline EU contribution in every one of the four
  grants (checked by script).

  On each fact sheet the per-organisation "Total cost" equals that organisation's "Net EU
  contribution", again to the cent. Nothing in CORDIS records any partner putting in its own money.

  Two structural points worth recording:
  - **The UK is in, out, and back in.** UKRI is the second-largest beneficiary of EUROPRACTICE 2016
    and NEXTS, receives **€0,00** under RETICLES (where it appears under "Partners (1)" with the
    note "Partner organisations contribute to the implementation of the action, but do not sign the
    Grant Agreement" and a total cost of "No data"), and is back as the second-largest beneficiary
    under Europractice 2.0. That is the Brexit gap in Horizon association, visible in the accounts of
    a chip service.
  - **The funding scheme changed.** The two H2020 grants are Innovation Actions ("IA"). The two
    newer ones are Coordination and Support Actions under a Joint Undertaking (KDT JU, then the
    Chips JU), which is the vehicle the EU now uses for infrastructure-type services.
- **DERIVED (arithmetic written out):**
  - Annual EU contribution, grant by grant (contribution ÷ duration in years):
    - EUROPRACTICE 2016: € 3 850 398,75 ÷ 2.5 yr = **€ 1 540 159,50 / yr**
    - NEXTS: € 7 989 055,00 ÷ 3.75 yr = **€ 2 130 414,67 / yr**
    - RETICLES: € 7 185 343,75 ÷ 3.0 yr = **€ 2 395 114,58 / yr**
    - Europractice 2.0: € 11 993 182,50 ÷ 3.0 yr = **€ 3 997 727,50 / yr**
  - The four together: € 3 850 398,75 + € 7 989 055,00 + € 7 185 343,75 + € 11 993 182,50 =
    **€ 31 017 980,00**, covering 2016-07-01 to 2028-09-30, a span of 12.25 years, a mean of
    **€ 2 532 080 / yr**.
  - The rate has risen: the 2025–2028 grant runs at **2.60×** the 2016–2018 grant's annual rate
    (3 997 727,50 ÷ 1 540 159,50 = 2.5956).
- **Bears on:**
  - **H6 (challenges).** This is the size of the hole. A brokerage that sells about 800 designs a
    year needs roughly €2.1–2.4 million a year of public money on top of what it charges — and the
    number the EU has just agreed for 2025–2028 is **€4.0 million a year**. The subsidy is not a
    rounding error on the price list in `SMB-7`; see `FUND-2` for the division.
  - **H8 (context).** The subsidy buys things a pure machine-time seller would not sell: 65,000
    concurrent tool licences, 96 training courses, a design-IP repository. How much of the €2.4m is
    brokerage and how much is training and tool licensing is **not separable from CORDIS**, and that
    matters — see the caveats.
  - **H6 (supports, weakly).** The EU contribution is not open-ended: it is a fixed-price grant
    renewed on a three-year cycle, and a competitive call. Somebody in Brussels believes the service
    is worth about €2.5 million a year, which is a ceiling as well as a floor.
- **Used in:** not yet.
- **Caveats:**
  - **"EU contribution equals total cost" does not mean the EU pays 100% of Europractice's costs.**
    It means the EU pays 100% of *the costs declared under these grants*. Europractice also takes
    membership fees and sells fabrication and licences (`FUND-3`), and that trading activity is
    outside the grant's cost base. CORDIS therefore bounds the **subsidy**, not the **turnover**.
  - Europractice's partners do far more than Europractice. imec's total income is of the order of
    €800m a year; €3.2m over three years is not a measure of imec.
  - The Grenoble beneficiary changes name between NEXTS (ADRUAG) and RETICLES (INP Grenoble). Both
    are the institutional hosts of CMP; CORDIS gives no explanation for the change.
  - RETICLES's "Total cost" for UKRI reads "No data", not zero, so the UK's own spending on its share
    of Europractice in 2022–2025 is not in CORDIS at all. It was funded nationally and is
    **not established here**.
  - CORDIS records *awarded* amounts. Final payments after audit can be lower. No final payment
    figure is public for any of the four.

### FUND-2. What the EU got for it: 6,791 designs over 9.25 years, i.e. about €2,800 of EU money per design

- **Sources** (CORDIS "Periodic Reporting" pages, which carry the Commission-published public
  summary of each reporting period):
  - EUROPRACTICE 2016, period 2: <https://cordis.europa.eu/project/id/688226/reporting>
  - NEXTS, period 2: <https://cordis.europa.eu/project/id/825121/reporting>
  - RETICLES, period 3: <https://cordis.europa.eu/project/id/101096239/reporting>
- **Verification:** Verified 2026-09-19, all three fetched and read. These are the project
  coordinator's own words as published by the Commission, not audited counts.
- **What it says:**
  - **EUROPRACTICE 2016** (2016-07-01 → 2018-12-31), work package 3, IC technologies: "In the first
    reporting period, a total of 530 designs were fabricated, while in the second reporting period a
    similar number of designs (i.e. 520) were recorded. In the extended period of the project,
    another 139 designs were fabricated." Work package 4, More-than-Moore: "In the first reporting
    period, a total of 56 designs were fabricated, while in the second reporting period a
    significant higher number of designs (i.e. 79) were recorded. In the extended period of the
    project, another 32 designs were fabricated."
  - **NEXTS** (2019-01-01 → 2022-09-30): "During the NEXTS project, more than 600 European
    Universities and Research Institutes got supported by easy and affordable access to
    state-of-the-art design tools and associated training. In addition, more than 3000 designs were
    fabricated in various technologies, ranging from 7 nm finFET to Si-Photonics technology."
    And, on the customer base actually buying silicon: "The impact on European level concerning IC
    prototyping and small volume projects is also very large with **183 European universities, 61
    European research institutes and 166 European companies fabricating various prototypes during
    the entire NEXTS project.**"
  - **RETICLES** (2022-10-01 → 2025-09-30): "During the project (October 2022 – September 2025),
    **2,435 MPW designs were submitted for fabrication.** 77% of them are coming from Europe, with
    nearly 25% of European users being SMEs." Separately, in the impact section: "Annually, more
    than 600 prototype designs were fabricated for European academic and industrial users".
    Portfolio: "the Europractice portfolio includes 102 technologies from 22 foundries and other
    technology providers, with 19 of them manufacturing in Europe."
  - RETICLES also reports the training side: "We delivered 96 training courses and technical
    workshops plus 29 webinars. They were attended by 4,238 delegates, including 261 university
    lecturers"; and "RETICLES enabled the delivery of over 65,000 concurrent licenses of design tool
    flows to universities and research centers across Europe."
- **DERIVED (arithmetic written out):**
  - EUROPRACTICE 2016 design count: IC 530 + 520 + 139 = **1,189**; More-than-Moore 56 + 79 + 32 =
    **167**; total **1,356** over 2.5 years = **542.4 designs/yr**.
    EU money per design: € 3 850 398,75 ÷ 1 356 = **€ 2 839,53**.
  - NEXTS: "more than 3000" over 3.75 years = **800 designs/yr** (a lower bound, because "more
    than"). EU money per design: € 7 989 055,00 ÷ 3 000 = **€ 2 663,02**, an *upper* bound because
    the denominator is a lower bound.
  - RETICLES: 2 435 submitted over 3 years = **811.7 designs/yr**. EU money per design submitted:
    € 7 185 343,75 ÷ 2 435 = **€ 2 950,86**. On the alternative denominator the same report gives —
    "more than 600 prototype designs … fabricated" annually, i.e. 1,800 over the project —
    € 7 185 343,75 ÷ 1 800 = **€ 3 991,86**.
  - **The three completed grants together:** € 19 024 797,50 of EU money, 1 356 + 3 000 + 2 435 =
    **6 791 designs**, over 2016-07-01 → 2025-09-30 (9.25 years). That is **734.2 designs a year**
    and **€ 2 801,47 of EU subsidy per design** (19 024 797,50 ÷ 6 791).
  - NEXTS's customer count: 183 + 61 + 166 = **410 organisations** fabricated anything at all in
    3.75 years, against "more than 600" institutions holding tool licences. So **about a third of
    the members who take the subsidised tools never buy a chip**, and the ones who do average
    3 000 ÷ 410 = **7.3 designs each over 3.75 years**, or about **two designs a year per buying
    customer**.
- **Bears on:**
  - **H6 (challenges, and this is the central number in this file).** Set the subsidy beside the
    price. `SMB-7` gives Europractice's cheapest commercial ticket as 6 mm² × €913/mm² =
    **€5,478** on the open-PDK 180 nm node, and its cheapest node is the exception: 12 mm² of GF
    130 nm BCDlite is €21,120. The EU is putting in about **€2,800 per design on top**. Against the
    cheap line that is **more than half as much again as the customer pays**; against a
    mid-portfolio ticket it is perhaps a tenth. Either way it is not small, and it is money nobody
    charges anybody.
  - **H5 (challenges).** Europe's entire subsidised long tail, over 9.25 years, bought **6,791
    designs** from **410-ish organisations**. That is the same order as MOSIS's realised scale in
    `SMB-5`, and it has not grown: 542/yr in 2016–18, 800/yr in 2019–22, 812/yr in 2022–25, against
    a subsidy that rose 2.6× over the same period.
  - **H6 (context).** The subsidy per design is *stable*: €2,840, €2,663, €2,951 across three
    separate competitive grants and nine years. Whatever it is buying, it is buying it at a
    consistent unit rate.
- **Used in:** not yet.
- **Caveats:**
  - **"Designs submitted" ≠ "designs fabricated" ≠ "paying orders".** RETICLES's own report uses
    2,435 submitted and "more than 600 … fabricated" annually in the same document; those cannot
    both be the same quantity. Both derivations are given above rather than choosing one.
  - **The denominator is wrong on purpose, and the error runs one way.** The grant does not only buy
    fabrication: it also buys 65,000 tool licences, 96 courses, a training programme, an IP
    repository and technology-incubation work. Dividing all of it by designs *overstates* the
    subsidy attributable to a fabricated chip. Nothing public splits the grant by work package, so
    the split cannot be made — see the verdict.
  - These counts come from the coordinator's own periodic reports. They do not match the annual
    activity reports in `DEM-16` line for line, and no reconciliation is offered by either source.
  - "more than 3000" and "more than 600" are floors quoted as if they were counts.


### FUND-3. Europractice's revenue side: a published fee schedule, a live list of every paying member, and about €557,500 a year of membership income against a €4.0m subsidy

- **Sources:**
  - UKRI-STFC, "EUROPRACTICE Membership" (the fee schedule):
    <https://www.europractice.stfc.ac.uk/membership/membership.html>
  - UKRI-STFC, "Active EUROPRACTICE Members" (the live member list, with each member's category):
    <https://www.europractice.stfc.ac.uk/membership/membership_list.cfml>
  - EUROPRACTICE, *Activity Report 2025*, section "EUROPRACTICE MEMBERSHIP":
    <https://europractice-ic.com/wp-content/uploads/2026/03/Europractice_AR2025_web.pdf>
  - EUROPRACTICE, *Activity Report 2024*, same section:
    <https://europractice-ic.com/wp-content/uploads/2025/10/Europractice_ActivityReport2024_webversion.pdf>
- **Verification:** Verified 2026-09-19. All four fetched and read; the two PDFs were converted with
  `pdftotext` and the quoted passages read out of the text layer. The member list page carries its own
  date stamp, "EUROPRACTICE Membership Summary / 19 September, 2026" — i.e. it was current on the day
  it was read.
- **How it was counted:** the member list is a plain HTML table, one row per member, with columns
  Site Number / Site Name / Country / Membership Category. A script parsed every row whose site
  number matches `^[A-Z]\d{5}$` and tallied the categories. 632 rows parsed; 630 carry a recognised
  category and 2 read "Unknown".
- **What it says:**
  - **The fee schedule** (STFC page, verbatim headings): "Full-IC annual membership, 1100 EURO";
    "Software-only annual membership, 600 EURO"; "FPGA-only annual membership, 200 EURO";
    "MPW-only annual membership, 600 EURO". "The annual membership fee year runs from 1 October to
    30 September." Eligibility: "Eligible Institutes must become a Member of EUROPRACTICE and pay the
    annual membership fee before they can make use of EUROPRACTICE services."
  - **What the fee is for**, *Activity Report 2025*, verbatim: "Together with the funding provided by
    the European Commission, Europractice needs additional support to provide high quality service to
    more than 600 European universities and research institutes. **Membership Fees pay for extra
    staff supporting this requested stimulation activity for academic institutions (not fully paid by
    the EC).** The annual Membership Fee is collected by STFC on behalf of the Europractice project
    partners." (Identical wording in the 2024 report.)
  - **How the fee splits**, *Activity Report 2024* and *2025*, verbatim: "Full-IC annual membership:
    1.100 € … **This membership fee is split 600 € for the CAD part (including 100 € to administer
    the membership) and 500 € for the prototyping part.**"
  - **The live membership**, counted from the list on 2026-09-19:

    | Category | Academic | Research lab | Total | Annual fee |
    |---|---:|---:|---:|---:|
    | Full-IC | 299 | 116 | 415 | € 1 100 |
    | Software-only | 85 | 50 | 135 | € 600 |
    | FPGA-only | 43 | 27 | 70 | € 200 |
    | MPW-only | 2 | 8 | 10 | € 600 |
    | *Unknown* | — | — | 2 | — |
    | **Total rows** | **430** | **202** | **632** | |

    42 distinct countries. The largest are Germany 140, Italy 74, France 61, Spain 60, UK 51,
    Turkey 21, Switzerland 18, Poland 17, Netherlands 16, Austria 16, Greece 15, Sweden 13. This
    matches the reports' standing claim of "more than 600 institutes in more than 40 countries from
    the EMEA zone".
  - For comparison, the EUROPRACTICE 2016 periodic report (`FUND-2`) gave "612 paid members" for
    October 2017 to September 2018. The paying membership has therefore been flat at ~610–630 for
    **eight years**.
- **DERIVED (arithmetic written out):**
  - Membership income at the published rates, from the counted list:
    299 × €1 100 = €328 900; 116 × €1 100 = €127 600; 85 × €600 = €51 000; 50 × €600 = €30 000;
    43 × €200 = €8 600; 27 × €200 = €5 400; 2 × €600 = €1 200; 8 × €600 = €4 800.
    **Total = €557 500 a year** from 630 members.
  - Split by the reports' own rule: the prototyping part is 415 Full-IC × €500 + 10 MPW-only × €600 =
    **€213 500**; the CAD part is 415 × €600 + 135 × €600 + 70 × €200 = **€344 000**;
    €213 500 + €344 000 = €557 500 ✓.
  - Against the EU money now running (Europractice 2.0, €3 997 727,50 a year, `FUND-1`):
    membership fees are **13.9%** of the subsidy, and the *prototyping-attributable* membership fees
    are **5.3%** of it.
  - Per design, on the 753 designs Europractice reports for 2025 (*Activity Report 2025*: "Our users
    submitted 753 designs across 14 foundries"): membership income is €557 500 ÷ 753 =
    **€740 per design**, against an EU subsidy of €3 997 727,50 ÷ 753 = **€5 309 per design** at the
    current grant rate.
- **Bears on:**
  - **H6 (challenges, hard).** The one recurring fee Europractice charges every customer covers
    about a seventh of the public money it receives, and the part of that fee earmarked for
    prototyping covers about a twentieth. The service's own annual report states the reason in
    plain language: the fee exists because the EC does **not** fully pay for the support staff.
  - **H8 (context).** The fee schedule is completely public, flat, and has four tiers, with no
    negotiation and no quote. As a piece of pricing design it is exactly the kind of thing
    foundry.api proposes. It just does not come close to covering the cost.
  - **H5 (challenges).** 630 paying members today against 612 in 2017/18. Eight years, a 2.6× rise
    in EU funding, a worldwide semiconductor boom, and the paying membership moved by about 3%.
- **Used in:** not yet.
- **Caveats:**
  - **The membership fee is not Europractice's revenue.** Tool licences are charged on top of it, and
    MPW fabrication is charged separately at the prices in `SMB-7`. What €557 500 measures is the
    *subscription* line, which is the only recurring charge whose rate and whose customer count are
    both public. **Total turnover is not published anywhere we could find.**
  - **A crude bound on the fabrication line, offered only as an order of magnitude.** If all 753 of
    2025's designs paid the cheapest discounted minimum ticket in `SMB-7` — IHP SG13C at 0.8 mm² ×
    €3 825 = €3 060 — fabrication billings would be 753 × €3 060 = **€2.30m**; at GF 180 MCU
    (6 mm² × €830 = €4 980), **€3.75m**; at GF 130 nm BCDlite (12 mm² × €1 600 = €19 200),
    **€14.5m**. The real figure is unknown and the spread is a factor of six. This is *not* a
    measurement, and it must not be quoted as one. What it does establish is that fabrication
    billings are of the same order as the subsidy, not obviously above or below it.
  - The member list is a snapshot of *active* members, not of members who paid in any given year, and
    STFC does not say whether a member in arrears is removed.
  - Full-IC, Software-only and FPGA-only members can also be paying for tool bundles at rates that
    are behind a member login and were not read.
  - The count of 632 is ours, not Europractice's; Europractice says "more than 600".

### FUND-4. The whole chain, 1995–2028: eleven EC grants, €87.0 million of EU money, and a declared cost of running the service that the partners part-funded themselves

- **Sources:** CORDIS open data, the European Commission's bulk project exports, downloaded 2026-09-19:
  - `https://cordis.europa.eu/data/cordis-fp4projects-csv.zip`
  - `https://cordis.europa.eu/data/cordis-fp5projects-csv.zip`
  - `https://cordis.europa.eu/data/cordis-fp6projects-csv.zip`
  - `https://cordis.europa.eu/data/cordis-fp7projects-csv.zip`
  plus the four post-2016 fact sheets already cited in `FUND-1`.
- **Verification:** Verified 2026-09-19. Each archive's `csv/project.csv` and `csv/organization.csv`
  were read directly. Every figure below is a field from those files. **The pre-2016 grants are not
  in the CORDIS web search index** — a full-text search for "EUROPRACTICE" or "EUROCHIP" on
  `cordis.europa.eu` returns only the H2020-and-later projects. They are only in the bulk exports.
  That is the single most useful thing learned here for anyone repeating this work.
- **How it was counted:** a script scanned each framework programme's `project.csv` for
  `europractice|eurochip` in any field, and a second script listed every project in each programme
  whose `organization.csv` row for imec carries `role == "coordinator"`, to catch grants that do not
  name Europractice in their title.
- **What it says:**

  | Grant ID | Acronym | Dates | Legal basis | Declared total cost | EU contribution | Partners' own share |
  |---|---|---|---:|---:|---:|---:|
  | 21101 | EUROPRACTICE | 1995-10-01 → 1999-09-30 | FP4-ESPRIT 4 | € 46 914 000 | **€ 35 000 000** | € 11 914 000 (25.4%) |
  | IST-1999-12057 | EUROPRACTICE IC | 2000-01-01 → 2003-02-28 | FP5-IST | € 4 500 000 | € 4 500 000 | € 0 |
  | IST-2001-37510 | EUROPRACTICE IC 2 | 2002-12-01 → 2005-12-31 | FP5-IST | € 5 565 196 | € 3 000 000 | € 2 565 196 (46.1%) |
  | *(none found)* | — | 2006-01-01 → 2007-12-31 | — | — | — | — |
  | 214157 | EUROPRACTICE IC4 | 2008-01-01 → 2010-12-31 | FP7-ICT | € 4 821 082 | € 3 150 000 | € 1 671 082 (34.7%) |
  | 257098 | EUROPRACTICE IC5 | 2010-04-01 → 2011-12-31 | FP7-ICT | € 2 927 421 | € 1 850 000 | € 1 077 421 (36.8%) |
  | 315961 | EUROPRACTICE 2012 | 2012-01-01 → 2014-12-31 | FP7-ICT | € 4 069 225 | € 2 541 000 | € 1 528 225 (37.6%) |
  | 610018 | EUROPRACTICE 2013 | 2013-07-01 → 2016-06-30 | FP7-ICT | € 5 965 000 | € 5 965 000 | € 0 |
  | 688226 | EUROPRACTICE 2016 | 2016-07-01 → 2018-12-31 | H2020-ICT | € 3 850 398,75 | € 3 850 398,75 | € 0 |
  | 825121 | NEXTS | 2019-01-01 → 2022-09-30 | H2020-ICT | € 7 989 055,00 | € 7 989 055,00 | € 0 |
  | 101096239 | RETICLES | 2022-10-01 → 2025-09-30 | HORIZON, KDT JU | € 7 185 343,75 | € 7 185 343,75 | € 0 |
  | 101252350 | Europractice 2.0 | 2025-10-01 → 2028-09-30 | HORIZON, Chips JU | € 11 993 182,50 | € 11 993 182,50 | € 0 |
  | **Total** | | 1995-10-01 → 2028-09-30 | | **€ 105 779 904** | **€ 87 023 980** | **€ 18 755 924 (17.7%)** |

  - **The 1995 grant is in a different league.** EUROPRACTICE (FP4, ESPRIT 4) had **23 participants**
    listed in `organization.csv` and was coordinated **not by imec but by the UK's Council for the
    Central Laboratory of the Research Councils (CCLRC)**, the predecessor of STFC, with Rutherford
    Appleton Laboratory also listed separately. Participants included imec, Fraunhofer (twice: the
    Gesellschaft and the Institut für Siliziumtechnologie), CEA-LETI, CSEM, SINTEF, CNM Barcelona,
    Robert Bosch, GEC Marconi, Sagem, Sextant Avionique, DELTA, DTU and others. The stated objective:
    "The overall objective is to stimulate wider exploitation of state-of-the-art microelectronics
    technologies by European industry. Basic Services (EUROPRACTICE) offers a cost-effective and
    flexible means of accessing ASICs, MCMs and Microsystems technologies through the provision of
    consultancy, training, software tools, design support, low-volume production runs and access to
    normally internal volume production facilities."
  - **From FP7 on it is three organisations.** `organization.csv` gives exactly three participants for
    each of EUROPRACTICE IC4, IC5 and 2012: imec (coordinator), STFC and Fraunhofer. The per-partner
    EU contributions:
    - IC4: imec € 1 428 715; STFC € 1 237 390; Fraunhofer € 483 895 (sums to € 3 150 000 ✓)
    - IC5: imec € 997 382; STFC € 599 618; Fraunhofer € 253 000 (sums to € 1 850 000 ✓)
    - 2012: imec € 1 261 001; STFC € 899 999; Fraunhofer € 380 000 (sums to € 2 541 000 ✓)
  - **There is a hole in the record for 2006 and 2007.** No FP6 grant for the Europractice IC service
    was found, by either search. The four FP6 records that mention Europractice at all are
    ACCORD (034041, € 997 676 EC), INTEGRAMPLUS (027540, € 3 799 459 EC), RF-PLATFORM (027468,
    € 2 899 460 EC) and BRIDGE (507307, € 580 000 EC) — all microsystems/packaging projects, none of
    them the CAD-and-MPW service. BRIDGE's own objective text says something worth quoting exactly:
    it will "coordinate the activities of the **65 EUROPRACTICE partners, who have agreed to continue
    with EUROPRACTICE for a further year at no additional funding**".
  - **The FP7 grants are the only ones that reveal an operating cost.** FP7 reimbursed a *fraction* of
    declared eligible cost, so `totalCost` and `ecMaxContribution` differ and the difference is what
    the partners paid themselves. From H2020 onwards the beneficiaries are non-profit research
    organisations reimbursed at 100%, so the two columns collapse and the cost information
    disappears.
- **DERIVED (arithmetic written out):**
  - **EU money per year, by era** (EU contribution ÷ years spanned):
    - FP4, 1995-10 → 1999-09: € 35 000 000 ÷ 4.0 = **€ 8 750 000 / yr**
    - FP5, 2000-01 → 2005-12: € 7 500 000 ÷ 6.0 = **€ 1 250 000 / yr**
    - FP7, 2008-01 → 2016-06: € 13 506 000 ÷ 8.5 = **€ 1 588 941 / yr**
    - H2020 + Horizon Europe, 2016-07 → 2028-09: € 31 017 980 ÷ 12.25 = **€ 2 532 080 / yr**
    - Whole period 1995-10 → 2028-09 (33.0 years): € 87 023 980 ÷ 33.0 = **€ 2 637 090 / yr**
  - **The declared cost of running the service, FP7 era** (total cost ÷ years), which is the closest
    thing to an operating budget anywhere in the public record:
    - IC4: € 4 821 082 ÷ 3 = **€ 1 607 027 / yr**, of which € 1 050 000 / yr from the EC
    - IC5: € 2 927 421 ÷ 1.75 = **€ 1 672 812 / yr**, of which € 1 057 143 / yr from the EC
    - EUROPRACTICE 2012: € 4 069 225 ÷ 3 = **€ 1 356 408 / yr**, of which € 847 000 / yr from the EC
    Across those three grants the EC covered **63.8%** of the declared cost and the partners found
    the other **36.2%** themselves: EC 3 150 000 + 1 850 000 + 2 541 000 = € 7 541 000 against
    declared cost 4 821 082 + 2 927 421 + 4 069 225 = € 11 817 728, and
    7 541 000 ÷ 11 817 728 = 0.6381.
  - Set against `DEM-16`'s design counts, the FP7 era ran at roughly 400–600 designs a year on about
    **€1.5m/yr of declared cost**, i.e. of the order of **€2 500–4 000 of declared cost per design**
    — the same band as `FUND-2` finds for the later grants from a completely different calculation.
- **Bears on:**
  - **H6 (challenges).** Thirty-three years and **€87 million** of EU money, for a service that has
    never in that time exceeded about a thousand designs a year. Nobody has ever run this thing
    without a subsidy, and the subsidy per year is now the highest it has been since the 1990s.
  - **H6 (supports, genuinely).** The FP7 numbers are the strongest pro-H6 evidence in this file:
    when the EC paid only part of the bill, **the partners paid the other third or so out of their
    own resources and kept the service running**, including through 2006–2007 when no dedicated
    grant is on record and BRIDGE says the partners agreed "to continue with EUROPRACTICE for a
    further year at no additional funding". A service that survives a funding gap is not a service
    with no revenue.
  - **H5 (challenges).** The 1995 grant funded 23 organisations to build a pan-European access
    service for "European industry". Thirty years on, the service is three or five organisations,
    630 mostly-academic paying members, and about 800 designs a year. The tail did not arrive.
- **Used in:** not yet.
- **Caveats:**
  - **The FP4 figure is not comparable to the rest.** €46.9m / €35m covered ASICs *and* multi-chip
    modules *and* microsystems across 23 partners with their own competence centres. Treating
    €8.75m/yr as "what Europractice cost in the 1990s" would be wrong. What it does establish is the
    order of the EU's original commitment.
  - **Currency.** The FP4 grant was signed in 1995, when the unit of account was the ECU, not the
    euro. CORDIS reports it in euro without stating a conversion. ECU and euro were set at 1:1 on
    1999-01-01, so the figure is arithmetically unchanged, but it is **1995 money** and is not
    inflation-adjusted anywhere in this entry.
  - **The grants overlap.** IC4 (to 2010-12) and IC5 (from 2010-04) run concurrently for nine months;
    EUROPRACTICE 2012 (to 2014-12) and 2013 (from 2013-07) overlap for eighteen. Per-year figures are
    therefore *era averages*, not the rate in any named year.
  - **"Total cost" is the cost declared under the grant, not the cost of the business.** It excludes
    the trading side entirely: buying wafer area from foundries and reselling it, and buying and
    reselling EDA licences, are not grant-eligible costs. What Europractice turns over is still not
    public.
  - **2006–2007 is unresolved.** Either the IC service ran with no dedicated EC grant, or a grant
    exists that neither search found. A "EUROPRACTICE IC 3" would be the obvious name; **no such
    record exists in the FP6 bulk export.**
  - `EUROCHIP` (1989–1995) is **not in CORDIS at all**, in any framework programme's export. The FP7
    hit on that acronym is an unrelated obesity-research consortium. See the blocked-sources list.

### FUND-5. MOSIS's federal money arrived as *purchases*, not as a grant: a separate "DARPA/NSF" price list, and an educational programme paid for by NSF plus donated wafers

- **Sources** (Internet Archive copies of `mosis.org` and `mosis.com`, both of which are gone from the
  live web):
  - "MOSIS DIRECT-FUNDING PRICE LIST (Valid July 1, 1996 through March 31, 1997)", archived
    1997-01-16:
    <https://web.archive.org/web/19970116072510id_/http://www.mosis.org/info/direct-funding-price-list.inf>
  - "NSF-sponsored Educational Use of MOSIS — POLICIES AND PROCEDURES FOR EDUCATIONAL USE OF
    DARPA/NSF SILICON BROKERAGE SERVICE (MOSIS)", archived 1997-04-18:
    <https://web.archive.org/web/19970418072820id_/http://www.mosis.org/nsf-educational.html>
  - "MOSIS FAQ: Educational Program", archived 2000-01-26:
    <https://web.archive.org/web/20000126044247id_/http://www.mosis.org/Faqs/faq-education.html>
  - "Budgets for Educational MOSIS Accounts", MOSIS announcement dated 1998-07-27, archived
    1999-02-24:
    <https://web.archive.org/web/19990224190349id_/http://www.mosis.org/New/Whatsnew/1998/980727-nsf-budgets.html>
  - NSF award 9809025, "CARE: Advanced Semiconductor Technology Access for Educational Use",
    University of Southern California: <https://www.nsf.gov/awardsearch/showAward?AWD_ID=9809025>
    (read through the public NSF awards API, `https://api.nsf.gov/services/v1/awards.json`)
- **Verification:** Verified 2026-09-19. The four archived pages were fetched with `curl` using the
  Wayback `id_` raw-content form (as `search-log.md` §1 already records, `WebFetch` refuses
  `web.archive.org`). The NSF award was read from NSF's public JSON API. **Wayback rate-limits
  hard**: after four or five requests it returns `Failed to connect ... port 443`; an 8-second delay
  between requests was enough.
- **What it says:**
  - **There were two price lists, and one of them was for the government.** The direct-funding list
    opens, verbatim: "The MOSIS Direct-Funding Price List should only be used by a government
    contractor whose sponsoring agency (**usually DARPA or NSF**) has sent fabrication funding
    directly to MOSIS. If funding has been sent directly to MOSIS, the contractor's award will not
    include any funds for fabrication. If your contract award DOES include funds for fabrication, you
    should use the 'MOSIS Price List for Domestic (U.S.) Users.'" Its price column is headed
    **"DARPA/NSF PRICE"**. On 2.0 µm CMOS, "Priced per project, price includes packaging":
    2.30 × 2.30 mm TinyChip, lot of 4, **$510**; 4.6 × 6.8 mm, lot of 12, $2,490; 6.9 × 6.8 mm, lot
    of 24, $5,690; 7.9 × 9.2 mm, lot of 32, $11,320.
  - **The service's own name for itself, in an official policy document**, is
    "**DARPA/NSF SILICON BROKERAGE SERVICE (MOSIS)**" (title of the 1997 educational policy page).
    The same page: "NSF and DARPA will review proposals on a semiannual basis and will have final
    authority on allocation of available funds to each project," and "Participants are expected to
    test all designs and report their testing results to NSF and DARPA."
  - **Who paid for the free academic programme.** The FAQ, verbatim: "**2. Who provides funding for
    the MOSIS educational program?** Funding is currently provided by: National Science Foundation
    (NSF) / American Microsystems, Inc. (AMI) / Hewlett Packard (HP) / The MOSIS Service". And, on
    why research designs were excluded: "This is important, because **the fabricators providing free
    wafers for this program** have only agreed to fabricate circuits designed by students in
    regularly scheduled university classes." The programme's scope: "The MOSIS Educational Program
    provides **free fabrication** of integrated circuits designed by students in organized classes at
    accredited U.S. educational institutions." Universities paid nothing: "Universities are not
    currently required to contribute any funding, however this may change in the future."
  - **The subsidy was rationed by headcount, and it was over-allocated.** The 1997 policy: "Beginning
    classes will receive budgets sufficient to fabricate one 2.0 micron CMOS TinyChip for **every two
    students** enrolled"; advanced classes "one 2.0 micron CMOS TinyChip or one 1.2 micron CMOS Low
    Noise Analog TinyChip **for each student**". The 1998 announcement: "On July 31, 1998, all
    unspent funds in NSF-sponsored CLASS and ACLAS accounts will be removed from those accounts …
    **In the past, budget allocations to educational accounts have significantly exceeded actual
    requirements.**"
  - **The one NSF award that can be found for MOSIS itself**: award 9809025 to the University of
    Southern California, PI **Herbert Schorr** (ISI's executive director), 1998-10-01 → 1999-09-30,
    **estimated total US$199,726, funds obligated US$199,726**. Abstract, verbatim: "The MOSIS
    service, through this award, provides low-cost custom and semi-custom VLSI prototyping and
    small-volume production quantities to educational institutions."
- **DERIVED (arithmetic written out):**
  - The DARPA/NSF TinyChip price of **$510** (1996-07 → 1997-03) against the domestic prices in
    `SMB-8` for the same part a year or so later — **$620 standard, $590 discount** (valid through
    1998-12-31) — is 510 ÷ 620 = 0.823, i.e. **17.7% below the standard price**, and 510 ÷ 590 =
    0.864, i.e. **13.6% below the discount price**. The dates differ by about eighteen months, so
    this is a rough comparison, but the direction is unambiguous: **the US government got a discount,
    and it paid.**
- **Bears on:**
  - **H6 (supports, importantly).** This is the mechanism that makes `SMB-5`'s "self-sustaining"
    claim and "receiving federal money" both true at once. DARPA and NSF did not write MOSIS an
    operating grant covering a deficit; they **pre-purchased fabrication at a published rate**. A
    service whose largest customer is a government buying at a price list is a business, and it is
    exactly what foundry.api proposes to be, minus the government.
  - **H6 (challenges).** The *free academic* half of it was a straightforward subsidy, and a large
    part of that subsidy was not cash at all: **AMI and HP donated the wafers**. A model that assumes
    a foundry sells machine time at a price has no room for a foundry giving the machine time away,
    and MOSIS's education programme ran for decades on exactly that. It ended in 2020 (`DEM-22`).
  - **H5 (context).** The rationing rule — one TinyChip per two beginning students — is a measurement
    of how small the underlying demand was: the binding constraint on a free chip programme was the
    class register, not anybody's willingness to pay.
- **Used in:** not yet.
- **Caveats:**
  - **None of this is a budget.** The direct-funding price list shows that DARPA and NSF bought from
    MOSIS; it does not show **how much** they bought. No annual total for DARPA or NSF purchases from
    MOSIS was found anywhere.
  - The $199,726 NSF award is a single year and is plainly a small slice of the educational
    programme, not its cost. NSF's award database does not reach reliably back to 1981, and no
    earlier MOSIS award is in it.
  - The FAQ's funder list ("NSF, AMI, HP, The MOSIS Service") is undated beyond its 2000-01-26
    capture, and "The MOSIS Service" appearing in its own funder list is unexplained: it may mean
    cross-subsidy from commercial revenue, which would be the single most interesting fact in this
    file if it could be confirmed. **It cannot be, from anything public.**
  - Archived vendor pages are as MOSIS published them, not audited.

### FUND-6. Testing "self-sustaining for 40 years" and "$10 million annually at its peak": the claims survive, the numbers behind them do not exist, and the decline is visible in MOSIS's own design counter

- **Sources:**
  - Stephanie Lee, USC ISI, "MOSIS 2.0's First Year: Bridging Research and Production", 2025-02-21:
    <https://www.isi.edu/news/972800/mosis-2-0s-first-year-bridging-research-and-production/>
    (the source already recorded as `SMB-5`)
  - MOSIS announcement page header, archived 2002-04-01: "50,000 designs and more than 20 years of
    experience":
    <https://web.archive.org/web/20020401213036id_/http://www.mosis.com/about/news/2002/020306_mep.html>
  - MOSIS, "About Us > What is MOSIS", archived 2012-02-03:
    <https://web.archive.org/web/20120203055035id_/http://www.mosis.com/about-us>
  - FPDS-NG public ATOM feed, <https://www.fpds.gov/ezsearch/FEEDS/ATOM?FEEDNAME=PUBLIC&q=…>
- **Verification:** Verified 2026-09-19. The ISI page was re-read; the two archived pages were
  fetched with `curl`; the FPDS query was run and its result counted.
- **What it says:**
  - The claims, as `SMB-5` records them: "Over four decades, MOSIS delivered more than 60,000
    integrated circuit designs and generated up to $10 million annually at its peak"; "At its peak,
    MOSIS fulfilled around 3,000 orders per year"; "Even though it was run by a university, it was a
    self-sustaining business for 40 years."
  - **Re-read on 2026-09-19, the 2025 ISI page still gives no year for the peak, no accounting basis,
    and no staff number.** There is no second, independent source for either the $10 million or the
    3,000 orders anywhere that this search reached.
  - **MOSIS's own design counter, from its own site:**
    - 2002-04-01 (page header): "50,000 designs and more than 20 years of experience"
    - 2012-02-03: "Since 1981, MOSIS has fabricated more than 50,000 circuit designs for commercial
      firms, government agencies, and research and educational institutions around the world."
    - 2024/2025 (ISI): "more than 60,000 integrated circuit designs" over four decades.
  - **FPDS-NG knows almost nothing about MOSIS.** A public ATOM query for
    `DESCRIPTION_OF_REQUIREMENT:"MOSIS"` returns **10 contract actions in total**, of which only
    **three** name the University of Southern California as vendor: NASA 2005 ($27,000, "MOSIS
    ACCT#2841-COM-GOV/NASA-MI.PN 10636, IBM 0.35 MICRON SIGE BICMOS 5HPE PROCESS"), a 2013 action
    ($6,500) and NASA 2015 ($20,800, "INTERGRATED CIRCUIT FABRICATION AT MOSIS OF TOF CHIP DESIGNS").
    Total obligated across those three: **$54,300.** The other seven are unrelated or are other
    agencies' purchases through third parties. These are **customers buying chips**, not anybody
    funding MOSIS.
- **DERIVED (arithmetic written out):**
  - **The decline, from MOSIS's own counter.** 50,000 designs in the 21 years 1981→2002 is
    50 000 ÷ 21 = **2,381 designs a year on average**. 60,000 designs in the 43 years 1981→2024 is
    60 000 ÷ 43 = **1,395 a year on average**. The implied count for 2002→2024 is
    60 000 − 50 000 = 10,000 designs over 22 years = **455 designs a year** — about **a fifth** of
    the first-two-decades rate, and about **a seventh** of the stated peak of 3,000.
  - At the stated peak, revenue per order was $10,000,000 ÷ 3,000 = **$3,333** (this is `SMB-5`'s
    derivation, repeated here because the next line depends on it).
  - Europractice today: **753 designs in 2025** (`FUND-3`). MOSIS at its peak did 3,000 ÷ 753 =
    **4.0×** that, on a service that took no operating grant.
- **Bears on:**
  - **H6 (mixed, and this is the honest answer).** The "self-sustaining" claim is *not* refuted:
    `FUND-5` shows a real mechanism by which MOSIS could cover its costs from sales while much of
    its sales came from federal agencies. But it is also **not corroborated**: no budget, no accounts,
    no revenue line, no staff count, and no year for the peak exists in any public source found. It
    rests on one sentence, spoken by a deputy director of the successor programme, in a promotional
    news item written by the host institution.
  - **H5 (challenges, hard).** MOSIS's own counter says the service ran at roughly 2,400 designs a
    year for its first two decades and roughly 455 a year for its last two. The American long tail
    for prototype chips did not grow when the internet, cheap EDA and open PDKs arrived. **It
    shrank by about 80%.**
  - **H6 (challenges).** The successor is not self-sustaining and says so: "achieve
    self-sustainability within the next few years and generate $20 million in annual revenue"
    (`SMB-5`). A business that was genuinely self-sustaining for forty years does not need a
    five-year federally funded programme to get back there.
- **Used in:** not yet.
- **Caveats:**
  - **The 50,000 figure may be stale in both captures.** `DEM-22` already records that MOSIS's public
    design counter did not move for a decade. If "more than 50,000" was already conservative in 2002,
    the 2002→2024 rate derived above is too low; if it was still being quoted unchanged in 2012
    because nobody updated the page, the true 2002 figure is unknown. **The derivation is an
    indication of direction, not a measurement of level**, and it should be quoted that way.
  - "more than 50,000" and "more than 60,000" are floors.
  - The $10m figure carries no year, no currency basis and no definition of revenue (gross billings
    including pass-through foundry cost, or net?). If it is gross billings, most of it was money
    passing through to foundries and it says nothing about what MOSIS cost to run.
  - FPDS-NG covers federal contract actions from roughly 2004 onward. **It cannot see the 1980s and
    1990s**, which is exactly when MOSIS's DARPA funding mattered. Its silence is a limitation of the
    source, not evidence about MOSIS.
  - USAspending's award-search endpoints are POST-only and this session was GET-only, so the
    assistance (grant) side of the federal record was not queried at all. See the blocked-sources
    list.

### FUND-7. CMC Microsystems publishes actual accounts — and in 2007/08 customers paid 9.15% of its revenue

- **Sources:**
  - CMC Microsystems, *Annual Report 2007/08*, "Statement of Revenue and Expenditure", archived
    2009-12-17:
    <https://web.archive.org/web/20091217114015id_/http://www2.cmc.ca/AnnualReport/financials/statement-of-revenue-and-expenditure>
  - CMC Microsystems, *Annual Report 2025-26*, "Statement of Revenue and Expenditure for the year
    ended March 31, 2026", pp. 35–36:
    <https://www.cmc.ca/wp-content/uploads/2026/09/CMCMicrosystemsAnnualReport_2025-26_EN.pdf>
    (the same PDF as `DEM-20`)
- **Verification:** Verified 2026-09-19. The 2025-26 PDF was downloaded and converted with
  `pdftotext`; the 2007/08 statement was fetched from the Internet Archive with `curl`. **CMC is the
  only one of the four programmes in this file that publishes a revenue-and-expenditure statement at
  all.** All figures are Canadian dollars.
- **What it says:**
  - **Year ended 2008-03-31** (the columns are "NSERC Funded Portion of the National Design Network",
    "Other", "ICP", "Total" 2008, "Total" 2007). Revenue lines, Total 2008:
    - "Grant from Natural Sciences and Engineering Research Council of Canada/ICP" **$9,700,060**
    - "Engineering fees" $522,088
    - "Cost sharing for fabrication" $268,425
    - "Interest" $132,380
    - "Donations for courses and annual symposium" $55,930
    - "Other - cost sharing" $143,328
    - **Total revenue $10,822,211** (2007: $10,812,493)

    Expenditure lines, Total 2008: "Salaries and benefits" **$5,285,705**; "Equipment purchases and
    development contracts" $1,965,613; "Travel" $477,329; "Professional fees" $460,261; "Training"
    $377,356; "Rent overhead" $331,751; "Amortization" $311,058; "Office and miscellaneous"
    $174,494; "Contract services" $123,849; "Printing" $96,195; "Telephone" $90,973; "Employee
    search and outplacement costs" $58,598; "Foreign exchange loss" $55,024; "Small equipment,
    supplies and equipment maintenance" $41,504; "Insurance" $30,251; "Repairs and alterations to
    premises" $2,539. **Total expenditure $9,882,500** (2007: $11,510,275).
  - **Year ended 2026-03-31.** "Operations": Revenues **21,535,763** (2025: 13,419,183);
    Expenditures **20,012,740** (2025: 17,066,020); the difference line reads **$1,523,023** for 2026
    and **-$3,646,837** for 2025. Balance sheet: total assets $9,120,399 (2025: $6,898,903);
    liabilities 9,684,682 (2025: 8,986,209); **Net Assets -564,283** (2025: -2,087,306).
    - Revenue pie, as labelled: "ISED **$16.1M**"; "Commercial Fabrication **$3.1M**"; "User Fees
      **$1.3M**"; "Subscriptions **$1.0M**"; "2025-26 Total Revenues $21.5M".
    - Expenditure pie: "FABrIC **$12.8M**"; "Salaries and Benefits **$4.0M**"; "Commercial
      Fabrication and CAD tools **$2.6M**"; "Other **$0.7M**"; "2025-26 Total Expenditures $20.0M".
    - The note beside it, verbatim: "FABrIC is funded by the Innovation, Science and Economic
      Development Canada's Strategic Response Fund and a variant of user fees. The funding agreement
      for this program was amended in 2025, resulting in $2.4M retroactive revenue, all of which was
      recognized in the 2025-26 fiscal year. The current year increase in expenditures correlates
      with the FABriC Challenge grants issued."
    - On the commercial arm: "In the past year, world-wide customers included **95 transactions from
      65 unique organizations** (companies, not-for-profit research organizations, and
      post-secondary) across 8 countries. Canadian customers were 19% of CMC's commercial business
      while the United States accounted for 71%." And: "CMC's increase in services to commercial and
      global customers generates revenue that accelerates innovative R&D in Canada by supporting the
      cost-effective delivery of advanced technologies and services to Canadian researchers."
- **DERIVED (arithmetic written out):**
  - **2007/08 — the cleanest single measurement in this whole file.**
    - Earned from customers = engineering fees 522,088 + cost sharing for fabrication 268,425 +
      donations 55,930 + other cost sharing 143,328 = **$989,771**.
    - As a share of revenue: 989,771 ÷ 10,822,211 = **9.15%**.
    - The NSERC/ICP grant: 9,700,060 ÷ 10,822,211 = **89.63%**. Interest is the remaining 1.22%.
    - Surplus: 10,822,211 − 9,882,500 = **+$939,711**. The prior year: 10,812,493 − 11,510,275 =
      **−$697,782**.
    - Salaries and benefits were 5,285,705 ÷ 9,882,500 = **53.5% of all spending**. A brokerage is
      a payroll.
  - **2025/26.**
    - Earned from customers = user fees 1.3 + subscriptions 1.0 + commercial fabrication 3.1 =
      **$5.4M**.
    - Spending other than the FABrIC pass-through = salaries 4.0 + commercial fabrication and CAD
      tools 2.6 + other 0.7 = **$7.3M**.
    - So the brokerage-and-services operation earned **$5.4M against $7.3M of cost — 74.0% —**
      leaving a **$1.9M gap** filled from public money.
    - Against `DEM-20`'s **240 prototypes fabricated in 2025/26**: non-FABrIC spending per prototype
      = $7.3M ÷ 240 = **CAD $30,417**; earned revenue per prototype = $5.4M ÷ 240 = **CAD $22,500**;
      the gap = **CAD $7,917 per prototype**.
    - Commercial arm: $3.1M ÷ 95 transactions = **CAD $32,632 per transaction**.
  - **The two years together, for scale.** In 2007/08 CMC recovered 9.15% of revenue from customers.
    In 2025/26 the earned lines are 5.4 ÷ 21.5 = **25.1%** of revenue, or **74.0%** of the
    non-FABrIC cost base. On either reading, **the direction over eighteen years is strongly towards
    paying its own way** — but it has not got there, and the gap is still about CAD $1.9m a year.
- **Bears on:**
  - **H6 (challenges, and this is the most precise evidence in the file).** A national
    multi-project-wafer brokerage, audited and published, recovered **nine per cent** of its revenue
    from the people it served. Not nine per cent of its costs — nine per cent of its revenue.
    Everything else was a grant.
  - **H6 (supports).** Eighteen years later the same organisation recovers about three quarters of
    its non-pass-through costs from customers, and its fastest-growing line is a commercial arm
    selling to foreigners at about CAD $32,600 a transaction. If any of the four programmes here is
    converging on self-financing, it is this one, and it is doing it by **selling to commercial
    customers abroad**, not by serving the domestic academic tail.
  - **H5 (challenges).** CAD $30,417 of cost per prototype, and 240 prototypes in a year, for a
    whole country.
- **Used in:** not yet.
- **Caveats:**
  - **The $30,417 per prototype is not the cost of a prototype.** The same $7.3M also buys CAD tool
    subscriptions, training, a startup incubator, cloud services and technical support for "over
    11,000 researchers and more than 1,200 companies". Dividing all of it by prototypes overstates
    what a prototype costs, exactly as in `FUND-2`. It is a *cost per unit of the thing the programme
    is famous for*, not a unit cost.
  - The 2025-26 figures are read off **pie-chart labels rounded to $0.1M**; the labelled slices sum
    to $20.1M against a stated $20.0M total, which is rounding, not error. The two audited totals
    (21,535,763 and 20,012,740) are exact.
  - **FABrIC is a pass-through and must be excluded from any unit-cost calculation.** It is a
    Government of Canada programme CMC *manages*: "20 Challenge projects valued at $35.6M were funded
    with a total FABrIC investment of $13.4M."
  - **No design count was recovered for 2007/08.** The per-design arithmetic above is done only for
    2025/26, where `DEM-20` supplies a count from the same document. For scale only, and **not to be
    quoted as a finding**: if 2007/08 ran at CMC's lifetime average of 13,495 ÷ 42 = 321 designs a
    year, $9,882,500 ÷ 321 = about CAD $30,800 per design — which lands in the same place as the
    2025/26 figure by a completely independent route.
  - The 2007/08 statement is an archived web rendering of the accounts, not the signed audited
    statements; the auditors' report page exists in the same archive but was not opened.
  - Currency: all CAD, unconverted.

### FUND-8. CMP (Grenoble): no accounts at all, but its EU line is now visible — €4.29m across three grants

- **Sources:** the CORDIS records in `FUND-1` and `FUND-4`, read for the Grenoble beneficiary only;
  plus `search-log.md` §1, which records that `mycmp.fr` and `cmp.imag.fr` are both dead.
- **Verification:** Verified 2026-09-19 (the CORDIS side). The CMP side is **not verifiable**: CMP
  publishes no accounts and its own website no longer exists.
- **What it says:**
  - CMP's institutional hosts appear as Europractice beneficiaries in three consecutive grants:
    - NEXTS (2019-01-01 → 2022-09-30): "ASSOCIATION POUR LE DEVELOPPEMENT DES RECHERCHES AUPRES DES
      UNIVERSITES DE L ACADEMIE DE GRENOBL", **€ 1 228 025,00**
    - RETICLES (2022-10-01 → 2025-09-30): "INSTITUT POLYTECHNIQUE DE GRENOBLE", **€ 1 455 625,00**
    - Europractice 2.0 (2025-10-01 → 2028-09-30): INSTITUT POLYTECHNIQUE DE GRENOBLE,
      **€ 1 607 791,25**
  - CMP is absent from the two H2020-and-earlier grants in which imec, STFC and Fraunhofer are the
    only beneficiaries; it joined the consortium with NEXTS, which the NEXTS periodic report confirms:
    "The consortium has been extended with CMP and TYNDALL, who provide access to complementary
    foundry services".
- **DERIVED (arithmetic written out):**
  - € 1 228 025,00 + € 1 455 625,00 + € 1 607 791,25 = **€ 4 291 441,25** of EU money to the Grenoble
    partner across 2019-01-01 → 2028-09-30, a span of 9.75 years: **€ 440 148 a year**.
  - Against `DEM-19`, which has CMP peaking at 401 circuits in 2007 and running 100–400 a year for
    thirty years: if CMP still runs at, say, 200 circuits a year, the EU line alone is about
    **€2,200 per circuit** — the same order as `FUND-2`'s €2,800. **This is an illustration, not a
    measurement**: no current CMP circuit count exists (see `DEM-19`).
- **Bears on:**
  - **H6 (context).** The French national MPW service takes about €440,000 a year of EU money on top
    of whatever CNRS, Grenoble INP and its customers provide. None of the rest is public.
- **Used in:** not yet.
- **Caveats:**
  - **This is CMP's EU line only**, and it is the *Europractice* EU line at that. CMP's French
    funding — CNRS, Grenoble INP, the Région — is not public and was not found.
  - The Grenoble beneficiary's legal name changes between grants (ADRUAG → INP Grenoble). Whether
    the money reached the same team is an assumption, though both are the documented institutional
    hosts of CMP.
  - The per-circuit figure uses an invented denominator. Do not cite it.
