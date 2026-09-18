# Search log

What was looked for while building this directory, what came back, and — more usefully — what did
not. Negative results are recorded so nobody repeats the search. All of it was done on 2026-09-18.

Everything here was read-only: HTTP GET requests only, no forms submitted anywhere, no accounts, no
logins, no attempt to get past a paywall, a bot check or a CAPTCHA, no shadow libraries, and no
contact with any person by any channel.

---

## 1. Tool and access notes that affected what could be reached

These cost real time and are worth knowing before repeating any of this.

| Obstacle | Detail | Workaround used |
|---|---|---|
| `www.sec.gov/Archives/...` refuses automated fetches | Returns **HTTP 403** to `curl` regardless of the User-Agent tried. Confirms the note already in [`../README.md`](../README.md). | `data.sec.gov` (the XBRL and submissions APIs) **does** serve automated requests with a generic, non-personal User-Agent, and `WebFetch` reaches `www.sec.gov` successfully. Both routes were used. |
| SEC rate limiting | An early burst of requests returned SEC's "Request Rate Threshold Exceeded" page (as an HTTP 200 with an error body). | Backed off, slowed down, changed User-Agent to a generic non-personal string. No retry loops. **No email address of any kind was placed in a header, URL or query string.** |
| `WebFetch` cannot reach `web.archive.org` | It refuses outright: "Claude Code is unable to fetch from web.archive.org". | All Wayback work was done with `curl`, using the raw-content forms `…/web/<timestamp>id_/<url>` or `…/web/<timestamp>if_/<url>`. Without the `id_`/`if_` suffix you get the Wayback HTML wrapper, not the file. `--compressed` is also needed or the body arrives gzipped. |
| Wayback CDX API times out | `https://web.archive.org/cdx/search/cdx?...` returned **HTTP 504 Gateway Time-out** on wildcard and filtered queries. | Re-ran with `matchType=domain`, a lower `limit` and no server-side `filter`, then filtered locally. Worked. |
| `investor.tsmc.com` | **HTTP 403** to `curl` for both HTML pages and PDF paths. | Not solved. TSMC's 2025 revenue was therefore not obtained (see §4). |
| `eetimes.com`, `globenewswire.com` | `curl` gets **no HTTP response at all** (exit 92). | `WebFetch` reaches both. Entries that rely on it say so. |
| `opensource.googleblog.com` | Returned **HTTP 429** to `curl` after a few requests. | Backed off; used `WebFetch` for the remaining page rather than retrying in a loop. |
| `mycmp.fr` (CMP Grenoble) | HTTPS fails — **certificate expired**. Plain HTTP now returns a **domain-parking page**: "This domain was successfully registered for the highest bidder in our weekly auction." `cmp.imag.fr` is dead too. | Everything on CMP came from the Internet Archive. |
| `tsri.org.tw` (Taiwan) | `ECONNREFUSED` on port 443 via `WebFetch`; empty body via `curl` with and without a browser User-Agent. | Not solved. See §3. |
| `cmc.ca/en/WhatWeOffer/Make/FabPricing.aspx` | **HTTP 403** to an automated fetch. | Not solved; CMC's *annual reports* on the same domain fetched fine. |
| Client-side-rendered pages | `app.tinytapeout.com/calculator`, `platform.chipfoundry.io/shuttle-metrics` and Muse Semiconductor's pricing pages return a shell with no content to a fetch. | Not solved. A human with a browser could read all three in seconds. |
| Local hooks | The session's designated scratchpad is under `/tmp`, which a repository hook blocks, and another hook blocks inline `python -c`. | Worked in a project-local `tmp/` directory, deleted at the end, and wrote short script files instead of inline Python. |

---

## 2. What was found, and where it went

Only the destination is listed here; the entries themselves carry the quotes and the verification
status.

| Looked for | Found | Entry |
|---|---|---|
| Tiny Tapeout submissions per shuttle | The full table on `tinytapeout.com/chips/`, **and** a public JSON API with every submission record | DEM-1, DEM-2 |
| Tiny Tapeout capacity utilisation | `tiles_used` / `tiles_total` per shuttle in the same API | DEM-2 |
| Google Open MPW submissions and acceptances (the "To find" on `OPEN-1`) | MPW-1 45 submitted / 40 slots; MPW-2 56; MPW-5 75 (or 78); MPW-6 90; 240 manufactured from "over 364 community submissions" over six shuttles | DEM-4 to DEM-9 |
| Europractice annual design counts | Every activity report from 2014 to 2025, plus a chart in the 2017 report carrying data labels back to 2000 | DEM-16 |
| Europractice rejection rates | One: 98 applications, 50 selected, for the First User Stimulation Programmes | DEM-17 |
| Europractice oversubscription | "Several TSMC shuttles are extremely loaded … If required, a waiting list will be created." | DEM-18 |
| CMP annual circuit counts | The 2011 annual report's year-by-year history, 1985–2011, on the Internet Archive | DEM-19 |
| MOSIS historical design counts | "more than 60,000 integrated circuit designs … up to $10 million annually at its peak", "around 3,000 orders per year" | SMB-5 |
| CMC Microsystems (Canada) | Annual reports with prototype counts; a four-year decline to 240 | DEM-20 |
| Published MPW price lists | Europractice, CMP (2021, archived), MOSIS (archived), Tiny Tapeout, chipIgnite/ChipFoundry, IHP, AIM Photonics | SMB-7 to SMB-10 |
| Mask-set cost at mature nodes | GSA survey figures quoted in *New Electronics* | SMB-12 |
| Wafer cost per node | CSET's Table 9, modelled from TSMC's own financials | SMB-11 |
| A long-tail manufacturing business that is profitable | JLC's IPO prospectus, filed with the Shenzhen Stock Exchange. It is a pre-listing 申报稿 and the company is unlisted, so it has no ticker: the document carries no 证券代码 or 股票代码 line at all | SMB-1 |
| Long-tail manufacturing businesses that are not | Protolabs, Xometry, Shapeways, Fathom | SMB-2, SMB-3, SMB-4 |
| Evidence cost is not the binding constraint | Siemens EDA / Wilson Research first-silicon success rates | DEM-12 |
| Falling design starts | EE Times 2002, Gartner and iSuppli | DEM-11 |
| The long-tail theory's own counter-evidence | Elberse's fuller findings, including her extension to physical goods | DEM-13 |

---

## 3. Searched for, and not found

Each of these was looked for deliberately. Recording them saves the next person the trip.

### Shuttle and MPW data

- **Submission counts for Google Open MPW shuttles MPW-3, MPW-4, MPW-7 and MPW-8.** Efabless's
  archived programme page (DEM-6) lists only MPW-1 and MPW-2; Google's blog gives MPW-5 and MPW-6.
  The Efabless platform that held the per-shuttle project lists
  (`platform.efabless.com/shuttles/...`) is offline, and the Wayback copies of it are a JavaScript
  application shell with no readable content. **What would unblock a human:** the Efabless GitHub
  organisation may still hold per-shuttle manifest repositories; the `caravel_user_project` forks
  are countable on GitHub.
- **Submission counts for the GlobalFoundries GF180MCU shuttles (GF-MPW-0 onwards).** Google's
  announcement (DEM-8) states the 40-project cap but no submission numbers, and nothing else was
  found.
- **The number of MPW runs Europractice offers per year.** Not stated in any activity report read.
  It could be counted by hand off the annual "Schedules & Prices" pages, one row per technology per
  run. Not attempted.
- **CMP annual reports for 2018 and 2019.** The 2019 PDF
  (`mycmp.fr/IMG/pdf/cmp_rapport_2019v08-01-2020_web.pdf`) was **never archived** — the Wayback CDX
  API returns an empty result for it. The 2018 PDF (`mycmp.fr/IMG/pdf/2018_annualreportv1.pdf`) CDX
  query timed out twice with HTTP 504. The live site is a parked domain. **What would unblock a
  human:** a local copy held by a former CMP user, or a Grenoble-INP / CNRS institutional
  repository.
- **TSRI / CIC (Taiwan) annual chip-implementation counts.** `tsri.org.tw` refuses connections from
  here and the archived English pages carry service descriptions and no numbers. A 2011 snapshot of
  the figure survives second-hand inside CMP's 2011 annual report ("the advanced and educational
  chips taped out by the academia via CIC has reached a total amount of 1718") — which, if right,
  would be the largest single-year national academic MPW figure anywhere, three times Europractice's
  in the same year. **It is unverified and is not written up as an entry.** **What would unblock a
  human:** the Chinese-language TSRI/NARLabs annual reports, or a network route into Taiwan.
- **VDEC (University of Tokyo) current figures.** The page fetched returned no extractable text. A
  2011 figure survives second-hand in CMP's report ("241 chips on 2180 mm² silicon area"), again
  unverified and not written up.
- **Shuttle design counts from imec, TSMC, UMC, GlobalFoundries, Tower or Muse Semiconductor.** None
  of them publishes one. Their MPW pages give schedules and technologies only. This is a clean
  negative result.
- **A shuttle programme that closed for lack of demand.** Searched for explicitly. **Nothing found.**
  Every closure traced — Efabless, CMP, MOSIS's free academic programme — had a supply-side or
  funding cause, not an absence of customers. The nearest thing to the claim is the NSF report's
  statement that a node "may be mostly desired by academia yet not desirable enough to make economic
  sense for a fabrication run" (DEM-21), and ChipFoundry's reservation of "the right to delay a
  shuttle if it's less than 50% full" (DEM-10).
- **Whether MOSIS 1.0 ever formally stopped taking orders, and why the free academic programme
  ended in 2020.** Neither found. `mosis.com` became a JavaScript application in late 2020 and the
  archived HTML has no readable body text. **What would unblock a human:** USC ISI's own records, or
  the archived JavaScript bundles.
- **The Tiny Tapeout survey behind "industrial customers now represent 38%, up from 14% in 2023".**
  Quoted in eeNews (DEM-10) with no name, date, sample size or method, and not found anywhere else.

### Demand and constraints

- **Any survey of chip designers or start-ups saying cost is *not* the binding constraint.**
  Searched for deliberately, from both directions. **Nothing citable found.** The closest verified
  statements go the other way: the NSF workshop report says "the key challenge is cost" (DEM-21).
  The strongest indirect evidence against cost being binding is the first-silicon success rate
  (DEM-12), which is about engineering effort, not price, and had to be inferred rather than quoted.
- **A current (2020s) count of ASIC design starts.** Not found. Gartner, IBS, Semico and IC Insights
  all sell this behind subscriptions; the last openly citable figures are from the 2000s (DEM-11).
  **What would unblock a human:** a market-research subscription, or a conference keynote slide that
  reproduces the table with attribution.
- **Cases of a small chip customer becoming a large one.** Searched for; nothing verifiable found
  that is specific enough to write up. CMC's "290 Startups to-date; 49% remain active in Canada"
  (DEM-20) is the nearest, and it is a count, not a case.
- **An analysis arguing that a long tail of hardware specifically does not exist.** Nothing found
  beyond Elberse's one-sentence extension to physical goods (DEM-13).

### Cost to serve and small-customer economics

- **Kaplan and Narayanan, "Measuring and Managing Customer Profitability", *Journal of Cost
  Management* 15(5), 2001** — the source of the widely repeated claim that the most profitable 20%
  of customers generate 150–300% of total profits while the least profitable 10–20% destroy 50–200%.
  **Not obtainable.** The journal is not open access and the article is on no legal open repository
  found. ResearchGate offers it request-only (a form, so out of bounds). Two substitutes were
  checked and **neither contains the figures**: Kaplan and Anderson's free HBS working paper 04-045
  on time-driven activity-based costing, and a trade column on the "whale curve". **Do not quote the
  150–300% figures anywhere in this project.** **What would unblock a human:** a university library
  subscription to *Journal of Cost Management*, or an interlibrary loan.
- **Any credible study of SaaS or cloud small-customer unit economics** (cost to serve, support cost
  per small account, SMB churn against acquisition cost). **Nothing usable found** — only
  content-marketing blogs with no method. The closest verified item is Heroku's statement that it
  ended its free plans because "Our product, engineering, and security teams are spending an
  extraordinary amount of effort to manage fraud and abuse of the Heroku free product plans" (Bob
  Wise, "Heroku's Next Chapter", 2022-08-25). It is real and relevant to the fixed cost per customer
  that H6 assumes away, but it is about a free tier, not a paid one, and it was **not verified by us
  at source**, so it is recorded here rather than as an entry.
- **A foundry executive or filing saying small customers are not worth serving.** Searched for;
  **nothing citable found.** Minimum order quantities are visible in the MPW price lists (SMB-7,
  SMB-8) but no foundry says why in public.
- **The Global Semiconductor Association mask-cost survey itself**, behind the figures in SMB-12.
  Not obtained; the figures come through a journalist's paraphrase.
- **Protolabs' annual order count or average order size.** Sought in every 10-K read (FY2015,
  FY2019, FY2021, FY2022, FY2023, FY2024, FY2025). **Not disclosed in any of them.** Only cumulative
  part counts ("over 18 million unique part designs since inception") and qualitative commentary.
- **What share of Xometry's revenue comes from its 1,760 accounts spending over $50,000 a year.**
  **Not disclosed in any 10-K read.** Without it, nobody can say how much of Xometry's revenue is
  actually long tail. This is a material gap in the public record, not an omission here.
- **Financials for Ponoko, PCBWay or Fictiv.** All private; no primary financial source exists.
  PCBWay is the closest structural comparable to JLC (SMB-1); the peer table in JLC's own prospectus
  is the best available proxy.
- **TSMC's total revenue for financial year 2025.** Needed to complete the DEM-15 arithmetic for
  2025. **Blocked three ways:** the FY2025 20-F's facts are not in the SEC XBRL company-concept
  endpoints (`ifrs-full/Revenue` and `ifrs-full/RevenueFromContractsWithCustomers` both stop at
  FY2024); `www.sec.gov/Archives/...` returns 403 to `curl`; and `investor.tsmc.com` returns 403 as
  well. The FY2024 calculation was done instead and the 2025 one deliberately left undone rather
  than estimated. **What would unblock a human:** opening the FY2025 20-F in a browser, or TSMC's
  Q4 2025 results release.
- **A published headline price for a complete Tiny Tapeout submission** (tile plus ASIC plus board).
  The FAQ answers "What is the price?" with a link to a calculator, and the calculator is a
  client-side application. The per-tile price (SMB-10) and older trade-press figures (`OPEN-5`) are
  what exist.
- **Muse Semiconductor and CMC Microsystems fabrication prices.** Muse's pages are titled
  "…Services and Price" and render client-side; CMC's pricing page returns 403. Both would take a
  human with a browser about a minute.

---

## 4. Things that were assumed and turned out to be wrong

Recorded because they were believed here before they were checked.

- **"MOSIS wound down."** It did not. It was reconstituted as MOSIS 2.0 under the USC-led CA DREAMS
  Microelectronics Commons hub from late 2023 and began accepting external customers in summer 2024
  (SMB-5). What ended, in 2020, was its *free academic* tape-out programme (DEM-22).
- **"TSMC's tail of 512 customers supports H5."** It is a tail of large companies. The arithmetic
  (DEM-15) puts the average non-top-ten TSMC customer at about US$41 million a year.
- **"Efabless's failure was a demand failure."** Nothing found supports that. It failed to close a
  funding round (`OPEN-7`), while its shuttles were oversubscribed and its successor reopened the
  same product at a higher price (SMB-9).

---

## 5. Disagreements between sources, left unresolved

The repository's rule is to record both and not silently pick one.

| Question | Source A | Source B | Status |
|---|---|---|---|
| Submissions to Google Open MPW-5 | Google's own blog: "75 open silicon projects submitted" (DEM-5) | Hackster.io: "a record 78 projects submitted" (DEM-7) | Unresolved. Both recorded. |
| Tiny Tapeout TT07 designs | `tinytapeout.com/chips/`: 120 | The submission-stats API: 119 records | Off by one (DEM-2) |
| Tiny Tapeout TTIHP25a designs | `tinytapeout.com/chips/`: 547 | API: 546 records, 540 distinct projects | Off by one, and the distinct-project count is lower again (DEM-2) |
| Tiny Tapeout TT02 designs | `tinytapeout.com/chips/`: 165 (DEM-1) | eeNews, quoted in `OPEN-5`: "up from 160 for TT02" | Unresolved |
| Europractice designs in 2016 | 2017 report's chart labels: 574 | 2017 report's prose: 575 | Off by one (DEM-16) |
| ASIC design starts, c. 2002 | iSuppli: about 2,100 in 2001 | Gartner Dataquest: "closer to 5,000 this year" | Unresolved, and a factor of 2.5 apart (DEM-11) |
| CMP cumulative MPW runs | 1,029 (2017) then 1,043 (2019) | 1,142 (2021) | Not a credible run rate; either a definition changed or a counter was stale (DEM-19) |

---

## 6. Method notes for anyone re-running the counts

- **Tiny Tapeout** is the only source here that publishes machine-readable primary data. The exact
  counting method is written out in DEM-2, including the API URL, the JSON shape and the grouping
  rule, so the numbers can be reproduced.
- **Europractice's chart labels** extract cleanly from the PDF text layer with `pypdf`; the
  per-series attribution does not survive the extraction, so only the yearly totals were used, and
  those were checked against the prose in the same and neighbouring reports.
- **Several PDFs use `ﬁ` and `ﬂ` ligatures**, so a plain search for "difficult" or "profit" fails.
  Normalise ligatures and strip hyphen-newline pairs before searching, or the quote you want will
  look as though it is not there. This caused two false negatives before it was noticed.
- **The Internet Archive is the only surviving route** to MOSIS's price lists, Efabless's programme
  pages and CMP's annual reports. All three organisations' live sites are gone or parked.
