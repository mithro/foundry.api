#!/usr/bin/env -S uv run --no-project python
"""Print a filer's recent filings of a given form type from a cached
``data.sec.gov/submissions`` JSON.

    uv run tools/list_filings.py tmp/sec/sub/CIK0001033767.json --form 20-F
"""

from __future__ import annotations

import argparse
import json
import pathlib


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--form", default="")
    ap.add_argument("--limit", type=int, default=10)
    args = ap.parse_args()
    d = json.loads(pathlib.Path(args.path).read_text())
    r = d["filings"]["recent"]
    cik = int(d["cik"])
    n = 0
    print(d.get("name"), "CIK", cik, "SIC", d.get("sic"), d.get("sicDescription"))
    for i in range(len(r["form"])):
        if args.form and r["form"][i] != args.form:
            continue
        accn = r["accessionNumber"][i]
        print(
            f"  {r['filingDate'][i]}  {r['form'][i]:8}  {accn}  "
            f"https://www.sec.gov/Archives/edgar/data/{cik}/"
            f"{accn.replace('-', '')}/{r['primaryDocument'][i]}"
        )
        n += 1
        if n >= args.limit:
            break


if __name__ == "__main__":
    main()
