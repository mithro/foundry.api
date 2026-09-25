#!/usr/bin/env python3
"""The distribution of software margins, by SIC code, from SEC XBRL frames.

Builds one record per filer per calendar-aligned fiscal year from the frames
fetched by fetch_sec.py, joins the SIC code from the submissions API, and prints
n / min / p10 / p25 / median / p75 / p90 / max for each metric in each SIC group.

The join that matters: a duration frame (CY2025) carries the filer's own fiscal
year end, which for software is often 31 January or 30 June.  Balance-sheet
items are therefore taken from whichever instantaneous frame (CY2025Q1I ...
CY2026Q2I) holds a fact at exactly that end date, not from CY2025Q4I blindly.

No mean is reported anywhere.  These distributions have tails that make a mean
meaningless - one filer with $40k of revenue and a $2m loss is a -5,000% margin.

Usage:
  uv run python tools/sec_margins/sic_distribution.py            # the tables
  uv run python tools/sec_margins/sic_distribution.py --rule40   # growth vs margin
  uv run python tools/sec_margins/sic_distribution.py --dupont   # the ROA arithmetic
"""
from __future__ import annotations

import argparse
import gzip
import json
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from fetch_sec import CACHE  # noqa: E402

# Revenue element preference.  Revenues is the total-revenue element; filers that
# do not use it almost always use the ASC 606 element instead.
REV_TAGS = [
    "Revenues",
    "RevenueFromContractWithCustomerExcludingAssessedTax",
    "RevenueFromContractWithCustomerIncludingAssessedTax",
]
INSTANT_TAGS = [
    "Assets",
    "StockholdersEquity",
    "PropertyPlantAndEquipmentNet",
    "CashAndCashEquivalentsAtCarryingValue",
    "Goodwill",
]
INSTANT_PERIODS = [f"CY{y}Q{q}I" for y in (2022, 2023, 2024, 2025, 2026) for q in (1, 2, 3, 4)]

# The SIC groups the write-up reports.  "Software and computer services" is the
# union that the question is really about.
# Labels are the SEC's own sicDescription strings, from the submissions API.
GROUPS: dict[str, list[str]] = {
    "7372 Services-Prepackaged Software": ["7372"],
    "7370 Services-Computer Programming, Data Processing, Etc.": ["7370"],
    "7371 Services-Computer Programming Services": ["7371"],
    "7373 Services-Computer Integrated Systems Design": ["7373"],
    "7374 Services-Computer Processing & Data Preparation": ["7374"],
    "7375 Services-Computer Facilities Management": ["7375"],
    "7377 Services-Computer Rental & Leasing": ["7377"],
    "7379 Services-Computer Related Services, NEC": ["7379"],
    "7389 Services-Business Services, NEC (catch-all)": ["7389"],
    "ALL software & computer services (737x)": [
        "7370", "7371", "7372", "7373", "7374", "7375", "7377", "7379",
    ],
    "3674 Semiconductors & Related Devices": ["3674"],
    "3559 Special Industry Machinery, NEC": ["3559"],
    "ALL filers with the tags": ["*"],
}

# Size bands within SIC 7372.  "The median listed software company" is a
# micro-cap, and Silex's SEK 1,385m of 2025 net sales is roughly US$145m at the
# 2025 average rate, so the $100m-$1bn band is its size peer group.
SIZE_BANDS = [
    ("7372, revenue < $100m", 0, 100e6),
    ("7372, revenue $100m-$1bn", 100e6, 1e9),
    ("7372, revenue > $1bn", 1e9, float("inf")),
]

METRICS = [
    ("operating_margin", "Operating margin = OperatingIncomeLoss / Revenues"),
    ("asset_turnover", "Asset turnover = Revenues / Assets"),
    ("roa", "Return on assets = OperatingIncomeLoss / Assets"),
    ("op_asset_turnover", "Revenues / (Assets - cash - goodwill)"),
    ("op_roa", "OperatingIncomeLoss / (Assets - cash - goodwill)"),
    ("gross_margin", "Gross margin = GrossProfit / Revenues"),
    ("rnd_pct", "R&D / Revenues"),
    ("sgna_pct", "SG&A / Revenues"),
    ("sbc_pct", "Share-based compensation / Revenues"),
    ("capex_intensity", "Capex / Revenues"),
    ("ppe_intensity", "PP&E net / Revenues"),
    ("cfo_margin", "Operating cash flow / Revenues"),
]

MIN_REVENUE = 1_000_000  # below this, ratios are noise from shells and startups


def frame(tag: str, period: str) -> list[dict]:
    p = CACHE / "frames" / f"{tag}_{period}.json.gz"
    if not p.exists():
        return []
    return json.loads(gzip.decompress(p.read_bytes()))["data"]


def duration_map(tag: str, period: str) -> dict[int, dict]:
    return {r["cik"]: r for r in frame(tag, period)}


def instant_index(tag: str) -> dict[tuple[int, str], float]:
    """(cik, end date) -> value, across every instantaneous frame pulled."""
    out: dict[tuple[int, str], float] = {}
    for period in INSTANT_PERIODS:
        for r in frame(tag, period):
            out[(r["cik"], r["end"])] = r["val"]
    return out


def build(period: str, instants: dict[str, dict]) -> tuple[list[dict], dict[str, int]]:
    oi = duration_map("OperatingIncomeLoss", period)
    revs = {t: duration_map(t, period) for t in REV_TAGS}
    others = {
        k: duration_map(t, period)
        for k, t in [
            ("gross_profit", "GrossProfit"),
            ("cost_of_revenue", "CostOfRevenue"),
            ("cogs", "CostOfGoodsAndServicesSold"),
            ("rnd", "ResearchAndDevelopmentExpense"),
            ("sgna", "SellingGeneralAndAdministrativeExpense"),
            ("sm", "SellingAndMarketingExpense"),
            ("ga", "GeneralAndAdministrativeExpense"),
            ("sbc", "ShareBasedCompensation"),
            ("capex", "PaymentsToAcquirePropertyPlantAndEquipment"),
            ("cfo", "NetCashProvidedByUsedInOperatingActivities"),
        ]
    }
    sic = json.loads((CACHE / "sic.json").read_text())

    drops = {
        "no OperatingIncomeLoss": 0,
        "no revenue element": 0,
        "revenue <= 0": 0,
        f"revenue < ${MIN_REVENUE:,}": 0,
        "no Assets at the fiscal year end": 0,
        "no SIC code": 0,
    }
    rows = []
    # The universe for the drop count is every CIK that reported either revenue or
    # operating income for the period.
    universe = set(oi)
    for t in REV_TAGS:
        universe |= set(revs[t])

    for cik in sorted(universe):
        if cik not in oi:
            drops["no OperatingIncomeLoss"] += 1
            continue
        end = oi[cik]["end"]
        rv = None
        for t in REV_TAGS:
            r = revs[t].get(cik)
            if r and r["end"] == end:
                rv = r
                rv_tag = t
                break
        if rv is None:
            drops["no revenue element"] += 1
            continue
        if rv["val"] <= 0:
            drops["revenue <= 0"] += 1
            continue
        if rv["val"] < MIN_REVENUE:
            drops[f"revenue < ${MIN_REVENUE:,}"] += 1
            continue
        assets = instants["Assets"].get((cik, end))
        if not assets or assets <= 0:
            drops["no Assets at the fiscal year end"] += 1
            continue
        s = sic.get(str(cik), {})
        if not s.get("sic"):
            drops["no SIC code"] += 1
            continue

        rec: dict = {
            "cik": cik,
            "name": oi[cik]["entityName"],
            "sic": s["sic"],
            "sic_desc": s.get("sicDescription"),
            "period": period,
            "fy_end": end,
            "revenue": rv["val"],
            "revenue_tag": rv_tag,
            "operating_income": oi[cik]["val"],
            "assets": assets,
            "accn": oi[cik]["accn"],
        }
        for k, m in others.items():
            r = m.get(cik)
            rec[k] = r["val"] if (r and r["end"] == end) else None
        rec["ppe"] = instants["PropertyPlantAndEquipmentNet"].get((cik, end))
        rec["equity"] = instants["StockholdersEquity"].get((cik, end))
        rec["cash"] = instants["CashAndCashEquivalentsAtCarryingValue"].get((cik, end))
        rec["goodwill"] = instants["Goodwill"].get((cik, end))

        rv_v = rec["revenue"]
        # Fallbacks.  Most software filers tag neither GrossProfit (they print
        # "cost of revenue" and let the reader subtract) nor the combined
        # SellingGeneralAndAdministrativeExpense (they split sales-and-marketing
        # from general-and-administrative).  Without these two fallbacks the
        # gross-margin and SG&A rows would be built from a handful of filers.
        if rec["gross_profit"] is None:
            for src in ("cost_of_revenue", "cogs"):
                if rec[src] is not None:
                    rec["gross_profit"] = rv_v - rec[src]
                    rec["gross_profit_derived"] = f"Revenues - {src}"
                    break
        if rec["sgna"] is None and rec["sm"] is not None and rec["ga"] is not None:
            rec["sgna"] = rec["sm"] + rec["ga"]
            rec["sgna_derived"] = "SellingAndMarketing + GeneralAndAdministrative"

        rec["operating_margin"] = rec["operating_income"] / rv_v
        rec["asset_turnover"] = rv_v / assets
        rec["roa"] = rec["operating_income"] / assets
        # Assets less cash and goodwill: a rough "operating assets" base.  Cash is
        # not productive capital and goodwill is the price of past acquisitions,
        # and both are a far larger share of a software balance sheet than of a
        # fab's.  Untagged cash or goodwill is treated as zero, which is the
        # conservative direction (it leaves the denominator larger).
        oa = assets - (rec["cash"] or 0) - (rec["goodwill"] or 0)
        rec["operating_assets"] = oa
        rec["op_asset_turnover"] = (rv_v / oa) if oa > 0 else None
        rec["op_roa"] = (rec["operating_income"] / oa) if oa > 0 else None
        for key, src in [
            ("gross_margin", "gross_profit"),
            ("rnd_pct", "rnd"),
            ("sgna_pct", "sgna"),
            ("sbc_pct", "sbc"),
            ("capex_intensity", "capex"),
            ("ppe_intensity", "ppe"),
            ("cfo_margin", "cfo"),
        ]:
            rec[key] = (rec[src] / rv_v) if rec[src] is not None else None
        rows.append(rec)
    return rows, drops


def pctile(xs: list[float], q: float) -> float:
    """Linear-interpolation percentile on a sorted list (numpy's default method)."""
    s = sorted(xs)
    if not s:
        return float("nan")
    i = (len(s) - 1) * q
    lo, hi = math.floor(i), math.ceil(i)
    return s[lo] if lo == hi else s[lo] + (s[hi] - s[lo]) * (i - lo)


def rank_of(xs: list[float], v: float) -> float:
    """Share of the population at or below v, in per cent."""
    return 100.0 * sum(1 for x in xs if x <= v) / len(xs)


def summarise(rows: list[dict], label: str, codes: list[str]) -> list[dict]:
    sel = rows if codes == ["*"] else [r for r in rows if r["sic"] in codes]
    print(f"\n### {label}   (n = {len(sel)} filers with revenue and operating income)")
    if not sel:
        return sel
    hdr = f"{'metric':18s} {'n':>5s} " + " ".join(
        f"{c:>9s}" for c in ("min", "p10", "p25", "median", "p75", "p90", "max")
    )
    print(hdr)
    print("-" * len(hdr))
    for key, _desc in METRICS:
        xs = [r[key] for r in sel if r[key] is not None]
        if not xs:
            print(f"{key:18s} {0:5d}   (no filer in this group tags it)")
            continue
        vals = [min(xs)] + [pctile(xs, q) for q in (0.10, 0.25, 0.50, 0.75, 0.90)] + [max(xs)]
        print(f"{key:18s} {len(xs):5d} " + " ".join(f"{100*v:8.1f}%" for v in vals))
    return sel


def dupont(rows: list[dict]) -> None:
    print("\n\n## DuPont: operating margin x asset turnover = return on assets")
    print("\nSilex Microsystems, 2025 (from the IPO prospectus and the filed accounts):")
    # Parent-company operating result, the figure the repo carries in LNI-17.
    sx_rev, sx_oi_parent, sx_oi_group, sx_assets = 1385e6, 314e6, 368e6, 2246e6
    for nm, oiv in (("parent-company EBIT (LNI-17)", sx_oi_parent), ("group EBIT", sx_oi_group)):
        m, t = oiv / sx_rev, sx_rev / sx_assets
        print(
            f"  {nm:30s} margin {100*m:5.2f}%  x turnover {t:5.3f}  = ROA {100*m*t:5.2f}%"
            f"   (SEK {oiv/1e6:,.0f}m / SEK {sx_assets/1e6:,.0f}m)"
        )
    for label, codes in GROUPS.items():
        sel = rows if codes == ["*"] else [r for r in rows if r["sic"] in codes]
        if len(sel) < 5:
            continue
        m = pctile([r["operating_margin"] for r in sel], 0.5)
        t = pctile([r["asset_turnover"] for r in sel], 0.5)
        roa = pctile([r["roa"] for r in sel], 0.5)
        print(
            f"  {label:45s} median margin {100*m:7.2f}%  median turnover {t:5.3f} "
            f" product {100*m*t:7.2f}%   median ROA {100*roa:7.2f}%"
        )
    # The two questions the write-up has to answer.
    sw = [r for r in rows if r["sic"] == "7372"]
    sw_roa = pctile([r["roa"] for r in sw], 0.5)
    sw_m = pctile([r["operating_margin"] for r in sw], 0.5)
    sw_t = pctile([r["asset_turnover"] for r in sw], 0.5)
    fab_t = 1385e6 / 2246e6
    print("\nQ1. At equal operating margin, how much better is software than the fab?")
    print(
        f"  SIC 7372 median asset turnover {sw_t:.3f} / Silex turnover {fab_t:.3f} = "
        f"{sw_t/fab_t:.3f}x  -> at the SAME operating margin the software firm earns "
        f"{sw_t/fab_t:.3f}x the return on assets."
    )
    print("\nQ2. What operating margin would the fab need to match SIC 7372's median ROA?")
    print(
        f"  required margin = median ROA {100*sw_roa:.3f}% / fab turnover {fab_t:.4f} = "
        f"{100*sw_roa/fab_t:.2f}%   (against Silex's actual 22.67% parent / 26.57% group)"
    )
    print(f"  (SIC 7372 median operating margin is {100*sw_m:.2f}%.)")


def rule40(rows_now: list[dict], rows_prior: list[dict], codes=("7372",), label="SIC 7372") -> None:
    print(f"\n\n## Rule of 40 [{label}]: is a low software margin a growth choice?")
    prior = {r["cik"]: r for r in rows_prior}
    pts = []
    for r in rows_now:
        if r["sic"] not in codes:
            continue
        p = prior.get(r["cik"])
        if not p or p["revenue"] <= 0:
            continue
        g = r["revenue"] / p["revenue"] - 1.0
        if not -0.9 < g < 5.0:  # drop reverse mergers and restatement artefacts
            continue
        pts.append((g, r["operating_margin"], r))
    print(f"  n = {len(pts)} {label} filers with both years of revenue and a sane growth rate")
    if len(pts) < 10:
        return
    gs = [p[0] for p in pts]
    ms = [p[1] for p in pts]

    def pearson(a, b):
        n = len(a)
        ma, mb = sum(a) / n, sum(b) / n
        cov = sum((x - ma) * (y - mb) for x, y in zip(a, b))
        va = math.sqrt(sum((x - ma) ** 2 for x in a))
        vb = math.sqrt(sum((y - mb) ** 2 for y in b))
        return cov / (va * vb) if va and vb else float("nan")

    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        rk = [0.0] * len(v)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
                j += 1
            avg = (i + j) / 2 + 1
            for k in range(i, j + 1):
                rk[order[k]] = avg
            i = j + 1
        return rk

    r_p = pearson(gs, ms)
    r_s = pearson(ranks(gs), ranks(ms))
    n = len(pts)
    t = r_s * math.sqrt((n - 2) / (1 - r_s**2)) if abs(r_s) < 1 else float("inf")
    print(f"  Pearson r(growth, operating margin)  = {r_p:+.3f}")
    print(f"  Spearman rho                         = {r_s:+.3f}   (t = {t:+.2f}, n = {n})")

    # OLS margin = a + b * growth, on winsorised margins so one -5,000% filer
    # does not set the slope.
    lo, hi = pctile(ms, 0.01), pctile(ms, 0.99)
    mw = [min(max(m, lo), hi) for m in ms]
    mg, mm = sum(gs) / n, sum(mw) / n
    sxx = sum((g - mg) ** 2 for g in gs)
    b = sum((g - mg) * (m - mm) for g, m in zip(gs, mw)) / sxx
    a = mm - b * mg
    resid = [m - (a + b * g) for g, m in zip(gs, mw)]
    se = math.sqrt(sum(e * e for e in resid) / (n - 2) / sxx)
    print(
        f"  OLS (margins winsorised at the 1st/99th pct): margin = {100*a:+.2f}% "
        f"{100*b:+.2f} pp per 1.00 of growth,  t = {b/se:+.2f}"
    )

    print("\n  Cross-tabulation by revenue-growth quintile (medians):")
    pts.sort(key=lambda p: p[0])
    q = len(pts) // 5
    print(f"  {'growth quintile':18s} {'n':>4s} {'median growth':>14s} {'median op margin':>17s}"
          f" {'median R&D/rev':>15s} {'median SBC/rev':>15s}")
    for i in range(5):
        chunk = pts[i * q: (i + 1) * q] if i < 4 else pts[4 * q:]
        gq = pctile([c[0] for c in chunk], 0.5)
        mq = pctile([c[1] for c in chunk], 0.5)
        rd = [c[2]["rnd_pct"] for c in chunk if c[2]["rnd_pct"] is not None]
        sb = [c[2]["sbc_pct"] for c in chunk if c[2]["sbc_pct"] is not None]
        print(
            f"  Q{i+1} (slowest→fastest) {len(chunk):4d} {100*gq:13.1f}% {100*mq:16.1f}%"
            f" {100*pctile(rd,0.5) if rd else float('nan'):14.1f}%"
            f" {100*pctile(sb,0.5) if sb else float('nan'):14.1f}%"
        )

    # The pooled correlation is dominated by the shrinking filers, whose margins
    # are terrible for a reason that has nothing to do with buying growth.  Split
    # the population at zero growth and test each half separately.
    print("\n  Split at zero growth, because the two halves are different stories:")
    for nm, sub in (("shrinking (growth < 0)", [p for p in pts if p[0] < 0]),
                    ("growing (growth >= 0)", [p for p in pts if p[0] >= 0]),
                    ("growing fast (growth >= 20%)", [p for p in pts if p[0] >= 0.20])):
        if len(sub) < 10:
            continue
        g = [x[0] for x in sub]
        mm_ = [x[1] for x in sub]
        rs = pearson(ranks(g), ranks(mm_))
        k = len(sub)
        tt = rs * math.sqrt((k - 2) / (1 - rs**2)) if abs(rs) < 1 else float("inf")
        print(f"    {nm:30s} n={k:4d}  median growth {100*pctile(g,.5):6.1f}%"
              f"  median margin {100*pctile(mm_,.5):7.1f}%"
              f"  Spearman {rs:+.3f} (t = {tt:+.2f})")

    print("\n  'Rule of 40' score = revenue growth + operating margin (GAAP):")
    scores = [g + m for g, m, _ in pts]
    print(
        "  " + "  ".join(
            f"{lbl}={100*pctile(scores, q):.1f}%"
            for lbl, q in (("p10", .1), ("p25", .25), ("median", .5), ("p75", .75), ("p90", .9))
        )
    )
    print(f"  share of filers clearing 40%: {100*sum(1 for s in scores if s >= 0.40)/n:.1f}%")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rule40", action="store_true")
    ap.add_argument("--dupont", action="store_true")
    ap.add_argument("--dump", metavar="SIC", help="print every filer in one SIC group")
    a = ap.parse_args()

    instants = {t: instant_index(t) for t in INSTANT_TAGS}
    rows25, drops25 = build("CY2025", instants)
    rows24, _ = build("CY2024", instants)

    print("# Software margins: the distribution, from SEC XBRL frames")
    print("\nMost recent complete fiscal year = the annual period the SEC frames API")
    print("assigns to CY2025 (each filer's own fiscal year, which for software often")
    print("ends 31 January or 30 June).  Prior year = CY2024.")
    print(f"\nCY2025: {len(rows25)} usable filers.   CY2024: {len(rows24)} usable filers.")
    print("\nDropped from CY2025, and why:")
    for k, v in drops25.items():
        print(f"  {v:6d}  {k}")

    if a.dump:
        sel = sorted(
            (r for r in rows25 if r["sic"] == a.dump),
            key=lambda r: -r["revenue"],
        )
        for r in sel:
            print(
                f"{r['name'][:42]:42s} {r['fy_end']} rev {r['revenue']:>16,.0f} "
                f"om {100*r['operating_margin']:8.2f}% at {r['asset_turnover']:6.3f} "
                f"roa {100*r['roa']:8.2f}%"
            )
        return

    if a.rule40:
        rule40(rows25, rows24)
        rule40(rows25, rows24,
               ("7370", "7371", "7372", "7373", "7374", "7375", "7377", "7379"),
               "all 737x")
        return
    if a.dupont:
        dupont(rows25)
        return

    for yr, rows in (("CY2025", rows25), ("CY2024", rows24)):
        print(f"\n\n# {yr}")
        for label, codes in GROUPS.items():
            summarise(rows, label, codes)
        for label, lo, hi in SIZE_BANDS:
            band = [r for r in rows if r["sic"] == "7372" and lo <= r["revenue"] < hi]
            print(f"\n### {label}   (n = {len(band)})")
            if not band:
                continue
            for key, _d in METRICS:
                xs = [r[key] for r in band if r[key] is not None]
                if not xs:
                    continue
                v = [min(xs)] + [pctile(xs, q) for q in (.1, .25, .5, .75, .9)] + [max(xs)]
                print(f"{key:18s} {len(xs):5d} " + " ".join(f"{100*x:8.1f}%" for x in v))
        # Aggregate (sum of revenue, sum of operating income) for the software
        # groups, as a counterweight to the median: the median filer is tiny.
        print("\n### Aggregates (sum of operating income / sum of revenue), not medians")
        for label, codes in GROUPS.items():
            sel = rows if codes == ["*"] else [r for r in rows if r["sic"] in codes]
            if not sel:
                continue
            tr = sum(r["revenue"] for r in sel)
            to = sum(r["operating_income"] for r in sel)
            ta = sum(r["assets"] for r in sel)
            toa = sum(r["operating_assets"] for r in sel if r["operating_assets"] > 0)
            tr2 = sum(r["revenue"] for r in sel if r["operating_assets"] > 0)
            to2 = sum(r["operating_income"] for r in sel if r["operating_assets"] > 0)
            print(f"  {label:45s} n={len(sel):5d}  revenue-weighted margin {100*to/tr:7.2f}%"
                  f"  turnover {tr/ta:5.3f}  ROA {100*to/ta:7.2f}%"
                  f"   | ex cash+goodwill: turnover {tr2/toa:5.3f}  ROA {100*to2/toa:7.2f}%")

    # Where Silex lands.
    print("\n\n## Silex Microsystems' 2025 operating margin as a percentile")
    for m, nm in ((0.2267, "22.67% (parent-company EBIT, LNI-17)"),
                  (0.2657, "26.57% (group EBIT, prospectus)")):
        print(f"\n  {nm}")
        groups = [(lb, [r for r in rows25 if codes == ["*"] or r["sic"] in codes])
                  for lb, codes in GROUPS.items()]
        groups += [(lb, [r for r in rows25 if r["sic"] == "7372" and lo <= r["revenue"] < hi])
                   for lb, lo, hi in SIZE_BANDS]
        for label, sel in groups:
            if len(sel) < 5:
                continue
            xs = [r["operating_margin"] for r in sel]
            roas = [r["roa"] for r in sel]
            oroas = [r["op_roa"] for r in sel if r["op_roa"] is not None]
            sx_roa = m * (1385.0 / 2246.0)
            sx_oroa = m * (1385.0 / 1980.0)   # assets less SEK 266m cash, no goodwill
            print(
                f"    {label:45s} margin pctile {rank_of(xs, m):5.1f}   "
                f"ROA {100*sx_roa:5.2f}% -> pctile {rank_of(roas, sx_roa):5.1f}   "
                f"ROA-ex-cash {100*sx_oroa:5.2f}% -> pctile {rank_of(oroas, sx_oroa):5.1f}"
            )

    out = CACHE.parent / "distribution_CY2025.json"
    out.write_text(json.dumps(rows25))
    (CACHE.parent / "distribution_CY2024.json").write_text(json.dumps(rows24))
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
