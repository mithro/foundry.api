#!/usr/bin/env -S uv run --no-project python
"""One table of the named foundry peer group, in each company's own reporting
currency, with every ratio derived in front of you.

Figures for SEC filers come from ``tools/foundry_peers.py`` (which reads the
SEC's XBRL ``companyfacts``); figures for the companies that do not file with
the SEC -- X-FAB (Euronext Paris), Vanguard (TWSE), Powerchip (TWSE), Silex
(Nasdaq Stockholm prospectus) and Saiwei/SWAYSURE (Shenzhen) -- are
transcribed here from the filings named in the ``source`` field, and every one
of those is quoted in ``resources/demand/semiconductor-margins.md``.

Ratios are currency-invariant, so no conversion is needed to compare them.
The USD column exists only to show relative size and states its rate.

    uv run tools/peer_table.py
"""

from __future__ import annotations

# Rates used only for the size column.  ECB annual average reference rates
# (https://data-api.ecb.europa.eu/service/data/EXR/A.<CCY>.EUR.SP00.A),
# retrieved 2026-09-25; TWD from each issuer's own convenience translation.
FX = {  # units of local currency per USD
    "USD": (1.0, "n/a"),
    "TWD": (31.370, "the issuers' own 20-F convenience rate at 2025-12-31"),
    "SEK": (
        11.0663058823529 / 1.1299831372549,
        "ECB 2025 annual averages EUR/SEK 11.0663 and EUR/USD 1.12998",
    ),
    "CNY": (
        7.787469921875 / 1.08238046875,
        "ECB 2024 annual averages EUR/CNY 7.78747 and EUR/USD 1.08238",
    ),
}

# revenue, ebit, assets, ppe, equity, capex, dda -- all in the unit named.
PEERS = [
    dict(
        name="TSMC", kind="pure-play foundry (leading edge)", fy=2025, ccy="TWD",
        unit=1e6, revenue=3_809_054.3, ebit=1_936_091.7, gross=2_281_294.0,
        assets=7_932_842.5, ppe=3_691_840.9, equity=5_355_038.7,
        capex=1_272_410.5, dda=679_684.0 + 8_412.4,
        source="Form 20-F for FY2025, filed 2026-04-16, accn 0001628280-26-025362",
    ),
    dict(
        name="TSMC", kind="pure-play foundry (leading edge)", fy=2024, ccy="TWD",
        unit=1e6, revenue=2_894_307.7, ebit=1_322_053.0, gross=1_624_353.6,
        assets=6_691_764.7, ppe=3_234_980.1, equity=4_244_266.5,
        capex=956_006.5, dda=653_610.5 + 9_186.1,
        source="Form 20-F for FY2024, filed 2025-04-17, accn 0001193125-25-083423",
    ),
    dict(
        name="UMC", kind="pure-play foundry (mature node)", fy=2025, ccy="TWD",
        unit=1e3, revenue=237_553_199, ebit=43_948_688, gross=68_906_499,
        assets=567_274_863, ppe=271_395_296, equity=365_824_997,
        capex=47_744_896, dda=56_427_377 + 2_831_540,
        source="Form 20-F for FY2025, filed 2026-04-30, accn 0001193125-26-193757",
    ),
    dict(
        name="UMC", kind="pure-play foundry (mature node)", fy=2024, ccy="TWD",
        unit=1e3, revenue=232_302_584, ebit=51_612_570, gross=75_654_080,
        assets=560_168_955, ppe=279_059_037, equity=365_450_098,
        capex=88_543_595, dda=45_472_102 + 2_695_564,
        source="Form 20-F for FY2024, filed 2025-04-24, accn 0001193125-25-092142",
    ),
    dict(
        name="GlobalFoundries", kind="pure-play foundry (mature node)", fy=2025,
        ccy="USD", unit=1e6, revenue=6_791, ebit=797, gross=1_690,
        assets=17_141, ppe=7_223, equity=11_928, capex=722, dda=1_135,
        source="Form 20-F for FY2025, accn 0001709048-26-000022",
    ),
    dict(
        name="GlobalFoundries", kind="pure-play foundry (mature node)", fy=2024,
        ccy="USD", unit=1e6, revenue=6_750, ebit=-214, gross=1_651,
        assets=16_799, ppe=7_762, equity=10_776, capex=625, dda=1_370,
        source="Form 20-F for FY2024, accn 0001709048-25-000024",
    ),
    dict(
        name="Tower Semiconductor", kind="specialty pure-play foundry", fy=2025,
        ccy="USD", unit=1e3, revenue=1_566_104, ebit=194_172, gross=363_854,
        assets=3_322_290, ppe=1_463_056, equity=2_919_287, capex=444_425,
        dda=303_112,
        source="Form 20-F for FY2025, accn 0001178913-26-002318",
    ),
    dict(
        name="Tower Semiconductor", kind="specialty pure-play foundry", fy=2024,
        ccy="USD", unit=1e3, revenue=1_436_122, ebit=191_314, gross=339_442,
        assets=3_080_485, ppe=1_286_622, equity=2_653_318, capex=436_153,
        dda=266_279,
        source="Form 20-F for FY2024, accn 0001178913-25-001537",
    ),
    dict(
        name="X-FAB Silicon Foundries", kind="specialty pure-play foundry",
        fy=2025, ccy="USD", unit=1e3, revenue=870_255, ebit=76_425,
        gross=None, assets=1_946_985, ppe=1_220_272, equity=1_053_305,
        capex=204_129, dda=120_402,
        source="X-FAB Annual Report 2025 (Euronext Paris), pp. 1069-1221 of the "
               "pdftotext extraction; consolidated IFRS statements",
    ),
    dict(
        name="X-FAB Silicon Foundries", kind="specialty pure-play foundry",
        fy=2024, ccy="USD", unit=1e3, revenue=816_383, ebit=85_543,
        gross=None, assets=1_906_713, ppe=1_144_620, equity=1_022_794,
        capex=509_467, dda=103_386,
        source="X-FAB Annual Report 2025, comparative column",
    ),
    dict(
        name="Vanguard International Semiconductor",
        kind="pure-play foundry (mature node)", fy=2025, ccy="TWD", unit=1e6,
        revenue=48_591, ebit=7_773, gross=13_654, assets=200_469, ppe=113_869,
        equity=83_590, capex=63_978, dda=8_552,
        source="VIS consolidated balance sheets, statements of comprehensive "
               "income and cash flows as of and for the year ended 2025-12-31, "
               "published on the company's investor site",
    ),
    dict(
        name="Powerchip (PSMC), nine months",
        kind="pure-play foundry (mature node)", fy=2025, ccy="TWD", unit=1e3,
        revenue=34_234_871, ebit=-5_240_729, gross=-2_331_326,
        assets=178_685_624, ppe=122_004_420, equity=82_000_187,
        capex=None, dda=None,
        source="PSMC consolidated financial statements: income statement is the "
               "nine months ended 2025-09-30 (Q3 2025 review report); balance "
               "sheet is the 2025-12-31 comparative column in the Q1 2026 "
               "review report",
    ),
    dict(
        name="SkyWater Technology", kind="specialty pure-play foundry (US)",
        fy=2025, ccy="USD", unit=1e3, revenue=442_139, ebit=-2_576,
        gross=86_928, assets=733_907, ppe=511_720, equity=187_819,
        capex=24_335, dda=35_670,
        source="Form 10-K for FY2025, accn 0001819974-26-000009; reconciles with "
               "LN-7 (518,540 + 215,367 = 733,907 of segment assets)",
    ),
    dict(
        name="Silex Microsystems (group)", kind="pure-play MEMS foundry",
        fy=2025, ccy="SEK", unit=1e6, revenue=1_385, ebit=368, gross=None,
        assets=2_246, ppe=942 + 369, equity=1_433, capex=195, dda=125,
        source="IPO prospectus approved by Finansinspektionen 2026-04-27, "
               "diary no. 25-37533, pp. 103-107",
    ),
    dict(
        name="Silex Microsystems (group)", kind="pure-play MEMS foundry",
        fy=2024, ccy="SEK", unit=1e6, revenue=1_226, ebit=339, gross=None,
        assets=2_265, ppe=825 + 415, equity=1_394, capex=78, dda=117,
        source="same prospectus, comparative column",
    ),
    dict(
        name="Saiwei / SWAYSURE group (Silex's then parent)",
        kind="MEMS foundry group building a second fab", fy=2024, ccy="CNY",
        unit=1.0, revenue=1_204_715_636.91, ebit=-254_276_329.43,
        gross=1_204_715_636.91 - 781_790_496.19, assets=7_011_337_774.25,
        ppe=1_799_636_378.42 + 891_261_115.57, equity=5_389_163_787.63,
        capex=None, dda=None,
        source="北京赛微电子股份有限公司 2024 年年度报告 (Beijing SWAYSURE 2024 "
               "annual report), published 2025-03-20, consolidated statements",
    ),
    dict(
        name="Amkor Technology", kind="outsourced assembly and test", fy=2025,
        ccy="USD", unit=1e3, revenue=6_707_981, ebit=467_385, gross=938_599,
        assets=8_136_309, ppe=3_870_808, equity=4_471_106, capex=904_614,
        dda=642_008,
        source="Form 10-K for FY2025, accn 0001047127-26-000014",
    ),
    dict(
        name="onsemi", kind="IDM", fy=2025, ccy="USD", unit=1e5 * 10,
        revenue=5_995_400_000 / 1e6, ebit=84_200_000 / 1e6,
        gross=1_983_900_000 / 1e6, assets=12_524_100_000 / 1e6,
        ppe=3_369_000_000 / 1e6, equity=7_673_300_000 / 1e6,
        capex=341_200_000 / 1e6, dda=686_000_000 / 1e6,
        source="Form 10-K for FY2025, accn 0001097864-26-000006 (MUSD)",
    ),
    dict(
        name="Texas Instruments", kind="IDM", fy=2025, ccy="USD", unit=1e6,
        revenue=17_682, ebit=6_023, gross=10_083, assets=34_585, ppe=12_320,
        equity=16_273, capex=4_550, dda=None,
        source="Form 10-K for FY2025, accn 0000097476-26-000059",
    ),
    dict(
        name="Analog Devices", kind="IDM", fy=2025, ccy="USD", unit=1e3,
        revenue=11_019_707, ebit=2_932_496, gross=6_773_478,
        assets=47_992_712, ppe=3_315_696, equity=33_815_755, capex=533_552,
        dda=None,
        source="Form 10-K for FY ended 2025-11-01, accn 0000006281-25-000153",
    ),
    dict(
        name="Intel", kind="IDM turned foundry", fy=2025, ccy="USD", unit=1e6,
        revenue=52_853, ebit=-2_214, gross=18_375, assets=211_429,
        ppe=105_414, equity=114_281, capex=14_646, dda=None,
        source="Form 10-K for FY2025, accn 0000050863-26-000011",
    ),
    dict(
        name="NVIDIA", kind="fabless (contrast)", fy=2025, ccy="USD", unit=1e6,
        revenue=130_497, ebit=81_453, gross=97_858, assets=111_601,
        ppe=6_283, equity=79_327, capex=None, dda=1_864,
        source="Form 10-K for FY ended 2025-01-26, accn 0001045810-25-000023",
    ),
    dict(
        name="AMD", kind="fabless (contrast)", fy=2025, ccy="USD", unit=1e6,
        revenue=34_639, ebit=3_694, gross=17_152, assets=76_926, ppe=2_312,
        equity=62_999, capex=974, dda=None,
        source="Form 10-K for FY ended 2025-12-27, accn 0000002488-26-000018",
    ),
]


def main() -> None:
    hdr = (
        f"{'Company':38} {'FY':>5} {'ccy':>4} {'revenue':>14} {'EBIT':>13} "
        f"{'EBIT%':>8} {'assets':>14} {'turn':>7} {'ROA':>8} {'PP&E/rev':>9} "
        f"{'capex%':>8} {'D&A%':>7}"
    )
    print(hdr)
    print("-" * len(hdr))
    rows = []
    for p in PEERS:
        r, e, a = p["revenue"], p["ebit"], p["assets"]
        margin = e / r
        turn = r / a
        roa = e / a
        ppe_rev = p["ppe"] / r if p["ppe"] is not None else None
        capex = p["capex"] / r if p["capex"] is not None else None
        dda = p["dda"] / r if p["dda"] is not None else None
        rows.append((p, margin, turn, roa))
        print(
            f"{p['name'][:38]:38} {p['fy']:>5} {p['ccy']:>4} {r:>14,.1f} "
            f"{e:>13,.1f} {margin*100:>7.2f}% {a:>14,.1f} {turn:>6.3f}x "
            f"{roa*100:>7.2f}% "
            + (f"{ppe_rev:>8.3f}x " if ppe_rev is not None else f"{'--':>9} ")
            + (f"{capex*100:>7.2f}% " if capex is not None else f"{'--':>8} ")
            + (f"{dda*100:>6.2f}%" if dda is not None else f"{'--':>7}")
        )

    print("\nArithmetic, written out, for the FY2025 pure-play foundries:\n")
    for p, margin, turn, roa in rows:
        if p["fy"] != 2025 or "foundry" not in p["kind"]:
            continue
        u = {1e6: "m", 1e3: "k", 1.0: ""}.get(p["unit"], "")
        print(f"  {p['name']} FY{p['fy']}  [{p['source']}]")
        print(f"    operating margin = {p['ebit']:,.1f} / {p['revenue']:,.1f}"
              f" = {margin*100:.2f}%   ({p['ccy']}{u})")
        print(f"    asset turnover   = {p['revenue']:,.1f} / {p['assets']:,.1f}"
              f" = {turn:.4f}x")
        print(f"    EBIT / assets    = {p['ebit']:,.1f} / {p['assets']:,.1f}"
              f" = {roa*100:.2f}%")
        print(f"      check margin x turnover = {margin:.6f} x {turn:.6f}"
              f" = {margin*turn*100:.2f}%")
        if p["ppe"] is not None:
            print(f"    PP&E / assets    = {p['ppe']:,.1f} / {p['assets']:,.1f}"
                  f" = {p['ppe']/p['assets']*100:.2f}%")
        if p["capex"] is not None:
            print(f"    capex / revenue  = {p['capex']:,.1f} /"
                  f" {p['revenue']:,.1f} = {p['capex']/p['revenue']*100:.2f}%")
        if p["equity"]:
            print(f"    EBIT / equity    = {p['ebit']:,.1f} /"
                  f" {p['equity']:,.1f} = {p['ebit']/p['equity']*100:.2f}%")
        rate, note = FX[p["ccy"]]
        print(f"    revenue in USD   = {p['revenue']*p['unit']:,.0f} {p['ccy']}"
              f" / {rate:.4f} = USD {p['revenue']*p['unit']/rate/1e6:,.0f} m"
              f"   [rate: {note}]")
        print()

    # Rank the FY2025 pure-play foundries.
    print("NOTE: the Powerchip row pairs a NINE-MONTH income statement with a")
    print("      year-end balance sheet, because PSMC's full-year 2025 statements")
    print("      were not obtainable.  Annualising the nine months by 4/3 gives")
    print(f"      EBIT {-5_240_729 * 4 / 3:,.0f} and EBIT/assets"
          f" {-5_240_729 * 4 / 3 / 178_685_624 * 100:.2f}%, and revenue"
          f" {34_234_871 * 4 / 3:,.0f} and turnover"
          f" {34_234_871 * 4 / 3 / 178_685_624:.3f}x.\n")
    print("FY2025 pure-play and specialty foundries ranked by operating margin:")
    pool = [(m, t, roa, p) for p, m, t, roa in rows
            if p["fy"] == 2025 and "foundry" in p["kind"]]
    pool.append((314 / 1385, 1385 / 2246, 314 / 2246,
                 dict(name="Silex, single-company view (LNI-17)")))
    for m, t, roa, p in sorted(pool, reverse=True):
        print(f"  {m*100:7.2f}%  turnover {t:.3f}x  EBIT/assets {roa*100:6.2f}%"
              f"   {p['name']}")

    print("\nSame group ranked by return on assets:")
    for m, t, roa, p in sorted(pool, key=lambda x: -x[2]):
        print(f"  {roa*100:7.2f}%  = margin {m*100:6.2f}% x turnover {t:.3f}x"
              f"   {p['name']}")


if __name__ == "__main__":
    main()
