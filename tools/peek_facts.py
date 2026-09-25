#!/usr/bin/env -S uv run --no-project python
"""Print the taxonomies, units and annual facts available in a cached
``companyfacts`` JSON.  A scratch helper for finding the right tag name for a
foreign private issuer that files under IFRS.

    uv run tools/peek_facts.py tmp/peek/tsmc.json --grep Revenue
"""

from __future__ import annotations

import argparse
import json
import pathlib


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--grep", default="")
    ap.add_argument("--list-only", action="store_true")
    args = ap.parse_args()
    d = json.loads(pathlib.Path(args.path).read_text())
    print(d["entityName"], "CIK", d["cik"])
    for tax, tags in d["facts"].items():
        print(f"-- taxonomy {tax}: {len(tags)} tags")
        for tag, body in sorted(tags.items()):
            if args.grep and args.grep.lower() not in tag.lower():
                continue
            if args.list_only:
                print(f"   {tag}")
                continue
            for unit, pts in body["units"].items():
                annual = [
                    p for p in pts
                    if p.get("form") in ("20-F", "10-K", "6-K", "40-F")
                    and p.get("fp") == "FY"
                ]
                if not annual:
                    continue
                print(f"   {tag} [{unit}]")
                for p in annual[-8:]:
                    print(
                        f"      fy={p.get('fy')} start={p.get('start','')}"
                        f" end={p.get('end')} val={p['val']:,}"
                        f" form={p.get('form')} accn={p.get('accn')}"
                    )


if __name__ == "__main__":
    main()
