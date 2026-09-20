# Repeat participation on Tiny Tapeout, keyed on GitHub username

*Our own analysis, recomputed 2026-09-19 from all 28 shuttle indexes at
`https://index.tinytapeout.com/<id>.json`, fetched by GET. Supersedes an earlier version of this
file that keyed on the free-text `author` field. Method at the foot.*

---

## Why this was redone

The first version of this analysis identified designers by the `author` string in each project
record. That field is free text, so it over-counts: one person who writes "Lucy Revi" on one shuttle
and a handle on the next becomes two people. The file said so, and predicted the true return rate was
"probably somewhat higher" than it reported.

**Every project record also carries a `repo` URL, and its owner segment is a GitHub username** — a
canonical identity that GitHub itself enforces as unique. All 4,814 records have a `repo`; 4,810
parse as `github.com`, three more are the `git@github.com:` SSH form and parse once that is handled,
and exactly one says `N/A`. So the canonical key is available for **99.98%** of the data, and this is
what the file now uses.

The prediction held. Keying on GitHub username finds **fewer distinct people** (2,450 against 2,634)
and a **higher return rate** (32.9% against 30.9%), which is exactly the direction name-splitting
would cause.

## The distribution

Distinct shuttles per GitHub account, over all 28 shuttles — 2,450 accounts, 3,891
account–shuttle participations, 4,813 designs:

| Shuttles | Accounts | % of accounts | Cumulative | % of participations |
|---|---|---|---|---|
| 1 | 1,643 | **67.06%** | 67.06% | 42.23% |
| 2 | 600 | **24.49%** | 91.55% | 30.84% |
| 3 | 110 | 4.49% | 96.04% | 8.48% |
| 4 | 31 | 1.27% | 97.31% | 3.19% |
| 5 | 18 | 0.73% | 98.04% | 2.31% |
| 6 | 12 | 0.49% | 98.53% | 1.85% |
| 7 | 9 | 0.37% | 98.90% | 1.62% |
| 8 | 6 | 0.24% | 99.14% | 1.23% |
| 9 | 4 | 0.16% | 99.31% | 0.93% |
| 10 | 6 | 0.24% | 99.55% | 1.54% |
| 12–18 | 5 | 0.20% | 99.76% | 1.90% |
| 22, 24, 25, 26, 26 | 5 | 0.20% | 99.96% | 3.17% |
| **28 (every shuttle)** | **1** | **0.04%** | 100.00% | 0.72% |

Excluding the eight process bring-up and port runs, the shape is essentially unchanged: 67.75% on
one shuttle, 24.54% on two, 4.10% on three.

**Headline numbers:**

- **32.9% of accounts return** for at least one more shuttle (807 of 2,450).
- **Repeat accounts make 57.8% of all participations** (2,248 of 3,891).
- Mean shuttles per account **1.588**; mean designs per account **1.964**.
- Gini on participations **0.295**; on designs per account **0.398**.

## The guessed shape, against the measured one

A working guess of *"5% on every shuttle, 10% on four, 20% on two, the rest on one"* was right about
the shape and right at the near end, and much too generous at the far end:

| | Guess | Measured |
|---|---|---|
| One shuttle only | "the remaining" (~65%) | **67.06%** ✓ |
| Two shuttles | 20% | **24.49%** ✓ |
| Four shuttles | 10% | **1.27%** ✗ |
| Every shuttle | 5% | **0.04% — one account** ✗ |

## The finding the name-based version could not see

**The account on all 28 shuttles is `tinytapeout` itself** — the programme's own GitHub
organisation, carrying 142 designs. It is infrastructure, not a customer.

The rest of the top of the table is largely the people who *run* the programme:

| Account | Shuttles | Designs | |
|---|---|---|---|
| `tinytapeout` | **28** | 142 | the project's own organisation |
| `urish` | 26 | 111 | Uri Shaked, Wokwi founder and TT collaborator |
| `mattvenn` | 26 | 82 | Matt Venn, TT founder |
| `htfab` | 25 | 68 | |
| `algofoogle` | 24 | 36 | |
| `michaelbell` | 22 | 41 | |
| `rejunity` | 18 | 59 | |
| `mole99` | 17 | 22 | |
| `dlmiles` | 14 | 31 | |
| `rebeccargb` | 13 | 65 | |

The organisation account alone is **3.0% of all designs**. Adding the two named founders takes it to
**7.0% of all designs** from three accounts. Of the 21 accounts appearing on nine or more shuttles —
together 8.2% of all participations — **three are the organisation or a founder**.

This matters for how the repeat rate should be read. The most committed repeat "customers" include
the people selling the product. That does not erase the other 804 returning accounts, but any
argument that leans on the depth of the tail should exclude the organisers first.

## Is it a long-tailed distribution?

**It is skewed, but it is not a power law over the bulk.** Fitting designs per account (excluding
the organisation account; n = 2,449, 4,671 designs, max 111, mean 1.907) and measuring the
Kolmogorov–Smirnov distance to the best-fitting discrete power law at each lower cut-off:

| k_min | α | KS distance | Accounts at or above k_min |
|---|---|---|---|
| 1 | 1.963 | **0.595** | 100.00% |
| 2 | 2.775 | **0.575** | 35.65% |
| 3 | 2.526 | 0.391 | 11.19% |
| 4 | 2.490 | 0.303 | 6.41% |
| 5 | 2.392 | 0.232 | 4.12% |
| 6 | 2.349 | 0.187 | 3.02% |
| 8 | 2.431 | 0.144 | 2.08% |
| 10 | 2.395 | 0.123 | 1.47% |

A power law requires a *small* KS distance. At k_min = 1 and 2 — which is 100% and 36% of accounts —
the fit is terrible. It only becomes respectable above about six designs, which is **3% of
accounts**. So there is a power-law-ish tail with α ≈ 2.4, sitting on a body that is not power-law
at all.

Stated plainly, designs per account:

| Designs | Accounts | % |
|---|---|---|
| 1 | 1,576 | 64.35% |
| 2 | 599 | 24.46% |
| 3 | 117 | 4.78% |
| 4 | 56 | 2.29% |
| 5–8 | 62 | 2.53% |
| **≥9** | **39** | **1.59%** |

This corroborates, on better data, the conclusion in
[`data-cuts-and-statistics.md`](data-cuts-and-statistics.md) that the distribution is not a power
law — and puts the Gini at **0.398** on designs, higher than the 0.356 that analysis reported but
still milder than household income.

## What this changes

- **"Nobody comes back" is wrong and should not be repeated.** A third of accounts return, and
  returning accounts make well over half of all participations.
- **"Year-on-year designer retention is 6–16%"** measures something much narrower — returning in the
  *next calendar year* — and should always be quoted next to the 32.9% cumulative figure, or it
  misleads.
- The recurring core is roughly **800 accounts**, of which about 40 are heavy users, and three of the
  heaviest are the organisers.
- A one-shuttle majority is the *expected* outcome for an educational programme, where cohorts are
  supposed to pass through. Judged as a course, 32.9% returning is a strong conversion rate.

**The limitation that still stands, and it is the important one:** this measures returning to Tiny
Tapeout, a €70 educational tile. It says nothing about whether any of these accounts go on to buy a
commercial run. **The transition this project needs evidence for is Tiny Tapeout → paid commercial
tape-out, and nothing here measures it.**

## Method

1. `GET https://index.tinytapeout.com/` lists every shuttle with its `id`.
2. For each id, `GET https://index.tinytapeout.com/<id>.json`; each project carries `repo`.
3. Identity key = the owner segment of the repo URL, lower-cased, matching both
   `https://github.com/<owner>/…` and `git@github.com:<owner>/…`. GitHub usernames are
   case-insensitive for identity, so lower-casing is correct and necessary.
4. **A browser `User-Agent` is required** — the default Python `urllib` agent receives HTTP 403 while
   `curl` succeeds. This silently defeats naive scripts and is recorded for the next person.

**Remaining caveats.** A person who changes their GitHub username, or who uses a personal account on
one shuttle and a university or employer organisation on another, still counts twice — so 32.9%
remains a *lower* bound on the true return rate. Conversely, a shared teaching or lab organisation
account used by many students counts as one returning participant when it is really many
non-returning ones, which pushes the other way. Neither effect can be sized from this data.
