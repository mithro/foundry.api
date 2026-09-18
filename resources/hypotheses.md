# Hypotheses

These are the claims foundry.api depends on, stated so they can be tested. For each one, the evidence is listed below it, split into what supports it, what challenges it, and what is still an unverified **Lead**. Reference IDs point to entries in [`references/`](references/), except `DEM` and `SMB`, which point to [`demand/`](demand/) — the evidence gathered specifically on H5 and H6.

Status of each hypothesis:
- **Well supported:** several verified sources, and no strong challenge.
- **Contested:** verified evidence on both sides.
- **Argued:** a reasonable argument, but little direct evidence yet.
- **Untested:** nothing gathered yet.

---

## H1. The doom spiral

**Claim.** High up-front cost (NRE) means only big customers can afford to make chips. That makes foundries organise around a few huge customers and chase scale, which pushes the cost of each new generation up again.

**Status:** Well supported for leading-edge manufacturing. Argued for mature nodes, where the business model spreads but the costs are far lower.

- **Supports:**
  - COST-1: design cost of $249M at 7nm and $725M at 2nm
  - COST-3: more than two dozen companies at 180nm in 1998, three at the leading edge by 2020
  - COST-4: GlobalFoundries halting 7nm for lack of customers
  - CONC-1: TSMC's top ten customers were 76% of revenue
  - CONC-3: GlobalFoundries' customers already have their own design teams
  - LEARN-1 to LEARN-4: why chasing scale is rational
- **Challenges:** none verified yet. A possible one: TSMC serves 522 customers, so the "tail" is not empty (CONC-2).
- **Leads:** COST-7 (TSMC capex trend).
- **Context:**
  - COST-2: older and revised IBS design-cost estimates (Partial)
  - COST-5: TSMC's $165B US investment
  - CONC-12: TSMC's 70.4% foundry share, and GlobalFoundries ranked fifth

## H2. Customer concentration damages a foundry

**Claim.** Big customers push margins down, make losing one catastrophic, lock the foundry into their products, make it risk-averse, and raise its cost of capital.

**Status:** Well supported on buyer power, dependence and the cost of capital. The efficiency counter-argument is still only partly verified.

- **Supports:**
  - CONC-1, CONC-3, CONC-5: the filings' own risk factors
  - CONC-6: Imagination's shares fell up to 71% when Apple, about half its revenue, planned to leave
  - FIN-1: Porter on buyer power in high-fixed-cost industries
  - RISK-1: customers depend on processes not changing
  - CONC-4: GlobalFoundries' top ten customers were 73–75% of wafers before its IPO
  - COST-8: TSMC spends 7.1% of revenue on R&D, guessing the future at its own expense
  - CONC-8: AMD paid $320M (2012), and $100M plus a warrant valued at $235M (2016), to loosen its GlobalFoundries supply agreement
  - CONC-11: TSMC's top ten customers rose to 78% of revenue in 2025
  - FIN-2: concentration raises a supplier's cost of equity and debt
  - FIN-3: concentration worsens loan terms, more so with relationship-specific investment
- **Mixed:** CONC-7, Apple's reported "known good die" terms (reported, then disputed).
- **Challenges:**
  - FIN-5 (Partial): Patatoukas (2012), concentration can bring efficiencies
  - FIN-6: Irvine, Park & Yıldızhan (2016)
- **Leads:**
  - FIN-4: Wal-Mart suppliers
  - CONC-9: capacity pre-emption (CoWoS)
  - CONC-10: value capture, Nvidia's gross margin versus TSMC's
  - CONC-13: the Huawei cut-off
  - CONC-14: Apple's move from Samsung to TSMC
  - FIN-8: hold-up theory
  - FIN-10: capital structure and customers
  - RISK-2: Intel's Copy EXACTLY!
  - RISK-3: long automotive requalification

## H3. Chasing scale is rational under the experience curve

**Claim.** Manufacturing costs fall predictably as cumulative production grows, so serving the biggest customers is the fastest way down the cost curve.

**Status:** Well supported for costs falling with cumulative production. Argued for "so serve the biggest customers", which is our inference.

- **Supports:**
  - LEARN-1: Wright (1936)
  - LEARN-2, LEARN-3: BCG's experience curve, built on semiconductor data
  - LEARN-4: Nagy et al. (2013), Wright's law gives the best forecasts
  - LEARN-5: solar's 20% learning rate
  - LEARN-7: Irwin & Klenow, DRAM learning rates average 20%
- **Challenges:** LEARN-4 caveat, where a time-based rule performs almost as well and yearly production (economies of scale) explains much of the predictability.
- **Leads:** LEARN-8 (Texas Instruments' learning-curve pricing).

## H4. Turning an idea into silicon can now be cheap

**Claim.** Open design kits, open tools, shared shuttles and AI are cutting the up-front cost of a chip, at least on mature processes.

**Status:** Contested. The design side is getting cheaper. The open design kits are still labelled previews. The one company built around the new tools failed to raise funding.

- **Supports:**
  - SW-1, SW-3: the software analogy
  - OPEN-1: SKY130 open design kit and free shuttles
  - OPEN-4: OpenROAD's no-human-in-loop goal
  - OPEN-5: Tiny Tapeout at $300 a design
  - OPEN-6: a GPT-4-assisted chip taped out
- **Mixed:** OPEN-2, OPEN-3 (open design kits, but "not intended" for production).
- **Challenges:** OPEN-7, Efabless shut down after failing to complete a funding round.
- **Leads:** OPEN-8, AlphaChip (contested claims).
- **Context:** COST-6, most automotive devices use mature nodes.

## H5. There is a long tail of demand for chips

**Claim.** Many potential chip customers exist whose ideas are never made because the up-front cost is too high. If it falls, they add up to a real market.

**Status: Contested, and weaker than we thought.** The chip-specific data asked for here has now been gathered ([`demand/`](demand/)), and it does not support the strong form of the claim.

The demand is real and it is *price-elastic*: every time the price of a tape-out has fallen sharply, more people have come. Tiny Tapeout has taken over 4,300 submissions in four years at €70 a tile plus a devkit (DEM-1, DEM-2, DEM-10, SMB-10), and every free or subsidised programme found has been oversubscribed — 45 submissions against 40 slots on Google's first Open MPW shuttle (DEM-4, DEM-6), 98 applications for 50 Europractice places (DEM-17).

But the *level* is small and the trend is not upward. When Google made fabrication, the design kit and the tools free and promoted it worldwide, the total global response over six shuttles was 364 submissions (DEM-9). Europractice ran between 363 and 614 designs a year for the whole of 2000 to 2017 and is now back to 753 after a peak of 985 (DEM-16). CMP peaked at 401 circuits in 2007 (DEM-19); CMC Microsystems fell in each of the three years for which figures were read, to 240, from a five-year total of 1,803 that implies a higher, unread 2022-23 (DEM-20); MOSIS managed about 60,000 designs and up to $10M of revenue a year in four decades (SMB-5). The count of ASIC design starts was falling through the 2000s on both analyst houses' numbers, and no current count is public (DEM-11). And the existing citation of TSMC's "tail" turns out not to support H5 at all: those customers average about US$41 million a year each (DEM-15).

The honest reading is that a long tail of *experiments* certainly exists and grows when the price falls; a long tail of *paying manufacturing demand* at a scale that could fill a fab has not been demonstrated by anything found.

- **Supports:**
  - DEM-1, DEM-2: 4,268 Tiny Tapeout designs on the site's own table and 4,314 submission records counted from its API; submissions by year 317 → 970 → 1,632; 7 of the 24 runs with submissions filled 100% of their tiles
  - DEM-4: the first Google-sponsored shuttle filled all 40 slots in 30 days, and "Approximately 60% of the designs were submitted by software, FPGA and hardware developers (non-IC experts) — demonstrating a significant untapped underlying interest"
  - DEM-5, DEM-6, DEM-9: submissions per Open MPW shuttle rose 45 → 56 → 75 → 90 against a fixed 40 slots
  - DEM-10: Tiny Tapeout's industrial share rose from 14% (2023) to 38%, so these are not only hobbyists (the survey behind it is **Partial**)
  - DEM-17: 98 applications for 50 places in Europractice's First User Stimulation Programmes
  - DEM-18: "Several TSMC shuttles are extremely loaded … If required, a waiting list will be created."
  - DEM-21: the NSF workshop report — shuttle programmes "can be overbooked", a lottery picked 40 projects per Open MPW shuttle, and "There is also the third option where a design is not taped-out at all"
  - SMB-1: JLC has 1,358,700 paying users placing 21.3 million orders a year, which is a long tail of hardware demand that unambiguously exists, though for printed circuit boards rather than chips
  - TAIL-1: Anderson's long tail
  - TAIL-2: the value of wider choice in books
  - OPEN-5: 174 submissions to one Tiny Tapeout round
- **Challenges:**
  - DEM-16: Europractice ran 363–614 designs a year for eighteen straight years, and 69% of 2024's submissions came from universities against 9% from European industry
  - DEM-9: 364 submissions worldwide across six shuttles when the whole thing was free
  - DEM-2: 9 of Tiny Tapeout's 24 runs with submissions came in below 75% of capacity, including TT07 at 58.8%, TT08 at 46.1% and TT10 at 46.9% after capacity rose to 512 tiles
  - DEM-10: ChipFoundry reserves "the right to delay a shuttle if it's less than 50% full"
  - DEM-11: ASIC design starts falling through the 2000s on both analyst houses' numbers; no current count is public
  - DEM-12: only 5% of IC/ASIC projects reported first-silicon success in 2026, down from 14.4% in 2024 — so the binding constraint looks like verification engineering, not the price of an attempt
  - DEM-13: Elberse's own data — "Rather than bulking up, the tail is becoming much longer and flatter" — and she extends the conclusion to physical goods
  - DEM-15: TSMC's 512 non-top-ten customers average about US$41M a year each, so CONC-2 and CONC-11 should no longer be read as support for H5
  - DEM-19, DEM-20, DEM-22: CMP peaked at 401 circuits and its domain is now parked; CMC has fallen to 240; MOSIS's free academic programme ended in 2020
  - SMB-4: Shapeways had "over one million customers" and one of them was 17–23% of revenue
  - TAIL-3: Elberse finds hits still dominate and consumers in the tail rate niche titles lower
- **Mixed:** DEM-21, whose one paragraph contains both the strongest statement that shuttles are overbooked and the strongest statement that a mature-node run can be "not desirable enough to make economic sense".
- **Context:** CONC-2, CONC-11 (TSMC's customer counts — see DEM-15 before citing them for H5); SMB-5 (MOSIS's realised scale); SMB-6 (Europractice's subsidy).
- **Needs:**
  - A current count of ASIC design starts. The public record stops in the 2000s (DEM-11).
  - Any survey of would-be chip customers about what actually stops them. None was found, in either direction (see [`demand/search-log.md`](demand/search-log.md)).
  - Cases of a small chip customer becoming a large one. Still none verified.
  - Submission counts for the Open MPW shuttles MPW-3, MPW-4, MPW-7, MPW-8 and the GF180MCU runs.

## H6. Small customers can each be profitable

**Claim.** If the fab does no per-customer engineering and sells machine time at published prices, each small customer is profitable.

**Status: Contested.** There is now one strong, audited example on each side, and the variable that separates them is not customer size.

For: JLC earns a 12.65% net margin from 1,358,700 paying users on an average order of about US$67, and its own risk factors say its gross margin is about 28% on the small-batch long tail against 2.76% on high-volume work — i.e. the long tail is the profitable part (SMB-1). MOSIS is described by its host institution as "a self-sustaining business for 40 years" (SMB-5). Against: Xometry has never made an operating profit in any year it has filed, on a 34.7% marketplace gross margin (SMB-3); Shapeways assembled over a million customers and went into Chapter 7 liquidation (SMB-4); Protolabs is profitable but its gross margin fell 14 points in a decade while revenue per customer went nowhere, and it is now deliberately chasing "larger orders" (SMB-2). Europractice says publicly that EU funding is what keeps it affordable (SMB-6).

The cost-to-serve data asked for here turns out to be published, in the one place nobody thinks to look: the MPW price lists themselves. Every one of them prices the fixed cost per project explicitly — a minimum billable area, a flat per-project fee, an annual membership, a surcharge for splitting a block among several small customers (SMB-7, SMB-8). MOSIS's 0.13 µm price was "$17,500 + ($4,000/mm² * area)" with a 10 mm² minimum: 30% of the cheapest possible ticket was fixed cost before any silicon (SMB-8). That fixed cost is exactly what H6 assumes away, and it does not go away because the fab stops doing engineering.

- **Supports:**
  - SMB-1: JLC — 1,358,700 paying users, US$67 average order, 12.65% net margin, largest customer 0.28% of revenue, and ~28% gross margin on the long tail against 2.76% on high volume
  - SMB-5: MOSIS, "a self-sustaining business for 40 years" at about $10M a year
  - SMB-9: chipIgnite's flat published price survived the collapse of the company that invented it and was restarted by its founders at $14,950
  - SMB-12: mature-node mask sets are now well under $100,000, so the fixed cost to recover per project is tens of thousands, not millions
  - SW-5: on AWS, small on-demand buyers pay more per unit than committed buyers, so small customers can pay a premium for flexibility
- **Challenges:**
  - SMB-3: Xometry, no operating profit in any filed year, 34.7% marketplace gross margin, and an explicit pivot to "large enterprise customers"
  - SMB-4: Shapeways, over a million customers, Chapter 7 liquidation on 2024-07-02, $176.9M accumulated deficit
  - SMB-2: Protolabs' gross margin 58.5% (2015) → 44.5% (2025) while revenue per customer grew 1.28% a year; its numeric customer-concentration disclosure was dropped after FY2022
  - SMB-6: Europractice says EU funding is what makes it affordable, and that without it "niche and emerging technologies from European sources could not be stimulated to a level that makes them viable"
  - SMB-7, SMB-8: every published MPW price list prices the fixed cost per small customer — minimum billable areas, per-project fees, and a €1,000 "verification charge" for splitting one block among four or more sub-designs
  - SMB-11: almost none of what a small customer pays is silicon, so "silicon is cheap" does not imply the price can fall
  - DEM-14: Daniel Nenni — open-source tool users "do it mainly due to cost and that is a tough customer base to profit from" (his stated opinion, not data)
  - OPEN-7: Efabless's failure, though it was an intermediary and not a fab
- **Mixed:** SMB-2 (profitable, but the margin trend and the strategy both run away from the tail); SMB-5 (self-sustaining for forty years, but its successor's stated goal is to "achieve self-sustainability within the next few years").
- **Needs:**
  - A fab's own margin by customer size. Still not public anywhere; SMB-1 to SMB-6 are analogues, not measurements.
  - What share of Xometry's revenue comes from its 1,760 accounts spending over $50,000 — not disclosed, and without it nobody can say how much of its revenue is long tail (SMB-3).
  - The academic cost-to-serve literature. Kaplan and Narayanan (2001) could not be obtained legally; **the widely repeated "20% of customers generate 150–300% of profits" figures must not be quoted in this project until someone with library access checks them.** See [`demand/search-log.md`](demand/search-log.md).

## H7. Many small customers reduce risk and remove buyer power

**Claim.** With thousands of small customers, none has leverage, and losing any one of them is noise.

**Status:** Argued from theory. Well supported as the reverse of H2.

- **Supports:** FIN-1 (Porter: buyers are powerful when few, or when large relative to the seller).
- **Leads:** FIN-7 (countervailing-power theory), FIN-9 (diversification theory).
- **Challenges (Partial):** FIN-5, enterprise concentration can bring efficiencies and stickiness.

## H8. Openness is necessary to attract many small customers

**Claim.** Published prices, visible queues and public results let people try without asking permission, which is what grows the customer base.

**Status:** Argued from analogy.

- **Supports:** SW-2 (AWS S3 launched with published, pay-as-you-go pricing and no minimum fee).
- **Needs:** evidence on how price transparency affects adoption by small buyers.

## H9. Many small, public experiments make a fab learn faster

**Claim.** Chip-making has ridden the experience curve on wafers but not on ideas. Many small, public experiments would add experience faster and share it.

**Status:** Contested and argued.

- **Supports:**
  - LEARN-6: Wilson et al., learning is faster for more granular energy technologies, "under certain conditions"
  - LEARN-7(e): learning does not carry well across chip generations, so each new generation starts over
- **Mixed:** LEARN-7(b, c). Firms learn about three times more from their own production than from others', but learning does spill over between firms, even across countries. That challenges `WHY.md`'s claim that what one team learns "adds little" to anyone else's experience. It also shows that spillovers exist to amplify.
- **Needs:** evidence on how much published process data speeds up learning at other firms.

## H10. Being paid for every attempt works in a world of skewed outcomes

**Claim.** Most attempts fail, but the fab is paid for all of them, and a few attempts produce most of the value.

**Status:** Well supported for outcomes being skewed. Argued for the fab capturing enough of that value.

- **Supports:**
  - SW-3: 96% of open-source value created by 5% of developers
  - SW-4: 55% of venture-backed start-ups terminated at a loss, while 6% produced about half the gross return
- **Challenges:** none recorded yet.

## H11. Markets and insurance can replace foundry judgement

**Claim.** Prices set by customers, insurers and futures providers can replace the foundry's own decisions about maintenance, risk, timing and priority (`PRINCIPLES.md` P3).

**Status:** Untested. So far the evidence is our own analysis, not outside sources.

- **Analyses:**
  - [`analyses/critical-review-of-principles-v0.10.md`](analyses/critical-review-of-principles-v0.10.md): incentive and mechanism flaws found
  - `AUCTIONS.md` at the repository root: worked comparison of auction styles
- **Context (Lead):** FIN-8, hold-up theory. General machine time sold on a market reduces relationship-specific investment.
- **Needs:** literature on electricity markets, spectrum auctions, reinsurance and catastrophe bonds, and exchange clearing houses.
