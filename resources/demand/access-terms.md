# Access terms: what a programme actually requires before it will make your chip (`ACC`)

Evidence gathered specifically for [`../analyses/open-access-audit.md`](../analyses/open-access-audit.md),
which asks two questions of every programme that claims to serve small chip customers:

1. **Is access actually open** — published prices, self-service purchase, no NDA, a redistributable
   PDK, no eligibility rule, open tooling, no gatekeeper, a visible queue, no export gate, a low
   fixed floor?
2. **Who actually pays** — is this a commercial entity trying to make a profit on this activity, or a
   university, a government programme, or one company's marketing budget?

Everything here was read-only: HTTP GET only, no forms submitted, no accounts created, no logins, no
quote requests, no attempt to get past a bot check. **Where a page says "register to download the
PDK" or "contact us for a price", that sentence is the finding.** It was recorded, not acted on.

---

### ACC-1. Tiny Tapeout's Terms and Conditions: mandatory Apache-2.0, mandatory publication, acceptance at Tiny Tapeout's sole discretion, and a full export-control regime

- **Source:** Tiny Tapeout B.V., "Tiny Tapeout Terms and Conditions": <https://tinytapeout.com/terms/>
  The page's own footer reads "Last Updated August 7th, 2026."
- **Verification:** **Verified 2026-09-18**, fetched with `curl` and read in full.
- **What it says**, verbatim:
  - **Acceptance is discretionary.** §1.2: "Tiny Tapeout may refuse to accept any Design or otherwise
    permit any individual or entity to participate in the Program and/or any Production Run in its
    sole discretion, including, without limitation, in the event of any failure to comply with these
    Terms or any applicable Production Run Requirements." The same clause gives the remedy: "In the
    event that your Design is not accepted for inclusion in a particular Production Run following your
    payment of any applicable Fees … Tiny Tapeout will provide you with a voucher for future
    Production Runs in the amount of such Fees."
  - **Publication is mandatory.** §1.3: "your Design and Design Documentation will be published and
    made publicly available on the Website, Tiny Tapeout GitHub pages and other promotional
    materials."
  - **An open-source licence is mandatory.** §4.1: "All Designs and Design Documentation must be
    licensed under terms and conditions compatible with the Apache License, Version 2.0".
  - **Export control.** §6.1: "You hereby undertake and agree to comply with all applicable national
    and foreign import, export and reexport control laws and regulations, including, without
    limitation, the Export Administration Regulations ("EAR") maintained by the U.S. Department of
    Commerce, trade and economic sanctions maintained by the US Treasury Department Office of Foreign
    Assets Control ("OFAC"), and the International Traffic in Arms Regulations ("ITAR") maintained by
    the US Department of State".
  - §6.2 names the excluded destinations: "(i) any country or territory subject to comprehensive,
    government-wide, or broad sectoral sanctions (currently consisting of Belarus, Cuba, Iran, North
    Korea, Russia, Syria, Venezuela, and the Crimea, Donetsk, Kherson, Luhansk, and Zaporizhzhia
    regions of Ukraine)".
  - §6.3 puts the burden on the customer: "You hereby represent and warrant that: (i) no Design and/or
    Design Documentation you submit hereunder would be subject to the ITAR, (ii) if such Design and/or
    Design Documentation is subject to the EAR, it is not controlled for purposes other than
    "Anti-Terrorism" (also known as "AT") purposes or is classified as EAR99; and (iii) you are not
    (a) located in a country to which export, reexport, transfer or release is prohibited by applicable
    Export Control Laws …".
  - §6.5 reserves termination: "Tiny Tapeout in its sole discretion has the right to terminate these
    Terms, suspend, cease, or terminate performance hereunder, or modify Tiny Tapeout's business
    relationship with you based on its interpretation of Export Control Laws".
  - **Fees are non-refundable.** §7: "Except as expressly set forth herein, all Fees are
    non-refundable."
  - **No testing is done.** §2.2: "TINY TAPEOUT AND ITS MANUFACTURERS DO NOT PERFORM ANY TESTING OF ANY
    CHIPS OR MANUFACTURED DESIGNS." (Capitals in the source.)
- **Bears on:**
  - **H8 (mixed, and this is the point of the entry).** Tiny Tapeout is the programme the repository
    treats as the most open thing in existence, and it is: €70 a tile, no institution required, no
    NDA, an Apache-2.0 PDK, a public design list. But its own terms contain a discretionary right of
    refusal, a compulsory open-source licence, compulsory publication of your design, a full
    EAR/OFAC/ITAR regime with named excluded countries, and non-refundable fees. **"Open access" and
    "no conditions" are not the same thing.** The conditions here are conditions of openness — you
    must publish — rather than conditions of exclusivity, which is a different shape from an NDA, and
    the audit scores it that way.
  - **H5 (context).** A resident of a sanctioned country cannot buy a Tiny Tapeout tile. That is a
    real, published eligibility boundary on the cheapest route to silicon that exists.
- **Used in:** [`../analyses/open-access-audit.md`](../analyses/open-access-audit.md).
- **Caveats:**
  - These are the terms as of 2026-08-07. Earlier versions were not checked, so nothing here shows
    when the export-control clauses were added.
  - The terms bind "your participation in the Tiny Tapeout semiconductor chip design program"; they
    say nothing about the foundry's own terms, and §2.1 says so: "inclusion of your Design on the Chip
    and the manufacture and supply thereof may be subject to additional terms and conditions of the
    applicable Manufacturer."
  - A discretionary right of refusal in a contract is not evidence that anyone has been refused. No
    rejection rate is published.

### ACC-2. Tiny Tapeout does not publish a headline price: the FAQ answers "What is the price?" with a link to a client-side calculator

- **Source:** Tiny Tapeout, "FAQ": <https://tinytapeout.com/faq/>
- **Verification:** **Verified 2026-09-18**, fetched with `curl` and read.
- **What it says**, verbatim:
  - "What is the price? You can use our handy calculator to check pricing." (The link is to
    `app.tinytapeout.com/calculator`.)
  - "How many chips will I receive? Can I order more? You only get 1 chip. If you want more chips you
    have to order more of the devkit PCBs - the early bird price is only available once per person."
  - "What PDK is used for the manufacture? We are using the open source Skywater 130nm PDK"
  - "How big can my design be? For TT04 to TT10, the standard tile size is about 160x100 um. This is
    enough for about 1000 digital logic gates, depending on their size."
  - "Do I need to use Wokwi, or could I use an HDL? If you're an advanced user, you can use the HDL of
    your choice."
  - "I'm stuck, how can I get support? Join the discord community with this link."
- **Bears on:**
  - **H8 (challenges, mildly).** The single cheapest and most open route to silicon in the world does
    **not** put its headline price on a page. `SMB-10` records the €70 per-tile shuttle-inclusion price
    and the analog-pin schedule, which *are* published as numbers; the all-in tile-plus-ASIC-plus-board
    price is not, and the calculator that computes it is a client-side application that returns no
    price text to a fetch. This is already recorded as a blocker in
    [`search-log.md`](search-log.md) and is repeated here because it matters for the audit's
    "prices published" criterion: the answer for Tiny Tapeout is *partly*.
- **Used in:** [`../analyses/open-access-audit.md`](../analyses/open-access-audit.md).
- **Caveats:** a calculator that anyone can open in a browser without logging in is much closer to a
  published price than "contact your local representative" is. The distinction the audit draws is
  between *a number a machine can read* and *a number a human can obtain without asking anyone*. Tiny
  Tapeout passes the second test and fails the first.

### ACC-3. ChipFoundry's chipIgnite FAQ: a published flat price, no open-source requirement, NDA-protected designs supported — and a reservation made by submitting a request form, not a checkout

- **Source:** ChipFoundry (UmbraLogic Technologies LLC), "chipIgnite FAQ":
  <https://chipfoundry.io/faqs>. Page footer: "© 2026 UmbraLogic Technologies LLC".
- **Verification:** **Verified 2026-09-18**, fetched with `curl` and read in full. This upgrades the
  **Partial** status that `OPG-9` records for the FAQ quotes, which were previously reported by a
  delegated agent rather than read by the entry's author.
- **What it says**, verbatim:
  - **Price.** "The standard pricing is $14,950 per project for standard shuttle participation. This
    includes 100 QFN packaged parts (or optionally all bare die)." And: "There is an option for an
    additional 50 bare die for $3000".
  - **Discounts are by negotiation.** "We do not offer discounts for individual project submissions.
    Discounts are available exclusively for organizations purchasing a pool of projects for academic,
    research, or commercial volume use. To request a custom quote for a project pool, please contact
    us."
  - **How you buy.** "How do I reserve a spot on a shuttle? You can reserve your spot on an upcoming
    shuttle by submitting a request to us through this form." Payment: "chipIgnite offers flexible
    payment options: Full payment at reservation / Deposit and milestone payments / Refund capability
    if shuttle minimums are not met".
  - **Undersubscription risk sits with the supplier.** "If a shuttle does not meet the minimum customer
    commitment threshold required for launch, you will be offered: A full refund of your project fee,
    or The option to roll over your project to the next scheduled shuttle".
  - **No open-source requirement.** "Do I need to open-source my design? No. Unlike some earlier
    programs, chipIgnite is a private shuttle with no open-source requirement for your designs." And
    on IP: "Restricted and monitored staff access to customer design files / Support for NDA-protected
    designs / Clear IP ownership terms", and "You retain full commercial rights to your designs and the
    resulting chips. There are no royalty or licensing fees for commercial deployment."
  - **Tooling.** "chipIgnite supports both open-source and commercial EDA tool flows: Open Source:
    OpenLane for RTL-to-GDSII digital design flow / Proprietary: Support for industry-standard
    commercial tools". And: "chipIgnite supports the SKY130 open-source PDK based on the 130nm
    Skywater Technology foundry process."
  - **Who it is for.** "Educational Institutions … Hardware Startups … Original Equipment Manufacturers
    (OEMs) … Independent Hardware Developers: Individuals looking to turn open-source designs into
    physical chips". **No eligibility rule of any kind is stated.**
  - **Continuity with Efabless.** "Building on the success of the Efabless chipIgnite program's
    community of over 10,000 members and 600+ fabricated chip designs".
  - **Capacity.** "Manufacturing Schedule: Limited initial schedule with 2 shuttles in 2025 and 3 in
    2026, compared to quarterly shuttles with chipIgnite".
- **Bears on:**
  - **H8 (mixed).** Price published, no eligibility rule, no NDA to see the PDK, an open flow
    supported, and a public live metrics API (`OPG-9`) — but **you cannot buy it with a card**. The
    purchase route is "submitting a request to us through this form", and any discount is "request a
    custom quote … please contact us". On the audit's self-service criterion ChipFoundry scores
    *partly*, not *open*.
  - **H6 (context).** "We do not offer discounts for individual project submissions" is a flat,
    non-negotiated price to the small customer and a negotiated one to the large — the exact opposite
    of the usual direction, and the shape `PRINCIPLES.md` argues for.
- **Used in:** [`../analyses/open-access-audit.md`](../analyses/open-access-audit.md).
- **Caveats:**
  - The FAQ text is internally inconsistent about which company is which: "How does ChipFoundry differ
    from Efabless?" is answered with bullets that call the *new* programme "chipIgnite" and the *old*
    one "chipIgnite" as well ("compared to quarterly shuttles with chipIgnite"). The intended contrast
    is clear from the prices ($14,950 against $9,750) but the wording is not.
  - "600+ fabricated chip designs" and "over 10,000 members" are the vendor's own round figures.
    `OPG-6` records Efabless's own "1300 designs and six hundred tapeouts" and `OPG-15` its "13K plus
    member community"; the FAQ's numbers are lower and undated.
  - A page titled `chipfoundry.io/terms` returns **HTTP 404**; the site's footer links to "Terms",
    "Privacy" and "Commercial" but the terms themselves were not read.

### ACC-4. Europractice's 2026 price list adds a third eligibility condition that its 2025 list did not have

- **Sources:**
  - EUROPRACTICE IC Service, "Schedules & Prices 2026": <https://europractice-ic.com/schedules-prices-2026/>
  - The 2025 list, already recorded as `SMB-7`: <https://europractice-ic.com/schedules-prices-2025/>
- **Verification:** **Verified 2026-09-18** for the 2026 page, fetched with `curl` and read. The 2025
  wording is quoted from `SMB-7`, which was verified from the page on the same date.
- **What it says.** The 2026 page states three conditions where the 2025 page stated the customer
  type and country only:

  > "What are Standard and Discounted prices? There are two prices in the Europractice lists:
  > Discounted and Standard.
  > **DISCOUNTED PRICE. Three conditions should be met for Discounted prices:**
  > Customer is an academic institution or a research facility from one of the 27 EU countries
  > together with Albania, Armenia, Azerbaijan, Bosnia-Herzegovina, Georgia, Iceland, Israel,
  > Liechtenstein, North Macedonia, Moldova, Montenegro, Norway, Switzerland, Turkey, Serbia, the UK
  > and Ukraine.
  > Customer is a registered Europractice member who has paid the Full-IC annual membership fee.
  > **The intended design will be done for educational purposes or for publicly funded research.**
  > STANDARD PRICE. Standard prices apply to all other customers."

  `SMB-7` records the 2025 page as saying only: "Customer is an academic institution or a research
  facility from one of the 27 EU countries together with Albania, … and Ukraine." … "Standard prices
  apply to all other customers."

  Other terms read on the same 2026 page:
  - **A per-foundry NDA, stated by the foundry rather than by Europractice.** Under Fraunhofer IISB:
    "To participate in a process run, customers must have a valid NDA and register at least 4 weeks in
    advance. Please consult the latest PDK release for complete specifications and guidelines. For
    NDA, PDK download, and registration please contact" (an address follows, which is not reproduced
    here and was not contacted).
  - **Export control is a registration step.** The X-FAB and ams OSRAM blocks give "Registration and
    Export Control information deadlines. Please download the Export Control file here." and under UMS:
    "Please fill in the Export Control questionnaire when registering your design and return it to"
    (again an address, not contacted). The downloadable file is
    `https://europractice-ic.com/wp-content/uploads/2025/01/Export_Control_Fraunhofer_v1.docx`.
  - **The open-PDK line is priced the same as in 2025:** "GLOBALFOUNDRIES 180 MCU (Open PDK) 913 /
    830", with footnote 4: "Price = area (mm²) * price/mm² with min. fabrication cost equivalent to
    6 mm²."
  - **Being small costs more per mm².** The standard GlobalFoundries MPW list prices "GLOBALFOUNDRIES
    130 nm BCDlite 1,760 / 1,600" per mm²; the mini@sic list — the option for customers too small for
    a whole block — prices "GLOBALFOUNDRIES 130nm BCDlite – Gen2 3,080 / 2,800" per mm².
  - **TSMC prices are still not tabulated:** "Prices for TSMC technologies can be calculated through
    the online Price Request Form:", with the one exception noted in `ACC-5`.
  - The €1,000 splitting charge survives, in dollars: "When 4 or more independent sub-designs are
    registered in one MPW submission to optimise the minimum charged area, an additional verification
    charge of 1,000 USD is applicable."
- **DERIVED (arithmetic written out):** 3,080 ÷ 1,760 = **1.75**, so a mini@sic customer on GF 130 nm
  BCDlite pays **75% more per mm²** than a customer who takes a standard MPW block. On the discounted
  column, 2,800 ÷ 1,600 = 1.75 as well.
- **Bears on:**
  - **H8 (supports, and this is the sharpest single line in the file).** Europractice's eligibility
    rules got **tighter** between 2025 and 2026, not looser. It is no longer enough to be an academic
    institution in an eligible country and a paid-up member; the *use* must now also be "educational
    purposes or … publicly funded research". A commercially motivated project at an eligible
    university now pays standard prices.
  - **H6 (challenges, extending `SMB-7`).** The mini@sic surcharge is the cost of serving a small
    customer, published as a price, by the organisation that has served small customers longest: the
    smaller your block, the more each square millimetre costs you.
- **Used in:** [`../analyses/open-access-audit.md`](../analyses/open-access-audit.md).
- **Caveats:**
  - **We cannot date the change.** The 2026 list has three conditions and `SMB-7`'s reading of the 2025
    list has two. We did not check archived captures of the 2025 page to see whether the third
    condition was added to it later, so "added between the 2025 and 2026 lists" is the safe statement
    and "added in 2026" is not.
  - The membership fee, the country list and the NDA/DKLA routing are `OPG-17`'s findings, read from
    Europractice's own access and membership pages; this entry adds only what the price list itself
    says.
  - Several addresses appear on the page as the route to an NDA, a PDK or an export-control form.
    **None of them was contacted.** Their existence is the finding.

### ACC-5. The one TSMC programme whose prices Europractice publishes is gated on TSMC's own approval and an NDA

- **Source:** EUROPRACTICE, "TSMC University FinFET Program":
  <https://europractice-ic.com/tsmc-university-finfet-program/>
- **Verification:** **Verified 2026-09-18**, fetched with `curl` and read.
- **What it says**, verbatim:
  - Standfirst: "Lowering the Barrier to TSMC N16 and N7 FinFET for Europractice-Member Universities".
  - Eligibility: "EUROPRACTICE-member universities can now gain access to TSMC FinFET technologies to
    be leveraged for their research, education and teaching." And: "The TSMC FinFET program is also
    open to universities in North America."
  - **The access procedure, in one sentence:** "To access TSMC FinFET technologies, please fill in the
    application form and return it to" (an address follows, which was not contacted). "**Applications
    will be reviewed and approved by TSMC, after which an NDA will be shared. Access will be granted
    through imec's secure data-sharing platform.**"
  - The published prices, "Prices for University FinFET Program", EUR per minimum area and per extra
    area:

    | Technology | EUR / min area | EUR / extra area |
    |---|---|---|
    | TSMC 7nm Log FinFET (min area = 2 mm²) | 49,050 | 2,384 / 0.1 mm² |
    | TSMC 7nm RF FinFET (min area = 2 mm²) | 51,000 | 2,479 / 0.1 mm² |
    | TSMC 16nm Log FinFET Compact (min area = 4 mm²) | 59,550 | 1,448 / 0.1 mm² |
    | TSMC 16nm RF FinFET Compact (min area = 4 mm²) | 61,850 | 1,504 / 0.1 mm² |
    | TSMC 16nm RF FinFET Compact mini@sic (min area = 1 mm²) | 16,850 | 1,685 / 0.1 mm² |
  - One of the two design kits is teaching-only: "N16ADFP (Academic Design Foster Package): For
    Teaching Purpose Only".
- **Bears on:**
  - **H8, and this is why the audit separates its criteria.** Here is a programme with **fully
    published prices** and **no open access at all**: you must be a university, you must be a
    Europractice member (or a North American university), you must submit an application, TSMC must
    approve it, you must then sign an NDA, and the design kit arrives through a "secure data-sharing
    platform". Published prices are necessary for open access and nowhere near sufficient, and this is
    the cleanest example of the two coming apart.
  - **H5 (context).** €49,050 is the smallest ticket on the cheapest FinFET line, before any tooling.
    `DEM-21`'s "some services require a minimum chip area of 2mm X 2mm, which comes at a cost close to
    $100,000" is the same order and is corroborated here from a published price list.
- **Used in:** [`../analyses/open-access-audit.md`](../analyses/open-access-audit.md).
- **Caveats:**
  - The prices are for universities only; no commercial price for these nodes is published anywhere we
    could read.
  - The application form was **not** downloaded, filled in or returned, and the address on the page was
    not contacted.

### ACC-6. All three open PDKs in the record carry the Apache License 2.0, verified from the repository metadata without logging in

- **Source:** the GitHub REST API, unauthenticated:
  - <https://api.github.com/repos/google/skywater-pdk>
  - <https://api.github.com/repos/google/gf180mcu-pdk>
  - <https://api.github.com/repos/IHP-GmbH/IHP-Open-PDK>
  - <https://api.github.com/repos/efabless/caravel>
- **Verification:** **Verified 2026-09-18**, all four fetched with `curl` with no credentials and the
  JSON read.
- **What it says:** every one of the four returns `"license": {"spdx_id": "Apache-2.0", "name":
  "Apache License 2.0"}`, and none is archived. The descriptions as returned:
  - `google/skywater-pdk` — "Open source process design kit for usage with SkyWater Technology
    Foundry's 130nm node."
  - `google/gf180mcu-pdk` — "PDK for GlobalFoundries' 180nm MCU bulk process technology (GF180MCU)."
  - `IHP-GmbH/IHP-Open-PDK` — "130nm BiCMOS Open Source PDK, dedicated for Analog, Mixed Signal and RF
    Design."
  - `efabless/caravel` — "Caravel is a standard SoC template with on chip resources to control and
    read/write operations from a user-dedicated space."
- **Bears on:**
  - **H4 and H8 (supports).** The audit's hardest openness criterion is not "free of charge" but
    "redistributable" — may a third party copy the design kit, fork it, build a course or a tool on it
    and publish the result? For SKY130, GF180MCU and IHP SG13G2 the answer is an OSI-approved yes, and
    it can be established by an anonymous HTTP GET in one second. For every other process in this
    audit the answer is no, and establishing that takes reading an access page.
  - It is the mechanism behind `efabless-and-the-open-shuttles.md` §2.3(c): Tiny Tapeout, the Zero to
    ASIC course, Wokwi's ASIC mode and the wafer.space, ChipFoundry, IHP and Cadence shuttles all exist
    downstream of these four licences.
- **Used in:** [`../analyses/open-access-audit.md`](../analyses/open-access-audit.md).
- **Caveats:**
  - A licence on a repository is not a statement that the process is production-qualified. `OPEN-2` and
    `OPEN-3` record that the GF180MCU and IHP kits describe themselves as previews and as "not intended
    to be used for production settings at this current time".
  - The GitHub API reports the licence GitHub detected, not the text of every file in the tree. Some
    parts of a PDK repository can carry different terms; the individual `LICENSE` files were not read
    for this entry.

