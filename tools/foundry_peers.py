#!/usr/bin/env -S uv run --no-project python
"""Named pure-play foundries and IDM contrasts, from their own SEC filings.

Reads the ``companyfacts`` JSON cached by ``tools/sec_fetch.py`` and prints,
for each company and fiscal year, the figures the filing itself carries plus
the ratios derived from them, with the accession number of the filing each
figure came from.  Foreign private issuers that file a 20-F under IFRS
(TSMC, UMC, Tower) are read from the ``ifrs-full`` taxonomy; 10-K filers from
``us-gaap``.

    uv run tools/foundry_peers.py --cache tmp/sec --years 2024,2025
"""

from __future__ import annotations

import argparse
import json
import pathlib

PEERS = [
    (1046179, "TSMC (Taiwan Semiconductor Manufacturing)", "pure-play foundry"),
    (1033767, "UMC (United Microelectronics)", "pure-play foundry"),
    (1709048, "GlobalFoundries Inc.", "pure-play foundry"),
    (928876, "Tower Semiconductor Ltd", "specialty pure-play foundry"),
    (1819974, "SkyWater Technology, Inc.", "US specialty pure-play foundry"),
    (1047127, "Amkor Technology, Inc.", "outsourced assembly and test"),
    (1097864, "onsemi (ON Semiconductor)", "IDM"),
    (97476, "Texas Instruments Incorporated", "IDM"),
    (6281, "Analog Devices, Inc.", "IDM"),
    (1045810, "NVIDIA Corporation", "fabless (contrast)"),
    (2488, "Advanced Micro Devices, Inc.", "fabless (contrast)"),
    (50863, "Intel Corporation", "IDM turned foundry"),
    (827054, "Microchip Technology Incorporated", "IDM"),
]

# Ordered candidate tags: the first that resolves wins.
CONCEPTS = {
    "revenue": [
        ("us-gaap", "RevenueFromContractWithCustomerExcludingAssessedTax"),
        ("us-gaap", "Revenues"),
        ("ifrs-full", "Revenue"),
        ("ifrs-full", "RevenueFromContractsWithCustomers"),
    ],
    "gross_profit": [
        ("us-gaap", "GrossProfit"),
        ("ifrs-full", "GrossProfit"),
    ],
    "operating_income": [
        ("us-gaap", "OperatingIncomeLoss"),
        ("ifrs-full", "ProfitLossFromOperatingActivities"),
    ],
    "capex": [
        ("us-gaap", "PaymentsToAcquirePropertyPlantAndEquipment"),
        ("ifrs-full", "PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"),
    ],
    "dda": [
        ("us-gaap", "DepreciationDepletionAndAmortization"),
        ("us-gaap", "DepreciationAmortizationAndAccretionNet"),
        ("us-gaap", "DepreciationAndAmortization"),
        ("ifrs-full", "DepreciationExpense"),
    ],
}
INSTANT_CONCEPTS = {
    "assets": [("us-gaap", "Assets"), ("ifrs-full", "Assets")],
    "ppe": [
        ("us-gaap", "PropertyPlantAndEquipmentNet"),
        (
            "us-gaap",
            "PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulated"
            "DepreciationAndAmortization",
        ),
        ("ifrs-full", "PropertyPlantAndEquipment"),
    ],
    "equity": [
        ("us-gaap", "StockholdersEquity"),
        ("ifrs-full", "EquityAttributableToOwnersOfParent"),
        ("ifrs-full", "Equity"),
    ],
}

ANNUAL_FORMS = ("10-K", "20-F", "40-F")


def facts(cache: pathlib.Path, cik: int) -> dict | None:
    p = cache / "facts" / f"CIK{cik:010d}.json"
    if not p.exists() or p.stat().st_size == 0:
        return None
    return json.loads(p.read_text())


def pick_duration(d: dict, candidates, fy: int):
    """Longest annual duration ending in fiscal year ``fy``."""
    for tax, tag in candidates:
        body = d["facts"].get(tax, {}).get(tag)
        if not body:
            continue
        for unit, pts in body["units"].items():
            best = None
            for p in pts:
                if p.get("form") not in ANNUAL_FORMS or p.get("fp") != "FY":
                    continue
                if p.get("fy") != fy or not p.get("start"):
                    continue
                span = (
                    int(p["end"][:4]) * 372 + int(p["end"][5:7]) * 31
                    + int(p["end"][8:10])
                ) - (
                    int(p["start"][:4]) * 372 + int(p["start"][5:7]) * 31
                    + int(p["start"][8:10])
                )
                if span < 300:  # not an annual period
                    continue
                if best is None or p["end"] > best["end"]:
                    best = p
            if best:
                return tag, unit, best
    return None


def pick_instant(d: dict, candidates, fy: int):
    for tax, tag in candidates:
        body = d["facts"].get(tax, {}).get(tag)
        if not body:
            continue
        for unit, pts in body["units"].items():
            best = None
            for p in pts:
                if p.get("form") not in ANNUAL_FORMS or p.get("fp") != "FY":
                    continue
                if p.get("fy") != fy or p.get("start"):
                    continue
                if best is None or p["end"] > best["end"]:
                    best = p
            if best:
                return tag, unit, best
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default="tmp/sec")
    ap.add_argument("--years", default="2024,2025")
    args = ap.parse_args()
    cache = pathlib.Path(args.cache)
    years = [int(y) for y in args.years.split(",")]

    for cik, name, kind in PEERS:
        d = facts(cache, cik)
        print(f"\n=== {name}  (CIK {cik}; {kind})")
        if d is None:
            print("    no cached companyfacts")
            continue
        for fy in years:
            vals: dict[str, tuple] = {}
            for key, cands in CONCEPTS.items():
                got = pick_duration(d, cands, fy)
                if got:
                    vals[key] = got
            for key, cands in INSTANT_CONCEPTS.items():
                got = pick_instant(d, cands, fy)
                if got:
                    vals[key] = got
            if "revenue" not in vals:
                print(f"  FY{fy}: no annual revenue fact")
                continue
            rev_tag, unit, rev = vals["revenue"]
            print(f"  FY{fy}  period {rev.get('start')} .. {rev['end']}"
                  f"  currency {unit}  form {rev.get('form')}"
                  f"  accn {rev.get('accn')}")
            for key in ("revenue", "gross_profit", "operating_income", "assets",
                        "ppe", "equity", "capex", "dda"):
                if key in vals:
                    tag, u, p = vals[key]
                    print(f"      {key:17} {p['val']:>20,}  [{tag}, {u},"
                          f" as of {p['end']}]")
                else:
                    print(f"      {key:17} {'--':>20}")
            r = vals["revenue"][2]["val"]
            oi = vals.get("operating_income", (None, None, {"val": None}))[2]["val"]
            ta = vals.get("assets", (None, None, {"val": None}))[2]["val"]
            eq = vals.get("equity", (None, None, {"val": None}))[2]["val"]
            ppe = vals.get("ppe", (None, None, {"val": None}))[2]["val"]
            cx = vals.get("capex", (None, None, {"val": None}))[2]["val"]
            gp = vals.get("gross_profit", (None, None, {"val": None}))[2]["val"]
            if oi is not None and r:
                print(f"      DERIVED operating margin = {oi:,} / {r:,}"
                      f" = {oi / r * 100:.2f}%")
            if gp is not None and r:
                print(f"      DERIVED gross margin     = {gp:,} / {r:,}"
                      f" = {gp / r * 100:.2f}%")
            if ta:
                print(f"      DERIVED asset turnover   = {r:,} / {ta:,}"
                      f" = {r / ta:.4f}x")
                if oi is not None:
                    print(f"      DERIVED EBIT / assets    = {oi:,} / {ta:,}"
                          f" = {oi / ta * 100:.2f}%")
                if ppe is not None:
                    print(f"      DERIVED PP&E / assets    = {ppe:,} / {ta:,}"
                          f" = {ppe / ta * 100:.2f}%")
            if ppe is not None and r:
                print(f"      DERIVED PP&E / revenue   = {ppe:,} / {r:,}"
                      f" = {ppe / r:.4f}x")
            if cx is not None and r:
                print(f"      DERIVED capex / revenue  = {cx:,} / {r:,}"
                      f" = {cx / r * 100:.2f}%")
            if eq and oi is not None:
                print(f"      DERIVED EBIT / equity    = {oi:,} / {eq:,}"
                      f" = {oi / eq * 100:.2f}%")


if __name__ == "__main__":
    main()
