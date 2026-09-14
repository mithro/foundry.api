# Assessment: "The Tyranny of the Whale" investor brief

| | |
|---|---|
| Item | "The Tyranny of the Whale: Why the World's Most Advanced Factories Are Hostage to a Handful of Customers — and Why Many Small Customers Would Be Better" |
| Where | Public Claude artifact: <https://claude.ai/public/artifacts/6633a222-4b09-4967-b923-b6cc9ceb1101> |
| Kind | Research brief for investors, "written in the style of a business-magazine feature". The page is labelled "Content is user-generated and unverified". |
| Read | 2026-09-13, in a logged-in Chrome session. The page blocks automated fetchers and headless browsers. |
| Assessed by | Claude, for foundry.api |

## What it argues

The brief looks at the same problem as `WHY.md`, from the investor's side:
- **Concentration.** A few "whale" customers dominate foundry revenue. It gives TSMC's top ten at 76% in 2024, and Nvidia and Apple together at about 36% in 2025.
- **What whales take.** They capture most of the value per wafer, dictate prices, pre-book scarce capacity, and can threaten to leave.
- **The foundry's exposure.** Meanwhile the foundry carries fabs costing more than $30B, 2–3 year build times, and high fixed costs.
- **Cost of capital.** Customer concentration measurably raises a supplier's cost of equity and debt and worsens its loan terms. That makes the next fab more expensive to finance, a second spiral inside ours.
- **The alternative.** A "many small customers" model, as in SMB software and cloud pricing, is more defensible. It diversifies demand, restores pricing by segment, and removes hold-up.
- **Counter-evidence it states itself.** Patatoukas (2012) finds that concentration can bring efficiencies, and enterprise customers are stickier.

## Cross-check against what we have verified

| Claim in the brief | Our status | Reference |
|---|---|---|
| TSMC top ten 68% / 70% / 76% (2022–24); largest 23% / 25% / 22% | **Verified**, matches the 20-F exactly | CONC-1 |
| TSMC serves 500+ customers | **Verified**: 522 in 2024 | CONC-2 |
| 2025: Nvidia 19%, Apple 17% of TSMC revenue | **Lead**: check the 2025 20-F | CONC-11 |
| TSMC held 69.9% of foundry revenue in 2025 | **Lead**. We verified 70.4% for Q4 2025, a different period, not a conflict. | CONC-12 |
| GlobalFoundries abandoned 7nm in 2018 | **Verified** | COST-4 |
| AMD paid GF $320M + $200M (2012) and $100M (2016) to loosen its supply agreement | **Lead** | CONC-8 |
| Huawei was 10–15% of TSMC's business in 2019 | **Lead** | CONC-13 |
| Nvidia booked more than 70% of 2025 CoWoS-L capacity | **Lead** | CONC-9 |
| Apple's "known good die" deal | **Partial**: reported, then disputed. The brief notes the dispute. | CONC-7 |
| Nvidia gross margin 75.0% against TSMC's 53–62% | **Lead** | CONC-10 |
| Design cost $416M at 5nm, $590M at 3nm (IBS) | **Partial**. It differs from the IBS figures in Arm's prospectus ($249M at 7nm, $725M at 2nm) because estimates from different years differ. | COST-1, COST-2 |
| TSMC capex from $36.3B (2022) to $52–56B guidance (2026) | **Lead** | COST-7 |
| Porter on buyer power | **Verified** | FIN-1 |
| Dhaliwal et al. (2016), Campello & Gao (2017) on cost of capital | **Lead** | FIN-2, FIN-3 |
| Patatoukas (2012) counter-argument | **Lead** | FIN-5 |
| Irwin & Klenow (1994) learning spillovers | **Verified** (abstract) | LEARN-7 |
| AWS Reserved Instances up to 72% off On-Demand | **Lead** | SW-5 |
| Private-equity thresholds: 15% / 20% / 30% single-customer share; 20–30% valuation discounts | **Unsourced** in the brief. Don't use them. | none |
| Wafer prices from $3,000 (28nm) to $30,000 (2nm) | **Lead**, and the brief itself says these are unofficial channel checks | none yet |

## How it bears on our hypotheses

- **H2, customer concentration damages a foundry.** The brief's biggest contribution is the cost-of-capital mechanism (FIN-2, FIN-3), which `WHY.md` doesn't yet use. It's the argument finance readers will find most convincing. It also adds concrete cases: AMD and GF hold-up, the Huawei cut-off, CoWoS pre-emption.
- **H6, small customers can each be profitable.** Its "small buyers pay more per unit" point (cloud on-demand against reserved pricing; shuttle prices per mm²) is presented as a disadvantage for small customers. For an open fab it's the business model: flexible customers pay a premium. `WHY.md` should say this explicitly so readers of both documents don't see a contradiction. It also fits `PRINCIPLES.md` P5, "every preference costs money".
- **H7, many small customers reduce risk and buyer power.** Supported by the brief's theory (FIN-7, FIN-9) and challenged by its own counter-evidence (FIN-5). `WHY.md` §6 doesn't yet address the stickiness and efficiency of large customers.
- **H9, many small, public experiments make a fab learn faster.** It cites Irwin & Klenow (LEARN-7). That paper's finding of real spillovers between chip firms challenges `WHY.md` §5's claim that one team's learning "adds little" to anyone else's.

## Gaps in the brief

- **No alternative.** It argues that many small customers are better, but gives no mechanism for how a foundry could get them. That's the gap `WHY.md` and `PRINCIPLES.md` fill.
- **It accepts the premise that NRE has to be high.** It treats small customers as buying multi-project wafer (MPW) space at a high cost per mm² and never questions why that cost is high.
- **The investor view is limited to existing foundries.** It recommends discounting concentrated foundries rather than building differently.

## Follow-ups

Status as of 2026-09-14 (`WHY.md` Draft v0.5):

1. **TSMC 2025 figures.** Done. Verified from the 2025 20-F: the top ten customers rose to 78% of revenue (CONC-11). `WHY.md` is updated.
2. **Finance papers.** Partly done. Dhaliwal et al. and Campello & Gao are verified (FIN-2, FIN-3), and the cost-of-capital mechanism is added to `WHY.md` §3. Patatoukas (FIN-5) is still only Partial, because every accessible copy of the abstract is blocked. The efficiency counter-argument is **not yet** in `WHY.md` §6.
3. **AMD and GlobalFoundries.** Done. Verified from AMD's 2012 and 2016 press releases and 2019 8-K (CONC-8); the seventh amendment was 2019, not 2018. Added to `WHY.md` §3.
4. **Irwin & Klenow.** Done. `WHY.md` §5 now says learning spreads between chip firms "but less than it could" (LEARN-7).
5. **Small customers paying more.** Done. Added to `WHY.md` §6 as an objection, citing AWS's reserved-instance discount (SW-5, now Verified).
