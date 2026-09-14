# Costs and consolidation (`COST`)

What it costs to design chips and build fabs, and how few companies can still keep up. This is the evidence for step 1 and step 4 of the doom spiral (H1).

---

### COST-1. Designing a chip costs about $249M at 7nm and $725M at 2nm

- **Source:** Arm Holdings plc, prospectus (Form 424B4) filed with the US SEC, 2023-09-14, citing International Business Strategy, Inc. (IBS): <https://www.sec.gov/Archives/edgar/data/1973239/000119312523235320/d550931d424b4.htm>
- **Verification:** Verified 2026-09-13, by us and by an independent fact-check. SEC pages refuse automated tools; they load in a browser, or with a declared contact user agent.
- **What it says:** "IC design costs were approximately $249 million for a 7nm chip and approximately $725 million for a 2nm chip".
- **Bears on:** H1 (supports: the up-front cost at the leading edge is prohibitive).
- **Used in:** `WHY.md` §1.
- **Caveats:**
  - These are consultancy estimates, and IBS revises them (see COST-2).
  - They apply to advanced nodes; mature nodes cost far less.
  - The prospectus spells the firm "International Business Strategy, Inc."; `WHY.md` uses "International Business Strategies".

### COST-2. Other IBS design-cost estimates, and why they differ

- **Source:**
  - Semiconductor Engineering, "Big Trouble At 3nm": <https://semiengineering.com/big-trouble-at-3nm/>
  - ALLPCB, "What Does Advanced-Process Chip Design Cost?", 2025-09-11: <https://www.allpcb.com/allelectrohub/what-does-advancedprocess-chip-design-cost>
  - An external investor brief (see analyses).
- **Verification:** **Partial.** Checked only through secondary sources, which disagree with each other.
- **What it says:**
  - The 2018 IBS figures were $51.3M at 28nm, $297.8M at 7nm and $542.2M at 5nm. That article also gives $500M–$1.5B at 3nm.
  - ALLPCB reports that IBS later revised these downwards: 28nm from about $85M to $51M, and 16/14nm from about $310M to $106M. It warns that the 2018 estimates "may no longer be accurate".
  - The investor brief gives $416M at 5nm and $590M at 3nm.
- **Bears on:** H1 (context).
- **Used in:** not yet. `WHY.md` uses COST-1 instead.
- **Caveats:** don't mix figures from different years in one chart. Cite the year of each estimate.

### COST-3. More than two dozen companies could make leading-edge chips in 1998; three by 2020

- **Source:** Mark LaPedus, "Will the U.S. CHIPS Act Succeed?", *Semiecosystem*, 2024-05-25, quoting David Schor of WikiChip: <https://marklapedus.substack.com/p/will-the-us-chips-act-succeed>
- **Verification:** Verified 2026-09-13.
- **What it says:**
  - "In 1998, more than two dozen companies could make chips in their fabs based on the 180nm process, which was the most advanced technology back then."
  - Schor: "As shrinking becomes more complex, requiring more capital, expertise, and resources, the number of companies capable of providing leading-edge fabrication has been steadily dropping… As of 2020, only three companies are now capable of fabricating integrated circuits on the most cutting-edge process: Intel, Samsung, and TSMC."
  - "Today's most advanced fabs cost $20 billion each."
- **Bears on:** H1 (supports: consolidation as costs rose).
- **Used in:** `WHY.md` §1, §2.
- **Caveats:** the first sentence is LaPedus's narration and the quote is Schor's; don't merge them into one quotation. A different source says 18 chipmakers had 130nm-capable fabs in 2001 (Lead: Semiconductor Engineering, "Regaining the Edge in U.S. Chip Manufacturing").

### COST-4. GlobalFoundries stopped 7nm development because it didn't have enough customers

- **Source:** Samuel K. Moore, "GlobalFoundries Halts 7-Nanometer Chip Development", *IEEE Spectrum*, 2018-08-28: <https://spectrum.ieee.org/globalfoundries-halts-7nm-chip-development>
- **Verification:** Verified 2026-09-13.
- **What it says:**
  - Subheadline: "After installing extreme-ultraviolet lithography, foundry finds it doesn't have enough customers for it".
  - Per the fact-check, the article says "there are not enough customers that need bleeding-edge 7-nm processes to make it profitable", that plans are "on indefinite hold" despite "having installed at least one EUV machine", and that layoffs "could be in the hundreds".
- **Bears on:**
  - H1 (supports: the spiral in one event).
  - H2 (supports: years of guessing the future written off).
- **Used in:** `WHY.md` §2, §3.
- **Caveats:** the article gives no loss figure. Leads for more detail:
  - HPCwire, 2018-08-29: 5% workforce cut
  - GF's own press release, via AnandTech
  - The external brief: former CEO Sanjay Jha estimated a 7nm fab at $10–12B, and AMD moved to TSMC

### COST-5. TSMC expects its total US investment to reach $165B

- **Source:** TSMC, "TSMC Intends to Expand Its Investment in the United States to US$165 Billion to Power the Future of AI", 2025-03-04: <https://pr.tsmc.com/english/news/3210>
- **Verification:** Verified 2026-09-13 by the fact-checker. pr.tsmc.com is behind a Cloudflare challenge that blocks plain curl.
- **What it says:** "Building on the company's ongoing $65 billion investment in its advanced semiconductor manufacturing operations in Phoenix, Arizona, TSMC's total investment in the U.S. is expected to reach US$165 billion."
- **Bears on:** H1 (context: the scale of leading-edge investment).
- **Used in:** `WHY.md` §1.
- **Caveats:** this is a US total over several sites and years, not one fab.

### COST-6. Most chips in cars are made on mature nodes

- **Source:** Mark LaPedus, "Chip Shortages Grow For Mature Nodes", *Semiconductor Engineering*, 2021-07-22: <https://semiengineering.com/chip-shortages-grow-for-mature-nodes/>
- **Verification:** Verified 2026-09-13.
- **What it says:** "Cars may have some leading-edge chips, but the vast majority of devices are based on mature nodes."
- **Bears on:**
  - H4 (context): an open fab on mature processes addresses most devices.
  - H1 (context): the leading-edge cost figures don't describe most chips.
- **Used in:** `WHY.md` §1.
- **Caveats:** it's about cars; there's no source yet for "most chips overall". A related Lead is the Hoover Institution, *The Silicon Triangle* ch. 2, which defines mature nodes as 28/40nm and above, and warns it is "a common misconception" that they are simply older, cheaper versions.

### COST-7. TSMC's capital spending keeps climbing

- **Source:** an external investor brief (see [`../analyses/tyranny-of-the-whale-brief.md`](../analyses/tyranny-of-the-whale-brief.md)).
- **Verification:** **Lead.**
- **What it says (per the brief):**
  - Capex of $36.3B (2022), about $30B (2023 and 2024), about $40B (2025), and guidance of $52–56B for 2026.
  - "Capital intensity exceeds 33% of revenue".
  - CEO C.C. Wei said the 2026 spending "contributes nothing" to 2026 revenue.
  - Gross margin was 56.1% in 2024, up from 54.4% in 2023, "mainly attributable to higher capacity utilization".
- **Bears on:**
  - H1 (supports: the scale needed keeps rising).
  - H2 (context: utilisation drives margins, so fabs can't refuse a customer that fills them).
- **Used in:** not yet.
- **To verify:** TSMC's quarterly earnings releases and its 2025 20-F.

### COST-8. The foundry pays to develop each process years ahead

- **Source:** TSMC, *2024 Business Overview*, published 2025: <https://investor.tsmc.com/sites/ir/annual-report/2024/2024%20Business%20Overview_0.pdf>
- **Verification:** Verified 2026-09-13 (PDF text).
- **What it says:**
  - "In 2024, TSMC continued to invest in research and development, with total R&D expenditures amounting to 7.1% of revenue."
  - It also describes 2nm development in 2024 ("baseline setup, yield enhancement…").
- **Bears on:** H2 (supports: the fab guesses the future at its own expense).
- **Used in:** `WHY.md` §3.
- **Caveats:** the figure covers all R&D, not only process development. The document's PDF metadata dates it to October 2025.
