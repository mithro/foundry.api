import json, pathlib, re, collections
idx = json.loads(pathlib.Path("tmp/idx.json").read_text())
IDS = [s["id"] for s in idx["shuttles"]]
P = pathlib.Path("tmp/shuttles")

host = collections.Counter(); bad = []
for sid in IDS:
    for pr in json.loads((P/f"{sid}.json").read_text())["projects"]:
        r = pr["repo"].strip()
        m = re.match(r"https?://(?:www\.)?([^/]+)/([^/]+)/([^/#?]+)", r)
        host[m.group(1) if m else "UNPARSEABLE"] += 1
        if not m: bad.append(r)
print("Hosts in the repo field:")
for h, n in host.most_common():
    print(f"  {h:28s} {n:>5,}")
if bad:
    print("\nUnparseable samples:", bad[:5])
