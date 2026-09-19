import json, urllib.request, pathlib, time
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36",
      "Accept": "application/json"}
def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()

idx = json.loads(get("https://index.tinytapeout.com/"))
pathlib.Path("tmp/idx.json").write_bytes(json.dumps(idx).encode())
out = pathlib.Path("tmp/shuttles")
for s in idx["shuttles"]:
    f = out / f"{s['id']}.json"
    if not f.exists():
        f.write_bytes(get(f"https://index.tinytapeout.com/{s['id']}.json"))
        time.sleep(0.2)
print(f"{len(idx['shuttles'])} shuttles on disk")
# how complete is the repo field?
miss = tot = 0
for s in idx["shuttles"]:
    for pr in json.loads((out / f"{s['id']}.json").read_text())["projects"]:
        tot += 1
        if not pr.get("repo"): miss += 1
print(f"{tot:,} project records, {miss} with no repo field ({miss/tot*100:.2f}%)")
