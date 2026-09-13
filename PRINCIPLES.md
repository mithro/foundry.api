# foundry.api — Principles (Draft v0.4)

| | |
|---|---|
| Status | Draft v0.4. Expected to change over several iterations. |
| Date | 2026-09-13 |
| Relationship to `DESIGN.md` | `DESIGN.md` is one attempt to implement these principles. Where the two disagree (§6), change one of them on purpose. Don't quietly work around the gap. |
| Terms | **The foundry** means the entity that runs the machines. Whether the market and the other roles belong to the same entity is an open question (§4). |

The principles come first, in priority order. The rest of the document works out what they mean. §2 covers each principle alone, §3 how they combine, §4 who does what, §5 concrete scenarios, §6 where `DESIGN.md` currently disagrees, and §7 what to settle next.

---

## 1. The principles

**A principle applies only where it does not conflict with an earlier one.** Where two conflict, the earlier one wins.

**P1. Do no harm.** Never run anything that endangers people, damages machines or shared infrastructure, contaminates other customers' wafers, or breaks the law. No amount of money and no other principle overrides this.

**P2. Everything is recorded.** Every action by customers, the foundry, the market and the machines is a recorded event. What ran, and what everyone was charged, can be rebuilt exactly from that record.

**P3. Everything is public.** The record is public, including the full history of every machine: runs, faults, maintenance, calibration and plans. Anyone must be able to see enough to price insurance and futures as well as the foundry could.

**P4. The foundry sells only what it provides now.** The foundry decides what runs next and sells the machine time and storage it provides. Futures, insurance, credit, forecasts and delivery promises come from others, never from the entity running the machines.

**P5. The foundry always gets paid.** The foundry is paid for everything it provides, whatever the outcome. Nothing runs unless someone has guaranteed the payment.

**P6. Customers pay for what they actually use.** A customer pays for the machine time their request actually uses, including setup, cleanup and any time it holds the machine, plus storage and consumables. Anyone who wants a fixed price buys one from someone willing to carry the variation.

**P7. Every run belongs to one customer.** One account is responsible for each run and pays for all of it. A customer who wants the benefits of running things together (shared batches, skipped setups, back-to-back steps) pays to arrange them.

**P8. Money decides.** Among requests that satisfy every earlier principle, the one that pays most runs next. Nothing else orders the queue: not customer size, loyalty, deadlines, or how far through a flow a lot is.

**P9. Run what is asked.** Anything that satisfies every earlier principle is run exactly as asked. The foundry does not design processes, judge whether a device will work, or second-guess a customer.

### How the order was chosen

Each row is a conflict that fixes which of two principles comes first. Rows marked *provisional* are pairs where no real conflict has been found yet, so their order is arbitrary for now.

| Earlier wins | Conflict that decides it |
|---|---|
| P1 over P2 | An emergency stop happens even if recording is down. It is recorded afterwards. |
| P1 over P3 | An export-controlled design, or personal data the law forbids publishing, stays unpublished. |
| P2 over P3 | *Provisional.* The public view is derived from the record, so the record comes first. |
| P3 over P4 | Forecasting isn't the foundry's job, but anything it already knows about the future, such as a planned maintenance date, must still be published. |
| P4 over P5 | The foundry could make its income more certain by selling futures or lending to customers. It may not. If the only way to be paid is to extend credit, the run doesn't happen. |
| P5 over P6 | Actual time isn't known until a run ends. A run can't start if nobody has guaranteed payment for however long it might take. |
| P6 over P7 | *Provisional.* No conflict found yet. |
| P7 over P8 | A stranger can't pay to have their wafers added to someone else's run. A broker who takes responsibility for the whole run can. |
| P8 over P9 | A customer doesn't get their lot run next by asking; they get it by paying the most. |
| P4 over P8 | No amount of money buys a reservation from the foundry. |
| P5 over P8 | The highest bid loses if no one has guaranteed the payment. |
| P6 over P8 | A customer can't pay the foundry extra to be charged a flat price instead of actual time. A flat price has to be bought from an insurer. |

---

## 2. What each principle means

### P1. Do no harm

- **Means:** every validation rule names what it protects: a person, a machine, a consumable, a shared facility, another customer's wafers, or a legal obligation. A rule that protects only the requesting customer's own result is not a P1 rule, so P9 says delete it.
- **Means:** protection is checked again just before a run starts, because machines and wafers change.
- **Means:** wherever possible a protection rule is a declared limit of a machine, not a judgement about a customer.
- **Means:** the foundry acts to protect even when nobody is paying (P1 over P5), then recovers the cost from whoever caused it (P5, P6).
- **Rules out:** DRC for yield, and refusing a safe but pointless request.
- **Open:** "or breaks the law" was not in the user's original list; it was added for export controls, IP takedowns and personal data (Q3).

### P2. Everything is recorded

- **Means:** all state is a replay of the record. Every auction decision and every charge is a deterministic function of it.
- **Means:** anything no participant controls enters only as a recorded event: machine results, insurers' decisions, callbacks, operator actions.
- **Means:** disputes are settled against the record, not anyone's memory.

### P3. Everything is public

- **Means:** each machine's full history is public: every run with its telemetry and actual duration, every fault, every maintenance action and part replaced, calibration results, and planned maintenance. That is what lets anyone, not just the foundry, price insurance and futures.
- **Means:** queues, bids, cleared prices, ledgers, designs and results are public, so customers can see why they are waiting.
- **Means:** the foundry measures the time it charges for (P6), so those measurements are public and overcharging is visible.
- **Rules out:** private contracts with the foundry, confidential designs, hidden floors, and anything only the foundry knows.
- **Open:** *when* bids become public. P3 outranks P8, so if live public bids make the auction work badly, the auction design has to adapt. The exception is if publishing bids once a clearing is final counts as satisfying P3 (Q10).
- **Open:** P3 excludes customers who need confidentiality. That is a deliberate market choice and should be recorded as one.

### P4. The foundry sells only what it provides now

- **Means:** scheduling is a single decision: when a machine is about to become free, which request gets it. The foundry keeps no plan and no calendar.
- **Means:** the foundry promises nothing about the future. Cycle time is an outcome of the market, not a commitment.
- **Means:** the foundry doesn't sell futures, insurance or credit, and doesn't act as a broker. Those markets can exist only because P3 gives everyone the same information the foundry has (I6).
- **Means:** the foundry may still bid its own present preferences, such as a floor that covers its costs or a subsidy to keep a furnace hot, because those are about what it will accept now.
- **Rules out:** reservations, calendars, delivery promises, postpaid accounts, the foundry as insurer or futures provider, and holding a machine idle as a bet.
- **Open:** a reserve price above cost ("I'd rather idle than sell cheap") is a bet on future demand. Does P4 allow it? (Q8)
- **Open:** whether the foundry should publish any projections, such as expected start times, given that anyone can compute them from public data.

### P5. The foundry always gets paid

- **Means:** the foundry is paid for the time and resources it provides even when machines fault, operators make mistakes, runs fail or customers cancel. Anyone who wants protection from those outcomes buys it from someone else.
- **Means:** nothing runs until its payment is guaranteed, either by the customer's own funds or by someone who has agreed to pay (a futures provider, an insurer, a lender). The foundry handles counterparty risk by demanding a guarantee, not by trusting anyone.
- **Means:** payment never depends on who caused a failure, so the foundry never needs to decide (I9).
- **Means:** a negative price, where the foundry pays a customer to keep a tool running, is the foundry buying something it values now.
- **Means:** if the foundry provided nothing, nothing is owed (S7).
- **Open:** who pays the foundry when a party that promised to pay fails to (§4, S15).

### P6. Customers pay for what they actually use

- **Means:** the unit of sale is measured machine-hours, not modelled ones. A run that overruns needs more time, and the customer pays for it.
- **Means:** a customer pays for the time they buy, whether or not they use all of it. If a step finishes early, they can sell the unused time back to the market (I12).
- **Means:** time the foundry can't provide, because the machine faults or goes down, isn't charged (P5: only what is provided is paid for).
- **Means:** setup is charged to the run that needs it, and cleanup to the run that causes it. Idle time while a request holds the machine counts.
- **Means:** storage while waiting and consumables drawn are also charged as used. Anything left unpriced will be over-consumed.
- **Means:** overruns and failures are risks that others price from public machine history (P3) and sell as insurance or futures. Underruns are handled by selling the unused time back (I12).
- **Means:** a program doesn't need a foundry-certified duration to be priced, so customers could write and publish their own programs within machine limits (S13).
- **Rules out:** flat per-run prices from the foundry, and free storage, inspection, rework or dummy wafers.

### P7. Every run belongs to one customer

- **Means:** one account is responsible for each run's hours and wafers. A price is never split between strangers.
- **Means:** the foundry doesn't look for combinations such as shared batches, same-program sequences or back-to-back steps. A customer who wants one has to win the slots that create it, or pay someone to arrange it, and the saving goes to whoever arranged it.
- **Means:** a machine that needs a full load is paid for in full by the one customer using it.
- **Open:** may a run's owner load other accounts' wafers with their consent, as a broker does (S4, Q12)?

### P8. Money decides

- **Means:** money is a customer's only way to change the order of the queue. A lot at step 199 of 200 has no claim on step 200.
- **Means:** a rival who values stopping you more than you value proceeding can buy the machine's time and leave it idle. That is legitimate, public and expensive.
- **Means:** a customer may hold a machine idle while an earlier step finishes, but only for as long as they outbid everyone else who wants the machine (I11).
- **Means:** the foundry's own preferences compete as bids in the same auction.
- **Rules out:** fairness quotas, first-come-first-served, deadline boosts, protection for small customers, and priority for nearly-finished lots.
- **Note:** P8 is eighth, not first. "If a customer is willing to pay enough, it can be done" holds for everything the earlier principles allow and for nothing they forbid.
- **Open:** whether P8 is compatible with serving thousands of small customers (Q5).

### P9. Run what is asked

- **Means:** the foundry's product is a set of machines, programs and limits, and it runs requests against them. Zero per-customer engineering (NRE) follows from this.
- **Means:** the customer makes every judgement about their device: the recipe, whether a measurement is acceptable, whether to continue after a failed check.
- **Means:** P9 comes last, so every refusal must trace back to an earlier principle. A refusal with no earlier principle behind it is a defect.
- **Rules out:** yield rules, "are you sure?" checks, foundry-recommended process changes, and picking a machine beyond what the customer allowed.

---

## 3. How the principles interact

**I1. No reservations, only people who pay** (P4 + P5 + P8). The foundry sells only what it provides now, and money decides who gets it. So the only way to secure future work is to have someone willing to pay in the auction when the time comes. A **future** is exactly that. A provider agrees to get you a slot at time T for price C. When T comes, the provider must win the auction for you, whatever it costs. If the auction is cheaper than C, the provider keeps the difference; if dearer than C, the provider covers it. The foundry is not a party to the contract. All it needs is to let one account bid and pay for another account's run.

**I2. Buying ahead means buying time early** (P4 + P6 + I1). A machine's time is sold when the machine becomes free, not when a customer would like to start. A provider who promised a later slot has to win the earlier clearing and pay for the idle time until the holder is ready. Otherwise a long run from someone else takes the machine (S8). I11 shows how that idle time is bought.

**I3. The market has to pay for efficiency the foundry won't plan** (P4 + P7). Grouping same-program work to avoid setups, or batching lots, is exactly the lookahead P4 forbids the foundry. Either customers and brokers pay to arrange it (I2), or it doesn't happen. The queueing analysis has to answer two things: how much throughput this costs compared with a planned schedule, and whether the market recovers it.

**I4. Reliability is priced, not promised** (P3 + P5 + P6). Customers pay for time even when a machine fails, so refunds give the foundry no reason to be reliable. The pressure comes from public machine history. Insurers charge more to cover unreliable machines, customers' total cost rises, and so they bid less. The economic analysis has to show whether that pressure is strong enough, especially for machines with no substitute.

**I5. Paying for actual time changes what a bid is** (P5 + P6 + P8). A run's total price can't be known when the auction clears, because its duration isn't known yet. The natural thing to bid is a rate per actual machine-hour, with the total settled when the run ends. That has two consequences:
- **Ranking:** the auction ranks rates. A run after a compatible program no longer ranks higher; it just costs less in total, which changes how P7's savings play out.
- **Guarantees:** under P5, payment must be guaranteed for a duration nobody knows yet. The guarantee could be a customer-set maximum duration at which the run stops, collateral, or an insurer who agrees to pay any overrun (S16).

A sale of "machine N for X hours at rate Y" (I11) would give the rate and a bounded duration together. What gets bid is Q4.

**I6. The foundry can stay out of risk markets only if nothing is private** (P3 + P4). The foundry can leave insurance and futures to others only because others see everything it sees. If anything material stays private, only the foundry (or people close to it) can price that risk, and the market for it either won't exist or will be unfair. So P3 has to cover planned maintenance, known machine problems and upcoming changes, not only past events.

**I7. Transparency outranks bidding strategy** (P3 over P8). Second-price auctions work best when bidders can't react to each other's live bids. Public live bids invite waiting, sniping, and bidding just under the leader to raise its price. Because P3 comes first, the auction must be designed to work with public bids, unless publishing bids once a clearing is final is accepted as meeting P3 (Q10).

**I8. Money can't buy harm, but everything else has a price** (P1 + P6 + P8). No bid overrides a protection rule. Anything a protection rule allows can be bought, so every cost it imposes on the foundry must be priced, including wear that doesn't damage the machine but isn't free.

**I9. Nobody at the foundry decides whose fault it was** (P3 + P5 + P6). Payment is for time used, whatever the cause, so the foundry has no reason to classify causes. It publishes telemetry, logs and inspection results, and the parties who care about the cause (the customer and the insurer) interpret them.

**I10. Waiting is a slow bid** (P6 + P8). A customer who won't pay the going price can wait, but waiting costs storage. Every lot in the foundry is always paying for something: either to move forward or to stay put.

**I11. Holding a machine idle is just buying its time** (P4 + P6 + P8 + P9). A customer may pay for a machine to sit idle while an earlier step finishes, but only if they outbid everyone else who wants that machine. This needs no new rule:
- **P6:** time the machine is held for the customer counts as time used, even when it does nothing.
- **P8:** the only way to hold the machine is to win it.
- **P4:** it isn't a reservation. The foundry is selling the machine's time now, to the highest bidder, who chooses to leave it idle. The view of the future ("my wafer arrives in 45 minutes") is the customer's, not the foundry's.

**The unit of sale (candidate).** Every sale is **"machine N for X hours at rate Y"**. Runs and idle holds are the same kind of sale. The buyer chooses X, and with it how much risk to take. At each sale, the auction ranks bids by rate Y, and the winner pays the runner-up's rate for the hours sold. When a sale ends, the machine's next X hours are auctioned again.

**Example.** A customer's coated wafer will be ready in about 45 minutes, and the exposure must start within 30 minutes of coating (S3). The aligner is free now. The customer can buy the 45 minutes in two ways:

| | **One sale: 1 × 45 min** | **Three sales: 3 × 15 min** |
|---|---|---|
| Auctions to win | One, now | Three: now, at +15 min and at +30 min |
| If a rival with a ready lot bids 250 cr/h at +30 min | Nothing changes: the customer already owns the time until +45 min | Unless the customer bids more than 250 cr/h, the rival wins the third sale. The rival's 1-hour exposure starts, the customer's wafer arrives at +45 min and waits until +90 min, the 30-minute window is missed, and the customer pays for rework (P9). |
| If nobody else wants the aligner | Pays the floor rate for 45 minutes | Pays the floor rate for each 15 minutes. It can stop buying if the earlier step is delayed or abandoned. |
| Payment exposure (P5) | 45 min × the bid rate, guaranteed up front | 15 min × the bid rate at a time; each later sale needs its own guarantee |

The foundry doesn't choose between these (P9). The customer trades certainty (one long sale) against flexibility and a lower commitment (several short ones), and takes the risk of the choice.

Consequences:
- **Holding costs what others give up.** Under second price the holder pays the runner-up's rate. Holding a machine nobody else wants is cheap; holding a contested one is expensive.
- **Waiting and blocking are the same transaction.** Holding the aligner for your own wafer and holding it to keep a rival out (S2) are the same sale at the same price. Nothing needs to tell them apart (P9).
- **Payment exposure is bounded.** A sale of X hours at rate Y can cost at most X × Y, which is easy to guarantee under P5. Anything longer needs another sale (S16).
- **A futures provider uses the same sales.** Keeping a promised slot available is just buying idle sales, long or short, until the holder is ready (S8).
- **Buying too much is less costly than it looks.** Unused time can be sold back (I12), which makes a long sale less risky than the table suggests. Simulation must include resale.
- **Continuous versus sold-once is a matter of X.** Many very short sales behave like a continuously contested hold; one long sale behaves like a block. Whether the market needs limits on X (a minimum, a maximum, or neither) is for simulation to decide, not wording (Q6).

---

**I12. Unused time can be sold back** (P5 + P6 + P7 + P8). A customer who bought X hours and finishes early can sell the rest of the time back to the market. The remainder becomes an ordinary sale ("machine N for the remaining hours"), and the bidder with the best rate wins it. The proceeds go to the customer selling it back, not the foundry.

**Example.** A customer buys the aligner as 1 × 90 minutes (a 45-minute idle hold, then a 45-minute exposure) at a bid of 200 cr/h. The runner-up's rate is 150 cr/h, so the customer pays 225 cr. The coated wafer arrives early at +30 minutes, and the exposure finishes at +70 minutes, leaving 20 minutes unused. The customer sells those 20 minutes back. A rival wins with a bid of 180 cr/h; the runner-up is 120 cr/h, so the rival pays 40 cr and the customer receives it. The customer's net cost is 185 cr, and the foundry was paid 225 cr either way.

Consequences:
- **The foundry's income doesn't change (P5).** The foundry was paid for all the time it provided, when the time was first sold. Reselling it moves money between customers only.
- **Unused and unprovided time are different.** Time the customer doesn't need is theirs to sell back. Time the foundry can't provide, because the machine faulted or went down, is never charged at all (P5, S6, S7).
- **Short remainders are worth less.** A remainder only becomes available once the step has actually finished, often at short notice. A customer who needs time to bring wafers to the machine may not be able to use it, so small remainders may attract few bids or none.
- **Each run still belongs to one customer (P7).** Whoever buys the remainder owns that time and the run in it. Nobody shares a sale.
- **Machine time becomes something people can trade.** Once time can be resold, some participants may buy time only to resell it. P8 allows that. Whether it helps (spreading risk, filling gaps) or hurts (people buying up a bottleneck to resell at a markup) is a question for simulation, not wording (Q6).

## 4. Who does what

Settled: the entity running the machines provides no insurance, futures or credit, and anyone else can (P4). Still open: which other roles exist, and which of them may be held by the same entity.

| Role | What it does | Why it might need to be separate |
|---|---|---|
| **Machine operator** (the foundry) | Runs the machines, measures the time used, publishes machine history, bids its own present preferences | This is the starting point. |
| **Market operator** | Accepts bids, runs the clearing rules, keeps and publishes the record | The foundry receives the money the market clears. If it also runs the market, it can see bids first, time its own bids, or change the rules. A deterministic public record (P2, P3) lets anyone check each clearing, but not the order in which bids arrived, or who changed the rules and why. |
| **Settlement** | Holds participants' funds, guarantees the foundry is paid (P5), settles between customers and providers | Holding other people's money is close to lending (P4). When a provider fails to pay a cleared price, someone has to pay the foundry for a run that has already started. |
| **Providers** | Insurance, futures, credit, brokering | Already separate from the foundry (P4). |
| **Provider of last resort** | Keeps the market working when ordinary providers won't: thin markets for rare machines, a provider failing mid-contract, a sudden demand for cover | Without one, nobody may be willing to sell a future on a machine with no substitute, and flows could stall. If the foundry played this role it would break P4. |

Questions this raises:
- **Which roles may be combined?** Machine operator plus market operator has the sharpest conflict of interest. Market operator plus settlement is a common pairing (an exchange with its own clearing house).
- **Does a provider of last resort need to exist?** The alternative is that a thin market simply means high prices, which P8 accepts.
- **If a provider of last resort exists, who funds it?** Also, does that funding become a hidden subsidy, when P6 says everything is priced?
- **Does P4's wording change?** If the market operator is separate, "the foundry decides what runs next" should become "the market decides what runs next, and the foundry runs it".
- **Could one market serve several machine operators?** If the market is separate, several foundries could sell into it. Out of scope for now, but a natural consequence.

---

## 5. Scenarios

Each scenario gives the situation, what the principles say happens, which principles apply, and what to examine next.

### S1. Step 199 of 200

A lot has finished 199 steps. Step 200 is a probe run on the only prober, and a new customer bids more for the prober's next slot.

- **What happens:** the newcomer wins (P8). The nearly-finished lot waits and pays storage (P6) until its owner bids more. If the owner wanted step 200's cost fixed, they should have bought a future before step 199 (I1).
- **Principles:** P4, P6, P8.
- **Examine:** how often lots near the end of their flow get priced out under realistic demand, and what futures on final steps cost.

### S2. A rival blocks the last step

A competitor buys the prober's next 12 hours and leaves it idle so the lot in S1 can't finish.

- **What happens:** allowed (P8). The competitor pays for the 12 hours actually held, publicly (P3, P6). The blocked customer can outbid for the next block, buy a future, or use another machine with the same capability.
- **Principles:** P3, P6, P8.
- **Examine:** blocking cost versus completion cost when only one machine has the capability. Public prices also show where a second machine would pay for itself. Buying one is a business decision outside the market.

### S3. Coat, then expose within 30 minutes

Resist must be exposed within 30 minutes of coating. The spin coater and the aligner are auctioned separately.

- **What happens:** the foundry does nothing special (P4). The customer has three options: bid high on both machines, buy the aligner's time before coating finishes and hold it idle (I11), or buy a future for the exposure. If they hold the aligner, they choose between one long sale and several short ones, and take the risk of losing a short one. If the window is missed, the customer pays for the rework (P5, P9).
- **Principles:** P4, P6, P7, P8, P9.
- **Examine:** how customers actually split idle holds under realistic competition, and how often short sales are lost at the worst moment (Q6).

### S4. A CMP tool needs a full load

The CMP tool needs 25 wafers per run. A customer has 6.

- **What happens:** the customer pays for the whole run (P7), including the 19 dummy wafers used (P6). Alternatively, a broker buys the run and sells the other 19 positions, and the foundry still deals with a single account.
- **Principles:** P4, P6, P7.
- **Examine:** whether P7 allows a run's owner to load other accounts' wafers with their consent. If so, who is responsible when one broker customer's wafer contaminates another's?

### S5. The furnace must stay hot

Cooling and requalifying the furnace costs about 12 hours, and there is no demand tonight.

- **What happens:** the foundry bids a negative price for its own furnace (P8). It would rather pay a customer to run something than let the tube cool, and P4 allows this because it is a preference about now. Any customer with a suitable lot is paid to run it, and consumables are still charged (P6).
- **Principles:** P4, P5, P6, P8.
- **Examine:** the price jump when a second bidder appears, and two bidders taking turns to collect the subsidy.

### S6. The machine faults mid-run

An etcher faults 40 minutes into what would have been a 2-hour run, and the wafers are scrapped.

- **What happens:** the customer pays for 40 minutes (P6). The rest of the time they bought isn't charged, because the foundry couldn't provide it (I12). The wafers are the customer's loss (P9). An insurer, if the customer bought insurance, decides whether to pay, using the public machine history and telemetry (P3). The foundry doesn't rule on the cause (I9).
- **Principles:** P3, P5, P6, P9.
- **Examine:** whether the pressure in I4 is enough to make the foundry fix the etcher.

### S7. The machine goes down before a won run starts

A run won its clearing and is locked in, but the machine goes down before the wafers are loaded.

- **What happens:** the foundry provided nothing, so nothing is owed (P5, P6). The request goes back into the auction when the machine returns. A futures provider behind that run must win again at whatever it costs (I1).
- **Principles:** P4, P5, P6.
- **Examine:** the reverse case, where the customer withdraws after winning. Under P6 they pay for the time the machine was actually held for them, not a penalty.

### S8. A futures provider loses money

A provider (never the foundry, P4) sold a customer a furnace slot at 15:00 for 400. The furnace frees at 13:00, with a rival's 11-hour anneal waiting, and another rival bids for the same slot.

- **What happens:** the provider must win the 13:00 clearing and hold the furnace idle until 15:00 (I11), either as one 2-hour sale or as several shorter ones that the rival could win. It must also outbid the rival for the 15:00 run. The auction costs the provider 900 in total, so it loses 500, publicly (P3). The customer pays the agreed 400. The foundry sees only bids and payments.
- **Principles:** P3, P4, P5, P6, P8.
- **Examine:** what guarantee a provider must give for an open-ended commitment to count as guaranteed payment under P5 (§4, S15).

### S9. A run overruns

An etch with endpoint detection runs 50% longer than usual.

- **What happens:** the customer pays for 1.5× the time (P6). The next customer starts late, with no compensation from the foundry. That timing risk belongs to whoever sold them a future, and insurers price overruns of that program on that machine from public history (P3).
- **Principles:** P3, P4, P6.
- **Examine:** how payment for an open-ended run is guaranteed (S16).

### S10. A customer abandons their wafers

A customer stops paying mid-flow, and their wafers sit in storage.

- **What happens:** storage keeps charging (P6) until the customer's guarantee of payment runs out. The foundry then stops providing what can't be paid for (P5), which physically means disposal after public notice (P2, P3). There are no postpaid accounts at the foundry (P4). If a third-party lender financed the customer, the lender carries the loss.
- **Principles:** P2, P3, P4, P5, P6.
- **Examine:** whether a lender can claim the wafers as collateral before disposal, and who decides.

### S11. Planned maintenance

The foundry wants the DRIE for a 6-hour chamber clean on Thursday.

- **What happens:** the plan is public as soon as the foundry has it (P3 over P4), so anyone pricing futures on the DRIE can account for it. When Thursday comes, the foundry either buys the machine's time like anyone else (P8) or, if skipping the clean would harm the machine, takes the machine down under P1.
- **Principles:** P1, P3, P4, P8.
- **Examine:** whether planned maintenance is a bid, a P1 case, or something else (Q9).

### S12. A contaminated wafer arrives

A customer ships wafers declared clean that actually carry gold.

- **What happens:** incoming inspection, paid for by the customer (P6), finds the gold, and clean tools refuse the wafers (P1). If inspection misses it and a furnace gets contaminated, the foundry acts first to protect the machine (P1 over P5), then recovers the requalification cost from the customer or their insurer (P5, P6).
- **Principles:** P1, P5, P6.
- **Examine:** how far a customer's liability for damage extends, and whether uninsured customers can realistically be allowed to ship wafers in.

### S13. A customer wants a process with no program

A customer wants a 1,050 °C anneal that isn't in the catalogue.

- **What happens:** within the machine's limits it runs (P1, P9), and the customer pays for the actual time of their own experiments (P6). Pricing no longer needs a certified duration, so the customer can write and publish the program for others to use.
- **Principles:** P1, P3, P6, P9.
- **Examine:** whether P1 requires the foundry to qualify programs near a machine limit, and who pays for that.

### S14. Setup as a side effect

Customer A runs a program that forces a long changeover before customer B's usual program.

- **What happens:** B pays for the setup time (P6). A did nothing wrong. B can bid to follow a compatible run instead, or accept the setup cost. With rate bids (I5), the setup doesn't change how B ranks, only what B pays in total.
- **Principles:** P6, P7, P8.
- **Examine:** whether setup should belong entirely to the incoming run. The outgoing customer chose the program that created the cost, so they could pay for returning the machine to a standard state.

### S15. A futures provider can't pay

A provider promised a customer a slot, but when the auction clears at 900 the provider can't pay.

- **What happens:** under P5 a bid counts only if payment is guaranteed, so the provider's bid never wins. The customer loses the slot and has a claim against the provider outside the market. If a settlement entity had guaranteed the provider, that entity pays the foundry and pursues the provider.
- **Principles:** P4, P5, P8.
- **Examine:** whether customers can tell in advance how solid a provider's promise is (P3 helps), and whether this is what a provider of last resort is for (§4).

### S16. An overrun nobody has funded

An etch runs until an endpoint detector triggers. The customer's funds cover 3 hours, and at 3 hours it hasn't finished.

- **What happens:** P5 means the run should never have started with open-ended exposure. Every request that can run long needs one of three things: a maximum duration at which it stops (the customer's instruction, P9, which is the X of its sale in I11), collateral, or an insurer committed to pay for the overrun. Stopping at the maximum may ruin the wafers; that is the customer's choice (P9), provided stopping is safe (P1).
- **Principles:** P1, P5, P6, P9.
- **Examine:** whether a maximum duration is a required part of every request, and what a sensible default is. If a run needs longer than the X it bought and someone else wins the next sale, does the run stop (if safe, P1) or does the run's owner automatically bid for more time?

---

## 6. Where `DESIGN.md` disagrees

Checked against `DESIGN.md` Draft v0.3. Each row is a decision to make, not something to patch quietly.

| `DESIGN.md` | Principle | Disagreement |
|---|---|---|
| §5.1, §10.2: prices use modelled program durations; actual durations never affect price | P6 | `DESIGN.md` must change to actual time. What gets bid is Q4. Foundry-certified durations then stop being needed for pricing (S13). |
| §10.6, §12.3, §19 (M6, M8): the foundry is a built-in provider of futures and insurance | P4 | Remove. Only third parties provide these. |
| §12.1: `postpaid` accounts with a `credit_limit` | P4 | Remove. Credit comes from third-party lenders. |
| §10.8: the foundry runs bidding policies (`deadline`, `budget`) for customers | P4 | Bidding strategy looks ahead, so it belongs to customers or third parties using the API. |
| §2.2, §10.9: the foundry publishes `projected_complete`, expected start times and `price_to_lead` | P4 | Projections look like promises. They could be dropped, clearly labelled non-binding, or left to third parties. |
| §5.6, §11.3, §14, §15.2: runs, telemetry, utilisation and a `maintenance` machine state are published, but no maintenance records, parts, calibration or planned maintenance | P3 | The full machine history and all plans must be published. |
| §2.4, §6: one service runs the machine registry, auction and ledger together | §4 | Whether these roles may be combined is undecided (Q1). |
| §12.3: the adapter classifies each failure's cause (`machine_fault`, `recipe`, `wafer`, `unknown`) | P5, I9 | Payment never depends on cause, so the foundry needn't classify it. Publishing the evidence may be enough. |
| §16: cancelling a won and locked run forfeits the full cleared price | P6 | Charge the time actually held, not a penalty (S7). |
| §5.1, §10.3: the subsidy applies only when no one else bids (`applies_when: no_competing_bid`) | P4, P8 | A present preference, so allowed, but it creates the collusion risk in S5. |
| §10.2, §10.3: a bid is a total `max_credits` for one run; idle bids are a separate kind, and one can't become a run | P6, I11 | If every sale is "machine N for X hours at rate Y" (I11), idle holds and runs are the same kind of sale. |
| §15.1, §17: live bids are readable by anyone before the clearing | P3, I7 | P3 outranks P8, so public bids stay unless "public once cleared" is accepted (Q10). |
| §5.1, §8 (`MP-045`): a `fill: exact` machine requires foundry dummy wafers or rejects the order | P7 | Consistent with the principles, but it excludes brokers (S4) unless a run may carry other accounts' wafers (Q12). |

---

## 7. Open questions for the next iteration

1. **Roles (§4).** Machine operator, market operator, settlement and provider of last resort: which must be separate, which can be combined, and who funds the last resort?
2. **The order itself.** Two pairs are provisional (P2/P3, P6/P7). Is one-customer-per-run (P7) really above money (P8)?
3. **Law in P1.** Was "or breaks the law" right to add, or does it need its own principle?
4. **What gets bid when time is actual (I5).** A rate per hour, a total settled afterwards, or "X hours at rate Y" (I11)? How is payment for an open-ended run guaranteed (S16)?
5. **P8 at scale.** Is "money decides" compatible with thousands of small customers? The scenario harness has to answer this; rewording won't.
6. **The unit of sale (I11).** Is every sale "machine N for X hours at rate Y"? To be settled by simulation and scenarios:
    - **Limits on X:** does the market need a minimum or maximum X, or can customers choose freely between continuous-like short sales and block-like long ones?
    - **Unused time:** settled in principle: the buyer pays for all X and may sell unused time back (I12). Still open:
      - Does the customer selling time back set a minimum price, or accept whatever the market pays?
      - Can owned time be sold back before it starts (for example the last hour of a three-hour sale, sold while the first hour is running), or only once the step has finished?
      - Is buying time only to resell it acceptable, or does it need limits?
    - **Running out of time:** what happens when a run needs longer than the X it bought (S16)?
7. **What futures need (I1).** Is it enough that one account can bid and pay for another's run? Under P7, which of holder and provider is "the customer" for the run? If the holder's wafers aren't ready at T, is that purely between holder and provider?
8. **Reserves above cost (P4).** Is refusing to sell cheap now, in the hope of better prices later, a forbidden bet on the future?
9. **Maintenance (S11).** Is planned maintenance a bid, a P1 case, or something else?
10. **When bids become public (I7).** Live, or once the clearing is final? Given P3 over P8, does "once final" count as public?
11. **Setup attribution (S14).** Does setup belong only to the incoming run, or is it shared with the outgoing one?
12. **Other accounts' wafers in a run (S4).** Allowed with consent, and with what responsibilities?
13. **Liability beyond time (S12).** P5 covers what the foundry provides. What about damage a customer causes?
14. **Missing principles.** Candidates not yet included:
    - "The customer owns their wafers and data" (asset rights, disposal, lenders' collateral).
    - "Every account is treated the same" (possibly implied by P3 + P8).

---

## Appendix — Changelog

**v0.4 (2026-09-13)**
- **New I12:** a customer who finishes early can sell the unused time back to the market, with a worked example. The foundry's income is unchanged. Time the foundry can't provide (a fault or breakdown) is never charged, which is different from time the customer doesn't use.
- **Updated:** P6, I11, S6 and Q6 to match.
- **Renamed variables:** futures (I1, Q7) now say "time T for price C", so they don't clash with the sale unit's "X hours at rate Y".

**v0.3 (2026-09-13)**
- **New I11:** holding a machine idle while an earlier step finishes is just buying its time, and only works while the customer outbids everyone else. It proposes a candidate unit of sale, "machine N for X hours at rate Y", with the buyer choosing X (for example 1 × 45 min or 3 × 15 min) and taking the risk.
- **Updated:** I2, I5, P8, S3, S8, S16, the `DESIGN.md` table and Q4 now refer to I11.
- **Replaced Q6:** "blocks of time as the primitive" is now "the unit of sale". Whether sales should behave continuously or as blocks is left to simulation.

**v0.2 (2026-09-12)**
- **Priority order.** Principles are now in priority order; where two conflict, the earlier one wins. The table in §1 records which conflict decided each placement.
- **Decisions applied:**
  - Customers pay for actual time (P6), and insurance and futures markets handle overruns, underruns and failures.
  - The foundry publishes each machine's full history and plans, so anyone can take part (P3).
  - The entity running the machines provides no insurance, futures or credit (P4).
- **New section §4 (Who does what):** the open question of machine operator versus market operator versus settlement versus provider of last resort.
- **Merged and split:**
  - "Refuse only to protect" became "Do no harm" (P1). "Refuse only" is now expressed by putting "Run what is asked" last (P9).
  - "Everything is priced" is merged into P6.
  - "The foundry is just another participant" is split across P3 (same information), P4 (no financial products) and P8 (its preferences are bids).
- **Renumbering:** v0.1 → v0.2 principle numbers:
  - P1 → P9
  - P2 → P1
  - P3 → P4
  - P4 → P3 / P4 / P8
  - P5 → P8
  - P6 → P6
  - P7 → P7
  - P8 → P6
  - P9 → P5
  - P10 → P3
  - P11 → P2
- **Scenarios:** S1–S14 keep their numbers, with S6, S9 and S13 now resolved by actual-time pricing. S15 (a provider can't pay) and S16 (an unfunded overrun) are new.

**v0.1 (2026-09-12)**: first distillation of `DESIGN.md` into eleven unordered principles.
