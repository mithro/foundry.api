# ChipFoundry (`CF`)

ChipFoundry.io — legally **UmbraLogic Technologies LLC**, a California-governed LLC — is the only
open-entry shuttle operator that is **unsubsidised** and, on the repository owner's account,
**deliberately investor-free**. Europractice has EU grants (`FUND-1`), MOSIS had federal money
(`FUND-4`), CMC has Canadian federal and provincial money (`FUND-5`), IHP's open MPW is a German
research institute's programme (`OPG-10`), Tiny Tapeout is a reseller that buys its wafer space
from other people (`PAY-5`), and wafer.space is the repository owner's own company (`PAY-9`).
ChipFoundry is the closest thing that exists to the business this project proposes: somebody
selling small slices of a mature-node wafer, at a published price, to strangers, and trying to
make the sums work without a grant.

So its record matters more than its size. This file collects every number about it we could find.

**Read this before any number below.** ChipFoundry publishes **no** revenue, no headcount, no
funding statement, no blog and no press releases. It has never filed with the SEC (`CF-5`). Every
figure here is either (a) a field from its own public, unauthenticated API, (b) a number read off a
dated Internet Archive capture of its own front page, or (c) an arithmetic derivation from those,
labelled as such. The API fields are **mutable and have been revised downwards after the fact**
(`CF-6`), and ChipFoundry does not define them anywhere. Nothing in this file is an audited or
self-reported financial figure, because no such figure exists.

**A correction this file makes to the rest of the repository.** Several files treat ChipFoundry as
"Efabless's successor" and the $9,750 → $14,950 move as a price rise by a continuing programme. That
is wrong on both counts, and `CF-1`, `CF-2`, `CF-3` and `CF-8` set out why: ChipFoundry was a
**separate new company** that launched its **own** product ("ChipCreate") on its **own** shuttles
("CC2509", "CC2511") at **$14,950 from its very first public page**, five months *before* it bought
the chipIgnite name. The $14,950 was never a rise; it was a new company's opening price, which
happens to be 53% above the price a dead company used to charge.

---

## Corporate history

### CF-1. ChipFoundry came into public existence in April 2025, six weeks after Efabless suspended operations — three independent registries agree

- **Sources:**
  - RDAP registry record for `chipfoundry.io` (Identity Digital, the `.io` registry operator):
    <https://rdap.identitydigital.services/rdap/domain/chipfoundry.io>
  - RDAP registry record for `umbralogic.com` (Verisign):
    <https://rdap.verisign.com/com/v1/domain/umbralogic.com>
  - GitHub REST API, organisation record: <https://api.github.com/orgs/chipfoundry>
  - Internet Archive CDX index for `chipfoundry.io`:
    `https://web.archive.org/cdx/search/cdx?url=chipfoundry.io&matchType=domain&output=text&fl=timestamp,original,statuscode&collapse=urlkey`
  - Internet Archive captures of `efabless.com` for the shutdown notice.
- **Verification:** **Verified 2026-09-20.** All four fetched directly with `curl` and read.
- **What it says:**

  | Event | Date | Source |
  |---|---|---|
  | Efabless homepage still normal, no notice | 2025-03-02 | Wayback `20250302002252` |
  | "**Shutdown Notice**: Due to funding challenges, Efabless has shut down operations until further notice." on the Efabless homepage | by 2025-03-11 | Wayback `20250311202950` |
  | `umbralogic.com` registered | **2025-04-09T18:19:59Z** | Verisign RDAP |
  | `chipfoundry.io` registered | **2025-04-15T21:03:43.737Z** | Identity Digital RDAP |
  | GitHub organisation `chipfoundry` created | **2025-04-21T17:36:51Z** | GitHub API |
  | First Internet Archive capture of `chipfoundry.io` | **2025-04-23T08:08:21Z** | Wayback CDX |

  For contrast, `efabless.com` was registered **2013-01-29T22:54:44Z** (Verisign RDAP) and the
  GitHub organisation `efabless` was created **2013-01-10T20:05:53Z** (GitHub API).
- **DERIVED (arithmetic written out):** the gap from the first archived Efabless shutdown notice
  (2025-03-11) to the registration of `umbralogic.com` (2025-04-09) is **29 days**; to the first
  archived ChipFoundry page (2025-04-23), **43 days**.
- **Bears on:**
  - **Corporate history (corrects the repository).** The repository's working picture has been
    "chipIgnite → ChipFoundry", a rename or continuation. It was not. A **new** legal entity, a
    **new** domain, a **new** GitHub organisation and a **new** brand all appeared inside two weeks
    in April 2025, after Efabless stopped.
  - **The owner's account, and where the public record does and does not support it.** The owner's
    account is that ChipFoundry "was launched *after* Efabless, by similar founders, with a similar
    structure and a similar offering, at a higher price … a separate new company operating in
    parallel/afterwards, not a rename", and that it "then acquired Efabless's assets and the
    chipIgnite name at a later stage." **Everything in that account except "in parallel" is
    corroborated here and in `CF-2`, `CF-3` and `CF-4`.** *Separate new company*: yes, three
    registries agree. *Similar founders*: yes (`CF-4`). *Similar offering at a higher price*: yes
    (`CF-2`, `CF-8`). *Acquired the assets and the name later*: yes, five months later (`CF-3`).
    **"In parallel" is the one part we could not verify and the public record points the other way**:
    every public trace of ChipFoundry begins *after* Efabless's shutdown notice, not alongside it.
    A company can of course be formed before it registers a domain, and we could not reach a state
    incorporation record (see the blocked list), so the formation date of UmbraLogic Technologies
    LLC itself remains unknown. What can be said is that **nothing public existed before
    2025-04-09**.
- **Used in:** `CF-2`, `CF-3`; the corrections listed at the foot of this file.
- **Caveats:**
  - A domain registration date is not an incorporation date. The LLC may predate it.
  - The Wayback Machine's *first* capture is a lower bound on a site's age, not its birthday; a site
    can exist unarchived. But here the first capture is eight days after the domain was registered,
    which leaves little room.
  - Efabless's homepage carried the shutdown banner by 2025-03-11; the exact day it went up is
    between 2025-03-02 and 2025-03-11. Tiny Tapeout's own announcement is dated **2025-03-01**
    (`CF-10`), so 2025-03-01 is the better date for the shutdown itself.

### CF-2. ChipFoundry's launch product was "ChipCreate", not chipIgnite — its own shuttles CC2509 and CC2511, at $14,950 on day one

- **Source:** Internet Archive capture of `https://chipfoundry.io/`, `20250423080821` (the earliest
  capture that exists), fetched in raw (`id_`) form:
  <https://web.archive.org/web/20250423080821id_/https://chipfoundry.io/>
- **Verification:** **Verified 2026-09-20**, fetched with `curl --compressed` and read in full.
- **What it says**, verbatim from that page:
  - The product is "**Chip Create**", "The Platform for Bringing Your Custom Chip Ideas to Life",
    "**$14,950 per tapeout**", including "Pre-built SoC design with RISC-V subsystem and
    peripherals", "Up to 15mm² of die space with a standard I/O ring", "38 fully -configurable I/Os",
    "Option of 100 QFN-packaged parts or Bare Die", "Plug and play development board", "Complete
    RTL-to-GDSII Open Source design flow".
  - A second product, "**Chip Discover**", "Coming Soon", "Ideal for students, makers, university
    courses" — "FPGA-base development board", "Free access to design tools", "**Option to
    manufacture your project with Tiny Tapeout**".
  - The schedule is headed "**Chip Create Shuttle Schedule**" and lists two shuttles, "**CC2509**"
    and "**CC2511**", with "Tapeout Date **September 16, 2025** / **November 11, 2025**" and
    "Delivery Date **February 14, 2026** / **April 11, 2026**".
  - The enquiry form's shuttle dropdown offers "CC2509 CC2511 CC26xx".
  - The footer reads "**© 2025 UmbraLogic Technologies LLC**".
  - The word "chipIgnite" appears **once**, in a paragraph of body copy — "look no further than
    ChipIgnite" — which by the next capture (2025-06-13) has been rewritten to "look no further than
    **ChipCreate**". It reads like copy pasted from the founders' previous employer and then
    corrected.
- **Bears on:**
  - **Corporate history (corrects the repository).** The "chipIgnite" brand was **not** ChipFoundry's
    at launch. Its shuttles were "CC" — ChipCreate — and were renamed "CI" only after the asset
    purchase (`CF-3`). ChipFoundry's own API still carries the scar: `CI2509`'s description is
    `"September 2025 MPW Shuttle (formerly CC2509)"` (`CF-6`).
  - **H6 (context).** The price was $14,950 on the **first day the company was visible**, before it
    owned anything of Efabless's. Whatever explains the gap to Efabless's $9,750, it is not a
    mid-programme price rise.
- **Used in:** `CF-3`, `CF-8`.
- **Caveats:** a marketing page is a statement of intent, not of trade. Nobody had bought anything
  on 2025-04-23.

### CF-3. The Efabless asset purchase came five months after launch, in September 2025, and the shuttles were renamed CC → CI in the same fortnight

- **Sources:**
  - Internet Archive captures of `https://chipfoundry.io/`: `20250904153017` (before) and
    `20250928020108` (after).
  - Internet Archive CDX index for `efabless.com`, which shows the homepage returning **301** from
    capture `20250910013043` onward and **404** from `20251204084757` onward.
  - The live redirect target, <https://chipfoundry.io/efabless> (which is where `https://efabless.com/`
    now lands).
  - GitHub REST API repository listing for the `chipfoundry` organisation.
- **Verification:** **Verified 2026-09-20.** Captures and the live page fetched with `curl` and read;
  the redirect confirmed with `curl -L -w '%{url_effective}'`.
- **What it says:**
  - The **2025-09-04** capture of the ChipFoundry front page still says "September MPW Shuttle is
    Open", "Shuttle Status for **CC2509**", schedule "CC2509 CC2511".
  - The **2025-09-28** capture says, as a banner: "**We've acquired the Efabless assets to build on
    the respected chipIgnite brand. Our mission to democratize silicon design continues, now with a
    more streamlined and powerful platform.**" The navigation has become "chipIgnite Overview", the
    schedule is now "**CI2511 CI2604 CI2606**", and the enquiry dropdown lists "CC2511 To Be
    Determined CC2604 CC2606 CC2609 CC2611".
  - `efabless.com` stopped serving its own site and began redirecting between **2025-09-02**
    (last 200) and **2025-09-10** (first 301). It now lands on `chipfoundry.io/efabless`, whose
    entire body is: "**Umbralogic Technologies LLC, doing business as ChipFoundry, has acquired the
    assets of Efabless Corporation.** We invite you to explore our new solutions and services:
    https://chipfoundry.io https://chipfoundry.io/chipignite".
  - **The rebrand can be dated to a fortnight from a third source.** ChipFoundry's YouTube channel
    feed (`https://www.youtube.com/feeds/videos.xml?channel_id=UCKBHanCVU1lDAEggUOYsBvg`) carries a
    video "**ChipCreate: Custom Silicon for Everyone**" published **2025-09-03** and a video
    "**chipIgnite - Custom Silicon for Everyone**" published **2025-09-18** — the same title, the
    same length of description, two weeks apart, with the product name swapped. The channel is now
    `@chipIgnite`; the handle it used until then, `@ChipCreate`, is the one linked from the
    2025-09-28 homepage capture and now returns HTTP 404.
  - **What demonstrably moved**, from the GitHub organisation listing: three repositories under
    `chipfoundry` have creation dates that **predate the organisation itself** and are Efabless's
    former flagship tools — `volare` (created **2022-03-18**, the SKY130/GF180MCU PDK version
    manager), `openlane2` (created **2023-01-16**, 374 stars), and `nix-eda` (created
    **2024-05-09**). Repositories are transferred with their history; these were transferred, not
    forked. ChipFoundry also holds `caravel`, `caravel_user_project`, `caravel_board`,
    `caravel_mgmt_soc_litex`, `open_pdks`, `ipm` and the `EF_*` / `CF_*` IP repositories.
- **DERIVED:** launch (2025-04-23) to acquisition banner (between 2025-09-04 and 2025-09-28) is
  **about five months**. The first ChipFoundry shuttle taped out 2025-09-12 (`CF-7`), i.e. **the
  company had already manufactured a shuttle under its own name before it owned the chipIgnite
  brand**.
- **Bears on:**
  - **Corporate history (corrects the repository).** `resources/analyses/industry-parallels.md`
    calls ChipFoundry the "successor to Efabless" and records both sites as "live". Neither is now
    accurate: ChipFoundry preceded the purchase as an independent going concern, and `efabless.com`
    is a redirect to a one-paragraph notice.
  - **H6 (context).** The acquisition looks like the purchase of a **brand and a toolchain** out of
    a failed company by people who had already restarted the business without them.
- **Used in:** `CF-8`, and the corrections at the foot of this file.
- **Caveats:**
  - No purchase price, no asset schedule and no date of completion is public anywhere we looked. The
    only public statement of the transaction is the single sentence quoted above.
  - "Assets of Efabless Corporation" is not defined. Whether it included the customer book, the
    pending designs, or the liabilities to customers whose chips were in the fab (`CF-10`) is not
    stated.

### CF-4. The founders are Efabless people: DiCorpo, Kassem and Patel, and the whole visible company is four named individuals

- **Sources:**
  - <https://chipfoundry.io/about> ("About Chip Foundry"), fetched live.
  - ChipFoundry's own public platform API: <https://platform.chipfoundry.io/api/v1/community>
  - Tiny Tapeout, "ChipFoundry announced as Tiny Tapeout sponsor", 2025-05-10:
    <https://tinytapeout.com/news/chipfoundry-sponsor/>
  - Efabless Corporation's Form D, SEC accession `0002039822-24-000001` (`CF-5`).
- **Verification:** **Verified 2026-09-20**, all fetched with `curl` and read.
- **What it says:**
  - The about page: "**ChipFoundry is owned by Umbralogic Technologies LLC**, a team of
    semiconductor industry veterans committed to removing barriers in custom chip development."
    Leadership: "**Jeff DiCorpo — CEO**", "**Mohamed Kassem — CTO**", "**Samir Patel — CSO**".
  - "Our Story": "**Born from the success of open source silicon, which created a thriving community
    of over 10,000 members and facilitated more than 600 fabricated chip designs**, ChipFoundry is
    our way of taking it even further." (The 10,000 members and 600 designs are Efabless's numbers,
    claimed as heritage.)
  - Tiny Tapeout, 2025-05-10, in its own words: "**Rising from the ashes of Efabless, Jeff DiCorpo
    and Mohamed Kassem have started ChipFoundry, offering their first SKY130 tapeout in
    September.**"
  - The `community` API returns **six** records in total, of which two are ChipFoundry staff —
    `{"name":"Jeff D","username":"jdicorpo","profile_title":"CEO","organization_name":"ChipFoundry"}`
    and `{"name":"Marwan Abbas","profile_title":"Head of Customer Engineering",
    "organization_name":"ChipFoundry"}` — one is the ChipFoundry organisation itself, and three are
    customers (an individual, AIST, and one unnamed).
  - **Mohamed Kassem was an Efabless executive officer and director**: he is listed as such on
    Efabless's 2024 Form D (`CF-5`). Jeff DiCorpo is *not* on that filing.
- **DERIVED:** the largest headcount that can be evidenced from public sources is **four named
  people** (DiCorpo, Kassem, Patel, Abbas). That is a floor, not an estimate; ChipFoundry publishes
  no headcount and has no careers page.
- **Bears on:**
  - **H6 (context, and this is the number that matters for the verdict).** If the business is run by
    something close to a handful of people, then the cost base against which `CF-11`'s derived
    revenue has to be judged is small — but so is the capacity to absorb a bad shuttle.
  - **Corporate history.** "Similar founders" in the owner's account is confirmed: the CTO of the
    new company was an executive officer and director of the old one.
- **Used in:** `CF-16`.
- **Caveats:**
  - The `community` API is an opt-in directory, not a staff list. Six records is the size of the
    *directory*, not of the company or its customer base.
  - Samir Patel's and Marwan Abbas's prior employment was not verified; only Kassem's is documented
    here, from the Form D.

### CF-5. ChipFoundry has never filed with the SEC — and Efabless's only filing shows it raised exactly $2.5m from exactly one investor, five months before it died

- **Sources:**
  - SEC EDGAR full-text search API, `https://efts.sec.gov/LATEST/search-index?q=%22UmbraLogic%22`
    and `…q=%22ChipFoundry%22` and `…q=%22Efabless%22`.
  - SEC EDGAR company search, `https://www.sec.gov/cgi-bin/browse-edgar?company=umbralogic&type=D&action=getcompany`.
  - SEC EDGAR submissions API, <https://data.sec.gov/submissions/CIK0002039822.json>.
  - Efabless Corp Form D, accession `0002039822-24-000001`:
    <https://www.sec.gov/Archives/edgar/data/2039822/000203982224000001/primary_doc.xml>
- **Verification:** **Verified 2026-09-20.** All fetched with `curl` and a declared non-email
  User-Agent. `efts.sec.gov` serves automated requests once a User-Agent is set;
  `www.sec.gov/cgi-bin/browse-edgar` also answered.
- **What it says:**
  - Full-text search for **"UmbraLogic"**: `"total":{"value":0}`. For **"ChipFoundry"**:
    `"total":{"value":0}`. The company-name search for `umbralogic` returns "**No matching
    companies.**"
  - The same search for **"Efabless"** returns `"total":{"value":21}`, the first hit being
    "**efabless Corp (CIK 0002039822)**", with further hits at SkyWater, QuickLogic, Knowles and
    Cypress. **The search plainly works**; the zero for UmbraLogic is a real zero.
  - `efabless Corp` has filed **exactly one** document with the SEC, a **Form D** filed
    **2024-10-08**, state of incorporation **Delaware**, address 969 Industrial Road, Suite I,
    San Carlos, CA. Its content, verbatim from the XML:
    `<dateOfFirstSale><value>2024-09-27</value></dateOfFirstSale>`,
    `<totalOfferingAmount>2500000</totalOfferingAmount>`,
    `<totalAmountSold>2500000</totalAmountSold>`, `<totalRemaining>0</totalRemaining>`,
    `<hasNonAccreditedInvestors>false</hasNonAccreditedInvestors>`,
    `<totalNumberAlreadyInvested>1</totalNumberAlreadyInvested>`. Signed by **Michael Wishart, Chief
    Executive Officer**, 2024-10-05.
  - The related persons on that filing are **Michael Wishart** (Executive Officer, Director),
    **Mohamed Kassem** (Executive Officer, Director), **Lucio Lanza** (Director), **Jack Hughes**
    (Director) and **Jeremy Hitchcock** (Director).
- **DERIVED:** from the single sale on **2024-09-27** to the shutdown notice (2025-03-01, `CF-10`)
  is **about five months**. $2,500,000 against `PAY-8`'s derived 2024 chipIgnite gross revenue of
  $1,560,000 is **1.6× one year of the programme's gross take**, raised from one investor and
  exhausted within five months.
- **Bears on:**
  - **The "no investors" claim (supports, weakly but in the only way a negative can).** A US company
    selling securities to outside investors under Regulation D files a Form D. UmbraLogic has filed
    nothing, and EDGAR does not know the name. **That is consistent with the owner's account that
    ChipFoundry took no outside investment, and it is the strongest public evidence available for
    it.** It is not proof: a company can be funded by its founders, by a bank, by revenue, or by a
    private placement that was mis-filed or exempt, and none of those leave an EDGAR trace.
    **Absence of a filing is not a statement of policy.** We found **no public statement by
    ChipFoundry or its founders of a "no investors" or "profitable from day one" position anywhere**
    (see the blocked list).
  - **H6 (context).** Efabless's last raise was $2.5m from a single accredited investor, five months
    before it stopped. The one public number about the money behind the old company says it was a
    bridge, not a Series B — which fits, without confirming, the owner's account that a funding
    round was blocked by an early investor refusing dilution. **Lucio Lanza**, of Lanza techVentures,
    an early-stage EDA investor, sits on that board; we name him because the filing does, **not**
    because we have any evidence he is the investor in question, and the repository should not imply
    that he is.
- **Used in:** `CF-16`.
- **Caveats:**
  - Form D covers exempt *securities* offerings. Debt, founder capital, revenue-financing, a
    foreign-only placement or an intra-family transfer need not appear.
  - We could not reach a state business registry to obtain UmbraLogic's formation date, registered
    agent or managers (see the blocked list), so the "no investors" claim rests on absence of
    evidence plus the owner's account.
  - The Form D's `totalAmountSold` equalling `totalOfferingAmount` means the round as filed closed
    fully. It says nothing about a *later*, larger round being sought and refused.

---

## The shuttles: every number we could find

### CF-6. The full commitment curve for every ChipFoundry shuttle, from dated captures of its own front page — and the numbers are revised downwards afterwards

- **Sources:**
  - ChipFoundry's live public API (no credentials required):
    <https://platform.chipfoundry.io/api/v1/shuttles/all-metrics>,
    <https://platform.chipfoundry.io/api/v1/shuttles/status>, and per shuttle
    `https://platform.chipfoundry.io/api/v1/shuttles/<slug>/metrics`.
  - **Twenty-eight Internet Archive captures of `https://chipfoundry.io/` between 2025-04-23 and
    2026-09-01**, which is where the earlier readings come from: until about 2026-03 the front page
    rendered the live counters server-side, so each capture froze that day's figures.
  - Two archived captures of the API itself:
    `https://web.archive.org/web/20260601170129if_/https://platform.chipfoundry.io/api/v1/shuttles/ci2605/metrics`
    and
    `https://web.archive.org/web/20260901183527if_/https://platform.chipfoundry.io/api/v1/shuttles/ci2609/metrics`.
- **Verification:** **Verified 2026-09-20.** Every capture listed below was fetched in raw (`id_`)
  form with `curl --compressed` and the figures read out of the rendered text; the two archived API
  responses were fetched with `if_` and read as JSON; the live API was re-fetched the same day.
  **This upgrades `OPG-9`'s caveat**, which marked the 2026-06-01 `ci2605` reading as *Partial*
  because a delegated agent had reported it — it is now re-fetched and confirmed exactly
  (`{"shuttle_name":"CI2605","interest":95,"planned":45,"reserved":34,"committed":29}`).
- **How it was counted** (reproducible): `curl` the Wayback CDX index for `chipfoundry.io`, fetch
  each homepage capture at `https://web.archive.org/web/<timestamp>id_/https://chipfoundry.io/`,
  strip tags, and read the four consecutive numbers labelled `Interest`, `Planned`, `Reserved`,
  `Committed`. From roughly 2026-03 onward the counter is client-rendered and the captures are
  blank, so the series continues from the API and its archived copies.
- **What it gives:**

  **CC2509 → CI2509** (tapeout 2025-09-12, shipped to customers 2026-05-19):

  | Read on | interest | planned | reserved | **committed** | note |
  |---|---:|---:|---:|---:|---|
  | 2025-06-13 | 80 | 24 | 7 | **2** | page says "Shuttle project status **out of 40 slots**" |
  | 2025-06-14 | 80 | 24 | 7 | **2** | |
  | 2025-07-11 | 88 | 29 | 18 | **7** | "Threshold achieved - confirmed GO for launch" |
  | 2025-08-07 | 92 | 33 | 27 | **17** | |
  | 2025-09-04 | 92 | 33 | 26 | **23** | last server-rendered reading before tapeout |
  | 2026-09-20 | 76 | 28 | 22 | **21** | live API, after the fact |

  **CC2511 → CI2511** (tapeout 2025-12-15, shipped 2026-06-26):

  | Read on | interest | planned | reserved | **committed** |
  |---|---:|---:|---:|---:|
  | 2025-09-28 | 42 | 26 | 12 | **7** |
  | 2025-10-09 | 50 | 34 | 16 | **9** |
  | 2025-11-11 | 55 | 39 | 19 | **14** |
  | 2025-11-15 → 2025-12-19 (six captures, all identical) | 62 | 42 | 23 | **20** |
  | 2026-09-20 | 53 | 37 | 24 | **23** |

  **CI2605** (tapeout 2026-06-04, fabrication 55% complete, delivery projected 2026-11-25):

  | Read on | interest | planned | reserved | **committed** |
  |---|---:|---:|---:|---:|
  | 2026-01-12 → 2026-01-14 (four captures) | 32 | 17 | 5 | **1** |
  | 2026-02-03 | 36 | 22 | 5 | **1** |
  | 2026-02-11 | 43 | 25 | 8 | **1** |
  | 2026-06-01 (archived API) | 95 | 45 | 34 | **29** |
  | 2026-09-20 | 73 | 43 | 32 | **29** |

  **CI2609** (open; commit date 2026-08-05, tapeout projected 2026-09-16):

  | Read on | interest | planned | reserved | **committed** |
  |---|---:|---:|---:|---:|
  | 2026-09-01 (archived API) | 69 | 34 | 18 | **10** |
  | 2026-09-20 | 79 | 35 | 21 | **16** |

  **CI2612** (open; opened 2026-06-08, commit projected 2026-10-08, tapeout projected 2026-12-07):

  | Read on | interest | planned | reserved | **committed** |
  |---|---:|---:|---:|---:|
  | 2026-09-20 | 110 | 35 | 3 | **0** |

- **DERIVED (arithmetic written out):**
  - **No completed shuttle has filled its own planned slot count.** 21 of 28, 23 of 37, 29 of 43 —
    **75.0%**, **62.2%**, **67.4%**. Across the three: 73 of 108 = **67.6%**.
  - **Against the slot count ChipFoundry advertised at launch, the shortfall is worse.** The
    2025-06-13 page sells CC2509 "out of **40** slots"; 21 committed is **52.5%** of 40. The three
    completed/fabricating shuttles together committed 73 slots where three 40-slot shuttles would be
    120 — **60.8%**.
  - **The fields are revised downwards after the shuttle closes, and now we can size the revision.**
    CI2509 went from `92/33/26/23` on 2025-09-04 to `76/28/22/21` a year later: interest −17.4%,
    planned −15.2%, reserved −15.4%, **committed −2 (−8.7%)**. CI2605 went from `95/45/34/29` on
    2026-06-01 to `73/43/32/29`: interest **−23.2%**, planned −2, reserved −2, committed unchanged.
    **`interest` is the field that gets cut; `committed` barely moves.** The most natural reading is
    that stale or duplicate enquiries are pruned, and that `committed` is the only field worth
    citing. Any citation of `interest` must carry the date it was read, and should be treated as an
    upper bound that the operator itself later reduces by 17–23%.
  - **`committed` climbs late and fast.** CI2605 stood at **1** committed on 2026-02-11 with a commit
    date of 2026-03-18, and finished at 29. CI2509 went 2 → 7 → 17 → 23 in eleven weeks. **A
    ChipFoundry shuttle looks empty until about a month before its commitment deadline.** That is a
    sharp and non-obvious operational fact, and it is the kind of thing that makes an
    auction-scheduled market hard: the information arrives at the last possible moment.
  - **Total committed slots to 2026-09-20: 21 + 23 + 29 + 16 + 0 = 89**, across five shuttles
    spanning first tapeout 2025-09-12 to a December 2026 tapeout still open.
- **Bears on:**
  - **H5 (challenges).** This is the sharpest version of `OPG-9`'s point. `interest` runs two to
    three times the slot count on every shuttle and has never once converted into a full run. And
    the operator's own later revisions say the operator does not believe its own `interest` figure
    either.
  - **H5 (supports, weakly).** `committed` is nonetheless rising across the series where the
    shuttles are comparable: 21 → 23 → 29 on the three completed/fabricating runs. **Three points
    is not a trend**, and `PAY-8`'s "+2.3%" year-on-year for ChipFoundry compares part-years.
  - **H6 (context).** 21, 23 and 29 paying customers per shuttle is the size of this business.
- **Used in:** `CF-7`, `CF-11`, `CF-16`; supersedes the numbers in `OPG-9` and the ChipFoundry rows
  of `PAY-8` with a dated series.
- **Caveats:**
  - **ChipFoundry defines none of these words.** "Committed" is read here, as in `OPG-9`, as "paid
    and locked in". That is an **inference**. The FAQ's payment terms ("Full payment at reservation
    / Deposit and milestone payments") mean a "committed" slot might be a deposit, not a full
    $14,950.
  - The two open shuttles will move.
  - The 2025-11-15 → 2025-12-19 run of six identical captures spans the CI2511 commitment date
    (2025-10-15) and the tapeout; it is possible the counter was simply frozen, not that no further
    commitments arrived, and the final figure of 23 (up from 20) says at least three arrived later.
  - **An unknown number of committed slots are not revenue** — see `CF-9` on ChipFoundry
    subsidising Tiny Tapeout, and `CF-11`.

### CF-7. The shuttle calendar: two runs in 2025, three in 2026 — down from the four to five ChipFoundry itself announced, with every delivery date slipping two to three months

- **Sources:**
  - <https://platform.chipfoundry.io/api/v1/shuttles/status> (nine dated milestones per shuttle,
    each with an `is_projected` flag), re-fetched 2026-09-20.
  - The "Shuttle Schedule" table on dated Internet Archive captures of `https://chipfoundry.io/`.
  - <https://chipfoundry.io/faqs>, fetched live 2026-09-20.
- **Verification:** **Verified 2026-09-20.**
- **What it says:**

  **Promised, in ChipFoundry's own FAQ** (still live, and still naming the old CC numbers):
  "**Manufacturing Schedule: Limited initial schedule with 2 shuttles in 2025 and 3 in 2026,
  compared to quarterly shuttles with chipIgnite**" … "CC2509: Submission deadline September 16,
  2025; Delivery February 2026. CC2511: Submission deadline November 11, 2025; Delivery April 2026.
  2026 Expansion: Three planned shuttles throughout 2026". Elsewhere the FAQ states "The typical
  timeline from submission to receiving your fabricated chips is **approximately 5 months**."

  **What was actually scheduled, and when it changed** (from the dated homepage schedule tables):

  | Capture | Shuttles listed | Commit dates | Tapeout dates | Delivery dates |
  |---|---|---|---|---|
  | 2025-04-23 | CC2509, CC2511 | — | 2025-09-16, 2025-11-11 | 2026-02-14, 2026-04-11 |
  | 2025-06-13 | CC2509, CC2511 | 2025-07-18, 2025-09-12 | 2025-09-16, 2025-11-11 | 2026-02-14, 2026-04-11 |
  | 2025-09-28 | CI2511, **CI2604**, **CI2606** | 2025-10-15, 2026-02-06, 2026-04-17 | 2025-11-11, 2026-04-07, 2026-06-06 | 2026-04-11, 2026-09-05, 2026-11-11 |
  | 2025-11-15 | CI2511, CI2604, CI2606 | unchanged | **2025-12-02**, … | **2026-05-02**, … |
  | 2025-12-07 | CI2511, **CI2605**, **CI2609** | 2025-10-15, 2026-03-18, 2026-07-22 | 2025-12-02, 2026-05-13, 2026-09-16 | 2026-05-02, 2026-10-13, 2027-02-16 |
  | 2026-02-03 | CI2605, CI2609, **CI2612** | — (table replaced by a link) | | |

  **What actually happened** (API milestones, `is_projected: false` unless marked):

  | Shuttle | Open | Commit | Tapeout | Wafers shipped | Customer shipped |
  |---|---|---|---|---|---|
  | CI2509 | 2025-05-01 | 2025-07-29 | **2025-09-12** | 2026-04-03 | **2026-05-19** |
  | CI2511 | 2025-08-01 | 2025-10-18 | **2025-12-15** | 2026-05-07 | **2026-06-26** |
  | CI2605 | 2026-01-01 | 2026-03-18 | **2026-06-04** | 2026-10-26 *(proj.)* | 2026-11-25 *(proj.)* |
  | CI2609 | 2026-01-29 | 2026-08-05 *(proj.)* | 2026-09-16 *(proj.)* | 2027-02-01 *(proj.)* | 2027-03-03 *(proj.)* |
  | CI2612 | 2026-06-08 | 2026-10-08 *(proj.)* | 2026-12-07 *(proj.)* | 2027-04-24 *(proj.)* | 2027-05-25 *(proj.)* |

  Every shuttle is `"process_node":"130nm"`, `"technology_pdk":"SkyWater SKY130"`. **There is no
  GF180MCU shuttle, and no second process of any kind, anywhere in ChipFoundry's schedule.**
- **DERIVED (arithmetic written out):**
  - **Announced but never run: CI2604 and CI2606.** Both were published with commit, tapeout and
    delivery dates on 2025-09-28 and had vanished by 2025-12-07, replaced by CI2605 and CI2609. The
    2025-09-28 enquiry dropdown offered **CC2604, CC2606, CC2609, CC2611** — four 2026 shuttles.
    **Three ran or are running.**
  - **Delivery slip, CI2509:** promised 2026-02-14 on the launch page; actually shipped 2026-05-19.
    **94 days late.** Tapeout was four days *early* (2025-09-16 promised, 2025-09-12 actual): the
    slip is entirely downstream of tapeout.
  - **Delivery slip, CI2511:** promised 2026-04-11 on the launch page, revised to 2026-05-02 in
    November 2025; actually shipped 2026-06-26. **76 days late against the original, 55 against the
    revision.** Tapeout promised 2025-11-11, revised 2025-12-02, actual **2025-12-15** — 34 days
    late.
  - **Cycle time against the FAQ's "approximately 5 months".** CI2509: commit 2025-07-29 to customer
    shipped 2026-05-19 = **294 days ≈ 9.7 months**. CI2511: 2025-10-18 to 2026-06-26 = **251 days ≈
    8.3 months**. Measured from tapeout instead: **250 days** and **193 days**. **The real figure is
    roughly twice the published one**, and the FAQ has not been corrected.
  - **Cadence.** Efabless ran four chipIgnite shuttles in 2024 (`PAY-8`). ChipFoundry ran two in
    2025 and is running three in 2026. Against Efabless's peak year that is **75%** of the
    cadence — and the FAQ says so itself, "compared to quarterly shuttles".
- **Bears on:**
  - **H6 (challenges).** The gap between a published five-month turnaround and a real
    eight-to-ten-month one is the clearest operational number in this file. Working capital sits in
    that gap: the customer pays at commitment and waits nine months.
  - **H5 (context).** Two announced shuttles were cancelled or renumbered before they ran. Slots are
    not a schedule; they are an intention that depends on enough people committing (`CF-12`).
  - **The auction design (context).** `PRINCIPLES.md` assumes a schedule a bidder can bid into. The
    only unsubsidised open-shuttle operator in existence moves its dates by one to three months
    routinely and deletes announced runs. A market design that assumes a fixed calendar is
    designing for a world that does not exist yet.
- **Used in:** `CF-16`.
- **Caveats:**
  - "Customer shipped" is ChipFoundry's own milestone; we have not verified that any customer
    received anything on those dates. Tiny Tapeout's independent dates (`CF-9`) are the only
    outside check and they are *estimates*.
  - The launch-page delivery dates (2026-02-14, 2026-04-11) were on a marketing page before anyone
    had bought; treating them as promises is a judgement.
  - CI2604/CI2606 may have been renumbered rather than cancelled — the dates moved too (CI2604's
    2026-04-07 tapeout became CI2605's 2026-05-13), which is consistent with either reading.

### CF-8. The price has been $14,950 for the whole of ChipFoundry's existence — and the $9,750 → $14,950 "rise" is a comparison between two different companies

- **Sources:** every Internet Archive capture of `https://chipfoundry.io/` from `20250423080821` to
  `20260901183525`, and <https://chipfoundry.io/faqs> live. For the Efabless side, `PAY-7`.
- **Verification:** **Verified 2026-09-20.**
- **What it says:**
  - "**$14,950 per tapeout**" appears on the **first** archived ChipFoundry page (2025-04-23, then
    as the price of "Chip Create") and on every capture since, including 2026-09-01. **No price
    change of any kind is visible across seventeen months.**
  - The live FAQ: "The standard pricing is **$14,950 per project** for standard shuttle
    participation. This includes 100 QFN packaged parts (or optionally all bare die)." /
    "There is an option for an additional **50 bare die for $3000**." / "**We do not offer discounts
    for individual project submissions.** Discounts are available exclusively for organizations
    purchasing a pool of projects for academic, research, or commercial volume use." /
    "**Pricing: chipIgnite projects are priced at $14,950 compared to $9,750**".
  - Payment terms, verbatim: "Full payment at reservation / Deposit and milestone payments / Refund
    capability if shuttle minimums are not met."
  - The refund clause, verbatim: "If a shuttle does not meet the minimum customer commitment
    threshold required for launch, you will be offered: A full refund of your project fee, or The
    option to roll over your project to the next scheduled shuttle."
- **DERIVED:** 14,950 ÷ 9,750 = **+53.3%**. But `PAY-7` establishes $9,750 was Efabless's price from
  May 2021 to its death, and `CF-2` establishes $14,950 was ChipFoundry's price from the day it
  appeared. **There is no date on which anyone raised a price.** The series is two flat prices, four
  years and one bankruptcy apart.
- **Bears on:**
  - **H6 (context, and it corrects `PAY-7` and `SMB-9`).** `PAY-7` already says this is "one price
    held flat for four years by one company, and then a 53% step change by a different company". This
    entry adds the fact that makes it unambiguous: **the 53% was there before ChipFoundry owned the
    chipIgnite name at all**, so it cannot be read as a rise applied to an inherited product.
  - **H6 (supports).** The most defensible reading of the two numbers is that **$9,750 did not cover
    the cost of running the service**, and that a company built to be self-supporting priced the same
    physical deliverable 53% higher from the outset. That is the single most useful fact in this file
    for `PRINCIPLES.md`: it is an independent, market-tested estimate of how far below cost the
    subsidised-and-then-dead price was. It is **not proof** — the two companies' cost structures,
    volumes and suppliers differ, and SkyWater's own prices moved over four years.
- **Used in:** `CF-11`, `CF-16`.
- **Caveats:**
  - $14,950 buys 100 QFN parts and an eval board; $9,750 bought 100 QFN or 300 WCSP and five eval
    boards (`PAY-7`). The bundles are **not identical**, and nobody has costed the difference.
  - Efabless's $3,500 chipIgnite Mini and $48,750/$87,750 university pools have no ChipFoundry
    equivalent that is public. ChipFoundry's pool discounts exist but the schedule is behind
    "contact us", so the **realised average price per slot is unknown and is below $14,950**.
  - Everything else ChipFoundry sells — production volumes, commercial SRAM, ReRAM, ML — is priced
    only through "Request a Quote". `chipfoundry.io/terms` returns HTTP 404 (`ACC-3`).

### CF-9. Tiny Tapeout is ChipFoundry's largest single repeat customer, buying five slots across four shuttles — and ChipFoundry subsidises part of what it sells to them

- **Sources:**
  - Tiny Tapeout's own chip table, <https://tinytapeout.com/chips/> (which `tinytapeout.com/runs/`
    redirects to), fetched 2026-09-20.
  - <https://chipfoundry.io/tinytapeout>, fetched live 2026-09-20.
  - Tiny Tapeout news posts: `/news/chipfoundry-sponsor/` (2025-05-10),
    `/news/sky130-confirmed/` (2025-06-26), `/news/ttsky25a-submitted/` (2025-10-01),
    `/news/ttsky25b-submitted/` (2025-11-20), `/news/2025-review/` (2026-01-08).
  - ChipFoundry's GitHub organisation, which carries per-run Tiny Tapeout repositories.
- **Verification:** **Verified 2026-09-20**, all fetched with `curl` and read.
- **What it says:**
  - Tiny Tapeout names the commercial shuttle each of its runs rode, in a public table:

    | TT run | Launched | Closed | Shuttle | Designs | Est. delivery |
    |---|---|---|---|---:|---|
    | TTSKY25a | 2025-06-27 | 2025-09-15 | **CI-2509** | 237 | 2026-07-03 |
    | TTSKY25b | 2025-09-18 | 2025-11-10 | **CI-2511** | 316 | 2026-08-30 |
    | TTSKY26a | 2026-02-27 | 2026-05-11 | **CI-2605** | 289 | 2026-12-20 |
    | TTSKY26b | 2026-04-25 | 2026-05-18 | **CI-2605** | 273 | 2026-12-20 |
    | TTSKY26c | 2026-05-26 | 2026-09-07 | **CI-2609** | 242 | 2027-05-12 |

    (The Efabless-era rows in the same table are CI-2211Q, CI-2304C, CI-2309, CI-2311, CI-2404,
    CI-2406, CI-2409, CI-2411 — and TT01 on "MPW7".)
  - ChipFoundry's GitHub organisation independently carries `nydesign-cc2509` (described "Tiny
    Tapeout SKY 25b shuttle using sky130A PDK on ChipFoundry CC2511 MPW"), `nydesign-ci2511`,
    `nydesign-ci2605` ("NYDesign CI2605 Tiny Tapeout chip") and `uofa-ci2609` ("University of Arizona
    Tiny Tapeout chip for ChipFoundry CI2609 (SKY130 openframe)"), plus
    `chipdiscover-wokwi-template` and `chipdiscover-verilog-template`, both described as
    "Submission template for Tiny Tapeout SKY130 (ChipFoundry) shuttles".
  - **ChipFoundry's own Tiny Tapeout page, verbatim:** "ChipFoundry is excited to be a proud partner
    of the Tiny Tapeout program… **Our partnership includes subsidizing the cost of fabrication for a
    portion of Tiny Tapeout projects.**"
  - Tiny Tapeout, 2026-01-08: "Huge thanks to our fab partners — SkyWater Technology, IHP,
    **ChipFoundry**, and wafer.space — for manufacturing our chips."
  - Tiny Tapeout, 2025-10-01: "**Thanks to ChipFoundry for sponsoring us** and keeping ASIC design and
    manufacturing affordable! … thanks to ChipFoundry you can tape out a single-tile digital design
    and receive your own ASIC for just €185 including shipping."
- **DERIVED:**
  - **Five ChipFoundry slots have gone to Tiny Tapeout** (one each on CI2509, CI2511 and CI2609, two
    on CI2605), out of **89** committed slots across all five shuttles — **5.6%**. Against the 73
    committed on the three completed/fabricating runs alone, four TT slots is **5.5%**.
  - At list price those five slots would be 5 × $14,950 = **$74,750**. ChipFoundry says it subsidises
    "a portion", so the cash received is **less than that, by an unknown amount, possibly zero**.
  - **Tiny Tapeout put 1,357 designs onto ChipFoundry silicon** (237 + 316 + 289 + 273 + 242) in five
    runs — against ChipFoundry's own 89 direct customers. **The reseller carries fifteen times the
    design count of the direct business.**
- **Bears on:**
  - **H5 (mixed, and it cuts hard).** The long tail of demand for SKY130 is real and it is enormous —
    1,357 designs in fourteen months. **But it arrives through one intermediary buying five slots**,
    and the price per design at the tail end is €185, not $14,950. That is the shape of the demand
    curve, measured.
  - **H6 (challenges).** The largest repeat customer is also a sponsee. Part of ChipFoundry's
    headline `committed` count is its own marketing spend.
  - **`PAY-8` needs amending.** It flags "at least five ChipFoundry-era slots are Tiny Tapeout's own
    purchases"; this entry identifies exactly which five, and adds that they are **partly
    subsidised**, so the double-count correction in `PAY-8`'s combined table understates the problem.
- **Used in:** `CF-11`, `CF-16`.
- **Caveats:**
  - "One slot per TT run" is an inference from the table's one-shuttle-per-run mapping; a TT chip
    might occupy more or less than a nominal slot, and TTSKY26a and TTSKY26b sharing CI2605 is the
    only case where the mapping is explicit about two.
  - "A portion" is not quantified anywhere. Neither party publishes what Tiny Tapeout pays.
  - Tiny Tapeout's delivery dates are its own estimates.

### CF-10. What happened to the designs Efabless left in the fab: TT08 was delivered in December 2025, TT09 has never been delivered

- **Sources:**
  - Tiny Tapeout, "Efabless shuts down - Tiny Tapeout will continue", 2025-03-01:
    <https://tinytapeout.com/news/efabless-shutsdown/>
  - Tiny Tapeout, "TT08 chip-on-board (COB) arrives", 2025-11-13:
    <https://tinytapeout.com/news/tt08-arrives/>
  - The chip table at <https://tinytapeout.com/chips/>.
- **Verification:** **Verified 2026-09-20.**
- **What it says:**
  - 2025-03-01, verbatim: "Efabless shuts down until further notice. … **Right now we have TT08
    awaiting packaging and TT09 still in the SkyWater Technology fab. These chips represent a huge
    investment of time and energy from hundreds of people, and we currently don't know if we'll
    receive them. We are prepared to offer a refund to all affected customers if we aren't able to
    ship those chips.** Current TT10 shuttle and future SkyWater Sky130 shuttles are paused while we
    explore options for Sky130 and other processes."
  - 2025-11-13: "**TT08 contains 135 designs**, and the first tests are in. … The bare dies are now
    mounted and wire-bonded".
  - The chip table, today: **TT08** — shuttle CI-2409, 135 designs, "Chips expected 2025-09-29",
    "**Shipped 2025-12-01**". **TT09** — shuttle CI-2411, **369 designs**, "Chips expected **TBD**",
    delivery column blank. **TT10** — "**Cancelled**".
- **DERIVED:**
  - TT08's chips arrived **about nine months after** Efabless stopped, and **about 18 months** after
    the CI-2409 tapeout (2024-09-16 per `PAY-8`).
  - **TT09's 369 designs have still not been delivered, 18 months after the shutdown and 22 months
    after tapeout.** It remains the largest single block of stranded open-silicon work.
  - TT10 was cancelled outright with 240 of 512 tiles already used (Tiny Tapeout's
    `submission-stats` API, `PAY-1`).
- **Bears on:**
  - **H6 (challenges, and this is the real cost of a shuttle operator failing).** The task brief's
    framing — "hundreds of designs, including 500 Tiny Tapeout projects from TT08 and TT09,
    seemingly stuck in fabrication limbo" — resolves to: **135 recovered after nine months, 369 still
    stuck, one whole shuttle cancelled.** 504 designs affected; 27% recovered.
  - **The auction design (context).** A customer's exposure when the operator fails is the whole
    lead time, and the lead time is nine months to two years. `PRINCIPLES.md` treats the auction as
    allocating capacity; this is the counterparty risk that sits behind the allocation.
- **Used in:** `CF-16`.
- **Caveats:**
  - Whether ChipFoundry's asset purchase (`CF-3`) covered any obligation to these customers is not
    stated anywhere public. We do **not** know who paid for TT08's recovery, and it should not be
    assumed ChipFoundry did.
  - "TBD" on TT09 is Tiny Tapeout's word; the chips may yet arrive.

### CF-11. What the whole visible business amounts to: 89 committed slots, a 25-article knowledge base, 100 marketplace IPs, three showcased projects

- **Sources:** ChipFoundry's public platform API, all fetched without credentials on 2026-09-20:
  `/api/v1/shuttles/all-metrics`, `/api/v1/shuttles/status`, `/api/v1/showcase`,
  `/api/v1/showcase/contests`, `/api/v1/community`, `/api/v1/knowledge-base`, `/api/v1/marketplace`.
- **Verification:** **Verified 2026-09-20.**
- **How it was found** (reproducible, and it extends `OPG-9`'s method): fetch
  `https://platform.chipfoundry.io/shuttle-metrics` — a 483-byte Vite shell — then fetch the
  JavaScript bundle it references (`/assets/index-BxHOwEBh.js`, 1.74 MB) and grep it for both quoted
  and template-literal paths beginning `/api`. That yields **28 literal and 26 templated endpoints**.
  Of those, seven answer HTTP 200 without credentials; `/api/v1/shuttles` itself returns
  `{"detail":"Not authenticated"}` and the rest are user- or organisation-scoped. There is no
  OpenAPI document: `/api/v1/openapi.json`, `/api/docs` and `/api/v1/docs` all return
  `{"detail":"Not Found"}`.
- **What it says:**

  | Endpoint | Returns |
  |---|---|
  | `/api/v1/showcase` | `"total": 3` — three published projects, **all on CI2511**: `microwatt-debugger`, `microwatt-soc-gen`, `microwatt-fpga` |
  | `/api/v1/showcase/contests` | `[]` — empty |
  | `/api/v1/community` | `"total": 6` — two ChipFoundry staff, the ChipFoundry organisation, and three customers (`CF-4`) |
  | `/api/v1/knowledge-base` | **25** articles, every one `published_at`/`updated_at` between **2026-09-16 and 2026-09-19** |
  | `/api/v1/marketplace` | **100** entries, 99 tagged `"section":"ip"` and one `"reference_designs"` |
  | `/api/v1/shuttles/all-metrics` | five shuttles, 89 committed slots in total (`CF-6`) |

- **DERIVED (arithmetic written out, and read the caveats before quoting any of it):**
  - **Gross revenue at list price, committed slots only:** CI2509 21 × $14,950 = **$313,950**;
    CI2511 23 × $14,950 = **$343,850**; CI2605 29 × $14,950 = **$433,550**; CI2609 16 so far ×
    $14,950 = **$239,200**; CI2612 0 = **$0**. **Total $1,330,550** across five shuttles.
  - **Delivered-and-paid-for so far** (the two shuttles that have reached customers): 44 slots,
    **$657,800**.
  - **Annualised on tapeouts:** the three tapeouts to date (2025-09-12, 2025-12-15, 2026-06-04) carry
    73 committed slots = **$1,091,350** over the 12.3 months from first to latest tapeout ≈
    **$1.06m/year of gross bookings**, before deducting subsidised Tiny Tapeout slots (`CF-9`) and
    before any cost.
  - **Against Efabless's peak:** `PAY-8` derives $1,560,000 of chipIgnite gross revenue in 2024.
    1,091,350 ÷ 1,560,000 = **70.0%**. ChipFoundry is running at roughly **seven-tenths of the dead
    company's best year**, at **1.53× the price**, which implies **about 46% of the unit volume**
    (73 slots a year against 160).
  - **Revenue per employee, on the four people we can name (`CF-4`):** $1,091,350 ÷ 4 = **about
    $273,000**. If the company is eight people it is about $136,000, which for a US
    semiconductor-services business is not a viable figure. **This single ratio is the crux of the
    verdict in `CF-16`**, and it is a derivation from a floor headcount, not a measurement.
- **Bears on:**
  - **H6 (context).** The visible business is small and the derived gross is about $1m a year. The
    knowledge base and the marketplace are the artefacts of a product organisation, not of a large
    one: all 25 articles were written or rewritten inside four days in September 2026.
  - **H5 (challenges).** Three projects in a public showcase, after five shuttles and 89 committed
    slots, and an empty contests list. Efabless ran design contests with free fabrication as prizes
    (`OPG-6`); ChipFoundry's contest table is empty. Whatever community activity there is, it is not
    visible here.
- **Used in:** `CF-16`.
- **Caveats — and these matter more than the numbers:**
  - **Every revenue figure above is committed slots × list price. It is not a measurement**, it is
    the same derivation `PAY-8` makes, with the same three holes: committed may be a deposit, pool
    discounts are unpublished, and Tiny Tapeout's slots are partly subsidised by ChipFoundry itself.
    The true figure is **below** $1.33m and we cannot say by how much.
  - It also **omits** everything ChipFoundry sells outside the shuttle — production volumes,
    commercial SRAM, ReRAM, ML, IP, support packages, design review — all of which are priced by
    quote and none of which is visible. The true figure is therefore **above** the shuttle
    derivation by an unknown amount too. **The two errors run in opposite directions and neither is
    bounded.**
  - The showcase is opt-in and, for a service whose selling point is "no open-source requirement"
    (`ACC-3`), most customers have every reason not to appear in it. **Three showcased projects is
    not three customers.**
  - "Revenue per employee" on a floor headcount of four is an upper bound on the ratio, not an
    estimate of it.

### CF-12. Two operational facts ChipFoundry has published about itself: the 50%-full launch rule, and the CI2511 metal-polygon incident with SkyWater

- **Sources:**
  - Tiny Tapeout, "ChipFoundry announced as Tiny Tapeout sponsor", 2025-05-10, and "ChipFoundry
    Sky130 Shuttle Confirmed", 2025-06-26.
  - ChipFoundry knowledge-base article `issues-with-large-metal-polygons-in-sky130-integrated-circuits`,
    from <https://platform.chipfoundry.io/api/v1/knowledge-base>.
- **Verification:** **Verified 2026-09-20.**
- **What it says:**
  - **The launch rule**, as Tiny Tapeout reported it on 2025-05-10: "One important detail to note:
    **their shuttles will only go ahead if at least 50% of the MPW slots are filled. ChipFoundry will
    confirm whether it's a 'go' two months before the final submission deadline.** If not enough
    designs are on board by then, the run gets pushed to the next shuttle."
  - **The GO decision, 2025-06-26:** "ChipFoundry has reached an early GO decision to run the
    ChipCreate MPW CC2509 Shuttle for September. **They have received enough project commitments to
    cover the costs needed to support the foundry and other suppliers running the shuttle.**"
  - **The CI2511 incident**, verbatim from ChipFoundry's own knowledge base: "During the CI2511
    shuttle, Skywater engineers identified several submissions containing large, continuous metal
    polygons in the interior of the die." … "Of particular concern in a multi-project wafer context
    is that some failure modes — particularly delamination — **can affect an adjacent die. This
    creates the risk that a single poorly-designed die can cause yield loss across multiple
    neighboring customer designs on the same shuttle.**" … "Because ChipFoundry's shuttle reticle
    places customer dies in close proximity, this risk is" [material].
- **Bears on:**
  - **H6 (supports, and it is the most directly quotable line in this file).** "Enough project
    commitments **to cover the costs needed to support the foundry and other suppliers**" is an
    operator stating, in public, that the shuttle is run on cost recovery and does not go ahead
    below it. **DERIVED — what the threshold was, in slots.** `CF-6` brackets the GO date
    (2025-06-26) between two captures: on **2025-06-14** CC2509 read `80 / 24 / 7 / 2` and on
    **2025-07-11** it read `88 / 29 / 18 / 7`. So on the day GO was called, **`committed` was
    between 2 and 7** and **`reserved` was between 7 and 18**, against a `planned` of 24–29. Half
    of `planned` is 12–15, which `reserved` crosses in exactly that window and `committed` does not
    come near. **The 50% rule is therefore a rule about *reservations*, not about paid commitments**
    — ChipFoundry committed to spend the money on a run that had, at most, seven customers who had
    actually paid. At $14,950 that is at most **$104,650** of committed revenue against a full
    SKY130 MPW lot. Both readings are inferences from two capture dates and should be quoted as
    such.
  - **The auction design (challenges).** A 50%-full rule and a two-month-ahead go/no-go is a
    *reservation-and-threshold* mechanism, not a market. Every unsubsidised operator in this
    repository — Efabless's $200 refundable deposit and "minimum project capacity" (`PAY-7`),
    ChipFoundry's 50% rule, `DEM-10`'s 50% clause — writes undersubscription risk into its terms
    rather than clearing it in a price. **`PRINCIPLES.md` should say why an auction does better than
    the thing three operators independently chose.**
  - **H6 (context).** MPW yield is a shared-fate problem between customers. A pooled run externalises
    one customer's design error onto their neighbours, and the operator absorbs the dispute.
- **Used in:** `CF-16`.
- **Caveats:**
  - The 50% rule is reported by Tiny Tapeout, not stated on ChipFoundry's own site; the FAQ's
    version is the vaguer "minimum customer commitment threshold". Treat the *number* 50% as
    second-hand.
  - "Enough commitments to cover the costs" is a sponsor's paraphrase of a supplier's decision. It
    is not an accounting statement, and the ≤7-slot bracket rests on the `CF-6` capture dates.
  - The knowledge-base article's closing sentence is truncated in the API payload as fetched.

### CF-13. The terms: a minimum of **20 confirmed participants** per shuttle, full pre-payment two weeks before the submission deadline, and a deposit that went from $200 refundable-at-Efabless to $500 non-refundable

- **Sources**, all fetched live on 2026-09-20 and all found from `https://chipfoundry.io/sitemap.xml`
  (none of them is linked from the front page):
  - <https://chipfoundry.io/reservations> — "chipIgnite Shuttle Reservation Deposit"
  - <https://chipfoundry.io/commercial-terms> — "chipIgnite Commercial Terms", "**Last Updated:
    November 13, 2025**"
  - <https://chipfoundry.io/payment-terms> — "ChipFoundry.io Payment Terms", "**Last Updated: April
    22, 2025**" (a stale page, still describing the launch terms)
- **Verification:** **Verified 2026-09-20**, all three fetched with `curl --compressed` and read in
  full.
- **What it says**, verbatim:
  - **The threshold, as a number.** The reservations page: "**A minimum of 20 confirmed participants
    is required for a shuttle fabrication run to proceed.** ChipFoundry provides regular reservation
    updates and will notify you once this threshold is met."
  - **The payment schedule** (commercial terms, 2025-11-13): "Initial Deposit: **$500 USD** due at
    reservation / First Milestone Payment: **50% of remaining balance due 60 days before** shuttle
    submission deadline / Final Payment: Remaining balance due **14 days before** shuttle submission
    deadline."
  - **The launch schedule, for comparison** (payment terms, 2025-04-22): "A **non-refundable deposit
    of $200 USD** is required to secure a reservation" / "Final Payment: Remaining balance due **30
    days before** shuttle submission deadline."
  - **The live reservation prices**: "Reservation for **CI2609** … **$500** per project" and
    "Reservation for **CI2612** … **$500** per project."
  - **Customer cancellation** (commercial terms): "The commitment deposit and final deposit are
    refundable if cancellation is requested prior to the commitment deadline… After the commitment
    deadline, the commitment deposit and final deposit are **non-refundable**. However, customers may
    apply these deposits to a future shuttle, subject to availability, upon payment of a **$500 USD
    change fee**." The April 2025 page had a softer ladder: 75% refund more than 60 days out, 50% at
    30–60 days, none inside 30 days.
  - **Delivery** (both pages): "Standard delivery is expected **approximately 5 months after the
    submission deadline**."
  - **Governing law and venue**: "binding arbitration in the **county of San Mateo, California**."
    Efabless's SEC filing gives its address as **San Carlos, CA**, which is in San Mateo County
    (`CF-5`).
  - **IP**: "Customers retain all intellectual property rights to their design. ChipFoundry makes no
    claim to ownership of Customer designs." / "Appropriate NDAs can be executed upon request."
- **DERIVED (arithmetic written out), and this is the most useful set of numbers in the file:**
  - **Every completed ChipFoundry shuttle has landed just above the stated minimum of 20.** CI2509
    finished at **21** (minimum + 1), CI2511 at **23** (+3), CI2605 at **29** (+9). **Not one has
    landed below it, and not one has landed far above it.** Read against `CF-6`'s finding that
    `committed` climbs almost entirely in the last few weeks, the picture is of a business that
    scrapes over its own viability line each time and then runs.
  - **CI2609 is currently at 16 committed** (`CF-6`, read 2026-09-20), **four short of the stated
    minimum**, with a projected tapeout of 2026-09-16 that has already passed. Either more
    commitments have arrived and the API has not caught up, or the run is being held. **This is the
    first ChipFoundry shuttle visibly at risk against its own published rule**, and it should be
    re-read.
  - **ChipFoundry is fully pre-paid roughly nine months before it delivers.** Final payment falls 14
    days before the submission deadline; `CF-7` measures actual delivery at **193–250 days after
    tapeout**. So the customer's money sits with the operator for **seven to eight months after the
    last payment**, and the operator carries no receivable at all. **This is the single most
    important structural fact about the business model**, and `PRINCIPLES.md` should state whether
    the auction it proposes is pre-paid on the same terms. An MPW operator that is pre-paid does not
    need working capital for the run; it needs only to survive between runs.
  - **The deposit tripled, from $200 to $500, and Efabless's $200 was refundable** ("$200 reservation
    fee (fully refundable if minimum projects not met)", `PAY-7`) **while ChipFoundry's has been
    non-refundable from the start.** The final-payment date also moved *later*, from 30 days to 14
    days before the deadline — a concession to customers, taken at the same time as the deposit was
    tripled.
  - **Reservation deposits are a revenue line nobody has counted.** `CF-6` gives `reserved` counts of
    22, 24, 32, 21 and 3 across the five shuttles = **102 reservations**. At $500 non-refundable
    that is **$51,000**, and at the earlier $200, proportionately less. It is small, but it is real
    money that does not appear in `PAY-8` or in `CF-11`, and the ones that never convert to
    `committed` are pure margin.
- **Bears on:**
  - **H6 (supports).** A published, numeric minimum of 20 customers is the clearest public statement
    anyone in this sector has made about the size of a viable MPW run. **DERIVED:** 20 × $14,950 =
    **$299,000** as the floor a SKY130 shuttle must book to proceed. That is a directly usable figure
    for `PRINCIPLES.md` and it is the operator's own number, not ours.
  - **The auction design (challenges, and it is the sharpest challenge in this file).**
    ChipFoundry's mechanism is: a non-refundable option fee ($500), a commitment deadline 60 days
    out at which half the money becomes non-refundable, full payment 14 days out, and a hard
    quantity floor of 20 below which nothing happens. **That is not a price mechanism at all — it is
    a quantity threshold with an option premium.** `PRINCIPLES.md` has to explain what an auction
    does better than this, given that this is what the only unsubsidised operator actually built,
    and given that the binding constraint it is designed around — you cannot run half a mask set —
    does not go away under any pricing rule.
  - **H5 (context).** "Customers retain all intellectual property rights" and "Appropriate NDAs can
    be executed upon request" confirm `ACC-3`: this is a **private** shuttle with no open-source
    requirement, so the visible design count (`CF-11`) will always understate the customer count.
- **Used in:** `CF-16`.
- **Caveats:**
  - Three pages give three slightly different versions of the same terms, and the payment-terms page
    is sixteen months stale and still names "ChipCreate" and the CC-era schedule. Which governs is
    not stated. The commercial terms (2025-11-13) are the most recent and the most formal.
  - "20 confirmed participants" is on the reservations page only; the FAQ and the commercial terms
    both say only "minimum customer commitment threshold" without a number. Tiny Tapeout's
    second-hand "50% of the MPW slots" (`CF-12`) is a *different* rule, and 50% of a 28–43 slot
    shuttle is 14–22. The two are compatible but not identical; **it is possible the rule is "20 or
    50%, whichever is greater"**, and we could not confirm it.
  - Academic and volume discounts are "case-by-case"; none of the three pages gives a rate.

### CF-14. The design contests are sponsor-funded, and ChipFoundry publishes their conversion: **234 proposals → 106 accepted → 3 fabricated**

- **Sources**, fetched live 2026-09-20:
  - <https://chipfoundry.io/challenges/microwatt> — "Microwatt Momentum Challenge 2025"
  - <https://chipfoundry.io/challenges/bmlabs> — "The NVM Innovation Contest"
  - <https://chipfoundry.io/sponsorship> — "Sponsor a Chipignite Design Challenge"
  - <https://platform.chipfoundry.io/api/v1/showcase>
  - The `chipIgnite` YouTube channel feed,
    `https://www.youtube.com/feeds/videos.xml?channel_id=UCKBHanCVU1lDAEggUOYsBvg`
- **Verification:** **Verified 2026-09-20.**
- **What it says:**
  - **The Microwatt Momentum Challenge 2025 publishes its own funnel as three headline figures:**
    "**234** Submitted Proposals", "**106** Accepted Proposals", "**3** Winning Designs Fabricated".
    Proposals were due 2025-09-22, final designs 2025-10-31. The three winners are named — MicroWatt-LX
    SoC Generator, Minimal Hardware-Debugger with Microwatt, FPGA Fabric Integration with Microwatt —
    and **they are exactly the three entries in ChipFoundry's public showcase API, all three tagged
    `"shuttle_name":"CI2511"`** (`CF-11`).
  - **The NVM Innovation Contest** (with BM Labs' ReRAM IP; proposals 2025-10-17, final designs
    2025-11-03, winners announced 2025-11-08): "**The winning design will be submitted to the
    November shuttle for free fabrication!** ChipFoundry will handle the tapeout and delivery of the
    packaged silicon parts directly to the winning design teams." The November shuttle is CI2511.
  - **Who pays.** ChipFoundry's sponsorship page sells exactly this: "Design Challenge Sponsorship
    Package — **Fabrication of 1 winning project on an MPW Shuttle.** Hosting for 1 promotional
    webinar…" and "Premium Design Challenge Sponsorship — **Fabrication of 3 winning projects on an
    MPW Shuttle.** BEST VALUE. Hosting for 2 promotional webinars…". Both are priced "**Inquire for
    Pricing**".
  - The YouTube feed confirms the cadence of these programmes: "Webinar - OpenPOWER HW Design
    Hackathon" (2025-09-11), "Webinar #2 - OpenPOWER HW Design Hackathon" (2025-09-25), "Webinar -
    NVM Innovation Contest" (2025-10-12), "Webinar: Systems to Silicon Design Contest" (2026-03-05).
    So there has been at least a third contest in 2026.
- **DERIVED (arithmetic written out):**
  - **The contest funnel is 234 → 106 → 3.** Acceptance 106 ÷ 234 = **45.3%**. Fabrication 3 ÷ 234 =
    **1.28%**, or 3 ÷ 106 = **2.8%** of accepted proposals.
  - **At least four of CI2511's 23 committed slots are contest prizes**, three from Microwatt and at
    least one from the NVM contest — **17.4% of that shuttle** — plus the Tiny Tapeout slot (`CF-9`),
    giving **at least five of 23, 21.7%, that no ordinary customer paid $14,950 for.**
  - **But they are not free.** The sponsorship page shows ChipFoundry **selling** the prize slots to
    a sponsor. So these slots are revenue — at an unpublished price, from a different kind of buyer.
    **This cuts both ways for `CF-11`'s derivation and it is why that derivation cannot be tightened.**
- **Bears on:**
  - **H5 (challenges, and it is a direct hit on the repository's growth evidence).** 234 people
    wrote a proposal; **three** got silicon. `PAY-8` already warns that Efabless's submission counts
    included contest entries competing for a free slot (`OPG-6`). Here is the conversion rate for
    that population, published by the operator: **1.3%**. **A contest proposal is not a customer, and
    the ratio is two orders of magnitude.** Every submission-based growth figure in
    `resources/demand/` should be read against this number.
  - **H6 (supports, and this is a business-model finding worth more than it looks).** ChipFoundry has
    found a **third party who will pay for a slot on behalf of somebody who would never have paid**:
    an IP vendor or an ecosystem body buying a contest. That is the same economic move as Tiny
    Tapeout's sponsors (`PAY-6`), SwissChips, and IEEE's TTSKY26b subsidy — **the long tail does not
    pay for itself; somebody with a strategic interest pays for it.** For a project whose thesis is
    that the tail can be served profitably, this is the most important pattern in the file after the
    price.
  - **H6 (context).** ChipFoundry's contest API (`/api/v1/showcase/contests`) returns `[]` while
    three contests demonstrably ran. The platform's public surface understates the business.
- **Used in:** `CF-11`, `CF-16`.
- **Caveats:**
  - "3 Winning Designs Fabricated" is ChipFoundry's own count and the showcase corroborates it, but
    we did not verify that the three chips exist.
  - Whether the NVM winner is inside or outside the 23 committed on CI2511 is unknown; we assume
    inside.
  - The sponsorship prices are not public, so the contest slots' contribution to revenue cannot be
    estimated at all.
  - 234 proposals for a *hackathon with free silicon as the prize* is not the same population as 234
    people considering a $14,950 purchase. The 1.3% is a conversion rate for free-entry interest, not
    for demand.

### CF-15. ChipFoundry has built an "Anchor / Tenant" production-aggregation product — an operator independently reinventing the problem this project proposes to auction

- **Source:** <https://chipfoundry.io/production> ("Production Aggregation — The Bridge Between
  Prototyping and Mass Production"), fetched live 2026-09-20. The page is in the sitemap and in the
  navigation, and the earliest Internet Archive capture of `/production` is **2026-02-11**.
- **Verification:** **Verified 2026-09-20.**
- **What it says**, verbatim:
  - "chipIgnite is introducing a new fabrication model designed to lower the barrier to entry for
    130nm volume production. **By aggregating multiple commercial projects onto a single production
    mask set, we unlock economies of scale previously reserved for high-volume enterprise silicon.**
    This **Anchor / Tenant** model serves two distinct customer needs: those who need control (The
    Anchor) and those who need access (The Tenant)."
  - "**The Anchor is the project that establishes the production schedule. By underwriting the
    production tooling, the Anchor secures 'Schedule Sovereignty' — the right to determine the
    tape-out date for a ChipFoundry-owned mask set that matches their product roadmap.**" Benefits:
    "Schedule Control: You determine when the train leaves the station." / "Volume Economics: Access
    high-volume unit pricing (**100k+ units**) immediately." / "**NRE Rebates: Receive financial
    credits (up to $75k) as Tenants join the run, effectively subsidizing your initial
    investment.**" Ideal for "Startups moving from MPW to their first commercial launch (**100k -
    500k units**)."
  - "**The Tenant is a 'rider' on an established Anchor run.** By utilizing the remaining capacity on
    the Anchor's mask, Tenants gain access to production-grade manufacturing without the prohibitive
    full-mask capital expenditure." Benefits: "**Reduced Capital Risk: Enter production for a 75%
    lower NRE than a dedicated mask set.**" / "Low Volume Support: Economically viable production
    runs starting as low as **10k units per year**." Ideal for "Niche industrial or IoT applications
    (**10k - 50k units**)", "University spinoffs or 'Maker' products", "Secondary chips that do not
    drive the primary system timeline."
  - The specification table: Anchor "Mask Control: Primary (You set the date)", Tenant "Secondary
    (**You match the date**)"; Anchor "NRE Investment: Standard Production Tooling", Tenant "**~25%
    of Standard Tooling**"; Anchor "Volume Target: 100k+ Units / Year", Tenant "10k - 100k Units /
    Year"; "Die Sizes: Full, 1/2, or 1/3 (Relative to Caravel Die)"; Tenant incentives "Volume Access
    (**sub-$5.00 per unit**)".
  - "Technical Baseline: Node: **SkyWater Technology 130nm CMOS**. Delivery: **Singulated, Untested
    Die (Gross Die)**. Optional Services: Wafer Sort (Testing), QFN Packaging, Tape & Reel."
  - The mechanism: "Anchor Commitment: The Anchor defines the tape-out date and underwrites the
    reticle base. **Tenant Enrollment: ChipFoundry opens the 'Tenant Portal,' allowing compatible
    designs to purchase slots on the Anchor's run.** Fabrication: the aggregation mask is generated
    (**owned and managed by ChipFoundry**)… Delivery: Wafers are diced, and independent lots are
    shipped to the Anchor and Tenants respectively."
- **DERIVED:** Tenant NRE at "~25% of Standard Tooling" and "75% lower" are the same statement.
  "Up to $75k" of Anchor rebate, if it is the whole of the Tenant NRE flowing back, implies a
  standard production tooling NRE for which $75k is a plausible fraction — but ChipFoundry publishes
  no absolute NRE figure, so **no dollar tooling cost can be derived from this page.**
- **Bears on:**
  - **The auction design (context, and this is the most directly relevant page ChipFoundry has
    published for this project).** `PRINCIPLES.md` proposes that the right to schedule a run be sold,
    and the repository owner's memory note records that "futures = someone wins the auction for you
    at any cost". **ChipFoundry has shipped a named product that sells exactly that right**:
    "Schedule Sovereignty — the right to determine the tape-out date". It sells it not by auction but
    by **underwriting**: whoever pays the tooling sets the date, and everyone else matches it. And it
    pays the Anchor a **rebate** as Tenants join — i.e. the Anchor is compensated, after the fact,
    for the option value it created. That is a real, deployed, commercial answer to the same problem,
    from the only unsubsidised operator there is, and `PRINCIPLES.md` must engage with it rather than
    reason from first principles.
  - **H5 (supports, cautiously).** The existence of the product implies ChipFoundry believes there is
    a population of customers at 10k–100k units a year who cannot afford a mask set — the tail one
    step up from prototyping. Whether any Anchor or Tenant has actually bought is **not stated
    anywhere**, and the page has no customer names, no case study and no "sold out" marker.
  - **H6 (context).** "Delivery: Singulated, Untested Die (Gross Die)" with sort, packaging and tape
    & reel as options is the cost-to-serve discipline `SMB`-series entries keep finding: the
    profitable version of a long-tail offer strips everything optional out of the base price.
- **Used in:** `CF-16`.
- **Caveats:**
  - **This is a marketing page for a product that may have no customers.** First archived 2026-02-11;
    nothing on the site, in the API or in the GitHub organisation shows an Anchor run existing. Treat
    every number on it as a price list, not as trade.
  - "sub-$5.00 per unit" and "up to $75k" are the only absolute figures and both are bounds, not
    prices.
  - The whole page is contingent on SkyWater accepting a ChipFoundry-owned production mask set; no
    statement from SkyWater is public.

---

## CF-16. Verdict: what ChipFoundry's record actually shows

**The honest headline: there is not enough public data to say whether an unsubsidised,
investor-free open-shuttle business works. There is enough to say what it looks like while it is
being attempted, and that picture is neither an endorsement nor a refutation.**

**What is now established.**

1. **It is a real, continuing, unsubsidised business.** Five shuttles in seventeen months, three
   taped out, two delivered to customers, 89 paying-or-committed slots, roughly **$1.1m a year of
   gross bookings at list price** (`CF-11`). It is not a project or a grant line item. Nobody is
   paying it to exist.
2. **It priced the same physical product 53% above the dead company's price, from its first public
   day, and has not moved that price in seventeen months** (`CF-2`, `CF-8`). If you want one number
   from this file, it is that one: the market's own estimate of how far below cost $9,750 was.
3. **It cut the cadence at the same time** — from four shuttles a year to two, then three, and it
   says so itself (`CF-7`). Higher price, fewer runs, same node. That is what a company optimising
   for survival rather than growth does.
4. **It has never filed with the SEC, and EDGAR does not know its name** (`CF-5`). That is the
   strongest available public corroboration of the "no investors" account, and it is weak evidence:
   a negative.
5. **It has never once filled a shuttle** (`CF-6`). 21 of 28, 23 of 37, 29 of 43 planned; 21 of the
   40 it originally advertised. And its own `interest` figures, which run two to three times its
   slot count, get quietly revised down by 17–23% after the fact.
6. **It publishes its own viability floor: 20 confirmed participants** (`CF-13`). **Every completed
   shuttle has landed just above it** — 21, 23, 29 — and never far above it. **DERIVED:** 20 ×
   $14,950 = **$299,000** is the operator's own number for what a SKY130 MPW run must book to
   proceed.
7. **It is paid in full about nine months before it delivers** (`CF-13`): final payment falls 14
   days before the submission deadline, and delivery lands 193–250 days after tapeout. The operator
   carries no receivable and needs no working capital for the run itself.
8. **It does not rely on the shuttle alone.** It sells reservation options ($500 non-refundable,
   `CF-13`), contest sponsorships (`CF-14`), IP, commercial SRAM, ReRAM, ML, support and design
   review, and it has launched an "Anchor / Tenant" **production** aggregation product (`CF-15`).
   None of that is visible in any number we can derive.

**What that adds up to, stated carefully.**

The business *clears its own bar* — it called GO on its first shuttle when it had "enough project
commitments to cover the costs" (`CF-12`), and it has run every shuttle it committed to since. But
**clearing a per-shuttle cost-recovery bar is not the same as covering a company**, and the gap
between the two is exactly where Efabless died with $2.5m of fresh money five months in the bank
(`CF-5`). The derived **$273,000 of gross bookings per named employee** (`CF-11`) is the number to
watch: it is calculated on a floor headcount of four, it is a ceiling not an estimate, and for a US
semiconductor-services company it is thin. If the real headcount is eight, the figure is not
survivable on shuttle revenue alone — which is presumably why production volumes, IP, SRAM, ReRAM,
ML and support packages are all on the price list behind "Request a Quote", and why none of them is
visible to us.

**And there is one live warning sign.** CI2609 stood at **16 committed on 2026-09-20** against the
published minimum of 20, with a projected tapeout of 2026-09-16 that has already passed (`CF-6`,
`CF-13`). If that number is current, it is **the first ChipFoundry shuttle to reach its tapeout
date below its own stated threshold.** It should be re-read before anything is concluded from it —
`committed` climbs late (`CF-6`) and the API may simply be stale — but it is the single most
informative number anyone could check next.

**Four findings that should change how this repository argues.**

- **Interest is not demand, and the operator agrees.** `CF-6` is the first place in this repository
  where we can watch an operator mark its own funnel down. Every "oversubscribed" figure elsewhere
  in `resources/demand/` is a submission count. This one is a paid count, and it is a third of the
  interest.
- **Commitment arrives at the last possible moment.** CI2605 had **one** committed slot five weeks
  before its commitment date and finished with 29 (`CF-6`). A shuttle looks like a failure until it
  suddenly isn't. Any market design — including this project's auction — that needs a demand signal
  earlier than the deadline is asking for information that does not exist yet.
- **Three independent unsubsidised operators all chose a threshold, not a price.** Efabless's $200
  refundable deposit and "minimum project capacity", ChipFoundry's **20-participant minimum** with a
  $500 non-refundable option fee and a 60-day commitment deadline, and `DEM-10`'s 50% clause
  (`CF-12`, `CF-13`, `PAY-7`). `PRINCIPLES.md` proposes clearing that risk through an auction. **It
  now has to explain why an auction beats the mechanism every practitioner picked**, and "they
  didn't think of it" is not the answer — the answer has to engage with the fact that below a
  threshold there is no price at which a single-customer mask set makes sense.
- **Somebody with a strategic interest pays for the tail; the tail does not pay for itself.**
  ChipFoundry's contest slots are **sold to a sponsor** (`CF-14`), its Tiny Tapeout slots are partly
  **subsidised by ChipFoundry itself** (`CF-9`), and Tiny Tapeout's own shuttles are in turn
  sponsored by IEEE, SwissChips, Tillitis and ChipFoundry (`PAY-6`). Meanwhile the contest funnel is
  **234 proposals → 3 chips, 1.3%**. For a project whose thesis is that a long tail of small
  customers can be served profitably, this is the pattern to answer: **at the thin end, the person
  who wants the chip is not the person who pays for it.**

**And ChipFoundry has already shipped a product that does part of what this project proposes.** The
"Anchor / Tenant" production model (`CF-15`) sells "**Schedule Sovereignty — the right to determine
the tape-out date**" to whoever underwrites the tooling, lets others buy slots on that run at "~25%
of Standard Tooling", and **rebates the Anchor up to $75k as Tenants join**. That is an
underwriting-plus-rebate mechanism for exactly the scheduling right `PRINCIPLES.md` proposes to
auction. Whether anyone has bought it is unknown. Either way, `PRINCIPLES.md` should say how an
auction differs from it and why that difference matters.

**What would settle it, and what we would need.** A single statement of revenue, headcount or
profitability from ChipFoundry; the terms of the Efabless asset purchase; the realised average price
per slot after academic discounts, volume pools, contest sponsorships and Tiny Tapeout subsidies;
whether any Anchor or Tenant has bought a production run; and CI2609's and CI2612's final committed
counts, which will be the first data point on whether 21 → 23 → 29 is a trend. Until then this file
records a company that is **surviving, small, priced to survive, pre-paid, diversifying away from
the shuttle, and not yet demonstrably profitable** — and says no more than that.

---

## Blocked sources, dead ends and things we could not check

| What | What happened | Status |
|---|---|---|
| **Any statement of profitability, revenue, funding or "no investors"** | ChipFoundry publishes no blog, no news page, no press releases and no careers page. `chipfoundry.io/blog`, `/news`, `/shuttles`, `/pricing` and `/terms` all 404 (this repeats the finding in `efabless-and-the-open-shuttles.md`). Nothing on the about page, FAQ, terms or knowledge base touches money beyond the $14,950 list price. | **Not found. The "no investors / profitable from day one" position rests entirely on the repository owner's account and on the negative SEC result in `CF-5`.** |
| **State corporate registry for UmbraLogic Technologies LLC** | The terms of service put the company under "the laws of the State of California", so California's Secretary of State is the right registry. `bizfileOnline.sos.ca.gov`'s business search is a **POST** API; this session was restricted to GET requests only, so it was not queried. Delaware's entity search is also POST-only. | **Blocked by method. The LLC's formation date, managers and registered agent are unknown, and with them the one fact that would settle "in parallel" vs "afterwards" in `CF-1`.** |
| **OpenCorporates** | `api.opencorporates.com/v0.4/companies/search?q=umbralogic` returns HTTP 401, `{"error":{"message":"Invalid Api Token"}}`. Requires an account. | **Blocked (no account created, by policy).** |
| **Web search** | This session's web-search budget was exhausted before the search for a profitability statement could be run. `html.duckduckgo.com/html/?q=…` returns a results-free shell to `curl`. | **Blocked.** |
| **Trade press** | No SemiEngineering, EE Times, Electronics Weekly or Hackaday article about ChipFoundry was reachable without search. The only contemporaneous third-party reporting we found is Tiny Tapeout's own news posts, which are a sponsee writing about a sponsor. | **Partial — one interested source only.** |
| **Conference talks** | FOSSi Dial-Up, ORConf, FOSDEM, Hackaday Supercon and RISC-V Summit slides were not reachable without search, and video transcripts were not attempted. Given `CF-4`'s founders, a talk very probably exists and would be the likeliest place to find a funding or profitability statement. **This is the highest-value unexplored lead.** | **Not attempted.** |
| **ChipFoundry's Spanish-language customer story** | The 2025-09-28 homepage capture carries a headline, "De la comunidad al silicio: una historia de chipIgnite con Silicluster" — in English, "**From the community to silicon: a chipIgnite story with Silicluster**". It is a **webinar**, published to ChipFoundry's YouTube channel on **2025-10-07**; the video itself was not watched and no transcript was retrieved. It is the only named ChipFoundry customer story we found. | **Identified, not watched.** |
| **ChipFoundry's webinars generally** | The channel feed lists sixteen videos from 2025-06-02 to 2026-03-18, including "Webinar - New CLI, OpenFrame, and Production" (2026-02-24) and "Webinar: Systems to Silicon Design Contest" (2026-03-05). **Any of these could contain the revenue, headcount or funding statement this task was looking for.** None was watched: no transcript API was used and video is out of reach of the tools here. **This is now the highest-value unexplored lead, ahead of the conference talks.** | **Not attempted.** |
| **Contest sponsorship prices** | <https://chipfoundry.io/sponsorship> sells "Fabrication of 1 winning project" and "Fabrication of 3 winning projects" packages, both priced "Inquire for Pricing". | **Not published.** |
| **Whether any Anchor or Tenant has bought a production run** (`CF-15`) | Nothing on the site, in the API or in the GitHub organisation names a production customer. | **Not found.** |
| **`/api/v1/shuttles`, `/api/v1/users/me`, `/api/v1/organizations/*`, `/api/v1/support-tickets`** | Return `{"detail":"Not authenticated"}` or 404. No account was created. | **Blocked, by policy.** |
| **The Efabless asset purchase terms** | One sentence exists publicly (`CF-3`). No price, no schedule of assets, no completion date, and no statement of what happened to customer obligations. | **Not found.** |
| **What ChipFoundry charges Tiny Tapeout** | Neither party publishes it; ChipFoundry says only that it subsidises "a portion" (`CF-9`). | **Not found.** |
| **Efabless's failure: the blocked funding round** | The owner's account is that Efabless died when a funding round was blocked by an early investor refusing dilution. `CF-5` establishes a $2.5m single-investor Form D five months before the end, and names the board. **We found no public source for the blocked-round account and it should be recorded as the owner's account only.** | **Owner's account, unverified.** |
| **TT09's 369 designs** | Tiny Tapeout's table still reads "TBD". No public statement of their fate. | **Open.** |
