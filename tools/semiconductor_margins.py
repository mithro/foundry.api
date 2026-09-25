#!/usr/bin/env -S uv run --no-project python
"""Distribution of operating margin, asset turnover and capital intensity
across every SEC filer in a given SIC code, from the SEC's free XBRL
"frames" API.

Run ``tools/sec_fetch.py`` first to populate the cache, then::

    uv run tools/semiconductor_margins.py --cache tmp/sec --year 2025

Medians and quartiles only: these tails are extreme and a mean is
meaningless in them.
"""

from __future__ import annotations

import argparse
import json
import math
import pathlib
import statistics
import sys

SIC_NAMES = {
    "3674": "Semiconductors and related devices",
    "3672": "Printed circuit boards",
    "3559": "Special industry machinery (incl. semiconductor equipment)",
    "3827": "Laboratory analytical instruments / optical instruments & lenses",
    "3826": "Laboratory analytical instruments",
    "3825": "Instruments for measuring and testing electricity",
    "7372": "Prepackaged software (context only; owned by the software agent)",
}

TARGET_SICS = ["3674", "3672", "3559", "3827", "3826"]


def load_frame(cache: pathlib.Path, concept: str, period: str) -> dict[int, float]:
    path = cache / "frames" / f"{concept}_{period}.json"
    if not path.exists() or path.stat().st_size == 0:
        return {}
    data = json.loads(path.read_text())
    out: dict[int, float] = {}
    for row in data["data"]:
        out[row["cik"]] = float(row["val"])
    return out


def load_sic(cache: pathlib.Path) -> dict[int, tuple[str, str]]:
    out: dict[int, tuple[str, str]] = {}
    for path in (cache / "sub").glob("CIK*.json"):
        if path.stat().st_size == 0:
            continue
        try:
            d = json.loads(path.read_text())
        except json.JSONDecodeError:
            continue
        cik = int(d.get("cik", 0) or 0)
        if not cik:
            continue
        out[cik] = (str(d.get("sic", "")), d.get("name", ""))
    return out


def quantile(values: list[float], q: float) -> float:
    """Linear-interpolation quantile, the same definition throughout."""
    if not values:
        return float("nan")
    s = sorted(values)
    if len(s) == 1:
        return s[0]
    pos = q * (len(s) - 1)
    lo = math.floor(pos)
    hi = math.ceil(pos)
    if lo == hi:
        return s[lo]
    return s[lo] + (s[hi] - s[lo]) * (pos - lo)


def percentile_of(values: list[float], x: float) -> float:
    """Share of the sample strictly below x, plus half the ties."""
    if not values:
        return float("nan")
    below = sum(1 for v in values if v < x)
    ties = sum(1 for v in values if v == x)
    return 100.0 * (below + 0.5 * ties) / len(values)


def spearman(xs: list[float], ys: list[float]) -> float:
    n = len(xs)
    if n < 3:
        return float("nan")

    def ranks(vs: list[float]) -> list[float]:
        order = sorted(range(len(vs)), key=lambda i: vs[i])
        r = [0.0] * len(vs)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and vs[order[j + 1]] == vs[order[i]]:
                j += 1
            avg = (i + j) / 2 + 1
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r

    rx, ry = ranks(xs), ranks(ys)
    mx, my = statistics.fmean(rx), statistics.fmean(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
    return num / den if den else float("nan")


def describe(name: str, values: list[float], as_pct: bool, out=sys.stdout) -> None:
    if not values:
        print(f"  {name:26} n=0", file=out)
        return
    f = (lambda v: f"{v * 100:8.2f}%") if as_pct else (lambda v: f"{v:8.3f} ")
    s = sorted(values)
    print(
        f"  {name:26} n={len(s):4d}"
        f"  min{f(s[0])} p10{f(quantile(s, .10))} p25{f(quantile(s, .25))}"
        f" median{f(quantile(s, .50))} p75{f(quantile(s, .75))}"
        f" p90{f(quantile(s, .90))} max{f(s[-1])}",
        file=out,
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default="tmp/sec")
    ap.add_argument("--year", type=int, default=2025)
    ap.add_argument(
        "--min-revenue",
        type=float,
        default=10e6,
        help="drop filers below this revenue; SIC 3674 is full of pre-revenue "
        "shells whose ratios are noise",
    )
    args = ap.parse_args()
    cache = pathlib.Path(args.cache)
    y = args.year

    rev_a = load_frame(cache, "Revenues", f"CY{y}")
    rev_b = load_frame(
        cache, "RevenueFromContractWithCustomerExcludingAssessedTax", f"CY{y}"
    )
    oi = load_frame(cache, "OperatingIncomeLoss", f"CY{y}")
    gp = load_frame(cache, "GrossProfit", f"CY{y}")
    capex = load_frame(cache, "PaymentsToAcquirePropertyPlantAndEquipment", f"CY{y}")
    dda = load_frame(cache, "DepreciationDepletionAndAmortization", f"CY{y}")
    assets = load_frame(cache, "Assets", f"CY{y}Q4I")
    ppe = load_frame(cache, "PropertyPlantAndEquipmentNet", f"CY{y}Q4I")
    equity = load_frame(cache, "StockholdersEquity", f"CY{y}Q4I")
    sic = load_sic(cache)

    print(f"# SEC XBRL frames, calendar year {y}")
    print(f"  Revenues                                   frame CY{y}: "
          f"{len(rev_a)} filers")
    print("  RevenueFromContractWithCustomerExcludingAssessedTax "
          f"frame CY{y}: {len(rev_b)} filers")
    print(f"  OperatingIncomeLoss                        frame CY{y}: "
          f"{len(oi)} filers")
    print(f"  GrossProfit                                frame CY{y}: "
          f"{len(gp)} filers")
    print(f"  PaymentsToAcquirePropertyPlantAndEquipment  frame CY{y}: "
          f"{len(capex)} filers")
    print(f"  DepreciationDepletionAndAmortization        frame CY{y}: "
          f"{len(dda)} filers")
    print(f"  Assets                                     frame CY{y}Q4I: "
          f"{len(assets)} filers")
    print(f"  PropertyPlantAndEquipmentNet               frame CY{y}Q4I: "
          f"{len(ppe)} filers")
    print(f"  StockholdersEquity                         frame CY{y}Q4I: "
          f"{len(equity)} filers")
    print(f"  SIC codes resolved from data.sec.gov/submissions: {len(sic)} filers")
    print()

    rows_by_sic: dict[str, list[dict]] = {}
    for cik, (code, name) in sic.items():
        if code not in TARGET_SICS:
            continue
        revenue = rev_a.get(cik)
        rev_source = "Revenues"
        if revenue is None:
            revenue = rev_b.get(cik)
            rev_source = "RevenueFromContractWithCustomer..."
        rows_by_sic.setdefault(code, []).append(
            dict(
                cik=cik,
                name=name,
                revenue=revenue,
                rev_source=rev_source,
                oi=oi.get(cik),
                gp=gp.get(cik),
                capex=capex.get(cik),
                dda=dda.get(cik),
                assets=assets.get(cik),
                ppe=ppe.get(cik),
                equity=equity.get(cik),
            )
        )

    silex_margin_company = 314 / 1385  # LNI-17, filed Swedish accounts
    silex_margin_group = 368 / 1385  # prospectus, consolidated
    silex_turnover = 1385 / 2246
    silex_roa = 368 / 2246
    silex_ppe_int = 942 / 2246  # owned PP&E / total assets
    silex_capex_int = 195 / 1385

    all_rows: list[dict] = []

    for code in TARGET_SICS:
        rows = rows_by_sic.get(code, [])
        print(f"## SIC {code} -- {SIC_NAMES.get(code, '')}")
        print(f"   filers with a resolved SIC and any frame data: {len(rows)}")

        have_rev_oi = [r for r in rows if r["revenue"] and r["oi"] is not None]
        print(f"   dropped, no revenue tag in CY{y}: "
              f"{sum(1 for r in rows if not r['revenue'])}")
        print(f"   dropped, no OperatingIncomeLoss tag in CY{y}: "
              f"{sum(1 for r in rows if r['oi'] is None)}")
        sized = [r for r in have_rev_oi if r["revenue"] >= args.min_revenue]
        print(f"   dropped, revenue below ${args.min_revenue:,.0f}: "
              f"{len(have_rev_oi) - len(sized)}")
        print(f"   n used for margin: {len(sized)}")

        margins = [r["oi"] / r["revenue"] for r in sized]
        gross = [
            r["gp"] / r["revenue"] for r in sized if r["gp"] is not None
        ]
        with_assets = [r for r in sized if r["assets"]]
        turnover = [r["revenue"] / r["assets"] for r in with_assets]
        roa = [r["oi"] / r["assets"] for r in with_assets]
        with_ppe = [r for r in with_assets if r["ppe"] is not None]
        ppe_int_assets = [r["ppe"] / r["assets"] for r in with_ppe]
        ppe_int_rev = [r["ppe"] / r["revenue"] for r in with_ppe]
        capex_int = [
            r["capex"] / r["revenue"] for r in sized if r["capex"] is not None
        ]
        dda_int = [r["dda"] / r["revenue"] for r in sized if r["dda"] is not None]
        with_eq = [r for r in sized if r["equity"] and r["equity"] > 0]
        roe = [r["oi"] / r["equity"] for r in with_eq]

        describe("operating margin", margins, True)
        describe("gross margin", gross, True)
        describe("asset turnover (x)", turnover, False)
        describe("operating income/assets", roa, True)
        describe("operating income/equity", roe, True)
        describe("PP&E / assets", ppe_int_assets, True)
        describe("PP&E / revenue (x)", ppe_int_rev, False)
        describe("capex / revenue", capex_int, True)
        describe("D&A / revenue", dda_int, True)

        if code == "3674" and margins:
            print()
            print("   Silex against this distribution:")
            print(f"     operating margin 22.67% (LNI-17, filed company accounts):"
                  f" percentile {percentile_of(margins, silex_margin_company):.1f}")
            print(f"     operating margin 26.57% (prospectus, consolidated):"
                  f" percentile {percentile_of(margins, silex_margin_group):.1f}")
            print(f"     asset turnover 0.617x:"
                  f" percentile {percentile_of(turnover, silex_turnover):.1f}")
            print(f"     operating income/assets 16.38%:"
                  f" percentile {percentile_of(roa, silex_roa):.1f}")
            print(f"     PP&E/assets 41.94%:"
                  f" percentile {percentile_of(ppe_int_assets, silex_ppe_int):.1f}")
            print(f"     capex/revenue 14.08%:"
                  f" percentile {percentile_of(capex_int, silex_capex_int):.1f}")
            print()
            print("   Does capital intensity explain the margin? "
                  "(SIC 3674, quartiles of PP&E/revenue)")
            pairs = [
                (r["ppe"] / r["revenue"], r["oi"] / r["revenue"], r["name"])
                for r in with_ppe
            ]
            pairs.sort()
            n = len(pairs)
            print(f"     n = {n}; Spearman rho(PP&E/revenue, operating margin) = "
                  f"{spearman([p[0] for p in pairs], [p[1] for p in pairs]):.3f}")
            for qi in range(4):
                lo = qi * n // 4
                hi = (qi + 1) * n // 4
                chunk = pairs[lo:hi]
                if not chunk:
                    continue
                print(
                    f"     Q{qi + 1} PP&E/revenue "
                    f"{chunk[0][0]:.3f}x-{chunk[-1][0]:.3f}x  n={len(chunk)}  "
                    f"median operating margin "
                    f"{quantile([c[1] for c in chunk], .5) * 100:7.2f}%   "
                    f"median PP&E/revenue {quantile([c[0] for c in chunk], .5):.3f}x"
                )
            print()
            print("   The ten largest SIC 3674 filers by revenue, for orientation:")
            top = sorted(sized, key=lambda r: -r["revenue"])[:10]
            for r in top:
                ta = r["assets"]
                print(
                    f"     {r['name'][:38]:38} rev ${r['revenue']/1e9:8.2f}bn"
                    f"  EBIT margin {r['oi']/r['revenue']*100:7.2f}%"
                    + (
                        f"  turnover {r['revenue']/ta:.3f}x"
                        f"  EBIT/assets {r['oi']/ta*100:7.2f}%"
                        if ta
                        else "  (no Assets tag)"
                    )
                )
        all_rows.extend(sized)
        print()

    # A cross-industry anchor: the whole frame, all SIC codes, for scale.
    print("## All SEC filers with both an operating income and a balance sheet "
          f"(CY{y}), any SIC")
    everyone = []
    for cik, (code, name) in sic.items():
        revenue = rev_a.get(cik) or rev_b.get(cik)
        if not revenue or revenue < args.min_revenue:
            continue
        if oi.get(cik) is None or not assets.get(cik):
            continue
        everyone.append(
            dict(name=name, sic=code, revenue=revenue, oi=oi[cik],
                 assets=assets[cik], ppe=ppe.get(cik))
        )
    print(f"   n = {len(everyone)}")
    describe("operating margin", [r["oi"] / r["revenue"] for r in everyone], True)
    describe("asset turnover (x)",
             [r["revenue"] / r["assets"] for r in everyone], False)
    describe("operating income/assets",
             [r["oi"] / r["assets"] for r in everyone], True)
    print()

    # What margin would a fab need to reach a given return on assets?
    print("## What operating margin does a fab need to hit a target return on "
          "assets?")
    sic3674 = [r for r in rows_by_sic.get("3674", [])
               if r["revenue"] and r["revenue"] >= args.min_revenue and r["assets"]]
    med_turn = quantile([r["revenue"] / r["assets"] for r in sic3674], .5)
    print(f"   median SIC 3674 asset turnover = {med_turn:.4f}x")
    print(f"   Silex asset turnover           = {silex_turnover:.4f}x")

    # Most SIC 3674 filers are fabless.  Isolate the ones that actually own a
    # plant: PP&E at or above 30 percent of revenue.
    fabby = [r for r in sic3674
             if r["ppe"] is not None and r["ppe"] / r["revenue"] >= 0.30]
    if fabby:
        ft = [r["revenue"] / r["assets"] for r in fabby]
        fm = [r["oi"] / r["revenue"] for r in fabby]
        fr = [r["oi"] / r["assets"] for r in fabby]
        print()
        print("   Restricting to plant-owning filers (PP&E >= 30% of revenue):")
        print(f"     n = {len(fabby)}")
        describe("asset turnover (x)", ft, False)
        describe("operating margin", fm, True)
        describe("operating income/assets", fr, True)
        print(f"     median plant-owning asset turnover = {quantile(ft, .5):.4f}x")
        print(f"     Silex operating-margin percentile within this subset ="
              f" {percentile_of(fm, silex_margin_company):.1f}"
              f" (22.67%) / {percentile_of(fm, silex_margin_group):.1f} (26.57%)")
        med_turn_fab = quantile(ft, .5)
        for target in (0.10, 0.15, 0.20, 0.25, 0.30, 0.40):
            print(
                f"     to earn {target*100:4.0f}% on assets at the plant-owning"
                f" median {med_turn_fab:.3f}x, margin must be"
                f" {target / med_turn_fab * 100:6.2f}%"
            )
        print()

    for target in (0.10, 0.15, 0.20, 0.25, 0.30, 0.40):
        print(
            f"   to earn {target*100:4.0f}% on assets:"
            f"  at {med_turn:.3f}x turnover needs margin"
            f" {target / med_turn * 100:6.2f}%;"
            f"  at Silex's {silex_turnover:.3f}x needs"
            f" {target / silex_turnover * 100:6.2f}%"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
