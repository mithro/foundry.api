# Economics of concentration and fixed cost (`ECON`)

The economics behind two arithmetic rules: why a concentrated customer base is risky (the Herfindahl
index and its reciprocal, the "effective number of customers"), and why a large fixed cost shrinks the
set of markets that can pay for it. This bears on H1, H2, H5, H7 and H10.

These entries were harvested from the endnotes of the outside document *Big Customers, Big Bets*
(assessed in [`../analyses/big-customers-big-bets.md`](../analyses/big-customers-big-bets.md)). Unlike
the `FIN` entries, which were taken on trust from another document's reference list, **every citation
here was checked against the Crossref DOI resolver and at least one second independent source**
(publisher page, RePEc/EconPapers, an author's own copy, PubMed, or a library catalogue). Where an
entry is **Partial**, the bibliographic details are confirmed but the text itself was not read; the
entry says so and names what blocked it.

**Overlap with `FIN`.** The document also cites three works the repository already holds. They are not
duplicated here:

| Document's citation | Existing entry | Note |
|---|---|---|
| Dhaliwal, Judd, Serfling & Shaikh (2016) | FIN-2 | The document's DOI, `10.1016/j.jacceco.2015.03.005`, is the correct one. **FIN-2's DOI is wrong** — see "Changes needed in other files" in the analysis. |
| Klein, Crawford & Alchian (1978) | FIN-8 | Citation checked: *Journal of Law and Economics* 21(2), Oct 1978, 297–326, doi:10.1086/466922. All correct as FIN-8 prints it. Williamson's 1985 book, which the document pairs with it, is new here as ECON-6. |
| Patatoukas (2012) | FIN-5 | Cited by the document as the counter-argument. On 2026-09-14 the owner decided not to pursue it; not pursued. Citation checked in passing: *The Accounting Review* 87(2), 2012, 363–392, doi:10.2308/accr-10198, all correct. |

The document also cites Arm's Form F-1 (COST-1), the GlobalFoundries 7nm halt (COST-4), the
Semiconductor Engineering pieces behind COST-3, and the Efabless/Google shuttle programme (OPEN-1,
OPEN-5). Those are not repeated here either.

---

## 1. Concentration, variance and the effective number of customers

### ECON-1. Idiosyncratic shocks stop averaging out when units are fat-tailed, and the Herfindahl index governs what is left

- **Source:** Xavier Gabaix, "The Granular Origins of Aggregate Fluctuations", *Econometrica* 79(3), May 2011, pp. 733–772. DOI 10.3982/ECTA8769. Author's own copy: <https://pages.stern.nyu.edu/~xgabaix/papers/granular.pdf>
- **Verification:** **Verified** 2026-09-18. Read the author's own PDF, whose front matter reads "Econometrica, Vol. 79, No. 3 (May, 2011), 733–772". Cross-checked against Crossref (title, volume, issue, pages and year all match) and the Econometric Society's listing.
- **What it says:**
  - Abstract: "I show that this argument breaks down if the distribution of firm sizes is fat-tailed, as documented empirically. The idiosyncratic movements of the largest 100 firms in the United States appear to explain about one-third of variations in output growth."
  - Equation (4)–(5): if all units have the same volatility σ, then σ_GDP = σ·h, "where h is the square root of the sales herfindahl of the economy", h = [Σ (S_it / Y_t)²]^(1/2). Gabaix then calls h itself "the herfindahl of the economy" for short.
  - "Empirically, the sales herfindahl h is quite large" for the United States.
- **Bears on:**
  - H2 (supports). This is the formal reason a concentrated customer list is a risk and not just an inconvenience: the law of large numbers does not rescue you when a few units are large.
  - H7 (supports, as the reverse): volatility falls as the square root of the Herfindahl, so many small customers genuinely do damp the swings.
- **Used in:** not yet.
- **Caveats:**
  - Gabaix's units are *firms in an economy*, not *customers of a firm*. Applying the identity to a customer list is an analogy, though an exact one arithmetically: the variance identity is the same. The document says so.
  - The result needs customers' shocks to be independent. Correlated customers (same end market, same paymaster) behave as one, which the document also flags.

### ECON-2. Network links between firms are a second route by which individual shocks become aggregate ones

- **Source:** Daron Acemoglu, Vasco M. Carvalho, Asuman Ozdaglar and Alireza Tahbaz-Salehi, "The Network Origins of Aggregate Fluctuations", *Econometrica* 80(5), 2012, pp. 1977–2016. DOI 10.3982/ECTA9623
- **Verification:** **Partial** 2026-09-18. Citation confirmed against Crossref (title, *Econometrica*, vol. 80, issue 5, pp. 1977–2016, 2012) and the publisher listing. The paper itself was not read.
- **What it says (per its own abstract as indexed):** microeconomic idiosyncratic shocks can propagate through input–output linkages and generate aggregate fluctuations, so the relevant structure is the network, not only the size distribution.
- **Bears on:** H2 (context). It is why "customers who all sell into the same market count as one customer" is more than a rhetorical flourish.
- **Used in:** not yet.
- **Caveats:** the document cites it in one clause, for correlated customers. It has not been checked that the paper says anything specifically about customer concentration.

### ECON-3. The Herfindahl index, its disputed parentage, and the "numbers equivalent"

- **Source:** Albert O. Hirschman, "The Paternity of an Index", *American Economic Review* 54(5), September 1964, pp. 761–762. JSTOR stable 1818582 (= DOI 10.2307/1818582)
- **Verification:** **Partial** 2026-09-18. The citation is confirmed: JSTOR's issue page for *The American Economic Review* Vol. 54, No. 5, Sep. 1964 exists at <https://www.jstor.org/stable/i331529>, and several independent secondary sources give the article at pp. 761–762 of that issue. **Blocker:** JSTOR's article and issue pages return a client-side loading error to every automated fetch, and the note is not open access anywhere reachable, so the two pages themselves were not read.
- **What it says (per secondary description, not read):** Hirschman claims prior authorship of the concentration index later named for Herfindahl. Hirschman's 1945 version used the square root of the sum of squared shares; Herfindahl's 1950 version dropped the square root.
- **Why it is here:** the document uses the index's **reciprocal** as the "effective number of customers" (it calls this the "numbers equivalent"). That is a usable quantitative tool the repository does not currently have. Worked arithmetic for TSMC, `DERIVED` from CONC-1 and CONC-2, is in the analysis file.
- **Bears on:** H2 and H7 (context: it gives both a single number to argue with).
- **Used in:** not yet.
- **Caveats:**
  - The "numbers equivalent" interpretation is standard in industrial organisation but is not, so far as we have checked, stated in Hirschman's two-page note. Do not attribute it to him.
  - Do not write "Herfindahl–Hirschman index" and cite Hirschman 1964 as if it defined the index. It is a priority note, not a definition.

### ECON-4. Bargaining outcomes are set by what each side can walk away to

- **Source:** John F. Nash, Jr., "The Bargaining Problem", *Econometrica* 18(2), April 1950, pp. 155–162. DOI 10.2307/1907266, JSTOR stable 1907266. Full text: <https://www.haverford.edu/sites/default/files/Nash1950.pdf>
- **Verification:** **Verified** 2026-09-18. Read the full article. Its JSTOR cover page reads "Source: Econometrica, Vol. 18, No. 2 (Apr., 1950), pp. 155-162". Cross-checked against Crossref and the Econometric Society's listing.
- **What it says:**
  - "A new treatment is presented of a classical economic problem, one which occurs in many forms, as bargaining, bilateral monopoly, etc."
  - "In a bargaining situation one anticipation is especially distinguished; this is the anticipation of no cooperation between the bargainers. It is natural, therefore, to use utility functions for the two individuals which assign the number zero to this anticipation."
- **Bears on:**
  - H2 (supports). The solution is defined on the surplus *above each party's disagreement point*, which is the formal statement of "the side with the worse fallback takes the price".
  - H7 (supports, as the reverse): a seller with many buyers has a fallback; a seller with one does not.
- **Used in:** not yet.
- **Caveats:** Nash's is an axiomatic cooperative solution, not a description of how negotiations actually run. It says what a "fair" split consistent with four axioms looks like, not that real bargainers reach it.

### ECON-5. In alternating-offer bargaining, agreement is immediate and the more patient side gets more

- **Source:** Ariel Rubinstein, "Perfect Equilibrium in a Bargaining Model", *Econometrica* 50(1), January 1982, pp. 97–109. DOI 10.2307/1912531. Author's own copy: <https://arielrubinstein.tau.ac.il/papers/11.pdf>
- **Verification:** **Partial** 2026-09-18. Citation confirmed against Crossref (Econometrica 50(1), 1982, first page 97), RePEc/IDEAS (pp. 97–109) and the Econometric Society's listing. **Blocker:** the author's own PDF is a page scan with no text layer, so its content could not be read; the text was checked only against the Econometric Society's abstract.
- **What it says (abstract, via the Econometric Society):** two players must agree on the partition of a pie of size 1, making proposals in turn; the paper characterises the perfect equilibrium partitions, and the outcome depends on bargaining costs or discount factors.
- **Bears on:** H2 (supports), H7 (supports, as the reverse). Same mechanism as ECON-4, in a non-cooperative model with time.
- **Used in:** not yet.
- **Caveats:**
  - **Page range discrepancy.** RePEc, JSTOR and the document give 97–109. The Econometric Society's own page gives 97–110. Both are in circulation; the scan runs to 14 pages, which is consistent with either. Use 97–109.
  - The "more patient side gets more" result is standard and correct, but it was not confirmed from the paper's own text here.

### ECON-6. Relationship-specific assets create hold-up (the book-length treatment)

- **Source:** Oliver E. Williamson, *The Economic Institutions of Capitalism*, The Free Press, 1985.
- **Verification:** **Partial** 2026-09-18. The edition is confirmed in library catalogue records (Oliver E. Williamson, 1985, Free Press / Collier Macmillan). The book was not read.
- **Why it is here:** FIN-8 already holds Williamson's 1979 *Journal of Law and Economics* article and Klein, Crawford & Alchian (1978). The 1985 book is the fuller statement and is a separate work; this entry exists so that FIN-8 is not silently extended.
- **Bears on:** H2 (supports), H11 (context: general machine time sold on a market is the opposite of a relationship-specific asset).
- **Used in:** not yet.
- **Caveats:** a book, not a study. Cite it for the framework, not for evidence.

### ECON-7. Variability has to be paid for in capacity, inventory or time

- **Sources:**
  - J. F. C. Kingman, "The single server queue in heavy traffic", *Mathematical Proceedings of the Cambridge Philosophical Society* 57(4), October 1961, pp. 902–904. DOI 10.1017/S0305004100036094
  - Wallace J. Hopp and Mark L. Spearman, *Factory Physics*, Irwin, 1996.
- **Verification:** **Partial** 2026-09-18. Kingman's citation is confirmed exactly against Crossref (title, journal, volume 57, issue 4, pages 902–904, October 1961). **Blocker:** Cambridge Core returned HTTP 500 on repeated attempts, so neither the abstract nor the text was read. *Factory Physics* is confirmed as a Hopp and Spearman title published by Irwin; library records give a first edition of 1995 or 1996 depending on the record.
- **What it says (per the document, unverified):** Kingman's approximation makes queue waiting time rise with the *variability* of arrivals and service, not only with utilisation, so uneven demand must be absorbed by idle capacity. The "variability is always paid for in inventory, capacity or time" phrasing is the document's attribution to Hopp and Spearman.
- **Bears on:**
  - H2 (supports): lumpy demand from a few large customers costs a fab spare capacity.
  - H6 and H7 (supports, as the reverse): many small, uncorrelated customers smooth arrivals.
  - H11 (context): this is the physics an open fab's pricing would have to price.
- **Used in:** not yet.
- **Caveats:**
  - The *Factory Physics* year should be settled before citing it. 1996 is the usual citation for the first edition; one catalogue record says 1995.
  - Neither source has been checked to say anything about semiconductor fabs specifically.

### ECON-8. Suppliers lose value when a big customer goes into distress, before any contract is lost

- **Source:** Michael G. Hertzel, Zhi Li, Micah S. Officer and Kimberly J. Rodgers, "Inter-firm linkages and the wealth effects of financial distress along the supply chain", *Journal of Financial Economics* 87(2), February 2008, pp. 374–387. DOI 10.1016/j.jfineco.2007.01.005. Abstract: <https://econpapers.repec.org/RePEc:eee:jfinec:v:87:y:2008:i:2:p:374-387>
- **Verification:** **Partial** 2026-09-18 (abstract only). Citation confirmed independently against Crossref and EconPapers/RePEc, which agree on all four authors, volume 87, issue 2, pages 374–387 and the year. **Blocker:** ScienceDirect returns HTTP 403 to automated fetches, so the full text was not read.
- **What it says (abstract):**
  - "This study broadens the investigation by examining the wealth effects of distress and bankruptcy filing for suppliers and customers of filing firms."
  - "On average, important wealth effects occur prior to and at bankruptcy filings and extend beyond industry competitors along the supply chain."
  - "Specifically, distress related to bankruptcy filings is associated with negative and significant stock price effects for suppliers."
- **Bears on:** H2 (supports). It is the mechanism behind the document's line that "the customer does not have to leave to damage the share price. It only has to be able to."
- **Used in:** not yet.
- **Caveats:** US listed firms across industries, not foundries. The effect studied is *customer distress*, not customer departure or price pressure.

---

## 2. Fixed cost, market size, and what gets built

### ECON-9. A market has to reach a size before it supports a first firm, and a larger size before a second

- **Source:** Timothy F. Bresnahan and Peter C. Reiss, "Entry and Competition in Concentrated Markets", *Journal of Political Economy* 99(5), October 1991, pp. 977–1009. DOI 10.1086/261786. Abstract: <https://ideas.repec.org/a/ucp/jpolec/v99y1991i5p977-1009.html>
- **Verification:** **Partial** 2026-09-18 (abstract only). Citation confirmed independently against Crossref and IDEAS/RePEc: both give volume 99, issue 5, 1991, pages 977–1009. **Blocker:** the University of Chicago Press full text is paywalled; no open-access copy was found by legal routes.
- **What it says (abstract):**
  - "Building on models of entry in atomistically competitive markets, the authors show how the number of producers in an oligopolistic market varies with changes in demand and market competition."
  - "Using data on geographically isolated monopolies, duopolies, and oligopolies, they study the relationship between the number of firms in a market, market size, and competition."
  - "The authors' empirical results suggest that competitive conduct changes quickly as the number of incumbents increases."
- **Bears on:**
  - H1 and H5 (supports the general shape): market size determines how many suppliers a market can carry.
  - H1 (supports, by the document's analogy): GlobalFoundries at 7nm is the "second dentist" problem at a $20B scale — the market was large, GF's share of it was not.
- **Used in:** not yet.
- **Caveats:** **the specific trades are unconfirmed.** The document says "one dentist or tyre dealer". The abstract says only "five retail and professional industries" and does not name them. Do not repeat the trade names until the paper is read.

### ECON-10. The division of labour is limited by the extent of the market

- **Source:** George J. Stigler, "The Division of Labor is Limited by the Extent of the Market", *Journal of Political Economy* 59(3), June 1951, pp. 185–193. DOI 10.1086/257075
- **Verification:** **Partial** 2026-09-18 (citation only). Confirmed exactly against Crossref: title, author, *Journal of Political Economy*, volume 59, issue 3, pages 185–193, June 1951. The article was not read (paywalled; no open-access copy found).
- **Bears on:** H5 and H6 (context). It is the oldest form of the document's second rule: specialisation, and so the fixed cost you can justify, is bounded by how big the market is.
- **Used in:** not yet.
- **Caveats:** the title is a quotation of Adam Smith, not Stigler's own coinage. Note that Brynjolfsson, Hu and Smith (ECON-13) render the same Smith line as "the division of labor is limited by the *scope* of the market"; Stigler's title, and Smith's own wording, use "extent".

### ECON-11. When a drug category's potential market grows 1%, non-generic entry grows about 5%

- **Source:** Daron Acemoglu and Joshua Linn, "Market Size in Innovation: Theory and Evidence from the Pharmaceutical Industry", *The Quarterly Journal of Economics* 119(3), August 2004, pp. 1049–1090. DOI 10.1162/0033553041502144. Authors' working-paper full text: <https://conference.nber.org/confer/2004/prs04/acemoglu.pdf>
- **Verification:** **Verified** 2026-09-18. Read the authors' own January 2004 full text in full for the relevant results. Citation confirmed independently against Crossref and IDEAS/RePEc: both give QJE 119(3), 2004, pp. 1049–1090, DOI 10.1162/0033553041502144.
- **What it says:**
  - Abstract: "Focusing on exogenous changes driven by U.S. demographic trends, we find that a 1 percent increase in the potential market size for a drug category leads to approximately a 5 percent increase in the number of new non-generic drugs."
  - Introduction: "a 1 percent increase in the size of the potential market for a drug category leads to a 7-10 percent increase in the total number of new drugs", of which "[m]uch of this response comes from the entry of generics".
  - Results: the estimate for non-generics on current market size "is 5.11, with standard error 2.22"; on five-year leads of market size it "is estimated to be 6.31 with standard error 2.18, which is significant at 1 percent". A specification in a later table gives 8.89 for non-generics, "but less precise (standard error = 4.57)".
  - "Interestingly, while generics respond to current market size, we find that non-generics respond to five-year leads of market size."
  - The published QJE abstract, which differs from the working paper's, says only that the authors "find a large effect of potential market size on the entry of nongeneric drugs and new molecular entities".
- **Bears on:**
  - **H5 (supports, strongly).** This is the best direct evidence in the repository that market size *causes* innovation, rather than merely correlating with it — and it identifies the effect from exogenous demographic change, not from anything the firms chose.
  - H1 (supports): if market size drives innovation, a rising fixed cost narrows what gets invented, not only what gets sold.
- **Used in:** not yet.
- **Caveats:**
  - **The document's "four to six percent" is a fair but not literal rendering.** The paper's own abstract says "approximately a 5 percent increase"; its non-generic point estimates are 5.11 (current market size) and 6.31 (five-year leads). The document's footnote correctly restricts the claim to non-generic drugs. Do not put "four to six percent" in quotation marks and attribute it to the paper.
  - The version read is the January 2004 pre-publication draft, not the QJE typeset text. Wording may differ; the numbers quoted above are the draft's.
  - Pharmaceuticals, not semiconductors. The transfer to chips is our inference.

### ECON-12. Computing is fragmenting into a fast lane of specialised chips and a slow lane of hand-me-downs

- **Source:** Neil C. Thompson and Svenja Spanuth, "The Decline of Computers as a General Purpose Technology", *Communications of the ACM* 64(3), March 2021, pp. 64–72. DOI 10.1145/3430936. Authors' working-paper version (November 2018): <https://ide.mit.edu/sites/default/files/publications/SSRN-id3287769.pdf>
- **Verification:** **Partial** 2026-09-18. The *CACM* citation is confirmed exactly against Crossref: both authors, *Communications of the ACM*, volume 64, issue 3, pages 64–72, print March 2021, DOI 10.1145/3430936. The **working-paper version was read in full**; the *CACM* article itself was not. **Blocker:** cacm.acm.org and dl.acm.org return HTTP 403 to automated fetches, and MIT's DSpace record returns HTTP 405.
- **What it says (2018 working paper, "The Decline of Computers as a General Purpose Technology: Why Deep Learning and the End of Moore's Law are Fragmenting Computing"):**
  - "This paper argues that technological and economic forces are now pushing computing in the opposite direction, making computer processors less general purpose and more specialized."
  - "This trend towards specialization threatens to fragment computing into 'fast lane' applications that get powerful customized chips and 'slow lane' applications that get stuck using general purpose chips whose progress fades."
  - "Applications that do not move to specialized chips will likely do so because they (i) will get little speed-up from them, (ii) do not comprise a sufficient market to justify the upfront fixed costs, or (iii) cannot coordinate their demand."
  - "But perhaps the biggest drawback of specialized processors are their fixed costs. For universal processors, the fixed costs (also called non-recurring engineering costs (NRE)) are distributed over a large number of [chips]."
  - Worked volumes: for a 10× speedup "at least ~167,000 chips are needed to make specialization attractive"; at 2× "it would take ~1,000,000 chips".
- **Bears on:**
  - **H1 (supports).** Rising fixed cost plus modest market growth is exactly the doom spiral, argued from the chip side.
  - **H5 (supports).** The applications that cannot "comprise a sufficient market to justify the upfront fixed costs" *are* the long tail. This is the closest thing the repository has to chip-specific evidence that the tail exists and is unserved.
- **Used in:** not yet.
- **Caveats:**
  - The version read is the 2018 working paper, which is longer and differently titled. Quotations above must not be attributed to the *CACM* article without reading it.
  - The paper's framing is universal-vs-specialised processors, not leading-edge-vs-mature nodes. The document's paraphrase — "only the largest markets can justify a leading-edge design, and everyone else lives on hand-me-downs" — is a reasonable but not literal restatement; Thompson and Spanuth's "left behind" applications are stuck on *general-purpose* chips, which is not quite the same thing as older nodes.

### ECON-13. The tail gets served when the fixed cost per product falls

- **Source:** Erik Brynjolfsson, Yu ("Jeffrey") Hu and Michael D. Smith, "From Niches to Riches: Anatomy of the Long Tail", *MIT Sloan Management Review* 47(4), Summer 2006, pp. 67–71. Authors' deposited full text in Carnegie Mellon's repository, DOI 10.1184/R1/6471422.v1: <https://kilthub.cmu.edu/articles/journal_contribution/From_Niches_to_Riches_The_Anatomy_of_the_Long_Tail/6471422>
- **Verification:** **Verified** 2026-09-18. Read the authors' deposited full text, whose header reads "Forthcoming in Sloan Management Review, Summer 2006, Vol. 47, No. 4, pp. 67-71." Citation cross-checked against the *MIT SMR* article page (Summer 2006, published 2006-07-01) and the MIT SMR / HBR store listings.
- **What it says:**
  - "Supply-Side Drivers: For all brick-and-mortar business, stocking decisions are driven by the [physical shelf]."
  - "Similarly, IT systems can change production costs for products directed at a niche audience."
  - "Books printed using traditional offset printing technologies are only profitable in volumes of 1,000 or more, and not all books have a sufficient readership to justify such a print run. Large print runs also involve the risk associated with the initial printing costs for a title with unknown demand. Using print-on-demand technologies, authors and small publishers can print individual titles for around $3.00 per copy."
  - "Managers should understand that the underlying economic principles are not new. Over 200 years ago, Adam Smith observed that 'the division of labor is limited by the scope of the market' because of the need to amortize fixed costs. What has changed is the technology and thus, both the size of the addressable market and the relevant fixed costs of production and distribution."
- **Bears on:**
  - **H5 (supports, strongly).** This is H5's mechanism stated by the people who measured the long tail: the tail is served when the fixed cost per product falls far enough that a small addressable market covers it. The minimum-economic-print-run figure (1,000 copies for offset) is the exact analogue of a mask set.
  - H4 and H6 (supports by analogy): print-on-demand at $3.00 a copy is a multi-project wafer.
- **Used in:** not yet.
- **Caveats:**
  - The repository already holds the same authors' 2003 paper as TAIL-2. This is a different, later, practitioner-facing article. Keep them distinct.
  - The version read is the authors' manuscript, not the *MIT SMR* typeset pages; the header states the forthcoming pagination rather than showing it.
  - TAIL-3 (Elberse) is the standing challenge to the long-tail literature and applies here too.

---

## 3. Is the size distribution of markets really a power law?

The document's headline second rule — "every zero added to the price of a bet removes about a zero from
the number of problems that could pay for it on their own" — rests on markets being Zipf-distributed.
**Its own footnote 11 says this is an inference, not a measurement:** "That markets follow it is an
inference from firms and cities, not a measurement; real distributions bend at both ends". The
following four entries are what that inference rests on, and how it would be tested.

### ECON-14. Power laws, Pareto distributions and Zipf's law: the standard survey

- **Source:** M. E. J. Newman, "Power laws, Pareto distributions and Zipf's law", *Contemporary Physics* 46(5), September 2005, pp. 323–351. DOI 10.1080/00107510500052444. Author's copy: <https://arxiv.org/abs/cond-mat/0412004>
- **Verification:** **Partial** 2026-09-18 (abstract only). Read the author-posted arXiv record, whose own journal reference reads "Contemporary Physics 46, 323-351 (2005)" with DOI 10.1080/00107510500052444; cross-checked against Crossref, which adds issue 5. The full survey was not read.
- **What it says (abstract):** "When the probability of measuring a particular value of some quantity varies inversely as a power of that value, the quantity is said to follow a power law, also known variously as Zipf's law or the Pareto distribution. Power laws appear widely in physics, biology, earth and planetary sciences, economics and finance, computer science, demography and the social sciences."
- **Bears on:** H5 and H10 (context: the shape of a skewed world).
- **Used in:** not yet.
- **Caveats:** a survey. It documents where power laws appear; it does not establish that market sizes are one of those places.

### ECON-15. US firm sizes are Zipf-distributed, with an exponent of essentially one

- **Source:** Robert L. Axtell, "Zipf Distribution of U.S. Firm Sizes", *Science* 293(5536), 2001-09-07, pp. 1818–1820. DOI 10.1126/science.1062081. Author's preprint: <https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/USFirmSizesAreZipfDistributed.RAxtell2001.pdf>
- **Verification:** **Verified** 2026-09-18. Read the author's own February 2001 preprint of the paper. Citation cross-checked against Crossref (*Science* 293, issue 5536, pp. 1818–1820, 2001-09-07) and the PubMed record (PMID 11546870).
- **What it says (preprint):**
  - "Utilizing data on the entire population of U.S. firms, including small businesses, we find that the Pareto distribution well describes the entire firm size distribution. Furthermore, the exponent of this distribution is essentially unity, thus we have the special case of the Zipf distribution."
  - "These results are shown to be robust to alternative definitions of firm size."
  - "The stability of this distribution over time makes it, along with the distribution of city sizes, perhaps the most robust statistical regularity in all the social sciences."
- **Bears on:** H5 (context, and partial support for the *shape* of the document's second rule): if the units are Zipf-distributed, the count of units above size S falls as 1/S, which is the document's rule.
- **Used in:** not yet.
- **Caveats:**
  - **This is about firms, not markets.** It is the strongest leg of the document's inference, and it is still an inference.
  - The preprint is titled "U.S. Firm Sizes are Zipf Distributed" and marked "Submitted to Nature"; the published version is the *Science* article above. Later work (for example a 2021 US Census Bureau working paper, "Heavy Tailed, but not Zipf") disputes the exponent. That dispute has not been checked here, but it should be before the Zipf claim is used hard.

### ECON-16. Zipf's law for cities

- **Source:** Xavier Gabaix, "Zipf's Law for Cities: An Explanation", *The Quarterly Journal of Economics* 114(3), August 1999, pp. 739–767. DOI 10.1162/003355399556133
- **Verification:** **Partial** 2026-09-18 (citation only). Confirmed exactly against Crossref: author, title, *The Quarterly Journal of Economics*, volume 114, issue 3, pages 739–767, 1999-08-01. Not read.
- **Bears on:** H5 (context). The second leg of the document's inference: cities as well as firms.
- **Used in:** not yet.
- **Caveats:** the document's short title omits the subtitle "An Explanation". Cite it in full.

### ECON-17. How to test whether something actually is a power law

- **Source:** Aaron Clauset, Cosma Rohilla Shalizi and M. E. J. Newman, "Power-Law Distributions in Empirical Data", *SIAM Review* 51(4), November 2009, pp. 661–703. DOI 10.1137/070710111. Authors' copy: <https://arxiv.org/abs/0706.1062>
- **Verification:** **Partial** 2026-09-18 (abstract only). Read the author-posted arXiv record, whose journal reference reads "SIAM Review 51, 661-703 (2009)" with DOI 10.1137/070710111; cross-checked against Crossref, which adds issue 4. The 43-page methods paper itself was not read.
- **What it says (abstract):**
  - "Commonly used methods for analyzing power-law data, such as least-squares fitting, can produce substantially inaccurate estimates of parameters for power-law distributions, and even in cases where such methods return accurate answers they are still unsatisfactory because they give no indication of whether the data obey a power law at all."
  - "Here we present a principled statistical framework for discerning and quantifying power-law behavior in empirical data. Our approach combines maximum-likelihood fitting methods with goodness-of-fit tests based on the Kolmogorov-Smirnov statistic and likelihood ratios."
  - "We also apply the proposed methods to twenty-four real-world data sets from a range of different disciplines, each of which has been conjectured to follow a power-law distribution. In some cases we find these conjectures to be consistent with the data while in others the power law is ruled out."
- **Bears on:** **H5 (challenges, methodologically).** This is the entry that stops the repository from hardening the document's Zipf rule of thumb into a law. Clauset, Shalizi and Newman's own finding is that many published power-law claims do not survive a proper test.
- **Used in:** not yet.
- **Caveats:** it is a method, not a finding about markets. Nobody, so far as we have checked, has applied it to the size distribution of *markets for engineered products* — which is precisely the gap.

---

## 4. Why the loop closes

### ECON-18. Where firms can buy share by spending more on fixed costs, competition raises the fixed cost

- **Source:** John Sutton, *Sunk Costs and Market Structure: Price Competition, Advertising, and the Evolution of Concentration*, MIT Press, 1991.
- **Verification:** **Partial** 2026-09-18 (citation only). Confirmed in library catalogue records: John Sutton, MIT Press, 1991. Not read.
- **What it says (per the document, unverified):** in industries where firms can win share by spending more on endogenous fixed costs, competition bids the fixed cost up, and concentration does **not** fall as the market grows.
- **Bears on:** **H1 (supports, and is the missing theoretical spine for it).** The doom spiral as `WHY.md` states it is exactly an endogenous-sunk-cost argument, and Sutton is where that argument is formalised. This is the single most valuable unread item in this file.
- **Used in:** not yet.
- **Caveats:** unread. The summary above is the document's, not ours. Sutton's empirical work is on food and consumer-goods industries; the application to semiconductors is the document's inference.

### ECON-19. Whether a bigger buyer makes a supplier invest more or less is theoretically ambiguous

- **Source:** Roman Inderst and Christian Wey, "Buyer power and supplier incentives", *European Economic Review* 51(3), April 2007, pp. 647–667. DOI 10.1016/j.euroecorev.2006.02.002
- **Verification:** **Partial** 2026-09-18 (citation only). Confirmed exactly against Crossref: both authors, title, *European Economic Review*, volume 51, issue 3, pages 647–667, April 2007. Not read.
- **Bears on:** **H2 and H7 (challenges, or at least complicates).** The document cites it against its own thesis: buyer power does not unambiguously reduce a supplier's incentive to invest. A repository that only records the supporting half of this literature is not doing its job.
- **Used in:** not yet.
- **Caveats:**
  - This is a **different paper** from the Inderst and Wey (2003) *RAND Journal of Economics* article already listed as a Lead under FIN-7. Do not merge them.
  - Unread.

---

## 5. Cases

### ECON-20. Cirrus Logic earns 89–91% of revenue from Apple and is highly profitable

- **Source:** Cirrus Logic, Inc., Annual Report on Form 10-K for the fiscal year ended 2025-03-29, filed 2025-05-23: <https://www.sec.gov/Archives/edgar/data/772406/000077240625000014/crus-20250329.htm>; and for the fiscal year ended 2026-03-28, filed 2026-05-21: <https://www.sec.gov/Archives/edgar/data/772406/000077240626000018/crus-20260328.htm>. Financial figures from the SEC's XBRL company facts API for CIK 0000772406.
- **Verification:** **Verified** 2026-09-18 from the filings' own text and from SEC XBRL data.
- **What it says:**
  - FY2025 10-K: "For the twelve-month periods ending March 29, 2025, March 30, 2024, and March 25, 2023, we had one end customer, Apple Inc., who purchased through multiple contract manufacturers and represented approximately 89 percent, 87 percent and 83 percent of the Company's total net sales, respectively."
  - FY2026 10-K: "For the twelve-month periods ending March 28, 2026, March 29, 2025, and March 30, 2024, we had one end customer, Apple Inc., who purchased through multiple contract manufacturers and represented approximately 91 percent, 89 percent and 87 percent of the Company's total net sales, respectively."
  - Reported results (XBRL, US-GAAP `RevenueFromContractWithCustomerExcludingAssessedTax` and `NetIncomeLoss`, annual periods from 10-K filings):

    | Fiscal year ended | Net sales | Net income | Net margin (`DERIVED`) |
    |---|---|---|---|
    | 2023-03-25 | $1,897.6M | $176.7M | 9.3% |
    | 2024-03-30 | $1,788.9M | $274.6M | 15.3% |
    | 2025-03-29 | $1,896.1M | $331.5M | 17.5% |
    | 2026-03-28 | $1,997.4M | $414.4M | 20.7% |

    `DERIVED`: net margin = net income ÷ net sales. 331.507 ÷ 1896.077 = 0.1749; 414.408 ÷ 1997.379 = 0.2075.
  - Concentration has *risen* every year (83% → 87% → 89% → 91%) while net income has risen every year and net margin has more than doubled.
- **Bears on:**
  - **H2 (challenges, directly and seriously).** H2 says big customers push margins down and make the supplier fragile. Here is a supplier at the theoretical extreme of concentration — one end customer, over nine-tenths of sales — whose margins are expanding, not contracting, and which has been profitable in every year on record.
  - **H7 (challenges).** If a 91%-concentrated supplier can be this profitable for this long, "many small customers" is not a necessary condition for a good business. It may be a condition for a *durable* one, but that is a different claim and needs different evidence.
  - H2 (supports, partially): the risk has not gone away, it has only not been realised. Cirrus Logic's own 10-K files this under risk factors, not under achievements, and Imagination Technologies (CONC-6) is what the tail of this distribution looks like.
- **Used in:** not yet. **It should be**, as a stated counter-example, not a footnote.
- **Caveats:**
  - Cirrus Logic is a fabless designer of mixed-signal and audio chips, not a foundry. It carries no fab capex, so the fixed-cost side of H1 and the cost-of-capital mechanism of FIN-2 and FIN-3 bite far less hard.
  - The figures show realised profit, not risk. FIN-2's claim is about the *cost of capital*, which is a price on variance; a firm can pay a higher discount rate and still report excellent earnings. Nothing here contradicts FIN-2. What it contradicts is the looser claim that concentration means poor margins.
  - "For more than a decade" (the document's phrase) is **not verified here**; only FY2023–FY2026 percentages were read. Earlier years were not checked.
  - The relationship is not symmetric: Apple has many suppliers, Cirrus Logic has one customer. That is the Nash point (ECON-4) in its purest form, and the outcome so far has still been good for Cirrus Logic.

### ECON-21. TSMC lost Huawei to an export ban and was not materially affected

- **Source:** Taiwan Semiconductor Manufacturing Company, Annual Report on Form 20-F for 2020, filed 2021-04-16: <https://www.sec.gov/Archives/edgar/data/1046179/000119312521118512/d94821d20f.htm>
- **Verification:** **Verified** 2026-09-18 from the filing's own text.
- **What it says:**
  - "In May 2020 and again in August 2020, the U.S. tightened its export control measures against Huawei Technology Co. Ltd. and its affiliates (collectively, 'Huawei'), including an expanded license requirement for providing Huawei with items subject to the U.S. export control jurisdiction. To comply with relevant laws and regulations, we have discontinued shipment of products to Huawei since September 15, 2020."
  - "As of the date of this annual report, our current results of operations have not been materially affected by the expanded export control regulations or the novel rules or measures adopted to counteract them."
  - "Our ten largest customers in 2018, 2019 and 2020 accounted for approximately 68%, 71% and 74% of our net revenue in the respective year. Our largest customer in 2018, 2019 and 2020 accounted for 22%, 23% and 25% of our net revenue in the respective year."
- **Bears on:**
  - H2 (mixed, and this is the honest reading). The second-largest customer of the world's largest foundry disappeared by government order, and the filing says the results were not materially affected. That is a real challenge to "losing a big customer is catastrophic". But the 2020–21 chip shortage refilled the capacity almost at once, which is luck, not structure.
  - H2 (supports): a customer can be removed by a third party the supplier has no relationship with. Concentration is exposure to other people's politics.
- **Used in:** not yet. This **verifies CONC-13**, which is currently a Lead.
- **Caveats:**
  - Huawei's share of TSMC's 2019 revenue (usually given as about 14%) is **not** in the filing. It is an analyst estimate. The 20-F never names Huawei as a customer or gives its share. The document says so; keep saying so.
  - "Not materially affected" is a statement about the period to the filing date, made by the company, in a risk-factor context.

### ECON-22. Imagination Technologies was sold for £550 million seven months after Apple left

- **Source:** Canyon Bridge Capital Partners, "Canyon Bridge Capital Partners completes the £550m acquisition of Imagination Technologies Group", press release, 2017-11-03: <https://canyonbridge.com/news-and-insights/canyon-bridge-capital-partners-completes-550m-acquisition-imagination-technologies-group/>
- **Verification:** **Verified** 2026-09-18 from the acquirer's own press release.
- **What it says:**
  - "Canyon Bridge paid 182 pence in cash for each Imagination share, valuing Imagination at approximately £550 million."
  - "Imagination shares delisted from the London Stock Exchange at 8.00 am on 3 November 2017."
- **Bears on:** H2 (supports). The full arc: Apple's announcement on 2017-04-03 (CONC-6), sale completed 2017-11-03.
- **Used in:** not yet. This is the second half of CONC-6, which stops at the share-price fall.
- **Caveats:**
  - The document cites a *Financial Times* article of 2017-11-04 for the £550 million figure. **The FT article was not read** (paywalled). The figure is verified instead from the acquirer's own release of 2017-11-03, which is a better source for it.
  - The document's BBC citation of 2017-04-03 was also not read (bbc.com is not fetchable from this environment), but the underlying facts are already Verified under CONC-6 from CNBC.

### ECON-23. Roman Britain: what happens to an economy with one paymaster

- **Sources:**
  - Bryan Ward-Perkins, *The Fall of Rome and the End of Civilization*, Oxford University Press, 2005.
  - A. S. Esmonde Cleary, *The Ending of Roman Britain*, Batsford, 1989.
- **Verification:** **Partial** 2026-09-18 (citations only). Both confirmed in library catalogue records: Ward-Perkins, OUP, 2005; A. S. Esmonde Cleary, Batsford, 1989 (later reissued by Routledge). Neither book was read.
- **What the document claims:** when imperial coin stopped arriving in the early 400s, the wheel-thrown pottery industry ceased and the towns emptied within two generations, without anyone having been dissatisfied with the potters.
- **Bears on:** H2 (context, by historical analogy).
- **Used in:** not yet.
- **Caveats:**
  - **The document flags its own dispute, and it is a real one.** Its footnote 8 says: "Historians disagree about how sudden and how bad the collapse was, and about which way causation ran; the 'transformation' school reads the same pottery evidence as changing tastes rather than impoverishment."
  - This is an illustration, not evidence. It should not be cited in `WHY.md` as support for anything.

### ECON-24. The *Great Eastern*: a bet whose market never arrived

- **Source:** Royal Museums Greenwich, "Great Eastern": <https://www.rmg.co.uk/stories/maritime-history/great-eastern>
- **Verification:** **Verified** 2026-09-18 for the claims RMG covers; the Science Museum page the document also cites was not reached.
- **What it says:**
  - "Work started in 1854 and, despite many problems, she was finally afloat in January 1858."
  - "At the time of the *Great Eastern*'s launch she was the largest ship in the world."
  - She was designed for "a voyage to India or Australia without stopping at coaling stations on the way", but "the *Great Eastern* was used to cross the Atlantic to America, a much shorter voyage".
  - "In 1864, she was sold for a fraction of her cost to a cable laying company."
  - "She was used to lay the first telegraph cable to America, and finally broken up in 1888."
- **Bears on:** H10 (context) and H5 (context): a fixed-cost bet sized for a market that did not exist, which was eventually repaid by a use nobody designed it for.
- **Used in:** not yet.
- **Caveats:**
  - **Three of the document's specifics are not in this source** and are unverified: "four thousand passengers", "roughly six times the size of anything afloat", and that she "bankrupted her builder and then her owners". RMG says only that she was the largest ship in the world and was sold in 1864 for a fraction of her cost.
  - See the analysis file: the document's own footnote 16 contradicts its main text on the builder.

### ECON-25. Iridium: $5 billion of satellites, a market that was not there, and a second life at a hundredth of the price

- **Sources:**
  - Craig Mellow, "The Rise and Fall and Rise of Iridium", *Air & Space / Smithsonian*, September 2004.
  - John Bloom, *Eccentric Orbits: The Iridium Story*, Grove Atlantic, 2016.
- **Verification:** **Partial** 2026-09-18. Bloom's book is confirmed in library catalogue records (John Bloom, 2016, Atlantic Monthly Press / Grove Atlantic). The Mellow article is confirmed to exist with that exact title, byline and September 2004 date. **Blocker:** smithsonianmag.com returns HTTP 403 to automated fetches and web.archive.org is not fetchable from this environment, so the article was not read and **none of the figures the document attributes to it were checked**.
- **What the document claims (unverified):** a $5 billion constellation of 66 satellites; a million subscribers needed; tens of thousands found (its footnote says 60,000); service began 1998-11-01; Chapter 11 on 1999-08-13; assets bought for about $25 million in December 2000; the US Department of Defense is the largest single customer today.
- **Bears on:** H10 (context), H5 (context), H11 (context: a government anchor customer rescuing a private bet).
- **Used in:** not yet. **Do not cite any of the numbers above until the article or another primary source is read.**
- **Caveats:** the document is unusually careful here — its footnote says the constellation was replaced in 2017–19, that the company has had loss-making years since, and that "'operated' is the claim, not 'profitable'". That carefulness is a point in the document's favour; it does not substitute for checking.

### ECON-26. What a customer big enough to fund the bet asks for in return

- **Sources:**
  - Apple's October 2018 agreement with Dialog Semiconductor: widely reported at $600 million, $300 million in cash plus $300 million prepaid for products over three years, with about 300 Dialog R&D staff and certain power-management assets transferring to Apple.
  - ASML's 2012 Customer Co-Investment Program: Intel, TSMC and Samsung together funded EUV research and took an aggregate 23% minority equity stake for €3.85 billion in cash, with an aggregate R&D funding commitment target of €1.38 billion. ASML's own press releases: <https://www.asml.com/en/news/press-releases/2012/samsung-joins-asmls-customer-co-investment-program-for-innovation-completing-the-program>
- **Verification:** **Partial** 2026-09-18. Both events are corroborated by multiple independent contemporaneous reports and, for ASML, by the titles and summaries of ASML's own press releases and its 2012 Form 6-K filings on EDGAR. **Blocker:** Apple's newsroom URL for the Dialog announcement returns HTTP 404, and the ASML release pages were read only in summary; neither primary announcement was read in full.
- **Bears on:**
  - H2 (supports): when a dominant customer is finished with a supplier, it can buy the engineers rather than merely leave (Dialog).
  - **H7 and H11 (mixed, and interesting).** ASML is the counter-case the document itself raises: three customers funded the bet and received *equity*, not exclusivity. A supplier that cannot be replaced is not squeezed. That is an argument that irreplaceability, not customer count, is what protects a supplier — which cuts against H7's mechanism even while agreeing with its conclusion.
- **Used in:** not yet.
- **Caveats:** the ASML shares issued to the three customers were non-voting except in defined circumstances, and the arrangement was approved by shareholders. Do not describe it as customers "owning" ASML.
