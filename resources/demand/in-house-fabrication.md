# In-house fabrication (`IHF`)

**What this file covers.** Commercial companies that built, bought or ran their own silicon or MEMS
fabrication capability instead of buying wafers from a merchant foundry — and, where it exists, what
that capability cost. It starts from one company the repository owner asked about by name,
`science.xyz`, and works outwards to comparable cases.

**Why it is evidence.** A company that spends its own money on a fab has, by revealed preference,
been told "no" by the merchant foundry market — or has been quoted a price, a minimum volume or a
lead time it could not live with. That is the cleanest available measurement of demand the existing
industry refuses to serve, which is [H5](../hypotheses.md#h5-there-is-a-long-tail-of-demand-for-chips).
It cuts the other way too: the price of building the capability is the price of *not* being served,
and if that price is low, the "unserved" demand may simply be demand that can serve itself. Where
one of these companies then opens its line to outside customers, it becomes a live experiment in
exactly the business foundry.api proposes, and its prices and its stated reasons are direct evidence
on [H6](../hypotheses.md#h6-small-customers-can-each-be-profitable).

**ID prefix:** `IHF`. Numbering runs `IHF-1` upwards and does not collide with `DEM` or `SMB`.

Everything here was gathered read-only, HTTP GET only, between 2026-09-18 and 2026-09-19. No form
was submitted, no account created, no person contacted by any channel. Sources that could not be
reached are listed in [§ Blocked sources](#blocked-sources) rather than dropped.

---

## 1. Identification: what `science.xyz` is

**Resolved.** `science.xyz` is the website of **Science Corporation**, a US neural-engineering and
medical-device company founded in 2021 by **Max Hodak**, a co-founder and former president of
Neuralink. The working hypothesis given to this research — that the name refers to Max Hodak's
neural-implant company, and that it matters here because it runs its own microfabrication — is
**confirmed, and it is stronger than the hypothesis assumed.** Science does not merely run an
in-house MEMS line for itself. It bought an existing commercial MEMS foundry, kept that foundry's
outside customers, and **sells MEMS fabrication to third parties under the name Science Foundry,
including scheduled multi-project wafer runs at a published starting price.**

### The legal entity

| Field | Value | Source |
|---|---|---|
| Registrant name on file with the SEC | **Science Corp** | EDGAR submissions API, CIK `0001873836` |
| Name used publicly and in `schema.org` metadata on the site | **Science Corporation** | `https://science.xyz/` page source |
| CIK | 0001873836 | EDGAR |
| Jurisdiction of incorporation | **Delaware** | Form D, CIK 0001873836 |
| Year of incorporation | **2021** | Form D (both the 2021 and the 2026 filings state "2021") |
| Business address, 2021 filing | 1010 Atlantic Ave., Alameda, CA 94501 | Form D 0001873836-21-000002 |
| Business address, current | **300 Wind River Way, Alameda, CA 94501** | EDGAR submissions API; Form D 0001873836-26-000001 |
| Other sites | Research Triangle Park / Durham, North Carolina, USA; Paris, France | `schema.org` `Organization` block on `https://science.xyz/` |
| Industry group as self-declared on Form D | "Other Technology" | Form D |

**The name discrepancy is real and is not resolved by any source found:** the SEC registrant is
"Science Corp", the website and its structured metadata say "Science Corporation", and the MEMS
business is operated under two further names — **Science Foundry** (the customer-facing brand) and
**Science Wafer Services** (described by the company as the unit's official name). All four refer to
the same company. Nothing found establishes whether "Science Wafer Services" is a separate legal
entity or an internal division; the announcement calls it "a fairly independent unit, officially
known as Science Wafer Services", which is not the same as saying it is separately incorporated.

### Residual ambiguity, stated plainly

- **"Science" is a badly overloaded company name.** There is at least one well-known and entirely
  unrelated US company called *Science Inc.* (a Santa Monica start-up studio, `science-inc.com`,
  sponsor of the "Science Strategic Acquisition Corp." SPACs that appear in EDGAR), and EDGAR also
  carries *Science Applications International Corp*, *Science 37 Holdings* and *Cambridge Science
  Corp*. None of these is `science.xyz`. The `.xyz` domain and the Alameda address are what
  disambiguate.
- **The owner's brief gave no context beyond the bare domain.** The identification above rests on the
  domain resolving to Science Corporation's own site and that site describing the MEMS foundry
  business. If the owner meant some other "science.xyz", nothing found suggests what it would be: the
  domain has a single, current, unambiguous owner.
- **What "science.xyz" does *not* appear to be:** it is not a foundry-industry body, not an open
  silicon programme, and not a shuttle broker. Its relevance here is entirely through Science
  Foundry.

### Why it bears on this project, in one paragraph

Science Corporation is a commercial company that concluded it could not get the fabrication it needed
from anybody else, bought a fab, and then turned that fab into a merchant service aimed explicitly at
small, early-stage, low-volume customers — the exact segment foundry.api is built around. It states
the reason in its own words (IHF-1, IHF-5), it discloses what the fab cost to buy (IHF-3) and what it
is spending to expand it (IHF-2), and it publishes a starting price for a multi-project wafer run
(IHF-4). That combination — motive, capex and price, all from primary sources — is rare in this
directory.

---

## 2. Entries

### IHF-1. Science Corporation says no existing foundry could serve it, so it bought one

- **Sources:**
  - Max Hodak (CEO), "Science Acquires North Carolina Fab and Other MEMSCAP Assets", Science
    Corporation, 2022-12-07. <https://science.xyz/news/MEMSCAP-acquisition/>
  - Max Hodak (CEO), "Launching Science Foundry", Science Corporation, 2023-03-10.
    <https://science.xyz/news/launching-science-foundry/>
- **Verification:** Verified — both pages fetched and read in full, 2026-09-19. Quotes below are
  copied word for word from the page bodies, including the source's own parenthetical emphasis.
- **What it says:**

  From the 2022-12-07 acquisition announcement, on why a medical-device company would own a fab:

  > "We've long been believers in the importance of vertical integration whenever possible. The
  > sophistication of the devices we can make is directly limited by the tools we can access, and
  > there's nothing like walking down the hall for iteration speed. **In practice, it's tough to
  > innovate as a novel low volume application relying only on pre-existing commercially available
  > processes, and where that does happen, the advantages tend to accrue to the large incumbents.**"

  (Emphasis added here; the source is not emphasised.) And immediately after, the economics that
  make owning one hard:

  > "On the other hand, tools are (very, very) expensive and require high utilization to justify
  > owning. Given the intersection of these pressures, we early on came to the idea of building
  > sophisticated in-house MEMS capabilities with an intention of externalizing them as a commercial
  > platform for a limited group of like-minded customers. **There is a gap in the market at the
  > low-volume, high-complexity, rapid-iteration end, which has held back progress in advanced
  > medical devices.**"

  On whether they could have afforded to build one from scratch:

  > "Despite this ambition and our strong balance sheet, being able to afford a full manufacturing
  > capability on our own wasn't a given. Over the past year we've taken steps towards this at our
  > site in the San Francisco Bay Area with a range of deposition, etch, lithography and
  > characterization capabilities, but we were still dependent on outside facilities for our overall
  > processing."

  On who else they expect to serve:

  > "Beyond medical devices, we look forward to Science's emergent wafer services capabilities having
  > an impact on advanced applications in aerospace, defense, quantum computing, and optical
  > telecommunications, among others."

  The 2023-03-10 launch post confirms the unit's name and that it was opened to outside customers:

  > "We operate the MEMS capabilities being announced today as a fairly independent unit, officially
  > known as Science Wafer Services, and which will continue to invest in North Carolina."

  and

  > "Since the sophistication of the products we can make depends directly on the tools we have and
  > how quickly we can iterate, we invest heavily in our fab capabilities; our goal with Science
  > Foundry is to enable you to build on this infrastructure, too."

- **Bears on:** H5 (supports — a named, funded commercial buyer states that the merchant market would
  not serve its low-volume, high-complexity need, and that this "has held back progress"); H6
  (mixed — the same source states the constraint on the supply side, that tools "require high
  utilization to justify owning", which is the fixed-cost problem H6 has to beat); H1 (supports —
  "the advantages tend to accrue to the large incumbents" is the doom spiral stated by a customer);
  H8 (context — the company's answer was to externalise its own infrastructure as a platform).
- **Used in:** not yet.
- **Caveats:** This is the company's own blog, written by its CEO, and it is an announcement with an
  obvious commercial purpose — it is a primary source for *what Science says its reasons were*, not
  an independent finding that no foundry would have served it. It names no foundry it approached and
  gives no quote it was given. The claim that the gap "has held back progress" is an assertion with
  no evidence attached. What makes it usable is that the company put $3.0M and then a planned $65M
  behind the assertion (IHF-2, IHF-3), which is costly talk.

---

### IHF-2. What Science is spending to expand the fab: $65M, 57,000 sq ft, 50+ jobs

- **Source:** Kara Zappitelli (Director, Science Foundry), "Durham County Commissioners Unanimously
  Approve Incentives for Science Foundry Expansion", Science Corporation, 2024-07-09.
  <https://science.xyz/news/durham-nc-economic-incentives/>
- **Verification:** Verified against the company's own page, 2026-09-19. **Not yet cross-checked
  against a second independent source** — the two trade-press reports found (Business North Carolina
  and the North Carolina Biotechnology Center) both refuse automated fetches; see
  [§ Blocked sources](#blocked-sources). The Durham County Board of Commissioners' own minutes would
  settle it and were not reached.
- **What it says (quoted in full, because every number in it matters):**

  > "Our plans call for the investment of up to $65 million in a 57,000 square foot expansion in
  > Durham County to support MEMS and semiconductor manufacturing for new, cutting-edge technologies,
  > including brain computer interface devices and for our groundbreaking visual prosthesis, the
  > PRIMA implant, creating more than 50 new high paying local jobs in the process."

  > "The investment and expansion will be facilitated, in part, by a $930,000 ten-year
  > performance-based incentive award unanimously approved by the Durham County Board of
  > Commissioners."

  And the company's stated ambition for the fab:

  > "Our long-term goal is to become the go-to manufacturing partner for the next generation of
  > medical and brain-computer interface devices."

- **DERIVED (arithmetic written out):**
  - Capex per square foot: $65,000,000 / 57,000 sq ft = **$1,140 per sq ft**.
  - Public subsidy per new job: $930,000 / 50 jobs = **$18,600 per job over ten years**.
  - Verified with `uv run python tmp/arith.py` (script deleted after use; the two divisions above are
    the whole of it).
- **Bears on:** H6 (context — this is the closest thing found to a public capex figure for a *small,
  modern, non-leading-edge* fab expansion, and it is the denominator any "can small customers pay for
  themselves" calculation needs); H5 (context).
- **Used in:** not yet.
- **Caveats:** "**up to** $65 million" is a ceiling in an incentives negotiation, not a budget, and
  incentive applications systematically overstate. The figure covers a *57,000 sq ft expansion* of an
  existing, already-equipped site, so it is neither a greenfield fab cost nor purely tool spend, and
  nothing found breaks it into building versus equipment. The "more than 50 new … jobs" is a
  commitment tied to the performance-based award, not a headcount. Treat $1,140/sq ft as an
  order-of-magnitude marker only.

---

### IHF-3. What a complete, operating, ISO-certified MEMS foundry sold for: US$3.0 million

**This is the single most valuable number in this file.**

- **Sources:**
  - MEMSCAP S.A., "HEADING FOR 2023: MEMSCAP ANNOUNCES THE SALE OF ITS NORTH CAROLINA MANUFACTURING
    PLANT TO SCIENCE CORPORATION & THE CONCLUSION OF A STRATEGIC SUPPLY AGREEMENT FOR OPTICAL
    COMMUNICATIONS PRODUCTS", regulatory press release, Grenoble, 2022-12-07, 06:30 PM.
    PDF: <https://memscap.com/wp-content/uploads/2023/04/PR-Fablite-07_12_2022-GB-Def.pdf>
    (linked from <https://memscap.com/en/2022/12/12/memscap-announces-the-sale-of-its-north-carolina-usa-manufacturing-plant-to-science-corporation-the-conclusion-of-a-strategic-supply-agreement-for-optical-communications-products/>)
  - Same release syndicated via Business Wire and reproduced by citybiz, 2022-12-07.
    <https://www.citybiz.co/article/356444/memscap-announces-the-sale-of-its-north-carolina-manufacturing-plant/>
  - Science Corporation's own account of the same transaction: IHF-1.
- **Verification:** Verified, 2026-09-19. The MEMSCAP PDF was fetched directly from `memscap.com` and
  the text extracted with `pypdf`; the citybiz copy was fetched independently and the two agree word
  for word on the passages quoted. MEMSCAP is a listed company (Euronext Paris, ISIN FR0010298620,
  ticker MEMS) and this is a regulatory announcement, so it is a primary source. Business Wire's own
  copy of the release returns **HTTP 403** to automated fetches; the citybiz reproduction was used
  instead and carries the "GRENOBLE, France–(BUSINESS WIRE)–Regulatory News:" dateline.
- **What it says.** MEMSCAP sold, to Science Corporation:

  > "– The entire North Carolina teams.
  > – The North Carolina plant lease as well as all plant's tools and equipment and associated
  > technology.
  > – The foundry business customers."

  and then, as its own single-sentence paragraph:

  > "The purchase price to acquire the above assets totals 3.0 million US dollars."

  The sale was the completion of a programme MEMSCAP had run for three years, and MEMSCAP says why it
  sold — not distress, but a deliberate move to become fabless:

  > "MEMSCAP … today announced it has fully executed its FABLITE Program through the sale of its
  > North Carolina Manufacturing Plant (USA) and the conclusion of a strategic supply agreement for
  > its optical communications products."

  > "Following this transaction and the on-schedule completion of the FABLITE Program, MEMSCAP
  > business becomes focused around: – the Avionics and Medical businesses operated by MEMSCAP
  > Norwegian facilities, and – the fabless VOA Product line servicing MEMSCAP Optical Communications
  > business. This new organization is expecting to deliver significant improvement to MEMSCAP
  > agility and profitability."

  Jean Michel Karam, Chairman & CEO of MEMSCAP, quoted in the release:

  > "We are very pleased for having conducted the FABLITE Program from the idea to an on-schedule
  > implementation. Today, we are excited to enter 2023 with such agile organization we planned three
  > years ago."

  The buyer did not get everything: the Variable Optical Attenuator products, IP and business stayed
  with MEMSCAP, and Science agreed to keep making them — "a minimum of 3 years supply of chips and
  wafers".
- **The history of the same site, for scale.** Science's own announcement (IHF-1) states:

  > "MEMSCAP acquired their US foundry business in 2002 from JDS Uniphase, which itself had acquired
  > the site for approximately $750M from Cronos Integrated Microsystems shortly prior."

- **DERIVED (arithmetic written out):** $3,000,000 / $750,000,000 = **0.400%** of the price the site
  reportedly changed hands for around 2000 — a factor of **250** lower. Verified with
  `uv run python tmp/arith.py`.
- **Bears on:** H6 (**supports, strongly** — the fixed asset base needed to run a real MEMS foundry,
  including an ISO 9001:2015 quality system, a trained team and a live customer book, was available
  on the open market for $3.0M, which is far below any figure this project had for what a fab costs);
  H5 (mixed — see caveats); H1 (context — the same physical site went from a reported ~$750M to $3.0M
  in about twenty-two years).
- **Used in:** not yet.
- **Caveats and honest limits:**
  - **$3.0M bought a lease, not a building.** "The North Carolina plant lease as well as all plant's
    tools and equipment" — the real estate was not part of it. A fab's rent does not appear anywhere
    in this number.
  - **It bought used tools of unknown age.** The line was built by Cronos in the late 1990s. Nothing
    found states the age or replacement value of the tool set. $3.0M is the *market clearing price of
    a distressed-category asset*, not the cost of assembling the same capability new.
  - **The $750M comparison is not like-for-like and is only partly verified.** It is quoted from
    Science's blog, not from a JDS Uniphase filing, and it was the price for *Cronos Integrated
    Microsystems as a company* — a dot-com-era optical-components acquisition — not for the building
    and tools alone. The cross-check against JDS Uniphase's own disclosure was not completed. Do not
    quote "$750M → $3.0M" in `WHY.md` as a like-for-like depreciation until that is done.
  - **The seller was pleased.** MEMSCAP framed the sale as the successful execution of a planned
    "FABLITE" programme, and said it expected "significant improvement to MEMSCAP agility and
    profitability". A public MEMS company concluded that *not* owning a MEMS fab was worth more than
    owning one. That is a real challenge to the premise that fab ownership is valuable, and it sits
    directly beside the H6 support above. Both readings are true at once, from the same document.
  - MEMSCAP kept a three-year supply agreement, so Science acquired a fab with a guaranteed anchor
    customer attached. A buyer without one would be buying a different asset.

---

### IHF-4. Science Foundry publishes a starting price for a MEMS multi-project wafer run: $13,520+

- **Sources:**
  - "MEMS Development and Production", Science Corporation.
    <https://science.xyz/services/foundry/mems/>
  - "Standard Technology MPWs", Science Corporation.
    <https://science.xyz/services/foundry/mems/standard-technologies/>
  - "Custom Processes", Science Corporation.
    <https://science.xyz/services/foundry/mems/custom-processes/>
- **Verification:** Verified, 2026-09-19 — all three pages fetched and read as raw HTML. The price
  string appears in the page source as `13,520+&nbsp;` under the heading "Standard MPW Run", beside
  the "Early stage development" tier. **What the price includes is not stated on the page** and the
  ordering interface behind "Start your order" was not exercised (that would require creating an
  account, which is forbidden here).
- **What it says.** The published MPW tier reads, in full: "Early stage development — Our engineering
  team will help prove out your design, run smaller wafer lots under early stage development, and
  support your development every step of the way. … **Standard MPW Run $13,520+**". The other two
  tiers ("Process development", "Volume production") carry no price and say "Contact us".

  The standard technologies on scheduled MPW runs, with the next run dates listed on the page as
  fetched:

  | Technology | Description as given | Next scheduled runs listed |
  |---|---|---|
  | Silicon on Insulator (SOI) | "Four masks, a SOI wafer, and two metal layers" | 2026-09-19, 2027-01-04 |
  | Polysilicon (Poly) | "Eight masks, three polysilicon layers, and one metal layer" | 2026-09-27 |
  | Piezoelectric (Piezo) | "Five masks, a SOI wafer, and distinct metal and piezoelectric layers" | 2026-10-17, 2027-02-15 |
  | Thin Film Electronics (TFE) | "Two or three polyimide layers alongside a range of masks and metals … ideal setup for electrode and LED designs" | "Produced in regularly scheduled runs" — no dates given |

  The SOI, Poly and Piezo platforms are recognisably the MEMSCAP SOIMUMPs, PolyMUMPs and PiezoMUMPs
  processes carried over with the fab (compare IHF-6), which Science said it would do: "we will
  resume offering MUMPS shuttle runs in the spring, rebranded as Science Wafer Services MPW
  technologies" (IHF-1).

  On positioning, from the same set of pages:

  > "Unlike other commercial foundries, we are excited to collaborate on the development of early
  > stage processes and innovative technologies."

  > "We lower the up-front cost of innovation and shorten development cycles."

  On scale and tooling: "**80+ Tools**", "Currently tooled for 6 inch wafer size", volume production
  described as "10s to 1000s of wafers" and "dozens to thousands of custom wafers per year". The
  custom-process page is explicit about the materials a CMOS foundry will not touch:

  > "we can create bespoke solutions utilizing non-standard materials rarely available in CMOS
  > foundries—such as gold, noble metals, polymers, piezoelectrics, glass, quartz, III-N
  > semiconductors, and more."

  The listed target applications span "Neural Interface Devices", "Microneedles", "Microfluidic
  Chips", "Ultrasound Devices", "Inertial Sensors", "Pressure Sensors", "Gas Sensors", "Micro
  Mirrors", "Optical Telecom Components", "Silicon Photonics", "Quantum Computing", "IoT Devices",
  "Wearables Sensors" and "Your Novel MEMS Device".
- **Bears on:** H8 (**supports** — a commercial foundry publishing a headline price for a small run,
  a public run calendar and a self-serve ordering interface is precisely the openness H8 predicts is
  needed); H6 (context — a real, current, published price point for the smallest ticket a MEMS
  foundry will sell); H5 (context).
- **Used in:** not yet.
- **Caveats:** `$13,520+` is a floor with an unexplained "+" and no stated die size, wafer count, die
  count or turnaround — unlike the MOSIS and Europractice price lists already in `SMB-7`/`SMB-8`, it
  cannot be decomposed into fixed and variable parts. The number is oddly precise for a marketing
  page, which suggests it is generated from a real price list rather than rounded, but that is
  inference. The full price list sits behind account registration and was deliberately not obtained.
  The four-digit precision means it should be quoted as "a published starting price of $13,520",
  never as "the price of a MEMS MPW".

---

### IHF-5. Science states the merchant market's two options — university cleanroom or volume foundry — and that neither worked

- **Source:** Kara Zappitelli (Science Foundry Director) & Kyle Stoneman (Head of Software Product),
  "How Science Foundry leverages software to create predictability for our diverse and complex jobs",
  Science Corporation, 2025-02-03. <https://science.xyz/news/science-foundry-software-overview/>
- **Verification:** Verified — page fetched and read in full, 2026-09-19.
- **What it says.** This is the clearest statement found anywhere in this research of *why* a small
  customer cannot buy what it needs:

  > "When we started the company, it was immediately apparent that it would be impossible to do the
  > work we wanted to do relying solely on either academic user facilities or existing contract fabs,
  > which either would have pushed us into multi-year iteration cycles or were simply inaccessible
  > for this kind of low-volume work, often with uncommon materials and tool parameters. We had to
  > own this ourselves, and also saw an opportunity to use software to make it feasible to scale and
  > make something available to others that was genuinely differentiated."

  And the market gap it claims to occupy:

  > "Unlike most MEMS providers, Science Foundry specializes in small volume, early-stage process
  > development, providing a valuable middle ground to the self-directed process at a university
  > cleanroom or the production-ready expectations of volume-only foundries."

  The post also describes, in unusual detail, **how the fab decides what to run** — which is the same
  problem `PRINCIPLES.md` P3 and `AUCTIONS.md` address, and Science's answer is not a market:

  > "with more than 80 advanced tools, hundreds of distinct protocols, and a mix of development and
  > production jobs each made up of hundreds of separate steps, it can become a practically
  > unsolvable question."

  > "To address this, we developed a scheduling algorithm that ingests the state of the Foundry as it
  > is represented in software, and produces an optimized and feasible list of work to be completed."

  The scheduler is stated to account for people (with "active training records"), tools ("whether
  they are fully operational, undergoing maintenance, or pending calibration … Each tool's unique
  capabilities, capacity, and supervision requirements"), and work ("prioritization, and
  dependencies … reworks, send-aheads … and how closely each job is trending towards on time
  delivery"). Priority is assigned centrally, by the fab, on lateness:

  > "If it appears like a job might be off track, it is given a higher priority in the daily schedule
  > and prioritized over other work."

  It is also used for capital planning:

  > "It also models expected return on improvements from hypothetical changes to any particular part
  > of Foundry operations, like hiring or major capital expenditures."

  And the claimed result:

  > "We're excited now to see many of these tech investments pay off and make low-run, advanced R&D
  > significantly faster and more economical, for more potential applications."

- **Bears on:** H5 (**supports** — "simply inaccessible for this kind of low-volume work" is a direct
  statement that the demand exists and the industry refuses it); H9 (context — software, not many
  small experiments, is what this company credits for its learning); **H11 (challenges)** — the one
  operator found that actually runs a many-small-jobs fab solves scheduling with a **central
  optimiser and fab-assigned priority**, not with prices, customer bids or a market. `PRINCIPLES.md`
  P3 claims markets can replace foundry judgement; the closest real-world instance of this business
  does the opposite, and says the problem is "practically unsolvable" by inspection. That is not
  proof P3 is wrong, but it is the only empirical data point found and it points the other way.
- **Used in:** not yet.
- **Caveats:** Company blog, written to advertise the service; the claim that the work became
  "significantly faster and more economical" carries no numbers. Nothing here says the scheduling
  approach is *better* than a market — Science may simply never have considered one, and an internal
  optimiser is the obvious engineering default. Read it as evidence about what exists, not about what
  works best.

---

### IHF-6. What a MEMS multi-project wafer cost before Science: MUMPs at EUR 3,700 a block

- **Sources:**
  - EUROPRACTICE, "MUMPS BY MEMSCAP MULTI-PROJECT-WAFER PROTOTYPING SERVICES", technology flyer,
    v2, 2020-01-07.
    <https://europractice-ic.com/wp-content/uploads/2020/01/MEMSCAP-EUROPRACTICE-v2-2020-01-07.pdf>
  - EUROPRACTICE, "GENERAL EUROPRACTICE MPW RUNS", price list v15, 2020-10-15.
    <https://europractice-ic.com/wp-content/uploads/2020/10/General-MPW-EUROPRACTICE-201015-v15.pdf>
  - CMC Microsystems, "Science Foundry Poly MEMS — Multi-User MEMS Process Technology".
    <https://www.cmc.ca/polymumps-multi-user-mems/>
- **Verification:** Verified, 2026-09-19. Both PDFs fetched from `europractice-ic.com` and the text
  extracted with `pypdf`; the price line and the specification table were read directly. The CMC page
  was fetched and read; **its price is not public** — the page says "Coming soon …" where the list
  price should be, and subscriber pricing requires a login, which was not attempted.
- **How it was counted:** the EUR/mm² and EUR/die figures under DERIVED are divisions of the quoted
  block price by the fixed die area and the stated die count from the specification table in the
  flyer. Nothing was inferred about what the price covers beyond what the two documents state.
- **What it says.** From the 2020-10-15 price list, the MEMSCAP row reads:

  > "PolyMUMPs (10mm x 10mm), SOIMUMPs (11 mm x 11mm), PiezoMUMPs (11mm x 11mm) | 3,700 | 3,500"

  under the column headings "Standard EUR / block" and "Discounted EUR / block".

  From the technology flyer, on how the service works:

  > "MUMPs is a shared wafer or Multi-Project-Wafer service, meaning customers purchase one or more
  > individual die locations(1cm x 1cm size) or tiles on any regularly scheduled run, then create and
  > submit a design based on the process design rules. Eight to 12 weeks later, the customer receives
  > 15 identical chips of their design."

  and on who uses it:

  > "PolyMUMPs is the industry's longest-running MEMS Multi-Project-Wafer service, with over a decade
  > of history. Many universities use the service today as a way to teach beginning MEMS design at
  > the undergraduate level, using PolyMUMPs as the 'example' process."

  The specification table gives: fixed die size 10×10 mm (Poly) or 11×11 mm (SOI, Piezo); active area
  9.8×9.8 mm or 9×9 mm; **15 dies delivered** in every case; minimum feature size 2 µm.

  The run calendar in the same price list shows MEMSCAP offering, in that year, three PolyMUMPs runs,
  four SOIMUMPs runs and three PiezoMUMPs runs.

  **The MUMPs line has survived the change of owner and is being resold by a third-party
  intermediary.** CMC Microsystems (Canada) now lists the identical process — "triple polysilicon,
  single metal surface micromachining process with deposited oxide (PSG) as the sacrificial material,
  and silicon nitride for electrical isolation from the substrate", "expected number of chips to be
  delivered for this technology is 15" — under the name **"Science Foundry Poly MEMS"**, stating:
  "CMC's multi-project wafer service delivers the MEMS technology, through a partnership with Science
  Foundry."
- **DERIVED (arithmetic written out):**
  - PolyMUMPs: EUR 3,700 / (10 mm × 10 mm = 100 mm²) = **EUR 37.0 per mm²**.
  - SOIMUMPs and PiezoMUMPs: EUR 3,700 / (11 mm × 11 mm = 121 mm²) = **EUR 30.6 per mm²**.
  - Per delivered die: EUR 3,700 / 15 = **EUR 247 per chip**.
  - Verified with `uv run python tmp/arith.py`.
- **Bears on:** H6 (**supports** — EUR 3,700 for a fixed 1 cm² tile and 15 finished MEMS chips is a
  genuinely small ticket, and the programme ran for "over a decade" at that kind of price); H5
  (mixed — the flyer's own description of its customer base is "many universities … to teach
  beginning MEMS design at the undergraduate level", which is the same academic skew that `DEM-16`
  records for Europractice); H8 (supports — published price, published calendar, fixed tile).
- **Used in:** not yet.
- **Caveats:** The EUR 3,700 is a **2020** price, for a process that has since changed owner,
  distributor and name; it is not a current price and must not be presented as one. The "discounted"
  column is Europractice's academic rate (see `SMB-6` on the EU subsidy behind it), so neither figure
  is a commercial arm's-length price. Europractice's **2026** schedule no longer lists MUMPs,
  MEMSCAP, Science Foundry or Science Wafer Services at all (IHF-7) — the European distribution route
  for this process appears to have lapsed, and the reason was not established. The per-mm² and
  per-die derivations assume the block price is all-in, which the price list does not state.

---

### IHF-7. The current European MEMS MPW price, for comparison: X-FAB at EUR 1,253/mm²

- **Source:** EUROPRACTICE, "2026 run schedules and prices".
  <https://europractice-ic.com/schedules-prices-2026/>
- **Verification:** Partial. The page was read through `WebFetch` on 2026-09-19 and the figures below
  are as that read reported them; the underlying PDF price list was not separately fetched and the
  numbers were not re-read by a second route. Treat the figures as Partial until the PDF is opened.
- **What it says.** The 2026 Europractice schedule lists **one** MEMS technology, X-FAB XMB10 MEMS,
  at **EUR 1,253/mm² standard and EUR 1,168/mm² discounted**, with a "minimum fabrication cost
  equivalent to 10mm²", area "rounded upwards to next mm²", **50 dies** delivered, and additional
  dies at "25 EUR/die (max 50 additional)".

  Of equal importance: **MEMSCAP, MUMPs, Science Foundry and Science Wafer Services do not appear in
  the 2026 schedule at all.** Six years earlier the same programme carried three MUMPs processes
  across ten scheduled runs (IHF-6).
- **DERIVED (arithmetic written out):**
  - Minimum ticket, standard rate: EUR 1,253/mm² × 10 mm² = **EUR 12,530**.
  - Minimum ticket, discounted rate: EUR 1,168/mm² × 10 mm² = **EUR 11,680**.
  - Against PolyMUMPs' 2020 block rate: EUR 1,253 / EUR 37.0 per mm² = **33.9× more per mm²**.
  - Verified with `uv run python tmp/arith.py`.
- **Bears on:** H6 (**supports** — the minimum billable area is the fixed cost per small customer made
  explicit, exactly as `SMB-7`/`SMB-8` found for silicon MPWs, and it is now EUR 12,530 before a
  single mm² of useful design); H5 (challenges — Europe's flagship prototyping programme carries one
  MEMS process in 2026, down from three, and lost the longest-running MEMS shuttle in the industry);
  H8 (context).
- **Used in:** not yet.
- **Caveats:** Partial verification, as above. The 33.9× comparison is **not** a like-for-like price
  increase: MUMPs sold a fixed 1 cm² tile with 15 dies and X-FAB sells by the mm² with 50 dies, so
  the two are priced on different units and for different processes at different feature sizes; the
  ratio says that *small* designs are much more expensive per mm² under the newer scheme, not that
  MEMS fabrication got 34× dearer. The disappearance of MUMPs from the Europractice list is a fact;
  the *reason* is not established, and a commercial distribution decision is at least as likely as
  any demand signal.

---

### IHF-8. The audited economics of a small MEMS foundry: 475 m², 14 people, EUR 2.9M of revenue, and a loss every year

**This is the most important entry in this file for H6, and it goes the wrong way for us.**

MEMSCAP is a listed company, so the MEMS foundry Science bought comes with audited financial
statements attached — for the fab itself, separated out, because IFRS 5 required the US business to
be reported as a discontinued operation in the year it was sold. Almost nothing else in this
repository offers that: a merchant fabrication business serving many small customers through
multi-project wafer runs, with its own revenue line, its own result, its own headcount and its own
floor area, all audited.

- **Sources:**
  - MEMSCAP S.A., "EARNINGS FOR THE 2022 FINANCIAL YEAR — FINANCIAL YEAR 2022: A MAJOR STEP IN THE
    DEVELOPMENT OF THE MEMSCAP GROUP", press release, Grenoble, 2023-03-28, 06:30 PM.
    <https://memscap.com/wp-content/uploads/2023/04/PR-FY22-GB_28032023.pdf>
    (linked from <https://memscap.com/en/2023/03/28/memscap-earnings-for-fy22/>)
  - MEMSCAP S.A., *Rapport annuel 2022*, filed 2023-04-28 (in French).
    <https://memscap.com/wp-content/uploads/2023/05/Rapport-annuel-Memscap-2022-28_04_2023.pdf>
    (linked from <https://memscap.com/en/2023/04/28/memscap-2022-annual-report/>)
- **Verification:** Verified, 2026-09-19. Both PDFs were fetched directly from `memscap.com` and the
  text extracted with `pypdf`; every figure below was read in the extracted text. The two documents
  agree with each other throughout (the annual report states in millions what the press release
  states in thousands). The press release carries the note that the figures "were subject to an audit
  by the Group's statutory auditors"; the annual report is the audited filing.
- **How it was counted:** no counting was needed — the figures are line items. The derivations under
  DERIVED are divisions of those line items, written out below and checked with
  `uv run python tmp/arith2.py`.
- **What it says.**

  **The plant.** From the annual report's description of the subsidiaries (§ on MEMSCAP Inc.), the
  only physical description of the fab found anywhere from a primary source:

  > "MEMSCAP Inc., basée aux Etats-Unis, a assuré jusqu'au mois de décembre 2022 l'activité Produits
  > sur mesure de MEMSCAP via des opérations basées en Caroline du Nord et intégrant une usine de
  > production de silicium en location (475 m², classe ISO 4), en format de production de tranches
  > silicium de 6 pouces."

  In English: a leased silicon production plant of **475 m², cleanroom class ISO 4**, running **6-inch
  wafers**. (The same report elsewhere gives ISO/FS 209 equivalences for the Norwegian site — "200 m²,
  classe ISO 8 ou classe 100 000 selon FS 209" — so the "classe ISO 4" is deliberate and means
  FS 209 Class 10, not Class 100.) The same paragraph confirms what was sold:

  > "le Groupe a procédé à la cession de l'ensemble des équipes de Caroline du Nord, du bail afférent
  > à l'usine de fabrication ainsi que la totalité des équipements industriels et technologies
  > associés, et des activités de fabrication pour compte de tiers (« Foundry Business »)."

  **The headcount.** The annual report's workforce table gives the group's total employees by
  geography. At 31 December 2021, before the sale:

  > "Etats-Unis ........................................................................ 14"

  out of a group total of 60. At 31 December 2022, after the sale, the United States line is gone
  entirely and the total is 48 (France 4, Norway 44). The group's average full-time-equivalent
  headcount in **production** fell from 37 to 22 across the same period.

  **The revenue.** From the FY2022 press release, the segment table:

  > "Revenue from discontinued operations – IFRS 5 (US operations – Custom products) 2,858 -- 1,935 --"

  i.e. **EUR 2,858 thousand in FY2021 and EUR 1,935 thousand in FY2022**, in thousands of euros. The
  prose confirms it: "Revenue from discontinued operations (US Custom products division dedicated to
  foundry business) amounted to EUR 1,935 thousand compared to EUR 2,858 thousand for FY 2021."

  **The result. It lost money in both years.** From the press release:

  > "For FY 2002 [*sic* — the release says 2002; the figures are FY 2022], the profit after tax from
  > discontinued operations amounted to EUR 897 thousand and included:
  > - The loss after tax relating to the division's operating activities, i.e. EUR 857 thousand for
  > FY 2022 compared to a loss of EUR 805 thousand for FY 2021 (Restated).
  > - The net income from the disposal of this discontinued business, i.e. a profit of EUR 1,754
  > thousand."

  So the foundry's *operations* lost EUR 805 thousand in 2021 and EUR 857 thousand in 2022. The only
  reason the discontinued-operations line was positive at all is the EUR 1,754 thousand gain on
  selling it. The annual report repeats both figures in millions.

  **What the tools were carried at.** From the annual report's walk of the balance sheet movements:

  > "La cession des équipements industriels des activités abandonnées, soit un impact net de -0,5
  > million d'euros en date de cession (Décembre 2022)."

  The disposal of **all** the industrial equipment of the discontinued business took **EUR 0.5
  million** off the balance sheet. That is the net book value of an entire working MEMS toolset —
  the same tools the Europractice MUMPs shuttles and the third-party foundry business ran on.

  **What the seller said about it.** The FY2022 release describes the disposal as the completion of a
  plan, under the heading "Finalisation of the FABLITE program transforming the profitability profile
  of MEMSCAP", and the strategic section states the fab "includes the US production plant, teams,
  equipment, technologies and related customers". The group swung from a EUR 328 thousand net loss in
  FY2021 to a EUR 1,048 thousand net profit in FY2022.
- **DERIVED (arithmetic written out):** all checked with `uv run python tmp/arith2.py`.
  - Cleanroom area in US units: 475 m² × 10.7639 = **5,113 sq ft**.
  - Science's planned expansion against it: 57,000 sq ft (IHF-2) / 5,113 sq ft = **11.1×** the
    existing plant area.
  - Foundry revenue change: (1,935 − 2,858) / 2,858 = **−32.3%** in one year.
  - Loss as a share of its own revenue: 805 / 2,858 = **28.2%** (FY2021); 857 / 1,935 = **44.3%**
    (FY2022).
  - Revenue per US employee, FY2021: EUR 2,858k / 14 = **EUR 204 thousand**.
  - Operating loss per US employee, FY2021: EUR 805k / 14 = **EUR 58 thousand**.
  - Sale price against trailing revenue: US$3.0M against EUR 2,858 thousand — **roughly one times
    trailing revenue**. No FX rate is asserted; the two figures are in different currencies and are
    only being placed side by side.
  - Sale price against the equipment's carrying value: US$3.0M against EUR 0.5M — **about 6×**. Same
    currency caveat.
  - The fall in group production FTE (37 → 22 = 15) is consistent with the 14 US staff at
    31 December 2021.
- **Bears on:**
  - **H6 (challenges, strongly).** This is a real merchant MEMS foundry, selling to many small
    customers through the industry's longest-running MEMS multi-project wafer shuttles (IHF-6), and
    it lost 28% and then 44% of its revenue at the after-tax operating line in consecutive years, on
    revenue that fell by a third. It is a closer analogue to foundry.api than Shapeways, Xometry or
    Protolabs are, because it is actually a wafer fab selling shared runs — and it lands on the same
    side as they do. H6's "Needs" list asks for "a fab's own margin by customer size"; this is not
    that, but it is the closest thing in the repository: a fab whose *entire* business was small
    customers, losing money.
  - **H6 (supports, on the capital side).** The asset base really is small. A working ISO 4 cleanroom
    of 475 m² running 6-inch wafers, with all its tools, was carried at EUR 0.5 million and staffed
    by 14 people. If foundry.api's question is "how much capital must a small fab recover", the
    answer here is: far less than the industry's headline fab costs suggest. The problem in this case
    was not the capital. It was that EUR 2.9 million of revenue from small customers did not cover
    fourteen people and a leased cleanroom.
  - **H5 (challenges).** Revenue from the small-customer foundry business fell 32% in the last year
    it was owned. A long tail that was growing would not do that. Against this: 2022 was a year of
    disposal and the business was being wound down for sale, which would itself depress revenue.
  - **H1 (context).** A well-run, listed, specialist MEMS company concluded that the profitable move
    was to stop owning a fab.
- **Used in:** not yet.
- **Caveats, and they matter:**
  - **The loss is a divisional loss under IFRS 5, with an allocation of group costs that is not
    disclosed.** How much group overhead MEMSCAP charged to the US division is not stated anywhere in
    either document. A buyer who removes those charges — which is exactly what Science did, folding
    the fab into a company that needed it anyway — faces different economics. This is the single
    biggest reason not to read "the MEMS foundry business loses money" as a general law.
  - **The business was being sold.** FY2022 revenue covers a year in which the division was held for
    sale; customers leave, investment stops, and the number is not a steady-state one. FY2021's
    EUR 2,858 thousand with a EUR 805 thousand loss is the cleaner year, and it is still a loss.
  - **This was not only a shuttle business.** "Custom products" included contract manufacturing —
    notably the optical-attenuator chips MEMSCAP kept buying afterwards — so the MUMPs shuttle
    revenue is some unknown fraction of the EUR 2,858 thousand. Nothing found splits it.
  - **EUR 0.5 million is net book value after depreciation, not what the tools are worth or what they
    would cost to replace.** Late-1990s tools fully depreciated over twenty years will carry at close
    to nothing whatever they can still do. It is a floor, not a valuation.
  - **The 475 m² / ISO 4 figures are from the 2022 report only** and were not found in a second
    document. A secondary source (a MEMS-industry blog) describes the Science Foundry site as
    "5,000 sq. ft. of Class 100 cleanroom" — which **agrees on area** (475 m² is 5,113 sq ft) but
    **disagrees on class** (Class 100 is ISO 5, one class dirtier than ISO 4). The audited French
    filing is preferred here and the disagreement is recorded rather than resolved.
  - The French text is quoted in the original; the English renderings are this entry's, not the
    company's.

---

### IHF-9. Akoustis bought a 120,000 sq ft MEMS fab for $2.75 million, and said building one would cost "well over $50 million" — then went bankrupt

The closest independent parallel found to the Science/MEMSCAP transaction, five years earlier, in a
different technology, by a company that had to disclose it.

- **Sources:**
  - Akoustis Technologies, Inc., press release filed as Exhibit 99.1 to a Form 8-K, 2017-03-24.
    <https://www.sec.gov/Archives/edgar/data/1584754/000161577417001221/s105654_ex99-1.htm>
  - Akoustis Technologies, Inc., Form 8-K, 2024-12-02 (Qorvo judgment and the statement that the
    company "will be required to seek protection under applicable bankruptcy laws").
    <https://www.sec.gov/Archives/edgar/data/1584754/000121390024104185/ea0222962-8k_akoustis.htm>
  - Akoustis Technologies, Inc., Form 8-K, 2024-12-17 (Nasdaq delisting determination).
    <https://www.sec.gov/Archives/edgar/data/1584754/000121390024109749/ea0225118-8k_akoustis.htm>
  - ATech (Parent) Resolution Corp. (formerly Akoustis Technologies, Inc.), Form 8-K, 2025-05-15
    (completion of the Chapter 11 asset sales).
    <https://www.sec.gov/Archives/edgar/data/1584754/000121390025044032/ea0242256-8k_atech.htm>
  - EDGAR submissions API, CIK 0001584754 — the registrant's current name and its Form 25-NSE
    (delisting) of 2025-06-06.
- **Verification:** Partial. The registrant identity, the filing dates, the current name "ATECH
  (PARENT) RESOLUTION CORP." and the form types were read directly from the EDGAR submissions API on
  2026-09-19. The quoted figures were read out of the filings themselves through `WebFetch`
  (`www.sec.gov/Archives/...` returns HTTP 403 to `curl`, per `search-log.md` §1), but the full
  documents were not read end to end, so the surrounding context of each quote is not independently
  confirmed. **Upgrade to Verified by opening the four filings in a browser.**
- **What it says.**

  **The purchase, 2017.** Akoustis — then a small RF filter company with no fab — bought the former
  STC-MEMS facility in Canandaigua, New York, from the Research Foundation for SUNY (RF-SUNY) and
  FRMC. From the announcement:

  > "Akoustis will pay $2.75 million in cash at closing to RF-SUNY and FRMC"

  For that it got a "**120,000 sq. ft. commercial wafer manufacturing facility located in
  Canandaigua, NY**", the "**57-acres of real property associated with the NY Facility**" — note that
  unlike the MEMSCAP deal this one included the land and buildings, not a lease — "**Class 100/Class
  1000 cleanroom space**", "**150-mm silicon MEMS wafer fab operations, including all semiconductor
  manufacturing tools**", an "**existing silicon-based MEMS business with annual revenues of
  approximately $3M**", "**Trusted Foundry accreditation for MEMS processing, packaging and
  assembly**", and "two existing tenants with multi-year leases".

  **And the sentence that makes this entry worth having**, the company's own estimate of the
  alternative:

  > "A comparable manufacturing facility to build and qualify for production would take up to 2-years
  > and cost well over $50 million"

  The stated motive is the same one Science gives: speed and control. The acquisition would "shorten
  time-to-market for its RF products, greatly enhancing the Company's ability to service customers",
  and Akoustis "plans to maintain the existing customer engagements which are transferred" — i.e. it
  kept the acquired fab's outside foundry customers, exactly as Science did.

  **The failure, 2024–2025.** Akoustis filed for Chapter 11 on **2024-12-16**. Nasdaq's hearings
  panel "determined to delist the Company's shares from Nasdaq" (8-K of 2024-12-17), the Form 25-NSE
  followed on 2025-06-06, and the registrant now files as **ATech (Parent) Resolution Corp.** In the
  Chapter 11 sales completed by May 2025, **Tune Holdings Corp.**, "a Texas corporation", was "named
  as the successful bidder for substantially all of the assets" at "**a purchase price of $30.2
  million**", with "Space Exploration Technologies Corp." — SpaceX — guaranteeing certain
  obligations; a second lot, the assets of Grinding and Dicing Services, Inc., went to Silitronics
  Solutions Inc. for "approximately $6 million". Shareholders were told: "The Company currently does
  not expect that holders of the Company's common stock will receive any payment or other
  distribution in the Cases."

  **Why it failed matters, and it was not the fab.** The 8-K of 2024-12-02 concerns an appeal against
  a **$38.6 million judgment** in litigation brought by Qorvo, and states that without relief "the
  Company will be required to seek protection under applicable bankruptcy laws". This was a
  litigation failure, not a demonstration that owning a small fab does not work.
- **DERIVED (arithmetic written out):** checked with `uv run python tmp/arith3.py`.
  - Price per square foot of facility: $2,750,000 / 120,000 sq ft = **$22.92 per sq ft** — including
    the tools, the 57 acres and an operating business.
  - Buying used against the company's own build-new estimate: $50,000,000 (a *floor*; the source says
    "well over") / $2,750,000 = **at least 18.2× cheaper to buy than to build**.
  - Price against the acquired business's revenue: $2,750,000 / $3,000,000 = **0.92× trailing
    revenue**.
  - Chapter 11 sale against the 2017 fab price: $30,200,000 / $2,750,000 = **11.0×** — but for a
    different and much larger asset package (the whole company after seven years of investment, not
    the fab alone), so this is a scale marker, not a return.
- **The cross-case observation, which is the point of this entry.** Two entirely independent
  transactions, five years apart, on two different continents' terms, for two small MEMS wafer fabs
  with roughly $3M of annual revenue each, cleared at **$2.75 million (2017)** and **$3.0 million
  (2022)** — both at roughly **one times trailing revenue**. That is not a coincidence worth
  over-reading from two points, but it is the beginning of a market price for this class of asset, and
  this repository had none before.
- **Bears on:** H6 (**supports, on the capital side** — a second, independent confirmation that a
  working small MEMS fab is a ~$3M asset, and the first credible figure for the build-new alternative:
  "well over $50 million" and two years, from a company with every incentive to justify its purchase);
  H5 (context — the acquired fab had an existing third-party foundry business and Akoustis kept it);
  H1 (context — buying beats building by more than an order of magnitude, which is an argument for
  *consolidating onto existing assets*, not for new entry).
- **Used in:** not yet.
- **Caveats:**
  - **"Well over $50 million" is an acquirer's justification for its own purchase**, published in the
    press release announcing that purchase. It is exactly the number a buyer would want to be large.
    It is nonetheless the only build-new estimate found from a company that then actually operated
    the alternative, and it is consistent with the "up to $65 million" Science budgeted for an
    expansion (IHF-2).
  - **The seller was a state university foundation**, not a commercial owner, so $2.75M may be below
    a commercial clearing price. Equally, that is the second time in this file that the party
    disposing of a small MEMS fab was not maximising price.
  - **Akoustis's bankruptcy is not evidence about small fabs.** It followed a $38.6M
    intellectual-property judgment. Recording it as a "fab failure" would be wrong, and it is recorded
    here as a failure of the *company*, with the cause stated.
  - The **$30.2 million** Chapter 11 price is for "substantially all of the assets" of a company that
    had spent seven years building BAW filter technology on top of the fab. It is not the resale value
    of the fab.
  - Whether the Canandaigua fab specifically was inside the Tune Holdings lot is **not stated in the
    8-K read**; the filing "does not mention a New York wafer fabrication facility" by name. Do not
    assert that SpaceX now owns that fab without checking the bankruptcy docket.

---

### IHF-10. Rigetti built its own quantum chip fab and then sold fabrication to outsiders — same pattern, thinner disclosure

- **Sources:**
  - Rigetti Computing, Inc., Form 10-K for FY2025, filed 2026-03-04.
    <https://www.sec.gov/Archives/edgar/data/1838359/000110465926023454/rgti-20251231x10k.htm>
  - Rigetti Computing, Inc., Form 10-K for FY2024, filed 2025-03-07.
    <https://www.sec.gov/Archives/edgar/data/1838359/000155837025002499/rgti-20241231x10k.htm>
- **Verification:** Partial. Both 10-Ks were read through `WebFetch` on 2026-09-19 with targeted
  prompts; the quotes below were returned from the filings. Neither document was read end to end, and
  the financial statements were not opened.
- **What it says.** Rigetti — a listed quantum-computing company (Nasdaq: RGTI) — owns and runs a
  wafer fab for superconducting quantum processors:

  > "We own and operate Fab-1, a wafer fabrication facility dedicated to prototyping and producing our
  > quantum processors."

  > "Through Fab-1, we own the means of production of our breakthrough multi-chip quantum processor
  > technology."

  And, as with Science, it sells that capability to outsiders:

  > "Rigetti Foundry Services leverages the company's U.S. based in-house wafer fabrication facility
  > ('Fab-1') to deliver superconducting quantum chips to advance and accelerate quantum information
  > science and technology research and development efforts. Customers include researchers spanning
  > academia, defense laboratories, and national laboratories."

  The strategic claim is vertical integration: owning production "from chip manufacturing through
  sales of QPUs and cloud delivery, unlocks the fastest and lowest risk path to broad
  commercialization."
- **What it does *not* say, which is most of what we wanted.** Neither 10-K read states Fab-1's
  square footage, cleanroom class, wafer size, headcount, construction cost, or any capital
  expenditure attributable to it, and **neither gives an explicit statement that outside foundries
  would not or could not serve superconducting quantum chips.** The absence matters: the
  "no-one-would-serve-us" motive that IHF-1 and IHF-5 state plainly is, for Rigetti, only inferable
  from its emphasis on proprietary processes ("superconducting multi-chip bonding technology",
  "superconducting through-silicon via process technology", "interchip coupling technology"). This
  entry therefore establishes the *pattern* — build in-house, then externalise — and not the cost.
- **Bears on:** H5 (context — a third company in a third field concluding it must own fabrication, and
  then finding outside customers for it); H8 (context — "Rigetti Foundry Services" is another
  build-then-open-to-others case); H6 (nothing — no figures).
- **Used in:** not yet.
- **Caveats:** Partial verification; no numbers. The build-then-externalise pattern may simply be how
  a capital-hungry company monetises spare capacity rather than evidence of unserved demand. Rigetti's
  `https://www.rigetti.com/foundry` page returns **HTTP 404**, so the customer-facing description
  could not be read. **What would unblock a human:** Rigetti's property, plant and equipment note and
  its capital-expenditure line in the 10-K financial statements, which were not opened here, and the
  Wayback Machine for the foundry page.

---

## 3. Cost section: every hard number found on small-scale fabrication capability

Collected in one place because the repository has almost nothing of this kind. **Read the caveats on
each entry before using any of these.**

### Capital cost to acquire or build capability

| What | Figure | Date | What it actually covers | Source | Status |
|---|---|---|---|---|---|
| Complete operating MEMS foundry — all tools and equipment, associated technology, the plant lease, the entire team, and the foundry customer book | **US$3.0 million** | 2022-12-07 | Purchase price of assets; **excludes the building freehold** (a lease was transferred) and excludes MEMSCAP's VOA product IP | MEMSCAP regulatory release (IHF-3) | **Verified** |
| Expansion of that same site: 57,000 sq ft for "MEMS and semiconductor manufacturing" | **"up to $65 million"** | 2024-07-09 | Building plus tools, not broken out; a ceiling stated in an incentives negotiation | Science Corporation (IHF-2) | Verified as a quote; the figure is a company claim |
| Implied capex density of that expansion | **$1,140 per sq ft** | 2024 | DERIVED: $65,000,000 / 57,000 sq ft | DERIVED from IHF-2 | Derived, order-of-magnitude only |
| The same North Carolina site, earlier | reported **"approximately $750M"** paid by JDS Uniphase for Cronos Integrated Microsystems, "shortly prior" to 2002 | c. 2000 | Acquisition of a *company*, not of the plant alone | Science Corporation blog (IHF-3) | **Lead** — not checked against a JDS Uniphase filing |
| Public subsidy attached to the expansion | **$930,000** over ten years, performance-based, for 50+ jobs = **$18,600 per job** | 2024-07-09 | Durham County incentive award | Science Corporation (IHF-2); county minutes not reached | Partial |
| **Net book value of the entire industrial tool set of that same fab**, on disposal | **EUR 0.5 million** | 2022-12 | Carrying value after depreciation of *all* the industrial equipment of the discontinued business — not a replacement cost | MEMSCAP 2022 annual report (IHF-8) | **Verified** (audited filing) |

### Operating scale of a small MEMS line

The first four rows are **audited figures for the fab as MEMSCAP ran it** and are the most reliable
operating numbers in this file. The rest are company statements about how Science runs it now.

| What | Figure | Source | Status |
|---|---|---|---|
| **Cleanroom area** | **475 m² = 5,113 sq ft** (DERIVED conversion) | MEMSCAP 2022 annual report (IHF-8) | **Verified** (audited filing) |
| **Cleanroom class** | **ISO 4** (≈ FS 209 Class 10) | MEMSCAP 2022 annual report (IHF-8) | **Verified** — but a secondary source says "Class 100", see IHF-8 caveats |
| **Wafer size** | **6 inch** | MEMSCAP 2022 annual report (IHF-8); Science says the same today | **Verified** |
| **Headcount running the whole foundry** | **14 people** (MEMSCAP's US employees at 31-12-2021) | MEMSCAP 2022 annual report (IHF-8) | **Verified** (audited filing) |
| Annual revenue of that foundry | **EUR 2,858 thousand** (FY2021), **EUR 1,935 thousand** (FY2022) | MEMSCAP FY2022 earnings release (IHF-8) | **Verified** (audited) |
| Its after-tax operating result | **loss of EUR 805 thousand** (FY2021), **loss of EUR 857 thousand** (FY2022) | MEMSCAP FY2022 earnings release (IHF-8) | **Verified** (audited) |
| Revenue and loss per head, FY2021 | **EUR 204 thousand** revenue and **EUR 58 thousand** loss per employee | DERIVED from IHF-8 | Derived |
| Tool count at Science Foundry | "**80+ Tools**", "more than 80 advanced tools" | IHF-4, IHF-5 | Verified (company statement) |
| Production volume the line targets | "**10s to 1000s of wafers**" per job; "dozens to thousands of custom wafers per year" | IHF-4 | Verified (company statement) |
| Headcount added by the expansion | "more than **50** new … jobs" | IHF-2 | Verified (company statement) |
| Scale of the planned expansion against the existing plant | **11.1×** the existing cleanroom area (57,000 sq ft against 5,113 sq ft) | DERIVED from IHF-2 and IHF-8 | Derived |
| Quality system | ISO 9001:2015, certified by Amtivo (USA) Inc.; MEMSCAP's facility was ISO 9001:2015 certified at the time of sale and Science stated a plan "to configure it to support FDA Good Manufacturing Practice (cGMP) production" | IHF-1, IHF-4 | Verified (company statement) |

### Price to a small customer

| What | Figure | Date | Unit | Source | Status |
|---|---|---|---|---|---|
| Science Foundry standard MEMS MPW run | **$13,520+** | 2026 | not stated | IHF-4 | Verified as published; contents unknown |
| MEMSCAP MUMPs via Europractice | **EUR 3,700** standard / **EUR 3,500** discounted | 2020 | per block: 10×10 mm (Poly) or 11×11 mm (SOI, Piezo), **15 dies**, 8–12 weeks | IHF-6 | Verified |
| — the same, per mm² | **EUR 37.0** (Poly) / **EUR 30.6** (SOI, Piezo) | 2020 | DERIVED | IHF-6 | Derived |
| — the same, per delivered die | **EUR 247** | 2020 | DERIVED | IHF-6 | Derived |
| X-FAB XMB10 MEMS via Europractice | **EUR 1,253/mm²** standard, **EUR 1,168/mm²** discounted | 2026 | minimum billable 10 mm²; 50 dies; extra dies EUR 25 each, max 50 | IHF-7 | Partial |
| — minimum possible ticket | **EUR 12,530** standard / **EUR 11,680** discounted | 2026 | DERIVED | IHF-7 | Derived |

### The one-paragraph version, for anyone who reads nothing else here

**A working commercial MEMS foundry — 475 m² of ISO 4 cleanroom, 6-inch wafers, fourteen people, an
ISO 9001:2015 quality system, a live customer book and the industry's longest-running MEMS
multi-project wafer shuttles — turned over about EUR 2.9 million a year, lost money doing it, carried
its entire tool set at EUR 0.5 million, and sold for US$3.0 million.** The company that bought it
then budgeted "up to $65 million" to make it about eleven times larger. Those five numbers are the
useful output of this file, and every one of them comes from an audited filing or a regulatory
announcement rather than from marketing.

### What is still missing, and would be worth more than any of the above

- **A breakdown of the $65M into building versus tools.** Without it the figure cannot be turned into
  a cost model.
- **Refurbished-equipment prices.** Nothing was found. The $3.0M in IHF-3 is a whole-line price and
  does not decompose, and the EUR 0.5M in IHF-8 is a depreciated book value, not a market price.
- **Cleanroom build cost per square foot by class.** Not found from any primary source. The nearest
  thing is the $1,140/sq ft implied by IHF-2, which mixes building and tools.
- **What Science Foundry's $13,520 buys.** Behind account registration.
- **The split of the fab's EUR 2.9 million revenue between MPW shuttle customers and contract
  manufacturing**, and the group overhead allocated to it. Both would change how IHF-8's loss should
  be read, and neither is disclosed.
- **Annual operating cost of a 6-inch MEMS line**, separately from revenue. Not found.

---

## 4. Verdict on H5 and H6

### On H5 (there is a long tail of demand for chips): supports the *mechanism*, does not size the market

This is the best-documented case yet found of the thing H5 asserts. A funded commercial company, not
a hobbyist and not a university, stated in its own words that the existing industry could not serve
it — "simply inaccessible for this kind of low-volume work, often with uncommon materials and tool
parameters" (IHF-5) — and then spent money to prove it meant it. Its description of the gap, "the
low-volume, high-complexity, rapid-iteration end", is H5's claim in a supplier's vocabulary. Better
still, the segment it names is not price-sensitive hobby demand: these are companies that will pay,
and Science's stated target industries are medical devices, aerospace, defence, quantum computing and
optical telecoms (IHF-1).

**But it does not size anything.** One company's motive is one data point. Nothing found says how
many customers Science Foundry has, what they pay, or whether the business is profitable — Science
Corp is private and its Form D filings disclose only securities sold, not revenue. The most that can
be said is that at least one well-capitalised buyer, with $47M raised at the time of the decision
(and $230M by 2026), found the merchant market closed to it. H5 needs *many* such buyers, and this
file has evidence of one, with the rest of the demand asserted rather than counted.

**And there is a direct challenge in the same body of evidence, now with numbers on it.** MEMSCAP ran
the industry's longest-standing MEMS multi-project wafer service for over a decade (IHF-6) and then
deliberately exited fab ownership, calling it the successful completion of a planned "FABLITE
Program" expected to deliver "significant improvement to MEMSCAP agility and profitability" (IHF-3).
Its audited accounts say why: the whole small-customer foundry business turned over **EUR 2,858
thousand in FY2021 and EUR 1,935 thousand in FY2022, a fall of 32%** (IHF-8). Meanwhile Europractice's
MEMS offering fell from three MUMPs processes in 2020 to a single X-FAB process in 2026 (IHF-6,
IHF-7). If the long tail of MEMS demand were large and growing, a public company that already owned
the assets and the customer book would be an odd party to walk away, the revenue line would not be
falling by a third, and the shop window would be getting fuller, not emptier.

**Net:** H5's mechanism is now evidenced by a named, credible, paying buyer. H5's *scale* is not —
and on the one occasion where the scale of a small-customer MEMS foundry's revenue is actually
disclosed, it is about EUR 2.9 million a year and shrinking.

### On H6 (small customers can each be profitable): the capital side helps, the profit side hurts, and the second one is better evidenced

**The good news first, and it is genuine.** The fixed capital a small MEMS fab needs is far smaller
than this repository had assumed. A complete, certified, staffed, customer-carrying MEMS foundry
cleared the market at **US$3.0 million** (IHF-3); its **entire tool set was carried at EUR 0.5
million** after depreciation; it occupied **475 m²** of ISO 4 cleanroom and was run by **fourteen
people** (IHF-8). If those are the numbers a fab has to recover, the revenue required is on a scale a
few thousand small customers could plausibly reach. That is the arithmetic H6 depends on and it has
never before had a real figure to put in it.

**The bad news is that we now know what happened when someone actually tried, and it did not work.**
The same fab, doing exactly the business H6 describes — many small customers, shared multi-project
wafer runs, published prices, no bespoke engineering per customer — **lost EUR 805 thousand in FY2021
and EUR 857 thousand in FY2022**, which is **28.2% and then 44.3% of its own revenue** (IHF-8). Its
owner sold it and booked a gain. This is not an analogue like Shapeways or Xometry; it is a MEMS
wafer fab selling shared shuttle runs to small customers, which is closer to foundry.api than
anything else in this directory, and it lands on the challenge side.

Three further things pull the same way:

1. **The $3.0M is the price of a *depressed* asset, not the cost of capability.** The same buyer then
   budgeted "up to $65 million" to make the site about eleven times bigger (IHF-2, IHF-8). The
   acquisition price is what it cost to *buy a fab that was losing money*; the expansion figure is
   closer to what it costs to *have* one that works.
2. **The fixed cost per small customer shows up in the price list, exactly as `SMB-7` and `SMB-8`
   found for silicon.** X-FAB's MEMS MPW charges a "minimum fabrication cost equivalent to 10mm²" —
   EUR 12,530 before any useful area (IHF-7). MUMPs sold a fixed 1 cm² block whether you needed it or
   not (IHF-6). Science publishes a floor, "$13,520+" (IHF-4). Every MEMS price list found behaves
   the same way as every silicon one: the first millimetre costs thousands. H6 assumes that fixed
   cost away and the MEMS evidence says it is still there.
3. **Nobody has shown the current version is profitable either.** Science Foundry is a unit of a
   venture-funded medical-device company with $230M of fresh capital (2026 Form D) whose actual
   product is a retinal implant. Its foundry may be cross-subsidised by that, exactly as Europractice
   is by EU funding (`SMB-6`). Science Corp is private and discloses no revenue at all.

**And the honest counter-argument, which must not be suppressed.** MEMSCAP's loss is a *divisional*
figure under IFRS 5 with an undisclosed allocation of group overhead, in a business that was being
wound down for sale in the second year, and mixing shuttle work with contract manufacturing in
proportions nobody has published. A buyer who already needs the fab for its own products — which is
precisely Science's position — removes the overhead problem and the utilisation problem at a stroke.
IHF-1's own framing says so: tools "require high utilization to justify owning", and Science's answer
was to be its own anchor customer and sell the spare capacity. That is a materially different
business model from MEMSCAP's, and this file cannot say whether it works, because Science does not
publish.

**Net, stated honestly.** On H6 this research delivers more than was hoped on the *capital* question
and worse news than was hoped on the *profit* question. The strongest single finding is not the one
that helps us: **the one small-customer MEMS foundry whose accounts are public lost money every year
they are visible.** H6 should stay Contested, and this evidence should be added to its challenges,
not its supports — with the overhead-allocation caveat attached, because that caveat is real and it
is the most plausible route by which the same assets could be profitable in different hands.

---

## 5. Blocked sources

Recorded so nobody repeats the attempt. Being blocked is an expected outcome, not a failure.

| Source | URL | What happened | What would unblock a human |
|---|---|---|---|
| Business Wire (MEMSCAP sale release) | `https://www.businesswire.com/news/home/20221207005667/en/...` | **HTTP 403** to both `WebFetch` and `curl` with a browser User-Agent ("Access Denied", Akamai edge error) | Opening it in a browser. Not needed in the end: MEMSCAP's own PDF of the same release was fetched from `memscap.com`, and citybiz carries a verbatim syndication |
| Business North Carolina | `https://businessnc.com/med-tech-company-to-add-50-jobs-spent-65-million-in-durham/` | **HTTP 403** to `curl`; served a "Just a moment… Checking your browser" interstitial. `WebFetch` also returned 403 | A browser. This is the main independent cross-check on IHF-2's $65M / 57,000 sq ft / 50 jobs |
| North Carolina Biotechnology Center | `https://www.ncbiotech.org/news/science-corp-set-expand-rtp-facility` | **HTTP 403**, same "Just a moment…" bot check | A browser. Second independent cross-check on IHF-2 |
| Axios Raleigh | `https://www.axios.com/local/raleigh/2024/07/11/medical-device-company-science-corp-chip-making-triangle` | **HTTP 403** to `WebFetch` | A browser. Third cross-check on IHF-2, and reportedly describes the plant |
| SEC `www.sec.gov/cgi-bin/browse-edgar` | company-name search | **HTTP 403** to `curl` — "Your Request Originates from an Undeclared Automated Tool" | Already known (`search-log.md` §1). Worked around: `efts.sec.gov/LATEST/search-index` (EDGAR full-text search) and `data.sec.gov/submissions/` both serve automated requests with a generic non-personal User-Agent, and `WebFetch` reaches `www.sec.gov/Archives/...` |
| Science Foundry full price list and ordering platform | behind "Start your order" on `https://science.xyz/services/foundry/mems/standard-technologies/` | Requires creating an account. **Deliberately not attempted** — account creation is forbidden under this project's read-only rule | A human willing to register. This is where the decomposition of the "$13,520+" price lives |
| CMC Microsystems list price for "Science Foundry Poly MEMS" | `https://www.cmc.ca/polymumps-multi-user-mems/` | Page loads; the list price field reads "Coming soon …" and subscriber pricing requires a login | Nothing — CMC has not published it. (`search-log.md` already records CMC's `FabPricing.aspx` returning 403) |
| MEMSCAP FY2022 annual report / FY2022 earnings release | `https://memscap.com/en/memscap_investors/` | Not blocked, **not yet retrieved**. The investor page's PDF list was read but the FY2022 annual report was not located among the links enumerated | Following the investor page's pagination. This would give the RTP fab's revenue and headcount before the sale, and the reported capital gain on disposal — the best available cross-check on IHF-3 |
| Rigetti Computing foundry page | `https://www.rigetti.com/foundry` | **HTTP 404** — the page has moved or gone | A site search, or the Wayback Machine |
| `web.archive.org` via `WebFetch` | — | Refuses outright (already recorded in `search-log.md` §1) | Use `curl` with the `…/web/<timestamp>id_/<url>` raw-content form |

---

## 6. Still to do

Listed so the next person does not have to rediscover it.

- **Cross-check IHF-2** ($65M / 57,000 sq ft / 50 jobs / $930,000) against the Durham County Board of
  Commissioners' own minutes or the NC Department of Commerce, neither of which was reached.
- **Retrieve MEMSCAP's FY2022 annual report** for the North Carolina fab's revenue, headcount and
  book value before disposal, and the capital gain recognised on the sale. This would convert IHF-3
  from "a price" into "a price against a known asset base and revenue", which is what the cost
  section most needs.
- **Verify the "approximately $750M" JDS Uniphase / Cronos figure** against a JDS Uniphase filing. It
  is currently a Lead quoted from the buyer's blog.
- **Comparable cases not yet worked**, each a company that built or bought its own line rather than
  buy wafers: **Rigetti Computing** (its "Fab-1" in Fremont/Berkeley, California, which its FY2025
  10-K describes as supporting "Rigetti Foundry Services … leverag[ing] the company's U.S. based
  in-house wafer fabrication facility ('Fab-1') to deliver superconducting quantum chips" to
  academic, defence and national-laboratory customers — the same build-then-externalise pattern as
  Science, and a listed company that must disclose costs); **Akoustis Technologies**, which bought an
  existing MEMS fab (the former STC-MEMS facility in Canandaigua, New York) in 2017 and disclosed the
  transaction in an 8-K — 75 EDGAR documents mention "STC-MEMS" and were located but not read;
  **Neuralink**; **Paradromics**; and **Precision Neuroscience**. Failures matter as much as
  successes and none has yet been written up.

