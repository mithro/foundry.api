#!/usr/bin/env python3
"""Fetch SEC XBRL data for the software-margin distribution (resources/demand/software-margins.md).

Everything comes from data.sec.gov, which is free and needs no key.  www.sec.gov
returns HTTP 403 to automated tools, so nothing here touches it: no
company_tickers.json, no DERA financial-statement data sets, no Archives.

Three kinds of call:
  frames   https://data.sec.gov/api/xbrl/frames/us-gaap/<tag>/USD/<period>.json
           every filer that reported <tag> for <period>, in one response.
           Duration periods are CYyyyy, instantaneous ones CYyyyyQnI.
  facts    https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json
           one filer, every tag, every period.  Used for the named comparators.
  subs     https://data.sec.gov/submissions/CIK##########.json
           used only for the SIC code; we read the first few KB and stop.

Rate limit is 10 requests/second; we sleep 0.15 s between calls.  Every response
is cached under tmp/sec/, which is gitignored, so a re-run is free.

Usage:  uv run python tools/sec_margins/fetch_sec.py [--stage frames|sic|facts|all]
"""
from __future__ import annotations

import argparse
import gzip
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

# A generic descriptive User-Agent.  Never a personal e-mail address.
UA = "foundry-api-research/1.0"
SLEEP = 0.15

ROOT = pathlib.Path(__file__).resolve().parents[2]
CACHE = ROOT / "tmp" / "sec"

# Income-statement / cash-flow tags: duration frames.
DURATION_TAGS = [
    "OperatingIncomeLoss",
    "Revenues",
    "RevenueFromContractWithCustomerExcludingAssessedTax",
    "RevenueFromContractWithCustomerIncludingAssessedTax",
    "GrossProfit",
    "ResearchAndDevelopmentExpense",
    "SellingGeneralAndAdministrativeExpense",
    "NetCashProvidedByUsedInOperatingActivities",
    "PaymentsToAcquirePropertyPlantAndEquipment",
    "ShareBasedCompensation",
    "AllocatedShareBasedCompensationExpense",
    "CostOfRevenue",
    "CostOfGoodsAndServicesSold",
    "SellingAndMarketingExpense",
    "GeneralAndAdministrativeExpense",
]
DURATION_PERIODS = ["CY2023", "CY2024", "CY2025"]

# Balance-sheet tags: instantaneous frames.  A filer's balance-sheet date is its
# own fiscal year end, which for software is often 31 January or 30 June, so we
# pull a wide band of quarters and later join on the exact date.
INSTANT_TAGS = [
    "Assets",
    "StockholdersEquity",
    "PropertyPlantAndEquipmentNet",
    # Total assets flatter a software company: most of the balance sheet is cash
    # and goodwill, not productive capital.  These two let the write-up also
    # report turnover on the assets that actually do the work.
    "CashAndCashEquivalentsAtCarryingValue",
    "Goodwill",
]
INSTANT_PERIODS = [f"CY{y}Q{q}I" for y in (2022, 2023, 2024, 2025, 2026) for q in (1, 2, 3, 4)]

# The named comparators of §2.  CIKs confirmed from data.sec.gov/submissions.
COMPARATORS = {
    "Microsoft": 789019,
    "Adobe": 796343,
    "Oracle": 1341439,
    "Salesforce": 1108524,
    "Workday": 1327811,
    "ServiceNow": 1373715,
    "Snowflake": 1640147,
    "Datadog": 1561550,
    "Atlassian": 1650372,
    "HubSpot": 1404655,
    "Zoom": 1585521,
    "Shopify": 1594805,
    "MongoDB": 1441816,
    "Twilio": 1447669,
    "Intuit": 896878,
    "SAP": 1000184,
    "Amazon": 1018724,
    # Wafer foundries, for the other side of the DuPont comparison.  TSMC, UMC and
    # Tower file 20-F; GlobalFoundries and SkyWater file 10-K.
    "GlobalFoundries": 1709048,
    "SkyWater": 1819974,
    "Tower": 928876,
    "TSMC": 1046179,
    "UMC": 1033767,
}


def get(url: str, dest: pathlib.Path, max_bytes: int | None = None) -> bytes | None:
    """Fetch url into dest (gzip-compressed cache).  Returns the body, or None on 404."""
    if dest.exists():
        return gzip.decompress(dest.read_bytes())
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            raw = resp.read(max_bytes) if max_bytes else resp.read()
            if resp.headers.get("Content-Encoding") == "gzip":
                try:
                    raw = gzip.decompress(raw)
                except (OSError, EOFError):
                    # A truncated ranged read of a gzip stream: decompress what we can.
                    d = __import__("zlib").decompressobj(16 + __import__("zlib").MAX_WBITS)
                    raw = d.decompress(raw)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            dest.with_suffix(".404").write_text("404\n")
            return None
        raise
    finally:
        time.sleep(SLEEP)
    dest.write_bytes(gzip.compress(raw))
    return raw


def stage_frames() -> None:
    jobs = [(t, p) for t in DURATION_TAGS for p in DURATION_PERIODS]
    jobs += [(t, p) for t in INSTANT_TAGS for p in INSTANT_PERIODS]
    for tag, period in jobs:
        dest = CACHE / "frames" / f"{tag}_{period}.json.gz"
        if dest.exists() or dest.with_suffix(".404").exists():
            continue
        url = f"https://data.sec.gov/api/xbrl/frames/us-gaap/{tag}/USD/{period}.json"
        body = get(url, dest)
        n = len(json.loads(body)["data"]) if body else 0
        print(f"{tag:55s} {period:10s} {n:6d}", flush=True)


def universe() -> set[int]:
    """Every CIK that appears in any CY2023-CY2025 duration frame we pulled."""
    ciks: set[int] = set()
    for p in sorted((CACHE / "frames").glob("*.json.gz")):
        if "Q" in p.name.split("_")[-1]:
            continue
        for row in json.loads(gzip.decompress(p.read_bytes()))["data"]:
            ciks.add(row["cik"])
    return ciks


SIC_RE = re.compile(rb'"sic"\s*:\s*"([^"]*)"')
SICDESC_RE = re.compile(rb'"sicDescription"\s*:\s*"([^"]*)"')
NAME_RE = re.compile(rb'"name"\s*:\s*"([^"]*)"')
FYE_RE = re.compile(rb'"fiscalYearEnd"\s*:\s*"([^"]*)"')


def stage_sic() -> None:
    """SIC code per CIK.  Only the head of each submissions file is read."""
    out = CACHE / "sic.json"
    known = json.loads(out.read_text()) if out.exists() else {}
    ciks = sorted(universe())
    print(f"{len(ciks)} CIKs in the frame universe; {len(known)} already known", flush=True)
    for i, cik in enumerate(ciks):
        if str(cik) in known:
            continue
        url = f"https://data.sec.gov/submissions/CIK{cik:010d}.json"
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                head = resp.read(4096)
        except urllib.error.HTTPError as e:
            known[str(cik)] = {"sic": None, "err": e.code}
            time.sleep(SLEEP)
            continue
        finally:
            pass
        time.sleep(SLEEP)

        def grab(rx):
            m = rx.search(head)
            return m.group(1).decode("utf-8", "replace") if m else None

        known[str(cik)] = {
            "sic": grab(SIC_RE),
            "sicDescription": grab(SICDESC_RE),
            "name": grab(NAME_RE),
            "fye": grab(FYE_RE),
        }
        if i % 200 == 0:
            out.write_text(json.dumps(known))
            print(f"  {i}/{len(ciks)}", flush=True)
    out.write_text(json.dumps(known))
    print(f"done: {len(known)} SIC records", flush=True)


def stage_facts() -> None:
    for name, cik in COMPARATORS.items():
        dest = CACHE / "facts" / f"CIK{cik:010d}.json.gz"
        if dest.exists():
            print(f"{name:12s} cached")
            continue
        url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
        body = get(url, dest)
        print(f"{name:12s} {len(body) if body else 0} bytes", flush=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", default="all", choices=["frames", "sic", "facts", "all"])
    a = ap.parse_args()
    if a.stage in ("frames", "all"):
        stage_frames()
    if a.stage in ("facts", "all"):
        stage_facts()
    if a.stage in ("sic", "all"):
        stage_sic()


if __name__ == "__main__":
    sys.exit(main())
