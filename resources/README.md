# Resources

This directory tracks the evidence behind foundry.api: references, papers, data, analyses and deep dives. For each one it records what the item actually says and whether it **supports** or **challenges** our hypotheses.

It is a working notebook, not a finished document. `WHY.md` and `PRINCIPLES.md` are where arguments are made. This directory is where the evidence for, and against, those arguments is collected and weighed.

## Layout

| Path | What it holds |
|---|---|
| [`hypotheses.md`](hypotheses.md) | The hypotheses we are testing (H1, H2, …). Each one links to the evidence for and against it. Start here. |
| [`references/`](references/) | Reference entries, grouped by topic. One entry per source. |
| [`demand/`](demand/) | Evidence gathered specifically on H5 (is there a long tail of demand for chips?) and H6 (can each small customer be profitable?), plus a log of what was searched and what could not be reached. |
| [`analyses/`](analyses/) | Longer write-ups: assessments of outside reports, internal reviews, and deep dives on a single question. |

### Reference topics

| File | ID prefix | Covers |
|---|---|---|
| [`references/software-analogies.md`](references/software-analogies.md) | `SW` | What cloud computing and open source did to the cost of trying ideas in software |
| [`references/costs-and-consolidation.md`](references/costs-and-consolidation.md) | `COST` | Chip design costs, fab costs, and how few companies can still keep up |
| [`references/customer-concentration.md`](references/customer-concentration.md) | `CONC` | Foundries' dependence on a few customers: filings, market share, case histories |
| [`references/finance-and-contracts.md`](references/finance-and-contracts.md) | `FIN` | Economics and finance research on buyer power, hold-up, and the cost of customer concentration |
| [`references/process-change-and-risk.md`](references/process-change-and-risk.md) | `RISK` | Why fabs avoid changing processes |
| [`references/learning-curves.md`](references/learning-curves.md) | `LEARN` | Wright's law, the experience curve, learning spillovers, and granular technologies |
| [`references/long-tail.md`](references/long-tail.md) | `TAIL` | The long tail, and the evidence against it |
| [`references/open-silicon-and-ai.md`](references/open-silicon-and-ai.md) | `OPEN` | Open design kits, open tools, cheap shuttles, AI-assisted design, and failures |

## Conventions

### Entry format

Each reference entry uses this shape:

```markdown
### CONC-1. Short title

- **Source:** Author, "Title", Publication, date. <URL>
- **Verification:** Verified | Partial | Lead (see below), with the date checked
- **What it says:** the key findings, with exact quotes where they matter
- **Bears on:** H2 (supports), H7 (challenges), …
- **Used in:** where our documents use it (e.g. `WHY.md` §2), or "not yet"
- **Caveats:** limits, disputes, conflicting figures
```

### Verification status

| Status | Meaning |
|---|---|
| **Verified** | We read the primary source ourselves and checked the quotes and figures word for word. The entry gives the date checked. |
| **Partial** | Some claims are checked, others aren't, or the claims were checked only against a secondary source (a news report of a filing, say). The entry says which parts. |
| **Lead** | Not checked. Usually taken from someone else's report. Never cite a Lead in `WHY.md` or `PRINCIPLES.md` until it has been verified. |

### How evidence bears on a hypothesis

| Label | Meaning |
|---|---|
| **Supports** | Makes the hypothesis more likely to be true |
| **Challenges** | Makes it less likely, or shows a limit or counter-example |
| **Mixed** | Cuts both ways |
| **Context** | Background needed to judge the hypothesis, without pushing either way |

### Rules

- **Challenges are as valuable as support.** Record them with the same care. Don't soften them.
- **Quote exactly.** Where an exact quote matters, copy it word for word, including the source's spelling (for example "labor"), and say where it appears.
- **Sites that block automated tools.** Many sites (SEC, BCG, some publishers) block automated fetch tools. Record whether a link loads in an ordinary browser, and how the source was checked.
- **Keep the index current.** When adding an entry, also update the relevant hypothesis in `hypotheses.md`.
- **Dates.** Use ISO 8601 (YYYY-MM-DD).
