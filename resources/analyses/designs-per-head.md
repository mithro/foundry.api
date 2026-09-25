# Designs per head: traditional brokers against the new providers

*Our own arithmetic, 2026-09-25. Every input is an existing entry; nothing here is a new
measurement. This file exists because the claim "modern brokers are dramatically less productive
per head than a 1984 service running on 1984 computers" was asserted in conversation before it was
written down, sourced or tested. It is written down here so it can be attacked.*

**Status: the arithmetic is solid; the comparability is not yet established.** Read §4 before
quoting any figure from §2. A research task (`research/productivity-drop`, output
`demand/broker-productivity.md`, entries `PRD-*`) is open specifically to test whether the four
traditional-provider numbers measure the same thing. **Until it reports, the 29.7× figure must not
be cited in `WHY.md` or `PRINCIPLES.md`.**

---

## 1. The two populations

The split that matters is **not** old-versus-new. It is what the service does with a person's time.

| | Provider | What it is |
|---|---|---|
| **Traditional** | MOSIS (1981–1994, DARPA-funded) | Government-funded broker, ISI/USC |
| | Europractice (2000–) | EU-grant-funded consortium: imec, Fraunhofer, CMP, STFC, Tyndall |
| | CMC Microsystems (1984–) | Canadian federally-funded national service |
| **New** | ChipFoundry (2025–) | Commercial, no external investors |
| | Tiny Tapeout (2022–) | Commercial, no external investors |
| | wafer.space (2025–) | Commercial, no external investors |

## 2. The numbers

Designs shipped per staff-member per year. **Sources are entry IDs; follow each one before using
the number.**

### Traditional

| Provider | Period | Designs | Staff | **Per head** | Source |
|---|---|---|---|---|---|
| MOSIS | Jul 1982 → Jun 1983 | 1,532 | 12 | **127.7** | `MOS-3` |
| MOSIS | Jul 1983 → Jun 1984 | 1,634 | 11 | **148.5** | `MOS-3` |
| MOSIS | Jul 1984 → Jun 1985 | 1,790 | 20 | **89.5** | `MOS-3` |
| MOSIS | Jul 1986 → Nov 1987 | ~1,683 | 27 | **62.3** (88.6 excl. 8 students) | `MOS-3` |
| Europractice | 2017 | 614 | 13 named | **47.2** | `DEM-16`, `FUNDX-5` |
| Europractice | 2024 | 837 | 21 named | **39.9** | `DEM-16`, `FUNDX-5` |
| Europractice | 2025 | 753 | 19 named | **39.6** | `DEM-16`, `FUNDX-5` |
| CMC Microsystems | FY2025/26 | 240 prototypes | 48 / 58 / 65 | **5.0 / 4.1 / 3.7** | `DEM-20`, `FUNDX-6` |
| MOSIS 2.0 | 2026 | one advertised MPW date | 4 named | *not computable* | `MOS-12` |

### New

| Provider | Period | Designs | Staff | **Per head** | Source |
|---|---|---|---|---|---|
| ChipFoundry | 2025-05-01 → 2026-09-20 | 89 committed slots | 4 named (a **floor**) | **16.0 – 22.2** | `CF-4`, `CF-6`, `CF-11` |
| Tiny Tapeout | 2025 | 1,492 designs | **not published** | *see §3* | `PAY-6`, `doubling-time-and-timelines.md` |
| wafer.space | 2026 to date | 24 customers (Run 2: 18, Run 3: 6 so far) | **zero full-time employees** | *undefined* | operator statement; `OPG-12` |

**ChipFoundry's arithmetic, both ways.** 89 committed slots ÷ 4 named staff = **22.2** if the whole
89 is taken as one year's work. Dating from the first shuttle opening (2025-05-01) to the reading
(2026-09-20) is 507 days = 1.388 years, so 89 ÷ 1.388 = 64.1/yr ÷ 4 = **16.0**. Both are
**ceilings**, because four is a floor on the headcount (`CF-4`: four named individuals is the
largest headcount evidenceable from public sources, not a company statement), and two of the five
shuttles are still filling.

## 3. Tiny Tapeout, without needing its headcount

Tiny Tapeout publishes no employee count, so the ratio cannot be computed. **It does not need to
be.** Invert it instead: *how many people could Tiny Tapeout employ and still match each
benchmark?*

| To match | Tiny Tapeout could employ |
|---|---|
| MOSIS 1983/84, 148.5 per head | **10.0 people** |
| MOSIS 1986/87, 62.3 per head | **23.9 people** |
| Europractice 2025, 39.6 per head | **37.6 people** |
| CMC FY2025/26 at 48 staff, 5.0 per head | **298.4 people** |

1,492 ÷ 148.5 = 10.0; 1,492 ÷ 39.6 = 37.6; 1,492 ÷ 5.0 = 298.4.

**This is the robust form of the claim.** It survives not knowing the headcount, because any
plausible value falls on the same side of the line. Tiny Tapeout would have to be a
thirty-eight-person company to be *as unproductive per head as Europractice*, and a
three-hundred-person company to be as unproductive as CMC.

wafer.space's ratio is **undefined, and that is the observation** — the denominator is zero. Two
completed runs and a live third, with no full-time employees at all.

## 4. What this does NOT establish — read before quoting §2

**These four traditional numbers may not measure the same thing.** Four specific problems, in
descending order of how much damage each does:

1. **CMC's 5.0 is the most suspect number in the table.** CMC is not only an MPW broker: it
   distributes CAD tool licences to Canadian universities, runs training, and operates labs. If most
   of its 48–65 people are not on the fabrication service, the denominator is wrong and **5.0 is an
   artefact**. `FUNDX-6` already says so in terms: against Europractice's figure "the two are not
   comparable — one is a real headcount, the other a published-contacts floor". **The 29.7× MOSIS/CMC
   ratio is therefore the weakest cell in this file, not the headline.**
2. **Europractice's 19 is a count of named website contacts, not FTEs.** `FUNDX-5` derives that the
   grant money per named person looks like "roughly half to two-thirds of a full-time equivalent
   each". If the real FTE count is ~11, Europractice's true figure is ~68, not 39.6, and the gap to
   MOSIS closes almost entirely.
3. **"Designs" is not defined identically.** MOSIS counted *projects*; Europractice counts *designs*;
   CMC counts *prototypes*; ChipFoundry counts *committed slots*, which `CF-6` warns may be deposits
   rather than sales; Tiny Tapeout counts *designs* of which many are student exercises on a shared
   die. A Tiny Tapeout tile and a CMC prototype are not the same unit of work.
4. **Node mix is uncontrolled.** MOSIS 1984 shipped 3 µm and 1.2 µm nMOS/CMOS. Europractice and CMC
   ship a spread including 65 nm and below. If the work per design has genuinely exploded, part of
   the decline is real complexity rather than lost efficiency.

**Two further gaps on the new-provider side:** ChipFoundry's 4 is a floor, so its ratio is a
ceiling; and Tiny Tapeout's headcount is absent entirely, which is why §3 is written as an
inversion rather than a ratio.

## 5. The correction this file makes to an earlier claim

An earlier conversational summary said the MOSIS head-count series "cuts against the automation
reading" — that because MOSIS was automated for its era and still needed subsidy, automation is not
what makes a broker cheap.

**That was a category error and it is withdrawn.** It conflated two different questions:

- **Productivity per head** — how many designs one person can ship. Automation drives this. MOSIS
  1983/84 got 148.5, and its own reports to DARPA describe automated vendor templates, computerised
  geometry processing and automated wafer-space allocation, with users perceiving MOSIS as "a black
  box that accepts artwork files electronically and responds with packaged IC devices"
  (`MOS-4`, `MOS-8`).
- **Cost recovery** — whether the price covers the cost. MOSIS failed this by charging $400 against
  $1,765/design of operating cost (`MOS-8`). That is a pricing and subsidy decision, not a
  productivity failure.

MOSIS 1984 is therefore **consistent with** the automation thesis, not against it: the automated
traditional provider got 148.5 per head, and the staff-intensive modern ones get 39.6 and 5.0. What
MOSIS shows is that *automation alone does not produce cost recovery if you price at a fifth of
cost.*

## 6. What the evidence actually supports

**Not** "new beats traditional". ChipFoundry is a new provider, has no external investors, and at
**16.0–22.2** sits *below* Europractice's 39.6. Vintage is not the variable.

The variable that separates the table is **whether a human is in the loop per design**:

| | Human per design? | Per head |
|---|---|---|
| wafer.space | no — self-service campaign | undefined (0 FTE) |
| Tiny Tapeout | no — self-service submission, automated harness | ≥148.5 at any headcount ≤ 10 |
| MOSIS 1983/84 | no — "a black box that accepts artwork files electronically" | 148.5 |
| Europractice | partly — a named human contact per foundry per partner (`FUNDX-5`) | 39.6 |
| ChipFoundry | yes — consultative, deposit-and-milestone (`CF-6`, `CF-9`) | 16.0–22.2 |
| CMC | yes — licences, training, labs, staffed support | 5.0 *(suspect, §4)* |

**The 1984 result is the load-bearing one**, because it removes the escape hatch that this only
became possible with modern software. An electronically-submitted, automatically-processed service
reached 148.5 designs per person **on 1984 computers**. The traditional providers have not got
closer to it since; they have moved away from it.

## 7. Open questions, assigned

| Question | Where it is being worked |
|---|---|
| Do the four traditional numbers measure the same thing? | `research/productivity-drop` → `PRD-*` |
| Extend MOSIS's 4-point head-count series (5 ISI reports still unrecovered) | same |
| Is the cause fundraising overhead, design complexity, NDA/PDK legal gating, foundry count, or volume collapse? | same |
| Tiny Tapeout's actual headcount | **unassigned.** KvK accounts for Tiny Tapeout B.V. are the route (`PAY-11`) and are behind a paid account we will not create |
| ChipFoundry's actual headcount | **unassigned.** No careers page, no statement (`CF-4`) |
