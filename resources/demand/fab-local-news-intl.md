# Small and specialty fabs outside the US, in the local record (`LNI`)

The national trade press reports that a fab "expands". The *local* paper, the municipal
planning file, the regional development agency and the filed accounts print the number:
the euros, the square metres, the head count, the grant. This file collects those numbers
for non-US small, specialty, MEMS and mature-node fabs, and for the institutes behind the
traditional multi-project-wafer brokers.

**The question it is trying to answer** is the one `hypotheses.md` says is missing: what
does it actually cost to stand up and staff a small fab, per unit of capacity and per job?
If the answer is large relative to what a long tail of very small customers can pay, that
is evidence against the project's thesis, and it is recorded here as such.

**Every non-English quote is given in the original and in English translation.** The
translations are ours.

**Currency.** Figures stand in the currency of their source. Where a conversion is shown it
uses the European Central Bank euro reference rates for **2026-09-24**
(<https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml>): EUR/SEK 11.2645,
EUR/GBP 0.85986, EUR/USD 1.1367, EUR/CAD 1.6047. The rate and date are repeated at each
conversion.

---

### LNI-1. Silex Microsystems, Järfälla: SEK 650 million buys 1,500 m² of extra cleanroom, 35% more capacity and 70–80 jobs at an existing 200 mm MEMS fab

> **Corrected 2026-09-25, after the prospectus itself was obtained (`LNI-18`).** This entry first
> read "SEK 500 million", which is what the press release says. The press release quotes only the
> 2027–2029 tranche. The prospectus states the figure in two parts: **"approximately SEK 150 million,
> expected to be incurred in 2026, followed by approximately SEK 500 million expected to be phased
> over the period from 2027 to 2029"** — **SEK 650 million in total** for the same +1,500 m² and the
> same +35%. Every derived figure below has been recomputed at SEK 650m. The prospectus also gives
> the staffing of the expansion, which the press release does not.

- **Source:** Silex Microsystems AB, "Silex offentliggör prospekt och pris inför det publika
  erbjudandet och noteringen av dess stamaktier på Nasdaq Stockholm", press release via MFN,
  2026-04-27.
  <https://www.mfn.se/a/silex-microsystems/silex-offentliggor-prospekt-och-pris-infor-det-publika-erbjudandet-och-noteringen-av-dess-stamaktier-pa-nasdaq-stockholm>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** Context on H5, H6 — this is the cleanest published capital-cost-per-unit-of-capacity
  figure found for a small specialty fab. It neither supports nor challenges on its own; it sets the
  price of the thing the thesis has to pay for.
- **What it says.** Silex is the world's largest pure-play MEMS foundry, operating one 200 mm fab in
  Järfälla, north-west of Stockholm. The IPO prospectus announcement sets out the use of proceeds in
  priority order. Original Swedish:

  > "…samt att finansiera utbyggnaden av renrumskapaciteten till cirka 1 500 kvadratmeter vid den
  > befintliga 200 mm fab:en i Järfälla, för att öka kapaciteten med cirka 35 procent till en
  > uppskattad kapitalinvestering om cirka 500 miljoner SEK under perioden 2027 till 2029."

  **English translation (ours):**

  > "…and to finance the expansion of cleanroom capacity by approximately 1,500 square metres at the
  > existing 200 mm fab in Järfälla, in order to increase capacity by approximately 35 percent, at an
  > estimated capital investment of approximately SEK 500 million over the period 2027 to 2029."

  The same release gives the existing cleanroom and the current trading:

  > "I dagsläget bedriver Silex sin verksamhet i en produktionsanläggning i Järfälla, som omfattar en
  > fab för 200 mm kiselproduktion. Silex fortsätter att investera i innovation och
  > kapacitetsutbyggnad vid anläggningen i Järfälla, med planer på att öka renrumskapaciteten med 35
  > procent och att utöka renrummet från 4 000 till 5 500 kvadratmeter."

  **English translation (ours):**

  > "At present Silex conducts its operations in a production facility in Järfälla, comprising a fab
  > for 200 mm silicon production. Silex continues to invest in innovation and capacity expansion at
  > the Järfälla facility, with plans to increase cleanroom capacity by 35 percent and to expand the
  > cleanroom from 4,000 to 5,500 square metres."

  > "För året som avslutades den 31 december 2025 uppgick Silex nettoomsättning till 1 385 miljoner
  > SEK och EBIT uppgick till 368 miljoner SEK."

  **English translation (ours):**

  > "For the year ended 31 December 2025 Silex's net sales amounted to SEK 1,385 million and EBIT
  > amounted to SEK 368 million."

  The first-priority use of proceeds is a US fab, at a much larger number:

  > "…föremål för godkännande från Kommittén för utländska investeringar i USA … till en uppskattad
  > kapitalinvestering om cirka 1 400 miljoner SEK"

  **English translation (ours):**

  > "…subject to approval from the Committee on Foreign Investment in the United States … at an
  > estimated capital investment of approximately SEK 1,400 million."

  The offering itself: 81 SEK per share, valuing Silex at about SEK 8,896 million, raising about
  SEK 1,000 million of new money before about SEK 65 million of transaction costs.

- **DERIVED (arithmetic written out)** — all at the corrected SEK 650m:
  - **Capital per square metre of cleanroom added:** SEK 650,000,000 ÷ 1,500 m² = **SEK 433,333/m²**.
    At the ECB reference rate of 2026-09-24, EUR/SEK 11.2645: SEK 433,333 ÷ 11.2645 = **€38,469/m²**.
  - **Cleanroom area check:** 5,500 m² − 4,000 m² = 1,500 m², i.e. **+37.5% of area for +35% of
    capacity**. The expansion is close to linear in floor area; there is no area economy of scale
    visible here.
  - **Capital per unit of annual revenue capacity:** 2025 net sales SEK 1,385m × 35% = **SEK 485m** of
    additional annual revenue at the same utilisation and price. SEK 650m of capex ÷ SEK 485m =
    **1.34× one year's incremental revenue**.
  - **Capital per job created by the expansion.** The prospectus states the staffing:
    "Approximately 50 operators and 20 to 30 engineers will be needed to support operations following
    the expansion of the production area" — **70 to 80 people**. SEK 650,000,000 ÷ 80 =
    **SEK 8,125,000 per job**; ÷ 70 = **SEK 9,285,714 per job**. In euro at EUR/SEK 11.2645:
    **€721,290 to €824,290 per job.** This is a *regulator-approved prospectus* figure rather than a
    press release, and it lands inside the €650,000–€935,000 band that `LNI-5`, `LNI-7`, `LNI-8` and
    `LNI-16` produced independently. **Five sites, four countries, two continents, the same answer.**
  - **US fab, for comparison:** SEK 1,400m ÷ 11.2645 = **€124.3m** for acquiring and converting an
    existing 200 mm IC fab with 3,000 m² of cleanroom — **€41,433/m²**, in the same range as the
    Järfälla brownfield rate of €38,469/m², for a fab bought rather than built.
- **Caveats.** SEK 650m is the *company's estimate*, not spend already incurred. It is unclear how
  much of it is shell and how much is tools; `LNI-6`'s 92/8 split says to assume mostly tools.
  "Capacity" is not defined in wafer starts anywhere in the prospectus. The 1.34× revenue ratio
  assumes the added capacity sells at 2025 prices and 2025 utilisation, which is an assumption, not a
  disclosure.

### LNI-2. The 300 mm fab Silex wants to build next door: 650 new jobs and 37,000 m², first reported out of a municipal planning file

- **Sources:**
  - Erik Lejdelin, "Silex vill bygga jättefabrik i Veddesta", *Mitt i* (Järfälla local edition),
    2024-02-06.
    <https://www.mitti.se/nyheter/silex-vill-bygga-jattefabrik-i-veddesta-6.3.194468.5a53adb4f7>
  - Jonas Karlsson, "Silex vill utöka produktionen i Järfälla", *SE Nytt*, 2024-02-07.
    <https://senytt.se/2024/02/07/silex-vill-utoka-produktionen-i-jarfalla/>
  - "Silex vill bygga ut fabrik och fördubbla produktionen", *Evertiq*, 2024-02-07.
    <https://evertiq.se/news/45095>
  - "Silex Microsystems går över till 300 mm-wafers i Järfälla", *Semi14*.
    <https://semi14.se/silex-microsystems-gar-over-till-300-mm-wafers-i-jarfalla/>
  - Järfälla kommun, "Världsledande teknik tar form lokalt – Silex Microsystems resa mot nästa
    tillväxtfas".
    <https://www.jarfalla.se/nyheter/nyheter/artiklar/varldsledandetekniktarformlokaltsilexmicrosystemsresamotnastatillvaxtfas.5.7f11d1f719dd25b962fac8.html>
- **Verification:** Partial. The 650 jobs and the planning-permission timeline are verified word for
  word in *Mitt i* and confirmed independently by *SE Nytt* and *Evertiq*; the current head count is
  verified from the municipality's own page. The 37,000 m² is taken from *Semi14*, a trade site, not
  from the planning file itself, and the SEK ~3 billion figure that circulates for this project could
  **not** be verified — see "What could not be got".
- **Date checked:** 2026-09-25
- **Bearing:** Context on H5 — the capital-per-job denominator for a greenfield specialty fab.
- **What it says.** *Mitt i* obtained the documents Silex filed with Järfälla municipality. Original
  Swedish:

  > "I handlingar som Mitt i begärt ut från kommunen uppger Silex att det kan röra sig om 650 nya
  > arbetstillfällen, vilket i så fall skulle göra bolaget till en av kommunens största arbetsgivare."

  **English translation (ours):**

  > "In documents that Mitt i requested from the municipality, Silex states that it could amount to
  > 650 new jobs, which would in that case make the company one of the municipality's largest
  > employers."

  > "Halvledartillverkaren Silex Microsystems har stora planer för sin fabrik i Veddesta. I höstas
  > ansökte de om planbesked hos Järfälla kommun för att kunna fördubbla sin produktion och i
  > november gav kommunen grönt ljus."

  **English translation (ours):**

  > "The semiconductor manufacturer Silex Microsystems has big plans for its factory in Veddesta.
  > Last autumn they applied for a planning decision from Järfälla municipality in order to be able
  > to double their production, and in November the municipality gave the green light."

  *SE Nytt* adds that the new plant "kan komma att generera hela 650 nya jobb" — "may come to
  generate a full 650 new jobs".

  Järfälla municipality's own write-up of a company visit gives the present head count:

  > "I dag har Silex över 220 ingenjörer och tekniker, och rekryteringarna fortsätter kontinuerligt
  > kopplat till bolagets fortsatta tillväxtplaner."

  **English translation (ours):**

  > "Today Silex has over 220 engineers and technicians, and recruitment continues continuously,
  > linked to the company's continued growth plans."

  and describes the origin of the business:

  > "Edvard Kälvesten beskrev Silex utveckling från starten 2002 i en lokal på 100 kvadratmeter i
  > Järfälla till dagens position som globalt branschledande aktör inom MEMS foundry."

  **English translation (ours):**

  > "Edvard Kälvesten described Silex's development from its start in 2002 in a 100-square-metre
  > premises in Järfälla to today's position as a globally leading actor in MEMS foundry."

  *Semi14* reports the plot size and the wafer-size step:

  > "37 000 kvadratmeter" for the new facility, moving from 200 mm (8 tum) to 300 mm (12 tum) wafers,
  > with a capacity increase of 125 percent.

  **English translation (ours):** "37,000 square metres"; from 200 mm (8 inch) to 300 mm (12 inch)
  wafers; capacity increase of 125 percent.

- **DERIVED (arithmetic written out):**
  - **Doubling the workforce doubles the jobs three times over.** Silex today employs "over 220
    engineers and technicians" and says the new fab could add **650** jobs. 650 ÷ 220 = **2.95×** the
    present technical head count, for roughly double the production. The new-jobs number is therefore
    not credible as a pure capacity ratio; either 220 excludes a large non-technical staff, or 650 is
    an outer bound offered to a planning authority. Treat 650 as the applicant's figure, which is
    what it is.
  - **Revenue per employee today.** *Do not* divide by 220: 220 is engineers and technicians only.
    The prospectus gives **484 employees as of 31 March 2026** (`LNI-18`) and the filed accounts give
    412 in 2024 (`LNI-17`), so revenue per head is **€254,000–€275,000**, not the €559,000 that 220
    would give. The working is in `LNI-18`.
- **Caveats.** The 650 figure is a planning-application claim by the applicant, reported from
  documents obtained under Sweden's public-access rules, not an audited or committed number. *Mitt i*
  gives no krona figure. The project was politically contested on Chinese-ownership grounds at the
  time of reporting; Silex has since returned to Swedish ownership and listed on Nasdaq Stockholm
  (2026-05-07), so the plan's current status is unknown.

### LNI-3. IHP Frankfurt (Oder): €15 million of public money for 500 m² of extra cleanroom — and €11.7m of it is EU regional funds

- **Sources:**
  - Ministerium für Wissenschaft, Forschung und Kultur des Landes Brandenburg,
    "IHP-Reinraumerweiterung", press release, 2021-03-04.
    <https://mwfk.brandenburg.de/mwfk/de/service/pressemitteilungen/ansicht/~04-03-2021-ihp-reinraumerweiterung>
  - EFRE Brandenburg, "Feierliche Inbetriebnahme des erweiterten Reinraums am IHP", 2021-03-05.
    <https://efre.brandenburg.de/efre/de/presse/pressemitteilung/~05-03-2021-feierliche-inbetriebnahme-des-erweiterten-reinraums-am-ihp>
  - IHP, "Clean Room Extension" (project fact table).
    <https://www.ihp-microelectronics.com/about-us/cleanroom-1>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** Context on H5 and H8. IHP is the institute that publishes the SG13G2 open PDK on which
  part of the open-shuttle world runs; this is what its cleanroom cost, and who paid.
- **What it says.** The Brandenburg science minister, Manja Schüle, at the commissioning. Original
  German:

  > "Deswegen haben wir, zusammen mit dem Bund und der EU, gerne 15 Millionen Euro in die
  > Reinraum-Erweiterung investiert. Damit schaffen wir Platz für neue Ideen."

  **English translation (ours):**

  > "That is why we have, together with the federal government and the EU, gladly invested 15 million
  > euros in the cleanroom extension. With it we are making room for new ideas."

  The ERDF share, from the EFRE Brandenburg release:

  > "Die Erweiterung des Reinraums wurde mit rund 11,7 Millionen Euro aus dem Europäischen Fonds für
  > regionale Entwicklung (EFRE) gefördert."

  **English translation (ours):**

  > "The extension of the cleanroom was funded with around 11.7 million euros from the European
  > Regional Development Fund (ERDF)."

  The scale, from the ministry release:

  > "Die Flächenerweiterung des Reinraums auf eine Größe von 1.500 Quadratmeter ermöglicht es dem IHP
  > einerseits, Partnern aus Wissenschaft und Forschung eine stabile BiCMOS Technologieplattform zur
  > Verfügung zu stellen…"

  **English translation (ours):**

  > "The area expansion of the cleanroom to a size of 1,500 square metres enables IHP on the one hand
  > to make a stable BiCMOS technology platform available to partners from science and research…"

  IHP's own fact table for the project (in English on IHP's site) gives:

  > "Additionally usable clean room area 500 m² / Gross floor area 3800 m² / Gross volume 18200 m² /
  > Length x Width 27 m x 35 m"

  and the schedule "Ready for Equipment 2020-09-30", "Usage of the building 2020-12", with
  construction starting from a building permit of 2018-09-05 — "in nur zweieinhalbjähriger Bauzeit"
  ("in only two and a half years of construction"), carried out "im laufenden Betrieb" ("during
  ongoing operation") of the existing cleanroom.

- **DERIVED (arithmetic written out):**
  - **Capital per square metre of added cleanroom:** €15,000,000 ÷ 500 m² = **€30,000/m²**.
  - **Public share:** €11.7m ÷ €15m = **78.0%** from the ERDF alone, with the rest from the federal
    government and the Land. This is a 100%-public building.
  - **Cross-check against `LNI-1`:** IHP €30,000/m² against Silex €29,592/m² is a **1.4% difference**
    on two projects a decade and a country apart. That agreement is worth stating plainly — but it
    also means something awkward. IHP's €30,000/m² buys a shell handed over "ready for equipment",
    i.e. **excluding the process tools**. If Silex's SEK 500m is on the same per-square-metre line,
    then either Silex's number is also mostly shell and the tools are extra, or IHP's building is
    unusually expensive. **A cleanroom shell alone therefore costs of order €30,000 per square
    metre**, and the tools sit on top of that.
- **Caveats.** €15m is the ministerial figure for the building project; it is not an audited
  construction cost and it is not stated whether it includes the metallisation tool bought separately
  under the Forschungsfabrik Mikroelektronik Deutschland programme (the release implies it does not).
  The total cleanroom after the work is 1,500 m², so the pre-existing cleanroom was 1,000 m² — the
  German text says the cleanroom was extended "um die Hälfte seiner Größe" ("by half its size"),
  consistent with 1,000 → 1,500 m².

### LNI-4. LFoundry Avezzano: €40 million of investment, and 13 permanent hires

- **Source:** Giammarco Giardini, "Avezzano: LFoundry, 40 milioni di investimento e 13 assunzioni a
  tempo indeterminato", *Rete8* (Abruzzo regional broadcaster), 2022-05-07.
  <https://www.rete8.it/cronaca/avezzano-lfoundry-40-milioni-di-investimento-e-13-assunzioni-a-tempo-indeterminato/>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Challenges** H5 and H6, and hard. This is the "€X million, Y jobs" datum in its
  purest form, and the ratio is terrible.
- **What it says.** Original Italian:

  > "Primo contratto di espansione siglato in provincia dell'Aquila. Riguarda LFoundry e prevede 40
  > milioni di investimento, 44 nuovi prodotti e 13 assunzioni. Questo permetterà a personale
  > specializzato di ottenere un contratto a tempo indeterminato nell'azienda di proprietà cinese dove
  > si producono semi conduttori. Con i 40 milioni di investimento si andrà ad aumentare la capacità
  > produttiva ammodernando anche gli impianti."

  **English translation (ours):**

  > "First expansion contract signed in the province of L'Aquila. It concerns LFoundry and provides
  > for 40 million of investment, 44 new products and 13 hires. This will allow specialised personnel
  > to obtain a permanent contract at the Chinese-owned company where semiconductors are produced.
  > With the 40 million of investment, production capacity will be increased, also modernising the
  > plant."

  > "I contratti di espansione permetteranno a 30 dipendenti prossimi alla pensione su 1.400 di
  > lasciare la fabbrica. Al loro posto entreranno 13 lavoratori a tempo indeterminato. … L'azienda
  > metterà sul piatto 2 milioni e 800 mila euro per assicurare la riuscita dell'operazione."

  **English translation (ours):**

  > "The expansion contracts will allow 30 employees close to retirement, out of 1,400, to leave the
  > factory. In their place 13 permanent workers will enter. … The company will put 2 million 800
  > thousand euros on the table to ensure the success of the operation."

  The unions' view, in the same report:

  > "Per i sindacati però si può fare di più a livello di investimento andando ad intercettare fondi
  > del Pnrr e i fondi europei Chips act."

  **English translation (ours):**

  > "For the unions, however, more can be done at the investment level by going after PNRR funds and
  > the European Chips Act funds."

- **DERIVED (arithmetic written out):**
  - **Capital per new permanent job:** €40,000,000 ÷ 13 = **€3,076,923 per job**.
  - **Net head count change:** −30 retirements + 13 hires = **−17**, against a base of 1,400. A
    €40 million capacity expansion at a mature-node fab *shrinks* the workforce by 1.2%.
  - **Capital per existing employee at the site:** €40,000,000 ÷ 1,400 = **€28,571** of new capex per
    head, for one round.
- **Caveats.** The €40m is the investment attached to a *contratto di espansione* — an Italian
  labour-market instrument that pairs early retirements with hiring and training — not necessarily
  the site's total capex. The €2.8m is the company's own contribution to the retirement scheme, not
  capex. FIOM-CGIL declined to sign the agreement, for reasons the report says were about union
  representation timing rather than the terms.
- **Why this cuts against the thesis.** The project's argument is that many very small customers can
  pay for real capital. LFoundry is a 1,400-person, 200 mm mature-node fab — exactly the class of
  asset the argument wants to fill. The published expansion arithmetic says €3.08 million of capital
  per job created, and a *falling* head count. Capacity at this class of fab is bought with equipment,
  not with people, and equipment is what a long tail of €10,000 customers would have to fund.

### LNI-5. Clas-SiC Wafer Fab, Lochgelly: the UK's only commercial SiC foundry, in its own filed accounts — 76 people, £8.35m of turnover, £58.9m of share premium raised, and a gross loss

- **Sources:**
  - Clas-SiC Wafer Fab Limited (company number **SC569032**), *Full accounts made up to 30 June 2025*,
    filed at Companies House 2026-01-29.
    <https://find-and-update.company-information.service.gov.uk/company/SC569032/filing-history>
    (document: <https://find-and-update.company-information.service.gov.uk/company/SC569032/filing-history/MzUwMjEyMDAyNWFkaXF6a2N4/document?format=xhtml&download=1>)
  - "Fife firm powering £12 million boost", Scottish Enterprise newsroom, 2026-08-19.
    <https://www.scottish-enterprise-mediacentre.com/news/fife-firm-powering-gbp-12-million-boost>
  - "Fife firm's funding boost to safeguard skilled jobs and boost exports", *Fife Today*
    (Fife Free Press group), 2026-08-19, 11:11 BST.
    <https://www.fifetoday.co.uk/business/fife-firms-funding-boost-to-safeguard-skilled-jobs-and-boost-exports-8929207>
  - "Lochgelly business Clas-SiC Wafer Fab makes £12m investment", *Central Fife Times*, 2026-08.
    <https://www.centralfifetimes.com/news/26480582.lochgelly-business-clas-sic-wafer-fab-makes-12m-investment/>
- **Verification:** Verified. The financial figures are read line by line out of the signed, audited
  iXBRL accounts downloaded from Companies House; the grant figures from Scottish Enterprise's own
  newsroom and two Fife papers.
- **Date checked:** 2026-09-25
- **Bearing:** **Challenges** H6 (can each small customer be profitable?) and **Supports** H5 on the
  *existence* of prototype demand. This is the single most directly relevant company found: a small
  Western foundry whose published strategy is rapid prototyping and low-rate production for small
  customers, with audited accounts.
- **What it says — the strategy is explicitly the long tail.** From the strategic report:

  > "Clas-SiC have continued in their focus on reprioritising customers to those needing rapid
  > prototyping, proved success in the licensing business, and advanced its technology in numerous
  > ways, now offering a wider range of process design kits (PDKs)."

  > "At the front end of the supply chain, we provide efficient rapid prototyping for the proof of
  > concept and the proof of design phases. We also offer Tech customers cost effective, low-rate
  > production so they can engage in the qualification process with their own customers to get their
  > products to market."

  and the customer base is said to be widening:

  > "Due to a very strong and growing global demand, despite tough competition from China, the
  > customer base for the development of new product designs continued to increase during the
  > financial year ended 30 June 2025, with the company expanding its customer base to a wider global
  > presence into South America and a strengthening base in Europe."

- **What it says — the numbers.** From the audited profit and loss account, balance sheet and notes,
  year ended 30 June 2025 (comparatives 2024):

  | | 2025 | 2024 |
  |---|---:|---:|
  | Turnover | £8,351,170 | £9,797,272 |
  | Cost of sales | £(9,069,129) | £(11,313,619) |
  | **Gross loss** | **£(717,959)** | **£(1,516,347)** |
  | Operating loss | £(3,281,743) | £(4,266,165) |
  | Loss for the financial year | £(3,028,086) | £(3,940,698) |
  | Average monthly employees incl. directors | **76** | **78** |
  | Wages and salaries | £3,306,722 | £3,305,770 |
  | Total staff remuneration (incl. NI, pension) | £3,782,638 | £3,758,604 |
  | Depreciation of owned tangible fixed assets | £2,259,976 | £2,223,877 |
  | Grants received (P&L) | £142,729 | £205,222 |
  | Research and development costs | £627,180 | £924,123 |
  | Tangible fixed assets, net book value | **£21,479,314** | £21,856,141 |
  | Tangible fixed assets, **cost** at 1 July 2024 | **£32,135,911** | — |
  | — of which leasehold land and buildings | £19,738,576 | — |
  | — of which plant and equipment | £12,237,691 | — |
  | Cash at bank | £10,930,557 | £218,558 |
  | Net assets | £29,477,050 | £22,501,810 |
  | **Share premium account** | **£58,883,519** | £48,902,038 |

  The directors' own three-year KPI table, as printed:

  | | 2025 | 2024 | 2023 |
  |---|---:|---:|---:|
  | Turnover | 8.4m | 9.8m | 10.3m |
  | Gross Profit / (Loss) | (0.7m) | (1.5m) | 1.1m |
  | Loss before tax | 3.3m | 4.3m | 1.7m |

  Turnover by geography, 2025: China and East Asia £4,559,446; Europe £2,958,700; USA and North
  America £833,024.

  On the new capital, from the strategic report:

  > "In October 2024, Clas-SiC signed a significant investment agreement with Archean Chemical
  > Industries Limited (ACIL) for £10m to be invested in capex for technology expansion, along with a
  > £2m loan for operating expenses and capital equipment."

  and on the grants it was then chasing:

  > "This investment is projected to be 'topped' up by grant funding from the UK and Scottish
  > Governments. Although not yet concluded to contract, both appear to be promising."

  That grant duly arrived, and the local press printed the split. Scottish Enterprise:

  > "A £1.9 million grant, part of a £12 million company investment, will support the growth of
  > Scotland's Critical Technologies supercluster, expanding a compound semiconductor wafer
  > manufacturer and creating new opportunities for staff and apprentices."

  Note what the jobs language is, and is not. Scotland's economy secretary Stephen Flynn, quoted in
  *Fife Today*:

  > "Clas-SiC's expansion will safeguard skilled jobs in Fife, strengthen our export base and support
  > the fundamental technologies that will power our transition to a cleaner economy."

  Not one of the four sources claims a single *new* job. The word is "safeguard".

- **DERIVED (arithmetic written out):**
  - **Cumulative equity raised per job:** share premium £58,883,519 + called-up share capital
    £127,169 = **£59,010,688** of equity subscribed since incorporation in 2017, against 76 average
    employees. £59,010,688 ÷ 76 = **£776,456 of equity raised per job**. At EUR/GBP 0.85986
    (ECB, 2026-09-24): £776,456 ÷ 0.85986 = **€903,003 per job**.
  - **Gross fixed assets per job:** £32,135,911 ÷ 76 = **£422,841 per job** (€491,756 at the same
    rate).
  - **Revenue per employee:** £8,351,170 ÷ 76 = **£109,884**. Compare Silex at €559,000 per head
    (`LNI-2`): Clas-SiC turns over about **one fifth** as much per person.
  - **Payroll intensity:** £3,782,638 ÷ £8,351,170 = **45.3% of turnover is staff cost**. This is
    almost exactly the 40–46% CMC Microsystems runs at (`FUNDX-1`), for a business that makes wafers
    rather than brokering them.
  - **Average cost per employee:** £3,782,638 ÷ 76 = **£49,772**.
  - **Gross margin:** £(717,959) ÷ £8,351,170 = **−8.6%**. Cost of sales alone exceeds revenue. The
    prototyping-and-low-rate-production model does not cover its own direct costs here.
  - **Asset turnover:** £8,351,170 of turnover on £21,479,314 of net fixed assets = **0.39×**.
  - **Depreciation per unit of revenue:** £2,259,976 ÷ £8,351,170 = **27.1%** of turnover is
    depreciation before any other cost. This is the number that decides whether a small fab can be
    filled by small orders.
  - **Grant intensity:** £142,729 of grants ÷ £8,351,170 of turnover = **1.7%** through the P&L in
    2025; the £1.9m Scottish Enterprise capital grant of August 2026 is **15.8%** of the £12m
    programme it sits inside (£1.9m ÷ £12m).
- **Caveats.** The £12m "company investment" reported in August 2026 and the £10m Archean capex
  agreement of October 2024 overlap to an unknown degree; they should not be added. Semiconductor
  Today reports 74 employees, against the accounts' average-monthly figure of 76 — use the accounts.
  The accounts are for a single company, not a group, and the LR&C licensing business means turnover
  is not all wafers. The 2023 turnover of £10.3m and gross *profit* of £1.1m show the business has
  been above water before; the direction since is down.
- **Why this matters more than the rest of the file.** Clas-SiC is the closest thing in the record to
  the business this project proposes: a small, Western, open-ish specialty foundry that says in its
  own audited strategic report that it prioritises customers needing rapid prototyping and low-rate
  production. It has **76 people**, has raised **£59 million of equity**, sits on **£32 million of
  gross fixed assets**, turns over **£8.4 million**, and made a **gross loss** in each of the last two
  years. Three quarters of a million pounds of equity per employee, and it still cannot cover cost of
  sales. Any claim that a long tail of small customers pays for real capital has to explain this
  company.

### LNI-6. X-FAB Dresden: US$43.5m buys 1,000 more wafer starts a month — and **92% of that money is equipment, not building**

- **Source:** Heiko Weckbrodt, "X-Fab baut seine Dresdner Chipfabrik aus", *Oiger* (Dresden), 2023-12-06.
  <https://oiger.de/2023/12/06/x-fab-baut-seine-dresdner-chipfabrik-aus/189256>
  (Weckbrodt was for sixteen years an editor at the *Dresdner Neueste Nachrichten*, covering the
  region's semiconductor industry; *Oiger* is his own Dresden news platform.)
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Challenges** H5 and H6, and is the most useful single entry in this file for costing
  a small fab. It puts a price on a wafer start per month, and it shows where the money goes.
- **What it says.** Original German:

  > "Der europäische Halbleiter-Auftragsfertiger (Foundry) investiert dafür bis Anfang 2025 rund rund
  > 43,5 Millionen Dollar (40,3 Millionen Euro) in neue Fertigungsanlagen und einen Erweiterungsbau,
  > kündigte Frank-Michael Schulze vom Projektstab an."

  **English translation (ours):**

  > "The European semiconductor contract manufacturer (foundry) is investing for this purpose, by
  > early 2025, around US$43.5 million (€40.3 million) in new production equipment and an extension
  > building, announced Frank-Michael Schulze of the project team."

  > "Insgesamt sollen durch den Ausbau die Produktionskapazitäten in Dresden um zehn Prozent auf dann
  > rund 11.500 Chipscheiben-Starts (Wafer) pro Monat steigen, informiert Schulze. Mit dem neuen
  > Brückenbau erweitere sich zugleich die verfügbare Reinraum-Produktionsfläche um 280 auf dann 3680
  > Quadratmeter."

  **English translation (ours):**

  > "In total, the expansion is intended to raise production capacity in Dresden by ten percent, to
  > around 11,500 wafer starts per month, Schulze reports. With the new bridge building the available
  > cleanroom production area is at the same time extended by 280 to 3,680 square metres."

  **The split between building and tools, which is the point of this entry:**

  > "Der Rohbau selbst wird etwa 3,5 Millionen Dollar kosten. Mit rund 40 Millionen Dollar wird der
  > Löwenanteil der aktuellen Investition auf die Chipfabrik-Ausrüstungen entfallen."

  **English translation (ours):**

  > "The shell construction itself will cost about US$3.5 million. With around US$40 million, the
  > lion's share of the current investment will fall on the chip-factory equipment."

  The fab as it stood before the work:

  > "Die Fabrik in Dresden gehört mit bisher 3400 Quadratmetern Reinraumfläche und reichlich 10.000
  > Wafer-Starts pro Monat zu den kleineren und älteren Fabs im X-Fab-Verbund … Beispielsweise
  > stellten die Eigentümer die Dresdner Fab zwischen 2009 und 2014 auf 200-Millimeter-Wafer um."

  **English translation (ours):**

  > "With 3,400 square metres of cleanroom area so far and a good 10,000 wafer starts per month, the
  > Dresden factory is among the smaller and older fabs in the X-Fab group … For example, the owners
  > converted the Dresden fab to 200-millimetre wafers between 2009 and 2014."

  And the group, for scale:

  > "Mit 4200 Beschäftigten und 740 Millionen Millionen Dollar Jahresumsatz gehört die Gruppe im
  > internationalen Maßstab zwar zu den eher kleinen Foundries. Die X-Fab ist aber das einzige
  > europäische Unternehmen in der Top 20 der größten Chip-Auftragsfertiger weltweit."

  **English translation (ours):**

  > "With 4,200 employees and US$740 million of annual revenue the group is, on an international
  > scale, one of the rather small foundries. X-Fab is however the only European company in the top
  > 20 of the world's largest chip contract manufacturers."

  (The duplicated word "Millionen Millionen" is in the original.)

- **DERIVED (arithmetic written out):**
  - **Capacity added:** the article gives +10% to "around 11,500" wspm. 11,500 ÷ 1.10 = **10,454 wspm
    before**, so the increment is 11,500 − 10,454 = **1,046 wafer starts per month**. (The article
    separately describes the pre-existing fab as "a good 10,000" wspm, consistent.)
  - **Capital per monthly wafer start, at the margin:** US$43,500,000 ÷ 1,046 = **US$41,587 per
    wafer start per month**. In euro on the article's own conversion, €40,300,000 ÷ 1,046 =
    **€38,528 per wspm**.
  - **Implied replacement cost of the whole fab:** 10,454 wspm × US$41,587 = **US$435 million** for a
    3,400 m², 200 mm specialty fab — if marginal cost equals average cost, which it will not exactly,
    but the order of magnitude is the point.
  - **Equipment share:** US$40m ÷ US$43.5m = **92.0% equipment, 8.0% building shell.**
  - **Shell cost per square metre:** US$3,500,000 ÷ 280 m² = **US$12,500/m²**.
  - **All-in cost per square metre of cleanroom:** US$43,500,000 ÷ 280 m² = **US$155,357/m²**.
  - **Cleanroom productivity:** 10,454 wspm ÷ 3,400 m² = **3.07 wafer starts per month per square
    metre of cleanroom**; after the work, 11,500 ÷ 3,680 = 3.13.
  - **Group revenue per employee:** US$740m ÷ 4,200 = **US$176,190**.
- **Why this matters, and how it corrects `LNI-3`.** The 92/8 split is the number that makes the rest
  of this file legible. IHP's €30,000 per square metre (`LNI-3`) and Silex's €29,592 (`LNI-1`) are not
  measuring the same thing as X-FAB's US$155,357; IHP's figure is a *building* handed over "ready for
  equipment", and per square metre of that building's **gross floor area** it is €15m ÷ 3,800 m² =
  **€3,947/m²**, which is an ordinary industrial construction number. **The cleanroom shell is the
  cheap part. The tools are the expensive part, by an order of magnitude**, and no amount of clever
  scheduling or open tooling changes what a deposition tool costs.
- **Caveats.** The US$/€ conversion is the article's own (43.5/40.3 = 1.0794 USD per EUR, consistent
  with December 2023); no conversion of ours is involved. "Capacity" here is wafer starts, undefined
  as to mask layers or process. The 280 m² is described as a *bridge* connecting the existing fab to
  the test centre, so part of the spend buys logistics rather than capacity; that would make the
  per-wafer-start figure conservative in one direction and the per-square-metre figure misleading in
  the other.

### LNI-7. Teledyne DALSA, Bromont, Québec: C$42m and eight federal millions for 40 jobs — and an explicit statement that Canadian SMEs use the fab for prototyping

- **Sources:**
  - Innovation, Sciences et Développement économique Canada, "Le Canada investit dans Teledyne pour
    poursuivre les avancées dans l'industrie des semi-conducteurs", 2025-03-21. Live URL:
    <https://www.canada.ca/fr/innovation-sciences-developpement-economique/nouvelles/2025/03/le-canada-investit-dans-teledyne-pour-poursuivre-les-avancees-dans-lindustrie-des-semi-conducteurs.html>
    Read via the Internet Archive capture of 2026-08-29:
    <http://web.archive.org/web/20260829131305/https://www.canada.ca/fr/innovation-sciences-developpement-economique/nouvelles/2025/03/le-canada-investit-dans-teledyne-pour-poursuivre-les-avancees-dans-lindustrie-des-semi-conducteurs.html>
  - Jean-François Guillet, "Semi-conducteurs: Teledyne Dalsa investit 42 millions dans son usine de
    Bromont", *La Voix de l'Est* (Granby, Québec), 2025-03-24 17:56, updated 18:03.
    <https://www.lavoixdelest.ca/affaires/2025/03/24/semi-conducteurs-teledyne-dalsa-investit-42-millions-dans-son-usine-de-bromont-CQOLUY3AS5E7TPI6LAAHLPQF5U/>
- **Verification:** Verified for the federal release (read in full from the Wayback capture; the live
  canada.ca URL would not complete a fetch, see "What could not be got"). Partial for *La Voix de
  l'Est*, which is behind a soft wall and was read through a summarising fetch rather than as raw
  text; its distinctive contribution — that the 40 jobs arrive "sur 3 à 5 ans" and that the line being
  replaced is about 30 years old — is recorded as reported, not as a checked quote.
- **Date checked:** 2026-09-25
- **Bearing:** **Mixed** on H5. The capital-per-job ratio is poor (challenges), but the release states
  in terms that small firms and research centres get design and prototyping access to the fab
  (supports).
- **What it says.** Original French:

  > "Aujourd'hui, la ministre de l'Innovation, des Sciences et de l'Industrie, l'honorable Anita
  > Anand, a annoncé l'octroi d'un financement de 8 millions de dollars par l'entremise du Fonds
  > stratégique pour l'innovation en appui à un projet de 42 millions de dollars visant à moderniser
  > de l'équipement."

  **English translation (ours):**

  > "Today, the Minister of Innovation, Science and Industry, the Honourable Anita Anand, announced
  > the granting of 8 million dollars of funding through the Strategic Innovation Fund in support of
  > a 42 million dollar project to modernise equipment."

  > "Le projet contribuera de façon marquée à la prospérité par la création de 40 emplois et le
  > maintien au pays de 560 emplois hautement spécialisés."

  **English translation (ours):**

  > "The project will contribute markedly to prosperity through the creation of 40 jobs and the
  > retention in the country of 560 highly specialised jobs."

  **The sentence that matters for H5** — twice, in slightly different words:

  > "En outre, des entreprises et des centres de recherche canadiens bénéficieront d'un accès à
  > l'infrastructure unique de Teledyne pour la conception et le prototypage de produits novateurs."

  **English translation (ours):**

  > "In addition, Canadian companies and research centres will benefit from access to Teledyne's
  > unique infrastructure for the design and prototyping of innovative products."

  > "Teledyne exploite deux usines de production de semi-conducteurs, à Bromont et à Edmonton, qui
  > s'appuient sur plus de 40 ans d'expertise. Des centres de recherche et des PME du Canada
  > bénéficient d'un accès à leur infrastructure pour la conception, le prototypage et la production
  > en grande quantité de produits novateurs."

  **English translation (ours):**

  > "Teledyne operates two semiconductor production plants, in Bromont and in Edmonton, drawing on
  > more than 40 years of expertise. Canadian research centres and SMEs benefit from access to their
  > infrastructure for the design, prototyping and high-volume production of innovative products."

  The technical content of the project:

  > "L'investissement annoncé aujourd'hui soutiendra la conversion de la chaîne de production de
  > dispositifs à couplage de charge (DCC) afin de faire passer la taille des tranches de 150 mm à 200
  > mm, ce qui permettra d'accroître l'efficacité et le rendement. … L'installation de Teledyne à
  > Bromont est l'une des rares usines de production de DCC encore en activité dans le monde."

  **English translation (ours):**

  > "The investment announced today will support the conversion of the charge-coupled device (CCD)
  > production line to move the wafer size from 150 mm to 200 mm, which will allow efficiency and
  > yield to be increased. … Teledyne's Bromont facility is one of the few CCD production plants still
  > operating in the world."

  > "Les tranches de 200 mm permettront de produire 1,8 fois plus de puces par rapport aux tranches de
  > 150 mm, ce qui se traduira par une augmentation de 40 % de l'efficacité et du rendement."

  **English translation (ours):**

  > "200 mm wafers will make it possible to produce 1.8 times more chips compared with 150 mm wafers,
  > which will translate into a 40% increase in efficiency and yield."

  And the programme total:

  > "Depuis 2023, le gouvernement a annoncé des investissements totalisant plus de 215 millions de
  > dollars pour des projets liés aux semi-conducteurs par l'entremise du Fonds stratégique pour
  > l'innovation."

  **English translation (ours):**

  > "Since 2023 the government has announced investments totalling more than 215 million dollars for
  > semiconductor-related projects through the Strategic Innovation Fund."

- **DERIVED (arithmetic written out):**
  - **Capital per new job:** C$42,000,000 ÷ 40 = **C$1,050,000 per job**. At the ECB reference rate
    of 2026-09-24, EUR/CAD 1.6047: C$1,050,000 ÷ 1.6047 = **€654,328 per job**.
  - **Public share:** C$8m ÷ C$42m = **19.0%**.
  - **Public money per job created:** C$8,000,000 ÷ 40 = **C$200,000 per job** of federal money alone.
  - **Capital per job if the 560 retained jobs are counted too:** C$42,000,000 ÷ 600 = **C$70,000**.
    Which of these two is the honest number is a matter of what the counterfactual is; both are
    printed here because announcements routinely quote the second and mean the first.
  - **Geometric check on the wafer-size claim:** (200/150)² = 1.78, against the release's "1.8 times
    more chips". The claim is simply the area ratio, and it is arithmetically right.
- **Caveats.** Canadian dollars; no conversion is applied to the source figures. The 560 "maintained"
  jobs are a claim about a counterfactual, not a measurement. The *La Voix de l'Est* report says the
  40 jobs arrive over three to five years, which the federal release does not say.

### LNI-8. Teledyne MEMS, Edmonton: C$20 million for 16 permanent jobs at a pure-play MEMS foundry, with C$620,000 of provincial money

- **Sources:**
  - Edmonton Global, "Teledyne Expands MEMS Manufacturing Operations in Edmonton", 2026-06-25.
    <https://edmontonglobal.ca/news/teledyne-expands-mems-manufacturing-operations-in-edmonton/>
  - Teledyne Technologies, "Teledyne MEMS Expands Edmonton Operations with Support from Government of
    Alberta", Business Wire, June 2026, as carried by StockTitan.
    <https://www.stocktitan.net/news/TDY/teledyne-mems-expands-edmonton-operations-with-support-from-f6q27uv3j579.html>
    (This URL served the full release to a scripted fetch on 2026-09-25 and then returned **403** to
    the same fetch an hour later, so it is rate-limiting rather than paywalled. Every figure taken
    from it also appears in the Edmonton Global release above; the Teledyne release is cited only for
    the "pure-play MEMS foundries … design, prototyping, and high-volume manufacturing" wording.)
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Challenges** H5 and H6. This is a small MEMS foundry — the closest analogue in
  business model to what the project describes — and its published capital-per-job is over a million
  Canadian dollars.
- **What it says.** From Edmonton Global, the regional economic development agency:

  > "Teledyne Technologies Incorporated, a global industrial technology company, is expanding its
  > microelectromechanical systems (MEMS) manufacturing operations in Edmonton. The $20 million
  > investment will support increased production capacity at Teledyne's Alberta MEMS Foundry, creating
  > 16 high-quality jobs, and strengthening the region's advanced manufacturing and semiconductor
  > ecosystem."

  > "Supported by a $620,000 grant from the Alberta government's Investment and Growth Fund (IGF), the
  > planned expansion includes targeted upgrades to Teledyne's existing facility in Edmonton and is
  > intended to unlock additional productivity and capacity to meet growing global demand."

  From Teledyne's own release, on what the site does and who it serves:

  > "Teledyne MEMS is one of the world's foremost pure-play MEMS foundries, offering design,
  > prototyping, and high-volume manufacturing for MEMS sensors, actuators, and microfabricated
  > semiconductor devices. With advanced 150 mm and 200 mm wafer capabilities and decades of process
  > expertise, Teledyne MEMS serves customers across automotive, industrial, medical, consumer, and
  > communications applications."

  > "The expansion, which includes new wafer processing, inspection, and automation equipment
  > alongside facility upgrades, reaffirms Teledyne's long-term commitment to Alberta…"

  The site is the former Micralyne, an Edmonton MEMS foundry spun out of University of Alberta
  microfabrication research in the 1990s and acquired by Teledyne in 2019.

- **DERIVED (arithmetic written out):**
  - **Capital per permanent job:** C$20,000,000 ÷ 16 = **C$1,250,000 per job**. At EUR/CAD 1.6047
    (ECB, 2026-09-24): C$1,250,000 ÷ 1.6047 = **€778,961 per job**.
  - **Public share:** C$620,000 ÷ C$20,000,000 = **3.1%** — much the smallest subsidy fraction in this
    file. Alberta paid **C$38,750 per permanent job** (C$620,000 ÷ 16).
  - **Cross-check against Clas-SiC:** €778,961 per job here against **€903,003** of equity raised per
    job at Clas-SiC (`LNI-5`), **€654,328** per job at Bromont (`LNI-7`) and **€934,947** of equity
    per job at Pragmatic (`LNI-16`). Four independent small-fab numbers, in three countries, land
    between **€650,000 and €935,000 per job.**
- **Caveats.** The C$20m is a company announcement of planned spend. "16 high-quality jobs" is the
  permanent figure; there are 20 further temporary construction jobs which are not counted here. No
  capacity figure in wafers is given.

### LNI-9. Fraunhofer ISIT, Itzehoe, 2008: €45 million to add 2,000 m² and, eventually, 200 jobs — and a customer base of "over 350 companies"

- **Source:** "Austermann: '55-Millionen-Investitionen in Leuchtturm der Spitzentechnologie' —
  Fraunhofer-ISIT in Itzehoe wächst um 2000 Quadratmeter und 200 neue Jobs", *bildungsklick.de*,
  press release of the Schleswig-Holstein Ministry for Science, Economy and Transport, 2008-06-26.
  <https://bildungsklick.de/hochschule-und-forschung/detail/fraunhofer-isit-in-itzehoe-waechst-um-2000-quadratmeter-und-200-neue-jobs>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Supports** H5 on the *number* of customers a small institute fab can hold;
  **Challenges** H6 on cost. ISIT is the institute from which X-FAB's Itzehoe MEMS fab (`MEMS Foundry
  Itzehoe`, spun out 2009) was born, so this is the capital behind one of Europe's MEMS prototyping
  routes.
- **What it says.** Original German:

  > "…soll das 150 Mitarbeiter starke Institut mit einer 45-Millionen-Euro-Investition um 2000
  > Quadratmeter und langfristig um 200 zusätzliche Arbeitsplätze erweitert werden."

  **English translation (ours):**

  > "…the 150-employee institute is to be expanded with a 45-million-euro investment by 2,000 square
  > metres and, in the long term, by 200 additional jobs."

  > "Neben dem Bau eines neuen Reinraums für die Mikrochip-Entwicklung und -Produktion erhält das
  > Institut in den kommenden zwei Jahren für rund zehn Millionen Euro auch neue Fertigungsanlagen,
  > mit denen Siliziumscheiben (so genannte Wafer) der modernsten Generation bearbeitet werden können.
  > Austermann stellte eine Landesförderung in Höhe von 7,5 Millionen Euro für die beabsichtigte
  > Modernisierung der Halbleiteranlage in Aussicht."

  **English translation (ours):**

  > "Besides the construction of a new cleanroom for microchip development and production, the
  > institute will also receive, over the coming two years and for around ten million euros, new
  > production equipment with which silicon discs (so-called wafers) of the most modern generation can
  > be processed. Austermann held out the prospect of state funding of 7.5 million euros for the
  > intended modernisation of the semiconductor plant."

  **The customer count, which is the reason this entry exists:**

  > "Das ISIT besitzt in Deutschland die größte Kapazität und Kompetenz in der Forschung und
  > Entwicklung der Mikrosystemtechnik und Leistungselektronik. Im Rahmen seiner industriellen
  > Auftragsforschung hat das Institut einen stabilen Kundenstamm von über 350 Unternehmen, davon etwa
  > 50 aus Schleswig-Holstein."

  **English translation (ours):**

  > "ISIT possesses the largest capacity and competence in Germany in the research and development of
  > microsystems technology and power electronics. In the framework of its industrial contract
  > research the institute has a stable customer base of over 350 companies, of which about 50 are
  > from Schleswig-Holstein."

  and, on how full the existing cleanroom was:

  > "Schon jetzt aber sei der bestehende Reinraum bis an die Grenzen ausgelastet."

  **English translation (ours):**

  > "Already now, however, the existing cleanroom is utilised to its limits."

  The new build:

  > "…ist der Bau eines separaten Gebäudes neben dem bestehenden Reinraum mit 1000 Quadratmetern
  > nutzbarer Reinraumfläche sowie Büro- und Messlaborflächen geplant."

  **English translation (ours):**

  > "…the construction of a separate building next to the existing cleanroom is planned, with 1,000
  > square metres of usable cleanroom area as well as office and measurement-laboratory space."

- **DERIVED (arithmetic written out):**
  - **Capital per job (long term):** €45,000,000 ÷ 200 = **€225,000 per job** — by far the lowest in
    this file, and a reminder that a *research institute's* jobs are cheaper per euro of capital than
    a production fab's, because the institute is buying people as well as tools.
  - **Capital per square metre of usable cleanroom:** €45,000,000 ÷ 1,000 m² = **€45,000/m²**
    (the 2,000 m² figure includes office and laboratory space).
  - **Equipment share:** €10m of tools ÷ €45m = **22%**, against X-FAB Dresden's 92% (`LNI-6`). The
    difference is that ISIT is building a whole new building with offices and labs, X-FAB is bolting
    a bridge onto an existing fab. Both numbers are right; they are answers to different questions.
  - **Land subsidy share of the tool spend:** €7.5m ÷ €10m = **75%** of the equipment modernisation
    offered by the Land of Schleswig-Holstein, with the rest from the Fraunhofer-Gesellschaft and EU
    funds.
  - **Customers per employee, before the expansion:** 350 customers ÷ 150 staff = **2.3 customers per
    member of staff.** Compare the count a long-tail fab would need. `analyses/customers-needed-to-fill-a-fab.md`
    puts 7,000 customers of 100 wafers a year at GlobalFoundries Fab 8 scale; ISIT holds 350 customers
    with 150 people. If customer-handling scales with head count at ISIT's ratio, 7,000 customers is
    **3,000 people** — which is the automation problem this project exists to solve, stated as a
    number.
- **Caveats.** 2008 euros, not adjusted. "200 additional jobs" is explicitly "langfristig" ("in the
  long term") and was a political announcement; whether it happened is not established here. The €45m
  headline sits under a headline quoting the minister at "55-Millionen-Investitionen", which the body
  text does not reconcile — the body text's €45m is used. "Over 350 companies" is a claim by the
  funding minister about the institute's contract-research book, not an audited customer list, and
  contract research is not the same as wafer purchase.

### LNI-10. ams OSRAM, Premstätten, Styria: €588 million for 250 jobs, with up to €200 million asked of the Chips Act

- **Source:** "Premstätten – ams Osram: 588 Millionen Euro für 250 neue Arbeitsplätze",
  *MeinBezirk.at* (Graz-Umgebung regional edition, Regionalmedien Austria), 2024-05-13 13:22.
  <https://www.meinbezirk.at/graz-umgebung/c-wirtschaft/588-millionen-euro-fuer-250-neue-arbeitsplaetze_a6689462>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Challenges** H5 and H6. The headline of a regional Austrian paper is literally the
  shape this file was set up to find, and the ratio is bad.
- **What it says.** Original German:

  > "Gemeinsam stellten Aldo Kamper, Vorstandsvorsitzender der ams-Osram AG, Bundesminister Martin
  > Kocher und LH Christopher Drexler die Pläne für Investitionen in Höhe von 588 Millionen Euro bis
  > 2030 vor."

  **English translation (ours):**

  > "Together, Aldo Kamper, chairman of the executive board of ams-Osram AG, federal minister Martin
  > Kocher and state governor Christopher Drexler presented the plans for investments amounting to 588
  > million euros up to 2030."

  > "Im Rahmen des European Chips Act wurde eine Förderung von bis zu 200 Millionen Euro beantragt.
  > Der Förderantrag von ams Osram wurde an die EU-Kommission zur Genehmigung übermittelt. … Dabei
  > werden in den kommenden Jahren insgesamt 250 neue Arbeitsplätze geschaffen."

  **English translation (ours):**

  > "Within the framework of the European Chips Act, funding of up to 200 million euros was applied
  > for. ams Osram's funding application was submitted to the EU Commission for approval. … In the
  > coming years a total of 250 new jobs will be created."

  The CEO on why:

  > "Mit der neuen Fabrik an unserem Stammsitz können wir mehr Raum für Innovationen schaffen, den
  > steigenden Bedarf unserer Kunden bedienen und Produkte vermehrt in Europa fertigen."

  **English translation (ours):**

  > "With the new factory at our headquarters we can create more room for innovation, serve the
  > growing demand of our customers and manufacture products increasingly in Europe."

- **DERIVED (arithmetic written out):**
  - **Capital per new job:** €588,000,000 ÷ 250 = **€2,352,000 per job**.
  - **Public share, if the application succeeds in full:** €200m ÷ €588m = **34.0%**, or **€800,000 of
    public money per job created** (€200,000,000 ÷ 250).
- **Caveats.** The €200m is *applied for*, not granted, as of the article's date. Other reporting puts
  the programme at "knapp 600 Millionen" ("just under 600 million") and mentions Austrian federal
  funding of €227m; those figures were not verified here and are not used. No cleanroom area or wafer
  capacity is given.

### LNI-11. Bosch Dresden, for contrast: €1 billion, 700 jobs, 300 mm

- **Source:** Wirtschaftsförderung Sachsen, "Bosch errichtet Halbleiterwerk in Dresden".
  <https://standort-sachsen.de/de/aktuelles/news/detail/n216-bosch-errichtet-halbleiterwerk-in-dresden>
- **Verification:** Partial. The €1bn and 700-jobs figures are read verbatim from the Saxon economic
  development agency's own page; the page carries no visible date and the federal-support figure
  quoted elsewhere (€140m–€200m) was **not** verified and is not used.
- **Date checked:** 2026-09-25
- **Bearing:** Context on H1 and H5 — the top of the range against which the small fabs above should
  be read.
- **What it says.** Original German:

  > "Insgesamt beläuft sich das Investitionsvolumen für den Standort auf rund eine Milliarde Euro."

  **English translation (ours):**

  > "In total the investment volume for the site amounts to around one billion euros."

  > "'Die neue Fertigung für Halbleiter ist die größte Einzelinvestition in der mehr als 130-jährigen
  > Geschichte von Bosch', sagte Dr. Volkmar Denner … In Dresden sollen bis zu 700 neue Arbeitsplätze
  > entstehen."

  **English translation (ours):**

  > "'The new semiconductor production is the largest single investment in Bosch's more than 130-year
  > history,' said Dr Volkmar Denner … In Dresden up to 700 new jobs are to be created."

- **DERIVED (arithmetic written out):**
  - **Capital per job:** €1,000,000,000 ÷ 700 = **€1,428,571 per job**.
  - This is *less* per job than ams OSRAM's €2.35m (`LNI-10`) and only about twice Teledyne
    Edmonton's €779k (`LNI-8`). **Capital per job does not fall as the fab gets bigger; if anything
    it is flat.** Whatever the case for a small fab is, "cheaper per job" is not it.
- **Caveats.** A 300 mm automotive fab is not comparable in product or process to anything else in
  this file. Included only to bound the range.

### LNI-12. CORNERSTONE, Southampton: the UK's academic silicon-photonics MPW said in 2020 that it "will be self-sustaining, with users paying for the service" — and has taken £17.1 million of EPSRC money since

- **Source:** UK Research and Innovation, Gateway to Research API,
  <https://gtr.ukri.org/gtr/api/projects> — the four project records and their linked `FUND` objects,
  queried on 2026-09-25:
  - `EP/L021129/1` "CORNERSTONE: Capability for OptoelectRoNics, mEtamateRialS, nanoTechnOlogy aNd
    sEnsing" — <https://gtr.ukri.org/gtr/api/projects/4DF2803A-836A-4CCC-8B3F-0BD3562E15A6>
  - `EP/T019697/1` "CORNERSTONE 2" —
    <https://gtr.ukri.org/gtr/api/projects/687D6AB3-28C6-41A3-8F47-1C44764A2F9A>
  - `EP/W035995/1` "CORNERSTONE 2.5" —
    <https://gtr.ukri.org/gtr/api/projects/13D55263-F076-4B41-A5C8-48FC636BB52B>
  - `EP/Z531066/1` "CORNERSTONE Photonics Innovation Centre (C-PIC)" —
    <https://gtr.ukri.org/gtr/api/projects/827B6825-2A3D-4F3E-9CC1-57029B5D6C75>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **How it was counted:** The GtR project search endpoint returns `null` for grant value; the amount
  lives on the linked `FUND` object. For each project the `links.link` array was filtered to
  `rel == "FUND"`, that URL fetched, and `valuePounds.amount` and the start/end epoch-millisecond
  timestamps read off. Category is `INCOME_ACTUAL` in every case, i.e. money actually received, not
  awarded-and-unspent. The script is four HTTP GETs and is reproducible from the URLs above.
- **Bearing:** **Challenges** H8 and, by extension, the "self-sustaining MPW" story the directory has
  been unpicking for MOSIS (`MOS-*`). This is the same claim, made in writing, in a grant application,
  and then contradicted by the same funder's own records.
- **What it says — the money:**

  | Grant | Reference | Funder | Value (INCOME_ACTUAL) | Period |
  |---|---|---|---:|---|
  | CORNERSTONE | `EP/L021129/1` | EPSRC | **£2,267,121** | 2014-09-14 – 2020-06-29 |
  | CORNERSTONE 2 | `EP/T019697/1` | EPSRC | **£1,494,157** | 2020-03-01 – 2023-02-28 |
  | CORNERSTONE 2.5 | `EP/W035995/1` | EPSRC | **£1,553,164** | 2022-12-02 – 2025-06-01 |
  | C-PIC | `EP/Z531066/1` | EPSRC | **£11,782,397** | 2024-05-31 – 2029-05-30 |
  | **Total** | | | **£17,096,839** | 2014 – 2029 |

- **What it says — the claim.** From the abstract of `EP/T019697/1` (CORNERSTONE 2), written in
  2019/2020, with our emphasis on the clause that matters:

  > "Southampton and Glasgow Universities currently contribute to a project entitled CORNERSTONE which
  > has established a new Silicon Photonics fabrication capability, based on the Silicon-On-Insulator
  > (SOI) platform, for academic researchers in the UK. **The project is due to end in December 2019,
  > after which time the CORNERSTONE fabrication capability will be self-sustaining, with users paying
  > for the service.**"

  The same abstract then asks for the opposite:

  > "Southampton, and Glasgow universities will work together to bring the new platforms to a state of
  > readiness to deliver the new functionality via a multi-project-wafer (MPW) mechanism to satisfy
  > significantly increasing demand, and deliver them to UK academic users **free of charge (to the
  > user)** for the final six months of the project, in order to establish credibility."

  > "We currently have 50 partners/users providing in-kind support to a value of to £1,705,000 and
  > cash to the value of £173,450."

  And `EP/Z531066/1` (C-PIC, 2024, £11.8m) states the problem as unsolved:

  > "However, access to silicon prototyping facilities remains a challenge in the UK due to the high
  > cost of both equipment and the cleanroom facilities that are required to house the equipment."

  with the ambition:

  > "Deliver the world's only open source, fully flexible silicon photonics prototyping foundry based
  > on industry-like technology, facilitating straightforward scale-up to commercial viability."

  The first grant, `EP/L021129/1`, is worth quoting for what it says about the underlying capital and
  about the sustainability arithmetic:

  > "The stepper will be located at Southampton University in the recent £120m cleanroom complex."

  > "The Southampton users alone need only generate a tiny fraction (0.2%) of their research portfolio
  > to cover running costs and dep[reciation]"

  and about *why* an academic MPW is needed at all — a direct statement of the H1 doom spiral from
  inside a research council application:

  > "The Capability is extremely timely, as silicon foundry services around the world are moving
  > towards a model in which standard platforms and devices will be offered, making it more difficult
  > for researchers to carry out innovative work at the device level, or in non-standard platforms."

- **DERIVED (arithmetic written out):**
  - **Total EPSRC money, 2014–2029:** £2,267,121 + £1,494,157 + £1,553,164 + £11,782,397 =
    **£17,096,839**.
  - **Money since the "self-sustaining" date:** the three grants after CORNERSTONE 1 total
    £1,494,157 + £1,553,164 + £11,782,397 = **£14,829,718**, all of it awarded *after* the statement
    that the capability would be self-sustaining from December 2019.
  - **Average annual public funding:** £17,096,839 over the 14.7 years from 2014-09-14 to 2029-05-30
    = **£1,163,000 per year**. The rate is accelerating: C-PIC alone is £11,782,397 over five years =
    **£2,356,000 per year**, about **2.9×** the 2014–2023 average.
  - **Cash from users, as declared in 2020:** £173,450, against £1,494,157 of grant in the same
    project — **10.4 pence of user cash per pound of grant.** In-kind support of £1,705,000 is not
    cash and cannot pay a technician.
- **Caveats.** "Self-sustaining" in the 2020 abstract refers to the *first* capability (SOI) and the
  later grants fund *new* platforms, training and an innovation centre, not a re-funding of the same
  thing. That is a real distinction and it is the defence the programme would offer. It does not
  change the fact that a service declared self-sustaining in 2019 has drawn £14.8m of public money
  since. The `INCOME_ACTUAL` category means received; for C-PIC, which runs to 2029, part of that is
  necessarily profiled rather than banked.

### LNI-13. CORNERSTONE's published price list, its 900 designs, and the subsidy per design

- **Sources:**
  - CORNERSTONE, "MPW Schedule & Costs".
    <https://cornerstone.sotonfab.co.uk/mpw/mpw-schedule-costs/>
  - CORNERSTONE Photonics Innovation Centre, "The silicon photonics crossroad: CORNERSTONE market
    research uncovers scale-up challenges as global momentum builds", press release, 2026-06-17, as
    carried by the National Law Review.
    <https://natlawreview.com/press-releases/silicon-photonics-crossroad-cornerstone-market-research-uncovers-scale>
  - CORNERSTONE, "About Us". <https://cornerstone.sotonfab.co.uk/about-us/>
- **Verification:** Verified for the price list and the 50% subsidies, read directly off the live
  page. Partial for the "over 900 unique SiPh designs" count, which was read through a summarising
  fetch of the press release rather than from a CORNERSTONE-hosted page.
- **Date checked:** 2026-09-25
- **Bearing:** **Supports** H5 on volume (900 designs, 130 organisations, 26 countries is a real long
  tail), **Challenges** H6 and H8 on whether it pays for itself.
- **What it says — the prices, as printed** (per design area, per MPW run):

  | Design area | SOI active devices | SOI passive with heaters | SOI passive devices | SiN (inc. visible) passive with heaters | SiN (inc. visible) passive | Ge-on-Si |
  |---|---:|---:|---:|---:|---:|---:|
  | 11.47 mm × 4.9 mm | £57,420 | £19,980 | £12,790 | | | |
  | 5.5 mm × 4.9 mm | £34,500 | £14,700 | £8,875 | | | |
  | 15.45 mm × 11.47 mm | | | | £19,980 | £9,470 | £15,550 |

  and the discounts:

  > "UK University 50% off"
  > "UK SME 1st time users 50% off"

  > "If you're based at a UK University then access to all MPW runs until May 2029 will be 50%
  > subsidised by the CORNERSTONE Photonics Innovation Centre. You will automatically receive this
  > subsidy when you sign-up to an MPW call."

  Delivery times, as printed: SOI active 36 weeks; SOI passive with heaters 14 weeks; SOI passive
  only 14 weeks; SiN with heaters 12 weeks; SiN passive only 12 weeks; Ge-on-Si 10 weeks.

  The service describes itself:

  > "CORNERSTONE is an open-source, licence-free silicon photonics prototyping foundry. Our
  > open-source model lowers the barriers to innovation in photonic integrated circuits (PICs), giving
  > researchers and innovators the freedom to design, fabricate, and test new ideas."

  The volume, from the June 2026 market-research release:

  > "Since 2017, CORNERSTONE has fabricated over 900 unique SiPh designs for over 130 organisations in
  > 26 countries."

- **DERIVED (arithmetic written out):**
  - **Public subsidy per design:** £17,096,839 of EPSRC money (`LNI-12`) ÷ 900 designs =
    **£18,996 per design.** Note that this is the same order as the *price* of a passive SOI design
    (£12,790) and about a third of an active SOI design (£57,420). **The taxpayer is paying roughly as
    much per design as the customer is.**
  - **A tighter version, matching the periods:** designs are counted "since 2017"; the grants running
    over 2014–2026 total £17,096,839 but C-PIC runs to 2029, so only part is spent. Taking the three
    completed grants (£2,267,121 + £1,494,157 + £1,553,164 = £5,314,442) against 900 designs gives
    **£5,905 per design** as a floor, and the full-programme figure of £18,996 as a ceiling. **The
    honest range is £5,900 to £19,000 of public money per design.**
  - **Designs per organisation:** 900 ÷ 130 = **6.9 designs per organisation.** This is a long tail of
    *organisations* with repeat business, not one-shot hobbyists — the shape H5 wants.
  - **Designs per year:** 900 designs over 2017–2026, nine years, = **100 designs a year.** Compare
    Europractice at 363–985 a year (`DEM-16`) and CMP's 401 peak (`DEM-19`): CORNERSTONE is an order of
    magnitude smaller, in one technology.
  - **Price per square millimetre:** SOI active, 11.47 × 4.9 = 56.20 mm² for £57,420 =
    **£1,022/mm²**. SOI passive, same area for £12,790 = **£228/mm²**. SiN passive,
    15.45 × 11.47 = 177.21 mm² for £9,470 = **£53/mm²**.
  - **Half-size is not half-price:** the 5.5 × 4.9 mm cell is 26.95 mm², 48.0% of the 56.20 mm² cell,
    but costs £34,500 ÷ £57,420 = **60.1%** as much for SOI active and £8,875 ÷ £12,790 = **69.4%** as
    much for SOI passive. **The fixed cost of serving one customer is visible directly in the price
    list** — roughly 20–40% of the smaller cell's price is the cost of having a customer at all,
    rather than the cost of their silicon. This is H6's problem, published as a tariff.
- **Caveats.** The prices are list prices before the 50% academic and first-time-SME discounts, so
  realised revenue per design is lower than the table suggests, probably much lower given that the
  user base is dominated by universities. The 900 designs is a marketing claim in a press release,
  not an audited count. Design-area categories differ between SOI and SiN, so the £/mm² figures are
  not strictly comparable across platforms.

### LNI-14. Vishay at Newport Wafer Fab: £51 million with £5 million of Welsh Government money, and no job number at all

- **Source:** Welsh Government, "£51 million Newport investment latest chapter in Wales' compound
  semiconductor success story", 2024-11-27.
  <https://www.gov.wales/51-million-newport-investment-latest-chapter-wales-compound-semiconductor-success-story>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Challenges** H5. The UK's largest semiconductor facility announced a £51m investment
  and the government press release describing it does not contain a single job figure for that
  investment.
- **What it says:**

  > "Vishay Intertechnology, one of the world's largest manufacturers of discrete semiconductors and
  > passive electronic components, has announced that it is investing £51 million in Newport Wafer
  > Fab, the UK's largest semiconductor facility - bringing new product range capabilities and skilled
  > job opportunities to Newport."

  > "The investment has been supported by £5 million of Welsh Government funding…"

  The release's job numbers all belong to other projects on the same site:

  > "a second US owned company, KLA, constructing its new European headquarters at Imperial Park,
  > Newport. With Welsh Government investment in the grid infrastructure at the site, the 215,000
  > square foot, $100 million development is creating a state-of-the-art innovation centre and
  > manufacturing facility and will include cleanrooms for R&D and manufacturing. Recruitment of up to
  > 750 employees is already underway."

  > "Centre 7, a world-class facility supported by Welsh Government as part of its International
  > Strategy, is already attracting inward investors recognising Wales as a semi-conductor hotspot,
  > with Microlink Devices, and CS Connected the first tenants at the 51,000 square foot Cardiff Gate
  > site."

- **DERIVED (arithmetic written out):**
  - **Public share of the Vishay investment:** £5m ÷ £51m = **9.8%**.
  - **KLA, for a per-job comparison:** US$100,000,000 ÷ 750 = **US$133,333 per job** for a 215,000
    sq ft (19,974 m²) headquarters-and-innovation-centre with some cleanroom. That is an order of
    magnitude below every *fab* number in this file (`LNI-5` through `LNI-11`), which is the point:
    **buildings full of engineers are cheap per job; buildings full of process tools are not.**
    US$100m ÷ 215,000 sq ft = **US$465 per square foot**, or US$5,007/m².
  - **Vishay's spend per job cannot be computed**, because no job figure is published. Recording the
    absence is the finding.
- **Caveats.** "Skilled job opportunities" is not a number and should not be treated as one. KLA's
  Newport site is a headquarters and innovation centre, not a production fab, so its per-job figure is
  not a fab figure. The $100m is US dollars in a Welsh Government release that otherwise uses pounds.

### LNI-15. Tyndall National Institute, Cork: over €100 million to roughly double an institute that already has 580 people

- **Source:** Department of Further and Higher Education, Research, Innovation and Science (Ireland),
  "Government Approves Major Expansion of Tyndall National Institute", press release.
  <https://www.gov.ie/en/department-of-further-and-higher-education-research-innovation-and-science/press-releases/government-approves-major-expansion-of-tyndall-national-institute/>
- **Verification:** Partial. The €100m figure and the 580-staff figure are quoted verbatim from the
  release; the release carries no visible date in the fetched text, and no job-creation number is
  given, so no capital-per-job figure can be derived.
- **Date checked:** 2026-09-25
- **Bearing:** Context on H5 and H8. Tyndall is one of the institutes behind Europractice-style access
  in Europe; this is what its next building costs.
- **What it says.** Minister James Lawless:

  > "This investment of over €100 million under the National Development Plan will significantly
  > strengthen Ireland's global position in cutting‑edge semiconductor research and innovation, and it
  > will be central to driving forward our ambition to become a true Silicon Ireland."

  The institute's size:

  > "Tyndall National Institute (TNI) is Ireland's largest dedicated research institute and is one of
  > Europe's leading ICT research centres, with over 580 staff, postgraduate students and industrial
  > researchers-in-residence, including 158 PhD students, actively registered in 2024."

  Tyndall's CEO, William Scanlon:

  > "The Government's support for the Tyndall North Mall Expansion is transformative for Ireland's
  > research and innovation ecosystem. … This new world-class research facility will enable Tyndall's
  > growth for the future and deliver greater economic impact, an expanded talent pipeline, and
  > strengthen Europe's strategic resilience in this critical sector."

- **DERIVED (arithmetic written out):**
  - **Capital per existing person:** €100,000,000 ÷ 580 = **€172,414 per head already there.** If the
    expansion roughly doubles the institute, as the project has been described, the implied capital
    per *new* person is of the same order — close to Fraunhofer ISIT's €225,000 per job (`LNI-9`) and
    an order of magnitude below the production-fab figures in this file.
  - **The pattern across `LNI-9`, `LNI-14` and `LNI-15`:** institute and office jobs cost
    **€130k–€230k** of capital each; production-fab jobs cost **€650k–€2.35m**. The difference is
    process equipment.
- **Caveats.** "Over €100 million" and "almost double the footprint" are the only quantities; no
  cleanroom area, no head count target, no date on the page as fetched. This entry is a marker, not a
  measurement.

### LNI-16. Pragmatic Semiconductor, Sedgefield: £287 million of equity, 357 people, **£901,000 of revenue**, a £64.9m annual loss and a material uncertainty over going concern

- **Sources:**
  - Pragmatic Semiconductor Limited (company number **07423954**), *Financial statements for the year
    ended 31 December 2025*, audited by Deloitte LLP (Cambridge), signed 2026-07-08, filed at
    Companies House 2026-07-23.
    <https://find-and-update.company-information.service.gov.uk/company/07423954/filing-history>
    (document:
    <https://find-and-update.company-information.service.gov.uk/company/07423954/filing-history/MzUzMjkwODMyNmFkaXF6a2N4/document?format=pdf&download=1>)
  - UK Infrastructure Bank (now the National Wealth Fund), "Bank announces £60 million direct equity
    investment to boost UK supply chain of semiconductors in the North-East".
    <https://www.nationalwealthfund.org.uk/news-and-publications/news/bank-announces-60-million-direct-equity-investment-to-boost-uk-supply-chain-of-semiconductors-in-the-north-east/>
- **Verification:** Verified. The accounts are a scanned PDF with no text layer — `pdftotext`
  extracts 42 bytes from 42 pages — so every figure below was read off the page images directly.
  The pages used are numbered 15–30 of the document (PDF pages 16–31).
- **Date checked:** 2026-09-25
- **Bearing:** **Challenges** H5, H6 and H7, more sharply than anything else in this directory. It also
  **Supports** H7's mechanism in the negative: with almost no revenue, the customer book is
  concentrated.
- **What the public story says.** The UK Infrastructure Bank, a state-owned development bank:

  > "The UK Infrastructure Bank has today announced a £60 million direct equity investment into
  > Pragmatic Semiconductor, a world leader in manufacturing flexible integrated circuits, to scale up
  > the domestic supply chain of semiconductors in North-East England."

  > "The Bank's financing is part of a £162 million funding round, alongside co-investor M&G's
  > Catalyst, to accelerate the production of Pragmatic's new flexible integrated circuits, creating
  > new manufacturing lines at its Pragmatic Park facility in Durham."

  > "The expansion of Pragmatic's North-East facility will support or create 500 highly skilled jobs
  > and contribute to the development of the North-East Advanced Material Electronics (NEAME) cluster
  > as an area for world-class innovation and quality."

  Pragmatic Park at Sedgefield was opened by HRH The Princess Royal in March 2024 as the UK's first
  300 mm wafer fab.

- **What the audited accounts say.** Statement of Comprehensive Income, year ended 31 December 2025
  (comparatives 2024), all figures £'000 as printed:

  | | 2025 | 2024 |
  |---|---:|---:|
  | **Revenue** | **901** | **1,693** |
  | Cost of sales | (1,986) | (1,851) |
  | **Gross loss** | **(1,085)** | (158) |
  | Administrative expenses | (64,574) | (55,858) |
  | Other operating income | 479 | 523 |
  | R&D Expenditure Credit | 23 | 355 |
  | **Operating loss** | **(65,157)** | (55,138) |
  | Finance income receivable | 2,240 | 5,644 |
  | Finance costs payable | (1,955) | (932) |
  | **Loss before taxation** | **(64,872)** | (50,425) |
  | Tax income | 8,173 | 7,199 |
  | **Net loss for the year** | **(56,699)** | (43,227) |

  Statement of Financial Position at 31 December 2025:

  | | 2025 | 2024 |
  |---|---:|---:|
  | Property, plant & equipment | **94,999** | 57,695 |
  | Right-of-use assets | 11,296 | 11,942 |
  | Cash and cash equivalents | 24,963 | 84,520 |
  | Treasury deposits | – | 25,921 |
  | Total assets | 153,259 | 207,088 |
  | Total liabilities | (28,771) | (30,757) |
  | **Net assets** | **124,488** | 176,331 |
  | Share capital | 2 | 2 |
  | **Share premium account** | **287,025** | 287,088 |
  | Share based payment reserve | 14,566 | 9,647 |
  | **Retained earnings** | **(177,348)** | (120,649) |

  Note 6, Employee remuneration — the average number of employees, including executive directors:

  | | 2025 | 2024 |
  |---|---:|---:|
  | Research and development | 119 | 95 |
  | Operations | 158 | 139 |
  | Sales and Marketing | 20 | 19 |
  | General and Administrative | 60 | 54 |
  | **Total** | **357** | **307** |

  with staff costs of **£36,951** thousand (2024: £29,260), of which wages and salaries £26,794.

  Note 4, on the customer book — **this is the H7 datum**:

  > "In 2025, 50% of revenue was generated from customers located in the UK (2024: 10%) and there were
  > 3 customers who each accounted for more than 10% of revenue in the year (2024: 3)."

  Revenue by location of customer, £'000: UK 451; Europe (excl. UK) 416; Americas 10; Rest of the
  World 24; total 901.

  Note 11, on the accumulated position:

  > "Subject to the UK tax authority's agreement, the Company has tax losses of approximately
  > £153,000,000 (2024: £112,350,000) available for carry forward and offset against future taxable
  > profits arising from the same trade."

  The going-concern note, in full where it matters:

  > "The Company incurred a loss after tax of £56,699,000 for the year ended 31 December 2025 (2024:
  > £43,226,883). The Company is capital intensive and has historically been primarily funded by
  > periodic equity raises as it scales to mass production. The Company will continue to incur losses
  > until it reaches sufficient scale in production and sales and the directors therefore have
  > commenced the next equity funding round taking place during 2026, having secured £36,000,000 of
  > bridge financing from existing investors in the form of convertible loan notes."

  > "The Company has a strong record of success in raising the financing required to support the
  > investment needed to bring the business to mass production. In 2023 to 2026 the Company raised
  > £179 million in its Series D fundraise…"

  > "The directors acknowledge that there can be no certainty that the funding required by the Company
  > will be received, although at the date of approval of these financial statements they have no
  > reasonable expectation that it will not be able to do so."

  and the conclusion the directors draw:

  > "Based on the above, the directors believe it remains appropriate to prepare the financial
  > statements on a going concern basis. However, the circumstances described indicate that there is a
  > material uncertainty that may cast significant doubt on the entity's ability to continue as a going
  > concern and, therefore, that it may be unable to realise its assets and discharge its liabilities
  > in the normal course of business."

  Cash flow, 2025: purchases of property, plant and equipment **£32,372** thousand; cash outflow from
  operating activities £(48,791); net change in cash £(59,557), from £84,520 to £24,963.

- **DERIVED (arithmetic written out):**
  - **Revenue per employee:** £901,000 ÷ 357 = **£2,524 per employee per year.** Clas-SiC, the other
    small UK fab in this file, does £109,884 (`LNI-5`); Silex does about €559,000 (`LNI-2`).
  - **Staff cost per employee:** £36,951,000 ÷ 357 = **£103,504.** Revenue covers **2.4%** of the
    payroll (£901,000 ÷ £36,951,000).
  - **Cumulative equity raised per job:** share premium £287,025,000 + share capital £2,000 =
    **£287,027,000**, ÷ 357 = **£803,997 per job.** At EUR/GBP 0.85986 (ECB, 2026-09-24) that is
    **€934,947 per job** — and it lands inside the €650,000–€900,000 band that `LNI-5`, `LNI-7` and
    `LNI-8` independently produced, slightly above the top of it.
  - **Against the promise:** the state development bank's release says the expansion "will support or
    create 500 highly skilled jobs". The average head count in the accounts two years later is
    **357** (2024: 307). 357 ÷ 500 = **71.4%**, and the accounts do not say how many of those are at
    Sedgefield rather than Cambridge.
  - **Net fixed assets per employee:** £94,999,000 ÷ 357 = **£266,104.** Adding right-of-use assets,
    £106,295,000 ÷ 357 = **£297,745.**
  - **Asset turnover:** £901,000 of revenue on £94,999,000 of net property, plant and equipment =
    **0.0095×**, i.e. **0.95%**. Clas-SiC, itself loss-making, manages 0.39× (`LNI-5`) — **41 times
    better.**
  - **Gross margin:** £(1,085,000) ÷ £901,000 = **−120.4%.** It costs £2.20 of direct cost to produce
    £1.00 of revenue.
  - **Loss per employee:** £56,699,000 ÷ 357 = **£158,820 per employee per year.**
  - **Cumulative loss against cumulative equity:** retained earnings £(177,348,000) ÷ share premium
    £287,025,000 = **61.8% of everything ever subscribed has been spent.**
  - **Capital intensity of the ramp:** 2025 purchases of PP&E £32,372,000 against revenue of £901,000
    = **35.9× revenue spent on plant in one year.**
- **Caveats.** These are the *company's* accounts, not a group consolidation; the group exemption is
  taken because Pragmatic Semiconductor Inc. has not begun trading. Revenue in a pre-mass-production
  company is not a measure of demand for its product, and the directors' case is precisely that
  revenue arrives after the capacity does. The "500 jobs" in the bank's release is over five years
  from 2023, so 2025 is not the terminal year. The £179m Series D and the £162m round described by the
  bank overlap and must not be added.
- **Why this is the most important entry in the file, and why it cuts against the thesis.** Pragmatic
  is the UK's flagship new fab. Its technology is *specifically* designed to be cheap: flexible ICs,
  no exotic lithography, "breakthrough low cost of customisation and rapid production cycles" in its
  own CEO's words. It is the closest thing Europe has to a fab built for a long tail of small,
  fast-turn customers. After £287 million of subscribed equity, £60 million of it from a state
  development bank, with 357 people and £95 million of plant on the books, it turned over **£901,000**
  in 2025 — **down** from £1.69 million in 2024 — from a customer book in which three customers are
  each over 10% of that. **The long tail did not turn up.** Any version of the argument that says
  small customers will pay for real capital has to say why this is not the counter-example, and
  "they built the wrong thing" is not available, because what they built is the thing the argument
  asks for.

### LNI-17. Silex's filed Swedish accounts: 301 → 412 employees in three years, and a *profitable* MEMS foundry runs payroll at about 28% of revenue

- **Source:** allabolag.se (UC Affärsinformation), company record for **Silex Microsystems AB**,
  org. nr **556591-5385**, Järfälla — key figures and accounts summary drawn from the company's filed
  annual reports.
  - Accounts: <https://www.allabolag.se/5565915385/bokslut>
  - Key figures: <https://www.allabolag.se/nyckeltal/silex-microsystems-ab/j%C3%A4rf%C3%A4lla/datorer-och-kringutrustningar-tillverkning/2K1SVSPI63ILT>
- **Verification:** Partial. The figures are read directly off allabolag's rendering of the filed
  accounts, not off the signed annual reports themselves (allabolag links the PDFs behind a
  registration wall; see "What could not be got"). The 2025 revenue of SEK 1,385,000 thousand
  reconciles exactly with the company's own IPO announcement (`LNI-1`), which is a strong check on the
  series. The 2025 employee count is shown as 0, i.e. not yet populated.
- **Date checked:** 2026-09-25
- **Bearing:** **Supports** H6, and is the single most encouraging number in this file. A pure-play
  MEMS foundry serving many customers can be solidly profitable.
- **What it says.** As printed (thousands of SEK, calendar years):

  | Year to 31 December | 2021 | 2022 | 2023 | 2024 | 2025 |
  |---|---:|---:|---:|---:|---:|
  | Nettoomsättning (net sales) | 1,020,125 | 980,557 | 1,095,243 | 1,226,000 | **1,385,000** |
  | Rörelseresultat efter avskrivningar (operating profit after depreciation) | 329,753 | 94,538 | 212,228 | 265,000 | **314,000** |
  | Anställda (employees) | 301 | 358 | 407 | **412** | not yet filed |
  | Personalkostnader per anställd, kSEK (staff cost per employee) | 679 | 725 | 732 | **830** | — |

  Swedish terms, translated: *nettoomsättning* = net turnover; *rörelseresultat efter avskrivningar* =
  operating result after depreciation; *anställda* = employees; *personalkostnader per anställd* =
  staff costs per employee.

- **DERIVED (arithmetic written out):**
  - **Revenue per employee, 2024:** SEK 1,226,000,000 ÷ 412 = **SEK 2,975,728**. At EUR/SEK 11.2645
    (ECB, 2026-09-24): **€264,169 per employee.**
  - **Revenue per employee, 2025.** Use the prospectus head count, not an aggregator's: Silex had
    **484 employees as of 31 March 2026** (`LNI-18`). SEK 1,385,000,000 ÷ 484 = SEK 2,861,570 =
    **€254,035**; annualising Q1 2026 (SEK 375m × 4) gives SEK 3,099,174 = **€275,131.** The range is
    **€254,000–€275,000 per head.**
  - **Payroll as a share of revenue, 2024:** SEK 830,000 per employee × 412 employees =
    SEK 341,960,000 of staff cost, ÷ SEK 1,226,000,000 of revenue = **27.9%.**
    **This is the benchmark the rest of the file should be read against.** Clas-SiC, loss-making, runs
    at 45.3% (`LNI-5`); CMC Microsystems, subsidised, runs at 39–46% (`FUNDX-1`); Silex, profitable,
    runs at 27.9%.
  - **Operating margin, 2025:** SEK 314,000,000 ÷ SEK 1,385,000,000 = **22.67%**, the
    **operating-company** figure (Silex Microsystems AB, filed Swedish accounts).
    **RECONCILED 2026-09-25 by `SEM-1`.** The prospectus's **consolidated group** operating profit
    for the same year is **SEK 368,000,000 = 26.57%**. The SEK 54m difference is the group's
    real-estate company, **Silex Properties AB**, whose rental income sits in Other operating
    income. Both figures are correct for what they measure; neither is an error. **Quote which one
    you mean.** The repo's convention from here: **22.67% (operating company) / 26.57% (group)**,
    and return-on-assets work uses the group figure because the balance sheet is consolidated.
  - **Head count growth:** 301 → 412 over 2021–2024 is **+36.9%**, a CAGR of **+11.0%/yr**, against
    revenue growth of SEK 1,020m → 1,226m = +20.2%, a CAGR of **+6.3%/yr**. **Silex has been adding
    people faster than revenue**, which is the opposite of the automation story, at the most
    successful small MEMS foundry in Europe.
  - **Revenue per employee against staff cost per employee, 2024:** SEK 2,975,728 ÷ SEK 830,000 =
    **3.59×.** A small fab needs roughly three and a half times payroll in revenue to be comfortably
    profitable. Clas-SiC turns over 2.21× its staff cost (£8,351,170 ÷ £3,782,638) and loses money;
    Pragmatic turns over 0.024× (`LNI-16`).
- **Caveats.** allabolag is a commercial re-publisher of Swedish filings, not the registry; the figures
  should be re-checked against Bolagsverket's own copies before being cited in `WHY.md`. **The
  prospectus (`LNI-18`) is the better source for anything it covers** — it is a regulator-approved
  document and it reconciles with this series on net sales for 2023, 2024 and 2025 to the million. Silex
  Microsystems AB is one company in a group that also includes Silex Properties AB; the group
  boundary is not established here. The 2025 employee count is not in the filed data yet.

### LNI-18. **The customer book of the world's leading pure-play MEMS foundry: about 85 customers, top ten = 77% of net sales, largest = 25%.** This is the H7 evidence, and it goes the wrong way

- **Source:** Silex Microsystems AB (publ), *Invitation to acquire ordinary shares in Silex
  Microsystems AB (publ)* — the IPO prospectus, 230 pages, approved and published by
  **Finansinspektionen** (the Swedish Financial Supervisory Authority) on **2026-04-27**, diary
  number **25-37533**, passported to Finland.
  - Register entry: <https://www.fi.se/sv/vara-register/prospektregistret/details?id=25-37533>
  - Document (11,451 kB PDF): <https://www.fi.se/sv/vara-register/prospektregistret/GetFile?id=25-37533>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **How it was counted:** The company's own site and the four bank sites named in the press release
  were dead ends. The route that works, and that should be used for any Swedish issuer, is the
  statutory register: search `https://www.fi.se/sv/vara-register/prospektregistret/?query=<name>`,
  follow the `details?id=<diary number>` link, and download `GetFile?id=<diary number>` with the
  detail page as the referer. The PDF has a proper text layer; `pdftotext -layout` gives 14,475 lines.
  Quotes below are copied from that extraction; the prospectus is in English, so no translation is
  needed except where noted.
- **Bearing:** **Challenges H7**, hard, and it is the first direct measurement of the thing
  `hypotheses.md` names as "the single most valuable piece of evidence this project could obtain".
  Mixed on H2.
- **What it says.** The risk factor, in full:

  > "**Silex has a high degree of customer concentration annually, which presents risks due to the
  > potential loss of or significant curtailment of purchases by such key customers.**
  > While Silex generates revenue from approximately 85 customers worldwide, Silex's ten largest
  > customers accounted for approximately 75 percent of Silex's net sales, and the largest customer
  > accounted for 23 percent of Silex's net sales for three months ended 31 March 2026, and Silex's
  > ten largest customers accounted for approximately 77 percent of Silex's net sales, and the largest
  > customer accounted for 25 percent of Silex's net sales for the year ended 31 December 2025."

  And the chart on p. 77, **"Top 10 customers: Share of net sales and years with Silex"**, whose
  printed share-of-net-sales-2025 column is:

  | Customer | Share of net sales, 2025 |
  |---|---:|
  | Customer #1 | **25%** |
  | Customer #2 | **19%** |
  | Customer #3 | 7% |
  | Customer #4 | 5% |
  | Customer #5 | 5% |
  | Customer #6 | 4% |
  | Customer #7 | 4% |
  | Customer #8 | 4% |
  | Customer #9 | 3% |
  | Customer #10 | 3% |
  | **Top 10** | **79% as printed; "approximately 77 percent" in the text** |

  The same chart plots relationship duration on a 2003–2025 axis, and the text gives the reading:

  > "As of 31 March 2026, eight out of Silex's ten largest customers have been Silex's customers since
  > 2017 or earlier, and Silex currently still retains its first customer and continues to manufacture
  > for it, both of which evidence the deep and longstanding relationships that Silex maintains with
  > its customers."

  The top ten's absolute net sales, year by year, as printed:

  | | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Q1 2025 | Q1 2026 |
  |---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
  | Net sales of the 2025 top-ten customers (SEK m) | 285 | 382 | 558 | 604 | 838 | 940 | **1,073** | 274 | 277 |

  Why the concentration exists, in the company's own words:

  > "Silex believes that the development of complex MEMS ­products creates significant long-term
  > stickiness, as customers invest considerable time and resources over multi-year development cycles
  > to co-develop highly specialised solutions together with the Company. This results in substantial
  > switching costs, deep integration into customers' product architectures and a strong reliance on
  > Silex's proven quality and reliability, particularly in performance-critical industries."

  The customer taxonomy, which is worth recording because it is the vocabulary of the market this
  project wants to enter:

  > "Silex's customers can be divided into Fabless customers that do not have their own MEMS or chip
  > production, Fab-light customers that make their basic chips in-house and IDMs who develop and
  > produce their own chips."

  Net sales by geography and by industry, 2025 (and Q1 2026 in brackets):

  - North America **54%** (58%), Europe 32% (31%), Asia 12% (9%), other 2% (2%).
  - Telecommunication **31%** (28%), consumer **30%** (29%), industrial and automotive 27% (25%), life
    science and medical 13% (18%).

  Head count:

  > "As of 31 March 2026, Silex had 484 employees, the majority of whom were in Sweden."

  And, on the definition that makes the headline margin readable — "Gross profit: Net sales less raw
  materials and consumables"; gross margin was **79% (2023), 82% (2024), 86% (2025)**.

- **DERIVED (arithmetic written out):**
  - **Top-ten share, checked against the absolute series:** SEK 1,073m ÷ SEK 1,385m = **77.47%** in
    2025; SEK 940m ÷ SEK 1,226m = **76.67%** in 2024; SEK 838m ÷ SEK 1,095m = **76.53%** in 2023;
    SEK 277m ÷ SEK 375m = **73.87%** in Q1 2026. **This is not a one-year artefact.**
  - **The comparison that matters.** TSMC's top ten customers were **76%** of revenue (`CONC-1`) and
    **78%** in 2025 (`CONC-11`). Silex's are **77%**. **The world's leading pure-play MEMS foundry,
    serving four separate end industries from a single 200 mm fab, has the same revenue concentration
    as the largest foundry on earth.** Specialty, diversity of application and twenty-year
    relationships did not produce dispersion.
  - **Effective number of customers (reciprocal Herfindahl, the measure
    [`analyses/data-cuts-and-statistics.md`](../analyses/data-cuts-and-statistics.md) introduced).**
    Using the printed chart and assuming the 75 customers outside the top ten split the remaining 21%
    **equally** — the assumption most favourable to dispersion, so this is an *upper bound*:
    - Top ten: 0.25² + 0.19² + 0.07² + 0.05² + 0.05² + 0.04² + 0.04² + 0.04² + 0.03² + 0.03²
      = 0.0625 + 0.0361 + 0.0049 + 0.0025 + 0.0025 + 0.0016 + 0.0016 + 0.0016 + 0.0009 + 0.0009
      = **0.1151**
    - Tail: 75 × (0.21 ÷ 75)² = 0.21² ÷ 75 = 0.0441 ÷ 75 = **0.000588**
    - H = 0.1151 + 0.000588 = **0.115688**; **1/H = 8.64 effective customers.**
    - As a share of the nominal count: 8.64 ÷ 85 = **10.2%.**
    - Rescaling the chart to the reported 77.47% top-ten share instead of the printed 79% gives
      H = 0.111347, 1/H = **8.98**, and 8.98 ÷ 85 = **10.6%**. The honest range is
      **8.6–9.0 effective customers, 10.2–10.6% of the nominal count.**
  - **Read that against the directory's existing numbers, because it cuts two ways.** In *ratio*
    terms Silex (10.2–10.6%) is far closer to Tiny Tapeout's designers (**14.4%**) than to TSMC
    (**2.3%**). In *absolute* terms Silex has **8.6–9.0 effective customers against TSMC's 11.8** —
    **the specialty MEMS foundry is more dependent on a handful of customers than TSMC is.** The
    ratio flatters Silex only because it has 85 customers rather than 522. For H7, which is about
    whether losing any one customer is noise, the absolute number is the one that decides it, and
    losing Customer #1 would remove **a quarter of net sales**.
  - **What a Silex customer is worth.** SEK 1,385m ÷ 85 = **SEK 16.3m per customer per year**, or
    **€1,447,000** at EUR/SEK 11.2645. Compare `DEM-15`: TSMC's customers average about
    **US$41 million** a year each. Silex's average customer is roughly **28× smaller than TSMC's** —
    and still a **€1.4 million-a-year company**.
  - **And what Silex's *tail* customer is worth.** Customers 11 to 85 — 75 of them — share
    21% of SEK 1,385m = **SEK 290.85m**, i.e. **SEK 3.878m each**, or **€344,250 per year each**
    (equal-split assumption again, so this is the *central* figure of a distribution that is certainly
    skewed). **The "tail" of the world's leading MEMS foundry is customers paying about a third of a
    million euros a year.** A JLC long-tail customer places orders averaging **US$67** (`SMB-1`).
    That is a factor of about **5,000×**. This is the number
    [`analyses/customers-needed-to-fill-a-fab.md`](../analyses/customers-needed-to-fill-a-fab.md)
    needs: the empirical tail of a real specialty fab is not small customers, it is mid-sized
    companies.
  - **Revenue per employee:** SEK 1,385,000,000 ÷ 484 = **SEK 2,861,570 = €254,035.** Annualising Q1
    2026 instead (SEK 375m × 4 = SEK 1,500m): SEK 3,099,174 = **€275,131.** Both supersede the
    €559,000 that dividing by the municipality's "220 engineers and technicians" produced in the first
    version of `LNI-2`.
  - **Materials are 14% of the price of a MEMS wafer.** Gross margin, defined by the prospectus as
    "net sales less raw materials and consumables", was **86%** in 2025. So **86 pence in every pound
    a MEMS customer pays is labour, depreciation, overhead and margin — not silicon.** This is
    `SMB-11` ("almost none of what a small customer pays is silicon") measured at a real fab, and it
    is the reason "silicon is cheap" does not imply the price can fall.
  - **Top-ten growth against total growth, 2019–2025:** the 2025 top ten grew SEK 285m → 1,073m,
    **×3.76**. Total net sales over 2021–2025 grew SEK 1,020m → 1,385m, **×1.36**. **The
    concentration has been getting worse, not better, while the company grew.**
- **Caveats.** The per-customer chart percentages are printed to whole numbers and sum to 79 against
  a stated "approximately 77 percent", so the Herfindahl is computed twice and given as a range. The
  85-customer count is "approximately". The equal-split tail assumption is stated at each use and is
  the most favourable one available; a skewed tail would make the effective number *lower* and the
  average tail customer *smaller than* €344,250 for most of them and much larger for a few. "Gross
  margin" here is materials-only and is **not** comparable to the gross margins quoted for Clas-SiC
  (`LNI-5`) or Pragmatic (`LNI-16`), which are after full cost of sales.
- **Why it matters and what it does to H7.** H7 says that with thousands of small customers none has
  leverage and losing any one is noise. The best specialty foundry in Europe — profitable, growing,
  serving four industries, twenty-year relationships — has **85** customers, a **25%** largest
  customer and **8.6–9.0** effective ones. It did not escape concentration by being specialised; it is
  as concentrated as TSMC. **H7's mechanism therefore requires the customer count to be genuinely
  enormous, in the thousands, not merely "many".** The PCB evidence already said the threshold was
  about a million customers before concentration collapsed (`PCB-5`, `SMB-1`); this says the same
  thing inside a wafer fab. The counter-reading, and it is a real one, is that Silex is highly
  profitable *with* that concentration — 22.7% operating margin, 86% materials margin, organic growth
  in 11 of the last 12 years — which is evidence against **H2**, not for it.

### LNI-19. Silex's prospectus splits revenue between customers in **development** and customers in **volume production** — and in Q1 2026 development overtook production

- **Source:** as `LNI-18` — Silex Microsystems AB (publ), IPO prospectus, Finansinspektionen diary
  number 25-37533, 2026-04-27, pp. 44–45 and 90–91.
  <https://www.fi.se/sv/vara-register/prospektregistret/GetFile?id=25-37533>
- **Verification:** Verified
- **Date checked:** 2026-09-25
- **Bearing:** **Supports H5 and H6.** This is the closest thing found to the JLC-style
  margin-by-order-size disclosure this directory has hunted across five industries, translated into
  the language of a fab: revenue from customers who are still prototyping, against revenue from
  customers in mass production.
- **What it says.** The split, as printed:

  | | 2023 | 2024 | 2025 | Q1 2025 | Q1 2026 |
  |---|---:|---:|---:|---:|---:|
  | Net sales from customers in the **development** phase (SEK m) | 404 | 422 | **614** | 134 | **191** |
  | Net sales from customers in the **volume production** phase (SEK m) | 691 | 804 | **771** | 200 | **185** |
  | Total net sales (SEK m) | 1,095 | 1,226 | 1,385 | 334 | 375 |

  > "Between 2023 and 2025, Silex's net sales ­generated from customers in the development phase grew
  > at a CAGR of 23 percent and Silex's net sales from customers in the volume production phase grew
  > at a CAGR of 6 percent. Silex estimates that in any given year, approximately 60 percent of
  > Silex's net sales is generated from customers that are in the volume production phase during the
  > relevant period. Correspondingly, approximately 40 percent of Silex's net sales is generated from
  > customers that are in the development phase during the relevant period."

  **On profitability across the two phases — the answer to the question `PCB-13` and `OIM-5` were
  asking:**

  > "Due to the payment mechanisms included in Silex's customer contracts, Silex's profit­ability is
  > fairly stable throughout the engagement phases, with payment received across various milestones of
  > the development and production qualification process. However, high volume orders for MEMS in the
  > volume production phase usually have a higher order value, which enables higher profits in
  > absolute terms for Silex."

  and, elsewhere in the same document:

  > "Another example of how Silex creates long-term value for its customers is its ability to support
  > them from early development through to full-scale production, **often maintaining comparable
  > margins across both phases**." *(emphasis ours)*

  **The funnel, stated as a number:**

  > "Silex undertakes on average approximately 15 new customer development programmes each year,
  > however, according to the Company's assessment, customer confidence was strengthened following the
  > new Swedish ownership, resulting in 24 new programmes in 2025."

  > "Based on Silex's experience, out of the approximately 15 customers that enter the development
  > phase, typically one or two ultimately progress to high-volume, high-revenue production. As Silex
  > generates revenue throughout the MEMS production process, from the development phase to the
  > production phase, customers' that do not reach the volume production phase still generate revenue
  > for Silex."

  > "Across Silex's portfolio, programmes that successfully transition to production typically
  > generate initial annual revenues of approximately SEK 10 to 20 million in their first year of
  > volume manufacturing. Over a period of two to four years, these programmes generally ramp up to
  > achieve peak annual revenues in the range of SEK 50 to 100 million…"

  > "As of 31 March 2026, approximately 20 customer programmes were in the production phase…"

  The shape of a development engagement:

  > "The MEMS development phase typically spans two to five years, with each development cycle lasting
  > around six months and involving between 200 and 700 process steps."

  And the commercial terms, which answer "who pays and when":

  > "…Silex generally requires an upfront initial instalment of at least 15 percent to support the
  > additional capacity-related investments. Allocation of resources for early development programmes
  > is determined through agreements with the customer. Customers have the option to increase resource
  > allocation and accelerate development timelines by committing additional funding to the
  > programme."

- **DERIVED (arithmetic written out):**
  - **Development overtook production in Q1 2026:** SEK 191m against SEK 185m, i.e. **50.8% of net
    sales came from customers who are still prototyping.** A year earlier it was 134 ÷ 334 = **40.1%**.
  - **Development-phase share by year:** 404 ÷ 1,095 = **36.9%** (2023); 422 ÷ 1,226 = **34.4%**
    (2024); 614 ÷ 1,385 = **44.3%** (2025).
  - **The growth is entirely on the prototyping side.** Development SEK 404m → 614m over two years is
    a CAGR of √(614/404) − 1 = **+23.3%/yr**; volume production SEK 691m → 771m is
    √(771/691) − 1 = **+5.6%/yr**. Of the SEK 290m of net-sales growth from 2023 to 2025,
    **SEK 210m (72.4%)** came from customers in development and SEK 80m (27.6%) from customers in
    volume production.
  - **Conversion rate:** 1 to 2 out of approximately 15 = **6.7% to 13.3%.** With 24 new programmes in
    2025 and the same rate, that is 1.6 to 3.2 programmes a year reaching volume.
  - **The lifetime value of a converted programme:** SEK 10–20m in year one, ramping over two to four
    years to SEK 50–100m a year at peak. At the midpoints — SEK 15m rising to SEK 75m — one converted
    programme is worth about **€6.66 million a year at peak** (SEK 75m ÷ 11.2645).
  - **What the 13 or 14 that do *not* convert are worth.** 2025 development-phase net sales were
    SEK 614m. If roughly 40–65 programmes are live in development at any time (2–5 year phase ×
    15–24 new a year), that is of order **SEK 9m–15m per development programme per year**, or
    **€800,000–€1,330,000** — and the prospectus says explicitly that these "still generate revenue
    for Silex" and that margins are "comparable across both phases".
  - **Programmes in production:** approximately 20 as of 31 March 2026, against SEK 771m of
    volume-production net sales in 2025 = **SEK 38.6m per production programme**, which sits neatly
    between the stated SEK 10–20m first year and SEK 50–100m peak.
  - **Cash terms:** a 15% minimum upfront instalment on a development programme worth SEK 9–15m a year
    is **SEK 1.35m–2.25m (€120,000–€200,000) paid before work starts.**
- **Caveats.** "Development phase" at Silex means a two-to-five-year, 200-to-700-process-step,
  co-developed custom MEMS programme with a company large enough to fund it. **It does not mean a
  hobbyist shuttle slot**, and the entry should not be read as though it did. The per-programme
  figures in the last three bullets divide a disclosed total by an *estimated* programme count and are
  order-of-magnitude only; the prospectus does not give the number of live development programmes.
  "Comparable margins across both phases" is a company statement, not a disclosed margin split.
- **Why this supports the thesis.** Two things here are genuinely strong evidence for H5 and H6, and
  they are the best in this file. **First, prototyping is not a loss-leader at a real fab** — Silex
  says its profitability is "fairly stable throughout the engagement phases" and that it often
  maintains "comparable margins across both phases". Every other data point in this directory on
  small-batch margin comes from PCBs (`PCB-7`, `PCB-13`) or from a MEMS owner's segment disclosure
  (`OIM-5`); this is the fab itself saying it in a prospectus. **Second, the prototyping side is where
  the growth is**: +23.3%/yr against +5.6%/yr, 72% of all growth, and in Q1 2026 it became the larger
  half of the business. A foundry whose development-phase revenue is growing four times as fast as its
  production revenue is the pattern H5 predicts. What it is *not* is a long tail — these are 15 to 24
  programmes a year with companies that can pay six figures up front.

### LNI-20. Kohesio, the EU's structural-fund beneficiary register, on the specialty fabs: IHP €22.4m across 9 projects, LFoundry €24.1m at a flat 50% co-financing rate — and no entry at all for X-FAB, Fraunhofer ISIT or Silex

- **Source:** European Commission, **Kohesio** — the public register of European Regional Development
  Fund, Cohesion Fund and ESF beneficiaries. <https://kohesio.ec.europa.eu/>
  Queried through the public JSON API on 2026-09-25:
  `https://kohesio.ec.europa.eu/api/beneficiaries?name=<name>&language=EN&page=0`
- **Verification:** Verified for the figures returned. **Partial as a statement about total EU
  funding**, because Kohesio's coverage is demonstrably incomplete — see the caveats, which are the
  most important part of this entry.
- **Date checked:** 2026-09-25
- **Bearing:** Context on H5 and H8, and a correction to how `LNI-3`, `LNI-4` and `LNI-6` should be
  read.
- **How it was counted:** The parameter that filters is **`name=`**. `keywords=`, `search=`,
  `beneficiary=` and `q=` are all silently ignored and return the whole register sorted by budget
  descending (709,684 beneficiaries), which is a trap: a query that looks like it worked returns
  Poland's national roads agency at the top. There is **no working per-project drill-down by
  beneficiary** on this API surface — `/api/projects?beneficiary=<entity>` also ignores the filter and
  returns all 2,269,971 projects — so only the beneficiary-level aggregates below could be obtained.
- **What it says.** Every row exactly as returned:

  | Beneficiary | Country | Projects | Total budget | EU budget | Co-financing rate |
  |---|---|---:|---:|---:|---:|
  | IHP GmbH – Leibniz-Institut für innovative Mikroelektronik | DE | **9** | **€22,393,213.29** | not returned | not returned |
  | IHP GmbH – Innovations for High Performance Microelectronics/Leibniz-Institut für innovative Mikroelektronik | DE | 1 | €145,100.00 | €87,060.00 | 60.0% |
  | IHP Solutions GmbH – Gesellschaft für technologiebasierten Innovationstransfer | DE | 3 | €21,125.50 | not returned | not returned |
  | **LFOUNDRY SRL** | IT | **3** | **€24,138,334.64** | **€12,069,167.32** | **50.0%** |
  | SOITEC LAB | FR | 1 | €6,525,000.00 | €3,100,000.00 | 47.51% |
  | Melexis GmbH | DE | 1 | €278,075.00 | not returned | not returned |

  Searches returning **nothing relevant**: `X-FAB` / `X-Fab` / `XFAB` (293 fuzzy hits, none of them
  the foundry — the top hits are the city of Warsaw and an Austrian employment charity called FAB);
  `Fraunhofer-Institut fur Siliziumtechnologie`, `Siliziumtechnologie`, `ISIT` and `Itzehoe` (0
  relevant); `Elmos` (0); `Silex` (4 hits, none of them the MEMS foundry — a Hungarian water-treatment
  company, a Hungarian automation company, a German lift servicer and a German English school).
  Searching `Fraunhofer` alone returns 40 beneficiaries with a combined budget of
  **€2,296,681,833.31**, none of which is identifiable as ISIT.

- **DERIVED (arithmetic written out):**
  - **IHP's three Kohesio identities together:** €22,393,213.29 + €145,100.00 + €21,125.50 =
    **€22,559,438.79** across **13 projects**, i.e. **€1,735,341 per project**.
  - **The €11.7m ERDF cleanroom grant in `LNI-3` is 52.2% of IHP's whole Kohesio total**
    (€11,700,000 ÷ €22,393,213.29). Either the cleanroom is the single dominant ERDF item in IHP's
    history, or — more likely, given the coverage gaps below — Kohesio does not hold all of it. The
    figures in `LNI-3` come from the Brandenburg ministry and the Brandenburg ERDF managing authority
    directly and should be preferred.
  - **LFoundry's EU money against its announced capex.** €12,069,167.32 of EU money against the €40m
    expansion in `LNI-4` is **30.2%** — though the Kohesio projects are not necessarily the same
    programme, and the *contratto di espansione* is a national labour instrument, not an ERDF one. The
    flat **50.0%** co-financing rate across all three LFoundry projects is the standard
    more-developed-region ERDF rate; Abruzzo is a transition region, so this is the rule, not a
    favour.
  - **EU money per job at LFoundry, on the `LNI-4` arithmetic:** €12,069,167.32 ÷ 13 new permanent
    jobs = **€928,397 of EU money per job**, if the two are connected — which is not established, and
    is recorded here as a bound rather than a claim.
- **Caveats, and they dominate this entry.** **Kohesio is not a complete record of EU money to these
  companies.** X-FAB — six fabs, four of them in the EU, including two in ERDF-eligible eastern
  Germany — has no entry at all. Fraunhofer ISIT, whose 2008 expansion the Schleswig-Holstein minister
  explicitly said would draw on "EU-Fördermittel" (`LNI-9`), has no entry. Silex, in Sweden, has no
  entry. Absence in Kohesio is evidence about Kohesio's coverage, not about the beneficiary. Coverage
  varies by member state, by programming period and by managing authority, and the pre-2014 periods
  are thin. Do not write "X-FAB received no EU structural funds"; write "Kohesio has no entry for
  X-FAB". The `euBudget` and `cofinancingRate` fields come back empty for several German
  beneficiaries, so the German totals are total project cost, not EU contribution.

---

## What the numbers add up to

Every figure below is derived in the entry named, with its arithmetic written out there.

### Capital cost per job

| Site | What was announced | Jobs | Capital per job | Entry |
|---|---|---:|---:|---|
| Fraunhofer ISIT, Itzehoe (2008) | €45m expansion | 200 (long term) | **€225,000** | `LNI-9` |
| Tyndall, Cork | >€100m | 580 existing | €172,000 per existing head | `LNI-15` |
| KLA, Newport (HQ + innovation centre) | US$100m | 750 | US$133,000 | `LNI-14` |
| Teledyne DALSA, Bromont | C$42m | 40 new | **C$1,050,000 / €654,000** | `LNI-7` |
| **Silex, Järfälla cleanroom expansion** | **SEK 650m (prospectus)** | **70–80 new** | **SEK 8.1–9.3m / €721,000–€824,000** | `LNI-1` |
| Teledyne MEMS, Edmonton | C$20m | 16 new | **C$1,250,000 / €779,000** | `LNI-8` |
| Clas-SiC, Lochgelly | £59.0m of equity raised since 2017 | 76 employed | **£776,000 / €903,000** | `LNI-5` |
| Pragmatic, Sedgefield | £287.0m of equity raised | 357 employed | **£804,000 / €935,000** | `LNI-16` |
| Bosch, Dresden | €1bn | 700 | **€1,429,000** | `LNI-11` |
| ams OSRAM, Premstätten | €588m | 250 | **€2,352,000** | `LNI-10` |
| LFoundry, Avezzano | €40m | 13 new (net −17) | **€3,077,000** | `LNI-4` |

**Two findings.** First, **capital per job does not fall as the fab gets smaller.** The
smallest MEMS foundry in the table (Edmonton, 16 jobs) costs more per job than the billion-euro
Bosch fab. Second, the cluster is tight: **five** independent small-fab figures — Bromont, Edmonton,
Clas-SiC, Pragmatic and Silex's own prospectus, across Canada, the UK and Sweden, in announcements,
audited accounts and a regulator-approved prospectus alike — land between **€650,000 and €935,000 of
capital per job.** Institute and office jobs, by contrast, cost
**€130,000–€230,000**. The gap is process equipment.

### Capital cost per unit of capacity

| Measure | Figure | Entry |
|---|---:|---|
| Cleanroom shell only, per m² (IHP, gross floor area) | **€3,947/m²** | `LNI-3` |
| Cleanroom shell only, per m² of cleanroom (X-FAB Dresden) | **US$12,500/m²** | `LNI-6` |
| Cleanroom shell only, per m² of cleanroom (IHP) | **€30,000/m²** | `LNI-3` |
| Cleanroom expansion incl. tools, per m² (Silex, planned, corrected to SEK 650m) | **€38,469/m²** | `LNI-1` |
| Cleanroom expansion incl. tools, per m² (Fraunhofer ISIT) | **€45,000/m²** | `LNI-9` |
| Cleanroom expansion incl. tools, per m² (X-FAB Dresden) | **US$155,357/m²** | `LNI-6` |
| **Per wafer start per month, at the margin (X-FAB Dresden)** | **US$41,587** | `LNI-6` |
| Capex ÷ one year's incremental revenue (Silex, corrected) | **1.34×** | `LNI-1` |
| Wafer starts per month per m² of cleanroom (X-FAB Dresden) | 3.07 | `LNI-6` |

**The finding:** X-FAB Dresden puts **92% of a brownfield fab expansion into equipment and 8% into
the building**. Cleanroom floor is an ordinary industrial construction cost. The tools are not, and
nothing in the open-source, open-PDK, automated-flow argument touches the price of a deposition tool.

### Does the money come back?

| Company | Revenue per employee | Payroll as % of revenue | Result |
|---|---:|---:|---|
| Silex Microsystems (484 staff, prospectus) | **€254,035** | **27.9%** | operating profit, 22.7% margin (2025); 86% materials margin |
| X-FAB group (2023, reported) | US$176,190 | not disclosed | — |
| Clas-SiC Wafer Fab (FY2025, audited) | £109,884 | **45.3%** | gross **loss**, −8.6% |
| CMC Microsystems (`FUNDX-1`) | — | 39–46% | deficit in 4 of 5 years |
| Pragmatic Semiconductor (2025, audited) | **£2,524** | **4,101%** | £64.9m loss, going-concern uncertainty |

### The honest summary, including what cuts against the thesis

**Against.** The thesis is that a large number of very small customers can pay for real capital.
Three things in this file argue they cannot, and they should be read before anything else.

1. **Pragmatic** (`LNI-16`). A fab built deliberately for cheap, fast, small-batch, highly
   customisable chips — the exact product the thesis calls for — has raised £287 million, employs 357
   people, and turned over **£901,000** in 2025, down from £1.69 million, with three customers each
   over 10% of that. This is the strongest single counter-example in the directory.
2. **Capital per job is flat across two orders of magnitude of fab size** (table above), and it sits
   at €650,000–€935,000 for small Western fabs. At Silex's revenue of €264,000 per head, a small fab
   must sell roughly **2.5 to 3.5 years of revenue per employee** just to return the capital that
   employee sits on, before wages.
3. **LFoundry** (`LNI-4`): €40 million of capacity expansion, 13 new permanent jobs and a net head
   count *fall* of 17. Capacity at a mature-node fab is bought with equipment, and equipment is what
   a tail of €10,000 customers would have to fund.

**And a fourth, which is the one that moves a hypothesis.** `LNI-18` is the first time anyone in this
directory has seen the revenue distribution across a real specialty fab's customer book, and **H7
loses.** Silex — profitable, growing, four end industries, twenty-year relationships, exactly the
"many small customers" foundry the hypothesis imagines — has **approximately 85 customers**, a **top
ten at 77% of net sales** and a **largest customer at 25%**. TSMC's top ten are 76–78%. Silex's
**effective number of customers is 8.6–9.0, fewer than TSMC's 11.8**, and the concentration has been
*rising*: the 2025 top ten grew ×3.76 since 2019 while total net sales grew ×1.36. Its "tail" —
customers 11 through 85 — averages about **€344,000 of spend a year each**, against **US$67 an order**
for a JLC long-tail customer. Being specialised did not buy dispersion. Only counts in the thousands
ever have.

**And a fifth, about the brokers rather than the fabs.** CORNERSTONE told EPSRC in 2020 that its MPW
capability "will be self-sustaining, with users paying for the service" from December 2019, and has
taken **£14.8 million** of further EPSRC money since (`LNI-12`). The public subsidy works out at
£5,900–£19,000 per design fabricated (`LNI-13`), against a list price of £12,790 for a passive SOI
cell. This is the MOSIS pattern (`MOS-*`) repeating in the UK, in the 2020s, with the receipts in the
funder's own database.

**For.** Three things genuinely support the thesis, and they are not small.

1. **Silex** (`LNI-17`, `LNI-1`). A pure-play MEMS foundry with 412 people, 22.7% operating margins,
   payroll at 27.9% of revenue, and a capacity expansion that pays back in about one year of
   incremental revenue. **Small, specialty, many-customer fabs can be very profitable.** Silex went
   from a 100 m² room in 2002 to a Nasdaq Stockholm listing at SEK 8.9 billion.
2. **Prototyping is not a loss-leader, and it is where the growth is (`LNI-19`).** Silex's
   prospectus splits net sales between customers in the development phase and customers in volume
   production: SEK 404m/691m (2023), 422m/804m (2024), 614m/771m (2025) and **SEK 191m against
   SEK 185m in Q1 2026 — the first quarter in which the prototyping half was the larger one.**
   Development grew **+23.3%/yr** against volume production's **+5.6%/yr** and accounts for **72.4% of
   all growth 2023–2025**. The company says its "profitability is fairly stable throughout the
   engagement phases" and that it often maintains "comparable margins across both phases". Every other
   small-batch-margin data point in this directory comes from PCBs or from a segment note; this is the
   fab itself saying it in a regulator-approved document.
3. **The customers exist and they are numerous.** Fraunhofer ISIT had "over 350 companies" in its
   contract-research book with 150 staff in 2008 (`LNI-9`). CORNERSTONE has fabricated "over 900
   unique SiPh designs for over 130 organisations in 26 countries" since 2017 — 6.9 designs per
   organisation, which is repeat business, not tourism (`LNI-13`). Canada's federal government states
   flatly that "Canadian research centres and SMEs benefit from access to their infrastructure for the
   design, prototyping and high-volume production of innovative products" at Bromont and Edmonton
   (`LNI-7`). Clas-SiC's audited strategic report says it is deliberately "reprioritising customers to
   those needing rapid prototyping" (`LNI-5`).
4. **The fixed cost of serving one customer is visible and it is not enormous.** CORNERSTONE's own
   price list charges 60.1% of the large-cell price for a cell 48.0% of the size (`LNI-13`), which
   implies roughly 20–40% of a small order's price is the cost of having a customer at all. That is
   the number automation has to attack, and it is a fraction, not a multiple.

**The balance, restated after the prospectus (2026-09-25).** The capital numbers are worse than the
project's framing assumes, the *margin* numbers are better, and the *customer-count* numbers are much
worse. A small fab costs about three quarters of a million euros per job wherever you look — five
independent sites now agree — and 92% of that is tools. A small fab that is *full* is a
23%-operating-margin business, and its prototyping work earns comparable margins to its production
work and grows four times faster. But **it is full with 85 customers, not with thousands**, its
largest customer is a quarter of its revenue, and its typical tail customer spends €344,000 a year.

So the shape of the answer has changed. It is no longer "does a long tail of small customers exist
and can it pay?" It is: **the economics of serving prototype and low-volume work at a fab are
genuinely good — Silex proves that — but every fab that has succeeded at it has done so with a few
dozen mid-sized corporate customers, and every attempt to do it with a genuinely large number of very
small ones (Pragmatic, and the subsidised MPWs in `LNI-12`) is either loss-making or publicly
funded.** The open question is no longer whether the margin is there. It is whether the customer
count can be got to the thousands without the average customer shrinking by the 5,000× that separates
a Silex tail customer from a JLC one — and nothing found here says it can.

---

## What I could not get, and why

Blocked items with the blocker named, so nobody repeats the work.

1. **Affärsvärlden, "Järfälla vill stoppa miljardinvestering – kopplas till Kinas militär"**
   (<https://www.affarsvarlden.se/artikel/jarfalla-vill-stoppa-miljardinvestering-kopplas-till-kinas-militar>).
   This is the source of the widely repeated **SEK ~3 billion** figure for the Silex 300 mm plan in
   Veddesta, and of the 37,000 m² plot. `curl` with a normal desktop user agent hits an infinite
   redirect loop (`curl: (47) Maximum (50) redirects followed`, HTTP 302) — a consent/paywall
   redirect cycle. **The SEK 3bn figure is therefore recorded nowhere in this file as a fact**, only
   as something that could not be verified. `LNI-2` uses only what *Mitt i*, *SE Nytt*, *Evertiq* and
   Järfälla kommun say.
2. **The Silex IPO prospectus — ✅ RESOLVED 2026-09-25, see `LNI-18` and `LNI-19`.** It was
   never on the company site or on any of the four bank sites the press release names
   (`silexmicrosystems.com`, `abgsc.com`, `seb.se`, `nordea.se/prospekt`, `avanza.se`), which is why
   the first pass missed it. It is in the **statutory register**, and that is where to look for any
   Swedish issuer: Finansinspektionen's Prospektregistret,
   `https://www.fi.se/sv/vara-register/prospektregistret/?query=<name>` → `details?id=<diary number>`
   → `GetFile?id=<diary number>` with the detail page as referer. Silex is diary number **25-37533**,
   approved 2026-04-27, 230 pages, 11.7 MB, with a proper text layer. It carried the customer
   concentration table, the development-versus-production revenue split, the head count, the staffing
   of the expansion and a correction to the capex figure in `LNI-1`.

   **CORRECTED 2026-09-25 by `SEM-1`, which re-read the same document.** The sentence that stood here
   — "It did not carry wafer starts or cleanroom utilisation… those two appear nowhere in 230 pages"
   — was **half wrong, and it was the half that mattered**. The prospectus **does** state cleanroom
   utilisation: **"approximately 60 percent"**, printed on pp. 25, 86 and 119, alongside the company's
   own claim of **"approximately 100 percent additional revenue"** available from the existing plant,
   fixed costs at **54% of total expenses**, and cumulative capital expenditure since founding of
   **SEK 1.9 billion**. That materially changes the reading of `LNI-17`: Silex earns its margin at
   **60% utilisation**, not at capacity.

   **Wafer starts and average selling price genuinely are absent**, and that negative has now been
   verified rather than repeated — the word "wafer" appears **89 times** in the prospectus and never
   next to a volume or a price.

   The remaining gap, restated: **no wafer-start or wafer-price figure has been found for any
   pure-play specialty fab.** `LNI-6` (X-FAB Dresden, 11,500 wspm on 3,680 m²) is the only wafer-start
   number in this file, and it comes from a local news report, not a filing.
3. **Pragmatic Semiconductor's accounts are a scanned PDF.** Companies House serves
   `format=pdf` only (no iXBRL) for company 07423954, and the file has no text layer:
   `pdftotext -layout` returns 42 bytes from 42 pages, and `gs` rewriting does not help. No
   `tesseract` or `ocrmypdf` is installed on this machine. The figures in `LNI-16` were read off the
   page images instead, which worked but is slow; anyone re-checking should do the same rather than
   trust a text extraction.
4. **Clas-SiC's PDF accounts are likewise unreadable** by `pdftotext` (`Illegal character in hex
   string`, 0 bytes out). The route that worked is the **iXBRL** version:
   `.../document?format=xhtml&download=1`. Use that for any Companies House filing that offers it.
5. **canada.ca will not complete a fetch from here.** Both the French and English ISED releases
   return `curl: (92) HTTP/2 stream 1 was not closed cleanly: INTERNAL_ERROR` on HTTP/2 and time out
   on `--http1.1`. The Internet Archive capture of 2026-08-29 served the full page and is what
   `LNI-7` quotes.
6. **elektroniknet.de** (the fullest German trade report on Bosch Dresden) returns an empty body to
   a scripted fetch. The Saxon state economic development agency's page was used instead, which is why
   `LNI-11` is **Partial** and does not carry the federal subsidy figure.
7. **Investissement Québec's press-release archive** renders its release bodies client-side; the 2014
   release announcing C$13m against a C$67.3m Teledyne project creating 300 jobs and maintaining 425
   could not be read, only its URL slug. That would have given a second Bromont capital-per-job point
   a decade earlier. Not used.
8. **allabolag.se puts the actual filed Swedish annual reports behind a registration wall.** The key
   figures in `LNI-17` are allabolag's rendering, not Bolagsverket's own documents, which is why that
   entry is **Partial**. No account was created, because this task is read-only.
9. **La Voix de l'Est** is behind a soft paywall; the article was read through a summarising fetch,
   not as raw text, so `LNI-7` marks its distinctive claims as reported rather than quoted.
10. **Kohesio — ✅ done 2026-09-25, see `LNI-20`, but it under-delivered.** The beneficiary-level
    aggregates came back cleanly for IHP, LFoundry, Soitec and Melexis. Two things did not work.
    First, **there is no per-project drill-down by beneficiary** on the public API:
    `/api/projects?beneficiary=<entity>` silently ignores the filter and returns all 2,269,971
    projects, as do `keywords=`, `search=` and `q=` on `/api/beneficiaries` (only `name=` filters).
    Second, **Kohesio simply has no entry for X-FAB, Fraunhofer ISIT or Silex**, so `LNI-6` and
    `LNI-9` gained nothing. **No CORDIS bulk CSV pull was attempted** — CORDIS covers Framework
    Programme research grants rather than structural funds, and would be the right source for IHP's
    and Tyndall's Horizon money, which is still unmeasured here.
11. **No wafer-price or customer-count disclosure was found for any of the pure-play fabs.** Silex,
    X-FAB and Teledyne MEMS all decline to publish wafer starts by customer, price per wafer, or the
    number of customers. Only CORNERSTONE (`LNI-13`) and Fraunhofer ISIT (`LNI-9`) put a customer
    count in public, and neither publishes the distribution of spend across it.
