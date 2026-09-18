# Efabless and the open shuttles: a deep dive

`OPEN-7` records that Efabless shut down in March 2025 and reads it as a challenge to H4 and H6:
cheap design did not make an intermediary viable. It also says, in its caveats, "This deserves a
proper deep dive". This is that deep dive.

It reads the evidence in [`open-programme-growth.md`](open-programme-growth.md) (`OPG-1`…`OPG-19`)
together with [`shuttle-programmes.md`](shuttle-programmes.md) (`DEM-1`…`DEM-22`) and
[`pricing-and-cost-to-serve.md`](pricing-and-cost-to-serve.md) (`SMB-6`…`SMB-13`), and answers four
questions:

1. **What actually happened to the numbers?** (§1)
2. **Why did a subsidised open programme grow when the older, better-resourced subsidised programmes
   did not?** (§2 — the long one)
3. **Where does the record stop, and why?** (§3)
4. **What do we still not know, and what would settle it?** (§4)

Two claims from the repository owner are examined and labelled throughout: that Efabless died of a
blocked funding round rather than weak demand, and that it did not subsidise Tiny Tapeout's prices.
§4 gives their status. A list of corrections other people need to make in files this document does
not own is at the end.

---

## 1. What the numbers actually say

### 1.1 The headline series

All from `OPG-1` and `OPG-2`, all reproduced from the source data and cross-checked against
Efabless's own archived platform pages.

| Programme | Shuttles | Slots | Submissions | Ratio | New users |
|---|---|---|---|---|---|
| Google Open MPW, SKY130 (MPW-1…8) | 8 | 320 | **617** | 1.93× | 181 (29.3%) |
| Google Open MPW, GF180MCU (MPW-0, MPW-1) | 2 | 80 | **204** | 2.55× | 71 (34.8%) |
| **Google total** | **10** | **400** | **821** | **2.05×** | 252 (30.7%) |
| chipIgnite, paid, SKY130 | 13 | 326 | **763** | 2.34× | 272 (35.6%) |
| **Everything Efabless ran** | **23** | **726** | **1,584** | **2.18×** | 524 (33.1%) |

Per shuttle, the Google SkyWater series went **37, 57, 53, 52, 75, 90, 106, 147**. The paid
chipIgnite series, by calendar year, went **28 → 133 → 225 → 377** — about 1.7× a year, twice
running, at a fixed $9,750–$14,950 with no external funding behind it (`OPG-7`, `OPG-8`).

### 1.2 The correction the repository needs

`DEM-9` records Google's own statement that it had "sponsored six shuttles on the Efabless platform,
manufacturing 240 designs from over 364 community submissions", and reads the 364 as the programme's
total response. **It is not.** It is the running total through MPW-6, in a blog post dated
2022-07-28, published while MPW-7 was still open for submissions. The cumulative series is
**37, 94, 147, 199, 274, 364, 470, 617** — and then two GF180MCU shuttles added 204 more.

**DERIVED:** 253 of the 617 SkyWater submissions, **41%**, arrived after the number Google published.
Counting both processes, 457 of 821, **56%**, arrived after it.

`DEM-9`'s reading — "the total global response over six shuttles and roughly sixteen months …
was 364 submissions … Four hundred submissions is a real community; it is not a market" — is
therefore built on a number that was already out of date when it was published. The correct
statement is that the free programme drew 821 submissions over about three years and was still
accelerating when it stopped (147 on its last SkyWater shuttle against 37 on its first). Whether
821 is "a market" is a different argument, and a fairer one to have.

### 1.3 The number that cuts the other way: how many people

This is the most important derived figure in this document and it works against H5.

The spreadsheet has a `Participants` column (distinct people per shuttle) and a `New Users` column.
Summed over all 23 shuttles: **1,232 participants** and **524 new users**. Participants cannot be
added across shuttles — the same person recurs — so 1,232 is an **upper bound** on distinct people.
`New Users` was evidently not tracked for the first two shuttles (both record 0, on a platform that
had only just launched), so a **lower bound** is 524 plus the population already present at MPW-2,
which had 54 participants: **578**.

**DERIVED: the whole Efabless story — 1,584 submissions, ten free shuttles and thirteen paid ones,
three years, two foundries, worldwide promotion by Google — came from somewhere between about 580
and 1,230 distinct people.** At the low end that is 2.7 submissions each (1,584 ÷ 578); at the high
end 1.3 (1,584 ÷ 1,232).

Two thirds of submissions came from returning users (`OPG-1`). And the ratio of designs to people
rose over time: **DERIVED**, MPW-1 was 37 projects from 32 participants = 1.16 each; MPW-8 was 144
projects from 94 participants = 1.53 each; CI 2411 was 119 from 75 = 1.59 each. **Part of the
growth in the submission count is the same people submitting more, not more people arriving.**

Set against `DEM-16` — Europractice at 753 to 985 designs *a year*, every year, for decades — the
open programme was never large. It was fast-growing and small.

### 1.4 The evidence that contradicts the growth story

Gathered here deliberately, because it is easy to leave out.

- **The first three chipIgnite shuttles did not fill.** CI 2106Q finished at 23 projects, CI 2110C
  at 28 and CI 2204C at 13, and Efabless's own platform labelled all three `Undersubscribed` —
  CI 2204C at **32.0%** of a nominal 40-slot shuttle (`OPG-2`, `OPG-3`). The very first Google
  shuttle, MPW-1, also came in under its slots, at 92%. For its first eighteen months the paid
  programme was failing by its own dashboard's standard.
- **The successor's completed shuttles have all come in under capacity.** ChipFoundry publishes
  `interest` and `committed` side by side. Interest runs at two to three times the slot count on
  every shuttle — and not one completed run has filled: 21 committed of 28 planned, 23 of 37, 29 of
  43 (`OPG-9`). **Every "oversubscribed" figure anywhere in this repository is a count of
  submissions or expressions of interest. Here is the one operator that publishes both sides of that
  gap, and the gap is large.**
- **A live open MPW run is short of its minimum.** IHP's SG13CMOS5L run closing 2026-11-09 has 44.5
  of the 90 mm² it needs, and IHP says so on its own page: "Minimal required area not reached yet"
  (`OPG-11`).
- **Demand at the bottom of the market is concentrated.** On IHP's SG13G2 run, two customers —
  IEEE CASS and Tiny Tapeout — hold 42 of 59.2 mm², **71%** (`OPG-11`). The long tail's showcase
  programme is itself dependent on two intermediaries.
- **A "submission" is not a design and is not a person, in both directions.** Google's own slides
  say a single course packed 8 to 16 projects into one slot on MPW-1 through MPW-6, and that Tiny
  Tapeout packed **152 projects into one slot** on MPW-7 (`OPG-5`). Nobody publishes a
  reconciliation between submissions, designs and people for any of these programmes.
- **Two suppliers now write undersubscription risk into their terms.** Tiny Tapeout's foundry partner
  "reserve[s] the right to delay a shuttle if it's less than 50% full" (`DEM-10`), and ChipFoundry
  offers a refund or roll-over "If a shuttle does not meet the minimum customer commitment threshold
  required for launch" (`OPG-9`). Efabless did the same from the start: the archived CI 2110C page
  says "Schedule depends on meeting minimum project capacity" and "$200 reservation fee (fully
  refundable if minimum projects not met)".
- **Open-silicon hardware products crowdfund badly.** Open-V raised 11% of its goal with 318 backers;
  Retro-uC raised 18% with 40; and Maverick-603, the one consumer product on Crowd Supply built on
  chipIgnite, reached 107% of goal with 62 backers and was then **suspended** (`OPG-13`).
- **Slot buyers are very few.** wafer.space, an unsubsidised open-PDK route at $2,000–$8,500,
  had 6 backers on its first run, 18 on its second and 5 so far on its third (`OPG-12`).
- **A named industry figure says the model does not pay.** Daniel Nenni, on the record: "the revenue
  model just did not work. People who use open source tools do it mainly due to cost and that is a
  tough customer base to profit from" (`OPG-16`).

None of this is fatal to H5. All of it is the shape of the thing H5 has to survive.

---

## 2. Question C: why did the subsidised open programme grow when the older subsidised programmes did not?

### 2.1 The fact to be explained

Between late 2020 and late 2022 the Google Open MPW programme went from **37 submissions a shuttle to
147** — a 4× rise in two years. Over the same period:

- **Europractice** (`DEM-16`): 896 designs in 2020, 985 in 2021, **731 in 2022**. Before that, it had
  run between 363 and 614 designs a year for the whole of 2000–2017 — eighteen essentially flat years.
  Since then: 813 (2023), 837 (2024), **753 (2025)**.
- **CMP**, France's national service (`DEM-19`): peaked at 401 circuits in 2007, was back to 273 by
  2011, and **no longer exists as an operating service**.
- **CMC Microsystems**, Canada's national service (`DEM-20`): fell in each of the three years read.
- **MOSIS** (`DEM-22`): its free academic tape-out programme **ended in 2020**, and its public design
  counter did not move for a decade.

And all four are subsidised. Europractice says so in its own words (`SMB-6`). The comparison document
marks Europractice, MOSIS and CMC as requiring external funding (`OPG-8`). All four have far larger
process portfolios (>20 technologies each against Google's two), far more staff (>70 at Europractice,
>100 at CMC against <10 at Efabless), and decades more history.

So: more money, more processes, more people, more time — and flat or falling, while the two-process,
sub-ten-person newcomer quadrupled.

### 2.2 The single most informative comparison in the evidence

Before the candidate explanations, one pair of numbers does more work than any of them.

`DEM-17` records a Europractice **First User Stimulation Programme**: "a total of 98 applications were
submitted to 6 First User Stimulation Programmes by 73 universities from 23 countries … and 50
designs were selected for fabrication." That is Europractice offering *free* first-time fabrication,
promoted, to its own eligible population.

**Ninety-eight applications.**

Google's programme, also free, also promoted, drew **617 submissions across eight SkyWater shuttles**
and 821 in total.

**Both programmes were free. The response differed by roughly eight-fold.** Whatever explains the
difference, it is **not price**, because the price was the same — zero — on both sides. This is the
strongest single piece of evidence in the file, and it points squarely at *who was allowed to apply
and what they had to do first*, not at what it cost.

(Caveat, honestly: the Europractice programme ran over a shorter window and was one line item in a
2017 annual report, while Google's ran three years with a global marketing campaign behind it. The
comparison is not controlled. But an eight-fold gap at the same price is not explained by scheduling.)

### 2.3 The candidate explanations, with the evidence for and against each

#### (a) Eligibility and access rules — **the strongest explanation, and it is established**

**For.** Europractice's own pages, read directly (`OPG-17`), say that to use its services at member
prices a person must:

- belong to an "academic institution or publicly funded research laborator[y] primarily engaged in
  university-like activities";
- be in one of about 44 listed countries (the 27 EU states plus 17 named others);
- "become a Member of EUROPRACTICE and **pay the annual membership fee before they can make use of
  EUROPRACTICE services**" — €1,100 for Full-IC or €600 for MPW-only;
- and go through "the necessary NDAs (Non-Disclosure Agreements), DKLAs (Design Kit License
  Agreements)" for each foundry.

CMC is Canadian. MOSIS was US. The comparison document marks Europractice and CMC "Commercial
Allowed: Restricted" (`OPG-8`).

Efabless's own MPW-7 page, read in the archive, says the opposite in one sentence: "**The shuttle
program is open to anyone**, provided that their project is fully open source and meets the other
program requirements."

And the composition data match. `DEM-16`: in 2024, **69% of Europractice submissions came from
European universities and research institutes and 9% from European industry**. `DEM-4`: on Google's
first shuttle, "Approximately 60% of the designs were submitted by software, FPGA and hardware
developers (non-IC experts)". These are not the same population at all.

**Against.** Europractice's *absolute* numbers are several times Google's: 753–985 designs a year
against 821 over the whole life of the open programme. Restricted access did not stop Europractice
being much the larger service. And non-members *can* buy Europractice MPW fabrication at standard
prices, so it is a gate and a paperwork step, not a wall.

**Verdict.** Established as a fact; strong as an explanation of the *composition* and of the *ceiling*.
A service whose membership is gated on institution type grows with the number of qualifying
institutions, and that number barely changes — which is precisely the shape of `DEM-16`'s
eighteen-year plateau. It is weaker as an explanation of the growth *rate*, because it explains why
Europractice could not grow rather than why Google's could.

#### (b) NDA requirements — **plausible mechanism, no measurement**

**For.** The comparison document's NDA row reads No, No, Yes, Yes, Yes, Yes for Google, chipIgnite,
Europractice, MUSE, MOSIS, CMC (`OPG-8`). Three independent confirmations:

- Google's own conference slides: "Open source, manufacturable 130nm PDK. **No NDA required, just
  clone.**" (`OPG-5`)
- Muse Semiconductor's own FAQ: "We require only two agreements: A Mutual Non-Disclosure Agreement
  (MNDA)…A **TSMC 3-way NDA** between Muse, TSMC, and the customer." (`OPG-18`)
- Europractice's own access page: "the necessary NDAs … DKLAs" (`OPG-17`)

And Matt Venn, looking back after Efabless died: "They weren't just an MPW provider - they offered
hundreds of packaged parts with **no NDAs**, great pricing, and a level of openness that was rare in
silicon. Losing them left hundreds of designs, including 500 Tiny Tapeout projects from TT08 and
TT09, seemingly stuck in fabrication limbo." (Matt Venn, "Review of 2025 and goals for 2026", Zero to
ASIC Course, dated on the page 2026-01-04: <https://www.zerotoasiccourse.com/post/year_update_2025/>
— **Verified 2026-09-18**, fetched with `curl` and the sentence matched character for character. The
same post gives Tiny Tapeout's 2025 output: "Tiny Tapeout sent over a thousand designs across 12
chips to 3 different fabs, including our first test chips for the GF180mcu process. Many of those
designs came from high schoolers and students - attendees of my exciting and engaging Tiny Tapeout
workshops.")

Note what that last sentence costs the growth thesis as well as what it gives it: the person who runs
the largest open-shuttle programme in the world attributes many of its designs to high schoolers and
students at his own workshops. That is a real population and it is not a market.

**Against.** **Nobody has measured how many people an NDA deters.** Not one source in this repository
counts a person who wanted to make a chip and did not because of an NDA. It is an inference from a
correlation with six data points.

Worse, the mechanism is weak for Europractice's actual population. A university signs a design-kit
licence once, institutionally; for the professor who then submits, the NDA is close to costless. So
the NDA cannot explain why *Europractice's own users* did not grow. It can only explain why the
people an NDA does deter — individuals, hobbyists, one-person startups, anyone without an institution
to sign for them — never appeared in Europractice's numbers. **That makes explanation (b) a special
case of explanation (a) rather than an independent cause.**

**Verdict.** Real, documented, and probably part of the answer — but entangled with eligibility, and
unmeasured. Do not state it as the cause.

#### (c) Open PDK versus PDK-under-NDA — **the deepest version, and it has the best supporting chain**

This is (b) taken seriously. An NDA is a signature; an open PDK is a different kind of object. Things
that exist *only* because the PDK could be copied, published and forked:

- **A public, reproducible design flow.** OpenLane, Apache 2.0 (`OPEN-1`), and the Caravel harness.
  The MPW-7 page's requirements are all self-checkable: "The project must be posted on a
  git-compatible repo and be publicly accessible", "must include a LICENSE file", "must contain a
  GDSII layout, which must be reproducible from source", "Projects must successfully pass the Open
  MPW precheck tool".
- **Teaching material built on it by third parties.** The Zero to ASIC course, which occupied a slot
  on every shuttle from MPW-1 to MPW-6 (`OPG-5`).
- **Tiny Tapeout**, which turned one slot into 152 designs (`OPG-5`) and has since run 4,268 designs
  across three foundries (`DEM-1`, `DEM-2`).
- **A graphical entry path** (Wokwi) used by 94 of the 249 projects on TT03 (`DEM-3`).
- **A chip designed by talking to a language model**, taped out through Tiny Tapeout (`OPEN-6`).

None of these could have been built on a PDK you have to sign for, because none of them could have
been published. This is the mechanism by which an open PDK produces *more designers*, not merely
easier access for the designers who already exist — and it is the only candidate explanation that
predicts a growth *rate* rather than a level.

**Against, and this is important.** The open PDKs are not production PDKs. GF180MCU's own repository
says "Experimental Preview" and "not intended to be used for production settings at this current
time" (`OPEN-2`); IHP's says the same (`OPEN-3`). So what the open PDK grew was a teaching,
experimenting and prototyping market on mature nodes. That is entirely consistent with the small
absolute numbers (§1.3), with two-thirds returning users, and with `DEM-16`'s observation that
Europractice's users are overwhelmingly academic anyway. **An open PDK may have widened the pool of
people who can make an experiment without widening the pool of people who can make a product** — and
H5 is about the latter.

**Verdict.** The best-supported causal chain, with a real and unresolved limit.

#### (d) Self-service sign-up versus a sales or application process — **partly established, partly false**

**For.** Efabless's requirements were machine-checkable and its precheck tool was public. Its
successors sell through a web checkout (ChipFoundry) or a crowdfunding page (wafer.space, `OPG-12`).
Europractice, by contrast, tells users on its own price list: "please make your design registration
as early as possible. **We will work with you and do our best to get your design on the run.** If
required, a waiting list will be created" (`DEM-18`) — a human broker in the loop, by design. Its
access page routes users to per-foundry contacts for NDAs and licences (`OPG-17`).

**Against, and this is a real problem for the explanation.** Google's programme was **not**
self-service. `DEM-8` records that each GlobalFoundries shuttle would "select 40 projects based on
the following criteria", including that "projects submitted earlier get additional chances to be
selected". There was a hard cap of 40 and an application process behind it. **DERIVED** acceptance
rates from `DEM-6`: 40/45 = 89%, 40/56 = 71%, 40/75 = 53% — and at MPW-8's 144 projects, 40/144 =
28%. By its last shuttle the free programme was rejecting roughly three applicants in four. That is
a *more* competitive application process than Europractice's stimulation programme, which selected
50 of 98 (`DEM-17`).

**Verdict.** True of the paid programmes (chipIgnite, ChipFoundry, wafer.space, Tiny Tapeout) and
false of the free one. It cannot be the explanation for the free programme's growth. It may well be
part of the explanation for chipIgnite's.

#### (e) Price, and what is included — **necessary, nowhere near sufficient**

**For.** `OPG-8`: free / $10k / ~$15k / ~$24k for 10 mm² of 130 nm, and packaging and development
boards **included** for Google and chipIgnite, **not included** for Europractice, MOSIS and CMC.
That difference is larger than it looks: a Europractice user receives bare die and must then arrange
packaging, a board and bring-up themselves — a cost, a delay and a skill requirement that a small
team may not have. Efabless shipped "5 evaluation board assemblies" and 100 packaged parts in the
price (archived CI 2110C page, `OPG-7`).

**Against.** §2.2 is the answer: **at a price of zero on both sides, the response differed eight-fold.**
Price cannot explain a gap that persists when the price is the same. And `DEM-17`'s caveat is exactly
right — "Oversubscription at a price near zero says nothing about demand at a price that covers
costs."

**Verdict.** Packaging-and-boards is a genuine and under-rated difference in what the customer
receives. Headline price is not the explanation.

#### (f) Community, documentation and tooling — **strong correlation, weak causation, and a caution**

**For.** The Efabless community grew from "almost 1100 members" at MPW-1 (`DEM-4`) to "more than
3,000" by mid-2022 (`DEM-5`) to "13K plus" at the end (`OPG-15`). There was a public Slack
(`open-source-silicon.dev`, on Google's slides), a developer portal, a course, a precheck tool and a
published design flow. We found nothing comparable for Europractice, MOSIS or CMC — no public forum,
no open tool chain, no third-party course built on their PDKs, because their PDKs cannot be
published.

**Against.** The community grew about 12× while submissions grew about 4× a shuttle. **The
overwhelming majority of those 13,000 people never submitted anything.** If community were the
mechanism, the conversion rate is startlingly low, and the 13,000 figure should not be cited as
evidence of demand.

**Verdict.** Community is what an open PDK makes possible (explanation (c)), and is better read as
its consequence than as an independent cause. The 13,000 : ~600–1,200 ratio is itself a finding, and
it is a caution, not a support.

#### (g) Promotion and visibility — **real, and the least interesting**

**For.** Google promoted the programme through its Open Source Blog (`DEM-5`, `DEM-8`, `DEM-9`), a
developer portal, SkyWater press releases (`DEM-4`) and conference talks on several continents
(`OPG-5`). `DEM-4` records the effect directly: the first submission window generated "1700
downloads in the first two weeks and fill[ed] all 40 available slots."

**Against.** Europractice publishes an annual report, a full public price list and a schedule. It is
not invisible; it markets to institutions rather than to individuals, which is (a) again.

**Verdict.** Certainly contributed to the *timing* and probably to the early slope. Does not explain
why the growth continued for three years, or why it continued in the paid programme after Google's
promotion had moved on.

#### (h) An explanation not on the list: the unit of account changed

Europractice counts a *design*. Efabless counted a *submission*, and a submission could contain 8, 16
or 152 designs (`OPG-5`). Some of the apparent growth is therefore an accounting difference between
the two series rather than a difference in demand.

**But not all of it**, and the platform data let us say so. Efabless's `Participants` figure — distinct
people per shuttle — rose from **32 on MPW-1 to 94 on MPW-8** (`OPG-2`), a 2.9× rise against the
submission count's 4.0×. **DERIVED:** the designs-per-participant ratio rose from 1.16 to 1.53. So
roughly three-quarters of the growth is more people and roughly a quarter is each person doing more.

**Verdict.** A necessary correction to the headline, not a debunking of it. Anyone comparing
Efabless's 147 with Europractice's 731 is comparing two different units and should say so.

### 2.4 What we conclude, and how confident we are

**Established, from primary sources read directly:**

- Europractice restricts membership by institution type and country, charges an annual fee before
  use, and routes users through NDAs and design-kit licences (`OPG-17`, verbatim from its own pages).
- The Google/Efabless programmes required no NDA and were open to anyone with an open-source project
  (`OPG-5` from Google's slides; the archived MPW-7 page from Efabless's).
- Muse requires two or three NDAs including a three-way NDA with TSMC (`OPG-18`).
- The open programme's growth is real, it is larger than `DEM-9` implies, and Efabless's own platform
  labelled sixteen of eighteen checked runs "Oversubscribed" (`OPG-2`).
- At a price of zero, Europractice's own stimulation programme drew 98 applications and Google's drew
  821 submissions (`DEM-17`, `OPG-1`).

**Our best reading, stated as a reading and not as a finding.** The difference is *not* mainly price,
because the eight-fold gap survives at zero price on both sides. It is that the two programmes were
serving different populations, and the older programmes' rules define their population as
"institutions of a certain type in a certain list of countries". Membership fees, NDAs, design-kit
licences and a sales conversation are each individually small, and are collectively decisive for
exactly the people the open programme picked up — individuals, software and FPGA developers,
one-person startups and course cohorts, "60% … non-IC experts" on the very first shuttle (`DEM-4`).
The open PDK is what let third parties build the on-ramps those people used (`OPEN-6`, `DEM-1`,
`OPG-5`), and that is why the effect compounded over three years instead of producing one spike.

**Conjecture, clearly labelled as such.** That the open PDK *caused* the growth rather than merely
accompanying it. That the older programmes could have grown the same way had they opened up. That
the population the open programme reached will ever buy silicon at a price that covers costs — the
absolute numbers (§1.3) and `OPG-16`'s "tough customer base to profit from" both argue against it.

**What would change our mind.** A single subsidised programme that opened its eligibility without
opening its PDK, or opened its PDK without opening its eligibility, and published the result. We did
not find one. IHP is the closest thing: its 2026 shift from a free German-funded programme to a paid
open-silicon programme with a participation agreement (`OPG-10`, `OPG-11`) is a natural experiment
running in public right now, and its CMOS5L run's registration bar is the number to watch.

---

## 3. Where the record stops, and why

**Every series in this file that ends, ends for a supply reason.**

- **The Google Open MPW series** ends at MPW-8 (SKY130, closed 2022-11) and GF MPW-1 (GF180MCU,
  closed 2023-12) because **Google stopped sponsoring shuttles**, not because submissions fell. The
  last SkyWater shuttle was the largest the programme ever ran, at 147 submissions and 360% of
  capacity by Efabless's own reckoning (`OPG-2`), and the last GF180MCU shuttle was 116 at 290%.
  **Both series end on their all-time high.**
- **The chipIgnite series** ends at CI 2411 (closed 2024-11-11) because **Efabless shut down at the
  end of February 2025** (`OPEN-7`, `OPG-15`). CI 2411 was the largest chipIgnite ever ran, at 119
  submissions and 298% of capacity. A further shuttle, **CI 2504, was open and had already taken 20
  projects from 20 participants, 14 of them new customers**, with three months still to run, when the
  company failed (`OPG-3`).
- **Tiny Tapeout's TT10** appears in its own table as "Cancelled" (`DEM-1`) and holds 112 submissions
  in the API (`DEM-2`). It was cancelled because its fab partner had died, not for want of designs.
  `DEM-10`'s source puts the damage at "500 chip designs" across TT08, TT09 and TT10.
- **CMP** stopped for administrative reasons at its foundries, which `DEM-19` already records as "a
  supply-side failure, not a demand one".
- **MOSIS's** free academic programme ended in 2020 (`DEM-22`) — again a decision, not a shortfall.

**So: no open shuttle series in this repository ends because demand ran out.** Anyone reading these
tables later must not take the last row as evidence of decline. Where a series continues under a new
operator — ChipFoundry on SKY130, IHP on SG13G2, wafer.space on GF180MCU, all three carrying Tiny
Tapeout (`OPG-9`, `OPG-10`, `OPG-11`, `OPG-12`) — the continuation is the honest end of the series,
and those operators' numbers are smaller and more mixed than Efabless's were.

---

## 4. The two owner-supplied claims, and what the public record does and does not support

### 4.1 "Efabless did not die of weak demand"

**Owner-supplied claim.** Efabless died because an early investor refused to be diluted, blocking a
new funding round from closing. Blocking funding to a growing startup is a known way to kill one.

**Status: owner-supplied, uncorroborated, and consistent with everything public.**

What the public record says, in full:

- The company's own shutdown notice: "Due to funding challenges, Efabless has shut down operations
  until further notice." (`OPG-15`)
- CEO Mike Wishart's letter, the primary text, recovered in full: "**On the brink of a wonderful next
  chapter, we were not able to close our Series B round** and must now tend to the inevitable
  necessities." (`OPG-15`)
- Hackster: "sources suggest a grant on which the company had been banking did not materialize"
  (`OPEN-7`) — a *different* proposed cause, unattributed.
- SemiWiki's founder Daniel Nenni: "the revenue model just did not work" (`OPG-16`) — a third, and he
  labels it his opinion.

**No public source names an investor, a dispute, or dilution.** `OPG-15` lists everything that was
tried to find one, including SEC EDGAR, which returned HTTP 403 because it requires a declared
identifying User-Agent that we will not send.

**What the demand evidence does establish, independently of the cause of death:** the programme was
growing, not shrinking, at the end. chipIgnite grew 1.7× a year for two consecutive years; its last
completed shuttle was its largest ever; and its next shuttle was already taking new paying customers
(§3). **"Efabless did not die of falling demand" is supported by the data. "Efabless died because an
investor blocked the round" is not, and must not be written into `WHY.md` or `PRINCIPLES.md` as
established.**

The honest summary for a reader: *the company was growing and failed to raise. Why the raise failed
is not public.* That is a more useful sentence than `OPEN-7`'s current one, and it is fully
supportable.

### 4.2 "Efabless did NOT subsidise Tiny Tapeout's prices"

**Owner-supplied claim.** Efabless did not subsidise Tiny Tapeout's prices; it sponsored free Tiny
Tapeout places for participants at some specific workshops. `OPEN-5`'s caveat, "The prices were
subsidised by Efabless at the time", is wrong.

**Status: `OPEN-5` is wrong as written, but the owner's replacement is not quite right either. The
public record supports a third, narrower statement.**

Tiny Tapeout's own pages, read across the Internet Archive (`OPG-14`), say:

1. In 2023 the price was **$100** for a tile, an ASIC and a board, with **no sponsor named on the
   page at all**.
2. From about January 2024 the home page read: "**The standard price is $300 plus shipping.** However,
   **Efabless is sponsoring a special early bird offer of $150** (plus shipping), **limited to one
   order per person.**" The FAQ made the cap explicit: "**The first 80 orders from individuals are
   sponsored by Efabless** … After those first 80 are gone, the price goes up to $300."
3. After Efabless died the sponsorship sentence disappeared and the next shuttle's price was **€150**
   for a tile, an ASIC and a board — the same as the sponsored early-bird rate, and half the
   unsponsored $300.

So:

- **`OPEN-5`'s "the prices were subsidised" is too broad and should be corrected.** The standard price
  was never sponsored. Businesses, universities and every individual after the first 80–100 paid the
  unsubsidised $300.
- **The owner's "Efabless did not subsidise Tiny Tapeout's prices" is too strong.** Tiny Tapeout's own
  home page said, in those words, for more than a year, that Efabless was sponsoring a $150 offer
  against a $300 standard price. That is a price subsidy. It is a *capped* subsidy aimed at
  individuals, which is a materially different thing from subsidising the price — but it is not
  nothing.
- **The workshop claim is partly supported.** chipIgnite and ChipFoundry both appear on Tiny Tapeout's
  workshop sponsor list (`OPG-14`). **We found no page anywhere stating that Efabless paid for free
  workshop places**, only that it is listed as a sponsor. Efabless did also sponsor fabrication
  directly as contest prizes — "The top ten winners will be awarded free fabrication of their
  designs" (`OPG-6`) — which is a third distinct form of support.
- **And the most useful fact of all, for H5:** prices did **not** rise when the sponsor disappeared.
  A subsidy propping up an artificially low price would predict the opposite.

**The accurate sentence, which `OPEN-5` should use:** *From TT06 (early 2024) until Efabless shut down,
Efabless sponsored a capped early-bird tier — the first 80–100 orders from individuals, one per
person, at $150 against a $300 standard price. The standard price was not sponsored, no sponsor was
named on Tiny Tapeout's pages before 2024, and prices did not rise when Efabless disappeared.*

---

## 5. What we could not verify, and what would unblock it

| What | Blocker | What would unblock a human |
|---|---|---|
| Whether CI 2209C ran, was cancelled or was rescheduled | **No Internet Archive capture exists** for `platform.efabless.com/shuttles/2209C` on any date (CDX returns nothing). Its page existed — it is in the platform navigation (`OPG-3`) — and the 2110C schedule gave it a tapeout of "September 19, 2022" | Someone who was on the Efabless platform, or a participant in the neighbouring shuttles |
| Submission counts for CI 2304C, CI 2306Q, CI 2311 | No archive captures at all; the spreadsheet is the only source | As above |
| Why Efabless's Series B did not close | SEC EDGAR returns **HTTP 403 — "Your Request Originates from an Undeclared Automated Tool"**; it requires a declared identifying User-Agent, which we will not send. Hackster returned **HTTP 403** to `WebFetch` | Opening EDGAR full-text search in an ordinary browser and looking for Efabless Corporation Form D filings. That is the most likely public record of the rounds |
| Muse Semiconductor's shuttle prices and schedule | `musesemi.com/shared-block-tapeout-pricing` is **entirely client-rendered (Wix)**; the ~494 KB response contains no prices, and the most recent Wayback capture (2026-05-21) is the same empty shell | Opening the page in a browser, or working back through the 2019–2021 captures, which may predate the JavaScript rewrite |
| Whether Efabless paid for free Tiny Tapeout workshop places | Its logo is on the workshop sponsor list; **no page states what the sponsorship bought** | A workshop announcement or report from 2023–2025 |
| How "submissions", "designs" and "people" reconcile in any of these programmes | **Nobody publishes a reconciliation.** Group submissions ran 8–16 projects per slot and Tiny Tapeout ran 152 (`OPG-5`) | The Efabless platform database, which is gone |
| Europractice's number of MPW runs per year | `DEM-16` already records this as not found in any activity report | — |
| ChipFoundry's definitions of `interest`, `reserved`, `committed` | Not documented anywhere we found; our reading of `committed` is an inference (`OPG-9`) | — |

**Routes that worked and are worth reusing.** The Internet Archive's raw-content form
(`https://web.archive.org/web/<timestamp>id_/<url>`) recovered eighteen dead Efabless platform pages
including their statistics blocks; the CDX API
(`https://web.archive.org/cdx/search/cdx?url=<pattern>*&output=text&fl=timestamp,original,statuscode`)
found them. A client-rendered page's data is often in an open API the page's own JavaScript bundle
names — that is how ChipFoundry's shuttle metrics were read (`OPG-9`). And a stacked bar chart's
values are frequently in `data-` attributes in the HTML, needing no JavaScript at all — that is how
IHP's per-customer registration figures were read (`OPG-11`).

---

## Changes needed in other files

This document and [`open-programme-growth.md`](open-programme-growth.md) are the only files this work
touched. Everything below needs to be applied by whoever owns the file.

### `resources/references/open-silicon-and-ai.md`

**1. `OPEN-5` — replace the wrong caveat.** The caveat currently reads:

> - The prices were subsidised by Efabless at the time.

Replace with:

> - **Pricing and sponsorship, corrected.** The standard price was not subsidised. From about
>   January 2024 until Efabless shut down, Efabless sponsored a **capped early-bird tier** — Tiny
>   Tapeout's own home page read "The standard price is $300 plus shipping. However, Efabless is
>   sponsoring a special early bird offer of $150 (plus shipping), limited to one order per person",
>   and its FAQ capped it at "The first 80 orders from individuals". Businesses, universities and
>   later individuals paid $300. Before 2024 no sponsor was named on Tiny Tapeout's pages at all, and
>   the price was $100 for a tile, an ASIC and a board. Prices did **not** rise when Efabless
>   disappeared: the next shuttle was €150. See `OPG-14` in
>   [`../demand/open-programme-growth.md`](../demand/open-programme-growth.md).

**2. `OPEN-7` — add the primary text and the fuller quote.** Add to the sources:

> - Mike Wishart, letter to the Efabless community, posted in full on SemiWiki 2025-03-05:
>   <https://semiwiki.com/forum/threads/efabless-just-shut-down.22217/>

and to "What it says":

> - The primary text of the CEO's statement is more specific than the trade-press paraphrase: "On the
>   brink of a wonderful next chapter, **we were not able to close our Series B round** and must now
>   tend to the inevitable necessities." The company's own notice read "Due to funding challenges,
>   Efabless has shut down operations until further notice."
> - Wishart also gives Efabless's final community size: "our 13K plus member community".

and to the caveats:

> - **Demand was rising, not falling, when the company died.** Its paid chipIgnite programme grew
>   about 1.7× a year for two consecutive years; its last completed shuttle, CI 2411, was the largest
>   it ever ran (119 submissions, 298% of capacity on Efabless's own page); and a further shuttle,
>   CI 2504, was open with 20 projects and 14 new customers when it shut down. See `OPG-7` and
>   `OPG-3`. **Do not read the end of the Efabless series as a fall in demand.**
> - The repository owner states, from direct knowledge, that the round was blocked by an early
>   investor who refused to be diluted. That is recorded as **owner-supplied and uncorroborated**;
>   see `OPG-15` for everything that was tried. Three mutually inconsistent public explanations exist
>   (a grant that did not arrive, a revenue model that did not work, an open-source model that
>   favours large firms) and none is evidenced.

**3. `OPEN-1` — close the "To find" note.** It asks "how many designs the Google Open MPW shuttles
received and manufactured". `DEM-4`…`DEM-9` partly answered it; `OPG-1` and `OPG-2` answer it in
full: **821 submissions across 10 shuttles against 400 slots**, per-shuttle figures cross-checked
against Efabless's own archived pages.

### `resources/demand/shuttle-programmes.md`

**4. `DEM-9` — correct the reading of 364.** The entry treats Google's "over 364 community
submissions" as the programme's total. It is the running total **through MPW-6**, published
2022-07-28 while MPW-7 was still open. The full series is 37, 57, 53, 52, 75, 90, 106, 147 = **617**
on SKY130, plus 88 and 116 on GF180MCU = **821 in total**. 41% of the SkyWater submissions and 56% of
all submissions arrived after the number Google published. The entry's conclusion — "Four hundred
submissions is a real community; it is not a market" — should be restated against 821 and against
the growth rate, or dropped. Cross-reference `OPG-1` and `OPG-2`.

**5. `DEM-6` — its "not found anywhere" note can be closed.** It says "MPW-3, MPW-4, MPW-6, MPW-7 and
MPW-8 submission counts were **not found anywhere**". They are on Efabless's own archived platform
pages: 53, 52, 86, 110, 144 respectively (`OPG-2`), with the retrieval method written out.

**6. `DEM-8` — its "not found" note can be closed.** It says the GF180MCU submission counts were not
found. GF MPW-0 finished at 86 and GF MPW-1 at 116 on Efabless's own pages (`OPG-2`).

**7. `DEM-2` — add the cross-programme caution.** Google's own slides state that a single course
packed 8–16 projects into one slot on MPW-1…MPW-6 and that Tiny Tapeout packed 152 projects into one
slot on MPW-7 (`OPG-5`). This is the sharpest available statement of why design counts, submission
counts and people are three different things.

### `resources/demand/README.md`

**8. Add the two new files to the directory's index**, with `OPG` as a new ID prefix:

| File | ID prefix | Covers |
|---|---|---|
| `open-programme-growth.md` | `OPG` | Open-PDK shuttle programmes: the full Efabless series, chipIgnite, ChipFoundry, IHP, wafer.space, and the crowdfunded open-silicon campaigns |
| `efabless-and-the-open-shuttles.md` | — | Deep dive: what the Efabless numbers say, why the open programme grew when the older subsidised ones did not, and why every series stops |

### `resources/hypotheses.md`

**9. Link the new evidence under H5 and H6.** Supporting: `OPG-1`, `OPG-2`, `OPG-3`, `OPG-6`,
`OPG-7`, `OPG-12` (weakly). Challenging: `OPG-9` (interest ≫ committed), `OPG-11` (concentration and
an undersubscribed run), `OPG-13` (failed campaigns), `OPG-16` (a named industry verdict), and §1.3
of this document (1,584 submissions from roughly 580–1,230 distinct people). `OPG-5` and `OPG-17`
bear on H4.

### `resources/demand/search-log.md`

**10. Record the blocked routes**, so nobody repeats them: SEC EDGAR returns HTTP 403 to automated
tools without a declared identifying User-Agent; `musesemi.com` pricing and schedule pages are
client-rendered and the Internet Archive captures them as empty shells; Hackster.io returned HTTP 403
to `WebFetch`; `platform.efabless.com/shuttles/2209C`, `/2304C`, `/2306Q` and `/CI 2311` have **no
Internet Archive captures at all**; `chipfoundry.io/blog`, `/news`, `/shuttles` and `/pricing` are
all 404 — ChipFoundry has no blog.

**11. Record the routes that worked**, from §5 above: the Wayback `id_` raw-content form and the CDX
API; reading a client-rendered page's data out of the API named in its own JavaScript bundle; and
reading chart values out of `data-` attributes in the HTML.

### `resources/README.md`

**12. No change requested**, but note that its "Layout" table does not mention `resources/demand/` at
all. Whoever owns that file may want to add a row.
