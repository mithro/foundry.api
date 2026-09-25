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
| [`references/economics-of-concentration.md`](references/economics-of-concentration.md) | `ECON` | Economics literature on customer concentration, harvested from other reports' reference lists |

### Evidence gathered for specific questions

`resources/demand/` holds evidence gathered to test H5 and H6 directly, rather than reference
entries harvested from the literature. It has its own [`README.md`](demand/README.md) and its own
ID prefixes:

| File | ID prefix | Covers |
|---|---|---|
| [`demand/shuttle-programmes.md`](demand/shuttle-programmes.md), [`demand/latent-demand-challenges.md`](demand/latent-demand-challenges.md) | `DEM` | Multi-project wafer and shuttle programmes, and the evidence against latent demand |
| [`demand/long-tail-businesses.md`](demand/long-tail-businesses.md), [`demand/pricing-and-cost-to-serve.md`](demand/pricing-and-cost-to-serve.md) | `SMB` | Public financials of long-tail manufacturing businesses, and what small-volume fabrication costs |
| [`demand/open-programme-growth.md`](demand/open-programme-growth.md) | `OPG` | Growth of the open-entry programmes |
| [`demand/payment-growth.md`](demand/payment-growth.md) | `PAY` | Money actually paid, per year, for the three programmes where customers pay: Tiny Tapeout, chipIgnite/ChipFoundry, wafer.space |
| [`demand/chipfoundry.md`](demand/chipfoundry.md) | `CF` | ChipFoundry (UmbraLogic Technologies LLC): the corrected corporate history, every published per-shuttle number, the whole price list, and a verdict on whether an unsubsidised, investor-free open-shuttle business works |
| [`demand/design-starts-and-mature-nodes.md`](demand/design-starts-and-mature-nodes.md) | `TRAD` | Design starts and mature-node demand in the traditional industry |
| [`demand/pcb-industry-comparables.md`](demand/pcb-industry-comparables.md) | `PCB` | Audited PCB makers' margin by order size — the closest industry parallel |
| [`demand/fab-local-news-intl.md`](demand/fab-local-news-intl.md) | `LNI` | What a small, specialty, MEMS or mature-node fab outside the US costs per square metre of cleanroom and per job, from local papers, municipal planning files, regional development agencies and filed accounts — with every non-English quote translated |
| [`demand/software-margins.md`](demand/software-margins.md) | `SWM` | What a software business actually earns, measured rather than recalled: the **whole distribution** of US-listed software and computer-services filers built from the SEC's XBRL frames API — operating margin, asset turnover, return on assets, gross margin, R&D, SG&A, stock-based compensation, capex and PP&E intensity, reported as median and quartiles by SIC code — plus seventeen named comparators with accession numbers, eight GAAP-versus-non-GAAP reconciliations, the DuPont decomposition against Silex's 22.7%, the AWS segment, and the Rule-of-40 growth-versus-margin regression |
| [`demand/other-industry-margins.md`](demand/other-industry-margins.md) | `OIM` | The same disclosure hunted outside PCBs: margin split by order size, batch size or channel in printing, pharmaceutical contract manufacturing, a MEMS wafer foundry, metals processing and freight — including the cases where the *bulk* end carries the margin |
| [`demand/in-house-fabrication.md`](demand/in-house-fabrication.md) | `IHF` | Companies that built or bought their own fab, and what it cost |
| [`demand/access-terms.md`](demand/access-terms.md) | `ACC` | What a programme requires before it will make your chip, and who pays |
| [`demand/fab-local-news.md`](demand/fab-local-news.md) | `LN` | What a small US fab costs to stand up and staff: capital cost per job and per unit of capacity, the CHIPS/state/county subsidy attached, head count, cleanroom area and node — from SEC filings, county agreements, state economic-development records and local news |
| [`demand/chipfoundry.md`](demand/chipfoundry.md) | `CF` | ChipFoundry: corporate history, shuttle commitment curves, prices and terms |
| [`demand/mosis-funding.md`](demand/mosis-funding.md) | `MOS` | MOSIS: DARPA's actual spend, the funding timeline, price and throughput series, head count, and the verdict on "self-sustaining for 40 years" |
| [`demand/programme-funding.md`](demand/programme-funding.md) | `FUND` | What a multi-project-wafer service costs to run, against what it charges |
| [`demand/programme-funding-deep.md`](demand/programme-funding-deep.md) | `FUNDX` | What the money buys, and how much of it is people: CMC's audited accounts, the FP7 grant reports, the Chips JU portfolio, head-count and payroll |
| [`demand/broker-productivity.md`](demand/broker-productivity.md) | `PRD` | Designs shipped per staff-member per year at MOSIS, Europractice and CMC: whether the four numbers measure the same thing (mostly they do not), the extended 1982–1987 MOSIS staff-and-throughput series recovered from five DTIC reports, and what actually drives the difference — batch size, scope creep and node advance |
| [`demand/payment-growth.md`](demand/payment-growth.md) | `PAY` | Money actually paid, over time, by the unsubsidised programmes |
| [`demand/in-house-fabrication.md`](demand/in-house-fabrication.md) | `IHF` | Companies that built or bought their own fab, and what it cost |
| [`demand/pcb-industry-comparables.md`](demand/pcb-industry-comparables.md) | `PCB` | Audited PCB makers' margin by order size |
| [`analyses/industry-parallels.md`](analyses/industry-parallels.md) | `PAR` | Parallels from cloud, machine learning, open source and the internet |
| [`analyses/designs-per-head.md`](analyses/designs-per-head.md) | — | Why the per-head productivity claim was withdrawn, and the batch-size finding that replaced it: MOSIS 32.8 designs per run, Europractice 3.04, Tiny Tapeout 124.3 |
| [`demand/programme-funding.md`](demand/programme-funding.md) | `FUND` | What a multi-project-wafer service costs to run: the EU grants behind Europractice, the federal money behind MOSIS, CMC's published accounts, and the subsidy per design |
| [`demand/shuttle-programmes.md`](demand/shuttle-programmes.md) | `DEM` | Multi-project wafer and shuttle programmes: designs submitted, accepted, and how full the runs were |
| [`demand/latent-demand-challenges.md`](demand/latent-demand-challenges.md) | `DEM` | Evidence that the latent demand for chips is not there, or that cost is not the binding constraint |
| [`demand/long-tail-businesses.md`](demand/long-tail-businesses.md) | `SMB` | Public financials of businesses serving a long tail of small manufacturing customers, and the ones that failed |
| [`demand/pricing-and-cost-to-serve.md`](demand/pricing-and-cost-to-serve.md) | `SMB` | Published prices for small-volume fabrication, mask and NRE costs, and the cost of serving a small customer |
| [`demand/README.md`](demand/README.md) | — | What H5 and H6 claim, what would prove or falsify each, which ID ranges live in which file |
| [`demand/search-log.md`](demand/search-log.md) | — | What was searched, what came back, every dead end, and which sites blocked automated tools |

`DEM` and `SMB` each run one sequence of numbers across their two files, so the numbers are not
contiguous within a file. [`demand/README.md`](demand/README.md) gives the ranges, and
[`demand/search-log.md`](demand/search-log.md) records the searches and the dead ends behind them.

## Conventions

### Entry format

Each reference entry uses this shape:

```markdown
### CONC-1. Short title

- **Source:** Author, "Title", Publication, date. <URL>   (or **Sources:** for several)
- **Verification:** Verified | Partial | Lead (see below), with the date checked
- **How it was counted:** optional — the reproducible method, where a figure was counted from data
  rather than quoted
- **What it says:** the key findings, with exact quotes where they matter
- **DERIVED (arithmetic written out):** optional — figures we computed, never presented as quotes.
  Small one-off derivations can instead be labelled **DERIVED** inline inside "Bears on"
- **Bears on:** H2 (supports), H7 (challenges), …
- **Used in:** where our documents use it (e.g. `WHY.md` §2), or "not yet"
- **Caveats:** limits, disputes, conflicting figures
```

`Source`/`Sources`, `Verification`, `What it says`, `Bears on`, `Used in` and `Caveats` are
required; `How it was counted` and `DERIVED` are optional and appear in the order shown.

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

## Checking the directory

```
uv run python tools/check_resources.py            # structural checks, no network
uv run python tools/check_resources.py --network  # also re-fetch every cited URL
uv run python tools/check_resources.py --strict   # exit 1 on any finding, for CI or a hook
```

**Run it before committing anything to `resources/`, and run `--network` before citing an entry in
`WHY.md` or `PRINCIPLES.md`.**

It exists because a specific set of errors sat here undiscovered for days: a claim that a page was
live after it had begun redirecting; a claim that a price was unpublished when it was published; an
entry left at **Partial** after somebody had verified it; an ID cited eighteen times that resolved
to nothing because its heading used the wrong level; and an absolute claim — "every free or
subsidised programme found has been oversubscribed" — contradicted by another entry in this same
directory. Each check targets one of those.

| Check | What it catches |
|---|---|
| **C1** duplicate ID | The same entry ID defined twice, so a citation is ambiguous |
| **C2** dangling reference | A citation to an ID that does not exist anywhere |
| **C3** Lead cited | An unverified **Lead** cited in `WHY.md` or `PRINCIPLES.md`, which the rules forbid |
| **C4** unindexed prefix | A new file whose ID prefix was never added to an index table |
| **C5** missing status or date | An entry with no **Verification:** line, or a non-Lead entry with no ISO date |
| **C6** stale volatile claim | An entry asserting something about live web state, or citing a moving source, not re-checked within `--stale-days` (default 60) |
| **C7** absolute claim | An evidential quantifier — "every…", "none of them", "no X has ever", "the only…" — in `hypotheses.md`, `WHY.md` or `PRINCIPLES.md`, where claims get compressed and lose their qualifiers |
| **C8** URL not 200 | *(--network)* A cited source that no longer resolves as it did |

**C6 and C7 are advisory.** They are prompts to re-check, not errors, and they are expected to fire.
C1–C5 and C8 are defects and should be fixed or explained.

Three entries currently fail C5 by design — `CF-17`, `PAR-37` and `TRAD-8` are verdict and summary
sections rather than sourced entries. Leave them, or give them a status line saying so.
