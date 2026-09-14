# Customer concentration (`CONC`)

How much foundries depend on a few customers, and what happens when a big customer leaves or pushes back. This is evidence for H1, H2 and H5.

---

### CONC-1. TSMC: ten customers are 76% of revenue, and the largest is 22%

- **Source:** Taiwan Semiconductor Manufacturing Company, Annual Report on Form 20-F for 2024, filed with the US SEC 2025-04-17: <https://www.sec.gov/Archives/edgar/data/1046179/000119312525083423/d896993d20f.htm>
- **Verification:** Verified 2026-09-13 from the filing's own text and its XBRL financial data (note 38).
- **What it says:**
  - Risk factors: "While we generate revenue from hundreds of customers worldwide, our ten largest customers in 2022, 2023 and 2024 accounted for approximately, 68%, 70% and 76% of our net revenue in the respective year. Our largest customer in 2022, 2023 and 2024 accounted for 23%, 25% and 22% of our net revenue in the respective year. Our second largest customer in 2022, 2023 and 2024 accounted for less than 10%, 11%, and 12% of our net revenue in the respective year."
  - "A more concentrated customer base will subject our revenue to seasonal demand fluctuations from our large customers and cause different seasonal patterns in our business."
  - Note 38, major customers at 10% or more of net revenue, 2024: Customer A NT$624,345.5M (22%) and Customer B NT$352,271.2M (12%). In 2023, Customer C was NT$241,152.4M (11%).
  - Credit risk: "the Company's ten largest customers accounted for 91 % and 93 % of accounts receivable" at the end of 2023 and 2024.
- **Bears on:**
  - H1 (supports).
  - H2 (supports: dependence, and seasonal exposure to large customers).
- **Used in:** `WHY.md` "In short", §2, §3, §5.
- **Caveats:**
  - The filing doesn't name customers. Apple (Customer A in 2024) and Nvidia are analyst attributions.
  - 2025 figures are in CONC-11 (verified).

### CONC-2. TSMC still serves 522 customers

- **Source:** TSMC, *2024 Business Overview*: <https://investor.tsmc.com/sites/ir/annual-report/2024/2024%20Business%20Overview_0.pdf>
- **Verification:** Verified 2026-09-13 (PDF text).
- **What it says:**
  - "In 2024, the Company manufactured 11,878 different products using 288 distinct technologies for 522 different customers."
  - "TSMC represented 34 percent of the Foundry 2.0 industry … output value in 2024". "Foundry 2.0" is TSMC's broadened definition, which includes packaging, testing, mask-making, and integrated device manufacturers excluding memory.
- **Bears on:**
  - H5 (supports: a tail of 512 customers outside the top ten shares about a quarter of revenue).
  - H1 (context).
- **Used in:** `WHY.md` "In short", §2, §5.
- **Caveats:** the 34% is on TSMC's own broad "Foundry 2.0" basis, not the usual foundry market-share basis (see CONC-12).

### CONC-3. GlobalFoundries: ten customers take 63% of wafers, and nearly all have their own design teams

- **Source:** GlobalFoundries Inc., Annual Report on Form 20-F for 2025, filed with the US SEC 2026-02-27: <https://www.sec.gov/Archives/edgar/data/1709048/000170904826000022/gfs-20251231.htm>
- **Verification:** Verified 2026-09-13 from the filing text.
- **What it says:**
  - "We depend on a small number of customers for a significant portion of our revenue and any loss of these or our other key customers, including potentially through further customer consolidation, could result in significant declines in our revenue."
  - "Our ten largest customers in 2025, 2024 and 2023 accounted for approximately 63%, 65% and 72% of our wafer shipment volume, respectively."
  - "Nearly all of our customers already maintain their own semiconductor design capability, and they may choose to leverage those design resources instead of utilizing our services."
  - "Given the time and costs associated with moving a single-sourced product to a competitor, clients are more likely to continue awarding us single-source contracts for such products."
  - "once our prices with a customer are negotiated, we are generally unable to revise pricing with that customer until our next regularly scheduled price adjustment."
  - "The Company's ten largest customers account for approximately 72.3 % and 80.1 % of the outstanding trade receivables balance as of December 31, 2025 and 2024, respectively."
- **Bears on:**
  - H1 (supports).
  - H2 (supports: dependence, lock-in in both directions, rigid pricing).
- **Used in:** `WHY.md` §2, §3.
- **Caveats:** the figures are wafer shipment volume, not revenue. Concentration is falling (72% in 2023, 63% in 2025), which is worth watching as a counter-trend.

### CONC-4. GlobalFoundries' concentration was higher before its IPO

- **Source:** GlobalFoundries Inc., Form F-1, 2021: <https://www.sec.gov/Archives/edgar/data/1709048/000119312521290644/d192411df1.htm>
- **Verification:** Verified 2026-09-13 (WebFetch of the filing).
- **What it says:**
  - "Our ten largest customers in 2018, 2019 and 2020 accounted for approximately 75%, 73% and 73% of our wafer shipment volume, respectively."
  - "Loss or cancellation of business from, significant changes in scheduled deliveries to, or decrease of products and services sold to any of these customers could significantly reduce our revenue."
- **Bears on:** H2 (supports).
- **Used in:** not yet.
- **Caveats:** a search summary said AMD was 28% of GF revenue in 2019 and 21% in 2020. Our fetch of the F-1 didn't find those figures, so treat them as a **Lead**.

### CONC-5. SkyWater: three customers are about three-quarters of revenue

- **Source:** SkyWater Technology, Inc., Annual Report on Form 10-K for the fiscal year ended 2025-12-28, filed with the US SEC 2026-03-11: <https://www.sec.gov/Archives/edgar/data/1819974/000181997426000009/skyt-20251228.htm>
- **Verification:** Verified 2026-09-13 for FY2025 and FY2024. FY2023 is **Partial** (search summary only).
- **What it says:**
  - "A significant portion of our sales are derived from three customers, the loss of which would adversely affect our financial results."
  - "Infineon accounted for 43% and 7% of our revenue for fiscal years ended December 28, 2025 and December 29, 2024, respectively. Two customers, other than Infineon, represented 21% and 10% of our revenue for the fiscal year ended December 28, 2025."
  - FY2024: two customers other than Infineon were 40% and 20%.
  - SkyWater acquired Infineon's Fab 25 in Austin. Per the fact-check it closed on 2025-06-30, with a supply agreement.
  - Unverified from a search summary: in the FY2023 10-K, four customers were 24%, 17%, 15% and 10% (66% together).
- **Bears on:** H2 (supports: buying a fab brings its anchor customer, and with it dependence).
- **Used in:** `WHY.md` §2, §3.
- **Caveats:** SkyWater is small (revenue about $442M in 2025, per the fact-check), so a few programmes dominate by nature.

### CONC-6. Imagination Technologies lost up to 71% of its value when Apple planned to leave

- **Source:** Karen Gilchrist, "Imagination Technologies shares plunge as much as 71 percent after Apple ends chip deal", CNBC, 2017-04-03: <https://www.cnbc.com/2017/04/03/imagination-technologies-shares-plunge-69-percent-after-apple-withdraws.html>
- **Verification:** Verified 2026-09-13.
- **What it says:**
  - "The company relies on Apple for about half of its revenues."
  - Shares fell by as much as 71% after Imagination announced that Apple planned to stop using its technology.
- **Bears on:** H2 (supports: what losing a dominant customer looks like).
- **Used in:** `WHY.md` §3.
- **Caveats:** Imagination licensed chip designs; it didn't make chips. The URL says "69 percent" and the headline says 71%.

### CONC-7. Apple reportedly paid TSMC only for working 3nm chips

- **Source:** MacRumors, "TSMC Not Charging Apple for Defective 3nm Chips Ahead of iPhone 15 Pro Introduction", 2023-08-07, reporting *The Information*: <https://www.macrumors.com/2023/08/07/tsmc-not-charging-apple-for-defective-chips/>
- **Verification:** **Partial.** The report is verified; the underlying claim is disputed.
- **What it says:** "TSMC is only charging Apple for 'known good dies,' with no fee for defective chips." The reason given is Apple's large orders and its "willingness to be the supplier's first customer for new manufacturing processes".
- **Bears on:** H2 (mixed): if true, the biggest customer gets terms nobody else gets.
- **Used in:** not yet. Deliberately left out of `WHY.md` because it's disputed.
- **Caveats:** analyst Ming-Chi Kuo said the report was not accurate. In his account Apple buys "finished goods" of the expected quality as a standard arrangement.

### CONC-8. AMD paid GlobalFoundries repeatedly to loosen their wafer supply agreement

- **Sources:**
  - AMD, "AMD Amends Wafer Supply Agreement With GLOBALFOUNDRIES", press release, 2012-12-06: <https://ir.amd.com/news-events/press-releases/detail/98/amd-amends-wafer-supply-agreement-with-globalfoundries>
  - AMD, "AMD Announces Multi-Year Amendment to the Wafer Supply Agreement With GLOBALFOUNDRIES", press release, 2016-08-31: <https://ir.amd.com/news-events/press-releases/detail/711/amd-announces-multi-year-amendment-to-the-wafer-supply-agreement-with-globalfoundries>
  - AMD, Form 8-K for Q4 2018 earnings, filed 2019-01-29 (reports the seventh amendment): <https://www.sec.gov/Archives/edgar/data/2488/000000248819000004/a20190129q418earnings8-k.htm>
- **Verification:** Verified 2026-09-14. The two press releases were read in full via curl; the 8-K was read via WebFetch.
- **What it says:**
  - **2012:** "AMD will make a termination payment of $320 million related to the take-or-pay agreement with GLOBALFOUNDRIES associated with the adjusted wafer purchase commitments in fourth quarter 2012. The cash impact of the termination fee will spread over several quarters: $80 million by Dec. 28, 2012; $40 million by Apr. 1, 2013; and A $200 million promissory note issued by AMD to GLOBALFOUNDRIES due on Dec. 31, 2013."
  - **2016 (sixth amendment, 2016–2020)**, in return for rights including flexibility to have "certain products" made by another foundry. AMD would:
    - "Make a $100 million cash payment to GF, paid in installments beginning in Q4 2016 through Q3 2017."
    - "Make quarterly payments to GF beginning in 2017 based on the volume of certain wafers purchased from another wafer foundry."
    - Grant a warrant for 75 million AMD shares to West Coast Hitech L.P., a Mubadala subsidiary.
    - Take "a one-time accounting charge in the third quarter of 2016 of approximately $335 million comprised of the $100 million payment and the $235 million value of the warrant."
  - **2019 (seventh amendment):** "On January 28, 2019, Advanced Micro Devices, Inc. (the "Company") entered into a seventh amendment (the "Seventh Amendment") to the Wafer Supply Agreement with GLOBALFOUNDRIES Inc." It "provides the Company with full flexibility to contract with any wafer foundry with respect to all products manufactured using 7nm and smaller technology nodes without any one-time payments or royalties by the Company to GF."
- **Bears on:**
  - H2 (supports): lock-in costs real money. A customer paid hundreds of millions of dollars, plus payments per wafer made elsewhere, to be free to use another foundry.
  - FIN-8 (context): a textbook relationship-specific contract.
- **Used in:** `WHY.md` §3 (from Draft v0.5).
- **Caveats:**
  - GlobalFoundries was spun out of AMD's own fabs in 2009 (background, not verified here), so this agreement is an extreme case of a factory tied to one customer.
  - The external brief dated the seventh amendment to 2018; the 8-K shows 2019-01-28.
  - A search summary says a later extension had AMD expected to buy about $2.1B of wafers from GF in 2022–2025. That's a **Lead**.

### CONC-9. Nvidia booked most of TSMC's advanced packaging capacity

- **Source:** an external investor brief, citing TrendForce (2025-02-24) and Morgan Stanley (via Astute Group).
- **Verification:** **Lead.**
- **What it says (per the brief):**
  - Nvidia "secured over 70% of TSMC's CoWoS-L advanced packaging capacity for 2025".
  - Nvidia is "predicted to book a total of 595,000 CoWoS wafers by 2026, accounting for approximately 60% of total global demand".
  - C.C. Wei called CoWoS "sold out through 2025 and into 2026".
- **Bears on:**
  - H2 (supports): big customers take scarce capacity first.
  - H6 (context): small customers get crowded out.
- **Used in:** not yet.

### CONC-10. The chip designer keeps more of the value than the foundry

- **Source:** an external investor brief, citing NVIDIA's February 2026 earnings release.
- **Verification:** **Lead.**
- **What it says (per the brief):** Nvidia reported a 75.0% GAAP gross margin in Q4 fiscal 2026, against TSMC's roughly 53–62%.
- **Bears on:** H2 (supports: value capture is weighted towards the big customer).
- **Used in:** not yet.
- **Caveats:** gross margins of a fabless designer and a manufacturer aren't directly comparable.

### CONC-11. In 2025 TSMC's concentration rose again, and Nvidia overtook Apple

- **Sources:**
  - Taiwan Semiconductor Manufacturing Company, Annual Report on Form 20-F for 2025, filed with the US SEC 2026-04-16: <https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm>
  - CNBC, "Nvidia set to supplant Apple as TSMC's largest customer", 2026-01-26: <https://www.cnbc.com/2026/01/26/nvidia-set-to-supplant-apple-as-tsmcs-largest-customer.html>
- **Verification:** Verified 2026-09-14 for the 20-F, read in a browser session because SEC blocks automated tools. The CNBC projection and the customer count are **Leads**.
- **What it says:**
  - Risk factors: "While we generate revenue from hundreds of customers worldwide, our ten largest customers in 2023, 2024 and 2025 accounted for approximately, 70%, 76% and 78% of our net revenue in the respective year. Our largest customer in 2023, 2024 and 2025 accounted for 25%, 22% and 19% of our net revenue in the respective year. Our second largest customer in 2023, 2024 and 2025 accounted for 11%, 12%, and 17% of our net revenue in the respective year. A more concentrated customer base may subject our revenue to seasonal demand fluctuations from our large customers…"
  - Major customers at 10% or more of net revenue, 2025:
    - Customer A: NT$726,974.3M (19%). In 2024 it was NT$352,271.2M (12%), so revenue from this customer rose about 106%.
    - Customer B: NT$645,178.7M (17%). In 2024 it was NT$624,345.5M (22%).
  - The labels are re-assigned each year: the 2025 filing's Customer A was 2024's second-largest customer.
  - Credit risk: "As of December 31, 2024 and 2025, the Company's ten largest customers accounted for 93% and 84% of accounts receivable, respectively."
  - **Leads:**
    - Analysts identify Customer A as Nvidia and Customer B as Apple.
    - Per the external brief, Ben Bajarin projected that in 2026 Nvidia would be about 22% and Apple about 18%.
  - Customer count (verified 2026-09-14 from TSMC's Q2 2026 results release, 2026-07-16, on Form 6-K: <https://www.sec.gov/Archives/edgar/data/1046179/000104617926000451/a2q26e_withguidancexfinal.htm>, and the TSMC 2025 annual report website): "TSMC deployed 305 distinct process technologies, and manufactured 12,682 products for 534 customers in 2025". With the top ten at 78%, the other 524 customers provided about 22% of revenue.
- **Bears on:**
  - H1 and H2 (supports): concentration keeps rising, reaching 78% in 2025, even as the largest customer changes.
- **Used in:** `WHY.md` "In short", §2, §3 and §5 (from Draft v0.5).
- **Caveats:** the filing doesn't name customers.

### CONC-12. TSMC's foundry market share, and GlobalFoundries' rank

- **Source:** TrendForce, "AI Demand Drives 4Q25 Global Top 10 Foundries Revenue Up 2.6% QoQ…", 2026-03-12: <https://www.trendforce.com/presscenter/news/20260312-12965.html>
- **Verification:** Verified 2026-09-13.
- **What it says:**
  - The quarter's revenue growth "allowed TSMC to maintain its leading position with a 70.4% market share".
  - "UMC remained fourth…"
  - "GlobalFoundries ranked fifth".
- **Bears on:** H1 (context).
- **Used in:** `WHY.md` §2.
- **Caveats:**
  - The figures are for Q4 2025 among the top ten foundries.
  - Per the brief, TrendForce's full-year 2025 share was 69.9% (Lead, via Focus Taiwan/CNA, 2026-03-13).

### CONC-13. Huawei was a large TSMC customer until US export rules cut it off

- **Source:** an external investor brief, citing Counterpoint Research.
- **Verification:** **Lead.**
- **What it says (per the brief):** Huawei was "roughly 10–15% of TSMC's business in 2019". TSMC stopped accepting Huawei orders after US rules were tightened in September 2020, and Apple, AMD and Nvidia absorbed the freed capacity.
- **Bears on:** H2 (supports): a big customer can vanish for reasons outside anyone's control. The loss was absorbed only because demand was strong.
- **Used in:** not yet.

### CONC-14. Apple moved its leading-edge chips from Samsung to TSMC

- **Source:** an external investor brief.
- **Verification:** **Lead.**
- **What it says (per the brief):** Apple shifted leading-edge logic from Samsung to TSMC around 2014–2016.
- **Bears on:** H2 (supports): a single customer's move can hollow out a foundry's node.
- **Used in:** not yet.
