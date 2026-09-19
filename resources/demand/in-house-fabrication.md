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

