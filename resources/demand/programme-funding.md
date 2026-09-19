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
