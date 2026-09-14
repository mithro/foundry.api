# Hypotheses

These are the claims foundry.api depends on, stated so they can be tested. For each one, the evidence is listed below it, split into what supports it, what challenges it, and what is still an unverified **Lead**. Reference IDs point to entries in [`references/`](references/).

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

**Status:** Argued. The general long-tail evidence is contested. Chip-specific evidence of latent demand is thin.

- **Supports:**
  - TAIL-1: Anderson's long tail
  - TAIL-2: the value of wider choice in books
  - OPEN-5: 174 submissions to one Tiny Tapeout round
  - CONC-2, CONC-11: TSMC's customers outside its top ten (512 in 2024, 524 in 2025) share a fifth to a quarter of revenue
- **Challenges:** TAIL-3, Elberse finds hits still dominate and consumers in the tail rate niche titles lower.
- **Needs:** chip-specific data on latent demand, such as shuttle waiting lists, university and startup tape-out counts, or multi-project wafer programme growth.

## H6. Small customers can each be profitable

**Claim.** If the fab does no per-customer engineering and sells machine time at published prices, each small customer is profitable.

**Status:** Argued.

- **Context:** SW-5 (Verified), where on AWS small on-demand buyers pay more per unit than committed buyers. That supports small customers paying a premium for flexibility.
- **Challenges:** OPEN-7, Efabless's failure, though it was an intermediary and not a fab.
- **Needs:** cost-to-serve data for multi-project wafer and shuttle programmes, and foundry service margins by customer size.

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
