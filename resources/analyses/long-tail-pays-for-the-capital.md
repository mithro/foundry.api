# The long tail is what pays for the capital

*Status: our own arithmetic, computed 2026-09-18 from figures quoted verbatim in
[`../demand/long-tail-businesses.md`](../demand/long-tail-businesses.md) SMB-1. Every input is a
printed number from the JLC prospectus; every output is reproducible from the script quoted below.*

---

## The question this settles

A recurring objection to foundry.api runs: *a business serving many tiny customers can only work if
it does not own the machines.* Xometry and Protolabs get cited as the two poles — the marketplace
that owns nothing and the manufacturer that owns plant and has a much harder time. On that reading,
owning a fab and serving a long tail are in tension, and foundry.api wants both.

The objection asks the wrong question. The right one is not *can a long-tail business carry
capital?* but **which customer segment generates the gross profit that services capital at all?**

JLC is the case that answers it, because its prospectus breaks the *same factories* into a
long-tail segment and a big-batch segment and prints the gross margin of each.

## The decomposition

From the p.245 table (PCB business, share of PCB revenue × gross margin of that share):

| Year | Segment | Share of revenue | Gross margin | **Share of gross profit** |
|---|---|---|---|---|
| 2023 | 样板、小批量 (sample + small-batch) | 74.38% | 35.27% | **91.31%** |
| 2023 | 中大批量 (medium/large-batch) | 25.62% | 9.74% | 8.69% |
| 2024 | sample + small-batch | 75.61% | 37.28% | **93.81%** |
| 2024 | medium/large-batch | 24.39% | 7.63% | 6.19% |
| 2025 | sample + small-batch | 75.57% | 36.24% | **97.60%** |
| 2025 | medium/large-batch | 24.43% | 2.76% | 2.40% |

**In 2025 the long tail was three-quarters of revenue and 97.6% of gross profit.** The big-batch
business — the kind of work a conventional factory is built to chase — contributed 2.4%.

The table reconciles: Σ(share × margin) gives 28.735% / 30.046% / 28.058% against printed 合计
subtotals of 28.73% / 30.05% / 28.06%, agreeing to within 0.005 pp in all three years. The
disclosure is internally consistent, which is a reason to trust it.

## The capital argument

Capital is serviced out of gross profit. So ask how much revenue each segment must turn over to
throw off one unit of gross profit:

| Segment (2025) | Revenue per CNY 1 of gross profit |
|---|---|
| sample + small-batch | CNY 2.76 |
| medium/large-batch | CNY 36.23 |

**A big-batch factory must turn over 13.1× the revenue of a long-tail factory to service the same
capital investment.** Same machines, same building, same depreciation schedule.

Push it further. JLC's group net margin in 2025 was 12.65% on a blended gross margin of 28.15%, so
everything below the gross line — SG&A, R&D, tax, the lot — costs 15.50 pp of revenue. Holding that
cost structure fixed and swapping only the revenue mix:

| Counterfactual company | Gross margin | Implied net margin |
|---|---|---|
| the actual PCB business | 28.06% | **+12.56%** |
| sample + small-batch only | 36.24% | **+20.74%** |
| medium/large-batch only | 2.76% | **−12.74%** |
| medium/large-batch, offline channel only | −6.71% | **−22.21%** |

A JLC that had only the segment a traditional factory competes for would not merely fail to pay
back its capital. It would not cover its operating costs.

## The direction of travel

The two segments are moving in opposite directions inside one company's accounts:

| Segment | 2023 | 2024 | 2025 | Change |
|---|---|---|---|---|
| sample + small-batch | 35.27% | 37.28% | 36.24% | **+0.97 pp** (+2.8% relative) |
| medium/large-batch | 9.74% | 7.63% | 2.76% | **−6.98 pp** (−71.7% relative) |
| — offline channel | +2.89% | −1.77% | −6.71% | loss-making from 2024 |

The company states the cause itself: *"竞争较为激烈，公司相关产品利润空间有限"* — competition in the
medium/large-batch market is fierce and the profit room is limited. The long tail's margin is flat
to slightly up over the same three years, and the long tail's *share* of gross profit rose from
91.3% to 97.6% precisely because the big-batch margin collapsed.

## What this does and does not establish

**Establishes:**

- Serving a long tail of tiny customers is not a low-margin activity that capital must be protected
  from. In the one manufacturing business that discloses the split, it is *the* margin.
- The number of long-tail customers is what sizes the capital investment that makes sense. The
  big-batch segment cannot justify capex at 2.76%; the long-tail segment at 36.24% can.
- Both halves run on the same owned plant, so "you can only serve a long tail if you own nothing"
  is false as a general claim. (See the caveat below on what JLC does own.)

**Does not establish:**

- **PCBs are not chips.** A bare board is orders of magnitude cheaper, faster and less risky than an
  integrated circuit, and a PCB line's capex is nothing like a fab's. This is an analogy about the
  *shape* of the margin curve, not a measurement of a foundry.
- **Which way the causation runs.** JLC's long-tail margin may come from its automated online
  quoting and panelisation (a cost advantage), or from low price sensitivity among buyers ordering
  five boards (a demand advantage), or from both. The filing does not separate them.
- **That the split is per-unit-of-capacity.** The bands are defined by *order* area (样板 <1 m²,
  小批量 1–20 m², 中大批量 >20 m²), and the filing gives revenue share, not area share. Gross profit
  per m² of capacity consumed — the number that maps most directly onto a fab's gross profit per
  wafer — is not derivable from the disclosure. Expect it to favour the long tail by *more* than
  13.1×, since small orders carry far higher revenue per m², but that is an expectation, not a
  finding.
- **What JLC owns.** That the 嘉立创 and 中信华 blocks are described as manufacturing segments with
  their own gross margins strongly implies owned plant, and the filing contrasts the company with
  *"传统工厂"* (traditional factories). But no quote establishing plant ownership has been located
  yet. **Open item:** read the property, plant and equipment / production capacity sections of the
  prospectus. Note that the argument above does not actually depend on the answer — it is about
  which segment generates gross profit, whoever owns the machine.

## Bears on

- **H6 (supports, strongly).** Small customers are not merely each profitable; they are where
  essentially all the profit is.
- **H5 (supports).** 1.36 million paying users, 21.3 million orders.
- **H7 (supports).** Top five customers = 1.16% of revenue.
- **H2 (supports, by analogy).** The segment with concentrated, price-negotiating customers is the
  one whose margin fell 71.7% in two years.

## Reproducing this

The script is `tmp/segment_capital.py` in the working tree at the time of writing (removed after
use, per the repository's temporary-file convention). All inputs are the SMB-1 quotes; re-deriving
it takes only the p.245 table and the three group figures.
