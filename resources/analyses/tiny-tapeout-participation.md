# Is participation itself long-tailed? The Tiny Tapeout designer distribution

*Our own analysis, computed 2026-09-19 from all 28 shuttle indexes at
`https://index.tinytapeout.com/<id>.json`, fetched by GET. Reproducible: the method is at the foot
of this file.*

---

## Why this exists

[`data-cuts-and-statistics.md`](data-cuts-and-statistics.md) reported that "nobody comes back" —
73.6% of designers make exactly one design, year-on-year retention 6–16% — and treated that as
evidence against H5. Two objections were raised against that reading, and both are good:

1. **The framing is wrong for an educational programme.** Tiny Tapeout is primarily educational. A
   low return rate is the *expected* outcome, not a defect. Saying it has poor retention is like
   saying Year 7 has zero retention because everyone moves on to Year 8. Cohorts are supposed to
   pass through.
2. **The distribution was never actually shown.** "73.6% one-and-done" is one number from a
   distribution that nobody had printed. Participation might itself be long-tailed — a few
   designers on every shuttle, more on a handful, most on one — which is a different and more
   interesting shape than "nobody comes back".

This file prints the distribution.

## The distribution

Counting **distinct shuttles per designer**, over all 28 shuttles (2,634 distinct designers, 4,065
designer–shuttle participations):

| Shuttles | Designers | % of designers | Cumulative | % of all participations |
|---|---|---|---|---|
| 1 | 1,820 | 69.10% | 69.10% | 44.77% |
| 2 | 605 | 22.97% | 92.07% | 29.77% |
| 3 | 108 | 4.10% | 96.17% | 7.97% |
| 4 | 38 | 1.44% | 97.61% | 3.74% |
| 5 | 20 | 0.76% | 98.37% | 2.46% |
| 6 | 13 | 0.49% | 98.86% | 1.92% |
| 7 | 5 | 0.19% | 99.05% | 0.86% |
| 8 | 3 | 0.11% | 99.16% | 0.59% |
| 9 | 3 | 0.11% | 99.28% | 0.66% |
| 10 | 6 | 0.23% | 99.51% | 1.48% |
| 12–17 | 8 | 0.30% | 99.81% | 2.78% |
| **21, 22, 25, 27, 27** | **5** | **0.19%** | **100.00%** | **1.99%** |

Excluding the eight small process bring-up and port runs (`tt03p5`, `ttihp0p1`–`0p4`,
`ttgf0p1`–`0p3`), which exist to port existing designs to a new PDK rather than to attract new
ones, the shape barely moves: 69.87% on one shuttle, 22.91% on two, 4.05% on three, and a tail
reaching 19.

## What it shows

**Yes, participation is long-tailed — and the shape was guessed almost exactly right at the
two-shuttle end.** A guess of "20% on two shuttles, the rest on one" lands on a measured 22.9% and
69.9%. The guess was too generous further out: 4 shuttles is 1.4% of designers, not 10%, and the
people on nearly every shuttle are **five individuals**, not 5%.

**"Nobody comes back" is too strong and should not be repeated.** The correct statements are:

- **30.9% of designers return for at least one more shuttle** (814 of 2,634).
- **Repeat designers account for 55.2% of all participations** (2,245 of 4,065).

These are the two numbers that get confused, and they point in opposite directions — which is
exactly the error this repository already caught once, in `OPG-1`. A minority who return, each
returning several times, produces both facts simultaneously. Neither is "nobody comes back".

**Concentration is real but moderate:**

| | Share of all participations |
|---|---|
| Top 1% of designers | 8.7% |
| Top 5% | 19.8% |
| Top 10% | 28.1% |
| Top 20% | 41.1% |

Mean participations per designer: **1.54**.

## And the educational objection is correct

A one-shuttle majority is what an educational programme is *supposed* to produce. A course that
retained most of its students indefinitely would be failing at its purpose. The right question is
not "why do 69% leave" but **"what fraction of a cohort converts to continued use, and is that
good?"** — and 30.9% returning at least once is a strong conversion rate for an educational
product by any ordinary standard.

The honest limitation cuts the other way, though: this file measures returning to **Tiny Tapeout**,
and Tiny Tapeout is a €70 educational tile, not a commercial tape-out. It cannot tell us whether
those designers go on to buy anything. **The transition this project actually needs evidence for is
Tiny Tapeout → a paid commercial run, and nothing here measures it.** That remains the gap named in
H5's Needs list: cases of a small chip customer becoming a large one.

## What this changes

- The "nobody comes back" framing in [`data-cuts-and-statistics.md`](data-cuts-and-statistics.md)
  §2 and in H5's Challenges list should be read against this table. The underlying arithmetic there
  was not wrong; the summary sentence was.
- The recurring-core estimate of "~1,250 people worldwide" is in the right region: 814 designers
  have returned at least once, and 2,634 have participated at all.
- **H10 (skewed outcomes)** gains a little: participation *is* skewed, with five people on 21–27
  shuttles. But it is not a power law — see `data-cuts-and-statistics.md` — and the top 20% hold
  41.1% of participations, which is skewed, not extreme.

## Method

1. `GET https://index.tinytapeout.com/` returns JSON listing every shuttle with its `id`.
2. For each `id`, `GET https://index.tinytapeout.com/<id>.json`; each project carries an `author`
   field. **A browser `User-Agent` is required** — the default Python `urllib` agent gets HTTP 403,
   while `curl` succeeds on the index. This is recorded because it silently blocks naive scripts.
3. Author names are normalised with Unicode NFKC, lower-cased, and internal whitespace collapsed,
   then a designer is counted once per distinct shuttle.

**Caveat on identity.** The `author` field is free text. Normalisation merges "Lucy Revi" and
"lucy  revi" but cannot merge a person who used a handle on one shuttle and a legal name on
another, nor split two distinct people sharing a common name. This biases the one-shuttle share
**upward** (the same person under two spellings counts as two one-shuttle designers), so the true
return rate is probably somewhat higher than 30.9%. It cannot bias in the other direction except
through name collisions, which are rare at this scale.
