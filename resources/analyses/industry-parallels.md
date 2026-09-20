# Industry parallels: is the software analogy load-bearing? (`PAR`)

`WHY.md` argues that chip manufacturing is stuck where software was before cheap experimentation, and that opening it up will do for chips what the internet, open source, cloud computing and machine learning did for software. This file tests that claim in both directions.

It is written to be read by an adversarial reviewer. **The conclusion is not that the analogy holds.**

- **Cloud computing** is load-bearing for the access model and misleading for the customer mix.
- **Open source** is load-bearing for chip design and misleading for chip manufacturing.
- **Machine learning** is misleading as the essay uses it, and is better evidence *for* the doom spiral than against it.
- **The internet** is illustrative only.
- A fifth analogue the essay does not use — **self-service physical manufacturing**, from PCB fabs to Protolabs to the two companies that went bankrupt doing exactly what `WHY.md` proposes — is the only one where the whole mechanism transfers, and it is the one the project should be arguing from.

Two things are missing from the essay entirely and are supplied here: **cycle time**, which is the first-order limit on how often a customer can return and which appears nowhere else in this repository, and **the coupling between customers who share one physical process**, which has no software analogue at all.

**ID prefix:** `PAR`, PAR-1 to PAR-39. Entries follow the format in [`../README.md`](../README.md). This file does not edit any other file; see the last section for changes that belong elsewhere.

**Verification counts:** 24 Verified, 13 Partial, 1 Lead, plus PAR-37, which is a summary of figures verified at other entries. Every blocker is recorded with the exact reason at the entry that hit it. Entries marked Partial for the specific reason that a delegated research pass, rather than this file's author, read the source are PAR-18, PAR-21, PAR-28, PAR-30, PAR-31, PAR-32, PAR-34, PAR-35 and PAR-39; each says so.

**Date compiled:** 2026-09-18.

---

## Contents

- [Part 1. Cycle time: the missing number](#part-1-cycle-time-the-missing-number) — PAR-1 to PAR-6
- [Part 2. The four analogues](#part-2-the-four-analogues) — PAR-7 to PAR-24
- [Part 3. Physical industries: the coupling, the successes and the failures](#part-3-physical-industries-the-coupling-the-successes-and-the-failures) — PAR-25 to PAR-35
- [Part 4. The counter-case on the long tail](#part-4-the-counter-case-on-the-long-tail) — PAR-36 to PAR-39
- [Part 5. Adjudication](#part-5-adjudication) — the verdicts
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
- **Verification:** Partial, 2026-09-18. Both pages were fetched and read by a delegated research pass and the quotes are reproduced from that read; we did not re-read either against the source ourselves.
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
- **Verification:** Partial, 2026-09-18. Each page was fetched and read by a delegated research pass; we did not re-read them ourselves, and the current (2026) S3 price was **not** verified at all because the AWS pricing page renders its tables in JavaScript.
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

### 3.2 Physical industries that tried the open, self-service, many-small-customers model — and failed

This is the section the brief asked for specifically, and it is the most useful part of the file. Two public companies built exactly the business `WHY.md` describes — published prices, instant online quoting, no salesperson, thousands of small customers, physical manufacturing — and both went bankrupt. Their filings are public.

#### PAR-26. Shapeways: self-serve 3D printing for thousands of small customers, liquidated under Chapter 7

- **Sources:**
  - Shapeways Holdings, Inc., Form 8-K, filed 2024-07-03, period of report 2024-07-02. Filing index: <https://www.sec.gov/Archives/edgar/data/1784851/000162828024030980/0001628280-24-030980-index.htm>; document: <https://www.sec.gov/Archives/edgar/data/1784851/000162828024030980/shpw-20240702.htm>
  - Financial figures from Shapeways' XBRL company facts (SEC CIK 0001784851), as tagged in its own Forms 10-K: <https://data.sec.gov/api/xbrl/companyfacts/CIK0001784851.json>
- **Verification:** Verified 2026-09-18. The 8-K text was read from the SEC filing; the financial figures were read from the SEC's XBRL API, which serves the values the company itself tagged in its 10-K filings.
- **What it says:**
  - "the Company ceased operations and filed a voluntary petition for relief under the provisions of Chapter 7", in the "United States Bankruptcy Court for the District of Delaware", on July 2, 2024. "Each of the Company's subsidiaries also ceased operations and filed voluntary petitions for bankruptcy relief."
  - "a Chapter 7 trustee will be appointed by the Bankruptcy Court and will administer the Company's bankruptcy estate, including liquidating the assets of the Company in accordance with the Bankruptcy Code."
  - "Following the Bankruptcy Filing, neither the Company nor any of its subsidiaries have officers or employees."
  - Revenue as tagged in its 10-K filings: 2020 $31,775,000 · 2021 $33,623,000 · 2022 $33,157,000 · 2023 $34,460,000.
  - Gross profit: 2020 $13,872,000 · 2021 $15,950,000 · 2022 $14,298,000 · 2023 $14,505,000.
  - Net loss attributable to parent: 2021 $16,376,000 · 2022 $20,221,000 · **2023 $43,911,000**.
  - **The finding that matters most**, from the 10-K narratives (read by a delegated research pass from the filings at <https://www.sec.gov/Archives/edgar/data/1784851/000162828024013659/shpw-20231231.htm>, <https://www.sec.gov/Archives/edgar/data/1784851/000162828023009934/shpw-20221231.htm> and <https://www.sec.gov/Archives/edgar/data/1784851/000119312522091992/d208861d10k.htm>):
    - FY2023 10-K: "We have delivered over 24 million parts to over one million customers in over 180 countries from inception through 2023. … **In 2023, one customer accounted for approximately 17% of our revenue.**"
    - FY2022 10-K: "In 2022, one customer accounted for approximately 20% of our revenue."
    - FY2021 10-K, risk factor heading: "**We depend on our largest customer for a substantial portion of our revenue.**" — "Our largest customer accounted for approximately 23% of our revenue for the year ended December 31, 2021."
    - FY2023 10-K: "There is substantial doubt as to our ability to continue as a going concern." Accumulated deficit at 2023-12-31: $176.9 million.
    - FY2022 10-K, stating the retreat explicitly: "**Our customer count may continue to decline as we increase our focus on middle market and enterprise opportunities.**"
  - Its own description of the model: "Historically, Shapeways has been a self-service digital manufacturing platform growing through our customers and through organic customer acquisition."
- **Bears on:**
  - **H5, H6, H7 (challenges, and this is the most direct challenge in the repository).** Shapeways is the closest existing thing to the business `WHY.md` proposes, in a different material. It had the customers. It had published prices and self-service. It did not have a profit, and its revenue did not grow.
  - **H7 (challenges, specifically and painfully).** A business with **over one million lifetime customers** still had one customer at 23%, 20% and 17% of revenue in successive years — and wrote a risk factor about it that reads exactly like SkyWater's and GlobalFoundries' (CONC-5). **Customer count is not customer base.** H7 assumes that many small customers means no customer has leverage. Shapeways had far more customers than TSMC's 534 (`WHY.md` §2) and a single-customer share — 23%, 20%, 17% — of the same order as TSMC's largest customer over the same years (25% in 2023, 22% in 2024, 19% in 2025, per CONC-11). Not worse than TSMC's, but not better either, from a base of a million customers instead of 534. We have no single-customer figure for GlobalFoundries, so no comparison is made there.
  - H10 (challenges): being paid for every attempt is necessary but plainly not sufficient.
- **Used in:** not yet.
- **Caveats:**
  - **3D printing is not chip-making**, and the differences cut both ways. Shapeways' machines are far cheaper than a fab's, so its fixed-cost advantage over a customer buying its own printer is far smaller — desktop 3D printers got good enough that customers could defect, which has no silicon equivalent. Against that, its cycle times were days rather than months, which should have made it *easier*, not harder.
  - The 2023 loss of $43.9m against $34.5m of revenue includes impairments we did not itemise; do not read it as pure cash burn.
  - We did not read the 10-K narrative, so we have no company explanation of the failure and offer none. What is verified is the shape: four years of flat revenue at a ~42% gross margin, accelerating losses, then liquidation.

- **DERIVED:** gross margin $14,505,000 ÷ $34,460,000 = **42.1%** in 2023. Revenue grew 8.4% in total across the four years 2020 to 2023 ($31.775m → $34.460m), or about 2.7% a year. **A 42% gross margin was not enough**, which is the number to hold against any projection for an open fab: if a self-service physical manufacturer with a 42% gross margin and thousands of small customers cannot cover its operating costs, the open-fab model needs either much higher margins or a far smaller cost base than Shapeways had.

#### PAR-27. Fast Radius: on-demand manufacturing, public in February 2022, Chapter 11 in November 2022

- **Source:** Fast Radius, Inc., Form 8-K, filed 2022-11-08, period of report 2022-11-04. Filing index: <https://www.sec.gov/Archives/edgar/data/1832351/000095017022022842/0000950170-22-022842-index.htm>; document: <https://www.sec.gov/Archives/edgar/data/1832351/000095017022022842/fsrd-20221104.htm>
- **Verification:** Verified 2026-09-18 for the quotes below (read from the SEC filing). The company's operating revenue is **not** verified: its only Form 10-K on EDGAR covers the predecessor shell company, so the XBRL facts are not the operating business's.
- **What it says:**
  - "On November 7, 2022, Fast Radius, Inc., a Delaware corporation … together with its wholly-owned subsidiaries (the 'Debtors'), filed voluntary petitions … for bankruptcy protection under Chapter 11 of Title 11 of the United States Bankruptcy Code", in the "United States Bankruptcy Court for the District of Delaware", "In re Fast Radius, Inc., et al., Case No. 22-11051".
  - The Debtors intended to "pursue a structured sale of their assets pursuant to a competitive bidding and auction process."
  - Days earlier: "On November 3, 2022, the Company's board of directors … approved a reduction in force of approximately 20% of the Company's workforce in order to reduce the Company's operating expenses."
  - EDGAR records the company as "formerly operated as 'ECP Environmental Growth Opportunities Corp.' through February 4, 2022" — so it became a public company in February 2022 and filed for bankruptcy in November 2022.
  - From its Form 10-Q for the quarter ended 2022-09-30 (<https://www.sec.gov/Archives/edgar/data/1832351/000095017022025107/fsrd-20220930.htm>, read by a delegated research pass), the condensed consolidated statements of net loss, in $000s: revenues 7,072 (Q3 2022) against 4,916 (Q3 2021); cost of revenues 6,372 against 7,049; **gross profit 700 against (2,133)**. For the nine months: revenues 20,609, gross profit 1,593, against revenues 13,579 and gross profit (498).
  - From the FY2021 10-K narrative: "As of December 31, 2021, we had an accumulated deficit of approximately $123.3 million, including 2021 net losses of approximately $67.9 million." And: "Our recurring losses from operations and negative cash flows raise substantial doubt about our ability to continue as a going concern."
- **Bears on:**
  - H5, H6 (challenges): a second, independent failure of the same model in the same period.
  - **H6 (challenges, sharply):** gross profit of $0.7m on $7.1m of revenue is roughly a 10% gross margin, and the prior-year comparatives are *negative* — it was selling parts for less than they cost to make. H6 says each small customer is profitable if the fab does no per-customer engineering. Fast Radius did on-demand digital manufacturing with instant quoting, and each small customer was not profitable.
- **Used in:** not yet.
- **Caveats:**
  - 2022 was a bad year for companies that listed via SPAC generally, so the failure is over-determined and should not be attributed solely to the business model. It is recorded as a data point, not a proof.
  - The Form 10-K on EDGAR for FY2021 is filed under the predecessor shell (ECP Environmental Growth Opportunities Corp.), so its income statement is the shell's; the operating figures above come from the 10-Q and from the 10-K's narrative and going-concern notes.

- **DERIVED:** public on 2022-02-04, Chapter 11 on 2022-11-07 — **276 days**, which is roughly one Tiny Tapeout shuttle (PAR-4). Q3 2022 gross margin 700 ÷ 7,072 = **9.9%**.

#### PAR-28. The recurring failure mode is the storefront, not the factory

- **Sources:**
  - Efabless shutdown notice, read via the Internet Archive capture of 2025-03-01: <https://web.archive.org/web/20250301210729/https://efabless.com/notice>. Successor: <https://chipfoundry.io/>. **Corrected 2026-09-20:** this previously said
    "<https://efabless.com/> and <https://chipfoundry.io/> (both live)". `efabless.com` last served
    HTTP 200 on **2025-09-02** and has redirected (301) to `chipfoundry.io/efabless` ever since.
    ChipFoundry is also **not** simply Efabless's successor — it is a separate company founded
    2025-04, which acquired Efabless's assets and the chipIgnite name later that year (`CF-1`).
  - Stratasys Ltd. Form 20-F for FY2015: <https://www.sec.gov/Archives/edgar/data/0001517396/000120677416005045/stratasys_20f.htm>. Acquisition announcement, Exhibit 99.1 to a Form 6-K: <https://www.sec.gov/Archives/edgar/data/0001517396/000110465913050451/a13-15347_1ex99d1.htm>
  - MOSIS: <https://www.mosis.org/about-us> (live, 2026-09-18), and the archived self-description at <https://web.archive.org/web/20020711010856/http://www.mosis.com/about/whatis.html>
  - BASF news release P-19-398, "BASF Acquires 3D Printing Service Provider Sculpteo", 2019-11-18: <https://www.basf.com/global/en/media/news-releases/2019/11/p-19-398>
- **Verification:** Partial, 2026-09-18. Each page was fetched and its quoted text read by a delegated research pass; we did not re-read them ourselves, and the pattern claim is our own synthesis, not a finding of any of these documents.
- **What it says:**
  - **Efabless**, the company that ran the open MPW programmes in `WHY.md` §4: "Shutdown Notice. Due to funding challenges, Efabless has shut down operations until further notice." Its site now says: "Umbralogic Technologies LLC, doing business as ChipFoundry, has acquired the assets of Efabless Corporation."
  - **MakerBot**, the flagship "3D printing for everyone" brand: Stratasys acquired it in 2013 with an "initial value of $403 million based on Stratasys' closing stock price of $84.60 as of June 19, 2013" (announcement) and an aggregate purchase price of "$493.7 million" at closing (FY2015 20-F). It then wrote the goodwill off in three steps: "$102.5 million" (FY2014), "$150.4 million" (Q1 2015) and "an additional non-tax-deductible impairment charge of $125.1 million" — "As of December 31, 2015, there was no remaining goodwill balance assigned to MakerBot reporting unit."
  - **MOSIS did not shut down**, contrary to a common assumption we started with. It is still running: "In 2023, MOSIS evolved into MOSIS 2.0 as a core component of the Defense Ready Electronics and Microdevices Superhub (CA DREAMS), one of eight regional innovation hubs established under the Department of War Microelectronics Commons Program through the CHIPS and Science Act of 2022." Its historic scale, from the 2002 archive: "Since 1981, MOSIS has fabricated more than 50,000 circuit designs for commercial firms, government agencies, and research and educational institutions around the world." And: "By June 1985, 1706 designs had been fabricated over the prior twelve months."
  - **Sculpteo** was acquired by BASF in 2019 and still operates; its designer Marketplace closed in 2023 (**Lead** — the company's own post at <https://www.sculpteo.com/blog/2023/10/13/the-marketplace-closure-will-have-no-impact-on-our-activities/> returned HTTP 403, so the wording and date are unverified).
- **Bears on:**
  - H5, H6 (challenges): in case after case the capital-intensive production asset survived and **the many-small-customers storefront on top of it was shed**. MakerBot, Sculpteo's Marketplace, Shapeways' shops, Ponoko's "make & sell", and Protolabs' own retreat (PAR-29) are the same move.
  - H8 (mixed): MOSIS is the strongest counter-example in the other direction — an open, published-price, many-small-customers silicon shuttle that has run since 1981. But it has run on 45 years of public funding, most recently CHIPS Act money. It is a subsidised service, not a self-sustaining business, which is the distinction `WHY.md` has to clear.
- **Used in:** not yet. OPEN-7 already covers Efabless's closure; this adds the successor and the pattern.
- **Caveats:**
  - **The pattern is our reading, not any source's finding.** Each case has its own causes; MakerBot's failure in particular is usually attributed to desktop-printer quality problems and competition, not to the storefront model.
  - The widely-quoted Efabless CEO line about being "unable to complete our latest funding round" appears only in secondary reporting; it is recorded in OPEN-7 and should stay marked as such. We did not find it in a primary document.
  - We found no SkyWater statement about the Efabless closure.
  - **Highest-value unchecked item in this whole file:** **ES2 (European Silicon Structures)**, 1985–1993, a pan-European fast-turnaround electron-beam direct-write "send us your design, get silicon" fab built explicitly for many small customers, which failed. If any historical case is the direct precedent for this project, it is that one, and nobody here has checked it. **Lead.**

### 3.3 Physical industries where it worked — and where the capital sits

#### PAR-29. Protolabs owns the machines, and has been losing small customers and margin for a decade

- **Sources:** Proto Labs, Inc. Forms 10-K, read from SEC EDGAR:
  - FY2025 (filed 2026-02-20): <https://www.sec.gov/Archives/edgar/data/1443669/000144366926000010/prlb-20251231.htm>
  - FY2018 (filed 2019-02-22): <https://www.sec.gov/Archives/edgar/data/1443669/000143774919003141/prlb20181231_10k.htm>
  - FY2015: <https://www.sec.gov/Archives/edgar/data/1443669/000143774916026114/prlb20151231_10k.htm>
- **Verification:** Verified 2026-09-18. We re-read the FY2025 headline quotes ourselves through the SEC filing; the FY2018 and FY2015 figures, the MD&A table and the margin series were read by a delegated research pass from the filings. Note: plain command-line fetches of `www.sec.gov` were refused for us ("Your Request Originates from an Undeclared Automated Tool") and succeeded for the delegated pass, so the block appears to be rate-based rather than absolute.
- **What it says:**
  - The business is exactly the shape `WHY.md` describes: "Our customers conduct nearly all their business with us over the Internet." "…we provide our customers an eCommerce experience where they can upload their part design and receive a rapid (or instantaneous) quote coupled with design for manufacturability feedback, evaluate the costs and lead times for a variety of manufacturing processes, and easily order parts at quantities 1 to 1 million-plus."
  - Fast: "Our technology-enabled digital engineering and manufacturing applications enable us to produce commercial-grade prototype and production plastic, metal, and liquid silicone rubber parts **in as fast as one day**."
  - Big tail: "We serve over 48,000 customers annually, ranging from the largest and most innovative organizations in the world, to entrepreneurs and small business owners." "Since our inception, we have manufactured over 700 million parts, and served over 300,000 customers".
  - Capital-intensive, in its own words: "Our quick-turn factory business model requires that we invest in our capacity well in advance of demand to ensure we can fulfill the expectations for quick delivery of products manufactured in house to our customers."
  - **And it is walking away from the tail, deliberately and in writing:** "During 2025, we served 48,415 unique customer contacts who purchased our products through our web-based customer interface, a decrease of 6.1% over the same period in 2024. Our customer contacts served decreased while our revenue increased. This was primarily due to our mix of customers served in 2025 as compared to 2024 and **our strategic focus to earn larger orders from our customers** as we strive to be their supplier of choice … Our revenue per customer contact grew 13.3% as compared to 2024."
  - Definition: "Customer contacts are product developers, engineers, procurement and supply chain professionals and other individuals who place an order, and that order is shipped and invoiced during the period."
  - Earlier years, when it was growing the tail: "During 2018, we served 45,968 unique product developers and engineers … an increase of 22.5% over the same period in 2017." "During 2015, we served 27,235 unique product developers and engineers, an increase of 26% over the same period in 2014." "During 2013, we served 16,128 unique product developers and engineers".
  - Margins: FY2013 62.4% of revenues; FY2014 61.3%; FY2015 58.5%; FY2017 56.3%; FY2018 53.6%; FY2024 44.6%; "Gross margin decreased to 44.5% of revenue in 2025 from 44.6% in 2024."
  - **Correction to a common assumption:** the recent 10-Ks carry **no quantified customer-concentration sentence and no 10% concentration note at all**. The quantified version is in the older filings: FY2018 and FY2015 both say "Our revenue is generated from a diverse customer base, with no single customer company representing more than 2% of our total revenue".
- **Bears on:**
  - **H7 (supports, and it is the best support H7 has):** here is a real, profitable, capital-owning manufacturer whose largest customer was under 2% of revenue. It can be done. `WHY.md` §5's third claim is not fantasy.
  - **H6 (challenges):** the same company's gross margin fell from 62.4% to 44.5% over twelve years while it did this, and it is now *reducing* its customer count on purpose. If serving many small customers were the profitable strategy, the company best placed to know would not be retreating from it.
  - H5 (mixed): 48,415 customers a year is a real tail; it peaked around 2023 at 53,464 and has fallen three years running.
- **Used in:** not yet.
- **Caveats:**
  - Injection moulding and CNC machining are not chip-making. Protolabs' machines cost thousands to millions; a fab costs billions. The direction of that difference is unclear: a fab's fixed-cost advantage over a customer's own equipment is far larger, which helps, but so is its need for utilisation, which hurts.
  - "Customer contacts" counts individuals who ordered, not companies, so the count and the concentration measure different things.
  - The falling margin has causes we did not investigate — mix, competition from Asian suppliers, its own network business at lower margin. Do not attribute it solely to serving small customers.

- **DERIVED:** revenue per customer contact, from the 10-K's own table: $9,425 (2023), $9,716 (2024), $11,012 (2025). Customer contacts 53,464 → 51,552 → 48,415, a fall of **9.4%** over two years, against revenue of $503.9m → $500.9m → $533.1m. The company is getting more revenue from fewer, larger customers. **That is the doom spiral's Step 2 and Step 3, in miniature, in a self-service physical manufacturing business with instant online quoting — the exact business model `WHY.md` proposes, drifting towards the exact outcome `WHY.md` wants to escape.**

#### PAR-30. Xometry owns no machines, and its small-customer count is growing 20% a year

- **Sources:** Xometry, Inc. Form 10-K for FY2025 (filed 2026-02-24): <https://www.sec.gov/Archives/edgar/data/1657573/000119312526066959/xmtr-20251231.htm>; Form 10-K for FY2022: <https://www.sec.gov/Archives/edgar/data/1657573/000095017023008494/xmtr-20221231.htm>
- **Verification:** Partial, 2026-09-18. Both filings were fetched and the quoted text read by a delegated research pass; we did not re-read them ourselves.
- **What it says:**
  - "The number of Active Buyers on our platform reached 81,821 as of December 31, 2025, up 20% from 68,267 as of December 31, 2024." FY2022: "Active Buyers on our platform reached 40,664 as of December 31, 2022, up 45% from 28,130 as of December 31, 2021."
  - Definitions: "we define Active Buyers as buyers who have made at least one purchase on our marketplace during the last twelve months."
  - Concentration: "For 2025, 2024, and 2023, no one customer accounted for more than 10% of the Company's revenues."
  - **The distinction that matters, in its own words:** "We are focused on driving strong free cash flow conversion given our **asset light model**, with capital expenditures that are predominately capitalized software costs." "All of our offices are leased and we do not own any real property." "We rely on our network of suppliers to provide the sophisticated manufacturing processes that we offer to our buyers."
  - Margins and losses: "Total gross margin was 39.1% for the year ended December 31, 2025, as compared to 39.5% … Gross margin for marketplace was 34.7% … Gross margin for our services was 88.6%." "We incurred a net loss available to common stockholders of $61.7 million in 2025 and, as a result of these losses, we had an accumulated deficit of $432.0 million as of December 31, 2025."
- **Bears on:**
  - **H6, H7 (mixed, and this is the sharpest comparison in the file).** Put PAR-29 and PAR-30 side by side. Protolabs owns the machines: 48,415 small customers, falling 6.1% a year, 44.5% gross margin, profitable. Xometry owns no machines: 81,821 small customers, rising 20% a year, 34.7% marketplace gross margin, losing $61.7m a year. **The many-small-customers model is growing where nobody owns the capital and shrinking where somebody does** — and neither version has yet shown that it pays.
- **Used in:** not yet.
- **Caveats:** a marketplace and a factory are not comparable businesses and we are comparing them anyway; treat the contrast as suggestive, not as a controlled test. Xometry's losses could be growth spending rather than a broken unit economics, and the filing does not settle it.

#### PAR-31. What self-service physical manufacturing looks like when it works: $2 and 24 hours

- **Sources:**
  - JLCPCB: <https://jlcpcb.com/> and <https://jlcpcb.com/about-us>
  - PCBWay: <https://www.pcbway.com/>
  - ChipFoundry (successor to Efabless): <https://chipfoundry.io/> and <https://chipfoundry.io/about>
  - Tiny Tapeout FAQ: <https://tinytapeout.com/faq/>
- **Verification:** Partial, 2026-09-18. A delegated research pass read each quoted string out of the raw HTML; we did not re-read them ourselves. **These are company marketing pages, not audited figures.** None of these companies is public and none of these numbers is independently attested.
- **What it says:**
  - JLCPCB's published product grid: "FR-4 PCBs … From $2.00 / 5 pcs **Build Time: 24 hours**"; "Flexible PCBs … From $2.00 / 5 pcs Build Time: 5-6 days"; "PCB Assembly … From $8.00 Build Time: 24 hours"; "Rapid Fab & Assembly As fast as 24 hours". Its own scale claims, footnoted "* As of Dec 2025": "9.5M + Customers"; "21M + Orders/Year"; "10,000 + Employees"; "180 + Countries Covered".
  - PCBWay: "PCB Prototype … From $5 /10pcs … Build Time:24 hours"; counters reading "256,000+ / Customers" and "128,000+ / Paying".
  - And the same page style, for silicon. ChipFoundry's chipIgnite: "**$14,950 / per tapeout**", for "Up to 15mm² of die space with a standard I/O ring" and the "Option of 100 QFN-packaged parts or Bare Die". Its about page: "Born from the success of open source silicon, which created a thriving community of over 10,000 members and facilitated more than 600 fabricated chip designs".
  - Tiny Tapeout's FAQ, on the wait: "**The chips are taking between 6 and 9 months to manufacture. Then we need to do PCBA, test and order fulfillment. So expect up to 1 year's wait time!**"
- **Bears on:**
  - **H8 (supports strongly):** published prices, published lead times, no salesperson, no negotiation, no minimum — and 9.5 million claimed customers. This is the mechanism `WHY.md` §5 idea 4 describes, working, at scale, in physical manufacturing.
  - **H5 (challenges, by the same page):** the PCB business does this at **$2.00 and 24 hours**. The silicon business does it at **$14,950 and up to a year**. Same model, same kind of page, four orders of magnitude apart in price and three in time. PCB fabrication became a commodity many-small-customers business because the cost and the wait fell to near-triviality. Silicon has not, and PAR-2 says the physics is moving the wrong way.
- **Used in:** not yet. This extends OPEN-5 (Tiny Tapeout at $300) with the commercial tier and the published wait.
- **Caveats:**
  - Marketing pages. "From $2.00" is a headline price for the cheapest configuration; "9.5M + Customers" is unaudited and its definition is unstated.
  - Tiny Tapeout's own price is calculator-gated ("Use the calculator to check current prices"), so the published figure here is the lead time, not the price. We did not operate the calculator, which would be submitting a form.
  - Seeed Studio's Fusion price is also calculator-gated; no headline price was obtained.

- **DERIVED:** JLCPCB's advertised 24-hour build time against Tiny Tapeout's own "up to 1 year's wait time" is a ratio of about **365×**. Against ChipFoundry's $14,950 per tape-out, JLCPCB's $2.00 for five boards is about **7,500×**. Both are self-service, both are published, both are Chinese or US companies selling to hobbyists and startups today. **That gap, not the gap between silicon and software, is the honest measure of how far silicon has to travel.**

#### PAR-32. The shipping container: the largest measured effect of a standardised physical interface

- **Source:** Daniel M. Bernhofen, Zouheir El-Sahli and Richard Kneller, "Estimating the effects of the container revolution on world trade", *Journal of International Economics*, Vol. 98 (C), 2016, pp. 36–50. The published version at <https://www.sciencedirect.com/science/article/abs/pii/S0022199615001403> is paywalled and was **not** fetched. The version read is the open-access accepted manuscript, every page stamped "ACCEPTED MANUSCRIPT", dated "September 2, 2015", at the University of Brighton repository: <https://cris.brighton.ac.uk/ws/portalfiles/portal/376845/JIE%20accepted%20manuscript%20online%20version%20(1).pdf>
- **Verification:** Partial, 2026-09-18. A delegated research pass fetched and read the accepted manuscript in full; we did not read it ourselves, and the accepted manuscript is not the version of record.
- **What it says:**
  - "Restricting our sample to North-North trade, which are mainly the early adopters, our benchmark specification which uses differences in the timing of adoption between countries suggests that the cumulative average treatment effect (ATE) of containerization was about 1,240% after 15 years. For all countries we find an effect that is smaller but still of economic importance at 900%."
  - Against trade policy: "Overall, we find that the estimated effects of containerization are generally much bigger than the estimated effects of the trade policy variables in all specifications." The cumulative ATE of a free-trade agreement is "about 68% at the end of 15-years"; of bilateral GATT membership, "194%".
  - **The authors' own caveat, which must travel with the number:** "an identification strategy based solely on differences in the timing of adoption of the container does not appear capable of providing convincing evidence of causal effects. The additional trade can be attributed to the container revolution only with caution."
- **Bears on:**
  - H8 (supports, by analogy): a standardised physical interface, which anyone could use without negotiating, produced an effect an order of magnitude larger than decades of trade diplomacy. That is the strongest available argument for standardisation and open interfaces in a physical industry.
  - H4 (context): the container did not make ships cheaper. It made the *interface between* transport modes cheap. The open-fab equivalent is the PDK and the tape-out format, not the fab.
- **Used in:** not yet.
- **Caveats:**
  - **Citation hygiene warning.** The headline number is different in every draft: a 2012 working paper says "about 700%" in its abstract and "790%" in its body (internally inconsistent); a 2014 revision says "about 500%" over 15 years; the 2016 JIE version says 1,240%. Anyone citing 700%, 790%, 517% or 500% is citing a different draft. Cite the 2016 set: 1,240% / 900% / GATT 194% / FTA 68%.
  - The published abstract contains no numbers. Do not attribute a percentage to it.
  - The authors themselves decline to claim causality for the all-country sample.

- **A related correction.** The widely-quoted loading-cost figure from M. Levinson's *The Box* is "**$5.83**" per ton for break-bulk against "15.8¢ per ton" for the SS *Ideal X*, from <https://worksthatwork.com/2/intermodal-container>: "When McLean's accountants ran the numbers, they pegged the cost of loading the SS Ideal X at 15.8¢ per ton, a tiny fraction of the US$5.83 it cost to load one ton of freight aboard an average break-bulk ship." Note the scope: this is the cost of *loading*, for one ship on one voyage in April 1956, as calculated by an interested party's own accountants. It is not an industry average. Better-sourced figures are in the free sample of chapter 1 of *The Box*, 2nd ed., at <http://assets.press.princeton.edu/chapters/s10724.pdf>: "In 1961, before the container was in international use, ocean freight costs alone accounted for 12 percent of the value of U.S. exports and 10 percent of the value of U.S. imports" (p. 11), and a cost table (p. 12) in which "Half the total outlay went for port costs". Levinson's own caveat, p. 10: "How much the container matters to the world economy has proven challenging to quantify."

### 3.4 The strongest written case that software analogies mislead about hardware

#### PAR-33. "Open source has not pervaded the hardware industry in an analogous way"

- **Source:** Gagan Gupta, Tony Nowatzki, Vinay Gangadhar and Karthikeyan Sankaralingam, "Open-source Hardware: Opportunities and Challenges", arXiv:1606.01980v2, 11 June 2016. <https://arxiv.org/pdf/1606.01980v2> (title page stamped "To Appear in IEEE Computer – Draft – Subject to Change"). Published as "Kickstarting Semiconductor Innovation with Open Source Hardware", *Computer*, vol. 50, no. 6, pp. 50–59, 2017, DOI 10.1109/MC.2017.162.
- **Verification:** Verified 2026-09-18 (PDF downloaded, text extracted, every quote below matched in place). The published *Computer* version was **not** read; note that its title differs, so the quotes must be attributed to the arXiv preprint.
- **What it says:**
  - "Open source has not pervaded the hardware industry in an analogous way. While open source has been fruitful at the system hardware and circuit board levels …, it has been **inconsequential at the semiconductor level** for SoC and FPGA design."
  - Why: "A similar virtuous cycle has not formed for OSH because OSH differs from OSS, preventing analogous pillars from taking hold. We view the differences and resulting challenges as follows: 1. **Fundamental differences.** These are inherent and arise because hardware requires physical embodiment (incurring manufacturing cost) and complex tools (to accomplish multiple non-trivial design processes), and is inherently concurrent (making it complex to reason about)."
  - The sharpest sentence: "Practicality is heavily impacted by hardware's fundamental difference to software of requiring a physical embodiment and complex (expensive) toolchains. **Neither platforms analogous to the PC, nor tools analogous to GCC are available to physically realize and design hardware, posing a significant entry barrier for hobbyists.**"
  - And the practical version: "the FPGA environment setup is often plagued with tool issues taking weeks and months, and is rarely like `apt-get module install`." "Licensing commercial EDA tools and fabricating a prototype can easily cost ∼$1M, well outside an hobbyist's budget". "Developing back-end tools and fabrication requires inputs and design rules from foundries, which they seldom disclose."
- **Bears on:**
  - **H4 (challenges), and it is the best-argued challenge available.** This is the exact argument — that the open-source *software* analogy fails for silicon — made by named academics with semiconductor-architecture standing, peer-reviewed in IEEE *Computer*, naming specific mechanisms rather than gesturing at "hardware is hard".
  - H4 (supports, in part): the paper's own remedy overlaps with `WHY.md` §4 — it says "Fab shuttle services can lower prototyping costs" and expects them to help. The authors are not opponents of the project's thesis; they are describing what has to be true for it to work.
- **Used in:** not yet.
- **Caveats:**
  - It is from 2016, before SKY130, OpenROAD's maturity, Tiny Tapeout and the current wave — so its "∼$1M" figure is out of date in the direction that helps `WHY.md`. OPEN-1, OPEN-4 and OPEN-5 are partly the answer to it. **That is the right way to use this source: as the checklist the project is trying to work through, with the design-tool items now largely ticked and the manufacturing items not.**
  - It is about open-source *hardware*, which is adjacent to but not the same as an open *fab*.

#### PAR-34. Mask sets: the NRE with no software equivalent

- **Source:** Dylan Patel, "The Dark Side Of The Semiconductor Design Renaissance – Fixed Costs Soaring Due To Photomask Sets, Verification, and Validation", SemiAnalysis, 2022-07-24. <https://semianalysis.com/2022/07/24/the-dark-side-of-the-semiconductor/>
- **Verification:** Partial, 2026-09-18. Fetched and the quotes read by a delegated research pass; the date is from the page's own JSON-LD (`datePublished` 2022-07-24T21:54:53+00:00). We did not re-read it. The figures themselves are the author's estimates, not a foundry price list, and no primary source for mask-set prices was found.
- **What it says:**
  - "Every unique chip design requires its own mask set."
  - "On a foundry process node, at 90nm to 45nm, mask sets cost on the order of hundreds of thousands of dollars. At 28nm it moves beyond $1M. With 7nm, the cost increases beyond $10M, and now, as we cross the 3nm barrier, mask sets will begin to push into the $40M range."
  - On respins, which is PAR-6's point from inside the industry: "For Ice Lake, it took Intel 6 revisions to ship, and Sapphire Rapids looks far more abysmal. They have done 12 steppings without it being fully validated for volume shipment. A0, A1, B0, C0, C1, C2, D0, E0, E2, E3, E4, and now E5."
  - And the conclusion, which is `WHY.md`'s own doom spiral stated by an industry analyst: "More companies will not have volumes high enough to amortize their fixed costs associated to mask sets to take advantage of improving cost per transistor." And: "As the semiconductor design renaissance flourishes, it won't all be rosy. There will be a path of littered bodies from failed designs."
- **Bears on:**
  - **H1 (supports), H4 (challenges):** the mask set is a per-design fixed cost with no software analogue at all. Software's equivalent of "make a new version" is free; silicon's is $1m at 28nm on a dedicated set. The shuttle model (PAR-3) exists precisely to amortise this, which is why shuttle economics are the whole game for a small customer.
- **Used in:** not yet. This is the first mask-cost evidence in the repository.
- **Caveats:** a Substack newsletter, not peer-reviewed, and the numbers are estimates. **We looked for a primary source for mask-set prices and did not find one** — foundries do not publish them. Treat these as orders of magnitude. Cross-check available: the eBeam Initiative mask turnaround times in PAR-2 are from an industry survey and are consistent with masks being a major, separately-managed cost and schedule item.

#### PAR-35. "Bits are inherently easier/cheaper to develop and distribute than atoms"

- **Source:** Ben Einstein, "Hardware is NOT the New Software", The Bolt Blog, dated on the page January 28, 2014. <https://blog.bolt.io/hardware-is-not-the-new-software/>. Byline at the foot of the post: "Ben Einstein was one of the founders of Bolt."
- **Verification:** Partial, 2026-09-18. Fetched and quoted by a delegated research pass; we did not re-read it.
- **What it says:**
  - "Everywhere I turn, someone is saying 'hardware is the new software.' Here's why they're wrong."
  - "When you compare hardware and software on paper, it's fairly justifiable: cost of goods is much higher, development time is longer, iterations are harder, manufacturing must be done, distribution channels are expensive, teams need more experience, cash flow is constrained, AND you still have to build a software product."
  - "By no means is building a hardware product the same as building a software product, now or ever. Bits are inherently easier/cheaper to develop and distribute than atoms."
  - But not a counsel of despair: "Hardware will never be as easy as software, but as long as startups and investors are prepared for these differences, the potential to build world-changing hardware companies is higher than ever."
- **Bears on:** H4 (challenges, rhetorically).
- **Used in:** not yet.
- **Caveats:** a short venture-capital blog post from 2014 by an investor with a position in hardware startups. It is recorded because it is a literal, dated rebuttal of the exact slogan `WHY.md` is adjacent to, not because it is strong evidence. PAR-33 carries the argument and PAR-34 the numbers; this one carries the phrasing.

---

## Part 4. The counter-case on the long tail

TAIL-3 already records Elberse's counter-evidence. These are the additions the brief asked for — including the response to Elberse, which cuts the other way and is recorded with the same care.

#### PAR-36. The response to Elberse: online channels really are less concentrated, and search tools are why

- **Source:** Erik Brynjolfsson, Yu Jeffrey Hu and Duncan Simester, "Goodbye Pareto Principle, Hello Long Tail: The Effect of Search Costs on the Concentration of Product Sales", *Management Science* 57, no. 8 (2011): 1373–1386. DOI 10.1287/mnsc.1110.1371.
- **Verification:** **Partial**, 2026-09-18. The abstract was read from the Semantic Scholar Graph API record for the DOI (<https://api.semanticscholar.org/graph/v1/paper/DOI:10.1287/mnsc.1110.1371>), which reproduces the publisher's abstract. The author names and publication date are from OpenAlex (<https://api.openalex.org>), which prints them as "Erik Brynjolfsson, Yu Jeffrey Hu, Duncan Simester"; Semantic Scholar prints the same authors as "Erik Brynjolfsson, Yu Hu, D. Simester". **The full paper was not read**, and the blocker is recorded below.
- **What it says (abstract, verbatim):** "Many markets have historically been dominated by a small number of best-selling products. The Pareto principle, also known as the 80/20 rule, describes this common pattern of sales concentration. However, information technology in general and Internet markets in particular have the potential to substantially increase the collective share of niche products, thereby creating a longer tail in the distribution of sales. This paper investigates the Internet's "long tail" phenomenon. By analyzing data collected from a multichannel retailer, it provides empirical evidence that the Internet channel exhibits a significantly less concentrated sales distribution when compared with traditional channels. Previous explanations for this result have focused on differences in product availability between channels. However, we demonstrate that the result survives even when the Internet and traditional channels share exactly the same product availability and prices. Instead, we find that consumers' usage of Internet search and discovery tools, such as recommendation engines, are associated with an increase the share of niche products."
- **Bears on:**
  - **H5 (supports, and it is the best counter to TAIL-3 in the repository).** Its design is the strong part: the same retailer, the same catalogue, the same prices, two channels — so the difference cannot be availability. The mechanism it identifies is **search and discovery**, not shelf space.
  - H8 (supports, and this is the transferable part): if the tail is made by *discoverability* rather than by availability, then `WHY.md` §5 idea 4 — published prices, visible queues, public results — is doing more work than it appears to. The open fab's catalogue and its search are part of the product.
- **Used in:** not yet. It should be added to `resources/references/long-tail.md` as the response to TAIL-3.
- **Caveats:**
  - **Abstract only.** The effect size, the retailer, the period and the robustness checks are all unread. Do not cite a number from this paper.
  - **Blocker, recorded exactly:** the open-access copy that OpenAlex and Semantic Scholar both point to, <https://dspace.mit.edu/bitstream/1721.1/74642/1/Brynjolfsson_Goodbye%20pareto.pdf>, is behind an AWS WAF CAPTCHA ("Human Verification … you need to verify that you're not a robot by solving a CAPTCHA puzzle"). We did not attempt to solve it. The SSRN copy and the INFORMS publisher page were also unreachable (403). The paper is legitimately open access and we could not legitimately reach it.
  - It is retail consumer goods, not business customers buying manufacturing time — the same limitation TAIL-3 has.

#### PAR-37. Where the tail has been measured since, it is thin

Not a single source; a summary of what this file found, so it is in one place.

- **Verification:** each figure is verified at the entry cited.
- **What it says:**
  - **Web attention:** the top 1,000 properties take 83% of UK time online (PAR-23).
  - **Web money:** two companies take around 80% of UK digital advertising (PAR-22).
  - **Open-source AI:** 206,880 of 5.6 million AI-related GitHub projects reach ten stars — 3.7% (PAR-19).
  - **Open-source contribution:** 17% of top non-npm projects have one developer writing over 80% of commits; 81% have ten or fewer (PAR-12). SW-3's 96%-of-value-from-5%-of-developers is the same shape.
  - **Venture returns:** 6% of venture-backed startups produced about half the gross return (SW-4).
  - **And in the closest physical case:** Shapeways had over one million lifetime customers and one customer at 17–23% of revenue (PAR-26).
- **Bears on:** H5 (challenges), H10 (supports).
- **The honest reading.** Every market where cheap experimentation arrived has the same shape: a very long tail of participants and a very short head that takes the money. `WHY.md` §5 is right that its argument does not need the tail to outsell the head. But it needs something it has not yet claimed out loud: that the tail keeps *paying* even though almost none of it succeeds. PAR-26 is the warning — a business can have a million customers, a thriving-looking tail, and still fail, because the tail does not pay enough and the head it does have is concentrated anyway.

#### PAR-38. Where to look next: process development as learning that cannot be simulated

- **Source:** Gary P. Pisano, "Learning-before-doing in the development of new process technology", *Research Policy* 25, no. 7 (1996): 1097–1119. DOI 10.1016/S0048-7333(96)00896-7.
- **Verification:** **Lead.** 2026-09-18. The citation above is verified against the Crossref record (<https://api.crossref.org/works/10.1016/S0048-7333(96)00896-7>), which gives the author as "Gary P. Pisano", volume 25, issue 7, pages 1097–1119, published print 1996-10. **No content was read.** The publisher page returned HTTP 403, OpenAlex records the work as closed access with no open copy, Semantic Scholar's record states the abstract has been "elided by the publisher", and the EconPapers record carries no abstract. We found no legitimate route to the text.
- **Why it is recorded anyway:** Pisano's distinction between *learning before doing* (simulation, theory, modelling) and *learning by doing* (physical trials) is the academic frame this whole question belongs to, and the repository has no entry in it. His argument, as it is generally described, is that where the underlying science is well understood you can substitute simulation for physical experiment, and where it is not you cannot. Semiconductor process development is the canonical "cannot" case. If that holds, it is the deepest reason cheap simulation does not make cheap silicon, and it would bear directly on H9 and on `WHY.md` §5's learning argument.
- **Bears on:** H9, H4 — direction unknown until someone reads it.
- **Caveats:** everything above after the citation is our characterisation of a paper we have not read. **Do not cite it until someone does.** A university library copy or an interlibrary route would settle it.

#### PAR-39. Manufacturing knowledge is tacit and local, and it travels when people change jobs

- **Source:** Gary P. Pisano and Willy C. Shih, "Restoring American Competitiveness", *Harvard Business Review*, July–August 2009, reprint R0907S. The HBR page at <https://hbr.org/2009/07/restoring-american-competitiveness> is paywalled. The text was read from a freely-hosted reprint PDF at <https://dailyreporter.com/files/2012/11/restoring-american-competitiveness.pdf>, which is stamped "This article is made available to you with compliments of FM Global Insurance."
- **Verification:** Partial, 2026-09-18. The reprint PDF was fetched and the quotes below were read from its extracted text. It is a distributed reprint, not the publisher's version of record, and its own footer restricts further posting — so treat the URL as the reading route, not the citation.
- **What it says:**
  - The industrial commons: "a commons can include R&D know-how, advanced process development and engineering skills, and manufacturing competencies related to a specific technology."
  - **Why it stays put:** "much technical knowledge, even in hard sciences, is highly tacit and therefore far more effectively transmitted face-to-face. Other studies show that the main way knowledge spreads from company to company is when people switch jobs. And even in America's relatively mobile society, it turns out that the vast majority of job hopping is local."
  - And the example that makes the point sharpest: "even though virtually all the raw data from the Human Genome Project … is available electronically all over the world, the drug research it has generated is heavily concentrated in the Boston, San Diego, and San Francisco areas."
  - On outsourcing: "the outsourcing has not stopped with low-value tasks like simple assembly or circuit-board stuffing. Sophisticated engineering and manufacturing capabilities that underpin innovation in a wide range of products have been rapidly leaving too."
- **Bears on:**
  - **H9 (challenges, and it is the most substantive challenge to H9 in the repository).** `WHY.md` §5 argues that thousands of small *public* experiments would pile up experience and give it "far more room to spread". Pisano and Shih's claim is that the part of manufacturing knowledge that matters is tacit, is transmitted face-to-face, and moves between firms mainly when engineers change jobs. Publishing the data may transfer much less than the essay assumes. The Human Genome Project line is the direct counter-example: total data openness, and the capability still concentrated in three cities.
  - This is consistent with LEARN-7, which already records that firms learn about three times more from their own production than from others'.
  - H4 (context): the same argument says design capability and manufacturing capability are not separable, which cuts against "the factory stops doing the customers' engineering".
- **Used in:** not yet.
- **Caveats:**
  - It is an HBR management article, not an empirical paper; the claims about tacit knowledge and job-hopping are summaries of other work that it does not cite in the reprint text we read.
  - Its purpose is an argument about US industrial policy, which is a different question from ours, and it has a clear thesis it is arguing for.
  - **It is a challenge to the *mechanism*, not a refutation.** Open-source software also transmits a great deal of tacit knowledge in public, through review and issue threads, and PAR-15 finds a measurable gain to contributors. The honest position is that publishing results helps less than the essay implies, not that it does not help.

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
| Marginal cost of one more attempt | fractions of a cent to a few dollars of compute | **$300 to €30,000**, or $14,950 commercially (OPEN-5; PAR-3; PAR-31) |
| Time from decision to result | seconds to minutes | **170 to 224 days** (PAR-3); 228 to 451 days (PAR-4) |
| Attempts available per year | thousands | **1 to 5** (PAR-3) |
| Cost of an attempt that fails | the compute you used | the whole attempt, plus the wait, and ~95% of projects need another (PAR-6) |
| Can you revert? | yes, instantly | no |
| Does one customer's failure hurt another's? | no | **yes** — see PAR-25 |

`WHY.md` argues from the first column to the second. Attempts per year differ by about **three orders of magnitude**, and cost per attempt by **at least four**. (The cost ratio is not stated precisely because the software side is not exactly zero and depends entirely on what is being run; three to six orders of magnitude covers any reasonable reading, and the argument does not turn on which.) **An argument that survives a factor of ten is not the same as an argument that survives a factor of a thousand, and the essay never tests it against the larger number.** Everything below is a variation on this.

The honest statement of the project's position after this review is narrower than `WHY.md`'s, and stronger for being narrow:

> Cheap experimentation in silicon means going from *one attempt every few years, for those who can afford several million dollars* to *a few attempts a year, for those who can afford a few thousand*. That is a real and large change. It is not the change that happened to software, and calling it that invites a reader who knows software to expect something that will not arrive.

### 5.1 Cloud computing — **load-bearing for the access model, misleading for the customer mix**

**What transfers.** All of the access mechanism, and it transfers well. A single enormous fixed-cost asset; published prices with no negotiation (SW-2); self-service; pay for what you use; a customer who could never own the asset renting a slice of it. The claim that this model brings in customers who were previously excluded is supported. So is `PRINCIPLES.md`'s "every preference costs money": committed buyers do pay far less per unit (SW-5, PAR-8), and the small flexible buyer pays the premium.

**What breaks.**

1. **The revenue did not follow the tail.** AWS carries about 1.5 years of revenue in contracts longer than a year at a 4.0-year weighted-average life (PAR-7). Its largest announced commercial event is one customer for $38bn over seven years (PAR-10). It pays to acquire the tail (PAR-11).
2. **The purest form of the model concentrated hardest.** CoreWeave rents an expensive shared physical asset by the hour, was founded in the pay-as-you-go era, publishes on-demand prices — and takes 67% of revenue from one customer, with 98% of revenue on **take-or-pay** contracts (PAR-9). That is worse concentration than TSMC's 78% across ten customers (CONC-11). And the instrument it converged on is the same take-or-pay contract that cost AMD $320m and then $335m to escape (CONC-8).
3. **Cycle time.** A cloud customer iterates in seconds; a fab customer 1 to 5 times a year (PAR-3). The cloud's defining property — that a failed experiment costs you an hour and is reverted — does not exist in silicon at all.
4. **The asset is not shared in the same way.** A cloud region is a large number of independent, interchangeable machines. A fab process is one physical resource that every customer's wafer passes through, so customers are coupled (PAR-25). AWS has nothing resembling this.

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

### 5.5 The fifth analogue nobody asked for: self-service physical manufacturing — **load-bearing, and the only one that is**

The four analogues the essay uses are all software. The analogue that actually tests the thesis is a physical one, and it is better evidence than any of them because it removes the one variable that ruins the others: these businesses make things out of atoms.

**What transfers.** All of it, and it is the only place where "all of it" is true. Published prices, instant quoting, no salesperson, no minimum order, thousands or millions of small customers, an expensive machine the customer could never buy. JLCPCB does it at $2.00 and 24 hours with a claimed 9.5 million customers (PAR-31). Protolabs does it profitably while owning its factories (PAR-29). MOSIS has done it for silicon since 1981 (PAR-28). The model is not speculative; it is ordinary.

**What breaks, and it is not what the essay expects.**

1. **It is not cost that separates PCBs from silicon; it is cost *and* time together.** $2.00 and 24 hours versus $14,950 and up to a year (PAR-31). PCB fabrication became a self-service commodity when *both* fell far enough. Silicon has moved a long way on price — from millions to $300 (OPEN-5) — and essentially not at all on time (PAR-1 against PAR-2, PAR-3).
2. **The businesses that own the machines retreat from the tail.** Protolabs says so in writing: "our strategic focus to earn larger orders from our customers", with the customer count down three years running and gross margin down 18 points in twelve years (PAR-29). Shapeways said the same before it failed: "Our customer count may continue to decline as we increase our focus on middle market and enterprise opportunities" (PAR-26). **Two independent firms, in different materials, both drifted from the tail towards the head — under exactly the commercial pressure `WHY.md` §2 describes.**
3. **A million customers did not prevent concentration.** Shapeways had over a million lifetime customers and one customer at 23% of revenue (PAR-26). H7's central assumption — that many small customers means no customer has leverage — has a direct counter-example in the closest available industry.
4. **Nobody has shown it pays.** Protolabs is profitable and shrinking its tail; Xometry is growing its tail and losing $61.7m a year; Shapeways ran a 42% gross margin and liquidated; Fast Radius ran a 10% gross margin and went bankrupt (PAR-26, PAR-27, PAR-29, PAR-30). **There is no example in this file of a company profitably growing a tail of small customers while owning the capital.** MOSIS comes closest and runs on 45 years of government money.

**Verdict: load-bearing, and it is the analogue the project should be arguing from.** It supports H8 strongly and challenges H6 and H7 hard, and both of those are more useful than another software comparison. `WHY.md` would be a much better essay if §5 and §6 argued from JLCPCB, Protolabs and Shapeways instead of from AWS — partly because the evidence is better, and mostly because an informed reader will raise Shapeways whether the essay does or not.

### 5.6 Summary table

| Analogue | Verdict | The one-line reason |
|---|---|---|
| Cloud computing | **Load-bearing for the access model, misleading for the customer mix** | Published self-service pricing brought the customers in; the money went to multi-year take-or-pay commitments, and the purest version of the model is 67% one customer (PAR-7, PAR-9) |
| Open source | **Load-bearing for design, misleading for manufacturing** | Its mechanism is the copy operation, and silicon has none (PAR-12, PAR-33) |
| Machine learning / AI | **Misleading — it is evidence for the doom spiral, not against it** | Training cost growing 2.4× a year; two academic models in 2025 against 93 from industry (PAR-16, PAR-17) |
| The internet / the web | **Illustrative only** | The cost collapse is real and entirely non-physical; the same mechanism produced an 80% advertising duopoly (PAR-20, PAR-22) |
| Self-service physical manufacturing | **Load-bearing — and the project should argue from this one** | The only analogue where the whole mechanism transfers, and the only one that tests H6 and H7 with real balance sheets (PAR-26, PAR-29, PAR-31) |

---

## Part 6. Open questions

Recorded rather than answered, because we could not settle them.

0. **What happened to ES2 (European Silicon Structures), 1985–1993?** A pan-European fast-turnaround electron-beam direct-write fab built explicitly to take designs from many small customers, which failed. **If any historical case is the direct precedent for this project, it is that one, and nobody has checked it.** It is not recorded here even as a Lead entry, because we have read nothing about it. This is the single highest-value unchecked item in the file and it should be someone's next task.
1. **How long does a PROM-style approval take?** PAR-25 shows a shared fab gates new materials through a committee. Nobody publishes the turnaround. If it is days, an open fab can automate it; if it is months, it is a second cycle time stacked on top of the first and it dominates everything.
2. **What is the cost to serve one MPW customer?** H6 needs this and we still do not have it. EUROPRACTICE publishes prices (PAR-3) but not costs. Nobody publishes the staff time per shuttle participant, which is the number that decides whether "no per-customer engineering" is achievable.
3. **What is the respin rate for small, mature-node designs?** PAR-6 gives 5% first-silicon success for IC/ASIC projects generally, weighted towards large commercial designs. The rate for a Tiny Tapeout-scale design on an open PDK is unknown and could be very different in either direction.
4. **Has MPW cycle time improved over 30 years?** PAR-3 gives current figures and the 2020 lead time; PAR-1 and PAR-2 give fab cycle time in 1992–1995 and 2017. We do not have a consistent MPW series. EUROPRACTICE schedules from the 1990s and 2000s would settle it and may exist in the Internet Archive.
5. **Do published prices actually attract small buyers?** H8 asks this and we found no study of price transparency and small-buyer adoption in any industry. The evidence we have is existence proofs (AWS, EUROPRACTICE, JLCPCB), not causal evidence.
6. **Is there a post-EUV measurement of cycle time at 7nm or 5nm?** PAR-2's 80–100 day figures were a 2017 projection that explicitly assumed no EUV. We found no measured replacement.
7. **What does an open fab do about the externality one customer imposes on the next?** No mechanism in `PRINCIPLES.md` or `AUCTIONS.md` prices it (PAR-25). Insurance is the obvious candidate and it is not obvious that it works: the loss is another party's yield, discovered late, and hard to attribute.
8. **Does the aggregator reading change the thesis?** Part 5.4 argues the web's evidence supports "be the aggregator", and the aggregator position is a near-monopoly in every case examined. If that is right, the project is claiming winner-take-most economics, which is a different and much stronger claim than `WHY.md` makes. Nobody has decided whether the project intends it.
9. **Is there any example of a company profitably growing a tail of small customers while owning the capital?** This file did not find one (Part 5.5, point 4). Protolabs is profitable and shrinking its tail; Xometry is growing its tail and losing money; Shapeways and Fast Radius failed; MOSIS is subsidised. If such an example exists it would be the most valuable single piece of evidence for H6 and H7, and if it does not exist that is itself the finding.
10. **Does Pisano's learning-before-doing distinction hold for semiconductor process development?** PAR-38 records the citation and nothing else, because no legitimate route to the text was found. It bears directly on H9.

---

## Changes needed in other files

This file does not edit anything else. Everything below is a change someone else should make.

### `resources/hypotheses.md`

The README's rule is that adding an entry means updating the hypothesis it bears on. These are the updates this file implies.

| Hypothesis | Change |
|---|---|
| **H1** | Add PAR-16 and PAR-17 as **supports by analogy** — frontier AI reproduced the doom spiral in a decade. Add PAR-2 as **supports**: the leading edge is getting slower as well as dearer. Add PAR-34 as **supports**: mask-set cost per design rising from hundreds of thousands at 90nm to an estimated $40m at 3nm. |
| **H2** | Add PAR-9 as **supports**: CoreWeave's risk factors are GlobalFoundries' risk factors. |
| **H3** | Add PAR-1 as **mixed**: "fab size above 7,000 wafer starts per week does not improve performance" is a measured limit on the returns to scale that Step 3 assumes. |
| **H4** | Status should change from "Contested" to note a second axis. Add PAR-2, PAR-3, PAR-4 and PAR-6 as **challenges**: cost is not the only barrier, and cycle time and respin rate are not falling. Add PAR-33 as the **best-argued challenge available**, and PAR-34 for mask cost. Add PAR-5 as **supports**. Promote the existing hedge "at least on mature processes" to a premise (see PAR-17). |
| **H5** | Add PAR-5 as the **strongest support** yet recorded (360 designs manufactured out of 600+ submissions). Add PAR-3 and PAR-4 as **challenges** (1–5 attempts a year). Add PAR-22, PAR-23, PAR-19 and PAR-37 as **challenges** — the tail is thin wherever it has been measured. Add PAR-36 as a **support** and as the response to TAIL-3. Add PAR-24 as **supports**. Add PAR-26, PAR-27 and PAR-29 as **challenges**. |
| **H6** | Add PAR-7, PAR-9 and PAR-11 as **challenges**: the cloud's money is in committed contracts and it pays to acquire the tail. Add PAR-25 as a **challenge**: "no per-customer engineering" is contradicted by the PROM committee that makes a shared fab possible. Add PAR-27 (a 10% gross margin on self-serve on-demand manufacturing) and PAR-29 (Protolabs' gross margin down 18 points in twelve years) as **challenges**. |
| **H7** | Add PAR-9 as the **strongest challenge in the repository**, and PAR-26 as the second: a company with over a million lifetime customers still had one customer at 23% of revenue. Add PAR-10 and PAR-22. Add PAR-29 as the best **support** H7 has — a profitable, capital-owning manufacturer with no customer above 2%. The status should move from "Argued from theory" to "Contested". |
| **H8** | Add PAR-3 as **supports with a sting**: the open, published-price, self-service shuttle model already exists and has not transformed the industry. Add PAR-31 as **strong support** in a physical industry (JLCPCB: published price, published lead time, 9.5 million claimed customers) and PAR-32 for standardised interfaces. Add PAR-24 as **mixed**: arXiv replaced the gate rather than removing it. Add PAR-21 and PAR-28 (MOSIS has done this since 1981, on public money). The "Needs" line about price transparency and small-buyer adoption is still unmet; see Part 6 item 5. |
| **H9** | Add PAR-39 as the **most substantive challenge** — manufacturing knowledge is tacit and local, so publishing results may transfer less than §5 assumes. Add PAR-15 as the **closest published support**, noting it locates the gain in the contributor, not the platform. Add PAR-17 and PAR-25 as **challenges**. Add PAR-12 as **mixed**. Add PAR-38 as a **Lead** worth chasing. |
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
8. **§6 should answer Shapeways.** The section is called "It can't work" and lists the objections. The strongest objection is not in it: two public companies built this business in physical manufacturing and both went bankrupt, and the one that survives is deliberately shedding its small customers (PAR-26, PAR-27, PAR-29). An informed reader will raise it. Better to raise it first.
9. **Consider replacing the software analogies in §5 and §6 with physical ones.** JLCPCB at $2.00 and 24 hours (PAR-31) makes the case for published self-service pricing better than AWS does, in the right kind of industry, and it comes with the honest contrast that the same model in silicon costs $14,950 and takes a year.

### `resources/references/software-analogies.md`

- **SW-5** should cross-reference PAR-8 (Google Cloud's committed-use discounts, which are explicitly take-or-pay: "You are billed monthly for your committed resources … regardless of whether or not you use those resources") and PAR-9. SW-5's caveat currently frames the brief's reading as the unfriendly one; PAR-7 and PAR-9 make the brief's reading the better-supported one.
- **SW-1** (Andreessen's hundredfold figure) should cross-reference PAR-21, which gives the same story from the sellers' own published prices rather than from an investor anecdote.
- **SW-3**'s caveat about the Open Path critique is still a Lead. Separately, PAR-12 adds what SW-3 does not: the contributor concentration behind the value concentration.

### `resources/references/open-silicon-and-ai.md`

- **OPEN-7** (Efabless's closure) should record the successor: efabless.com now states "Umbralogic Technologies LLC, doing business as ChipFoundry, has acquired the assets of Efabless Corporation", and ChipFoundry's chipIgnite is selling tape-outs at "$14,950 / per tapeout" (PAR-28, PAR-31). It should also note that the CEO quote it carries appears only in secondary reporting; we found no primary source for it.
- **OPEN-5** (Tiny Tapeout at $300) should record the published wait alongside the price: "The chips are taking between 6 and 9 months to manufacture … So expect up to 1 year's wait time!" (PAR-31), and PAR-4's measured 228–451 days from shuttle close to shipped chips.
- A new entry is warranted for **MOSIS**, which has run an open, published-price, many-small-customers silicon shuttle continuously since 1981 and is still running as "MOSIS 2.0" under the CHIPS Act (PAR-28). It is both the best precedent for the project and the sharpest question about it, since it has never stood without public funding.

### `resources/references/long-tail.md`

- **PAR-36** should be added here as the direct response to TAIL-3: Brynjolfsson, Hu and Simester (2011) find the internet channel significantly less concentrated than the traditional channel *at the same retailer with the same catalogue and prices*, and attribute it to search and discovery tools rather than to shelf space. Abstract only; the blocker is recorded at PAR-36.
- The Lead at the end of TAIL-3, "The Long Tail Debate: A Response to Chris Anderson" (2008), is **blocked**: <https://hbr.org/2008/07/the-long-tail-debate-a-respons> serves only the header and the first sentence to an unauthenticated reader. Verified from that fragment: the author is Anita Elberse and the piece opens "my recent article in the _Harvard Business Review_, '[Should You Invest in the Long Tail?]' has stirred up a debate among long-tail enthusiasts and critics alike." The body was not read. Record it as blocked rather than leaving it as an open Lead.
- The "Evidence that would help" list should be updated: PAR-5 supplies the shuttle oversubscription figure it asks for, and PAR-4 supplies a submissions-over-time series.

### `resources/README.md`

- The "Reference topics" table lists ID prefixes for files in `references/`. `PAR` is used in an `analyses/` file. Either add a line noting that analyses may also carry an ID prefix, or move these entries into `references/`. Our preference is to leave them here, because the adjudication in Part 5 is the point of the file and it is not a reference list.
