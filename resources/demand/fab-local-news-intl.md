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

### LNI-1. Silex Microsystems, Järfälla: SEK 500 million buys 1,500 m² of extra cleanroom and 35% more capacity at an existing 200 mm MEMS fab

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

- **DERIVED (arithmetic written out):**
  - **Capital per square metre of cleanroom added:** SEK 500,000,000 ÷ 1,500 m² = **SEK 333,333/m²**.
    At the ECB reference rate of 2026-09-24, EUR/SEK 11.2645: SEK 333,333 ÷ 11.2645 = **€29,592/m²**.
  - **Cleanroom area check:** 5,500 m² − 4,000 m² = 1,500 m², i.e. **+37.5% of area for +35% of
    capacity**. The expansion is close to linear in floor area; there is no area economy of scale
    visible here.
  - **Capital per unit of annual revenue capacity:** 2025 net sales SEK 1,385m × 35% = **SEK 485m** of
    additional annual revenue at the same utilisation and price. SEK 500m of capex ÷ SEK 485m =
    **1.03× one year's incremental revenue**. A small MEMS fab's brownfield capacity therefore costs
    roughly one year of the revenue it will produce.
  - **US fab, for comparison:** SEK 1,400m ÷ 11.2645 = **€124.3m** for acquiring and converting an
    existing 200 mm IC fab with 3,000 m² of cleanroom — **€41,433/m²**, i.e. 1.4× the Järfälla
    brownfield rate, for a fab bought rather than built.
- **Caveats.** SEK 500m is the *company's estimate* of a 2027–2029 programme, not spend already
  incurred. It is unclear from the announcement how much of it is shell and how much is tools;
  `LNI-3` suggests the shell alone can absorb most of a number of this size. "Capacity" is not
  defined in wafer starts. The 1.03× revenue ratio assumes the added capacity sells at 2025 prices
  and 2025 utilisation, which is an assumption, not a disclosure.

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
  - **Revenue per employee today:** SEK 1,385m (2025 net sales, `LNI-1`) ÷ 220 = **SEK 6.30m per
    head**; ÷ 11.2645 = **€559,000 per head**. This is the number a would-be small fab has to match
    to pay a European wage bill.
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
