# Critical review of `PRINCIPLES.md` Draft v0.10

| | |
|---|---|
| Item | Adversarial review of `PRINCIPLES.md` Draft v0.10 by an independent reviewer sub-agent |
| Date | 2026-09-13 |
| Scope | Contradictions, conflicts between principles, economic and incentive flaws, gaps, arithmetic, cross-references, clarity, and the accuracy of the claims about `DESIGN.md` |
| Status checked against | `PRINCIPLES.md` Draft v0.12 and `AUCTIONS.md` Draft v0.1 |

This page records the review's main findings and what has happened to each since, so they are neither lost nor re-litigated. Finding IDs (A1, B1, …) are the reviewer's.

**Status labels:**
- **Resolved:** changed in a later draft.
- **Decided:** the owner considered it and deliberately kept the design.
- **Open:** not yet addressed.

## A. Defects

| ID | Finding | Status |
|---|---|---|
| A1 | The I11 worked example was wrong: one 45-minute sale didn't protect the exposure that followed it | **Resolved** in v0.11. The one-sale option now covers the wait and the exposure. |
| A2 | The foundry recovering costs "from whoever caused it" contradicted "the foundry never decides cause" | **Resolved** in v0.11. Costs go through damage cover and the foundry's backstop insurance (I16). |
| A3 | "Pay for actual time" (P4, I5, S7) contradicts "pay for the time you bought" (I11, I12, Q6) | **Open.** P4 still says "actual time it holds", and its explanation says "pays for the time they buy". Tracked as Q4 and Q6. |
| A4 | S9 lets an overrun take time from someone else's sale, which I11 and I14 forbid | **Open.** Tracked under S16 and Q6. |
| A5 | P4 builds in a working assumption (reading (a)), and "whatever the outcome" was false when insurers fail | **Partly resolved** in v0.11: the backstop insurance covers failed guarantees. Reading (a) is still in the principle text (Q14). |
| A6 | P3's "closed list" leaves out storage, inspection, disposal, formula bids, performing maintenance and wafer transport | **Open.** |
| A7 | P5's "pays most" disagrees with ranking by rate; there's no tie-break, and arrival order is ruled out | **Open**, tracked as Q16 and worked through in `AUCTIONS.md`. |
| A8 | I12 arithmetic was wrong (+70 should have been +75 minutes) | **Resolved** in v0.11 (15 minutes unused, 195 cr net). |
| A9 | Refunds were undefined for resold time that the foundry couldn't provide | **Open.** |
| A10 | The order table stated the broker question as settled, while four other places called it open | **Resolved** in v0.11 (marked open, Q12). |
| A11 | P2 still mentioned "plans", and whether provider contracts were public was undefined | **Resolved** in v0.11. "Plans" was removed, and P2 now covers every participant. |
| A12 | The order table's claim that every row rests on a real conflict is overstated; the P3-over-P4 row isn't a conflict | **Open.** |
| A13 | Setup and cleanup attribution is inconsistent with S14 | **Open** (Q11). |
| A14 | Who may buy maintenance, and whether it must be carried out, is settled in one place and open in another | **Open** (Q9). |
| A15 | Several `DESIGN.md` citations were inaccurate, and some conflicts were missed | **Resolved** in v0.12. The table moved into `DESIGN.md` Appendix C, with corrections and the missed conflicts added. |

## B. Design weaknesses

| ID | Finding | Status |
|---|---|---|
| B1 | Ranking by rate with runner-up pricing, plus public live bids and futures that must win, lets a cheap short bid force a huge price on a long winner (the example is 50,000 cr) | **Open.** `AUCTIONS.md` compares seven auction styles on this case. The mechanism is undecided (Q16). |
| B2 | A fully hedged foundry has no reason to operate well | **Decided** (v0.11): the foundry should take whatever operating risk pays after insurance, and insurers price that risk (I4). |
| B3 | The downtime insurer, which decides maintenance, doesn't bear scrap, drift, or the price effects after maintenance | **Decided** (v0.11): the downtime insurer is meant to bear the consequences of delaying maintenance, including effects on customers (working reading in I14). Policy-term distortions are noted. |
| B4 | Choosing the insurer is unacknowledged discretion, and an affiliated insurer could hide a markup | **Open.** |
| B5 | The floor and subsidy formulas need forecasts from a foundry that is forbidden to forecast | **Decided** (v0.11): formulas use market prices from insurers and futures providers in place of forecasts. |
| B6 | Payment guarantees cover time but not damage, so a throwaway account can wreck a furnace | **Resolved** (v0.11): every job carries damage cover, and the foundry holds backstop insurance (I16). |
| B7 | No one is named to resolve disputes, and the foundry measures its own billing | **Open.** |
| B8 | Operators, wafer transport, staging lead time, shared utilities and recording outages don't fit "machine N for X hours" | **Open.** |
| B9 | "Breaks the law" in P1 creates private information, and may force judgements about intent | **Open** (Q3). |
| B10 | In-fab storage is scarce but not auctioned | **Open.** |

## C. Challenges to the owner's decisions

The reviewer challenged these decisions. They're recorded for later consideration; none of them has changed a decision yet.
1. Futures should have a cap rather than being must-win.
2. Deductibles, or liability cover by default, would keep the foundry's incentive to operate well.
3. A published engineering rule may decide maintenance better than insurer-bought hours.
4. Law should be separated from safety in P1.
5. The P3 exceptions should be accepted now, with governance.
6. Bids should be published only once a clearing is final.

## How it bears on our hypotheses

- **H11, markets and insurance can replace foundry judgement.** The review is the main evidence so far, and it's cautionary. Several of its weaknesses (B1, B4, B7, B8) are places where "no discretion" either needs a mechanism nobody has designed yet, or quietly relies on someone's judgement.
