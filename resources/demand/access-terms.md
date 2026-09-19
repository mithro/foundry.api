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

