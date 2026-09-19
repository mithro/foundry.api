# Cutting the data: what survives, what does not

*Adversarial re-analysis of the evidence in [`../`](../), computed 2026-09-18/19. Every number below
is either quoted from a repository entry or computed by a script printed in place. Where a figure in
the repository is derived, it has been recomputed from the quoted primary numbers and the answer is
stated even when it disagrees with us.*

**Status: in progress.** Sections are committed as they are finished. The verdict table and the
arithmetic errata are at the end and are being filled in as the cuts complete.

---

## 1. Method

### 1.1 The rule this document obeys

The central claim under test is a **contrast between two populations**: commercial chip demand behind
conventional foundry access (claimed flat or falling in *number of customers*), and open-entry
programmes (claimed to be growing sharply).

**The two populations are compared by trend and direction only, never by level.** A Gartner "design
start" is a unique tapeout of a product a company expects to sell. A Tiny Tapeout "design" is a
0.018 mm² tile on a shared die. They are not commensurable and no ratio, difference or common axis
between them is meaningful. `design-starts-and-mature-nodes.md` states this rule at the top of the
file and this document keeps it.

That rule costs more than it looks. It means the strongest available form of the project's claim is
not "more chips are being made" but "two series are moving in opposite directions", and a
two-direction claim is only as good as the two trends. Section 2 tests both.

### 1.2 What can and cannot be computed with this evidence

**Can be computed:**

- Growth rates on any series with three or more dated points.
- Concentration measures — Gini, Herfindahl `H = Σsᵢ²`, effective number `1/H`, top-decile share —
  wherever per-unit counts exist. They exist in exactly four places: Tiny Tapeout's per-project
  indexes (§3), IHP's per-customer registered area (`OPG-11`), TSMC's three disclosed shares
  (`CONC-1`, `CONC-11`), and JLC's top-five (`SMB-1`).
- Exact-arithmetic checks on every `DERIVED` figure in the repository (§8).
- Sensitivity: how far an input must move before a conclusion flips (§7).

**Cannot be computed, and no amount of care fixes it:**

- **Any margin for any open-PDK programme.** No operator publishes cost. `OPG-1`'s caveat is exactly
  right: the sheet says how many people bought, not whether selling to them paid. Every statement in
  this document about H6 is therefore about analogues, never about a measurement of a shuttle.
- **A confidence interval on a survey with no published base.** The 14% → 38% industrial share
  (`DEM-10`) has no sample size anywhere. §9 computes what sample size *would* be needed; it does
  not compute a CI, because none exists.
- **A power-law fit on eight points.** IHP's eight registered customers cannot support a
  distributional test and §4 says so rather than fitting one anyway.
- **Anything about people, from the Efabless data.** `Participants` cannot be added across shuttles.
  The repository already bounds the distinct-person count at 578–1,232 and that is the best anyone
  can do from what survives.

### 1.3 A new data source, and why it matters

The one place where genuine **per-designer** data exists is the public Tiny Tapeout shuttle indexes
at `https://index.tinytapeout.com/<slug>.json`, one file per shuttle, each listing every project on
that die with an `author` field. Twenty-four of them were fetched on 2026-09-18 (`tt01`, `tt10` and
`ttihp26b` return 404). Nothing in `resources/` uses them. They are the only dataset in the entire
evidence base that can answer "how many distinct people, how often do they come back, and how
skewed is the distribution" without assumption. §3 and §4 are built on them.

Two caveats on that source, stated before any conclusion rests on it:

1. **An `author` string is not an identity.** Names are normalised here (lower-cased, parentheticals
   and punctuation stripped) but "ReJ aka Renaldas Zioma" and "Renaldas Zioma" still resolve to two
   strings, and group entries ("SPC Engineering Club", "FH Joanneum", "Tiny Tapeout") are single
   strings covering many people. The designer count below is therefore an **over-count of strings
   and an under-count of humans inside group entries**, in unknown proportion.
2. **The index lists what was on the die, not what was submitted.** TT03's index carries 249
   projects, of which `DEM-3` records only 100 as new submissions and 149 as re-runs of TT02. That
   distinction turns out to matter enormously and is the subject of §3.2.

### 1.4 Honest limits

- Most of these series have **n between 3 and 8**. A three-point trend is not a finding and this
  document labels it so every time.
- The two populations are measured in **almost disjoint time windows**. The Gartner decline is
  1994–2013; the open-programme growth is 2020–2026. There is no year in which a credible
  traditional-decline series and a credible open-growth series are both measured. §2.2 makes this
  explicit because it is, on its own, a serious problem for the two-population claim.
- Every open-programme count is produced by the operator, from its own database, with no independent
  audit anywhere. `OPG-4`'s caveat is correct: "It is a consistency check between two views of one
  vendor's database, not corroboration by an unrelated party."

---

## 3. Cut: the Tiny Tapeout distribution, from real per-designer data

### 3.1 The question

The repository asserts a long tail. It has never fitted one. With 4,562 project records carrying
author names across 24 shuttles, the distribution can be measured.

### 3.2 The finding that changes the growth series: a large share of "designs" are re-runs

Before any distribution, one thing has to be taken out. Some Tiny Tapeout shuttles are
**process bring-up runs that re-tape existing designs on a new process**, not new demand. The
indexes make this visible for the first time: a record is flagged as a re-run if its macro name, or
its (author, title) pair, has appeared on an earlier shuttle.

```python
# tmp/tt_reruns.py  (abridged)
seen_mac, seen_at = set(), set()
for sl in ORDER:                       # shuttles in deadline order
    for mac, author, title in proj[sl]:
        if mac in seen_mac or (author, title) in seen_at:
            rerun[Y[sl]] += 1
        else:
            new[Y[sl]] += 1
        seen_mac.add(mac); seen_at.add((author, title))
```

| Shuttle | Deadline | Designs | First-time | Re-runs | Re-run share |
|---|---|---:|---:|---:|---:|
| tt02 | 2022-12-02 | 166 | 164 | 2 | 0.012 |
| tt03 | 2023-04-23 | 249 | 89 | 160 | **0.643** |
| tt04 | 2023-09-08 | 143 | 139 | 4 | 0.028 |
| tt05 | 2023-11-04 | 173 | 159 | 14 | 0.081 |
| tt06 | 2024-04-19 | 238 | 227 | 11 | 0.046 |
| tt07 | 2024-06-01 | 120 | 107 | 13 | 0.108 |
| tt08 | 2024-09-06 | 135 | 117 | 18 | 0.133 |
| ttihp0p2 | 2024-11-04 | 95 | 26 | 69 | **0.726** |
| tt09 | 2024-11-10 | 369 | 331 | 38 | 0.103 |
| ttihp25a | 2025-03-12 | 564 | 131 | 433 | **0.768** |
| ttihp0p3 | 2025-05-19 | 23 | 14 | 9 | 0.391 |
| ttcad25a | 2025-06-10 | 257 | 20 | 237 | **0.922** |
| ttihp25b | 2025-09-01 | 81 | 64 | 17 | 0.210 |
| ttsky25a | 2025-09-15 | 237 | 153 | 84 | 0.354 |
| ttsky25b | 2025-11-10 | 316 | 278 | 38 | 0.120 |
| ttgf0p2 | 2025-11-24 | 52 | 16 | 36 | **0.692** |
| ttihp26a | 2026-03-23 | 283 | 263 | 20 | 0.071 |
| ttihp0p4 | 2026-03-28 | 40 | 7 | 33 | **0.825** |
| ttsky26a | 2026-05-11 | 289 | 254 | 35 | 0.121 |
| ttsky26b | 2026-05-18 | 273 | 241 | 32 | 0.117 |
| ttgf26a | 2026-06-22 | 95 | 79 | 16 | 0.168 |
| ttgf26b | 2026-06-22 | 90 | 78 | 12 | 0.133 |
| ttgf0p3 | 2026-07-03 | 32 | 14 | 18 | 0.562 |
| ttsky26c | 2026-09-07 | 242 | 215 | 27 | 0.112 |

By year:

| Year | All design records | First-time designs | Re-runs | Re-run share |
|---|---:|---:|---:|---:|
| 2022 | 166 | 164 | 2 | 0.012 |
| 2023 | 565 | 387 | 178 | 0.315 |
| 2024 | 957 | 808 | 149 | 0.156 |
| **2025** | **1,530** | **676** | **854** | **0.558** |
| 2026 (to Sep) | 1,344 | 1,151 | 193 | 0.144 |

**In 2025, 56% of Tiny Tapeout's record year was the same designs run again.** Three shuttles do
almost all of it: `ttihp25a` (433 re-runs of 564), `ttcad25a` (237 of 257) and `ttgf0p2` (36 of 52).
Those are the IHP mass-port run, the Cadence run and the GF bring-up run — a deliberate,
well-motivated engineering exercise in porting an existing library to three new processes, and not
a signal of new demand.

What this does to the growth rate:

| Window | All design records | First-time designs |
|---|---:|---:|
| 2023 → 2025 CAGR | **+64.6 %/yr** | **+32.2 %/yr** |
| 2023 → 2026 CAGR (2026 partial, so a lower bound) | +33.5 %/yr | +43.8 %/yr |

The headline growth rate roughly **halves** on the matched complete-year window once re-runs are
removed. The growth is still large and still positive — this is not a debunking — but the
repository's "1,632 submissions in 2025" and "4,268 designs" figures should never be quoted as a
count of *distinct designs*, and the 2025 step in particular is an artefact of three port runs.

### 3.3 Who submits: concentration across designers

```python
# tmp/tt_dist.py  (abridged)
cnt = collections.Counter(normalised_author for each design record)
x   = np.array(sorted(cnt.values())[::-1], float)      # designs per designer, descending
s   = x / x.sum();  H = float(np.sum(s**2))
gini = (2*np.sum(np.arange(1,len(x)+1)*np.sort(x))/(len(x)*x.sum())) - (len(x)+1)/len(x)
```

Result, over 4,409 design records (TT03's carried-over re-runs removed) and 2,625 normalised
designer strings:

| Measure | Value |
|---|---:|
| Distinct designer strings | 2,625 |
| Designs | 4,409 |
| Mean designs per designer | **1.68** |
| Median / max | 1 / 150 |
| **Gini** | **0.356** |
| Herfindahl `H` | 0.002642 |
| **Effective number of designers `1/H`** | **378.5** |
| Top decile share of designs | 0.367 |
| Top 1% share | 0.169 |
| Top ten designers' share | 0.118 |
| Designers with exactly one design | **0.736** |
| Repeat rate (≥ 2 designs) | **0.264** |
| Share of designs by repeat designers | 0.562 |
| Designers appearing on more than one shuttle | 0.234 |
| Mean shuttles per designer | 1.43 |

**This is a long tail, and it is a mild one.** A Gini of 0.36 is less unequal than household income
in most countries. The effective number of designers is 378 out of 2,625 — compare TSMC's effective
customer count of 11.8 out of 522 (`big-customers-big-bets.md`). By the measure the repository
itself adopted for customer concentration, **Tiny Tapeout's design base is about thirty-two times
less concentrated than TSMC's revenue base**. That is a real and defensible result for H7, and it is
the first time it has been computed rather than asserted.

But the same table cuts hard against H5. Three-quarters of designers make exactly one design. The
top ten designer strings — several of whom are Tiny Tapeout's own staff and instructors — account
for 12% of everything. And the single largest string (150 designs) is the programme's founder-side
account.

### 3.4 The cohort table: almost nobody comes back

| Year | Designs | Active designers | First-time | New share | Retained from prior year |
|---|---:|---:|---:|---:|---:|
| 2022 | 166 | 122 | 122 | 1.000 | — |
| 2023 | 412 | 335 | 316 | 0.943 | 0.156 |
| 2024 | 957 | 666 | 613 | 0.920 | 0.143 |
| 2025 | 1,530 | 971 | 553 | 0.570 | 0.616 |
| 2026 (to Sep) | 1,344 | 1,094 | 1,021 | 0.933 | 0.063 |

The 2025 anomaly is the same artefact as §3.2. Per shuttle, the share of designers who had appeared
before is:

| Kind of run | Shuttles | Share of designers seen before |
|---|---|---:|
| Ordinary new-design shuttles | tt04–tt09, ttsky25a/b, ttsky26a/b/c, ttihp25b, ttihp26a, ttgf26a/b | **0.10 – 0.34** |
| Port / bring-up runs | ttihp0p2, ttihp0p3, ttihp0p4, ttgf0p2, ttgf0p3, ttcad25a, ttihp25a | **0.55 – 0.95** |

**On an ordinary shuttle, roughly 85–90% of the designers have never used the programme before.**
Year-on-year designer retention outside the port runs is 6–16%.

**What this means.** Read one way it is the best possible news for H5: the population is not
exhausted, new people keep arriving in larger numbers every year, and the programme is not simply
recirculating a fixed community. Read the other way it is the worst possible news for H6: a customer
who buys once and never returns has a lifetime value of one purchase, and a business whose
annual churn is 85–90% must acquire its entire customer base again every year, forever. §5 models
what that does to lifetime value explicitly.

Note also that this **contradicts the Efabless reading in `OPG-1`**, which says "about two-thirds of
all submissions … came from people who had submitted before" and concludes "the base is much
narrower than the submission count suggests". On Tiny Tapeout's own per-designer data the opposite
holds: 74% of designers appear once, and the share of *submissions* from repeaters (56%) is high
only because a small number of people submit a great many. The two statistics — share of purchases
from repeaters, and share of purchasers who repeat — point in opposite directions, and the
repository has been quoting the first as though it implied the second.

### 3.5 Fill rates, by process family

From the `submission-stats` API, `tiles_used / tiles_total`, excluding shuttles not yet populated:

| Process | n | Mean fill | Min | Max |
|---|---:|---:|---:|---:|
| SKY130 | 13 | 0.828 | 0.461 (tt08) | 1.000 |
| IHP | 7 | 0.836 | 0.575 (ttihp0p4) | 1.000 |
| GF180MCU | 4 | 0.922 | 0.719 (ttgf0p3) | 1.000 |

**Simpson check.** The pooled fill rate is not the reverse of any subgroup's: all three families sit
in the 0.83–0.92 band and all three contain both full and half-empty runs. But the *time* pattern
inside SKY130 is worth stating, because the repository's H5 challenge list (`DEM-2`) quotes the
2024 trough as though it were the state of the programme:

```
tt04 0.649 · tt05 0.745 · tt06 1.000 · tt07 0.588 · tt08 0.461 · tt09 0.938 · tt10 0.469
ttcad25a 0.943 · ttsky25a 0.986 · ttsky25b 0.988 · ttsky26a 1.000 · ttsky26b 1.000 · ttsky26c 0.996
```

The last six SKY130 shuttles have all filled 94%+ and four of them filled completely. `DEM-2`'s
"9 of the 24 runs came in below 75% of capacity" is arithmetically right and chronologically
misleading: seven of those nine are either 2023–2024 runs or small bring-up shuttles. **On the
SKY130 line the fill rate has been rising monotonically since mid-2025.** That is a point in H5's
favour that the repository currently records as a point against it.

---

*Sections 2 (growth rates and the two-population claim), 4 (fitting the distribution), 5 (repeat
behaviour and lifetime value), 6 (attacking the JLC decomposition), 7 (sensitivity), 8 (arithmetic
errata), 9 (small-number statistics), 10 (verdict table) and 11 (the strongest argument against the
project) follow.*
