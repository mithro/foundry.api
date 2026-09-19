"""Repeat participation on Tiny Tapeout shuttles, keyed on GitHub username.

Identity key = the owner segment of the project's `repo` URL, lower-cased
(GitHub usernames are case-insensitive for identity).
"""
import json, pathlib, re, collections

idx = json.loads(pathlib.Path("tmp/idx.json").read_text())
SH = idx["shuttles"]
IDS = [s["id"] for s in SH]
P = pathlib.Path("tmp/shuttles")
BRINGUP = {"tt03p5","ttihp0p1","ttihp0p2","ttihp0p3","ttihp0p4","ttgf0p1","ttgf0p2","ttgf0p3"}

OWNER = re.compile(r"(?:https?://(?:www\.)?github\.com/|git@github\.com:)([^/]+)/", re.I)

def owner(repo):
    m = OWNER.match(repo.strip())
    return m.group(1).lower() if m else None

def build(exclude=frozenset()):
    shuttles = collections.defaultdict(set)   # user -> {shuttle ids}
    designs  = collections.Counter()          # user -> design count
    skipped = 0
    for sid in IDS:
        if sid in exclude: continue
        for pr in json.loads((P/f"{sid}.json").read_text())["projects"]:
            o = owner(pr["repo"])
            if o is None:
                skipped += 1; continue
            shuttles[o].add(sid); designs[o] += 1
    return shuttles, designs, skipped

def table(title, shuttles, designs, nsh):
    n = len(shuttles)
    tot_part = sum(len(v) for v in shuttles.values())
    tot_des = sum(designs.values())
    print(f"\n{'='*78}\n{title}\n  {n:,} distinct GitHub accounts | {tot_part:,} account-shuttle "
          f"participations | {tot_des:,} designs | {nsh} shuttles\n{'='*78}")
    c = collections.Counter(len(v) for v in shuttles.values())
    print(f"  {'shuttles':>8} {'accounts':>9} {'% accts':>8} {'cum %':>7} {'participations':>15} {'% of them':>10}")
    cum = 0.0
    for k in sorted(c):
        pc = c[k]/n*100; cum += pc
        print(f"  {k:>8} {c[k]:>9,} {pc:>7.2f}% {cum:>6.2f}% {k*c[k]:>15,} {k*c[k]/tot_part*100:>9.2f}%")
    rep = sum(v for k,v in c.items() if k>1)
    repp = sum(k*v for k,v in c.items() if k>1)
    print(f"\n  accounts on >1 shuttle      : {rep:,} of {n:,} = {rep/n*100:.1f}%")
    print(f"  participations by repeaters : {repp:,} of {tot_part:,} = {repp/tot_part*100:.1f}%")
    print(f"  mean shuttles per account   : {tot_part/n:.3f}   mean designs: {tot_des/n:.3f}")
    vals = sorted((len(v) for v in shuttles.values()), reverse=True)
    for pct in (1,5,10,20):
        k = max(1, round(n*pct/100))
        print(f"  top {pct:>2}% of accounts hold   : {sum(vals[:k])/tot_part*100:5.1f}% of participations")
    # Gini on participations
    s = sorted(len(v) for v in shuttles.values())
    cumw = sum((i+1)*x for i, x in enumerate(s))
    gini = (2*cumw)/(len(s)*sum(s)) - (len(s)+1)/len(s)
    print(f"  Gini (participations)       : {gini:.3f}")
    return c

sh_all, de_all, skipped = build()
print(f"(records with no parseable GitHub owner, excluded: {skipped})")
table("ALL 28 SHUTTLES — keyed on GitHub username", sh_all, de_all, len(IDS))

sh_m, de_m, _ = build(exclude=BRINGUP)
table("EXCLUDING the 8 process bring-up / port runs", sh_m, de_m, len(IDS)-len(BRINGUP))

print("\n" + "="*78 + "\nTOP 20 ACCOUNTS BY DISTINCT SHUTTLES (all 28)\n" + "="*78)
for o, s in sorted(sh_all.items(), key=lambda kv: (-len(kv[1]), -de_all[kv[0]]))[:20]:
    print(f"  {o:28s} {len(s):>3} shuttles   {de_all[o]:>4} designs")
