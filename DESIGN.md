# foundry.api — Design Document (Draft v0.3)

*Open, auction-scheduled silicon/MEMS foundry orchestration prototype*

| | |
|---|---|
| Status | Draft v0.3 |
| Date | 2026-09-12 |
| License | Apache 2.0 (code, schemas, docs) |

> **Foundry in the cloud: make a chip, quick.** Anyone can design a chip now; everyone should be able to make one. Today's fabs are run by three big, high-touch customers. foundry.api is the software for running a fab the other way — for a large number of small, low-touch customers: fabrication as a service with no custom engineering, every machine's time auctioned openly to the highest bidder, and everything — queues, prices, tool states, results — public.

---

## 0. Summary

foundry.api is an API-first service for running an open, auction-scheduled foundry. It lets anyone:

- **Define a recipe** — an ordered list of process, metrology, analysis and logistics steps executed on the foundry's machines, built from forkable templates, and checked against rules that protect the foundry's machines and operations — never against whether the device will work.
- **Order a recipe** against a design (GDS), a set of physical assets (wafers and masks — foundry-supplied or shipped in) and a bid schedule.
- **Have every step scheduled by auction** — each machine continuously sells its next run to the bidder offering the most per machine-hour. The foundry itself is a bidder, setting a floor or paying to keep expensive-to-stop tools running.

Everything is public: machines and their programs, live auctions, what is on every tool, storage, ledgers and run assets. A read-only web GUI renders this state; all writes go through the API.

---

## 1. Motivation

Anyone can design a chip now; almost nobody can get one made quickly. The typical fab earns ~70 % of its revenue from three customers, who use that leverage to compress margins, and it is organisationally hostile to adding small customers because every new customer means custom engineering (NRE). Academic nanofabs absorb a few thousand designs a year but are slow and non-commercial.

foundry.api exists to run a foundry the opposite way:

- **Many customers, less bespoke work.** Fabrication as a service: fixed machine programs and forkable templates instead of per-customer process development. The foundry sells qualified capabilities, not engineering hours.
- **Machine time as an open market.** Like a compute spot market, every tool's next slot is auctioned publicly to the highest bidder; the foundry participates with its own bids rather than negotiating contracts.
- **Speed as the product.** Faster iteration *is* better design. The system is built to make cycle time visible and biddable, so a customer can buy speed when they need it.
- **Transparency as the customer-acquisition strategy.** Publishing every queue, price, and machine state removes the information asymmetry that makes fabs unapproachable.

The longer-term direction is silicon as a cloud service: designs go in, measured data (e-test, probe, characterisation) comes out, and physical delivery becomes optional.

---

## 2. Goals, non-goals, principles

### 2.1 Goals

1. **Recipe authoring via API** from typed steps and forkable templates. Steps target a capability and may be locked to one machine or a set.
2. **Machine-protection validation only.** Recipes and designs are checked against rules that keep tools and foundry operations safe (limits, chemistries, contamination, form factor, pattern density, program compatibility, fillable mask orders). Nothing checks whether the *device* will work — that is the user's responsibility. Chemistry and thermal limits live in each machine's declared `limits`; global rules are structural.
3. **Orders with designs and physical assets.** Designs are public GDS/OASIS. Wafers and masks are tracked assets with owners, locations and storage charges.
4. **Money-only auction scheduling.** The bid worth the most per machine-hour runs next; the foundry bids too (reserve or subsidy); prices can be negative; guaranteed slots exist only as futures the foundry sells. If a lot is blocked because its owner won't pay, that is the intended outcome.
5. **Runs produce assets** (images, tables, logs, actual durations, consumable draws). Recipes can include metrology, analysis and halt conditions; a fired halt places the order in `held` until the owner decides.
6. **Machine registry, programs, consumables, utilisation, ledger** — all public.
7. **No new languages or formats.** Documents are YAML/JSON with JSON Schema. Assets use PNG/CSV/Parquet/JSON/NDJSON. Expressions, where unavoidable, use an existing sandboxed language or are delegated to callbacks.
8. **Read-only GUI.**

### 2.2 Design targets

Numbers the architecture, auction and GUI metrics should be judged against (from the motivating vision; not prototype requirements):

| Target | Value | Where it shows up |
|---|---|---|
| Customers | ~7,000 accounts at ~100 wafers/yr each | account and asset model scale; no per-customer configuration anywhere |
| Throughput | ~700,000 wafers/yr (gigafab-comparable) | event log and projection volumes; batch tools |
| Cycle time | ≤ 5 weeks order-to-data for a standard template | `projected_complete` on every order; cycle-time percentiles per template on the overview page |
| NRE | zero — templates + programs only, no custom process work | `programs_only` default (§5.1); templates as the primary path (§7) |
| Node focus | mature nodes: analog, power, industrial, secure silicon | shipped templates; SKY130 as the complex reference |

### 2.3 Non-goals (prototype)

- Real tool control (SECS/GEM, OPC-UA). The prototype ships a simulator behind the adapter interface.
- Confidentiality. Nothing is private except API secrets and webhook URLs.
- Real payments. Credits are abstract; prepaid and postpaid *enforcement* are demonstrated so a real foundry can plug in billing.
- Physics/TCAD, yield prediction, DRC-for-yield.

### 2.4 Principles

- API is the product; GUI is a viewer.
- Versioned, immutable, content-addressed documents.
- Explainable rejections: rule id, subject, measured value, limit, hint.
- Deterministic, replayable scheduling from an append-only event log.
- Boring technology: Postgres, one service, HTTP+JSON, SSE.

---

## 3. Reference processes

**Simple — Science Corp. TFE flow.** 3 masks (+ helper levels), 16 steps, 6-inch 500 µm fused silica: polyimide spin/cure, bilayer resist, contact litho, Ti/Pt/Au evaporation, lift-off, hard-mask etch, laser release. Shipped as template `tpl_tfe-3mask`.

**Complex — SkyWater S8/SKY130.** ~200 steps of `<mask> → <implant|etch> → <strip>` triplets between oxidations, LPCVD depositions, CMP and RTA anneals. Shipped as a ~40-step front-end excerpt `tpl_sky130-fe` using macros.

What they force into the model: step DAGs that are almost always linear, with macros; coupling windows between steps (resist coat → expose; HF dip → deposition); batch tools (furnaces, wet benches, implanters); contamination classes (no gold in front-end tools); fixed furnace programs (a tube that only runs its qualified 10-hour cycle); per-layer mask metadata; metrology after critical steps (film thickness after oxidation, sheet resistance after implant/anneal) with halt thresholds.

---

## 4. Glossary

| Term | Meaning |
|---|---|
| **Foundry** | One facility. One per deployment. Also an *account* that can bid. |
| **Account** | Anyone who can own assets, hold credits and bid: users (by API key) and the foundry itself. |
| **Machine** | A physical tool. Has capabilities, programs, limits, consumables, a foundry bid, state. |
| **Capability** | Typed thing a machine can do (`deposit.pvd.evaporation`). Steps request capabilities. |
| **Program** | A named, locked configuration on a machine (`furnace-A/bake_10h`) with an authoritative time model (setup, process, cleanup), a bundled rate per machine-hour and declared wafer-state effects. Steps may run "free" params within a capability's limits, or a program with fixed params. |
| **Consumable** | Something drawn per run: gas, chemical, resist, target, substrate wafer, mask blank, chamber hours. Charged in one of three modes (§11). |
| **Asset (physical)** | Wafer, lot, mask, carrier. Has owner, location, storage class, charges. |
| **Asset (run output)** | File produced by a run: image, table, log, telemetry, report. Public. |
| **Design** | Uploaded GDSII/OASIS + layer inventory. Public. |
| **Step** | Atomic recipe element: process, metrology, analysis, logistics or manual. |
| **Machine time** | The commodity every auction sells, in hours: `setup(previous program → program) + process(program, lot) + cleanup(program)`. Computed from the program, never estimated. |
| **Recipe / Template** | Steps (a DAG via `depends_on`, usually near-linear) + layer map + wafer spec + asset requirements. Immutable once published. |
| **Order → Lot → Order-step** | An order produces one lot (wafers); each recipe step becomes an order-step. One execution of an order-step on a machine is a *run*, the unit that is bid on and scheduled. |
| **Bid** | `max_credits` an account will pay in total for one run of an order-step. Auctions compare bids as an implied rate, `max_credits / machine_time(run)`, so a bidder whose program matches the machine's current program (no setup) gets more rate for the same money. |
| **Foundry bid** | The foundry's standing bid for a machine's own idle time, expressed as an adjustment to the program's bundled rate: `F = rate_credits_per_hour + adjustment`. Positive adjustment = reserve, negative = subsidy (F may go below zero), zero = break-even. Optionally overridden per program. |
| **Auction / Slot / Run** | Per-machine ranking of candidate runs → the next run, locked `clear_ahead_s` before the machine frees → the execution with telemetry and outputs. **A run belongs to exactly one account**; runs are never shared between accounts. |
| **Slot future** | A contract bought in advance: the right to have one named run start on a machine inside a time window at a fixed strike price, pre-empting the auction. Sold by the foundry; price-cap variants by external providers (§10.6). |
| **Halt** | A condition evaluated on run outputs; if true, the order goes to `held`. |
| **Ledger** | Append-only account entries: bids cleared, consumables, storage, shipping, insurance, claims, subsidies. |
| **Contamination class** | Ordered label on wafers and machines. Demo ordering: `clean < organic < metal_std < gold` (`organic` = resist/polyimide present). The ordering is a foundry-level ruleset constant, not a fixed enum. |

---

## 5. Domain model

```mermaid
erDiagram
    FOUNDRY ||--o{ MACHINE : has
    FOUNDRY ||--o{ STORAGE_LOCATION : has
    MACHINE ||--o{ CAPABILITY : provides
    MACHINE ||--o{ PROGRAM : "locked configs"
    MACHINE ||--|| FOUNDRY_BID : "standing bid"
    MACHINE ||--o{ RUN : executes
    ACCOUNT ||--o{ LEDGER_ENTRY : has
    ACCOUNT ||--o{ PHYSICAL_ASSET : owns
    ACCOUNT ||--o{ ORDER : places
    ACCOUNT ||--o{ CONSIGNMENT_STOCK : holds
    PHYSICAL_ASSET }o--|| STORAGE_LOCATION : "stored at (or on-tool / in-transit / external)"
    RECIPE ||--|{ STEP : "ordered"
    RECIPE ||--|| LAYER_MAP : declares
    ORDER }o--|| RECIPE : uses
    ORDER }o--o{ DESIGN : "mask set"
    ORDER ||--|| LOT : produces
    LOT ||--|{ WAFER : contains
    LOT ||--|{ ORDER_STEP : "one per step"
    ORDER_STEP ||--o{ BID : "current + history"
    ORDER_STEP }o--o| RUN : "executed in"
    RUN ||--o{ RUN_ASSET : produces
    RUN ||--o{ CONSUMABLE_DRAW : records
    ORDER ||--o{ HOLD : "held decisions"
    ORDER ||--o{ INSURANCE_POLICY : covered_by
    INSURANCE_POLICY }o--|| INSURANCE_PROVIDER : "foundry or external"
    SHIPMENT }o--o{ PHYSICAL_ASSET : moves
```

### 5.1 Machine (with programs and foundry bid)

```yaml
id: mach_furnace-A
name: "Furnace tube A (wet/dry oxidation)"
kind: thermal.furnace
wafer_sizes_mm: [150]
contamination_class: clean
batch: {fill: min, size: 25, min_fill: 5, carrier: quartz_boat_25}   # fill: single | any | min | exact (§10.2)
capabilities:
  - id: thermal.oxidation
    mode: programs_only              # free | programs_only | both
  - id: thermal.anneal.furnace
    mode: programs_only
programs:                            # locked configurations; a step references one by id
  - id: dry_ox_900_20nm
    capability: thermal.oxidation
    params: {temp_c: 900, ambient: dry_O2, time_min: 45, ramp_c_per_min: 10}   # constants
    time:                            # machine-time model — authoritative, not estimated (§10.2)
      setup_s: 1800                  # default when the previous program has no setup_matrix entry
      process_s: 9000                # per run (batch tools); per wafer when batch.fill == single
      cleanup_s: 0
    rate_credits_per_hour: 130       # bundled: machine time + bundled consumables (O2, N2, quartz wear); the foundry's cost basis
    metered_consumables: []          # none pass-through for this program
    effects:                         # wafer-state transitions applied by the wafer-state engine (§8)
      stack_push: {material: SiO2, thickness_nm: 20}
  - id: bake_10h
    capability: thermal.anneal.furnace
    params: {temp_c: 1000, ambient: N2, time_min: 600}
    time: {setup_s: 3600, process_s: 39600, cleanup_s: 0}
    rate_credits_per_hour: 150
    effects: {anneal: true}
limits:                              # machine-protection hard limits (still enforced even for programs)
  max_temp_c: 1150
  forbidden_wafer_materials: [Au, Cu, Al, photoresist, polyimide]
  gas_combinations:                  # per machine, not global: this tube has a pyrogenic torch and may burn H2 in O2
    allowed: [[H2, O2]]
    forbidden: [[SiH4, O2]]
foundry_bid:                         # the foundry's standing bid for this machine's idle time (§10.3)
  mode: subsidy                      # reserve | subsidy | none
  adjustment_credits_per_hour: -150  # F = program rate + adjustment → dry_ox clears down to −20 cr/h
  applies_when: no_competing_bid     # always | no_competing_bid — a subsidy only when the tube would otherwise idle
  budget_credits_per_day: 2000       # cap on subsidy paid out per day; exhausted → mode behaves as none
  per_program: {bake_10h: {adjustment_credits_per_hour: 0}}   # optional override
  note: "Tube must stay at temperature; cooling + requalification costs ~12 h — worth more than a run's consumables"
setup_matrix:                        # setup_s by previous program; same program → 0 (no entry needed)
  dry_ox_900_20nm→bake_10h: 1800
  bake_10h→dry_ox_900_20nm: 3600
clear_ahead_s: 1800                  # the next run is locked this long before the machine frees (§10.4)
state: {status: running, run_id: run_…, program: dry_ox_900_20nm, since: …, free_at: …}
```

Machines whose capability `mode: free` expose a params JSON Schema with limits and a time model as a function of params (implemented in code per capability, like consumable draw functions, §11.1); `both` lets a step either pick a program or supply params within limits. **Programs are the normal case**: a fixed catalogue of qualified configurations is what lets the foundry serve thousands of customers with no per-customer engineering (§1). Free params are the exception, for tools like RIE where users legitimately tune within a safe envelope.

**Batch `fill` modes.** `single`: one wafer at a time, `process_s` is per wafer. `any`: 1…`size` wafers per run. `min`: `min_fill`…`size`. `exact`: exactly `size` (a CMP tool whose heads must all be loaded); a lot smaller than `size` is topped up with foundry dummy wafers charged as the metered consumable `dummy_wafer_<diameter>`, or rejected at validation if the machine declares no `dummy_fill`. Whatever the mode, a run holds one account's lot (or several of its lots on the same program); the account pays for the whole run.

### 5.2 Step (in a recipe) — process, with pinning and coupling

```yaml
- id: BOX
  type: thermal.oxidation
  capability: thermal.oxidation
  machines: [mach_furnace-A]          # pin to one; or a list; or omit for "any machine with the capability"
  program: dry_ox_900_20nm            # locked config; params come from the program
  depends_on: SMAT
  max_queue_time_from_prev_s: 172800  # coupling window; on breach → order held (§10.6)
  outputs: []                         # expected run assets (declared by the program/type; may add more)
  default_bid_credits: 300            # max_credits for one run of this step, total incl. setup (§10.2); orders may override
```

### 5.3 Step — metrology, analysis, halt

```yaml
- id: BOX_thk
  type: metrology.thickness
  capability: metrology.ellipsometry
  program: sio2_on_si_9pt
  depends_on: BOX
  outputs:
    - {name: thickness_map, format: csv, schema: metrology.thickness_map/v1}   # columns: wafer_id, site, x_mm, y_mm, thickness_nm
    - {name: raw, format: json}
- id: BOX_check
  type: analysis.check                # no machine; runs on the analysis worker
  depends_on: BOX_thk
  inputs: [BOX_thk.thickness_map]
  checks:                             # declarative, no expression language needed for the common case
    - {id: thk_mean,  stat: mean, field: thickness_nm, min: 18.5, max: 21.5, unit: nm}
    - {id: thk_range, stat: max_minus_min, field: thickness_nm, max: 2.0, group_by: wafer_id}
  on_fail: hold                       # hold (default, §10.7) | continue (record findings, proceed) | abort
  outputs: [{name: report, format: json, schema: analysis.check_report/v1}]
- id: BOX_custom
  type: analysis.callback             # delegate anything richer to a callback
  depends_on: BOX_thk
  inputs: [BOX_thk.raw]
  callback: {url: https://example.org/foundry-hooks/box-analysis, timeout_s: 300, signing_key_id: k_…}
  on_fail: hold
- id: ISONIT
  type: deposit.cvd.lpcvd
  depends_on: [BOX_check, BOX_custom]  # depends_on takes one id or a list; steps form a DAG, not a chain
  program: sin_lpcvd_150nm
```

### 5.4 Step — logistics

```yaml
- id: MASKS
  type: logistics.mask_fab            # foundry orders photomasks from the design
  vendor: maskco                      # from the foundry's vendor list, with lead time & price per layer
  layers: [METAL1, OUTLINE1, TOPMETAL]
  spec: {blank: "5in quartz Cr", min_feature_um: 2.0}
- id: IN_INSPECT
  type: logistics.receive_inspect     # gate for anything arriving: user-shipped wafers/masks, external returns
  capability: metrology.incoming
  program: wafer_incoming_std         # visual, thickness, bow, flat orientation, contamination swab
  outputs: [{name: inspection, format: json, schema: logistics.inspection/v1}]
  on_fail: hold
- id: EXT_ALD
  type: logistics.external_process    # ship out, have something done, come back
  vendor: aldhouse
  shipment: {carrier: ups, service: express, insured: true}
  expected_turnaround_days: 7
  returns_to: IN_INSPECT_2            # every external return must be followed by receive_inspect
- id: SHIP
  type: logistics.ship_out            # outgoing shipping is part of the recipe
  destination: {account_address_ref: primary}
  packaging: wafer_carrier_25_n2
```

### 5.5 Physical assets

```yaml
id: wfr_01J8…
kind: wafer                          # wafer | mask | carrier
owner: acct_9f3e
lot: lot_01J8…
scribe: "FA-2026-09-0442-07"
spec: {material: fused_silica, diameter_mm: 150, thickness_um: 500}
state: {contamination_class: gold, materials: [Ti, Pt, Au, polyimide], resist_present: false}   # maintained by the wafer-state engine
location: {kind: storage, id: stor_n2cab-3, since: 2026-09-12T13:20:00Z}   # storage | on_tool | in_transit | external | disposed | shipped
storage_class: n2_cabinet             # drives the charge rate
provenance: foundry_supplied          # foundry_supplied | user_shipped | external_returned
history: [...]                        # every location change is an event
```

Masks are the same shape with `kind: mask`, `layer: METAL1`, `design: des_…`, `vendor_order: …`, `storage_class: mask_box`, and usage counts. A mask is a reusable asset: the same owner may reference it in later orders instead of paying for `logistics.mask_fab` again.

### 5.6 State machines

Written as transition tables (state × event → state) because every transition is an event in the log; the diagrams they replace could not show what happens to sibling steps, reworked steps or cancelled orders.

**Order** — `draft · validating · rejected · in_progress · held · complete · aborted`. There is no separate "awaiting assets" phase: wafer supply, mask fabrication and incoming inspection are ordinary logistics order-steps (§7.1), scheduled and charged like everything else.

| From | Event | To | Notes |
|---|---|---|---|
| `draft` | `order.submitted` | `validating` | recipe + design + assets + funding checked (§8, §9, §12) |
| `validating` | `validation.failed` | `rejected` | report public and permanent |
| `validating` | `validation.passed` | `in_progress` | order-steps created; roots become `eligible` |
| `in_progress` | `hold.opened` (any §10.7 reason) | `held` | eligible steps withdrawn from auctions |
| `held` | `hold.resolved {continue \| rework_to_step}` | `in_progress` | see order-step table |
| `held` | `hold.resolved {abort}` · `hold.timed_out` | `aborted` | assets stay in storage, charged, until shipped or disposed |
| `in_progress` | `order.cancelled` (owner) | `aborted` | a `running` run finishes and is charged; a `queued` run forfeits (§16) |
| `in_progress` | `order_step.done` (last step) | `complete` | |

**Order-step** — `blocked · eligible (sub-state unfunded) · queued · running · done · failed · skipped · cancelled`. Each order-step carries an `attempt` counter; rework creates a new attempt and keeps the old run and its assets in history.

| From | Event | To | Notes |
|---|---|---|---|
| `blocked` | all `depends_on` steps `done`/`skipped` and required assets present | `eligible` | |
| `eligible` | funding check fails / passes (§12.1) | `eligible.unfunded` ⇄ `eligible` | listed in the auction, never wins |
| `eligible` | order `held` / `continue` | `blocked · order_held` ⇄ `eligible` | |
| `eligible` | `auction.cleared` (or future exercised) | `queued` | locked; price reserved on the account |
| `queued` | `order_step.cancelled` (owner) | `eligible` | `forfeit` of the cleared price written; re-bid allowed |
| `queued` | `run.started` | `running` | |
| `running` | `run.finished {outcome: ok}` | `done` | analysis steps: `pass` |
| `running` | `run.finished {outcome: fail}` | `failed` | opens a hold with the run's `cause` and evidence |
| `eligible` · `queued` | coupling window breached (§10.6) | `failed` | hold reason `coupling_breach` |
| `failed` | `hold.resolved {continue}` | `skipped` | successors treat `skipped` as satisfied |
| `failed` | `hold.resolved {rework_to_step: X}` | `blocked` | X and every step downstream of X (including this one) get a new attempt; X becomes `eligible` when its inputs are present; earlier `done` steps are untouched |
| any non-terminal | order `aborted` | `cancelled` | |

**Machine** — `idle · setup · running · maintenance · down`, driven by adapter events (§15.2). `offline_by_bid` is a *derived* display state: `idle` with `foundry_bid.mode == reserve` and no candidate above the floor (§10.4). It is never stored.

| From | Event | To |
|---|---|---|
| `idle` | `run.dispatched` | `setup` (or `running` when setup is 0) |
| `setup` | `run.started` | `running` |
| `running` | `run.finished` | `idle` |
| any | `machine.state_changed {maintenance \| down}` (adapter or foundry) | `maintenance` / `down` — a `running` run finishes with `outcome: fail, cause: machine_fault` |
| `maintenance` · `down` | `machine.state_changed {idle}` | `idle` |

**Hold** — `open → resolved {action} | timed_out`. **Physical asset location** — `storage ⇄ on_tool`, `storage → in_transit → external → in_transit → awaiting_inspection → storage`, `storage → shipped`, `storage → disposed`; every change is an event (§5.5).

---

## 6. Architecture

```mermaid
flowchart LR
    subgraph clients [External clients]
        EDA[EDA / scripts / other systems]
        GUI[Read-only web GUI]
        CB[User callback endpoints]
        INS[External insurance providers]
    end
    subgraph core [foundry.api service]
        API[HTTP API · OpenAPI 3.1]
        RS[Recipes]
        OS[Orders · lots · assets]
        REG[Machine registry · programs]
        AUC[Auction & dispatch]
        LED[Ledger · accounts]
        EVT[(Event log)]
        DB[(Postgres)]
        OBJ[(Object store: designs, run assets)]
        SSE[SSE stream]
    end
    subgraph workers [Workers]
        RV[Recipe rule engine]
        DV[Design checker]
        AN[Analysis worker: checks + callbacks]
        BOT[Bid policies]
    end
    subgraph fab [Machine layer]
        SIM[Simulator]
        ADP[Real adapters - future]
    end
    EDA --> API
    GUI -->|GET| API
    GUI --> SSE
    API --> RS & OS & REG & LED
    RS --> RV
    OS --> DV
    OS --> AN --> CB
    LED <--> INS
    RS & OS & REG & LED --> DB
    OS & AUC & LED --> EVT --> SSE
    AUC <--> SIM
    AUC <-.-> ADP
    SIM --> REG
    SIM --> OBJ
```

**Language:** Python (FastAPI, Pydantic v2, SQLAlchemy/asyncpg, Postgres, `gdstk`/KLayout for GDS inventory and geometry checks, `pytest`). Scheduler is a pure module with no I/O so it could be ported to Go. Go-first alternative: keep the design checker and analysis worker as a Python sidecar. GUI: static TypeScript, `GET` + SSE only.

**Repository:** `foundry.api/` with `schemas/` (JSON Schema for every document), `templates/`, `rulesets/`, `foundries/demo/`, the Python package `foundryapi/` (`api`, `recipes`, `validation`, `orders`, `assets`, `scheduler`, `ledger`, `insurance`, `analysis`, `registry`, `sim`, `events`), `web/`, `tests/`, `docs/`.

---

## 7. Recipes

### 7.1 Document

YAML/JSON validated against `schemas/recipe.schema.json`. Published recipes are immutable, versioned, content-hashed.

```yaml
schema: foundry.api/recipe/v1
name: tfe-3mask
version: 3
forked_from: tpl_tfe-3mask@2
wafer: {material: fused_silica, diameter_mm: 150, thickness_um: 500, polish: DSP, initial_contamination_class: clean}
assets_in:                                   # expanded at publish into leading logistics steps (supply_wafers / mask_fab / receive_inspect), so provisioning is scheduled and charged like any other step
  wafers: {source: [foundry_supplied, user_shipped], min: 1, max: 25}     # max ≤ smallest batch.size on the path (MP-045)
  masks:  {source: [mask_fab, user_shipped, existing_asset], layers: [METAL1, OUTLINE1, TOPMETAL]}
layer_map:                                   # machine-protection metadata only: gds → name, polarity, which tool consumes it
  - {name: METAL1,   gds: [10, 0], polarity: light, required: true}
  - {name: VIA,      gds: [20, 0], polarity: dark,  required: true}
  - {name: OUTLINE1, gds: [20, 1], polarity: dark,  required: true}
  - {name: OUTLINE2, gds: [21, 0], polarity: dark}
  - {name: TAB,      gds: [22, 0], polarity: light}
  - {name: TOPMETAL, gds: [30, 0], polarity: light, required: true}
  - {name: RELEASE,  gds: [40, 0], polarity: light, required: true}
  - {name: XZONE,    gds: [41, 0], polarity: dark}
steps: [ ... ]                               # §5.2–5.4
```

The layer map carries no min width/space: those are yield rules and are the user's problem (§9). It carries what the foundry needs to protect tools: which layer feeds the laser (area limit), which is etched (density limit), polarity (mask-fab spec).

### 7.2 Step types (v0.3 catalogue)

| Family | Types | Notes |
|---|---|---|
| `coat.*` | `coat.spin`, `coat.spray` | |
| `litho.*` | `litho.expose_develop`, `litho.expose`, `litho.develop`, `litho.direct_write` | direct-write consumes a design layer, no mask asset |
| `deposit.*` | `pvd.evaporation`, `pvd.sputter`, `cvd.lpcvd`, `cvd.pecvd`, `ald`, `epi` | |
| `thermal.*` | `oxidation`, `anneal.furnace`, `anneal.rta`, `cure`, `bake` | usually `programs_only` |
| `etch.*` | `rie`, `drie`, `wet`, `ion_mill`, `xef2` | |
| `strip.*` | `wet`, `ash` | |
| `implant.*` | `ion` | |
| `planarize.*` | `cmp` | |
| `clean.*` | `rca`, `piranha`, `solvent`, `hf_dip` | |
| `metrology.*` | `thickness`, `profilometry`, `sem`, `optical`, `probe` (e-test), `sheet_resistance`, `incoming` | always declare `outputs` |
| `analysis.*` | `check` (declarative stats vs. limits), `callback` (delegated), `expr` (optional CEL, §13) | no machine; `on_fail: hold \| continue \| abort` |
| `logistics.*` | `supply_wafers` (foundry-supplied substrates, metered), `mask_fab`, `receive_inspect`, `external_process`, `ship_out`, `store` (explicit long-term storage with class) | provisioning steps are generated from `assets_in` |
| `backend.*` | `dice`, `release.laser`, `wafer_bond` | |
| `manual.*` | `inspect`, `note`, `operator_task` | scheduled on the `operator` pseudo-machine at its rate |

### 7.3 Macros, versioning, forking

YAML macros expanded at publish time; drafts mutable, publish freezes and assigns a version; forks carry lineage; any recipe referenced by an order is permanent.

---

## 8. Recipe validation (machine protection)

Rules are versioned documents in `rulesets/machine-protection.yaml`, evaluated against the expanded recipe, the machine registry (including programs) and a simulated wafer state threaded through the steps. **Rules protect machines, consumables and shared infrastructure — never the user's device.**

Rule bodies are written in the evaluator chosen in §13; the schema is evaluator-agnostic:

```yaml
schema: foundry.api/ruleset/v1
name: machine-protection
version: 8
rules:
  - id: MP-001  # Params within limits (free-mode capability) or program exists on a candidate machine
    scope: step
    severity: error
    evaluator: builtin              # a handful of rules are implemented in code because they are structural
    check: params_or_program_valid
  - id: MP-010  # Contamination class of wafer ≤ every candidate machine's class
    scope: step
    evaluator: builtin
    check: contamination_compatible
  - id: MP-011  # Forbidden wafer materials for machine
    scope: step
    evaluator: cel
    expr: "!machine.limits.forbidden_wafer_materials.exists(m, m in wafer.materials)"
  - id: MP-020  # Step temperature ≤ machine max_temp_c (free-mode params; programs are pre-qualified)
    scope: step
    evaluator: cel
    expr: "!has(step.effective_params.temp_c) || step.effective_params.temp_c <= machine.limits.max_temp_c"
  - id: MP-030  # Gas combination allowed by the machine's limits.gas_combinations (per machine — a tube with a pyrogenic torch burns H2 in O2 by design)
    scope: step
    evaluator: builtin
    check: gas_combinations_allowed
  - id: MP-040  # Duration ≤ machine max continuous run
  - id: MP-045  # Lot fits one run on every candidate machine of every step: ≤ batch.size, ≥ min_fill, == size for fill: exact unless dummy_fill (checked at order time)
  - id: MP-050  # Wafer diameter supported by every pinned/candidate machine
  - id: MP-060  # Pinned machine actually provides the capability/program
  - id: MP-070  # Every external_process is followed by receive_inspect before any tool step
  - id: MP-080  # Every logistics.mask_fab layer exists in layer_map; polarity matches vendor spec
  - id: MP-090  # Coupling window ≥ successor's setup + the predecessor's cleanup (warning)
  - id: MP-100  # Consignment consumables referenced by a step exist in the owner's consignment stock (checked at order time)
```

`step.effective_params` = program params when a program is used, else the step's own params. **CEL convention:** every optional field is guarded with `has()` (as in MP-020); a rule that throws is reported as an `error` finding against the rule itself, never silently passed.

Note what is *not* a global rule: "no resist above 150 °C" or "never mix H2 and O2" would reject the reference processes (polyimide cures at ~350 °C; pyrogenic wet oxidation burns H2 in O2 on purpose). Such limits belong to the machine that has them — `forbidden_wafer_materials`, `gas_combinations`, `max_temp_c` — and MP-011/020/030 merely enforce whatever each machine declares.

**Wafer-state engine.** Rules read `wafer.{contamination_class, materials, resist_present, stack, thickness_um}`. That state is produced by threading declared **effects** through the steps: every program (§5.1) and, for free-mode capabilities, every step type declares its `effects` (`stack_push`, `stack_pop`, `materials_add`, `materials_remove`, `resist: present|removed`, `contamination_class_min`, `thickness_delta_um`, `anneal`). Effects are part of the machine registry and are versioned with it. The same engine state is persisted per physical wafer (§5.5), so incoming-inspection results can overwrite it (a user-shipped wafer arrives with gold on it → it can never enter `clean` tools, regardless of what the recipe claims), and the foundry account may override it with a public, reasoned event.

Validation reports carry `rule, severity, subject, measured, limit, message, hint` per finding; errors block publish; reports are public and permanent. Rules are re-evaluated at dispatch time against the machine revision in force; a failure blocks the step and holds the order.

---

## 9. Designs and design checks (machine protection only)

`POST /designs` stores the GDS/OASIS content-addressed, extracts layer inventory, hierarchy, bbox, polygon count, renders previews, and publishes it. On `POST /orders` (or standalone `POST /designs/{id}/check?recipe=`), two passes run:

**Layer-map conformance (`LM-*`)** — required layers present; unknown layers warned and ignored; bbox within wafer usable area and edge exclusion; unique top cell.

**Machine protection (`MK-*`)** — computed with `gdstk` booleans on the layers the recipe says feed each tool:

| Rule | Protects |
|---|---|
| `MK-001` per-layer pattern density in machine-declared `[min,max]` per window | etch loading, CMP dishing, evaporator source burn-through |
| `MK-002` no geometry in the tool's edge-exclusion ring | handlers, chucks, clamps |
| `MK-003` step-declared layer exclusions and area caps (`exclude: [[RELEASE, XZONE]]`, `RELEASE` area ≤ the laser's `max_release_area_mm2`) | laser release optics/stage; generic, parametrised by the step |
| `MK-004` min trench width vs. DRIE aspect-ratio ceiling | endpoint detection, chamber |
| `MK-005` vertex/polygon count ≤ direct-write ceiling | writer time bound |
| `MK-006` mask-fab: min feature ≥ vendor min for the chosen blank | prevents unfillable mask orders |
| `MK-007` no geometry on layers the recipe never consumes (warning) | catches layer-number mistakes that would waste a mask |

There is **no DRC for yield**. The repo may ship the foundry's *advisory* KLayout deck as a downloadable file for users to run themselves, but the server never gates on it. This is a deliberate liability boundary and is stated on every design page.

---

## 10. Auction and scheduling

### 10.1 Principle

Every machine sells its **time**. Its next run goes to the account whose bid is worth the most per machine-hour above the foundry's own floor, the way a compute spot market sells instance-hours. Bids are money; nothing else reorders the queue. An order-step whose owner won't pay enough simply waits, visibly, forever — while its wafers accrue storage charges.

### 10.2 The unit of sale: a run

A **run** is one order-step's lot executing one program on one machine (on a batch tool, several lots of the *same account* on the same program may share a run, up to `batch.size`). **A run belongs to exactly one account.** Nobody shares a run with a stranger; there is no cross-account batching and no shared pricing. One person is responsible for the lot and the hours.

The machine time a run needs depends on what ran before it:

```
machine_time(run | prev) = setup(prev_program → program)          # setup_matrix, else program.time.setup_s; same program → 0
                         + process(program, lot)                   # time.process_s per run, or × wafers when batch.fill == single
                         + cleanup(program)                        # time.cleanup_s
hours(run | prev)        = machine_time / 3600
```

All three terms come from the program (§5.1) and are authoritative — the foundry qualifies them with the program. Real durations are recorded on the run and feed the utilisation statistics, but never the price.

A bid is `max_credits`: the most the account will pay, in total, for that run. The auction compares bids as an implied **rate** `r = max_credits / hours(run | prev)`. A bidder whose program matches the machine's current program needs no setup, so the same `max_credits` buys a higher rate — bidders who can exploit matching settings win more often at the same money, and bidders who need a changeover pay for it. No bidder ever pays more than `max_credits`.

Lot sizing follows the machine: an order's lot must fit in one run on every candidate machine of every step (`wafers ≤ batch.size`, `≥ min_fill` for `fill: min`, `== size` for `fill: exact` unless the machine offers `dummy_fill`) — validated at order time (`MP-045`). There are no split lots; an order that needs more wafers than the smallest batch on its path is two orders.

### 10.3 Bidders

- **Order-steps** that are `eligible`: predecessors done, assets present, account able to fund `max_credits` (§12). Their bid is the step's `default_bid_credits` unless the owner or a bid policy (§10.8) overrides it.
- **The foundry**, via each machine's `foundry_bid`. Its floor rate for a program is `F = program.rate_credits_per_hour + adjustment` (optionally per program):
  - `reserve` (positive adjustment): "don't run anyone below F". If no candidate reaches F, the machine idles and is shown as `offline_by_bid`. This is how a foundry takes a machine out of service gracefully, or refuses cheap jobs before scheduled maintenance.
  - `subsidy` (negative adjustment; F may go below zero): "I would rather pay than have this tool stop" — furnaces, epi reactors, anything with expensive shutdown/requalification cycles. Bounded by `applies_when: no_competing_bid` (only when the queue would otherwise be empty) and `budget_credits_per_day`.
  - `none` (zero): the foundry breaks even at its bundled rate.

  A foundry bid is public and appears in the queue like any other row.
- **Slot-future holders** (§10.6): a run covered by a future whose window is open pre-empts the auction.

### 10.4 Clearing rule (per machine)

Clearing is **just-in-time**: the next run is decided at `free_at − clear_ahead_s` (immediately, if the machine is idle) — `clear_ahead_s` being the time the foundry needs to stage wafers from storage to the tool. Until that moment bids on the machine compete freely and a late high bidder can still win; at that moment the winner is **locked** (`queued`) and cancelling it forfeits the cleared price (§16). The rule is re-run on every relevant event before the lock (bid changed, step became eligible, machine state changed, future bought).

```
prev = M.current_program (or last program run)
if a slot future on M is exercisable now (holder's step eligible, window open):
    W = the future's run; price = future.strike; lock W; emit auction.cleared {…, via: future}; stop
C = candidate runs: eligible order-steps s with M ∈ machines(s), funded(s), not locked on another machine
for s in C:
    h(s) = hours(run(s) | prev)
    r(s) = max_credits(s) / h(s)
    F(s) = floor rate of M for program(s)          # rate + adjustment; subsidy only if applies_when/budget allow
    surplus(s) = r(s) − F(s)
rank C by surplus desc, ties by eligible_since asc       # nothing else
W = top of C
if C empty or surplus(W) < 0:
    no clearing; M shows offline_by_bid if foundry_bid.mode == reserve else idle
R = highest surplus among C \ W excluding runs owned by W's account (0 if none)
rate(W)  = F(W) + R                                       # the lowest rate that would still have won
price(W) = rate(W) × h(W)                                 # second price with the foundry as a participant; ≤ max_credits(W)
lock W as queued; reserve price(W) against the owner's account
emit auction.cleared {machine, run, program, prev_program, hours, rate, price, floor, runner_up_surplus, losers_snapshot}
```

`price` can be **negative**: if `F(W) = −20 cr/h` and no one else bids, `rate(W) = −20` and the winner is credited `20 × h` for running (§10.5 shows why this is rational for the foundry). Metered consumables are still charged separately, so a user cannot profit by burning gold; the subsidy budget bounds what the foundry can lose.

Bids from the same account never set that account's price (multi-unit Vickrey): an account with two lots queued on one tool simply wins the next two slots; the price of each is set by other accounts' bids or the floor.

### 10.5 Pricing-rule analysis

| Rule | Incentive for bidders | API churn | Foundry control | Verdict |
|---|---|---|---|---|
| **First-price** | Shade bids just above the next competitor; requires watching the queue | High (constant re-bidding) | Reserve only | Simple to explain; poor for headless clients |
| **Second-price (Vickrey) on rate, foundry as participant** | Bid true value once | Low | Reserve *and* subsidy fall out naturally: the foundry's bid is just another bid that sets the floor; setup cost enters through the time model | **Adopted** |
| **Uniform-price batch auction** | Truthful for single units | Low | Same | Not needed: runs are never shared between accounts (§10.2) |
| **Time-window reservations** | Predictability | Low | Blocks the tool at a price the foundry did not set | Replaced by **slot futures** (§10.6), which are reservations *sold* by the foundry at its price |

Why second-price works with a negative foundry bid: the foundry's subsidy is its *true valuation* of keeping the tool running (avoided shutdown and requalification cost per hour). Second-price with the foundry bidding its true value means the tool runs exactly when foundry + users together value running it more than idling — including when the user's valuation is small and the foundry tops it up.

Ranking by surplus (rate above floor) rather than by rate alone matters only when floors differ per program on one machine: it makes the foundry prefer the run that leaves it the most margin per hour, which is what a seller of time wants.

**Manipulation notes.**
- *Shill bids* from the same account never lower a price (they are excluded from setting it) and can only raise the prices others pay if the shill would itself be a real, funded, wafer-in-storage run — i.e. at real cost.
- *Bid-under-the-leader* (the classic second-price attack: bid just below the leader to raise its price without winning) is possible. Its cost is that the griefer must hold a real eligible lot in storage on that machine, and risks winning if the leader withdraws; the foundry's `minimum_increment` and per-key write limits (§16) bound how finely it can be played. Not eliminated, stated.
- A foundry could overstate a subsidy — but it pays it, within its own daily budget.
- Cancelling a `queued` (locked) run forfeits the cleared price (§16); lowering a bid on an *eligible* (not yet locked) step is free.

### 10.6 Coupling windows and slot futures

Some step pairs must follow each other closely (resist coat → expose; HF dip → deposition). A step declares `max_queue_time_from_prev_s`; projections (§10.9) show `must_start_by` for it. **The auction itself has no deadline mechanism**: people set the price they are willing to pay, and the recipe's window is information. If the window is breached, the order-step **fails** and the order goes to `held` with reason `coupling_breach` (§10.7); the owner picks continue-anyway / rework-to-step / abort and pays for rework steps at auction like any other steps. There is no free rework. If the breach was caused by the machine (`down` during the window), the hold records cause `machine_fault` with evidence, so it is insurable (§12.3).

The way to *guarantee* a coupled successor is to buy its slot in advance. A **slot future** is a contract:

```yaml
id: fut_01J8…
provider: prov_foundry                 # the foundry sells pre-emptive futures; external providers sell price caps (below)
holder: acct_9f3e
run: {order: ord_01J8…, step: BOX, machine: mach_furnace-A, program: dry_ox_900_20nm, wafers: 8}
window: {not_before: 2026-09-12T15:00:00Z, not_after: 2026-09-12T21:00:00Z}
strike_credits: 380                    # what the run costs if exercised, regardless of the auction
premium_credits: 45                    # paid now, non-refundable unless the provider fails to deliver
terms_url: https://…
```

- **Exercise.** When the holder's order-step becomes `eligible` inside the window, the machine's next clearing is that run at `strike_credits`; it pre-empts the auction. The queue shows the future as a row (`future · window · strike`) so other bidders can see that the next slot is spoken for.
- **Expiry.** If the step is not eligible at any clearing inside the window (predecessor late, unfunded), the future lapses; the premium is kept by the provider.
- **Provider failure.** If the machine cannot deliver inside the window (down, maintenance, or the foundry oversold), the provider refunds premium and pays the coverage in its terms (typically the rework of the predecessor). Filed automatically like an insurance claim.
- **Pricing.** The foundry (built-in provider) quotes from the market-rate percentiles for the program, the current queue and its own schedule (e.g. `p90 rate × hours + margin`), and limits futures per machine (`futures_capacity`, e.g. at most 30 % of the next 24 h) so the spot market is not hollowed out. External providers cannot pre-empt a machine they don't own; through the same provider interface (§12.3) they sell **price caps**: the provider bids without limit on the holder's behalf inside the window and pays the difference between the cleared price and the strike.

Futures resolve the earlier open question about time-window reservations: reservations exist, but only as something the foundry *sells* at its own price, so they are just another bidder in the same public book.

### 10.7 Halts and the `held` state

Any of these put an order in `held`: an `analysis.*` step's `on_fail: hold`, a coupling breach, a run outcome `fail`, an incoming inspection failure, a dispatch-time revalidation failure, or an account that cannot fund the next step (`unfunded` for longer than `foundry.unfunded_hold_after_s`). While held:

- the order's `eligible` steps are withdrawn from every auction (shown as `blocked · order_held`) and return to `eligible` on `continue`;
- wafers/masks sit in storage at their class rate (charged to the owner);
- the owner resolves via `POST /orders/{id}/holds/{hold_id}/resolve` with `{action: continue | rework_to_step, step_id | abort, note}`;
- `foundry.hold_timeout_s` (e.g. 14 days) auto-aborts; assets then keep charging until shipped (`ship_out` can be ordered standalone) or, after `foundry.abandon_after_s`, are disposed and the account is closed out. Disposal of user-shipped assets is a contractual right the account accepts on registration (`foundry.terms_url`), and every step of the path is a public event with notice periods.

All hold events, decisions and notes are public.

### 10.8 Bid policies (server-side, optional)

`none` (default), `deadline` (raise the critical-path step's `max_credits` to `price_to_lead` when projected completion slips past target, within a budget; optionally buy the foundry's future when `price_to_lead` exceeds the future's strike + premium), `budget` (spread a budget across remaining machine-hours). Policies place ordinary bids, emitting `order_step.bid_changed {placed_by: policy:…}`.

### 10.9 Projections

For every order-step: expected start (given current bids, futures and program time models), `price_to_lead` per candidate machine (the `max_credits` that would currently rank first, computed from the runner-up's surplus and this run's hours), the foundry's current future quote for the step, and `must_start_by` from coupling windows. Recomputed on every clearing, streamed via SSE.

### 10.10 Worked example (furnace with subsidy)

Furnace A has just finished `bake_10h`. Rates: `dry_ox_900_20nm` 130 cr/h, `bake_10h` 150 cr/h. Foundry bid: subsidy, adjustment −150 cr/h on `dry_ox` (F = −20), 0 on `bake_10h` (F = 150). Setup `bake_10h → dry_ox` = 3600 s. Candidates at the clearing moment:

| Run | Program | Wafers | `max_credits` | hours (incl. setup) | rate | floor | surplus |
|---|---|---|---|---|---|---|---|
| ord_M · BOX | dry_ox | 8 | 300 | 1.0 + 2.5 = 3.5 | 85.7 | −20 | **105.7** |
| ord_P · BOX | dry_ox | 6 | 200 | 3.5 | 57.1 | −20 | 77.1 |
| ord_S · ANNEAL | bake_10h | 2 | 600 | 0 + 11.0 = 11.0 | 54.5 | 150 | −95.5 (below floor) |

- Winner: ord_M. Runner-up surplus (ord_P) = 77.1 → `rate = −20 + 77.1 = 57.1 cr/h`, `price = 57.1 × 3.5 = 200 cr` — exactly ord_P's bid, as second price should be. ord_M's owner bid 300 and pays 200.
- Had ord_P not existed: `rate = F = −20`, `price = −70 cr` → ord_M's owner is *credited* 70 cr; the foundry pays 70 cr (from its subsidy budget) rather than let the tube cool.
- Had the previous program been `dry_ox` (no setup): ord_M needs 2.5 h, rate 120 cr/h — the same 300 cr bid ranks higher. This is the "my settings match the last run" advantage; the owner could also have bid *less* and still won.
- Had the foundry set `reserve +100` on `dry_ox` (F = 230): no candidate reaches the floor; the tube shows `offline_by_bid` with the queue and the 230 cr/h floor visible to all.
- ord_S never clears here (54.5 < 150). Its owner can raise `max_credits` to 1,650, wait for the subsidy budget to be exhausted (then `dry_ox` bidders compete at F = 130), or buy a future.

### 10.11 Determinism

`scheduler.decide(state, event, clock) -> [Decision]` is pure; the demo event log replays to byte-identical `auction.cleared` events. Everything non-deterministic — adapter outcomes, callback verdicts and latencies, future quotes from external providers, operator inputs — enters the system only as recorded events, so replay never calls out.

---

## 11. Machines, programs, consumables, storage, utilisation

### 11.1 Consumable charging modes

| Mode | Where the cost lives | Example | Charged how |
|---|---|---|---|
| **bundled** | inside a program's (or free-mode capability's) `rate_credits_per_hour` | furnace O2/N2, quartz wear, RIE SF6 at nominal flow, electricity, chamber hours | Part of the foundry's floor; no separate line item. The foundry sets the rate from historical draw. |
| **metered** | pass-through at actual draw × unit cost | evaporated Au/Pt (grams, wafer-dependent), mask blanks, substrate wafers, custom targets | Separate ledger line at run end (`consumable.metered`); *estimated* at validation for the projection. |
| **consignment** | customer-owned stock held at the foundry | customer's own 4-inch SOI wafers, their proprietary resist, their sputter target | No unit charge; stock decremented from `CONSIGNMENT_STOCK(account, consumable)`; storage charged by class; step validation fails at order time if stock is insufficient (`MP-100`). |

Each consumable in a machine's rate table declares `mode` and, for metered ones, a *draw function* (`draw = f(program|params, wafer_count)`) implemented per capability in code and unit-tested — no expression language needed. A program's bundled rate is what makes `foundry_bid.mode: none` well-defined: `F = rate_credits_per_hour`, the foundry's break-even rate for that program.

*Open exploration (§18 Q3):* whether consignment stock should also be biddable/sellable between accounts, and whether bundled rates should be re-derived automatically from metered history.

### 11.2 Storage

```yaml
storage_locations:
  - {id: stor_shelf-1,  class: ambient_shelf, capacity: {wafer_carriers: 40, mask_boxes: 60}}
  - {id: stor_n2cab-3,  class: n2_cabinet,    capacity: {wafer_carriers: 12}}
  - {id: stor_maskvault, class: mask_vault,   capacity: {mask_boxes: 200}}
storage_rates:
  - {class: ambient_shelf, unit: wafer, credits_per_day: 0.10}
  - {class: n2_cabinet,    unit: wafer, credits_per_day: 0.60}
  - {class: mask_vault,    unit: mask,  credits_per_day: 0.25}
  - {class: mask_box,      unit: mask,  credits_per_day: 0.05}
```

Storage accrues per asset per hour (billed daily to the ledger as `storage.wafer` / `storage.mask`) from arrival until the asset is on a tool, in transit, shipped or disposed. A wafer *between steps* is in storage. This is the mechanism that makes "blocked because unwilling to pay" self-limiting: waiting is not free. Recipes can move assets to a cheaper class with `logistics.store`. Storage occupancy and rates are public.

### 11.3 Utilisation and market data

Hourly buckets of `running/setup/idle/offline_by_bid/maintenance/down`, wafers, runs, credits cleared (may be negative), per machine and per capability; plus per-program clearing *rate* percentiles in credits per machine-hour ("market rate") and the foundry's current future offer price. Derived from events, rebuildable.

---

## 12. Accounts, ledger, insurance

### 12.1 Accounts and enforcement modes

Credits are abstract. Every account has a `funding` mode, demonstrated in the prototype:

| Mode | Rule | Effect on bidding |
|---|---|---|
| `prepaid` | `balance ≥ 0` always | a bid counts only if `balance − reserved_for_queued − projected_storage_7d ≥ max_credits`; otherwise `eligible.unfunded` |
| `postpaid` | `balance ≥ −credit_limit` | same check against `credit_limit` instead of 0 |
| `unlimited` | demo bots and the foundry account | never unfunded |

Reaching the limit while a lot is mid-flow → `held (unfunded)` → timeout → abort → storage keeps accruing → disposal after `abandon_after_s`. Every step of that path is an event.

### 12.2 Ledger

Append-only entries `(seq, ts, account, counter_account, kind, amount, refs)`. Kinds: `run.cleared` (the run's price — negative or positive — posted at `run.started`, reserved from `auction.cleared`), `consumable.metered`, `storage.wafer`, `storage.mask`, `mask_fab`, `shipping`, `insurance.premium`, `insurance.claim`, `future.premium`, `future.strike` (replaces `run.cleared` for an exercised future), `future.claim` (provider failed to deliver), `subsidy` (foundry's side of a negative price), `forfeit` (cancelled queued run), `deposit`, `adjustment`. The foundry is an account, so its books balance against users'. Everything is public (`GET /accounts/{id}/ledger`).

### 12.3 Providers: insurance and slot futures (pluggable; foundry and external providers look identical)

```yaml
provider:
  id: prov_foundry              # built-in; or prov_acme for external
  products: [insurance, future, price_cap]   # external providers: insurance and price_cap only (§10.6)
  quote_url: https://…/quote    # POST {product, order, steps | run, machine stats, market rates} → {premium, strike?, coverage, terms_url}
  claim_url: https://…/claim    # POST {run, outcome, cause, cause_evidence, assets, ledger refs} → {decision, payout}
  webhook_signing_key: …
```

- At order submit (or later per step), `POST /orders/{id}/insurance {provider, steps: [...] | all}` obtains a quote; accepting it writes `insurance.premium` and a `policy` record on the order.
- A run outcome `fail` on a covered step automatically files a claim; the provider's decision writes `insurance.claim` and, if the policy says so, refunds the charged machine time and funds a rework at the provider's expense.
- **Cause is evidence-backed.** The adapter classifies every failure as `machine_fault | recipe | wafer | unknown` *and* must cite `cause_evidence`: telemetry channels and time ranges, log line ranges, or inspection assets — all public run assets (§14). The foundry classifies faults on its own machines, so the evidence is what lets an external provider (or the public) audit the classification; a claim decision that disagrees with the adapter's cause is itself a public event.
- The built-in provider prices premiums from the machine's historical fault rate and covers `machine_fault` only; an external provider can cover anything. The foundry can also buy insurance for its own subsidy exposure or machine damage through the same interface.
- **Default with no policy: machine time is always charged, whatever the outcome — including `machine_fault`.** Metered consumables actually drawn are charged too. Insurance is the only way to move that risk; it can cover the charged time, the wafers, and the rework. This is deliberate: the foundry sells time, and the price of reliability is quoted separately and publicly by whoever is willing to underwrite it.
- **Slot futures** use the same provider record with `product: future` (foundry only, pre-emptive) or `price_cap` (any provider). Quotes, exercise, expiry and provider-failure claims are described in §10.6.

---

## 13. Expression language analysis

Needed in three places: machine-protection rules (foundry-authored), analysis/halt conditions (user-authored) and, optionally, bid policies. Requirements: sandboxed, deterministic, embeddable in YAML/JSON, readable in the GUI, not invented here.

| Option | Sandboxing | Expressiveness | Readability in GUI | Ecosystem | Fit for foundry rules | Fit for user analysis |
|---|---|---|---|---|---|---|
| **Declarative checks** (`stat/field/min/max` JSON, §5.3) | Total (no code) | Low — thresholds, groupings | Excellent | n/a | Covers ~60 % of rules (limits) | Covers the common e-test case |
| **Callback / webhook** (server POSTs inputs, expects `{pass, findings}`) | User's problem; server only sees a verdict | Unlimited | Only the verdict is visible | Any language | Poor for foundry rules (must be public & auditable) | **Best**: users run whatever they like, on their infrastructure |
| **CEL** | Strong: non-Turing-complete, bounded cost, typed | Medium — boolean/arith over structured data, list macros | Good (one-liners) | Google, `cel-python`, `cel-go` (both languages we might use) | **Good**: rules like MP-011 are one line, evaluated identically in the GUI | Fine for simple checks |
| **JSONLogic** | Strong | Low–medium; awkward for aggregations | Poor (nested JSON) | Many ports | Adequate | Adequate |
| **Rego / OPA** | Strong | High | Medium; needs OPA sidecar | Policy-focused | Good but heavy | Overkill |
| **Sandboxed Python** (RestrictedPython / subprocess + seccomp) | Weak-to-medium; endless escape surface | Unlimited | Good | Everything | Risky on a public server | Risky; users get this via callbacks anyway |
| **Starlark / Lua** | Medium (deterministic, resource-limited) | High | Good | Bazel/Buck ecosystem | Reasonable but another runtime | Reasonable |

**Recommendation:**
1. **Declarative checks first.** Most limits and e-test thresholds need no language. The schema stays JSON.
2. **Callbacks for everything user-defined.** `analysis.callback` and (optionally) bid-policy callbacks. The user's code is theirs; the foundry records inputs, verdict, and latency. Signed requests, timeouts, retries, and a public "callback failed → held" path.
3. **CEL as the single inline expression language** for foundry rules that aren't structural, chosen because it is sandboxed by construction, has both Python and Go implementations (protecting the Go-port option), and renders as a readable one-liner in the rules page. `analysis.expr` exposes the same evaluator to users for small checks. Rego and Python are rejected for a public server; JSONLogic for readability.

The rule and step schemas carry an `evaluator` field so this decision is reversible without changing documents.

---

## 14. Run assets

Every run produces assets into the object store, listed on `GET /runs/{id}/assets` and downloadable by anyone:

| Asset | Format | Producer |
|---|---|---|
| `telemetry` | NDJSON (`ts, channel, value, unit`) | adapter/simulator |
| `summary` | JSON (`actual_duration_s, program, params_effective, outcome, cause, consumable_draw[]`) | dispatcher |
| `log` | text | adapter |
| metrology outputs | CSV/Parquet with declared schema id, plus JSON raw | metrology programs |
| images | PNG/JPEG (`optical`, `sem`, wafer maps rendered by the server) | metrology programs, server |
| `analysis report` | JSON (`checks[], pass, findings[]`) | analysis worker |
| `inspection` | JSON | incoming inspection |

For many customers the run assets — particularly probe/e-test tables and wafer maps — *are* the deliverable, and a recipe may end with `metrology.probe` and `logistics.store` (or disposal) instead of `ship_out` (§1). Schemas for structured outputs live in `schemas/assets/`; producers declare which schema they emit so callbacks and the GUI can rely on them. Nothing is deleted; large binaries may be tiered to cold storage after N days.

---

## 15. Public API

Conventions: `/v1`, JSON, OpenAPI 3.1, ULIDs, cursor pagination, `Idempotency-Key`, unauthenticated reads, API-key writes, RFC 9457 problem+json errors. Reads: foundry, machines, auctions, runs, utilisation, consumables, capabilities, step types, templates/recipes, designs, orders, order-steps, events (+SSE), rulesets, validation reports. Writes: recipe drafts/validate/publish/fork, design upload/check, orders/cancel, bids (per-step and bulk + policy), webhooks. Demo-only: `/sim/advance`, `/sim/reset`. Additional endpoints:

| Method & path | Auth | Purpose |
|---|---|---|
| `GET /machines/{id}/programs` | – | Locked configurations, durations, bundled rates, metered consumables |
| `GET /machines/{id}/auction` | – | Queue incl. the foundry bid row, unfunded rows, batch formation state |
| `PUT /machines/{id}/foundry-bid` | foundry | Set reserve/subsidy (public event) |
| `GET /assets` · `GET /assets/{id}` · `GET /accounts/{id}/assets` | – | Physical assets, locations, storage charges to date |
| `POST /shipments` · `GET /shipments/{id}` | key | Standalone inbound/outbound shipping; inbound creates `awaiting_inspection` assets |
| `POST /orders` | key | Includes `assets: {wafers: {source, count | asset_ids}, masks: {source, asset_ids | mask_fab}}` and `insurance` |
| `GET /orders/{id}/holds` · `POST /orders/{id}/holds/{hid}/resolve` | key+owner | Held-order decisions |
| `GET /runs/{id}/assets` · `GET /assets/{id}/content` | – | Run outputs |
| `GET /accounts/{id}` · `GET /accounts/{id}/ledger` | – | Balance, mode, limit, entries |
| `POST /accounts/{id}/deposit` | demo/admin | Prepaid top-up (demo) |
| `GET /insurance/providers` · `POST /orders/{id}/insurance` · `GET /orders/{id}/insurance` | key | Quotes, policies, claims |
| `GET /consignment/{account}` | – | Consignment stock |
| `GET /storage` · `GET /storage/rates` | – | Occupancy, rates |
| `GET /vendors` | – | Mask-fab and external-process vendors, lead times, prices |
| `POST /callbacks/test` | key | Dry-run a callback endpoint with a sample payload |


---

## 16. Openness, abuse, safety

| Risk | Mitigation |
|---|---|
| Bid churn / spam | Per-key write limits; `minimum_increment` on `max_credits`; unfunded bids never clear |
| Bid-under-the-leader (raise a rival's second price without winning) | Not eliminated (§10.5). Costs the griefer a real, funded lot in storage on that machine plus the risk of winning; bounded by `minimum_increment` and write limits; every bid change is public and attributable |
| Bid-and-cancel griefing | Cancelling a `queued` step writes `forfeit` of the cleared price; lowering a queued bid below its cleared price is rejected |
| Exploiting negative prices (subsidy farming: repeat cheap runs to collect the subsidy) | Metered consumables are always charged; a subsidy applies only when the tool would otherwise idle (`applies_when`), is capped by `budget_credits_per_day`, and is the foundry's explicit choice |
| Futures hoarding | `futures_capacity` per machine; premium is forfeited on expiry; futures are non-transferable |
| Unfunded lots occupying storage | Storage always charges; timeout → abort → disposal path is automatic and public |
| Callback abuse (slow/evil endpoints) | Timeouts, size caps, signed requests, outbound allow-list per foundry, failure → `held`, never retried indefinitely |
| Malicious GDS | Size/hierarchy/polygon caps; checker in a sandboxed subprocess with CPU/mem/time limits |
| Rule bypass | Rules re-evaluated at dispatch against machine revision in force; fail-safe to `held` |
| IP | All designs public by declaration; takedown route; sha256 dedupe |
| PII | Only public key ids and optional display names; email addresses are never published in any form (a hash is reversible for any known address); webhook/callback URLs redacted to hostname in public views |

---

## 17. Read-only GUI

Static single-page app, `GET` + SSE only; no login, no API key, nothing that writes. Every page links to the JSON that produced it. Live updates via the event stream. Money is always shown with its basis ("9.0 bid · paid 3.0 · foundry bid −6.0").

Site map: `/` overview · `/machines/:id` · `/auctions` · `/orders` · `/orders/:id` · `/holds` · `/recipes` · `/recipes/:id@v` · `/designs/:id` · `/runs/:id` · `/assets/:id` · `/storage` · `/accounts/:id` · `/vendors` · `/insurance` · `/rules` · `/reports/:id` · `/events`.

**Foundry overview `/`** — the foundry bid and unfunded/held counts are first-class:

```
┌───────────────────────────────────────────────────────────────────────────────────────────────┐
│ foundry.api · Demo Foundry               clock 2026-09-12 14:02 UTC (sim ×60)   ● live  {json} │
│ [Overview] [Auctions] [Orders] [Holds] [Recipes] [Designs] [Storage] [Accounts] [Rules] [Events]│
├───────────────────────────────────────────────────────────────────────────────────────────────┤
│ Machines 15: running 8 · setup 1 · idle 2 · offline-by-bid 2 · maint 1 · down 1               │
│ Orders: in_progress 19 · held 4 · awaiting_assets 6 · unfunded steps 7   Wafers in fab 88     │
│ Cleared 24h: +1,842 cr (subsidies paid −96 cr)   Storage billed 24h: 41 cr   Claims 24h: 1    │
├──────────────────────────────┬──────────────────────────────────┬──────────────┬───────────────┤
│ MACHINE            STATE     │ NOW                              │ FOUNDRY BID  │ TOP BID       │
├──────────────────────────────┼──────────────────────────────────┼──────────────┼───────────────┤
│ ● Evaporator #1    running   │ ord_C s04 6w ▓▓▓▓▓░░░ 62% →15:30 │ none (18.5)  │ ord_B 30.0    │
│ ● Furnace tube A   running   │ dry_ox 14w batch ▓▓▓░░░░ →17:00  │ −6.0 subsidy │ ord_M 9.0     │
│ ◌ RIE #1        offline-by-bid│ –  (reserve 40 > top bid 14.2)  │ +40 reserve  │ ord_A 14.2    │
│ ◌ DRIE          offline-by-bid│ –  (maint. 18:00; reserve 999)  │ +999 reserve │ ord_T 40.0    │
│ ● Contact aligner  running   │ ord_A s03 4w ▓░░░░░░░ 10% →14:35 │ none (9.5)   │ ord_N 11.0    │
│ ○ Spin coater #2   idle      │ –  (top bid 6.5 < floor 7.2)     │ none (7.2)   │ ord_Q 6.5 ⚠   │
│ ● Operator         running   │ ord_H IN_INSPECT 25w →14:20      │ none (45/h)  │ ord_V 12.0    │
│ …                            │                                  │              │               │
├──────────────────────────────┴──────────────────────────────────┴──────────────┴───────────────┤
│ HELD (4)  ord_H coupling_breach 2d · ord_J analysis BOX_check 6h · ord_L unfunded 1d · ord_W …│
│ RECENT  14:02 auction.cleared Furnace A batch 14w @ 3.0 (outside 3.0, F −6.0)                  │
│         14:01 hold.opened ord_J BOX_check thk_mean 22.1 nm > 21.5                              │
│         13:59 ledger  acct_9f3e  storage.wafer −2.40  (4 wafers · n2_cabinet · 1 day)           │
└───────────────────────────────────────────────────────────────────────────────────────────────┘
```

**Machine detail `/machines/mach_furnace-A`** — programs and batch formation visible:

```
┌───────────────────────────────────────────────────────────────────────────────────────────────┐
│ ← Machines   Furnace tube A   thermal.furnace   class clean   batch 25 (min 5)   ● running     │
├───────────────────────────────────────────────────────────────────────────────────────────────┤
│ PROGRAMS (programs_only)                                                                        │
│  dry_ox_900_20nm   900 °C dry O2 45 min   3.0 h/run   bundled 400 cr/run (16.0/w @25)   market p50 5.5/w │
│  bake_10h          1000 °C N2 600 min    12.0 h/run   bundled 1800 cr/run (72/w @25)   market p50 61/w  │
│ FOUNDRY BID  subsidy −6.0 cr/w  "tube must stay hot; cool-down + requal ≈ 12 h"  set 09-10 by foundry │
│ LIMITS  ≤1150 °C · forbidden on wafer: Au Cu Al resist polyimide · 150 mm only                 │
├──────────────────────────────────────┬────────────────────────────────────────────────────────┤
│ NOW  run_01J8…  dry_ox_900_20nm      │ NEXT SLOT — batch forming for dry_ox_900_20nm           │
│ batch 14w: ord_G 6, ord_H 5, ord_J 3 │ #  order  step  w   bid    funded  same prog            │
│ started 14:02 → 17:00                │ 1  ord_M  BOX   8   9.0    ✓       ✓  ┐                 │
│ price 3.0/w (outside bid 3.0)        │ 2  ord_P  BOX   6   4.0    ✓       ✓  │ batch 19w        │
│ tube 900.2 °C  O2 4.0 slm            │ 3  ord_R  BOX   5   1.0    ✓       ✓  ┘ price ≈ max(−6, 0.5)=0.5 │
│ telemetry ▸  assets ▸                │ 4  ord_S  RTA…  2   0.5    ✓       ✗ (bake_10h)          │
│                                      │ –  ord_U  BOX   4   12.0   ✗ unfunded (prepaid 30 cr)    │
│                                      │ waits until 16:00 for min_fill? no — 19 ≥ 5, runs at idle │
├──────────────────────────────────────┴────────────────────────────────────────────────────────┤
│ UTILISATION 7d  running 82% · setup 4% · idle 3% · offline-by-bid 0% · maint 11%               │
│ Cleared 7d +2,110 cr · subsidies paid −312 cr · wafers 611 · runs 26 · faults 1 (claim paid)   │
└───────────────────────────────────────────────────────────────────────────────────────────────┘
```

**Order detail `/orders/ord_J` (held)**:

```
┌───────────────────────────────────────────────────────────────────────────────────────────────┐
│ ← Orders  ord_01J8J  "sky130-fe test lot"  owner acct_9f3e (prepaid, bal 412 cr)   ⏸ HELD      │
│ recipe sky130-fe@2 · design des_… · lot lot_… 6 wafers (foundry_supplied) · masks: direct-write │
│ insurance: prov_foundry, machine_fault, steps all, premium 18 cr                                │
├───────────────────────────────────────────────────────────────────────────────────────────────┤
│ HOLD hold_01J8…  opened 14:01  reason analysis_fail  step BOX_check                            │
│   thk_mean = 22.1 nm  (limit 18.5–21.5)   report ▸   wafer map ▸                                │
│   storage accruing: 6w × n2_cabinet 0.60/day = 3.60 cr/day   auto-abort in 13d 22h              │
│   owner options via API: continue · rework_to_step (BOX, SMAT) · abort          {json}          │
├────┬───────────────────┬──────────┬──────────────┬─────────────────────────────┬───────────────┤
│ #  │ step              │ status   │ bid / paid   │ machine · time              │ assets        │
├────┼───────────────────┼──────────┼──────────────┼─────────────────────────────┼───────────────┤
│ 1  │ SMAT (manual)     │ done     │ 5 / 5        │ Operator · 09-11 20:10 (10m)│ note          │
│ 2  │ BOX (dry_ox)      │ done     │ 9 / 3.0      │ Furnace A · 09-11 22:00 3h  │ telemetry, log│
│ 3  │ BOX_thk           │ done     │ 4 / 2.5      │ Ellipsometer · 09-12 13:40  │ thickness_map ▸ wafer map ▸│
│ 4  │ BOX_check         │ FAILED   │ –            │ analysis · 14:01            │ report ▸      │
│ 5  │ ISONIT (lpcvd)    │ blocked  │ 12           │ LPCVD B · est –             │               │
│ …  │                   │          │              │                             │               │
│ 41 │ SHIP (ship_out)   │ blocked  │ 0            │ Shipping · –                │               │
├────┴───────────────────┴──────────┴──────────────┴─────────────────────────────┴───────────────┤
│ LEDGER (this order)  bids −78.5 · consumables (metered) −0 · storage −4.80 · mask_fab 0 · ins −18 │
└───────────────────────────────────────────────────────────────────────────────────────────────┘
```

**Storage `/storage`**:

```
┌───────────────────────────────────────────────────────────────────────────────────────────────┐
│ Storage   occupancy & rates   billed 24h: 41.2 cr                                             │
├──────────────────┬──────────────┬───────────┬──────────────────────────────────────────────────┤
│ location         │ class        │ occupancy │ contents (owner · lot · since · charge to date)  │
├──────────────────┼──────────────┼───────────┼──────────────────────────────────────────────────┤
│ stor_n2cab-3     │ n2_cabinet   │ 9/12      │ acct_9f3e lot_J 6w 1d 3.60 · acct_4a lot_B 2w …  │
│ stor_shelf-1     │ ambient_shelf│ 31/40     │ acct_c1 lot_L (unfunded, held 1d) 25w 4d 10.0 ⚠  │
│ stor_maskvault   │ mask_vault   │ 118/200   │ acct_9f3e METAL1 rev C 38d 9.50 · …              │
│ external         │ –            │ 12 wafers │ acct_7b lot_X @ aldhouse, due back 09-18 ▸       │
│ in_transit       │ –            │ 3 masks   │ maskco → foundry, ETA 09-14 ▸                    │
└──────────────────┴──────────────┴───────────┴──────────────────────────────────────────────────┘
```

**Account `/accounts/acct_9f3e`** — mode, balance, credit limit, reserved-for-queued, projected storage, assets, orders, full ledger with running balance and links to runs/holds/policies.

**Run `/runs/run_01J8…`** — program/params effective, batch members, telemetry chart, consumable draw (bundled vs metered), outcome + cause, claim status, asset list with previews (wafer maps rendered server-side from CSV).

**Recipe viewer** — step list with type, capability, pinned machines per step, program badges, metrology outputs and checks inline, logistics steps drawn as a timeline with vendor lead times, and the per-step wafer-state strip.

---

## 18. Open questions

1. **Time-window reservations** — still deferred. Emulate with `not_before` + high bid, or add real reservations later?
2. **Foundry bid granularity** — per machine vs. per program (a furnace may want a subsidy for `dry_ox` but a reserve for `bake_10h`). Leaning per-program with a machine default.
3. **Consumables** — should consignment stock be transferable/sellable between accounts? Should bundled rates auto-update from metered history? Should metered draws be *bid-able* (a cap on consumable spend per step)?
4. **Batch pricing** — uniform price per batch vs. each member pays own second price. Uniform is simpler and fairer inside a batch; confirm.
5. **Held timeouts** — 14-day hold timeout and abandon-after are foundry constants; should recipes shorten them?
6. **Callback identity** — should callbacks be allowed to *set bids* (a user's own scheduler)? Powerful, but it turns callbacks into a bidding-bot API. Probably yes with a separate scope on the API key.
7. **Wafer-state truth** — when incoming inspection disagrees with the recipe's assumed state, inspection wins. Is manual override by the foundry account needed?
8. **Split lots** — child lots are tracked; do they get their own bids, or inherit the parent's?
9. **Insurance claim disputes** — provider decision is final; do we need a public dispute record?
10. **Data-only orders** — for "silicon as a cloud service", should a recipe be allowed to end without `ship_out` or `store`, with wafers disposed after probe data is published? What is the retention/disposal policy and price?
11. **Go boundary** — CEL exists in both languages; the design checker (`gdstk`/KLayout) and analysis worker stay Python regardless.

---

## 19. Milestones

| M | Deliverable |
|---|---|
| M0 | JSON Schemas (recipe, step types, machine, program, ruleset, order, assets, ledger), demo foundry, TFE template, OpenAPI skeleton |
| M1 | Recipes + rule engine (builtin + CEL) + wafer-state + reports; `foundry-api validate` CLI |
| M2 | Designs: upload, inventory, LM/MK checks in sandbox |
| M3 | Accounts/ledger (prepaid, postpaid), physical assets, storage charging, shipments, incoming inspection |
| M4 | Orders, lots, order-steps, holds, event log, SSE, webhooks |
| M5 | Auction with foundry bid, negative prices, batches, projections; simulator; replay tests |
| M6 | Run assets, metrology programs, `analysis.check` + `analysis.callback`, halt → held |
| M7 | Insurance provider interface + built-in provider + claims |
| M8 | GUI (all pages), SKY130 excerpt template, public demo, docs |

## Appendix A — Demo foundry machines

Spin coaters ×2, convection oven, contact aligner, maskless writer, evaporators ×2, RIE ×2, DRIE, wet bench (Au), wet bench (clean), furnace tube A, RTA, laser release, profilometer, ellipsometer, prober, operator and shipping pseudo-machines. Furnace A and RTA `programs_only` with subsidies; RIE #1 carrying a reserve during the demo to show `offline_by_bid`; vendors `maskco` (5-inch Cr masks, 5-day lead, 1,200 cr/layer) and `aldhouse` (external ALD, 7-day turnaround).
