# Cutting the data: what survives, what does not

*Adversarial re-analysis of the evidence in [`../`](../), computed 2026-09-18/19. Every number below
is either quoted from a repository entry or computed by a script printed in place. Where a figure in
the repository is derived, it has been recomputed from the quoted primary numbers and the answer is
stated even when it disagrees with us.*

**Status: complete.** Sections 1-11 below. The verdict table and the
arithmetic errata are at the end.

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

## 2. Cut: growth rates on both sides, on matched windows

### 2.1 Every series we hold

CAGR is endpoint-to-endpoint; the p-value is from a log-linear OLS regression of `log(value)` on
year, which uses every point rather than only the ends.

```python
# tmp/growth.py
def cagr(a, b, yrs): return (b/a)**(1.0/yrs) - 1.0
def ols_loggrowth(years, vals):        # slope of log(value) on year, with a t-test
    y = np.log(vals); b, a = np.polyfit(years, y, 1)
    se = sqrt(sum((y - (a+b*years))**2)/(n-2) / sum((years-years.mean())**2))
    return exp(b)-1, 2*t.sf(abs(b/se), n-2)
```

**Traditional (population 1)**

| Series | Window | n | CAGR | log-OLS p |
|---|---|---:|---:|---:|
| Gartner ASIC design starts (`TRAD-19`) | 1994–2013 | 18 | **−8.0 %** | <0.0001 |
| …measured part only | 1994–2008 | 13 | **−8.4 %** | <0.0001 |
| Europractice designs (`DEM-16`) | 2000–2025 | 26 | **+1.8 %** | 0.0000 |
| …2000–2017, the "flat" claim | 2000–2017 | 18 | **+1.5 %** | 0.0001 |
| CMP circuits (`DEM-19`) | 1993–2015 | 12 | +1.3 % | 0.141 |
| CMC prototypes (`DEM-20`) | 2017–2025 | 7 | −2.8 % | **0.796** |
| TSMC distinct products **[stock]** (`TRAD-16`) | 2019–2025 | 7 | +2.8 % | 0.096 |
| TSMC distinct customers **[stock]** (`TRAD-16`) | 2019–2025 | 7 | +1.1 % | 0.085 |

**Open (population 2)**

| Series | Window | n | CAGR | log-OLS p |
|---|---|---:|---:|---:|
| Tiny Tapeout design records | 2022–2026 | 5 | +68.7 % | 0.033 |
| Tiny Tapeout **first-time** designs | 2022–2026 | 5 | +62.8 % | 0.024 |
| Tiny Tapeout tiles sold | 2023–2026 | 4 | +76.2 % | 0.103 |
| Tiny Tapeout active designers | 2022–2026 | 5 | +73.0 % | 0.013 |
| Google Open MPW submissions (`OPG-1`) | 2020–2023 | 4 | +46.4 % | **0.452** |
| chipIgnite submissions (`OPG-7`) | 2021–2024 | 4 | +94.8 % | 0.009 |
| IHP free-MPW designs (`OPG-10`) | 2023–2025 | 3 | +483 % | 0.078 |
| Efabless community members (`OPG-15`) | 2021–2025 | 3 | +85.4 % | 0.110 |

**Three results the repository does not currently reflect.**

1. **Europractice is not flat, and it is not declining. It is rising, significantly.** Over the
   eighteen years the repository describes as "eighteen years, essentially flat … There is no sign
   here of a dam waiting to burst", the log-linear trend is **+1.5%/yr with p = 0.0001**. The 2000–2025
   trend is +1.8%/yr, also significant. `DEM-16` files this series under H5 **Challenges**. On the
   arithmetic it belongs under Supports, weakly. The range framing ("between 363 and 614 designs a
   year") conceals a 28% rise across the window.
2. **CMC's "decline" is not statistically distinguishable from noise** (p = 0.80, n = 7). `DEM-20`
   is already careful — it says "It is not a four-year decline, and the entry should not be cited as
   one" — but it still lists the series under H5 Challenges. It cannot bear that weight.
3. **Google's Open MPW growth is not significant either** (p = 0.45, n = 4), because the series is
   37 → 162 → 506 → 116 and the last year is a stub (one GF shuttle). The programme's growth is
   real per-shuttle; as an annual series it is four points with a collapse at the end caused by
   Google stopping.

### 2.2 The matched-window problem, which is the most serious finding in this section

Years in which *any* traditional series and *any* open series both have a datum: **2020–2025 only.**

- The Gartner decline — the only traditional series with a large, highly significant downward
  trend — **ends in 2013**, and its last five points are a forecast made in March 2009.
- The open-programme growth — every series of it — **begins in 2020**.

**There is not one year in which a credible traditional-decline series and a credible open-growth
series are both measured.** The two-population contrast is assembled from two non-overlapping eras.

What the overlapping years actually contain:

| Series | 2021 → 2025 | CAGR | 2022 → 2025 | CAGR |
|---|---|---:|---|---:|
| Europractice designs | 985 → 753 | **−6.5 %** | 731 → 753 | **+1.0 %** |
| CMC prototypes | 400 → 240 | −12.0 % | 498 → 240 | −21.6 % |
| TSMC products [stock] | 12,302 → 12,682 | +0.8 % | 12,698 → 12,682 | −0.0 % |
| TSMC customers [stock] | 535 → 534 | −0.0 % | 532 → 534 | +0.1 % |
| Tiny Tapeout design records | — | — | 166 → 1,530 | +109.7 % |
| Tiny Tapeout active designers | — | — | 122 → 971 | +99.7 % |

**The sign of the Europractice trend in the overlap window depends entirely on the start year:**

| Start | → 2025 CAGR | log-OLS %/yr | p | n |
|---|---:|---:|---:|---:|
| 2016 | +3.1 % | +3.4 % | 0.098 | 10 |
| 2017 | +2.6 % | +2.2 % | 0.320 | 9 |
| 2018 | +2.7 % | +0.5 % | 0.827 | 8 |
| 2019 | −2.6 % | −2.9 % | 0.152 | 7 |
| 2020 | −3.4 % | −3.5 % | 0.204 | 6 |
| **2021** | **−6.5 %** | −3.9 % | 0.343 | 5 |
| 2022 | +1.0 % | +1.2 % | 0.760 | 4 |

2021 is the all-time peak of a 26-year series, and `DEM-16`'s own caveat records that the 2019 step
up is partly the absorption of CMP's counts rather than new demand. **Nothing in the record makes
2021 the right place to start**, and no start year in the overlap window produces a significant
decline.

**Conclusion of the cut, stated plainly.** In the only window where the two populations can be
compared at all, the open side grows fast and significantly, and *the traditional side does not
decline in any statistically defensible way*. The traditional decline that the project's thesis
rests on is a 1994–2013 phenomenon. It may well still be true in 2025; nothing we hold measures it.
The honest version of the two-population claim is therefore: **"open programmes are growing
sharply, and the conventional route has been flat-to-slightly-up for a quarter of a century."**
That is a weaker but genuinely supported claim, and it is close to the narrower statement
`design-starts-and-mature-nodes.md` already reaches by a different route.

### 2.3 The Gartner decline itself is two recessions

| Window | CAGR | log-OLS %/yr | p | n |
|---|---:|---:|---:|---:|
| 1994–2013 | −8.0 % | −9.8 % | <0.00001 | 18 |
| 1997–2013 | −10.1 % | −10.3 % | <0.00001 | 15 |
| 2000–2013 | −9.8 % | −8.6 % | <0.00001 | 12 |
| 2002–2013 | −6.0 % | −6.9 % | 0.00001 | 10 |
| **2002–2008 (between the recessions)** | — | **−5.2 %** | 0.007 | 5 |

The decline is real and significant under every start year. But it is about **−5%/yr between the
two recessions** and about −10%/yr when 2001 and 2009 are included. `TRAD-6` already says
"Fitting a single exponential across 2000–2012 attributes to a secular trend what is substantially
two recessions"; this quantifies it. The secular part is roughly half the headline.

### 2.4 Free versus paid — the cut that was expected to be decisive, and is not

| | Window | From → to | CAGR |
|---|---|---|---:|
| **Free / subsidised** | | | |
| Google Open MPW (Google-funded) | 2020–2023 | 37 → 116 | +46.4 % |
| IHP free MPW (German public funds) | 2023–2025 | 2 → 68 | +483 % |
| Europractice (EU-subsidised) | 2000–2025 | 480 → 753 | +1.8 % |
| CMC (Canadian public funds) | 2017–2025 | 300 → 240 | −2.8 % |
| **Paid** | | | |
| chipIgnite submissions ($9,750–$14,950) | 2021–2024 | 51 → 377 | **+94.8 %** |
| Tiny Tapeout tiles (€70–$300) | 2023–2026 | 510 → 2,788 | **+76.2 %** |
| Tiny Tapeout active designers | 2022–2026 | 122 → 1,094 | **+73.0 %** |
| wafer.space backers | 2025–2026 | 6 → 23 | +283 % (n = 2) |
| **ChipFoundry `committed` (paid)** | 2025–2026 | 44 → 45 | **+2.3 %** |
| ChipFoundry `interest` (unpaid) | 2025–2026 | 129 → 262 | +103 % |

**This cut does not undermine the growth claim; it strengthens it.** The paid series grow *faster*
than the subsidised ones. The IHP row is meaningless (a base of 2) and the wafer.space row has n = 2,
but chipIgnite and Tiny Tapeout are the two longest paid series and both are near +80%/yr. The
project's "demand appears when the price falls" story is supported by demand that people *paid for*,
which is precisely the evidence the repository says it is weakest on.

**The one place it bites — and it bites in exactly one place.**

> ### ⚠️ Correction, 2026-09-20 — reservations are not a general feature
>
> This paragraph previously said ChipFoundry's `committed` field was "the only series in the entire
> evidence base that counts money committed rather than interest expressed". **That is wrong, and
> the error matters because it licensed a discount that was then applied too widely.**
>
> **The $500 reservation tier is peculiar to ChipFoundry and Efabless.** Only those two operate a
> funnel with an intermediate, cheap, non-binding state between "interested" and "paid". Everywhere
> else there is no such state:
>
> | Programme | What its numbers are |
> |---|---|
> | **wafer.space** | **Actual sales.** Crowd Supply backers have paid. There is no reservation concept. |
> | **Tiny Tapeout** | **Actual sales.** Reservations are at **full price, non-transferable and non-refundable** — they are purchases, not options. |
> | **Google Open MPW** | No reservation concept. Submissions were free applications to a subsidised programme; the manufactured count is real fabrication. The gap here is *selection*, not payment. |
> | **ChipFoundry / Efabless** | **The only ones known to have a $500 reservation tier**, hence the only ones where `reserved` and `committed` differ. |
> | **Europractice, CMP, CMC, MOSIS** | **Not established.** How these price and reserve, and whether any deposit or cancellable booking sits between application and fabrication, has not been checked. Do not assume either way. |
>
> So ChipFoundry's `interest → committed` conversion is a measurement of **ChipFoundry's own
> funnel**, not a universal discount factor. It must never be applied to wafer.space backer counts
> or Tiny Tapeout tile counts, which are money already paid.

ChipFoundry's `committed` field is **+2.3%/yr** against +103%/yr for `interest` on the same
shuttles. Two points is not a trend and this must not be presented as one. It remains the only
direct measurement of the interest-to-payment gap *in a programme that has such a gap*.

### 2.5 Drop-one-programme robustness

Is "open programmes grow" driven by Tiny Tapeout alone? The only window in which more than one open
series has both endpoints is **2023 → 2024**; chipIgnite dies in 2024 and ChipFoundry and
wafer.space start in 2025, so no open aggregate spans more than two consecutive years.

| Aggregate (2023 → 2024) | From | To | Change |
|---|---:|---:|---:|
| all three (TT tiles + chipIgnite + IHP) | 737 | 2,163 | **+193.5 %** |
| drop Tiny Tapeout | 227 | 394 | **+73.6 %** |
| drop chipIgnite | 512 | 1,786 | +248.8 % |
| drop IHP | 735 | 2,146 | +192.0 % |

**The conclusion survives.** Removing Tiny Tapeout cuts the growth rate by roughly two-thirds but
leaves it strongly positive: chipIgnite on its own grew +67.6% that year and +94.8%/yr over
2021–2024. The growth finding is **not** an artefact of one programme.

Two cautions. First, these three series count different objects (tiles, submissions, designs) and
adding them is only defensible as a robustness check, never as a level. Second, **Tiny Tapeout's
tiles sit inside chipIgnite's and IHP's slots**, so the aggregate double-counts; `OPG-11` says
exactly this ("Do not add IHP's customer count to Tiny Tapeout's design count"). The drop-one test
is valid because it only asks whether the sign survives; the aggregate itself should not be quoted.

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

## 4. Cut: is it actually a power law? (No.)

### 4.1 The question

`TAIL-1` asserts a long tail. `ECON-17` (Clauset, Shalizi & Newman) warns that most published
power-law claims fail a proper test. Nobody has run the test on anything in this repository. With
2,625 designers and 4,409 designs, it can be run.

### 4.2 The procedure and the result

Discrete power law `p(k) ∝ k^−α` for `k ≥ k_min`; α by MLE on the discrete likelihood with a
Hurwitz-zeta normalisation; `k_min` chosen to minimise the discrete KS distance
`D = max_v |F_emp(v) − F_fit(v)|`; goodness of fit by the CSN synthetic-data bootstrap.

```python
# tmp/fitdist.py  (abridged)
def nll(alpha, d, kmin):  return len(d)*np.log(zeta(alpha, kmin)) + alpha*np.sum(np.log(d))
def ks(d, alpha, kmin):
    v, c = np.unique(np.sort(d), return_counts=True)
    return np.max(np.abs(np.cumsum(c)/len(d) - (1 - zeta(alpha, v+1)/zeta(alpha, kmin))))
# kmin chosen by minimising ks; GOF p = share of synthetic power-law datasets with D >= D_obs
```

| `k_min` | n in tail | α̂ | KS `D` | CSN GOF `p` | Verdict (CSN rule: p < 0.1 rules it out) |
|---|---:|---:|---:|---:|---|
| 1 | 2,625 | 2.605 | 0.0306 | **0.000** | **ruled out** |
| 2 | 692 | 3.066 | 0.0462 | **0.000** | **ruled out** |
| 3 | 224 | 2.684 | 0.0484 | 0.085 | ruled out (marginally) |
| 4 | 118 | 2.504 | 0.0445 | 0.476 | not ruled out |
| 5 | 76 | 2.389 | 0.0495 | 0.673 | not ruled out |

**The distribution of designs per designer is not a power law.** It is ruled out over the whole
range and over the body. A power law cannot be rejected only on the extreme tail — the 76 to 118
designers with four or more designs, which is 3–4% of the population. A Vuong likelihood-ratio test
against a discrete lognormal on the full range is inconclusive (R = −6.33, z = −1.31, p = 0.192): the
data do not distinguish the two.

**What to do with this.** The honest statement is: *designs per designer are moderately skewed, with
a heavy-ish upper tail consistent with a power law of exponent ≈ 2.5 above four designs, and nothing
resembling a power law below that.* Any sentence in `WHY.md` or `PRINCIPLES.md` of the form "the
distribution is a power law" should be struck. The useful properties — that a few participants do a
lot and most do one thing — survive without the label, and they are better measured by the Gini and
the Herfindahl than by an exponent.

### 4.3 Concentration, measured the same way everywhere

Every dataset in the repository with per-unit counts, put through the same three measures. Gini and
`1/H` are dimensionless shape measures, so comparing them across populations does **not** violate
the trends-not-levels rule — it compares the *shape* of two distributions, not their size.

| Dataset | n | Gini | `H` | `1/H` | Top-decile share |
|---|---:|---:|---:|---:|---:|
| Tiny Tapeout: designs per designer | 2,625 | 0.356 | 0.00264 | **378.5** | 0.367 |
| Efabless: submissions per shuttle | 23 | 0.291 | 0.0550 | 18.2 | 0.168 |
| TSMC 2024: revenue per customer | 522 | 0.745 | 0.0850 | **11.8** | 0.780 |
| TSMC 2025: revenue per customer | 534 | 0.765 | 0.0871 | 11.5 | 0.798 |
| JLC 2025: revenue per paying user | 1,358,700 | — | 2.82 × 10⁻⁵ | 35,487 | — |
| IHP SG13G2: mm² per customer | 8 | 0.571 | 0.285 | 3.5 | 0.405 |
| IHP CMOS5L: mm² per customer | 3 | 0.307 | 0.465 | 2.1 | 0.629 |
| wafer.space: backers per run | 3 | 0.299 | 0.458 | 2.2 | 0.621 |
| ChipFoundry: committed per shuttle | 3 | 0.073 | 0.340 | 2.9 | 0.397 |

Bootstrap 95% CIs on the Tiny Tapeout figures (3,000 resamples of designers):

| | Point | 95% CI |
|---|---:|---|
| Gini | 0.356 | [0.300, 0.413] |
| `H` | 0.00264 | [0.0011, 0.0046] |
| `1/H` | 378.5 | [219, 950] |
| Top-decile share | 0.367 | [0.312, 0.422] |

Dropping the single largest designer string (150 designs — a programme-side account) moves Gini to
0.334 and `1/H` to 628. **The concentration result is not driven by one participant**, which is the
drop-one test for §4.

**The comparison that matters, and it favours the project.** The effective number of participants as
a share of the nominal number is 14.4% for Tiny Tapeout's designers against **2.3% for TSMC's
customers**. Whatever else is true, the open programme's activity really is spread across a far
larger effective base than a foundry's revenue is. This is the cleanest quantitative support H7 has
ever had, and it was not in the repository.

**Four cautions that must travel with it.**

1. TSMC's number is revenue; Tiny Tapeout's is design count. Money and activity are different
   things, and the money version of the Tiny Tapeout number would be more concentrated (larger
   designs cost more tiles).
2. The TSMC figures rest on an even-split assumption inside two undisclosed blocks; the repository
   already shows the answer moves from 11.8 to 7.0 if the tail is correlated.
3. The JLC row is **not usable**. An even split below the disclosed top five is an upper bound on
   the effective number, and the true value is unknowable from the filing. It is printed only so the
   assumption is visible.
4. Four of the nine rows have n ≤ 8. `1/H` on three points is arithmetic, not evidence. **The IHP,
   wafer.space and ChipFoundry rows should never be quoted.** They are in the table to show how
   little per-customer data exists, not to support a conclusion.

---

## 5. Cut: repeat behaviour, and what a 26% repeat rate is worth

### 5.1 The cohort table, with censoring stated

Designers are assigned to the cohort of the year they first appear; "lifetime designs" counts every
design they have made up to 2026-09.

| Cohort | Designers | Mean lifetime designs | Share who ever repeat | Years observed |
|---|---:|---:|---:|---:|
| 2022 | 122 | 4.02 | 0.934 | 4 |
| 2023 | 316 | 2.55 | 0.203 | 3 |
| 2024 | 613 | 2.30 | 0.659 | 2 |
| 2025 | 553 | 1.31 | 0.204 | 1 |
| 2026 | 1,021 | 1.11 | 0.066 | 0 |
| **All** | **2,625** | **1.74** | **0.290** | — |

(These use the full index including TT03's carried-over re-runs; with those removed the overall mean
is 1.68 and the repeat rate 0.264. The difference does not change any conclusion.)

The 2022 and 2024 cohorts look anomalous for the reason in §3.2 — they were swept up in the 2025
port runs, which re-ran their designs. **The only clean cohorts are 2023 and 2025**, and their
"ever repeat" rates are 0.203 and 0.204.

**A realistic estimate of eventual lifetime purchases per acquired designer is therefore 2.5 with
three years to run, and about 1.7 on the full censored population.**

### 5.2 The repeat data rule out a homogeneous customer base

```python
P1 = mean(v == 1) = 0.7097       # share of designers with exactly one design
mean = 1.7379                    # mean designs per designer
# homogeneous geometric: after each purchase you return with probability p
p = 1 - P1 = 0.2903  ->  implied mean = 1/(1-p) = 1.4090
```

The homogeneous model **under-predicts the observed mean by 23%**. Fitting a two-segment mixture
(share *q* buy once and never return; the rest return with probability *p₂* each time) to the same
two moments:

| Segment | Share of designers | Repeat probability | Expected lifetime designs |
|---|---:|---:|---:|
| One-and-done | 52.1% | 0 | 1.00 |
| Core | 47.9% | 0.607 | 2.54 |

**The core is about 1,256 designers producing roughly 70% of all designs.** This is the real shape
of the customer base: half the people who ever arrive buy once, and a persistent minority of about
1,250 people worldwide account for most of the activity.

That number — **roughly 1,250 recurring participants, worldwide, after four years, at a price
between €70 and $300** — is the single most important quantity in this document, and it should be
the number the project argues against, not 4,268.

### 5.3 Lifetime value, and the size of the line in money

Tiles sold per year, from `tiles_used` in the submission-stats API:

| Year | Tiles |
|---|---:|
| 2023 | 510 |
| 2024 | 1,769 |
| 2025 | 2,661 |
| 2026 (to September) | 2,788 |
| **Total** | **7,728** |

| Price basis | Lifetime gross revenue | 2025 gross revenue |
|---|---:|---:|
| €70 per tile (`SMB-10`, shuttle inclusion only) | **€540,960** | €186,270 |
| €150 all-in tile + ASIC + board (2025 IHP price, `OPG-14`) | €1,159,200 | €399,150 |
| $300 all-in standard price (TT06 era, `OPG-14`) | $2,318,400 | $798,300 |

Lifetime value per acquired designer, at the observed mean of 1.74 designs:

| Price per design | LTV, for ever |
|---|---:|
| €70 | **€122** |
| €150 | €261 |
| $300 | $521 |

**What this means.** The entire worldwide output of the most successful open-silicon programme ever
run is, on its own published prices, between half a million and two and a third million dollars of
gross revenue across four years. `SMB-5` records MOSIS at "up to $10 million annually at its peak" —
in 1990s money. Set beside `SMB-1`'s JLC at CNY 10.29 bn, or against the $14,950 cost of the single
chipIgnite slot each Tiny Tapeout shuttle occupies, the scale is the finding.

A full 512-tile SKY130 shuttle sells €35,840 of tile inclusion against a $14,950 slot. That is a
real gross margin on the shuttle purchase, and it says nothing about PCBs, packaging, shipping, the
devkit bill of materials, or anybody's time — none of which is published anywhere.

**The honest reading for H6.** A lifetime value of €122–$521 per customer, with 85–90% of customers
never returning, is a business that must be almost entirely self-serve and almost entirely
word-of-mouth, because there is no room in that number for a sales motion, a support call, or a
customer-acquisition spend of more than a few tens of euros. That is *consistent* with what
`PRINCIPLES.md` proposes. It is also exactly what `OPG-16` means by "a tough customer base to profit
from", and this is the first time the repository has been able to put a figure on it.

---

## 6. Cut: attacking the JLC decomposition

[`long-tail-pays-for-the-capital.md`](long-tail-pays-for-the-capital.md) is the strongest single
piece of evidence in the repository. It is attacked here from scratch, with every input taken from
the `SMB-1` quotes and nothing taken from the analysis.

### 6.1 The arithmetic is right

```python
# tmp/jlc.py -- the p.245 table, four leaf rows + two subtotals per year
blend_leaf = sum(share*margin for the four channel rows)
blend_sub  = share_ss*margin_ss + share_big*margin_big
```

| Year | Leaf-level Σ(share × margin) | Subtotal-level | Printed 合计 (total) | Largest discrepancy |
|---|---:|---:|---:|---:|
| 2023 | 0.28735 | 0.28729 | 0.2873 | +0.0049 pp |
| 2024 | 0.30046 | 0.30048 | 0.3005 | −0.0042 pp |
| 2025 | 0.28058 | 0.28061 | 0.2806 | −0.0024 pp |

The revenue shares also sum to 1.0000 in every year. **The disclosure reconciles and the analysis's
reconciliation claim ("agreeing to within 0.005 pp in all three years") is exactly right.**

The share-of-gross-profit headline reproduces to four decimal places:

| Year | Long tail's share of gross profit | Analysis |
|---|---:|---|
| 2023 | 0.9131 | 91.31% ✓ |
| 2024 | 0.9381 | 93.81% ✓ |
| 2025 | **0.9760** | 97.60% ✓ |

**No arithmetic error was found anywhere in this document.** Everything below is about
interpretation.

### 6.2 Fragility 1 — the 13.1× is a ratio with a collapsing denominator

| Year | Revenue per 1 of gross profit, long tail | …big batch | Ratio |
|---|---:|---:|---:|
| 2023 | 2.84 | 10.27 | **3.62×** |
| 2024 | 2.68 | 13.11 | **4.89×** |
| 2025 | 2.76 | 36.23 | **13.13×** |

The headline "13.1×" nearly **quadrupled in two years** while the long tail's own margin went
35.27 → 37.28 → 36.24, i.e. flat. **The entire movement is in the denominator.** Sensitivity:

| Big-batch margin | Ratio | vs printed |
|---|---:|---:|
| 0.76% | 47.7× | +263% |
| 1.76% | 20.6× | +57% |
| **2.76% (as printed)** | **13.1×** | — |
| 3.76% | 9.6× | −27% |
| 5.76% | 6.3× | −52% |
| 9.74% (the 2023 value) | 3.7× | −72% |

**A one-percentage-point error in a single printed number moves the headline from 13.1× to 9.6× or
20.6×.** This is the most fragile figure in the repository. It should be quoted as "the long tail
generates most of the gross profit, and the multiple has ranged from 3.6× to 13.1× across three
disclosed years", never as "13.1×".

### 6.3 Fragility 2 — the counterfactual assumes overhead is fully variable

The analysis holds "everything below the gross line" at 15.50 pp of revenue, derived as group gross
margin (28.15%) minus group net margin (12.65%), and then applies it to **PCB-only** segment
margins. Two problems, one fatal and one not.

**Not fatal.** The 15.50 pp is treated as variable in revenue, but removing the big-batch segment
removes 24.43% of PCB revenue from the same plant. If any of that overhead is fixed, the ratio
rises:

| Share of overhead assumed fixed | Overhead ratio | Long-tail-only net margin |
|---|---:|---:|
| 0% (as in the analysis) | 15.50% | **+20.74%** |
| 25% | 16.75% | +19.49% |
| 50% | 18.01% | +18.23% |
| 75% | 19.26% | +16.98% |
| **100%** | 20.51% | **+15.73%** |

**The "a sample-and-small-batch-only JLC would be more profitable" conclusion survives even if every
penny of overhead is fixed.** That is a strong result and it should be stated: it is robust to a
100% error in the key assumption.

**The mirror conclusion is not symmetric** and the analysis does not say so. On the same logic the
big-batch-only counterfactual goes from −12.74% to −60.69% as overhead is moved from fully variable
to fully fixed. The "−12.74%" printed in the analysis is the *most favourable* value in the range.

**Fatal to the presentation, not the conclusion.** Mixing a group-level overhead ratio with
PCB-level gross margins means the row labelled "the actual PCB business 28.06% → +12.56%" is not a
computation of anything JLC reports; the reported 12.65% comes from 28.15% − 15.50%, which is true
by construction. The counterfactual rows should be labelled as segment-margin arithmetic under a
group cost structure, not as implied net margins.

### 6.4 Fragility 3 — **order size is not customer size**, and this is the real problem

`SMB-1`'s own glossary, quoted in the entry: 样板 (sample boards) is an order **under 1 m²**,
小批量 (small batch) is **1–20 m²**, 中大批量 (medium and large batch) is **over 20 m²**. These are
**order-area bands**. They are not customer segments.

The analysis reads them as customer segments throughout — "long-tail customers", "the segment with
concentrated, price-negotiating customers", "small customers are not merely each profitable; they
are where essentially all the profit is". **Nothing in the filing links an order-area band to a
customer size.** A large industrial buyer ordering five prototype boards sits in the 样板
(sample-board) band. JLC's own disclosed top-five customers are Megmeet, Haier, Wasion, 华立科技
(Huali Technology) and 尚研 (Shangyan) — large industrial firms — and the filing does not say which
band their orders fall in.

The prose `SMB-1` quotes does associate the bands with channels and with customer character (the
online 嘉立创 (JLC) block serves "highly dispersed" customers; the offline 中信华 (Zhongxinhua)
block serves customers who "negotiate prices"). That is real support for the reading, and it is why the conclusion is probably
directionally right. But it is an association stated by the company in its business narrative, not a
measurement, and the entry's bearing on **H6** — "*small customers* can each be profitable" — is
carried entirely by that association.

**The defensible version of the finding is: small *orders* carry a high margin and large *orders*
carry none.** That is still extremely relevant to a foundry, because a foundry's problem is exactly
small orders. It is not the same statement as "small customers are where the profit is", and the
repository should stop making the second one from this evidence.

The separate fact that JLC's top five fell from 2.00% → 1.37% → 1.16% of revenue is genuine support
for **H7**, and it does not depend on any of the above.

### 6.5 Fragility 4 — what if the big batch is the filler?

Capital is serviced out of gross profit **per unit of capacity consumed**. The filing gives revenue
share, not area share, and the analysis correctly flags this as "does not establish". Push it
further. Let `k` be the ratio of revenue per m² in the long tail to revenue per m² in big batch;
`k` must be well above 1 because the bands are defined at <1 m² and >20 m².

| `k` | Big batch's share of area consumed | …for 2.4% of the gross profit |
|---|---:|---:|
| 2 | 39.3% | 2.4% |
| 5 | 61.8% | 2.4% |
| 10 | 76.4% | 2.4% |
| 20 | 86.6% | 2.4% |
| 50 | 94.2% | 2.4% |

On any plausible `k`, **the big-batch segment consumes most of the plant and returns almost
nothing**. The analysis reads this as making the long tail look *better* ("expect it to favour the
long tail by more than 13.1×"). There is a second reading it does not consider, and it cuts the
other way:

> This is what **yield management** looks like. Near-zero-margin bulk work absorbs capacity the
> long tail cannot fill and carries a share of fixed cost, which is exactly why the long tail's
> price can be held at a 36% margin. On that reading the long-tail margin is partly *enabled by*
> the existence of the filler, and a "sample and small-batch only" JLC — which is what an open fab
> would be — would not keep 36.24%.

**Neither reading can be settled from the filing.** But the second is the one an adversarial
reviewer will raise, it is the standard explanation for exactly this margin pattern in
capacity-constrained manufacturing, and the analysis should state it. It also matters directly to
`PRINCIPLES.md`: a fab that sells *only* to the long tail has nobody to sell its idle capacity to.

### 6.6 What would have to be true for the decomposition to mislead

In descending order of how likely each is:

1. **The order-size/customer-size elision is doing the work** (§6.4). Likely; partly conceded by the
   filing's own prose, but unresolved.
2. **The big batch is filler that subsidises the long tail's price** (§6.5). Plausible and untested.
3. **2025's 2.76% is an outlier and the multiple reverts to 3–5×** (§6.2). The three-year series
   says this is the most likely single-number correction.
4. **The overhead ratio is wrong.** Tested in §6.3; the conclusion survives a 100% error.
5. **The disclosure is wrong.** No evidence for it; the table reconciles to 0.005 pp.

### 6.7 And the caveat the analysis states but does not weigh

"PCBs are not chips." The analysis says so. It is worth a number: `PAR-31` puts JLCPCB at **$2.00
and 24 hours** against chipIgnite at **$14,950 and up to a year**. A margin structure observed at
$2.00 and 24 hours is being used to argue about a product at 7,500× the price and 365× the wait.
That is not an argument against using it — it is the best analogue available — but it should be
carried in the same sentence as the 97.6%.

---

## 7. Cut: sensitivity — how far must each input move before the conclusion flips?

A conclusion that survives a 50% error in its inputs is worth more than one that needs them exact.
Here is which is which.

| # | Conclusion | What would have to be wrong | Verdict |
|---|---|---|---|
| A | **chipIgnite grew** (+94.8%/yr, 2021–2024) | Replace submissions with **slots**, a hard upper bound on paying customers: 32 → 60 → 93 → 160, **+71.0%/yr**. To flatten, 2024 must fall from 377 to 51 — an 86% overstatement. | **Very robust** |
| B | **Tiny Tapeout grew** | To flatten, the final year must fall by 82–89% on every measure (first-time designs, tiles, active designers). | **Very robust** |
| C | **Traditional demand is declining** | No datum need be wrong at all. Moving the Europractice window's start from 2021 to 2022 **flips the sign**, from −6.5%/yr to +1.0%/yr. | **Fails immediately** |
| D | **JLC: the long tail generates almost all the gross profit** | For the long tail to fall below 90% of gross profit, the big-batch margin must reach 12.5%; below 80%, 28.0%; below 75%, **37.4% — higher than the long tail's own 36.24%**. | **Very robust** |
| D′ | **JLC: 13.1× revenue per unit of gross profit** | A **1 pp** error in one printed number gives 9.6× or 20.6×. The same figure was 3.6× and 4.9× in the two prior years. | **Fragile** |
| E | **Open-programme participation is far less concentrated than a foundry's revenue** | TT effective designers 378.5 (bootstrap CI 219–950) of 2,625 = 14.4% (CI 8.4–36.2%); TSMC 11.8 of 522 = 2.3%, or 1.3% on the correlated-tail variant. The gap is 4× at the very worst end and 28× at the point estimate. | **Robust** |
| F | **Lifetime value is small** | For LTV to reach €500 at €70 a tile, mean designs per designer must be 7.1 against an observed 1.68 — a 4× error. €1,000 needs a 9× error. | **Robust** |

**The pattern is stark.** Everything the project claims about the *open* side survives errors of 80%
or more. Everything it claims about the *traditional* side fails on a one-year change of window.
The asymmetry is not in the project's favour, because the two-population contrast needs both halves.

### 7.1 The interest → committed discount, applied honestly

ChipFoundry is the only operator publishing both sides. Pooled conversion **73/202 = 0.361**, 95% CI
[0.298, 0.430] (beta, treating each expression of interest as a trial — which over-states precision,
because the three shuttles are not exchangeable).

| Count | As published | × 0.361 | 95% CI |
|---|---:|---:|---|
| Efabless submissions (`OPG-1`) | 1,584 | 572 | [472, 681] |
| Google Open MPW (`OPG-1`) | 821 | 296 | [245, 353] |
| chipIgnite submissions (`OPG-7`) | 763 | 275 | [227, 328] |

**Where it must not be applied:** Tiny Tapeout tiles and **wafer.space Crowd Supply backers** are
**completed transactions**, not expressions of interest, and discounting them would be wrong.
Europractice's counts are of designs actually *fabricated*, so the discount is equally wrong there,
but note that **how Europractice prices and reserves has not been checked** — whether any deposit or
cancellable booking sits between application and fabrication is simply unknown, and should not be
assumed either way. Tiny Tapeout reservations in particular are **full price,
non-transferable and non-refundable**, so they are purchases. `DEM-1`, `DEM-2`, `DEM-16`, `OPG-12`
and `PAY-9` are safe. `OPG-1`, `OPG-2`, `OPG-7` and every "oversubscribed" percentage in the
repository are not. **Google Open MPW is a third case**: its submissions were free applications and
the gap between submitting and being made is *selection*, not payment, so a payment-derived discount
is the wrong instrument there too.

Applied to `OPG-1`'s headline: **1,584 submissions is on the order of 570 paid projects**, and on
the repository's own bound of 578–1,232 distinct people, that is roughly one paid project per person
over the whole life of the Efabless programme.

---

## 8. Arithmetic errata

**Every `DERIVED` figure in `resources/` was recomputed from its quoted primary numbers. About 120
checks were run (`tmp/errata.py`). Not one arithmetic error was found.** That is an unusual result
and it should be recorded as such: the repository's arithmetic is sound.

What follows is therefore a list of **wording, framing and reconciliation errors**, not arithmetic
ones. They are listed in descending order of how much they matter.

| # | File / entry | What it says | What the arithmetic says |
|---|---|---|---|
| 1 | `demand/shuttle-programmes.md`, `DEM-16`; `hypotheses.md` H5 | Europractice "ran between 363 and 614 designs a year for the whole of 2000 to 2017 — eighteen years, essentially flat"; filed under H5 **Challenges** | The log-linear trend over those eighteen years is **+1.5%/yr, p = 0.0001** — a significant *rise* of 28% across the window. All three sub-series also rise (Research +8.1%/yr p = 0.0004; Academic +1.8%/yr p = 0.008; Industry +0.8%/yr p = 0.16). **It is weak support for H5, not a challenge.** |
| 2 | `hypotheses.md` H5 | "every free or subsidised programme found has been oversubscribed — 45 submissions against 40 slots on Google's first Open MPW shuttle (DEM-4, DEM-6)" | `OPG-2` records Efabless's own platform labelling MPW-1 **`Undersubscribed`, 37/40 = 92%**, and `OPG-4` records the 45-vs-37 disagreement as unresolved. `OPG-2` and `OPG-3` further record CI 2106Q (57%), CI 2110C (70%) and CI 2204C (32%) as undersubscribed. **The sentence is contradicted inside the repository and should be struck.** |
| 3 | `demand/open-programme-growth.md`, `OPG-15` | "submissions grew about 4× a year at the peak" | Google Open MPW went 37 → 147 across eight shuttles spanning 2020-11 to 2022-11: **about 4× over two years, i.e. ~2× a year.** chipIgnite grew 1.68–1.80× a year. Nothing in the repository grew 4× a year. Should read "about 4× over the series". |
| 4 | `OPG-7` vs `OPG-1` | `OPG-7`: chipIgnite "grew roughly 1.7× a year for three consecutive years". `OPG-1`: "Roughly 1.7× a year, twice in a row" | The three steps are **2.45×, 1.80×, 1.68×**. `OPG-1` is right; `OPG-7` is not. The two entries contradict each other. |
| 5 | `demand/efabless-and-the-open-shuttles.md` §2.2 | "Both programmes were free. The response differed by roughly eight-fold… This is the strongest single piece of evidence in the file" | 821 ÷ 98 = 8.4× is right, but it compares **821 submissions over ~3 years and 10 shuttles** with **98 applications to 6 programmes in one activity year**. Per year it is **2.8×**; per run, **5.0×**. The direction survives; the magnitude does not, and the document calls this its strongest evidence. |
| 6 | `analyses/industry-parallels.md`, `PAR-5` vs `DEM-1` | `PAR-5`: "summing the Designs column across the 19 closed shuttles listed gives **4,049** designs". `DEM-1`: the same page, the same day, **4,268** across 23 rows | The difference is exactly the four bring-up shuttles TTGF0p3 (32), TTIHP0p4 (40), TTGF0p2 (52) and TTIHP0p2 (95) = 219. **Reconciled, but neither entry says so**, and a reader comparing the two will conclude one is wrong. |
| 7 | `demand/design-starts-and-mature-nodes.md`, `TRAD-6` point 3 | "over the three unmeasured years 2013–2014" | 2013 and 2014 are **two** years. The arithmetic `(6,200/11,000)^(1/3)` is right for the 2012→2015 elapsed span; the wording is wrong. |
| 8 | `hypotheses.md` H5 | "Tiny Tapeout has taken over 4,300 submissions in four years **at €70 a tile plus a devkit**" | `OPG-14` establishes that the price was **$100** all-in in 2023, **$150 sponsored / $300 standard** through 2024–25, and **€150 all-in (€70 per extra tile)** only from mid-2025. Quoting one price for a four-year series conflates populations facing a three-fold price range, and `OPG-14` says so explicitly. Also "over 4,300" is `DEM-2`'s API count, which excludes TT01–TT03; `DEM-1`'s page count of 4,268 includes them. The two are different populations. |
| 9 | `demand/pricing-and-cost-to-serve.md`, `SMB-11` | "a small MPW customer pays roughly 300,000 times the silicon's share of a wafer's sale price… the ratio is about 40,000 times" | The arithmetic divides a **euro** price per mm² by a **dollar** price per mm². Converting at the entry's own ECB rate (`SMB-9`, EUR 1 = USD 1.1481) gives **349,000×** and **44,900×**. The orders of magnitude are unaffected, but the units are mixed. |
| 10 | `demand/shuttle-programmes.md`, `DEM-2` | "4,314 submission records… 4,308 distinct `project_id`" | Re-fetched 2026-09-18/19: **4,318 records**. The entry's own caveat predicts this. Noted only to confirm the caveat is doing its job. |

### 8.1 Two things that are right and look wrong

- **`TRAD-19`'s reconstruction reproduces exactly.** Anchoring on 2005 = 3,623 and applying the
  printed growth labels gives 2006 = 3,409 against the 3,408 that EE Times published independently.
  All eight derived years were recomputed and match the entry.
- **`big-customers-big-bets.md`'s effective-customer-count arithmetic reproduces exactly**, including
  the 11.77, the 1.2332, the 1.52 and the "largest customer is 57% of the index".

---

## 9. Small-number statistics

Poisson 95% confidence intervals on counts the repository quotes as trends:

| Count | Value | 95% CI |
|---|---:|---|
| wafer.space Run 1 backers | 6 | [2.2, 13.1] |
| wafer.space Run 2 backers | 18 | [10.7, 28.4] |
| wafer.space Run 3 backers (live) | 5 | [1.6, 11.7] |
| ChipFoundry CI2509 committed | 21 | [13.0, 32.1] |
| ChipFoundry CI2511 committed | 23 | [14.6, 34.5] |
| ChipFoundry CI2605 committed | 29 | [19.4, 41.6] |
| IHP Dec-2023 designs | 2 | [0.2, 7.2] |
| IHP Sep-2025 designs | 19 | [11.4, 29.7] |

- **wafer.space 6 → 18** is a real rise (exact binomial p = 0.023) *if* the two runs are
  exchangeable, which they are not — the goalpost moved during Run 1 (`OPG-12`) and Run 2 had a
  placeholder goal. `OPG-12`'s "a 3× rise" should carry the CI.
- **wafer.space 18 → 5** cannot be tested; Run 3 is still open.
- **ChipFoundry 21, 23, 29** — OLS slope +4.0 per shuttle, **p = 0.179, n = 3. No trend can be
  established.** `OPG-9`'s "the clearest picture available of the size of this business" is right;
  any reading of direction from it is not.
- **IHP's 2 → 68** is arithmetically +483%/yr and statistically meaningless off a base of 2.

**The `DEM-10` survey (14% → 38% industrial) has no published base.** What sample size would make it
significant:

| n per wave | z | p |
|---:|---:|---:|
| 10 | 1.22 | 0.221 |
| 20 | 1.73 | 0.084 |
| **30** | **2.12** | **0.034** |
| 50 | 2.74 | 0.006 |
| 100 | 3.87 | 0.0001 |

About **30 respondents per wave** would suffice. That is a plausible number for a programme of this
size, so the finding is not implausible — but no CI can be computed and it must be quoted as a
direction, never as "industrial customers are 38%".

### 9.1 Base rates: who are these people?

| Source | Academic | Commercial / industry | Hobbyist / other |
|---|---|---|---|
| Europractice 2024 (`DEM-16`) | 69% European universities and research institutes | 9% European industry | 22% non-European |
| chipIgnite, per `OPG-8`'s footnote | 37 academic/yr (66%) | 19 commercial/yr (34%) | — |
| Europractice, per `OPG-8` | 500 academic/yr (71%) | 200 commercial/yr (29%) | — |
| Tiny Tapeout survey (`DEM-10`, **no base published**) | ~42% implied residual | 38% industrial | 20% hobbyist |
| Google Open MPW MPW-1 (`DEM-4`) | — | — | "Approximately 60% … software, FPGA and hardware developers (non-IC experts)" |

**Why this matters and why it cannot be resolved.** The four splits use four different taxonomies,
one has no base, one is a 2022 internal document with no method, and the fifth counts a *skill*
category rather than an *employer* category. `OPG-8`'s own caveat warns that its chipIgnite figures
do not match `OPG-1`. Matt Venn's own year-in-review (quoted in the deep dive) attributes many Tiny
Tapeout designs to "high schoolers and students — attendees of my … workshops".

The honest statement: **a programme growing on student cohorts is different evidence from one
growing on companies, and the repository cannot presently tell which it has.** The one series that
could settle it — Tiny Tapeout's own survey — has no published sample. This is the single cheapest
piece of missing evidence in the whole project.

### 9.2 Survivorship

The open-programme evidence is drawn from survivors. The denominator of programmes launched, as far
as the repository records them:

| Ran and continues | Ran and stopped | Never ran / failed |
|---|---|---|
| Tiny Tapeout, ChipFoundry, IHP, wafer.space, Cadence/SkyWater, Europractice, CMC, MUSE, MOSIS 2.0 | Google Open MPW (sponsor stopped), chipIgnite under Efabless (operator died), CMP (foundries withdrew), MOSIS free academic programme (funding ended), IHP free era (funding ended) | Open-V (11% of goal), Retro-uC (18%), Maverick-603 (funded then suspended), Libre RISC-V M-Class (abandoned) |

That is **9 continuing, 5 stopped, 4 failed** — a survival rate of 9/18 = **50%** over the period,
and every one of the five stoppages was a supply-side decision rather than a demand shortfall, which
`efabless-and-the-open-shuttles.md` §3 establishes carefully and correctly.

**How much does survivorship bias the growth rate?** It can be bounded. Two of the five stopped
series are in the growth aggregate (Google Open MPW, chipIgnite) and both are included at their
terminal values, which is the conservative treatment. The four failed crowdfunding campaigns were
never in it. The honest statement is that **the bias is small for the shuttle series, because the
repository already counts the dead ones**, and large for any inference from crowdfunding, where the
repository counts four failures against one live campaign and `OPG-13` says so.

The bias that *is* present, and is not acknowledged: **the repository has no record of programmes
that were proposed and never launched, and no record of the five Crowd Supply open-silicon campaigns
as a base rate.** `OPG-13` establishes that Crowd Supply's entire "Open Silicon" category contains
four projects. A category with four entries after a decade is itself a finding.

---

## 10. Verdict table

"Cannot address" is used freely and is not a criticism of the evidence-gathering; it means the data
in `resources/` does not bear on the question in a way that survives a statistical test.

| H | Claim | Hardest cut | Verdict |
|---|---|---|---|
| **H1** | The doom spiral: high NRE means only big customers can make chips, which pushes cost up again | §2.3 — the Gartner decline decomposed | **Supports, with a correction.** The decline is real and significant under every start year, but about **−5.2%/yr between the recessions** against −10%/yr with 2001 and 2009 in. `TRAD-15`'s point — that value, units and gate count *per design* rose while the count fell — means the count is partly measuring integration. The mechanism survives; the magnitude should be halved. |
| **H2** | Customer concentration damages a foundry | §4.3 — concentration measured identically | **Cannot address from this data.** The repository's own Cirrus Logic counter-example (`ECON-20`) is a firm at the limit of the independent variable with margins moving the wrong way, and nothing in the demand data speaks to a foundry's margin by customer concentration. |
| **H3** | Chasing scale is rational under the experience curve | — | **Cannot address.** No cut in this document bears on it. |
| **H4** | Turning an idea into silicon can now be cheap | §5.3 — LTV and programme scale | **Supports on price, challenges on everything else.** €70 a tile is real and the price has fallen. But `PAR-3`/`PAR-4` give 1–5 attempts a year and 228–451 days, and §5.3 shows the whole worldwide line is €0.5–2.3m of gross revenue in four years. Cheap is established; consequential is not. |
| **H5** | There is a long tail of demand for chips | §2.2 — the matched-window problem; §3.4 — retention | **Challenged, and the framing is wrong.** The open side's growth is robust to an 80% error and survives dropping any one programme (§2.5). The *contrast* does not survive, because the traditional decline is a 1994–2013 phenomenon and flips sign in the overlap window on a one-year change of start date (§7C). Separately, 74% of designers appear once and year-on-year retention outside port runs is 6–16% (§3.4), and 56% of the record 2025 was re-runs (§3.2). **The population is growing; it is a population of one-time experimenters.** |
| **H6** | Small customers can each be profitable | §6 — the JLC attack; §5.3 — LTV | **Contested, and weaker than `long-tail-pays-for-the-capital.md` implies.** JLC's decomposition is arithmetically sound and robust (§7D), but it establishes that **small orders** carry the margin, not that **small customers** do (§6.4), and the big-batch segment may be the filler that makes the long-tail price sustainable (§6.5). On the open-silicon side, an LTV of €122–$521 with 85–90% never returning leaves no room for any cost to serve beyond a web form. |
| **H7** | Many small customers reduce risk and remove buyer power | §4.3 — effective number of participants | **Supports, and this is the first real measurement.** Tiny Tapeout's effective number of designers is **14.4% of the nominal count** against TSMC's **2.3%**, bootstrap-robust (§7E). Against it: `OPG-11`'s IHP run where two intermediaries hold 71% of registered area, and `SMB-4`'s Shapeways with a million customers and one at 23% of revenue. **Concentration at the bottom of the market is real and must be watched.** |
| **H8** | Openness is necessary to attract many small customers | §2.4 — free versus paid | **Cannot address.** The free/paid cut shows paid programmes growing *faster*, which is consistent with H8 and equally consistent with three other stories. No study of price transparency and small-buyer adoption exists (`PAR-6`, open question 5). |
| **H9** | Many small, public experiments make a fab learn faster | §3.2 — the port runs | **Cannot address, with one relevant observation.** The IHP, GF and Cadence bring-up runs are precisely "many small public experiments used to qualify a new process", and they worked — 433 designs ported to IHP in one run. That is an existence proof of the *mechanism*, with no measurement of the learning. |
| **H10** | Being paid for every attempt works in a world of skewed outcomes | §4.2 — the power-law test | **Challenges the framing.** The outcome distribution here is **not** a power law (CSN p = 0.000) and is only power-law-like above four designs (3–4% of designers). Gini 0.356 is mild. H10's premise of extreme skew is not what the one measurable distribution shows. The skew in `SW-3` and `SW-4` is much stronger; whether it transfers is untested. |
| **H11** | Markets and insurance can replace foundry judgement | §6.5 — the filler question | **Cannot address, with one warning.** If JLC's near-zero-margin bulk segment is capacity filler that carries fixed cost, a fab that sells *only* to the long tail has no filler and no buyer of last resort for idle capacity. `PRINCIPLES.md` should say who buys the slack. |

---

## 11. The strongest argument against the project, built from our own evidence

This is the most valuable section in the document and it is made as strong as it honestly can be.

---

**The project's case is a contrast between two populations. The contrast does not exist in the
data, and what is left in its place is a hobby.**

**First, half the contrast is missing.** The claim is that conventional chip demand is shrinking in
number of customers while open-entry demand grows. The only evidence of a shrinking conventional
population is Gartner's ASIC design-start series. It ends in 2013 and its final five points are a
forecast made in March 2009 at the bottom of the financial crisis (`TRAD-19`). Every open-programme
series begins in 2020. **There is not one year in which both halves of the contrast are measured.**
In the six years where anything overlaps — 2020 to 2025 — the conventional side does not decline:
Europractice's trend flips sign depending on whether you start in 2021 or 2022 and is significant in
neither direction; CMC's fall has p = 0.80 on seven points; TSMC's product count is up 17.9% and its
customer count is flat. The repository's own design-starts file already reaches this conclusion by a
different route — "The broad 'design starts are collapsing' claim, as drawn on the owner's chart,
does not survive." The statistics agree. **The doom spiral may be real; nothing we hold measures it
after 2013.**

**Second, the growth that does exist is the wrong shape.** The open side genuinely grows, robustly,
at 70–95%/yr, and it survives dropping any one programme. But the per-designer data — which nobody
had looked at until this document — says what is growing is a stream of one-time experimenters.
**73.6% of designers make exactly one design. Outside the process-port runs, 85–90% of designers on
any given shuttle have never used the programme before, and year-on-year retention is 6% to 16%.**
Fifty-six per cent of the record 2025 was the same designs run again on a new process. A business
whose customers never return is not compounding; it is refilling a leaking bucket, and it must
acquire its entire customer base again every year, for ever.

**Third, the money is not there, by two independent measures.** The whole worldwide output of the
most successful open-silicon programme ever run is **7,728 tiles in four years** — between €540,960
and $2.3 million of gross revenue depending on which of its own published prices you use.
`SMB-5` records MOSIS at "up to $10 million annually at its peak", in 1990s money, and the
repository correctly calls that "smaller than one mid-sized customer of a real fab". The open-PDK
era is an order of magnitude *below* MOSIS. Lifetime value per acquired designer is **€122** at €70
a tile and **$521** at the highest price the programme ever charged. And the one operator that
publishes money committed rather than interest expressed — ChipFoundry — reports **21, 23 and 29
paying customers per shuttle**, converting only **36%** of expressed interest, on shuttles planned
for 28, 37 and 43. Nobody has ever published a count of paying open-shuttle customers above forty
per run.

**Fourth, the best profitability evidence is about the wrong variable.** `long-tail-pays-for-the-capital.md`
is arithmetically impeccable — every figure reproduces, and its central finding survives a 1,200%
error in its key input. But JLC's bands are defined by **order area** (<1 m², 1–20 m², >20 m²), not
by customer size. What it establishes is that **small orders carry a high margin**. The step from
there to "small customers are where the profit is" — which is what H6 needs — rests on an
association asserted in the company's own business narrative, and JLC's disclosed top-five customers
are Megmeet, Haier and Wasion. Worse, on any plausible revenue-per-m² ratio the near-zero-margin
bulk segment is consuming **40% to 94% of the plant** for 2.4% of the gross profit. That is the
signature of yield-management filler carrying fixed cost. If it is, the long tail's 36% margin is
partly *enabled by* the bulk work — and a fab that sells only to the long tail, which is what the
project proposes, has nobody to sell its idle capacity to.

**Fifth, the distribution is not the one the argument assumes.** H10 rests on extreme skew: most
attempts fail, a few produce most of the value, and the fab is paid either way. The one distribution
in the repository that can actually be fitted is not a power law — Clauset–Shalizi–Newman rules it
out with p = 0.000 over the body, and it survives only above four designs, which is 3–4% of
participants. The Gini is 0.356, less unequal than household income in most countries. There is no
fat tail of future giants visible in this data. There is a mild skew, a large one-time cohort, and
about **1,250 recurring participants worldwide** after four years and three foundry processes.

**Put together, the strongest hostile reading is this.** Open-PDK silicon has demonstrated,
convincingly, that lowering the price of an attempt brings more people. It has not demonstrated that
those people come back, that they pay enough, that there are enough of them, or that the population
behind them is growing relative to anything. The conventional route it is supposed to be replacing
has been flat-to-slightly-up for twenty-five years, not collapsing. And the one company built on
exactly this thesis, at exactly these prices, growing at exactly these rates, could not raise a
Series B — and the clearest public explanation of why remains a named observer's judgement that
"people who use open source tools do it mainly due to cost and that is a tough customer base to
profit from" (`OPG-16`). Nothing computed in this document contradicts him.

---

### 11.1 What survives, honestly

The argument above is the strongest hostile case. It is not the whole truth, and three things
survive it intact:

1. **The growth is real and robust.** It survives an 80% error in the final year, survives dropping
   any one programme, survives replacing submissions with slots (§7A), and is *faster* in the paid
   programmes than the subsidised ones (§2.4). The project's claim that demand appears when price
   falls is supported by demand people paid for.
2. **The dispersion is real and now measured.** Effective participants are 14.4% of the nominal
   count against 2.3% for TSMC's revenue, robust to bootstrap and to dropping the largest
   participant. H7 has its first measurement.
3. **The narrow version of the thesis is undamaged.** Not "fewer chips are wanted", but: *the number
   of organisations for which a commercial custom chip is economically possible is small and stable,
   the bar per design has risen, and the open route reaches a population the conventional route
   structurally cannot.* Every cut in this document is consistent with that. It is the claim the
   project should be making.

---

## Reproducing this

Scripts, all run with `uv run python`, all removed after use per the repository's convention:
`tmp/tt_dist.py` (per-designer distribution), `tmp/tt_reruns.py` (re-run share), `tmp/fitdist.py`
(power-law fit and bootstrap), `tmp/conc.py` (concentration across datasets), `tmp/ltv.py` (cohorts,
lifetime value, scale), `tmp/growth.py` (CAGRs, matched windows, free/paid, drop-one),
`tmp/smalln.py` (Simpson, start-year sensitivity, Poisson CIs), `tmp/jlc.py` (the JLC attack),
`tmp/sens.py` (sensitivity), `tmp/errata.py` (≈120 arithmetic checks).

The only external data used are the public Tiny Tapeout endpoints, fetched 2026-09-18:
`https://app.tinytapeout.com/api/shuttles/submission-stats` and
`https://index.tinytapeout.com/<slug>.json` for 24 shuttles. Everything else is quoted from
`resources/`.
