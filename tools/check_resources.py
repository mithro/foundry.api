#!/usr/bin/env python3
"""Consistency checker for resources/.

Run it with:  uv run python tools/check_resources.py
With network: uv run python tools/check_resources.py --network

It exists because a set of errors in this repository sat undiscovered for days:
a claim that a page was live after it had started redirecting; a claim that a
price was unpublished when it was published; an entry left at Partial after
somebody had verified it; and an absolute quantifier ("every programme found
has been oversubscribed") contradicted by another entry in the same directory.

Each check below targets one of those failure modes.  Checks are advisory by
default; --strict makes any finding exit non-zero, for use in CI or a hook.
"""
from __future__ import annotations
import argparse, datetime, pathlib, re, sys, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
RES = ROOT / "resources"
ROOTDOCS = [ROOT / "WHY.md", ROOT / "PRINCIPLES.md"]

ENTRY_RE = re.compile(r"^#{2,4}\s+([A-Z][A-Z0-9]*)-(\d+)[.:]?\s+(.*)$", re.M)
REF_RE = re.compile(r"\b([A-Z]{2,6})-(\d+)\b")
DATE_RE = re.compile(r"\b(20\d{2}-\d{2}-\d{2})\b")
ISO_TODAY = datetime.date.today()

# Claims about live web state: these rot silently and must be re-checked.
VOLATILE = re.compile(
    r"\b(?:both live|is live|now live|still live|currently|returns? HTTP|serves? HTTP|"
    r"404s?|403s?|301s?|redirects?|is not published|are not published|not published anywhere|"
    r"cannot buy|can no longer|behind a login|behind an account|client-side|"
    r"no price (?:is )?published|publishes no)\b", re.I)
# Domains whose content moves under you.
LIVE_DOMAIN = re.compile(r"(crowdsupply\.com|platform\.chipfoundry\.io|index\.tinytapeout\.com|"
                         r"app\.tinytapeout\.com|/api/)", re.I)
# Absolute quantifiers: where the overclaims happened.
# Evidential quantifiers only.  A bare "nobody" is usually design prose in PRINCIPLES.md
# ("nobody can jump the queue") and flagging it buries the real findings.
ABSOLUTE = re.compile(r"\b(?:every (?:programme|program|company|entry|one|single)|"
                      r"all (?:programmes|programs|of them)|none of (?:them|the)|"
                      r"no \w+ has ever|the only (?:one|series|entry|programme|company)|"
                      r"never once|in every case|without exception)\b", re.I)

class Finding:
    def __init__(self, check, path, line, msg):
        self.check, self.path, self.line, self.msg = check, path, line, msg
    def __str__(self):
        rel = self.path.relative_to(ROOT) if self.path else "-"
        loc = f"{rel}:{self.line}" if self.line else str(rel)
        return f"  [{self.check}] {loc}\n      {self.msg}"

def md_files(base):
    return sorted(p for p in base.rglob("*.md"))


# resources/README.md documents the entry format using a worked example, which is
# not a real entry.  Parse entries from everything except that file.
def entry_files(base):
    return [p for p in md_files(base) if p != base / "README.md"]

def parse_entries(files):
    """id -> {path, line, title, status, dates, body}"""
    entries = {}
    for p in files:
        text = p.read_text(encoding="utf-8")
        lines = text.splitlines()
        hits = list(ENTRY_RE.finditer(text))
        for i, m in enumerate(hits):
            eid = f"{m.group(1)}-{m.group(2)}"
            start = text[:m.start()].count("\n") + 1
            end = text[:hits[i+1].start()].count("\n") + 1 if i+1 < len(hits) else len(lines)
            body = "\n".join(lines[start-1:end])
            # The canonical statuses are Verified / Partial / Lead, but entries also use
            # Owner-supplied and Derived where those are the honest description.  Accept any
            # status word; the check is that a Verification line exists at all.
            ver = re.search(r"\*\*Verification:?\*\*:?[\s\-]*\**\s*([A-Z][A-Za-z-]+)", body)
            entries.setdefault(eid, []).append({
                "path": p, "line": start, "title": m.group(3).strip(),
                "status": (ver.group(1) if ver else None),
                "dates": [datetime.date.fromisoformat(d) for d in DATE_RE.findall(body)],
                "body": body,
            })
    return entries

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stale-days", type=int, default=60,
                    help="flag volatile claims not re-checked in this many days")
    ap.add_argument("--strict", action="store_true", help="exit 1 if anything is found")
    ap.add_argument("--network", action="store_true",
                    help="re-fetch each entry's source URLs and report status")
    a = ap.parse_args()

    files = md_files(RES)
    entries = parse_entries(entry_files(RES))
    F: list[Finding] = []

    # -- C1: duplicate entry IDs ------------------------------------------------
    for eid, occ in entries.items():
        if len(occ) > 1:
            where = ", ".join(f"{o['path'].relative_to(ROOT)}:{o['line']}" for o in occ)
            F.append(Finding("C1-duplicate-id", occ[0]["path"], occ[0]["line"],
                             f"{eid} is defined {len(occ)} times: {where}"))

    # -- C2: dangling cross-references -----------------------------------------
    known = set(entries)
    prefixes = {e.split("-")[0] for e in known}
    for p in files + [d for d in ROOTDOCS if d.exists()]:
        for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith(("http", "<http", "|", ">")) and "](" not in line:
                pass  # still scan; URLs rarely contain ID-like tokens
            for m in REF_RE.finditer(line):
                ref, pre = f"{m.group(1)}-{m.group(2)}", m.group(1)
                if pre in prefixes and ref not in known:
                    F.append(Finding("C2-dangling-ref", p, n,
                                     f"cites {ref}, which is not defined anywhere"))

    # -- C3: a Lead must never be cited in WHY.md or PRINCIPLES.md --------------
    leads = {eid for eid, occ in entries.items()
             if any((o["status"] or "").lower() == "lead" for o in occ)}
    for doc in ROOTDOCS:
        if not doc.exists():
            continue
        for n, line in enumerate(doc.read_text(encoding="utf-8").splitlines(), 1):
            for m in REF_RE.finditer(line):
                ref = f"{m.group(1)}-{m.group(2)}"
                if ref in leads:
                    F.append(Finding("C3-lead-cited", doc, n,
                                     f"{ref} is an unverified Lead and must not be cited here"))

    # -- C4: every prefix in use is indexed in a README ------------------------
    readme_text = "".join((RES / f).read_text(encoding="utf-8")
                          for f in ("README.md", "demand/README.md") if (RES / f).exists())
    for pre in sorted(prefixes):
        if not re.search(rf"`{pre}(?:-\d+)?`", readme_text):
            ex = next(o for eid, occ in entries.items() if eid.startswith(pre + "-") for o in occ)
            F.append(Finding("C4-unindexed-prefix", ex["path"], ex["line"],
                             f"prefix {pre} is used but appears in no README index table"))

    # -- C5: every entry needs a Verification status and a date ----------------
    for eid, occ in entries.items():
        for o in occ:
            if o["status"] is None:
                F.append(Finding("C5-no-status", o["path"], o["line"],
                                 f"{eid} has no **Verification:** line"))
            elif (o["status"] or "").lower() != "lead" and not o["dates"]:
                # A Lead has by definition not been checked, so a date is meaningless there.
                F.append(Finding("C5-no-date", o["path"], o["line"],
                                 f"{eid} is marked {o['status']} but carries no ISO date"))

    # -- C6: volatile claims that have not been re-checked recently ------------
    for eid, occ in entries.items():
        for o in occ:
            if not VOLATILE.search(o["body"]) and not LIVE_DOMAIN.search(o["body"]):
                continue
            newest = max(o["dates"], default=None)
            if newest is None:
                continue
            age = (ISO_TODAY - newest).days
            if age > a.stale_days:
                why = "claims about live web state" if VOLATILE.search(o["body"]) else "cites a live/moving source"
                F.append(Finding("C6-stale-volatile", o["path"], o["line"],
                                 f"{eid} {why} but was last checked {newest} ({age} days ago) "
                                 f"— re-fetch before citing"))

    # -- C7: absolute quantifiers in the load-bearing summaries -----------------
    # Deliberately narrow.  Analyses are discursive and "nobody" is fine there; the
    # error this catches ("every free or subsidised programme found has been
    # oversubscribed", contradicted by OPG-2) was in hypotheses.md, which is where
    # claims get compressed into one line and lose their qualifiers.
    for p in [RES / "hypotheses.md"] + [d for d in ROOTDOCS if d.exists()]:
        for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith(">"):   # already inside a correction note
                continue
            m = ABSOLUTE.search(line)
            if m:
                F.append(Finding("C7-absolute-claim", p, n,
                                 f'absolute quantifier "{m.group(0)}" — check it against the '
                                 f"whole directory before leaving it unqualified"))

    # -- C8 (network, opt-in): do the cited URLs still resolve as claimed? -----
    if a.network:
        import urllib.request, urllib.error
        UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
        seen = {}
        for eid, occ in sorted(entries.items()):
            for o in occ:
                for url in re.findall(r"<(https?://[^>\s]+)>", o["body"])[:2]:
                    if url in seen:
                        code = seen[url]
                    else:
                        try:
                            req = urllib.request.Request(url, headers=UA, method="HEAD")
                            with urllib.request.urlopen(req, timeout=25) as r:
                                code = r.status
                        except urllib.error.HTTPError as e:
                            code = e.code
                        except Exception as e:
                            code = type(e).__name__
                        seen[url] = code
                    if code != 200:
                        F.append(Finding("C8-url-not-200", o["path"], o["line"],
                                         f"{eid}: {url} -> {code}"))

    by = collections.Counter(f.check for f in F)
    print(f"resources/: {len(files)} files, {len(entries)} entries, {len(prefixes)} ID prefixes\n")
    for check in sorted(by):
        print(f"{check}  ({by[check]})")
        for f in [x for x in F if x.check == check][:40]:
            print(f)
        if by[check] > 40:
            print(f"      … and {by[check]-40} more")
        print()
    if not F:
        print("No findings.")
    else:
        print(f"{len(F)} finding(s). C6 and C7 are advisory prompts to re-check, not errors.")
    return 1 if (F and a.strict) else 0

if __name__ == "__main__":
    sys.exit(main())
