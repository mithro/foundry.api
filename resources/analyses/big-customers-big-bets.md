# Assessment: "Big Customers, Big Bets"

| | |
|---|---|
| Item | "Big Customers, Big Bets: Two pieces of arithmetic, simple enough for a ten-year-old, that decide which problems get solved" |
| Where | Six-page PDF, PDF creation date 2026-09-07, publicly downloadable: <https://drive.google.com/uc?export=download&id=1ISBL0SPcdAVNZsmLbmYx3aGcflmCmNNY> |
| Kind | An explainer, not a research paper. Written for a general reader, with twenty-four endnotes on pages 5–6 carrying the apparatus. |
| Read | 2026-09-18. Downloaded and the text extracted with `pypdf`. |
| Assessed by | Claude, for foundry.api |
| Reference entries harvested | [`../references/economics-of-concentration.md`](../references/economics-of-concentration.md), ECON-1 to ECON-26 |

## What it argues

Two arithmetic rules, and the circle they make together.

**Rule 1, the problem with big customers.** A supplier's exposure is not the *number* of its customers
but the sum of the squares of their shares — the Herfindahl index. Its reciprocal is the **effective
number of customers**. Ten equal customers give ten; one customer at 90% of sales plus nine at about 1%
gives 1.2. Squaring is what makes big shares count more than their size. Concentration then costs the
supplier in four ways: catastrophic loss when a big customer goes (for reasons that need have nothing
to do with the supplier); a bargaining squeeze set by fallbacks rather than fairness (Nash, Rubinstein);
hold-up once the supplier sinks capital specific to the relationship (Klein/Crawford/Alchian,
Williamson); and the cost of idle capacity that lumpy demand forces (Kingman), plus a measurably higher
cost of capital (Dhaliwal et al., Hertzel et al.).

**Rule 2, the problem with big bets.** A fixed cost paid before the first unit — NRE — needs a market
big enough to repay it. The child's invitation example: hand-writing at $1 each, a $20 stamp at 10¢
each, a $2,000 press at 1¢ each; break-even at about 20 and about 2,000 cards. "Two extra zeros on the
price of the tool; two extra zeros on the size of the party needed to justify it." Then the claim that
does the work: **if market sizes are Zipf-distributed, every zero added to the price of a bet removes
about a zero from the number of markets that could pay for it alone.** Hence the biggest bets must be
the most *general* ones, and a rising NRE quietly deletes problems from the list anyone will try to
solve (Acemoglu & Linn; Thompson & Spanuth; Brynjolfsson/Hu/Smith).

**Section 3, the circle.** Big bets mean few customers can pay, so big-bet makers get big customers
(rule 2 makes rule 1). Big customers, being few, want the biggest markets and lowest costs, so the
supplier optimises for that end and outspends rivals on the next bet (rule 1 makes rule 2). What slows
the loop is outside it: markets growing faster than bets, and the escape — one customer pays for the
bet and everyone reuses it, which is the foundry model, and which "only works for a supplier that has
already survived the first rule."

This is, almost exactly, `WHY.md`'s doom spiral (H1) with the arithmetic shown and a second, quantified
rule bolted on. The parts the repository does not yet have are the effective-customer-count tool, the
Sutton endogenous-sunk-cost spine under H1, and the market-size-causes-innovation evidence under H5.

## Are its references trustworthy?

**Yes — this is the most citation-accurate outside document the repository has assessed.** Nineteen
DOIs were resolved against the Crossref API. **Every single one resolves to exactly the work cited,
with the author names, title, journal, volume, issue, year and page range all matching what the
document prints.** Book citations (Williamson 1985, Sutton 1991, Ward-Perkins 2005, Esmonde Cleary
1989, Bloom 2016, Hopp & Spearman) all check out against library catalogue records. Its two SEC
citations (TSMC's 2020 20-F, Cirrus Logic's FY2025 10-K) quote their filings correctly. Its £550
million Imagination figure is confirmed from the acquirer's own press release.

The document is also unusually honest about its own weak points. It flags the Zipf claim as an
inference rather than a measurement *and names the right method for testing it* (Clauset, Shalizi &
Newman). It flags the Roman Britain "transformation" school against its own reading. It flags that
Huawei's 14% share is an analyst estimate, not a TSMC disclosure. It states a counter-example to its
own thesis (Cirrus Logic) in the same footnote as the supporting evidence, and it cites Inderst & Wey
(2007) for the proposition that its own mechanism is theoretically ambiguous. It says "'operated' is
the claim, not 'profitable'" about Iridium. The earlier "Tyranny of the Whale" assessment found two
citation errors; the equivalent search here found none.

### What is wrong, or shaky

Nothing rises to a wrong citation. Six things are worth recording.

1. **An internal contradiction about the *Great Eastern*'s builder.** The main text (page 4) says "She
   bankrupted her builder and then her owners." Endnote 16 says "Her builder, John Scott Russell,
   failed in 1856, before she was launched". A ship launched in 1858 cannot have bankrupted a man who
   failed in 1856. The endnote is right and the main text is loose. Do not repeat the main-text form.
2. **Unsourced specifics about the *Great Eastern*.** "Four thousand passengers" and "roughly six times
   the size of anything afloat" are not in the Royal Museums Greenwich page the document cites, which
   says only that she was the largest ship in the world at launch (ECON-24).
3. **Acemoglu & Linn's elasticity is paraphrased, not quoted.** The document says "four to six
   percent". The paper's own abstract says "approximately a 5 percent increase"; its non-generic point
   estimates are 5.11 on current market size and 6.31 on five-year leads, with one less precise
   specification at 8.89 (ECON-11). The document's range is defensible and its footnote correctly
   restricts the claim to non-generic drugs — but the range is the document's, not the paper's.
4. **Bresnahan & Reiss's trades are unconfirmed.** "One dentist or tyre dealer" is not in the abstract,
   which says only "five retail and professional industries". Plausible, unchecked (ECON-9).
5. **The Thompson & Spanuth paraphrase shifts the axis.** The document has them saying "only the
   largest markets can justify a leading-edge design, and everyone else lives on hand-me-downs". Their
   argument is about *specialised versus general-purpose* processors; the applications left behind are
   stuck on general-purpose chips, which is not the same as being stuck on older nodes (ECON-12).
6. **Rubinstein's page range.** The document gives 97–109, matching JSTOR and RePEc. The Econometric
   Society's own page says 97–110. Not the document's error; noted so nobody "corrects" it.

One thing in the document is **more accurate than what the repository currently holds**: its DOI for
Dhaliwal et al. (2016) is `10.1016/j.jacceco.2015.03.005`, which resolves correctly. FIN-2's DOI is
wrong. See the last section.

## Cross-check against what we have verified

| Claim in the document | Our status | Reference |
|---|---|---|
| Herfindahl reciprocal is the "effective number of customers"; ten equal customers give ten, one at 90% plus nine at 1% gives 1.2 | **Verified** arithmetic (`DERIVED`). 1/(10×0.1²) = 10.00; 1/(0.9² + 9×0.01²) = 1.2332, which rounds to 1.2 | ECON-3 |
| Endnote 2: "Ten new 1-percent customers move the effective count from 1.2 to about 1.5" | **Verified** arithmetic (`DERIVED`). Ten new customers each at 1% of the enlarged total dilute the whale from 90% to 81%: H = 0.81² + 19×0.01² = 0.6580, so 1/H = 1.52 | ECON-3 |
| Fat tails stop shocks averaging out; volatility scales with the square root of the Herfindahl | **Verified** from Gabaix's own text: σ_GDP = σ·h, h = [Σ(S/Y)²]^½ | ECON-1 |
| Bargaining splits are set by each side's fallback (Nash 1950) | **Verified** from the article: the no-cooperation anticipation is normalised to zero | ECON-4 |
| The more patient side gets more, and agreement is immediate (Rubinstein 1982) | **Partial** — abstract only; the author's PDF is an untexted scan | ECON-5 |
| Hold-up: sinking capital specific to one customer weakens your position | **Lead**, already held | FIN-8, ECON-6 |
| Kingman: uneven demand must be paid for in idle capacity | **Partial** — citation exact, text unread (Cambridge Core returned HTTP 500) | ECON-7 |
| Concentrated suppliers pay more for capital | **Verified** (abstract) | FIN-2, FIN-3 |
| Suppliers lose value when a major customer nears bankruptcy (Hertzel et al.) | **Partial** — abstract read, citation confirmed twice | ECON-8 |
| Patatoukas (2012) finds efficiency gains from concentration | **Partial**; owner decided 2026-09-14 not to pursue | FIN-5 |
| **Cirrus Logic earned 89% of revenue from Apple in fiscal 2025 and has prospered** | **Verified** from the 10-K, and it is now 91% in FY2026, with net margin up from 9.3% to 20.7% over four years | **ECON-20** |
| Imagination: more than half its revenue from Apple, shares fell about 70% in April 2017 | **Verified** (71%, "about half of its revenues") | CONC-6 |
| Imagination sold for £550 million before the year was out | **Verified** from Canyon Bridge's own release: completed 2017-11-03 at 182p a share | ECON-22 |
| TSMC "discontinued shipment of products to Huawei since September 15, 2020"; largest customer 25%; results not materially affected | **Verified** from the 2020 20-F, all three | ECON-21 |
| Huawei was roughly a seventh of TSMC's 2019 sales | **Lead**, and the document itself says it is an analyst estimate, not a disclosure | CONC-13 |
| TSMC's effective customer count is "about a dozen" | **Verified** and reproduced: 11.77 (`DERIVED`, below) | ECON-3, CONC-1, CONC-2 |
| TSMC 2024: largest 22%, second 12%, top ten 76% | **Verified**, matches the 20-F exactly | CONC-1 |
| The top-ten figure has been rising for several years | **Verified**: 68% (2022), 70% (2023), 76% (2024), 78% (2025) | CONC-1, CONC-11 |
| Market sizes follow Zipf's law | **The document's own footnote says this is an inference, not a measurement.** Firms (Axtell) and cities (Gabaix) are Verified/confirmed; markets are not measured by anyone we have found | ECON-14 to ECON-17 |
| US firm sizes are Zipf-distributed with exponent essentially one | **Verified** from Axtell's own preprint. Caveat: later work disputes the exponent | ECON-15 |
| The honest way to test a power law is Clauset, Shalizi & Newman | **Partial** (abstract), and it supports the document's caution: many published power-law claims fail a proper test | ECON-17 |
| Bresnahan & Reiss: a town must reach a size for one firm, a larger size for two | **Partial** — abstract confirms market size and firm count; the named trades do not appear in it | ECON-9 |
| Acemoglu & Linn: 1% more potential market, 4–6% more new drugs (non-generic) | **Verified** as to substance; the paper says "approximately a 5 percent increase", with estimates of 5.11 and 6.31 | ECON-11 |
| Thompson & Spanuth: only the largest markets justify a leading-edge design | **Partial** — the 2018 working paper was read in full and supports the mechanism; the *CACM* 2021 text is blocked (HTTP 403) | ECON-12 |
| "The tail gets served when the fixed cost per product falls" | **Verified** from the authors' own text: "What has changed is the technology and thus, both the size of the addressable market and the relevant fixed costs of production and distribution" | ECON-13 |
| GlobalFoundries stopped 7nm on 2018-08-27 because most customers had no plans for it | **Verified** | COST-4 |
| AMD's freedom at 7nm was formalised in the Seventh Amendment, filed 2019 | **Verified**, and the 2019 date is right — the earlier brief had this wrong as 2018 | CONC-8 |
| Design cost about $249M at 7nm and $725M at 2nm (IBS, via Arm's F-1) | **Verified**, and the document repeats Arm's wording and flags the estimate as disputed | COST-1 |
| Eighteen companies at the leading edge in 2001; three by 2021 | **Lead**. The repository's verified figure is "more than two dozen at 180nm in 1998" from a different source; the "18 at 130nm in 2001" figure is the same Semiconductor Engineering piece already recorded as a Lead under COST-3 | COST-3 |
| A leading-edge fab costs about $20 billion | **Verified** as a figure in circulation | COST-3 |
| Sutton: competition raises the fixed cost and concentration does not fall as the market grows | **Partial** (citation only). Unread, and it is the most valuable unread item here | ECON-18 |
| Inderst & Wey (2007): the effect of buyer power on supplier investment is ambiguous | **Partial** (citation only). Note this is a *different* paper from the Inderst & Wey (2003) already in FIN-7 | ECON-19 |
| Apple paid $600M for part of Dialog's business and about 300 staff, October 2018 | **Partial** — multiple contemporaneous reports agree; Apple's own newsroom URL is dead | ECON-26 |
| ASML's three customers funded EUV and received shares, not exclusivity | **Partial** — corroborated by ASML's own press-release titles and 2012 6-K filings | ECON-26 |
| Roman Britain: coin stopped, pottery industry ceased, towns emptied | **Partial** (citations only; books unread). The document flags the historiographical dispute itself | ECON-23 |
| *Great Eastern*: launched 1858, sold 1864 for a fraction of her cost, laid the first transatlantic cable | **Verified** from Royal Museums Greenwich | ECON-24 |
| *Great Eastern*: four thousand passengers, six times the size of anything afloat, bankrupted her builder | **Unverified**, and the last one is contradicted by the document's own endnote | ECON-24 |
| Iridium: $5B, 66 satellites, a million subscribers needed, 60,000 found, bought for $25M in 2000 | **Lead**. The Smithsonian article is blocked (HTTP 403) and none of these figures were checked | ECON-25 |
| Multi-project wafers as the small-market version of the shared bet | **Verified** as a practice | OPEN-1, OPEN-5 |

## The effective number of customers: does the arithmetic reproduce?

This is the document's most immediately usable contribution, and the repository does not currently have
it. The index is `H = Σ sᵢ²` over customers' revenue shares; the **effective number of customers** is
`1/H`. It answers "how many customers do you *really* have?" in one number, and it is the number the
variance identity in Gabaix (ECON-1) actually depends on.

Endnote 10 computes TSMC's from the 2024 filing: "a largest customer at 22 percent, a second at 12, and
a top ten at 76 percent gives one over the sum of squares of roughly twelve."

**`DERIVED`.** Inputs are all Verified figures the repository already holds: largest customer 22%,
second 12%, top ten 76% (CONC-1, TSMC's 2024 Form 20-F); 522 customers in total (CONC-2, TSMC's *2024
Business Overview*). The filing gives no shares for customers 3–10 or for the tail, so the calculation
must assume something; the natural assumption, and the one that reproduces the document's number, is
that each block is evenly split.

```
customers 3-10   = 76% - 22% - 12%  = 42%, over 8 customers = 5.25% each
tail             = 100% - 76%       = 24%, over 512 customers = 0.0469% each

H = 0.22²  +  0.12²  +  8 x 0.0525²  +  512 x 0.000469²
  = 0.048400 + 0.014400 + 0.022050 + 0.000113
  = 0.084962

1/H = 11.77
```

**It reproduces.** 11.77 is "roughly twelve". Note where the risk sits: the largest customer alone
contributes 0.0484 of the 0.0850 — **57% of the whole index** — while all 512 tail customers together
contribute 0.000113, or 0.13%. That is the document's point about squaring, in TSMC's own numbers.

It is also robust. Varying the assumptions:

| Assumption | 1/H |
|---|---|
| Base case above | **11.77** |
| Tail ignored entirely (top ten only) | 11.79 |
| Customers 3–10 unequal (3rd at 10%, 4th–10th share the rest) | 11.42 |
| 2025 figures (CONC-11: largest 19%, second 17%, top ten 78%, 524 customers) | 11.48 |
| **Whole tail treated as one correlated customer** | **7.02** |

The document's two illustrative figures also check out exactly: ten equal customers give 10.00, a 90%
whale with nine 1% customers gives 1.2332, and endnote 2's claim that ten new 1-percent customers move
the count "from 1.2 to about 1.5" gives 1.52 once the new customers are treated as *adding* to total
sales and so diluting the whale from 90% to 81%.

The first four rows all land between 11.4 and 11.8, so the answer does not depend on the guesses. The last
row is the one that matters for us: if the 512 small customers are not independent — if they rise and
fall together with one end market, as the document warns ("customers who are all paid by the same
paymaster, or all sell into the same market, count as one customer however many names are on the list")
— the effective count drops by a third. **For foundry.api that is the load-bearing caveat on H7.** A
thousand small customers who are all building the same kind of thing for the same cycle are not a
thousand customers.

Caveats on the tool itself:
- It is only as good as the disclosure. TSMC publishes three numbers; everything between them is a
  guess. State the assumption whenever the figure is used.
- It measures *revenue* concentration. It says nothing about which customers are hard to replace, which
  the ASML case (ECON-26) suggests may matter more.
- Attribute the index to the industrial-organisation literature, not to Hirschman's 1964 note, which we
  have not read (ECON-3).

## How it bears on our hypotheses

**H1, the doom spiral.** This is the document's strongest contribution after the index. It supplies the
mechanism `WHY.md` argues by assertion: **Sutton's endogenous sunk costs** (ECON-18). If firms can buy
market share by spending more on fixed costs, competition bids the fixed cost up and concentration does
*not* fall as the market grows. That is the doom spiral as a result in industrial organisation rather
than as a story about semiconductors. It is currently unread, and reading it is the highest-value
follow-up in this file. The document also closes the loop in the direction `WHY.md` leaves open: big
bets *produce* big customers, not only the reverse.

**H2, customer concentration damages a foundry.** Mostly reinforcement of what CONC and FIN already
hold, with two additions. First, Gabaix (ECON-1) turns "concentration is risky" from an intuition into
a variance identity, which is worth having when arguing with someone quantitative. Second, and more
important, **the document hands us a serious counter-example and we must not bury it**: see below.

**H5, there is a long tail of demand for chips.** The document does more for H5 than anything else the
repository has assessed. H5 has been "Argued" because chip-specific evidence of latent demand is thin.
Three of its references change that:
- **Acemoglu & Linn (ECON-11)** is causal evidence that market size drives *invention*, identified off
  exogenous demographics. It is the general form of H5's claim, tested.
- **Thompson & Spanuth (ECON-12)** name the tail in chips explicitly: applications left behind because
  they "do not comprise a sufficient market to justify the upfront fixed costs".
- **Brynjolfsson, Hu & Smith (ECON-13)** state H5's mechanism in the words of the people who measured
  the long tail: the tail is served when the fixed cost per product falls. Their offset-printing
  break-even of 1,000 copies is the exact analogue of a mask set, and print-on-demand at $3.00 a copy
  is the exact analogue of a shuttle.

Against that, **Clauset, Shalizi & Newman (ECON-17)** is a methodological warning we should keep
pointed at ourselves: most published power-law claims do not survive a proper test, and nobody has
tested the size distribution of markets for engineered products.

**H7, many small customers reduce risk and remove buyer power.** Supported by the arithmetic (ECON-1,
ECON-3, ECON-4). Challenged by Cirrus Logic (ECON-20), by Inderst & Wey (ECON-19), and — most
interestingly — by ASML (ECON-26), where what protected the supplier was not customer count but
irreplaceability. The correlated-tail sensitivity above is a further limit on H7 that comes out of the
document's own tool.

**H10, being paid for every attempt works in a world of skewed outcomes.** The *Great Eastern* and
Iridium are two clean illustrations of bets whose markets never arrived, both eventually repaid by a
use nobody designed for. Both are illustrations, not evidence, and the Iridium figures are unverified.

**H11, markets and insurance can replace foundry judgement.** Two indirect contributions. Williamson
and hold-up (ECON-6, FIN-8) make the case that selling *general* machine time is structurally different
from selling a relationship: there is no specific asset to be held up over. And the document's Iridium
footnote — "the rescue rode on a Department of Defense contract, which is the first rule rescuing the
second" — is a reminder that the buyer of last resort in these stories is usually a government.

## Where the document is weak

- **The Zipf step is the whole second rule, and it is an inference.** Firms are Zipf-distributed
  (ECON-15, and even that exponent is disputed by later work). Cities are. *Markets* are not measured
  by anyone the document cites, and the document says so. Everything downstream — "for every market
  that could repay a ten-billion-dollar bet, there are on the order of a hundred thousand that could
  repay a hundred-thousand-dollar one" — is a rule of thumb with an honest label on it. **The
  repository must keep that label on.** It is a useful way to think about orders of magnitude and it is
  not a law. If we ever want it to be more than that, ECON-17 says how to find out.
- **No treatment of correlation, despite naming it.** The document says correlated customers count as
  one, then computes TSMC's effective count as if 512 tail customers were independent. The sensitivity
  above shows that assumption is doing a third of the work.
- **The escape is asserted, not costed.** "One customer pays for the bet, everyone reuses it" is the
  foundry model and the document says it "only works for a supplier that has already survived the first
  rule". It never says how a supplier survives rule 1 in the first place — which is exactly the gap
  `WHY.md` and `PRINCIPLES.md` exist to fill. Its own escape hatch, "markets that grow faster than the
  bets do", is named in one clause and never examined.
- **It accepts NRE as given.** Like the "Tyranny of the Whale" brief, it treats the fixed cost as a
  fact of nature that shrinks the market, rather than asking what makes NRE high and whether that is
  changeable. H4 is the hypothesis it never considers.
- **Two of the three case studies are illustrative history.** Roman Britain and the *Great Eastern*
  are vivid and carry no evidential weight; the document's own endnotes half-admit it for Rome.
- **It is an explainer.** No data of its own, no model, nothing testable. Its value to us is its
  reference list and its one arithmetic tool.

## The Cirrus Logic counter-example

Recorded here explicitly rather than in a footnote, because it is the strongest single challenge to H2
and H7 the repository has.

Cirrus Logic's Form 10-K states, verbatim: *"For the twelve-month periods ending March 28, 2026, March
29, 2025, and March 30, 2024, we had one end customer, Apple Inc., who purchased through multiple
contract manufacturers and represented approximately 91 percent, 89 percent and 87 percent of the
Company's total net sales, respectively."*

Over those years its net income rose from $176.7M (FY2023) to $414.4M (FY2026) and its net margin rose
from 9.3% to 20.7% (`DERIVED`, ECON-20). Concentration rose every year. Profitability rose every year.

H2 says big customers "push margins down, make losing one catastrophic, lock the foundry into their
products, make it risk-averse, and raise its cost of capital." Cirrus Logic is the theoretical worst
case on the first clause and the margins went **up**. That is not a quibble; it is a firm at the limit
of the independent variable behaving the opposite of the way the hypothesis predicts.

What survives of H2 against it:
- The **risk** claim is untouched. Cirrus Logic's margins are realised outcomes; FIN-2's claim is about
  the *price of variance*, which a profitable firm still pays. Imagination Technologies (CONC-6,
  ECON-22) is the same bet resolving the other way, and the document places them side by side
  deliberately.
- Cirrus Logic is **fabless**. It sinks no $20B in a fab, so rule 2 barely applies to it and the
  cost-of-capital mechanism bites far less. The hypothesis is about *foundries*; this is a designer.
- It may be **irreplaceable in its niche**, which the ASML case (ECON-26) suggests is the real
  protection. If so, the operative variable is substitutability, not customer count — and that would
  weaken H7's *mechanism* even where H7's conclusion holds.

What this should change: H2's status line should distinguish the risk claim (well supported) from the
margin claim (contested, with a live counter-example). H7 should record that concentration is
compatible with excellent and rising profitability, and that the case for many small customers is about
variance and durability, not about margins.

## Open questions

1. **Read Sutton (1991).** It is the formal version of H1 and nobody in the repository has read it.
2. **Has anyone applied Clauset/Shalizi/Newman to the size distribution of markets or product
   categories?** If the answer is no, say so plainly wherever the "one zero for one zero" rule is used.
3. **Does the tail correlate?** The base-case effective-customer count for TSMC falls from 11.8 to 7.0
   if the tail moves together. Is there data on how correlated small foundry customers' demand is? This
   is the single most decisive unknown for H7.
4. **Cirrus Logic before FY2023.** The document says "between about two-thirds and nine-tenths of its
   revenue from Apple for more than a decade". Only FY2023–FY2026 were checked. Earlier 10-Ks would
   settle whether this is a decade-long counter-example or a recent one.
5. **Are there concentrated *foundries* that prospered?** Cirrus Logic is fabless, which is the easy
   rebuttal. A concentrated, capital-intensive manufacturer with rising margins would be much harder to
   answer, and we should look for one rather than wait to be shown one.
6. **Bresnahan & Reiss's five trades**, and whether the "second dentist" threshold really scales the
   way the document applies it to a $20B fab.
7. **Does any foundry publish enough to compute its own effective customer count more precisely than
   three data points allow?** GlobalFoundries reports by wafer volume, not revenue (CONC-3), which
   would give a different and possibly more useful number.

## Document 2 — "The Tyranny of the Whale": reference harvest not completed

The task also asked for a re-read of the public Claude artifact at
<https://claude.ai/public/artifacts/6633a222-4b09-4967-b923-b6cc9ceb1101>, specifically for its
references section.

**Not reached.** Two legal routes were tried on 2026-09-18:
- A direct fetch of the public artifact URL returned only the page shell — Anthropic's corporate footer
  and no document content. The page renders its body client-side and blocks automated fetchers, exactly
  as [`tyranny-of-the-whale-brief.md`](tyranny-of-the-whale-brief.md) recorded on 2026-09-13.
- The first-party artifact read tool rejected the `/public/artifacts/` form and, on the `/artifact/`
  form of the same ID, reported that the artifact was not found or not shared with this account.

No bot check was circumvented and no browser automation was attempted. **Blocker: client-side rendering
plus an automated-fetcher block on claude.ai public artifact pages, and no artifact-share access.**

What is therefore unresolved:
- Whether the brief has a formal reference list at all, or only inline attributions. The existing
  assessment's cross-check table lists sources but does not say it harvested a bibliography.
- Whether it cites anything not already captured as FIN-1…FIN-10, CONC-*, COST-*, LEARN-7 or SW-5.
- Its private-equity concentration thresholds (15%/20%/30%) and valuation discounts (20–30%), which the
  existing assessment marks **Unsourced** — if the brief has a reference list, that is where a source
  for them would be.
- Its wafer-price range ($3,000 at 28nm to $30,000 at 2nm), which the brief itself attributes to
  unofficial channel checks.

Worth noting: the two documents overlap on Porter, Dhaliwal et al., Campello & Gao and Patatoukas, and
*Big Customers, Big Bets* gets the Dhaliwal DOI right where the repository has it wrong (below). That
is weak evidence that the two documents were built from different reference work rather than one from
the other.

## Changes needed in other files

These are edits this assessment could not make, listed for whoever owns those files.

1. **`resources/references/finance-and-contracts.md`, FIN-2 — the DOI is wrong.** FIN-2 gives
   `10.1016/j.jacceco.2015.08.003`. That DOI resolves to Lennox, Wu & Zhang, "The effect of audit
   adjustments on earnings quality: Evidence from China", *Journal of Accounting and Economics* 61(2–3),
   2016, pp. 545–562 — a different paper by different authors. The correct DOI for Dhaliwal, Judd,
   Serfling & Shaikh, "Customer concentration risk and the cost of equity capital", *JAE* 61(1), 2016,
   pp. 23–48, is **`10.1016/j.jacceco.2015.03.005`**, confirmed against Crossref on 2026-09-18. It is
   the DOI *Big Customers, Big Bets* prints. FIN-2's volume, issue, pages and author names are all
   correct; only the DOI needs changing.
2. **`resources/references/finance-and-contracts.md`, FIN-8** — the Klein, Crawford & Alchian citation
   was independently confirmed on 2026-09-18 (*Journal of Law and Economics* 21(2), October 1978,
   pp. 297–326, doi:10.1086/466922). Worth marking as citation-checked, and worth a cross-reference to
   ECON-6 for Williamson's 1985 book.
3. **`resources/references/finance-and-contracts.md`, FIN-7** — add a warning that Inderst & Wey have
   *two* relevant papers. FIN-7 holds the 2003 *RAND* article; ECON-19 holds "Buyer power and supplier
   incentives", *European Economic Review* 51(3), 2007, pp. 647–667, which argues the effect is
   theoretically ambiguous. They should not be conflated.
4. **`resources/references/finance-and-contracts.md`, FIN-5** — the Patatoukas citation was confirmed
   in passing (*The Accounting Review* 87(2), 2012, pp. 363–392, doi:10.2308/accr-10198). Not pursued
   further, per the 2026-09-14 decision.
5. **`resources/references/customer-concentration.md`, CONC-13 (Huawei cut-off, currently a Lead)** —
   can be upgraded. ECON-21 verifies the 2020 20-F's own words on the shipment halt, the September 15
   2020 date, the 25% largest-customer share and "not materially affected". The 14% share of 2019
   revenue remains an analyst estimate and should stay a Lead.
6. **`resources/references/customer-concentration.md`, CONC-6** — add the outcome. ECON-22 verifies the
   £550 million Canyon Bridge sale, completed 2017-11-03 at 182p a share, from the acquirer's own
   press release. CONC-6 currently stops at the share-price fall.
7. **`resources/hypotheses.md`, H2** — add ECON-20 (Cirrus Logic) under **Challenges**, and split the
   status line so the risk and cost-of-capital claims stay "well supported" while the margin claim
   becomes "contested". Add ECON-1 and ECON-8 under Supports.
8. **`resources/hypotheses.md`, H5** — add ECON-11 (Acemoglu & Linn), ECON-12 (Thompson & Spanuth) and
   ECON-13 (Brynjolfsson, Hu & Smith) under **Supports**; add ECON-17 (Clauset et al.) as a
   methodological caution. The "Needs" line about chip-specific latent demand is partly answered by
   ECON-12. The status could reasonably move from "Argued" to "Argued, with the mechanism now
   evidenced outside chips and named inside them".
9. **`resources/hypotheses.md`, H7** — add ECON-20 and ECON-19 under **Challenges**, ECON-1 and ECON-4
   under **Supports**, and record the correlated-tail limit: TSMC's effective customer count falls from
   11.8 to 7.0 if the tail moves together.
10. **`resources/hypotheses.md`, H1** — add ECON-18 (Sutton) as the theoretical spine, marked Partial
    and unread, and ECON-12.
11. **`resources/README.md`** — add a row to the "Reference topics" table:
    `references/economics-of-concentration.md` | `ECON` | Economics of concentration and fixed cost:
    the Herfindahl index and effective customer count, bargaining and hold-up, market size and
    innovation, and the power-law question.
12. **`WHY.md`** — if the effective-customer-count tool is adopted, it belongs there with its
    assumptions stated, and the Cirrus Logic counter-example belongs in the same section as the
    Imagination case rather than being left out.
