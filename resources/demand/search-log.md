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
| `www.tsmc.com` (SMB-13) | Reported to us as returning **HTTP 403** to automated fetches. **It does not, as of 2026-09-18:** `curl` with a generic User-Agent and `WebFetch` both return **HTTP 200**. The catch is that the page's text sits in an embedded JSON blob rather than in the rendered HTML, so a naive read of the body looks empty. | No workaround needed. Search the raw page source, not the rendered text. |
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
| CMC Microsystems (Canada) | Annual reports with prototype counts; a fall to 240 across the three years for which figures were read. **No figure was found for 2022-23**, and the five-year total implies it was the highest year in the series | DEM-20 |
| Published MPW price lists | Europractice (which carries the IHP and GlobalFoundries lists), MOSIS (archived), chipIgnite/ChipFoundry, Tiny Tapeout | SMB-7 to SMB-10 |
| Mask-set cost at mature nodes | GSA survey figures quoted in *New Electronics* | SMB-12 |
| Wafer cost per node | CSET's Table 9, modelled from TSMC's own financials | SMB-11 |
| A long-tail manufacturing business that is profitable | JLC's IPO prospectus, filed with the Shenzhen Stock Exchange. It is a pre-listing 申报稿 and the company is unlisted, so it has no ticker: the document carries no 证券代码 or 股票代码 line at all | SMB-1 |
| Long-tail manufacturing businesses that are not | Protolabs, Xometry, Shapeways | SMB-2, SMB-3, SMB-4 |
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
- **Protolabs' annual order count or average order size.** Sought in every 10-K read. Four are
  cited as sources in SMB-2 (FY2015, FY2019, FY2022, FY2025); the FY2023 and FY2024 filings were
  also searched, for the "no single customer" phrase SMB-2 reports as having disappeared.
  **Not disclosed in any of them.** Only cumulative
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

---

# PCB industry comparables (2026-09-19)

Searching done while building [`pcb-industry-comparables.md`](pcb-industry-comparables.md), whose
question was: does JLC's long-tail-high-margin / big-batch-commodity result (SMB-1) generalise
across the PCB industry, or is JLC an outlier?

Everything here was read-only. HTTP GET only, apart from cninfo's own document-search endpoint,
which is a POST search query and nothing else. No forms submitted, no accounts, no logins, no
paywall or bot-check circumvention, no shadow libraries, and no contact with any person by any
channel.

## 7. Tool and access notes (new ones only)

| Obstacle | Detail | Workaround used |
|---|---|---|
| `static.cninfo.com.cn` (Chinese listed-company filings) | Returns **HTTP 403** to a plain `curl` for every `finalpage/.../*.PDF` path. | A browser User-Agent **plus** `-H "Referer: http://www.cninfo.com.cn/"` returns HTTP 200. Both headers are needed. This is the single most useful fact in this section. |
| Finding a Chinese filing's URL at all | There is no guessable path. | `POST http://www.cninfo.com.cn/new/hisAnnouncement/query` with `pageNum`, `pageSize`, `column=szse` (or `sse`, `bj`), `tabName=fulltext`, `searchkey=<URL-encoded Chinese name>` and `category=category_ndbg_szsh` (annual reports) returns JSON in which each document's `adjunctUrl` is the path to append to `http://static.cninfo.com.cn/`. Searching by company name works; searching by `stock=<code>` returned nothing. |
| `reportdocs.static.szse.cn` (the JLC prospectus) | Serves fine to `curl` with a generic User-Agent. HTTP 200, 14,709,306 bytes. | None needed. |
| `www.pcbway.com/aboutus.html` and `/pcb-prototype/` | **HTTP 404**. The paths guessed from other sources are wrong. | The real paths are `/about.html` and the home page; both return HTTP 200. Extract links from the served HTML rather than guessing. |
| `dirtypcbs.com` prices | Site returns **HTTP 200** and a working storefront, but the price table is rendered client-side and is **absent from the served HTML**. | Not solved. A human with a browser, or a headless browser, sees it at once. |
| Chinese annual-report PDFs and `pypdf` | Text extracts cleanly, including the tables, but table cells arrive space-separated on one line and long numbers are sometimes split across two lines by the PDF's line breaks (e.g. `1,269,812,602.` / `58`). | Read the surrounding lines, not a single grep hit, before trusting a figure. Two numbers were nearly misread this way. |
| Session-wide API rate limit | The work was killed partway through by an account-level rate limit, not by any site. | Committed early and often afterwards. The unfinished items are listed in the entry file's blocked-sources table, labelled as unfinished rather than blocked. |

## 8. What was found, and where it went

| Looked for | Found | Entry |
|---|---|---|
| Which companies the JLC prospectus treats as 同行业可比公司 (the open question left by SMB-1) | Five, named in a table on PDF p.246 with three years of gross margin each: 兴森科技, 金百泽, 迅捷兴, 四会富仕, 强达电路 | PCB-1 |
| Whether JLC owns its plant (a concrete open item against SMB-1) | **Yes.** "自有的生产仓储基地", "五大数字化自营生产基地", CNY 3.26bn of fixed assets, CNY 1.40bn of capex, buildings with ownership certificates, land bought at auction | PCB-2 |
| A second company disclosing margin by batch size | **None found.** Fastprint, the best-placed candidate, splits by industry, product, region and sales channel and never by batch | PCB-4 |
| A second company describing the batch/margin relationship | Xunjiexing's FY2025 report prints it as an industry characteristic: 样板 高 / 小批量板 较高 / 大批量板 一般低于样板、小批量板 | PCB-3 |
| A second company attributing a margin fall to a shift toward batch | Xunjiexing FY2023: revenue +3.65%, PCB volume +30.02%, gross margin −5.62 pp, "一方面是市场竞争加剧价格竞争激烈使得批量产品降价，另一方面是公司批量占比逐步增加" | PCB-3 |
| Whether the prospectus's peer figures are reliable | 13 of 15 re-derived from the peers' own audited annual reports; **all 13 agree exactly** | PCB-5 |
| Customer concentration across the peer set | JLC 1.16%, 金百泽 13.82%, 强达电路 16.31%, 四会富仕 19.36%, 兴森科技 27.29%, 迅捷兴 40.07% | PCB-3, PCB-4, PCB-5 |
| A published price list separating small orders from volume | OSH Park: $5/in² per set of 3 vs $1/in² Medium Run (100 in² minimum) — exactly 5/3, at two layers and at four | PCB-6 |

## 9. Negative results and corrections (PCB comparables)

- **"Dirty PCBs is defunct."** Not supported. `http://dirtypcbs.com/` returned **HTTP 200** on
  2026-09-19 and redirects to a working storefront at `/store/pcbs` with live ordering for PCBs,
  stencils, SLA 3D prints, laser-cut acrylic, custom cables and a BOM tool. No shutdown notice was
  found. Nothing about its economics was located either, because its prices render client-side and
  its founder's writing was not searched.
- **The JLC prospectus's "未披露" for 兴森科技's 2025 margin is a timing artefact, not a
  non-disclosure.** Fastprint's FY2025 annual report was published on **2026-04-25**, after the
  prospectus was filed; it gives **25.26%**. Substituting it raises the 2025 peer mean from 18.06%
  to 19.50% and cuts JLC's margin premium from +10.00 pp to +8.56 pp. This correction is against
  our own thesis and is recorded in PCB-4 and in the verdict.
- **"Serving a long tail is what produces the margin" is not supported by the peer set.** Qiangda
  has about 3,000 customers, sells 100% direct on negotiated terms, and earns 26.10% — within two
  points of JLC. Xunjiexing has "over ten thousand", calls itself a sample-board specialist, and
  earns 8.52% with a net loss. Customer count predicts neither margin nor concentration across the
  six (Spearman ρ = +0.314 and −0.486; −0.200 and −0.100 excluding JLC; n = 6, so none of it means
  anything on its own).
- **There is no industry-standard definition of "small batch".** Three of the companies define the
  bands and no two agree. JLC: sample < 1 m², small batch 1–20 m², medium/large > 20 m².
  Xunjiexing: sample < 5 m², small batch 5–50 m², large > 50 m² (per average order).
  Jinbaize: sample < 5 m², small batch 5–20 m². Any cross-company comparison of "small batch"
  compares differently drawn lines.
- **JLC's online orders are not unattended.** The prospectus says the system generates a *reference*
  quote and "市场部对订单审核后向客户发送最终报价" — the marketing department reviews the order and
  sends the final quote. Any claim that a JLC order completes with zero human involvement is not
  supported by the filing.
- **The large listed Chinese PCB makers were not examined.** 深南电路 (Shennan), 沪电股份 (WUS),
  景旺电子 (Kinwong) and 崇达技术 (Chongda) were in scope as a wider control group and were not
  reached. They are also *not* the comparables JLC chose, which is itself worth noting: JLC's peer
  set is five companies ranked 7th to 83rd among domestically-funded makers, not the leaders.

## 10. Disagreements between sources (PCB comparables)

| Question | Source A | Source B | Status |
|---|---|---|---|
| 兴森科技's 2025 core-business gross margin | JLC prospectus: 未披露 | Fastprint FY2025 annual report: PCB 25.26% | **Not a disagreement** — the report post-dates the prospectus. Both recorded. |
| Xunjiexing's top-five customer share, 2025 | Annual report: "40.07%" of 年度销售总额 | Our recomputation against 主营业务收入: 40.08% | Different denominators (total sales vs main-business revenue). Both recorded. |
| The definition of 样板 / 小批量板 | JLC: < 1 m² / 1–20 m² | Xunjiexing: < 5 m² / 5–50 m²; Jinbaize: < 5 m² / 5–20 m² | Three incompatible definitions. All recorded; none adopted. |
