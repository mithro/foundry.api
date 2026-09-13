# foundry.api — Auction and bid styles (Draft v0.1)

| | |
|---|---|
| Status | Draft v0.1. A comparison, not a decision. |
| Date | 2026-09-13 |
| Principles | Governed by `PRINCIPLES.md` Draft v0.12, which leaves the auction mechanism open (Q16). Principles are cited by number and name: **P1** Do no harm, **P2** Everything is recorded and public, **P3** The foundry does as little as possible, **P4** Every hour is paid for, **P5** Money decides, **P6** Run what is asked. |

This document works each candidate way of running the auction through the same three cases, and lists the pros and cons of each. It doesn't recommend one: the choice needs simulation. All numbers were computed by a script, not by hand.

---

## 1. What any style has to satisfy

- **P2:** bids and clearings are public (either live, or once a clearing is final if that counts as public, Q10), and every clearing can be reproduced exactly from the record.
- **P3:** the foundry has no discretion in clearing. The rules are published.
- **P4:** a winner's payment is guaranteed before its time starts. The candidate unit of sale is "machine N for X hours at rate Y" (I11), and unused time can be sold back (I12).
- **P5:** nothing but money decides who wins. Ties can't be broken by arrival order.
- **P6:** each customer chooses how long to bid for (X), and any conditions on their bid.

---

## 2. The three cases

In every case the machine is free now, the floor is 50 cr/h, and every bid is funded.

| | Bids |
|---|---|
| **Case 1. Ordinary demand** | A: 10 h at 100 cr/h (a long run). B: 2 h at 120 cr/h. C: 0.1 h (6 minutes) at 300 cr/h (a short, urgent job). |
| **Case 2. A spoiler against a future that must win** | A: a futures provider that must win the next 10 hours whatever it costs (I1). B: 2 h at 120 cr/h. C: 0.1 h at 5,000 cr/h, a bid C doesn't mind losing (its guarantee only needs to cover 500 cr). |
| **Case 3. A griefer** | C: really wants 0.1 h, and bids 5,000 cr/h. D: bids 0.1 h at 4,900 cr/h, only to make C pay more. |

---

## 3. The styles

### Style 1. Pay your own bid, highest rate wins (first price)

**How it works.** The highest rate wins the next sale, for the hours it asked for, and pays its own rate for them.

- **Case 1:** C wins and pays 30 cr, then B pays 240 cr, then A pays 1,000 cr. The foundry receives 1,270 cr. That assumes bidders bid their true value, which in a first-price auction they won't (see cons).
- **Case 2:** to win now, A must bid just over 5,000 cr/h, and pays about 50,000 cr. If A's future lets it wait 6 minutes while C's sale runs, A only has to beat B afterwards (just over 120 cr/h) and pays about 1,200 cr. If C wins, C really pays 500 cr for its 6 minutes.
- **Case 3:** bids are public, so C must bid just over D's 4,900 cr/h and pays about 490 cr, where it would otherwise have paid about 5 cr. But D takes a real risk: if C withdraws, D wins and pays 490 cr.

**Pros**
- A losing bid never sets anyone else's price.
- Spoiling works only if the spoiler is willing to win and pay.
- A bid's guarantee is simply its own bid.

**Cons**
- Bidders shade their bids below their true value and watch the queue, re-bidding constantly.
- With live public bids, everyone bids just above the visible competition, so what the foundry earns depends on who happens to be watching.
- A future that must win is still exposed to high bids that are credible.

### Style 2. Pay the runner-up's rate for your own hours (second price on rate)

**How it works.** The highest rate wins. It pays the runner-up's rate, or the floor if there is no runner-up, for its own hours. This is what earlier drafts of `PRINCIPLES.md` I11 assumed.

- **Case 1:** C pays 12 cr (B's rate), B pays 200 cr (A's rate), and A pays 500 cr (the floor). The foundry receives 712 cr.
- **Case 2:** A wins and pays 5,000 × 10 = 50,000 cr. C pays nothing.
- **Case 3:** C pays 490 cr, where it would pay 5 cr without D. D pays nothing. If C withdraws, D wins at the floor and pays 5 cr.

**Pros**
- Each bidder can simply bid its true value once.
- Little re-bidding.
- Well understood for selling single items.

**Cons**
- A short, high-rate losing bid sets the price for every hour of a long winner (Case 2). The damage has no limit and costs the spoiler nothing.
- Griefing (Case 3) is almost free.
- Live public bids make targeting easy.

### Style 3. Pay what you displace, hour by hour (second price per covered hour)

**How it works.** The highest rate wins. For each part of its hours, the winner pays the highest competing rate among bids long enough to have covered that part, or the floor. This is a simplification of the idea behind Vickrey–Clarke–Groves (VCG) pricing, which charges each winner the value its win takes away from everyone else.

- **Case 1:** the same as Style 2. The foundry receives 712 cr.
- **Case 2:** A pays 500 cr for the first 0.1 h (C's 5,000 cr/h), 228 cr for the next 1.9 h (B's 120 cr/h), and 400 cr for the last 8 h (the floor): 1,128 cr in total.
- **Case 3:** C pays 490 cr, the same as Style 2, because C's and D's bids are the same length.

**Pros**
- A losing bid can only raise the winner's price for the hours it asked for. The damage is limited to what the spoiler's own guarantee covers (500 cr in Case 2).
- Bidders can still bid their true value per hour.

**Cons**
- Harder to explain.
- Griefing between bids of the same length is still free (Case 3).
- "Bids long enough to cover that part" ignores bidders who could have started later. Full VCG pricing needs the best alternative schedule, which is exactly the lookahead P3 forbids the foundry.

### Style 4. Highest total wins (hours × rate), pay your own bid

**How it works.** The bid with the highest total value (hours × rate) wins, and pays its own bid.

- **Case 1:** the totals are A 1,000 cr, B 240 cr and C 30 cr, so the order is A, B, C. C's urgent 6-minute job waits 12 hours, even though it offers 300 cr/h. The foundry receives 1,270 cr.
- **Case 2:** A only needs a total above C's 500 cr, so it bids just above the floor and pays about 500 cr. The spoiler has no effect.
- **Case 3:** the bids are the same length, so this is the same as Style 1: with D visible, C pays about 490 cr.

**Pros**
- A short spoiler can't move a long bid.
- A future that must win is cheap to honour.

**Cons**
- Long bids at low rates beat short, valuable ones.
- A hog bidding 100 hours at just above the floor (a total of about 5,001 cr) beats every bid in Case 1 and locks the machine for 100 hours at nearly the floor rate.
- Needs a maximum X or some other limit, which is a rule someone has to set (P3).

### Style 5. Fixed-length increments (for example, every sale is 15 minutes)

**How it works.** Time is only sold in equal increments, each auctioned just before it starts, and a longer run has to win consecutive increments. Shown here with second price per increment.

- **Case 1:** C wins the first increment and pays 30 cr (B's rate for 15 minutes), for a 6-minute job; it can sell back the other 9 minutes (I12). B wins the next 8 increments and pays 200 cr (A's rate). A wins the last 40 and pays 500 cr (the floor). The foundry receives 730 cr.
- **Case 2:** A must win 40 increments. It pays 1,250 cr for the first (against C), 210 cr for the next 7 (against B), and 400 cr for the remaining 32 (the floor): 1,860 cr in total.
- **Case 3:** C's 0.1 h rounds up to one increment, so C pays 4,900 cr/h × 0.25 h = 1,225 cr.

**Pros**
- Every bid compares like with like, so there is no manipulation across bids of different lengths.
- Simple to display.

**Cons**
- A running job has to win every next increment while its wafers are in the machine. A rival bidding 1,000 cr/h for each next increment costs it 250 cr per increment, or ruins the run. That is a hostage problem.
- Preventing the hostage problem means giving a running job a claim on its next increments, which is priority by something other than money (P5). The alternative is pre-buying all the increments, which turns this back into Styles 1–4 with a long X.
- Short jobs pay for minutes they don't use.
- Many more auctions.

### Style 6. Ascending clock (English auction)

**How it works.** A public rate per hour rises. Bidders, each with their own X, drop out as it passes their limit. The last one left wins its X at the rate where the second-to-last dropped out.

- **Case 1:** if bidders stay in up to their true rates, this is the same as Style 2. The foundry receives 712 cr.
- **Case 2:** A never drops out. C knows A must win, so C can keep pushing the price up with no risk. A pays at least 50,000 cr, and more if C keeps going.
- **Case 3:** D stays in until 4,900 cr/h, and C pays 490 cr. D risks C dropping out first, in which case D wins at 4,900 cr/h.

**Pros**
- Transparent price discovery, which suits P2.
- Bidders can see why they lost.

**Cons**
- A bidder that must win can be pushed up without limit.
- Every clearing takes time.
- Bots and fast connections have an advantage.
- Has the same problem as Style 2 with bids of different lengths.

### Style 7. Descending clock (Dutch auction)

**How it works.** The rate starts high and falls. The first bidder to accept wins its X at the current rate.

- **Case 1:** each bidder accepts somewhere at or below its value. Strategically this is like Style 1.
- **Case 2:** A must accept before the rate falls to 5,000 cr/h, where C might accept, so A pays about 50,000 cr. If the clock starts higher and A doesn't know where C would accept, A accepts sooner and pays more.
- **Case 3:** D can only affect C by actually accepting first, which means winning and paying 490 cr.

**Pros**
- Griefing requires actually winning.
- Fast.

**Cons**
- The same bid shading as Style 1.
- Races to accept at the right moment.
- A future that must win is still expensive.

---

## 4. Modifiers that work with any style

- **Sealed until cleared.** Bids are recorded but published only when the clearing is final. This stops targeted spoiling (C can't see that A must win), and griefing that needs to see the leader (D). It doesn't stop a standing high bid for a short time. It is only allowed if "public once cleared" satisfies P2 (Q10), because P2 outranks P5.
- **A fee per bid.** Every bid, winning or losing, pays a small fee, so spoiling and griefing cost something (P4).
  - *Con:* it discourages honest bids.
  - *Con:* the fee is a rule someone has to set (P3).
- **Futures that don't have to win at any cost.** A future can carry a cap on what the provider will pay, or a window (for example "within 15 minutes of T") so the provider can let a short spoiler go first. In Case 2 under Style 1, that cuts A's cost from about 50,000 cr to about 1,200 cr. This changes the futures side, and helps every style.
- **Guarantees scaled to impact.** A bid's guarantee covers the most it could raise anyone else's price, as well as what it would pay if it won. Style 3 already limits that impact to the bid's own hours.

---

## 5. Summary

| Style | Case 1: foundry receives | Case 2: must-win A pays | Case 3: C pays, with D griefing | Can a losing bid raise someone else's price? | Main weakness |
|---|---|---|---|---|---|
| 1. Pay own bid, by rate | 1,270 cr (before shading) | about 50,000 cr (about 1,200 cr if A may wait) | about 490 cr; D risks winning | No, but visible bids force outbidding | Shading and re-bidding |
| 2. Runner-up's rate, own hours | 712 cr | 50,000 cr | 490 cr; D risks nothing | Yes, without limit | Spoiling across bid lengths |
| 3. Per covered hour | 712 cr | 1,128 cr | 490 cr; D risks nothing | Yes, but only for the loser's own hours | Complexity; griefing between equal lengths |
| 4. Highest total, pay own bid | 1,270 cr (C waits 12 h) | about 500 cr | about 490 cr; D risks winning | No | Long low-rate bids hog the machine |
| 5. Fixed 15-minute increments | 730 cr | 1,860 cr | 1,225 cr | Yes, per increment | Hostage problem mid-run |
| 6. Ascending clock | 712 cr | at least 50,000 cr, with no limit | 490 cr; D risks winning | Yes | A bidder that must win can be pushed without limit |
| 7. Descending clock | similar to Style 1 | about 50,000 cr | 490 cr, only if D accepts and pays | No | Shading and races |

---

## 6. Observations so far

These are observations, not recommendations.

1. **The biggest exposure comes from three things together:** ranking by rate across bids of different lengths, bids that must win at any cost, and live public bids. Removing any one of them reduces it sharply: pricing per covered hour (Style 3) or ranking by total (Style 4), futures with caps or windows, or sealing bids until cleared.
2. **Losing bids are free in second-price styles.** There, a losing bid can set someone else's price at no cost (Case 3). First-price and descending styles make that cost something, at the price of bid shading and constant re-bidding.
3. **Fairness between short and long jobs pulls against spoiler resistance.** Ranking by rate favours short urgent jobs but exposes long ones. Ranking by total protects long jobs but lets them hog the machine.
4. **Fixed increments swap one problem for another:** manipulation across bid lengths for a hostage problem during a run.
5. **Every style still needs two rules:** a published tie-break that isn't arrival order (P5), and a rule for runs that take longer than the X they bought (`PRINCIPLES.md` S16).

---

## 7. Next steps

- **More styles to compare:**
  - bids for several consecutive sales at once
  - a uniform clearing price across a batch window
  - clearing at fixed times rather than whenever a machine frees
- **Simulation:** run each style with bot bidders (truthful bidders, bid shaders, spoilers, griefers, futures providers that must win, and hogs). Measure foundry income, cycle time by customer size, and the cost of each attack.
- **Decisions:** settle `PRINCIPLES.md` Q16 and Q10 from the results.
