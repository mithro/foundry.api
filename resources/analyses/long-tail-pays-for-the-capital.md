# The long tail is what pays for the capital

*Status: our own arithmetic, computed 2026-09-18 from figures quoted verbatim in
[`../demand/long-tail-businesses.md`](../demand/long-tail-businesses.md) SMB-1. Every input is a
printed number from the JLC prospectus; every output is reproducible from the script quoted below.*

*A note on language: the source is a Chinese-language filing. Chinese passages are quoted in the
original because the original is the evidence; **the English renderings are ours**, and each follows
the passage it translates.*

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
| 2023 | 样板、小批量 (sample boards + small batch) | 74.38% | 35.27% | **91.31%** |
| 2023 | 中大批量 (medium and large batch) | 25.62% | 9.74% | 8.69% |
| 2024 | sample + small-batch | 75.61% | 37.28% | **93.81%** |
| 2024 | medium/large-batch | 24.39% | 7.63% | 6.19% |
| 2025 | sample + small-batch | 75.57% | 36.24% | **97.60%** |
| 2025 | medium/large-batch | 24.43% | 2.76% | 2.40% |

**In 2025 the long tail was three-quarters of revenue and 97.6% of gross profit.** The big-batch
business — the kind of work a conventional factory is built to chase — contributed 2.4%.

The table reconciles: Σ(share × margin) gives 28.735% / 30.046% / 28.058% against the printed
合计 ("total") subtotals of 28.73% / 30.05% / 28.06%, agreeing to within 0.005 pp in all three
years. The
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

**Quote that ratio as a range, not a point.** It was **3.6× in 2023 and 4.9× in 2024**; it reached
13.1× only because the big-batch margin collapsed, and because the denominator is small a 1 pp error
in it gives 9.6× or 20.6×. The *direction* is robust; the magnitude is not.

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

The company states the cause itself: *"竞争较为激烈，公司相关产品利润空间有限"* — "competition is
relatively fierce and the profit room for the Company's related products is limited", i.e.
competition in the medium/large-batch market is fierce and the profit room is limited. The long tail's margin is flat
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
- **That the split is per-unit-of-capacity.** The bands are defined by *order* area
  (样板, sample boards, <1 m²; 小批量, small batch, 1–20 m²; 中大批量, medium and large batch,
  >20 m²), and the filing gives revenue share, not area share. Gross profit
  per m² of capacity consumed — the number that maps most directly onto a fab's gross profit per
  wafer — is not derivable from the disclosure. Expect it to favour the long tail by *more* than
  13.1×, since small orders carry far higher revenue per m², but that is an expectation, not a
  finding.
- ~~**What JLC owns.**~~ **Settled 2026-09-19 — see PCB-2 in
  [`../demand/pcb-industry-comparables.md`](../demand/pcb-industry-comparables.md).** JLC owns its
  plants outright: *"自有的生产仓储基地"* ("its own production and warehousing bases"),
  *"五大数字化自营生产基地"* ("five digital, self-operated production bases"), net fixed assets
  **CNY 3,257,464,600** of which **CNY 952,981,900** is buildings, capex **CNY 1,395,139,797.89** in
  2025, land-use rights of CNY 469m with registered title numbers. It is not a broker. The
  Xometry-versus-Protolabs framing this document opens with is therefore refuted directly by the
  balance sheet of the company it analyses.
- **Capital intensity, for comparison:** JLC turns its fixed assets **3.16× a year**; Fastprint,
  its largest named peer, turns them **1.19×**.

## The idle-plant test, and what it settles

The strongest objection to this analysis is that the big-batch segment might be **yield-management
filler** — work taken at 2.76% to keep an otherwise idle plant busy, in which case the long tail's
36% margin is partly *enabled* by having somewhere to dump spare capacity, and a long-tail-only fab
would have nobody to sell its slack to. On any plausible revenue-per-m² ratio the big-batch segment
consumes 40–94% of the plant for 2.4% of the gross profit, which is exactly what filler would look
like.

**The prospectus answers it, and the answer goes the other way.** JLC recorded an audited
fixed-asset impairment of **CNY 131,365,100** at end-2025:

> 因 **PCB 中大批量订单相对不饱和**等原因导致公司部分机器设备出现闲置的情形…计提了固定资产减值准备

— "because medium- and large-batch PCB orders were relatively unsaturated, some of the Company's
machinery and equipment became idle … a provision for impairment of fixed assets was recognised."
The provision is *"主要为对江西中信华、江苏中信华固定资产所计提"* — "recognised mainly against the
fixed assets of 江西中信华 (Jiangxi Zhongxinhua) and 江苏中信华 (Jiangsu Zhongxinhua)" — and the
subsidiary schedule identifies 江苏中信华 (Jiangsu Zhongxinhua) as the *"中大批量PCB生产基地"*, the
medium- and large-batch PCB production base.

So the big-batch plant is not absorbing slack from the long tail. **It is idle enough to be written
down**, while the long-tail plant runs at 76.78% utilisation and 99.33% sell-through. The filler
hypothesis is not supported in the one case where it can be tested.

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
