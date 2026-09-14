# Open silicon and AI (`OPEN`)

Open process design kits (PDKs), open design tools, low-cost shuttles, AI-assisted chip design, and the failures. This is evidence for and against H4, H5 and H6.

---

### OPEN-1. The first foundry-supported open design kit, with free manufacturing for selected open designs

- **Source:** SkyWater Technology, "Google Partners with SkyWater and Efabless to Enable Open Source Manufacturing of Custom ASICs", 2020-11-12: <https://www.skywatertechnology.com/google-partners-with-skywater-and-efabless-to-enable-open-source-manufacturing-of-custom-asics/>
- **Verification:** Verified 2026-09-13.
- **What it says:**
  - The programme is enabled by "the first foundry-supported open source process design kit (PDK) for 130 nm mixed-signal CMOS technologies (SKY130 process)".
  - "open source designs selected by the program will be fabricated at no cost to the designers."
  - Per a search summary: Efabless released an Apache 2.0-licensed open-source design flow, openLANE.
- **Bears on:**
  - H4 (supports).
  - H5 (context): a test of latent demand when manufacturing is free.
- **Used in:** `WHY.md` §4.
- **Caveats:** free manufacturing was paid for by Google, which is a subsidy, not a business model.
- **To find:** how many designs the Google Open MPW shuttles received and manufactured, as evidence for H5.

### OPEN-2. GlobalFoundries' 180nm open design kit is still a preview

- **Source:** Google and GlobalFoundries, GF180MCU open-source PDK repository: <https://github.com/google/gf180mcu-pdk>
- **Verification:** Verified 2026-09-13.
- **What it says:**
  - "Current Status -- Experimental Preview".
  - "Google and GlobalFoundries are currently treating the current content as an experimental preview / alpha release."
  - "While the GF180MCU process node and the PDK from which this open source release was derived have been used to create many designs that have been successfully manufactured commercially in significant quantities, the open source PDK is not intended to be used for production settings at this current time."
- **Bears on:** H4 (mixed): open, but not yet for production.
- **Used in:** `WHY.md` §4.
- **Leads:** Google Open Source Blog, "Announcing GlobalFoundries Open MPW Shuttle Program", October 2022 (the page rate-limited us). Per a search summary it describes Google-sponsored no-cost shuttles, with the first test shuttle open for submissions 2022-10-31 to 2022-12-05.

### OPEN-3. IHP's 130nm BiCMOS open design kit is also a preview

- **Source:** IHP, IHP Open Source PDK repository: <https://github.com/IHP-GmbH/IHP-Open-PDK>
- **Verification:** Verified 2026-09-13.
- **What it says:**
  - "130nm BiCMOS Open Source PDK, dedicated for Analog/Digital, Mixed Signal and RF Design".
  - "the open source PDK is not intended to be used for production at this moment."
  - IHP is the Leibniz Institute for High Performance Microelectronics, in Frankfurt (Oder), Germany (verified from ihp-microelectronics.com).
- **Bears on:** H4 (mixed).
- **Used in:** `WHY.md` §4.

### OPEN-4. OpenROAD aims for chip layout with no human in the loop

- **Source:** The OpenROAD Project documentation: <https://openroad.readthedocs.io/en/latest/>
- **Verification:** Verified 2026-09-13.
- **What it says:**
  - OpenROAD "holistically attacks the multiple facets of today's design cost crisis: engineering resources, design tool licenses, project schedule, and risk."
  - "The IDEA program targets no-human-in-loop (NHIL) design, with 24-hour turnaround time and zero loss of power-performance-area (PPA) design quality."
  - Per the fact-check: the project "was launched in June 2018 within the DARPA IDEA program".
- **Bears on:** H4 (supports, as a goal).
- **Used in:** `WHY.md` §4.
- **Caveats:**
  - The 24-hour, no-human target is the DARPA programme's, and it's a goal, not an achievement.
  - There's no source yet on how close open tools come to commercial tools on quality of results.

### OPEN-5. Tiny Tapeout: a custom chip design for $300

- **Source:** Nick Flaherty, "Round 6 opens for Tiny Tapeout low cost ASICs", *eeNews Europe*, 2024-02-02: <https://www.eenewseurope.com/en/round-6-opens-for-tiny-tapeout-low-cost-asics/>
- **Verification:** Verified 2026-09-13.
- **What it says:**
  - "the first 100 submissions from individuals are only increasing by $50, to $150 for 1 tile, the ASIC and the demo board. For businesses, universities, and individuals after those first 100 are sold, the new price is $300 for 1 tile, the ASIC and the demo board."
  - "There were 174 submissions for the recent TT05 project, using 75% of the available space and up from 160 for TT02."
  - It "combines hundreds of ASIC designs from researchers and developers on a single chip on a 130nm process run at Skywater".
  - tinytapeout.com (checked 2026-09-13) now lists shuttles on IHP, SkyWater and GlobalFoundries processes.
- **Bears on:**
  - H4 (supports: very low cost for small digital designs).
  - H5 (supports, weakly): hundreds of paying designers per round.
- **Used in:** `WHY.md` §4.
- **Caveats:**
  - A slot is a tiny area on a shared chip, useful for learning and small experiments, not products.
  - The prices were subsidised by Efabless at the time.

### OPEN-6. A processor designed in conversation with GPT-4 was manufactured

- **Sources:**
  - NYU Tandon School of Engineering, "Chip Chat: Conversations with AI models can help create microprocessing chips, NYU Tandon researchers discover", 2023-06-05: <https://engineering.nyu.edu/news/chip-chat-conversations-ai-models-can-help-create-microprocessing-chips-nyu-tandon-researchers>
  - Jason Blocklove, Siddharth Garg, Ramesh Karri and Hammond Pearce, "Chip-Chat: Challenges and Opportunities in Conversational Hardware Design", arXiv:2305.13243, 2023: <https://arxiv.org/abs/2305.13243>
- **Verification:** Verified 2026-09-13.
- **What it says:**
  - The paper's abstract: "a hardware engineer co-architects a novel 8-bit accumulator-based microprocessor architecture with the LLM according to real-world hardware constraints. We then sent the processor to tapeout in a Skywater 130nm shuttle".
  - The press release: "This study resulted in what we believe is the first fully AI-generated HDL sent for fabrication into a physical chip". Manufacturing access was provided via Tiny Tapeout.
- **Bears on:** H4 (supports: AI lowers the skill and effort needed to describe hardware).
- **Used in:** `WHY.md` §4.
- **Caveats:**
  - A single case study, with an experienced engineer doing the verification.
  - The design is very small.

### OPEN-7. Efabless shut down after failing to complete a funding round

- **Sources:**
  - Nick Flaherty, "Tiny Tapeout hit as eFabless closes", *eeNews Europe*, 2025-03-02: <https://www.eenewseurope.com/en/tiny-tapeout-hit-as-efabless-closes/>
  - Gareth Halfacree, "Open Source Silicon Project Tiny Tapeout Hits Trouble as Efabless Shuts Its Doors", Hackster.io, 2025-03-03: <https://www.hackster.io/news/open-source-silicon-project-tiny-tapeout-hits-trouble-as-efabless-shuts-its-doors-9ac7fab1649d>
- **Verification:** Verified 2026-09-13.
- **What it says:**
  - CEO Mike Wishart: "Unfortunately, despite our best efforts, we were unable to complete our latest funding round, As a result, eFabless has shut down operations until further notice."
  - The company "has shut down over the weekend", after "struggling to raise funds in recent months".
  - Per the fact-check, Hackster says "Due to funding challenges" and "sources suggest a grant on which the company had been banking did not materialize".
  - Tiny Tapeout's in-progress shuttles were left in limbo.
- **Bears on:**
  - H4 (challenges): cheap design didn't make an intermediary viable.
  - H6 (challenges, possibly): serving many small customers through an intermediary on top of a traditional foundry didn't pay.
- **Used in:** `WHY.md` §4.
- **Caveats:**
  - One company's funding failure has many possible causes.
  - Efabless sat between customers and a conventional foundry, which is arguably the point: it didn't change the foundry's model.
  - This deserves a proper deep dive (see analyses).

### OPEN-8. AlphaChip: reinforcement learning for chip floorplanning (contested)

- **Sources:**
  - Google DeepMind, "How AlphaChip transformed computer chip design": <https://deepmind.google/blog/how-alphachip-transformed-computer-chip-design/>
  - Wikipedia, "AlphaChip (controversy)": <https://en.wikipedia.org/wiki/AlphaChip_(controversy)>
- **Verification:** **Lead.**
- **What it says (per search summaries):**
  - A *Nature* paper in 2021 described reinforcement-learning floorplanning.
  - Google says the method has been used for several generations of its TPU chips.
  - Its performance claims are disputed.
- **Bears on:** H4 (mixed).
- **Used in:** not yet. Deliberately left out of `WHY.md` because the claims are disputed.
