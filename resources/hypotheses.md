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

The demand is real and it is *price-elastic*: every time the price of a tape-out has fallen sharply, more people have come. Tiny Tapeout has taken 4,268 designs on its own table, or 4,314 submission records counted from its API — two different populations that must not be added or rounded together — over four years at prices that ran $100, then $150, then $300 before the €70-a-tile-plus-devkit structure quoted here (DEM-1, DEM-2, DEM-10, SMB-10, OPG-14), and some free or subsidised programmes have been oversubscribed — 98 applications for 50 Europractice places (DEM-17). **Not all of them, and the claim that they all were is contradicted inside this directory:** Efabless's own platform labelled MPW-1 *Undersubscribed* at 37 of 40, and chipIgnite runs CI 2106Q, CI 2110C and CI 2204C filled 57%, 70% and 32% (OPG-2).

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
  - DEM-16 (**corrected 2026-09-19**): Europractice's 2000–2017 series does not plateau. Regressing log(designs) on year over the verified portion gives **+2.14%/yr, t = +5.15** (480 → 614, endpoint CAGR +1.46%/yr). It is weak support, not a challenge.
  - IHF-1, IHF-5: Science Corporation, a funded commercial buyer, states that existing fabs were "simply inaccessible for this kind of low-volume work, often with uncommon materials and tool parameters", and bought a MEMS foundry rather than keep trying to buy the service
  - PAY-6, PAY-8, PAY-9: **the growth is visible in money, not only in submissions.** Tiny Tapeout's derived gross revenue rises every year, ≈$12k → $42k → $167k → $195k → €342k (nine months of 2026), a +156%/yr CAGR over 2022–2025; chipIgnite's paid slots rose 32 → 52 → 93 → 160, +71%/yr; wafer.space took $55,500 then $175,000 then $125,000-and-open at published unsubsidised prices. **All three are derivations from published prices and published unit counts, not measurements**
- **Challenges:**
  - DEM-16, *partly*: 69% of 2024's submissions came from universities against 9% from European industry. **The "eighteen flat years" half of this entry was wrong and has been moved to Supports** — see the Supports list and the correction note in DEM-16 itself.
  - DEM-9: 364 submissions worldwide across six shuttles when the whole thing was free
  - DEM-2: 9 of Tiny Tapeout's 24 runs with submissions came in below 75% of capacity, including TT07 at 58.8%, TT08 at 46.1% and TT10 at 46.9% after capacity rose to 512 tiles
  - DEM-10: ChipFoundry reserves "the right to delay a shuttle if it's less than 50% full"
  - **CF-6: the only operator that publishes both sides of the funnel has never once filled a shuttle.** 21 committed of 28 planned, 23 of 37, 29 of 43 — and its `interest`, which runs two to three times its slot count, is **revised down by 17–23% by the operator itself** after the run closes. Interest is not demand, and the operator agrees
  - **CF-14: ChipFoundry's own design contest converted 234 proposals into 3 fabricated chips — 1.3%.** Every submission-based growth figure in `demand/` should be read against that ratio
  - **CF-9: the long tail reaches ChipFoundry through one intermediary.** Tiny Tapeout put 1,357 designs onto ChipFoundry silicon in five runs while buying **five slots**, at €185 a design rather than $14,950 — and ChipFoundry subsidises part of even that
  - DEM-11: ASIC design starts falling through the 2000s on both analyst houses' numbers; no current count is public
  - DEM-12: only 5% of IC/ASIC projects reported first-silicon success in 2026, down from 14.4% in 2024 — so the binding constraint looks like verification engineering, not the price of an attempt
  - DEM-13: Elberse's own data — "Rather than bulking up, the tail is becoming much longer and flatter" — and she extends the conclusion to physical goods
  - DEM-15: TSMC's 512 non-top-ten customers average about US$41M a year each, so CONC-2 and CONC-11 should no longer be read as support for H5
  - DEM-19, DEM-20, DEM-22: CMP peaked at 401 circuits and its domain is now parked; CMC has fallen to 240; MOSIS's free academic programme ended in 2020
  - SMB-4: Shapeways had "over one million customers" and one of them was 17–23% of revenue
  - TAIL-3: Elberse finds hits still dominate and consumers in the tail rate niche titles lower
  - **Re-runs (data-cuts analysis):** 56% of Tiny Tapeout's record 2025 was designs already run before, on process bring-up shuttles (`ttihp25a`: 433 re-runs of 564). Stripping them halves the growth rate — 2023→2025 CAGR falls from **+64.6%/yr to +32.2%/yr**, still positive but far less than the headline
  - **Retention (data-cuts analysis):** 73.6% of Tiny Tapeout designers make exactly one design ever; year-on-year designer retention is 6–16%; a two-segment fit gives a recurring core of about **1,250 people worldwide**. That, not 4,268, is the size of the repeat population
  - IHF-8: the one small-customer MEMS foundry with public audited accounts saw revenue fall **32% in its final year**
  - **LN-9: a county built a fab to sell shared cleanroom access on a membership model, and "that interest never materialized".** Osceola County, Florida's $75m, 109,000 sq ft Kissimmee fab was designed around exactly the demand H5 assumes; it was rebranded and repointed at defence contracts before it opened in 2017, and nine years after ICAMR was launched the whole 500-acre campus employed "roughly 90 people" against about $200m of county and local money — **$2,222,222 of county capital per realised job**. A third instance of the `IHF-8`/`OPEN-7` failure mode, at a third site, with a third funding model
  - IHF-6, IHF-7: Europractice's MEMS offering fell from three MUMPs processes in 2020 to one X-FAB process in 2026
  - ACC-11: a third instance of the CMP/Efabless pattern — a long-running service vanishing from the public internet
  - **PAY-8: revenue grew more slowly than submissions on the longest paid series there is.** Over 2021–2024 chipIgnite's submissions rose 7.39× (+94.8%/yr) and its paid slots rose 5.00× (+71.0%/yr), because a 40-slot shuttle caps money and nothing caps interest. On the successor the divergence is total: ChipFoundry's `interest` went 129 → 262 while `committed` went 44 → 45
  - **PAY-8, PAY-6: the sector's money fell 46% in 2025, the year its unit counts set a record.** The three programmes together took $1,726,925 in 2024 and $931,158 in 2025, while `data-cuts-and-statistics.md` §3.2 records 2025 as Tiny Tapeout's largest year ever. The cause is Efabless's failure, not a demand collapse — but a submission series hides exactly that kind of risk and a revenue series shows it
  - PAY-5: an unknown but large share of recent Tiny Tapeout tiles is sponsorship and institutional block booking rather than small-buyer money — "Half the area and PCBs have been reserved for [the IEEE]" on TTSKY26b, with only "40 non-subsidized PCBs" left
  - PAY-9: wafer.space's whole worldwide response in thirteen months is **30 orders**
- **Mixed:** DEM-21, whose one paragraph contains both the strongest statement that shuttles are overbooked and the strongest statement that a mature-node run can be "not desirable enough to make economic sense".
- **Context:** CONC-2, CONC-11 (TSMC's customer counts — see DEM-15 before citing them for H5); SMB-5 (MOSIS's realised scale); SMB-6 (Europractice's subsidy).
- **Needs:**
  - A current count of ASIC design starts. The public record stops in the 2000s (DEM-11).
  - Any survey of would-be chip customers about what actually stops them. None was found, in either direction (see [`demand/search-log.md`](demand/search-log.md)).
  - Cases of a small chip customer becoming a large one. Still none verified.
  - Submission counts for the Open MPW shuttles MPW-3, MPW-4, MPW-7, MPW-8 and the GF180MCU runs.

## H6. Small customers can each be profitable

**Claim.** If the fab does no per-customer engineering and sells machine time at published prices, each small customer is profitable.

**Status: Contested — and the condition that decides it has now been identified.**

Across seven companies in five industries that print a margin split by order size
([`demand/other-industry-margins.md`](demand/other-industry-margins.md)), the small end wins in
five cases and loses in two, and **what sorts them is not customer size but whether a small order
repeats a frozen process or is a first-of-a-kind that consumes its own process development.**

| Small order is… | Cases | Small end |
|---|---|---|
| a **repetition of a frozen process** | JLC (PCB), Cimpress (print), Knight-Swift (freight), Catalent (CDMO clinical supply) | **wins** |
| a **first-of-a-kind consuming process development** | Asymchem, Porton (CDMO) | **loses** |
| both, sold separately | Silex (MEMS) — bespoke development priced as its own service | **wins** |

**This is the sharpest open question the project has.** A shuttle on which every design is novel
looks structurally like a CDMO's clinical line, not like JLC. Porton 2023 is JLC 2025 exactly
mirrored: its small-batch line was 17.39% of revenue and **2.62% of gross profit**, against JLC's
75.57% and 97.60%. Which of the two foundry.api resembles is **a design decision in `PRINCIPLES.md`
and `DESIGN.md`, not an empirical fact** — it turns on whether the fab sells a frozen, published
process that customers target, or bespoke process work per customer. There is an audited example on each side, and the variable that separates them is not customer size.

The decisive new evidence is IHF-8: MEMSCAP's North Carolina MEMS foundry — a merchant wafer fab selling to many small customers through MUMPs multi-project runs, 475 m² of ISO 4 cleanroom, 6-inch wafers, fourteen people — **lost EUR 805k then EUR 857k, being 28.2% then 44.3% of its own revenue**, in the two years visible before it was sold. Unlike Xometry or Shapeways it *is* a wafer fab, which makes it the closest analogue this directory holds, and it lands against H6. The counter-argument is recorded with it: the loss is a divisional IFRS 5 figure with an undisclosed group-overhead allocation, in a business being wound down for sale, and a buyer that is its own anchor customer faces different economics.

For: JLC earns a 12.65% net margin from 1,358,700 paying users on an average order of about US$67, and its own margin-by-order-size table puts gross margin at **36.24%** on sample and small-batch work against **2.76%** on medium and large batches, with the offline big-batch channel outright loss-making at **−6.71%** (SMB-1). **28.06% is the blended whole-PCB figure and must not be quoted as the small-batch margin** — it already contains the 2.76% segment. Decomposed, the long tail is 75.57% of PCB revenue but **97.60% of gross profit** ([`analyses/long-tail-pays-for-the-capital.md`](analyses/long-tail-pays-for-the-capital.md)). MOSIS is described by its host institution as "a self-sustaining business for 40 years" (SMB-5). Against: Xometry has never made an operating profit in any year it has filed, on a 34.7% marketplace gross margin (SMB-3); Shapeways assembled over a million customers and went into Chapter 7 liquidation (SMB-4); Protolabs is profitable but its gross margin fell 14 points in a decade while revenue per customer went nowhere, and it is now deliberately chasing "larger orders" (SMB-2). Europractice says publicly that EU funding is what keeps it affordable (SMB-6).

The cost-to-serve data asked for here turns out to be published, in the one place nobody thinks to look: the MPW price lists themselves. Every one of them prices the fixed cost per project explicitly — a minimum billable area, a flat per-project fee, an annual membership, a surcharge for splitting a block among several small customers (SMB-7, SMB-8). MOSIS's 0.13 µm price was "$17,500 + ($4,000/mm² * area)" with a 10 mm² minimum: 30% of the cheapest possible ticket was fixed cost before any silicon (SMB-8). That fixed cost is exactly what H6 assumes away, and it does not go away because the fab stops doing engineering.

- **Supports:**
  - SMB-1: JLC — 1,358,700 paying users, US$67 average order, 12.65% net margin, largest customer 0.28% of revenue, and ~28% gross margin on the long tail against 2.76% on high volume
  - SMB-5: MOSIS, "a self-sustaining business for 40 years" at about $10M a year
  - SMB-9: chipIgnite's flat published price survived the collapse of the company that invented it and was restarted by its founders at $14,950
  - **CF-8, CF-16: a new, unsubsidised company re-based the whole inherited price list by about +50%, and has held it for seventeen months.** The shuttle went $9,750 → $14,950 (**+53.3%**), the ML product $14,750 → $22,250 (**+50.8%**) and $30,000 → $45,000 (**+50.0%**). **Three products, three repricings, all +50% to +53%** — which is an outside estimate that the subsidised-era price was about **a third below** the cost of providing the service, and that there is a price at which it can be provided
  - **CF-13: ChipFoundry is paid in full about nine months before it delivers**, and publishes its own viability floor — "a minimum of 20 confirmed participants" per run, i.e. **20 × $14,950 = $299,000** of bookings. Every completed shuttle has cleared it: 21, 23, 29
  - **CF-16: the operator's own price list says fabrication is the entry point, not the margin.** A Tier-1 IP licence is **$42,900**, an individual block up to **$33,900**, SRAM **$2,500**, support **$1,000** — against a **$14,950** tapeout. A long-tail fabrication business that works may have to look like this
  - SMB-12: mature-node mask sets are now well under $100,000, so the fixed cost to recover per project is tens of thousands, not millions
  - SW-5: on AWS, small on-demand buyers pay more per unit than committed buyers, so small customers can pay a premium for flexibility
  - **FUND-4: when the European Commission funded only part of Europractice, the partners covered the rest themselves and kept the service running.** FP7 reimbursed a fraction of declared cost, so the operating cost is visible there and nowhere else: about EUR 1.5–1.7m/yr to run the service, of which the EC paid **63.8%** and the partners found **36.2%**. They also continued through 2006–2007 with **no dedicated grant on record** — FP6 BRIDGE says the partners "agreed to continue with EUROPRACTICE for a further year at no additional funding". From H2020 onward, non-profits are reimbursed at 100%, total cost equals EU contribution, and the cost information disappears
  - PCB-1: JLC's PCB gross margin beats the mean of the five peers its own prospectus names by **+8.56 pp** in 2025 (corrected from the printed +10.00 pp, which omitted Fastprint's later-published 25.26%), and the prospectus attributes the gap to "销售模式和客户结构差异" — "differences in sales model and customer structure"
  - PCB-2: JLC **owns its plants** — net fixed assets CNY 3,257,464,600 including CNY 952,981,900 of buildings, CNY 1.395bn of capex in 2025, registered land titles. It also took a **CNY 131,365,100 fixed-asset impairment** because "PCB 中大批量订单相对不饱和" ("medium- and large-batch PCB orders are relatively under-full") left big-batch equipment idle, while the long-tail plant ran at 76.78% utilisation
  - PCB-3: a second audited company, 迅捷兴 (Xunjiexing), attributes a 5.62-point margin fall to a shift toward batch work — volume **+30.02%**, margin down. **Superseded by PCB-11, which is far stronger — cite that instead**
  - **PCB-7: a second independent prospectus lands within 0.8 pp of JLC.** 强达电路 (Qiangda, SZSE 301628) prints the same split at p.289: in 2024 H1 the tail was 85.79% of revenue at **32.37%** gross margin against **3.17%** for large batch — **98.40% of gross profit**, against JLC's 97.60%, from a completely separate filing with a different sponsor
  - **PCB-11: Xunjiexing ran the experiment forwards and lost.** Revenue **+42.47%**, gross profit **−15.37%**. Large-batch revenue nearly doubled (**+77.93%**) while large-batch gross profit fell **44%**. Four customers at **32.03% of revenue** were sold at a combined **−11.26% gross margin**. Net loss CNY 22.4m, utilisation 41.55%, the new Zhuhai plant at −44.45%. One company moving from the tail towards volume in consecutive audited years, and being made worse off. **It also proves a long tail is not sufficient** — the same company is a declared sample specialist with 10,000+ customers and it is losing money
  - **PCB-13: the controlled test.** 中富电路 (Zhongfu) is a *large-batch* house — 61.79% of revenue is orders over 50 m² — answering an exchange asking why its margin was falling, so it had no incentive to flatter small batch. It splits margin by order batch **inside each product family**, which holds layer count roughly constant, and **small batch wins 8 of 8 cells** (1.15×–2.66×). This is the best evidence in the directory that the order-size effect is not a product-mix artefact
  - **Eighteen company-periods across five companies, and in not one does a larger-order tier out-earn a smaller-order tier.** All five decompositions reconcile to within 0.01 pp of the filings' own printed figures
  - **OIM-5: a real MEMS wafer foundry prints the split, and the small-batch side wins every year.** 赛微电子, owner of Sweden's Silex, published gross margin separately for bespoke MEMS process development and volume wafer manufacturing for four years. The bespoke half won by +53.5, +31.0, +4.6 and +6.7 pp; in 2022 it was 46.6% of revenue and **70.3% of gross profit**. The company describes Swedish FAB1&2 as "a pilot line plus small-batch production line" and Beijing FAB3 as "a scale volume-production line" — two fabs, two strategies, and the small-batch one is the better business. **Its new volume fab ran at −50.00% gross margin while ramping**, which independently corroborates the idle-plant test in [`analyses/long-tail-pays-for-the-capital.md`](analyses/long-tail-pays-for-the-capital.md)
  - IHF-11 (**🚩 DISPUTED 2026-09-25 — do not cite, see the banner in [`demand/in-house-fabrication.md`](demand/in-house-fabrication.md)**): the **tool set** of a working 150 mm MEMS fab is claimed to be a **one-to-two-million-dollar** asset — US$1.0 million contracted and US$2,124,650 independently appraised in the Akoustis deal, EUR 498 thousand of net book value at MEMSCAP — against "well over $50 million" to build a facility new. **The tools are not the obstacle.** *(Corrected 2026-09-19: this line previously read "a complete working small MEMS fab is a ~US$3M asset at roughly 1× trailing revenue". Both headline prices turned out to describe different things — Akoustis' was 63.6% real estate plus a $1.73M clawback, GAAP consideration $4.58M, and was set "without significant price negotiation" by a public-sector seller; MEMSCAP's carried no building and no liabilities but came with EUR 655 thousand a year of rent. See IHF-3 and IHF-9.)*
- **Challenges:**
  - SMB-3: Xometry, no operating profit in any filed year, 34.7% marketplace gross margin, and an explicit pivot to "large enterprise customers"
  - SMB-4: Shapeways, over a million customers, Chapter 7 liquidation on 2024-07-02, $176.9M accumulated deficit
  - SMB-2: Protolabs' gross margin 58.5% (2015) → 44.5% (2025) while revenue per customer grew 1.28% a year; its numeric customer-concentration disclosure was dropped after FY2022
  - SMB-6: Europractice says EU funding is what makes it affordable, and that without it "niche and emerging technologies from European sources could not be stimulated to a level that makes them viable"
  - SMB-7, SMB-8: every published MPW price list prices the fixed cost per small customer — minimum billable areas, per-project fees, and a €1,000 "verification charge" for splitting one block among four or more sub-designs
  - SMB-11: almost none of what a small customer pays is silicon, so "silicon is cheap" does not imply the price can fall
  - DEM-14: Daniel Nenni — open-source tool users "do it mainly due to cost and that is a tough customer base to profit from" (his stated opinion, not data)
  - OPEN-7: Efabless's failure, though it was an intermediary and not a fab
  - **CF-11, CF-17: the successor is running at about 70% of the dead company's best year, at 1.53× the price — so roughly 46% of the unit volume.** 89 committed slots over five shuttles, ≈$1.06m/yr of gross bookings at list price, and **about $273,000 per named employee on a floor headcount of four**. That is a ceiling, not an estimate, and for a US semiconductor-services business it is thin
  - **CF-7: real cycle time is 8.3–9.7 months against a published "approximately 5 months"**, deliveries ran 76–94 days late, two announced 2026 shuttles were never run, and the cadence is down from Efabless's four a year to two then three
  - **CF-14, CF-9: at the thin end, the person who wants the chip is not the person who pays for it.** ChipFoundry sells contest prize slots to sponsors, subsidises "a portion" of the Tiny Tapeout slots it sells, and Tiny Tapeout's own shuttles are sponsored by IEEE, SwissChips, Tillitis and ChipFoundry
  - **IHF-8: audited losses of 28.2% then 44.3% of revenue at a merchant MEMS foundry serving small customers through shuttle runs — the strongest challenge in this directory, because it is a wafer fab and not an intermediary**
  - **LN-7: the same company reported a high-mix segment and an anchor-customer segment side by side, and only the anchor-customer one made money.** SkyWater's FY2025 10-K splits Legacy SkyWater (Bloomington + Kissimmee, "highly customized projects in a low-volume research and development environment") from SkyWater Texas (Fab 25, one customer on a take-or-pay). Legacy: **$(34,496) thousand operating loss on $266,847 thousand of revenue, −12.93%**. Texas: **+$31,920 thousand on $175,292 thousand, +18.21%**. Direct fab labour is almost identical in the two (29.97% against 30.24% of revenue); **the difference is SG&A, 25.02% against 4.63%** — which is the cost-to-serve H6 assumes away, measured inside one wafer fab. Caveats are real and are set out at full strength in the entry (Texas is six months, its revenue unwinds a $120m off-market supply contract, and corporate SG&A sits in the Legacy column) but none of them turns −12.93% positive
  - **LN-14, LN-17: building capacity costs about 14× as much per job, and 18× as much per wafer start, as buying it.** Across eleven US sites the capital cost per job runs from $80,000 to $5,357,143 (**67×**). The three cheapest are all purchases of an operating fab from a seller who wanted out — **$80,000** (Tower/Maxim San Antonio, 2016), **$98,214** (Akoustis Canandaigua, 2017), **$101,884** (SkyWater Fab 25, 2025) — a 27% band across ten years, three states and two wafer sizes; the eight build-or-tool rows average **$1,300,816 a job**. On capacity rather than jobs the same split appears independently: Tower bought 28,000 wafer starts a month at **$1,429/wspm** while Polar built 20,000 at **$26,250/wspm**. Whatever a long tail can pay for, it is not $1.3m of capital per job — but $93k a job, for a fab somebody else is exiting, is a different question
  - **MOS-8: DARPA paid roughly six times the ticket price to keep MOSIS running.** IDA Paper P-2429 Vol. II (April 1991), a case study written *for DARPA*, puts the first decade at "**about $30 million in facility and staff costs plus roughly $14 million in project support costs**" — $44m, ≈$4.4m/yr. Against ~12,950 designs 1981–89 that is **$2,317 per design of facility-and-staff cost alone (5.8× the $400 list price of a 1987 TinyChip), or $3,398 all-in (8.5×)**. The longest-running MPW service in history never covered its operating cost from its price list during the period anyone measured it
  - **MOS-10: the brokerage model already failed once, in 1984.** Synmos, a commercial silicon broker, handled 1,400 chips 1981–83 with DARPA as its main customer and was "on ice" by 1984 with no order for over a year. DARPA's programme manager Paul Losleben: *"Synmos was not adding enough value to the process… **there may not yet be sufficient demand for a brokerage service for any one broker to survive.**"* H5 asked and answered in the negative forty years ago, by the person funding the alternative
  - IHF-9: the *other* small MEMS fab in this directory needed **government grants for 36.5% of its FY2016 revenue** to lose only $1.5 million, its third-party fabrication revenue **halved** in the year before it was sold ($5,018,139 → $2,872,939), and it burned about $3.0 million of cash a year. Two independent merchant MEMS fabs, two continents, both losing money on small customers
  - IHF-3, IHF-11 (**🚩 DISPUTED 2026-09-25 — do not cite**): the cheap part of a fab is claimed to be the tools, with the recurring facility cost the real burden. MEMSCAP paid **EUR 655 thousand a year** to rent a 475 m² cleanroom it did not own — **22.9%** of the division's revenue — and the Akoustis fab's **utilities alone** cost $1,132,403 a year
  - PCB-4: Fastprint's IC-substrate line runs at **−16.06%** gross margin explicitly because it "尚未实现大批量生产" ("has not yet achieved large-batch production") and carries undiluted labour and depreciation — the capital-intensity argument stated by a company living it, and silicon sits far closer to the substrate end than to bare board
  - PCB-5: 强达电路 (Qiangda) has about 3,000 customers, sells 100% direct on negotiated terms, and earns **26.10%** — within two points of JLC. 迅捷兴 (Xunjiexing) has "over ten thousand" customers, calls itself a sample-board specialist, and earns **8.52% with a net loss**. Customer count predicts neither margin nor concentration
  - ACC-4: Europractice's mini@sic surcharge — **3,080 ÷ 1,760 = 1.75, a 75% premium for being small**
  - ACC-12: CMP's itemised per-project fixed fees, published
  - **PCB-9: small orders cost more to sell, and this is a real cost the gross-margin tables hide.** 崇达技术 (Chongda) prints selling expense at **7.09–7.25% of revenue** for the sample house against **3.07–3.37%** for large-batch peers. **Every margin figure in the PCB and other-industry evidence is a *gross* margin, and no filing anywhere allocates SG&A by order size** — so "97.6% of gross profit" must never be restated as a share of *profit*
  - PCB-14: 本川智能 (Benchuan) — margin rises 18.26% → 38.69% on **layer count alone**, which is a confound for every order-size table that does not control for it (PCB-13 is the only one that does)
  - **OIM-3, OIM-4: two independent audited CDMOs print JLC's table upside down, across seven company-years.** 博腾股份 (Porton): small-batch/clinical at **6.84%** gross margin against **53.48%** for commercial volume in 2023 — 17.39% of revenue and **2.62% of gross profit**. 凯莱英 (Asymchem) 2024: **39.42%** small against **53.32%** bulk. This is the strongest challenge to H6 in the directory and belongs beside SMB-1 with equal prominence
  - **OIM-6: the gross-margin advantage may not survive customer acquisition.** Cimpress is the only company found that publishes both segment gross margin and a measure below it, and the long tail's **23-point gross-margin lead becomes 0.26 points at segment EBITDA** — advertising costs 15% of revenue to acquire micro-businesses against 5% for the wholesale channel, eating **98.9%** of the advantage. **Nothing in SMB-1 says what it costs JLC to acquire 1.36 million users**
  - **OIM-7: where a time series exists, the long-tail premium is narrowing** — Cimpress 29.6 → 22.9 pp over six years, Silex 53.5 → 6.7 pp — and two of the five companies stopped publishing the split in their latest annual report
  - **FUND-7: CMC Microsystems is the only multi-project-wafer broker anywhere with audited accounts, and customers cover a minority of its cost.** In the year to 2008-03-31 customers paid **9.15%** of revenue (CAD 989,771 of 10,822,211) against an 89.63% government grant. In the year to 2026-03-31, stripping the FABrIC pass-through, it earned CAD 5.4m against CAD 7.3m of cost — **74.0% recovery**, i.e. **CAD 30,417 of cost per prototype and a CAD 7,917 subsidy per prototype** on 240 prototypes. This is a measurement, not an analogue
  - **MOS-3: the traditional brokers have got dramatically *less* productive per head than a 1984 service running on 1984 computers.** ISI's own annual reports to DARPA give MOSIS's head count as **12 (1983), 11 (1984), 20 (1985), 27 (1986/87)**, at **128, 149, 90 and 62 designs per head**. Europractice today is **39.6** (`DEM-16`, `FUNDX-5`) and CMC **5.0** (`DEM-20`, `FUNDX-6`). The 1984 point is the load-bearing one because it removes the escape hatch that self-service only became possible with modern software: MOSIS's own reports describe users perceiving it as "a black box that accepts artwork files electronically and responds with packaged IC devices" (`MOS-4`). **The variable is not vintage but whether a human is in the loop per design** — ChipFoundry, a *new* provider, sits at 16.0–22.2, below Europractice. Decomposition, the inversion that removes Tiny Tapeout's missing headcount, and four named comparability defects are in [`analyses/designs-per-head.md`](analyses/designs-per-head.md). **The 29.7× MOSIS/CMC ratio is the weakest cell and must not be cited until `PRD-*` reports** — CMC also runs tool licensing, training and labs, so its denominator may be wrong. Separately, MOSIS still needed ≈$3.0m/yr of facility-and-staff money against a $400 ticket: that is a pricing failure, not a productivity failure, and the two must not be conflated
  - FUND-9 (**corrected — see FUNDX-1**): CMC's audited statements put payroll at **39.3%** of all spending, not the 54.8% read off a single fund's pie chart, and the share is **falling** (53.5% in 2008 → 39–46% across FY2022–26) (CMC 53.5% in FY2008, 54.8% in FY2026). H6 assumes per-customer engineering away; it does not assume away the payroll that a service of this kind actually runs on
  - FUND-2: Europractice's EU subsidy is **EUR 2,801 per design** over 2016-07 → 2025-09 (EUR 19,024,797.50 for 6,791 designs, stable at EUR 2,840 / 2,663 / 2,951 across three separate competitive grants), rising to **EUR 5,309 per design** at the grant rate now running — against SMB-7's EUR 5,478 cheapest commercial ticket
- **PAY-4: Tiny Tapeout's best-documented shuttle earned $16,600.** TT04 ran ten weeks, drew 143 projects from over 30 countries, and sold 235 tiles and 97 boards — against a chipIgnite slot costing $9,750 at the time. **PAY-6** puts the whole programme at roughly $0.6m–$1.0m of gross revenue over five years
  - **PAY-8: chipIgnite's best year was $1.56m gross, and the company died four months later.** **PAY-10** adds the last financing: $2.5m of *debt* from a single investor on 2024-09-27, with the Form D's revenue box marked "Decline to Disclose"
  - **PAY-9, PAY-6: 71% of the sector's 2026 money comes from about fifty orders a year** at $7,000–$15,000 each; the remaining 29% comes from 1,358 Tiny Tapeout designs at €70–€400. The long tail is real in headcount and nearly absent in money — which is `CONC`-style concentration at the bottom of the market, as `OPG-11` also found at IHP
- **Mixed:** SMB-2 (profitable, but the margin trend and the strategy both run away from the tail); SMB-5 (self-sustaining for forty years, but its successor's stated goal is to "achieve self-sustainability within the next few years").
- **Needs:**
  - A fab's own margin by customer size. Still not public anywhere; SMB-1 to SMB-6 are analogues. **FUND-7 is a genuine measurement of customer cost-recovery, but of a broker rather than a fab.**
  - Europractice's **turnover**. The subsidy is now exact but the total cost is not computable, because turnover is unpublished: the public price list and design count bound fabrication billings only to EUR 2.3m–14.5m/yr, a factor of six. The document that would settle it is imec's Certificate on the Financial Statements (Form C) for a Europractice grant, or its accounts with a Europractice segment note (FUND-2).
  - For MOSIS, **nothing is computable**: no budget, no revenue line, no staff count and no year for the claimed "$10M at peak" exists anywhere public (FUND-5, FUND-6).
  - What share of Xometry's revenue comes from its 1,760 accounts spending over $50,000 — not disclosed, and without it nobody can say how much of its revenue is long tail (SMB-3).
  - The academic cost-to-serve literature. Kaplan and Narayanan (2001) could not be obtained legally; **the widely repeated "20% of customers generate 150–300% of profits" figures must not be quoted in this project until someone with library access checks them.** See [`demand/search-log.md`](demand/search-log.md).

## H7. Many small customers reduce risk and remove buyer power

**Claim.** With thousands of small customers, none has leverage, and losing any one of them is noise.

**Status: Supported where it has been measured, but it needs far more customers than assumed.**
The previous status line — "well supported as the reverse of H2" — was wrong, and the PCB evidence
is what corrected it. A long customer *list* does not produce a long-tailed *revenue* distribution.

Among audited PCB makers, customer count and revenue concentration are close to unrelated below
about a million customers: 四会富仕 (Sihui Fushi) with **595** customers has 19.36% of revenue in
its top five, while 迅捷兴 (Xunjiexing) with **over ten thousand** has **40.07%**, Hikvision alone
at 12.58%. Five companies
spanning 595 to 20,000 customers all sit between 13.8% and 40.1%. Only JLC, at **1,358,700** paying
users, reaches 1.16% (PCB-1, PCB-5, SMB-1).

**But that threshold is a PCB artefact and does not transfer to a fab** (corrected 2026-09-19; see
[`analyses/customers-needed-to-fill-a-fab.md`](analyses/customers-needed-to-fill-a-fab.md)). It was
derived from a business whose long-tail customer buys about five boards. A customer buying 100
wafers a year is worth roughly **285×** a JLC long-tail customer, so **7,000 such customers fill
about 700,000 wafers a year — 58,333 wafer starts per month, roughly GlobalFoundries Fab 8 scale** —
and 7,000 similarly-sized customers give a top-five share of **0.07%**. What drives the PCB
threshold is *inequality of order size*, not customer count.

**The real open question is therefore whether a fab's customers would be similarly sized.** If
annual wafer demand is itself long-tailed, concentration returns at once and H7 is back in
difficulty. The distribution of annual wafer volume across a real mature-node fab's customer book
is now the single most valuable piece of evidence this project could obtain.

Where it has been measured directly, though, it holds well.

- **Supports:**
  - FIN-1 (Porter: buyers are powerful when few, or when large relative to the seller)
  - **Effective number of participants** (reciprocal Herfindahl, as a share of nominal count), computed for the first time: **14.4% for Tiny Tapeout designers against 2.3% for TSMC customers** — 1.3% on the correlated-tail variant. Bootstrap CI [8.4%, 36.2%], robust to dropping the largest participant ([`analyses/data-cuts-and-statistics.md`](analyses/data-cuts-and-statistics.md))
  - SMB-1: JLC's top five customers are **1.16%** of revenue, and its largest is 0.28%
  - OIM-2: Reliance — 125,000 customers, 4.6 million orders, a **$3,120** average order, and a largest customer at **0.6% of sales**. A second audited data point for extreme dispersion beside JLC's 0.28%
  - **PCB-8: concentration rises with order size inside a single company.** 金百泽 (Jinbaize) prints top-20 customer concentration separately for each order-size tier: **28.50%** (sample) → **37.56%** (small batch) → **52.25%** (medium batch), monotonic in all three years. Nothing else in the directory measures concentration and order size on the same customers in the same firm — this is H7's mechanism observed directly rather than inferred across companies
- **Leads:** FIN-7 (countervailing-power theory), FIN-9 (diversification theory).
- **Challenges:**
  - PCB-5, PCB-3: customer count does not predict concentration below ~1M customers (above)
  - FIN-5 (Partial): enterprise concentration can bring efficiencies and stickiness

## H8. Openness is necessary to attract many small customers

**Claim.** Published prices, visible queues and public results let people try without asking permission, which is what grows the customer base.

**Status: Argued; the open-and-commercial quadrant is populated but untested at scale.**
The audit in [`analyses/open-access-audit.md`](analyses/open-access-audit.md) scored every programme
on two separate axes — *is access genuinely open*, and *is this a commercial entity trying to profit* —
because conflating them had been hiding the finding.

**The "genuinely open AND genuinely commercial" quadrant is not empty. It has four members:
wafer.space, Tiny Tapeout, Efabless chipIgnite and ChipFoundry.io.** But the whole quadrant is
plausibly **US$1–3M of annual revenue worldwide**, against MOSIS — a *university* brokerage on
*closed* PDKs — at "up to $10 million annually at its peak" thirty years ago. It is populated and
has never been tested at scale.

**A different cell is empty: open, commercial, AND independent of a subsidised PDK has no members
at all.** All four run on SKY130, GF180MCU or SG13G2 — kits that exist because Google paid SkyWater
and GlobalFoundries, and a German federal project paid IHP. **No private actor has ever paid to open
a PDK.**

What the audit found actually predicts behaviour:
- **Eligibility rules predict who shows up.** Europractice's rules define its population and its
  composition matches exactly (69% universities, 9% industry); Google's rules were facts about a
  repository, and 60% of its designs came from non-IC experts.
- **PDK redistributability predicts what third parties can build** — the only criterion that
  predicts a rate rather than a composition.
- **Published prices predict almost nothing.** See the challenges below.

- **Supports:**
  - SW-2: AWS S3 launched with published, pay-as-you-go pricing and no minimum fee
  - ACC-6: Apache-2.0 on all four open kits
  - ACC-9: machine-checkable requirements, as against facts about who you are
  - ACC-7, ACC-3: self-serve routes in the open-and-commercial quadrant
  - FUND-3: a completely public, flat, four-tier membership fee schedule with no negotiation has existed for decades — **but it raises EUR 557,500/yr against a EUR 3,997,727.50/yr subsidy, about one seventh.** Europractice's own *Activity Report 2025* says the fees "pay for extra staff supporting this requested stimulation activity for academic institutions (not fully paid by the EC)" 
- **Challenges:**
  - ACC-5: the TSMC University FinFET Program publishes prices to the euro and is closed on six
    other criteria — "Applications will be reviewed and approved by TSMC, after which an NDA will be
    shared"
  - ACC-10: MEMSCAP published MUMPs prices, a run schedule and redistributable design rules,
    commercially, for **thirty-one years** on a closed process, and reached "Over 80 full process
    runs" at 3–4 a year. Transparency without an open PDK bought longevity, not scale
  - ~~ACC-8: the AFRL/AFWERX design challenge drew 82 designs in 45 days, 1.82/day against Google's
    first open shuttle at 1.50/day, so a closed, gate-kept programme out-drew the open one per day of
    window.~~ **Withdrawn 2026-09-19.** The primary sources were found (`ACC-15`, `ACC-16`): phase 1
    ran **78 days**, not 45; what was submitted was a **business plan with a block diagram**, not a
    design (`ACC-13`); **ten of the 82 were selected** (`ACC-14`); Google's MPW-1 window was **99
    days**, not 30 (`OPG-20`); and at 1.05 proposals a day the AFRL rate is beaten by **four of the
    six Google shuttles with a recoverable window**, the fastest by 3.3×. MPW-1 was the only one it
    beat, and MPW-1 is the one the audit chose. Entry to the AFRL challenge was free and there was
    **no prize** — "no guarantees, no prizes and no contracts". See the audit §6.5
  - ACC-1: even the most open programme retains a discretionary right of refusal and a full
    ITAR/OFAC regime
  - §6.1 of the audit: the sector is smaller today than MOSIS was in 1995 — **and `PAY-6` to `PAY-9` now confirm it bottom-up**: the three paying programmes together took $312k (2021), $519k (2022), $949k (2023), **$1.73m (2024)**, $931k (2025) and $1.37m in the first 8.6 months of 2026, or about **$1.9m annualised**, against `SMB-5`'s MOSIS at "up to $10 million annually at its peak" in 1990s money
- **Openness is not a ratchet:** three closings to one opening. MOSIS 1.0 published a price formula
  to the dollar and MOSIS 2.0 publishes none; MUMPs went to zero when its page 404'd in 2023;
  Europractice's eligible-country list lost Belarus and Russia. Only IHP became more open.
- **Needs:** any case of an open-and-commercial programme operating above roughly $10M/yr.

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

**Status: Contested. The one distribution we can actually measure is not extreme.**
Fitting the Tiny Tapeout per-designer distribution — the only per-designer data in this project —
a Clauset–Shalizi–Newman test **rules out a power law** at k_min = 1 and 2 (goodness-of-fit
p = 0.000); it survives only above four designs, which is 3–4% of designers, and a Vuong test
against a lognormal is inconclusive. **Gini is 0.356**, milder than household income. The skew H10
assumes is real in venture returns and open-source contribution (SW-3, SW-4), but it is *not* what
the one measurable chip-design population shows. Any claim in this project that the distribution is
a power law should be struck.

- **Supports:**
  - SW-3: 96% of open-source value created by 5% of developers
  - SW-4: 55% of venture-backed start-ups terminated at a loss, while 6% produced about half the gross return
- **Challenges:**
  - The Tiny Tapeout distribution is not a power law, and Gini is 0.356 (above; see
    [`analyses/data-cuts-and-statistics.md`](analyses/data-cuts-and-statistics.md))
  - 73.6% of designers make exactly one design ever, so most "attempts" have no second attempt
    behind them to be paid for

## H11. Markets and insurance can replace foundry judgement

**Claim.** Prices set by customers, insurers and futures providers can replace the foundry's own decisions about maintenance, risk, timing and priority (`PRINCIPLES.md` P3).

**Status:** Untested. So far the evidence is our own analysis, not outside sources.

- **Analyses:**
  - [`analyses/critical-review-of-principles-v0.10.md`](analyses/critical-review-of-principles-v0.10.md): incentive and mechanism flaws found
  - `AUCTIONS.md` at the repository root: worked comparison of auction styles
- **Challenges:**
  - **IHF-5: the only operator found of a real many-small-jobs fab does the opposite of P3.** Science
    Foundry schedules with a central optimiser and fab-assigned priority — "If it appears like a job
    might be off track, it is given a higher priority" — not prices, bids or a market, and describes
    the problem as "practically unsolvable" by inspection, with "more than 80 advanced tools,
    hundreds of distinct protocols, and a mix of development and production jobs each made up of
    hundreds of separate steps"
- **Context (Lead):** FIN-8, hold-up theory. General machine time sold on a market reduces relationship-specific investment.
- **Needs:** literature on electricity markets, spectrum auctions, reinsurance and catastrophe bonds, and exchange clearing houses.
