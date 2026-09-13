# foundry.api — Principles (Draft v0.10)

| | |
|---|---|
| Status | Draft v0.10. Expected to change over several iterations. |
| Date | 2026-09-13 |
| Relationship to `DESIGN.md` | `DESIGN.md` is one attempt to implement these principles. Where the two disagree (§6), change one of them on purpose. Don't quietly work around the gap. |
| Terms | **The foundry** means the entity that runs the machines. Whether the market and the other roles belong to the same entity is an open question (§4). |

The principles come first, in priority order. The rest of the document works out what they mean. §2 covers each principle alone, §3 how they combine, §4 who does what, §5 concrete scenarios, §6 where `DESIGN.md` currently disagrees, and §7 what to settle next.

---

## 1. The principles

**A principle applies only where it does not conflict with an earlier one.** Where two conflict, the earlier one wins.

**P1. Do no harm.** Never run anything that endangers people, damages machines or shared infrastructure, contaminates other customers' wafers, or breaks the law. No amount of money and no other principle overrides this.

**P2. Everything is recorded and public.** Every action by customers, the foundry, the market and the machines is recorded, and the record is public, including each machine's full history of runs, faults, maintenance, calibration and plans. Anyone must be able to rebuild what happened, and to price risk as well as the foundry could.

**P3. The foundry does as little as possible.** It operates its machines, records and publishes what they do, and sells their time now to whoever the market says won it; any other action is a safety call or follows a published rule driven by prices others set. Everything else (what time is worth, what risks cost, when to maintain, when anything will happen, futures, insurance and credit) is decided and provided by customers, insurers and other providers from public data.

**P4. Every hour is paid for.** Each hour of machine time is sold to one account, which pays for the actual time it holds (including setup, cleanup and idle time) plus storage and consumables, and nothing runs until that payment is guaranteed. Hours the foundry can't provide are paid for by the foundry's own insurance, so the foundry always gets paid, whatever the outcome.

**P5. Money decides.** Among requests that satisfy every earlier principle, the one that pays most runs next, and nothing else orders the queue: not customer size, loyalty, deadlines, or how far through a flow a lot is. Every preference costs money, whether about timing, machine state or running things together, so picky customers pay more and flexible customers pay less.

**P6. Run what is asked.** Anything that satisfies every earlier principle is run exactly as asked. The foundry does not design processes, judge whether a device will work, or second-guess a customer.

### How the order was chosen

Each row is a conflict that fixes which of two principles comes first. Consolidation merged both pairs whose order was only provisional, so every row now rests on a real conflict.

| Earlier wins | Conflict that decides it |
|---|---|
| P1 over P2 | An emergency stop happens even if recording is down, and is recorded afterwards. An export-controlled design, or personal data the law forbids publishing, stays unpublished. |
| P1 over P3 | A safety call is a judgement, not a price-driven rule. It's allowed because P1 comes first. |
| P2 over P3 | The foundry makes no forecasts, but anything it knows that affects prices, such as a problem it has noticed on a machine or a change to its rules, must still be published. |
| P3 over P4 | The foundry could make its income more certain by selling futures or lending to customers. It may not. If the only way to be paid is to extend credit, the run doesn't happen. |
| P3 over P5 | No amount of money buys a reservation from the foundry. |
| P3 over P6 | A customer can ask for a run, but can't ask the foundry to judge anything for them, such as the best time to run or a delivery date. |
| P4 over P5 | The highest bid loses if no one has guaranteed the payment. A stranger can't pay to have their wafers added to someone else's sale, but a broker who takes responsibility for the whole sale can. A customer can't pay the foundry extra to be charged a flat price instead of actual time; a flat price has to be bought from an insurer. |
| P5 over P6 | A customer doesn't get their lot run next by asking; they get it by paying the most. |

---

## 2. What each principle means

### P1. Do no harm

- **Means:** every validation rule names what it protects: a person, a machine, a consumable, a shared facility, another customer's wafers, or a legal obligation. A rule that protects only the requesting customer's own result is not a P1 rule, so P6 says delete it.
- **Means:** protection is checked again just before a run starts, because machines and wafers change.
- **Means:** wherever possible a protection rule is a declared limit of a machine, not a judgement about a customer.
- **Means:** the foundry acts to protect even when nobody is paying (P1 over P4), then recovers the cost from whoever caused it (P4).
- **Rules out:** DRC for yield, and refusing a safe but pointless request.
- **Open:** "or breaks the law" was not in the user's original list; it was added for export controls, IP takedowns and personal data (Q3).

### P2. Everything is recorded and public

**Recorded**
- **Means:** all state is a replay of the record. Every auction decision and every charge is a deterministic function of it.
- **Means:** anything no participant controls enters only as a recorded event: machine results, insurers' decisions, callbacks, operator actions.
- **Means:** disputes are settled against the record, not anyone's memory.

**Public**
- **Means:** each machine's full history is public: every run with its telemetry and actual duration, every fault, every maintenance action and part replaced, calibration results, and planned maintenance. That is what lets anyone, not just the foundry, price insurance and futures, and lets customers judge how much a machine's current state matters to them (I15).
- **Means:** queues, bids, cleared prices, ledgers, designs and results are public, so customers can see why they are waiting.
- **Means:** the foundry measures the time it charges for (P4), so those measurements are public and overcharging is visible.
- **Rules out:** private contracts with the foundry, confidential designs, hidden floors, and anything only the foundry knows.
- **Open:** *when* bids become public. P2 outranks P5, so if live public bids make the auction work badly, the auction design has to adapt. The exception is if publishing bids once a clearing is final counts as satisfying P2 (Q10).
- **Open:** P2 excludes customers who need confidentiality. That is a deliberate market choice and should be recorded as one.

### P3. The foundry does as little as possible

**What the foundry does.** This is a closed list; anything not on it belongs to someone else.
1. Operate the machines, including safety calls (P1).
2. Measure what happens, record it and publish it (P2).
3. Hand each machine's time to whoever the market says won it.
4. Collect payment, and buy its own insurance (P4).

- **Means:** every foundry action is either a safety call or follows a published rule driven by prices others set. The rules are part of the public record (P2), so anyone can check that the foundry followed them.
- **Means:** every judgement the foundry might otherwise make is replaced by a price someone else sets:

  | Decision | Who decides | What the foundry follows |
  |---|---|---|
  | When and how often to maintain | The downtime insurer, and anyone else who buys maintenance hours | Nothing to decide: it performs maintenance in hours someone bought (I14) |
  | When machine time is most valuable | Customers | Clearing prices |
  | What a risk costs | Insurers | Premiums |
  | The foundry's own floor and subsidies | A published formula | Running cost including the downtime premium. For a subsidy, the cost the run avoids, such as requalifying a cooled furnace. No markup and no speculative reserve. |
  | When anything will be done | Futures providers | Futures prices |
  | What a machine's state is worth | Customers and step insurers | Conditional bids and step premiums (I15) |
  | Whose fault a failure was | Insurers | Nothing to decide: payment doesn't depend on cause (I9) |
  | Where to add capacity | Investors, from public clearing prices | Outside the foundry's operation (candidate exception below) |

- **Means:** the foundry provides as little as possible. Services that don't need its machines, such as shipping, mask making, analysis, or storage outside the cleanroom, can come from other providers.
- **Means:** the foundry promises nothing about the future and publishes no projections. Cycle time is an outcome of the market, and anyone can compute projections from public data.
- **Means:** the foundry doesn't sell futures, insurance or credit, and doesn't act as a broker. It may *buy* insurance (I13). Those markets can exist because P2 gives everyone the same information the foundry has (I6).
- **Rules out:** reservations, calendars, delivery promises, projections, postpaid accounts, reserves above cost, discretionary discounts or priorities, the foundry as insurer or futures provider, the foundry classifying failure causes, and the foundry running bidding strategies for customers.

**Exceptions.** Aim for the strict form, and fall back only where following it has a consequence we are unwilling to accept. Each accepted exception is listed here with the consequence that justifies it. None is accepted yet. Candidates (Q8):
- **Writing and changing the rules.** Someone has to write the published rules and formulas the foundry follows. Unless a market operator or another party writes them, this is foundry discretion. At minimum, changes should be public in advance and recorded (P2).
- **Business decisions.** Buying or retiring machines, choosing which capabilities to offer, and staffing aren't market operations. Public prices can inform them, but someone still decides.
- **Machine limits and procedures.** Declaring a machine's safe limits and its maintenance procedures is probably a P1 safety call rather than an exception, but it is still judgement.

### P4. Every hour is paid for

**Sold to one account**
- **Means:** each hour is sold to exactly one account, which is responsible for that time and the wafers in it. A price is never split between strangers.
- **Means:** a machine that needs a full load is paid for in full by the one account using it.
- **Open:** may that account load other accounts' wafers with their consent, as a broker does (S4, Q12)?

**Paid for the actual time held**
- **Means:** the unit of sale is measured machine-hours, not modelled ones. A run that overruns needs more time, and the customer pays for it.
- **Means:** a customer pays for the time they buy, whether or not they use all of it. If a step finishes early, they can sell the unused time back to the market (I12).
- **Means:** setup is charged to the run that needs it, and cleanup to the run that causes it. Idle time while a request holds the machine counts.
- **Means:** storage while waiting and consumables drawn are also charged as used. Anything left unpriced will be over-consumed.
- **Means:** overruns and failures are risks that others price from public machine history (P2) and sell as insurance or futures. Underruns are handled by selling the unused time back (I12).
- **Means:** a program doesn't need a foundry-certified duration to be priced, so customers could write and publish their own programs within machine limits (S13).

**Guaranteed before it runs**
- **Means:** nothing runs until its payment is guaranteed, either by the customer's own funds or by someone who has agreed to pay (a futures provider, an insurer, a lender). The foundry handles counterparty risk by demanding a guarantee, not by trusting anyone.
- **Means:** actual time isn't known until a run ends, so a request that could run long needs a maximum duration, collateral, or someone committed to pay for the overrun (S16).
- **Open:** who pays the foundry when a party that promised to pay fails to (§4, S15).

**The foundry always gets paid**
- **Means:** the foundry is paid for the time and resources it provides even when machines fault, operators make mistakes, runs fail or customers cancel. Anyone who wants protection from those outcomes buys it from someone else.
- **Means:** payment never depends on who caused a failure, so the foundry never needs to decide (I9).
- **Means:** time the foundry can't provide, because a machine breaks down or needs unplanned maintenance, isn't charged to the customer. The foundry's own downtime insurance pays for it; this insurance is effectively required for every machine, and its premium is part of the machine's running cost. Customers cover their own losses with step insurance, if they choose to buy it (I13, S7).
- **Means:** a negative price, where the foundry pays a customer to keep a tool running, comes from a published formula: the cost the run saves the foundry, such as requalifying a cooled furnace (P3).
- **Rules out:** flat per-run prices from the foundry; free storage, inspection, rework or dummy wafers; and splitting one sale's price between strangers.

### P5. Money decides

- **Means:** money is a customer's only way to change the order of the queue. A lot at step 199 of 200 has no claim on step 200.
- **Means:** each condition a customer puts on a request narrows the time they will accept, whether it's about timing, which machine, or the machine's state (such as time since maintenance or calibration). They then compete for less, so they pay more and may wait longer. A customer with high margins or a tolerant recipe can take the hours picky customers refuse, and pays less for them (I15).
- **Means:** running things together is a preference like any other. The foundry doesn't look for combinations such as shared batches, same-program sequences or back-to-back steps. A customer who wants one has to win the sales that create it, or pay someone to arrange it, and the saving goes to whoever arranged it.
- **Means:** a rival who values stopping you more than you value proceeding can buy the machine's time and leave it idle. That is legitimate, public and expensive.
- **Means:** a customer may hold a machine idle while an earlier step finishes, but only for as long as they outbid everyone else who wants the machine (I11).
- **Means:** the foundry's own bids (its floor, and subsidies such as keeping a furnace hot) follow published formulas (P3). Maintenance hours are bought by whoever wants the maintenance, normally the downtime insurer (I14).
- **Rules out:** fairness quotas, first-come-first-served, deadline boosts, protection for small customers, and priority for nearly-finished lots.
- **Note:** P5 is fifth, not first. "If a customer is willing to pay enough, it can be done" holds for everything the earlier principles allow and for nothing they forbid.
- **Open:** whether P5 is compatible with serving thousands of small customers (Q5).

### P6. Run what is asked

- **Means:** the foundry's product is a set of machines, programs and limits, and it runs requests against them. Zero per-customer engineering (NRE) follows from this.
- **Means:** the customer makes every judgement about their device: the recipe, whether a measurement is acceptable, whether to continue after a failed check.
- **Means:** P6 comes last, so every refusal must trace back to an earlier principle. A refusal with no earlier principle behind it is a defect.
- **Means:** the customer decides how much a machine's state (time since maintenance, calibration, recent faults) matters to them, and can make a request conditional on it. What those conditions cost is P5.
- **Rules out:** yield rules, "are you sure?" checks, foundry-recommended process changes, and picking a machine beyond what the customer allowed.

---

## 3. How the principles interact

**I1. No reservations, only people who pay** (P3 + P4 + P5). The foundry sells only the time it provides now and makes no promises about later, and money decides who gets it. So the only way to secure future work is to have someone willing to pay in the auction when the time comes. A **future** is exactly that. A provider agrees to get you a slot at time T for price C. When T comes, the provider must win the auction for you, whatever it costs. If the auction is cheaper than C, the provider keeps the difference; if dearer than C, the provider covers it. The foundry is not a party to the contract. All it needs is to let one account bid and pay for another account's run.

**I2. Buying ahead means buying time early** (P3 + P4 + I1). A machine's time is sold when the machine becomes free, not when a customer would like to start. A provider who promised a later slot has to win the earlier clearing and pay for the idle time until the holder is ready. Otherwise a long run from someone else takes the machine (S8). I11 shows how that idle time is bought.

**I3. The market has to pay for efficiency the foundry won't plan** (P3 + P4). Grouping same-program work to avoid setups, or batching lots, is exactly the lookahead P3 forbids the foundry. Either customers and brokers pay to arrange it (I2), or it doesn't happen. The queueing analysis has to answer two things: how much throughput this costs compared with a planned schedule, and whether the market recovers it.

**I4. Reliability is priced, not promised** (P2 + P4). The foundry insures its downtime and customers insure their losses (I13), so neither refunds nor lost income push the foundry to be reliable. The pressure comes from premiums priced on public machine history. An unreliable machine makes the foundry's downtime premium, and so its running cost and floor, rise. It also makes customers' step premiums rise, so they bid less. The economic analysis has to show whether that pressure is strong enough, especially for machines with no substitute, and whether the foundry can end up gaining from its own failures (I13).

**I5. Paying for actual time changes what a bid is** (P4 + P5). A run's total price can't be known when the auction clears, because its duration isn't known yet. The natural thing to bid is a rate per actual machine-hour, with the total settled when the run ends. That has two consequences:
- **Ranking:** the auction ranks rates. A run after a compatible program no longer ranks higher; it just costs less in total, which changes who gets the saving from running things together (P5).
- **Guarantees:** under P4, payment must be guaranteed for a duration nobody knows yet. The guarantee could be a customer-set maximum duration at which the run stops, collateral, or an insurer who agrees to pay any overrun (S16).

A sale of "machine N for X hours at rate Y" (I11) would give the rate and a bounded duration together. What gets bid is Q4.

**I6. The foundry can stay out of risk markets only if nothing is private** (P2 + P3). The foundry can leave insurance and futures to others only because others see everything it sees. If anything material stays private, only the foundry (or people close to it) can price that risk, and the market for it either won't exist or will be unfair. So P2 has to cover planned maintenance, known machine problems and upcoming changes, not only past events.

**I7. Transparency outranks bidding strategy** (P2 over P5). Second-price auctions work best when bidders can't react to each other's live bids. Public live bids invite waiting, sniping, and bidding just under the leader to raise its price. Because P2 comes first, the auction must be designed to work with public bids, unless publishing bids once a clearing is final is accepted as meeting P2 (Q10).

**I8. Money can't buy harm, but everything else has a price** (P1 + P4 + P5). No bid overrides a protection rule. Anything a protection rule allows can be bought, so every cost it imposes on the foundry must be priced, including wear that doesn't damage the machine but isn't free.

**I9. Nobody at the foundry decides whose fault it was** (P2 + P4). Payment is for time used, whatever the cause, so the foundry has no reason to classify causes. It publishes telemetry, logs and inspection results, and the parties who care about the cause (the customer and the insurer) interpret them.

**I10. Waiting is a slow bid** (P4 + P5). A customer who won't pay the going price can wait, but waiting costs storage. Every lot in the foundry is always paying for something: either to move forward or to stay put.

**I11. Holding a machine idle is just buying its time** (P3 + P4 + P5 + P6). A customer may pay for a machine to sit idle while an earlier step finishes, but only if they outbid everyone else who wants that machine. This needs no new rule:
- **P4:** time the machine is held for the customer counts as time used, even when it does nothing.
- **P5:** the only way to hold the machine is to win it.
- **P3:** it isn't a reservation. The foundry is selling the machine's time now, to the highest bidder, who chooses to leave it idle. The view of the future ("my wafer arrives in 45 minutes") is the customer's, not the foundry's.

**The unit of sale (candidate).** Every sale is **"machine N for X hours at rate Y"**. Runs and idle holds are the same kind of sale. The buyer chooses X, and with it how much risk to take. At each sale, the auction ranks bids by rate Y, and the winner pays the runner-up's rate for the hours sold. When a sale ends, the machine's next X hours are auctioned again.

**Example.** A customer's coated wafer will be ready in about 45 minutes, and the exposure must start within 30 minutes of coating (S3). The aligner is free now. The customer can buy the 45 minutes in two ways:

| | **One sale: 1 × 45 min** | **Three sales: 3 × 15 min** |
|---|---|---|
| Auctions to win | One, now | Three: now, at +15 min and at +30 min |
| If a rival with a ready lot bids 250 cr/h at +30 min | Nothing changes: the customer already owns the time until +45 min | Unless the customer bids more than 250 cr/h, the rival wins the third sale. The rival's 1-hour exposure starts, the customer's wafer arrives at +45 min and waits until +90 min, the 30-minute window is missed, and the customer pays for rework (P6). |
| If nobody else wants the aligner | Pays the floor rate for 45 minutes | Pays the floor rate for each 15 minutes. It can stop buying if the earlier step is delayed or abandoned. |
| Payment exposure (P4) | 45 min × the bid rate, guaranteed up front | 15 min × the bid rate at a time; each later sale needs its own guarantee |

The foundry doesn't choose between these (P6). The customer trades certainty (one long sale) against flexibility and a lower commitment (several short ones), and takes the risk of the choice.

Consequences:
- **Holding costs what others give up.** Under second price the holder pays the runner-up's rate. Holding a machine nobody else wants is cheap; holding a contested one is expensive.
- **Waiting and blocking are the same transaction.** Holding the aligner for your own wafer and holding it to keep a rival out (S2) are the same sale at the same price. Nothing needs to tell them apart (P6).
- **Payment exposure is bounded.** A sale of X hours at rate Y can cost at most X × Y, which is easy to guarantee under P4. Anything longer needs another sale (S16).
- **A futures provider uses the same sales.** Keeping a promised slot available is just buying idle sales, long or short, until the holder is ready (S8).
- **Buying too much is less costly than it looks.** Unused time can be sold back (I12), which makes a long sale less risky than the table suggests. Simulation must include resale.
- **Continuous versus sold-once is a matter of X.** Many very short sales behave like a continuously contested hold; one long sale behaves like a block. Whether the market needs limits on X (a minimum, a maximum, or neither) is for simulation to decide, not wording (Q6).

**I12. Unused time can be sold back** (P4 + P5). A customer who bought X hours and finishes early can sell the rest of the time back to the market. The remainder becomes an ordinary sale ("machine N for the remaining hours"), and the bidder with the best rate wins it. The proceeds go to the customer selling it back, not the foundry.

**Example.** A customer buys the aligner as 1 × 90 minutes (a 45-minute idle hold, then a 45-minute exposure) at a bid of 200 cr/h. The runner-up's rate is 150 cr/h, so the customer pays 225 cr. The coated wafer arrives early at +30 minutes, and the exposure finishes at +70 minutes, leaving 20 minutes unused. The customer sells those 20 minutes back. A rival wins with a bid of 180 cr/h; the runner-up is 120 cr/h, so the rival pays 40 cr and the customer receives it. The customer's net cost is 185 cr, and the foundry was paid 225 cr either way.

Consequences:
- **The foundry's income doesn't change (P4).** The foundry was paid for all the time it provided, when the time was first sold. Reselling it moves money between customers only.
- **Unused and unprovided time are different.** Time the customer doesn't need is theirs to sell back. Time the foundry can't provide, because the machine faulted or went down, isn't charged to the customer; the foundry's downtime insurance pays for it (I13).
- **Short remainders are worth less.** A remainder only becomes available once the step has actually finished, often at short notice. A customer who needs time to bring wafers to the machine may not be able to use it, so small remainders may attract few bids or none.
- **Each run still belongs to one customer (P4).** Whoever buys the remainder owns that time and the run in it. Nobody shares a sale.
- **Machine time becomes something people can trade.** Once time can be resold, some participants may buy time only to resell it. P5 allows that. Whether it helps (spreading risk, filling gaps) or hurts (people buying up a bottleneck to resell at a markup) is a question for simulation, not wording (Q6).

**I13. Every outage has two kinds of loss, and each is insured separately** (P2 + P3 + P4 + P6). When a machine can't provide time (a breakdown, a fault mid-run, maintenance that overruns), both the foundry and its customers lose something, and each insures its own loss:

| | **Downtime insurance** | **Step insurance** |
|---|---|---|
| Who buys it | The foundry, for each machine | The customer, for each step they commit to |
| What it pays | The market value of the machine time lost, paid to the foundry | A refund of what the customer paid for the failed step, the agreed value of lost wafers, and the cost of rework (paid to the foundry through the auction) |
| Where the premium ends up | In the machine's running cost, so in its floor rate and in every customer's price on that machine | In that customer's cost of the step |
| Priced from | The insurer's own predictions from public machine history (P2) | The insurer's own predictions from public machine history (P2) and the customer's process |
| Required? | Effectively yes: P4 requires the foundry to be paid for time it can't provide | No: the customer chooses (P6), and carries their own losses without it |
| Seller | Never the foundry (P3) | Never the foundry (P3) |

**Example.** A customer buys 2 hours on an etcher, and the auction clears at 150 cr/h. The etcher faults 40 minutes in, scrapping the wafers, and stays down for 6 hours.
- **The customer:** pays for the 40 minutes provided, 100 cr. The other 80 minutes (200 cr) aren't charged, under the working assumption below.
- **The foundry's downtime insurer:** pays the foundry the market value of the 6 lost hours. At a recent clearing rate of 140 cr/h that's 840 cr.
- **The customer's step insurer:** refunds the 100 cr, pays the agreed value of the lost wafers, and pays for rework. Rework means buying this step and the earlier ones again at auction, say 1,500 cr, most of which is paid to the foundry.

**Interactions to think through:**
- **Is time the foundry can't provide charged to the customer?** There are two readings:
  - **(a)** The customer isn't charged, and the foundry's downtime insurance covers those hours.
  - **(b)** The customer pays for all the time they bought, as with unused time (I12). Their step insurance refunds them, and the foundry's downtime insurance covers only lost time nobody had bought.

  Both make the foundry whole; they differ in who carries the cost and what each premium covers. This document currently assumes (a).
- **Double payment.** If the customer pays for time that wasn't provided *and* the downtime insurer pays market value for the same hours, the foundry is paid twice. Whichever reading is chosen, each hour is paid for once.
- **The foundry may gain from its own failures.**
  - **Lost income is replaced.** In the example, the customer and the downtime insurer together pay the foundry 940 cr for the 6 hours 40 minutes from the start of the run. Had the etcher worked, it would have earned about 950 cr (300 cr from this customer, then 4 hours 40 minutes at 140 cr/h).
  - **Rework is extra demand.** The rework also creates demand for machine time, paid for by the customer's insurer. If the machines aren't fully booked, or the rework pushes prices up, the foundry comes out ahead of a day with no failure.
  - **Two ways to push back.** One is premiums: both insurers charge more on unreliable machines. The other is *liability* cover: when the cause is a machine fault, the customer's insurer recovers the rework cost from the foundry's insurer, so the foundry's own premium carries it. Which gives the foundry the right incentive is a question for the economic analysis (I4).
- **Measuring the market value of lost time.** Recent clearing rates are public (P2), but they can be pushed up just before an outage the foundry expects, for example by bids from parties close to the foundry. The foundry itself has no discretionary reserve to push them with (P3). The measure has to be hard to manipulate and settled against the record (P2).
- **Planned maintenance isn't insured; it is bought.** Insurance covers uncertain losses. Planned maintenance is paid for by whoever buys the hours for it, normally the downtime insurer itself (I14). Maintenance that overruns, or is forced by a fault, is insurable downtime.
- **Failure must not be cheaper than maintenance.** If the foundry decided maintenance, underpriced downtime insurance would make letting machines fail its cheapest option. Because the downtime insurer buys the maintenance (I14), the party that pays for failures is the one deciding how much to maintain. A wrong prediction costs that insurer, in claims or in maintenance hours. Whether competition between insurers keeps their predictions good enough is a question for the economic analysis (I15).
- **Cause matters to insurers, even though the foundry ignores it.** The foundry still doesn't decide whose fault an outage was (I9), but the insurers must. If a customer's contaminated wafer takes a furnace down (S12), that customer is liable, and the foundry's downtime insurer will want to recover from them or their insurer.
- **One outage, many claims at once.** A single breakdown affects every customer with wafers on or waiting for that machine, as well as the foundry. The losses are correlated, which is where a provider of last resort may be needed (§4). An insurer writing both kinds of policy on the same machine would be on both sides of every dispute about cause.
- **Rework is bought at whatever the auction charges.** A step insurer paying for rework is exposed to future auction prices, so step insurance carries some of a future's risk. Policies may need a cap, or to be paired with futures.
- **Resold time, idle holds and futures.**
  - **Resold time:** when an outage hits time that was sold back (I12), the loss belongs to the time's current owner.
  - **Idle holds:** an outage during an idle hold (I11) can make the holder miss a coupling window, which is a loss for step insurance.
  - **Futures:** a future for a slot during an outage can't be delivered by anyone. Whether the provider or the holder bears that depends on the future's terms.

**I14. Maintenance is bought machine time, and insurers decide when** (P2 + P3 + P4 + P5). Maintenance takes a machine's hours out of sale, so those hours have to be bought at auction like any others. Under P3 the foundry doesn't decide when to buy them:
- **The downtime insurer decides.** It pays for unplanned outages (I13), so it is the party that gains from maintenance. It buys maintenance hours when its own prediction says they cost less than the claims they prevent, and the foundry performs the maintenance in those hours.
- **The real cost is priced.** Maintenance hours cost what others would have paid for them: the runner-up's rate, published (P2).
- **Customers can pay for the machine state they want.** Depending on the machine, time just after maintenance may be better (more reliable, better calibrated) or worse (more likely to fail, more variable) than later time (I15). What customers pay for those hours is a price the insurer, and anyone else buying maintenance, can take into account.

**Example (illustrative numbers).** A DRIE is due a 6-hour chamber clean. Its downtime insurer predicts from the machine's history that failure risk rises with time since cleaning (the "wears out" profile in I15), and that each day without a clean adds about 50 cr of expected claims.

| Option | Best competing bid | Cost of the hours | Insurer's predicted extra claims | Insurer's total |
|---|---|---|---|---|
| Clean on Thursday afternoon | 300 cr/h | 6 h × 300 = 1,800 cr | none | 1,800 cr |
| Clean on Sunday night | 80 cr/h | 6 h × 80 = 480 cr | 3 days × 50 = 150 cr | 630 cr |

The insurer buys Sunday night. The foundry decides nothing; it performs the clean in hours someone bought. For a machine that runs in, the hours after a clean clear lower, and an insurer that buys maintenance too often pays for that, both in the hours it buys and in its claims.

**Consequences and things to watch:**
- **Real money changes hands.** The insurer pays the foundry for the maintenance hours, so maintenance is income for the foundry, not a payment to itself. The insurer recovers the cost through premiums, so maintenance still ends up in the machine's running cost.
- **The foundry never bids for maintenance in its own auction.** That removes the risk of a seller placing maintenance bids it never means to win to push prices up. The same risk remains for the foundry's formula bids, such as its floor and furnace subsidies (S5).
- **Who else may buy maintenance?** Anyone who values it could buy maintenance hours: a step insurer, or a picky customer who wants a freshly cleaned machine for their own run. P5 allows it. A rival could buy "maintenance" just to take the machine's time, but they pay for the hours and the parts, as with any idle hold (I11). Whether to allow it is Q9.
- **Parts and labour are priced.** Parts and consumables used in maintenance are charged to whoever bought the hours (P4), so over-maintenance costs its buyer.
- **Bought maintenance must happen.** The foundry performs its published maintenance procedure in hours bought for maintenance and records it with evidence (P2). It doesn't choose what to do.
- **No insurer, no maintenance.** A machine nobody will insure has nobody to buy its maintenance until P1 forces the machine down. That is either an acceptable outcome (an uninsurable machine degrades until it's unsafe) or a case for a provider of last resort (§4).
- **Maintenance is time the foundry can't sell, but it isn't downtime.** Hours bought for maintenance aren't lost time, so downtime insurance doesn't pay for them. An overrun beyond the hours bought is insurable downtime, or is covered by buying more hours.
- **Safety still overrides the auction.** If waiting for a cheap slot would make the machine dangerous or damage it, P1 wins: the machine comes down now, whatever the market price. That forced outage counts as insurable downtime (I13).
- **Sales already made are respected.** A maintenance buyer, like any buyer, can only buy hours at a clearing. It can't interrupt a sale someone else already won, except under P1. To be sure of a particular slot it can buy a future (I1).
- **A machine's state has to be measurable.** For customers and insurers to price it, calibration results, process results and faults by time since maintenance must be public (P2). Otherwise premiums and customers' bids are guesswork.
- **Customers may want the post-maintenance slot in advance.** Buying it before anyone has bought the maintenance is a bet on the future, so it comes from futures providers, not the foundry (P3, I1).
- **Fallback.** If insurer-bought maintenance turns out to have consequences we won't accept, the fallback is a published foundry rule: buy maintenance hours whenever they cost less than the premium reduction the insurer quotes. That brings back the problems above of the foundry paying itself and bidding in its own auction.

**I15. Being picky costs; being flexible pays** (P2 + P3 + P5 + P6). This is P5 applied to machine state. The insurance market decides what a machine's state is worth for risk, and each customer decides what it is worth to them. Nobody else decides either.
- **Insurers set premiums from their own predictions.** Neither the foundry nor this document says how risk changes with maintenance. Insurers read the public history (P2) and compete on how well they predict. A wrong prediction costs the insurer who made it.
- **Machines have different profiles.** The history may show any shape, for example:

  | Profile | Right after maintenance | After a long time running | Who gets cheaper time |
  |---|---|---|---|
  | **Bathtub** | Failures more likely, from problems introduced by the maintenance itself | Low for a while, then rising as parts wear | Flexible customers take the hours just after maintenance and late in the cycle; picky ones pay for the middle |
  | **Runs in** | Worse or more variable results until the machine settles | More stable and more reliable | Flexible customers take the post-maintenance hours; picky ones pay for later ones |
  | **Wears out** | Best results and fewest failures | Gradually less reliable | Picky customers pay for the post-maintenance hours; flexible ones take the late ones |

- **Reliability and process quality are different things.** Downtime insurers care whether the machine stops. Customers and step insurers also care how well it processes: calibration, drift, run-to-run variation. A machine can be reliable but drifting, or accurate but fault-prone, and each can follow a different profile.
- **Customers decide how much to care (P6).** A customer can make a request conditional on public machine state, for example "only if the machine has run at least 20 lots since maintenance and its last calibration is within spec". They can also simply not bid at times they don't like. Being picky narrows the hours they will accept, so they pay more for those hours and may wait longer.
- **Flexible customers get what others refuse.** A customer with high margins or a tolerant recipe can bid for the hours picky customers avoid. Those hours clear lower because fewer people want them, so the flexible customer pays less, and the machine's time still gets sold.
- **Maintenance timing follows the insurer's prediction.** The foundry doesn't decide when to maintain at all (I14). The downtime insurer buys maintenance hours based on its own prediction of the machine's profile, and customers who care about post-maintenance state show it through what they pay for the hours that follow.
- **Things to watch:**
  - **Conditions need exact, public machine state.** Machine state must be recorded exactly and published (P2). Otherwise customers can't write conditions, and nobody can check them when a sale clears.
  - **Thin markets predict poorly.** If few insurers cover a rare machine, their predictions may be poor. That is another case for a provider of last resort (§4).
  - **Wrong predictions cost whoever made them.** An insurer that misjudges a machine's profile maintains it too often or too rarely, and pays for that in maintenance hours or in claims. Competing insurers and a public claims record correct this, not a rule.

---

## 4. Who does what

Settled: the entity running the machines provides no insurance, futures or credit, and anyone else can (P3). Still open: which other roles exist, and which of them may be held by the same entity.

| Role | What it does | Why it might need to be separate |
|---|---|---|
| **Machine operator** (the foundry) | Runs the machines, measures the time used, publishes machine history, and follows published rules. Its only bids are formula floors and subsidies (P3). | This is the starting point. |
| **Market operator** | Accepts bids, runs the clearing rules, keeps and publishes the record | The foundry receives the money the market clears. If it also runs the market, it can see bids first, time its own bids, or change the rules. A deterministic public record (P2) lets anyone check each clearing, but not the order in which bids arrived, or who changed the rules and why. |
| **Settlement** | Holds participants' funds, guarantees the foundry is paid (P4), settles between customers and providers | Holding other people's money is close to lending (P3). When a provider fails to pay a cleared price, someone has to pay the foundry for a run that has already started. |
| **Providers** | Insurance, futures, credit, brokering | Already separate from the foundry (P3). |
| **Provider of last resort** | Keeps the market working when ordinary providers won't: thin markets for rare machines, a provider failing mid-contract, a sudden demand for cover | Without one, nobody may be willing to sell a future on a machine with no substitute, and flows could stall. If the foundry played this role it would break P3. |

Questions this raises:
- **Which roles may be combined?** Machine operator plus market operator has the sharpest conflict of interest. Market operator plus settlement is a common pairing (an exchange with its own clearing house).
- **Does a provider of last resort need to exist?** The alternative is that a thin market simply means high prices, which P5 accepts.
- **If a provider of last resort exists, who funds it?** Also, does that funding become a hidden subsidy, when P4 says everything is priced?
- **Who writes the foundry's rules?** Under P3 the foundry follows published rules and formulas. If the machine operator writes them, that is its remaining discretion (a candidate exception under P3). A market operator or another body could write them instead.
- **P3 already fits a separate market.** P3 says the foundry hands time to whoever the market says won it, which works whether or not the market operator is a separate entity.
- **Could one market serve several machine operators?** If the market is separate, several foundries could sell into it. Out of scope for now, but a natural consequence.

---

## 5. Scenarios

Each scenario gives the situation, what the principles say happens, which principles apply, and what to examine next.

### S1. Step 199 of 200

A lot has finished 199 steps. Step 200 is a probe run on the only prober, and a new customer bids more for the prober's next slot.

- **What happens:** the newcomer wins (P5). The nearly-finished lot waits and pays storage (P4) until its owner bids more. If the owner wanted step 200's cost fixed, they should have bought a future before step 199 (I1).
- **Principles:** P3, P4, P5.
- **Examine:** how often lots near the end of their flow get priced out under realistic demand, and what futures on final steps cost.

### S2. A rival blocks the last step

A competitor buys the prober's next 12 hours and leaves it idle so the lot in S1 can't finish.

- **What happens:** allowed (P5). The competitor pays for the 12 hours actually held, publicly (P2, P4). The blocked customer can outbid for the next block, buy a future, or use another machine with the same capability.
- **Principles:** P2, P4, P5.
- **Examine:** blocking cost versus completion cost when only one machine has the capability. Public prices also show where a second machine would pay for itself. Buying one is a business decision outside the market.

### S3. Coat, then expose within 30 minutes

Resist must be exposed within 30 minutes of coating. The spin coater and the aligner are auctioned separately.

- **What happens:** the foundry does nothing special (P3). The customer has three options: bid high on both machines, buy the aligner's time before coating finishes and hold it idle (I11), or buy a future for the exposure. If they hold the aligner, they choose between one long sale and several short ones, and take the risk of losing a short one. If the window is missed, the customer pays for the rework (P4, P6).
- **Principles:** P3, P4, P5, P6.
- **Examine:** how customers actually split idle holds under realistic competition, and how often short sales are lost at the worst moment (Q6).

### S4. A CMP tool needs a full load

The CMP tool needs 25 wafers per run. A customer has 6.

- **What happens:** the customer pays for the whole run, including the 19 dummy wafers used (P4). Alternatively, a broker buys the run and sells the other 19 positions, and the foundry still deals with a single account.
- **Principles:** P3, P4.
- **Examine:** whether P4 allows a run's owner to load other accounts' wafers with their consent. If so, who is responsible when one broker customer's wafer contaminates another's?

### S5. The furnace must stay hot

Cooling and requalifying the furnace costs about 12 hours, and there is no demand tonight.

- **What happens:** the foundry's published subsidy formula bids a negative price for its own furnace, up to the requalification cost a run would avoid (P3). Any customer with a suitable lot is paid to run it, and consumables are still charged (P4).
- **Principles:** P3, P4, P5.
- **Examine:** the price jump when a second bidder appears, two bidders taking turns to collect the subsidy, and whether a seller's formula bid can still be used to push up prices (I14).

### S6. The machine faults mid-run

An etcher faults 40 minutes into what would have been a 2-hour run, and the wafers are scrapped.

- **What happens:** the customer pays for 40 minutes (P4). The rest of the time they bought isn't charged; the foundry's downtime insurance pays the foundry for the lost hours instead. The wafers are the customer's loss (P6) unless they bought step insurance, which refunds the 40 minutes, pays for the wafers and funds rework (I13). The insurers use public machine history and telemetry (P2). The foundry doesn't rule on the cause (I9).
- **Principles:** P2, P4, P6.
- **Examine:** whether the pressure in I4 is enough to make the foundry fix the etcher, given that insurance replaces its lost income and rework adds demand (I13).

### S7. The machine goes down before a won run starts

A run won its clearing and is locked in, but the machine goes down before the wafers are loaded.

- **What happens:** the customer owes nothing for time the foundry couldn't provide, and the foundry's downtime insurance pays it for the lost hours (P4, I13). The request goes back into the auction when the machine returns. A futures provider behind that run must win again at whatever it costs (I1).
- **Principles:** P3, P4.
- **Examine:** the reverse case, where the customer withdraws after winning. Under P4 they pay for the time the machine was actually held for them, not a penalty.

### S8. A futures provider loses money

A provider (never the foundry, P3) sold a customer a furnace slot at 15:00 for 400. The furnace frees at 13:00, with a rival's 11-hour anneal waiting, and another rival bids for the same slot.

- **What happens:** the provider must win the 13:00 clearing and hold the furnace idle until 15:00 (I11), either as one 2-hour sale or as several shorter ones that the rival could win. It must also outbid the rival for the 15:00 run. The auction costs the provider 900 in total, so it loses 500, publicly (P2). The customer pays the agreed 400. The foundry sees only bids and payments.
- **Principles:** P2, P3, P4, P5.
- **Examine:** what guarantee a provider must give for an open-ended commitment to count as guaranteed payment under P4 (§4, S15).

### S9. A run overruns

An etch with endpoint detection runs 50% longer than usual.

- **What happens:** the customer pays for 1.5× the time (P4). The next customer starts late, with no compensation from the foundry. That timing risk belongs to whoever sold them a future, and insurers price overruns of that program on that machine from public history (P2).
- **Principles:** P2, P3, P4.
- **Examine:** how payment for an open-ended run is guaranteed (S16).

### S10. A customer abandons their wafers

A customer stops paying mid-flow, and their wafers sit in storage.

- **What happens:** storage keeps charging (P4) until the customer's guarantee of payment runs out. The foundry then stops providing what can't be paid for, which physically means disposal after public notice (P2). There are no postpaid accounts at the foundry (P3). If a third-party lender financed the customer, the lender carries the loss.
- **Principles:** P2, P3, P4.
- **Examine:** whether a lender can claim the wafers as collateral before disposal, and who decides.

### S11. Planned maintenance

The DRIE is due a 6-hour chamber clean, and demand on Thursday is high.

- **What happens:** the foundry makes no decision (P3). The DRIE's downtime insurer, predicting from the machine's history, buys 6 hours when they cost less than the claims it expects to prevent, for example Sunday night rather than Thursday (I14). The foundry performs the clean in those hours and records it (P2). If waiting would make the machine unsafe or damage it, P1 overrides and the machine comes down now. An overrun beyond the hours bought is insurable downtime (I13).
- **Principles:** P1, P2, P3, P4, P5.
- **Examine:** whether insurer-bought maintenance produces the right amount of maintenance, and what happens to a machine no insurer will cover (Q9).

### S12. A contaminated wafer arrives

A customer ships wafers declared clean that actually carry gold.

- **What happens:** incoming inspection, paid for by the customer (P4), finds the gold, and clean tools refuse the wafers (P1). If inspection misses it and a furnace gets contaminated, the foundry acts first to protect the machine (P1 over P4), then recovers the requalification cost from the customer or their insurer (P4). The foundry's downtime insurer, having paid for the outage, will also want to recover from the customer (I13).
- **Principles:** P1, P4, I13.
- **Examine:** how far a customer's liability for damage extends, and whether uninsured customers can realistically be allowed to ship wafers in.

### S13. A customer wants a process with no program

A customer wants a 1,050 °C anneal that isn't in the catalogue.

- **What happens:** within the machine's limits it runs (P1, P6), and the customer pays for the actual time of their own experiments (P4). Pricing no longer needs a certified duration, so the customer can write and publish the program for others to use.
- **Principles:** P1, P2, P4, P6.
- **Examine:** whether P1 requires the foundry to qualify programs near a machine limit, and who pays for that.

### S14. Setup as a side effect

Customer A runs a program that forces a long changeover before customer B's usual program.

- **What happens:** B pays for the setup time (P4). A did nothing wrong. B can bid to follow a compatible run instead, or accept the setup cost. With rate bids (I5), the setup doesn't change how B ranks, only what B pays in total.
- **Principles:** P4, P5.
- **Examine:** whether setup should belong entirely to the incoming run. The outgoing customer chose the program that created the cost, so they could pay for returning the machine to a standard state.

### S15. A futures provider can't pay

A provider promised a customer a slot, but when the auction clears at 900 the provider can't pay.

- **What happens:** under P4 a bid counts only if payment is guaranteed, so the provider's bid never wins. The customer loses the slot and has a claim against the provider outside the market. If a settlement entity had guaranteed the provider, that entity pays the foundry and pursues the provider.
- **Principles:** P3, P4, P5.
- **Examine:** whether customers can tell in advance how solid a provider's promise is (P2 helps), and whether this is what a provider of last resort is for (§4).

### S16. An overrun nobody has funded

An etch runs until an endpoint detector triggers. The customer's funds cover 3 hours, and at 3 hours it hasn't finished.

- **What happens:** P4 means the run should never have started with open-ended exposure. Every request that can run long needs one of three things: a maximum duration at which it stops (the customer's instruction, P6, which is the X of its sale in I11), collateral, or an insurer committed to pay for the overrun. Stopping at the maximum may ruin the wafers; that is the customer's choice (P6), provided stopping is safe (P1).
- **Principles:** P1, P4, P6.
- **Examine:** whether a maximum duration is a required part of every request, and what a sensible default is. If a run needs longer than the X it bought and someone else wins the next sale, does the run stop (if safe, P1) or does the run's owner automatically bid for more time?

---

## 6. Where `DESIGN.md` disagrees

Checked against `DESIGN.md` Draft v0.3. Each row is a decision to make, not something to patch quietly.

| `DESIGN.md` | Principle | Disagreement |
|---|---|---|
| §5.1, §10.2: prices use modelled program durations; actual durations never affect price | P4 | `DESIGN.md` must change to actual time. What gets bid is Q4. Foundry-certified durations then stop being needed for pricing (S13). |
| §10.6, §12.3, §19 (M6, M8): the foundry is a built-in provider of futures and insurance | P3 | Remove. Only third parties provide these. |
| §12.1: `postpaid` accounts with a `credit_limit` | P3 | Remove. Credit comes from third-party lenders. |
| §10.8: the foundry runs bidding policies (`deadline`, `budget`) for customers | P3 | Bidding strategy looks ahead, so it belongs to customers or third parties using the API. |
| §2.2, §10.9: the foundry publishes `projected_complete`, expected start times and `price_to_lead` | P3 | The foundry makes no forecasts. Remove; third parties can compute projections from public data. |
| §5.1, §10.3: the foundry sets its bid adjustment and reserves at its own discretion (`adjustment_credits_per_hour`, a `reserve` of +400) | P3 | Floors and subsidies must follow published formulas from costs, and there are no discretionary or speculative reserves. |
| §5.4, §7.2: mask fabrication, external processing and shipping are foundry-run logistics steps | P3 | Services that don't need the foundry's machines can come from other providers. The foundry only hands over and receives wafers. |
| §5.6, §11.3, §14, §15.2: runs, telemetry, utilisation and a `maintenance` machine state are published, but no maintenance records, parts, calibration or planned maintenance | P2 | The full machine history and all plans must be published. |
| §2.4, §6: one service runs the machine registry, auction and ledger together | §4 | Whether these roles may be combined is undecided (Q1). |
| §5.6, §10.3, §15.2, §17: maintenance is a machine state the foundry sets directly, or a very high reserve bid (the DRIE's `reserve 9999` before maintenance) | P3, P5, I14 | Maintenance hours are bought at auction by whoever wants the maintenance, normally the downtime insurer, and the foundry performs it. Time since maintenance and calibration results must also be published so customers and insurers can price them (P2). |
| §10.3, §15.1: bids carry no conditions on machine state | P6, I15 | Customers need to be able to make a request conditional on public machine state, such as time since maintenance or calibration results. |
| §12.3: with no insurance policy, the customer is charged for machine time even on `machine_fault`, and foundry insurance is optional and bought from the built-in provider | P3, P4, I13 | Customers aren't charged for time the foundry can't provide (working assumption, reading (a)). Every machine carries downtime insurance from a third party, with the premium in its rate, and customers can buy step insurance. |
| §12.3: the adapter classifies each failure's cause (`machine_fault`, `recipe`, `wafer`, `unknown`) | P4, I9 | Payment never depends on cause, so the foundry needn't classify it. Publishing the evidence may be enough. |
| §16: cancelling a won and locked run forfeits the full cleared price | P4 | Charge the time actually held, not a penalty (S7). |
| §5.1, §10.3: the subsidy applies only when no one else bids (`applies_when: no_competing_bid`) | P3, P5 | Allowed only as a published formula (the requalification cost a run avoids), not a discretionary setting. It still creates the collusion risk in S5. |
| §10.2, §10.3: a bid is a total `max_credits` for one run; idle bids are a separate kind, and one can't become a run | P4, I11 | If every sale is "machine N for X hours at rate Y" (I11), idle holds and runs are the same kind of sale. |
| §15.1, §17: live bids are readable by anyone before the clearing | P2, I7 | P2 outranks P5, so public bids stay unless "public once cleared" is accepted (Q10). |
| §5.1, §8 (`MP-045`): a `fill: exact` machine requires foundry dummy wafers or rejects the order | P4 | Consistent with the principles, but it excludes brokers (S4) unless a run may carry other accounts' wafers (Q12). |

---

## 7. Open questions for the next iteration

1. **Roles (§4).** Machine operator, market operator, settlement and provider of last resort: which must be separate, which can be combined, and who funds the last resort?
2. **The order itself.** Consolidation removed both provisional pairs. Is each remaining conflict in §1 decided the right way? For example, should selling each hour to one account (part of P4) really rank above money (P5)?
3. **Law in P1.** Was "or breaks the law" right to add, or does it need its own principle?
4. **What gets bid when time is actual (I5).** A rate per hour, a total settled afterwards, or "X hours at rate Y" (I11)? How is payment for an open-ended run guaranteed (S16)?
5. **P5 at scale.** Is "money decides" compatible with thousands of small customers? The scenario harness has to answer this; rewording won't.
6. **The unit of sale (I11).** Is every sale "machine N for X hours at rate Y"? To be settled by simulation and scenarios:
    - **Limits on X:** does the market need a minimum or maximum X, or can customers choose freely between continuous-like short sales and block-like long ones?
    - **Unused time:** settled in principle: the buyer pays for all X and may sell unused time back (I12). Still open:
      - Does the customer selling time back set a minimum price, or accept whatever the market pays?
      - Can owned time be sold back before it starts (for example the last hour of a three-hour sale, sold while the first hour is running), or only once the step has finished?
      - Is buying time only to resell it acceptable, or does it need limits?
    - **Running out of time:** what happens when a run needs longer than the X it bought (S16)?
7. **What futures need (I1).** Is it enough that one account can bid and pay for another's run? Under P4, which of holder and provider is "the customer" for the run? If the holder's wafers aren't ready at T, is that purely between holder and provider?
8. **Exceptions to P3.** Which candidate exceptions listed under P3 are accepted: writing and changing the rules, business decisions, machine limits and procedures? What unacceptable consequence justifies each one? Are there other places where "no discretion" has a consequence we won't accept? (Reserves above cost are answered: not allowed.)
9. **Maintenance (I14, S11).** Settled in principle: maintenance hours are bought at auction, normally by the downtime insurer, and the foundry performs the maintenance. P1 overrides when waiting would be unsafe. Still open:
    - **Who may buy maintenance:** only the machine's downtime insurer, or anyone (a step insurer, a picky customer, a rival)? What happens to a machine no insurer will cover (I14)?
    - **Enforcement:** must a winning maintenance bid be carried out, and what evidence is recorded?
    - **Measurement:** how are "time since maintenance" and calibration quality measured and published, so customers and insurers can price them?
    - **Data:** does the public record contain enough (runs and faults since maintenance, calibration and process results) for insurers and customers to estimate each machine's profile (I15)?
    - **Conditional requests:** which machine-state conditions can a request carry, and how are they checked when a sale clears (I15)?
10. **When bids become public (I7).** Live, or once the clearing is final? Given P2 over P5, does "once final" count as public?
11. **Setup attribution (S14).** Does setup belong only to the incoming run, or is it shared with the outgoing one?
12. **Other accounts' wafers in a run (S4).** Allowed with consent, and with what responsibilities?
13. **Liability beyond time (S12).** What about damage a customer causes? How do the downtime insurer and the customer's step insurer settle who pays (I13)?
14. **Downtime and step insurance (I13).**
    - **Charging:** is time the foundry can't provide charged to the customer, reading (a) or (b)? The document assumes (a).
    - **Market value:** how is the market value of lost time measured so it can't be manipulated?
    - **Incentives:** should step insurance recover rework costs from the foundry's downtime insurer when a machine is at fault (liability cover), so the foundry can't gain from its own failures?
    - **Conflicts of interest:** may one insurer write both kinds of policy on the same machine?
    - **Correlated losses:** who absorbs correlated losses when one outage triggers many claims at once (§4)?
15. **Missing principles.** Candidates not yet included:
    - "The customer owns their wafers and data" (asset rights, disposal, lenders' collateral).
    - "Every account is treated the same" (possibly implied by P2 + P5).

---

## Appendix — Changelog

**v0.10 (2026-09-13)**
- **P3 is now "The foundry does as little as possible", in its strict form.** Every foundry action is a safety call or follows a published rule driven by prices others set. Customers, insurers and other providers decide and provide everything else. The rule is to fall back only where following it has a consequence we won't accept.
- **P3's explanation** now has:
  - a closed list of what the foundry does
  - a table of each decision, who makes it, and what the foundry follows instead
  - candidate exceptions, none of them accepted yet
- **Order table:** new rows for P1 over P3 and P3 over P6, and a reworded P2 over P3.
- **Maintenance (I14):** now decided and bought by the downtime insurer, not the foundry. That removes the foundry paying itself and the foundry bidding in its own auction. It adds "no insurer, no maintenance", and a published foundry rule as the fallback.
- **Also updated to match:** P4, P5, I13, I15, S5, S11, §4, the `DESIGN.md` table (projections, discretionary reserves, foundry-run logistics, maintenance, subsidy), and Q8 (now about the exceptions to P3) and Q9.

**v0.9 (2026-09-13)**
- **Consolidated from nine principles to six.** No decision changed; the merged principles say the same things in fewer places.
  - "Everything is recorded" and "Everything is public" became **P2. Everything is recorded and public**.
  - "The foundry always gets paid", "Customers pay for what they actually use" and "Every run belongs to one customer" became **P4. Every hour is paid for**.
  - Running things together (from the old P7) and wanting a fixed price (from the old P6) were already covered by P5's "every preference costs money" and P3's "futures and insurance come from others", so they aren't repeated.
- **Order table:** the two provisional pairs disappear, because each merged into a single principle.
- **Renumbering:** v0.8 → v0.9 principle numbers:
  - P1 → P1
  - P2 → P2
  - P3 → P2
  - P4 → P3
  - P5 → P4
  - P6 → P4
  - P7 → P4
  - P8 → P5
  - P9 → P6

  All references in §3–§7 were renumbered. Earlier changelog entries keep the numbers they had at the time.

**v0.8 (2026-09-13)**
- **P8 wording:** picky versus flexible is now part of P8's own text: "Every preference costs money, so picky customers pay more and flexible customers pay less." P8 gains a bullet explaining it.
- **P9 and I15:** P9 now covers only the customer's right to attach conditions to a request, and I15 is described as P8 applied to machine state.

**v0.7 (2026-09-13)**
- **Premiums are set only by the insurance market.** Insurers predict from public data. The document no longer assumes that risk rises with time since maintenance, or that freshly maintained time is better.
- **New I15:** being picky costs and being flexible pays. It covers:
  - three example machine profiles (bathtub, runs in, wears out)
  - reliability versus process quality
  - requests conditional on public machine state
  - flexible customers buying the hours others refuse
  - maintenance timing following market prices rather than a known profile
- **Updated to match:** P3, P9, I13, I14 (the example now names its profile), S11, the `DESIGN.md` table and Q9.

**v0.6 (2026-09-13)**
- **New I14:** maintenance is bought machine time. The foundry buys a machine's hours from the market like any customer, which:
  - prices the income it gives up by taking the machine down
  - lets it choose when to maintain, weighing that cost against downtime premiums that rise the longer maintenance is delayed
  - lets customers pay more for freshly maintained, better calibrated time
- **I14 example and risks:** a worked example (clean Thursday or Sunday), plus the payment going in a circle, a seller bidding in its own auction, the difference between maintenance and downtime, P1 overriding, and measuring post-maintenance value.
- **I13:** planned maintenance is bought, not insured, and downtime insurance must not make failure cheaper than maintenance.
- **Also updated:** P3, P4, P8, S11, the `DESIGN.md` table, and Q9 (resolved in principle; remaining sub-questions listed).

**v0.5 (2026-09-13)**
- **P5:** the foundry is also paid for time it can't provide, through downtime insurance it buys as a running cost.
- **New I13:** downtime insurance (bought by the foundry, pays the market value of lost time) and step insurance (bought by customers, pays refunds, lost wafers and rework). Includes a worked example and the interactions to think through:
  - whether the customer is charged for time the foundry can't provide
  - double payment
  - the foundry gaining from its own failures
  - manipulation of "market value"
  - planned maintenance not being insurable
  - cause disputes between insurers
  - correlated claims
  - rework at auction prices
- **Updated to match:** P4, P6, I4, I12, S6, S7, S11, S12, the `DESIGN.md` table, and Q9 and Q13. There is a new Q14, and missing principles moved to Q15.

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
