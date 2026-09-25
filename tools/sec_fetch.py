#!/usr/bin/env -S uv run --no-project python
"""Fetch SEC XBRL "frames" data and per-filer SIC codes into a local cache.

Used by ``tools/semiconductor_margins.py`` to build the distribution of
operating margin, asset turnover and capital intensity across every SEC filer
in a given SIC code.

No API key is needed.  ``data.sec.gov`` asks for a declared ``User-Agent`` and
a rate limit of 10 requests per second; both are honoured below.  No personal
identifier of any kind is sent.

Usage (from the repository root)::

    uv run tools/sec_fetch.py --cache tmp/sec

Everything is cached to disk, so a second run costs no network traffic.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
import time
import urllib.error
import urllib.request

USER_AGENT = "foundry-api-research/1.0"
MIN_INTERVAL = 0.12  # seconds between requests -> < 10 req/s

# Income-statement / cash-flow concepts use *duration* frames (CY2025).
DURATION_CONCEPTS = [
    "Revenues",
    "RevenueFromContractWithCustomerExcludingAssessedTax",
    "OperatingIncomeLoss",
    "GrossProfit",
    "PaymentsToAcquirePropertyPlantAndEquipment",
    "DepreciationDepletionAndAmortization",
]

# Balance-sheet concepts use *instantaneous* frames (CY2025Q4I).
INSTANT_CONCEPTS = [
    "Assets",
    "PropertyPlantAndEquipmentNet",
    "StockholdersEquity",
]

_last_call = [0.0]


def _get(url: str) -> bytes:
    wait = MIN_INTERVAL - (time.monotonic() - _last_call[0])
    if wait > 0:
        time.sleep(wait)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=90) as fh:
            return fh.read()
    finally:
        _last_call[0] = time.monotonic()


def fetch_json(url: str, path: pathlib.Path) -> dict | None:
    """Fetch ``url`` into ``path`` unless already cached.  None on 404."""
    if path.exists():
        if path.stat().st_size == 0:
            return None
        return json.loads(path.read_text())
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        body = _get(url)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            path.write_bytes(b"")
            return None
        raise
    path.write_bytes(body)
    return json.loads(body)


def frame_url(taxonomy: str, concept: str, period: str) -> str:
    return (
        f"https://data.sec.gov/api/xbrl/frames/{taxonomy}/{concept}/USD/{period}.json"
    )


def fetch_frames(cache: pathlib.Path, years: list[int]) -> None:
    for year in years:
        for concept in DURATION_CONCEPTS:
            period = f"CY{year}"
            fetch_json(
                frame_url("us-gaap", concept, period),
                cache / "frames" / f"{concept}_{period}.json",
            )
            print(f"frame {concept} {period}", file=sys.stderr)
        for concept in INSTANT_CONCEPTS:
            period = f"CY{year}Q4I"
            fetch_json(
                frame_url("us-gaap", concept, period),
                cache / "frames" / f"{concept}_{period}.json",
            )
            print(f"frame {concept} {period}", file=sys.stderr)


def frame_ciks(cache: pathlib.Path, concept: str, period: str) -> set[int]:
    path = cache / "frames" / f"{concept}_{period}.json"
    if not path.exists() or path.stat().st_size == 0:
        return set()
    data = json.loads(path.read_text())
    return {row["cik"] for row in data["data"]}


def fetch_submissions(cache: pathlib.Path, ciks: list[int]) -> None:
    total = len(ciks)
    for i, cik in enumerate(sorted(ciks), 1):
        padded = f"{cik:010d}"
        path = cache / "sub" / f"CIK{padded}.json"
        if path.exists():
            continue
        fetch_json(f"https://data.sec.gov/submissions/CIK{padded}.json", path)
        if i % 200 == 0:
            print(f"submissions {i}/{total}", file=sys.stderr)


def fetch_companyfacts(cache: pathlib.Path, ciks: list[int]) -> None:
    for cik in ciks:
        padded = f"{cik:010d}"
        path = cache / "facts" / f"CIK{padded}.json"
        if path.exists():
            continue
        fetch_json(
            f"https://data.sec.gov/api/xbrl/companyfacts/CIK{padded}.json", path
        )
        print(f"companyfacts {padded}", file=sys.stderr)


# Named peers whose full fact set we want, regardless of frame membership.
NAMED_PEERS = {
    1046179: "Taiwan Semiconductor Manufacturing Company (TSMC), 20-F, IFRS",
    1033767: "United Microelectronics Corporation (UMC), 20-F, IFRS",
    1709048: "GLOBALFOUNDRIES Inc., 10-K",
    928876: "Tower Semiconductor Ltd, 20-F",
    1819974: "SkyWater Technology, Inc., 10-K",
    1047127: "Amkor Technology, Inc., 10-K",
    1097864: "ON Semiconductor Corporation (onsemi), 10-K",
    97476: "Texas Instruments Incorporated, 10-K",
    6281: "Analog Devices, Inc., 10-K",
    1045810: "NVIDIA Corporation, 10-K",
    2488: "Advanced Micro Devices, Inc., 10-K",
    50863: "Intel Corporation, 10-K",
    827054: "Microchip Technology Incorporated, 10-K",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default="tmp/sec")
    ap.add_argument("--years", default="2025,2024")
    ap.add_argument("--skip-submissions", action="store_true")
    args = ap.parse_args()

    cache = pathlib.Path(args.cache)
    years = [int(y) for y in args.years.split(",")]

    fetch_frames(cache, years)

    # SIC codes are only needed for filers that could possibly make the cut:
    # those that reported both an operating income and a balance sheet.
    wanted: set[int] = set()
    for year in years:
        oi = frame_ciks(cache, "OperatingIncomeLoss", f"CY{year}")
        assets = frame_ciks(cache, "Assets", f"CY{year}Q4I")
        wanted |= oi & assets
    print(f"filers with both OperatingIncomeLoss and Assets: {len(wanted)}",
          file=sys.stderr)

    if not args.skip_submissions:
        fetch_submissions(cache, sorted(wanted))

    fetch_companyfacts(cache, sorted(NAMED_PEERS))
    fetch_submissions(cache, sorted(NAMED_PEERS))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
