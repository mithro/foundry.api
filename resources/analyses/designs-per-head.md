# Designs per head, and the batch size underneath it

*Our own arithmetic. First written 2026-09-25; **substantially rewritten the same day** after
`PRD-1`…`PRD-13` tested the comparison and broke most of it.*

**The headline claim in the first version of this file is withdrawn.** "Modern brokers are
dramatically less productive per head than a 1984 service running on 1984 computers" was asserted
in conversation, written up, and then tested. It did not survive. What replaced it is narrower,
better sourced, and more useful: **the gap is not in people, it is in batch size.**

---

## 1. What was withdrawn, and why

Three errors, all pushing the same way.

**(a) 1984 was the maximum of a noisy series, and the series was four points long only because five
documents had not been recovered.** All five are now recovered (`PRD-1`). MOSIS's complete
designs-per-named-person series:

| ISI report (period) | Named staff | Projects | Per head |
|---|---:|---:|---:|
| 1982 ATR (Jul 1981 → Jun 1982) | **13** *(new)* | 809 | **62.2** |
| 1983 ATR | 12 | 1,532 | 127.7 |
| 1984 ATR | 11 | 1,634 | **148.5** ← the number that was quoted |
| 1985 ATR | 20 | 1,790 | 89.5 |
| 1986 ATR (Jul 1985 → Jun 1986) | **27** *(new, and re-dated)* | 1,683 | 62.3 |
| 1987 ATR (Jul 1986 → Nov 1987) | 27 | 1,345/yr | **49.8** |

62 → 128 → 149 → 90 → 62 → 50. **1984 is the single highest point**; the mean is 90.0 and MOSIS's
own last measured year is **49.8**. The roster of 27 was also mis-dated: it is first printed in the
**1986** report and repeated verbatim in 1987, so it belongs to 1985/86.

**(b) The denominators were not the same kind of object** (`PRD-5`, `PRD-6`, `PRD-3`).

- **Europractice.** Three of the nineteen named contacts are printed on the contact page as *design
  tools*, *training courses* and *academic membership* — not fabrication. **753 ÷ 16 = 47.1.**
- **CMC.** 48–65 is a whole-organisation count, and CMC's audited statements put
  fabrication-and-packaging at **19.1% / 28.9% / 34.0%** of expenditure in FY2026 / FY2025 / FY2023.
  Re-based pro-rata the range is **10.9 – 26.3**, not 5.0. The numerator is too big as well: only
  **1,369 of 1,803** five-year "designs prototyped" were MPW.
- **MOSIS.** Its 11 is a *project-chapter roster* that excluded ISI's separate **37-person computer
  centre**, which ran MOSIS's machines. One person is printed in both chapters of the same report.

**(c) The unit survived, and that part was sound.** MOSIS "projects", Europractice "designs" and
CMC "prototypes" are all designs placed on a shared reticle and delivered as packaged parts
(`PRD-4`). This was the defect I expected to be fatal and it was not.

### The corrected comparison

| | Per head | vs MOSIS's last measured year (49.8) |
|---|---:|---:|
| MOSIS 1986/87 | **49.8** | — |
| Europractice 2025, fabrication-facing | **47.1** | **1.06×** |
| CMC FY2026, re-based, middle estimate | **14.3** | **3.5×** |

**Against MOSIS's peak instead of its last year**, the ratios are 3.2× and 10.4×. **The 29.7×
figure quoted earlier is dead and must not be used anywhere.**

**Europractice is within 6% of MOSIS on people.** The "traditional brokers got worse at using
people" story is, as regards Europractice, false.

## 2. What the evidence actually supports: batch size

`PRD-8`. MOSIS put **32.8 designs on every run**. Europractice's 2026 schedule — parsed from its own
HTML grid — offers **124 technology lines, 307 filled month-cells, 248 distinct
technology-and-date submission slots on 154 calendar dates**, for 753 designs:
**753 ÷ 248 = 3.04 designs per slot.**

**And the decomposition is exact.** Designs per head = (designs per run) × (runs per head):

| | Designs per run | × runs per head | = per head |
|---|---:|---:|---:|
| MOSIS 1986/87 | 32.8 | 1.52 | **49.8** ✓ |
| Europractice 2025 | 3.04 | 15.5 | **47.1** ✓ |

**The modern service runs ten times as many shuttle events per person and puts eleven times fewer
designs on each. They cancel exactly.** The headcount story was the residue of two effects that
offset; the real difference is portfolio fragmentation — ~90 technologies from 20+ foundries, at
**8.4 designs per technology per year**, against MOSIS's 635.

### Where the new providers sit on the axis that matters

| Provider | Designs per run | Source |
|---|---:|---|
| **Tiny Tapeout 2025** | **124.3** (1,492 ÷ 12 shuttles) | `PAY-6`, `doubling-time-and-timelines.md` |
| MOSIS 1986/87 | 32.8 | `PRD-2`, `PRD-8` |
| wafer.space Run 2 | 18 | `OPG-12` |
| ChipFoundry | 17.8 (89 ÷ 5 shuttles) | `CF-6`, `CF-11` |
| **Europractice 2026** | **3.04** | `PRD-8` |

**Tiny Tapeout's batch is 40.9× Europractice's and 3.8× MOSIS's best.** *(On `PAY-6`'s narrower count of 1,455 designs on revenue-bearing shuttles rather than the 1,492 in the index data, it is 121.3 per shuttle and 39.9× — the conclusion does not turn on which count is used.)* *This* is the real and
defensible version of the claim, and it is a much better one for this project than the
productivity claim was, because **batch size is the thing an auction-scheduled foundry directly
controls.** Aggregating demand onto fewer, fuller reticles is not a side effect of the design; it
is the design.

## 3. Designs per head, with the new providers

| Provider | Period | Designs | Staff | Per head | Source |
|---|---|---:|---|---:|---|
| MOSIS | 1986/87 | 1,345/yr | 27 | **49.8** | `PRD-2` |
| Europractice | 2025 | 753 | 16 fab-facing | **47.1** | `PRD-5` |
| ChipFoundry | 2025-05 → 2026-09 | 89 slots | 4 named (a floor) | **16.0 – 22.2** | `CF-4`, `CF-6` |
| CMC | FY2026 | 240 | re-based 9.1–22.1 | **10.9 – 26.3** | `PRD-6` |
| Tiny Tapeout | 2025 | 1,492 | **not published** | *see below* | `PAY-6` |
| wafer.space | 2026 | 24 customers | **zero FTE** | *undefined* | operator |

**Tiny Tapeout, without needing its headcount.** Invert it — how many people could it employ and
still match each benchmark?

| To match | TT could employ |
|---|---:|
| MOSIS's peak, 148.5 | **10.0** |
| MOSIS's last year, 49.8 | **30.0** |
| Europractice corrected, 47.1 | **31.7** |
| CMC corrected middle, 14.3 | **104.3** |

The inversion is still the robust form, and it still holds on the corrected benchmarks: Tiny
Tapeout would have to be a **thirty-two-person** company to be as unproductive per head as
Europractice. But note the honest consequence of §1 — **against Europractice the bar is now 47.1,
not 39.6, and against MOSIS it is 49.8, not 148.5.** The claim is weaker than it was this morning.

**ChipFoundry remains the awkward case**: a new provider, no external investors, at 16.0–22.2 —
*below* Europractice. Vintage is not the variable.

## 4. The other candidate causes, tested

From `PRD-7` through `PRD-13`. Each was tested rather than assumed.

| Candidate | Verdict |
|---|---|
| **Batch size / portfolio fragmentation** | **Supported, and it is the mechanism.** The decomposition closes exactly on both services (`PRD-8`) |
| **Scope creep** | **Supported, qualitatively and cleanly.** MOSIS 1986: *"it is the sole responsibility of the user to see that the submitted patterns yield working designs"* — comparing itself to *"a publisher of conference proceedings"*. Europractice 2025: *"extensive Design Rule and Electrical Rule Checkings are performed on all designs submitted to the Service."* **Per-design checking is the one cost that cannot be amortised over a run** (`PRD-7`) |
| **Design complexity** | **Third, and measured in period.** One node step, 3 µm → 2 µm, cost MOSIS 1.9–3.0× of batch size and 1.89× of turnaround, *in 1987*. **The complexity penalty is a property of chasing the edge, not of the edge being at 3 nm** (`PRD-9`) |
| **"It's all mature nodes anyway"** *(our own counter-argument)* | **One third true.** Europractice 2025 is one third mature (0.11–0.35 µm); 65 nm is 172 designs (22.8%); named 22 nm is 134 (17.8%); four universities at 7 nm FinFET (`PRD-10`) |
| **NDA / PDK legal gating (H8)** | **Supported but thin.** MOSIS 1987: *"a set of non-proprietary design rules applicable to a multiple vendor base"*, and **zero legal or contracts roles across 110 name-years of roster**. Europractice 2025 names one legal role among nineteen. **No broker publishes a count of agreements processed, so the cost is not sized anywhere** (`PRD-11`) |
| **Fundraising overhead** *(the first hypothesis raised)* | **Real, visible, and too small.** MOSIS: one instrument for nine years. CMC: six public instruments in five years with the base turning over completely. Professional fees +79.6% and outreach +59.8% in one year — but together **6.7% of spending**. Cannot explain a 2–10× gap (`PRD-13`) |
| **Volume collapse alone** | **No.** Throughput fell 1,345 → 753 → 240, but the corrected denominators fell with it |
| **Fewer foundries means less work** | **False.** MOSIS 1982 named 4 wafer vendors and 3 mask houses; Europractice has *"nearly 90 technologies from more than 20 foundries"* — 5.6–7.8 technologies per fabrication-facing person against MOSIS's 0.15 (`PRD-12`) |

**One finding here bears directly on H8 and is worth separating out.** MOSIS could refuse to check
designs — *"not to address the spelling, grammar, syntax, ideas, or concepts"* — **because its rules
were public**. A broker distributing an NDA'd PDK cannot let the customer own correctness in the
same way. Openness and the ability to run a hands-off, high-batch service are linked, and that link
is a mechanism rather than a correlation. It is not yet quantified.

## 5. What is still not established

- **No Europractice FTE count exists in public.** The 16 is a named-contacts floor. If the real
  establishment is 30, the figure drops to 25.1 and MOSIS beats it 2×. The Chips JU Annex 1
  person-months would settle it and are unpublished.
- **No CMC headcount since 2018, and no staff split by function anywhere.** The 19.1–34.0%
  re-basing is by *expenditure share*, not by people. Ontario's public-sector salary disclosure is
  the untried next step.
- **No broker publishes a count of NDAs, PDK licences or export declarations.** This is what H8 most
  needs, and it appears not to exist.
- **Tiny Tapeout's headcount** (route: KvK accounts, `PAY-11`, behind a paid account we will not
  create) and **ChipFoundry's** (no careers page, no statement, `CF-4`).
- **CMC's node mix** is not published at all; Europractice's per-node counts for 2025 are unlabelled
  raster bar charts.
- **MOSIS 1988–89 has no roster and never will** — the Final Technical Report has no MOSIS chapter.

## 6. What may be cited where

| Claim | Status |
|---|---|
| Batch size 32.8 vs 3.04, and the exact decomposition | **Citable.** `PRD-8` |
| Tiny Tapeout's 124.3 designs per shuttle | **Citable.** `PAY-6` |
| MOSIS's full six-point series, 62.2 → 49.8 | **Citable.** `PRD-1`, `PRD-2` |
| The scope-creep quotes | **Citable.** `PRD-7` |
| "Europractice is within 6% of MOSIS per head" | **Citable with its caveat** — 16 is a floor |
| Anything per-head about CMC | **Range only, 10.9–26.3.** Never the single figure |
| **"29.7× more productive than CMC"** | **WITHDRAWN. Do not use.** |
| **"148.5 designs per head" as *MOSIS's* productivity** | **Only as the series maximum**, never unqualified |
