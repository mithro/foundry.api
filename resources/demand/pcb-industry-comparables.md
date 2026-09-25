# PCB industry comparables (`PCB`)

## What this file is for

[`long-tail-businesses.md`](long-tail-businesses.md) SMB-1 records one company's accounts —
JLC's — showing that in printed-circuit-board manufacturing the *long tail* is the profitable
segment and big-batch work is the low-margin commodity: 36.24% gross margin on sample and
small-batch boards against 2.76% on medium- and large-batch, and
[`../analyses/long-tail-pays-for-the-capital.md`](../analyses/long-tail-pays-for-the-capital.md)
turns that into 97.6% of PCB gross profit coming from the tail.

**One company is not a pattern.** This file tests whether the JLC result generalises across the PCB
industry or whether JLC is an outlier. It collects every other PCB manufacturer we could find that
discloses anything about margin by batch size, order size, channel or customer size.

## Why PCB manufacturing is the chosen parallel

It is the closest available analogue to what foundry.api proposes:

- **Capital-intensive process manufacturing.** Plating lines, drills, AOI, lamination presses —
  bought in advance, depreciated over years, and profitable only when kept full.
- **Sold online at published prices with automated quoting**, to enormous numbers of very small
  customers who never speak to a salesperson.
- **The same physical process is also sold conventionally**, in big batches, on negotiated terms, to
  a small number of large accounts — inside the same companies, on the same machines. That is the
  controlled comparison a fab never publishes.
- **Several of the participants are listed** in Shenzhen, Shanghai or on the STAR Market and file
  audited annual reports with segment disclosures.

## Where the analogy breaks down — honestly

1. **A PCB is not a chip.** Bare-board fabrication is orders of magnitude cheaper, faster and less
   risky than an integrated circuit. A JLC sample board ships in 24 hours; a tape-out takes months.
2. **Capital intensity is nowhere near comparable.** JLC's *entire* group fixed-asset base at
   end-2025 was CNY 3.26 billion (≈US$450M), of which PCB machinery at original cost was CNY 1.79
   billion. A single mature-node fab is tens of billions of dollars. The *direction* of the
   capital argument may transfer; the magnitude does not.
3. **There is no mask cost and no NRE cliff.** PCB tooling is a film and a drill program. The fixed
   cost per design that dominates chip economics (see SMB-7, SMB-8) has no PCB equivalent of
   comparable size, so PCB evidence cannot settle whether a *chip* long tail clears its fixed cost.
4. **No process qualification.** A PCB customer does not have to re-qualify a product because the
   fab changed a recipe. The switching costs and risk aversion that dominate H-RISK do not apply.
5. **Chinese cost base.** Most of the companies here are Chinese. Labour, land, electricity and a
   dense domestic supply chain are part of why the margins are what they are.
6. **Yield and binning.** PCB yield loss is scrap; silicon yield loss is a distribution over
   performance bins that changes what you can sell. Nothing here bears on that.

So: this file can establish whether *the pattern* — long tail high margin, big batch commodity —
is a general property of online-sold process manufacturing, or a JLC idiosyncrasy. It cannot
establish that a fab would see the same numbers.

Entries use the ID prefix `PCB`. Derived figures are labelled **DERIVED** and the arithmetic is
written out; all of it is reproduced by a script, quoted in the entries, and was run before the
figures were written down.

**A note on language.** Almost every source in this file is a Chinese-language filing. Chinese
passages are quoted in the original, exactly as the filing prints them, because the original is the
evidence; **every English rendering in this file is ours**, not the source's, and each is given
immediately after the passage it translates, after an em-dash. Chinese company names, headings,
table headers and row labels are glossed in English wherever they appear. Document reference
numbers, audit report numbers, certificate numbers and URLs are identifiers and are left as
printed.

---

### PCB-1. JLC's prospectus names its five comparable PCB companies and prints their margins — and JLC beats the peer average by a gap that widened from 3.6 to 10.0 percentage points in three years

- **Source:** 深圳嘉立创科技集团股份有限公司 (Shenzhen JLC Technology Group Co., Ltd.), 招股说明书（申报稿）
  (IPO prospectus, filed draft), Shenzhen Stock Exchange, April 2026. Same document as SMB-1:
  <http://reportdocs.static.szse.cn/UpFiles/rasinfodisc1/202604/RAS_202604_22164565DA37A2A6A74520902DB3E1B3350542.pdf>
  The tables below are on PDF pages 246–247 (document pages 1-1-245 and 1-1-246) and PDF page 147
  (document page 1-1-146).
- **Verification:** Verified 2026-09-19. The PDF was downloaded from the exchange's own document
  server (HTTP 200, 14,709,306 bytes), its text extracted with `pypdf`, and every figure below
  located and read in place. The transcription was then checked by recomputing the printed
  industry averages from the transcribed peer figures (see DERIVED) — all three years reproduce to
  the last printed digit, which is a strong check that the table has been copied correctly.
- **What it says:**
  - **SMB-1 left open which companies the prospectus treats as 同行业可比公司. This is the answer.**
    Under the heading "3、与同行业可比公司主营业务毛利率比较分析" ("3. Comparative analysis of
    core-business gross margin against comparable companies in the same industry"), the prospectus
    prints, with columns 可比公司名称 / 2025年度 / 2024 年度 / 2023年度 — "name of comparable
    company / financial year 2025 / financial year 2024 / financial year 2023" (年度 = financial
    year). Transcribed with the Chinese as printed and our English beside it:

    | 可比公司名称 (comparable company) | 2025年度 (FY2025) | 2024 年度 (FY2024) | 2023年度 (FY2023) |
    |---|---|---|---|
    | **PCB 行业** (PCB industry) | | | |
    | 兴森科技 (Fastprint) | 未披露 | 26.96% | 28.72% |
    | 金百泽 (Jinbaize) | 21.17% | 23.97% | 28.42% |
    | 迅捷兴 (Xunjiexing) | 8.52% | 14.33% | 15.14% |
    | 四会富仕 (Sihui Fushi) | 16.45% | 19.03% | 24.55% |
    | 强达电路 (Qiangda Circuit) | 26.10% | 27.58% | 28.63% |
    | **PCB 行业均值** (PCB industry mean) | **18.06%** | **22.37%** | **25.09%** |
    | **本公司 PCB 业务** (this Company's PCB business) | **28.06%** | **30.05%** | **28.73%** |

    "未披露" means *not disclosed*, and appears wherever a peer had not yet published that year's
    figure. The table's footnote reads: "注：部分可比公司同时存在其他主营业务，表中取相关数据。"
    — "Note: some comparable companies also have other core businesses; the table takes the relevant
    data." (Our translation.)
  - **The prospectus explains the 2023 outlier itself, and the explanation is the thesis.**
    Immediately under the table: "2023 年，迅捷兴受批量订单占比逐步提升，且市场竞争加剧价格竞争激烈使得批量产品降价的影响，毛利率相对较低，剔除迅捷兴后，PCB 行业毛利率均值为 27.58%，与发行人 PCB 业务毛利率水平不存在显著差异。"
    — "In 2023 Xunjiexing, affected by the gradually rising share of batch orders and by the price
    cuts on batch products caused by intensified market competition and fierce price competition,
    had a relatively low gross margin; excluding Xunjiexing, the PCB industry mean gross margin is
    27.58%, which is not significantly different from the issuer's PCB gross margin level." (Our
    translation.)
  - **The issuer attributes its own margin premium to the sales model and the customer mix, in
    terms.** For 2024: "2024 年，公司 PCB 业务毛利率同比小幅增长，高于同行业可比公司均值，主要系因公司 PCB 业务主要通过线上模式服务中小客户，客户需求和产品价格较为稳定；同时，公司产品结构和销售结构持续优化，多层板销售占比和外销收入占比持续提升，产量扩大后规模效应提升，使得毛利率进一步提升。"
    — "In 2024 the Company's PCB gross margin rose slightly year on year and was higher than the mean
    of comparable companies in the same industry, mainly because the Company's PCB business serves
    small and medium customers chiefly through the online model, so customer demand and product
    prices are relatively stable; at the same time the Company's product mix and sales mix continued
    to improve, the share of multilayer board sales and the share of export revenue kept rising, and
    scale effects improved as output expanded, which lifted the gross margin further." (Our
    translation.)
    And for 2025: "2025 年，铜、锡等主要原材料价格上涨导致生产成本提升，公司 PCB 业务毛利率与同行业可比公司毛利率有所下降，变动趋势一致。公司PCB 业务毛利率高于同行业可比公司均值主要系销售模式和客户结构差异所致。"
    — "In 2025 rising prices of copper, tin and other main raw materials pushed up production costs;
    the Company's PCB gross margin and comparable companies' gross margins both fell, moving in the
    same direction. The Company's PCB gross margin being higher than the mean of comparable
    companies in the same industry is mainly caused by differences in **sales model and customer
    structure**." (Our translation; emphasis ours.)
  - **The same five companies are also ranked by size**, on PDF p.147 under "3）行业排名情况
    ①印制电路板业务" — "3) Industry ranking. (1) Printed-circuit-board business" — with the source
    note "注：同行业可比公司数据来源于CPCA 协会内资 PCB 企业排名，上述排名依据为营业收入；嘉立创未参与CPCA 协会 2023 年和 2024 年企业榜单，上述排名系根据公司印制电路板业务营业收入测算得出"
    — "the comparable-company data come from the CPCA association's ranking of domestically-funded
    PCB enterprises, ranked on revenue; JLC did not take part in the CPCA's 2023 and 2024 enterprise
    lists, and the above ranking is estimated from the Company's PCB business revenue" (our
    translation):

    | Company | Rank among domestically-funded PCB makers, 2023 | 2024 |
    |---|---|---|
    | 嘉立创 (JLC) | 16th | 17th |
    | 兴森科技 (Fastprint) | 7th | 8th |
    | 四会富仕 (Sihui Fushi) | 25th | 23rd |
    | 强达电路 (Qiangda) | 53rd | 53rd |
    | 金百泽 (Jinbaize) | 62nd | 59th |
    | 迅捷兴 (Xunjiexing) | 78th | 83rd |

    On JLC's own row the prospectus adds: "中国电路板百强企业中目前没有主要通过产业互联网模式开展业务的企业，公司系印制电路板行业的产业互联网龙头企业"
    — "among China's top hundred circuit-board enterprises there is currently no enterprise that
    conducts its business mainly through the industrial-internet model; the Company is the leading
    industrial-internet enterprise in the printed-circuit-board industry." (Our translation.)
  - **The customer counts of the same peer set** are printed on PDF pp.144–145 in the table
    "公司及同行业公司的用户及订单数量对比情况", each with the filing it came from:

    | Company | What is disclosed (quoted) | Source cited by the prospectus |
    |---|---|---|
    | 嘉立创 (JLC) | paying users 84.39万 / 100.52万 / **135.87万**; orders 1,450.24万 / 1,780.69万 / **2,129.08万** (万 = 10,000, so 843,900 / 1,005,200 / **1,358,700** paying users and 14,502,400 / 17,806,900 / **21,290,800** orders) | — |
    | 金百泽 (Jinbaize) | "公司已为全球 20,000 多家客户的产品研发与硬件创新提供了一站式电子制造服务" | 2025 年半年度报告 (2025 half-year report) |
    | 兴森科技 (Fastprint) | "公司积累了丰厚的客户资源，先后与全球超过 4,000 家高科技研发、制造和服务企业进行合作" | 2025 年半年度报告 (2025 half-year report) |
    | 迅捷兴 (Xunjiexing) | "受益于公司在 PCB 样板、小批量板领域多年的深耕，公司累计服务了过万家企业" | 2025 年年度报告 (2025 annual report) |
    | 四会富仕 (Sihui Fushi) | "客户数量从2017 年的 143 家增长至 2022 年的 595 家" | reply to a convertible-bond review enquiry letter, data to end-March 2023 |
    | 强达电路 (Qiangda) | "2025 年，公司服务的活跃客户近3,000 家" | 2025年度报告 (2025 annual report) |

    Translations of the five quoted sentences, ours, in the same order: Jinbaize "has provided
    one-stop electronic manufacturing services for the
    product development and hardware innovation of more than 20,000 customers worldwide"; Fastprint
    "has accumulated abundant customer resources and has cooperated with more than 4,000 high-tech
    R&D, manufacturing and service enterprises worldwide"; Xunjiexing "benefiting from many years of
    deep cultivation in PCB sample boards and small-batch boards, has cumulatively served more than
    ten thousand enterprises"; Sihui Fushi's "customer count grew from 143 in 2017 to 595 in 2022";
    Qiangda "served nearly 3,000 active customers in 2025".
- **DERIVED (arithmetic written out):** every figure below was computed and checked by a
  throwaway Python script (`uv run python`) before being written down, and the arithmetic is
  reproduced here in full so a reader can redo it without the script.
  - **Transcription check.** Mean of the five transcribed peer figures, 2023:
    (28.72 + 28.42 + 15.14 + 24.55 + 28.63) ÷ 5 = 25.0920% against the printed **25.09%**.
    2024: (26.96 + 23.97 + 14.33 + 19.03 + 27.58) ÷ 5 = 22.3740% against printed **22.37%**.
    2025, over the four that disclosed: (21.17 + 8.52 + 16.45 + 26.10) ÷ 4 = 18.0600% against
    printed **18.06%**. All three reproduce exactly.
  - **The prospectus's own re-computation also reproduces.** Excluding Xunjiexing for 2023:
    (28.72 + 28.42 + 24.55 + 28.63) ÷ 4 = 27.5800% against the printed **27.58%**.
  - **The gap, and its trajectory.** JLC PCB margin minus peer mean:
    2023: 28.73 − 25.09 = **+3.64 pp**. 2024: 30.05 − 22.37 = **+7.68 pp**.
    2025: 28.06 − 18.06 = **+10.00 pp**. The gap has widened every year.
  - **Customer-count ratio.** JLC's 1,358,700 paying users in 2025 against Sihui Fushi's 595
    customers (2022) = **2,284×**; against Qiangda's ~3,000 active customers = **453×**; against
    Fastprint's 4,000 = **340×**; against Jinbaize's 20,000+ = **68×**.
- **Bears on:**
  - **H6 (supports).** This is the natural experiment the repository wanted. Same industry, same
    country, same three years, same accounting standards, audited or reviewed in every case — and
    the one company that sells online to a million-odd tiny customers earns 28.06% while the mean of
    the five conventional PCB makers it names as its own comparables earns 18.06%. The issuer,
    writing under prospectus liability, attributes the difference to "销售模式和客户结构差异" —
    differences in sales model and customer structure.
  - **H6 (supports, on the trajectory).** The gap is not static. It went +3.64 → +7.68 → +10.00 pp
    while the peer mean fell 25.09% → 18.06%. The conventional PCB business is being competed down;
    the online long-tail business is not.
  - **H6 and H5 (context, cutting against a naive reading).** Customer *count* does not predict
    margin within the peer set. Xunjiexing has served "more than ten thousand enterprises" and is a
    declared sample/small-batch specialist, and it has by far the *lowest* margin of the six
    (8.52% in 2025). Jinbaize claims 20,000+ customers and earns 21.17%. Sihui Fushi has 595
    customers and earns 16.45%. Qiangda has ~3,000 and earns 26.10%. A long customer list is
    plainly not sufficient. See PCB-3 for what Xunjiexing itself says is happening to it.
- **Used in:** not yet.
- **Caveats:**
  - **These figures are the prospectus's rendering of the peers' numbers, not the peers' own
    filings** — but they have now been checked. The footnote "部分可比公司同时存在其他主营业务，表中取相关数据"
    — "some comparable companies also have other core businesses; the table takes the relevant data"
    — means the issuer has selected a line from each peer's accounts, and for 金百泽 (Jinbaize) the
    line it selected is identifiable: 印制电路板 ("printed circuit boards", 21.17%), not the wider
    电子电路 ("electronic circuits") industry line (22.16%).
    **Thirteen of the fifteen peer figures have been re-derived from the peers' own audited annual
    reports and every one agrees exactly** — see PCB-3 (Xunjiexing, all three years), PCB-4
    (Fastprint, 2023 and 2024) and PCB-5 (Jinbaize, Sihui Fushi and Qiangda). Only 金百泽 (Jinbaize)
    2023 and 强达电路 (Qiangda) 2023 remain unchecked, and those two are **Partial**.
  - **This is a comparison of blended 主营业务毛利率 ("core-business gross margin"), not of batch
    segments.** Only JLC prints a
    margin split by batch size. The peer column is one number per company per year.
  - **The comparable set is chosen by the issuer.** It is conspicuously *not* the big listed Chinese
    PCB makers (深南电路 Shennan, 沪电股份 WUS, 景旺电子 Kinwong, 崇达技术 Chongda). It is five
    small-to-mid companies ranked 7th to 83rd among domestically-funded makers. A company choosing
    its own comparables has an interest in the comparison; that JLC's chosen peers make it look good
    is not neutral evidence, and the selection is itself a caveat on the 10.00 pp gap.
  - The document is a filed *draft* prospectus ("申报稿" — "filed draft"). The financial statements
    carry an audit report (number 容诚审字[2026]518Z0073, an identifier, left as printed) by
    容诚会计师事务所 (Rongcheng Certified Public Accountants, **verified 2026-09-19** as the China
    member firm of RSM International, trading in English as *RSM China CPA LLP* — see SMB-1 in
    [`long-tail-businesses.md`](long-tail-businesses.md) for the quote from RSM's own site); the
    business narrative does not.
  - All translations are ours; the Chinese is quoted exactly so a reader can check them.

### PCB-2. JLC owns its plant: five production bases on about a million square metres, CNY 3.26bn of fixed assets, CNY 1.4bn of capex in one year — and an audited impairment taken against the big-batch factories because they are not full

- **Source:** the same JLC prospectus as PCB-1 and SMB-1. The passages below are on PDF p.21
  (doc p.1-1-20), p.46 (1-1-45), pp.154–155 (1-1-153/154), pp.162–164 (1-1-161/163), pp.278–280
  (1-1-277/279), p.317 (1-1-316), and the cash-flow statement.
- **Verification:** Verified 2026-09-19 from the extracted PDF text, as for PCB-1. **This entry
  settles the open item recorded against SMB-1: we had no quote establishing that JLC owns its
  plant. It does, and the filing says so in several independent places.**
- **What it says:**
  - **Own ordering site, own production and warehousing bases** (PDF p.21, under 概览, "Overview"): "凭借强大的自主研发能力，通过自建的下单网站和自有的生产仓储基地，公司提供覆盖 EDA/CAM 工业软件、印制电路板制造、电子元器件购销、电子装联等全产业链一体化服务，年交付订单量超千万笔。"
    — "Relying on strong in-house R&D capability, and **through its self-built ordering website and
    its own production and warehousing bases**, the Company provides integrated whole-industry-chain
    services covering EDA/CAM industrial software, printed-circuit-board manufacturing, electronic
    component purchase and sale, and electronic assembly, delivering more than ten million orders a
    year." (Our translation; emphasis ours. 自建 = self-built; 自有 = owned by itself.)
  - **Five production bases, about one million square metres** (same page): "经过十余年的沉淀与发展，公司陆续在广东省内的珠海、惠州、韶关及江西吉安、江苏淮安等地建立了占地约百万平方米的五大现代化数字生产基地和两大智能电子元器件仓储基地，实现了业务条线的垂直化整合和产业链的纵向延伸。"
    — "Over more than ten years of accumulation and development, the Company has successively
    established, in Zhuhai, Huizhou and Shaoguan in Guangdong province and in Ji'an in Jiangxi and
    Huai'an in Jiangsu, **five modern digital production bases occupying about one million square
    metres** and two intelligent electronic-component warehousing bases, achieving vertical
    integration of its business lines and vertical extension of its industrial chain." (Our
    translation.)
  - **"Self-operated" manufacturing, stated as such** (PDF p.317): "2021 年，公司三大运营板块完成整合，打造了广东惠州、珠海、韶关，江苏淮安，江西吉安五大数字化自营生产基地，实现了产品自营制造，保证了交期和产品质量。在广东珠海和江苏淮安，公司建有两大智能仓储中心。"
    — "In 2021 the Company completed the integration of its three operating blocks and built five
    digital **self-operated** production bases in Huizhou, Zhuhai and Shaoguan in Guangdong, Huai'an
    in Jiangsu and Ji'an in Jiangxi, achieving **self-operated manufacturing of its products**,
    which guarantees delivery times and product quality. In Zhuhai, Guangdong and Huai'an, Jiangsu
    the Company has built two intelligent warehousing centres." (Our translation; emphasis ours.)
  - **The balance sheet agrees.** Fixed assets (固定资产, "fixed assets") at 31 December 2025 /
    2024 / 2023, PDF p.278, printed 单位：万元 ("unit: 10,000 yuan"). Chinese row labels are the
    filing's; the English beside them is ours:

    | | 2025-12-31 | 2024-12-31 | 2023-12-31 |
    |---|---|---|---|
    | 账面原值 (gross cost) | 486,761.56 | 378,642.68 | 297,843.17 |
    | 　房屋及建筑物 (buildings) | 120,964.14 | 96,278.41 | 64,530.00 |
    | 　机器设备 (machinery) | 303,094.93 | 235,262.10 | 196,828.30 |
    | 累计折旧 (accumulated depreciation) | 147,878.59 | 112,904.54 | 84,713.12 |
    | 减值准备 (impairment provision) | 13,136.51 | 13,586.93 | 11,483.33 |
    | **账面价值 (net book value)** | **325,746.46** | **252,151.21** | **201,646.72** |
    | 　房屋及建筑物 (buildings) | 95,298.19 | 76,489.33 | 47,839.07 |
    | 　机器设备 (machinery) | 200,505.76 | 152,004.88 | 133,393.42 |

    i.e. net fixed assets of **CNY 3,257,464,600** at end-2025, of which **CNY 952,981,900 is
    buildings the company carries as its own**. The prospectus adds: "报告期内，公司固定资产规模快速增加，主要系为满足公司经营规模扩大的需要，不断改造升级和新建产线，使得公司固定资产相应增加。"
    — "During the reporting period the Company's fixed assets grew rapidly, mainly because, to meet
    the needs of its expanding operating scale, it continually rebuilt, upgraded and newly built
    production lines." (Our translation.)
  - **Title deeds and land.** PDF p.162 has the heading "2、房屋及建筑物 （1）已取得所有权证的房屋及建筑物"
    — "2. Buildings and structures. (1) Buildings and structures **for which ownership certificates
    have been obtained**" — with the
    schedule cross-referenced to the appendix. Some Huai'an buildings are on a "先租后售"
    (lease-first, purchase-later) arrangement with the Lianshui development-zone authority and
    and "权属尚未转让给江苏中信华、江苏嘉立创" ("title has not yet been transferred to 江苏中信华 /
    Jiangsu Zhongxinhua and 江苏嘉立创 / Jiangsu JLC"). Land is held on land-use rights: at PDF p.276
    the intangibles note gives 土地使用权 ("land-use rights") net book value 46,935.16 万元 at
    end-2025 (**CNY 469,351,600**), and the text at p.164 records that in December 2025 subsidiary
    先进电子 (Xianjin Dianzi, "Advanced Electronics" — the filing gives no English name) bought at
    auction a 43,753.89 m² plot in Fushan Industrial Park, Doumen District, Zhuhai, certificate
    number "粤（2026）珠海市不动产权第 0010066 号" (a Guangdong real-property certificate number, left
    as printed because it is an identifier).
  - **Capacity, output and utilisation** (PDF p.154, under "1、主要产品的产能、产量和销量" —
    "1. Capacity, output and sales volume of the main products"). 万平方米 = 10,000 m²:

    | PCB | 2025 | 2024 | 2023 |
    |---|---|---|---|
    | 产能 capacity (万平方米 / 10,000 m²) | 1,153.46 | 1,049.53 | 936.90 |
    | 产量 output (万平方米 / 10,000 m²) | 885.61 | 801.16 | 717.38 |
    | 销量 sold (万平方米 / 10,000 m²) | 879.71 | 799.05 | 717.12 |
    | 产能利用率 capacity utilisation (%) | 76.78 | 76.34 | 76.57 |
    | 产销率 sold/output ratio (%) | 99.33 | 99.74 | 99.96 |

    Footnote: "注：产能利用率=产量/产能、产销率=销量/产量。" — "Note: capacity utilisation = output ÷
    capacity; sold/output ratio = sales volume ÷ output."
  - **Machinery matched to capacity** (PDF p.279): PCB machine-equipment gross cost
    (PCB 机器设备原值 — "gross original cost of PCB machinery and equipment") **178,801.33 万元** in
    2025, 156,146.48 in 2024, 140,809.62 in 2023, printed alongside the capacity line above; PCBA
    machine equipment 51,184.11 / 37,532.05 / 28,968.77 万元 (i.e. CNY 511,841,100 / 375,320,500 /
    289,687,700). The text concludes "报告期内，公司 PCB、PCBA 产能及产量均随着相应机器设备原值增加而增长，仍处在高速成长期。"
    — "during the reporting period the Company's PCB and PCBA capacity and output both grew as the
    gross cost of the corresponding machinery grew; it is still in a high-growth phase." (Our
    translation.)
  - **Capex.** Cash-flow statement, 购建固定资产、无形资产和其他长期资产支付的现金 (cash paid to
    acquire and construct fixed assets, intangibles and other long-term assets): **1,395,139,797.89**
    (2025), 1,047,946,931.78 (2024), 832,890,078.98 (2023).
  - **The impairment — and what the auditors say caused it.** PDF p.279–280, under
    "（4）固定资产减值准备计提情况" — "(4) Recognition of provisions for impairment of fixed assets":
    "公司于报告期每期末对固定资产是否存在减值迹象进行判断并进行减值测试，因 PCB 中大批量订单相对不饱和等原因导致公司部分机器设备出现闲置的情形，固定资产存在减值迹象，公司对出现减值迹象的固定资产进行了减值测试，并根据可回收金额计提了固定资产减值准备。"
    — "The Company assesses at each period end whether there are indications of impairment of fixed
    assets and performs impairment tests. **Because medium- and large-batch PCB orders are
    relatively under-full, among other reasons, some of the Company's machinery has become idle**,
    there are indications of impairment of fixed assets, and the Company performed impairment tests
    on the fixed assets showing such indications and recognised impairment provisions according to
    their recoverable amounts." (Our translation; emphasis ours.) And: "报告期各期末，公司固定资产减值准备金额分别为 11,483.33 万元、13,586.93 万元和 13,136.51 万元，主要为对江西中信华、江苏中信华固定资产所计提减值准备。"
    — "the fixed-asset impairment provisions at each period end were CNY 114,833,300, 135,869,300
    and 131,365,100, **mainly provisions against the fixed assets of Jiangxi Zhongxinhua and Jiangsu
    Zhongxinhua**." (Our translation.)
  - **Zhongxinhua is the big-batch block, in the issuer's own words.** The subsidiary schedule at
    PDF p.46 describes 江苏中信华电子科技有限公司 (Jiangsu Zhongxinhua Electronic Technology Co.,
    Ltd.) under "主营业务情况及在发行人业务板块中定位"
    (core business and position within the issuer's business blocks) as: "主要从事PCB生产、销售，系发行人中大批量PCB生产基地"
    — "mainly engaged in PCB production and sale; **it is the issuer's medium- and large-batch PCB
    production base**." (Our translation.) It is 100% owned by 嘉立创 (JLC).
  - **How it sells** (PDF pp.112–113, under "（2）销售模式" — "(2) Sales model"): "公司印制电路板业务采用"线上为主、线下为辅"的销售模式。线上渠道主要为样板、小批量板订单；线下渠道主要为中大批量板订单。线上模式下，公司主要采用"先款后货"的结算模式；线下模式下，公司通常会根据客户的经营情况、合作历史、信用状况等给予客户一定的信用期限。"
    and "线上模式下，客户可通过公司官网、下单助手客户端等渠道自助下单。销售流程方面，客户登录公司线上自助下单网站注册账号，根据自身需求提交 PCB 设计文件，并对 PCB 的材质、工艺、交期等信息进行个性化选择，系统自动生成参考报价，市场部对订单审核后向客户发送最终报价，客户完成付款后公司即可组织后续生产、包装及发货等环节。"
    — "The Company's PCB business uses a sales model of 'online primary, offline supplementary'. The
    online channel is mainly sample-board and small-batch-board orders; the offline channel is
    mainly medium- and large-batch-board orders. Under the online model the Company mainly uses
    payment-before-goods settlement; under the offline model it usually grants customers a credit
    period based on their operating condition, history of cooperation and credit standing." And:
    "Under the online model, customers can place orders themselves through the Company's official
    website, the ordering-assistant client and other channels. In the sales process, the customer
    logs in to the Company's online self-service ordering website and registers an account, submits
    a PCB design file according to their own needs, and makes personalised selections of the PCB's
    material, process, delivery time and so on; **the system automatically generates a reference
    quotation, the marketing department reviews the order and sends the customer a final quotation**,
    and once the customer has completed payment the Company can organise the subsequent production,
    packaging and shipping." (Our translation; emphasis ours.)
    By contrast, the offline model: "业务员先与客户就产品的价格、数量、工艺等关键的合同要素初步沟通达成一致" — "the salesperson first
    communicates with the customer and reaches agreement on key contract terms such as price,
    quantity and process."
- **DERIVED (arithmetic written out):** computed and checked by script before being written
  down; the arithmetic is reproduced in full below.
  - **Utilisation reproduces.** 717.38 ÷ 936.90 = 76.57%; 801.16 ÷ 1,049.53 = 76.34%;
    885.61 ÷ 1,153.46 = 76.78%. Exactly the printed figures.
  - **Average PCB price reproduces.** 292,745.25万元 ÷ 717.12万 m² (i.e. CNY 2,927,452,500 ÷
    7,171,200 m²) = CNY 408.22/m²;
    336,096.74 ÷ 799.05 = CNY 420.62/m²; 388,369.64 ÷ 879.71 = CNY 441.47/m² against printed
    441.48 (rounding). The prospectus's own price table prints 408.22 / 420.62 / 441.48, so the
    revenue, volume and price lines are mutually consistent.
  - **Capital intensity of the PCB business.** PCB machinery at gross cost ÷ annual capacity:
    2025: CNY 1,788,013,300 ÷ 11,534,600 m² = **CNY 155.01 per m² of annual capacity**
    (2024: CNY 148.78/m²; 2023: CNY 150.29/m²).
    PCB revenue per CNY 1 of PCB machinery at gross cost: 2025: 388,369.64 ÷ 178,801.33 = **2.17**
    (2024: 2.15; 2023: 2.08).
  - **Group capital intensity.** Capex ÷ revenue, 2025: 1,395,139,797.89 ÷ 10,287,064,200 =
    **13.56%**. Revenue ÷ net fixed assets: 10,287,064,200 ÷ 3,257,464,641.06 = **3.16×**.
- **Bears on:**
  - **H6 (supports).** SMB-1's open question is closed: **JLC owns the machines.** It is not a
    broker, not a marketplace, not an asset-light aggregator. Five owned production bases, CNY 3.26
    billion of fixed assets, CNY 1.4 billion of capex in a single year, buildings on its own balance
    sheet with ownership certificates, land held on land-use rights it bought at auction. The
    long-tail margin in SMB-1 is being earned by a company carrying the capital, which is what the
    read-across to a fab requires. The objection recorded in
    [`../analyses/long-tail-pays-for-the-capital.md`](../analyses/long-tail-pays-for-the-capital.md)
    — "a business serving many tiny customers can only work if it does not own the machines" — is
    directly contradicted by this filing.
  - **H6 (supports, sharply).** The impairment is the single most pointed fact in this file. In an
    audited set of accounts, the company wrote down machinery **because the big-batch orders were
    not there to fill it** — "PCB 中大批量订单相对不饱和…部分机器设备出现闲置", "medium- and
    large-batch PCB orders are relatively under-full … some machinery has become idle" — and the
    write-down
    fell on the two Zhongxinhua entities, which the same filing identifies as the medium- and
    large-batch production base. The segment that in SMB-1 earns 2.76% is also the segment whose
    plant is idle enough to impair. Meanwhile the long-tail segment is running at 76.78%
    utilisation and 99.33% sell-through.
  - **H6 (challenges, mildly).** Group utilisation is only about 76%, and flat across three years.
    A fab's payback arithmetic is far more sensitive to utilisation than a PCB shop's, so this is
    not a model of a full factory.
  - **H8 (mixed, and this must not be overstated).** The online flow is *not* fully unattended. The
    prospectus says the system generates a *reference* quote and "市场部对订单审核后向客户发送最终报价"
    — "the marketing department reviews the order and then sends the customer the final quotation". Whether that review is a
    rubber stamp on 21 million orders a year, an automated rules engine described in
    organisational language, or a real human touch on some fraction of orders, the filing does not
    say. Any claim in our documents that a JLC order completes with zero human involvement is not
    supported by this text.
- **Used in:** not yet.
- **Caveats:**
  - "占地约百万平方米" — "occupying about one million square metres" — is *site area across five
    bases*, not
    cleanroom or plant floor area, and not PCB capacity. PCB capacity is separately given as
    11.53 million m² of board per year.
  - The fixed-asset, capex and utilisation figures are **group-wide** and include PCBA, electronic
    components, 3D printing and CNC. Only the PCB machinery line (178,801.33 万元, CNY 1,788,013,300)
    and the PCB
    capacity line are PCB-specific, and even those span both the long-tail and the big-batch
    factories, which cannot be separated from this disclosure.
  - Parts of the Huai'an premises are used under a lease-first/purchase-later arrangement with a
    local-government company and title has not yet passed. JLC's ownership of its plant is
    substantial but not uniformly complete.
  - **Depreciation is not separately disclosed in a form we could isolate for PCB.** Accumulated
    depreciation grew from 84,713.12 to 147,878.59 万元 (CNY 847,131,200 to CNY 1,478,785,900) over
    three years, but annual depreciation by
    segment is not printed.

### PCB-3. Xunjiexing, a declared sample-board specialist, says in its own audited report that its margin fell because its mix shifted to batch work — and that top-five customers are 40% of its revenue

- **Sources:** 深圳市迅捷兴科技股份有限公司 (Shenzhen Xunjiexing Technology Co., Ltd.), Shanghai
  Stock Exchange STAR Market code **688655**, annual reports (年度报告, "annual report"), all
  fetched from cninfo's
  own document server `static.cninfo.com.cn`:
  - FY2025, published 2026-03-28: <http://static.cninfo.com.cn/finalpage/2026-03-28/1225048380.PDF>
  - FY2024, published 2025-03-18: <http://static.cninfo.com.cn/finalpage/2025-03-18/1222822088.PDF>
  - FY2023, published 2024-04-27: <http://static.cninfo.com.cn/finalpage/2024-04-27/1219887245.PDF>
- **Verification:** Verified 2026-09-19. All three PDFs downloaded (HTTP 200; 3,299,798 /
  5,068,593 / 4,723,408 bytes), text extracted with `pypdf`, every figure located and read in
  place, and the gross margins recomputed from the printed revenue and cost figures.
- **How it was counted:** `static.cninfo.com.cn` returns **HTTP 403** to a plain `curl`. It serves
  the PDF with a browser User-Agent plus `-H "Referer: http://www.cninfo.com.cn/"`. The filing list
  comes from cninfo's own search endpoint, `POST http://www.cninfo.com.cn/new/hisAnnouncement/query`
  with `column=szse&tabName=fulltext&searchkey=<name>&category=category_ndbg_szsh`, which returns
  JSON containing each document's `adjunctUrl`.
- **What it says:**
  - **The company defines itself as a sample and small-batch business.** FY2025 report §(二)
    公司发展战略 ("(2) The Company's development strategy"), p.60: "公司发展战略始终聚焦于样板、小批量，致力于为客户提供从样品研发到中试再到量产的一站式服务。"
    — "The Company's development strategy has always focused on sample boards and small batches,
    committed to providing customers with one-stop service from sample R&D through pilot production
    to mass production." (Our translation.) And p.21: "公司起步于样板…目前，国内 PCB 企业多以大批量业务为主，专注于样板业务的企业较少。"
    — "The Company started from sample boards … At present most domestic PCB enterprises are
    mainly in large-batch business, and few enterprises specialise in sample-board business." (Our
    translation.) It notes it is "被 CPCA 评为内资 PCB 企业'快板/样板'特色产品主要企业" — rated by
    the CPCA as a principal enterprise for 'quick-turn / sample board' speciality products among
    domestically-funded PCB enterprises.
  - **It prints, as an industry characteristic, exactly the pattern JLC's segment table shows.**
    FY2025 report pp.20–21, under "（4）PCB 样板、批量行业特点" ("(4) Characteristics of the PCB
    sample-board and batch-board industry"), a table with columns 样板 / 小批量板 / 大批量板 (sample
    board / small-batch board / large-batch board). Selected rows, transcribed, with the Chinese as
    printed and our English beside it:

    | 项目 (item) | 样板 (sample board) | 小批量板 (small-batch board) | 大批量板 (large-batch board) |
    |---|---|---|---|
    | 平均订单面积 (average order area) | 5 平方米以下 (under 5 m²) | 5～50 平方米 (5–50 m²) | 50 平方米以上 (over 50 m²) |
    | 订单量 (order volume) | 订单数量多、产品种类多 (many orders, many product types) | 订单数量较多、产品种类较多 (relatively many orders, relatively many product types) | 订单数量少、产品种类少 (few orders, few product types) |
    | 交货期 (lead time) | 一般 10 天以内 (generally within 10 days) | 一般 10～20 天 (generally 10–20 days) | 一般 20 天以上 (generally over 20 days) |
    | 客户维护 (customer servicing) | 客户多、售后服务要求最高 (many customers; the highest after-sales service requirement) | 客户较少 (relatively few customers) | 客户较少 (relatively few customers) |
    | **毛利率 (gross margin)** | **高 (high)** | **较高 (relatively high)** | **一般低于样板、小批量板 (generally lower than sample and small-batch boards)** |

    And beneath it: "而中大批量板订单可以通过提高自动化水平进行规模化生产，更关注自身的产能、良率和成本管控等因素。"
    — "Medium- and large-batch board orders, by contrast, can be produced at scale by raising the
    level of automation, and are more concerned with capacity, yield and cost control." (Our
    translation.)
  - **The FY2023 report says the margin fell because the mix shifted to batch.** FY2023 report
    p.42, under "主营业务分行业、分产品、分地区、分销售模式情况的说明" — "Explanation of core business
    by industry, by product, by region and by sales model": "2023年公司主营业务收入较上年同期增加3.65%，其中主营产品PCB销量较去年同比增长了30.02%，为此公司毛利率减少5.62个百分点，主要原因是单价下降因素导致，一方面是市场竞争加剧价格竞争激烈使得批量产品降价，另一方面是公司批量占比逐步增加。"
    — "In 2023 the Company's core-business revenue rose 3.65% year on year, and the sales volume of
    its main product, PCB, grew 30.02% year on year; the Company's gross margin nevertheless fell by
    5.62 percentage points, mainly caused by a fall in unit price — on the one hand because
    intensified market competition and fierce price competition drove down the prices of **batch
    products**, and on the other because **the Company's batch share gradually increased**." (Our
    translation; emphasis ours.)
    The same page: "报告期，公司仍以内销为主，内销毛利率减少7.39个百分点，主要是批量订单价格下降叠加大批量占比上升影响。"
    — "In the reporting period the Company remained mainly domestic; the domestic gross margin fell
    7.39 percentage points, mainly the effect of falling batch-order prices compounded by a rising
    share of large batch." (Our translation.)
  - **Segment table, three years.** From "主营业务分行业情况" ("core business by industry") in each
    report, all in CNY:

    | | 营业收入 (revenue) | 营业成本 (cost of sales) | 毛利率 (gross margin) |
    |---|---|---|---|
    | 2023 | 445,662,776.81 | 378,200,246.35 | **15.14%** |
    | 2024 | 452,462,851.68 | 387,604,201.66 | **14.33%** |
    | 2025 | 644,608,709.53 | 589,717,354.22 | **8.52%** |

    All three are single-product (印制电路板, "printed circuit boards") — Xunjiexing publishes no
    split by batch size in its
    own accounts, only the industry-characteristics table quoted above.
  - **The FY2025 explanation is different, and is not about mix.** FY2025 report p.50: "毛利率下降的主要原因是 2025 年上半年子公司珠海迅捷兴一期智慧样板厂投产，报告期新工厂尚处于产能磨合阶段，大幅增加的人工、折旧等固定成本未被摊薄，叠加 PCB 行业上游原材料价格上涨等因素所致。"
    — "The main reason for the fall in gross margin is that in the first half of 2025 the subsidiary
    Zhuhai Xunjiexing's phase-one intelligent sample-board plant came into production; during the
    reporting period the new plant was still in its capacity run-in stage, the sharply increased
    fixed costs such as labour and depreciation were not spread, and this was compounded by rising
    upstream raw-material prices in the PCB industry." (Our translation.)
  - **It is loss-making.** FY2025 report §四、风险因素(二) ("4. Risk factors, (2)"): "2025 年公司实现归属于上市公司股东的净利润-2,237.90 万元，实现归属于上市公司股东的扣除非经常性损益的净利润-2,637.74 万元"
    — net loss attributable to shareholders of the listed company of **CNY 22,379,000**, and
    **CNY 26,377,400** excluding non-recurring items. (Our translation.)
  - **Customer concentration: the opposite of JLC's.** FY2025 report pp.52–53, under
    "A.公司主要销售客户情况" — "A. The Company's main sales customers":
    "前五名客户销售额25,833.50万元，占年度销售总额40.07%；其中前五名客户销售额中关联方销售额0万元，占年度销售总额0%。"
    — "Sales to the top five customers were CNY 258,335,000, **40.07% of total annual sales**; of
    which sales to related parties were nil." The table:

    | 序号 (no.) | 客户名称 (customer name) | 销售额 (sales, 万元 / CNY 10,000) | 占年度销售总额比例 (share of total annual sales) |
    |---|---|---|---|
    | 1 | 海康威视 (Hikvision) | 8,111.57 | **12.58%** |
    | 2 | 大华股份 (Dahua) | 6,799.46 | 10.55% |
    | 3 | NCABGROUP | 4,993.30 | 7.75% |
    | 4 | 视源股份 (CVTE) | 3,283.55 | 5.09% |
    | 5 | 北斗星通 (BDStar) | 2,645.62 | 4.10% |
    | 合计 (total) | | 25,833.50 | 40.07% |

    Prior years, same disclosure: FY2024 "前五名客户销售额17,371.51 万元，占年度销售总额38.40%" —
    "sales to the top five customers were 17,371.51 万元 [CNY 173,715,100], 38.40% of total annual
    sales"; FY2023 "前五名客户销售额 17,913.20 万元，占年度销售总额40.19%" — "sales to the top five
    customers were 17,913.20 万元 [CNY 179,132,000], 40.19% of total annual sales".
  - **And it is moving toward large customers, deliberately.** FY2025 report p.50: "未来，公司将持续加快市场开发，进一步提高大客户订单份额比等，加速实现公司规模效应，以提升盈利能力水平。"
    — "In future the Company will continue to accelerate market development and **further raise the
    share of large-customer orders**, so as to bring forward its scale effects and raise its
    profitability." (Our translation; emphasis ours.) And in the operating plan, p.61, for the
    Xinfeng base: "2026 年，信丰工厂首要任务是以服务大客户为主，通过导入批量订单把产能填满，发挥规模效应。"
    — "In 2026 the Xinfeng plant's primary task is to serve large customers, **filling capacity by
    bringing in batch orders** and realising scale effects." (Our translation.)
  - **It has also just copied JLC's channel.** FY2025 report p.25: "为了发挥珠海智慧样板厂样板批量化生产模式优势，公司 PCB 网上商城已于 2026 年 1 月 4 日正式上线，开启 PCB 线上接单新篇章。"
    — "To exploit the advantages of the Zhuhai intelligent sample-board plant's batched-sample
    production model, the Company's **PCB online mall went live on 4 January 2026**, opening a new
    chapter of taking PCB orders online." (Our translation.) The Zhuhai plant is described at p.61
    as pursuing "通过多个订单合拼生产的样板批量化生产新模式" — "a new model of batched sample-board
    production, combining multiple orders into one production run" — which is panelisation, the
    same mechanism OSH Park and Dirty PCBs used.
- **DERIVED (arithmetic written out):** computed and checked by script before being written
  down; the arithmetic is reproduced in full below.
  - **Margins reproduce from the printed revenue and cost, and match JLC's prospectus exactly.**
    (445,662,776.81 − 378,200,246.35) ÷ 445,662,776.81 = **15.14%**;
    (452,462,851.68 − 387,604,201.66) ÷ 452,462,851.68 = **14.33%**;
    (644,608,709.53 − 589,717,354.22) ÷ 644,608,709.53 = **8.52%**.
    The JLC prospectus attributes 15.14% / 14.33% / 8.52% to 迅捷兴 (Xunjiexing) for 2023 / 2024 /
    2025. **The
    two sources agree to the printed digit in all three years.** That is one of the five peer
    columns in PCB-1 independently verified against the peer's own audited annual report.
  - **Average price per m².** PCB sold (from each year's 产销量情况分析表, "analysis table of
    production and sales volumes"): 461,321.66 m² (2023),
    487,547.25 m² (2024), 743,951.49 m² (2025). Revenue ÷ area = **CNY 966.06 / 928.04 / 866.47
    per m²**. Falling 10.3% over two years while volume rose 61%.
  - **Against JLC.** JLC's 2025 blended PCB price is CNY 441.48/m², Xunjiexing's CNY 866.47/m² —
    Xunjiexing sells at **1.96×** JLC's average price per unit area and still earns 8.52% against
    JLC's 28.06%.
  - **Top-five shares recomputed** against main-business revenue (64,460.87 万元, CNY 644,608,700):
    12.58%, 10.55%, 7.75%, 5.09%, 4.10%, summing to **40.08%** against the printed 40.07% of
    年度销售总额 ("total annual sales", a marginally larger denominator).
  - **Effective number of customers (reciprocal Herfindahl), with the arithmetic and its limits.**
    H = Σsᵢ². Only the top five shares are disclosed, so the true H cannot be computed; what can be
    computed is a range. Taking the known shares alone (equivalent to assuming the remaining
    revenue is atomised among infinitely many infinitesimal customers) gives the **maximum**
    effective number; treating the entire remainder as one single customer gives the **minimum**.
    - Xunjiexing 2025: H from the top five = 0.1258² + 0.1055² + 0.0775² + 0.0509² + 0.0410² =
      0.03724108, so 1/H ≤ **26.9**. With the 59.92% remainder as a single block, H = 0.39632665 and
      1/H ≥ **2.5**. **The effective number of customers is at most about 27.**
    - JLC 2025, for contrast, from the top five in SMB-1 (0.28%, 0.25%, 0.23%, 0.22%, 0.18%):
      H from the known shares = 0.00002746, so 1/H ≤ **36,417**; with the 98.84% remainder as one
      block, 1/H ≥ 1.0. The upper bound is what is informative here: JLC's disclosed concentration
      is consistent with tens of thousands of effective customers; Xunjiexing's is not consistent
      with more than about twenty-seven.
    - **This bound is weak in one direction and must not be quoted as a point estimate.** Neither
      company discloses the shape of its tail. The honest statement is: the upper bound on JLC's
      effective customer count is three orders of magnitude above Xunjiexing's.
- **Bears on:**
  - **H6 (supports).** A second company, independently, states the same relationship JLC's segment
    table shows — and states it as a characteristic of the *industry*, not of itself: sample boards
    high margin, small batch relatively high, large batch generally lower. And its FY2023 report
    gives the mechanism in its own words: revenue up 3.65%, volume up 30.02%, margin down 5.62 pp,
    because the batch share rose and batch prices fell. That is the JLC pattern observed from
    inside a different company.
  - **H7 (challenges, hard).** This is the most damaging finding in this file. Xunjiexing has
    "cumulatively served more than ten thousand enterprises", specialises in sample boards, and
    nevertheless takes **40.07% of its revenue from five customers**, with Hikvision alone at
    12.58%. A long customer *list* does not produce a long-tailed *revenue* distribution. This is
    the Shapeways lesson (SMB-4) reproduced in the industry we are using as the parallel, and in a
    company that looks, from its self-description, exactly like the kind of business H7 assumes is
    safe.
  - **H5 and H7 (challenges).** The declared direction of travel is away from the tail:
    "further raise the share of large-customer orders", and "filling capacity by bringing in batch
    orders". That is the third company in this repository — after Protolabs (SMB-2) and Xometry
    (SMB-3) — whose stated strategy is to move up-market. The pattern of *firms choosing to leave
    the tail* is now more consistent than the pattern of tail margins.
  - **H6 (challenges).** Xunjiexing is a sample-board specialist losing money (CNY −22.4M in 2025)
    at an 8.52% gross margin, while selling at nearly twice JLC's price per square metre. Being in
    the long tail is evidently not sufficient for the long-tail margin. Whatever JLC has, it is not
    simply "serves small customers".
- **Used in:** not yet.
- **Caveats:**
  - **The 2025 margin collapse has a stated cause that is not mix**: a new plant in run-in with
    undiluted fixed costs, plus raw-material prices. Attributing 8.52% to the long tail would be
    wrong. The mix explanation is the company's own for **2023**, not 2025.
  - The "毛利率 高 / 较高 / 一般低于样板、小批量板" row — gross margin "high / relatively high /
    generally lower than sample and small-batch boards" — is a **qualitative industry description in the
    business section of an annual report**, not an audited segment number. It is corroboration of
    the direction, not a measurement.
  - The band definitions differ from JLC's and the two are **not** interchangeable. Xunjiexing:
    sample < 5 m², small batch 5–50 m², large batch > 50 m² per average order. JLC (SMB-1 glossary,
    PDF p.13): sample < 1 m², small batch 1–20 m², medium/large batch > 20 m². Any cross-company
    comparison of "small batch" is comparing differently drawn lines.
  - "累计服务了过万家企业" — "has cumulatively served more than ten thousand enterprises" — is
    **cumulative since inception**, like Shapeways' "over one million
    customers", and is not an annual active count. The annual active count is not disclosed.
  - The "top five customers" disclosure is of *total annual sales*; the segment table is of
    *main-business revenue*. The two denominators differ slightly (40.07% vs our 40.08%).

### PCB-4. Fastprint, the seventh-largest domestic PCB maker and a declared sample/small-batch leader, publishes no batch split — and its 28.72% PCB margin is falling while its customer concentration nearly doubled in two years

- **Sources:** 深圳市兴森快捷电路科技股份有限公司 (Shenzhen Fastprint Circuit Tech Co., Ltd.),
  Shenzhen Stock Exchange code **002436**, annual reports (年度报告, "annual report"), from cninfo's
  own document
  server:
  - FY2025, published 2026-04-25: <http://static.cninfo.com.cn/finalpage/2026-04-25/1225184929.PDF>
  - FY2024, published 2025-04-25: <http://static.cninfo.com.cn/finalpage/2025-04-25/1223267526.PDF>
  - FY2023, published 2024-04-25: <http://static.cninfo.com.cn/finalpage/2024-04-25/1219790493.PDF>
- **Verification:** Verified 2026-09-19. All three PDFs downloaded (HTTP 200; 1,495,341 /
  7,024,938 / 6,889,110 bytes; 234 / 251 / 241 pages), text extracted with `pypdf`, figures located
  and read in place and the margins recomputed from the printed revenue and cost.
- **What it says:**
  - **It is the closest thing in the peer set to a company that ought to publish the split, and it
    does not.** FY2025 report §一、报告期内公司从事的主要业务 ("1. The main businesses the Company
    engaged in during the reporting period"), p.14: "传统 PCB 业务聚焦于样板快件及批量板的研发、设计、生产、销售和表面贴装"
    — "The traditional PCB business focuses on the R&D, design, production, sale and surface mount
    of **quick-turn sample boards and batch boards**." (Our translation.) And in the risk section,
    p.29: "虽然公司在 PCB样板、小批量板和 IC封装基板、半导体测试板等细分行业具有相对领先优势，但仍面临较为严峻的竞争形势。"
    — "although the Company has a relatively leading advantage in the PCB sample-board, small-batch
    board, IC packaging substrate and semiconductor test board sub-sectors, it still faces a fairly
    severe competitive situation." (Our translation.)
    **But its segment tables split revenue and margin by 行业 ("industry": PCB / semiconductor /
    other), by 产品 ("product"), by 地区 ("region") and by 销售模式 ("sales model": direct sales /
    through traders) — never by batch size.** Searching all three annual reports for 样板毛利率
    ("sample-board gross margin"), 小批量 ("small batch") together with 毛利率 ("gross margin"), or
    any batch-size margin split returns nothing.
  - **The PCB margin, three years.** FY2023 report, table "占公司营业收入或营业利润 10%以上的行业…的情况"
    — "industries … accounting for more than 10% of the Company's revenue or operating profit":
    PCB revenue 4,090,502,302.37, cost 2,915,691,055.62, **毛利率 (gross margin) 28.72%**,
    "同比下降 1.57 个百分点" ("down 1.57 percentage points year on year").
    FY2025 report, same table: PCB revenue 4,897,079,816.57, cost 3,660,050,280.12, **毛利率
    25.26%**, "毛利率比上年同期增减 −1.70%" ("change in gross margin against the same period last
    year: −1.70 [percentage points]"). The FY2025 narrative, p.14: "报告期内，公司 PCB业务实现收入 489,707.98万元、同比增长 13.89%，毛利率25.26%、同比下降 1.70个百分点。"
    — "in the reporting period the Company's PCB business achieved revenue of CNY 4,897,079,800, up
    13.89% year on year, with a gross margin of 25.26%, down 1.70 percentage points year on year."
    (Our translation.)
  - **Its semiconductor arm is loss-making at the gross line, and the stated reason is that it is
    not yet in volume.** FY2025, p.14: "公司半导体业务（包括 IC封装基板和半导体测试板业务）实现收入 190,960.55万元、同比增长 48.62%，毛利率-9.28%…毛利率为负主要系 FCBGA封装基板项目尚未实现大批量生产，人工、折旧、能源和材料等费用投入较大。"
    — "the semiconductor business … achieved revenue of CNY 1,909,605,500, up 48.62%, with a gross
    margin of **−9.28%** … the negative gross margin is mainly because the FCBGA packaging substrate
    project **has not yet achieved large-batch production**, and the inputs of labour, depreciation,
    energy and materials are large." (Our translation.) The printed segment table gives IC封装基板
    ("IC packaging substrates") at **−16.06%** and 半导体测试板 ("semiconductor test boards") at
    **+38.03%** for 2025.
  - **Customer concentration, rising fast.** FY2025 report, 公司主要客户情况 ("the Company's main
    customers"): "前五名客户合计销售金额（元）1,963,516,796.09 / 前五名客户合计销售金额占年度销售总额比例 27.29%"
    — "total sales to the top five customers (yuan) 1,963,516,796.09 / share of total annual sales
    taken by the top five customers 27.29%" — with 客户一 (Customer One) 939,456,588.09 = **13.06%**,
    客户二 (Customer Two) 552,598,629.41 = 7.68%, 客户三 (Customer Three) 210,422,079.94 = 2.92%,
    客户四 (Customer Four) 145,696,735.54 = 2.03%, 客户五 (Customer Five) 115,342,763.11 = 1.60%. The
    customers are anonymised ("客户一" … "客户五", "Customer One" … "Customer Five"). The same line in
    the two earlier reports: FY2024 "1,490,025,281.33 … 25.62%"; FY2023 "849,983,989.64 … 15.85%".
  - **It states the cost of serving many customers, and it is the opposite of JLC's arrangement.**
    FY2025 report, risk factor 3, p.29: "报告期内，公司应收账款净额 221,617.12 万元，占公司总资产的 14.69%，占营业收入的 30.80%，公司应收账款的账龄符合行业特点，但由于公司客户数量庞大，一定程度上增加了应收账款管理的成本与发生坏账的风险。"
    — "In the reporting period the Company's net accounts receivable were CNY 2,216,171,200, 14.69%
    of total assets and 30.80% of revenue; the ageing of the receivables is in line with industry
    characteristics, but **because the Company's customer count is enormous, this to some degree
    increases the cost of managing receivables and the risk of bad debts**." (Our translation;
    emphasis ours.) JLC, by contrast, sells its online long tail on 先款后货 — "payment before goods"
    (PCB-2) — and its prospectus says "报告期内，公司应收账款周转率远高于同行业可比公司" ("the
    Company's accounts-receivable turnover during the reporting period was far higher than that of
    comparable companies in the same industry").
  - **Capital.** Fixed assets at 31 December 2025 **CNY 6,069,980,640.55** (40.25% of total assets),
    down 4.88% on 6,168,287,598.69 a year earlier; of which CNY 2,115,111,962.52 is pledged as
    security for borrowings ("抵押借款" — "mortgage/pledge-secured borrowings"). Capex
    (购建固定资产、无形资产和其他长期资产支付的现金 — "cash paid to acquire and construct fixed assets,
    intangible assets and other long-term assets") **852,683,193.60** in 2025 and 1,127,871,170.01
    in 2024. No PCB capacity-utilisation figure is printed for the PCB business in any of the three
    reports; utilisation is discussed only qualitatively and only for the CSP substrate line
    ("产能利用率逐季提升" — "capacity utilisation rose quarter by quarter").
- **DERIVED (arithmetic written out):** computed and checked by script before being written
  down; the arithmetic is reproduced in full below.
  - **Margins reproduce, and two more of PCB-1's five peer columns are now verified against the
    peer's own filing.** (4,090,502,302.37 − 2,915,691,055.62) ÷ 4,090,502,302.37 = **28.72%**;
    (4,897,079,816.57 − 3,660,050,280.12) ÷ 4,897,079,816.57 = **25.26%**; and 25.26 + 1.70 =
    **26.96%** for 2024. The JLC prospectus attributes 28.72% (2023) and 26.96% (2024) to 兴森科技
    (Fastprint). **Both agree exactly.**
  - **The prospectus's "未披露" ("not disclosed") for 2025 is a timing artefact, and this entry fills
    it.** JLC's
    prospectus was filed in April 2026; Fastprint's FY2025 annual report was published on
    **2026-04-25**. Fastprint's 2025 PCB gross margin is **25.26%**. Substituting it into PCB-1's
    2025 peer set gives a mean of (25.26 + 21.17 + 8.52 + 16.45 + 26.10) ÷ 5 = **19.50%**, against
    the printed four-company mean of 18.06%. JLC's 2025 gap over the peer mean therefore narrows
    from +10.00 pp to **+8.56 pp** once Fastprint's now-published figure is included. That is our
    computation, not the prospectus's, and it is a correction *against* our own thesis.
  - **Capital intensity, against JLC.** Revenue ÷ fixed assets: 7,194,624,804.67 ÷ 6,069,980,640.55
    = **1.19×**, against JLC's 3.16× (PCB-2). Capex ÷ revenue: 852,683,193.60 ÷ 7,194,624,804.67 =
    **11.85%**, against JLC's 13.56%. Fastprint turns its fixed assets **2.66× more slowly** than
    JLC while spending a similar share of revenue on capex.
  - **Receivables check.** 2,216,171,200 ÷ 7,194,624,804.67 = **30.80%**, reproducing the printed
    figure exactly.
  - **Effective number of customers.** H from the 2025 top five = 0.1306² + 0.0768² + 0.0292² +
    0.0203² + 0.0160² = 0.02447533, so 1/H ≤ **40.9**; with the 72.71% remainder as a single block,
    1/H ≥ 1.8. Same caveat as PCB-3: an upper bound, not a point estimate.
- **Bears on:**
  - **H6 (context, and a hole in the evidence).** The single best candidate for a second
    batch-split disclosure — a listed company that says in its own risk factors that it leads in
    sample and small-batch PCB, and that runs volume production alongside it — publishes revenue and
    margin split four different ways and **never by batch size**. This is the strongest available
    evidence that JLC's p.245 table is close to unique. Chinese listing rules require segment
    disclosure by 行业 (industry), 产品 (product), 地区 (region) and 销售模式 (sales model); they do
    not require it by order size, so nobody does it unless, like JLC, they have to explain to a
    listing committee where their profit comes from.
  - **H6 (supports, indirectly, and by a different route).** Fastprint's own semiconductor segment
    is a natural experiment inside one company: the IC substrate line runs at **−16.06%** gross
    margin explicitly *because* it "has not yet achieved large-batch production" and is carrying
    undiluted labour, depreciation and energy. That is the *opposite* sign to the PCB long-tail
    story, and it is the conventional capital-intensity argument stated plainly by a company living
    it. Recorded here because it cuts against us: in a genuinely capital-heavy process, being off
    volume destroys the margin. Whatever makes small-batch PCB profitable does not transfer
    automatically to a process with substrate-like economics — and silicon is far closer to the
    substrate end.
  - **H7 (challenges).** Top-five concentration went 15.85% → 25.62% → **27.29%** in two years, with
    one customer at 13.06%. That is the third company here (with Xunjiexing and Shapeways) where a
    large customer *list* sits alongside a concentrated *revenue* distribution.
  - **H6 (context).** Fastprint's receivables risk factor is a rare explicit statement of the
    cost-to-serve of a long tail: an enormous customer count raises receivables-management cost and
    bad-debt risk. JLC removes that cost entirely by taking payment before goods. That is a design
    choice foundry.api could copy and a reason JLC's margin is not simply "more customers".
- **Used in:** not yet.
- **Caveats:**
  - Fastprint's blended margin is dominated by things that are not the PCB long tail: an IC
    substrate business in pre-volume ramp, an overseas distribution arm (Fineline), and an SSD
    business. Its 25.26% PCB line is the only comparable number, and even that mixes quick-turn
    sample work with volume boards, HDI and SLP.
  - **The top-five customers are anonymised** ("客户一" … "客户五", "Customer One" … "Customer
    Five"), so the concentration cannot be
    cross-checked against the customers' own filings, and the concentration is likely driven by the
    memory-chip substrate customers rather than by the PCB business.
  - The 2025 PCB margin (25.26%) is **our** substitution into PCB-1's peer mean. The prospectus's
    18.06% remains what the prospectus prints, and both numbers are recorded above.
  - Capacity and utilisation for the PCB business are not disclosed in any of the three reports, so
    the capital-intensity comparison with JLC rests on revenue ÷ fixed assets, a cruder measure that
    is distorted by Fastprint's pre-revenue substrate plant.

### PCB-5. The other three peers, read from their own filings: every one of PCB-1's fifteen numbers checks out — and customer count predicts neither margin nor concentration

- **Sources:** annual reports (年度报告, "annual report") from cninfo's own document server,
  `static.cninfo.com.cn`:
  - **四会富仕电子科技股份有限公司** (Sihui Fushi Electronic Technology), SZSE **300852**:
    FY2025, published 2026-03-31, <http://static.cninfo.com.cn/finalpage/2026-03-31/1225060159.PDF>;
    FY2023, published 2024-03-30, <http://static.cninfo.com.cn/finalpage/2024-03-30/1219474187.PDF>
  - **深圳市强达电路股份有限公司** (Shenzhen Qiangda Circuit), SZSE **301628**:
    FY2025, published 2026-04-10, <http://static.cninfo.com.cn/finalpage/2026-04-10/1225088989.PDF>
  - **深圳市金百泽电子科技股份有限公司** (Shenzhen Jinbaize Electronic Technology), SZSE **301041**:
    FY2025, published 2026-04-21, <http://static.cninfo.com.cn/finalpage/2026-04-21/1225132278.PDF>
- **Verification:** Verified 2026-09-19. All four PDFs downloaded (HTTP 200; 2,058,322 /
  3,059,109 / 1,613,774 / 1,475,326 bytes; 178 / 186 / 224 / 211 pages), text extracted with
  `pypdf`, and every margin recomputed from the printed revenue and cost.
- **What it says:**
  - **四会富仕 (Sihui Fushi)**, FY2025 report §2 收入与成本 ("2. Revenue and cost"), table
    "占公司营业收入或营业利润 10%以上的行业…的情况" ("industries … accounting for more than 10% of the
    Company's revenue or operating profit"): 分产品 ("by product") 印制电路板 ("printed circuit
    boards") revenue 1,831,397,613.10, cost 1,530,196,764.46, **毛利率 (gross margin) 16.45%**,
    "毛利率比上年同期增减 −2.58%" ("change in gross margin against the same period last year:
    −2.58 [percentage points]"). FY2023 report, same table: revenue 1,269,812,602.58, cost
    958,088,572.22, **毛利率 24.55%**. Its sales-model row reads **直销 100.00%** ("direct sales
    100.00%") — 100% direct sales, no traders, no online channel. Top five customers, FY2025:
    "前五名客户合计销售金额（元）374,057,905.28 / 前五名客户合计销售金额占年度销售总额比例 19.36%"
    ("total sales to the top five customers (yuan) 374,057,905.28 / share of total annual sales
    taken by the top five customers 19.36%"), largest 109,793,426.64 = **5.68%**; FY2023:
    304,943,584.50 = **23.18%**, largest 83,541,306.73 = 6.35%. Customers are anonymised
    ("第一名" … "第五名", "No. 1" … "No. 5").
  - **强达电路 (Qiangda)**, FY2025 report, same table: 分产品 ("by product") 印制电路板 ("printed
    circuit boards") revenue 909,167,885.09, cost 671,885,078.30, **毛利率 (gross margin) 26.10%**,
    "毛利率比上年同期增减 −1.48%" ("change in gross margin against the same period last year:
    −1.48 [percentage points]"). 分销售模式 ("by sales model") **直销 100.00%** ("direct sales
    100.00%"). Top five customers: "前五名客户合计销售金额（元）148,294,679.88 / …占年度销售总额比例 16.31%"
    ("total sales to the top five customers (yuan) 148,294,679.88 / … share of total annual sales
    16.31%"), largest 43,553,460.22 = **4.79%**.
  - **金百泽 (Jinbaize)**, FY2025 report, same table: 分行业 ("by industry") 电子电路 ("electronic
    circuits") revenue 684,095,960.17, cost 532,508,551.93, 毛利率 (gross margin) 22.16%; 分产品
    ("by product") **印制电路板** ("printed circuit boards") revenue 399,552,498.09, cost
    314,971,857.02, **毛利率 21.17%**, "毛利率比上年同期增减 −2.80%" ("change in gross margin against
    the same period last year: −2.80 [percentage points]"); 电子制造服务 ("electronic manufacturing
    services", EMS) revenue 210,035,476.99, 毛利率 24.11%. **This resolves the prospectus footnote**
    "部分可比公司同时存在其他主营业务，表中取相关数据" ("some comparable companies also have other core
    businesses; the table takes the relevant data") for this company: JLC took the 印制电路板
    (printed circuit board) product line, not the 电子电路 (electronic circuits) industry line.
    Top five customers: "前五名客户合计销售金额（元）96,817,113.38 / …占年度销售总额比例 13.82%"
    ("total sales to the top five customers (yuan) 96,817,113.38 / … share of total annual sales
    13.82%"), largest 25,187,347.83 = **3.60%** — the lowest concentration of any company here
    except JLC.
  - **金百泽 (Jinbaize) is the peer that most resembles JLC's positioning, and it says so.** FY2025
    report,
    p.11: "公司在 PCB样品研发服务和小批量领域属于行业前端水平" — "the Company is at the leading edge
    of the industry in PCB sample R&D services and small batches" (our translation); and p.11:
    "公司拥有大亚湾 PCB 总部、西安等各地区智能制造生产基地，以 PCB 样板为入口，顺应各行业电子化升级和个性化需求趋势，发展中小批量 PCB 板，满足越来越多的客户对 PCB 样板和 PCB 中小批量一站式采购的需求"
    — "The Company has its Daya Bay PCB headquarters and intelligent manufacturing bases in Xi'an and
    other regions; **taking the PCB sample board as its entry point**, and following the trend of
    electronification and personalised demand across industries, it develops small- and
    medium-batch PCB, meeting the demand of more and more customers for one-stop purchase of PCB
    sample boards and small- and medium-batch PCB." (Our translation.)
  - **A third, incompatible definition of the size bands.** 金百泽 (Jinbaize)'s FY2025 glossary,
    p.4: "样板 指 印制电路板样品，面积通常在 5㎡以下"; "小批量板 指 小批量印制电路板，面积通常为 5-20㎡"
    — "样板 (sample board): printed-circuit-board samples, of area usually under 5 ㎡ [m²]";
    "小批量板 (small-batch board): small-batch printed circuit boards, of area usually 5–20 ㎡". That
    is a third set of thresholds, agreeing with Xunjiexing on the sample cutoff (5 m²) and with JLC
    on the small-batch ceiling (20 m²), and matching neither in full. **There is no industry-standard
    definition of "small batch".**
- **DERIVED (arithmetic written out):** computed and checked by script before being written
  down; the arithmetic is reproduced in full below.
  - **All fifteen of PCB-1's peer figures now check out.** Recomputed from each company's own
    printed revenue and cost:

    | | recomputed | prospectus | |
    |---|---|---|---|
    | 兴森科技 (Fastprint) 2023 PCB | 28.72% | 28.72% | agrees |
    | 兴森科技 (Fastprint) 2024 (25.26 + 1.70) | 26.96% | 26.96% | agrees |
    | 兴森科技 (Fastprint) 2025 PCB | 25.26% | 未披露 (not disclosed) | published after filing (PCB-4) |
    | 金百泽 (Jinbaize) 2025 PCB | 21.17% | 21.17% | agrees |
    | 金百泽 (Jinbaize) 2024 (21.17 + 2.80) | 23.97% | 23.97% | agrees |
    | 迅捷兴 (Xunjiexing) 2023 / 2024 / 2025 | 15.14 / 14.33 / 8.52% | same | agrees |
    | 四会富仕 (Sihui Fushi) 2023 | 24.55% | 24.55% | agrees |
    | 四会富仕 (Sihui Fushi) 2025 | 16.45% | 16.45% | agrees |
    | 四会富仕 (Sihui Fushi) 2024 (16.45 + 2.58) | 19.03% | 19.03% | agrees |
    | 强达电路 (Qiangda) 2025 | 26.10% | 26.10% | agrees |
    | 强达电路 (Qiangda) 2024 (26.10 + 1.48) | 27.58% | 27.58% | agrees |

    Only 金百泽 (Jinbaize) 2023 (28.42%) and 强达电路 (Qiangda) 2023 (28.63%) were not re-derived,
    because their FY2023
    reports were not downloaded. Thirteen of fifteen are directly verified; the other two are
    Partial.
  - **The peer set laid side by side, 2025:**

    | Company | Customers (best available) | PCB gross margin | Top-5 share | Top-1 share |
    |---|---|---|---|---|
    | JLC 嘉立创 | 1,358,700 paying | 28.06% | **1.16%** | **0.28%** |
    | 金百泽 Jinbaize | 20,000+ | 21.17% | 13.82% | 3.60% |
    | 迅捷兴 Xunjiexing | 10,000+ cumulative | **8.52%** | **40.07%** | 12.58% |
    | 兴森科技 Fastprint | 4,000+ | 25.26% | 27.29% | **13.06%** |
    | 强达电路 Qiangda | ~3,000 active | 26.10% | 16.31% | 4.79% |
    | 四会富仕 Sihui Fushi | 595 (2022) | 16.45% | 19.36% | 5.68% |

  - **Rank correlations across the six, computed and reported because they are unhelpful to us.**
    Spearman ρ between customer count and 2025 gross margin = **+0.314**; between customer count and
    top-5 share = **−0.486**. Excluding JLC, which is the case under test rather than an
    observation: ρ = **−0.200** and **−0.100** respectively. **With n = 6 (n = 5) none of these is
    evidence of anything.** They are reported to make the point that the ordering is not clean, not
    to claim a relationship in either direction.
- **Bears on:**
  - **H6 (context, and it strengthens PCB-1).** The peer table in the JLC prospectus is not a
    convenient rendering: thirteen of its fifteen numbers reproduce exactly from the peers' own
    audited annual reports. PCB-1 can be relied on as a transcription. What it is a transcription
    *of* — a set the issuer chose — remains a caveat.
  - **H7 (challenges, and the challenge is now sharper than in PCB-3).** Customer count does not
    predict revenue concentration at all in this set. Sihui Fushi, with **595** customers, has
    **19.36%** in its top five. Xunjiexing, with **over ten thousand**, has **40.07%**. Jinbaize,
    with over twenty thousand, has 13.82%. Whatever produces a long-tailed revenue distribution, it
    is not simply having many customers on the books. The only company here whose concentration is
    an order of magnitude below everyone else's is the only one with a million-odd customers — so
    the relationship may be real but highly non-linear, requiring a customer base two orders of
    magnitude larger than any conventional PCB maker's before it bites.
  - **H6 (challenges).** Nor does customer count predict margin. Qiangda, with about 3,000
    customers and 100% direct negotiated sales, earns **26.10%** — within two points of JLC's
    28.06%, and above every other peer. Whatever JLC's 28.06% is evidence for, "online long tail
    beats conventional PCB" is too coarse a statement of it: one conventional PCB maker in this set
    is nearly as profitable.
- **Used in:** not yet.
- **Caveats:**
  - All three companies anonymise their top five customers, so none of the concentration figures can
    be cross-checked against the customers' own filings.
  - The "customers" column mixes incompatible counts — JLC's *annual paying users*, Xunjiexing's
    *cumulative since inception*, Qiangda's *active in the year*, Sihui Fushi's count as of
    March 2023, and Fastprint's and Jinbaize's undated "over N" marketing figures. The correlations
    above are computed on that mixture and should not be treated as measurements.
  - None of the three publishes capacity, utilisation or area sold in a form that allows a price per
    square metre, so the capital-intensity comparison cannot be extended to them.
  - 金百泽 (Jinbaize) 2023 and 强达电路 (Qiangda) 2023 remain Partial: taken from the JLC
    prospectus, not re-derived.

### PCB-6. The companies with no filings: OSH Park prices the small-order premium at exactly 5/3 in a public price list; DirtyPCBs is not dead; PCBWay claims its own factory and publishes nothing

None of the four companies the repository owner named alongside JLCPCB files audited accounts
anywhere we could find. Their evidence is price lists, About pages and Wayback captures, and it is
labelled accordingly — this entry is **Partial** as a whole, with the OSH Park price table
**Verified**.

- **Sources:**
  - OSH Park, LLC, "Fabrication Services" (its pricing page): <https://oshpark.com/pricing>,
    footer "© Copyright 2023 OSH Park, LLC"
  - DirtyPCBs.com: <http://dirtypcbs.com/> — which redirects to <http://dirtypcbs.com/store/pcbs>
  - PCBWay: <https://www.pcbway.com/about.html> and <https://www.pcbway.com/>
- **Verification:** Fetched and read 2026-09-19. OSH Park's price table was read out of the served
  HTML and every figure below is quoted from it; that part is **Verified**. The DirtyPCBs and
  PCBWay statements are **Partial** — they are company self-descriptions with nothing to check them
  against.
- **What it says:**
  - **OSH Park publishes a complete, unconditional price list with no setup fee, no minimum for its
    prototype service, and a separate, cheaper price for volume.** Quoted exactly from the page:

    | Two Layer Boards — Service | Cost | Time To Ship |
    |---|---|---|
    | Prototype | "$5 per square inch, per set of 3" | "9-12 calendar days" |
    | Super Swift | "$10 per square inch, per set of 3" | "4-5 business days" |
    | 2oz 0.8mm | "$5 per square inch, per set of 3" | "12-21 calendar days" |
    | Flex | "$10 per square inch, per set of 3" | "Temporarily suspended 12-21 calendar days" |
    | After Dark | "$5 per square inch, per set of 3" | "12-21 calendar days" |
    | **Medium Run** | **"$1 per square inch. 100 square inch minimum, must be in multiple of 10"** | "12-21 calendar days" |

    | Four Layer Boards — Service | Cost | Time To Ship |
    |---|---|---|
    | Prototype | "$10 per square inch, per set of 3" | "9-14 calendar days" |
    | Super Swift | "$20 per square inch, per set of 3" | "5-6 business days" |
    | **Medium Run** | **"$2 per square inch, 100 square inch minimum. Must be in multiple of 3"** | "12-21 calendar days" |

    Six layer: "Prototype — $15 per square inch, per set of 3 — 12-21 calendar days".
  - **It does not own a plant, and says who makes the boards is elsewhere.** The page opens:
    "OSH Park is a community printed circuit board (PCB) order that brings you high quality,
    lead-free boards which are **manufactured in the United States** and shipped for free to
    anywhere in the world." (Emphasis ours.) It calls itself a "community printed circuit board
    order" — i.e. an aggregator that panelises many customers' boards onto shared panels — not a
    manufacturer.
  - **DirtyPCBs is alive.** The brief for this research recorded it as "defunct". As of 2026-09-19
    `http://dirtypcbs.com/` returns **HTTP 200** and redirects to a working storefront at
    `/store/pcbs`, titled "PCBs cheap! - DirtyPCBs.com", with live navigation for "Order New PCBs",
    "Shared PCBs", "PCB Stencils", "PCB Cloning", "SLA 3D Prints", "Laser Cut Acrylic", "Custom
    Cables", "Dirty BOM", "China Mail Forwarding", "Chip Decapping", "Fulfillment and Shipping",
    "China export brokerage" and an "API". **The prices are computed client-side and do not appear
    in the served HTML**, so none could be read; the order form's column headings are "File /
    Material / Layers / Quantity / Price". No claim about its economics or its survival is made
    here beyond the fact that the site serves orders.
  - **PCBWay claims factories of its own and publishes no numbers.** Its About page: "With more than
    a decade in the field of PCB prototype and fabrication, we are committed to meeting the needs of
    our customers from different industries in terms of quality, delivery, cost-effectiveness and
    any other demanding requests." Section headings on the same page name "**Inside PCBWay
    Factory**", "Inside PCBWay Assembly Factory", "Inside CNC Machining Factory", "Inside 3D
    Printing Factory", "Inside Injection Molding Factory", and a selling point reads "Best Value /
    **Manufacturer Direct Pricing**". On delivery: "Through the years we are proud to have been
    keeping an on-time delivery rate of 99%. … We work in three shifts to make sure your PCBs will
    be on your desk as agreed up and as early as possible." A site-wide banner on 2026-09-19 read
    "**PCBWay factories** will be closed on Sep 25, and Oct 1-4 (GMT+8)." The About page names its
    trading entity: "PCBWay works globally with its Hong Kong entity, Hong Kong Yanghui Information
    Technology Limited, to provide reliable manufacturing and secure global payment services for
    creators, engineers, and businesses." **No revenue, order count, customer count, margin or
    capacity figure is published anywhere on the site we read.**
- **DERIVED (arithmetic written out):** computed and checked by script before being written
  down; the arithmetic is reproduced in full below.
  - **OSH Park's own price list contains the small-order premium, and it is the same at both layer
    counts.** Prototype price per *board* per square inch is the quoted price divided by the set of
    three:
    - 2 layer: $5 ÷ 3 = **$1.6667** per board-in², against Medium Run at **$1.00** → ratio
      **1.6667×**.
    - 4 layer: $10 ÷ 3 = **$3.3333** per board-in², against Medium Run at **$2.00** → ratio
      **1.6667×**.
    Both are exactly 5/3. Whoever set these prices applied a uniform 66.7% premium to the
    three-off product over the hundred-square-inch product.
  - **The minimum ticket differs by 20×.** A 1 in² two-layer board in three copies costs
    1 × $5 = **$5.00** with no setup fee and no minimum. The cheapest possible Medium Run order is
    the 100 in² minimum × $1 = **$100.00**. 100 ÷ 5 = **20×**.
- **Bears on:**
  - **H6 (supports, modestly).** This is the pattern of SMB-1 and PCB-3 showing up in a *published
    price list* rather than in a margin disclosure. A US aggregator that has to cover its own costs
    charges 1.667× as much per board per unit area for three-off prototypes as for hundred-square-inch
    runs. Prices are not margins — OSH Park's costs for the two products differ too — but a seller
    that must survive on published prices has priced small orders at a premium, not a discount, and
    has done so consistently for years.
  - **H8 (supports).** OSH Park is the cleanest published example in this file of the model
    foundry.api proposes: a complete public price list, no setup fee, no minimum, no quote request,
    no salesperson, and a price you can compute yourself from the area of your board before you
    upload anything.
  - **H6 (context, cutting against).** OSH Park owns no plant. Its margin is the spread between what
    it charges and what a US fab charges it for a shared panel, and neither side of that spread is
    public. It cannot tell us whether a *capital-owning* long-tail business works; only PCB-2 can.
  - **H5, H6, H7 (nothing).** No customer counts, order counts, revenue, margin or concentration
    figures exist for any of these three. That absence is the finding: the three best-known Western
    and Chinese online PCB brands aimed squarely at the long tail publish, between them, not one
    number that bears on whether the long tail pays.
- **Used in:** not yet.
- **Caveats:**
  - **Prices are not margins.** The 1.667× premium reflects OSH Park's own costs as well as its
    pricing power, and a three-off prototype genuinely costs more per unit area to make than a
    hundred-square-inch run — that is the whole point of the comparison, but it means the ratio
    cannot be read as a margin ratio.
  - The OSH Park page carries a 2023 copyright notice, so the price table may be stale relative to
    the fetch date. No Wayback comparison was run, so **how these prices have moved over time is not
    established here** — that was in scope and was not done.
  - **The premise that Dirty PCBs is defunct is not supported by what the site returns.** No
    founder's post about its economics or about any shutdown was located; the Dangerous Prototypes
    blog was not searched. Anything this repository says about Dirty PCBs having died needs checking
    before it is used.
  - PCBWay's "Inside PCBWay Factory" claim is a marketing heading on its own website. Nothing
    corroborates it. It is recorded as a claim, not as an established fact, and it is the kind of
    claim a broker also makes.
  - **Seeed Studio (Fusion PCB), Eurocircuits, Aisler, Beta LAYOUT / Multi-CB, Advanced Circuits /
    4PCB, Sierra Circuits and Elecrow were not reached at all.** See the blocked-sources list.

---

## Comparison table

Every cell is sourced in the entry above it; "—" means the figure is not disclosed anywhere we
could reach, and that absence is itself part of the finding.

| | JLC (嘉立创) | Xunjiexing (迅捷兴) | Fastprint (兴森科技) | Jinbaize (金百泽) | Sihui Fushi (四会富仕) | Qiangda (强达电路) |
|---|---|---|---|---|---|---|
| Listing | SZSE, IPO filed Apr 2026 | SSE STAR 688655 | SZSE 002436 | SZSE 301041 | SZSE 300852 | SZSE 301628 |
| Core gross margin 2023 / 2024 / 2025 | **28.73 / 30.05 / 28.06%** (PCB) | 15.14 / 14.33 / **8.52%** | 28.72 / 26.96 / **25.26%** (PCB line) | 28.42 / 23.97 / 21.17% | 24.55 / 19.03 / 16.45% | 28.63 / 27.58 / 26.10% |
| Verified against the company's own filing? | n/a (is the source) | **Yes, all 3 years** | **Yes, 2023 and 2024; 2025 added by us** | **Yes, 2024 and 2025** | **Yes, 2023, 2024 and 2025** | **Yes, 2024 and 2025** |
| Margin split by batch size | **Yes** — 36.24% sample+small-batch vs 2.76% medium/large-batch, 2025 (SMB-1) | No numeric split; qualitative table only | **No** — splits by industry, product, region, channel, never by batch | **No** — splits PCB vs EMS only | **No** | **No** |
| Customers | **1,358,700 paying users (2025)**; 9.59M registered | "over 10,000" cumulative | "over 4,000" worldwide | "over 20,000" worldwide | 143 (2017) → 595 (2022) | ~3,000 active (2025) |
| Orders / year | **21,290,800 (2025)** | — | — | — | — | — |
| Top-5 customer share | **1.16% (2025)** | **40.07% (2025)**; top-1 12.58% | 15.85 → 25.62 → **27.29%**; top-1 13.06% | **13.82% (2025)**; top-1 3.60% | 23.18% (2023) → **19.36% (2025)**; top-1 5.68% | **16.31% (2025)**; top-1 4.79% |
| Effective customers (1/H, upper bound) | ≤ ~36,400 | ≤ ~27 | ≤ ~41 | — | — | — |
| Capacity | 11.53M m²/yr PCB, 76.78% utilised | 0.74M m² sold 2025; 0.60M m²/yr batch + 0.72M m²/yr sample planned | Not disclosed | — | — | — |
| Average price per m² | CNY 441.48 (2025) | CNY 866.47 (2025) | Not computable (no area disclosed) | — | — | — |
| Capital intensity | Fixed assets CNY 3.26bn; capex CNY 1.40bn (2025); revenue/FA **3.16×**; capex/revenue 13.56% | Fixed assets CNY 753M (2025), up 134% | Fixed assets CNY 6.07bn; capex CNY 853M; revenue/FA **1.19×**; capex/revenue 11.85% | — | — | — |
| Owns plant? | **Yes** — five owned bases, ~1M m² of site, title deeds, land-use rights | Yes — Shenzhen, Xinfeng, Zhuhai | Yes — CNY 2.12bn of it pledged for borrowings | Yes — Daya Bay HQ plant, Xi'an | Yes | Yes |
| Pricing model | Online self-service, auto reference quote, **payment before goods**; offline = negotiated | Direct sales + traders, negotiated; online mall launched 2026-01-04 | Direct sales 94.21%, traders 5.79%; receivables **30.80% of revenue** | Negotiated | **直销 100.00%** ("direct sales 100.00%") — all direct, negotiated | **直销 100.00%** ("direct sales 100.00%") — all direct, negotiated |
| CPCA rank (domestic PCB makers) | ~16th / 17th (estimated) | 78th / 83rd | 7th / 8th | 62nd / 59th | 25th / 23rd | 53rd / 53rd |
| Bottom line | Net margin 12.65% (2025) | **Net loss CNY 22.4M (2025)** | Net profit up 168% (2025), semiconductor arm at −9.28% gross | PCB 21.17%, EMS 24.11% | — | 26.10%, the best of the five peers |

### The companies that file nothing (PCB-6)

| | OSH Park | DirtyPCBs | PCBWay | Seeed Fusion |
|---|---|---|---|---|
| Files audited accounts? | No | No | No | No — and whether it ever did on NEEQ was not checked |
| Owns plant? | **No** — "manufactured in the United States", i.e. it brokers | Not established | Claims "PCBWay factories" on its own site; uncorroborated | Not checked |
| Published price list? | **Yes, complete** — $5/in² per set of 3, no minimum, no setup fee; Medium Run $1/in², 100 in² minimum | Yes, but computed client-side and unreadable from the served HTML | Yes, via an online quoter | Not checked |
| Small-order premium in its own price list | **1.667×** per board-in², identical at 2 and 4 layers | — | — | — |
| Any revenue, order, customer, margin or capacity figure? | **None** | **None** | **None** | **None** |

## Verdict: does the JLC pattern generalise?

**Partly, and the part that generalises is not the part that would have been most useful.**

Three separate claims have to be kept apart.

**1. "Within one company, sample/small-batch work carries a much higher gross margin than
big-batch work." — Supported, by two independent companies.** JLC prints the numbers (36.24% vs
2.76% in 2025, SMB-1). Xunjiexing, a different company with a different owner on a different
exchange, prints the same relationship as a description of the industry — 样板 (sample boards) high, 小批量
(small batch) relatively high, 大批量 (large batch) generally lower — and then, in its FY2023 report,
explains a 5.62-point margin fall by
a rising batch share and falling batch prices while its *volume* grew 30%. Two companies is not
many, but they are independent, both audited, and they point the same way. JLC's own prospectus
also uses the mechanism as an explanation for a *third party's* results — that Xunjiexing's 2023
margin was low "受批量订单占比逐步提升…影响", "affected by the gradually rising share of batch orders".

**2. "The online long-tail seller earns a higher blended margin than conventional PCB makers." —
Supported, with two caveats, one of which we found against ourselves.** JLC's PCB margin beat the
mean of its five named comparables by +3.64, +7.68 and +10.00 percentage points in 2023, 2024 and
2025, and the gap widened every year as the peer mean fell from 25.09% to 18.06%. The issuer
attributes the gap to "销售模式和客户结构差异" — "differences in sales model and customer structure".
First caveat:
JLC chose the comparables, and it conspicuously did not choose the large listed Chinese PCB makers.
Second caveat, and it is ours, not the prospectus's: the 2025 peer mean of 18.06% excludes Fastprint
because its FY2025 report had not yet been published when the prospectus was filed. It has been
published since, on 2026-04-25, at 25.26% (PCB-4). Putting it back gives a five-company 2025 mean of
19.50% and cuts JLC's gap from +10.00 to **+8.56 pp**. The direction and the widening survive; the
headline number does not.

**3. "Serving a long tail is what produces the margin." — NOT supported. The evidence actively
contradicts the simple version.** All five peers have now been read in their own filings, and
customer count does not predict margin. Xunjiexing has served "over ten thousand" enterprises,
calls itself a sample-board specialist, and has the *lowest* margin in the set (8.52%) and a net
loss. Sihui Fushi, with 595 customers and 100% direct negotiated sales, earns 16.45%. **Qiangda,
with about 3,000 active customers and also 100% direct negotiated sales, earns 26.10% — within two
points of JLC and above every other peer.** Jinbaize, the peer that positions itself closest to
JLC ("taking the PCB sample board as its entry point", 20,000+ customers), earns 21.17%. The
Spearman rank correlation between customer count and 2025 gross margin across the six is +0.314,
and −0.200 with JLC removed; with n = 6 neither means anything, which is the point. If the long
tail alone produced the margin, this ordering would be impossible. Whatever JLC has — scale,
panelisation across millions of orders, an integrated EDA front end, payment before goods, vertical
integration into components and assembly, or simply a customer base two orders of magnitude beyond
any conventional PCB maker's — it is not reducible to "small customers".

There is also one piece of evidence from outside the filings. **OSH Park, which has to survive on
published prices and owns no plant, charges exactly 1.667× as much per board per square inch for a
three-off prototype as for a hundred-square-inch run — the same ratio at two layers and at four**
(PCB-6). A price is not a margin. But a seller with no negotiating channel at all has independently
concluded that small orders bear a premium, not a discount.

And a fourth finding, which is a challenge and belongs in the verdict rather than a footnote:

**4. Customer count and revenue concentration are almost unrelated.** Xunjiexing's ten thousand
customers coexist with 40.07% of revenue in five accounts and 12.58% in one; Fastprint's top five
went 15.85% → 27.29% in two years. Meanwhile **Sihui Fushi, with 595 customers, is at 19.36%** —
less than half Xunjiexing's concentration on a twentieth of the customers. JLC's top five are
1.16%. H7 cannot be argued from a customer list. It has to be argued from a concentration
disclosure. The one pattern that does hold is a discontinuity rather than a gradient: five
companies with hundreds to tens of thousands of customers all sit between 13.8% and 40.1% top-five
concentration, and the one company with 1.36 million sits at 1.16%. If many small customers remove
buyer power, the evidence here says it takes a *lot* more of them than any conventional
manufacturer has.

**On the companies with no filings.** OSH Park, DirtyPCBs, PCBWay and Seeed — the four brands most
associated in the English-speaking world with cheap PCBs for a long tail — publish, between them,
**not one figure** bearing on whether the long tail pays: no revenue, no order count, no customer
count, no margin, no capacity. That is itself a finding, and it explains why this file is almost
entirely Chinese: China's listing rules are the only reason any of this evidence exists. Two
corrections also belong here. **DirtyPCBs is not defunct** — `dirtypcbs.com` returns HTTP 200 and
serves orders as of 2026-09-19 — so any claim in this repository that it died needs checking.
And PCBWay's claim to own its factories is a heading on its own website with nothing to corroborate
it.

**On what can be known at all.** The industry is far more disclosed than expected, because China's
listing rules force it: five PCB companies' margins printed in one table, each traceable to an
audited annual report on a public document server, and three of those fifteen company-years now
verified directly against the company's own filing (Xunjiexing 2023–2025, Fastprint 2023–2024,
plus Fastprint 2025 which the prospectus could not yet have). But **only JLC publishes a margin
split by batch size, and we now have direct evidence that the best-placed peer chooses not to.**
Fastprint calls itself a leader in sample and small-batch PCB, runs volume production alongside it,
and splits its segment disclosure four different ways — by industry, product, region and sales
channel — and never by order size (PCB-4). Chinese listing rules require those four cuts; they do
not require batch size. JLC's p.245 table exists because a listing committee made it explain where
its profit comes from, not because anyone in this industry routinely publishes it. If JLC lists and
stops filing prospectuses, this evidence stops being renewed.

**What would settle it.** A second company publishing gross margin split by order size. **We
looked at the best candidate and it does not exist there.** The remaining candidates are
prospectuses and review-enquiry replies (问询函回复) of other PCB companies, where the exchange can
compel an issuer to break out a margin the annual report does not — Qiangda and Sihui Fushi both
have such documents on cninfo and neither has been read; see the open items below.

## Blocked and incomplete sources

| Source | URL | What happened | What would unblock a human |
|---|---|---|---|
| cninfo document server | `http://static.cninfo.com.cn/finalpage/...` | **HTTP 403** to a plain `curl` | Solved: a browser User-Agent plus `-H "Referer: http://www.cninfo.com.cn/"` returns HTTP 200. Recorded here so nobody loses the time again. |
| 金百泽 (Jinbaize) 2023 and 强达电路 (Qiangda) 2023 annual reports | cninfo | **Not read.** Those two margins (28.42% and 28.63%) remain **Partial** — taken from the JLC prospectus, not re-derived. All thirteen other peer figures were verified. | Nothing external — the documents are free on cninfo and download fine with the header trick above. It needs the time. |
| Exchange review-enquiry replies (问询函回复, "replies to enquiry letters") for Qiangda and Sihui Fushi | cninfo | **Not read.** These are where an exchange can compel a margin breakdown the annual report omits — the JLC prospectus already cites one of Sihui Fushi's for its customer count. Most likely place a second batch-split disclosure exists. | Nothing external. |
| Western small-batch specialists (Eurocircuits, Aisler, Beta LAYOUT/Multi-CB, Advanced Circuits/4PCB, Sierra Circuits, Elecrow) | various | **Not reached.** Ran out of budget. | Belgian NBB Central Balance Sheet Office (`consult.cbso.nbb.be`) and the German Bundesanzeiger both publish small-company accounts free; a human with a browser can retrieve Eurocircuits NV's and Beta LAYOUT GmbH's filed accounts directly, and those are the two most likely to contain a Western margin figure. |
| Seeed Studio / 深圳市矽递科技 (Shenzhen Xilidi Technology, i.e. Seeed) | cninfo, NEEQ | **Not searched.** If Seeed ever traded on NEEQ (新三板, the "New Third Board") it would have published audited annual reports with segment revenue. Unchecked. | Nothing external — a `column=bj` / NEEQ search on cninfo would settle it in minutes. |
| DirtyPCBs prices | `http://dirtypcbs.com/store/pcbs` | **HTTP 200, but the prices are rendered client-side** and are absent from the served HTML. The order form's headings ("File / Material / Layers / Quantity / Price") come through; the numbers do not. | A human with a browser sees the whole price table immediately. A headless browser would also work. |
| Dangerous Prototypes / Ian Lesnet's posts on DirtyPCBs' economics | dangerousprototypes.com | **Not searched.** | Nothing external. |
| OSH Park price history | `web.archive.org` captures of `oshpark.com/pricing` | **Not run.** The current prices were read live; the trajectory was not established. | Nothing external. `WebFetch` refuses web.archive.org; `curl` with the raw `…/web/<timestamp>id_/<url>` form and `--compressed` works, per [`search-log.md`](search-log.md). |

**None of these was blocked by a paywall, a login or a bot check, and nothing on this list defeated
us.** They are unfinished, and the reason is recorded honestly: the session hit an API rate limit
partway through and the remaining budget was spent on the two items with the highest evidentiary
value — the peer table and the plant-ownership quote. The one genuine technical obstacle is the
client-side rendering of DirtyPCBs' prices, and even that is trivial for a human.

---

# Second pass, 2026-09-25: entries PCB-7 onwards

Everything above this line was written in an earlier session, which closed by saying that **only
JLC publishes a margin split by batch size** and that the remaining hope was an exchange
review-enquiry reply. That verdict is now wrong, and this section says so with the documents in
hand. The consolidated table, the revised verdict and the blocked-source list for this pass are at
the end of the file. **The verdict above (§"Verdict: does the JLC pattern generalise?") is
superseded by [the second-pass verdict](#second-pass-verdict-2026-09-25); it is left in place
because it records what was believed on the evidence then available, and because its claims 1, 3
and 4 still stand.**

Nothing in this section was reached through a login, a paywall, a form or a CAPTCHA. Every document
is a free public filing on `static.cninfo.com.cn`, downloaded with the User-Agent-plus-Referer
recipe already recorded in [`search-log.md`](search-log.md).

---

### PCB-7. Qiangda Circuit's IPO prospectus prints gross margin split by *order area* — 44.86% on orders under 5 m² against 7.00% on orders over 50 m², over four periods, from the same two factories. It is a second JLC table, and in one respect a better one

- **Source:** 深圳市强达电路股份有限公司 (Shenzhen Qiangda Circuit Co., Ltd., SZSE ChiNext
  **301628**), 首次公开发行股票并在创业板上市招股说明书 ("Prospectus for the initial public
  offering of shares and listing on the ChiNext board"), filed 2024-10-17, Shenzhen Stock Exchange,
  via cninfo:
  <http://static.cninfo.com.cn/finalpage/2024-10-17/1221409205.PDF>
  The tables and passages below are on PDF pp. 79–80 (doc pp. 1-1-78/79, the definition and the
  three-column comparison), p. 161 (1-1-160, capacity and utilisation), pp. 267–268 (1-1-266/267,
  revenue by order area), pp. 274–276 (1-1-273/275, volume, price and order count by order area)
  and **p. 289 (1-1-288, the gross-margin table)**.
- **Verification:** Verified 2026-09-25. The PDF was downloaded from cninfo's own document server
  (HTTP 200, 10,676,895 bytes, 426 pages), its text extracted with `pypdf`, and every figure below
  read in place. The transcription was then checked three ways by script, and all three checks
  reproduce the filing's own printed totals exactly — see DERIVED. Reporting period ("报告期") is
  FY2021, FY2022, FY2023 and 2024 H1; the financial statements are audited by
  中汇会计师事务所（特殊普通合伙） (ZhongHui Certified Public Accountants LLP).
- **What it says:**
  - **The company defines its segments by the area of a single order, and prints the thresholds.**
    The note under the revenue table (PDF p.268) reads: "注：样板指订单面积在 5 平方米以下的印制电路板，小批量板指订单面积在 5-50 平方米的印制电路板，大批量板指订单面积在 50 平方米以上的印制电路板。"
    — "Note: 样板 (*sample boards*) means printed circuit boards with an order area under 5 square
    metres; 小批量板 (*small-batch boards*) means printed circuit boards with an order area of 5 to
    50 square metres; 大批量板 (*large-batch boards*) means printed circuit boards with an order area
    above 50 square metres." (Our translation.) The business section (PDF p.79) states the same
    thresholds as "每单 5 平方米以下 / 5-50 平方米 / 50 平方米以上" — "under 5 m² per order /
    5–50 m² / over 50 m²". **This is a cut by order size, stated as such, in square metres.**
  - **The gross-margin table itself** (PDF p.289). The heading is "②按订单面积划分" —
    "(2) Split by order area" — and the sentence introducing it is
    "报告期内，发行人 PCB 按订单面积划分的毛利率如下表所示：" — "During the reporting period the
    issuer's PCB gross margin split by order area is as shown in the table below." (Our translation.)
    The column headers are 收入占比 / 毛利率（剔除运费）/ 毛利率（含运费） — "share of revenue /
    gross margin (excluding freight) / gross margin (including freight)". Transcribed with the
    Chinese row labels as printed and our English beside them:

    | 类型 (type) | 2024 年 1-6 月 share (2024 H1) | GM excl. freight | GM incl. freight | 2023 年度 share (FY2023) | GM excl. | GM incl. | 2022 年度 share (FY2022) | GM excl. | GM incl. | 2021 年度 share (FY2021) | GM excl. | GM incl. |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|
    | 样板 (sample boards, <5 m²/order) | 52.54% | 45.42% | **44.57%** | 48.70% | 45.63% | **44.86%** | 42.87% | 44.25% | **43.46%** | 39.40% | 44.71% | **43.93%** |
    | 小批量板 (small-batch boards, 5–50 m²) | 33.25% | 15.99% | **13.08%** | 34.36% | 18.91% | **16.31%** | 35.12% | 18.31% | **15.89%** | 38.14% | 15.92% | **13.71%** |
    | 大批量板 (large-batch boards, >50 m²) | 14.21% | 6.21% | **3.17%** | 16.94% | 10.47% | **7.00%** | 22.01% | 14.95% | **12.05%** | 22.46% | 15.39% | **12.83%** |
    | PCB 产品 (PCB products, total) | 100.00% | 30.06% | **28.22%** | 100.00% | 30.50% | **28.63%** | 100.00% | 28.69% | **26.87%** | 100.00% | 27.14% | **25.42%** |

  - **The issuer states the conclusion in its own words, under prospectus liability.** Immediately
    under the table: "样板具有单笔订单面积小、品种多、快速交付等特点，对样板企业生产组织的管理复杂程度及柔性化生产能力提出了较高的要求。样板产品单次采购的产品数量和面积较少，客户对单价的敏感性相对较低，样板产品的生产和交货特性，均要求 PCB 生产企业从前端销售、工程服务、生产流程等各个环节针对客户的个性化需求进行优化调整，样板生产企业对客户的议价能力相对较强。此外，样板产品中层数较高的高附加值产品收入占比提升。上述因素综合使得样板产品的毛利率远高于小批量板和大批量板产品，具有合理性。"
    — "Sample boards are characterised by a small area per order, a large number of varieties and
    rapid delivery, which place high demands on the management complexity of a sample-board
    company's production organisation and on its flexible-manufacturing capability. Because the
    quantity and the area purchased at one time are small for sample-board products, **customers are
    relatively insensitive to unit price**; the production and delivery characteristics of
    sample-board products require a PCB manufacturer to optimise and adjust every link — front-end
    sales, engineering services, production flow — to the customer's individual requirements, and
    **a sample-board manufacturer's bargaining power over its customers is relatively strong**. In
    addition, the revenue share of high-value-added products with more layers within sample-board
    products has risen. The above factors taken together make **the gross margin of sample-board
    products far higher than that of small-batch and large-batch board products, which is
    reasonable**." (Our translation; emphasis ours.)
  - **The business section prints the same claim as a structural comparison, not an accident of one
    year.** PDF pp. 79–80, a three-column table 项目 / 样板 / 小批量板 / 大批量板 ("item / sample
    boards / small-batch boards / large-batch boards"), rows transcribed and translated:

    | 项目 (item) | 样板 (sample) | 小批量板 (small batch) | 大批量板 (large batch) |
    |---|---|---|---|
    | 订单面积 (order area) | 每单 5 平方米以下 (under 5 m² per order) | 5-50 平方米 (5–50 m²) | 50 平方米以上 (over 50 m²) |
    | 客户管理 (customer management) | 客户数量众多且分散、行业跨度较大、对快速响应要求高，一般要求企业的销售、工程师、计划人员技术素质要求较高，需提供 7×24 小时服务 — "customers are numerous and dispersed, span a wide range of industries and demand rapid response; the company's sales, engineering and planning staff are generally required to be of high technical calibre, and 7×24-hour service must be provided" (the filing gives this one cell across the sample and small-batch columns) | *(same cell)* | 客户集中度高，一般不要求快速响应、对成本较为敏感 — "customer concentration is high; rapid response is generally not required; relatively cost-sensitive" |
    | 客户需求 (customer requirement) | 研究、开发和试验阶段的专业需求 — "professional needs at the research, development and trial stage" | 专业用户应用市场为主 — "mainly the professional-user application market" | 普通用户应用市场为主 — "mainly the ordinary-user application market" |
    | 议价能力 (bargaining power) | PCB 厂商议价能力高 — "**the PCB maker's bargaining power is high**" | PCB 厂商议价能力较高 — "the PCB maker's bargaining power is relatively high" | PCB 厂商议价能力一般 — "the PCB maker's bargaining power is average" |

  - **Revenue, volume, price and order count, all four cut by order area.** PDF pp. 267–268 and
    274–275. Amounts in 万元 (CNY 10,000) as printed:

    | Item | 2024 H1 | FY2023 | FY2022 | FY2021 |
    |---|---|---|---|---|
    | 样板 revenue (sample, 万元) | 19,399.38 | 33,280.82 | 30,099.22 | 27,195.46 |
    | 其中：1m² 以下样板 ("of which: sample boards under 1 m²") | 12,229.89 | 20,289.39 | 17,693.69 | 15,346.21 |
    | 小批量板 revenue (small batch, 万元) | 12,277.65 | 23,482.62 | 24,654.96 | 26,328.51 |
    | 大批量板 revenue (large batch, 万元) | 5,246.36 | 11,579.90 | 15,448.24 | 15,504.06 |
    | 合计 (total, 万元) | 36,923.39 | 68,343.34 | 70,202.42 | 69,028.03 |
    | 样板 销售均价 (sample average price, CNY/m²) | 4,005.88 | 3,774.64 | 3,525.22 | 3,033.81 |
    | 小批量板 销售均价 (CNY/m²) | 1,204.35 | 1,163.63 | 1,194.92 | 1,090.22 |
    | 大批量板 销售均价 (CNY/m²) | 877.99 | 859.23 | 965.79 | 937.85 |
    | 样板 订单数量 (sample order count, 万笔 = 10,000 orders) | 7.08 | 12.35 | 11.28 | 10.86 |
    | 小批量板 订单数量 (万笔) | 0.75 | 1.49 | 1.56 | 1.77 |
    | 大批量板 订单数量 (万笔) | 0.07 | 0.12 | 0.15 | 0.16 |
    | 样板 平均面积 (sample average area, m²/order) | 0.68 | 0.71 | 0.76 | 0.83 |
    | 小批量板 平均面积 (m²/order) | 13.53 | 13.58 | 13.24 | 13.68 |
    | 大批量板 平均面积 (m²/order) | 90.40 | 108.86 | 109.71 | 100.80 |

    And in the issuer's own words (PDF p.275): "报告期内，公司以样板和小批量板销售为主，如上表所示，发行人每年的销售订单数量呈逐年上升趋势，2023 年度已接近 14 万余笔，其中样板和小批量订单占总订单数量的比重分别为 88%左右和 11%左右，大批量板订单数量仅占 1%左右。"
    — "During the reporting period the Company's sales are mainly sample boards and small-batch
    boards. As the table above shows, the issuer's annual sales order count has risen year by year
    and approached more than 140,000 orders in FY2023, of which sample-board and small-batch orders
    are about 88% and about 11% of the total order count respectively, while large-batch board
    orders are only about 1%." (Our translation.)
  - **Two factories, split by segment, and the company says why.** PDF p.268:
    "深圳强达专注于生产各类样板和特殊复杂产品，江西强达则主要定位于小批量板以快速响应客户对新产品从样板开发到最终定型批量生产的需求，另外会选择性地承接一些大批量板订单。"
    — "Shenzhen Qiangda concentrates on producing sample boards of every kind and special, complex
    products, while Jiangxi Qiangda is positioned mainly on small-batch boards, so as to respond
    quickly to customers' need to take a new product from sample development through to final
    settled batch production; it also selectively takes on some large-batch board orders." (Our
    translation.) Earlier on the same page the filing describes what the second plant fixed:
    "江西强达的投产和产量的释放，不仅解决了公司原有样板和批量板混线生产的问题、提升了生产效率" — "the commissioning of Jiangxi
    Qiangda and the release of its output not only solved the Company's previous problem of running
    sample boards and batch boards mixed on one line, and raised production efficiency…" (Our
    translation.)
  - **Turning work away, explicitly.** PDF p.162, explaining capacity utilisation of 93.94%,
    84.76%, 83.97% and 86.38% across the four periods:
    "同时，随着 PCB 市场需求减缓、公司持续优化产品结构，公司放弃了部分批量板订单" — "at the same
    time, as PCB market demand slowed and the Company continued to optimise its product mix, the
    Company **gave up some batch-board orders**" (our translation); and for 2023,
    "公司受 PCB 市场需求疲软，大批量板市场竞争尤为激烈的影响" — "the Company was affected by weak
    PCB market demand and by **particularly fierce competition in the large-batch board market**"
    (our translation). Capacity over the four periods was 51.71 / 52.67 / 50.69 / 24.78 万平方米
    (517,100 / 526,700 / 506,900 / 247,800 m²).
- **DERIVED (arithmetic written out):** all of this is computed by
  `tmp/qiangda_check.py` (a throwaway script, not committed; the arithmetic is reproduced here in
  full so a reader can redo it without the script). Three independent reconstructions of the
  filing's own printed totals all succeed, which is the transcription check.
  - **Check A — the revenue shares reproduce.** FY2023: 33,280.82 + 23,482.62 + 11,579.90 =
    68,343.34万元, exactly the printed total; 33,280.82 ÷ 68,343.34 = 48.696% against the printed
    **48.70%**; 23,482.62 ÷ 68,343.34 = 34.360% against **34.36%**; 11,579.90 ÷ 68,343.34 = 16.944%
    against **16.94%**. All twelve share cells across the four periods reproduce to within
    0.005 pp.
  - **Check B — the segment margins reproduce the blended PCB margin.** Gross profit per segment =
    revenue × margin (including freight). FY2023: 33,280.82 × 44.86% = 14,929.78; 23,482.62 ×
    16.31% = 3,830.02; 11,579.90 × 7.00% = 810.59; total 19,570.38万元; 19,570.38 ÷ 68,343.34 =
    **28.64%** against the printed PCB total of **28.63%** (0.005 pp of rounding). 2024 H1:
    8,646.30 + 1,605.92 + 166.31 = 10,418.53; ÷ 36,923.39 = **28.22%** against printed **28.22%**.
    FY2022 gives 26.87% against 26.87%; FY2021 gives 25.42% against 25.42%. **The two tables, on
    pages 22 apart, are mutually consistent to the last printed digit.**
  - **Check C — share of gross profit by segment**, the decomposition that matters:

    | Period | 样板 (sample) | 小批量板 (small batch) | 大批量板 (large batch) | **样板 + 小批量板** |
    |---|---|---|---|---|
    | FY2021 | 68.09% | 20.57% | 11.34% | **88.66%** |
    | FY2022 | 69.36% | 20.77% | 9.87% | **90.13%** |
    | FY2023 | 76.29% | 19.57% | 4.14% | **95.86%** |
    | 2024 H1 | 82.99% | 15.41% | 1.60% | **98.40%** |

    FY2023 worked: 14,929.78 ÷ 19,570.38 = 76.29%; 3,830.02 ÷ 19,570.38 = 19.57%; 810.59 ÷
    19,570.38 = 4.14%.
  - **The JLC-shaped two-way split.** Collapsing Qiangda's three tiers to the two JLC uses
    (sample + small batch against large batch):

    | Period | tail revenue | tail share of PCB revenue | tail gross margin | large-batch gross margin | **tail share of gross profit** |
    |---|---|---|---|---|---|
    | FY2021 | 53,523.97万元 | 77.54% | 29.06% | 12.83% | **88.66%** |
    | FY2022 | 54,754.18万元 | 77.99% | 31.05% | 12.05% | **90.13%** |
    | FY2023 | 56,763.44万元 | 83.06% | 33.05% | 7.00% | **95.86%** |
    | 2024 H1 | 31,677.03万元 | 85.79% | 32.36% | 3.17% | **98.40%** |
    | *JLC, FY2025 (SMB-1)* | *—* | *75.57%* | *36.24%* | *2.76%* | ***97.60%*** |

    JLC's own figure recomputed for comparability: (75.57 × 36.24) ÷ (75.57 × 36.24 + 24.43 × 2.76)
    = 2,738.6568 ÷ (2,738.6568 + 67.4268) = **97.60%**. Qiangda's 2024 H1 figure of 98.40% is
    arrived at from a completely independent filing by a completely different company, and lands
    within 0.8 pp of it.
  - **Price premium on a small order.** FY2023: 3,774.64 ÷ 859.23 = **4.39×** per square metre.
    2024 H1: 4,005.88 ÷ 877.99 = **4.56×**. FY2022: 3.65×. FY2021: 3.24×. The premium widened in
    every period.
  - **Margin ratio, sample to large batch.** FY2021 43.93 ÷ 12.83 = 3.42×; FY2022 3.61×; FY2023
    44.86 ÷ 7.00 = 6.41×; 2024 H1 44.57 ÷ 3.17 = **14.06×**. JLC's FY2025 equivalent is 36.24 ÷
    2.76 = 13.13×. The two companies' most recent periods are within one point of each other.
  - **Average order value, computed from revenue ÷ order count.** FY2023: sample 33,280.82万元 ÷
    123,500 orders = **CNY 2,695 per order**; small batch 23,482.62万元 ÷ 14,900 = CNY 15,760;
    large batch 11,579.90万元 ÷ 1,200 = CNY 96,499. Total orders FY2023 = 139,600, of which sample
    88.47%, small batch 10.67%, large batch 0.86% — reproducing the filing's own "about 88% / about
    11% / only about 1%".
  - **Gross profit per order.** FY2023: sample 14,929.78万元 ÷ 123,500 = CNY 1,209 of gross profit
    per sample order; large batch 810.59万元 ÷ 1,200 = CNY 6,755 per large-batch order. A
    large-batch order is worth 5.6× as much gross profit as a sample order and there are 103 times
    fewer of them, which is the whole argument in one line.
- **Bears on:**
  - **H6 (supports, strongly).** This is the second instance the file was looking for, and it is
    not a weaker one. Against JLC's single year and two tiers, Qiangda prints **four periods and
    three tiers**, with the threshold stated in square metres, on two named factories, cross-checked
    against its own revenue, volume, price and order-count tables. The direction is identical, the
    magnitude is comparable, and the tail's share of gross profit lands at 95.86% and 98.40% in the
    two most recent periods against JLC's 97.60%.
  - **H6 (supports, on the mechanism).** Qiangda does not merely report the margin gap, it explains
    it in the same terms the repository uses: the small-order customer is **price-insensitive**
    ("客户对单价的敏感性相对较低") and the maker's **bargaining power is high** ("PCB 厂商议价能力高"),
    while the large-batch customer is **cost-sensitive and concentrated** ("客户集中度高…对成本较为敏感").
  - **H7 (supports).** The bargaining-power row of the p.79 table is an issuer's own statement,
    made in a prospectus, that concentration and cost sensitivity travel together and that a
    dispersed customer base is where the pricing power is.
  - **H6 (context, and it cuts against a naive reading).** Qiangda has only ~3,000 active customers
    (PCB-1, PCB-5) and about 140,000 orders a year, against JLC's 1.36 million users and 21 million
    orders — a factor of 150 on orders. It still gets the same shape of result. **The margin
    structure therefore does not require internet scale.** What it requires, on this evidence, is a
    small order.
  - **The capital argument (supports, directionally).** The company's own explanation of falling
    utilisation is that it *gave up batch orders* and that the large-batch market is where
    competition is "particularly fierce", while its capacity fell from 517,100 m² to 506,900 m²
    across FY2021–FY2023 and its sample revenue rose 22%. That is the JLC impairment story (PCB-2)
    told from the other side: the tail is what justifies keeping the plant.
- **Used in:** not yet.
- **Caveats:**
  - **These are gross margins, not contribution or net margins.** Nothing here allocates SG&A, and
    a business of 140,000 small orders plainly costs more to sell and to plan than 1,200 large
    ones. The prospectus does not allocate operating expense by segment and neither do we. **The
    97.6%/98.4% figures are shares of *gross* profit and must never be described as shares of
    profit.**
  - **"Order area" is a proxy for order size, not a price band.** A 4.9 m² order of an exotic
    twenty-layer board and a 4.9 m² order of a two-layer board sit in the same bucket. The filing
    itself says the sample tier's margin is partly driven by layer-count mix
    ("样板产品中层数较高的高附加值产品收入占比提升"), so the order-size effect and the product-mix
    effect are **not separated** in this table. This is a real confound and it is the main reason
    this entry does not settle the question on its own.
  - **Qiangda is a declared sample/small-batch specialist**, not a company that happens to have
    both. It chose this mix and optimised for it, so this is not a clean natural experiment either;
    it is the same *kind* of evidence as JLC's, from a company with the same *kind* of strategy.
    The unbiased test would be a big-batch house that also runs a sample line, and PCB-4 established
    that the best such candidate (Fastprint) does not publish the split.
  - **The disclosure exists because of a listing review, again.** This is an IPO prospectus, not an
    annual report. Qiangda's subsequent annual reports (PCB-5) carry no such table. The finding of
    PCB-4 — that Chinese listing rules mandate splits by industry, product, region and channel but
    **not** by order size — survives; what has changed is that we now know exchanges ask for the
    order-size cut often enough that more than one company has printed it.
  - Two smaller cross-checks were not possible: the prospectus gives no cost-by-segment table, so
    the gross-profit decomposition above is reconstructed from revenue × margin rather than read
    directly, and the reconstruction's only validation is that it reproduces the printed blended
    margin (Check B). It does, in all four periods.
  - All translations are ours; the Chinese is quoted exactly so a reader can check them.

### PCB-8. Jinbaize's IPO prospectus does the same thing three years earlier — margin by order area for 2018–2020, plus the one disclosure nobody else makes: **customer concentration by order size, inside one company**, rising from 28.50% to 52.25% as orders get bigger

- **Source:** 深圳市金百泽电子科技股份有限公司 (Shenzhen Jinbaize Electronic Technology Co., Ltd.,
  SZSE ChiNext **301041**), 首次公开发行股票并在创业板上市招股说明书 ("Prospectus for the initial
  public offering of shares and listing on the ChiNext board"), filed 2021-08-04, via cninfo:
  <http://static.cninfo.com.cn/finalpage/2021-08-04/1210652347.PDF>
  Passages below are on PDF p.121 (doc p.1-1-120, the segment definition), pp.181–182
  (1-1-180/181, revenue and concentration by segment), pp.418–420 (1-1-417/419, revenue, area,
  price and margin by order area for 2018–2019, and the abandoned orders) and **p.482 (1-1-481,
  the gross-margin table)**.
- **Verification:** Verified 2026-09-25. Downloaded from cninfo (HTTP 200, 8,254,605 bytes,
  654 pages), text extracted with `pypdf`, every figure read in place. Three independent
  transcription checks all reproduce the filing's own printed totals — see DERIVED. Reporting
  period is FY2018, FY2019, FY2020.
- **What it says:**
  - **Same definition, three tiers, different thresholds from Qiangda's.** PDF p.121, in a table
    headed 区别 / PCB 样板 / 小批量板 / 中、大批量板 ("difference / PCB sample boards / small-batch
    boards / medium- and large-batch boards"), the row reads:
    "订单规模 每单 5 平方米以下 5-20 平方米 20 平方米以上"
    — "**order size**: under 5 m² per order / 5–20 m² / over 20 m²." (Our translation. Note the
    row label is 订单规模, literally "order size", not "order area".) The same table's customer row
    reads "客户需求 研究开发阶段 需求：快速、便捷 | 批量生产阶段 需求：成本优先"
    — "customer requirement: research and development stage, needs fast and convenient | volume
    production stage, needs cost first" (our translation), and its customer-management row:
    "客户数量较多、行业跨度大、要求复杂…需要高效的客户管理制度 | 客户集中度高，销售服务较为单纯"
    — "customers are numerous, span a wide range of industries, and their requirements are complex…
    an efficient customer-management system is needed | customer concentration is high, sales
    service is comparatively simple" (our translation).
  - **The gross-margin table** (PDF p.482), under the heading
    "（1）PCB 制造业务毛利率分析 / 1）订单面积维度的分析" — "(1) Analysis of the PCB manufacturing
    business's gross margin / 1) **Analysis on the order-area dimension**" (our translation).
    Column headers 收入占比 / 毛利率 — "share of revenue / gross margin":

    | 产品结构 (product structure) | 2020 年 share | 2020 GM | 2019 年度 share | 2019 GM | 2018 年度 share | 2018 GM |
    |---|---|---|---|---|---|---|
    | 样板 (sample boards, <5 m²/order) | 53.30% | **39.60%** | 55.60% | **36.06%** | 49.52% | **34.33%** |
    | 小批量 (small batch, 5–20 m²) | 27.14% | **20.96%** | 27.72% | **25.55%** | 25.63% | **25.01%** |
    | 中批量 (medium batch, >20 m²) | 19.57% | **18.21%** | 16.69% | **20.37%** | 24.85% | **18.42%** |
    | 总计 (total) | 100.00% | **30.35%** | 100.00% | **30.53%** | 100.00% | **27.99%** |

  - **The issuer's explanation, again in bargaining-power terms.** PDF p.483:
    "报告期内公司的 PCB 订单在 10 万笔左右，90%以上的订单都是样板订单，但样板订单的面积较小，故整体收入占比仍在 50%-60%左右。由于 PCB 样板的小批量、多订单、多品种的特点，制造难度较批量板显著提高，公司议价能力较高，故毛利率显著高于小批量板和中批量板。"
    — "During the reporting period the Company's PCB orders numbered around 100,000 a year, and over
    90% of the orders were sample-board orders, but because sample-board orders are small in area,
    their share of total revenue is still only about 50–60%. Because of the small-batch,
    many-order, many-variety characteristics of PCB sample boards, the manufacturing difficulty is
    significantly higher than for batch boards and **the Company's bargaining power is relatively
    high, so the gross margin is significantly higher than that of small-batch boards and
    medium-batch boards**." (Our translation; emphasis ours.)
  - **Revenue, area, price and margin by order area, 2018 and 2019** (PDF p.418), under the heading
    "①发行人放弃批量板订单的具体情况" — "(1) The specifics of the issuer giving up batch-board
    orders". Units as printed: 万元 / 平方米 / 元每平方米.

    | 分类 (class) | 销售收入 (revenue, 万元) | 总面积 (total area, m²) | 平均单价 (average unit price, CNY/m²) | 毛利率 (gross margin) |
    |---|---|---|---|---|
    | 中批量板 (medium batch) 2019 | 6,222.86 | 58,097.04 | 1,071.12 | 20.37% |
    | 中批量板 2018 | 10,502.18 | 101,858.00 | 1,031.06 | 18.42% |
    | 小批量板 (small batch) 2019 | 10,336.81 | 70,119.75 | 1,474.17 | 25.55% |
    | 小批量板 2018 | 10,829.19 | 75,428.68 | 1,435.69 | 25.01% |
    | 样板 (sample) 2019 | 20,735.29 | 65,045.43 | 3,187.82 | 36.06% |
    | 样板 2018 | 20,926.46 | 66,592.88 | 3,142.45 | 34.33% |

  - **Named customers dropped, with each one's gross margin printed.** This is the most concrete
    thing in any of these filings. PDF pp.418–419, introduced by
    "PCB 批量生产是一种更成熟传统的制造服务，成本竞争剧烈。发行人放弃的批量板订单，主要因为客户采用价格竞争的采购策略，并无法充分体现发行人竞争优势，且毛利率低呈逐渐下降趋势。发行人在履行以上订单过程中，要承担较大的管理成本、资金成本、回款风险及质量风险，但是这类订单无法给发行人带来盈利。"
    — "PCB volume production is a more mature, traditional manufacturing service, and cost
    competition in it is fierce. The batch-board orders the issuer gave up were given up mainly
    because the customers used a price-competition purchasing strategy, which cannot properly
    express the issuer's competitive advantages, and because the gross margin is low and trending
    gradually down. In performing those orders the issuer had to bear considerable management cost,
    capital cost, collection risk and quality risk, but **orders of this kind cannot bring the
    issuer any profit**." (Our translation; emphasis ours.) The table (万元):

    | 客户 (customer) | 批量板收入 2019 (batch-board revenue) | 2018 | 减少额 (decrease) | 毛利率 2019 (GM) | 2018 |
    |---|---|---|---|---|---|
    | 深圳市世纪云芯科技有限公司 (Shenzhen Century Yunxin Technology) | – | 1,360.86 | 1,360.86 | – | **2.94%** |
    | 浙江亿邦通信科技有限公司 (Zhejiang Ebang Communication Technology) | – | 692.48 | 692.48 | – | **11.75%** |
    | 山东新北洋信息技术股份有限公司及其关联公司 (Shandong New Beiyang Information Technology and its affiliates) | 326.28 | 953.32 | 627.04 | 21.04% | 11.19% |
    | 合计 (total) | 326.28 | 3,006.65 | 2,680.38 | | |

    And the explanation: "发行人放弃了世纪云芯和亿邦通信两家比特币领域的订单和山东新北洋部分低毛利订单。世纪云芯和亿邦通信主要从事比特币行业，所需的 PCB 为比特币矿机所需的哈希板，产品单一且技术溢价较低，世纪云芯的毛利率仅 2.94%，亿邦通信的毛利率也仅有 11.75%，均明显低于其他订单。"
    — "The issuer gave up the orders of Century Yunxin and Ebang Communication, two companies in the
    bitcoin field, and part of Shandong New Beiyang's low-margin orders. Century Yunxin and Ebang
    Communication are mainly in the bitcoin industry; the PCBs they need are the hash boards
    required by bitcoin mining machines, a single product type with a low technology premium.
    **Century Yunxin's gross margin was only 2.94% and Ebang Communication's only 11.75%**, both
    clearly lower than other orders." (Our translation; emphasis ours.)
  - **Customer concentration by order size, within one company.** PDF p.182, introduced by
    "报告期内样板、小批量、中批量业务收入中各前 20 大客户及其收入占比情况如下"
    — "the share of revenue held by the top 20 customers within each of the sample-board,
    small-batch and medium-batch businesses during the reporting period is as follows" (our
    translation):

    | 类别 (class) | 2020 年 | 2019 年 | 2018 年 |
    |---|---|---|---|
    | 样板 (sample) | **28.50%** | 28.59% | 31.14% |
    | 小批量 (small batch) | 37.56% | 41.45% | 39.51% |
    | 中批量 (medium batch) | **52.25%** | 56.64% | 67.11% |

    followed by "体现了相比样板业务上的客户分散，在中小批量业务上大客户集中的趋势。"
    — "This reflects the trend that, compared with the dispersion of customers in the sample-board
    business, large customers are concentrated in the small- and medium-batch businesses." (Our
    translation.) **Nothing else in this file measures concentration and order size on the same
    customers, in the same company, in the same year.**
  - **Small-batch customers come from sample customers.** PDF p.181: 91.24% / 90.20% / 92.57% of
    small-batch *customers* and 98.01% / 98.23% / 98.76% of small-batch *revenue* came from
    sample-board customers in 2020 / 2019 / 2018; for medium batch, 88.12% / 87.29% / 93.75% of
    customers and 95.93% / 92.93% / 82.81% of revenue. The filing calls sample customers a
    "流量入口" — a "**traffic entrance**", the Chinese internet term for a funnel top (our
    translation).
  - **Segment-level capacity constraint.** PDF p.483: "公司服务 PCB 批量板的产能不足，往往选择委外加工的方式处理，整体毛利率较低且易受大客户影响。"
    — "The Company's capacity for serving PCB batch boards is insufficient, so it often chooses to
    subcontract them, which gives a lower overall gross margin and leaves it easily affected by
    large customers." (Our translation.) Self-produced margin was 30.90% / 31.50% / 31.84% against
    subcontracted 21.41% / 26.54% / 24.87% across 2018–2020 (PDF p.418).
- **DERIVED (arithmetic written out):** computed by `tmp/jinbaize_check.py` (throwaway, not
  committed); reproduced here.
  - **Check A — revenue shares reproduce.** FY2020: 21,823.44 + 11,112.80 + 8,012.01 =
    40,948.25万元 against the printed 40,948.26 (one 万元-cent of rounding); 21,823.44 ÷ 40,948.26 =
    53.295% against printed **53.30%**. All nine share cells reproduce to within 0.005 pp.
  - **Check B — segment margins reproduce the blended PCB margin.** FY2020: 21,823.44 × 39.60% =
    8,642.08; 11,112.80 × 20.96% = 2,329.24; 8,012.01 × 18.21% = 1,458.99; total 12,430.31万元;
    ÷ 40,948.26 = **30.36%** against printed **30.35%**. FY2019 gives 30.53% against 30.53%; FY2018
    gives 27.99% against 27.99%. The tables on pages 182 and 482 are mutually consistent.
  - **Check C — the printed unit prices are revenue ÷ area exactly.** FY2019 sample:
    20,735.29万元 × 10,000 ÷ 65,045.43 m² = CNY 3,187.82/m², the printed figure to the cent. All
    six price cells reproduce.
  - **Share of gross profit by segment:**

    | Year | 样板 (sample) | 小批量 (small) | 中批量 (medium) | **样板 + 小批量** |
    |---|---|---|---|---|
    | FY2018 | 60.74% | 22.90% | 16.36% | **83.64%** |
    | FY2019 | 65.67% | 23.20% | 11.13% | **88.87%** |
    | FY2020 | 69.52% | 18.74% | 11.74% | **88.26%** |

    FY2020 worked: 8,642.08 ÷ 12,430.31 = 69.52%.
  - **Price premium on a small order.** FY2019: 3,187.82 ÷ 1,071.12 = **2.98×**; FY2018:
    3,142.45 ÷ 1,031.06 = **3.05×**.
  - **Margin ratio, sample to medium batch.** FY2018 34.33 ÷ 18.42 = 1.86×; FY2019 1.77×; FY2020
    39.60 ÷ 18.21 = **2.17×**.
  - **Concentration rises monotonically with order size in all three years**, verified by script:
    28.50 < 37.56 < 52.25 (2020), 28.59 < 41.45 < 56.64 (2019), 31.14 < 39.51 < 67.11 (2018).
    Medium-batch top-20 concentration is 1.83× / 1.98× / 2.16× the sample-board figure.
  - **The dropped orders, in context.** The three named customers gave up 2,680.38万元 of
    batch-board revenue, which the filing itself puts at 62.64% of the fall in medium-batch revenue
    from 2018 to 2019. Medium-batch revenue fell 10,502.18 → 6,222.86 = 4,279.32万元;
    2,680.38 ÷ 4,279.32 = **62.63%**, reproducing the filing's 62.64%.
- **Bears on:**
  - **H6 (supports).** A third company, a third independent filing, the same direction. Sample
    boards out-earn medium batch by 1.77× to 2.17× on gross margin in every year disclosed, and
    the tail carries 83.64% to 88.87% of PCB gross profit.
  - **H6 (supports, and it is the weakest of the three magnitudes).** Jinbaize's gap is much
    smaller than JLC's (13.13×) or Qiangda's (14.06×). Its bottom tier is 中批量 (over 20 m²), not
    a true large-batch tier, and a lot of its batch work is subcontracted rather than run on its own
    plant. **This is a real instance of the pattern at a much more modest magnitude, and the file
    should not average the three as if they measured the same thing.**
  - **H7 (supports, and this is the strongest single piece of concentration evidence in the file).**
    Everything else here compares concentration *between* companies, where a hundred things differ.
    Jinbaize splits one company's own customer base by order size and finds the top-20 share
    roughly doubling from the small-order tier to the large-order tier, in all three years. That is
    a within-company measurement of exactly the claim H7 makes.
  - **H6 (supports, on the mechanism, with a named counter-example).** Century Yunxin, a bitcoin
    hash-board buyer, bought 1,360.86万元 of boards at **2.94% gross margin** and was dropped. A
    large, concentrated, price-competing customer is not merely less profitable here; the issuer
    states that such orders "cannot bring the issuer any profit" once management cost, capital cost,
    collection risk and quality risk are counted.
  - **H5 (context).** "Over 90% of orders were sample-board orders" but only 50–60% of revenue.
    The tail is overwhelming in *count* and merely dominant in *value* — the same shape as
    Qiangda's 88%/52.54% and JLC's 21 million orders at 75.57% of revenue.
- **Used in:** not yet.
- **Caveats:**
  - **This is 2018–2020 data, published in 2021.** It is the oldest of the three margin tables and
    predates the current PCB downturn. Jinbaize's blended PCB margin has since fallen from 30.35%
    (2020) to 21.17% (2025) (PCB-1), and nothing tells us how that fall is distributed across the
    tiers.
  - **The tiers are not the same tiers as Qiangda's or JLC's.** Jinbaize cuts at 5 and 20 m²,
    Qiangda at 5 and 50 m², JLC does not publish a threshold at all. Cross-company comparison of
    the *levels* is therefore unsafe; only the *direction* compares.
  - **Subcontracting confounds the bottom tier.** Jinbaize buys in a fifth to a third of its PCB
    output, concentrated in batch work, so its medium-batch margin is partly a trading margin and
    not a manufacturing one. Qiangda's and JLC's tiers are made in their own plants.
  - The concentration table is **top-20 share within each segment**, not a top-5 or an HHI, and the
    segments have very different customer counts (650 small-batch customers against 261 medium in
    2020), which mechanically pushes the smaller segment's top-20 share up. That effect is real and
    unquantified; it does not explain the whole 28.50% → 52.25% gap, but it is part of it.
  - All translations are ours; the Chinese is quoted exactly so a reader can check them.

### PCB-9. Chongda, then the sixth-largest domestic PCB maker, told the exchange in 2016 that the margin ranking sample > small batch > large batch is a *property of the industry* — and gave the mechanism: a sample house has to leave equipment idle, and charges for it

- **Source:** 深圳市崇达电路技术股份有限公司 (Shenzhen Chongda Circuit Technology Co., Ltd., now
  崇达技术股份有限公司, SZSE **002815**), 首次公开发行股票招股说明书 ("Prospectus for the initial
  public offering of shares"), filed 2016-09-21, via cninfo:
  <http://static.cninfo.com.cn/finalpage/2016-09-21/1202711273.PDF>
  Passages below are on PDF pp.31–32 (doc pp.30–31, the operating statistics), p.102 (101, the
  segment definitions), p.112 (111, price transmission), p.140 (139, order-count distribution),
  p.291 (290, revenue by order area), **pp.305–306 (304–305, the margin ranking and the peer
  classification)** and p.312 (311, selling expense).
- **Verification:** Verified 2026-09-25. Downloaded from cninfo (HTTP 200, 2,657,900 bytes,
  385 pages), text extracted with `pypdf`, figures read in place. Reporting period FY2013, FY2014,
  FY2015 and 2016 Q1.
- **What it says:**
  - **The ranking, stated as an industry property.** PDF p.305, under the heading
    "6、公司毛利率、净利率高于大批量板企业的原因 /（1）小批量板毛利率一般高于大批量板、低于样板"
    — "6. Why the Company's gross margin and net margin are higher than those of large-batch board
    companies / (1) A small-batch board's gross margin is generally higher than a large-batch
    board's and lower than a sample board's" (our translation):
    "PCB 企业按照客户订单面积和应用领域划分，可细分为样板企业、小批量板企业、大批量板企业，一般来说，样板毛利率最高、小批量板毛利率次之、大批量板毛利率稍低。"
    — "PCB companies, divided **by customer order area** and application field, can be subdivided
    into sample-board companies, small-batch-board companies and large-batch-board companies.
    Generally speaking, **the sample board's gross margin is the highest, the small-batch board's
    gross margin comes next, and the large-batch board's gross margin is somewhat lower**." (Our
    translation; emphasis ours.)
  - **The mechanism, and it is the capital argument in one sentence.** Same page:
    "由于样板要求的交货期限最短，一般为 10 天以内，样板企业需要空置部分设备满足客户交货要求，因此样板企业在报价时会额外加收制板费、工程费等费用，样板的议价能力较强，报价远高于批量板，因此毛利率最高。"
    — "Because the delivery time a sample board demands is the shortest, generally within 10 days,
    **a sample-board company needs to leave part of its equipment idle in order to meet customers'
    delivery requirements**, and therefore a sample-board company adds board-making fees,
    engineering fees and other charges when it quotes; the sample board's bargaining power is
    strong and its quoted price is far above a batch board's, so its gross margin is the highest."
    (Our translation; emphasis ours.)
  - **And the other side of it, on why large batch is the lowest.** Same page:
    "在与客户的议价过程中，大批量 PCB 生产企业出于整单利润总额的考虑，一般会适当降低部分毛利率。目前，国内大批量 PCB 生产企业数量较多，竞争最为激烈，也是影响大批量毛利率的重要因素。因此，大批量 PCB 行业毛利率在 PCB 细分行业最低。"
    — "In bargaining with customers, large-batch PCB producers, thinking about the total profit of
    the whole order, generally reduce part of the gross margin appropriately. At present there are
    many large-batch PCB producers domestically and competition among them is the fiercest, which is
    also an important factor affecting large-batch gross margin. Therefore **the large-batch PCB
    sub-industry's gross margin is the lowest of the PCB sub-industries**." (Our translation;
    emphasis ours.)
  - **A between-company version of the JLC table, for FY2013 and FY2014.** PDF p.306:
    "2013 年，同行业上市公司中的大批量板企业的 PCB 产品毛利率最低值为-0.02%（天津普林），最高值为 26.60%（伊顿电子），平均值为 18.04%；2014 年，同行业上市公司中的大批量板企业的 PCB 产品毛利率最低值为 5.02%（天津普林），最高值为 26.03%（伊顿电子），平均值为 17.35%。报告期内，PCB 细分行业的差异使公司 PCB 产品毛利率高于大批量板企业（较平均水平高 10 个百分点以上）"
    — "In 2013 the lowest PCB gross margin among the large-batch board companies in the listed peer
    group was −0.02% (天津普林 Tianjin Printronics), the highest 26.60% (依顿电子 Ellington
    Electronics), the mean **18.04%**; in 2014 the lowest was 5.02% (Tianjin Printronics), the
    highest 26.03% (Ellington), the mean **17.35%**. During the reporting period the differences
    between PCB sub-industries made the Company's PCB gross margin higher than the large-batch
    board companies' (**more than 10 percentage points above the average level**)." (Our
    translation; emphasis ours.) Chongda's own main-business gross margin over the same years is
    given on PDF p.307 as 36.08% (2014) and 34.93% (2015).
  - **The peer classification table** (PDF p.306), headed 公司名称 / 产品特点 — "company name /
    product characteristics", with the source note "数据来源：上市公司公开披露的财务报告及招股说明书"
    — "source: listed companies' publicly disclosed financial reports and prospectuses". Our
    translation of the classification in full:

    | 公司名称 (company) | Segment, as Chongda classifies it | Average order area, where given |
    |---|---|---|
    | 兴森科技 (Fastprint) | 样板 — sample boards | 均单面积 1-2 m² ("average order area 1–2 m²") |
    | 依顿电子 (Ellington) | 大批量板 — large batch | — |
    | 胜宏科技 (Victory Giant) | 大批量板 — large batch | — |
    | 博敏电子 (Bomin) | 大批量板 — large batch | — |
    | 天津普林 (Tianjin Printronics) | 样板、小批量、大批量均能生产 — "can produce sample, small-batch and large-batch alike" | — |
    | 沪电股份 (WUS) | 大批量板 — large batch; 客户较集中 ("customers fairly concentrated") | — |
    | 超声电子 (Ultrasonic Electronics, PCB business) | 大批量为主，兼顾小批量、样板 — "mainly large batch, also small batch and sample"; 客户较集中 | — |
    | 超华科技 (Chaohua, PCB business) | 大批量 — large batch | — |
    | 中京电子 (Zhongjing) | 大批量 — large batch | — |
    | 崇达技术 (Chongda, the issuer) | 小批量 — small batch; 国际高端市场为主，客户较分散 ("mainly the international high-end market, customers fairly dispersed") | 均单面积为 8 m² ("average order area 8 m²") |

  - **Chongda's own revenue split by order area** (PDF p.291), with the note
    "注：本公司大批量板指面积在 50m² 以上的订单。" — "Note: the Company's large-batch boards means
    orders of area above 50 m²." (Our translation.) Amounts 万元:

    | 订单面积 (order area) | 2016 Q1 | share | 2015 | share | 2014 | share | 2013 | share |
    |---|---|---|---|---|---|---|---|---|
    | 小批量板 (small batch, ≤50 m²) | 33,148.29 | 70.69% | 121,943.83 | 71.25% | 116,784.44 | 75.60% | 96,439.97 | 80.13% |
    | 大批量板 (large batch, >50 m²) | 13,744.46 | 29.31% | 49,201.01 | 28.75% | 37,692.89 | 24.40% | 23,911.66 | 19.87% |
    | 合计 (total) | 46,892.75 | 100.00% | 171,144.85 | 100.00% | 154,477.33 | 100.00% | 120,351.62 | 100.00% |

    **No margin split accompanies it.** Chongda discloses revenue by order area and stops there.
  - **Order-size statistics, and the order count by area band.** PDF pp.31–32:

    | 项目 (item) | 2016 Q1 | 2015 | 2014 | 2013 |
    |---|---|---|---|---|
    | 订单数量（个）(order count) | 39,656 | 143,681 | 129,853 | 117,041 |
    | 均单面积（平方米）(average order area, m²) | 8.14 | 7.81 | 7.56 | 6.68 |
    | 交货期（天）(delivery time, days) | 13 | 13 | 13 | 14 |
    | 平均日处理订单数（个）(average orders processed per day) | 436 | 394 | 356 | 321 |
    | 平均单个订单金额（万元）(average order value, 万元) | 1.18 | 1.19 | 1.19 | 1.03 |
    | 客户数量（个）(customer count) | 800 | 938 | 768 | 632 |

    and (PDF p.140) "报告期内，本公司单个订单面积在 50 平方米以下的订单数量分别为 114,938 个、126,975 个、139,989 个和 38,539 个，分别占公司订单总数的 98.20%、97.78%、97.43%和 97.18%。"
    — "During the reporting period the number of the Company's orders with a single-order area under
    50 square metres was 114,938, 126,975, 139,989 and 38,539, being 98.20%, 97.78%, 97.43% and
    97.18% of total orders respectively." (Our translation.)
  - **The honest counterweight, which this file needs and did not have: small orders cost more to
    sell.** PDF p.312, on selling expense as a share of revenue:
    "本公司小批量板每个订单的均单面积较小、订单数量较多，物流以快递为主，物流费用较高；同时，本公司销售人员也相应较多，销售人员工资薪酬占比高于同行业水平。与小批量板相比，大批量板销售费用相对较低，样板销售费用相对较高。"
    — "The Company's small-batch boards have a small average area per order and a large number of
    orders; logistics is mainly by courier, so logistics cost is high; at the same time the Company
    has correspondingly more sales staff, and sales-staff pay is a higher share than the industry
    level. **Compared with small-batch boards, large-batch boards' selling expense is relatively
    low and sample boards' selling expense is relatively high.**" (Our translation; emphasis ours.)
    The printed ratios of selling expense to revenue over 2013–2016 Q1: 兴森科技 Fastprint (sample)
    7.09% / 6.62% / 6.99% / 7.25%; 崇达技术 Chongda (small batch) 4.09% / 3.99% / 4.18% / 4.20%;
    the peer mean (mostly large batch) 3.07% / 3.07% / 3.20% / 3.37%.
  - **Price transmission.** PDF p.112: "小批量板厂商由于客户数量多，均单面积小，客户对交期要求严格，因此卖方具有一定议价能力，通常可以将部分原材料价格上涨等因素向下游传导。与大批量板厂商相比，小批量板厂商受宏观经济周期波动以及原材料价格波动等因素影响相对较小。"
    — "Because small-batch board makers have many customers, a small average order area and
    customers with strict delivery requirements, the seller has a degree of bargaining power and can
    usually pass part of raw-material price rises and similar factors downstream. Compared with
    large-batch board makers, small-batch board makers are relatively less affected by macroeconomic
    cycles and raw-material price swings." (Our translation.)
- **DERIVED (arithmetic written out):**
  - **Average order value from the filing's own two figures.** FY2015: 171,144.85万元 ÷ 143,681
    orders = CNY 11,912 per order against the printed 平均单个订单金额 of 1.19万元 = CNY 11,900.
    Reproduces. FY2013: 120,351.62万元 ÷ 117,041 = CNY 10,283 against printed 1.03万元 = CNY 10,300.
  - **The "10 percentage points" claim checks out.** FY2014: Chongda's main-business margin 36.08%
    minus the large-batch peer mean 17.35% = **18.73 pp**, comfortably over the "10 个百分点以上"
    the filing claims. FY2013: the filing gives the 2013 peer mean as 18.04%; Chongda's 2013
    main-business margin is not quoted on that page, and we have not read it, so this year is
    **not** cross-checked.
  - **Selling-expense penalty for small orders.** Fastprint (sample) 7.09% against the large-batch
    peer mean 3.07% in FY2013 = **4.02 pp** of extra selling expense; Chongda (small batch) 4.09%
    − 3.07% = 1.02 pp. Against a gross-margin advantage the filing puts at over 10 pp, the selling
    expense penalty is real but does not come close to cancelling it — on these figures the sample
    house keeps roughly 6 pp of the 10 pp advantage after selling expense, and that is before
    engineering, planning and customer-service headcount that sits in administrative expense rather
    than selling expense. **This calculation is ours, it mixes two companies' figures with a peer
    mean, and it should be treated as an order-of-magnitude sanity check, not a result.**
- **Bears on:**
  - **H6 (supports, at the level of an industry claim rather than a company's own numbers).** An
    issuer with 143,681 orders a year and CNY 1.7bn of revenue told a listing regulator, in a
    document carrying prospectus liability, that the margin ordering sample > small batch > large
    batch is a general property of the PCB industry, and gave a causal mechanism for it.
  - **The capital argument (supports, and this is the most useful sentence found in this pass).**
    "样板企业需要空置部分设备满足客户交货要求" — a sample-board company **must keep part of its
    equipment idle** to hold the delivery promise, and charges for it. That is precisely the
    trade foundry.api proposes: idle capacity is not waste in a quick-turn business, it is the
    product, and the price recovers it. It is also the reason the margin is high rather than a
    reason it should not be.
  - **H7 (supports).** Chongda's classification table puts "客户较集中" (customers fairly
    concentrated) beside every large-batch peer and "客户较分散" (customers fairly dispersed)
    beside itself, and the price-transmission passage says the dispersed seller can pass on input
    costs. Both are the issuer's own characterisation.
  - **H6 (challenges — the cost-to-serve counterweight).** Chongda states plainly that small orders
    cost more to sell, and that sample boards cost the most of all, and the printed expense ratios
    bear it out: 7.09–7.25% of revenue at the sample house against 3.07–3.37% at the large-batch
    peers. **Any use of the 97.6% or 98.4% gross-profit figures elsewhere in this repository must
    carry this alongside it.** The tail's advantage at the gross line is partly spent below it.
- **Used in:** not yet.
- **Caveats:**
  - **Chongda does not publish its own margin by order area** — only revenue. The margin ranking is
    an industry statement plus a between-company comparison, not a within-company table. It is
    weaker evidence than PCB-7 or PCB-8 and is recorded as a different *kind* of evidence.
  - **The data are from 2013–2016.** The Chinese PCB industry has changed a great deal since, and
    Chongda's own strategy changed with it: PCB-10 records Mingyang's 2018 prospectus noting that
    Chongda had by 2017 adopted a strategy of "守住小批量市场，开拓中大批量市场" — "hold the
    small-batch market, open up the medium- and large-batch market" (our translation), which is the
    opposite direction of travel from the one this file's thesis would predict, and which ended
    with Chongda at a 20.24% blended margin in 2023 (PCB-7's peer table).
  - The 2013 peer mean of 18.04% and the 2014 mean of 17.35% are **Chongda's** computations from
    other companies' reports, not ours, and we have not re-derived them from the underlying
    filings.
  - The selling-expense arithmetic under DERIVED is ours and is a rough comparison across
    companies. It is not a segment-level cost allocation and must not be quoted as one.
  - All translations are ours; the Chinese is quoted exactly so a reader can check them.

### PCB-10. A census of who actually discloses the order-size cut: seven listed Chinese PCB makers have printed revenue by order area, but only three have ever printed *margin* by order area — and one of the three is JLC

- **Sources:**
  - 强达电路 IPO prospectus (PCB-7), PDF pp.157–159 (doc pp.1-1-156/158): the table
    "（1）公司与同行业可比公司基本经营情况对比" — "(1) Comparison of the Company's and comparable
    companies' basic operating situation", which has a column headed
    "最近一年已披露的按订单面积分类收入占比" — "**the most recent year's disclosed share of revenue
    classified by order area**", with a per-company source note.
  - 深圳明阳电路科技股份有限公司 (Shenzhen Mingyang Circuit Technology Co., Ltd., SZSE **300739**),
    首次公开发行股票并在创业板上市招股说明书（更新后）("IPO prospectus, updated"), 2018-01-25:
    <http://static.cninfo.com.cn/finalpage/2018-01-25/1204362738.PDF> — PDF pp.115–116, 122, 146,
    316–317.
  - 崇达技术 IPO prospectus (PCB-9), PDF p.291.
  - 金百泽 IPO prospectus (PCB-8), PDF p.482.
- **Verification:** Verified 2026-09-25. The Qiangda and Chongda and Jinbaize documents are those
  verified in PCB-7, PCB-9 and PCB-8. The Mingyang prospectus was downloaded from cninfo
  (HTTP 200, 10,005,613 bytes, 379 pages) and read the same way. **This entry reports what each
  filing does and does not contain; where a company's disclosure is asserted only by Qiangda's
  table and has not been read in that company's own filing, the row says so and the status for that
  row is Partial.**
- **What it says:**
  - **Qiangda's peer table names seven companies' order-area revenue splits.** Transcribed from
    PDF pp.157–158, with the two relevant columns only (the full table also carries main business,
    application field, CPCA rank, PCB revenue, region split, margin and R&D intensity):

    | 公司简称 (company) | 样板 (sample) | 小批量板 (small batch) | 大/中批量板 (large/medium batch) | 2023 主营业务毛利率 (FY2023 main-business GM) |
    |---|---|---|---|---|
    | 中富电路 (Zhongfu Circuit) | 1.50% | 36.71% | 61.79% | 13.13% |
    | 金百泽 (Jinbaize) | 48.91% | 26.09% | 25.00% | 27.19% |
    | 本川智能 (Benchuan Intelligent) | 21.62% | 38.55% | 39.83% | 11.60% |
    | 迅捷兴 (Xunjiexing) | 30.13% | 36.82% | 33.05% | 15.14% |
    | 四会富仕 (Sihui Fushi) | 未披露 (not disclosed) | 未披露 | 未披露 | 24.55% |
    | 明阳电路 (Mingyang) | 未披露 | 未披露 | 未披露 | 21.70% |
    | 崇达技术 (Chongda) | 未披露 | 未披露 | 52.83% | 20.24% |
    | 兴森科技 (Fastprint) | 46.96% | 48.94% | – | 28.72% |
    | 公司 (Qiangda, the issuer) | 42.87% | 35.12% | 22.01% | 28.74% |

    with the crucial note 2: "最近一年已披露的按订单面积分类收入占比，公司、崇达技术和金百泽为 2021 年数据，中富电路、本川智能、迅捷兴为 2020 年数据，兴森科技为 2015 年数据，四会富仕、明阳电路未披露，同行业可比公司未披露 2022 年按订单面积分类的收入占比。"
    — "For the most recent year's disclosed share of revenue classified by order area: the Company,
    Chongda and Jinbaize are 2021 data; Zhongfu, Benchuan and Xunjiexing are 2020 data; Fastprint is
    **2015** data; Sihui Fushi and Mingyang have not disclosed it; **the comparable companies in the
    same industry did not disclose the order-area revenue split for 2022**." (Our translation;
    emphasis ours.) And note 5: "金百泽按订单面积分类为样板、小批量板、中批量板，订单面积分别为 5 平方米以下、5-20 平方米、20-50 平方米等。"
    — "Jinbaize classifies by order area into sample boards, small-batch boards and medium-batch
    boards, with order areas of under 5 m², 5–20 m² and 20–50 m² respectively." (Our translation.)
  - **So the practice is dying, not spreading.** Read as a time series, the note says the most
    recent order-area disclosure available in 2024 was 2021 for three companies, 2020 for three
    more, and **2015 for Fastprint**; and that *nobody* in the peer set published it for 2022. The
    order-size cut is a thing companies print **while they are being reviewed for a listing or a
    fundraising, and stop printing once they are listed.**
  - **Mingyang: the definition and the price-sensitivity claim, without the margin split.** Mingyang
    defines the same tiers (PDF p.115): "（4）按均单面积可分为样板、小批量板、大批量板" — "(4) By
    average order area, divided into sample boards, small-batch boards and large-batch boards";
    sample "订单面积一般不超过 5 平方米，平均在 1 平方米左右" — "order area generally not over 5 m²,
    averaging around 1 m²"; large batch "订单面积一般在 50 平方米以上" — "order area generally above
    50 m²". It discloses the revenue share of orders under 50 m² — 73.10% / 69.55% / 65.77% /
    60.21% across FY2014–2017 H1 — and average order area of 11.75 / 14.07 / 13.96 / 12.20 m², and
    **no margin split**. Its comparison table (PDF p.122) prints a row the others do not:

    | 项目 (item) | 小批量板 (small batch) | 大批量板 (large batch) |
    |---|---|---|
    | 客户价格敏感度 (customer price sensitivity) | 小批量产品数量多，均单面积小，且对产品特性要求高，客户更看重产品品质、交期、服务，**对价格较为不敏感** — "small-batch products are many in number with a small average order area and demand high product characteristics; customers care more about product quality, delivery time and service, and are **comparatively insensitive to price**" | 大批量板的订单数量少，均单面积大，客户看重采购成本，**对价格更为敏感** — "large-batch boards have few orders with a large average order area; customers care about procurement cost and are **more sensitive to price**" |

    (Our translations.) And on capacity, PDF p.146:
    "作为小批量板制造企业，保持适当的产能冗余有利于加快交货速度。"
    — "As a small-batch board manufacturer, **maintaining an appropriate degree of capacity
    redundancy is advantageous for speeding up delivery**." (Our translation.) That is Chongda's
    "leave equipment idle" point, from a different issuer two years later.
  - **Mingyang also records Chongda changing direction.** PDF p.317: "根据崇达技术 2017 年半年报，其'守住小批量市场，开拓中大批量市场'的发展战略"
    — "according to Chongda's 2017 half-year report, its development strategy of 'hold the
    small-batch market, open up the medium- and large-batch market'". (Our translation.)
- **DERIVED:** none beyond counting. **Of the nine companies in Qiangda's table, seven have at some
  point published revenue by order area (Zhongfu, Jinbaize, Benchuan, Xunjiexing, Chongda,
  Fastprint, Qiangda) and two have not (Sihui Fushi, Mingyang — though Mingyang publishes a
  ≤50 m² revenue share, which is the same cut at one threshold, so "two" is arguably one).
  Of those seven, exactly two have been found to publish *gross margin* by order area: Qiangda
  (PCB-7) and Jinbaize (PCB-8). Adding JLC, which is not in this table and which splits by batch
  size rather than by area, gives three.**
- **Bears on:**
  - **H6 (context, and it reframes the whole file).** The earlier verdict above treated JLC's table
    as near-unique. It is not: the *definition* by order area is an industry-standard classification
    used by at least nine listed Chinese PCB makers, printed with identical thresholds (5 m², 50 m²)
    in filings from 2016, 2018, 2021 and 2024 by four different issuers with four different
    sponsors. What is rare is the **margin** cut, not the **order-size** cut.
  - **H6 (challenges, on renewability).** Nobody published the order-area split for FY2022. The
    evidence base is a set of listing documents, not a running series, and it is not being renewed.
  - **The capital argument (supports).** Two separate issuers, eight years apart, independently
    state that a small-order business must hold spare capacity: Chongda's "需要空置部分设备"
    ("needs to leave part of its equipment idle") and Mingyang's "保持适当的产能冗余有利于加快交货速度"
    ("maintaining an appropriate degree of capacity redundancy is advantageous for speeding up
    delivery").
- **Used in:** not yet.
- **Caveats:**
  - **The rows for 中富电路 (Zhongfu), 本川智能 (Benchuan) and 兴森科技 (Fastprint) in the table
    above are Qiangda's rendering of those companies' disclosures and have NOT been read in the
    companies' own filings.** Those three rows are **Partial**. Zhongfu's and Benchuan's IPO
    prospectuses were not retrieved in this pass and Fastprint's 2015 disclosure was not located;
    see the blocked list.
  - Qiangda selected this comparable set and had an interest in a comparison that makes a
    sample/small-batch specialist look good, exactly as PCB-1 noted of JLC's set. The overlap
    between the two chosen sets is itself informative: both issuers picked small-to-mid specialists
    and neither picked 深南电路 Shennan, 沪电股份 WUS, 景旺电子 Kinwong or 胜宏科技 Victory Giant.
  - Mingyang's figures are FY2014–2017 H1 and Chongda's FY2013–2016 Q1. Neither is current.
  - All translations are ours; the Chinese is quoted exactly so a reader can check them.

### PCB-11. The Shanghai exchange ordered Xunjiexing to break out margin by order size for FY2025, and it did — sample boards are 23.37% of revenue and **83.50% of gross profit**; revenue grew 42.47% while gross profit fell 15.37%, because the growth was all large batch

- **Source:** 深圳市迅捷兴科技股份有限公司 (Shenzhen Xunjiexing Technology Co., Ltd., SSE STAR
  Market **688655**), 关于对上海证券交易所 2025 年年度报告的信息披露监管问询函回复的公告
  ("Announcement on the reply to the Shanghai Stock Exchange's regulatory enquiry letter on the
  disclosure in the 2025 annual report"), 公告编号 2026-032, dated 2026-05-12, via cninfo:
  <http://static.cninfo.com.cn/finalpage/2026-05-12/1225292252.PDF>
  The enquiry letter it answers is 《关于深圳市迅捷兴科技股份有限公司 2025 年年度报告的信息披露监管问询函》（上证科创公函【2026】0114 号）
  — "Regulatory enquiry letter on the disclosure in the 2025 annual report of Shenzhen Xunjiexing
  Technology Co., Ltd." (document number left as printed). A separate 立信会计师事务所（特殊普通合伙）
  (BDO China Shu Lun Pan Certified Public Accountants LLP) verification opinion was filed the same
  day at `finalpage/2026-05-12/1225292253.PDF`; it was **not** downloaded (37 MB) and nothing here
  depends on it.
- **Verification:** Verified 2026-09-25. Downloaded from cninfo (HTTP 200, 407,033 bytes,
  50 pages), text extracted with `pypdf`. **This document gives revenue *and cost* per segment, so
  the gross-profit decomposition is read directly rather than reconstructed** — and every printed
  margin, share and total reproduces from the revenue and cost figures exactly, to the last printed
  digit, in both years (see DERIVED).
- **What it says:**
  - **This is the review-enquiry mechanism working exactly as the earlier verdict in this file
    guessed it might.** The exchange's question, quoted from PDF p.1:
    "（2）**区分样板、小批量板和大批量板，补充说明相关收入、成本、毛利率、营收占比及变动情况**，结合不同业务模式，分析公司营业收入增长与技术人员变动趋势不一致的原因；"
    — "(2) **Distinguishing sample boards, small-batch boards and large-batch boards,
    supplementarily explain the relevant revenue, cost, gross margin, share of revenue, and their
    changes**; and, in the light of the different business models, analyse why the Company's revenue
    growth and the trend in its technical headcount are inconsistent." (Our translation; emphasis
    ours.) A stock exchange asked a listed PCB company to print the margin split by order size, and
    it printed it. That is the same causal route that produced JLC's p.245 table and Qiangda's
    p.289 table, but here it happened to a company that was **already listed**, against an annual
    report, which the earlier verdict in this file did not think was available.
  - **The table** (PDF p.7), headed "(一) 区分样板、小批量板和大批量板，补充说明相关收入、成本、毛利率、营收占比及变动情况" —
    "(1) Distinguishing sample boards, small-batch boards and large-batch boards, supplementary
    explanation of the relevant revenue, cost, gross margin, share of revenue and their changes".
    Amounts 万元:

    | 项目 (item) | 2025 收入 (revenue) | 收入占比 (share) | 成本 (cost) | 毛利率 (GM) | 2024 收入 | 收入占比 | 成本 | 毛利率 | 收入变动 (rev. change) | 毛利率变动 (GM change) |
    |---|---|---|---|---|---|---|---|---|---|---|
    | 样板 (sample boards) | 15,065.76 | 23.37% | 10,482.37 | **30.42%** | 12,994.88 | 28.72% | 8,173.85 | **37.10%** | +15.94% | −6.68 pp |
    | 小批量板 (small-batch boards) | 25,043.60 | 38.85% | 24,382.09 | **2.64%** | 18,565.71 | 41.03% | 17,339.27 | **6.61%** | +34.89% | −3.97 pp |
    | 大批量板 (large-batch boards) | 24,351.51 | 37.78% | 24,107.28 | **1.00%** | 13,685.70 | 30.25% | 13,247.30 | **3.20%** | +77.93% | −2.20 pp |
    | 合计 (total) | 64,460.87 | 100.00% | 58,971.74 | **8.52%** | 45,246.29 | 100.00% | 38,760.42 | **14.33%** | +42.47% | −5.81 pp |

    with the company's explanation: "报告期公司主营业务收入增长 42.47%，主要源自大批量板收入增加，增幅达 77.93%。大批量板销售增加主要系公司提供从样板向批量板生产一站式服务模式延伸，样板及小批量板客户产品定型后的批量生产需求增加，同时信丰厂大批量板产能顺利爬升，扩大市场接单能力"
    — "In the reporting period the Company's main-business revenue grew 42.47%, mainly from the
    increase in large-batch board revenue, which rose 77.93%. The increase in large-batch board
    sales was mainly because the Company extended its one-stop service model from sample boards
    through to batch production; demand for volume production rose after sample-board and
    small-batch-board customers' products were settled; and at the same time the Xinfeng plant's
    large-batch capacity ramped up smoothly, widening its capacity to take market orders." (Our
    translation.)
  - **Average selling price and unit cost, by segment** (PDF pp.7–9), in 元/㎡ (CNY per square
    metre). Each segment gets its own table with the cost broken into 直接材料 / 直接人工 /
    制造费用 / 其他 — "direct materials / direct labour / manufacturing overhead / other (processing
    and freight)":

    | | 样板 (sample) 2025 | 2024 | 小批量板 (small) 2025 | 2024 | 大批量板 (large) 2025 | 2024 |
    |---|---|---|---|---|---|---|
    | 销售均价 (average selling price, CNY/m²) | **1,619.17** | 1,808.96 | 890.63 | 903.05 | **658.86** | 651.32 |
    | 单位成本 (unit cost, CNY/m²) | 1,126.58 | 1,137.85 | 867.11 | 843.39 | 652.25 | 630.46 |
    | 其中 直接材料 (of which direct materials) | 560.06 | 560.93 | 485.77 | 431.50 | 381.41 | 346.17 |
    | 直接人工 (direct labour) | 195.90 | 193.76 | 99.60 | 106.06 | 74.41 | 70.13 |
    | 制造费用 (manufacturing overhead) | 301.34 | 302.11 | 246.67 | 271.29 | 174.46 | 195.04 |
    | 其他 (other: processing and freight) | 69.28 | 81.05 | 35.07 | 34.54 | 21.97 | 19.12 |
    | 毛利率 (gross margin) | 30.42% | 37.10% | 2.64% | 6.61% | 1.00% | 3.20% |

  - **"增收不增利"** (PDF p.2) — the company's own four-character summary, "revenue up but profit
    not up". The full sentence: "2025 年公司主营业务收入同比增长 42.47%，但整体毛利率由 14.33%下滑至 8.52%，呈现'增收不增利'特征。"
    — "In 2025 the Company's main-business revenue grew 42.47% year on year, but the overall gross
    margin slid from 14.33% to 8.52%, showing the characteristic of 'revenue up, profit not up'."
    (Our translation.) And the cause, same page: "①公司收入增长主要来源于**传统中低端市场批量订单**，使得公司销售价格较上年下降 6.62%"
    — "(1) The Company's revenue growth came mainly from **batch orders in the traditional
    mid- and low-end market**, so the Company's selling price fell 6.62% against the previous year."
    (Our translation; emphasis ours.) Reported net loss attributable to the parent for FY2025 is
    亏损 2,237.90万元 — a loss of CNY 22.379 million, "较去年同期增亏" ("a wider loss than the same
    period last year").
  - **Four named-but-anonymised customers, a third of revenue, at a negative gross margin**
    (PDF p.6). Introduced by "2025 年公司平均售价为 866.60 元，低于平均售价的订单主要客户情况如下"
    — "The Company's average selling price in 2025 was CNY 866.60 [per m²]; the main customers whose
    orders were below the average price are as follows" (our translation). Amounts 万元:

    | 序号 | 客户名称 (customer) | 2025 收入 | 2025 成本 | 2025 毛利率 | 2024 收入 | 2024 成本 | 2024 毛利率 |
    |---|---|---|---|---|---|---|---|
    | 1 | 客户C (Customer C) | 8,111.57 | 9,477.24 | **−16.84%** | 4,226.89 | 4,487.05 | −6.15% |
    | 2 | 客户A (Customer A) | 6,799.46 | 7,861.54 | **−15.62%** | 4,801.74 | 5,489.95 | −14.33% |
    | 3 | 客户F (Customer F) | 3,283.55 | 3,220.57 | 1.92% | 2,122.39 | 1,878.16 | 11.51% |
    | 4 | 客户J (Customer J) | 2,449.96 | 2,410.54 | 1.61% | 1,538.68 | 1,580.84 | −2.74% |
    | | 合计 (total) | 20,644.54 | 22,969.89 | **−11.26%** | 12,689.70 | 13,436.00 | −5.88% |

    "公司主要低价订单客户集中在安防领域。" — "The Company's main low-price-order customers are
    concentrated in the security/surveillance field." (Our translation.) The 安防 (security)
    application area is 24.76% of FY2025 revenue at a gross margin of **−14.33%** (PDF p.2), the
    worst of the eight application areas disclosed, and it grew 61.16%.
  - **Top-5 customer concentration, computed separately inside each order-size segment**
    (PDF pp.10–11). The reply lists each segment's five largest customers with the year the
    relationship started, registered capital and amount; the subtotals are:

    | | 样板 (sample) | 小批量板 (small batch) | 大批量板 (large batch) |
    |---|---|---|---|
    | 2025 top-5 share of that segment | **37.88%** | 42.22% | **45.54%** |
    | 2024 top-5 share of that segment | 40.97% | 40.36% | **51.75%** |

    The same three customers — 客户A, 客户B, 客户C — appear in the top five of all three segments,
    and 客户C alone is 16.53% of large-batch revenue in 2025.
  - **The layer-count cut, printed in the same document, for the same two years** (PDF p.5), which
    matters because it is the confound PCB-7's caveats flagged:

    | 项目 | 2025 收入 (万元) | 占比 | 毛利率 | 2024 收入 | 占比 | 毛利率 |
    |---|---|---|---|---|---|---|
    | 八层以上 (more than eight layers) | 13,447.93 | 20.86% | **29.86%** | 8,228.93 | 18.19% | **35.66%** |
    | 八层以下 (fewer than eight layers) | 51,012.94 | 79.14% | **2.89%** | 37,017.36 | 81.81% | **9.59%** |
    | 合计 | 64,460.87 | 100.00% | 8.52% | 45,246.29 | 100.00% | 14.33% |

  - **Capacity and the new plant** (PDF p.3): overall capacity utilisation **41.55%**; the Zhuhai
    plant, commissioned in 2025, earned a gross margin of **−44.45%** on revenue of 4,121.55万元
    against cost of 5,953.76万元; excluding Zhuhai the company's margin would have been 12.13%
    rather than 8.52%. New fixed cost at Zhuhai in 2025: 固定资产折旧 933.89万元 (fixed-asset
    depreciation) plus 间接生产人员薪酬 364.37万元 (indirect production staff pay) = 1,298.26万元.
  - **And it is opening an online shop** (PDF p.6): "为助力更多个性化样板订单导入，发挥样板批量化模式优势，公司 PCB 网上商城已于 2026 年 1 月上线，开启线上销售模式，尚处于推广阶段。"
    — "To help bring in more individual sample-board orders and bring out the advantage of the
    sample-board batching model, the Company's PCB online shop went live in January 2026, opening an
    online sales model; it is still at the promotion stage." (Our translation.) That updates PCB-3,
    which recorded the launch date.
- **DERIVED (arithmetic written out):** computed by `tmp/xjx_check.py` (throwaway, not committed).
  - **Check A — the printed table reproduces from revenue and cost, exactly.** FY2025:
    15,065.76 + 25,043.60 + 24,351.51 = 64,460.87万元, the printed total; 10,482.37 + 24,382.09 +
    24,107.28 = 58,971.74万元, the printed total cost; (15,065.76 − 10,482.37) ÷ 15,065.76 =
    **30.42%**, the printed sample margin; (24,351.51 − 24,107.28) ÷ 24,351.51 = **1.00%**, the
    printed large-batch margin; (64,460.87 − 58,971.74) ÷ 64,460.87 = **8.52%**, the printed
    blended margin. Every cell in both years reproduces. **Unlike PCB-7 and PCB-8, no
    reconstruction is needed: the cost column is printed.**
  - **Gross profit by segment, read directly:**

    | | 样板 (sample) | 小批量板 (small) | 大批量板 (large) | total |
    |---|---|---|---|---|
    | FY2025 gross profit (万元) | 4,583.39 | 661.51 | 244.23 | 5,489.13 |
    | FY2025 share of gross profit | **83.50%** | 12.05% | 4.45% | 100% |
    | FY2025 share of revenue | 23.37% | 38.85% | 37.78% | 100% |
    | FY2024 gross profit (万元) | 4,821.03 | 1,226.44 | 438.40 | 6,485.87 |
    | FY2024 share of gross profit | **74.33%** | 18.91% | 6.76% | 100% |
    | FY2024 share of revenue | 28.72% | 41.03% | 30.25% | 100% |

    样板 + 小批量板 = **95.55%** of gross profit in FY2025 and 93.24% in FY2024. Worked for 2025:
    4,583.39 ÷ 5,489.13 = 83.50%.
  - **The single most striking number in this pass.** Revenue 45,246.29 → 64,460.87万元 =
    **+42.47%**. Gross profit 6,485.87 → 5,489.13万元 = **−15.37%**. Growing revenue by 42% by
    selling large batch destroyed a sixth of the company's gross profit. Broken out:

    | Segment | revenue change | gross profit change |
    |---|---|---|
    | 样板 (sample) | +15.94% | −4.93% |
    | 小批量板 (small batch) | +34.89% | **−46.06%** |
    | 大批量板 (large batch) | **+77.93%** | **−44.29%** |

    Nearly doubling large-batch revenue *reduced* large-batch gross profit by 44%.
  - **Price and margin ratios.** FY2025: 1,619.17 ÷ 658.86 = **2.46×** on price per m²; 30.42 ÷
    1.00 = **30.4×** on margin. FY2024: 2.78× and 11.6×.
  - **Concentration by segment.** Rising strictly with order size in 2025 (37.88 < 42.22 < 45.54);
    in 2024 sample and small batch are within 0.61 pp of each other (40.97 and 40.36) so the
    ordering is **not** strictly monotonic, but large batch is 10.78 pp above sample in 2024 and
    7.66 pp above in 2025. **Reported honestly: the pattern holds at the ends, not at every step.**
  - **Order size is not the same cut as layer count, and this document proves it.** Reconstructing
    gross profit from the layer table: FY2024, 8+ layers is 18.19% of revenue at 35.66% =
    **45.25%** of gross profit, against the order-size table's 74.33% for sample boards. The two
    cuts give very different answers in 2024 and similar ones in 2025 (73.15% against 83.50%).
    Reconstructed totals: 6,484.40万元 and 5,489.83万元 against the order-size table's 6,485.87
    and 5,489.13 — agreement to within 0.02%, so both tables describe the same gross profit.
    **This is the first direct evidence in this file that the order-size effect is not simply the
    layer-count effect wearing a different label.** It does not disentangle them — there is no
    cross-tabulation — but it rules out their being identical.
  - **The loss-making customers in context.** 20,644.54万元 ÷ 64,460.87万元 = **32.03%** of
    main-business revenue was sold at a combined gross margin of −11.26%, a gross loss of
    2,325.35万元 — against total company gross profit of 5,489.13万元. Take those four customers
    away and the remaining 67.97% of revenue would have produced 7,814.48万元 of gross profit at a
    17.86% margin. (That is a counterfactual and a crude one — those customers absorb fixed cost —
    but the arithmetic is: 5,489.13 + 2,325.35 = 7,814.48; 7,814.48 ÷ (64,460.87 − 20,644.54) =
    17.83%, and the 0.03 pp difference from 17.86% is rounding in the printed inputs.)
  - **The Zhuhai plant reconciles.** 4,121.55 + 60,339.32 = 64,460.87万元 and 5,953.76 + 53,017.98
    = 58,971.74万元, both the printed totals; (4,121.55 − 5,953.76) ÷ 4,121.55 = −44.45%, printed.
- **Bears on:**
  - **H6 (supports, and this is now the single best entry in the file).** A fourth company, a
    fourth independent document, the same direction — and the only one where the exchange itself
    demanded the cut, the cost column is printed so nothing has to be reconstructed, and the data
    are FY2025. Sample boards are 23.37% of revenue and 83.50% of gross profit.
  - **H6 (supports, in the most direct form available anywhere in this repository).** Xunjiexing
    ran the experiment the other way round. It grew, it grew by selling large batch, and its gross
    profit fell 15.37% and its net result went further into loss. This is not a cross-section
    comparing a tail seller with a volume seller; it is one company moving from the tail towards
    volume and being made worse off, in consecutive audited years, with the arithmetic printed at
    the exchange's insistence.
  - **H7 (supports).** Top-5 concentration inside the large-batch segment is 45.54% against 37.88%
    inside the sample segment (FY2025), and 51.75% against 40.97% (FY2024). Two named customers
    together took 14,911.03万元 of revenue at roughly −16% gross margin. That is buyer power with
    a number on it.
  - **H6 (challenges, and this is the important one).** **A long tail is not sufficient.**
    Xunjiexing has served "over ten thousand enterprises" (PCB-1), is a declared sample-board
    specialist, has the second-highest sample-board margin in this file at 30.42% — and is losing
    money, because 76.63% of its revenue sits in two tiers earning 2.64% and 1.00%. Having a
    profitable tail does not save a company that funds a big-batch business out of it. Anyone
    reading the 83.50% figure as good news should read the 8.52% blended margin and the CNY 22.4m
    net loss beside it.
  - **The capital argument (mixed, and instructive).** The company's 41.55% utilisation and its
    new plant's −44.45% margin show what an unfilled fab costs. But the plant was built for, and
    filled with, low-margin security-market batch work, which is precisely the choice the
    repository's thesis argues against. The filing describes the ramp as the cause of the loss;
    the mix is at least as much of it.
- **Used in:** not yet.
- **Caveats:**
  - **Xunjiexing does not print its order-area thresholds in this document.** Qiangda's peer table
    (PCB-10) records Xunjiexing's order-area split for 2020, so a definition exists somewhere in
    its IPO prospectus, which was **not** retrieved (the STAR-market IPO filings did not come back
    under a cninfo `column=sse` category search; see the blocked list). Without the thresholds,
    this table's tiers cannot be assumed identical to Qiangda's 5/50 m² or Jinbaize's 5/20 m².
  - **This is a reply to an enquiry letter, not an audited financial statement.** The board
    certifies it, and the auditor filed a verification opinion the same day which we did not read.
    The figures tie exactly to the FY2025 annual report's headline revenue (68,913.22万元 total,
    64,460.87万元 main business) and margin (8.52%), both of which PCB-3 already verified
    independently from the annual report.
  - **The customers are anonymised** as 客户A through 客户P. Registered capital is given for most
    of them, which would identify several to a determined reader, but we have not attempted it and
    no name should be inferred.
  - **The segment margins are heavily contaminated by the Zhuhai ramp in 2025.** Zhuhai made mostly
    security-market product, which is batch work, so the collapse in the small- and large-batch
    margins is partly a start-up cost and not a steady-state price. The FY2024 column is the
    cleaner one, and it still shows 37.10% against 3.20%.
  - All translations are ours; the Chinese is quoted exactly so a reader can check them.
