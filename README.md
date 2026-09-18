# foundry.api

> ## ⚠️ Warning: AI in use — use at own risk
>
> Almost everything in this repository was written with heavy use of AI (Claude). It has been
> directed and reviewed by a human, but it has not been independently verified end to end.
> Expect mistakes: wrong numbers, misread sources, confident-sounding claims that don't hold up,
> and design decisions that contradict each other between documents.
>
> Check anything you intend to rely on against the primary source before you use it. The
> `resources/` directory records which sources have actually been verified and which are still
> unchecked leads — treat the unchecked ones as unproven.

*An open, auction-scheduled silicon/MEMS foundry, designed API-first.*

Anyone can design a chip now; almost nobody can make one. Today's leading fabs are built around a
handful of very large, high-touch customers. foundry.api explores running a fab the other way:
for a large number of small, low-touch customers, with every machine's time sold by open auction
to the highest bidder, and everything — queues, prices, machine state, results — public.

This is a set of design documents and collected evidence. There is no working software here yet.

## Start here

| Document | What it is |
|---|---|
| [`WHY.md`](WHY.md) | **Why.** Why chip manufacturing got stuck serving a few giants, and why that could change. Written for people who know open source, cloud and AI, but not the chip industry. Draft v0.6. |
| [`PRINCIPLES.md`](PRINCIPLES.md) | **How, in principle.** Six priority-ordered principles, what each one means, how they interact, worked scenarios, and the questions still open. This is the root document. Draft v0.12. |
| [`AUCTIONS.md`](AUCTIONS.md) | **The auction, undecided.** Seven candidate auction and bid styles worked through the same three cases, with the pros and cons of each. A comparison, not a decision. Draft v0.1. |
| [`DESIGN.md`](DESIGN.md) | **The detailed design.** API, data model, scheduling and clearing. Older than the principles and not yet rewritten to match them; the known conflicts are listed in its Appendix C. Draft v0.3. |
| [`resources/`](resources/) | **The evidence.** Hypotheses (H1–H11), reference entries with verification status, and analyses. |

`PRINCIPLES.md` is the root. Where a design conflicts with a principle, the principle wins and the
design records the conflict.

## Status

Early and unsettled. In particular:

- The auction mechanism is not chosen. It needs simulation ([`AUCTIONS.md`](AUCTIONS.md), `PRINCIPLES.md` Q16).
- The settlement model — whether a customer pays for the time bought or the time actually used — is still contradictory inside `PRINCIPLES.md`.
- Several hypotheses have thin evidence, especially latent demand and whether small customers can each be profitable ([`resources/hypotheses.md`](resources/hypotheses.md)).
- `DESIGN.md` predates the principles.

Criticism, counter-evidence and sources that contradict the argument are welcome; see
[`resources/README.md`](resources/README.md) for how evidence is recorded.

## Licence

Apache 2.0. See [`LICENSE`](LICENSE).
