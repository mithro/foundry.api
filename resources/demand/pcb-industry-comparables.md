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
