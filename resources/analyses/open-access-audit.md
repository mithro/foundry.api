# The open-access audit: which small-customer programmes were actually open, and which were actually businesses

**Status: first pass, committed incomplete on purpose.** Fifteen programmes are scored below. The
MEMS programmes, X-FAB, imec, Fraunhofer, VTT, EuroCDP and SkyWater's and GlobalFoundries' own direct
offerings are **not yet audited** and are marked as such in the matrix. A matrix with fifteen rows
filled in and the rest marked honestly is more useful than a complete one that does not exist.

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

**Axis 2: P(S) — a company trying to profit, materially underwritten by others.** `OPG-8`'s comparison
table marks chipIgnite as the **only** one of six programmes with "Requires External Funding: **No**",
and that has been read in this repository as "chipIgnite was a business rather than a subsidy". That
is right about the *product* and wrong about the *company*. By Efabless's own account (`ACC-8`) its
platform was built on a Google-sponsored shuttle, the "**DARPA-funded** no-human-in-the-loop OpenRoad
project", an in-kind partnership with Silicon Catalyst, a foundry that open-sourced its PDK, and EDA
and IP from Mentor, Arm and X-FAB. Its CEO's closing letter lists the same: "Without the support of
GlobalFoundries, SkyWater, Synopsys, Google, XFAB, AFRL, Arm and many others, we would not have come
this far" (`OPG-15`). And it died when a Series B did not close (`OPG-15`) — a venture-funded company
is by definition not yet covering its costs.

**This is the single most important correction the audit makes.** chipIgnite is the repository's only
example of demand at a price that might cover costs, and the price it charged was set by a company
whose tool chain, PDK and first three years of demand were paid for by others.

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
| A5 | **0, and it got tighter.** 2025: an academic institution in one of ~44 listed countries, and a paid-up member. 2026 adds a third condition: "**The intended design will be done for educational purposes or for publicly funded research.**" Non-members may buy, at standard prices. Membership must be paid "before they can make use of EUROPRACTICE services" — €1,100 Full-IC or €600 MPW-only. | `ACC-4`, `OPG-17` |
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
| A1 | **2.** Published per-run: "SG13G2 - 2800€ per ㎟" and "SG13CMOS5L - 1500€ per ㎟", with "Minimum area 90㎟" and "Lowest price 900€ per ㎟" printed on the page. | `OPG-11` |
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

