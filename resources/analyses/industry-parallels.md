# Industry parallels: is the software analogy load-bearing? (`PAR`)

`WHY.md` argues that chip manufacturing is stuck where software was before cheap experimentation, and that opening it up will do for chips what the internet, open source, cloud computing and machine learning did for software. This file tests that claim in both directions.

It is written to be read by an adversarial reviewer. The conclusion is **not** that the analogy holds. Of the four analogues, one is load-bearing in a narrow and specific way, two are illustrative only, and one points the other way — it is better evidence *for* the doom spiral than against it.

**ID prefix:** `PAR`. Entries follow the format in [`../README.md`](../README.md). This file does not edit any other file; see the last section for changes that belong elsewhere.

**Date compiled:** 2026-09-18.

---

## Contents

- [Part 1. Cycle time: the missing number](#part-1-cycle-time-the-missing-number)
- [Part 2. The four analogues](#part-2-the-four-analogues)
- [Part 3. Physical industries: the coupling, the successes and the failures](#part-3-physical-industries-the-coupling-the-successes-and-the-failures)
- [Part 4. The counter-case on the long tail](#part-4-the-counter-case-on-the-long-tail)
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

### PAR-3. A shared academic shuttle: about 6 months from booking to chips, 1 to 5 chances a year, and the wait gets longer at finer nodes

The single best cycle-time dataset we found, because EUROPRACTICE publishes both ends of the schedule for every run, so the lead times can be computed rather than asserted.

- **Sources:**
  - EUROPRACTICE IC Service, "TSMC RUN SCHEDULE 2026", January 26, 2026 – v1.3c (the mini@sic schedule). <https://europractice-ic.com/wp-content/uploads/2025/11/TSMC_EPmini@sicschedule2026V1_3c.pdf>
  - EUROPRACTICE IC Service, "2020 MINI@SIC EUROPRACTICE MPW RUN SCHEDULE AND PRICELIST", version 201015 – v6. <https://europractice-ic.com/wp-content/uploads/2020/10/Miniasic-MPW-EUROPRACTICE-201015-v6.pdf>
- **Verification:** Verified 2026-09-18 (both PDFs downloaded and their text extracted; all dates, quotes and prices read from the documents).

#### The 2026 schedule

- **What it says:** the published columns are "Technology", "Month", "Run", "Foundry ref", "Fab", "Reserve before", "Signed quote/PO before", "Dry run GDS", "Final GDS", "Tape-out", "Estimated shipment date". Notes attached to the tables:
  - "Shipment date is an estimation. Additional cycle time of (1~3 weeks) might be required."
  - "The estimated shipment date is applicable for reservations with quantity <200 dies. If additional samples are required, additional cycle time of (1~3 weeks) might be needed."
  - "Cycle time estimates are based on typical conditions. Corner wafers or SHDMiM processing requires additional cycle time."
  - Optional services that add still more: "Lead free & cupper bumping: 4 days"; "Extra wafer thinning (thinner than 10mils): up to 12 days".
  - Booking is committing: "Single reservation for multiple chips"; "No backup reservation".

- **DERIVED (arithmetic shown, computed with a script from the published dates):**

  | Technology | Runs in 2026 | Tape-out → estimated shipment | Reserve-before → estimated shipment |
  |---|---|---|---|
  | 0.13 µm BCD Plus | 1 | 62 days | 170 days |
  | 65 nm CMOS | 5 | 73 days | 189–202 days |
  | 40 nm Logic / MS-RF | 2 | 72 days | 192–194 days |
  | 28 nm RF HPC Plus | 5 | 82 days | 189–200 days |
  | 16 nm RF FinFET Compact | 2 | 85 days | 199–224 days |

  Three things fall out of this table, and all three matter.
  1. **The end-to-end wait is about six months**, every time, on every node — 170 to 224 days from the booking deadline to estimated shipment, before the "1~3 weeks" of slack the schedule itself warns about.
  2. **The number of chances per year is 1 to 5.** Not thousands. Not hundreds. On 16 nm it is two.
  3. **Tape-out to shipment gets monotonically longer at finer nodes**: 62 → 73 → 72 → 82 → 85 days from 0.13 µm to 16 nm. This is an independent, current, primary-source confirmation of PAR-2's claim that cycle time rises with node, measured from a published schedule rather than from an interview.

#### The 2020 schedule (the numeric lead-time statement and the prices)

- **What it says:**
  - The "Microblock" offer on TSMC 28nm HPC/HPC+ gives a designer 1 mm² of silicon. Its published terms are: "Designed area: 1110µm x 1110µm."; "**Lead time of 106 days, including tapeout preparation.**"; "100 parts per participation."; "**2 runs per year** with timing tuned towards key conferences."
  - Booking is not casual: "Microblock and mini@sic reservations/registrations should be done no later than **4 months before the deadline**." For several TSMC technologies, "please make reservation 4 months in advance."
  - Withdrawal is penalised: "Withdrawal of the Microblock or mini@sic block later than one week before the deadline is subject to a penalty of 50% of the amount due."
  - Run frequency in 2020, counted from the schedule tables: TSMC 0.18µm general purpose 3 runs; TSMC 65nm 4 runs; TSMC 40nm 2 runs; TSMC 28nm HPC 2 runs and HPC+ 2 runs; GlobalFoundries 22nm FDSOI 3 runs; UMC 65nm 3 runs; X-FAB XH018 2 runs.
  - Prices per block, standard / discounted (discounted requires the customer to be an academic or publicly funded research body in an eligible country and a paid-up EUROPRACTICE member): TSMC 0.18µm €3,100 / €2,640; TSMC 65nm €12,550 / €11,820; TSMC 40nm €16,880 / €15,880; TSMC 28nm €15,850 / €13,650; TSMC 28nm **Microblock €9,750 / €7,650**; GF 130nm BCDlite €5,900 / €4,900; GF 22nm FDSOI €29,900 / €24,900.
  - What "cheapest possible" buys: for TSMC at 65nm and 28nm, "100 samples"; for TSMC 0.18µm, "40 samples".
- **Bears on:**
  - H4 (mixed): a real published price for a first chip, far below a dedicated mask set — but €7,650 is not $0, and the discounted price is not available to a commercial customer.
  - **H5 (challenges), H6 (context): 1 to 5 runs a year is the ceiling on how often a small customer can iterate**, and roughly six months is the wait each time.
  - H8 (supports): prices and schedules are published openly, with no negotiation, which is exactly the model `WHY.md` §5 asks for — and it has existed since the 1990s without producing the explosion `WHY.md` predicts. **That is the most awkward single fact in this file for the essay's argument:** the open, published-price, self-service, many-small-customers shuttle model already exists, has existed for three decades, and has not transformed the industry.
- **Used in:** not yet.
- **Caveats:**
  - EUROPRACTICE is a subsidised European service, and its discounted prices require the customer to be an academic or publicly funded body. Its prices are not a commercial foundry's prices.
  - "Lead time" and "estimated shipment" are to delivery of unpackaged, untested die: "Prices are given for the delivery of unpackaged, untested prototypes. Encapsulation and testing will be charged separately."
  - Shipment dates in the 2026 schedule are EUROPRACTICE's own estimates, and the document says so.
  - The 2020 prices are five years stale; we quote them for scale, not as current.
  - **Blocked:** the general (non-mini@sic) TSMC MPW schedule for 2026, at <https://europractice-ic.com/wp-content/uploads/2025/11/TSMC_EP_MPW_schedule_2026_V1_3b.pdf>, 404s; the version linked from the 2026 schedules page downloads but is an image-only PDF with no extractable text, so we could not read the general-MPW dates. The mini@sic schedule above is what we could verify.

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

Taken in order of how close they are to the claim, not in the order `WHY.md` uses them: cloud computing first, because it is the analogue the project itself says is closest; the internet last, because it is the one used most rhetorically and least mechanically.

### 2.1 Cloud computing

This is the analogue the project leans on hardest, and the one that most rewards a hard look. The surface fit is excellent: a huge fixed-cost asset, rented by the hour, at published prices, to people who could never buy one. The evidence below says the *access model* transferred and the *customer mix* did not.

#### PAR-7. AWS's money is in multi-year commitments, not in the pay-as-you-go tail

- **Sources:**
  - Amazon.com, Inc., Form 10-Q for the quarterly period ended June 30, 2025. <https://www.sec.gov/Archives/edgar/data/1018724/000101872425000086/amzn-20250630.htm>
  - Amazon.com, Inc., "Amazon.com Announces Fourth Quarter Results", 2026-02-05 (Q4 and full-year 2025 earnings release). <https://s2.q4cdn.com/299287126/files/doc_earnings/2025/q4/earnings-result/AMZN-Q4-2025-Earnings-Release.pdf>
- **Verification:** Verified 2026-09-18. The 10-Q paragraph was read from the SEC filing; the earnings release PDF was downloaded and its text read directly. Note: `www.sec.gov` refuses plain command-line fetches ("Your Request Originates from an Undeclared Automated Tool"); the filing was read through our fetch tool, which the site does serve.
- **What it says:**
  - 10-Q, Q2 2025: "Additionally, we have performance obligations, primarily related to AWS, associated with commitments in customer contracts for future services that have not yet been recognized in our consolidated financial statements. For contracts with original terms that exceed one year, those commitments not yet recognized were approximately $195 billion as of June 30, 2025. The weighted-average remaining life of our long-term contracts is 4.0 years."
  - Earnings release: "AWS segment sales increased 24% year-over-year to $35.6 billion" in Q4 2025, and for the full year "AWS segment sales increased 20% year-over-year to $128.7 billion". "AWS segment operating income was $45.6 billion, compared with operating income of $39.8 billion in 2024."
  - Amazon's own XBRL tagging of `RevenueRemainingPerformanceObligation` stops after Q2 2020 (last tagged value $41.0 billion at 2020-06-30, from the Q2 2020 10-Q), so the series has to be read out of the filing text rather than the structured data.
- **Bears on:**
  - H6 (challenges), H7 (challenges): the cloud is held up as proof that you can build a huge infrastructure business on many small self-serve customers. Its own disclosures say the revenue base is contracted, long-dated and large.
  - H8 (context): published pay-as-you-go pricing is the *front door*, not the revenue model.
- **Used in:** not yet.
- **Caveats:**
  - Remaining performance obligations are not the same as revenue share by customer size. Amazon does not disclose revenue by customer, or any customer-concentration figure for AWS. It is possible that a large number of mid-sized customers, not a few giants, sign these contracts. We cannot tell from the filing and should not pretend otherwise.
  - The phrase is "primarily related to AWS", so the $195 billion is not purely AWS.
  - The 10-Q figure (June 2025) and the revenue figure (full-year 2025) are from different periods; the derived ratio below is therefore approximate and is labelled as such.

- **DERIVED (arithmetic shown):** $195bn of commitments not yet recognised ÷ $128.7bn AWS net sales for 2025 = **1.5 years of AWS revenue already committed** under contracts with original terms longer than a year, at a weighted-average remaining life of 4.0 years. The comparison mixes a mid-2025 balance with a full-year 2025 flow and is indicative only.

#### PAR-8. Cloud committed-use discounts are paid whether or not the capacity is used

- **Source:** Google Cloud, "Committed use discounts (CUDs) for Compute Engine" (Compute Engine documentation). <https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview>
- **Verification:** Verified 2026-09-18.
- **What it says:**
  - "You get a discount of up to 70% for memory-optimized machine series and a discount of up to 55% for all other machine series."
  - "You are billed monthly for your committed resources until the end of your commitment term, regardless of whether or not you use those resources."
  - Terms are "either 1 year or 3 years", and a "3-year plan offers a higher discount rate than a 1-year plan."
- **Bears on:**
  - H6 (context), H7 (challenges): this is a **take-or-pay contract**. It is the same instrument as the AMD/GlobalFoundries wafer agreement in `WHY.md` §3, which the essay presents as a symptom of the doom spiral. The largest, most successful "rent the expensive machine" businesses in the world converged on it voluntarily.
- **Used in:** not yet. Extends SW-5, which covers AWS reserved instances but not the obligation to pay for unused capacity, and not a second provider.
- **Caveats:** a documentation page, not a filing. It states list terms; actual enterprise agreements are negotiated and not public.

#### PAR-9. CoreWeave — the purest "rent the expensive machine by the hour" business — is 67% one customer and 98% take-or-pay

- **Source:** CoreWeave, Inc., Form 10-K for the fiscal year ended December 31, 2025. <https://s205.q4cdn.com/133937190/files/doc_financials/2025/q4/CoreWeave-Inc-FY25-10-K-7.pdf> (also filed at <https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm>)
- **Verification:** Verified 2026-09-18 (PDF downloaded, text extracted, all quotes read in place).
- **What it says:**
  - Risk factor heading: "A substantial portion of our revenue is driven by a limited number of our customers, and the loss of, or a significant reduction in, spending from one or a few of our top customers would adversely affect our business, operating results, financial condition, and prospects."
  - "We recognized an aggregate of approximately 67% of our revenue from our top customer, Microsoft, for the year ended December 31, 2025. We recognized an aggregate of approximately 77% of our revenue from our top two customers for the year ended December 31, 2024. We recognized an aggregate of approximately 73% of our revenue for the year ended December 31, 2023, from our top three customers. None of our other customers represented 10% or more of our revenue for the year ended December 31, 2025."
  - The Customer Concentration note gives the table: Customer A 67% (2025), 62% (2024), 35% (2023); Customer B 15% (2024), 17% (2023); Customer C 21% (2023). "Customer A and D accounted for 68% and 11% of accounts receivable, net, respectively, as of December 31, 2025."
  - On the contract form: "We currently sell access to our platform either through committed contracts, which are take-or-pay, or on-demand, which are pay-as-you-go. For the years ended December 31, 2025, 2024, and 2023, committed contracts accounted for over 98%, 96% and 88% of our revenue, respectively."
  - And why it will persist: "We expect that our customer concentration with a limited number of top customers is likely to continue in future years because of the long-term nature of contracts with those customers."
  - Scale: "Our revenue was $5.1 billion, $1.9 billion, and $229 million for the years ended December 31, 2025, 2024, and 2023, respectively", with "net losses of $1.2 billion, $863 million, and $594 million" in the same years. "As of December 31, 2025, we had $60.7 billion of remaining performance obligations ("RPO"), compared to $15.1 billion of RPO as of December 31, 2024. As of December 31, 2025, our committed contracts had a weighted-average contract duration of approximately five years."
  - Named forward commitments: OpenAI "committed to pay us up to approximately $6.5 billion through May 31, 2031"; Meta Platforms, Inc. "initially committed to pay us up to approximately $14.2 billion through December 2031".
- **Bears on:**
  - **H7 (challenges, strongly).** This is the central hypothesis — that many small customers remove buyer power — and here is a company that rents an extremely expensive shared physical asset by the hour, founded in the pay-as-you-go era, with published on-demand prices, that ended up *more* concentrated than TSMC. TSMC's top ten are 78% of revenue (CONC-11); CoreWeave's top **one** is 67%.
  - **H2 (supports):** its own risk factors read like GlobalFoundries' and SkyWater's.
  - **H6 (challenges):** the on-demand pay-as-you-go tail is under 2% of revenue.
  - H10 (challenges): being paid for every attempt is not what happened; being paid by three hyperscalers is.
- **Used in:** not yet.
- **Caveats:**
  - CoreWeave sells GPU capacity in an extraordinary demand spike, which may be a phase rather than an equilibrium. The 2023 → 2025 trend is towards *more* concentration, not less, but three years is a short series.
  - It is a young company still raising capital; a mature CoreWeave might look different.
  - The 88% → 96% → 98% committed-contract series could reflect deliberate strategy (financing capex against contracts) rather than an absence of small-customer demand. The filing does not separate the two.

- **DERIVED:** RPO $60.7bn ÷ 2025 revenue $5.1bn = **about 12 years of current revenue already contracted**, at a weighted-average duration of about five years.

#### PAR-10. The largest publicly announced cloud contract is one customer at $38 billion over seven years

- **Source:** Amazon, "AWS announces new partnership to power OpenAI's AI workloads" (About Amazon). <https://www.aboutamazon.com/news/aws/aws-open-ai-workloads-compute-infrastructure>
- **Verification:** Partial, 2026-09-18. The quotes below were read from the page. The page as served to us did not carry a machine-readable publication date; contemporaneous reporting dates the announcement to 2025-11-03, which we have **not** verified against a primary source.
- **What it says:** "Under this new $38 billion agreement, which will have continued growth over the next seven years", "OpenAI is accessing AWS compute comprising hundreds of thousands of state-of-the-art NVIDIA GPUs, with the ability to expand to tens of millions of CPUs".
- **Bears on:** H7 (challenges): the mature cloud's headline commercial event is a single whale, not the tail.
- **Used in:** not yet.
- **Caveats:** a press release, with no contract terms disclosed. "$38 billion" is a headline number whose recognition profile is unknown.

- **DERIVED:** $38bn ÷ 7 years ≈ $5.4bn a year, or about **4% of AWS's 2025 revenue of $128.7bn** (PAR-7) from one customer on one agreement.

#### PAR-11. The cloud buys its tail: AWS gives startups credits

- **Source:** Amazon Web Services, "AWS Activate". <https://aws.amazon.com/activate/>
- **Verification:** Partial, 2026-09-18. The credit figure was read from the page; the eligibility tiers and the programme's stated rationale were not stated on the page in the form we asked for.
- **What it says:** the page offers "up to $200,000 in AWS Activate Credits", with "additional credits available for AI startups ready to scale", described as offsetting costs "on infrastructure, data services, and AI/ML models".
- **Bears on:**
  - H6 (challenges): the tail is not simply profitable at published prices; the largest cloud provider pays to acquire it.
  - H5 (context): it does imply the provider believes the tail contains future large customers, which is `WHY.md` §5's third claim.
- **Used in:** not yet.
- **Caveats:** a marketing page. It says nothing about how many startups receive credits, the cost of the programme, or its return.

### 2.2 Open source software

SW-3 already records the Hoffmann, Nagle and Zhou demand-side value estimate. The entries here go to the parts of the open-source story the essay does not tell: who actually does the work, who pays for it, and what it did not fix. The mechanism that matters for our question is that **open source lowered the cost of *copying* work that had already been done**. Silicon has no copy operation, which is why this analogue transfers to chip *design* and not to chip *manufacturing*.

#### PAR-12. Most widely-used open source is written by a handful of people, not a crowd

- **Sources:**
  - F. Nagle, J. Dana, J. Hoffman, S. Randazzo and Y. Zhou, "Census II of Free and Open Source Software — Application Libraries", The Linux Foundation and The Laboratory for Innovation Science at Harvard, March 2022. <https://www.linuxfoundation.org/hubfs/Census%20II%20FINAL%202March2022.pdf>
  - F. Nagle, K. Powell, R. Zitomer and D. A. Wheeler, "Census III of Free and Open Source Software / Application Libraries", The Linux Foundation, December 2024. <https://www.linuxfoundation.org/hubfs/LF%20Research/lfr_censusiii_120424a.pdf>
- **Verification:** Verified 2026-09-18 (both PDFs fetched and read).
- **What it says:**
  - Census II, from over half a million observations: "Reviewing 49 of the top 50 non-npm projects from our lists, for commits in the year 2021, it was found that 23% of projects had one developer accounting for more than 80% of the lines of code (LOC) added. Further, 94% of projects had fewer than ten developers accounting for more than 90% of the LOC added. These findings are counter to the typically held belief that thousands or millions of developers are responsible for developing and maintaining FOSS projects. At a higher level, it was found that 136 developers were responsible for more than 80% of the LOC added to these 50 FOSS projects."
  - Census III, from "over twelve million observations": "Reviewing 47 of the top 50 non-npm projects from our version-agnostic direct list, for commits in the year 2023, it was found that 17% of projects had one developer accounting for more than 80% of commits authored. Further, 40% of projects had only one or two developers accounting for more than 80% of commits authored, 64% of projects had four or less developers accounting for more than 80% of commits authored, and 81% of projects had ten or less developers accounting for more than 80% of commits authored."
  - Census II on the fragility this creates: "Many of the Top 500 packages on our lists are hosted under individual developer accounts. The consequences of such heavy reliance upon individual developer accounts must not be discounted."
- **Bears on:**
  - H10 (supports): extremely skewed contribution, consistent with SW-3's "96% of the demand-side value is created by only 5% of OSS developers".
  - H9 (mixed): the open-source learning story is not "a million experiments"; it is a very small number of people doing the work in public. That weakens `WHY.md` §5's implicit model of open source as mass parallel experimentation, while strengthening the separate claim that *publishing* results multiplies their value.
- **Used in:** not yet.
- **Caveats:**
  - The two editions measure different things. Census II counts **lines of code added**; Census III counts **commits authored**. The apparent fall from 23% to 17% is partly a change of metric, not a change in the world. Do not present it as a trend.
  - Neither Census publishes a "N packages account for X% of all usage" statistic. Their concentration finding is about contributors per project. Do not let a usage-concentration number be attributed to Census.

#### PAR-13. Open source is mostly paid work, done by companies

- **Source:** The Linux Foundation, "2017 Linux Kernel Development Report". <https://www.linuxfoundation.org/hubfs/Reports/LinuxKernelReport_2017.pdf>
- **Verification:** Verified 2026-09-18 (PDF fetched and read).
- **What it says:**
  - "The top 10 contributors, including the groups 'unknown' and 'none,' make up just over 54 percent of the total contributions to the kernel; that is up slightly from the previous version of this report. It is worth noting that, even if one assumes that all of the 'unknown' contributors are working on their own time, well over 85 percent of all kernel development is demonstrably done by developers who are being paid for their work."
  - "Interestingly, the volume of contributions from unpaid developers has been in slow decline for many years. It was 14.6 percent in the 2012 version of this report, but is 8.2 percent this time around."
  - Top contributing companies, changes 4.8–4.13: Intel 13.1%, "none" 8.2%, Red Hat 7.2%, Linaro 5.6%, "unknown" 4.1%, IBM 4.1%, consultants 3.3%, Samsung 3.2%, SUSE 3.0%, Google 3.0%.
  - And a tail does exist: "But there is a 'long tail' of companies (nearly 500 of which do not appear in the above list) which have made significant changes since the 4.7 release."
- **Bears on:**
  - H4 (challenges, indirectly): the open-source analogy is often read as "volunteers made it free". The kernel's own numbers say the opposite — it is corporate R&D, coordinated in public. An open-silicon ecosystem on the same model would need the same corporate funding, and `WHY.md` does not say where that comes from.
  - H5 (context): a long tail of ~500 contributing companies exists alongside a concentrated head, which is the shape `WHY.md` §5 hopes for.
- **Used in:** not yet.
- **Caveats:** the report is from 2017. We could not reach a newer Linux Foundation kernel report carrying the paid/unpaid percentages; the 2020 "Kernel History Report" does not contain them. Treat the 85% as of 2017.

#### PAR-14. What open source did not fix: critical infrastructure maintained by one unpaid person

- **Sources:**
  - Nadia Eghbal, "Roads and Bridges: The Unseen Labor Behind Our Digital Infrastructure", Ford Foundation, 2016. <https://www.fordfoundation.org/media/2976/roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure.pdf>
  - Cyber Safety Review Board, "Review of the December 2021 Log4j Event", published 2022-07-11. <https://www.cisa.gov/sites/default/files/publications/CSRB-Report-on-Log4-July-11-2022_508.pdf>
- **Verification:** Verified 2026-09-18 (both PDFs fetched and read).
- **What it says:**
  - Eghbal on OpenSSL before Heartbleed: "By 2014, two-thirds of all Web servers were using OpenSSL"; "Despite the number of individuals and companies relying on their software, OSF never received more than $2,000 in donations per year. Gross revenues (which came from consulting and contract work) never broke $1M"; "There was enough to pay the salary of one developer, Stephen Henson. That meant that two-thirds of the Web relied on encryption software maintained by just one full-time employee."
  - S. Marquess, quoted by Eghbal: "The mystery is not that a few overworked volunteers missed this bug; the mystery is why it hasn't happened more often."
  - Eghbal on why nobody fixes it: "No individual company or organization is incentivized to address the problem alone, because open source code is a public good." And: "Many infrastructure projects have no legal entity at all."
  - The Cyber Safety Review Board, a US government body, on Log4j: "The event also called attention to security risks unique to the thinly-resourced, volunteer-based open source community. This community is not adequately resourced to ensure that code is developed pursuant to industry-recognized secure coding practices and audited by experts."
  - And: "The Board concluded that a focused review, performed by someone with sufficient experience with the security implications of adding the JNDI support, could have identified the unintended functionality (i.e., the vulnerability). Unfortunately, the resources to perform such a review were not available to the volunteer developers who led this open-source project in 2013."
- **Bears on:**
  - H4 (challenges): open source made software cheap to *use*, not cheap to *maintain*. The equivalent risk for open silicon is an open PDK or tool chain that everyone depends on and nobody funds — which is what OPEN-2 and OPEN-3 (preview-status PDKs) and OPEN-7 (Efabless's closure) already hint at.
  - H8 (context): openness attracted users far faster than it attracted money.
- **Used in:** not yet.
- **Caveats:** Eghbal's report is advocacy commissioned by a funder with an interest in the conclusion; its factual claims about OpenSSL's finances are sourced to the project's own people. The CSRB report is a government review with a security remit, so its framing emphasises risk.

#### PAR-15. Firms contribute to open source because contributing teaches them more than free-riding

- **Source:** Frank Nagle, "Learning by Contributing: Gaining Competitive Advantage Through Contribution to Crowdsourced Public Goods", *Organization Science* 29, no. 4 (July–August 2018): 569–587.
- **Verification:** Partial, 2026-09-18. The citation was read from the author's own CV at <https://www.hbs.edu/ris/Profile%20Files/Frank_Nagle_CV_11-3-24_ce20c46a-4111-4d45-8f05-31f99a5452a5.pdf>; the abstract was read from the Internet Archive capture of the HBS record page at <https://web.archive.org/web/20240223112758/https://www.hbs.edu/faculty/Pages/item.aspx?num=54809>, because the live page returns HTTP 403. The full paper was not read.
- **What it says:** "This study argues that such firms learn by contributing as they receive feedback from the crowd of more experienced users and are therefore able to better capture value from using the goods. … this study shows that contributing firms capture up to 100% more productive value from usage of OSS than their free-riding peers."
- **Bears on:**
  - **H9 (supports).** This is the closest published test of `WHY.md` §5's claim that public experiments make everyone learn faster, and it finds the effect in the direction the essay needs — but it locates the benefit in the *contributor*, not in the platform. Applied to a fab, it argues customers who publish results gain; it does not show the fab gains.
  - H8 (supports, indirectly).
- **Used in:** not yet.
- **Caveats:** abstract only. "Up to 100% more" is an upper bound from a matched observational design, not a causal experiment. A companion paper, "Open Source Software and Firm Productivity", *Management Science* 65, no. 3 (2019): 1191–1215, is recorded as a **Lead**: its publisher page returned HTTP 403 and we did not read the abstract.

### 2.3 Machine learning and AI

This is the analogue that points the other way. `WHY.md` §1 puts AI alongside open source and the cloud as a force that made experimentation cheap. On the evidence, frontier AI is a near-perfect replica of the chip industry's doom spiral — rising cost per attempt, a shrinking number of organisations that can pay, and falling disclosure — while the cheap, open, many-participants part of AI sits one or two generations behind the frontier. That is exactly the relationship between leading-edge and mature nodes in chip-making.

#### PAR-16. Frontier AI training cost is growing 2.4× a year and will exclude all but the best-funded

- **Source:** Ben Cottier, Robi Rahman, Loredana Fattorini, Nestor Maslej, Tamay Besiroglu and David Owen, "The rising costs of training frontier AI models", arXiv:2405.21015. <https://arxiv.org/abs/2405.21015> (v1 submitted 2024-05-31; v2 2025-02-07)
- **Verification:** Verified 2026-09-18. Abstract read from the arXiv abstract page; the detailed figures below were read from the PDF at <https://arxiv.org/pdf/2405.21015>.
- **What it says:**
  - Abstract: "The analysis reveals that the amortized cost to train the most compute-intensive models has grown precipitously at a rate of 2.4x per year since 2016 (90% CI: 2.0x to 2.9x). … **If the trend of growing development costs continues, the largest training runs will cost more than a billion dollars by 2027, meaning that only the most well-funded organizations will be able to finance frontier AI models.**"
  - "We find that the most expensive publicly-announced training runs to date are OpenAI's GPT-4 at $40M and Google's Gemini Ultra at $30M."
  - Growth-rate table: amortized hardware CapEx plus energy, 2.4× per year (90% CI 2.0–2.9), doubling time 9 months (8–12), R² 0.58, N = 41. Excluding TPU-based models the rate rises to 3.0× per year.
  - "we estimate that it cost $800M to acquire the hardware used to train GPT-4, compared to $40M for the [amortized cost]".
  - Team size: "The number of reported contributors increased from 25 for GPT-3 to 284 for GPT-4".
- **Bears on:**
  - **H1 (supports, by analogy — and this is the important direction).** A rising cost per attempt, doubling every nine months, with the population of organisations able to pay shrinking, is the doom spiral, re-run in a different industry in a single decade. The essay cites AI as an escape; the primary literature on AI describes a trap.
  - H4 (challenges as used in `WHY.md` §1): AI is not uniformly a cheapening force.
- **Used in:** not yet.
- **Caveats:** cost estimates for private training runs are modelled, not observed; the paper is explicit about method sensitivity. Its own cloud-rental method gives roughly twice the amortized figure — the same team's GPT-4 estimate is "$40M" amortized and about "$79 million" by cloud rental. Cite the method, not just the number.

#### PAR-17. Ninety-three notable AI models from industry in 2025, two from academia

- **Source:** Stanford Institute for Human-Centered AI, *AI Index Report 2026*, Chapter 1, "Research and Development". <https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_1_research_development.pdf>
- **Verification:** Verified 2026-09-18 (PDF downloaded, text extracted, quotes read in place).
- **What it says:**
  - "Industry produced over 90% of notable AI models in 2025, but the most capable models are now the least transparent. Training code, parameter counts, dataset sizes, and training duration are no longer disclosed for several of the most resource-intensive systems, including those from OpenAI, Anthropic, and Google."
  - "The development of notable AI models continues to be predominantly concentrated in industry … the share produced by industry has grown steadily and now represents the largest share by a wide margin (91.2%). **In 2025, Epoch AI identified two notable AI models originating from academia, compared to 93 from industry.**"
  - "In 2025, the top contributors were OpenAI (20), Google (14), and Alibaba (11)."
  - On the compute underneath: "Total capacity has increased by an estimated 3.3x per year since 2022, reaching approximately 17.1 million H100-equivalents. Nvidia AI chips currently account for over 60% of total compute, with Google and Amazon supplying much of the remainder".
- **Bears on:**
  - **H1 (supports by analogy), H4 (challenges as used).** In the most celebrated example of "anyone can now build with it", university laboratories have been driven out of the frontier almost entirely in about ten years. This is the clearest available warning that falling unit costs do not prevent concentration when the *scale* of a competitive attempt rises faster than the unit cost falls — which is precisely `WHY.md`'s own Step 4.
  - H9 (challenges): the most valuable work is becoming *less* public, not more.
- **Used in:** not yet.
- **Caveats:** "notable models" is Epoch AI's own curated selection, with inclusion criteria that favour large, well-publicised systems. Academic work that is not a frontier model release — datasets, methods, evaluation — is not counted, so the figure measures presence at the frontier, not academic contribution overall.

#### PAR-18. The other direction: inference prices fell by a median of 50× a year

- **Sources:**
  - Ben Cottier, Ben Snodin, David Owen and Tom Adamczewski, "LLM inference prices have fallen rapidly but unequally across tasks", Epoch AI, 2025-03-12. <https://epoch.ai/data-insights/llm-inference-price-trends>
  - Stanford Institute for Human-Centered AI, *AI Index Report 2025*, Chapter 1. <https://hai.stanford.edu/assets/files/hai_ai-index-report-2025_chapter1_final.pdf>
- **Verification:** Verified 2026-09-18 (both fetched and read by a delegated research pass; quotes reproduced from that read). Marked **Partial** for the AI Index figures, which we did not re-read against the PDF ourselves.
- **What it says:**
  - Epoch AI: "the price to achieve GPT-4's performance on a set of PhD-level science questions fell by 40x per year. The rate of decline varies dramatically depending on the performance milestone, ranging from 9x to 900x per year." And: "Across all of these benchmarks and performance thresholds, we found prices declining between 9x per year and 900x per year, with a median of 50x per year."
  - AI Index 2025: "the inference cost for an AI model scoring the equivalent of GPT-3.5 (64.8) on MMLU … dropped from $20 per million tokens in November 2022 to just $0.07 per million tokens by October 2024 (Gemini-1.5-Flash-8B)—a more than 280-fold reduction in approximately 1.5 years."
- **Bears on:**
  - H4 (supports): the cost of *using* a capability collapses even while the cost of *creating* it explodes.
  - H5 (supports, by analogy): that collapse is what opened ML to a large number of small builders.
- **Used in:** not yet.
- **Caveats:** these are prices, not costs, and are set strategically in a land-grab. Epoch's own caution: "The fastest price drops in that range have occurred in the past year, so it's less clear that those will persist."

- **The reading that matters for us.** The two halves of the AI story map cleanly onto chip-making: the frontier training run is the leading-edge node, and cheap inference on a year-old model is the mature node. In AI as in chips, the cheap and open part of the market sits a generation or two behind the frontier and cannot catch it. If the analogy is taken seriously, it says an open fab is necessarily a **mature-node** business — which `WHY.md` half-concedes ("at least on mature processes" in H4) but does not build into its argument.

#### PAR-19. Many more people can build with ML, but the engagement is thin

- **Sources:**
  - Stanford Institute for Human-Centered AI, *AI Index Report 2026*, Chapter 1, §1.5 "Open-Source AI Software". <https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_1_research_development.pdf>
  - Hugging Face model index, model counts read from the page. Live: <https://huggingface.co/models>. Historical, via the Internet Archive: <https://web.archive.org/web/20211130070153/https://huggingface.co/models> and <https://web.archive.org/web/20230531211532/https://huggingface.co/models>
- **Verification:** Verified 2026-09-18 for the AI Index quotes (PDF read). Partial for the Hugging Face counts, which are a live site counter rather than a published statistic; the historical points are citable only as archive captures.
- **What it says:**
  - AI Index 2026: "The number of AI-related GitHub projects increased from 1,549 in 2011 to approximately 5.6 million in 2025, with year-over-year growth accelerating 23.7% from 2024. **However, most repositories often consist of personal or experimental work and receive minimal attention. When filtering for projects with at least 10 stars, a rough proxy for community engagement, the count drops to 206,880 in 2025.**"
  - "From 2023 to 2025, model uploads more than tripled, while dataset uploads grew fourfold."
  - Hugging Face model counts as displayed: 21,671 (archive capture 2021-11-30); 215,597 (2023-05-31); 3,075,514 (live, 2026-09-18).
- **Bears on:**
  - H5 (mixed). Both halves matter. Millions of people did start building — and the overwhelming majority of what they built drew no attention at all. 206,880 out of 5.6 million is **3.7%** clearing a ten-star bar.
  - H10 (supports): that is the skew the essay's model depends on, observed directly.
- **Used in:** not yet.
- **Caveats:** GitHub stars are a weak proxy for value. The Hugging Face counter is a raw upload count including forks, quantisations and duplicates, so it overstates distinct work by an unknown factor.

- **DERIVED:** 206,880 ÷ 5,600,000 = **3.7%** of AI-related GitHub projects reach ten stars. If an open fab's tail behaves the same way, roughly 96% of tape-outs would attract no external interest whatever. `WHY.md` §5's case does not require otherwise — it requires only that each attempt is paid for — but the essay should say so plainly rather than implying a thriving ecosystem.

### 2.4 The internet and the web

The web is the analogue `WHY.md` reaches for first and defends least. Both halves of its history have to be recorded: it produced the largest explosion of independent publishers in history *and* the most concentrated advertising market in history, at the same time, from the same mechanism.

#### PAR-20. The number of websites went from 18,957 to about 1.5 billion

- **Sources:**
  - Mike Prettejohn, "The first year August 1995 - August 1996", Netcraft, dated August 1st, 1996. Read via the Internet Archive: <http://web.archive.org/web/19961230090403/http://www.netcraft.com:80/survey/year1.html>
  - Netcraft, "July 2026 Web Server Survey". <https://www.netcraft.com/blog/july-2026-web-server-survey>
- **Verification:** Verified 2026-09-18. The 1996 page was read from the Internet Archive because the live Netcraft site no longer hosts it; the 2026 survey was read live.
- **What it says:**
  - "The first Netcraft Web Server Survey was done over the last weekend in July 1995. It had responses from 18,957 hosts."
  - "The growth in the number of sites from 18,957 a year ago to todays 342,081 partly reflects the natural growth in the number of sites, and partly that we have got better at finding them."
  - July 2026: "In the July 2026 survey we received responses from 1,494,915,628 sites across 305,348,459 domains and 14,772,048 web-facing computers."
- **Bears on:** H5 (supports, by analogy), H4 (supports, by analogy): when the cost of publishing fell to near zero, the number of publishers rose by nearly five orders of magnitude.
- **Used in:** not yet.
- **Caveats:**
  - **Sites are not publishers.** July 2026 counts 1.49 billion sites across only 305 million domains — most "sites" are parked, duplicated or machine-generated hostnames. Do not use the site count as a count of independent publishers; the domain count is the more conservative figure.
  - Netcraft themselves warn that early growth "partly reflects … that we have got better at finding them".
  - The survey is universally cited as the "August 1995" survey but Netcraft's own text says the run was "over the last weekend in July 1995".

- **DERIVED:** 1,494,915,628 ÷ 18,957 = a factor of about **78,900** in 31 years. On the more defensible domain count, 305,348,459 ÷ 18,957 ≈ **16,100**.

#### PAR-21. And the cost of publishing collapsed: domain registration $50 a year to about $10, storage $0.15 a GB-month to $0.023

- **Sources:**
  - InterNIC / Network Solutions, "Fee for Registration of Domain Names", read via the Internet Archive capture of 1997-01-09: <http://web.archive.org/web/19970109000617/http://www.rs.internic.net:80/domain-info/fee-policy.html>
  - VeriSign, Inc., "Verisign Reports First Quarter 2026 Results". <https://investor.verisign.com/news-releases/news-release-details/verisign-reports-first-quarter-2026-results>
  - Jeff Barr, "Amazon S3", AWS News Blog, 2006-03-14. <https://aws.amazon.com/blogs/aws/amazon_s3/>
  - "AWS Storage Update – S3 & Glacier Price Reductions + Additional Retrieval Options for Glacier", AWS News Blog, 2016-11-21. <https://aws.amazon.com/blogs/aws/aws-storage-update-s3-glacier-price-reductions/>
- **Verification:** Verified 2026-09-18 by a delegated research pass that fetched each page; the current (2026) S3 price was **not** verified because the AWS pricing page renders its tables in JavaScript.
- **What it says:**
  - InterNIC, 1995–96 terms: "The Registration Fee for a new domain name is $100.00. New domain names are valid for two years"; "there will be an Maintenance Fee of $50.00 per year per domain name".
  - Verisign, 2026: "Verisign announces that it will increase the annual registry-level wholesale fee for each new and renewal .com domain name registration from $10.26 to $10.97 effective Nov. 1, 2026."
  - S3 at launch, 2006: "storing 1 GB of data for 1 month costs just 15 cents. Transferring data in and out of the system costs 20 cents per GB."
  - S3 in 2016: S3 Standard in US East (Northern Virginia) fell to "$0.0230" per GB-month for the first 50 TB.
- **Bears on:** H4, H8 (supports by analogy): SW-1's hundredfold figure is a single investor anecdote; these are published prices from the sellers themselves.
- **Used in:** not yet. This is the sourced version of what SW-1 asserts anecdotally.
- **Caveats:** the $10.26 is a wholesale registry fee, not a retail price. The 1995 fee is nominal, so the real fall is larger than 5×. No current S3 price was verified.

#### PAR-22. The same mechanism produced the most concentrated advertising market on record

- **Sources:**
  - Competition and Markets Authority, "Online platforms and digital advertising: Market study final report", 1 July 2020. <https://assets.publishing.service.gov.uk/media/5efc57ed3a6f4023d242ed56/Final_report_1_July_2020_.pdf>
  - Australian Competition and Consumer Commission, "Digital Platforms Inquiry — Final Report", June 2019. <https://www.accc.gov.au/system/files/Digital%20platforms%20inquiry%20-%20final%20report.pdf>
  - Australian Competition and Consumer Commission, "Digital advertising services inquiry — Final report", August 2021. <https://www.accc.gov.au/system/files/Digital%20advertising%20services%20inquiry%20-%20final%20report.pdf>
- **Verification:** Verified 2026-09-18. The CMA PDF was downloaded and the headline quotes below were re-read in place by us directly; the ACCC quotes were read by a delegated pass that downloaded both reports.
- **What it says:**
  - CMA, summary paragraph 16: "We estimate that around £14 billion was spent on digital advertising in the UK in 2019, around 80% of which was spent on Google and Facebook. Search advertising comprised around half of these revenues, at over £7 billion, and display expenditure was over £5 billion."
  - CMA, paragraph 2.63: "Overall, we estimate that around 80% of all expenditure on search and display advertising in the UK in 2019 was accrued as revenue by just two companies – Google and Facebook. This includes the revenue from advertising on each of their own platforms, as well as from intermediation services."
  - CMA, paragraph 18: "Google has generated around 90% or more of UK search traffic each year over the last ten years and generated over 90% of UK search advertising revenues in 2019."
  - CMA, paragraph 19: "Facebook (including Instagram, which it bought in 2012) generated over half of UK display advertising revenues in 2019. For comparison, its largest competitor, YouTube (owned by Google), earned between 5 and 10%."
  - CMA on why it persists: "We have not seen a significant challenge to the position of Google and Facebook for many years and have identified a number of characteristics of these markets that inhibit entry and expansion by rivals and undermine effective competition. These include: • network effects and economies of scale; • consumer decision making and the power of defaults; • unequal access to user data;"
  - CMA, paragraph 5.3, which is the sharpest line for our purposes: "However, Google and Facebook's collective share of digital advertising revenues is significantly greater than the share of time spent by users on these platforms, suggesting that their ability to monetise through advertising is not simply a function of scale."
  - ACCC 2019: "The ACCC estimates that for a typical AU$100 spent by advertisers on online advertising (excluding classifieds): $47 goes to Google (some of which is for the provision of ad tech services) $24 goes to Facebook $29 goes to all other websites and ad tech." And: "Outside of Google and Facebook, online advertising is highly fragmented with a large number of websites offering ad inventory, each with a small market share."
  - ACCC 2021, on the pipe rather than the revenue: "In 2020, we estimate that over 90% of ad impressions traded via the ad tech supply chain passed through at least one Google service."
- **Bears on:**
  - **H5, H7 (challenges).** A tail of hundreds of millions of publishers exists and captures a small minority of the money. If an open fab's tail behaves the same way, the fab had better be the aggregator and not one of the tail.
  - H7 (supports, in one specific reading): Google's own *customers* are millions of small advertisers, which is the position `WHY.md` wants the fab to occupy. The analogy works in the aggregator direction and fails in the participant direction — and `WHY.md` does not distinguish the two.
- **Used in:** not yet.
- **Caveats:**
  - The CMA and ACCC figures are UK 2019 and Australia 2018 respectively, with different scopes (the ACCC excludes classifieds). **Do not merge them into a single global "~80%" claim.**
  - The CMA notes its own denominator differs from the industry's: "the most recent IAB/PwC Digital Adspend Report estimated that total spend on UK search advertising was around £8 billion in 2019, and spend on display advertising was around £6.2 billion" — roughly 10–13% above the CMA's estimate.
  - We rejected the US House Judiciary Subcommittee's "Investigation of Competition in Digital Markets" as a source for this: its advertising-share figures are footnoted to journalism, not to primary data.

#### PAR-23. Attention concentrated too: the top 1,000 properties take 83% of time online

- **Source:** Competition and Markets Authority, "Online platforms and digital advertising: Market study final report", 1 July 2020, paragraphs 2.14–2.17 and Figure 2.2. <https://assets.publishing.service.gov.uk/media/5efc57ed3a6f4023d242ed56/Final_report_1_July_2020_.pdf>
- **Verification:** Verified 2026-09-18 (the "83% of total user time spent online" note was re-read by us in the downloaded PDF).
- **What it says:**
  - "UK consumers spent around 83% of their total time online on these top 1000 properties, with the remaining 17% split between an extremely long tail of websites." Figure 2.2's source note states the method: "Comscore MMX Multi-Platform, Total Digital Population, Desktop aged 6+, Mobile aged 13+, February 2020, UK."
  - "Of the total time spent by UK users online in February 2020, 37% was on sites owned by either Google (including YouTube) or Facebook (including Instagram and WhatsApp)."
  - "The characteristics of many of these markets are such that they tend to tip towards high levels of concentration."
- **Bears on:** H5 (challenges): this is TAIL-3's finding reproduced at the scale of the whole web, by a regulator, with the panel definition stated.
- **Used in:** not yet.
- **Caveats:** UK only, a single month, and *time spent* rather than pageviews or referrals. No primary source with a stated methodology was found for referral-traffic share; the widely-circulated referral figures come from vendor blogs whose panels are not documented.

#### PAR-24. arXiv: removing a gatekeeper multiplied volume by about a thousand — but the gate was replaced, not removed

- **Sources:**
  - arXiv, "Monthly submissions" statistics page and its published CSV. <https://arxiv.org/stats/monthly_submissions>, data at <https://arxiv.org/stats/get_monthly_submissions>
  - arXiv, *2025 Annual Report*. <https://info.arxiv.org/about/reports/2025_arXiv_annual_report.pdf>
  - arXiv, "Endorsement". <https://info.arxiv.org/help/endorsement.html>
- **Verification:** Verified 2026-09-18 by a delegated research pass that fetched the page, downloaded the CSV and cross-checked it against the annual report. The three agree.
- **What it says:**
  - Statistics page: "Total number of submissions as of September 18, 2026 = 3,173,333 ." The chart covers "each month since August 1991".
  - 2025 Annual Report: "284,486 submissions in 2025"; "23,707 submissions per month, on average"; "Most submissions in a month, ever 27,692 in October 2025"; "6 billion total downloads"; "5 million+ monthly active users"; "28 staff members"; "262 moderators".
  - And: "arXiv received 284,486 new submissions in 2025, up from 244,031 the previous year – an increase of over 16%."
  - Free at the point of use: "There are no fees or costs for article submission." "Since our founding in 1991, arXiv has been free to use and open to all."
  - **But a gate remains:** "arXiv requires that users be endorsed before submitting their first paper to arXiv or a new category", in order to "verify that arXiv contributors belong to the scientific community in a fair and sustainable way that can scale with arXiv's growth".
- **Bears on:**
  - H5, H8 (supports): removing a cost and a gatekeeper multiplied participation enormously, and openness was the mechanism.
  - **H8 (challenges, and this is the useful part):** arXiv did not remove the gatekeeper. It replaced an expensive editorial gate with a cheap membership-verification gate, and still employs 262 moderators. An open fab is likely to need the same: a cheap, fast, scalable check that the customer is not going to damage the shared resource — which is what the Stanford PROM committee in PAR-33 actually is.
- **Used in:** not yet.
- **Caveats:**
  - Submissions are not independent authors and are not successful results.
  - arXiv's own operational notes describe strain from volume and mention lower-quality submissions; we did not read those paragraphs cleanly enough to quote them, so that observation is recorded as unverified.
  - Minor inconsistency in arXiv's own data: the page says "since August 1991" while the CSV's first row is July 1991, with 2 submissions.

- **DERIVED (from arXiv's own CSV, summed by us in a script):** yearly submission totals 1995: 13,014 · 2000: 30,601 · 2005: 46,855 · 2010: 70,131 · 2015: 105,280 · 2020: 178,329 · 2024: 244,031 · 2025: 284,486. From 13,014 in 1995 to 284,486 in 2025 is a factor of **21.9** in 30 years — an order of magnitude less than the web's growth, because the supply of people qualified to submit is bounded in a way the supply of people able to make a web page is not. **That bound is the closer analogue for silicon.**

---

## Part 3. Physical industries: the coupling, the successes and the failures

### 3.1 The break with no software analogue: customers sharing one physical process are coupled

#### PAR-25. The world's most open shared fab forbids new materials without committee approval

- **Sources:**
  - Stanford Nanofabrication Facility, "Cleanliness Groups for Process Flows". <https://snfguide.stanford.edu/guide/materials/cleanliness-groups-for-process-flows>
  - Stanford Nanofabrication Facility, "New Process or Material Requests (PROM)". <https://snfguide.stanford.edu/guide/materials/new-process-or-material-requests-prom>
- **Verification:** Verified 2026-09-18 (both pages downloaded and the text extracted and read).
- **What it says:**
  - The purpose: "Cleanliness groups are used to classify equipment and materials at SNF to minimize cross-contamination risk. The choice of equipment in a process sequence will depend on the previous equipment used as well as the materials in your samples. In general, wafers can be processed in only equipment within the same or lower level of cleanliness."
  - The "Clean" group, for front-end CMOS: "CMOS compatible substrates and film materials only. **Wafers containing any metals or metal films are strictly prohibited from being processed in this equipment.**"
  - Contamination is a one-way ratchet: "Wafers with any previous processing in Semi-Clean and Flexible equipment will require additional considerations before returning to Clean tools. Such considerations may include procedures before processing in the previous equipment (such as chamber coating) or post-processing procedures (such as decontamination.)"
  - For the MOCVD tools: "Wafers containing any other materials requires ProM review and obtain approval."
  - Why wet processing is the worst case: "Wet benches are the first line of defense for protecting against cross-contamination. But a contaminated wet chemical bath is also the most effective means of spreading that contamination to any materials processed in that bath."
  - And the governance: "If you would like to perform 'non-standard' work in our labs, please contact us. We use a format for documenting new [m]aterials that we call PROM." — "**The PROM committee will help you define a path to testing your ideas while keeping the rest of the researchers' in the fab going as well.**"
  - The rules' provenance: "Our rules about materials are based on traditional cleanroom practices, where ionic migration properties of materials governed which tools could be used for specific purposes."
- **Bears on:**
  - **H11 (challenges), and it challenges `WHY.md` §5 "Four ideas for the factory" idea 1 directly.** The essay says a customer "rents time on the machines it needs, tries its own settings within the limits that keep the machines safe". SNF is a real shared fab, run for many small users, with published rules, and it does not work that way. The binding limits are not *machine-safety* limits, which a price or a deposit could cover. They are limits that protect **other customers' yield**, and they are enforced by a standing committee that reviews every non-standard material before it enters the building.
  - **H9 (challenges):** the experiments the essay most wants — new materials, unusual settings — are exactly the ones a shared physical process cannot simply allow.
  - H6 (challenges): "no per-customer engineering" is contradicted by the existence of the PROM committee, which is per-customer engineering by another name, and is the thing that makes the shared fab possible.
- **Used in:** not yet.
- **Caveats:**
  - SNF is a university research facility, not a production foundry. Its tolerances and its economics are different, and a production fab's rules would be *stricter*, not looser — which makes this a lower bound on the problem, not an upper one.
  - We could not read the associated "Legacy Materials/Contamination Policy" page (HTTP 403), nor find a published statement of how long a PROM review takes. The turnaround time of the approval gate is an open question and would be worth knowing.
  - This is a rules page, not a study. It shows what an operating shared fab believes it must do; it does not quantify how much yield is at stake.

**Why this matters more than it looks.** It is the one break in the analogy with no software counterpart at all. A cloud customer running broken code cannot lower another customer's success rate. A fab customer running an unapproved material can, silently, for months, across every wafer that touches the same tool afterwards. Every mechanism `WHY.md` and `PRINCIPLES.md` propose — published prices, self-service booking, "every preference costs money", insurance, futures — prices *the customer's own* risk. None of them price the externality the customer imposes on the next customer, and that externality is the reason fabs are conservative. It is not only buyer power.

### 3.2 Physical industries that opened up, and physical industries that tried and failed

*(filled in below)*

---

## Part 4. The counter-case on the long tail

*(filled in below)*

---

## Part 5. Adjudication

For each analogue: what transfers, what breaks, and a plain verdict. The scale used is:

- **Load-bearing** — the mechanism genuinely applies, and an argument may rest on it.
- **Illustrative** — useful for explaining the shape of the idea to a reader, but it cannot carry weight. Do not derive a prediction from it.
- **Misleading** — the analogue points the other way, or the differences are large enough that using it imports a false conclusion.

### 5.0 The break that applies to all four

Before the individual verdicts, the one number that governs every comparison.

| | Software on a cloud | Silicon on a shuttle |
|---|---|---|
| Marginal cost of one more attempt | ≈ $0 | **$300 to €30,000** (OPEN-5; PAR-3) |
| Time from decision to result | seconds to minutes | **170 to 224 days** (PAR-3); 228 to 451 days (PAR-4) |
| Attempts available per year | thousands | **1 to 5** (PAR-3) |
| Cost of an attempt that fails | the compute you used | the whole attempt, plus the wait, and ~95% of projects need another (PAR-6) |
| Can you revert? | yes, instantly | no |
| Does one customer's failure hurt another's? | no | **yes** — see Part 4 |

`WHY.md` argues from the first column to the second. The ratios between them are roughly 10^4 in cost per attempt and 10^3 in attempts per year. **An argument that survives a factor of ten is not the same as an argument that survives a factor of a thousand, and the essay never tests it against the larger number.** Everything below is a variation on this.

The honest statement of the project's position after this review is narrower than `WHY.md`'s, and stronger for being narrow:

> Cheap experimentation in silicon means going from *one attempt every few years, for those who can afford several million dollars* to *a few attempts a year, for those who can afford a few thousand*. That is a real and large change. It is not the change that happened to software, and calling it that invites a reader who knows software to expect something that will not arrive.

### 5.1 Cloud computing — **load-bearing for the access model, misleading for the customer mix**

**What transfers.** All of the access mechanism, and it transfers well. A single enormous fixed-cost asset; published prices with no negotiation (SW-2); self-service; pay for what you use; a customer who could never own the asset renting a slice of it. The claim that this model brings in customers who were previously excluded is supported. So is `PRINCIPLES.md`'s "every preference costs money": committed buyers do pay far less per unit (SW-5, PAR-8), and the small flexible buyer pays the premium.

**What breaks.**

1. **The revenue did not follow the tail.** AWS carries about 1.5 years of revenue in contracts longer than a year at a 4.0-year weighted-average life (PAR-7). Its largest announced commercial event is one customer for $38bn over seven years (PAR-10). It pays to acquire the tail (PAR-11).
2. **The purest form of the model concentrated hardest.** CoreWeave rents an expensive shared physical asset by the hour, was founded in the pay-as-you-go era, publishes on-demand prices — and takes 67% of revenue from one customer, with 98% of revenue on **take-or-pay** contracts (PAR-9). That is worse concentration than TSMC's 78% across ten customers (CONC-11). And the instrument it converged on is the same take-or-pay contract that cost AMD $320m and then $335m to escape (CONC-8).
3. **Cycle time.** A cloud customer iterates in seconds; a fab customer 1 to 5 times a year (PAR-3). The cloud's defining property — that a failed experiment costs you an hour and is reverted — does not exist in silicon at all.
4. **The asset is not shared in the same way.** A cloud region is a large number of independent, interchangeable machines. A fab process is one physical resource that every customer's wafer passes through, so customers are coupled (Part 4). AWS has nothing resembling this.

**Verdict: load-bearing for H8 (openness and published prices attract customers who could not otherwise buy), misleading for H7 (many small customers remove buyer power).** The cloud is the best evidence the project has for its access model and the *strongest single piece of evidence against its risk model*. `WHY.md` §6 uses AWS reserved-instance pricing to argue that small customers happily pay more. The same disclosures say the money is in the customers who commit.

### 5.2 Open source software — **load-bearing for design, misleading for manufacturing**

**What transfers.** Shared, free building blocks genuinely cut the cost of building something new (SW-3), and firms that contribute learn more than firms that free-ride (PAR-15). That supports `WHY.md` §4 exactly: open PDKs and open tools are lowering the cost of chip *design*. H4's design-side half is well supported.

**What breaks.**

1. **Open source's mechanism is the copy operation, and silicon has none.** The reason open source made software cheap is that the marginal cost of the thousandth user of a library is zero. A fab has no copy operation: the thousandth wafer costs about what the first one did, minus a learning-curve discount. Every claim that transfers "what open source did" to a fab has to survive the removal of the one property that made it work. Applied to manufacturing, it does not.
2. **The crowd is not a crowd.** 17% of the top non-npm projects have one developer writing more than 80% of commits; 81% have ten or fewer doing so (PAR-12). Over 85% of Linux kernel work is done by paid employees of companies (PAR-13). Open source is not mass parallel experimentation; it is a small number of mostly-paid people working in public.
3. **It did not solve funding.** Two-thirds of the web's encryption rested on one full-time developer, on an organisation that "never received more than $2,000 in donations per year" (PAR-14). The open-silicon equivalent is visible already: open PDKs stuck at preview status (OPEN-2, OPEN-3) and Efabless closing for want of a funding round (OPEN-7).

**Verdict: load-bearing for H4's design half; misleading if extended to manufacturing.** The essay should stop using "as open source did for software" as a general warrant in §5 and confine it to §4, where it is earned.

### 5.3 Machine learning and AI — **misleading, and it is better evidence for the doom spiral than against it**

**What transfers.** Falling inference prices — a median of 50× a year across benchmarks (PAR-18) — genuinely put a capability in many more hands, and AI-assisted design is a real reduction in the cost of a chip design (OPEN-6).

**What breaks.** Everything else, and it breaks in the direction of `WHY.md`'s own Step 4.

1. Frontier training cost is growing 2.4× a year, doubling roughly every nine months, and the paper's own conclusion is "only the most well-funded organizations will be able to finance frontier AI models" (PAR-16). Read `WHY.md` §2's four-step spiral against that sentence: it is the same spiral, running about ten times faster.
2. In 2025 there were **two** notable models from academia and 93 from industry, and the most capable ones stopped disclosing training details (PAR-17). An industry that started as the most open in computing has, in a decade, concentrated to a handful of firms and closed up. That is the outcome `WHY.md` is trying to avoid, produced by cheap tools.
3. The cheap, open, many-participants part of AI sits one or two generations behind the frontier and cannot reach it. **That is the relationship between mature nodes and the leading edge, reproduced exactly.**

**Verdict: misleading as used in `WHY.md` §1. But it is genuinely valuable as a warning, and the essay would be stronger if it used it that way.** AI shows that falling cost per unit does not prevent concentration when the scale of a competitive attempt rises faster than the unit cost falls. It also implies something the project should state openly: an open fab is a **mature-node business**, and the leading edge is not coming back within reach. H4's hedge, "at least on mature processes", should be promoted from a hedge to a premise.

### 5.4 The internet and the web — **illustrative**

**What transfers.** The cost of publishing collapsed (PAR-21) and the number of publishers rose by four to five orders of magnitude (PAR-20). arXiv shows the same pattern in a professional field (PAR-24). As a way of telling a reader "when the cost of trying falls, many more people try", this is fine and true.

**What breaks.**

1. **Nothing about the web's mechanism is physical.** Zero marginal cost, instant distribution, unlimited parallelism, free reverts. Of the properties that produced the outcome, silicon has none.
2. **The tail did not capture the value.** Around 80% of UK digital advertising went to two companies (PAR-22); 83% of time online went to the top 1,000 properties (PAR-23). The web produced the largest long tail in history *and* the most concentrated market in history, from the same mechanism, at the same time.
3. **The essay's own use of it is ambiguous in an important way.** `WHY.md` §5 cites Anderson's "Google makes most of its money off small advertisers" — that is the **aggregator's** position, not a tail participant's. The web's evidence is that the aggregator position is extremely valuable and extremely concentrated. Taking it seriously means the open-fab thesis is not "a fab can serve the tail" but "**one** fab can be the aggregator for the tail, and being second is worth little". `WHY.md` never says this, and it changes what the project is claiming.
4. **arXiv shows the gate is replaced, not removed.** arXiv still requires endorsement and still employs 262 moderators (PAR-24). Volume grew 22× in 30 years, not 78,000× as the web did, because the supply of qualified participants is bounded. Silicon's bound is tighter still.

**Verdict: illustrative.** Keep it in §1 as a way of orienting a reader who knows software. Do not derive any prediction about an open fab from it, and add the concentration half, because leaving it out is the kind of omission an informed reader will notice and hold against the rest of the essay.

---

## Part 6. Open questions

Recorded rather than answered, because we could not settle them.

1. **How long does a PROM-style approval take?** PAR-25 shows a shared fab gates new materials through a committee. Nobody publishes the turnaround. If it is days, an open fab can automate it; if it is months, it is a second cycle time stacked on top of the first and it dominates everything. This is the highest-value unknown in the file.
2. **What is the cost to serve one MPW customer?** H6 needs this and we still do not have it. EUROPRACTICE publishes prices (PAR-3) but not costs. Nobody publishes the staff time per shuttle participant, which is the number that decides whether "no per-customer engineering" is achievable.
3. **What is the respin rate for small, mature-node designs?** PAR-6 gives 5% first-silicon success for IC/ASIC projects generally, weighted towards large commercial designs. The rate for a Tiny Tapeout-scale design on an open PDK is unknown and could be very different in either direction.
4. **Has MPW cycle time improved over 30 years?** PAR-3 gives current figures and the 2020 lead time; PAR-1 and PAR-2 give fab cycle time in 1992–1995 and 2017. We do not have a consistent MPW series. EUROPRACTICE schedules from the 1990s and 2000s would settle it and may exist in the Internet Archive.
5. **Do published prices actually attract small buyers?** H8 asks this and we found no study of price transparency and small-buyer adoption in any industry. The evidence we have is existence proofs (AWS, EUROPRACTICE, JLCPCB), not causal evidence.
6. **Is there a post-EUV measurement of cycle time at 7nm or 5nm?** PAR-2's 80–100 day figures were a 2017 projection that explicitly assumed no EUV. We found no measured replacement.
7. **What does an open fab do about the externality one customer imposes on the next?** No mechanism in `PRINCIPLES.md` or `AUCTIONS.md` prices it (PAR-25). Insurance is the obvious candidate and it is not obvious that it works: the loss is another party's yield, discovered late, and hard to attribute.
8. **Does the aggregator reading change the thesis?** Part 5.4 argues the web's evidence supports "be the aggregator", and the aggregator position is a near-monopoly in every case examined. If that is right, the project is claiming winner-take-most economics, which is a different and much stronger claim than `WHY.md` makes. Nobody has decided whether the project intends it.

---

## Changes needed in other files

This file does not edit anything else. Everything below is a change someone else should make.

### `resources/hypotheses.md`

The README's rule is that adding an entry means updating the hypothesis it bears on. These are the updates this file implies.

| Hypothesis | Change |
|---|---|
| **H1** | Add PAR-16 and PAR-17 as **supports by analogy** — frontier AI reproduced the doom spiral in a decade. Add PAR-2 as **supports**: the leading edge is getting slower as well as dearer. |
| **H2** | Add PAR-9 as **supports**: CoreWeave's risk factors are GlobalFoundries' risk factors. |
| **H3** | Add PAR-1 as **mixed**: "fab size above 7,000 wafer starts per week does not improve performance" is a measured limit on the returns to scale that Step 3 assumes. |
| **H4** | Status should change from "Contested" to note a second axis. Add PAR-2, PAR-3, PAR-4 and PAR-6 as **challenges**: cost is not the only barrier, and cycle time and respin rate are not falling. Add PAR-5 as **supports**. Promote the existing hedge "at least on mature processes" to a premise (see PAR-17). |
| **H5** | Add PAR-5 as the **strongest support** yet recorded (360 designs manufactured out of 600+ submissions). Add PAR-3 and PAR-4 as **challenges** (1–5 attempts a year). Add PAR-22, PAR-23 and PAR-19 as **challenges** — the tail is thin wherever it has been measured. Add PAR-24 as **supports**. |
| **H6** | Add PAR-7, PAR-9 and PAR-11 as **challenges**: the cloud's money is in committed contracts and it pays to acquire the tail. Add PAR-25 as a **challenge**: "no per-customer engineering" is contradicted by the PROM committee that makes a shared fab possible. |
| **H7** | Add PAR-9 as the **strongest challenge in the repository**. Add PAR-10 and PAR-22. The status should move from "Argued from theory" to "Contested", because there is now a direct counter-example in the industry the hypothesis is modelled on. |
| **H8** | Add PAR-3 as **supports with a sting**: the open, published-price, self-service shuttle model already exists and has not transformed the industry. Add PAR-24 as **mixed**: arXiv replaced the gate rather than removing it. Add PAR-21. The "Needs" line about price transparency and small-buyer adoption is still unmet; see Part 6 item 5. |
| **H9** | Add PAR-15 as the **closest published support** — but note it locates the gain in the contributor, not the platform. Add PAR-17 and PAR-25 as **challenges**. Add PAR-12 as **mixed**. |
| **H10** | Add PAR-12 and PAR-19 as **supports**: skew observed directly in two more domains. |
| **H11** | Add PAR-25 as a **challenge**: no proposed mechanism prices the externality one customer imposes on the next. |

### `WHY.md`

In rough order of how much they matter.

1. **§1 has no cycle time in it, and that is the biggest single gap in the essay.** A reader who knows software will assume "cheap to try" implies "quick to try". It does not. One paragraph with PAR-3's table would fix it, and the essay is more credible for naming the limit than for omitting it.
2. **§5, "Four ideas for the factory", idea 1 is contradicted by an operating shared fab.** "tries its own settings within the limits that keep the machines safe" — PAR-25 shows the binding limits are not machine-safety limits but limits protecting other customers' yield, enforced by a committee. Either the sentence needs rewriting or the essay needs to say how an open fab prices that externality.
3. **§6's cloud argument is incomplete in a way a hostile reader will find.** Quoting AWS reserved-instance discounts to show small customers happily pay more, without mentioning that AWS carries about 1.5 years of revenue in multi-year commitments (PAR-7) and that the purest version of the model is 67% one customer on take-or-pay (PAR-9), is selective. Add them and answer them.
4. **§5's "as open source did for software" should be confined to §4.** Open source's mechanism is the copy operation and silicon has none (Part 5.2).
5. **§1 and §4 use AI as a cheapening force.** It is also the fastest-running example of the doom spiral in history (PAR-16, PAR-17). Using it in both directions would strengthen the essay considerably.
6. **§5's long-tail passage should record the concentration half of the web story** (PAR-22, PAR-23), and should decide whether the essay is claiming the tail position or the aggregator position (Part 5.4, point 3).
7. **Factual addition for §4:** about 95% of IC/ASIC projects now need a respin (PAR-6). "Cheap first chip" is a weaker claim than it sounds if you need three of them.

### `resources/references/software-analogies.md`

- **SW-5** should cross-reference PAR-8 (Google Cloud's committed-use discounts, which are explicitly take-or-pay: "You are billed monthly for your committed resources … regardless of whether or not you use those resources") and PAR-9. SW-5's caveat currently frames the brief's reading as the unfriendly one; PAR-7 and PAR-9 make the brief's reading the better-supported one.
- **SW-1** (Andreessen's hundredfold figure) should cross-reference PAR-21, which gives the same story from the sellers' own published prices rather than from an investor anecdote.
- **SW-3**'s caveat about the Open Path critique is still a Lead. Separately, PAR-12 adds what SW-3 does not: the contributor concentration behind the value concentration.

### `resources/references/long-tail.md`

- The Lead at the end of TAIL-3, "The Long Tail Debate: A Response to Chris Anderson" (2008), is **blocked**: <https://hbr.org/2008/07/the-long-tail-debate-a-respons> serves only the header and the first sentence to an unauthenticated reader. Verified from that fragment: the author is Anita Elberse and the piece opens "my recent article in the _Harvard Business Review_, '[Should You Invest in the Long Tail?]' has stirred up a debate among long-tail enthusiasts and critics alike." The body was not read. Record it as blocked rather than leaving it as an open Lead.
- The "Evidence that would help" list should be updated: PAR-5 supplies the shuttle oversubscription figure it asks for, and PAR-4 supplies a submissions-over-time series.

### `resources/README.md`

- The "Reference topics" table lists ID prefixes for files in `references/`. `PAR` is used in an `analyses/` file. Either add a line noting that analyses may also carry an ID prefix, or move these entries into `references/`. Our preference is to leave them here, because the adjudication in Part 5 is the point of the file and it is not a reference list.
