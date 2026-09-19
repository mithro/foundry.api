# Demand and small-customer economics (`DEM`, `SMB`)

This directory collects the evidence for and against the two hypotheses the whole foundry.api
argument rests on, and which the rest of the repository had the least evidence for:

- **H5. There is a long tail of demand for chips.** Many potential chip customers exist whose ideas
  are never made because the up-front cost is too high. If that cost falls, they add up to a real
  market.
- **H6. Small customers can each be profitable.** If the fab does no per-customer engineering and
  sells machine time at published prices, each small customer is profitable.

## Why these two matter more than the others

foundry.api proposes running a chip factory for a large number of small, low-touch customers instead
of a handful of large, high-touch ones (see the root [`README.md`](../../README.md) and
[`WHY.md`](../../WHY.md) §5).

Two things have to be true for that to be a business rather than a hobby:

1. **The customers have to exist.** Not "would be nice to have" — actually exist, in numbers, and be
   willing to pay. If the reason few people make chips is something other than up-front cost —
   design skill, verification effort, IP licensing, packaging, test, certification, or simply that
   an FPGA or an off-the-shelf part does the job — then dropping the price changes little. H5 fails
   and the model has no market.
2. **Each of them has to pay for itself.** A fab has enormous fixed costs. If serving a small
   customer costs more than that customer pays, then a thousand of them is a thousand times the
   loss, not a business. H6 fails and the model is a subsidy.

If either fails, the thesis fails. Neither is a detail.

## What would convince us, and what would falsify each one

**H5 would be convincingly proven by:** submission counts to low-cost shuttle and multi-project
wafer (MPW) programmes that grow over time and consistently exceed the capacity offered; waiting
lists; rejection rates; customers who arrive with no prior chip experience; and cases of a small
customer growing into a large one.

**H5 would be falsified by:** shuttle programmes that offer capacity and cannot fill it; programmes
that close for want of takers; evidence that the number of chip design starts is flat or falling
even as the cost of trying falls; or credible evidence that cost is not the binding constraint.

**H6 would be convincingly proven by:** published accounts of a manufacturing business that serves
tens of thousands of very small customers at a healthy gross margin, with a disclosed cost to serve;
or MPW price lists that can be compared with the underlying wafer and mask cost and shown to cover
it.

**H6 would be falsified by:** such a business earning a thin or negative margin; a pattern of these
businesses failing; or cost-to-serve analysis showing small customers cost more than they pay.

**Both hypotheses are about the fab's side of the transaction, and both are honestly still open.**
Read the Status lines in [`../hypotheses.md`](../hypotheses.md) before you cite anything from here.

## How the entries are organised

| File | IDs | Covers |
|---|---|---|
| [`shuttle-programmes.md`](shuttle-programmes.md) | `DEM-1` … `DEM-10`, `DEM-16` … `DEM-19` | Multi-project wafer and shuttle programmes: how many designs are submitted, how many are accepted, how full the runs are, and how that changed over time |
| [`latent-demand-challenges.md`](latent-demand-challenges.md) | `DEM-11` … `DEM-15`, `DEM-20` … `DEM-22` | Evidence that the latent demand is not there, or that cost is not the binding constraint |
| [`long-tail-businesses.md`](long-tail-businesses.md) | `SMB-1` … `SMB-6` | Public financials of businesses built on a long tail of small manufacturing customers, and the ones that failed |
| [`pricing-and-cost-to-serve.md`](pricing-and-cost-to-serve.md) | `SMB-7` … `SMB-13` | Published prices for small-volume fabrication, mask and NRE costs, and what it costs to serve a small customer |
| [`in-house-fabrication.md`](in-house-fabrication.md) | `IHF-1` … `IHF-11` | Companies that built or bought their own silicon or MEMS fabrication rather than buy the service, why, and what it cost. Runs its own number sequence |
| [`pcb-industry-comparables.md`](pcb-industry-comparables.md) | `PCB-1` … `PCB-6` | Audited PCB makers' gross margin by order size, customer counts, concentration and capital intensity — the closest industry parallel to selling fabrication online to a long tail |
| [`access-terms.md`](access-terms.md) | `ACC-1` … `ACC-16` | What a programme requires before it will make your chip: prices, NDAs, PDK licences, eligibility, tooling, gatekeepers, export control — and who pays |
| [`search-log.md`](search-log.md) | — | What was searched, what came back, and every dead end, so nobody repeats the search |

Each prefix uses a single running number **across** its files, so `DEM-9` and `SMB-9` are each unique
wherever they sit. The numbers are therefore not contiguous within a file: the ranges above say which
are where. Counter-evidence that belongs beside the number it qualifies — undersubscribed shuttle
runs, for instance — stays in `shuttle-programmes.md` rather than being moved to the challenges file.

The two prefixes are new and do not collide with the existing `SW`, `COST`, `CONC`, `FIN`, `RISK`,
`LEARN`, `TAIL` or `OPEN` entries in [`../references/`](../references/).

## Reading the verification statuses

Same three statuses as the rest of `resources/` — see [`../README.md`](../README.md). In short:

| Status | Meaning |
|---|---|
| **Verified** | Somebody fetched the primary source and read the quoted words and figures in it, on the date given. Where a number was counted or derived rather than quoted, the entry shows the method or the arithmetic. |
| **Partial** | Only part was checked, or it was checked only against a secondary source. The entry says exactly which part. |
| **Lead** | Not checked. Never cite a Lead in `WHY.md` or `PRINCIPLES.md`. |

Two conventions matter especially here:

- **Derived numbers are labelled `DERIVED` and the arithmetic is written out**, so a reader can
  check it. A derived number is never presented as a quote.
- **Blocked sources are kept, not deleted.** If a source could not be reached, the entry says which
  URL, what happened, what was tried, and what would unblock it for a human with library access. See
  [`search-log.md`](search-log.md) for the full list. A well-documented dead end is a result.

## The rule this directory is held to

From [`../README.md`](../README.md): *"Challenges are as valuable as support. Record them with the
same care. Don't soften them."* Several entries here damage H5 or H6. They are labelled
**challenges** and they are not buried.
