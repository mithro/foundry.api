"""Is the designs-per-account distribution long-tailed?  And how much is the TT team itself?"""
import json, pathlib, re, collections, math

idx = json.loads(pathlib.Path("tmp/idx.json").read_text())
IDS = [s["id"] for s in idx["shuttles"]]
P = pathlib.Path("tmp/shuttles")
OWNER = re.compile(r"(?:https?://(?:www\.)?github\.com/|git@github\.com:)([^/]+)/", re.I)

sh = collections.defaultdict(set); de = collections.Counter()
for sid in IDS:
    for pr in json.loads((P/f"{sid}.json").read_text())["projects"]:
        m = OWNER.match(pr["repo"].strip())
        if m:
            o = m.group(1).lower(); sh[o].add(sid); de[o] += 1

# Accounts belonging to the programme itself / its founders, documented in the repo:
#   tinytapeout = the project's own GitHub organisation
#   mattvenn    = Matt Venn, founder (Zero to ASIC Course)
#   urish       = Uri Shaked, Wokwi founder and TT collaborator
ORG = {"tinytapeout"}
FOUNDERS = {"mattvenn", "urish"}

tot_p = sum(len(v) for v in sh.values()); tot_d = sum(de.values())
print("HOW MUCH OF THE 'REPEAT PARTICIPATION' IS THE PROGRAMME ITSELF?")
for label, keys in (("the tinytapeout org account", ORG),
                    ("+ the two named founders", ORG | FOUNDERS)):
    p = sum(len(sh[k]) for k in keys if k in sh)
    d = sum(de[k] for k in keys if k in sh)
    print(f"  {label:30s} {len(keys)} accounts -> {p:>3} participations ({p/tot_p*100:4.1f}%), "
          f"{d:>3} designs ({d/tot_d*100:4.1f}%)")
rep_accounts = [k for k,v in sh.items() if len(v) > 1]
rep_p = sum(len(sh[k]) for k in rep_accounts)
core = [k for k in rep_accounts if len(sh[k]) >= 9]
print(f"\n  accounts on >=9 shuttles: {len(core)} -> {sum(len(sh[k]) for k in core)/tot_p*100:.1f}% of all participations")
print(f"  of those {len(core)}, {len(set(core) & (ORG|FOUNDERS))} are the org or a founder")

print("\n" + "="*78)
print("IS IT A POWER LAW?  designs per account, excluding the org account")
print("="*78)
xs = sorted((v for k, v in de.items() if k not in ORG), reverse=True)
n = len(xs)
print(f"  n = {n:,} accounts, {sum(xs):,} designs, max = {xs[0]}, mean = {sum(xs)/n:.3f}")

def alpha_ks(data, kmin):
    d = [x for x in data if x >= kmin]
    if len(d) < 10: return None
    a = 1 + len(d)/sum(math.log(x/(kmin-0.5)) for x in d)
    # KS distance against the discrete power law
    zeta = sum(k**-a for k in range(kmin, 20000))
    d_sorted = sorted(d)
    ks = 0.0
    for i, x in enumerate(d_sorted):
        emp = (i+1)/len(d_sorted)
        cdf = 1 - sum(k**-a for k in range(kmin, int(x)+1))/zeta
        ks = max(ks, abs(emp - (1-cdf)))
    return a, ks, len(d)

print(f"  {'k_min':>6} {'alpha':>7} {'KS D':>8} {'n>=k_min':>9} {'% of accts':>11}")
for kmin in (1,2,3,4,5,6,8,10):
    r = alpha_ks(xs, kmin)
    if r:
        a, ks, m = r
        print(f"  {kmin:>6} {a:>7.3f} {ks:>8.4f} {m:>9,} {m/n*100:>10.2f}%")

print("\n  Interpretation: a power law needs a SMALL KS distance.  Large D at k_min=1-2")
print("  means the bulk of the distribution is not power-law; it only starts to fit")
print("  once the one-and-two-design accounts (the overwhelming majority) are dropped.")

print("\n" + "="*78)
print("SHAPE, stated plainly")
print("="*78)
c = collections.Counter(xs)
for k in sorted(c)[:8]:
    print(f"  {k:>3} design(s): {c[k]:>5,} accounts ({c[k]/n*100:5.2f}%)")
big = sum(v for k, v in c.items() if k >= 9)
print(f"  >=9 designs: {big:>5,} accounts ({big/n*100:5.2f}%)")
s = sorted(xs); cum = sum((i+1)*x for i, x in enumerate(s))
print(f"\n  Gini (designs per account, org excluded): {(2*cum)/(len(s)*sum(s)) - (len(s)+1)/len(s):.3f}")
