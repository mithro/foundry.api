# Industry parallels: is the software analogy load-bearing? (`PAR`)

`WHY.md` argues that chip manufacturing is stuck where software was before cheap experimentation, and that opening it up will do for chips what the internet, open source, cloud computing and machine learning did for software. This file tests that claim in both directions.

It is written to be read by an adversarial reviewer. The conclusion is **not** that the analogy holds. Of the four analogues, one is load-bearing in a narrow and specific way, two are illustrative only, and one points the other way — it is better evidence *for* the doom spiral than against it.

**ID prefix:** `PAR`. Entries follow the format in [`../README.md`](../README.md). This file does not edit any other file; see the last section for changes that belong elsewhere.

**Date compiled:** 2026-09-18.

---

## Contents

- [Part 1. Cycle time: the missing number](#part-1-cycle-time-the-missing-number)
- [Part 2. The four analogues](#part-2-the-four-analogues)
- [Part 3. Physical industries that opened up](#part-3-physical-industries-that-opened-up)
- [Part 4. The counter-case](#part-4-the-counter-case)
- [Part 5. Adjudication](#part-5-adjudication)
- [Part 6. Open questions](#part-6-open-questions)
- [Changes needed in other files](#changes-needed-in-other-files)

---

## Part 1. Cycle time: the missing number

`WHY.md` never mentions cycle time. It is the first-order determinant of how often a customer can come back, and it is where the software analogy fails hardest. Before this file there was no cycle-time evidence anywhere in this repository.

### PAR-1. Fab cycle time per mask layer varied from 1.8 to 4.1 days across 28 fabs

- **Source:** Robert C. Leachman and David A. Hodges, "Benchmarking Semiconductor Manufacturing", Competitive Semiconductor Manufacturing Program, Engineering Systems Research Center, University of California at Berkeley. <https://microlab.berkeley.edu/csm/IRWpaper.PDF>
- **Verification:** Verified 2026-09-18 (PDF text extracted and read).
- **What it says:**
  - The study covered "28 wafer fabrication facilities in the United States, the United Kingdom, Germany, Spain, Japan, Korea and Taiwan", with participants including Intel, IBM, Samsung, TSMC, UMC, Toshiba, Motorola and Texas Instruments. "The time interval covered is from the middle of 1992 to the middle of 1995."
  - Table 2, memory fabs, "Cycle time per mask layer (days)": **best 1.8, average 2.9, worst 4.1**.
  - The metrics are normalised to "twenty mask layers" — that was the reference process complexity of the period.
  - The spread across fabs was large on every metric: "important quantitative indicators of productivity, including defect density (yield), major equipment production rates, wafer throughput time, and effective new process introduction to manufacturing, vary by factors of 3 to as much as 5 across an international sample of 28 fabs."
  - The paper also records that the fabs varied in size "by a factor of almost fifty" in wafer starts, and that "Large fabs lead almost every one of our labor and equipment productivity metrics, although fab size above 7,000 wafer starts per week does not improve performance."
- **Bears on:**
  - H9 (context): this is the classic measurement of how much fabs differ, and the study's whole purpose was to find which *practices* explain the difference — evidence that process knowledge is the scarce thing.
  - H4, H5 (challenges): fixes the scale of the wait.
  - H3 (mixed): "fab size above 7,000 wafer starts per week does not improve performance" is a limit on the returns to scale that Step 3 of the doom spiral assumes.
- **Used in:** not yet.
- **Caveats:** the data is from 1992–1995. Its value here is as the *historical baseline* for PAR-2, not as a current figure. The paper is a conference-style summary of a larger programme; it does not name which fab scored what.

- **DERIVED (arithmetic shown):** at the average of 2.9 days per mask layer and the paper's own 20-layer normalisation, a wafer lot took 2.9 × 20 = **58 days** in the fab, ignoring mask making, assembly and test. At the best score, 1.8 × 20 = **36 days**.

### PAR-2. Fab cycle time has got *longer* per chip as nodes advanced, from about 40 days at 28nm to about 100 days at 5nm

- **Source:** Mark LaPedus, "Battling Fab Cycle Times", *Semiconductor Engineering*, 2017-02-16. <https://semiengineering.com/battling-fab-cycle-times/>
- **Verification:** Verified 2026-09-18. Page fetched and quotes matched against the raw HTML; the publication date is taken from the page's own `datePublished` metadata, `2017-02-16T08:05:38+00:00`.
- **What it says:**
  - "Cycle time is the amount of time it takes to process a wafer lot in a fab from start to finish. Typically, a wafer lot consists of 25 wafers … An advanced logic process could have from 600 to 1,000 steps or more."
  - Quoting Robert Leachman, "a professor of industrial engineering and operations research" (the same author as PAR-1): "Generally, the most common metric for cycle time in the fab is 'days per mask layer.' On average, a fab takes 1 to 1.5 days to process a layer. The best fabs are down to 0.8 days, Leachman said."
  - "A 28nm device has 40 to 50 mask layers. In comparison, a 14nm/10nm device has 60 layers, with 7nm expected to jump to 80 to 85. 5nm could have 100 layers. So, using today's … techniques, the cycle times are increasing from roughly 40 days at 28nm, to 60 days at 14nm/10nm, to 80 to 85 days at 7nm. 5nm may extend to 100 days using today's techniques".
  - Leachman again, on the direction of travel: "The cost per memory cell or transistor is still coming down. It's probably coming down a lot slower than it used to as we move toward the end of Moore's Law … But the speed at which we get them is not coming down. It's going up. That's the big challenge."
  - Masks add their own wait. Citing the eBeam Initiative Mask Makers Survey, mask turnaround time (TAT) is "about 7.28 days for a 28nm mask"; "TATs jumped to 12.82 days for a 16nm/20nm mask"; "TATs fell to 8.67 days for a 14nm mask"; "At 10nm/7nm, though, the TAT is expected to increase to 9.52 days".
  - Why queueing dominates: "the biggest contributor to cycle times is wait times", and, from M. Lercel of ASML, "If you run a fab at a very low utilization rate, you can run at raw processing times. But the higher utilization y[ou run at]…" — a fab that is kept busy is a fab that is slow.
  - Cycle time is expensive to the fab as well as the customer. R. Cappel of KLA-Tencor: "Every day that I'm in a fab, it costs me more money to produce that chip."
- **Bears on:**
  - H4 and H5 (challenges): cheap is not the same as fast. Even if NRE falls to zero, a customer gets a small number of attempts per year.
  - H1 (supports, by a route the essay does not use): the leading edge is getting slower as well as more expensive.
  - H9 (challenges): learning by experiment is bounded by how fast experiments complete, and that rate is getting worse at the leading edge.
  - H6 (context): "Every day that I'm in a fab, it costs me more money" is the fab's side of the same fact — idle work-in-progress is cost, so a fab that is fast is a fab that is under-utilised.
- **Used in:** not yet.
- **Caveats:**
  - Trade press, not a peer-reviewed study — but the central numbers are attributed to a named academic who is the author of the primary benchmarking study in PAR-1, which is the strongest available cross-check.
  - The 2017 projections for 7nm and 5nm were forward-looking; EUV lithography was expected to reduce layer counts and the article says so. We have **not** found a post-EUV measurement. Treat the 80–100 day figures as the article's projection, not as observed fact.
  - The mask TAT numbers are from an industry survey of mask makers, reported second-hand.

- **DERIVED (arithmetic shown):** comparing PAR-1 (1992–1995) with PAR-2 (2017):
  - **Days per mask layer improved:** average 2.9 → 1 to 1.5; best 1.8 → 0.8. Roughly a two-fold improvement in 22 years.
  - **End-to-end fab cycle time did not:** 2.9 × 20 layers = 58 days then; 40 to 50 layers at 28nm at ~1.25 days = 50 to 63 days. Essentially unchanged.
  - Over the same period the deploy cycle in software went from days or weeks to seconds. **The per-unit metric improved in both industries; the thing the customer actually waits for improved by about 10^6 in one and not at all in the other.**

### PAR-3. A shared academic shuttle quotes a 106-day lead time and runs twice a year

- **Source:** EUROPRACTICE IC Service, "2020 MINI@SIC EUROPRACTICE MPW RUN SCHEDULE AND PRICELIST", version 201015 – v6. <https://europractice-ic.com/wp-content/uploads/2020/10/Miniasic-MPW-EUROPRACTICE-201015-v6.pdf>
- **Verification:** Verified 2026-09-18 (PDF downloaded and text extracted; all quotes and prices read from the document).
- **What it says:**
  - The "Microblock" offer on TSMC 28nm HPC/HPC+ gives a designer 1 mm² of silicon. Its published terms are: "Designed area: 1110µm x 1110µm."; "**Lead time of 106 days, including tapeout preparation.**"; "100 parts per participation."; "**2 runs per year** with timing tuned towards key conferences."
  - Booking is not casual: "Microblock and mini@sic reservations/registrations should be done no later than **4 months before the deadline**." For several TSMC technologies, "please make reservation 4 months in advance."
  - Withdrawal is penalised: "Withdrawal of the Microblock or mini@sic block later than one week before the deadline is subject to a penalty of 50% of the amount due."
  - Run frequency in 2020, counted from the schedule tables: TSMC 0.18µm general purpose 3 runs; TSMC 65nm 4 runs; TSMC 40nm 2 runs; TSMC 28nm HPC 2 runs and HPC+ 2 runs; GlobalFoundries 22nm FDSOI 3 runs; UMC 65nm 3 runs; X-FAB XH018 2 runs.
  - Prices per block, standard / discounted (discounted requires the customer to be an academic or publicly funded research body in an eligible country and a paid-up EUROPRACTICE member): TSMC 0.18µm €3,100 / €2,640; TSMC 65nm €12,550 / €11,820; TSMC 40nm €16,880 / €15,880; TSMC 28nm €15,850 / €13,650; TSMC 28nm **Microblock €9,750 / €7,650**; GF 130nm BCDlite €5,900 / €4,900; GF 22nm FDSOI €29,900 / €24,900.
  - What "cheapest possible" buys: for TSMC at 65nm and 28nm, "100 samples"; for TSMC 0.18µm, "40 samples".
- **Bears on:**
  - H4 (mixed): a real published price for a first chip, far below a dedicated mask set — but €7,650 is not $0, and the discounted price is not available to a commercial customer.
  - H5 (challenges), H6 (context): **2 runs a year on 28nm is the ceiling on how often a small customer can iterate.**
  - H8 (supports): prices and schedules are published openly, with no negotiation, which is exactly the model `WHY.md` §5 asks for — and it has existed since the 1990s without producing the explosion `WHY.md` predicts.
- **Used in:** not yet.
- **Caveats:**
  - This is the 2020 price list, chosen because it is the version that states the lead time numerically. The 2026 schedules exist at <https://europractice-ic.com/schedules-prices-2026/> and show more runs per year on TSMC 65nm and 28nm, but the run-count reading for 2026 is **Partial**: it came from an automated read of the schedule page, not from the underlying PDFs, and the current TSMC PDF link published on that page returned 404 when fetched directly.
  - EUROPRACTICE is a subsidised European service. Its prices are not a commercial foundry's prices.
  - "Lead time" here is from tape-out preparation to delivery of unpackaged, untested die. "Prices are given for the delivery of unpackaged, untested prototypes. Encapsulation and testing will be charged separately."

### PAR-4. The cheapest open shuttle in the world takes 7.5 to 15 months from close to chips in hand

- **Source:** Tiny Tapeout, "Chips" / runs table. <https://tinytapeout.com/runs/> (page also served at <https://tinytapeout.com/chips/>)
- **Verification:** Verified 2026-09-18. The full table was read from the page source. The page's own `dateModified` is `2026-09-15T20:16:23+01:00`.
- **What it says:** the published columns are "Run", "Launched", "Closed", "Shuttle", "Designs", "Chips expected", "Estimated delivery date". Selected rows, exactly as published:
  | Run | Launched | Closed | Designs | Delivery |
  |---|---|---|---|---|
  | TT02 | 2022-11-09 | 2022-12-02 | 165 | Shipped 2024-01-25 |
  | TT03 | 2023-03-01 | 2023-04-23 | 100 | Shipped 2024-03-28 |
  | TT04 | 2023-07-01 | 2023-09-08 | 143 | Shipped 2024-05-24 |
  | TT05 | 2023-09-11 | 2023-11-04 | 174 | Shipped 2024-07-05 |
  | TT06 | 2024-01-30 | 2024-04-19 | 238 | Shipped 2024-12-07 |
  | TT07 | 2024-04-22 | 2024-06-01 | 120 | Shipped 2025-01-15 |
  | TT08 | 2024-06-10 | 2024-09-06 | 135 | Shipped 2025-12-01 |
  | TT09 | 2024-09-07 | 2024-11-10 | 369 | TBD |
  | TT10 | 2024-11-11 | Cancelled | – | – |
  | TTIHP25a | 2025-03-12 | 2025-03-28 | 547 | 2026-05-31 |
  | TTSKY26c | 2026-05-26 | 2026-09-07 | 242 | 2027-05-12 |
- **Bears on:**
  - H4, H5 (challenges): this is the *most* favourable case in existence — the cheapest slot, the smallest design, an open PDK, a programme built for beginners — and it still takes the better part of a year.
  - H5 (supports, separately): see PAR-5 for the demand side.
  - H9 (challenges): a learning loop that closes once a year is a slow learning loop.
- **Used in:** not yet.
- **Caveats:** the delivery dates are as Tiny Tapeout publishes them; future rows are estimates and are labelled as such here. Tiny Tapeout is a shared-block programme riding on other people's shuttles, so its wait includes the host shuttle's schedule, not just fab cycle time.

- **DERIVED (arithmetic shown):** days from "Closed" to the published shipping date, for the seven runs that have actually shipped:
  | Run | Closed → shipped | Days | Weeks | Months |
  |---|---|---|---|---|
  | TT02 | 2022-12-02 → 2024-01-25 | 419 | 59.9 | 13.8 |
  | TT03 | 2023-04-23 → 2024-03-28 | 340 | 48.6 | 11.2 |
  | TT04 | 2023-09-08 → 2024-05-24 | 259 | 37.0 | 8.5 |
  | TT05 | 2023-11-04 → 2024-07-05 | 244 | 34.9 | 8.0 |
  | TT06 | 2024-04-19 → 2024-12-07 | 232 | 33.1 | 7.6 |
  | TT07 | 2024-06-01 → 2025-01-15 | 228 | 32.6 | 7.5 |
  | TT08 | 2024-09-06 → 2025-12-01 | 451 | 64.4 | 14.8 |

  Range **228 to 451 days**; mean 310 days. The fastest shuttle ever run by the cheapest open silicon programme in the world delivered in **7.5 months**. TT09 closed on 2024-11-10 and its delivery is still published as "TBD" as of the page's last modification on 2026-09-15 — **more than 22 months** after close, with no chips.

- **DERIVED (the comparison that matters):** a software team using a cloud provider can deploy, observe and revert many times an hour. Take a conservative 10 deploys per working day: 10 × 250 = 2,500 attempts a year. A Tiny Tapeout customer gets **1 to 2 attempts a year**. That is a ratio of roughly **10^3**. A EUROPRACTICE 28nm Microblock customer gets **2 a year** (PAR-3). This is the single largest quantitative gap between the analogy and the thing it is an analogy for, and `WHY.md` does not mention it.

### PAR-5. Free and cheap shuttles are oversubscribed: 360 designs manufactured out of more than 600 submissions

- **Source:** Aaron Cunningham, "Open source PDKs joining the Linux Foundation's CHIPS Alliance", *Google Open Source Blog*, Wednesday, November 8, 2023. Original URL <https://opensource.googleblog.com/2023/11/open-source-pdks-joining-linux-foundation-chips-alliance.html>; read via the Internet Archive capture of 2026-04-16 at <http://web.archive.org/web/20260416232123/https://opensource.googleblog.com/2023/11/open-source-pdks-joining-linux-foundation-chips-alliance.html>
- **Verification:** Verified 2026-09-18 against the archived capture. The live URL redirected our fetch to a Google bot-check page, which we did not attempt to pass; the Wayback capture was used instead.
- **What it says:**
  - "Since its inception, the program has launched eight shuttle runs on SKY130 and an initial test run on GF180MCU, the last of which are being packaged now. With 40 slots per shuttle, we've manufactured 360 designs out of over 600 submissions from 19 countries around [the world]."
  - "Low-cost manufacturing options will continue to be available through this transition, both through commercial shuttle offerings like Efabless' ChipIgnite program and also through educational efforts like [Tiny Tapeout]."
- **Bears on:**
  - H5 (supports): this is the best direct evidence in the repository of *latent* demand. When the price of a tape-out was set to zero, demand exceeded supply by roughly 1.7 times even with a rationing process.
  - H4 (supports): 600+ submissions is 600+ designs that existed and would not otherwise have been made.
- **Used in:** not yet.
- **Caveats:**
  - The slots were **free**, paid for by Google. Demand at a price of zero says little about demand at €7,650 or at a commercial price. This is the central weakness of the datum and it should not be glossed.
  - "over 600 submissions" is Google's own count of its own programme, with no published methodology; submissions are not necessarily distinct teams.
  - The programme's commercial successor, Efabless, later shut down (OPEN-7).

- **DERIVED:** 360 manufactured ÷ 600 submitted = **60% acceptance**, i.e. the free shuttle was oversubscribed by about 1.7 times. Tiny Tapeout's published table (PAR-4) gives a separate demand series: summing the "Designs" column across the 19 closed shuttles listed gives **4,049 designs**, rising from 152 on TT01 (closed 2022-09-01) to 547 on TTIHP25a (closed 2025-03-28).

### PAR-6. 95% of chip projects now need a respin — so each attempt costs a full cycle time and is usually not the last

- **Sources:**
  - Harry Foster, "The 2026 Functional Verification Study: Evidence of a New Verification Operating State", *Verification Horizons* (Siemens Digital Industries Software), 2026-09-08. <https://blogs.sw.siemens.com/verificationhorizons/2026/09/08/the-2026-functional-verification-study/>
  - Harry Foster, "Part 12: The 2020 Wilson Research Group Functional Verification Study", *Verification Horizons*, 2021-02-03. <https://blogs.sw.siemens.com/verificationhorizons/2021/02/03/part-12-the-2020-wilson-research-group-functional-verification-study/>
- **Verification:** Verified 2026-09-18 for the quoted sentences (both pages fetched). The underlying Wilson Research Group study methodology and sample size were **not** read; that part is **Partial**.
- **What it says:**
  - 2026 study: "Among IC/ASIC respondents, only 5% reported first-silicon success in 2026, compared with 14.4% in 2024." And: "The broader spin distribution reinforces the same pattern, with the overwhelming majority of respondents reporting multiple spins before production."
  - 2020 study: "only about 32 percent of today's projects are able to achieve first silicon success", alongside "the number of required spins before production has not increased".
- **Bears on:**
  - H4 (challenges): the up-front cost of a chip is not one tape-out. On the 2026 figure it is, in expectation, several.
  - H5, H6 (challenges): a customer who needs three attempts at 6 to 12 months each needs two to three *years* and three times the money.
  - H1 (supports): rising respin rates are another force pushing chip-making towards those who can afford to fail repeatedly.
- **Used in:** not yet.
- **Caveats:**
  - This is a vendor-run survey (Siemens EDA sponsors the Wilson Research Group study). It is self-reported by verification engineers, who are a population with an interest in the problem looking large. The response base is not stated in the blog posts we read.
  - The sharp fall from 32% (2020) to 14.4% (2024) to 5% (2026) is steep enough to suspect a change in sample or question wording. We could not check this. Treat the *direction* as better supported than the exact levels.
  - The figures cover IC/ASIC projects generally, weighted towards complex commercial designs, not towards the small mature-node designs an open fab would serve. The respin rate for a Tiny Tapeout-scale design is unknown and probably different.

---

## Part 2. The four analogues

*(filled in below)*

---

## Part 3. Physical industries that opened up

*(filled in below)*

---

## Part 4. The counter-case

*(filled in below)*

---

## Part 5. Adjudication

*(filled in below)*

---

## Part 6. Open questions

*(filled in below)*

---

## Changes needed in other files

*(filled in below)*
