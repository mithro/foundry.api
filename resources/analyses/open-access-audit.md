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

