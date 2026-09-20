# The long tail (`TAIL`)

Whether many low-volume products or customers can add up to a real market, and the evidence against it. This bears on H5, and indirectly on H6 and H7.

---

### TAIL-1. Anderson (2004): many misses can add up to more than the hits

- **Source:** Chris Anderson, "The Long Tail", *Wired*, 2004-10-01: <https://www.wired.com/2004/10/tail/>
- **Verification:** Verified 2026-09-13.
- **What it says:**
  - "If the 20th-century entertainment industry was about hits, the 21st will be equally about misses."
  - "Combine enough nonhits on the Long Tail and you've got a market bigger than the hits."
  - "Google, for instance, makes most of its money off small advertisers (the long tail of advertising), and eBay is mostly tail as well—niche and one-off products."
- **Bears on:**
  - H5 (supports).
  - H7 (context): Google as a business built on many small customers.
- **Used in:** `WHY.md` §5.
- **Caveats:**
  - Anderson's tail is mostly about niche *products*; our use is about many small *customers*. The Google example is the closest match.
  - Anderson was editor of *Wired* and wrote a best-selling book on the idea, so he had a stake in it.

### TAIL-2. Online bookstores' wider choice was worth far more to consumers than lower prices

- **Source:** Erik Brynjolfsson, Yu (Jeffrey) Hu and Michael D. Smith, "Consumer Surplus in the Digital Economy: Estimating the Value of Increased Product Variety at Online Booksellers", *Management Science* 49(11), 2003, pp. 1580–1596. Abstract: <https://econpapers.repec.org/RePEc:inm:ormnsc:v:49:y:2003:i:11:p:1580-1596>
- **Verification:** Verified 2026-09-13 for the abstract quotes (via EconPapers). The full paper wasn't read: MIT DSpace and SSRN blocked our tools.
- **What it says:**
  - "the increased product variety of online bookstores enhanced consumer welfare by $731 million to $1.03 billion in the year 2000, which is between 7 and 10 times as large as the consumer welfare gain from increased competition and lower prices in this market."
  - Per a search summary (**Partial**): the number of titles at Amazon was more than 23 times the number on the shelves of a typical Barnes & Noble superstore.
- **Bears on:** H5 (supports: wider choice has real value).
- **Used in:** `WHY.md` §5.
- **Caveats:** it measures value to *buyers*, not whether sellers of niche items earn enough. It doesn't show the tail outselling the hits.

### TAIL-3. Elberse (2008): online, hits still dominate, and tail customers like niche products less

- **Source:** Anita Elberse, "Should You Invest in the Long Tail?", *Harvard Business Review*, July–August 2008: <https://hbr.org/2008/07/should-you-invest-in-the-long-tail> (full-text reprint used for checking: <https://geminisufscar.files.wordpress.com/2009/05/shouldyouinvestinthelongtail.pdf>)
- **Verification:** Verified 2026-09-13 against the reprint.
- **What it says:**
  - **Rhapsody** (an online music service whose subscribers had more than 1 million tracks to choose from): "the top 10% of titles accounted for 78% of all plays, and the top 1% of titles for 32% of all plays."
  - **Quickflix** (an Australian DVD-by-mail service with just under 16,000 titles): "the top 10% of DVDs accounted for 48% of all rentals, and the top 1% for 18% of all rentals."
  - "It is a myth that obscure books, films, and songs are treasured. What consumers buy in internet channels is much the same as what they have always bought."
  - Hit products "naturally monopolize" light consumers. "Heavy users are more likely to venture into the long tail, but they choose a mix of hit and obscure products." Obscure titles are "appreciated less than popular titles".
  - Per the fact-check: "The importance of individual best sellers is not diminishing over time. It is growing."
- **Bears on:**
  - H5 (challenges): concentration persists even when shelf space is unlimited.
  - H7 (challenges, possibly): the head may keep dominating revenue.
- **Used in:** `WHY.md` §5, which argues the open-fab case needs only more modest things than the tail outselling the hits.
- **Caveats:**
  - The study covers music and video consumption, not business customers buying manufacturing time.
  - Heavy users "venturing into the tail" may be the closer analogue for experimenters.
  - Leads: the related HBR piece "The Long Tail Debate: A Response to Chris Anderson" (2008): <https://hbr.org/2008/07/the-long-tail-debate-a-respons>

---

## How this applies to chips

These are notes, and they are our interpretation.

- **Chip foundries do have a tail.** TSMC's 512 customers outside its top ten share about a quarter of revenue (CONC-1, CONC-2). The open question is how much *latent* demand sits beyond that tail: ideas never made because the up-front cost was too high.
- **What the argument needs.** Elberse's evidence means the open-fab case shouldn't claim the tail will outsell the head. It needs three more modest things, which are separate hypotheses:
  - each small customer is profitable (H6)
  - many small customers spread risk (H7)
  - the tail keeps producing experiments, a few of which grow large (H10)
- **Evidence that would help** — most of this has now been gathered into
  [`../demand/`](../demand/), and the answers are mixed at best:
  - growth in multi-project wafer (MPW) and shuttle programmes over time → **found, and it is
    mostly flat.** Europractice ran 363–614 designs a year from 2000 to 2017 (DEM-16); CMP peaked at
    401 in 2007 (DEM-19); CMC has fallen to 240 (DEM-20). Tiny Tapeout is the exception and is
    growing fast (DEM-1, DEM-2).
  - waiting lists and oversubscription on free shuttles such as Google Open MPW (OPEN-1) → **found.**
    Every free or subsidised programme traced was oversubscribed (DEM-4 to DEM-9, DEM-17, DEM-18),
    but so was the total response modest: 364 submissions worldwide over six free shuttles (DEM-9).
  - university and start-up tape-out counts → **partly found** (DEM-16, DEM-19, DEM-20, DEM-22).
  - cases where a small customer became a large one → **still not found.** See
    [`../demand/search-log.md`](../demand/search-log.md).
- **Also worth reading before citing TAIL-3:** DEM-13 records the parts of the same Elberse article
  that bear hardest on this project — the tail becoming "much longer and flatter", and her own
  extension of the conclusion to physical goods.
