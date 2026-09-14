# Learning curves (`LEARN`)

Wright's law, the experience curve, learning spillovers, and whether small, numerous units learn faster. This is evidence for H3 (why chasing scale is rational) and H9 (whether many public experiments learn faster).

---

### LEARN-1. Wright (1936): labour cost falls along a predictable curve as production accumulates

- **Source:** T. P. Wright, "Factors Affecting the Cost of Airplanes", *Journal of the Aeronautical Sciences* 3(4), February 1936, pp. 122–128. DOI 10.2514/8.155. PDF: <https://pdodds.w3.uvm.edu/research/papers/others/1936/wright1936a.pdf>
- **Verification:** Verified 2026-09-13 (PDF text, pp. 124–125).
- **What it says:** in Fig. 3 "such a curve appears; there called the eighty percent curve". Wright explains: "This "eighty percent" has a definite meaning in that it represents the factor by which the average labor cost in any quantity shall be multiplied in order to determine the average labor cost for a quantity of twice that number of airplanes."
- **Bears on:** H3 (supports).
- **Used in:** `WHY.md` §2, Step 3.
- **Caveats:**
  - It measures labour cost for one aircraft model, not total cost.
  - The PDF has line-break hyphens ("per­ cent", "air­ planes").

### LEARN-2. BCG (1968): costs fall 20–30% each time accumulated production doubles

- **Source:** Bruce Henderson, "The Experience Curve", Boston Consulting Group, 1968: <https://www.bcg.com/publications/1968/business-unit-strategy-growth-experience-curve>
- **Verification:** Verified 2026-09-13 with WebFetch. bcg.com returns 403 to curl.
- **What it says:**
  - "Costs decline by some characteristic amount each time accumulated experience is doubled."
  - "The characteristic decline is consistently 20-30% each time accumulated production is doubled."
  - "The rate of decline is surprisingly consistent, even from industry to industry."
- **Bears on:** H3 (supports).
- **Used in:** not yet; `WHY.md` uses LEARN-3.
- **Caveats:** a consultancy's claim of consistency, not a systematic study.

### LEARN-3. BCG (1973): the experience curve was built on semiconductor data

- **Source:** Bruce Henderson, "The Experience Curve—Reviewed (Part II)", Boston Consulting Group, 1973-01-01: <https://www.bcg.com/publications/1973/corporate-finance-strategy-portfolio-management-experience-curve-reviewed-part-ii-the-history>
- **Verification:** Verified 2026-09-13 with WebFetch; the fact-check also used a Wayback Machine copy.
- **What it says:**
  - "Semiconductors provided the evidence on which to build the experience curve concept itself."
  - "Price data supplied by the Electronic Industries Association was compared with accumulated industry volume. Two distinct patterns emerged. In one pattern, prices, in current dollars, remained constant for long periods and then began a relatively steep and long continued decline in constant dollars. In the other pattern, prices, in constant dollars, declined steadily at a constant rate of about 25 percent each time accumulated experience doubled. That was the experience curve. That was 1966."
  - "Experience curve is the name applied in 1966 to overall cost behavior by The Boston Consulting Group. The name was selected to distinguish this phenomenon from the well known and well documented learning curve effect." The older learning curve "only applied to direct labor."
- **Bears on:** H3 (supports: chips are where the experience curve was first shown).
- **Used in:** `WHY.md` §2, Step 3.
- **Caveats:**
  - The 25% applies to one of two patterns, not the whole industry.
  - It is industry-wide price data, not one firm's costs.

### LEARN-4. Wright's law forecasts technology costs best, but only just

- **Source:** Béla Nagy, J. Doyne Farmer, Quan M. Bui and Jessika E. Trancik, "Statistical Basis for Predicting Technological Progress", *PLOS ONE* 8(2): e52669, 2013: <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0052669>
- **Verification:** Verified 2026-09-13.
- **What it says:**
  - "Using a new database on the cost and production of 62 different technologies… we test the ability of six different postulated laws to predict future costs."
  - "Wright's law produces the best forecasts, but Moore's law is not far behind."
  - The datasets include "DRAM" and "Transistor".
  - Per the fact-check: "the fact that Goddard is not that much worse indicates that much of the predictability comes from annual production, suggesting that economies of scale are important."
- **Bears on:**
  - H3 (supports, with a caveat): time-based and scale-based rules also predict well, so cumulative experience isn't clearly the only driver.
- **Used in:** `WHY.md` §2, Step 3.

### LEARN-5. Solar panels: a 20% learning rate

- **Source:** Max Roser, "Learning curves: What does it mean for a technology to follow Wright's Law?", Our World in Data, 2023-04-18: <https://ourworldindata.org/learning-curve>
- **Verification:** Verified 2026-09-13.
- **What it says:** "The learning rate of solar panels is 20%. This means that with each doubling of the installed cumulative capacity, the price of solar panels declined by 20%."
- **Bears on:** H3 (context: a familiar example).
- **Used in:** `WHY.md` §2, Step 3.

### LEARN-6. More granular energy technologies learn faster, under certain conditions

- **Source:** Charlie Wilson, Arnulf Grubler, Nuno Bento, Steve Healey, Simon De Stercke and Caroline Zimm, "Granular technologies to accelerate decarbonization", *Science* 368(6486), 2020, pp. 36–39: <https://www.science.org/doi/10.1126/science.aaz8060> (authors' manuscript: <https://pure.iiasa.ac.at/id/eprint/16400/1/Granularity_Manuscript_preprint.pdf>)
- **Verification:** Verified 2026-09-13 against the published text (a reposted copy) and the manuscript.
- **What it says (published version):**
  - "We show that learning is faster for more-granular energy technologies, using two different formulations of the learning rate…"
  - "In both cases, more-granular technologies offer more opportunities for repetitive, replicative experience to drive faster improvement."
  - Conclusions: "Under certain conditions, more-granular technologies are empirically associated with faster diffusion, lower investment risk, faster learning, more opportunities to escape lock-in, more equitable access, more job creation, and higher social returns on innovation investment."
  - Examples range "from solar panels, e-bikes, and smart thermostats to carbon capture and storage, light rail transit…"
  - The manuscript's figure caption distinguishes the conventional learning rate per doubling of cumulative *capacity* from a "descaled 'true' learning rate" per doubling of cumulative *numbers of units*.
- **Bears on:** H9 (supports, by analogy): more, smaller units give more learning cycles.
- **Used in:** `WHY.md` §5.
- **Caveats:**
  - Energy technologies only.
  - The results are simple two-variable correlations.
  - The published piece is an "INSIGHTS" (policy) article with no abstract. A longer sentence in the manuscript abstract doesn't appear in the published version.

### LEARN-7. Learning spills over between chip firms, but firms learn most from their own production

- **Source:** Douglas A. Irwin and Peter J. Klenow, "Learning-by-Doing Spillovers in the Semiconductor Industry", *Journal of Political Economy* 102(6), 1994, pp. 1200–1227. DOI 10.1086/261968. PDF: <http://klenow.com/LBD_Spillovers.pdf>
- **Verification:** Verified 2026-09-14 (abstract, from the authors' PDF).
- **What it says:** "Using quarterly, firm-level data on seven generations of dynamic random access memory (DRAM) semiconductors over 1974-92, we find that
  - (a) learning rates average 20 percent,
  - (b) firms learn three times more from an additional unit of their own cumulative production than from an additional unit of another firm's cumulative production,
  - (c) learning spills over just as much between firms in different countries as between firms within a given country,
  - (d) Japanese firms are indistinguishable from others in learning speed, and
  - (e) intergenerational learning spillovers are weak, being marginally significant in only two of seven DRAM generations."
- **Bears on:**
  - H3 (supports: the 20% learning rate in chips).
  - H9 (mixed):
    - (b) and (c) show real spillovers between firms. That challenges `WHY.md` §5's claim that one team's learning "adds little" to others, and it also shows there are spillovers to amplify.
    - (e) supports "each new generation starts over".
- **Used in:** `WHY.md` §5 (from Draft v0.5), which now says learning spreads between firms "but less than it could".
- **Caveats:** DRAM is high-volume commodity memory. Spillovers among many small, varied experiments may behave differently.

### LEARN-8. Texas Instruments priced chips on the learning curve

- **Source:** Commoncog, "Texas Instruments - Inventing Learning Curve Pricing": <https://commoncog.com/c/cases/texas-instruments-learning-curve/>
- **Verification:** **Lead.** A secondary case study we haven't read.
- **What it says (per a search summary):** Texas Instruments worked with BCG to price below cost ahead of expected cost declines ("learning curve pricing").
- **Bears on:** H3 (supports, possibly): chip firms have long used the curve to justify chasing volume.
- **Used in:** not yet.
