# Semiconductor margins, and where a specialty fab actually sits (`SEM`)

## What this file is for

[`fab-local-news-intl.md`](fab-local-news-intl.md) `LNI-17` records that **Silex Microsystems, the
world's largest pure-play MEMS foundry, earned SEK 314 million of operating profit on SEK 1,385
million of net sales in 2025 — a 22.7% operating margin.** That is the most encouraging single
number in this directory, and until now it has had nothing to be compared against except
recollection.

This file replaces the recollection with measurement. It does three things:

1. **Finishes Silex.** The repo had its income statement and not its balance sheet. `SEM-1` reads
   the balance sheet, the cash-flow statement and the depreciation note out of the IPO prospectus,
   so Silex can be judged on **return on assets** rather than on margin. A fab's margin is struck
   after depreciating a cleanroom; the margin on its own tells you almost nothing.
2. **Builds the distribution.** `SEM-3` computes, from the SEC's free XBRL data, the whole
   distribution of operating margin, asset turnover, return on assets and capital intensity across
   **every SEC filer in SIC 3674** and four neighbouring codes — not a hand-picked basket — so that
   22.7% gets a percentile.
3. **Names the peers.** `SEM-4` puts every listed pure-play and specialty foundry we could reach
   into one table from its own filings, in its own reporting currency, with the arithmetic visible.

Everything here is reproducible. `tools/sec_fetch.py`, `tools/semiconductor_margins.py`,
`tools/foundry_peers.py`, `tools/peer_table.py` and `tools/silex_returns.py` are committed
alongside it, and the figures below are their output.

## What it found, in one paragraph

**Silex is not typical. It is second only to TSMC.** Among ten listed pure-play and specialty
foundries, Silex's 22.7% (26.6% on the consolidated figure) is beaten by TSMC alone; the median of
the group is **12.07%**, and three of the ten lost money. Against the whole of SIC 3674 — 73 SEC
filers with revenue over $10m — the **median operating margin is 1.48%** and Silex sits at the
**82nd percentile** (89th on the consolidated figure). On return on assets, which is the honest
cross-industry measure, Silex's 16.38% is at the **89th percentile** of SIC 3674, at the **91st**
of the plant-owning subset, and **3.82× the foundry peer median of 4.29%**. **And it does this at about 60 percent capacity utilisation**, which
the prospectus states three separate times. Two findings cut hard the other way. First, capital
intensity does **not** explain semiconductor margins: across SIC 3674 the rank correlation between
PP&E-to-revenue and operating margin is **+0.05**, i.e. nothing, so the comforting story that fabs
earn low margins *because* they are capital-heavy is not supported by the data. Second, the peer
with by far the largest customer count — X-FAB, with more than 400 customers against Silex's 85 —
earns **8.78%**, a third of Silex's margin, which is the opposite of what H7 predicts.

## Entry IDs

`SEM-1` … `SEM-8`. Entries are at heading level `###` so `tools/check_resources.py` can find them.

---

### SEM-1. **Silex's balance sheet, at last: SEK 2,246 million of total assets, 0.617× asset turnover and a 16.38% return on assets** — the figure the whole cross-industry comparison needed

- **Source:** Silex Microsystems AB (publ), *Invitation to acquire ordinary shares in Silex
  Microsystems AB (publ)* — the IPO prospectus, 230 pages, approved and published by
  **Finansinspektionen** on **2026-04-27**, diary number **25-37533**. Consolidated statement of
  profit or loss p. 103, consolidated statement of comprehensive income p. 104, consolidated
  balance sheet pp. 105–106, consolidated statement of cash flows p. 107, alternative performance
  measures p. 108, depreciation note p. 122.
  - Register entry: <https://www.fi.se/sv/vara-register/prospektregistret/details?id=25-37533>
  - Document: <https://www.fi.se/sv/vara-register/prospektregistret/GetFile?id=25-37533>
- **Verification:** Verified. The PDF was downloaded with the detail page as `Referer`
  (SHA-256 `a4c363ed5dc05c7a069591a797431cc25bd0c9ef0b15c5a27faf7b4fe472c911`, 11,725,825 bytes) and
  read with `pdftotext -layout`, which yields 14,475 lines. Every figure below is copied from that
  extraction. The prospectus is in English.
- **Date checked:** 2026-09-25
- **Bearing:** **Supports** H6 and **Supports** H5 on the capital side; **Context** for H2. It also
  **corrects** `LNI-17`, which took its figures from an aggregator's rendering of the operating
  company's filed accounts and not from the group's audited statements.
- **How it was counted:** `uv run tools/silex_returns.py`. Every input is a printed figure; every
  ratio is shown as a division below.

**The consolidated statement of profit or loss, as printed (MSEK):**

| | 2023 | 2024 | 2025 | Q1 2025 | Q1 2026 |
|---|---:|---:|---:|---:|---:|
| Net sales | 1,095 | 1,226 | **1,385** | 334 | 375 |
| Other operating income | 56 | 81 | 58 | 14 | 31 |
| Total revenue | 1,151 | 1,307 | 1,443 | 349 | 407 |
| Raw materials and supplies | (226) | (226) | (190) | (47) | (54) |
| Other external expenses | (199) | (268) | (324) | (59) | (80) |
| Personnel expenses | (336) | (353) | (383) | (96) | (109) |
| Depreciation and amortisation | (108) | (117) | (125) | (31) | (31) |
| Other operating expenses | (5) | (5) | (54) | (30) | (5) |
| Total expenses | (875) | (968) | (1,075) | (262) | (278) |
| **Operating profit** | **276** | **339** | **368** | **87** | **128** |
| Profit for the period | 214 | 273 | 269 | 61 | 103 |

**The consolidated balance sheet, as printed (MSEK) — this is the part the repo did not have:**

| Assets, at 31 December | 2023 | 2024 | 2025 | at 31 March 2026 |
|---|---:|---:|---:|---:|
| Intangible assets | 1 | 0 | 0 | 0 |
| Buildings and land | 401 | 426 | 439 | 434 |
| Machinery and other technical facilities | 368 | 348 | 314 | 302 |
| Equipment, tools, fixtures and fittings | 17 | 15 | 20 | 18 |
| Construction in progress | 35 | 36 | **169** | 196 |
| Right-of-use assets | 412 | 415 | 369 | 357 |
| Long-term receivables from Group companies | 277 | – | – | – |
| Deferred tax assets | 8 | 8 | 20 | 21 |
| **Total non-current assets** | **1,519** | **1,248** | **1,331** | **1,329** |
| Inventory | 205 | 191 | 222 | 219 |
| Trade receivables | 253 | 312 | 325 | 416 |
| Current receivables from Group companies | 15 | 24 | – | – |
| Derivatives | – | 11 | 12 | – |
| Other current receivables | 20 | 22 | 38 | 24 |
| Prepaid expenses and accrued income | 25 | 24 | 52 | 55 |
| Cash and cash equivalents | 311 | 434 | 266 | 334 |
| **Total current assets** | **830** | **1,018** | **915** | **1,049** |
| **TOTAL ASSETS** | **2,349** | **2,265** | **2,246** | **2,377** |

| Equity and liabilities, at 31 December | 2023 | 2024 | 2025 | at 31 March 2026 |
|---|---:|---:|---:|---:|
| Share capital | 4 | 4 | 5 | 5 |
| Other paid-in capital | 508 | 530 | 553 | 553 |
| Reserves | 27 | 50 | 47 | 37 |
| Retained earnings incl. profit for the period | 919 | 809 | 827 | 931 |
| **Total equity attributable to shareholders of the Parent** | **1,458** | **1,394** | **1,433** | **1,526** |
| Non-current lease liabilities | 180 | 154 | 106 | 91 |
| Liabilities to credit institutions (non-current) | 216 | 197 | 179 | 175 |
| Deferred tax liabilities | 75 | 89 | 111 | 109 |
| Derivative financial instruments | 3 | 2 | 1 | 1 |
| **Total non-current liabilities** | **474** | **443** | **397** | **375** |
| **Total current liabilities** | **416** | **429** | **415** | **476** |
| **Interest-bearing net debt** (non-IFRS) | **195** | **16** | **101** | **14** |
| Equity ratio, % (non-IFRS) | 62.1 | 61.5 | 63.8 | 64.2 |

**Capital expenditure, depreciation and cash flow, as printed (MSEK):**

| | 2023 | 2024 | 2025 | Q1 2025 | Q1 2026 |
|---|---:|---:|---:|---:|---:|
| Net cash flows from operating activities | 352 | 377 | 353 | 84 | 112 |
| **Investment in tangible fixed assets (capex)** | **(111)** | **(78)** | **(195)** | (22) | (28) |
| Acquisition of subsidiaries | (430) | – | – | – | – |
| Dividends paid | (278) | (383) | (250) | – | – |
| Depreciation — buildings | 19 | 19 | 20 | 5 | 5 |
| Depreciation — machinery and other technical equipment | 44 | 49 | 49 | 12 | 13 |
| Depreciation — inventories and tools | 6 | 6 | 9 | 2 | 2 |
| Depreciation — leases (machinery and building) | 39 | 43 | 47 | 11 | 11 |
| Amortisation of intangible assets | 1 | 1 | 0 | 0 | 0 |
| **Depreciation and amortisation, total** | **108** | **117** | **125** | **31** | **31** |
| EBITDA (non-IFRS) | 384 | 456 | 493 | 118 | 159 |
| Adjusted EBIT (non-IFRS) | 276 | 355 | 397 | 92 | 133 |
| Capital employed (non-IFRS) | 1,965 | 1,843 | 1,800 | 1,883 | 1,875 |
| Return on capital employed, % (non-IFRS) | 14.4 | 17.8 | 20.2 | 18.4 | 21.8 |

And the depreciation policy, which matters because it is conservative and therefore depresses the
margin:

> "Silex applies a 12-year depreciation period, despite that average asset lifespan is typically
> 20 years."

- **DERIVED (arithmetic written out):** script `tools/silex_returns.py`.

  | | 2023 | 2024 | 2025 |
  |---|---:|---:|---:|
  | Operating margin = EBIT ÷ net sales | 276 ÷ 1,095 = **25.21%** | 339 ÷ 1,226 = **27.65%** | 368 ÷ 1,385 = **26.57%** |
  | Asset turnover = net sales ÷ total assets | 1,095 ÷ 2,349 = **0.4662×** | 1,226 ÷ 2,265 = **0.5413×** | 1,385 ÷ 2,246 = **0.6167×** |
  | **Return on assets = EBIT ÷ total assets** | 276 ÷ 2,349 = **11.75%** | 339 ÷ 2,265 = **14.97%** | 368 ÷ 2,246 = **16.38%** |
  | check: margin × turnover | 0.252055 × 0.466156 = 11.75% | 0.276509 × 0.541280 = 14.97% | 0.265704 × 0.616652 = 16.38% |
  | Return on equity = profit for the period ÷ equity | 214 ÷ 1,458 = **14.68%** | 273 ÷ 1,394 = **19.58%** | 269 ÷ 1,433 = **18.77%** |
  | Owned PP&E (buildings + machinery + equipment + CIP) | 401+368+17+35 = **821** | 426+348+15+36 = **825** | 439+314+20+169 = **942** |
  | PP&E ÷ total assets | 821 ÷ 2,349 = **34.95%** | 825 ÷ 2,265 = **36.42%** | 942 ÷ 2,246 = **41.94%** |
  | PP&E ÷ net sales | 821 ÷ 1,095 = **0.7498×** | 825 ÷ 1,226 = **0.6729×** | 942 ÷ 1,385 = **0.6801×** |
  | PP&E + right-of-use ÷ net sales | 1,233 ÷ 1,095 = **1.1260×** | 1,240 ÷ 1,226 = **1.0114×** | 1,311 ÷ 1,385 = **0.9466×** |
  | Capex ÷ net sales | 111 ÷ 1,095 = **10.14%** | 78 ÷ 1,226 = **6.36%** | 195 ÷ 1,385 = **14.08%** |
  | D&A ÷ net sales | 108 ÷ 1,095 = **9.86%** | 117 ÷ 1,226 = **9.54%** | 125 ÷ 1,385 = **9.03%** |
  | D&A ÷ owned PP&E | 108 ÷ 821 = **13.15%** | 117 ÷ 825 = **14.18%** | 125 ÷ 942 = **13.27%** |
  | Capex ÷ D&A | 111 ÷ 108 = **1.03×** | 78 ÷ 117 = **0.67×** | 195 ÷ 125 = **1.56×** |
  | EBITDA ÷ total assets | 384 ÷ 2,349 = **16.35%** | 456 ÷ 2,265 = **20.13%** | 493 ÷ 2,246 = **21.95%** |

  - **On average rather than year-end assets**, which is how return on assets is usually struck:
    2024 average assets = (2,265 + 2,349) ÷ 2 = 2,307.0, so EBIT ÷ average assets =
    339 ÷ 2,307.0 = **14.69%** and turnover = 1,226 ÷ 2,307.0 = **0.5314×**; 2025 average assets =
    (2,246 + 2,265) ÷ 2 = 2,255.5, so EBIT ÷ average assets = 368 ÷ 2,255.5 = **16.32%** and
    turnover = 1,385 ÷ 2,255.5 = **0.6141×**. The year-end and average figures agree to within
    0.3 percentage points, because the balance sheet has barely moved in three years.
  - **Q1 2026, annualised (unaudited interim, so illustrative):** operating margin
    128 ÷ 375 = **34.13%**; asset turnover (375 × 4) ÷ 2,377 = **0.6310×**; return on assets
    (128 × 4) ÷ 2,377 = **21.54%**.
  - **Reconciling with `LNI-17`.** `LNI-17` quotes operating profit of **SEK 314m** for 2025, from
    allabolag's rendering of *Silex Microsystems AB*'s own filed accounts. The prospectus's
    consolidated figure is **SEK 368m**. The difference is 368 − 314 = **54 MSEK**, or 3.90% of net
    sales, and it is the group's *Other* segment — the note on p. F-7 says "The segments defined by
    Silex are MEMS and Other… The Other segment comprises the Group's real estate operations…
    revenue from the Other segment is reported under Other operating income… mainly… rental income
    from the real estate operations." In other words, the operating company pays rent to a sister
    company, and the group figure keeps it. **Both numbers are right for their own boundary:**
    314 ÷ 1,385 = **22.67%** at the operating company, 368 ÷ 1,385 = **26.57%** at the group.
    Everything downstream in this file quotes both.
  - **The fab cost SEK 1.9 billion in total.** "Between the establishment of the Company and
    31 March 2026, Silex's capital expenditure amounted to a total of SEK 1.9 billion" (p. 84,
    footnoted "Refers to investments in tangible fixed assets, as well as investments in
    right-of-use assets and sale-and leaseback transactions, excluding the acquisition of Silex
    Properties AB"). Against that: 2025 net sales ÷ cumulative capex = 1,385 ÷ 1,900 = **0.7289×**,
    and 2025 EBIT ÷ cumulative capex = 368 ÷ 1,900 = **19.37%**. **A 200 mm specialty fab that
    cost SEK 1.9 billion cumulative — about USD 194 million at the ECB 2025 average — throws off
    SEK 368 million of operating profit a year.** That is a far smaller number than any of the
    greenfield capital costs in [`fab-local-news.md`](fab-local-news.md), and it is the most
    important scale datum in this file.
- **Caveats.** The 2023 balance sheet was restated by the company when it moved from the
  "function of expense" to the "nature of expense" presentation, and the prospectus says so in a
  footnote to both balance-sheet pages. The Q1 2026 column is unaudited interim information
  reviewed under ISRE 2410, not audited. "Other operating expenses" jumps from 5 to 54 MSEK in
  2025 and the company's own Adjusted EBIT adds back SEK 29m of non-recurring items, so the clean
  2025 margin is arguably the adjusted 397 ÷ 1,385 = **28.66%**, not 26.57%. Total assets include
  SEK 266m of cash; on assets net of cash, 2025 return on assets is 368 ÷ (2,246 − 266) =
  **18.59%**.

---

### SEM-2. **Silex earns that margin at about 60 percent utilisation, and says so three times** — plus the confirmed negative: no wafer starts, no average selling price, in 230 pages

- **Source:** the same prospectus, diary number 25-37533. The utilisation statements are on p. 25
  (risk factors), p. 86 (business overview) and p. 119 (operating and financial review).
- **Verification:** Verified. Same extraction as `SEM-1`.
- **Date checked:** 2026-09-25
- **Bearing:** **Supports** H5 and H6, strongly. **This entry corrects a previous pass**, which
  reported that the prospectus contains no utilisation figure. It contains three, and they agree.
- **What it says.** From p. 86:

  > "Silex currently operates at a medium utilisation level of approximately 60 percent, with
  > employees working in five shifts, 365 days a year 24/7 through rotating shift work to allow for
  > constant manufacturing."

  > "Utilisation remains well below maximum capacity, providing significant headroom to scale
  > production within the existing facility, while at the same time offering development
  > turnaround times that are market leading. Silex believes there is potential to achieve
  > approximately 100 percent additional revenue, depending on product mix in its current 200 mm
  > wafer production in Järfälla."

  From p. 119:

  > "Silex currently operates at medium utilisation levels of approximately 60 percent with
  > constant manufacturing 24/7 supported by rotating shift work by its employees. … Currently,
  > utilisation remains well below maximum capacity, providing significant headroom to scale
  > production within the existing facility, and Silex believes there is potential to achieve
  > approximately 100 percent additional revenue, depending on product mix. For example, periods of
  > high EBIT margins, have in part been attributable to a favourable product mix, particularly a
  > higher share of advanced development programmes."

  And the cost structure, from the same page:

  > "The Company's cost base is structured such that direct costs, on an illustrative basis,
  > including raw materials and subcontractors, account for approximately 25 percent of total
  > costs, while semi-fixed costs, primarily consisting of personnel expenses for engineers and
  > operators, account for approximately 30 percent of total costs. Once again, on an illustrative
  > basis, the remaining approximately 45 percent of costs are fixed in nature and include expenses
  > related to buildings, support function personnel and maintenance of machinery, including
  > depreciation. For the years ended 31 December 2025, 2024 and 2023, Silex's fixed costs
  > accounted for 54 percent, 46 percent and 42 percent, respectively, of the Group's total
  > expenses."

  The risk factor on p. 25 repeats it: "In 2025, fixed costs accounted for 54 percent of the
  Group's total expenses."

  **The plant, and what expanding it costs:**

  > "Silex currently operates one production facility in Järfälla, Sweden, which includes two fabs
  > utilising 200 mm wafer production. Silex continues to invest in innovation and capacity
  > expansion at the Järfälla site, with plans to increase cleanroom capacity by 35 percent and
  > increasing the cleanroom from 4,000 to 5,500 square metres. … The estimated capital expenditure
  > for the cleanroom expansion is approximately SEK 150 million, expected to be incurred in 2026,
  > followed by approximately SEK 500 million expected to be phased over the period from 2027 to
  > 2029. Approximately 50 operators and 20 to 30 engineers will be needed to support operations
  > following the expansion of the production area."

  And on the shape of the capital, which is the sentence this project should keep:

  > "The most significant portion of the investment in relation to MEMS manufacturing facilities is
  > the original outlay to construct the facility, cleanroom, ventilation, and production lines,
  > which together comprise the fab. After the initial investment, more capacity can be obtained by
  > smaller investments to, for example, new cleanroom area or new equipment, without having to
  > build the whole infrastructure."

- **DERIVED (arithmetic written out):** script `tools/silex_returns.py`.
  - **Cleanroom capital cost per square metre for the expansion:** SEK 150m (2026) + SEK 500m
    (2027–2029) = SEK 650,000,000 for 1,500 m² of added cleanroom = **SEK 433,333 per m²**. At the
    ECB 2025 annual averages (EUR/SEK 11.0663, EUR/USD 1.12998, so SEK 9.7934 per USD) that is
    **USD 44,247 per m²**. This is directly comparable with the cleanroom cost-per-square-metre
    series in [`fab-local-news-intl.md`](fab-local-news-intl.md).
  - **Staff added per square metre:** 50 operators + 20–30 engineers = 70–80 people for 1,500 m²,
    i.e. **one person per 19–21 m² of new cleanroom.**
  - **The headroom, priced.** 2025 total expenses 1,075 MSEK, of which fixed 54% = 0.54 × 1,075 =
    **580 MSEK**, leaving 1,075 − 580 = **494 MSEK** variable. If net sales doubled to 2,770 (the
    "approximately 100 percent additional revenue" the company claims is available) with fixed
    costs unchanged and variable costs scaling one-for-one, total revenue = 2,770 + 58 = 2,828,
    total expenses = 580 + 2 × 494 = 1,570, so **EBIT = 2,828 − 1,570 = 1,258 MSEK, a 45.4% EBIT
    margin (1,258 ÷ 2,770) and a 56.0% return on today's assets (1,258 ÷ 2,246).** This is an
    illustration, not a forecast — the prospectus says the cleanroom expansion costs SEK 150m in
    2026 plus about SEK 500m over 2027–2029, so the asset base would not stay at 2,246, and
    doubling revenue at constant product mix is exactly what the company warns is not guaranteed.
    But it does establish the direction and the rough magnitude: **the second half of a fab's
    capacity is worth several times the first half of its profit.**
- **The confirmed negative.** The prospectus gives **no wafer-start figure, no wafer output figure
  and no average selling price per wafer.** Searched (case-insensitively, over the whole 14,475-line
  extraction): "wafer start", "wafers per month/year/week", "wpm", "wafer output", "throughput",
  "average selling price", "ASP", "price per wafer", "per wafer", "revenue per wafer", "unit
  price". The word "wafer" appears 89 times and never next to a volume or a price. The three hits
  for "price per" are all the share price and the C-share subscription price. **This negative is
  now verified rather than repeated, and it holds.** Capacity is disclosed only as a utilisation
  percentage and a cleanroom area.
- **Caveats, stated plainly.** The prospectus contradicts itself on the fixed-cost share: p. 86
  says "In 2025, fixed costs accounted for approximately 50 percent of the Group's total expenses"
  while p. 25 and p. 119 both say 54 percent. The 54 percent figure is given as a three-year series
  and is the one used above; the 50 percent figure is left unexplained. "Approximately 60 percent"
  is the company's own characterisation in an offering document, is not defined (utilisation of
  what — tool hours, wafer slots, cleanroom area?), and is unaudited. The claimed "approximately
  100 percent additional revenue" is explicitly qualified "depending on product mix", and the same
  page says a favourable mix is part of why the EBIT margin has been high — so the two claims pull
  against each other.

---

### SEM-3. **The distribution, not a basket: the median SEC filer in SIC 3674 earns a 1.48% operating margin, and Silex's 22.7% is at the 82nd percentile**

- **Source:** the U.S. Securities and Exchange Commission's XBRL "frames" and "submissions" APIs,
  which publish every filer's tagged financial data as free JSON with no key.
  - `https://data.sec.gov/api/xbrl/frames/us-gaap/<concept>/USD/CY2025.json` (duration concepts)
  - `https://data.sec.gov/api/xbrl/frames/us-gaap/<concept>/USD/CY2025Q4I.json` (instant concepts)
  - `https://data.sec.gov/submissions/CIK##########.json` (SIC code)
- **Verification:** Verified. Fetched 2026-09-25 with a declared generic `User-Agent`
  (`foundry-api-research/1.0`) and a 0.12-second inter-request delay, well inside SEC's 10 req/s
  limit. Nine frames and 4,988 submissions files were cached to disk; the analysis is offline and
  reproducible from the cache.
- **Date checked:** 2026-09-25
- **Bearing:** **Supports** H6 (Silex's profitability is unusually good, not typical) and
  **Challenges** the framing that a fab's low margin is a fact of physics.
- **How it was counted:** `uv run tools/sec_fetch.py --cache tmp/sec --years 2025,2024` then
  `uv run tools/semiconductor_margins.py --cache tmp/sec --year 2025`. Revenue is
  `Revenues` where tagged, otherwise `RevenueFromContractWithCustomerExcludingAssessedTax`.
  Quantiles are linear-interpolation quantiles on the sorted sample. **Medians and quartiles only —
  no means.** A mean of these tails is meaningless: the SIC 3674 operating margin runs from −268.80%
  to +60.46%.

**Frame coverage, CY2025:**

| Concept | Frame | Filers |
|---|---|---:|
| `Revenues` | CY2025 | 2,241 |
| `RevenueFromContractWithCustomerExcludingAssessedTax` | CY2025 | 2,701 |
| `OperatingIncomeLoss` | CY2025 | 4,643 |
| `GrossProfit` | CY2025 | 2,420 |
| `PaymentsToAcquirePropertyPlantAndEquipment` | CY2025 | 3,559 |
| `DepreciationDepletionAndAmortization` | CY2025 | 2,733 |
| `Assets` | CY2025**Q4I** | 6,153 |
| `PropertyPlantAndEquipmentNet` | CY2025**Q4I** | 4,206 |
| `StockholdersEquity` | CY2025**Q4I** | 5,758 |
| SIC codes resolved | — | 4,988 |

**SIC 3674, semiconductors and related devices.** 102 filers had a resolved SIC code and some
frame data. Dropped: **21** with no revenue tag in CY2025, **8** with no `OperatingIncomeLoss`
tag, **8** with revenue below $10,000,000 (SIC 3674 is full of pre-revenue shells whose ratios are
noise). **n = 73.**

| Measure | n | min | p10 | p25 | **median** | p75 | p90 | max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Operating margin | 73 | −268.80% | −48.05% | −20.50% | **1.48%** | 13.40% | 26.52% | 60.46% |
| Gross margin | 71 | −20.72% | 13.99% | 28.02% | **44.26%** | 54.96% | 67.77% | 97.54% |
| Asset turnover | 73 | 0.036× | 0.251× | 0.393× | **0.519×** | 0.652× | 0.879× | 3.022× |
| Operating income ÷ assets | 73 | −101.59% | −18.22% | −7.89% | **0.71%** | 6.35% | 16.90% | 63.05% |
| Operating income ÷ equity | 67 | −266.26% | −25.84% | −8.33% | **1.57%** | 12.07% | 25.36% | 82.89% |
| PP&E ÷ assets | 67 | 0.75% | 2.20% | 4.31% | **8.72%** | 21.15% | 38.67% | 52.70% |
| PP&E ÷ revenue | 67 | 0.024× | 0.041× | 0.077× | **0.199×** | 0.369× | 0.869× | 5.108× |
| Capex ÷ revenue | 69 | 0.62% | 1.37% | 2.63% | **4.40%** | 8.31% | 22.32% | 42.42% |
| D&A ÷ revenue | 37 | 0.86% | 1.72% | 2.62% | **6.54%** | 9.57% | 12.90% | 22.34% |

**Where Silex falls (percentile = share strictly below, plus half the ties):**

| Silex measure | Value | Percentile of SIC 3674 |
|---|---:|---:|
| Operating margin, operating-company view (`LNI-17`) | 22.67% | **82.2** |
| Operating margin, group view (prospectus) | 26.57% | **89.0** |
| Asset turnover | 0.617× | **69.9** |
| Operating income ÷ assets | 16.38% | **89.0** |
| PP&E ÷ assets | 41.94% | **91.0** |
| Capex ÷ revenue | 14.08% | **82.6** |

**Restricting to filers that actually own plant** (PP&E ≥ 30% of revenue — most of SIC 3674 is
fabless), **n = 21**: median asset turnover **0.476×**, median operating margin **1.40%**, median
operating income ÷ assets **0.67%**. Silex's operating margin is at the **85.7th** percentile of
this subset on the 22.67% figure and the **90.5th** on 26.57%.

**The four neighbouring SIC codes, for calibration:**

| SIC | What it is | n | median operating margin | median asset turnover | median EBIT ÷ assets | median PP&E ÷ revenue |
|---|---|---:|---:|---:|---:|---:|
| 3674 | Semiconductors and related devices | 73 | **1.48%** | 0.519× | 0.71% | 0.199× |
| 3672 | Printed circuit boards | 12 | **4.45%** | 1.227× | 5.17% | 0.166× |
| 3559 | Special industry machinery (semiconductor equipment) | 11 | **8.73%** | 0.682× | 3.81% | 0.124× |
| 3827 | Lab analytical / optical instruments and lenses | 4 | **21.55%** | 0.774× | 10.46% | 0.124× |
| 3826 | Laboratory analytical instruments | 17 | **−9.49%** | 0.449× | −5.86% | 0.203× |
| — | **All SEC filers, any SIC, revenue ≥ $10m** | **2,845** | **4.35%** | **0.654×** | **3.25%** | — |

- **DERIVED (arithmetic written out):**
  - **Semiconductors are a below-average business, on every one of the three measures.** SIC 3674's
    median operating margin of 1.48% is **2.87 percentage points below** the all-filer median of
    4.35%; its median asset turnover of 0.519× is **0.135× below** the all-filer 0.654×; and its
    median return on assets of 0.71% is **2.54 percentage points below** the all-filer 3.25%. The
    compounding is the point: 0.0148 × 0.519 = 0.77% against 0.0435 × 0.654 = 2.84%, so **the
    median semiconductor company earns roughly a quarter of the median public company's return on
    its assets** (0.71 ÷ 3.25 = 0.218×).
  - **The PCB cross-check, against `PCB-1`…`PCB-14`.** PCB makers (SIC 3672) earn barely a *quarter* of the
    semiconductor gross margin — 10.12% median against 44.26%, i.e. 22.9% of it — and yet earn a **higher return on
    assets**: 5.17% against 0.71%, because they turn their assets 1.227× against 0.519×.
    5.17 ÷ 0.71 = **7.3× the return on assets on a quarter of the gross margin.** Any argument in
    this repo that reasons from PCB margins to fab margins has to carry that 2.4× difference in
    asset turnover with it.
- **Caveats, at full strength.**
  - **This is SEC filers only.** TSMC, UMC and Tower file 20-Fs and are tagged in the `ifrs-full`
    taxonomy, so they are *not* in these `us-gaap` frames. Neither are Silex, X-FAB, Vanguard or
    Powerchip. `SEM-4` handles them one by one.
  - **SIC codes are the filer's own self-classification** and are coarse. NVIDIA, Broadcom, Intel,
    Micron, Applied Materials, Texas Instruments, NXP, STMicroelectronics, AMD and Analog Devices
    are all SIC 3674, which mixes fabless designers, IDMs and equipment makers into one code. That
    is why the plant-owning subset is reported separately.
  - **Frames are calendar-aligned.** A filer with a fiscal year ending well away from 31 December
    may be assigned to a frame or may be missing from it. Analog Devices' FY ended 2025-11-01 and
    does appear in CY2025; NVIDIA's FY ending 2026-01-25 appears with $215.94bn of revenue, i.e.
    its FY2026, not the FY2025 used in `SEM-4`. Any single-company figure should be read from
    `SEM-4`, which uses the filing's own period, not from this table.
  - **Year-end assets, not average assets**, because the frames give a point-in-time balance sheet.
    For Silex the difference is 0.06 percentage points (`SEM-1`).
  - **n = 73 is small**, and the quartiles of a 73-point sample are not precise. The direction of
    the result — a median near zero and Silex in the top fifth — is robust to any reasonable change
    in the filters; the exact percentile is not.

---

### SEM-4. **The named peer group: among eleven listed pure-play and specialty foundries, only TSMC beats Silex — on margin and on return on assets**

- **Sources:** each company's own filing. SEC filers were read from the SEC's XBRL `companyfacts`
  API (`https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`) and, where the FY2025
  facts had not yet propagated, from the R-files of the filing itself.
  - **TSMC**, Form 20-F for FY2025, filed 2026-04-16, accession **0001628280-26-025362**:
    <https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm>
    (FY2024: accession 0001193125-25-083423)
  - **UMC**, Form 20-F for FY2025, filed 2026-04-30, accession **0001193125-26-193757**:
    <https://www.sec.gov/Archives/edgar/data/1033767/000119312526193757/d91630d20f.htm>
    (FY2024: accession 0001193125-25-092142)
  - **GlobalFoundries Inc.**, Form 20-F for FY2025, accession **0001709048-26-000022**
    (FY2024: 0001709048-25-000024)
  - **Tower Semiconductor Ltd**, Form 20-F for FY2025, accession **0001178913-26-002318**
    (FY2024: 0001178913-25-001537)
  - **SkyWater Technology, Inc.**, Form 10-K for FY2025, accession **0001819974-26-000009**:
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997426000009/skyt-20251228.htm>
  - **Amkor Technology, Inc.**, Form 10-K for FY2025, accession **0001047127-26-000014**
  - **onsemi**, Form 10-K for FY2025, accession **0001097864-26-000006**
  - **Texas Instruments**, Form 10-K for FY2025, accession **0000097476-26-000059**
  - **Analog Devices**, Form 10-K for the year ended 2025-11-01, accession **0000006281-25-000153**
  - **Intel**, Form 10-K for FY2025, accession **0000050863-26-000011**
  - **NVIDIA**, Form 10-K for the year ended 2025-01-26, accession **0001045810-25-000023**
  - **AMD**, Form 10-K for the year ended 2025-12-27, accession **0000002488-26-000018**
  - **X-FAB Silicon Foundries SE** (Euronext Paris), *Annual Report 2025*, consolidated IFRS
    statements: <https://www.xfab.com/fileadmin/X-FAB/Investor_Relations/Reports/X-FAB_Annual_Report_2025_ENG.pdf>
  - **Vanguard International Semiconductor Corporation** (TWSE 5347), consolidated balance sheets,
    statements of comprehensive income and statements of cash flows as of and for the year ended
    2025-12-31, published on the company's investor site:
    <https://media-vis.todayir.com/20260203135256914051011_en.pdf>
  - **Powerchip Semiconductor Manufacturing Corporation** (TWSE 6770), consolidated financial
    statements: nine months ended 2025-09-30
    (<https://www.powerchip.com/upload/media/financials/quarterly_result/2025Q3_CFS_EN.pdf>) and
    the three months ended 2026-03-31, whose balance sheet carries the 2025-12-31 comparative
    (<https://www.powerchip.com/upload/media/financials/quarterly_result/2026Q1_CFS_EN.pdf>)
  - **Silex Microsystems AB (publ)**, prospectus diary number 25-37533 — see `SEM-1`
- **Verification:** Verified for every SEC filer, X-FAB, Vanguard and Silex. **Partial for
  Powerchip**, whose full-year 2025 consolidated statements could not be obtained (see "What could
  not be got"); its income statement below is nine months and its balance sheet is the year-end
  comparative from the following quarter's filing, and the row is labelled as such.
- **Date checked:** 2026-09-25
- **Bearing:** **Supports** H6. **Challenges** H7 — see `SEM-5`.
- **How it was counted:** `uv run tools/foundry_peers.py --cache tmp/sec --years 2024,2025` and
  `uv run tools/peer_table.py`. Ratios are currency-invariant, so nothing is converted to compute
  them; the USD column in the script exists only to show relative size, and it states its rate.

**Everything in each company's own reporting currency, as printed:**

| Company | FY | ccy | revenue | operating income | **operating margin** | total assets | **asset turnover** | **EBIT ÷ assets** | PP&E ÷ revenue | capex ÷ revenue | D&A ÷ revenue |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| TSMC | 2025 | TWD m | 3,809,054.3 | 1,936,091.7 | **50.83%** | 7,932,842.5 | 0.480× | **24.41%** | 0.969× | 33.40% | 18.06% |
| TSMC | 2024 | TWD m | 2,894,307.7 | 1,322,053.0 | 45.68% | 6,691,764.7 | 0.433× | 19.76% | 1.118× | 33.03% | 22.90% |
| **Silex (group)** | **2025** | **SEK m** | **1,385** | **368** | **26.57%** | **2,246** | **0.617×** | **16.38%** | 0.947× | 14.08% | 9.03% |
| **Silex (operating co., `LNI-17`)** | **2025** | **SEK m** | **1,385** | **314** | **22.67%** | **2,246** | **0.617×** | **13.98%** | — | — | — |
| Silex (group) | 2024 | SEK m | 1,226 | 339 | 27.65% | 2,265 | 0.541× | 14.97% | 1.011× | 6.36% | 9.54% |
| UMC | 2025 | TWD k | 237,553,199 | 43,948,688 | **18.50%** | 567,274,863 | 0.419× | **7.75%** | 1.142× | 20.10% | 24.95% |
| UMC | 2024 | TWD k | 232,302,584 | 51,612,570 | 22.22% | 560,168,955 | 0.415× | 9.21% | 1.201× | 38.12% | 20.73% |
| Vanguard (VIS) | 2025 | TWD m | 48,591 | 7,773 | **16.00%** | 200,469 | 0.242× | **3.88%** | 2.343× | 131.67% | 17.60% |
| Tower Semiconductor | 2025 | USD k | 1,566,104 | 194,172 | **12.40%** | 3,322,290 | 0.471× | **5.84%** | 0.934× | 28.38% | 19.35% |
| Tower Semiconductor | 2024 | USD k | 1,436,122 | 191,314 | 13.32% | 3,080,485 | 0.466× | 6.21% | 0.896× | 30.37% | 18.54% |
| GlobalFoundries | 2025 | USD m | 6,791 | 797 | **11.74%** | 17,141 | 0.396× | **4.65%** | 1.064× | 10.63% | 16.71% |
| GlobalFoundries | 2024 | USD m | 6,750 | (214) | −3.17% | 16,799 | 0.402× | −1.27% | 1.150× | 9.26% | 20.30% |
| X-FAB | 2025 | USD k | 870,255 | 76,425 | **8.78%** | 1,946,985 | 0.447× | **3.93%** | 1.402× | 23.46% | 13.84% |
| X-FAB | 2024 | USD k | 816,383 | 85,543 | 10.48% | 1,906,713 | 0.428× | 4.49% | 1.402× | 62.41% | 12.66% |
| SkyWater | 2025 | USD k | 442,139 | (2,576) | **−0.58%** | 733,907 | 0.602× | **−0.35%** | 1.157× | 5.50% | 8.07% |
| Intel | 2025 | USD m | 52,853 | (2,214) | −4.19% | 211,429 | 0.250× | −1.05% | 1.994× | 27.71% | — |
| Powerchip (9M 2025) | 2025 | TWD k | 34,234,871 | (5,240,729) | **−15.31%** | 178,685,624 | — | — | 3.564× | — | — |
| *Amkor (OSAT contrast)* | 2025 | USD k | 6,707,981 | 467,385 | 6.97% | 8,136,309 | 0.824× | 5.74% | 0.577× | 13.49% | 9.57% |
| *onsemi (IDM contrast)* | 2025 | USD m | 5,995.4 | 84.2 | 1.40% | 12,524.1 | 0.479× | 0.67% | 0.562× | 5.69% | 11.44% |
| *Texas Instruments (IDM)* | 2025 | USD m | 17,682 | 6,023 | 34.06% | 34,585 | 0.511× | 17.42% | 0.697× | 25.73% | — |
| *Analog Devices (IDM)* | 2025 | USD k | 11,019,707 | 2,932,496 | 26.61% | 47,992,712 | 0.230× | 6.11% | 0.301× | 4.84% | — |
| *NVIDIA (fabless)* | FY ended 2025-01-26 | USD m | 130,497 | 81,453 | 62.42% | 111,601 | 1.169× | 72.99% | 0.048× | — | 1.43% |
| *AMD (fabless)* | 2025 | USD m | 34,639 | 3,694 | 10.66% | 76,926 | 0.450× | 4.80% | 0.067× | 2.81% | — |

- **DERIVED (arithmetic written out):** every row above is `tools/peer_table.py` output; the
  divisions for the FY2025 foundries are printed in full by that script. Worked examples:
  - TSMC FY2025: 1,936,091.7 ÷ 3,809,054.3 = **50.83%**; 3,809,054.3 ÷ 7,932,842.5 = **0.4802×**;
    1,936,091.7 ÷ 7,932,842.5 = **24.41%**; check 0.508287 × 0.480163 = 24.41%.
  - UMC FY2025: 43,948,688 ÷ 237,553,199 = **18.50%**; 237,553,199 ÷ 567,274,863 = **0.4188×**;
    43,948,688 ÷ 567,274,863 = **7.75%**.
  - X-FAB FY2025: 76,425 ÷ 870,255 = **8.78%**; 870,255 ÷ 1,946,985 = **0.4470×**;
    76,425 ÷ 1,946,985 = **3.93%**.
  - Vanguard FY2025: 7,773 ÷ 48,591 = **16.00%**; 48,591 ÷ 200,469 = **0.2424×**;
    7,773 ÷ 200,469 = **3.88%**.
  - **Powerchip, annualising the nine months by 4/3** so the ratio is at least dimensionally right:
    operating loss (5,240,729) × 4 ÷ 3 = **(6,987,639)**, revenue 34,234,871 × 4 ÷ 3 =
    **45,646,495**, so turnover = 45,646,495 ÷ 178,685,624 = **0.255×** and EBIT ÷ assets =
    (6,987,639) ÷ 178,685,624 = **−3.91%**.
  - **The ranking.** FY2025 pure-play and specialty foundries by operating margin: TSMC 50.83%,
    **Silex 26.57% (22.67% on the operating-company view)**, UMC 18.50%, Vanguard 16.00%, Tower
    12.40%, GlobalFoundries 11.74%, X-FAB 8.78%, SkyWater −0.58%, Intel −4.19%, Powerchip −15.31%.
    **Median of those ten (excluding the duplicate Silex view): (12.40 + 11.74) ÷ 2 = 12.07%.**
    Silex is **14.50 percentage points above the peer median** on the group figure and **10.60**
    above it on the operating-company figure.
  - **The same group by return on assets:** TSMC 24.41%, **Silex 16.38% (13.98%)**, UMC 7.75%,
    Tower 5.84%, GlobalFoundries 4.65%, X-FAB 3.93%, Vanguard 3.88%, SkyWater −0.35%, Intel −1.05%,
    Powerchip −3.91% (annualised). Sorted: −3.91, −1.05, −0.35, 3.88, 3.93, 4.65, 5.84, 7.75,
    16.38, 24.41, so the **median of the ten is (3.93 + 4.65) ÷ 2 = 4.29%.** Silex is
    16.38 ÷ 4.29 = **3.82× the peer median** on the group figure and 13.98 ÷ 4.29 = **3.26×** on
    the operating-company figure. **Median asset turnover of the ten: 0.433×.**
  - **Silex has the highest asset turnover in the group** (0.617×; SkyWater is second at 0.602×).
    Its turnover beats TSMC's 0.480×, UMC's 0.419× and
    Vanguard's 0.242×. That is the mechanical reason its return on assets is high: a small, old,
    fully-built 200 mm fab carries far less balance sheet per krona of revenue than a fab that is
    still being built.
  - **The asset-turnover spread inside the peer group is 3.2×** — from Powerchip's 0.192× (as
    printed, nine months) to Silex's 0.617× — which is almost as wide as the margin spread. Any
    comparison done on margin alone is throwing away half the variance.
- **Caveats.**
  - **Powerchip's row mixes periods** and is marked. Its full-year 2025 statements were not
    obtainable; see "What could not be got".
  - **Vanguard's 131.67% capex ratio and 0.242× turnover are an artefact of building a fab**: it
    consolidated the VSMC Singapore joint venture in 2025, and PP&E rose 158% year on year, from
    NT$44,141m to NT$113,869m. Its *operating* business is not unusually unproductive; its balance
    sheet is full of a fab that is not yet producing. The same caution applies to GlobalFoundries
    in 2024 and to Powerchip throughout.
  - **SkyWater reconciles with `LN-7`.** Total assets 733,907 = the 518,540 (Legacy) + 215,367
    (Texas) segment assets in `LN-7`; revenue 442,139 and operating loss (2,576) are the same
    consolidated figures. `LN-7`'s finding stands: the high-mix segment lost 12.93% while the
    anchor-customer segment made 18.21%, and the consolidated −0.58% here is the two netted.
  - **Currencies are not converted** for any ratio, because ratios are dimensionless. Where the
    script does show a USD figure it uses the issuers' own 20-F convenience rate of **TWD 31.370
    per USD at 2025-12-31**, and, for Silex, **SEK 9.7934 per USD** derived from the ECB 2025
    annual average reference rates EUR/SEK 11.0663058823529 and EUR/USD 1.1299831372549
    (<https://data-api.ecb.europa.eu/service/data/EXR/A.SEK.EUR.SP00.A>, retrieved 2026-09-25).
    On that rate Silex's SEK 1,385m of net sales is **USD 141 million** — the smallest company in
    the table by a factor of six.
  - **"Operating income" is not identical across accounting frameworks.** The IFRS filers'
    `ProfitLossFromOperatingActivities` and the US filers' `OperatingIncomeLoss` sit at slightly
    different points relative to other income and to share of associates. The differences are small
    relative to the spread being measured, but they are not zero.

---

### SEM-5. **X-FAB has five times Silex's customer count and a third of its margin** — the cleanest available test of H7, and it fails

- **Source:** X-FAB Silicon Foundries SE (Euronext Paris: XFAB), *Annual Report 2025*, for the year
  ended 2025-12-31, prepared "in compliance with articles 3:6 and 3:32 of the Belgian Code on
  Companies and Associations".
  <https://www.xfab.com/fileadmin/X-FAB/Investor_Relations/Reports/X-FAB_Annual_Report_2025_ENG.pdf>
- **Verification:** Verified. Downloaded 2026-09-25 (8,769,636 bytes) and read with
  `pdftotext -layout`; every quote below is copied from that extraction.
- **Date checked:** 2026-09-25
- **Bearing:** **Challenges H7**, and **challenges H6** in its "many small customers means a good
  business" form. Also **Context** for H8.
- **What it says.** The company at a glance:

  > "Serving >400 customers worldwide" … "Approximately 4,300 employees representing 45
  > nationalities" … "6 manufacturing facilities in US, Europe and Asia" … "Listed on Euronext
  > Paris since April 6 2017"

  The concentration risk factor, in full:

  > "A significant portion of X-FAB's revenue comes from a relatively limited number of customers.
  > X-FAB's largest customer, Melexis, accounted for 43% of the Group's revenue in 2025, while the
  > Group's top three customers accounted for 53% of revenue and its top five customers accounted
  > for 58% of revenue during the year. None of X-FAB's customers are prohibited by contract from
  > purchasing from other semiconductor suppliers. In the past, customers have switched to other
  > semiconductor suppliers with little or no notice…"

  And its own account of why small orders are its business:

  > "Due to the high degree of product customization, X-FAB as a specialty foundry is less
  > vulnerable to the extreme price and demand volatility experienced by many competitors in the
  > broader foundry market. X-FAB's focus on highly customized products often results in smaller
  > production volumes and requires more engineering input per unit, creating a high value-add for
  > the customer."

  > "The long-term availability of these high-quality products is essential for X-FAB's customers,
  > since X-FAB is the sole source for most of the products it manufactures. A large portion of
  > these products have long product lifecycles of ten or more years. For example, X-FAB's first
  > medical MEMS product, a sensor used to monitor blood pressure, has been in production for more
  > than 25 years."

  The consolidated figures, as printed (thousands of U.S. dollars):

  | | 2025 | 2024 |
  |---|---:|---:|
  | Revenue | 870,255 | 816,383 |
  | **Operating profit** | **76,425** | **85,543** |
  | Profit for the period | 30,128 | 61,526 |
  | Property, plant, and equipment | 1,220,272 | 1,144,620 |
  | **Total assets** | **1,946,985** | **1,906,713** |
  | Total equity | 1,053,305 | 1,022,794 |
  | Depreciation and amortization, before effect of grants and subsidies | 120,402 | 103,386 |
  | Payments for property, plant, equipment, and intangible assets | (204,129) | (509,467) |

  The auditor's key-audit-matter note gives the capital intensity in one line:

  > "The net carrying value of property, plant and equipment as at December 31, 2025 amounts to USD
  > 1.220,3 million, representing 62,7% of the Group's total assets."

- **DERIVED (arithmetic written out):**
  - **Operating margin:** 76,425 ÷ 870,255 = **8.78%** (2024: 85,543 ÷ 816,383 = **10.48%**).
  - **Asset turnover:** 870,255 ÷ 1,946,985 = **0.4470×**. **Return on assets:**
    76,425 ÷ 1,946,985 = **3.93%**; check 0.087819 × 0.447000 = 3.93%.
  - **Revenue per employee:** 870,255,000 ÷ 4,300 = **USD 202,385**. Silex:
    SEK 1,385,000,000 ÷ 484 employees (`LNI-18`) = SEK 2,861,570 = **USD 292,197** at SEK 9.7933
    per USD. **Silex earns 44.4% more revenue per head** (292,197 ÷ 202,385 = 1.444×).
  - **The H7 comparison, side by side.** Both are pure-play specialty foundries selling customised
    process work to a long tail of design houses.

    | | X-FAB | Silex |
    |---|---:|---:|
    | Customers | **>400** | ~85 (`LNI-18`) |
    | Largest customer, share of revenue | **43%** (Melexis) | 25% |
    | Top three / top five | 53% / 58% | (top ten: 77%) |
    | Fabs | 6, in 3 continents | 1, in Järfälla |
    | Employees | ~4,300 | 484 |
    | Revenue | USD 870m | USD 141m |
    | **Operating margin** | **8.78%** | **26.57% / 22.67%** |
    | **Return on assets** | **3.93%** | **16.38% / 13.98%** |
    | PP&E ÷ total assets | 62.7% | 41.9% |

    **The foundry with nearly five times the customer count has a third of the margin and a quarter
    of the return on assets, and is simultaneously *more* concentrated on its largest customer
    (43% against 25%).** H7 says that many small customers reduce risk and remove buyer power, and
    therefore should show up as a better business. In the only pair of directly comparable
    specialty foundries that both publish the numbers, it shows up as a worse one. The mechanism
    that does separate them is visible in the same table: six fabs on three continents against one,
    and 62.7% of the balance sheet in plant against 41.9%.
  - **X-FAB's 2024 capex of USD 509,467 thousand was 62.41% of that year's revenue**, against
    23.46% in 2025. Two years of building at that rate is what put the extra plant on the balance
    sheet, and the margin went *down* over the same period (10.48% → 8.78%).
- **Caveats.** X-FAB's mix is not Silex's: X-FAB is mostly analog/mixed-signal CMOS with a
  microsystems line (USD 100.7 million of 2025 revenue) and a small wide-bandgap line (4% of
  revenue), whereas Silex is entirely MEMS. Melexis is a related party of sorts — both X-FAB and
  Melexis sit in the Xtrion orbit — which complicates reading the 43% as arm's-length
  concentration. And X-FAB carries the Altis fab at Corbeil-Essonnes and the Lubbock fab, both
  acquired rather than built, which loads the balance sheet in a way Silex's single owned site does
  not.

---

### SEM-6. **The free consistency check: Silex's Chinese parent, consolidating the same fab, printed an operating *loss* of CNY 254 million in 2024** — and the reconciliation works to 1.2%

- **Sources:** 北京赛微电子股份有限公司 (Beijing SWAYSURE / Saiwei Electronics Co., Ltd., SZSE:
  300456), annual reports from `static.cninfo.com.cn`:
  - 2024 年年度报告, published 2025-03-20: <http://static.cninfo.com.cn/finalpage/2025-03-20/1222847674.PDF>
  - 2025 年年度报告, published 2026-03-27: <http://static.cninfo.com.cn/finalpage/2026-03-27/1225036416.PDF>
- **Verification:** Verified 2026-09-25. Both PDFs downloaded and read with `pdftotext -layout`.
  Chinese-language filings; the English renderings are ours and the Chinese is given alongside.
- **Date checked:** 2026-09-25
- **Bearing:** **Challenges** the reading of `LNI-17` as evidence that a MEMS foundry group is a
  good business, while **Supporting** the narrower claim that *this particular fab* is. It is also
  the reason `OIM-5`'s segment split stops after 2024.
- **What it says.**
  - **The group deconsolidated Silex in July 2025**, which is why the 2025 accounts cannot be used
    for this check. From the 2025 report:

    > "报告期内，公司 2025 年 7 月完成对原全资子公司瑞典 Silex 控制权的出售，本次股权交易完成后，
    > 瑞典 Silex 由公司全资子公司转变为公司参股子公司，不再纳入公司合并报表范围"
    > — "During the reporting period, in July 2025 the Company completed the sale of control of its
    > formerly wholly-owned subsidiary Sweden Silex. On completion of this equity transaction,
    > Sweden Silex changed from a wholly-owned subsidiary of the Company into an equity-accounted
    > investee, and **is no longer included in the scope of the Company's consolidated statements**."

    > "2023-2025 年，瑞典 Silex 业务收入占公司 MEMS 业务收入的比例分别为 85.56%、82.69%、77.72%"
    > — "In 2023–2025, Sweden Silex's business revenue accounted for **85.56%, 82.69% and 77.72%**
    > respectively of the Company's MEMS business revenue."

    > "2025 年 7 月，瑞典 Silex 的控制权转让事项已完成交割，但瑞典 Silex 仍为公司持股 45.24%的重要
    > 参股子公司"
    > — "In July 2025 the transfer of control of Sweden Silex was completed, but Sweden Silex
    > remains an important associate in which the Company holds **45.24%**."

  - **The 2024 consolidated income statement, as printed (CNY):**

    | 项目 (item) | 2024 年度 | 2023 年度 |
    |---|---:|---:|
    | 一、营业总收入 (total operating revenue) | 1,204,715,636.91 | 1,299,682,668.54 |
    | 二、营业总成本 (total operating costs) | 1,432,317,582.43 | 1,411,700,577.11 |
    | ── 营业成本 (cost of sales) | 781,790,496.19 | 919,974,132.37 |
    | ── 销售费用 (selling expenses) | 29,304,870.92 | 18,792,517.86 |
    | ── 管理费用 (administrative expenses) | 148,281,360.25 | 120,852,329.24 |
    | ── 研发费用 (**R&D expenses**) | **454,830,833.84** | 356,656,207.29 |
    | ── 财务费用 (finance expenses) | 12,008,719.43 | (10,208,853.80) |
    | 三、营业利润 (**operating profit/loss**) | **(254,276,329.43)** | 31,709,241.73 |
    | 五、净利润 (net profit/loss) | (255,255,953.51) | 72,048,921.38 |

  - **The 2024 consolidated balance sheet, as printed (CNY):**

    | | 2024-12-31 | 2023-12-31 |
    |---|---:|---:|
    | 固定资产 (fixed assets) | 1,799,636,378.42 | 1,708,633,598.89 |
    | 在建工程 (construction in progress) | 891,261,115.57 | 754,177,596.31 |
    | **资产总计 (total assets)** | **7,011,337,774.25** | 7,261,878,738.03 |
    | 归属于母公司所有者权益合计 (equity attributable to parent) | 4,923,596,975.33 | 5,162,100,953.14 |
    | 所有者权益合计 (total equity) | 5,389,163,787.63 | 5,628,929,609.25 |

- **DERIVED (arithmetic written out):**
  - **The reconciliation, and it works.** The ECB annual average reference rates for 2024 are
    EUR/SEK **11.432519140625** and EUR/CNY **7.787469921875**
    (<https://data-api.ecb.europa.eu/service/data/EXR/A.SEK.EUR.SP00.A> and `.../A.CNY.EUR.SP00.A`,
    retrieved 2026-09-25), so SEK→CNY = 7.787469921875 ÷ 11.432519140625 = **0.681156**.
    Silex's 2024 net sales of SEK 1,226,000,000 (`SEM-1`) = **CNY 835,097,256**. The parent says
    Silex was **82.69%** of group MEMS revenue, and `OIM-5` records group MEMS revenue for 2024 as
    99,804.58 万元 = **CNY 998,045,800**; 998,045,800 × 0.8269 = **CNY 825,284,072**. The two
    routes differ by 835,097,256 − 825,284,072 = CNY 9,813,184, i.e. **1.19%** — within the error
    of an annual-average exchange rate applied to a year of transactions. **The Swedish accounts
    and the Chinese accounts are describing the same business, and they agree.**
  - **The whole group, on the same measures as `SEM-4`:**
    operating margin = (254,276,329.43) ÷ 1,204,715,636.91 = **−21.11%**;
    asset turnover = 1,204,715,636.91 ÷ 7,011,337,774.25 = **0.1718×**;
    return on assets = (254,276,329.43) ÷ 7,011,337,774.25 = **−3.63%**;
    gross margin = (1,204,715,636.91 − 781,790,496.19) ÷ 1,204,715,636.91 = **35.11%**;
    PP&E + CIP ÷ revenue = (1,799,636,378.42 + 891,261,115.57) ÷ 1,204,715,636.91 = **2.234×**.
  - **What turns a profitable fab into a loss-making group:** R&D of CNY 454,830,833.84 is
    **37.75%** of revenue (454,830,833.84 ÷ 1,204,715,636.91), and construction in progress of
    CNY 891,261,115.57 is **12.71%** of total assets — a second fab, Beijing FAB3, being built and
    ramped. The gross margin is a respectable 35.11%; everything below it is the cost of building
    the next fab. **Silex earned SEK 339m of operating profit in the same year that the group that
    owned it lost CNY 254m.** Converting Silex's EBIT at the same 0.681156 rate gives
    CNY 230,911,884, so the rest of the group lost
    (254,276,329.43) − 230,911,884 = **CNY 485,188,213** at the operating line.
  - **This is the single most useful thing in the entry for this project.** A fab that is running
    makes money; the group that is building the *next* fab does not. Silex's 22.7% is the number of
    a paid-for fab at 60% utilisation. It is not the number of an entrant.
- **Caveats.** Chinese GAAP 营业利润 ("operating profit") sits below investment income, credit and
  asset impairments and gains on asset disposals, so it is not an exact analogue of IFRS operating
  profit. Excluding finance expenses to get closer to EBIT gives
  1,204,715,636.91 − 1,432,317,582.43 + 12,008,719.43 = **CNY (215,593,226.09)**, a −17.90% margin
  — the sign and the order of magnitude do not change. The group also contains a semiconductor
  equipment business, an IC design service business (展诚科技, acquired September 2025) and the
  Beijing and Shenzhen Silex entities, so it is not a pure MEMS-foundry group. The 45.24% residual
  stake means the 2026 accounts will show Silex only as equity-accounted income.

---

### SEM-7. **Capital intensity does not explain semiconductor margins.** Rank correlation between PP&E-to-revenue and operating margin across SIC 3674: **+0.05**

- **Source:** as `SEM-3` — SEC XBRL frames CY2025 and CY2025Q4I plus SIC codes from
  `data.sec.gov/submissions`, 67 SIC 3674 filers with revenue ≥ $10m that tagged both
  `PropertyPlantAndEquipmentNet` and `OperatingIncomeLoss`.
- **Verification:** Verified 2026-09-25, computed from the cached frames.
- **Date checked:** 2026-09-25
- **Bearing:** **Challenges** a standard claim that appears throughout this repo's sources and in
  `PRINCIPLES.md`'s reasoning — that fabs earn thin margins because they carry heavy plant.
- **How it was counted:** `uv run tools/semiconductor_margins.py --cache tmp/sec --year 2025`.
  Spearman rank correlation computed with average ranks for ties; no library.

| PP&E ÷ revenue quartile | range | n | median operating margin | median PP&E ÷ revenue |
|---|---|---:|---:|---:|
| Q1 (least capital-intensive) | 0.024× – 0.069× | 16 | **−4.98%** | 0.043× |
| Q2 | 0.074× – 0.174× | 17 | **+6.92%** | 0.110× |
| Q3 | 0.199× – 0.338× | 17 | **+7.27%** | 0.243× |
| Q4 (most capital-intensive) | 0.400× – 5.108× | 17 | **+1.31%** | 0.697× |

**Spearman ρ(PP&E ÷ revenue, operating margin) = +0.050, n = 67.**

- **DERIVED (arithmetic written out):**
  - **The relationship is not monotonic and is not negative.** The *least* capital-intensive
    quartile has the *worst* median margin (−4.98%), and the two middle quartiles are the best.
    If capital intensity drove margin down, Q1 would be the best and Q4 the worst; the observed
    order is Q3 > Q2 > Q4 > Q1.
  - **The correlation is indistinguishable from zero.** ρ = +0.050 on n = 67; the two-sided 5%
    critical value for Spearman's ρ at n = 67 is about ±0.24, so this is nowhere near significant
    in either direction.
  - **Where the capital intensity *does* show up is asset turnover, and therefore return on
    assets.** SIC 3674's median PP&E ÷ revenue is 0.199× and its median asset turnover is 0.519×;
    the plant-owning subset (PP&E ≥ 30% of revenue, n = 21) has median asset turnover **0.476×**
    against 0.519× for the whole code, and median return on assets **0.67%** against 0.71%. The
    penalty is real but it is a *turnover* penalty, not a *margin* penalty:
    0.519 ÷ 0.476 = **1.09×**, so a plant-owning semiconductor firm needs roughly 9% more margin
    than the code median to earn the same return on its assets.
  - **The fabless contrast makes the same point from the other side.** NVIDIA's PP&E is 4.8% of
    revenue and it earns 62.42%; AMD's is 6.7% and it earns 10.66%. Analog Devices' is 30.1% and it
    earns 26.61%; Texas Instruments' is 69.7% and it earns 34.06%. **Texas Instruments carries
    fourteen times NVIDIA's plant relative to revenue and more than twice Analog Devices',
    and out-earns Analog Devices on margin.** Owning a fab is not what decides the margin.
  - **So what does?** The evidence in this file points at two things, and neither is capital.
    First, **utilisation** — Silex says outright that "the profitability of Silex's operations, like
    that of other pure play foundries more generally, is closely tied to its utilisation level"
    (`SEM-2`), and at 60% it is already at the 82nd percentile. Second, **whether the company is
    building.** Every low-margin foundry in `SEM-4` is mid-build or just post-build:
    GlobalFoundries at −3.17% in 2024 and 11.74% in 2025; Vanguard with capex at 131.67% of
    revenue; Powerchip at −15.31%; Saiwei's group at −21.11% with 12.71% of assets in construction
    in progress (`SEM-6`). Silex's capex was 6.36% of revenue in 2024 and 14.08% in 2025.
- **Caveats.** Cross-sectional, one year, 67 companies, no controls. A fab under construction
  carries PP&E and produces no revenue, which pushes a company into Q4 and simultaneously wrecks
  its margin — that should *create* a negative correlation, and none is observed, which strengthens
  the finding rather than weakening it. But it also means Q4 is contaminated by companies that are
  temporarily, not structurally, in it. `PropertyPlantAndEquipmentNet` is net of accumulated
  depreciation, so an old paid-for fab looks capital-light and a new one looks capital-heavy; on
  gross PP&E the ordering might differ, and gross PP&E is not consistently tagged.

---

### SEM-8. Verdict: the four questions, answered

- **Verification:** This is a summary of `SEM-1` … `SEM-7`, not an independent source. Every figure
  in it is derived in the entry cited beside it.
- **Date checked:** 2026-09-25
- **Bearing:** H5, H6, H7.

**1. Where does Silex's 22.7% fall?**

- **Against SIC 3674** (73 SEC filers, revenue ≥ $10m, CY2025): **82.2nd percentile** on the
  operating-company figure of 22.67%, **89.0th** on the group figure of 26.57%. The median of that
  population is **1.48%** (`SEM-3`).
- **Against the plant-owning subset of SIC 3674** (n = 21): **85.7th** and **90.5th** percentile;
  median **1.40%** (`SEM-3`).
- **Against the named pure-play and specialty foundry peer group** (ten companies, FY2025): **second
  of ten, behind TSMC alone.** Peer median 12.07%; Silex is 10.6 to 14.5 percentage points above it
  (`SEM-4`).
- **On return on assets**, which is the measure that matters: 16.38% (13.98% on the operating-company
  figure) against a SIC 3674 median of **0.71%** — the **89th percentile** — and a foundry peer
  median of **4.29%**, so **3.82× the peer median** (`SEM-3`, `SEM-4`).

**2. On return on assets rather than operating margin, how does a fab compare?**

The semiconductor side of the join, cleanly:

| | median asset turnover | median operating margin | median return on assets |
|---|---:|---:|---:|
| SIC 3674, all filers ≥ $10m revenue (n = 73) | **0.519×** | 1.48% | **0.71%** |
| SIC 3674, plant-owning (PP&E ≥ 30% of revenue, n = 21) | **0.476×** | 1.40% | **0.67%** |
| SIC 3672, printed circuit boards (n = 12) | 1.227× | 4.45% | 5.17% |
| All SEC filers, any SIC, ≥ $10m revenue (n = 2,845) | 0.654× | 4.35% | 3.25% |
| Named pure-play foundries, FY2025 (n = 10) | 0.433× | 12.07% | 4.29% |
| **Silex, FY2025** | **0.617×** | **26.57% / 22.67%** | **16.38% / 13.98%** |

**The margin a fab needs, to reach a given return on assets, at the plant-owning median turnover of
0.476×** (`tools/semiconductor_margins.py`):

| Target return on assets | Margin needed at 0.476× (plant-owning median) | at 0.519× (SIC 3674 median) | at Silex's 0.617× |
|---:|---:|---:|---:|
| 10% | **21.02%** | 19.25% | 16.22% |
| 15% | **31.53%** | 28.88% | 24.32% |
| 20% | **42.03%** | 38.50% | 32.43% |
| 25% | **52.54%** | 48.13% | 40.54% |
| 30% | **63.05%** | 57.75% | 48.65% |
| 40% | **84.07%** | 77.01% | 64.87% |

Arithmetic: return on assets = operating margin × asset turnover, so margin = target ÷ turnover.
0.10 ÷ 0.476 = 0.2102; 0.20 ÷ 0.476 = 0.4203; and so on. **The software agent owns the other side
of this join.** To state the semiconductor side without prejudging it: a plant-owning semiconductor
manufacturer at the median turnover of **0.476×** must earn a **21.02%** operating margin to reach
a 10% return on assets, **42.03%** to reach 20% and **84.07%** to reach 40%. Whatever return on
assets the software comparison lands on, divide it by 0.476 and that is the operating margin a fab
would have to earn to match it. On today's actual figures, **the median SIC 3674 filer earns 0.71%
on its assets and the median SEC filer of any kind earns 3.25%**, so a semiconductor company is
already earning roughly **a fifth** of the all-industry return on its assets before software is
mentioned at all.

**3. Is Silex unusual, or is 22.7% simply what a full specialty fab earns?**

**Silex is unusual, and this cuts against the project's thesis. No new entrant should plan on
22.7%.** The evidence:

- 22.7% is the **82nd percentile** of SIC 3674 and **second of ten** among listed pure-play
  foundries. "Simply what a specialty fab earns" would be the peer median of **12.07%**, or the
  SIC 3674 median of **1.48%** (`SEM-3`, `SEM-4`).
- The 35-point spread the repo asked about — Silex +22.7%, SkyWater Legacy −12.93% (`LN-7`),
  Pragmatic catastrophic (`LNI-16`) — is **not** explained by any of the three candidate
  mechanisms in the form they were posed:
  - **Utilisation:** tested, and it points the *other* way from the obvious reading. Silex earns
    22.7% at **~60% utilisation** (`SEM-2`) with, on its own arithmetic, **100% more revenue
    available from the same plant**. Utilisation is not what makes Silex good; it is the headroom
    Silex still has. Meanwhile Saiwei's Beijing FAB3 was "仍处于产能爬坡阶段" — "still in its
    capacity ramp-up phase" — with a **−50.00%** gross margin on China-origin MEMS revenue in 2022
    (`OIM-5`). Utilisation explains the *disasters*, not the *winners*.
  - **Scale:** tested, and it fails outright. Silex is the **smallest** company in `SEM-4` — USD
    141 million of revenue, one fab, 484 people — and earns the second-highest margin. X-FAB is six
    times larger with six fabs and earns 8.78% (`SEM-5`). TSMC is 860 times larger and earns
    50.83%. There is no monotone relation with size in this group.
  - **Customer concentration:** tested, and it fails in the direction H7 does not want. Silex has
    **85** customers and a top-one share of **25%**; X-FAB has **>400** customers and a top-one
    share of **43%**, and earns a third of the margin (`SEM-5`). SkyWater's high-mix Legacy segment
    loses 12.93% while its single-anchor-customer Texas segment makes 18.21% (`LN-7`). Pragmatic
    had three customers over 10% of a £901,000 revenue line and lost £65.2 million (`LNI-16`). The
    customer book does not order these outcomes.
- **What does separate them, on the evidence in this file:**
  1. **Whether the fab is paid for.** Silex's cumulative capital expenditure since founding is
     **SEK 1.9 billion** against SEK 1,385 million of annual revenue and SEK 2,246 million of total
     assets (`SEM-1`). Its capex was 6.36% of revenue in 2024. Every loss-maker in `SEM-4` is
     mid-build: Vanguard's capex was **131.67%** of revenue; Saiwei carried 12.71% of its assets in
     construction in progress and lost 21.11% at the operating line while owning the very fab that
     made 27.65% (`SEM-6`); GlobalFoundries went from −3.17% to +11.74% as its build wound down;
     Pragmatic had spent £287 million of share premium to reach £901,000 of revenue (`LNI-16`).
     **A fab's margin is a statement about the age of its plant, not about its market.**
  2. **Cost to serve, when it is not amortised over a long relationship.** `LN-7` already showed
     Legacy SkyWater spending 25.02% of revenue on SG&A against Texas's 4.63%. Silex avoids this
     not by having few customers but by having **old** ones: "eight out of Silex's ten largest
     customers have been Silex's customers since 2017 or earlier, and Silex currently still retains
     its first customer" (`LNI-18`). It runs payroll at 27.9% of revenue (`LNI-17`) against
     Clas-SiC's 45.3% (`LNI-5`).
  3. **Product mix.** Silex names it itself: "periods of high EBIT margins, have in part been
     attributable to a favourable product mix, particularly a higher share of advanced development
     programmes" (`SEM-2`) — which is `OIM-5`'s finding restated by the company. The bespoke
     low-volume end carried a 39.90% gross margin against 33.19% on volume wafers in 2024.
- **The honest summary for `WHY.md`:** Silex is the **second-best** foundry in this ten-company
  peer group on return on assets. It is a twenty-three-year-old, largely depreciated, single-site
  200 mm fab running at 60% of capacity, with an eighty-five-name customer book that mostly dates
  from before 2017, and its 22.7% is what *that* is worth. A new entrant has none of those four things. The
  right planning number from this file is not 22.7% but the peer median of **12.07%** on margin and
  **4.29%** on assets, with the observation that **three of ten listed foundries lost money in
  FY2025**.

**4. Does capital intensity actually explain fab margins?**

**No, and that is a finding.** Across 67 SIC 3674 filers the rank correlation between PP&E-to-revenue
and operating margin is **+0.05** — nothing — and the quartile medians are non-monotonic, with the
*least* capital-intensive quartile posting the *worst* median margin at −4.98% (`SEM-7`). Texas
Instruments carries PP&E at 69.7% of revenue and earns 34.06%; Analog Devices carries 30.1% and
earns 26.61%. What capital intensity does cost you is **turnover**, and therefore return on assets:
the plant-owning subset turns its assets 0.476× against 0.519× for the code as a whole, so it needs
about 9% more margin to earn the same return. **The standard story — "fabs earn thin margins
because cleanrooms are expensive" — is not supported. The defensible version is narrower: fabs earn
thin *returns* because a cleanroom sits on the balance sheet at roughly one year's revenue, and
because the return is destroyed while it is being built rather than after.**

---

## What could not be got, and why

- **Powerchip's full-year 2025 consolidated financial statements.** PSMC publishes only the most
  recent quarters at
  `https://www.powerchip.com/upload/media/financials/quarterly_result/<period>_CFS_EN.pdf`; the
  2025Q3 and 2026Q1 files are live, `2025Q4_CFS_EN.pdf` returns 404 (and once, transiently, a
  Cloudflare 521), and no `annual_report/` path resolves. The financials index page is
  JavaScript-rendered and exposes only the current quarter's link. The Taiwan doc server at
  `doc.twse.com.tw/server-java/t57sb01` requires a form POST, which was not used. Wayback could not
  be reached from this machine at all (`web.archive.org` refused the connection). **Workaround
  used:** the nine-month income statement from the reviewed Q3 2025 statements plus the 2025-12-31
  balance sheet from the comparative column of the Q1 2026 statements, clearly labelled, with an
  annualised variant shown. **Still open:** PSMC's audited FY2025 operating result, capex and D&A.
- **TSMC's and UMC's FY2025 figures were not in the SEC's `companyfacts` API** as of 2026-09-25,
  although both 20-Fs were filed (TSMC 2026-04-16, UMC 2026-04-30). The API's latest facts for both
  are FY2024. **Workaround used:** the R-files of the FY2025 filings themselves, read through
  `WebFetch` because `www.sec.gov/Archives/...` returns HTTP 403 to `curl` under every User-Agent
  tried — the same block recorded in `OIM-1`. `data.sec.gov` has no such block and answered every
  request.
- **X-FAB's customer-count-by-revenue-band chart (Fig. 4.3, p. 17 of the Annual Report 2025)** is a
  raster image with no text layer, so the distribution of X-FAB's >400 customers across revenue
  bands could not be read. It is exactly the figure H5 and H7 want. Reading it would need the
  VNC-Chrome escalation or an OCR pass over the page image; neither was done.
- **X-FAB's Shanghai STAR Market prospectus** was not located. The task brief mentions one; searches
  did not surface it, and no attempt was made through the SSE's filing portal.
- **Silex's wafer starts, wafer output and average selling price per wafer.** Verified absent from
  the 230-page prospectus (`SEM-2`) — this is now a checked negative, not an assumption.
- **A same-basis Saiwei group figure for 2025.** The July 2025 deconsolidation of Silex makes the
  2025 group accounts non-comparable, and the 2025 report merges `OIM-5`'s two MEMS lines into one
  ("MEMS 纯代工"), so the process-development-versus-volume split ends with 2024.
- **Gross PP&E for SIC 3674.** `PropertyPlantAndEquipmentGross` is tagged by too few filers to build
  a distribution, so the capital-intensity cross-tab in `SEM-7` uses net PP&E, which flatters old
  paid-for plant.
- **Non-US listed foundries in the distribution.** The SEC frames cover `us-gaap` filers only, so
  SIC 3674 in `SEM-3` excludes every 20-F filer. A genuinely global distribution would need a
  different data source; the named peers in `SEM-4` are the partial substitute.
