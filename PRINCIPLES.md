# foundry.api — Principles (Draft v0.1)

| | |
|---|---|
| Status | Draft v0.1. Expected to change over several iterations. |
| Date | 2026-09-12 |
| Relationship to `DESIGN.md` | `DESIGN.md` is one attempt to implement these principles. Where the two disagree (§5), change one of them on purpose. Don't quietly work around the gap. |

The principles come first, each in one or two sentences. The rest of the document works out what they mean. §2 covers each principle alone, §3 how they combine, §4 concrete scenarios, §5 where `DESIGN.md` currently disagrees, and §6 what to settle next.

---

## 1. The principles

### The foundry's job

**P1. Run what is asked.** The foundry's job is to run its machines the way customers ask. It does not design processes, judge whether a device will work, or plan anyone's flow.

**P2. Refuse only to protect.** A request is refused only if it would harm people, machines, consumables, shared infrastructure or other customers' wafers. Everything else runs, however unwise.

**P3. Decide only what runs now.** The foundry decides one thing: what each machine does next. Forecasts, reservations, selling future capacity, delivery dates and future prices are the market's job.

**P4. The foundry is just another participant.** When the foundry wants something from its own machines, it bids for it like anyone else. If it sells insurance or futures, it does so on the same terms, and with the same information, as any other provider.

### Money

**P5. Money decides.** If a customer pays enough, their work runs next. Nothing else orders the queue: not customer size, loyalty, deadlines, or how far through a flow a lot is.

**P6. Customers pay for the time they use.** The foundry sells machine time. A customer pays for all of it: setup, processing, cleanup and any time their request holds the machine.

**P7. Every run belongs to one customer.** Nobody shares a run by default. A customer who wants to run things together (sharing a batch, following the same program to skip setup, chaining steps back-to-back) pays to make that happen.

**P8. Everything is priced, including waiting.** Machine time, storage, consumables, shipping and operator time all cost money. Anything left unpriced will be over-consumed.

**P9. The foundry always gets paid.** The foundry is paid for everything it provides, whatever the outcome. Refunds, guarantees and risk belong to insurance and futures, sold by whoever wants to underwrite them.

### Information

**P10. Everything is public.** Everything except credentials is public: machines, queues, bids, prices, ledgers, designs and results. A market can only price what it can see.

**P11. Everything is an event.** Every action by customers, the foundry and machines is a recorded event. What runs now is a deterministic function of those events.

### Precedence

P2 overrides everything: no amount of money buys a run that endangers people or machines. Otherwise the principles should never conflict. If a scenario shows a conflict, a principle is badly worded; record it in §6.

---

## 2. What each principle means

### P1. Run what is asked

- **Means:** the foundry's product is a set of machines, programs and limits, and it runs requests against them. Zero per-customer engineering (NRE) follows from this; it doesn't need to be a separate goal.
- **Means:** the customer makes every judgement about their device: the recipe, whether a measurement is acceptable, whether to continue after a failed check. The foundry measures and reports; it never decides for the customer.
- **Rules out:** yield rules, "are you sure?" checks, foundry-recommended process changes, and the foundry picking the "best" machine beyond what the customer allowed.
- **Open:** who writes new programs. If only the foundry can, the program catalogue is an engineering service (S13).

### P2. Refuse only to protect

- **Means:** every validation rule names what it protects: a person, a machine, a consumable, a shared facility, or the next customer's wafers (through contamination). A rule that only protects the requesting customer's own result is deleted.
- **Means:** protection is checked again just before a run starts, because machines and wafers change.
- **Means:** a protection rule is a limit of a machine, not a judgement about a customer, so it belongs in that machine's declared limits wherever possible.
- **Rules out:** DRC for yield, refusing a safe but pointless request, and refusing because the customer can't "really" want this.

### P3. Decide only what runs now

- **Means:** scheduling is a single decision: when a machine is about to become free, which request gets it. The foundry keeps no plan and no calendar.
- **Means:** the foundry promises nothing about when anything will happen. Cycle time is an outcome of the market, not a commitment.
- **Means:** anything that needs a view of the future (deadlines, delivery dates, secured slots, price forecasts, bidding strategies) is done by customers or third parties. They use public data (P10) and ordinary bids.
- **Rules out:** reservations, calendars, foundry-promised delivery dates, holding a machine idle for an expected better customer, and batching work across time on anyone's behalf.
- **Open:** whether the foundry should publish *any* projections, such as expected start times. They are useful, but they look like promises. Anyone could compute them from public data.

### P4. The foundry is just another participant

- **Means:** the foundry's own preferences are public, priced bids in the same auction. Examples: keeping a furnace hot, clearing a tool before maintenance, refusing to run below cost.
- **Means:** if the foundry sells insurance, futures or credit, it is an ordinary provider with no information other providers lack. Anything it knows that affects prices must be public (P10) before it trades on it: maintenance plans, fault history, upcoming machine changes.
- **Rules out:** foundry-priority jobs, private discounts, hidden floors, and any instrument that lets the foundry or anyone else bypass the auction.
- **Open:** maintenance (S11). Taking a machine down for safety falls under P2 and needs no bid. Choosing *when* to do planned maintenance is an economic decision, and arguably should be a bid.

### P5. Money decides

- **Means:** money is a customer's only way to change the order of the queue. A lot at step 199 of 200 has no claim on step 200; its owner simply has to pay more than anyone else for that slot.
- **Means:** a rival who values stopping you more than you value proceeding can buy the machine's time and leave it idle. That is legitimate, public and expensive.
- **Means:** willingness to pay must be backed by funds; an unfunded bid is not a bid.
- **Rules out:** fairness quotas, first-come-first-served, deadline boosts, protection for small customers, and priority for nearly-finished lots.
- **Open:** whether P5 is compatible with serving thousands of small customers (`DESIGN.md` §2.2). The scenario harness has to answer this (`DESIGN.md` §10.12 H1); rewording won't settle it.

### P6. Customers pay for the time they use

- **Means:** the unit of sale is machine-hours, not wafers, steps or results. A run that needs a changeover costs more than the same run after a compatible one, because it uses more time.
- **Means:** setup belongs to the run that needs it; cleanup belongs to the run that causes it.
- **Means:** time used includes time the machine sits idle while held for the customer, for example an idle bid or a tool waiting for their wafer.
- **Open, and the most important:** is the charge based on *actual* or *modelled* time? With actual time, customers carry machine variability (a long etch costs more), and the foundry doesn't need to certify program durations. With modelled time, the foundry carries the variability, and the price is known when the auction clears. `DESIGN.md` §10.2 uses modelled time (S9).
- **Open:** if a machine fails partway through a run, is only the time up to the failure charged? P6 says yes (S6).

### P7. Every run belongs to one customer

- **Means:** one account is responsible for each run's hours and wafers. A price is never split between strangers.
- **Means:** the foundry doesn't look for combinations such as shared batches, same-program sequences or back-to-back steps. A customer who wants one has to win the slots that create it, or pay someone to arrange it. The saving goes to whoever arranged and paid for it.
- **Means:** a machine that needs a full load, such as a CMP tool, is paid for in full by the one customer using it. Filling the empty positions is that customer's problem.
- **Open:** may a run's owner load wafers belonging to other accounts, with their consent? This is a broker or shuttle (S4). P7 still holds because one account is responsible, but the run's owner and the wafers' owners differ.

### P8. Everything is priced, including waiting

- **Means:** wafers waiting in the foundry pay for storage. A lot whose owner won't pay to proceed costs that owner money every day, so a lot can't sit blocked forever for free.
- **Means:** the price list covers every cost the foundry bears: wear, consumables, operator time, requalification after contamination. A missing price is a defect, because someone will find it and exploit it.
- **Rules out:** free storage, free inspection, free rework, free dummy wafers.

### P9. The foundry always gets paid

- **Means:** the foundry is paid for the time and resources it provides even when machines fault, operators make mistakes, runs fail or customers cancel. Anyone who wants protection from those outcomes buys insurance.
- **Means:** the foundry doesn't need to decide whose fault a failure was. It publishes the evidence (P10), and customers and insurers argue about the cause.
- **Means:** anyone who commits to pay (a customer, a futures provider) must have the funds when the run clears. The foundry handles counterparty risk by requiring funds, not by trusting anyone.
- **Means:** a negative price, where the foundry pays a customer to keep a tool running, is not an exception. The foundry is buying something it values (P4).
- **Rules out:** refunds issued by the foundry, goodwill credits, and the foundry extending credit, except as an ordinary lender under P4.
- **Clarify:** P9 covers only what the foundry *provides*. If nothing was provided, nothing is owed (S7).

### P10. Everything is public

- **Means:** queues, bids, cleared prices, machine states and fault histories are public. Insurers and futures providers can price risk, and customers can see why they are waiting.
- **Means:** public reliability data is what keeps the foundry honest under P9. Insurance on unreliable machines costs more, so customers bid less for them.
- **Rules out:** private contracts with the foundry, confidential designs, hidden floors.
- **Open:** *when* bids become public. Live bids visible before a clearing invite sniping, and bidding just under the leader to raise its price. Publishing bids once the clearing is final may serve P10's purpose without that cost (`DESIGN.md` §10.12 H2).
- **Open:** P10 excludes customers who need confidentiality. That is a deliberate market choice and should be recorded as one.

### P11. Everything is an event

- **Means:** prices, holds, disposals and disputes can be rebuilt and audited from the log, and replaying it gives the same decisions.
- **Means:** anything outside the foundry's control, such as a machine result, an insurer's decision or a callback, enters only as a recorded event.

---

## 3. How the principles interact

**I1. No reservations, only people who pay** (P3 + P5 + P9). The foundry decides only what runs now, and money decides it. So the only way to secure future work is to have someone willing to pay in the auction when the time comes. A **future** is exactly that. A provider agrees to get you a slot at time X for cost Y. When X comes, the provider must win the auction for you, whatever it costs. If the auction is cheaper than Y, the provider keeps the difference; if dearer, the provider covers it. The foundry takes no part in the contract. All it needs is to let one account bid and pay for another account's run.

**I2. Buying ahead means buying time early** (P3 + P6 + I1). A machine's time is sold when the machine becomes free, not when a customer would like to start. A provider who promised a slot later than that has to win the earlier clearing and pay for the machine to sit idle until the holder is ready. Otherwise a long run from someone else takes the machine (S8). Futures providers will therefore buy blocks of time, some of it idle. That suggests a possible simplification: the foundry sells **blocks of machine time**, and a run is just the smallest block. The block's owner decides what happens inside it: run their own lot, run a broker's customers, or nothing (Q3).

**I3. The market has to pay for efficiency the foundry won't plan** (P3 + P7). Grouping same-program work to avoid setups, or batching lots, is exactly the lookahead P3 forbids the foundry. Either customers and brokers pay to arrange it (I2), or it doesn't happen. The queueing analysis has to answer two things: how much throughput this costs compared with a planned schedule, and whether the market recovers it (`DESIGN.md` §10.12 H3).

**I4. Reliability is priced, not promised** (P9 + P10). The foundry is paid even when its machine fails, so refunds give it no reason to be reliable. The pressure comes from public fault histories. Insurers charge more to cover unreliable machines, customers' total cost of using them rises, and so they bid less. The economic analysis has to show whether that pressure is strong enough, especially for machines with no substitute.

**I5. The foundry can't trade on inside information** (P4 + P10). A foundry selling futures or insurance would be trading against its customers while knowing its own maintenance plans and machine health. Under P4 it may trade only on public information, so everything it knows that affects prices has to be published before it trades. The simpler alternative is that the foundry sells no financial products at all (Q5).

**I6. Transparency and bidding strategy pull in different directions** (P5 + P10). Second-price auctions work best when bidders can't react to each other's bids. Fully public live bids invite waiting, sniping and bidding just under the leader. P10's purpose (pricing risk, explaining waits) may be served by publishing bids once a clearing is final. This has to be tested, not assumed (Q7).

**I7. Money can't buy danger, but everything else has a price** (P2 + P5 + P8). No bid overrides a protection rule. Anything a protection rule allows can be bought. So every cost an allowed run imposes on the foundry must be priced, including wear that doesn't damage the machine but isn't free.

**I8. Charging actual time opens up the program catalogue** (P1 + P6). If customers pay for actual machine time (Q1), the foundry no longer needs to certify how long a program takes in order to price it. Customers could then write and publish their own programs within machine limits (P2). The foundry would offer only machines, limits and rates, which is P1 in its strongest form (S13).

**I9. Nobody at the foundry decides whose fault it was** (P1 + P9 + P10). Payment never depends on the cause of a failure, so the foundry has no reason to classify causes. It publishes telemetry, logs and inspection results, and the parties who care about the cause (the customer and the insurer) interpret them.

**I10. Waiting is a slow bid** (P5 + P8). A customer who won't pay the going price can wait, but waiting costs storage. Every lot in the foundry is always paying for something: either to move forward or to stay put.

---

## 4. Scenarios

Each scenario gives the situation, what the principles say happens, which principles apply, and what to examine next.

### S1. Step 199 of 200

A lot has finished 199 steps. Step 200 is a probe run on the only prober, and a new customer bids more for the prober's next slot.

- **What happens:** the newcomer wins (P5). The nearly-finished lot waits and pays storage (P8) until its owner bids more. If the owner wanted step 200's cost fixed, they should have bought a future before step 199 (I1).
- **Principles:** P3, P5, P8, P9.
- **Examine:** how often lots near the end of their flow get priced out under realistic demand, and what futures on final steps cost (`DESIGN.md` §10.12 H1).

### S2. A rival blocks the last step

A competitor buys the prober's next 12 hours and leaves it idle so the lot in S1 can't finish.

- **What happens:** allowed (P5). The competitor pays the full rate for 12 idle hours, publicly (P6, P10). The blocked customer can outbid for the next block, buy a future, or use another machine with the same capability.
- **Principles:** P5, P6, P10.
- **Examine:** blocking cost versus completion cost when only one machine has the capability (`DESIGN.md` §10.12 H6). Public prices also show the foundry where a second machine would pay for itself. Buying one is a business decision outside the scheduler.

### S3. Coat, then expose within 30 minutes

Resist must be exposed within 30 minutes of coating. The spin coater and the aligner are auctioned separately.

- **What happens:** the foundry does nothing special (P3). The customer has three options: bid high on both machines, buy the aligner's time before coating finishes and leave it idle (P6), or buy a future for the exposure. If the window is missed, the customer pays for the rework (P1, P9).
- **Principles:** P1, P3, P6, P7.
- **Examine:** whether a block of time that includes idle waiting (I2) is the natural way to do this, or whether it needs its own mechanism.

### S4. A CMP tool needs a full load

The CMP tool needs 25 wafers per run. A customer has 6.

- **What happens:** the customer pays for the whole run (P6, P7), and the 19 dummy wafers are a priced consumable (P8). Alternatively, a broker buys the run and sells the other 19 positions to other customers, and the foundry still deals with a single account.
- **Principles:** P3, P6, P7, P8.
- **Examine:** whether P7 allows a run's owner to load other accounts' wafers with their consent. If so, who is responsible when one broker customer's wafer contaminates another's?

### S5. The furnace must stay hot

Cooling and requalifying the furnace costs about 12 hours, and there is no demand tonight.

- **What happens:** the foundry bids a negative price for its own furnace (P4): it would rather pay a customer to run something than let the tube cool. Any customer with a suitable lot is paid to run it, and metered consumables are still charged (P8).
- **Principles:** P4, P5, P9.
- **Examine:** the price jump when a second bidder appears, and two bidders taking turns to collect the subsidy (`DESIGN.md` §10.12 H4).

### S6. The machine faults mid-run

An etcher faults 40 minutes into a 2-hour run, and the wafers are scrapped.

- **What happens:** the customer pays for the time used (P6, P9). The wafers are the customer's loss (P1). If the customer bought insurance, the insurer decides whether to pay, based on public telemetry and logs (P10). The foundry doesn't rule on the cause (I9).
- **Principles:** P1, P6, P9, P10.
- **Examine:** whether "time used" means 40 minutes or the full 2 hours won. Also whether I4 alone gives the foundry enough reason to fix the etcher.

### S7. The machine goes down before a won run starts

A run won its clearing and is locked in, but the machine goes down before the wafers are loaded.

- **What happens:** the foundry provided nothing, so nothing is owed (P6, P9). The request goes back into the auction when the machine returns. A futures provider behind that run must win again at whatever it costs (I1).
- **Principles:** P3, P6, P9.
- **Examine:** the reverse case, where the customer withdraws after winning. `DESIGN.md` §16 charges the full cleared price. P6 and P9 suggest charging only for what was committed: staging, setup, and the time the machine sits unsold because of the withdrawal.

### S8. A futures provider loses money

A provider sold a customer a furnace slot at 15:00 for 400. The furnace frees at 13:00, with a rival's 11-hour anneal waiting, and another rival bids for the same slot.

- **What happens:** the provider must win the 13:00 clearing, pay for two idle hours and outbid the rival (I2). The auction costs the provider 900 in total, so it loses 500, publicly (P10). The customer pays the agreed 400. The foundry sees only bids and payments (P3, P4, P9).
- **Principles:** P3, P5, P6, P9, P10.
- **Examine:** how much a provider must hold in funds for an open-ended commitment to be credible, and whether providers can hedge with each other.

### S9. A run overruns

An etch with endpoint detection runs 50% longer than its program's usual time.

- **What happens:** it depends on Q1. If customers pay for actual time, this customer pays 1.5×, and the next customer starts late with no compensation; that timing risk belongs to whoever sold them a future. If customers pay for modelled time, the foundry absorbs the overrun, and has a reason to set pessimistic models.
- **Principles:** P3, P6, P9.
- **Examine:** which choice produces honest prices, and what each does to futures pricing.

### S10. A customer abandons their wafers

A prepaid customer stops paying mid-flow, and their wafers sit in storage.

- **What happens:** storage keeps charging (P8) until the account runs out of funds. The foundry then stops providing storage it can't be paid for, which physically means disposing of the wafers after public notice (P9, P11). If a postpaid customer doesn't pay, the foundry was acting as a lender, which P4 allows only as an ordinary, disclosed provider.
- **Principles:** P4, P8, P9, P11.
- **Examine:** whether postpaid accounts should exist, or credit should always come from a third party.

### S11. Planned maintenance

The foundry wants the DRIE for a 6-hour chamber clean on Thursday.

- **What happens:** under P4 the foundry buys the machine's time like anyone else, and the cost is the revenue it gives up. The plan affects prices, so it is made public in advance (P10, I5). Taking a machine down for safety falls under P2 and needs no bid.
- **Principles:** P2, P4, P10.
- **Examine:** whether the auction is the right mechanism for maintenance at all. Skipping maintenance eventually harms the machine, which might make planned maintenance a P2 case too.

### S12. A contaminated wafer arrives

A customer ships wafers declared clean that actually carry gold.

- **What happens:** incoming inspection, paid for by the customer (P6), finds the gold, and clean tools refuse the wafers (P2). If inspection misses it and a furnace gets contaminated, requalification is a cost the foundry bore, and under P9 the customer or their insurer pays it.
- **Principles:** P2, P6, P8, P9.
- **Examine:** how far a customer's liability for damage extends, and whether uninsured customers can realistically be allowed to ship wafers in.

### S13. A customer wants a process with no program

A customer wants a 1,050 °C anneal that isn't in the catalogue.

- **What happens:** within the machine's limits it runs (P1, P2), and the customer pays for their own experiments (P6). If the foundry must certify how long a program takes before it can be priced, then adding a program is foundry engineering work, which conflicts with P1. If customers pay for actual time (Q1), they can write and publish programs themselves (I8).
- **Principles:** P1, P2, P6.
- **Examine:** whether P2 requires the foundry to qualify some programs (for example anything near a machine limit), and who pays for that.

### S14. Setup as a side effect

Customer A runs a program that forces a long changeover before customer B's usual program.

- **What happens:** B's next run costs more because it needs the setup (P6). A did nothing wrong. B can bid to follow a compatible run instead, or pay for the setup.
- **Principles:** P5, P6, P7.
- **Examine:** whether setup should belong entirely to the incoming run. The outgoing customer chose the program that created the cost, so they could pay for returning the machine to a standard state.

---

## 5. Where `DESIGN.md` disagrees

Checked against `DESIGN.md` Draft v0.3. Each row is a decision to make, not something to patch quietly.

| `DESIGN.md` | Principle | Disagreement |
|---|---|---|
| §5.1, §10.2: program times are authoritative, and actual durations never affect price | P6 | Customers pay for modelled time, not time used. Depends on Q1 (S9). |
| §10.8: the foundry runs bidding policies (`deadline`, `budget`) for customers | P3 | A bidding strategy looks ahead. Under P3 it belongs to customers or third parties using the API. |
| §2.2, §10.9: the foundry publishes `projected_complete`, expected start and `price_to_lead` | P3 | Projections look like promises. They could be dropped, labelled non-binding, or left to third parties. |
| §12.1: `postpaid` accounts with a `credit_limit` | P4, P9 | The foundry lends to customers. It must be an ordinary disclosed lender, or credit comes from a third party. |
| §10.6, §12.3: the foundry is the built-in provider of futures and insurance, quoting from its own schedule and data | P4, P10 | Needs I5 (everything the foundry knows that affects prices is published first), or the foundry sells no financial products (Q5). |
| §12.3: the adapter classifies each failure's cause (`machine_fault`, `recipe`, `wafer`, `unknown`) | P9, I9 | Payment never depends on cause, so the foundry needn't classify it. Publishing the evidence may be enough. |
| §16: cancelling a won and locked run forfeits the full cleared price | P6, P9 | A penalty, not a charge for time used (S7). |
| §5.1, §10.3: the subsidy applies only when no one else bids (`applies_when: no_competing_bid`) | P4, P5 | A foundry preference that depends on who else is bidding. Arguably a legitimate bid, but it creates the collusion risk in S5. |
| §10.3: idle bids buy time the machine spends doing nothing, and can't become a run | P6, I2 | If blocks of time are the primitive (Q3), an idle block and a run are the same thing. |
| §15.1, §17: live bids are readable by anyone before the clearing | P10, I6 | May need "public once cleared" (Q7). |
| §5.1, §8 (`MP-045`): a `fill: exact` machine requires foundry dummy wafers or rejects the order | P7, P8 | Consistent with the principles, but it excludes brokers (S4) unless a run may carry other accounts' wafers (Q9). |

---

## 6. Open questions for the next iteration

1. **Actual or modelled time (P6).** Do customers pay for the machine time actually used or for the modelled time? This drives S6, S9, S13 and I8.
2. **P5 at scale.** Is "money decides" compatible with thousands of small customers? The scenario harness has to answer this; rewording won't.
3. **Blocks of time as the primitive (I2).** Should the foundry sell the next N hours of a machine and let the buyer decide what runs in them? Runs, idle bids, back-to-back steps, broker runs and futures would all become one mechanism.
4. **What the foundry must provide for futures (I1).** Is it enough that one account may bid and pay for another account's run, with the contract entirely between the two parties? If the holder's wafers aren't ready at X, is that purely between holder and provider? Under P7, which of them is "the customer" responsible for the run?
5. **Financial products (I5).** Should the foundry sell insurance, futures or credit at all? The alternative is selling only machine time and storage and leaving every financial product to third parties.
6. **Maintenance (S11).** Is planned maintenance a bid, a protection case, or something else?
7. **When bids become public (I6).** Live, or once the clearing is final?
8. **Setup attribution (S14).** Does setup belong only to the incoming run, or is it shared with the outgoing one?
9. **Other accounts' wafers in a run (S4).** Allowed with consent, and with what responsibilities?
10. **Liability beyond time (S12).** P9 covers what the foundry provides. What about damage a customer causes?
11. **Missing principles.** Candidates not yet included:
    - "The customer owns their wafers and data" (asset rights, disposal).
    - "The foundry treats every account the same" (possibly implied by P5 + P10).
    - Engineering choices such as "no new languages or formats". These probably belong in `DESIGN.md`, not here.
