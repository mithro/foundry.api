# How many customers does it take to fill a fab?

*Our own arithmetic, 2026-09-19. This corrects a conclusion drawn in
[`data-cuts-and-statistics.md`](data-cuts-and-statistics.md) and in the H7 status line by applying
a PCB-derived threshold to chips, where it does not belong.*

---

## The error being corrected

From the audited PCB makers we learned that customer count barely predicts revenue concentration:
595 customers gives a top-five share of 19.36%, "over ten thousand" gives 40.07%, and only JLC's
1,358,700 reaches 1.16% (`PCB-1`, `PCB-5`, `SMB-1`). The conclusion drawn was that **the dispersion
H7 wants "appears at a million customers, not at ten thousand"**.

**That conclusion does not transfer to a fab, and stating it without qualification was wrong.** It
was derived from a business whose long-tail customer buys about five boards for tens of dollars. A
chip customer buying production wafers is a different order of magnitude of customer, and the
number needed is correspondingly smaller.

## The arithmetic

Take a customer buying **100 wafers a year** — a modest production volume, not a prototype:

| | |
|---|---|
| 7,000 customers × 100 wafers/yr | **700,000 wafers/yr** |
| | **58,333 wafer starts per month** |
| | 13,462 per week, 1,918 per day |

For scale:

| Reference | Approx. capacity | 58,333 wspm as a share |
|---|---|---|
| TSMC "GIGAFAB" threshold, as commonly cited | 100,000 wspm | 58.3% |
| GlobalFoundries Fab 8 (Malta, NY) | ~60,000 wspm | 97.2% |
| A large 200 mm mature-node fab | ~40,000 wspm | 146% |
| A small or specialty fab | ~10,000 wspm | 583% |

**Seven thousand customers at 100 wafers a year each fills a very large fab.** It is not a
GIGAFAB on TSMC's 100,000-wspm definition, so that label should not be used, but it is roughly the
scale of GlobalFoundries' Fab 8 and comfortably larger than a typical mature-node 200 mm fab. The
capacity figures above are approximate industry figures and should be replaced with sourced ones
before this is cited anywhere load-bearing.

## Why the million-customer threshold does not apply

Annual spend per customer differs by orders of magnitude between the businesses being compared:

| Customer type | Annual spend | Source |
|---|---|---|
| JLC PCB long-tail customer | **~US$1,052** | revenue ÷ paying users, `SMB-1` |
| Tiny Tapeout participant | **~€70** | per tile |
| Chip customer at 100 wafers/yr | **~US$300,000** | at US$3,000/wafer, mature node |

A 100-wafer-a-year chip customer is worth about **285×** a JLC long-tail customer. To match the
revenue JLC gets from 1.36 million customers you need roughly **4,800 chip customers**.

So "you need a million customers for dispersion" is an artefact of measuring in PCB customers. In
wafer customers the same revenue dispersion arrives three orders of magnitude sooner.

## What this does to H7

If a fab's customers each buy a broadly similar number of wafers, concentration falls immediately:

| Equal-sized customers | HHI | Effective customers | Top-5 share |
|---|---|---|---|
| 595 | 0.001681 | 595 | 0.84% |
| 3,000 | 0.000333 | 3,000 | 0.17% |
| 7,000 | 0.000143 | 7,000 | **0.07%** |
| 10,000 | 0.000100 | 10,000 | 0.05% |

Against the measured PCB figures — 595 customers → 19.36%, 10,000 → 40.07% — the difference is
entirely **inequality of order size**, not customer count. PCB makers have wildly unequal customers
(one Hikvision account is 12.58% of 迅捷兴's revenue, *Hikvision* being a large Chinese
video-surveillance manufacturer). A fab selling wafer starts to customers who each need production
quantities has a naturally flatter distribution.

**The open question, and it is the real one:** would a fab's customers actually be similarly sized?
Nothing here establishes that. If the distribution of wafer demand is itself long-tailed — a few
customers wanting 10,000 wafers and most wanting 20 — concentration returns immediately and H7 is
back in difficulty. **This is now the most valuable single piece of evidence this project could
acquire: the distribution of annual wafer volume across a real mature-node fab's customer book.**

## Revenue scale, for context

| Wafer price | Revenue at 700,000 wafers/yr |
|---|---|
| US$1,000 | US$0.70 bn/yr |
| US$3,000 | US$2.10 bn/yr |
| US$5,000 | US$3.50 bn/yr |

For comparison, the entire open-and-commercial shuttle sector is plausibly **US$1–3 million a
year** ([`open-access-audit.md`](open-access-audit.md) §6.1). The gap between the population that
exists today and the population that would fill a fab is the central practical problem, and it is a
gap in *customer size* far more than in *customer count*: 7,000 customers is an achievable number,
but 7,000 customers each buying 100 production wafers a year is a completely different population
from the ~2,600 people who have ever submitted a Tiny Tapeout tile.

## Bears on

- **H7 (supports, with the threshold corrected).** The PCB-derived "one million customers" figure
  does not apply to a fab. Seven thousand wafer customers gives a top-five share of 0.07% if they
  are similarly sized.
- **H5 (context).** Reframes the demand question: the project does not need a million customers, it
  needs a few thousand who each want production volume. That is a much smaller number of a much
  rarer kind of customer.
- **H6 (context).** At US$3,000/wafer and 100 wafers, a "small" customer is a US$300,000-a-year
  account — not small in any sense that makes per-customer cost-to-serve a problem.

---

## The assumed customer size has now been checked against a real fab — and it was right

*Added 2026-09-25, from `LNI-18`.*

Everything above rests on one assumption made without evidence: that a chip customer buys **100
wafers a year, ~US$300,000**. Silex Microsystems' IPO prospectus — approved by Finansinspektionen,
diary number 25-37533, 2026-04-27 — is the first document that lets it be tested against a real
specialty foundry's customer book.

**Silex's customers 11 through 85** share 21% of SEK 1,385m of net sales, i.e.
SEK 1,385m × 0.21 ÷ 75 = **SEK 3.878m ≈ €344,000 per customer per year**. The average across all 85
is SEK 1,385m ÷ 85 = **€1.45m**.

| | Annual spend |
|---|---|
| **Assumed** here, 100 wafers at US$3,000 | **~US$300,000** |
| **Measured** at Silex, tail customers 11–85 | **~€344,000 (~US$395,000)** |

**The assumption was right, within about 30%.** That is a genuine validation, and it is the first
one this file has had.

### But it breaks the other half of the argument

The size was right; **the count was not.** This file assumes **7,000** such customers. Silex, the
world's leading pure-play MEMS foundry, profitable and growing for twenty years, has
**approximately 85** — and about **75** in the tail band.

| | Assumed here | Measured at Silex |
|---|---:|---:|
| Tail customer's annual spend | ~US$300,000 | ~€344,000 ✅ |
| Number of such customers | **7,000** | **~75** ❌ |

**Two orders of magnitude.** And §"Why the million-customer threshold does not apply" above argued
that in wafer customers the dispersion H7 needs "arrives three orders of magnitude sooner" than the
million PCB customers. `LNI-18` contradicts that directly: at 85 customers Silex's top ten take
**77%** of net sales — the same as TSMC's 76–78% — and its effective number of customers (1/H) is
**8.6–9.0, fewer in absolute terms than TSMC's 11.8**. Its concentration has *risen* as it grew.

### What this actually leaves standing

- **The unit economics of the target customer are confirmed.** A €344,000-a-year customer exists in
  quantity at a real specialty fab, and `LN-18`'s arithmetic says 1,560 of them at 100 wafers/yr
  fill a 156,000-wafer/yr fab with capital of only **$19,231 per customer if the fab is bought**.
- **The population size is the whole problem, and it is unmeasured at the top end.** Nobody has
  shown that 1,560 — let alone 7,000 — such customers exist and are reachable. Silex found 85 in
  twenty years.
- **The customer this project is designed for is not the customer that fills a fab.** A Tiny Tapeout
  participant pays ~€70; a Silex tail customer pays ~€344,000. That is a factor of **4,900**. The
  bridge between the two populations — whether tape-out customers *become* wafer customers — is
  the load-bearing unknown, and nothing in this directory measures it.

**Do not cite the 7,000-customer figure as though the population were established.** It is an
arithmetic requirement, not an observation.
