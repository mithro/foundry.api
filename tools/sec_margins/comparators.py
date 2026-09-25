#!/usr/bin/env python3
"""Named software comparators, from each filer's own companyfacts JSON.

The fiscal year to report is chosen the same way the distribution in
sic_distribution.py chooses it: whichever annual period the SEC's frames API
assigns to CY2025 (and CY2024).  That keeps a named company and the population
it sits in on the same footing, even though software fiscal years end in
January, May, June, July and November as well as December.

For each company and year it prints revenue, GAAP operating income, operating
margin, total assets, asset turnover, operating income / assets, gross margin,
R&D, SG&A, share-based compensation, capex and PP&E, with the us-gaap (or
ifrs-full) tag and the accession number each figure came from.

Balance-sheet items are read at the income statement's own end date, so the
DuPont decomposition uses ending assets, not average assets.

Usage:  uv run python tools/sec_margins/comparators.py [--company Adobe]
"""
from __future__ import annotations

import argparse
import datetime
import gzip
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from fetch_sec import CACHE, COMPARATORS  # noqa: E402

ANNUAL_FORMS = {"10-K", "20-F", "40-F", "10-K/A", "20-F/A", "40-F/A"}

# Preference order per concept.  The first tag with an annual value at the target
# end date wins; the tag actually used is printed, because the fallbacks are not
# always like-for-like (Adobe reports marketing and G&A separately, for example).
DURATION = {
    "revenue": [
        "us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax",
        "us-gaap:Revenues",
        "us-gaap:RevenueFromContractWithCustomerIncludingAssessedTax",
        "ifrs-full:Revenue",
        "ifrs-full:RevenueFromContractsWithCustomers",
    ],
    "operating_income": [
        "us-gaap:OperatingIncomeLoss",
        "ifrs-full:ProfitLossFromOperatingActivities",
    ],
    "gross_profit": ["us-gaap:GrossProfit", "ifrs-full:GrossProfit"],
    "rnd": [
        "us-gaap:ResearchAndDevelopmentExpense",
        "us-gaap:ResearchAndDevelopmentExpenseSoftwareExcludingAcquiredInProcessCost",
        "ifrs-full:ResearchAndDevelopmentExpense",
    ],
    "sgna": [
        "us-gaap:SellingGeneralAndAdministrativeExpense",
        "ifrs-full:SellingGeneralAndAdministrativeExpense",
    ],
    # Used only when SellingGeneralAndAdministrativeExpense is absent: the two
    # lines summed.  Flagged in the output with a "+" suffix on the tag.
    "sgna_parts": [
        "us-gaap:SellingAndMarketingExpense",
        "us-gaap:GeneralAndAdministrativeExpense",
        "ifrs-full:SalesAndMarketingExpense",
        "ifrs-full:AdministrativeExpense",
    ],
    "sbc": [
        "us-gaap:ShareBasedCompensation",
        "us-gaap:AllocatedShareBasedCompensationExpense",
        "ifrs-full:ExpenseFromSharebasedPaymentTransactionsWithEmployees",
        "ifrs-full:ExpenseFromSharebasedPaymentTransactionsInWhichGoodsOrServicesReceived"
        "DidNotQualifyForRecognitionAsAssets",
    ],
    "capex": [
        "us-gaap:PaymentsToAcquirePropertyPlantAndEquipment",
        "us-gaap:PaymentsToAcquireProductiveAssets",
        "us-gaap:PaymentsToAcquireOtherProductiveAssets",
        "ifrs-full:PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities",
        "ifrs-full:PurchaseOfPropertyPlantAndEquipmentIntangibleAssetsOtherThanGoodwill"
        "InvestmentPropertyAndOtherNoncurrentAssets",
    ],
    "cfo": [
        "us-gaap:NetCashProvidedByUsedInOperatingActivities",
        "ifrs-full:CashFlowsFromUsedInOperatingActivities",
    ],
}
INSTANT = {
    "assets": ["us-gaap:Assets", "ifrs-full:Assets"],
    "ppe": [
        "us-gaap:PropertyPlantAndEquipmentNet",
        "us-gaap:PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfter"
        "AccumulatedDepreciationAndAmortization",
        "ifrs-full:PropertyPlantAndEquipment",
        "ifrs-full:PropertyPlantAndEquipmentIncludingRightofuseAssets",
    ],
    "equity": [
        "us-gaap:StockholdersEquity",
        "ifrs-full:EquityAttributableToOwnersOfParent",
        "ifrs-full:Equity",
    ],
}


def load(cik: int) -> dict:
    return json.loads(gzip.decompress((CACHE / "facts" / f"CIK{cik:010d}.json.gz").read_bytes()))


def best_unit(facts: dict, tax: str, tag: str) -> tuple[str, list[dict]]:
    """The currency in which the filer actually reports this tag (most facts wins)."""
    try:
        u = facts["facts"][tax][tag]["units"]
    except KeyError:
        return "", []
    cur = max(u, key=lambda c: len(u[c]))
    return cur, u[cur]


def pick_duration(facts: dict, tags: list[str], end: str) -> dict | None:
    for t in tags:
        tax, tag = t.split(":", 1)
        cur, rows = best_unit(facts, tax, tag)
        cands = []
        for r in rows:
            if r["end"] != end or not r.get("start") or r.get("form") not in ANNUAL_FORMS:
                continue
            d0 = datetime.date.fromisoformat(r["start"])
            d1 = datetime.date.fromisoformat(r["end"])
            if not 330 <= (d1 - d0).days <= 400:
                continue
            cands.append(r)
        if cands:
            r = min(cands, key=lambda r: r["accn"])
            return {"val": r["val"], "cur": cur, "tag": t, "accn": r["accn"], "fy": r.get("fy")}
    return None


def pick_instant(facts: dict, tags: list[str], end: str) -> dict | None:
    for t in tags:
        tax, tag = t.split(":", 1)
        cur, rows = best_unit(facts, tax, tag)
        cands = [r for r in rows if r["end"] == end and r.get("form") in ANNUAL_FORMS]
        if cands:
            r = min(cands, key=lambda r: r["accn"])
            return {"val": r["val"], "cur": cur, "tag": t, "accn": r["accn"]}
    return None


def frame_ends() -> dict[str, dict[int, dict]]:
    """CY period -> cik -> the OperatingIncomeLoss fact the SEC assigned to it."""
    out = {}
    for period in ("CY2024", "CY2025"):
        p = CACHE / "frames" / f"OperatingIncomeLoss_{period}.json.gz"
        out[period] = {r["cik"]: r for r in json.loads(gzip.decompress(p.read_bytes()))["data"]}
    return out


def latest_annual_end(facts: dict) -> str | None:
    """Most recent annual period end for which both revenue and op income exist."""
    ends = set()
    for key in ("revenue", "operating_income"):
        e = set()
        for t in DURATION[key]:
            tax, tag = t.split(":", 1)
            _, rows = best_unit(facts, tax, tag)
            for r in rows:
                if r.get("form") in ANNUAL_FORMS and r.get("start"):
                    d0 = datetime.date.fromisoformat(r["start"])
                    d1 = datetime.date.fromisoformat(r["end"])
                    if 330 <= (d1 - d0).days <= 400:
                        e.add(r["end"])
            if e:
                break
        ends = e if not ends else (ends & e)
    return max(ends) if ends else None


def build(name: str, cik: int, end: str, label: str) -> dict | None:
    facts = load(cik)
    rev = pick_duration(facts, DURATION["revenue"], end)
    oi = pick_duration(facts, DURATION["operating_income"], end)
    if not rev or not oi:
        return None
    r: dict = {"company": name, "cik": cik, "period": label, "fy_end": end}
    r["currency"] = rev["cur"]
    for k, f in (("revenue", rev), ("operating_income", oi)):
        r[k], r[k + "_tag"], r[k + "_accn"] = f["val"], f["tag"], f["accn"]
    for k in ("gross_profit", "rnd", "sbc", "capex", "cfo"):
        f = pick_duration(facts, DURATION[k], end)
        r[k] = f["val"] if f else None
        r[k + "_tag"] = f["tag"] if f else None
    f = pick_duration(facts, DURATION["sgna"], end)
    if f:
        r["sgna"], r["sgna_tag"] = f["val"], f["tag"]
    else:
        parts = [pick_duration(facts, [t], end) for t in DURATION["sgna_parts"]]
        parts = [p for p in parts if p]
        r["sgna"] = sum(p["val"] for p in parts) if parts else None
        r["sgna_tag"] = " + ".join(p["tag"] for p in parts) if parts else None
    for k in INSTANT:
        f = pick_instant(facts, INSTANT[k], end)
        r[k] = f["val"] if f else None
        r[k + "_tag"] = f["tag"] if f else None
    return r


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--company")
    a = ap.parse_args()
    frames = frame_ends()
    rows = []
    for name, cik in COMPARATORS.items():
        if a.company and a.company.lower() not in name.lower():
            continue
        seen_ends = set()
        for period in ("CY2024", "CY2025"):
            fr = frames[period].get(cik)
            if not fr:
                continue
            row = build(name, cik, fr["end"], period)
            if row:
                rows.append(row)
                seen_ends.add(fr["end"])
        le = latest_annual_end(load(cik))
        if le and le not in seen_ends:
            row = build(name, cik, le, "latest")
            if row:
                rows.append(row)

    hdr = (
        f"{'company':11s} {'per':7s} {'FY end':11s} {'cur':4s} {'revenue':>15s} {'op inc':>15s} "
        f"{'op mgn':>8s} {'assets':>15s} {'turn':>6s} {'OI/A':>8s} {'gross':>8s} "
        f"{'R&D':>8s} {'SG&A':>8s} {'SBC':>8s} {'capex':>8s} {'PP&E':>8s}"
    )
    print(hdr)
    print("-" * len(hdr))

    def pct(x, b):
        return f"{100*x/b:7.2f}%" if (x is not None and b) else "       -"

    for r in sorted(rows, key=lambda r: (r["company"], r["fy_end"])):
        rv, at = r["revenue"], r["assets"]
        print(
            f"{r['company']:11s} {r['period']:7s} {r['fy_end']:11s} {r['currency']:4s} "
            f"{rv:15,.0f} {r['operating_income']:15,.0f} {100*r['operating_income']/rv:7.2f}% "
            f"{(at or 0):15,.0f} {(rv/at if at else 0):6.3f} "
            f"{pct(r['operating_income'], at)} {pct(r['gross_profit'], rv)} "
            f"{pct(r['rnd'], rv)} {pct(r['sgna'], rv)} {pct(r['sbc'], rv)} "
            f"{pct(r['capex'], rv)} {pct(r['ppe'], rv)}"
        )

    out = CACHE.parent / "comparators.json"
    out.write_text(json.dumps(rows, indent=1))
    print(f"\nwrote {out}  ({len(rows)} rows)")
    print("\nnon-default tags and accession numbers, latest row per company:")
    for name in COMPARATORS:
        rs = [r for r in rows if r["company"] == name]
        if not rs:
            print(f"  {name:11s} NO DATA")
            continue
        r = max(rs, key=lambda r: r["fy_end"])
        odd = [
            f"{k}={r[k + '_tag']}"
            for k in ("revenue", "operating_income", "gross_profit", "rnd", "sgna", "sbc",
                      "capex", "ppe")
            if r.get(k + "_tag")
            and r[k + "_tag"]
            not in (
                "us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax",
                "us-gaap:OperatingIncomeLoss",
                "us-gaap:GrossProfit",
                "us-gaap:ResearchAndDevelopmentExpense",
                "us-gaap:SellingGeneralAndAdministrativeExpense",
                "us-gaap:ShareBasedCompensation",
                "us-gaap:PaymentsToAcquirePropertyPlantAndEquipment",
                "us-gaap:PropertyPlantAndEquipmentNet",
            )
        ]
        print(f"  {name:11s} {r['fy_end']}  accn={r['operating_income_accn']}  {'; '.join(odd)}")


if __name__ == "__main__":
    main()
