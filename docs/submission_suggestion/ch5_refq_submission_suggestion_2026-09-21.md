# Chapter 5 RefQ 投稿建议与后续任务路线（2026-09-21）

## 0. 文档用途

本文件用于第五章 RefQ 小论文后续投稿决策、Codex 任务规划和投稿材料准备。

它不是 manuscript authority，也不修改科学基线或已接受稿件版本。

本文档记录的是 **2026-09-21 时点**、基于当前 `MS-R03` 叙事与稿件状态的投稿建议。期刊的 SCIE 收录状态、投稿指南、special issue eligibility、审稿速度和征文期限都可能变化；正式投稿前必须再次核验。

---

## 1. 当前稿件 authority

```text
SCIENTIFIC_BASELINE = P0-v3

ACCEPTED_MANUSCRIPT_REVISION = MS-R03
STAGE = SUBMISSION_CONDENSED_ACCEPTED

CURRENT_SHA =
E59F96FF05279797BD047B127B537FEA2D1FB618478DBB5455C36EA2A83777F9

ACCEPTED_SNAPSHOT =
versions/MS-R03_POST_SUBMISSION_CONDENSED_E59F96FF.md

EDITORIAL_COMPLETE = YES
VENUE_INDEPENDENT_CONDENSATION_COMPLETE = YES

JOURNAL_SPECIFIC_PREPARATION_PENDING = YES
FINAL_ENGLISH_ABSTRACT_PENDING = YES
FINAL_SUBMISSION_READY = NO
```

Accepted manuscript lineage:

```text
MS-R01
→ MS-R02 EDITORIAL_COMPLETE_ACCEPTED
→ MS-R03 SUBMISSION_CONDENSED_ACCEPTED
```

MS-R03 的中文摘要已经压缩为约 297 个汉字、无 citation；当前英文摘要仅有 `ABS-R01` 术语对齐参考，不是权威投稿译文。

---

## 2. 当前论文叙事主线

当前稿件不再以泛化的“knowledge flow / Reference Coupling”作为主叙事，而以以下结构为核心：

```text
observable fine-grained Reference evidence
→ artifact-to-project semantic membership
→ membership-induced aggregation / quotient construction
→ Reference Quotient (RefQ)
→ Project-level Reference Quotient Network (RefQN)
→ source role / target role / first-order undirected structural view
→ bounded DBMS subdomain comparison
```

核心贡献不是：

```text
new generic graph-coarsening algorithm
new generic quotient operator
dependency ground truth
task-resolution ground truth
causal knowledge-flow model
```

核心贡献是：

1. 将细粒度 Reference evidence 到项目级 RefQ/RefQN 的 relation construction 显式化为可检查的 construction contract；
2. 明确 endpoint eligibility、semantic membership、non-project/self-loop policy 和 observation completeness；
3. 在 seed-centered asymmetric observation 下分离 source role、target role 与 first-order structural view；
4. 提供可追溯、弱语义的项目级 structural relation asset，并在 DBMS 场景完成经验刻画。

因此，投稿 venue 的最佳匹配关键词应优先考虑：

```text
software ecosystems
cross-project relations
mining software repositories
empirical software engineering
open-source software
socio-technical / network analysis
software repository analytics
reproducible empirical study
```

而不是仅按 “database” 或 “graph theory” 选择 venue。

---

## 3. 当前投稿约束

基准日期：

```text
CURRENT_DATE = 2026-09-21
45_DAY_WINDOW_END = 2026-11-05
```

### 3.1 硬约束

```text
SCI_OR_SCIE_INDEXED = REQUIRED
```

本轮优先按 SCIE 口径筛选。

### 3.2 主要排序因素

优先级：

```text
1. 与 MS-R03 当前叙事和贡献的适配度
2. SCIE 收录
3. 首次编辑/审稿回复速度
4. 45 天内是否存在可合法投稿的 deadline / special issue
5. 最终接受周期
```

“deadline 在 45 天以内”是偏好，不应为了 deadline 强行投 scope 不匹配或 invitation-only / selected-papers-only 的 special issue。

期望第一次明确回复最好不超过约 6 个月，但不是硬约束；当候选适配度相近时，first-decision speed 应作为最高优先级的 tie-breaker。

---

## 4. 推荐投稿序列

## 4.1 Tier 1：双首选

### 1A. Journal of Systems and Software (JSS) — Regular Article

**当前定位：首选之一，略偏结构/生态叙事。**

适配原因：

- JSS 持续发表 software ecosystems、OSS ecosystem、cross-project / network-oriented empirical studies；
- 2026 年仍有 software ecosystems / systems-of-systems 专题和相关研究；
- 当前 RefQ 稿件同时包含：
  - relation construction/formalization；
  - software ecosystem empirical setting；
  - network structure characterization；
  - reproducible empirical evidence；
- 相比纯 empirical-results paper，JSS 对“方法构念 + ecosystem empirical characterization”的容纳度较自然。

推荐 framing：

```text
explicit cross-project references
→ software ecosystem relation construction
→ Reference Quotient
→ structural roles and network organization
```

审稿速度：

- JSS EiC Paris Avgeriou 公开的 2025 年数据：
  `median submission-to-first-decision = 76.5 days`
  （2024 年为 99 天）。
- 第三方数据库 Peeref 在 2026-09-21 显示的 peer-review turnaround 约 16 周。
- 因此可合理按约 2.5–4 个月量级预期首轮决定，但不能视为保证。

SCIE：

- 当前公开索引数据库显示 JSS 被 SCIE 收录。
- 正式投稿前仍应在 Clarivate Master Journal List 再次核验。

当前建议：

```text
JSS_REGULAR_ARTICLE = STRONG_PRIMARY
```

不要仅因为 45 天窗口内存在 JSS special issue 就强行匹配。

---

### 1B. Empirical Software Engineering (EMSE) — Regular Paper

**当前定位：与 JSS 几乎同档；若 first-decision speed 权重更高，可以升为第一顺位。**

Springer 官方当前描述：

> applied software engineering research with a strong empirical focus

并强调：

- empirical results；
- relevance to researchers/practitioners；
- replicability / expandability；
- research-practice connection。

MS-R03 与其高度匹配的部分：

```text
294 seed projects
repository-derived evidence
explicit sample/admission contract
five RQs
descriptive + Spearman + Kruskal-Wallis + BH-FDR
sensitivity analysis
observation boundary
reproducibility appendix
relation/data release
frozen P0-v3 provenance
```

推荐 framing：

```text
observable repository evidence
→ reproducible construction contract
→ large-scale empirical study
→ role-aware and observation-aware characterization
```

速度：

Springer 官方 2026-09-21 页面显示：

```text
Submission to first decision (median) = 24 days
```

SCIE：

Springer 官方 journal page 明确列出：

```text
Science Citation Index Expanded (SCIE)
```

主要风险：

EMSE reviewer 可能更集中追问：

- DBMS-only sample 的 external validity；
- 294 seed sampling；
- 2023-only observation window；
- extraction / membership validity；
- RQ3 statistical design；
- reproducibility package。

这些问题当前稿件已经有较完整的 defenses，因此不是阻塞项。

当前建议：

```text
EMSE_REGULAR_PAPER = STRONG_PRIMARY
```

若“首轮反馈速度”权重大于“ecosystem structural framing 自然度”，可排序：

```text
1. EMSE
2. JSS
```

---

## 4.2 Tier 2

### 3. Information and Software Technology (IST) — Regular Article

适配度：高，但低于 JSS / EMSE。

优点：

- empirical software engineering 明确在 scope 内；
- 长期接收 software repositories / empirical methodology / OSS 研究；
- SCIE 收录；
- 当前第三方公开审稿信息约 `9.6 weeks` turnaround。

当前风险：

IST 对“software technology / development practice contribution”的要求较显性。

当前 RefQ 的实践意义是：

```text
candidate screening
structural inspection
evidence organization
manual-review prioritization
```

而不是：

```text
validated maintenance tool
developer productivity intervention
automated decision system
```

因此若投 IST，需要在不扩张科学 claim 的前提下更清晰地表达 §5.3 的 engineering relevance。

值得注意的是，IST 2026 年 editorial 明确指出 desk rejection 常见原因包括：

```text
scope misalignment
insufficient empirical validation
inadequate reporting
```

所以不能只因为其层级高就直接复用 JSS framing。

当前建议：

```text
IST = STRONG_BACKUP
```

---

## 4.3 Tier 3：速度型 SCIE backup

### 4. Journal of Software: Evolution and Process (JSEP)

Wiley 官方信息：

```text
Submission to first decision (median) = 28 days
```

并明确：

```text
Science Citation Index Expanded (SCIE)
```

期刊接收 empirical studies，且 author guideline 明确有 `Empirical` manuscript type。

优点：

- 速度快；
- 软件工程身份明确；
- empirical study 形式兼容；
- 支持 Free Format submission；
- 强调 data accessibility。

不足：

当前 RefQ 稿件并不以 software evolution/process 为核心，因此 topical fit 弱于 JSS / EMSE / IST。

当前建议：

```text
JSEP = FAST_SCIE_BACKUP
```

---

### 5. Software: Practice and Experience (SPE)

Wiley 官方当前指标：

```text
Submission to first decision (median) = 14 days
```

官方 indexing 页面明确列出：

```text
Science Citation Index Expanded
```

优点：

- 首轮速度极快；
- 仍发表 OSS empirical studies。

主要问题：

SPE 核心偏：

```text
practical software techniques
tools
implementation
system/software engineering practice
```

当前 RefQ 并没有以工程工具实施与实践效果评价为核心，因此 scope friction 明显高于前三名。

当前建议：

```text
SPE = FAST_BUT_LOWER_FIT_BACKUP
```

不要因为 14 天 median first decision 把它提前到 JSS/EMSE/IST 前面。

---

## 4.4 Tier 4

### 6. Science of Computer Programming (SCP)

SCIE：当前公开数据库显示收录。

问题：

- topical fit 可接受但不突出；
- 第三方公开 peer-review turnaround 约 `27.2 weeks`，已经接近/略超过“半年首轮回复”的偏好边界；
- 因此在候选充足时优先级低。

当前建议：

```text
SCP = LAST_REGULAR_BACKUP
```

---

## 5. 2026-09-21 起 45 天内 CFP / deadline 审计

窗口：

```text
2026-09-21 → 2026-11-05
```

结论：

```text
NO_OPEN_SPECIAL_ISSUE_FOUND_THAT_CLEARLY_OUTRANKS_JSS_OR_EMSE_REGULAR
```

### 5.1 JSS

ScienceDirect 当前显示：

#### AI Techniques for Performance, Reliability, and Sustainability of Modern Software Systems

```text
deadline = 2026-09-30
```

与 RefQ 的核心主题不匹配。

#### Bridging AI, Automation, and Sustainability in Software Testing (AST 2026 Selected Papers)

```text
deadline = 2026-10-15
```

标题明确为 AST 2026 Selected Papers；当前 RefQ 不是相应 selected paper，不应视为一般开放入口。

因此：

```text
DO_NOT_FORCE_JSS_SPECIAL_ISSUE
USE_JSS_REGULAR_IF_JSS_SELECTED
```

### 5.2 Science of Computer Programming

当前 ScienceDirect CFP 中：

#### Selected papers from the 29th Ibero-American Conference on Software Engineering (CIbSE 2026)

```text
deadline = 2026-10-30
```

主题本身包含：

```text
open source
empirical software engineering
software ecosystems
repository mining / software analytics
```

但它是 `Selected papers from CIbSE 2026`。

除非当前稿件具有该 conference 的明确 eligibility / invitation，否则：

```text
NOT_ELIGIBLE_AS_NORMAL_OPEN_CALL
```

### 5.3 EMSE

当前 Springer journal page 显示开放 collections：

- Software Security Testing (SECUTE 2026): 2026-11-30
- Human-Centered AI Transformation for Software Engineering: 2027-01-31
- Empirical Studies for Prompt Engineering in Software Engineering: 2027-03-01

均不在 45 天以内，且与当前 RefQ 主题不优于 Regular Paper。

历史/邀请型 collection（如 FORGE selected papers）不能当作普通投稿入口。

---

## 6. 当前正式推荐排序

如果按：

```text
SCIE = hard constraint
fit = primary
first-decision speed = strongest secondary criterion
deadline ≤45 days = bonus only
```

则：

```text
TIER 1
1A. JSS Regular Article
1B. EMSE Regular Paper

TIER 2
3. IST Regular Article

TIER 3
4. JSEP Empirical / Regular
5. SPE Regular Article

TIER 4
6. SCP Regular Article
```

### JSS vs EMSE 的真正差异

不是简单的“第一 vs 第二”，而是 framing 不同：

```text
JSS:
structural relation + software ecosystem + network organization

EMSE:
empirical repository evidence + reproducibility + study design
```

若重视：

```text
ecosystem / structural narrative naturalness
```

则：

```text
JSS > EMSE
```

若重视：

```text
first-decision speed
empirical-study reviewer familiarity
```

则：

```text
EMSE > JSS
```

因此当前最合理的下一步不是直接确定第一投稿，而是执行：

```text
SUB-A01 =
JSS-vs-EMSE target-venue comparative audit
```

---

## 7. 不建议的路线

当前不建议：

```text
1. 为了 45 天 deadline 强行改投低适配 special issue
2. 为 selected-papers-only call 假设自己有 eligibility
3. 先把全文翻译成英文，再决定 JSS / EMSE
4. 为不同 venue 同时维护两套完整 manuscript
5. 因为某刊 first decision 快就忽略 scope fit
6. 再无目标修改已经 accepted 的 MS-R03
```

当前 manuscript revision 只有在：

```text
journal-specific hard requirement
or
final English expression requires bounded semantic-preserving adjustment
```

时才应继续推进。

---

## 8. 后续任务路线

当前状态：

```text
MS-R03
SUBMISSION_CONDENSED_ACCEPTED
```

推荐路线：

```text
SUB-A01
JSS vs EMSE comparative target-venue audit
READ-ONLY
        ↓
TARGET_VENUE_FREEZE
        ↓
SUB-A02
target-journal author-guideline / artifact requirement mapping
READ-ONLY
        ↓
if manuscript-content changes are truly required:
MS-R04
venue-specific bounded manuscript adjustment
        ↓
FINAL CHINESE SEMANTIC SOURCE FREEZE
        ↓
LANG-A01
authoritative English full-manuscript translation
+ fresh English Abstract translated from accepted Chinese Abstract
        ↓
LANG-A02
English semantic-equivalence + native-style QA
        ↓
SUB-A03
cover letter / highlights / declarations / CRediT /
data availability / supplemental-package closure
        ↓
SUB-A04
final journal-specific submission preflight
        ↓
SUBMISSION
```

原则：

```text
venue selection precedes full English translation
venue requirements precede manuscript restructuring
translation does not silently reopen science
submission packaging does not redefine manuscript semantics
```

---

## 9. SUB-A01 应解决的问题

SUB-A01 不改 MS-R03，只回答：

1. JSS 和 EMSE 哪一个与当前 manuscript framing 更匹配？
2. 两刊当前是否均保持 SCIE？
3. Regular Article / Regular Paper 的 manuscript types 和 scope 是否接受当前研究类型？
4. 当前 title / abstract / contribution framing 在哪一刊 desk-reject risk 更低？
5. 是否存在 length / abstract / keyword / structure 要求会迫使 MS-R04？
6. 两刊是否要求：
   - highlights；
   - graphical abstract；
   - structured abstract；
   - declarations；
   - CRediT；
   - data availability；
   - code/data repository；
   - supplemental files；
   - anonymization；
7. Appendix A 更适合留 main manuscript 还是 supplement？
8. Table 4.6f / Table 4.7 是否有必要因 venue rule 才移动？
9. English title / terminology framing 应采用哪套 journal-facing rhetoric？
10. 预期 first-decision speed 和 submission-to-acceptance 数据的证据等级如何？
11. 最终给出：
   - `TARGET_VENUE_RECOMMENDATION`
   - `ALTERNATE_VENUE`
   - 但不得凭空修改 manuscript。

---

## 10. SUB-A01 decision policy

不采用简单分数决定。

推荐采用 evidence matrix：

```text
SCIE_STATUS
SCOPE_FIT
RECENT_ARTICLE_FIT
METHOD_FIT
CONTRIBUTION_FIT
DATA_REPRODUCIBILITY_FIT
DESK_REJECT_RISK
FIRST_DECISION_SPEED
FORMAT_CHANGE_COST
SUPPLEMENT_CHANGE_COST
TRANSLATION_FRAMING_COST
```

其中：

```text
SCIE_STATUS = hard gate
```

若两刊均通过 hard gate，则：

```text
SCOPE_FIT
+ CONTRIBUTION_FIT
+ DESK_REJECT_RISK
```

优先于速度。

速度用于高适配候选之间的 tie-break。

---

## 11. 当前来源与核验记录

核验日期：

```text
2026-09-21
```

### EMSE — official Springer

Journal home:
https://link.springer.com/journal/10664

当前页面记录：

```text
strong empirical focus
encourages replicable / expandable studies
submission to first decision median = 24 days
SCIE listed in Abstracted and indexed in
```

### JSS

Journal:
https://www.sciencedirect.com/journal/journal-of-systems-and-software

2025 journal performance by EiC Paris Avgeriou:
https://www.linkedin.com/posts/parisavgeriou_editorial-board-activity-7444366033177468928-zvpA

记录：

```text
2025 submissions = 2167
accepted = 308
median submission-to-first-decision = 76.5 days
```

2026 software-ecosystem editorial/example:
https://www.sciencedirect.com/science/article/pii/S0164121226000488

Current SCIE cross-check:
https://www.peeref.com/journals/5213/journal-of-systems-and-software

### IST

Current SCIE / turnaround cross-check:
https://www.peeref.com/journals/3562/information-and-software-technology

2026 desk-rejection editorial:
https://www.sciencedirect.com/science/article/pii/S0950584926001862

### JSEP — official Wiley

Journal:
https://onlinelibrary.wiley.com/journal/20477481

Author guidelines:
https://onlinelibrary.wiley.com/page/journal/20477481/homepage/forauthors.html

Indexing:
https://onlinelibrary.wiley.com/page/journal/20477481/homepage/productinformation.html

Current publisher metrics include:

```text
submission to first decision median = 28 days
SCIE indexed
```

### SPE — official Wiley

Journal:
https://onlinelibrary.wiley.com/journal/1097024x

Indexing:
https://onlinelibrary.wiley.com/page/journal/1097024x/homepage/productinformation.html

Current publisher metrics include:

```text
submission to first decision median = 14 days
SCIE indexed
```

### SCP

Current SCIE / review-time cross-check:
https://www.peeref.com/journals/7410/science-of-computer-programming

### Current ScienceDirect calls for papers

https://www.sciencedirect.com/browse/calls-for-papers?subject=computer-science

Relevant-looking calls must be checked for `Selected Papers`, invitation, conference-extension, and topic eligibility before use.

---

## 12. Freshness rule

This document is authoritative only for the decision context at:

```text
2026-09-21
```

Before actual submission, re-check at minimum:

```text
SCIE_STATUS
AIMS_AND_SCOPE
ARTICLE_TYPE
ABSTRACT_LIMIT
WORD/PAGE_LIMIT
REFERENCE_STYLE
ANONYMIZATION
DATA_AVAILABILITY
SUPPLEMENT_POLICY
HIGHLIGHTS
GRAPHICAL_ABSTRACT
CREDIT
DECLARATIONS
CURRENT_CFP_ELIGIBILITY
CURRENT_FIRST_DECISION_METRIC
```

Do not treat historical review-time numbers as guarantees.

---

## 13. Current recommendation code

```text
PRIMARY_TARGET_SET = {JSS, EMSE}

DEFAULT_LEAN = JSS
SPEED_PRIORITY_LEAN = EMSE

STRONG_BACKUP = IST
FAST_SCIE_BACKUPS = {JSEP, SPE}
LAST_REGULAR_BACKUP = SCP

NEXT_TASK =
SUB-A01_JSS_VS_EMSE_TARGET_VENUE_COMPARATIVE_AUDIT
```

