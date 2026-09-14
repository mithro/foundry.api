# Software analogies (`SW`)

What cloud computing and open source did to the cost of trying ideas in software. These analogies are central to `WHY.md` §1 and to hypotheses H4, H8 and H10.

---

### SW-1. The cost of running an internet application fell a hundredfold in a decade

- **Source:** Marc Andreessen, "Why Software Is Eating the World", *The Wall Street Journal*, 2011-08-20. Republished by Andreessen Horowitz: <https://a16z.com/why-software-is-eating-the-world/>
- **Verification:** Verified 2026-09-13 against the a16z republication.
- **What it says:** "In 2000, when my partner Ben Horowitz was CEO of the first cloud computing company, Loudcloud, the cost of a customer running a basic Internet application was approximately $150,000 a month. Running that same application today in Amazon's cloud costs about $1,500 a month."
- **Bears on:** H4 (supports, by analogy: when infrastructure cost falls, experimentation rises).
- **Used in:** `WHY.md` §1.
- **Caveats:** a single illustrative figure from an investor with an interest in the story, not a systematic cost study.

### SW-2. AWS launched with published, pay-as-you-go pricing and no minimum fee

- **Source:** Amazon, "Amazon Web Services Launches" (Amazon S3 press release), 2006-03-14: <https://press.aboutamazon.com/2006/3/amazon-web-services-launches>
- **Verification:** Verified 2026-09-13.
- **What it says:** "S3 lets developers pay only for what they consume and there is no minimum fee. Developers pay just $0.15 per gigabyte of storage per month and $0.20 per gigabyte of data transferred."
- **Bears on:**
  - H8 (supports): anyone could try the service at a published price, without negotiating.
  - H6 (context).
- **Used in:** `WHY.md` §1, §6.
- **Caveats:** shows what the pricing model was, not that it caused adoption.

### SW-3. Open source is worth trillions to the firms that use it, and its value is highly skewed

- **Source:** Manuel Hoffmann, Frank Nagle and Yanuo Zhou, "The Value of Open Source Software", Harvard Business School Working Paper 24-038, 2024: <https://www.hbs.edu/ris/Publication%20Files/24-038_51f8444f-502c-4139-8bf2-56eb4b65c58a.pdf>
- **Verification:** Verified 2026-09-13 (PDF text).
- **What it says:**
  - "We estimate the supply-side value of widely-used OSS is $4.15 billion, but that the demand-side value is much larger at $8.8 trillion."
  - "We find that firms would need to spend 3.5 times more on software than they currently do if OSS did not exist."
  - "96% of the demand-side value is created by only 5% of OSS developers."
- **Bears on:**
  - H4 (supports, by analogy: shared, free building blocks cut costs).
  - H10 (supports: value is concentrated in a few contributors).
- **Used in:** `WHY.md` §1.
- **Caveats:** the demand-side value is a replacement-cost estimate, not measured revenue. Critics have questioned the method, for example "Questioning 'The Value of Open Source Software'" on Open Path, which is a Lead we haven't read.

### SW-4. Entrepreneurship is experimentation with skewed, unknowable outcomes, and cheaper technology led to more of it

- **Source:** William R. Kerr, Ramana Nanda and Matthew Rhodes-Kropf, "Entrepreneurship as Experimentation", NBER Working Paper 20358, 2014, published in the *Journal of Economic Perspectives* 28(3): <https://www.nber.org/system/files/working_papers/w20358/w20358.pdf>
- **Verification:** Verified 2026-09-13 (PDF text).
- **What it says:**
  - "We argue that entrepreneurship is about experimentation: the probabilities of success are low, extremely skewed and unknowable until an investment is made."
  - "About 55 percent of startups that received venture capital over this period were terminated at a loss, and only 6 percent of them returned more than five times their investment." Per the fact-check, that 6% "accounted for about 50 percent of the gross return".
  - Cheaper technology, including open source software and cloud computing: "This reduced entry barrier has led to an explosion of experimentation with new entrepreneurial ideas in this area."
- **Bears on:**
  - H10 (supports: skewed outcomes).
  - H4 and H5 (supports: cheaper experiments lead to more experiments).
- **Used in:** `WHY.md` §1, §6.
- **Caveats:** the sample is venture-backed start-ups in one period; see the paper for its dates.

### SW-5. On AWS, committed buyers pay far less per unit than on-demand buyers

- **Source:** AWS pricing pages, as cited in an external investor brief (see [`../analyses/tyranny-of-the-whale-brief.md`](../analyses/tyranny-of-the-whale-brief.md)).
- **Verification:** **Lead.** We haven't checked AWS's current pages.
- **What it says (per the brief):** Standard Reserved Instances "provide the most significant discount (up to 72% off On-Demand)", and all-upfront reservations go up to 75% off.
- **Bears on:**
  - H6 (context): small, flexible buyers pay a premium per unit. For an open fab that premium is a feature. It matches "every preference costs money" in `PRINCIPLES.md` P5.
  - H7 (context): large committed buyers still get better terms.
- **Used in:** not yet.
- **Caveats:** the brief uses this to argue that small buyers are disadvantaged. The same fact supports charging small customers more for flexibility.
