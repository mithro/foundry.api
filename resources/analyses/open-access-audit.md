# The open-access audit: which small-customer programmes were actually open, and which were actually businesses

**Status: first pass, committed incomplete on purpose.** Eighteen programmes are scored below,
including one MEMS programme (MEMSCAP's MUMPs, §3.16). The other MEMS shuttles — Silex, Teledyne
DALSA, Tronics, IMT — and X-FAB, imec, Fraunhofer, VTT, EuroCDP and SkyWater's and GlobalFoundries'
own direct offerings are **not yet audited** and are marked as such in the matrix. A matrix with
eighteen rows filled in and the rest marked honestly is more useful than a complete one that does not
exist.

**One of our own claims has already been withdrawn.** `ACC-4` originally read Europractice's 2026
price list as tightening its eligibility rules. `ACC-12` — CMP's October 2019 price list, recovered
later in the same session — shows the condition was seven years old. The claim is corrected in place
rather than quietly removed, and it is listed in §4 alongside everyone else's contradictions.

---

## 1. Why one category was two, and why conflating them hid the finding

Everything in [`../demand/`](../demand/) has been filed under a single heading: *programmes that serve
small chip customers*. Tiny Tapeout, Europractice, MOSIS, CMC, the Google Open MPW shuttles, Muse,
IHP and chipIgnite all sit in the same tables, and their design counts get compared with each other
as though they measured the same thing.

They do not, and the reason is that two entirely different variables have been travelling together
under one name.

**Axis 1 — is access actually open?** Can a person who knows nobody, belongs to nothing and has a
credit card get a chip made? This is a question about *rules*: published prices, self-service
purchase, NDAs, whether the design kit can be copied and redistributed, eligibility by institution
type or country, whether commercial EDA licences are required, whether a gatekeeper decides, whether
the queue is visible, export control, and how large the smallest possible order is.

**Axis 2 — is it a business?** Who actually pays for the wafers? A university running a service at
cost recovery, a national programme whose budget comes from a research ministry, a corporation
running a shuttle out of a marketing budget, and a company trying to earn a margin on each order are
four different organisms. They grow for different reasons, they stop for different reasons, and only
one of them tells you anything about whether foundry.api's business model can work.

**Why conflating them hid the finding.** The repository's most-cited comparison is
[`../demand/efabless-and-the-open-shuttles.md`](../demand/efabless-and-the-open-shuttles.md) §2.2:
Europractice's *free* First User Stimulation Programme drew **98 applications** (`DEM-17`) while
Google's *free* Open MPW programme drew **821 submissions** (`OPG-1`). Because both were free, price
is ruled out. The deep dive reads that gap as evidence about openness. But Europractice's free
programme and Google's free programme differ on **both** axes at once — Europractice is subsidised
*and* restricted, Google was subsidised *and* open — so the comparison cannot separate "openness
attracts people" from anything else that differs between a national consortium and a Google campaign.

Splitting the axes makes three things visible that were not:

1. **Published prices and open access are different criteria, and they come apart.** The TSMC
   University FinFET Program publishes a full price list down to the euro — and to use it you must be
   a university, be a Europractice member, submit an application, have TSMC approve it, sign an NDA
   and receive the design kit through "imec's secure data-sharing platform" (`ACC-5`). It scores
   **2/2 on published prices and 0/2 on six other openness criteria**. Any claim of the form "the
   industry does not publish prices, therefore it is closed" is too quick.
2. **Open to apply is not open to access.** Google's own shuttle page said "The shuttle program is
   open to anyone" (`ACC-9`) while the programme took 40 projects per run by lottery. **DERIVED:** at
   MPW-8's 144 projects against 40 slots, 40 ÷ 144 = **28% accepted — roughly three applicants in
   four were turned away**, on the run the repository cites as the programme's high point.
3. **The commercial axis is where the evidence is thinnest, and it is the axis H6 actually needs.**
   Sorting by who pays shows that almost every programme with large numbers is subsidised, and almost
   every genuinely commercial one is tiny. That is a much more uncomfortable finding than "openness
   works", and it is the one §6 has to deal with.

---

## 2. The scoring rubric

Stated so anyone can re-score a programme from its published pages without asking us what we meant.

### 2.1 Axis 1 — openness

Ten criteria. Each scores **2 (open)**, **1 (partial)** or **0 (closed)**. Where a programme publishes
nothing on a criterion and we could not establish it, the cell is **`?`** and is **excluded from both
the numerator and the denominator** — so a score is always printed as *n* / *max*, and the max varies.
**Never treat `?` as 0.**

| # | Criterion | 2 — open | 1 — partial | 0 — closed |
|---|---|---|---|---|
| **A1** | **Prices published** | A number for the thing a small customer buys, on a public page, no login | Some lines published, or a public calculator rather than a number, or a headline only | "Contact us", "request a quote", "log in for prices" |
| **A2** | **Self-service purchase** | Complete the purchase yourself with a card, no human in the loop | A reservation or registration form with no negotiation | A sales conversation, a purchase order, or a quote request |
| **A3** | **PDK without an NDA** | No agreement at all before you can read the design kit | A click-through or participation agreement you can read before signing | A negotiated NDA, a three-way NDA, or a design-kit licence agreement |
| **A4** | **PDK redistributable** | An OSI-approved licence — name it | Free of charge, no redistribution | Under NDA |
| **A5** | **No eligibility rule** | Anyone, anywhere | A rule most could satisfy (an incorporated entity, a sanctions carve-out), or a price penalty rather than a bar | Must be a university, a member institution, or in a listed country |
| **A6** | **Open tooling suffices** | A documented open RTL-to-GDSII flow the programme itself supports | Open flow usable for part of the job (digital but not analog), or open tools tolerated but not supported | Commercial EDA licences required |
| **A7** | **No gatekeeper** | Anyone who pays and passes machine-checkable requirements is in | A light review, a capacity lottery, or a discretionary clause with no published review process | An application reviewed and approved by a named party |
| **A8** | **Queue and results visible** | Live counts *and* past results public to outsiders | Schedule published, outcomes not | Nothing public |
| **A9** | **No export/citizenship gate** | Nothing imposed on the buyer beyond the law of their own country | A generic export-control compliance clause or a questionnaire at registration | Citizenship, ITAR, security clearance, or domestic-only pricing |
| **A10** | **Low fixed floor** | Smallest possible order under US$1,000 | US$1,000–20,000 | Over US$20,000, or a membership fee payable before you may buy anything |

**A note on A9 that matters.** Scoring "nothing stated" as 2 does not mean the programme is outside
export law. Everyone is inside it. The criterion asks what the *programme* puts in front of the buyer:
a clause the buyer must accept, a form they must fill in, or a nationality they must have.

**A note on A4 that matters more.** Free-of-charge and open-source are not the same thing and the
difference is the whole mechanism in
[`../demand/efabless-and-the-open-shuttles.md`](../demand/efabless-and-the-open-shuttles.md) §2.3(c).
A PDK you may copy, fork and publish lets *third parties* build courses, tools and resellers on it. A
PDK that is merely free does not. That is why A4 is scored separately from A3.

### 2.2 Axis 2 — who actually pays

Four categories, one letter each. A programme may carry a second letter in brackets where the
evidence shows a mixture; the bracket is not decoration, it is a finding.

| Letter | Category | Test |
|---|---|---|
| **U** | University or government research lab | The host is a university or a state institute; the mission is stated as research, education or national capability; cost recovery rather than margin |
| **S** | Government- or corporate-subsidised programme | A named third party pays and the programme is not trying to break even. **Name the grant, the agency, the framework programme number or the corporate sponsor, or do not use this letter** |
| **P** | Commercial entity trying to make a profit on this activity | A company sells the service at a price intended to exceed its cost |
| **M** | Commercial entity running it as marketing or ecosystem-building for another business | A company runs it to sell something else — tools, wafers at volume, an ecosystem |

**P(S)** therefore means "a company trying to profit, materially underwritten by others". That
combination turns out to describe almost every commercial entrant in the record, and §6 argues it is
the single most important qualification on our thesis.

### 2.3 Rules for this audit

- Every criterion answered with an **exact quote and a URL and the date checked**, or marked `?`.
- **Quotes come from what a programme publishes.** No sign-up flow was tested, no form submitted, no
  account created, no quote requested, no human contacted by any channel. Where a page says
  "register to download the PDK" or "contact us for a price", **that sentence is the finding**.
- Where a programme's marketing and its terms disagree, the disagreement is recorded as a finding in
  its own right and flagged in §4.
- Arithmetic is checked by script (`tmp/check_arithmetic.py`, run and deleted).

---

## 3. Programme-by-programme audit

Dates in each entry are the date the page was read. Entries marked **`ACC-n`** cite new evidence in
[`../demand/access-terms.md`](../demand/access-terms.md); entries marked `DEM`, `SMB`, `OPG` or `OPEN`
cite evidence already in the repository, with that entry's own verification status.

### 3.1 Google Open MPW (SKY130 and GF180MCU), 2020–2023 — **15/18 open · S/M**

| | Finding | Source |
|---|---|---|
| A1 | **2.** Free, and said so: "Make Your Own Chips for Free"; "Costs for fabrication, packaging, evaluation boards and shipping are covered by Google for this program." | `DEM-6`, `ACC-9` |
| A2 | **1.** Nothing to buy; submission was a repository plus a platform account, with no salesperson. Not a purchase, so not a card checkout either. | `ACC-9` |
| A3 | **2.** Google's own slides: "Open source, manufacturable 130nm PDK **No NDA required, just clone.**" | `OPG-5` |
| A4 | **2.** `google/skywater-pdk` and `google/gf180mcu-pdk` both return `"spdx_id": "Apache-2.0"` from the unauthenticated GitHub API. | `ACC-6` |
| A5 | **2.** "The shuttle program is open to anyone, provided that their project is fully open source and meets the other program requirements." | `ACC-9` |
| A6 | **2.** Requirements are machine-checkable and the flow is public: "must contain a GDSII layout, which must be reproducible from source", "Projects must successfully pass the Open MPW precheck tool". | `ACC-9`, `OPEN-1` |
| A7 | **0, and this is the finding.** 40 slots per run, chosen: "Each shuttle run will select 40 projects based on the following criteria" (`DEM-8`); the NSF report calls it "a lottery system … to select which set of 40 projects is fabricated on each shuttle" (`DEM-21`). **DERIVED:** MPW-8 finished at 144 projects against 40 slots = **28% accepted**. | `DEM-8`, `DEM-21`, `OPG-2` |
| A8 | **2.** Efabless's platform printed, per shuttle, "Participants … New Users … Projects … Capacity N / 40 … % … Oversubscribed" — publicly, and the Internet Archive kept it. | `OPG-2` |
| A9 | **`?`.** No export-control text was found on the shuttle pages read. Not established either way. | — |
| A10 | **2.** Zero. | `DEM-6` |

**Axis 2: S/M — corporate-subsidised ecosystem-building.** Who pays is stated by the operator in one
sentence: "The rules were simple; create a fully open source design and **Google would pay for your
prototypes**" (`ACC-8`). Google's own blog frames the goal as ecosystem: "allowing around 250 open
source projects to manufacture their own silicon" (`DEM-5`). Nobody was trying to break even, and the
programme ended when the sponsor stopped, not when demand fell
([`../demand/efabless-and-the-open-shuttles.md`](../demand/efabless-and-the-open-shuttles.md) §3).

**Marketing versus terms:** "open to anyone" (marketing, and true of applying) against a 40-slot
lottery (operations, and decisive for three applicants in four). Recorded as the audit's cleanest
example of the gap.

### 3.2 Efabless chipIgnite, 2021–2025 — **16/18 open · P(S)**

| | Finding | Source |
|---|---|---|
| A1 | **2.** "The starting price of $9750 per project includes 100 QFN or 300 WCSP packaged parts and five evaluation boards" (2021); "$14,950 per tapeout" at the successor. | `SMB-9` |
| A2 | **1.** "Guaranteed reservation with $200 deposit", on the platform. Whether that was a card checkout was not established. | `OPG-7` |
| A3 | **2.** No NDA; Matt Venn's retrospective: "they offered hundreds of packaged parts with **no NDAs**". | `OPG-5`, deep dive §2.3(b) |
| A4 | **2.** SKY130 and Caravel both Apache-2.0. | `ACC-6` |
| A5 | **2.** No eligibility rule found anywhere. Efabless's own description of who bought: "startups, Fortune 500 companies, universities, and research institutions around the world". | `OPG-6` |
| A6 | **2.** "Complete EDA design flow" included in the price; OpenLane public. | `OPG-7`, `OPEN-1` |
| A7 | **2.** "Private shuttle -- no open-source requirement"; pay and you are on it. No review process published. | `OPG-7` |
| A8 | **2.** Same public platform statistics as the free programme, including the two runs it labelled `Undersubscribed`. | `OPG-2` |
| A9 | **`?`.** Efabless's terms of service could not be recovered — see §7. | — |
| A10 | **1.** $9,750, later $14,950. | `SMB-9` |

**Axis 2: P — a commercial programme sold at a price the customer pays.**

> ### ⚠️ Correction, 2026-09-19
>
> **An earlier version of this section scored chipIgnite `P(S)` — "a company trying to profit,
> materially underwritten by others" — and called that "the single most important correction the
> audit makes". That scoring was wrong and has been withdrawn.** It rested on three mistakes:
>
> 1. **It conflated the company with the product.** Efabless ran *two distinct programmes*: the
>    **Google-sponsored Open MPW**, which was subsidised, and **chipIgnite**, which customers paid
>    for. Operating a subsidised programme alongside a paid one does not make the paid one
>    subsidised. `OPG-8`'s "Requires External Funding: **No**" for chipIgnite was correct.
> 2. **It treated equity investment as subsidy.** GlobalFoundries was an **investor in Efabless**,
>    not a provider of subsidies. An investor buying equity expects a return; that is the ordinary
>    financing of any company and is categorically different from a grant or a sponsorship. Naming
>    supporters and partners in a farewell letter is not evidence that a product was sold below
>    cost.
> 3. **It reasoned that "a venture-funded company is by definition not yet covering its costs".**
>    That is a non-sequitur. Venture funding says nothing about the unit economics of a particular
>    product line, and nothing found says chipIgnite was sold below its marginal cost.
>
> **The corrected position:** chipIgnite belongs in the open-and-commercial quadrant as a genuine
> `P`. It remains true that Efabless died when a Series B did not close (`OPG-15`), and true that
> the *PDK* chipIgnite ran on was opened by Google's money — that second point is real, it is
> recorded under §6.2, and it applies to every member of the quadrant. Neither fact makes the
> product a subsidy.

chipIgnite is the repository's clearest example of demand at a price the customer actually paid:
$9,750, later $14,950 (`SMB-9`), on a private shuttle with "no open-source requirement" (`OPG-7`).
What the open PDK underneath it was paid for by others is a separate question, treated in §6.2.

### 3.3 Tiny Tapeout — **16/20 open · P(S)**

| | Finding | Source |
|---|---|---|
| A1 | **1.** The per-tile price is published — "each tile is 70€" — and the analog-pin schedule with it. The all-in price is not: "What is the price? You can use our handy calculator to check pricing", and the calculator is a client-side application. | `SMB-10`, `ACC-2` |
| A2 | **2.** A public store and pre-purchase page; no salesperson anywhere in the flow. | `DEM-1`, `ACC-2` |
| A3 | **2.** No NDA. | `OPG-5`, `ACC-1` |
| A4 | **2.** SKY130, GF180MCU and IHP SG13G2, all Apache-2.0. | `ACC-6` |
| A5 | **1.** No institution, country or company requirement — **except** the export clause, which names excluded territories: "Belarus, Cuba, Iran, North Korea, Russia, Syria, Venezuela, and the Crimea, Donetsk, Kherson, Luhansk, and Zaporizhzhia regions of Ukraine". | `ACC-1` |
| A6 | **2.** Wokwi, an HDL of your choice, and a GitHub Action that produces the GDS: "If you're an advanced user, you can use the HDL of your choice." | `ACC-2` |
| A7 | **2, with a recorded reservation.** No review process is published and tiles are pre-purchased — but the terms reserve the right: "Tiny Tapeout may refuse to accept any Design … in its sole discretion". No rejection rate is published. | `ACC-1` |
| A8 | **2.** A public, unauthenticated JSON API giving `tiles_total`, `tiles_used` and every submission record, plus a results page per shuttle. | `DEM-1`, `DEM-2` |
| A9 | **0.** A full EAR / OFAC / ITAR regime in the terms, with named excluded countries and a customer warranty: "You hereby represent and warrant that: (i) no Design and/or Design Documentation you submit hereunder would be subject to the ITAR". | `ACC-1` |
| A10 | **2.** €70. The smallest published unit of chip manufacturing found anywhere. | `SMB-10` |

**Axis 2: P(S).** Tiny Tapeout B.V. is a company and sells at published prices. But `OPG-14` records
that from about January 2024 until Efabless died, "Efabless is sponsoring a special early bird offer
of $150" against a $300 standard price, capped at "The first 80 orders from individuals"; and the live
workshops page lists sponsors including chipIgnite, ChipFoundry, IEEE, IEEE SSCS, Synopsys, CMC, Chip
Design Germany, DTU and several universities. Its founder attributes much of its output to workshops:
"Many of those designs came from high schoolers and students - attendees of my exciting and engaging
Tiny Tapeout workshops" (deep dive §2.3(b)).

**Marketing versus terms, and it is a real one.** Tiny Tapeout is presented throughout this repository
as the most open route to silicon that exists. Its own terms require you to license your design under
Apache 2.0, publish it, accept that it may be refused at the operator's sole discretion, and warrant
that you are not in a sanctioned country, with all fees non-refundable (`ACC-1`). None of that makes
it less open than its competitors — the conditions are conditions *of* openness rather than of
exclusivity — but "no conditions" is not what the contract says, and the audit scores what the
contract says.

### 3.4 Europractice — **3/20 open · S**

| | Finding | Source |
|---|---|---|
| A1 | **1.** A full public price list for most foundries, with no login — and TSMC, the largest, excluded: "Prices for TSMC technologies can be calculated through the online Price Request Form:". | `SMB-7`, `ACC-4` |
| A2 | **0.** "To reserve your seat on a run, please register your design in the Registration Form or contact the Europractice partner responsible for the technology", and a human broker is explicit elsewhere: "We will work with you and do our best to get your design on the run." | `ACC-4`, `DEM-18` |
| A3 | **0.** "Here are quick links to the access information to particular foundries together with the **necessary NDAs (Non-Disclosure Agreements), DKLAs (Design Kit License Agreements)** and contact details"; and per foundry, e.g. Fraunhofer IISB: "customers must have a valid NDA and register at least 4 weeks in advance." | `OPG-17`, `ACC-4` |
| A4 | **1.** Of more than twenty technologies, exactly one is redistributable: "GLOBALFOUNDRIES 180 MCU (Open PDK)". | `ACC-4`, `ACC-6` |
| A5 | **0.** Three cumulative conditions on the 2026 list: an academic institution or publicly funded lab; in one of ~44 listed countries; a paid-up member; **and** "**The intended design will be done for educational purposes or for publicly funded research.**" Non-members may buy, at standard prices. Membership must be paid "before they can make use of EUROPRACTICE services" — €1,100 Full-IC or €600 MPW-only. **We first read the purpose condition as new in 2026 and that was wrong**: `ACC-12` finds it in CMP's October 2019 list, applied to the same members. What *did* change is the country list — CMP's 2019 list named Belarus and Russia, and Europractice's 2026 list names neither. | `ACC-4`, `ACC-12`, `OPG-17` |
| A6 | **0.** Europractice's other main business is selling commercial tool licences — "65,000 concurrent licenses of design tool flows" a year — and the foundry PDKs are vendor PDKs. | `SMB-6` |
| A7 | **0.** A human broker by design (A2), and for FinFET "Applications will be reviewed and approved by TSMC". | `DEM-18`, `ACC-5` |
| A8 | **1.** Schedules and deadlines published per technology per run; per-run submission counts never published; annual totals published in the activity reports. | `ACC-4`, `DEM-16` |
| A9 | **0.** Export control is a registration step for several foundries: "Registration and Export Control information deadlines. Please download the Export Control file here."; and under UMS, "Please fill in the Export Control questionnaire when registering your design". | `ACC-4` |
| A10 | **0.** A membership fee before you may buy, plus a minimum billable area on every line, plus a €1,000 charge for splitting a block four ways. **DERIVED:** the cheapest commercial ticket on the open-PDK line is 6 mm² × €913 = **€5,478**; on GF 130 nm BCDlite it is 12 × €1,760 = **€21,120**. | `SMB-7`, `ACC-4` |

**Axis 2: S — EU-subsidised, by its own account.** "European Union (EU) funding has significantly
lowered the cost of participating in and using the Europractice service… Absent public funding,
advanced technologies would be made available much later or not at all, niche and emerging
technologies from European sources could not be stimulated to a level that makes them viable"
(`SMB-6`). Launched by the European Commission in 1995 as successor to EUROCHIP.

**New finding: a small-customer surcharge, published.** The standard GlobalFoundries MPW line prices
130 nm BCDlite at €1,760/mm²; the mini@sic line — the option for customers too small to take a whole
block — prices the same family at €3,080/mm². **DERIVED:** 3,080 ÷ 1,760 = **1.75, a 75% surcharge
for being small** (`ACC-4`). That is the cost of serving a small customer, turned into a price, by the
organisation that has been doing it longest.

### 3.5 ChipFoundry.io (UmbraLogic Technologies LLC) — **16/18 open · P**

| | Finding | Source |
|---|---|---|
| A1 | **2.** "The standard pricing is $14,950 per project for standard shuttle participation." | `ACC-3` |
| A2 | **1, and this is the surprise.** "You can reserve your spot on an upcoming shuttle by **submitting a request to us through this form**." Discounts are explicitly negotiated: "To request a custom quote for a project pool, please contact us." | `ACC-3` |
| A3 | **2.** No NDA to see the PDK; the PDK is SKY130. | `ACC-3` |
| A4 | **2.** Apache-2.0. | `ACC-6` |
| A5 | **2.** None published. The stated audience is "Educational Institutions … Hardware Startups … OEMs … Independent Hardware Developers". | `ACC-3` |
| A6 | **2.** "Open Source: OpenLane for RTL-to-GDSII digital design flow". | `ACC-3` |
| A7 | **2.** "chipIgnite is a private shuttle with no open-source requirement for your designs"; no review published. | `ACC-3` |
| A8 | **2, and it is the best in the audit.** A public, unauthenticated API prints `interest`, `planned`, `reserved` and `committed` per shuttle. | `OPG-9` |
| A9 | **`?`.** `chipfoundry.io/terms` returns HTTP 404; no export text found. | §7 |
| A10 | **1.** $14,950. | `ACC-3` |

**Axis 2: P — commercial, and no subsidy found.** A Delaware-style LLC footer ("© 2026 UmbraLogic
Technologies LLC"), a published price, and terms that put the fill risk on itself: "If a shuttle does
not meet the minimum customer commitment threshold required for launch, you will be offered: A full
refund of your project fee, or The option to roll over your project to the next scheduled shuttle"
(`ACC-3`). **No grant, agency or corporate sponsor was found for it.** On the evidence gathered,
ChipFoundry is the audit's cleanest example of a genuinely open, genuinely commercial programme.

**And it is small.** Its own API gives committed customers per shuttle as 21, 23 and 29, against
planned slots of 28, 37 and 43 — **not one completed shuttle has filled** (`OPG-9`). **DERIVED:**
21 × $14,950 = **$313,950** and 29 × $14,950 = **$433,550** of gross revenue per shuttle, at "2
shuttles in 2025 and 3 in 2026" (`ACC-3`).

### 3.6 IHP Open Silicon MPW (paid, 2026) — **14/18 open · U(S)**

| | Finding | Source |
|---|---|---|
| A1 | **2.** Published per-run: "SG13G2 - 2800€ per ㎟" and "SG13CMOS5L - 1500€ per ㎟", with "Minimum area 90㎟" and "Lowest price 900€ per ㎟" printed on the page. (㎟ is the single-character form of mm², as the source prints it: €2,800 and €1,500 per mm², 90 mm² minimum, €900 per mm² floor.) | `OPG-11` |
| A2 | **1.** A registration page, and "**Participation requires signing the Open Silicon MPW Program Participation Agreement.**" | `OPG-11` |
| A3 | **1.** A participation agreement, not an NDA, and the PDK is public regardless. | `OPG-11` |
| A4 | **2.** `IHP-GmbH/IHP-Open-PDK`, Apache-2.0. | `ACC-6` |
| A5 | **2** for the paid programme (none published) — but **0 for the free era it replaced**: "Project funds can be used exclusively to produce chip designs for **non-commercial activities**, such as university education, research projects, and others." | `OPG-10`, `OPG-11` |
| A6 | **2.** Open PDK, open flow, submissions by pull request against a public repository. | `OPG-10` |
| A7 | **1.** The free era selected: "All designs, which have passed tests will be submitted for a selection process according to criteria presented below." The paid era appears to be registration, but no statement either way was found. | `OPG-10` |
| A8 | **2, and it is remarkable.** The registration page publishes **every customer's name and registered area, live**: IHP_ext 2, Lund University 1, Navia Labs 9, Tiny Tapeout B.V. 18, NEBULA MICROSYSTEMS 3, Simra AI 1, Ulster University 1.2, IEEE Circuits and Systems Society 24. | `OPG-11` |
| A9 | **`?`.** Not established. | — |
| A10 | **1.** No per-customer minimum was found; the *run* has one, and the price falls as aggregate area rises. | `OPG-11` |

**Axis 2: U(S) — a Leibniz institute, and the free era was a named German public project.** "It is
also a central point for design fabrication under the concept of IHP Free MPW runs funded by a public
German project **FMD-QNC (16ME083)**" (`OPG-10`). The 2026 paid programme is the same institute
charging for the same thing — which makes it the best natural experiment in the record (§6.4).

**A finding worth stating on its own.** IHP prices **openness itself**: "Customers who choose to
release their designs under the Apache License 2.0 can benefit from our lowest-cost MPW offering",
and "For customers who do not wish to disclose their intellectual property, IHP offers participation
in the same open-silicon MPW program at 20% off the standard MPW price" (`OPG-11`). Against IHP's
standard SG13G2 price of €7,300/mm² (Partial, `SMB-7`), the open route at €2,800/mm² is **DERIVED** a
62% discount. Nowhere else in this audit is the value of publishing a design quoted as a number.

### 3.7 wafer.space — **17/18 open · P** *(conflict of interest: the repository owner's own company)*

| | Finding | Source |
|---|---|---|
| A1 | **2.** A four-row price card with early-bird and standard prices and the per-die price computed on the page: $2,000/$3,000 up to $7,000/$8,000, every slot "1000 dies per slot". | `ACC-7` |
| A2 | **2.** Crowd Supply checkout. No salesperson at any point. | `ACC-7`, `OPG-12` |
| A3 | **2.** None. | `ACC-7` |
| A4 | **2.** GF180MCU, Apache-2.0. | `ACC-6` |
| A5 | **2.** None published. | `ACC-7` |
| A6 | **2.** Open flow; the site links a "LibreLane pad ring generator" and a project template. | `ACC-7` |
| A7 | **2.** No review; buy a slot, submit a clean GDS by the deadline. | `ACC-7` |
| A8 | **2.** Published deadlines to the minute, a live backer count, and the previous run's full design list: "29 open-source designs from universities, startups, and hobbyists worldwide", named, with source links. | `ACC-7` |
| A9 | **`?`.** No terms page found on `wafer.space`; Crowd Supply's own terms were not read. | §7 |
| A10 | **1.** $2,000. | `ACC-7` |

**Axis 2: P — commercial, Singapore-registered, no subsidy found.** "© 2025 Wafer Space PTE. LTD."
Its own FAQ separates openness of the kit from openness of the customer's design: "**Do I have to
open-source my design? No. The PDK is open; your design can be open or closed.**" (`ACC-7`).

**And it is the smallest thing in the audit.** 6 backers, then 18, then 5 so far (`OPG-12`, `ACC-7`).
**This row must be discounted for self-interest**: it is our own company, scored by us, on our own
rubric, and it comes out top. It is included because leaving it out would be worse, and flagged
because a reader must be able to strike it.

### 3.8 MOSIS 1.0 (USC ISI, 1981–c. 2020) — **4/14 open · U**

| | Finding | Source |
|---|---|---|
| A1 | **2.** Public price lists for decades: "First lot of 40 parts (rounded to nearest whole dollar): $17,500 + ($4,000/mm² * 32.081 mm²) = $145,824". | `SMB-8` |
| A2 | **1.** Orders through MOSIS's own system; not established whether a card sufficed. | `SMB-8` |
| A3 | **0.** Foundry PDKs (Orbit, IBM, TSMC) under vendor NDA. | `OPG-8` |
| A4 | **0.** None redistributable. | `OPG-8` |
| A5 | **`?`, and this is a gap worth naming.** MOSIS published a "**domestic** price list", which implies a domestic/foreign distinction with an export dimension — **we did not recover the eligibility text that goes with it.** | `SMB-8`, §7 |
| A6 | **0.** Commercial EDA. | `OPG-8` |
| A7 | **`?`.** Not established. | — |
| A8 | **1.** Schedules published; per-run results not. | `SMB-8` |
| A9 | **`?`.** See A5. | §7 |
| A10 | **0.** "The minimum area for 0.13 micron processes is 10.0 mm²", and the fixed fee alone was $17,500. **DERIVED:** at the minimum, $17,500 + 10 × $4,000 = $57,500, of which **30% is fixed charge before any silicon**. | `SMB-8` |

**Axis 2: U — a university service, and the one entity in the whole record described as covering its
own costs.** "'MOSIS has been extremely successful,' Mike Haney, Deputy Director of the DREAMS hub,
said. '**Even though it was run by a university, it was a self-sustaining business for 40 years.**'"
(`SMB-5`). Its *free academic* programme was separately subsidised and was withdrawn: "MOSIS
previously had a free academic program for tape-outs which was supported by NSF and industry but was
discontinued in 2020" (`DEM-21`). **MOSIS 2.0 is U(S)** — it runs under the federally funded CA
DREAMS Microelectronics Commons hub and its stated goal is to "achieve self-sustainability within the
next few years" (`SMB-5`), i.e. it is not self-sustaining now.

**Scale, for the comparison in §6.3:** "Over four decades, MOSIS delivered more than 60,000 integrated
circuit designs and generated **up to $10 million annually at its peak**", at "around 3,000 orders per
year" (`SMB-5`).

### 3.9 MUSE Semiconductor — **1/18 open · P/M (unresolved)**

| | Finding | Source |
|---|---|---|
| A1 | **0.** Pages titled "…Services and Price" that contain no price. The Wix application renders client-side and the ~494 KB response has no price string; the most recent Wayback capture is the same empty shell. | `SMB-13`, `OPG-18` |
| A2 | **0.** Not possible; the route is a quote. | `OPG-18` |
| A3 | **0.** "We require only two agreements: A Mutual Non-Disclosure Agreement (MNDA)…A **TSMC 3-way NDA** between Muse, TSMC, and the customer." (plus a Master Technology Usage Agreement for TSMC IP access) | `OPG-18` |
| A4 | **0.** TSMC PDK. | `OPG-18` |
| A5 | **1.** University-focused but not university-only: "Yes! We have several commercial customers. Semiconductor startups and semiconductor IP suppliers can access TSMC technology cost-effectively." | `OPG-18` |
| A6 | **0.** TSMC flow. | — |
| A7 | **0.** A three-way NDA with the foundry is a foundry approval step by construction. | `OPG-18` |
| A8 | **0.** The schedule page is the same unreadable shell. | `OPG-18` |
| A9 | **`?`.** Not established. | — |
| A10 | **0.** `OPG-8` gives "~$24k USD" for 10 mm² of the nearest node — **unverified, from the comparison document alone**. | `OPG-8` |

**Axis 2: P/M, unresolved.** A commercial company acting as TSMC's university channel. Whether it is
trying to profit on the shuttle or to seed TSMC's future customer base is not established, and
`OPG-8` marks its external-funding cell "Maybe?".

### 3.10 TSMC cyberShuttle — **0/18 open · P/M**

Every criterion that could be checked is closed, and the whole finding is one sentence on TSMC's own
page: "**If you are a TSMC customer, login to TSMC-Online or contact your local TSMC representative
for the latest CyberShuttle® schedule.**" (`SMB-13`, verified). No price, no schedule, no PDK without
a foundry relationship, no eligibility for anyone who is not already a customer, nothing public about
the queue. A1–A8 and A10 score 0; A9 is `?`. **DERIVED:** nine criteria established, eighteen points available, zero scored.

**Axis 2: P/M.** The world's largest foundry, running a shuttle for customers it already has.

### 3.11 TSMC University FinFET Program, via Europractice / imec IC-link — **3/18 open · S**

The audit's demonstration that **published prices and open access are independent**.

- **A1 = 2.** Full published price table: "TSMC 7nm Log FinFET (min area = 2mm²) 49,050" EUR, down to a
  mini@sic line at "16,850" EUR for 1 mm² (`ACC-5`).
- **A5 = 0.** "EUROPRACTICE-member universities"; "also open to universities in North America".
- **A7 = 0 and A3 = 0**, in one sentence: "**Applications will be reviewed and approved by TSMC, after
  which an NDA will be shared. Access will be granted through imec's secure data-sharing platform.**"
- **A4 = 0**, **A6 = 0**, **A2 = 0**, **A8 = 1** (MPW schedules published), **A9 = `?`**,
  **A10 = 0** (**DERIVED:** €49,050 ÷ 2 mm² = **€24,525/mm²** at the minimum).
- One kit is teaching-only: "N16ADFP (Academic Design Foster Package): **For Teaching Purpose Only**".

**Axis 2: S.** Inside the EU-subsidised Europractice envelope, with TSMC contributing access —
corporate ecosystem-building on the foundry's side and public subsidy on the broker's.

### 3.12 Cadence / SkyWater SKY130 MPW aggregation — **partially audited, 6/8 scored · M**

- **A1 = 2:** "USD $10,000 per design", with "40 bare die" (`OPG-19`, **Partial**).
- **A3 = 1:** each submission requires "an executed legal agreement" — less than an NDA, more than
  "just clone".
- **A4 = 2:** the open SKY130 PDK.
- **A6 = 1:** verification "uses the Cadence® Pegasus™ Physical Verification Solution, based on the
  SKY130 design rules" — a commercial tool in the required path.
- A2, A5, A7, A8, A9, A10: **not established.**

**Axis 2: M.** The largest EDA vendor running an open-PDK shuttle. "Cadence plans to offer multiple
MPW runs per year"; the audience is "students and researchers to entrepreneurs and early-stage
teams". No slot or submission count is published, so it cannot enter any series (`OPG-19`).

### 3.13 CMC Microsystems (Canada) — **not audited beyond two cells · U(S)**

- **A1 = 0:** `cmc.ca/en/WhatWeOffer/Make/FabPricing.aspx` returns **HTTP 403** to an automated fetch
  (`SMB-13`, search log). Not established whether prices are published to a human with a browser.
- **A3 = 0** and **A5 = 0** on `OPG-8`'s comparison-document cells ("NDAs required: Yes";
  "Commercial Allowed: Restricted") — **owner-supplied, not confirmed from CMC's own pages.**
- Everything else: **not audited.**

**Axis 2: U(S).** A publicly funded Canadian national programme; `DEM-20` records 13,495 designs over
42 years and a fall to 240 prototypes in 2025-26, and warns that "A falling count may be a falling
budget."

### 3.14 CMP / Circuits Multi-Projets (France) — **context row, defunct · U(S)**

Not scorable: "CMP no longer exists as an operating service"; `mycmp.fr` is a parked domain and
`cmp.imag.fr` is dead (`DEM-19`). It ran 100–400 circuits a year for thirty years and stopped for
supply-side reasons — Europractice's 2022 report records that CMP "had to stop fabrication activities
at STMicroelectronics, ams and CEA-Leti due to administrative reasons". A successor, CIME-P, appears
in Europractice's 2026 schedule as the body designs are submitted to (`ACC-4`), but its own terms were
**not audited**.

### 3.15 The AFRL / AFWERX design challenge, 2018–2020 — **context row, and the audit's best counter-example · S**

Closed on almost every criterion: the node was 14 nm, "the designs were proprietary", entry was by
competition, and selection was by a government body. **A4 = 0, A5 = 0, A7 = 0.** The one open
criterion is unusual: "the entrants had to agree to publish their IC designs, the intended
applications and other key information in order to enter the challenge" (`ACC-8`).

**It drew 82 unique IC designs in 45 days, "80 percent from small enterprises and academics", with
"the cost of IP, EDA and foundry … covered" if selected** (`ACC-8`, **Partial** — Efabless's own
newsletter describing someone else's programme; the primary AFRL source was not found).

**DERIVED:** 82 ÷ 45 days = **1.82 designs a day**, against Google's first open shuttle at 45 ÷ 30 =
**1.50 a day** (or 37 ÷ 30 = 1.23 on Efabless's own platform count). **A closed, gate-kept,
government-funded competition out-drew the open shuttle per day of open window.** §6.2 deals with
what that does and does not show.

---

### 3.16 MEMSCAP MUMPs (PolyMUMPs, SOIMUMPs, PiezoMUMPs), 1992–2023 — **10/18 open · P/M**

The only MEMS programme audited, and the most interesting row in the table, because it is the one
combination the rest of the record lacks: **a commercial company publishing prices on a closed
process.**

| | Finding | Source |
|---|---|---|
| A1 | **2.** A public price list, no login: "1 Standard Die Site - 15 die delivered" at **$5,800** non-academic and **$4,200** academic, "Additional Standard Die Sites on same run $3000/ea". | `ACC-10` |
| A2 | **0.** A quote number, an FTP account and a CAPTCHA stand between you and a submission: "you'll need the temporary userid and password assigned to you in your reservation confirmation email"; the submission form requires "Quote# *". | `ACC-10` |
| A3 | **1.** No NDA to read the design rules, which are a public download — but the CAD kits are routed through tool vendors: "To receive design kits for Coventorware, SoftMEMS, or Intellisense, please visit the following links". | `ACC-10` |
| A4 | **1, and it is an unusual 1.** "**All of the documents below are free to download and distribute.**" That is explicit redistribution permission for design rules, run data, FAQs and course slides — but it is a sentence on a web page, not a licence, and it covers the documentation, not the process. | `ACC-10` |
| A5 | **2.** No institution, country or company requirement found. The academic rate is a **discount**, not a gate: **DERIVED**, $4,200 ÷ $5,800 = **72.4%** of the commercial rate. | `ACC-10` |
| A6 | **0.** L-Edit, CoventorWare, IntelliSense or SoftMEMS. There is no open MEMS flow here at all. | `ACC-10` |
| A7 | **2.** "reserve a die site on a scheduled run, and start designing!" No review or selection process is described anywhere. | `ACC-10` |
| A8 | **1.** A published run schedule with design deadlines and ship dates — PolyMUMPs runs 133–136, PiezoMUMPs 23–26, SOIMUMPs 74–77 — but **no submission count, no fill rate and no list of who was on a run**, ever. | `ACC-10` |
| A9 | **`?`.** Nothing found. MEMSCAP is French with a US operation and MEMS can be export-controlled, so absence of a statement is not evidence of absence. | §7 |
| A10 | **1.** $4,200–$5,800. | `ACC-10` |

**Axis 2: P/M.** A listed French company (MEMSCAP S.A., Crolles) running a shuttle beside a sensor and
optical-attenuator business. Its own page calls it "a well-established, Multi Project Wafer
**commercial** program". No subsidy was found. But the parent's revenue comes from products, and the
half-year results MEMSCAP publishes today describe only those products — which is why the row is
P/M rather than P.

**And it is gone from the public internet.** The MUMPs page last returned HTTP 200 on **2023-01-30**
and was **404 by 2023-11-15**; MEMSCAP's current site has no foundry or MPW section at all; and
`memsrus.com`, the programme's historic domain, is now a spam blog (`ACC-11`). **Nothing found says
the programme stopped, and this audit does not claim it did** — but a new customer reading MEMSCAP's
site today would not learn that a MEMS shuttle exists. That is the access barrier this audit measures,
in its maximum form.

**Why this row matters more than its score.** MUMPs ran for thirty-one years, published its prices
throughout, published a run schedule, let anyone redistribute its design rules, and had no eligibility
rule — on a **closed** process, with **no open tooling**, as a **commercial** programme. If openness
of the *PDK* were the whole mechanism, MUMPs should have been unable to build a community; if
published prices and free documentation were sufficient, it should have grown. Neither happened:
"Over 80 full process runs … to hundreds of organizations" in three decades, at three to four runs a
year. **It is the audit's best single case that published prices and free documentation are not
sufficient, and it sits directly against `ACC-8`'s case that an open PDK is not necessary.**

### 3.17 MOSIS 2.0 (USC ISI, under CA DREAMS), 2024– — **1/6 scored · U(S)**

The successor to §3.8, and it is a different organism. Audited from pages fetched during this session
on 2026-09-18; **Partial**, because the pages were retrieved by a delegated agent that was terminated
before reporting, and were read here from the saved files rather than re-fetched.

| | Finding |
|---|---|
| A1 | **0.** **No price appears anywhere** on the MOSIS 2.0 home page, MPW-services page or IC-design page. A search of all three for a currency figure or the word "price" returns nothing. |
| A2 | **0.** The route is a form and an account: "Don't miss out on any upcoming MOSIS 2.0 MPW runs. Click the button below to sign up and secure your spot!" under a button reading "MPW Run Sign Up", with "Login" in the site navigation. |
| A8 | **1.** A public tapeout-schedule tool: "Please use the fields below to find a tapeout schedule for our available foundry services", with a "Foundry Service" selector listing GlobalFoundries, HRL, Intel, Northrop Grumman Corporation, RTX, Samsung, Sandia National Lab, SkyWater and Teledyne. The schedule carries a caveat: "Our DIB partners' MPW schedules are subject to change based on MOSIS 2.0 and Foundry internal schedules. Additional MPW tape-out opportunities may be available upon request for dedicated MPW services". |
| A3, A4, A5, A6, A7, A9, A10 | **`?`.** Not established from the pages read. **No export-control, ITAR or citizenship text was found** on any of them — which is notable given the funder, and is an absence, not a finding. |

**Axis 2: U(S) — a university institute inside a defence programme, and it says so.** From its own
FAQ: "CA DREAMS, led by the University of Southern California Information Sciences Institute
(USC/ISI), accelerates the development of onshore microelectronics hardware by uniting academic and
industry institutions. As part of the **Department of War's Microelectronics Commons Program**, CA
DREAMS focuses on three key objectives: advancing RF technologies for rapid prototyping, enabling
seamless lab-to-fab transitions, and training the next generation of engineers and technicians in
cutting-edge RF and microelectronics." And: "MOSIS 2.0 functions at the core of CA DREAMS by
connecting innovators to a vast network of nanofabrication and foundry services". Page footer: "©2026
University of Southern California". `SMB-5` already records that its goal is to "achieve
self-sustainability within the next few years" — i.e. it is not self-sustaining.

**The change that matters for this audit.** MOSIS 1.0 published its prices for decades — `SMB-8` has
them down to the dollar, "$17,500 + ($4,000/mm² * area)". **MOSIS 2.0 publishes none.** The service
that pioneered the published price list for small chip customers, and that was described by its own
host as "a self-sustaining business for 40 years", has been rebuilt as a sign-up form inside a defence
programme. **On the audit's first criterion it went backwards.**

Its brokered portfolio is also far larger than 1.0's: "commercial silicon MPW services from leading
foundries, including TSMC, Intel, Samsung, SkyWater Technology, GlobalFoundries, and Tower
Semiconductor. Covering technology nodes from 12 nm to 350 nm", plus "three DoW-volume fabs—HRL
Laboratories, Teledyne, and Northrop Grumman—to offer advanced group III/V MPW services". Breadth up,
transparency down.

### 3.18 X-FAB, prototyping services — **2/8 scored · P**

A commercial foundry's own shuttle, audited only on what its prototyping page shows. **Partial**: the
page was fetched during this session by a delegated agent that was terminated before reporting, and
was read here from the saved file.

| | Finding |
|---|---|
| A1 | **0.** No price anywhere on the page. For anything outside the published schedule: "If you cannot find a suitable MPW shuttle in the schedule below, please **contact your local sales manager** who will check the possibility of additional MPW runs that are available on request." And on lead times: "To find out the timescales of standard engineering lots please **contact your local sales and support office**." |
| A2 | **0.** The route is a sales contact. The page's own contact form carries a reCAPTCHA field. |
| A5 | **1.** No bar, but a routing: "**European Academic institutions are requested to apply via the EUROPRACTICE program.**" X-FAB "has joined in 2013" that programme, which "offers specialized customer support for academic participants and SMEs on a worldwide basis". So an academic in Europe inherits Europractice's three conditions (§3.4) rather than dealing with X-FAB. |
| A8 | **1.** A published "MPW Schedule 2026" with columns "PROCESS / TAPE-IN / DATA RELEASE / SAMPLES OUT" — e.g. "XT011 3-Nov-2025 17-Nov-2025 22-May-2026" — across 1.0 µm, 350 nm, 180 nm, 130 nm and 110 nm. No fill rates, no participant counts. |
| A3, A4, A6, A7, A9, A10 | **`?`.** Not established from the page read. The site navigation includes an "IP Portal", which suggests a login, but that was not checked. |

**Axis 2: P — a commercial foundry, selling prototyping as a step toward volume.** The page frames it
that way: both services carry the disadvantage "**No volume production with these masks**", and the
MPW's benefit is "Development charges significantly reduced". X-FAB is also one of the companies
Efabless's CEO thanked for support (`OPG-15`), so it appears on both sides of this audit.

**What the row is worth.** It is the plain commercial baseline the open programmes are measured
against: a real foundry, a real published schedule, and no price without a salesperson.

## 4. Where marketing and terms disagree

Recorded prominently, as instructed, because each one is a finding in its own right.

| Programme | The marketing | The terms | Verdict |
|---|---|---|---|
| **Google Open MPW** | "The shuttle program is open to anyone" (`ACC-9`) | 40 slots per run, selected by lottery (`DEM-8`, `DEM-21`); **28% accepted at MPW-8** | **Both true, and the gap is the point.** Open to apply ≠ open to access |
| **Tiny Tapeout** | The cheapest, most open route to silicon; €70 a tile | Apache-2.0 compulsory, publication compulsory, refusal at "sole discretion", full EAR/OFAC/ITAR regime with named excluded countries, all fees non-refundable (`ACC-1`) | Not a contradiction, but "no conditions" is not what the contract says |
| **ChipFoundry** | "$14,950 per project", published, flat | "reserve your spot … by submitting a request to us through this form"; discounts "request a custom quote … contact us" (`ACC-3`) | **A published price you cannot buy without a form.** Self-service scores 1, not 2 |
| **Europractice** | A public price list, thirty years old, no login | Membership fee before use; institution type, country and — new in 2026 — *purpose* (`ACC-4`, `OPG-17`) | The price list is open; the service is not |
| **TSMC University FinFET** | Prices published to the euro | "Applications will be reviewed and approved by TSMC, after which an NDA will be shared" (`ACC-5`) | The sharpest case of the two criteria coming apart |
| **chipIgnite / Efabless** | `OPG-8`: "Requires External Funding: **No**" | *(the apparent contradiction was withdrawn 2026-09-19 — see the correction box in §3.2)* | **No contradiction. `OPG-8` was right: chipIgnite was paid for by its customers.** Efabless separately ran the subsidised Google Open MPW; GlobalFoundries was an investor, not a subsidiser |
| **MOSIS** | "a self-sustaining business for 40 years" (`SMB-5`) | Its free academic arm was "supported by NSF and industry" and was discontinued in 2020 (`DEM-21`); MOSIS 2.0's goal is to "achieve self-sustainability within the next few years" | Two different things called MOSIS |
| **MOSIS 1.0 → 2.0** | The service that pioneered published prices for small chip customers | MOSIS 2.0 publishes **no price at all**; the route is an "MPW Run Sign Up" form and a login (§3.17) | **It went backwards on the audit's first criterion** |
| **Europractice eligibility** | We claimed the 2026 list tightened the rules (`ACC-4` as first written) | CMP's October 2019 list carries the same purpose condition for the same members (`ACC-12`) | **Our own overstatement, corrected.** What did change is that Belarus and Russia left the eligible-country list |

---

## 5. The matrix

`2` open · `1` partial · `0` closed · `?` not established (excluded from the score) · `—` not yet
audited. **Score = points ÷ points available on the criteria actually established.**

| Programme | A1 price | A2 self-serve | A3 no NDA | A4 redistributable | A5 no eligibility | A6 open tools | A7 no gatekeeper | A8 queue visible | A9 no export gate | A10 low floor | **Open score** | **Axis 2** | Scale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **wafer.space** | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | ? | 1 | **17/18** | **P** | 6, 18, 5 backers |
| **Tiny Tapeout** | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 0 | 2 | **16/20** | **P** | ~4,300 designs in 4 yr |
| **Efabless chipIgnite** | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | ? | 1 | **16/18** | **P** | 763 subs / 13 shuttles; dead |
| **ChipFoundry.io** | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | ? | 1 | **16/18** | **P** | 21–29 paying per shuttle |
| **Google Open MPW** | 2 | 1 | 2 | 2 | 2 | 2 | 0 | 2 | ? | 2 | **15/18** | **S/M** | 821 subs / 10 shuttles; ended |
| **IHP Open Silicon MPW** | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | ? | 1 | **14/18** | **U(S)** | 59.2 mm² registered on one run |
| **Cadence/SkyWater MPW** | 2 | — | 1 | 2 | — | 1 | — | — | — | — | **6/8** | **M** | not published |
| **Europractice** | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | **3/20** | **S** | 753–985 designs/yr |
| **MEMSCAP MUMPs** | 2 | 0 | 1 | 1 | 2 | 0 | 2 | 1 | ? | 1 | **10/18** | **P/M** | >80 runs in 31 yr; page gone 2023 |
| **MOSIS 1.0** | 2 | 1 | 0 | 0 | ? | 0 | ? | 1 | ? | 0 | **4/14** | **U** | ~3,000 orders/yr at peak |
| **MOSIS 2.0** | 0 | 0 | ? | ? | ? | ? | ? | 1 | ? | ? | **1/6** | **U(S)** | not published |
| **TSMC Univ. FinFET** | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | ? | 0 | **3/18** | **S** | not published |
| **X-FAB prototyping** | 0 | 0 | ? | ? | 1 | ? | ? | 1 | ? | ? | **2/8** | **P** | not published |
| **MUSE Semiconductor** | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | ? | 0 | **1/18** | **P/M** | not published |
| **TSMC cyberShuttle** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ? | 0 | **0/18** | **P/M** | not published |
| **CMC Microsystems** | 0 | — | 0 | — | 0 | — | — | — | — | — | **0/6** | **U(S)** | 240 prototypes 2025-26 |
| **CMP (defunct)** | — | — | — | — | — | — | — | — | — | — | **n/a** | **U(S)** | peaked 401 circuits/yr |
| **AFRL design challenge** | — | — | — | 0 | 0 | — | 0 | — | — | — | **0/6** | **S** | 82 designs in 45 days |
| Silex, Teledyne DALSA, Tronics, IMT | — | — | — | — | — | — | — | — | — | — | **not audited** | — | — |
| imec, Fraunhofer, VTT | — | — | — | — | — | — | — | — | — | — | **not audited** | — | — |
| SkyWater direct, GF direct | — | — | — | — | — | — | — | — | — | — | **not audited** | — | — |
| EuroCDP | — | — | — | — | — | — | — | — | — | — | **not audited** | — | — |

**Read the Europractice row against the others carefully.** 3/20 against Tiny Tapeout's 16/20 is a
real difference in access rules. It is *not* a claim that Europractice is worse at its job:
Europractice fabricates more designs a year than the entire Google Open MPW programme fabricated in
its life, on more than twenty processes up to 12 nm, for a population it was built to serve.

---

## 6. Verdict: does openness or profit-motive predict growth?

### 6.1 The quadrants, and which are empty

Cross the two axes. Take "open" as **≥ 12/18-equivalent** (two-thirds of available points) and
"commercial" as **P or P(S)**.

| | **Subsidised / academic (U, S, M)** | **Commercial (P)** |
|---|---|---|
| **Open (≥ ⅔)** | Google Open MPW (S/M), IHP Open Silicon (U(S)), Cadence/SkyWater (M) | **wafer.space, ChipFoundry.io, Tiny Tapeout, Efabless chipIgnite** |
| **Closed (< ⅔)** | Europractice (S), MOSIS 1.0 (U), MOSIS 2.0 (U(S)), CMC (U(S)), CMP (U(S)), TSMC Univ. FinFET (S), AFRL (S) | **MEMSCAP MUMPs (P/M, 10/18 — the near miss)**, X-FAB (P), MUSE (P/M), TSMC cyberShuttle (P/M) |

**MEMSCAP's MUMPs is the row to look at hardest**, because at 10/18 it is the only entry that sits
near the line from the *closed* side while being commercial. It published its prices for thirty-one
years, published a run schedule, let anyone redistribute its design rules, and imposed no eligibility
rule — and it still scores 0 on open tooling and 0 on self-service, because the process was closed and
every route to a submission ran through a quote (§3.16). It is the audit's cleanest demonstration that
**published prices plus free documentation, without an open PDK or an open tool flow, produce a
service that lasts three decades and stays small.**

**So the "genuinely open AND genuinely commercial" quadrant is not empty. It has four members. That
is the good news, and it is the only good news in this section.**

Now look at what is in it:

- **Efabless chipIgnite** — dead. Failed to close a Series B (`OPG-15`).
- **ChipFoundry.io** — 21, 23 and 29 paying customers per shuttle; **not one completed shuttle has
  filled its planned slots** (`OPG-9`). **DERIVED:** ~$314k–434k gross per shuttle, at 2–3 shuttles a
  year, is roughly **$1M a year of gross revenue**.
- **wafer.space** — 6, 18 and 5 backers. **Our own company**, scored by us.
- **Tiny Tapeout** — thousands of designs, but at €70–€300 each, and it buys its wafer space from the
  other three. It is a reseller sitting on top of this quadrant, not an independent occupant of it:
  `OPG-11` shows Tiny Tapeout B.V. as an 18 mm² line in IHP's book, and `OPG-5` shows it as one slot
  on Google's MPW-7 containing 152 projects.

**DERIVED, and this is the number that matters:** the entire genuinely-open-and-genuinely-commercial
sector, worldwide, in 2026, is **plausibly one to three million dollars of annual revenue**. MOSIS —
a university service, on closed PDKs, thirty years ago — "generated up to $10 million annually at its
peak" (`SMB-5`). **The open commercial sector today is several times smaller than a single university
brokerage was at its peak in the 1990s.**

**Therefore the honest statement is:** the quadrant is populated but has never been tested at scale.
H8 says openness is *necessary* to attract many small customers. Nothing here refutes that. But
nothing here demonstrates the other half either — that an open programme can attract *enough* paying
customers to sustain a fab — because **no genuinely open, genuinely commercial programme has ever got
above about $1M a year, and the one that grew fastest died.**

There is a second empty cell worth naming: **open AND commercial AND independent of a subsidised
PDK.** It has **no members at all**. Every one of the four occupants runs on SKY130, GF180MCU or
SG13G2 — three design kits that exist because Google paid SkyWater and GlobalFoundries, and because a
German federal project paid IHP (`ACC-6`, `OPG-10`, `ACC-8`). **The commercial open sector is a
downstream of a subsidy.** That is not an argument against it; it is an argument that the causal
story runs through the PDK, and that no private actor has yet paid to open one.

### 6.2 Being adversarial: four ways our thesis could be wrong

The task asked for these to be tested, not listed. Each is tested against the matrix.

**(a) "The growing programmes are the subsidised ones and openness is incidental — we have the
causation backwards."**

**Partly true, and this is the strongest challenge in the audit.** Every programme in the record that
ever reached a large absolute number was subsidised: Europractice (753–985 designs a year, EU-funded),
MOSIS (~3,000 orders a year at peak, and its free arm NSF-funded), CMC (13,495 designs in 42 years,
publicly funded), Google Open MPW (821 submissions, Google-funded). The unsubsidised ones are the
small ones.

And the **AFRL design challenge is a direct counter-example on the growth question**: a closed-PDK,
proprietary-design, competition-gated, government-funded programme drew **82 designs in 45 days** —
**DERIVED** 1.82 a day against Google's 1.50 a day on MPW-1 (`ACC-8`). Whatever drew those people, it
was not an open PDK, because there was not one. It was that somebody else paid for IP, EDA and
foundry.

**What survives the challenge.** Subsidy explains the *level* but not the *slope*. Europractice ran
between 363 and 614 designs a year for eighteen consecutive years while subsidised throughout
(`DEM-16`); CMP peaked and died while subsidised; CMC is falling while subsidised. Subsidy without
open access produces a plateau. The open programmes grew — Google 37 → 147 a shuttle, chipIgnite 1.7×
a year for two years, Tiny Tapeout 317 → 970 → 1,632 submissions a year (`OPG-1`, `OPG-7`, `DEM-2`).
**The defensible claim is the weaker one: subsidy sets the level, openness is associated with the
slope, and no evidence here isolates either as a cause.**

**(b) "No genuinely open *and* genuinely commercial programme has ever existed at scale, so our
thesis is untested rather than supported."**

**This one is true, and §6.1 says so.** Four occupants, combined revenue plausibly under $3M a year,
one dead, one ours. The repository should stop treating chipIgnite's growth as evidence that the model
works commercially: the company that ran it never covered its costs, was underwritten by at least
eight named organisations (`ACC-8`, `OPG-15`), and failed to raise. **H8's status should read "argued,
with a populated but untested quadrant", not "supported".**

**(c) "The university programmes serve small customers perfectly well and we are inventing a
problem."**

**Half true.** Europractice fabricates more designs a year (753–985) than the whole Google Open MPW
programme managed in its life (821) and offers twenty-plus processes to 12 nm. If you are a European
academic, you are well served and have been since 1989.

**But the rules define the population, and the audit quantifies it.** To use the discounted service
in 2026 you must be an academic institution or publicly funded lab, in one of ~44 countries, a
fee-paying member, **and** — new this year — doing the design "for educational purposes or for
publicly funded research" (`ACC-4`). `DEM-16`: in 2024, **69% of submissions came from European
universities and research institutes and 9% from European industry**. That is not a market being
served badly; it is a different market. The person foundry.api is designed for — an individual, a
two-person company, someone outside the EMEA list — is not in it, pays standard prices, signs NDAs per
foundry, and buys bare die with no packaging.

**(d) "'Growth' is an artefact of counting submissions (free, low commitment) rather than paid
orders."**

**Largely true for the free programmes, and the audit should not soften it.** `OPG-5`: a single course
packed 8–16 projects into one slot, and Tiny Tapeout packed 152 into one. The deep dive's §1.3 puts
the entire Efabless story at **580–1,230 distinct people**. ChipFoundry publishes both sides of the gap
and it is large: `interest` of 76, 53 and 73 against `committed` of 21, 23 and 29 (`OPG-9`).

**What survives.** chipIgnite's series is **paid** orders at $9,750–$14,950 and it grew 1.7× a year
twice running (`OPG-7`). ChipFoundry's `committed` is paid and rose 21 → 23 → 29 across three shuttles
(`OPG-9`). wafer.space's backers are paid and went 6 → 18 (`OPG-12`). These are small numbers but they
are not submission counts. **The growth is real and the scale is tiny; both must be said in the same
sentence.**

### 6.3 What the audit actually establishes about openness

Taking the two axes separately, as the whole point of this document. **A fifth point was added after
the rest of this section was written, because the evidence arrived late and cuts against us: see
item 5.**

1. **Eligibility openness (A5) predicts *who shows up*, and the evidence is strong.** Europractice's
   rules define its population as institutions of a given type in a given list of countries, and its
   composition matches exactly (69% universities, 9% industry). Google's rules were facts about a
   repository, and its composition matched that instead ("Approximately 60% of the designs were
   submitted by software, FPGA and hardware developers (non-IC experts)", `DEM-4`). **This is the best
   supported finding in the audit.**
2. **PDK redistributability (A4) predicts *what third parties can build*, and the evidence is good.**
   Tiny Tapeout, the Zero to ASIC course, Wokwi's ASIC mode, ChipFoundry, wafer.space, Cadence's
   aggregation service and IHP's open route all exist downstream of four Apache-2.0 repositories
   (`ACC-6`). None of them could exist on a PDK you sign for. This is the only mechanism in the record
   that predicts a *rate* rather than a *level*.
3. **Published prices (A1) predict almost nothing on their own.** The TSMC University FinFET Program
   publishes prices to the euro and is closed on six other criteria (`ACC-5`); Tiny Tapeout, the most
   open programme in the audit, does *not* publish a headline price (`ACC-2`). H8's phrasing —
   "published prices, visible queues and public results" — bundles three things of which the first is
   the weakest. **MEMSCAP's MUMPs settles this one.** It published prices *and* a run schedule *and*
   redistributable design rules, commercially, for thirty-one years, with no eligibility rule — and it
   reached "Over 80 full process runs … to hundreds of organizations" at three to four runs a year
   (`ACC-10`). Transparency without an open PDK and an open tool flow bought longevity, not scale.
4. **Commercial profit-motive predicts nothing good, and possibly something bad.** The only programme
   in the record that died was the commercial one. The only entity described as self-sustaining is a
   university. The four commercial occupants of the open quadrant are collectively smaller than MOSIS
   was in 1995. Daniel Nenni's verdict remains the sharpest public statement against us and remains
   unrefuted: "the revenue model just did not work. People who use open source tools do it mainly due
   to cost and that is a tough customer base to profit from" (`OPG-16`, his stated opinion).
5. **Openness is not a ratchet, and we were wrong to assume it was.** Two of the corrections in this
   audit run the same way. **MOSIS went backwards**: 1.0 published a price formula to the dollar for
   decades; 2.0 publishes no price at all and asks you to sign up (§3.17). **MEMSCAP's MUMPs went to
   zero**: thirty-one years of published prices and a published schedule, and then the page 404s and
   the domain becomes a spam blog (`ACC-11`). **Europractice's country list contracted**: Belarus and
   Russia were eligible in 2019 and are not in 2026 (`ACC-12`). Against that, the only programme that
   became *more* open in the period is IHP, which moved from a free, non-commercial-only, German-funded
   run to a paid one open to anyone who signs a participation agreement (§3.6). **Three closings to one
   opening.** Anyone arguing that the industry is trending open has to explain that ratio, and this
   audit cannot.

### 6.4 The experiment that will settle it, running now

**IHP.** The same institute, the same process, the same open PDK, moving from a free German-funded
programme restricted to "non-commercial activities" (`OPG-10`) to a paid programme at €2,800/mm² open
to anyone who signs a participation agreement (`OPG-11`). It publishes every registered customer and
their area, live. One of its two current runs has **44.5 of the 90 mm² it needs** and says so on its
own page in bold.

That is a genuinely open, genuinely priced programme whose demand is visible to outsiders in real
time — which is exactly what this repository has never had. **The CMOS5L registration bar is the
single number most worth watching**, and it is in the one place where the operator gains nothing by
publishing it.

---

## 7. Blocked sources

Everything below was attempted read-only. Being blocked is recorded, not worked around.

| What | Blocker | What would unblock a human |
|---|---|---|
| **Web search, from part-way through** | The session's web-search budget was exhausted (200/200 calls). Later evidence had to come from `curl` against URLs already known | A raised search budget; nothing about the sources themselves is blocked |
| **Silex, Teledyne DALSA, Tronics, IMT** | Not audited. The delegated agent gathering the MEMS programmes was terminated by a session-wide API rate limit before reporting; MEMSCAP's MUMPs was then audited directly (§3.16, `ACC-10`, `ACC-11`) but the others were not | A pass over `silexmicrosystems.com`, Teledyne DALSA's MEMS pages, `tronicsgroup.com` and `imtmems.com`, plus the CMC and Europractice MEMS catalogues |
| **Whether MUMPs is still buyable through a reseller** | Not checked. MUMPs was resold through CMC Microsystems and Europractice; whether either still lists it would settle whether the programme survives its own website's disappearance | The Europractice technology index (it lists a MEMS section: CEA-Leti, Science, SINTEF, Tyndall, X-FAB) and CMC's catalogue — the latter behind an HTTP 403 for automated fetches |
| **X-FAB, imec, Fraunhofer, VTT, EuroCDP, CIME-P** | Same cause — not audited | As above. Europractice's per-foundry access pages are the fastest route; its 2026 price list already shows Fraunhofer IISB requires "a valid NDA" (`ACC-4`) |
| **MOSIS's domestic/foreign eligibility text** | Its price lists are titled "domestic", implying an export or nationality distinction; the eligibility page behind it was not recovered. `mosis.com` became a JavaScript application in late 2020 and the archived HTML has no readable body | Working back through pre-2000 Wayback captures of `mosis.com/Orders/`, which are plain HTML and did serve to `curl` for `SMB-8` |
| **MUSE Semiconductor prices and schedule** | `musesemi.com/shared-block-tapeout-pricing` returns HTTP 200 but is a Wix application with no price in the ~494 KB body; the recent Wayback captures are the same shell | Opening the page in an ordinary browser, or working back through the 2019–2021 captures which may predate the rewrite |
| **CMC Microsystems prices** | `cmc.ca/en/WhatWeOffer/Make/FabPricing.aspx` returns **HTTP 403** to an automated fetch | A browser. CMC's annual-report PDFs on the same domain fetch fine |
| **ChipFoundry's terms of service** | `chipfoundry.io/terms` returns **HTTP 404**, although the site footer links to "Terms", "Privacy" and "Commercial" | Following the footer link from a rendered page; the link target was not resolvable from the fetched HTML |
| **Efabless's terms of service and technology licence agreement** | The Wayback CDX API returns a single capture of `efabless.com/info_terms_of_services`, status **302**, i.e. a redirect and no content. The Internet Archive was also **"Temporarily Offline"** for part of this session | Retrying the CDX search for `efabless.com/page/terms/`, `efabless.com/privacy/` and the `marketplace/?q=content/technology-license-agreement` forms, all of which appear in the URL index |
| **The primary AFRL / AFWERX design-challenge source** | Not found before the search budget ran out. Everything in `ACC-8` is at one remove, through Efabless's newsletter | A search of AFRL, AFWERX or Centauri/KBR press releases from 2018–2020, or a SAM.gov / DoD contract record |
| **Tiny Tapeout's all-in headline price** | `app.tinytapeout.com/calculator` is a client-side application returning no price text to a fetch | A browser, in seconds. Already recorded in `search-log.md` |
| **wafer.space's own terms and export-control position** | No terms page found; `wafer.space/faq/` (trailing slash) is **404** while `/faq` is 200. Crowd Supply's terms were not read | Crowd Supply's site-wide terms of service, and a browser pass over `wafer.space` |
| **SEC EDGAR, for Efabless's funding rounds** | Returns **HTTP 403** — "Your Request Originates from an Undeclared Automated Tool" — and requires a declared identifying User-Agent, which we will not send | EDGAR full-text search in a browser, looking for Efabless Corporation Form D filings. This is the most likely public record of who funded chipIgnite and how much |

**Nothing in this audit was obtained by registering, logging in, requesting a quote, submitting a
form, or contacting any person.** Several pages name an address as the route to an NDA, a PDK or an
export-control questionnaire. Those sentences are quoted as findings. None of the addresses was used.
