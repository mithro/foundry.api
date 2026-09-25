#!/usr/bin/env -S uv run --no-project python
"""Return-on-assets arithmetic for Silex Microsystems AB (publ).

Every input is a figure printed in the IPO prospectus approved by
Finansinspektionen on 2026-04-27, diary number 25-37533 (the consolidated
statement of profit or loss on p. 103, the consolidated balance sheet on
pp. 105-106, and the consolidated statement of cash flows on p. 107).

Run from the repository root::

    uv run tools/silex_returns.py
"""

from __future__ import annotations

# MSEK, as printed in the prospectus.  The 2022 column is not in the
# prospectus; the prospectus prints 2023, 2024, 2025 and Q1 2026/2025.
NET_SALES = {2023: 1095, 2024: 1226, 2025: 1385}
TOTAL_REVENUE = {2023: 1151, 2024: 1307, 2025: 1443}
OPERATING_PROFIT = {2023: 276, 2024: 339, 2025: 368}
ADJUSTED_EBIT = {2023: 276, 2024: 355, 2025: 397}
EBITDA = {2023: 384, 2024: 456, 2025: 493}
PROFIT_FOR_PERIOD = {2023: 214, 2024: 273, 2025: 269}
DANDA = {2023: 108, 2024: 117, 2025: 125}
CAPEX = {2023: 111, 2024: 78, 2025: 195}  # "Investment in tangible fixed assets"

TOTAL_ASSETS = {2022: None, 2023: 2349, 2024: 2265, 2025: 2246}
NON_CURRENT_ASSETS = {2023: 1519, 2024: 1248, 2025: 1331}
EQUITY = {2023: 1458, 2024: 1394, 2025: 1433}
NET_DEBT = {2023: 195, 2024: 16, 2025: 101}

# Tangible fixed assets, owned, as printed (buildings and land + machinery and
# other technical facilities + equipment/tools/fixtures + construction in
# progress).  Right-of-use assets are shown separately.
PPE_OWNED = {
    2023: 401 + 368 + 17 + 35,
    2024: 426 + 348 + 15 + 36,
    2025: 439 + 314 + 20 + 169,
}
ROU = {2023: 412, 2024: 415, 2025: 369}

# Interim / point figures
Q1_2026 = dict(net_sales=375, operating_profit=128, total_assets=2377,
               equity=1526, net_debt=14)


def pct(x: float) -> str:
    return f"{x * 100:.2f}%"


def main() -> None:
    print("Silex Microsystems AB (publ) -- consolidated, IFRS, MSEK")
    print("Source: Finansinspektionen prospectus register, diary no. 25-37533,")
    print("approved 2026-04-27.  Income statement p. 103, balance sheet")
    print("pp. 105-106, cash flow p. 107.\n")

    header = (f"{'':38}" + "".join(f"{y:>10}" for y in (2023, 2024, 2025)))
    print(header)
    rows = [
        ("Net sales", NET_SALES),
        ("Total revenue", TOTAL_REVENUE),
        ("Operating profit (EBIT)", OPERATING_PROFIT),
        ("Adjusted EBIT", ADJUSTED_EBIT),
        ("EBITDA", EBITDA),
        ("Profit for the period", PROFIT_FOR_PERIOD),
        ("Depreciation and amortisation", DANDA),
        ("Capex (tangible fixed assets)", CAPEX),
        ("Total assets", TOTAL_ASSETS),
        ("Non-current assets", NON_CURRENT_ASSETS),
        ("PP&E owned (excl. right-of-use)", PPE_OWNED),
        ("Right-of-use assets", ROU),
        ("Total equity", EQUITY),
        ("Interest-bearing net debt", NET_DEBT),
    ]
    for label, d in rows:
        print(f"{label:38}" + "".join(f"{d.get(y, ''):>10}" for y in (2023, 2024, 2025)))

    print("\nDERIVED -- arithmetic written out\n")
    for y in (2023, 2024, 2025):
        ns, ebit, ta, eq = NET_SALES[y], OPERATING_PROFIT[y], TOTAL_ASSETS[y], EQUITY[y]
        ppe = PPE_OWNED[y]
        ppe_rou = ppe + ROU[y]
        print(f"--- {y} ---")
        print(f"  Operating margin        = {ebit} / {ns}"
              f" = {pct(ebit / ns)}")
        print(f"  Asset turnover          = {ns} / {ta}"
              f" = {ns / ta:.4f}x")
        print(f"  Return on assets (EBIT) = {ebit} / {ta}"
              f" = {pct(ebit / ta)}")
        print(f"     check: margin x turnover = {ebit/ns:.6f} x {ns/ta:.6f}"
              f" = {pct((ebit / ns) * (ns / ta))}")
        print(f"  Return on equity (net)  = {PROFIT_FOR_PERIOD[y]} / {eq}"
              f" = {pct(PROFIT_FOR_PERIOD[y] / eq)}")
        print(f"  PP&E intensity (owned)  = {ppe} / {ns}"
              f" = {ppe / ns:.4f}x  ({pct(ppe / ta)} of total assets)")
        print(f"  PP&E intensity (+ROU)   = {ppe_rou} / {ns}"
              f" = {ppe_rou / ns:.4f}x")
        print(f"  Capex intensity         = {CAPEX[y]} / {ns}"
              f" = {pct(CAPEX[y] / ns)}")
        print(f"  D&A / net sales         = {DANDA[y]} / {ns}"
              f" = {pct(DANDA[y] / ns)}")
        print(f"  D&A / PP&E owned        = {DANDA[y]} / {ppe}"
              f" = {pct(DANDA[y] / ppe)}")
        print(f"  Capex / D&A             = {CAPEX[y]} / {DANDA[y]}"
              f" = {CAPEX[y] / DANDA[y]:.2f}x")
        print(f"  EBITDA / total assets   = {EBITDA[y]} / {ta}"
              f" = {pct(EBITDA[y] / ta)}")
        print()

    # Average-assets variants, which is how ROA is normally struck.
    print("--- ROA on average assets (2024, 2025) ---")
    for y in (2024, 2025):
        avg = (TOTAL_ASSETS[y] + TOTAL_ASSETS[y - 1]) / 2
        print(f"  {y}: average assets = ({TOTAL_ASSETS[y]} + {TOTAL_ASSETS[y-1]}) / 2"
              f" = {avg:.1f};  EBIT/avg assets = {OPERATING_PROFIT[y]} / {avg:.1f}"
              f" = {pct(OPERATING_PROFIT[y] / avg)}")
        print(f"       asset turnover on average assets = {NET_SALES[y]} / {avg:.1f}"
              f" = {NET_SALES[y] / avg:.4f}x")
    print()

    # Q1 2026 annualised
    q = Q1_2026
    print("--- Q1 2026, annualised (x4); unaudited interim ---")
    print(f"  Net sales x4     = {q['net_sales']} x 4 = {q['net_sales'] * 4}")
    print(f"  EBIT x4          = {q['operating_profit']} x 4"
          f" = {q['operating_profit'] * 4}")
    print(f"  Operating margin = {q['operating_profit']} / {q['net_sales']}"
          f" = {pct(q['operating_profit'] / q['net_sales'])}")
    print(f"  Asset turnover   = {q['net_sales'] * 4} / {q['total_assets']}"
          f" = {q['net_sales'] * 4 / q['total_assets']:.4f}x")
    print(f"  ROA (EBIT)       = {q['operating_profit'] * 4} / {q['total_assets']}"
          f" = {pct(q['operating_profit'] * 4 / q['total_assets'])}")
    print()

    # The allabolag (parent-company) view used by LNI-17.
    print("--- Reconciling LNI-17 (Silex Microsystems AB, filed Swedish accounts) ---")
    print("  LNI-17 operating profit 2025 (allabolag, single company) = 314")
    print("  Prospectus consolidated operating profit 2025            = 368")
    print(f"  Difference = 368 - 314 = {368 - 314} MSEK"
          f" = {pct((368 - 314) / 1385)} of net sales")
    print(f"  Margin on the single-company figure = 314 / 1385"
          f" = {pct(314 / 1385)}")
    print(f"  Margin on the consolidated figure   = 368 / 1385"
          f" = {pct(368 / 1385)}")
    print("  The Other segment is the group's real-estate company (Silex Properties")
    print("  AB); its revenue is reported in Other operating income, so the")
    print("  consolidated figure carries rental income that the operating company's")
    print("  own accounts pay out as rent.")
    print()

    # Utilisation headroom arithmetic.
    print("--- Utilisation headroom (prospectus p. 86 and p. 119) ---")
    print("  Stated utilisation: 'approximately 60 percent'.")
    print("  Stated headroom:    'approximately 100 percent additional revenue,")
    print("                       depending on product mix'.")
    print("  Fixed costs 2025: 54% of total expenses = 0.54 x 1,075 ="
          f" {0.54 * 1075:.0f} MSEK")
    print("  Variable costs 2025 = 1,075 -"
          f" {0.54 * 1075:.0f} = {1075 - 0.54 * 1075:.0f} MSEK")
    print("  If net sales doubled to 2,770 with fixed costs unchanged and")
    print("  variable costs scaling 1:1 with revenue:")
    var2 = (1075 - 0.54 * 1075) * 2
    fixed = 0.54 * 1075
    # other operating income held flat at 58
    rev2 = 2770 + 58
    ebit2 = rev2 - (fixed + var2)
    print(f"    total revenue = 2,770 + 58 = {rev2:.0f}")
    print(f"    total expenses = {fixed:.0f} + 2 x {1075 - fixed:.0f}"
          f" = {fixed + var2:.0f}")
    print(f"    EBIT = {rev2:.0f} - {fixed + var2:.0f} = {ebit2:.0f}")
    print(f"    EBIT margin = {ebit2:.0f} / 2,770 = {pct(ebit2 / 2770)}")
    print(f"    ROA on today's assets = {ebit2:.0f} / 2,246"
          f" = {pct(ebit2 / 2246)}")
    print("  (Illustrative only: the prospectus says the cleanroom expansion")
    print("   costs SEK 150m in 2026 plus about SEK 500m over 2027-2029, so the")
    print("   asset base would not in fact stay at 2,246.)")
    print()

    print("--- Capital raised against capital deployed ---")
    print("  Cumulative capital expenditure from founding to 2026-03-31:")
    print("    SEK 1.9 billion (prospectus p. 84, excluding the acquisition of")
    print("    Silex Properties AB).")
    print(f"  2025 net sales / cumulative capex = 1,385 / 1,900 ="
          f" {1385 / 1900:.4f}x")
    print(f"  2025 EBIT / cumulative capex      = 368 / 1,900 ="
          f" {pct(368 / 1900)}")


if __name__ == "__main__":
    main()
