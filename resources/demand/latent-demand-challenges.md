# Evidence against the latent demand (`DEM`)

`resources/README.md` says: *"Challenges are as valuable as support. Record them with the same care.
Don't soften them."* These entries were gathered by deliberately looking for reasons H5 is wrong.

Three separate lines of attack turn up. First, the count of chip designs being started has been
falling for twenty-five years, not rising. Second, the binding constraint on getting a working chip
may be verification engineering rather than money. Third, the long-tail theory's own most-cited
empirical test found the tail getting longer and flatter, and its author says so explicitly for
physical goods too.

The counter-evidence *inside* the shuttle data — undersubscribed runs, the 40-slot cap, the modest
total response to free manufacturing — is in [`shuttle-programmes.md`](shuttle-programmes.md) under
DEM-2, DEM-9 and DEM-10, next to the supporting numbers, rather than separated out here.

---

### DEM-11. ASIC design starts were already falling in 2002, and the two analyst houses that counted them disagreed by 2.5×

- **Source:** Crista Souza, "ASIC starts decline due to rising cost, complexity", *EE Times*,
  2002-11-11: <https://www.eetimes.com/asic-starts-decline-due-to-rising-cost-complexity/>
- **Verification:** Verified 2026-09-18 by fetching the page, through `WebFetch` — `curl` to
  `eetimes.com` returned no HTTP response at all (exit 92). The quotes are as `WebFetch` returned
  them from the page; author and date were returned with them.
- **What it says:**
  - Attributed to Jordan Selburn of iSuppli Corp.: "the number of ASIC design starts this year will
    drop to half the level reached in 1998"; "ASIC design starts are projected to decline from about
    2,100 in 2001 to 1,750 in 2006"; and the market forecast "ASIC market to dwindle from $11 billion
    worldwide in 2001 to a core business in the range of $6 billion to $8 billion annually".
  - Attributed to Bryan Lewis of Gartner Dataquest: Dataquest "puts the number closer to 5,000 this
    year, declining to just over 3,000 in 2006".
- **Bears on:**
  - **H5 (challenges).** The number of new chip designs started per year was falling twenty-five
    years ago and was forecast to keep falling. H5 asserts a large reservoir of unmade chips held
    back by cost; the industry's own counters recorded the opposite trend in the actual number of
    designs.
  - **H1 (supports).** The reason given is the one the doom spiral predicts: rising cost and
    complexity.
- **Used in:** not yet.
- **Caveats:**
  - **The two houses disagree by about 2.5× on the level** — 2,100 versus 5,000 for essentially the
    same year. The *direction* is agreed; the *level* is not, and neither is a published methodology.
    Do not quote either number as "the" figure.
  - "ASIC design starts" excludes FPGA designs, and part of the decline is a migration to FPGAs and
    to standard parts rather than an absence of demand for custom function.
  - This is a 2002 article. A current design-start count was **not found**; see
    [`search-log.md`](search-log.md).
  - A later aggregation (Sean Murphy, "ASIC Design Starts Dropping: Implications for EDA",
    SKMurphy Inc., 2007-04-11, <https://www.skmurphy.com/blog/2007/04/11/asic-design-starts-dropping-implications-for-eda/>)
    reproduces a Gartner table reading 2000: 7,749 → 2008: 3,048 and attributes to Bryan Lewis the
    definition "a design start equals a unique tapeout". **Status: Lead.** We did not open that page
    ourselves and the underlying Gartner tables are not public.

### DEM-12. Only 5% of chip projects get working first silicon, and the reasons given are about engineering, not money

- **Sources:** Harry Foster, Chief Scientist Verification, Siemens EDA, *Verification Horizons* blog:
  - "The 2026 Functional Verification Study: Evidence of a New Verification Operating State",
    2026-09-08:
    <https://blogs.sw.siemens.com/verificationhorizons/2026/09/08/the-2026-functional-verification-study/>
  - "Why First-Silicon Success Is Getting Harder for System Companies", 2025-09-03:
    <https://blogs.sw.siemens.com/verificationhorizons/2025/09/03/why-first-silicon-success-is-getting-harder-for-system-companies/>
- **Verification:** Verified 2026-09-18 for the 2026 post, fetched and read in full. The 2025 post's
  figures ("only 14% of ASIC/SoC projects achieved first-silicon success — the lowest figure in more
  than twenty years", "60–70% of engineering effort in chip projects belongs in verification") were
  reported to us but **we did not open that page ourselves: treat the 2025 quotes as Partial**.
- **What it says (2026 post, read directly):**
  - "Among IC/ASIC respondents, only 5% reported first-silicon success in 2026 , compared with 14.4%
    in 2024 ."
  - "The broader spin distribution reinforces the same pattern, with the overwhelming majority of
    respondents reporting multiple spins before production."
  - Foster's own reading of why: "It is tempting to look for a single explanation—a shortage of
    verification engineers, inadequate methodologies, schedule pressure, increasing design size, or
    insufficient automation. I don't think the data supports such a simple conclusion." And: "the
    2026 findings show a verification environment that is increasingly dominated by processor-rich,
    acceleration-class systems with embedded software and expanding safety, security, and other
    assurance requirements."
  - He also cautions against over-reading the metric: "This is one reason I believe we need to be
    careful when interpreting first-silicon success."
- **Bears on:**
  - **H5 (challenges, and this is the most serious challenge found).** If 86–95% of *funded,
    professional* chip projects need at least one respin, then the money to buy a tape-out is not
    what stands between an idea and a working chip. Cheap machine time buys you one attempt.
    Reducing the price of an attempt from $50,000 to $5,000 turns an expensive failure into a cheap
    one; it does not by itself produce a product. Anyone arguing H5 has to explain what the cheap
    attempts are *for* — learning and experiment (which is `WHY.md` §5's actual argument), not
    finished products.
  - **H4 (challenges):** the falling cost of design does not appear to be translating into working
    silicon.
- **Used in:** not yet.
- **Caveats:**
  - **Sample size, sampling frame and question wording are not stated in the blog post.** The
    underlying Siemens EDA / Wilson Research Group study was not obtained. The respondent base is
    self-selected industry professionals working on large, complex designs; a Tiny Tapeout tile is
    not in that population and its "first-silicon success" rate could be very different.
  - Siemens EDA sells verification tools, so it has an interest in verification looking hard.
  - Foster himself says the study "does not establish that processor content, AI acceleration,
    safety, security, DFT integration, or any other individual factor causes lower first-silicon
    success."
  - The 5% figure is one year and a sharp fall from 14.4%; one data point is not a trend.

### DEM-13. Elberse's own data: when distribution got cheap, the tail got longer and flatter — and she says it applies to physical goods

- **Source:** Anita Elberse, "Should You Invest in the Long Tail?", *Harvard Business Review*,
  July–August 2008, reprint R0807H. Read from the full-text reprint at
  <https://geminisufscar.files.wordpress.com/2009/05/shouldyouinvestinthelongtail.pdf> (the same copy
  `TAIL-3` uses).
- **Verification:** Verified 2026-09-18. The PDF was downloaded and the text extracted and searched;
  each quote below was located in the extracted text. (The PDF uses "ﬁ"/"ﬂ" ligatures, which are
  rendered as ordinary "fi"/"fl" here.)
- **What it says** — these go beyond what `TAIL-3` already records:
  - On what happened to the tail as the channel widened: "we found that sales did shift measurably
    into the tail: The number of titles that sold only a few copies almost doubled for any given week
    from 2000 to 2005. In the same period, however, the number of titles with no sales at all in a
    given week quadrupled. Thus the tail represents a rapidly increasing number of titles that sell
    very rarely or never. **Rather than bulking up, the tail is becoming much longer and flatter.**"
  - And at the head: "our research also showed that success is concentrated in ever fewer
    bestselling titles at the head of the distribution curve. From 2000 to 2005 the number of titles
    in the top 10% of weekly sales dropped by more than 50%—an increase in concentration that is
    common in winner-take-all markets".
  - On how thin the tail is: "In my most recent correspondence with managers at Nielsen SoundScan, I
    learned that of the 3.9 million digital tracks sold in 2007 (the large majority for 99 cents each
    through Apple iTunes), an astonishing 24% sold only one copy, and 91%—3.6 million tracks—sold
    fewer than 100 copies."
  - Her conclusion: "The data show how difficult it is to profit from the tail." And: "My research
    suggests that the tail is long and flat, and therefore that content providers will find it hard
    to profit much from it."
  - Her advice for anyone operating in the tail: "When producing niche goods for the tail end of the
    distribution, keep costs as low as possible. Your odds of success aren't favorable here either,
    and they will probably become less so. The extremely low demand for the large array of products
    in the tail means that simply recovering the costs of producing them will be challenging."
  - **And she extends it to hardware herself:** "Although my research has focused on media content
    and information goods, these recommendations probably apply to physical goods as well. In fact,
    their payoff for manufacturers and retailers of physical goods might be bigger, because of the
    higher production costs involved."
- **Bears on:**
  - **H5 (challenges).** The closest thing to a controlled experiment on "what happens when the cost
    of trying collapses" found that the number of items selling almost nothing exploded while the
    head got more concentrated. That is exactly the shape a fab would see: thousands of designs that
    are never made twice.
  - **H6 (challenges).** "keep costs as low as possible … simply recovering the costs of producing
    them will be challenging" is the direct statement of the H6 problem, by the researcher who
    measured it.
  - **H10 (context, and mildly supporting).** Elberse's finding that the head gets *more*
    concentrated is compatible with `WHY.md`'s argument, which does not need the tail to outsell the
    head — only for a few tail experiments to grow.
- **Used in:** not yet. `TAIL-3` is used in `WHY.md` §5 and records the Rhapsody and Quickflix
  concentration figures; this entry records the parts of the same article that bear hardest on the
  foundry case and were not previously written down.
- **Caveats:**
  - Music and video, in 2008, not manufacturing. The read-across is Elberse's own, in one sentence,
    and it is an opinion rather than a measurement.
  - The reprint PDF is a course copy, not HBR's own hosting. The authoritative version is behind
    hbr.org's paywall, which we did not attempt to bypass.
  - Elberse is arguing a position against Anderson, and both had a book to sell.

### DEM-14. A named industry figure on why this customer base does not pay

- **Source:** Daniel Nenni, founder of SemiWiki, in the forum thread "efabless just shut down",
  post #5, dated on the page "Mar 5, 2025":
  <https://semiwiki.com/forum/threads/efabless-just-shut-down.22217/>
- **Verification:** Verified 2026-09-18, the thread was fetched and the post read in place, with its
  author label ("Daniel Nenni — Founder — Staff member") and date.
- **What it says, verbatim:**
  - "Yes, big foundries are not a fan of open source tools. TSMC silicon verifies EDA tools and IP so
    customers can be assured of success. The whole trusted foundry thing. We worked with eFabless
    when they first started. It was fun and very educational but the revenue model just did not work.
    **People who use open source tools do it mainly due to cost and that is a tough customer base to
    profit from.** My opinion."
- **Bears on:**
  - **H6 (challenges).** A selection argument, and a sharp one: the customers a cheap open route
    attracts are, by construction, the ones least able or willing to pay. That is not an argument
    about cost to serve; it is an argument about willingness to pay, and H6 does not address it.
  - **H5 (challenges, indirectly).** If the latent demand is latent *because* it is
    price-sensitive at the very bottom, it may never be worth much at any price that covers a fab.
- **Used in:** not yet.
- **Caveats:**
  - **This is a forum post and the author labels it "My opinion".** It is evidence of what a
    well-placed observer thinks, not of what is true. It is recorded because it is the clearest
    statement found of the selection problem, by someone named and identifiable, not because it
    settles anything.
  - Nenni runs a site funded by the commercial EDA and IP industry, which is the incumbent side of
    this argument.
  - A reply in the same thread, from a user identified only by the handle "revsemi" (2025-03-05),
    reads "The problem is that such an open source definition actually makes it very hard for small
    companies to survive." We have no real name for that account and have not invented one; it is
    recorded here only so the thread is not misrepresented as unanimous.

### DEM-15. TSMC's "tail" is not made of small customers: about US$41 million each

- **Sources:** all primary figures are already verified elsewhere in this repository; this entry is
  arithmetic on them.
  - Revenue: Taiwan Semiconductor Manufacturing Company, Annual Report on Form 20-F for 2024, filed
    2025-04-17, accession 0001193125-25-083423, as published in the SEC's own XBRL company-concept
    API: <https://data.sec.gov/api/xbrl/companyconcept/CIK0001046179/ifrs-full/Revenue.json> —
    `2024-01-01 .. 2024-12-31`, TWD 2,894,307,700,000 and USD 88,268,000,000.
  - Customer count: `CONC-2` (TSMC, *2024 Business Overview*, Verified 2026-09-13): "In 2024, the
    Company manufactured 11,878 different products using 288 distinct technologies for 522 different
    customers."
  - Concentration: `CONC-11` (TSMC 20-F for 2025, Verified 2026-09-14): "our ten largest customers in
    2023, 2024 and 2025 accounted for approximately, 70%, 76% and 78% of our net revenue in the
    respective year."
- **Verification:** Verified 2026-09-18 for the revenue figures, read from the SEC XBRL API
  (`data.sec.gov` serves automated requests; `www.sec.gov/Archives/...` returns HTTP 403 to `curl`).
  The customer count and concentration percentage are Verified entries already in
  [`../references/customer-concentration.md`](../references/customer-concentration.md).
- **DERIVED (arithmetic written out), for financial year 2024:**
  - Customers outside the top ten: 522 − 10 = **512**.
  - Their share of revenue: 100% − 76% = **24%**.
  - Their revenue: US$88,268,000,000 × 0.24 = **US$21,184,320,000**.
  - Average per customer: US$21,184,320,000 ÷ 512 = **US$41,375,625**, i.e. about **US$41 million a
    year each**.
  - In New Taiwan dollars: NT$2,894,307,700,000 × 0.24 ÷ 512 = **NT$1,356,706,734**, about
    NT$1.36 billion each.
- **Bears on:**
  - **H5 (challenges the way the existing evidence is read).** `hypotheses.md` lists CONC-2 and
    CONC-11 under "Supports" for H5, on the grounds that TSMC's 512 customers outside its top ten
    share about a quarter of revenue. That is true, but the *average* member of that tail spends
    about US$41 million a year with TSMC. These are not small customers in any sense foundry.api
    means. The existing foundry tail is a tail of *large companies*; it is not evidence that a tail
    of tiny ones exists or would pay.
  - **H5 (context).** It does not follow that no tail of small customers exists — only that TSMC's
    customer list is not evidence for one, and should not be cited as if it were.
- **Used in:** not yet. `WHY.md` §5 currently cites the TSMC tail; this entry is the arithmetic a
  reader would need to judge that citation, and a reason to be careful with it.
- **Caveats:**
  - **An average is not a distribution.** The 512 are certainly themselves heavily skewed: customers
    ranked 11 to 30 will be far above the mean and the smallest will be far below. The smallest TSMC
    customer may well be small. What the arithmetic rules out is the tail being *typically* small.
  - The 76% is stated as "approximately" in the filing, so the 24% is approximate too.
  - The 522 customers (calendar 2024, from the Business Overview) and the 76% (from the 20-F) are
    from two different TSMC documents for the same year.
  - **The equivalent 2025 calculation could not be completed.** TSMC's 2025 total revenue is not in
    the SEC XBRL concept endpoints (the FY2025 20-F was filed by a different agent and its facts are
    not indexed there), `www.sec.gov/Archives/...` returns 403 to `curl`, and
    `investor.tsmc.com` returns 403 as well. With 534 customers and the top ten at 78% (both from
    `CONC-11`), the answer would be close to US$50 million each, but we have not verified TSMC's 2025
    revenue and so do not state it. See [`search-log.md`](search-log.md).
