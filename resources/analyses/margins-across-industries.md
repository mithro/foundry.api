# What a 22.7% operating margin is actually worth

*Our own synthesis, 2026-09-25, joining [`demand/software-margins.md`](../demand/software-margins.md)
(`SWM-1`…`SWM-9`) and [`demand/semiconductor-margins.md`](../demand/semiconductor-margins.md)
(`SEM-1`…`SEM-8`). Both were built from the SEC's free XBRL frames API across 3,598 filers, with
reproducible scripts in [`tools/sec_margins/`](../../tools/sec_margins/) and `tools/`.*

**This file exists because the question was first answered from memory, and the memory was wrong in
its central reasoning.** The claim made in conversation was: *"a fab and a SaaS business on the same
operating margin are not equally good businesses; the fab is worse,"* because software carries
almost no fixed assets and therefore turns them over faster.

**That is backwards, and the data says so plainly.**

---

## 1. The reasoning that was wrong

The argument rested on software having much higher asset turnover than a fab. Measured:

| | Asset turnover | vs Silex (0.617×) |
|---|---:|---:|
| **Silex Microsystems** | **0.617×** | — |
| SIC 7372 median | 0.546× | **0.89×** |
| SIC 7372, revenue > $1bn | 0.505× | 0.82× |
| SIC 7372 revenue-weighted aggregate | 0.416× | **0.67×** |
| SIC 7372 p75 | 0.774× | 1.26× |
| SIC 7372 p90 | 1.149× | 1.86× |

**The median listed software company turns its assets over more slowly than a MEMS wafer foundry.**
The reason is that a software balance sheet is mostly cash, marketable securities and goodwill —
none of which produces revenue. On the like-for-like correction (both sides ex cash and goodwill,
Silex 0.6995×) software does pull ahead, to **1.404×**, but that is a far cry from the order of
magnitude the original argument assumed.

So the answer to *"at equal operating margin, how much better is software?"* is **0.68× to 1.86×** —
a band that straddles one — **not 3×**.

## 2. The distribution, which is the part that actually answers the question

CY2025, medians and quartiles because these tails are extreme (`SWM-2`):

| SIC group | n | p25 | **median op margin** | p75 | **median ROA** |
|---|---:|---:|---:|---:|---:|
| **7372 Prepackaged Software** | 211 | −26.1% | **−4.5%** | 9.1% | **−2.2%** |
| All 737x software and data | 411 | −32.2% | **−3.3%** | 9.5% | **−1.9%** |
| 3674 Semiconductors | 86 | −21.0% | **1.0%** | 12.6% | **0.4%** |
| All filers with the tags | 3,598 | −23.9% | **2.1%** | 12.8% | **1.4%** |
| 7372, revenue $100m–$1bn *(Silex's band)* | 82 | −15.1% | **−3.0%** | 4.4% | **−2.1%** |
| 7372, revenue > $1bn | 68 | −2.1% | **10.7%** | 22.2% | **5.3%** |

**The median listed software company loses money at the operating line.** Not "has a thin margin" —
loses money. In Silex's own revenue band, the median is **−3.0%**.

### Where Silex falls

| Group | 22.67% (operating company) | 26.57% (group) | ROA 16.38% |
|---|---:|---:|---:|
| SIC 7372 Software | **89.1st** | **91.0th** | **94.8th** |
| All 737x | 88.6th | 91.2nd | 92.2nd |
| All 3,598 filers | 87.8th | 91.0th | 93.0rd |
| 7372, $100m–$1bn | **95.1st** | **95.1st** | 93.9th |
| SIC 3674 Semiconductors | 82.6th | 88.4th | 89.5th |

**A MEMS wafer foundry is in the top decile of the software industry on its own preferred measure.**

## 3. The number the original question wanted

*What operating margin would a fab need to match software's return on assets?* Divide by Silex's
0.617× turnover (`SWM-6`):

| Benchmark | Its ROA | Margin a fab needs |
|---|---:|---:|
| SIC 7372 median | −2.16% | −3.50% |
| SIC 7372 p75 | 5.47% | 8.87% |
| **7372 revenue-weighted aggregate** | **11.33%** | **18.38%** |
| **7372 top decile** | **11.73%** | **19.02%** |
| Intuit | — | 21.60% |
| SAP | — | 22.17% |
| **AWS** | **18.06%** | **29.29%** |
| Microsoft | 20.76% | 33.66% |
| Adobe | — | 47.87% |

**A fab at 22.67% clears the whole listed software industry in aggregate and its top decile. It is
beaten by AWS, Microsoft and Adobe, and by nothing else measured.**

## 4. Two things that inflate the software figures people quote

**Non-GAAP** (`SWM-5`, eight companies' own 8-K reconciliations). The GAAP→non-GAAP gap runs
**9.61 pp (Adobe) to 41 pp (Snowflake), median 22.55 pp**, and stock-based compensation — 8.30% to
36.52% of revenue — explains most but not all of it. **Six of the eight are below Silex on GAAP and
four are loss-making.** The headline margins in the trade press are not the ones in the accounts.

**Survivorship in the basket.** Picking Microsoft, Adobe and Oracle and calling it "software" is
selecting the top decile. The median is negative.

## 5. The finding that most damages an argument this project actually uses

**`SWM-7`: the cloud analogy has stopped being asset-light.**

| AWS, 2025 | |
|---|---:|
| Net sales | $128,725m |
| Operating income | $45,606m = **35.43%** |
| Segment assets | $252,588m |
| Asset turnover | **0.510×** |
| Return on assets | **18.06%** (down from 25.54% in 2024) |
| **P&E additions** | **$96,496m = 74.96% of revenue** |
| **Net PP&E** | **$190,055m = 147.64% of revenue** |

**AWS's capex intensity is 5.32× Silex's and 2.27× TSMC's.** Oracle's net PP&E is **148.40%** of
revenue — higher than TSMC, UMC, GlobalFoundries or Tower. Microsoft's FY2026 capex is **34.94%** of
revenue. CoreWeave, which the SEC classifies as *Services-Prepackaged Software*, spent **200.92% of
revenue** on plant.

**[`analyses/industry-parallels.md`](industry-parallels.md) leans on cloud as the model for
API-first, self-service, utility-priced infrastructure. That parallel is still sound on the demand
side and is now dead on the balance sheet.** "The AWS of silicon" in 2026 means a business with a
fab's capital structure at ten times the scale. Anyone using the analogy must stop implying it
escapes capital intensity.

## 6. And the finding that most damages the fab side

**22.7% is not what a specialty fab earns. It is what the second-best one earns** (`SEM-4`).

| | Operating margin | ROA |
|---|---:|---:|
| TSMC | 50.83% | 24.41% |
| **Silex** | **26.57%** | **16.38%** |
| UMC | 18.50% | 7.75% |
| Tower | 12.40% | 5.84% |
| GlobalFoundries | 11.74% | 4.65% |
| X-FAB | 8.78% | 3.93% |
| SkyWater | −0.58% | −0.35% |
| Powerchip | −15.31% | −3.91% |

**Peer median: 12.07% margin, 4.29% ROA.** Silex is **3.82× the peer median**, and three of ten
listed pure-play foundries lost money in FY2025.

`SEM-8`'s conclusion, which this file adopts: **the planning number for a new entrant is the peer
median, not Silex.** Silex is a 23-year-old, largely depreciated, single-site 200 mm fab running at
**60% utilisation** with a customer book that mostly predates 2017. A new entrant has none of those.

## 7. What the two sides agree on

**Capital intensity does not explain margins on either side of the comparison.**

- Semiconductors (`SEM-7`): across 67 SIC 3674 filers, **Spearman ρ(PP&E ÷ revenue, operating
  margin) = +0.050**, against a 5% critical value of ±0.24. The *least* capital-intensive quartile
  is the *worst* (−4.98%). TI carries PP&E at 69.7% of revenue and earns 34.06%.
- Software (`SWM-7`): the most capital-intensive businesses in the sample — AWS, Oracle, CoreWeave —
  are among the most profitable, not the least.

**The penalty for owning plant is to turnover, not to margin.** Plant-owning median turnover 0.476×
against 0.519×, i.e. about **9% more margin needed for the same return**. That is a real cost and it
is an order of magnitude smaller than the folk version of the story.

## 8. What may be cited, and what may not

| Claim | Status |
|---|---|
| Silex is at the 89th–95th percentile of listed software on operating margin | **Citable.** `SWM-3` |
| The median listed software company loses money at the operating line | **Citable.** `SWM-2` |
| A fab at 22.67% beats software's revenue-weighted aggregate ROA | **Citable.** `SWM-6` |
| AWS capex is 74.96% of revenue, 5.32× Silex's | **Citable, and it cuts against us.** `SWM-7` |
| Peer-median foundry economics are 12.07% / 4.29%, not Silex's | **Citable. Use this for planning.** `SEM-4` |
| Capital intensity does not predict margin | **Citable.** `SEM-7`, `SWM-7` |
| **"Software is a far better business than a fab"** | **WITHDRAWN. Not supported at the median on any measure computed here.** |
| Silex's 86.3% "Gross margin 1" | **Never compare with a software gross margin** — it is net sales less raw materials only |

## 9. Caveats that travel with all of it

- **US SEC registrants only.** No private software companies, no non-SEC filers. The software
  population is therefore listed companies, which skews large and skews toward the growth-funded.
- **Ending assets, not average.** Fine for stable balance sheets, less so for anyone mid-acquisition.
- **The ex-cash-and-goodwill correction removes cash and equivalents only** — there is no consistent
  marketable-securities tag — so it **understates** software's operating-asset turnover. The 1.404×
  is a floor.
- **Silex's parent/group boundary**: 22.67% is Silex Microsystems AB, 26.57% the consolidated group
  including Silex Properties AB. Both are carried everywhere. Return-on-assets work uses the group
  figure, because the balance sheet is consolidated.
- **TSMC's and UMC's FY2025 20-F facts are not yet in SEC `companyfacts`**, so those rows are read
  from the filings directly or are FY2024.
- **AWS's share of Amazon's $247.8bn of unallocated corporate assets is undisclosed**, so its ROA is
  computed on disclosed segment assets and is therefore an upper bound.
