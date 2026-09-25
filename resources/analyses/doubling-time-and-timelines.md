# How fast is the customer base doubling, and what would 10k or 100k a year take?

*Our own analysis, 2026-09-20. Tiny Tapeout figures are computed from all 28 shuttle indexes plus
the operator's own `submission-stats` API; wafer.space figures are from its three Crowd Supply
campaign pages. Method and caveats at the foot.*

**Deliberately excluded: the size of the market today.** At roughly $1–2m a year across the whole
unsubsidised sector ([`../demand/payment-growth.md`](../demand/payment-growth.md)) the absolute
numbers are too small to support conclusions. **Rate of change is the only thing worth reading off
them**, and that is all this file does.

---

## Tiny Tapeout: customers per year

"Customer" here is a distinct GitHub account owning at least one project on a shuttle that year,
with the programme's own `tinytapeout` organisation account excluded. Six of the 28 shuttles carry
no date in either the `deadline` field or any submission record; the table is given both ways.

| Year | Customers | Growth | First-time customers | Designs |
|---|---|---|---|---|
| 2022 | 193 | — | 193 | 428 |
| 2023 | 259 | +34.2% | 231 | 469 |
| 2024 | 643 | **+148.3%** | 575 | 960 |
| 2025 | **923** | +43.5% | 509 | 1,492 |
| 2026 (part year, to 07-30) | 1,019 | — | **941** | 1,322 |

*(Excluding the six undated shuttles instead of interpolating them gives 258 / 640 / 916 for
2023–2025 — within 1% of the above. The choice does not matter.)*

### Doubling time

Log-linear fit over the complete years 2022–2025:

| Series | Growth | **Doubling time** |
|---|---|---|
| Customers per year | **+75.1%/yr** | **1.24 years** |
| First-time customers per year | +46.5%/yr | 1.81 years |
| Designs per year | +120.8%/yr | 0.88 years |

On dated shuttles only the customer figure is +88.4%/yr and 1.09 years. **So the honest statement is
that Tiny Tapeout's customer base has been doubling every 1.1–1.25 years.**

### The two things that complicate it

**First-time customers are growing much more slowly than total customers** — 1.81 years to double
against 1.24 — and in 2025 the count of first-timers actually *fell*, 575 → 509. Total customers
kept rising because the base kept returning. That is a programme converting its existing audience
faster than it is finding a new one, which is a leading indicator worth watching.

**But 2026 reverses it sharply.** In a part year it already shows **941 first-time customers**
against 2025's 509. Note what that implies: of 1,019 accounts active in 2026, **941 are new and only
78 returned from an earlier year** — a 7.7% year-on-year return rate, which independently reproduces
the "6–16% annual retention" figure from
[`data-cuts-and-statistics.md`](data-cuts-and-statistics.md) from a different direction. Growth here
is acquisition, not retention.

### Timeline from 923 customers in 2025

| Growth assumed | Doubling | Reach 10,000 | Year | Reach 100,000 | Year |
|---|---|---|---|---|---|
| **measured, +75.1%** | 1.24 y | 4.3 y | **2029** | 8.4 y | **2033** |
| three-quarters of it, +56.4% | 1.55 y | 5.3 y | 2030 | 10.5 y | 2035 |
| half of it, +37.6% | 2.17 y | 7.5 y | 2032 | 14.7 y | 2040 |
| a quarter of it, +18.8% | 4.03 y | 13.8 y | 2039 | 27.2 y | 2052 |
| +30% floor | 2.64 y | 9.1 y | 2034 | 17.9 y | 2043 |
| +15% floor | 4.96 y | 17.0 y | 2042 | 33.5 y | 2059 |

**Read the second and third rows, not the first.** Four years of data cannot support extrapolating a
+75% rate for a decade, and no programme in the evidence base has ever sustained one. The defensible
claim is the *range*: **10,000 customers a year is 4–8 years away if growth merely halves, and
100,000 is 8–15 years away on the same assumption.**

## What those numbers would require in silicon

*(**Corrected 2026-09-25.** The first version of this section used "1.76 tiles per design". That
was an error: **1.76 is `PAY-6`'s 2025→2026 *revenue* growth ratio**, 341,710 ÷ 194,670, not a tile
count. Caught by `LN-18`'s author. The corrected figures are below, and they move the headline from
555 shuttles to a range.)*

This is where the projection stops being arithmetic and starts being a manufacturing problem. Two
of the three ratios are stable; **the tiles-per-design ratio is not**, and the projection is
directly proportional to it:

| Tiles per design, from `PAY-6` | Value |
|---|---:|
| 2025 (1,352 tiles ÷ 1,455 designs) | **0.93** |
| Lifetime (6,218 ÷ 4,258) | **1.46** |
| 2026 to date (2,553 ÷ 1,358) | **1.88** |

A 2× spread across three overlapping windows, so the honest output is a band, not a number. Holding
1.62 designs per customer and 512 tiles per shuttle:

| Customers/yr | Designs/yr | Shuttles/yr at 0.93 | at 1.46 | at 1.88 |
|---|---:|---:|---:|---:|
| 923 (2025 actual) | 1,492 | 2.7 | 4.3 | 5.5 |
| 10,000 | 16,165 | **29.3** | **46.1** | **59.4** |
| 100,000 | 161,647 | **293** | **461** | **594** |

**And the 512-tile assumption is the optimistic bound, by 4.5×.** The 2025 row predicts 2.7 to 5.5
shuttles; Tiny Tapeout actually ran **12**. Realised density was **1,352 ÷ 12 = 112.7 tiles per
shuttle**, not 512 — shuttles do not fill. Re-running the table at realised density gives **133–270
shuttles a year for 10,000 customers** and **1,333–2,697 for 100,000**.

So the conclusion survives the correction and hardens: ten thousand customers a year is **between
half a shuttle and five shuttles a week**, and a hundred thousand is **between six and fifty a
week**, against the 12 a year Tiny Tapeout ran in 2025. Tile capacity per shuttle could rise, which
changes the shuttle count but not the wafer area. **The constraint at 100k is not demand — it is
whether anyone will run you hundreds to thousands of shuttles a year.**

## wafer.space: two and a half data points

Stated plainly because that is what exists. wafer.space is the repository owner's own company, so
these are our own numbers.

| Campaign | Backers | Raised | Status |
|---|---|---|---|
| GF180MCU Run 1 | **6** | $55,500 | closed 2025-11-28 |
| GF180MCU Run 2 | **18** | $175,000 | closed 2026-06-29 |
| GF180MCU Run 3 | **6** so far | $125,000 so far | **live**, ends 2026-12-19 |

**Run 1 → Run 2 is 6 → 18 backers, a 3× rise in 213 days.** Annualised that is **+558%/yr, a
doubling every 4.4 months.**

**That number should not be used for anything.** It is two points; the second campaign benefited
from the first existing at all; and it is the kind of rate that only ever appears at the very
beginning of a series. **Run 3 is not a third data point** — it is mid-campaign with 91 days left,
and comparing its running total to two closed campaigns would be the same error the AFRL comparison
made.

For completeness, from the 24 backers of Runs 1 and 2 combined:

| Growth assumed | Reach 10,000/yr | Reach 100,000/yr |
|---|---|---|
| Run 1 → Run 2 rate (+558%) | 3.2 y | 4.4 y |
| +100%/yr | 8.7 y | 12.0 y |
| +50%/yr | 14.9 y | 20.6 y |
| +30%/yr | 23.0 y | 31.8 y |

And what it would mean, at Run 3's $7,000 full-slot price and 1,000 dies per slot:

| Slots/yr | Revenue | Dies | Distinct reticles/yr |
|---|---|---|---|
| 24 | $0.2m | 24,000 | ~0.5 |
| 10,000 | **$70m** | 10 million | ~229 (≈19/month) |
| 100,000 | **$700m** | 100 million | ~2,293 (≈191/month) |

At 19.67 mm² a slot and ~858 mm² a reticle, about **44 slots fit per reticle**. Ten thousand slots a
year is 229 distinct reticles — which is a real business and a hard operations problem. A hundred
thousand is 191 new reticles a month, and that is not a scaled-up version of the same activity.

## What this actually tells the project

1. **The doubling time is the robust finding: 1.1–1.25 years for Tiny Tapeout customers**, measured
   three ways that agree. That is faster than any traditional programme in the evidence base —
   Europractice's design count over the same period is flat to slightly falling (`DEM-16`).
2. **The projections are illustrative, not forecasts.** Four years and two campaigns cannot forecast
   a decade. Their value is in bracketing: 10,000/yr is plausibly this decade, 100,000/yr is not
   obviously reachable before the 2040s unless growth holds at rates nothing has sustained.
3. **The binding constraint flips.** Below ~10,000 customers a year the problem is demand. Above it,
   the problem is shuttle throughput and reticle operations. The project's thesis is about the first
   regime, and `PRINCIPLES.md` is about the second — and nothing in this repository yet addresses
   running 50+ shuttles a year.
4. **Acquisition, not retention, is doing the work.** 941 of 1,019 accounts active in 2026 are
   first-timers. A model that assumes customers accumulate is wrong for this population; the
   population is replaced roughly every year.

## Method and caveats

- Tiny Tapeout customers: distinct lower-cased GitHub owner from each project's `repo` URL, per
  shuttle, assigned to the year of the shuttle's `deadline` from
  `https://app.tinytapeout.com/api/shuttles/submission-stats`. A browser `User-Agent` is required;
  the default `urllib` agent gets HTTP 403.
- Six shuttles (`tt02`, `tt03`, `tt03p5`, `tt05of`, `ttihp0p1`, `ttgf0p1`) have no deadline and no
  submission records. They were assigned the year of the nearest preceding dated shuttle in the
  chronological index. Both variants are reported above and differ by under 1%.
- **2026 is a part year** (latest shuttle deadline 2026-07-30) and is excluded from every fit.
- A designer using two GitHub accounts counts twice; a shared teaching account counts once for a
  whole class. Neither can be sized. See
  [`tiny-tapeout-participation.md`](tiny-tapeout-participation.md).
- wafer.space figures are from live campaign pages and will move.
