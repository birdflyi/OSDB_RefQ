# Chapter 5 RefQ SUB-A01：JSS vs EMSE 目标期刊比较审计

## 1. 任务身份与结论

```text
TASK = CH5_REFQ_SUB_A01_JSS_VS_EMSE_TARGET_VENUE_COMPARATIVE_AUDIT
AUDIT_DATE = 2026-09-21
TASK_MODE = READ_ONLY_TARGET_VENUE_DECISION

TARGET_VENUE_RECOMMENDATION = JSS
ALTERNATE_VENUE = EMSE
SUBMISSION_ROUTE = JSS_REGULAR_ARTICLE
MS_R04_REQUIRED = NO

DECISION = CH5_REFQ_SUB_A01_PASS_RECOMMEND_JSS
```

推荐 JSS 的决定不是来自简单加权分数，也不是继承此前 submission-suggestion 文档的默认偏好。决定顺序严格采用：SCIE hard gate → scope/story fit → contribution fit → desk-reject risk → manuscript-change cost → first-decision speed。

JSS 对当前稿件的“cross-project explicit Reference evidence → project-level relation construction → software-ecosystem structural representation → role-aware network characterization”叙事具有更直接的容纳空间。EMSE 同样高度可投，且当前官方首轮决定中位数显著更快；但其经验研究定位会把更多审稿注意力集中到 DBMS-only 外部效度、2023-only 时间窗、extraction/membership validation 与 RQ3 统计设计。当前 MS-R03 已对这些问题作出较完整防御，因此 EMSE 是强备选而非不适配期刊。

## 2. 稿件 authority 与预检

Repository preflight：

```text
REPOSITORY = D:/github_repo/OSDB_RefQ
BRANCH = ch5-refq-repository-identity-correction-v1
HEAD_BEFORE_SUB_A01 = 0feb56ad0bc4830b4405b22db733dda163de7fe9
REMOTE_HEAD_BEFORE_SUB_A01 = 0feb56ad0bc4830b4405b22db733dda163de7fe9
PREFLIGHT = PASS
```

Manuscript authority：

```text
ACCEPTED_MANUSCRIPT_REVISION = MS-R03
CURRENT_SHA = E59F96FF05279797BD047B127B537FEA2D1FB618478DBB5455C36EA2A83777F9
MS_R03_SNAPSHOT_SHA = E59F96FF05279797BD047B127B537FEA2D1FB618478DBB5455C36EA2A83777F9
CURRENT_EQUALS_MS_R03_SNAPSHOT = YES

SIDECAR_SHA = D74798B4CD7325522207DCBFBF4CDDA6A743E32A77D3E30BE0A5AB13A163015D
MANIFEST_SHA = 5FFAF0A6C638BA3321C9861737AECCA423EF14E8731D5B87312797F251A112A4
ABS_R01_SHA = 68E85D74989880AC549B2A115FAC181BC46F40F5C0A50C4B664B639D86F534C9

SUBMISSION_SUGGESTION_SHA = 84B866CBAA03DC795062CDF2DCA2FFF7A90FCFFF10DF4476AA62498642E8D834
```

本审计完整读取了 `docs/submission_suggestion/ch5_refq_submission_suggestion_2026-09-21.md`，但把它仅作为当日 shortlist 与历史网页研究上下文，未把其中 `DEFAULT_LEAN = JSS` 当作结论。

当前稿件的实际主线为：

```text
observable fine-grained Reference evidence
→ artifact-to-project semantic membership
→ membership-induced aggregation / quotient construction
→ Reference Quotient (RefQ)
→ Project-level RefQN
→ source role / target role / first-order structural view
→ bounded DBMS subdomain comparison
```

稿件没有把 RefQ 宣称为新通用 graph-coarsening algorithm、通用 quotient operator、dependency ground truth、task-resolution ground truth 或 causal knowledge-flow model。

## 3. 证据新鲜度与等级

```text
LIVE_WEB_RECHECK = PARTIALLY_AVAILABLE
EMSE_OFFICIAL_PUBLISHER_RECHECK = AVAILABLE
JSS_SCIENCEDIRECT_DIRECT_RECHECK = BLOCKED_BY_HTTP_403_CLOUDFLARE
JSS_EDITORIAL_MANAGER_RECHECK = AVAILABLE
JSS_EDITOR_REPORTED_TIMING_RECHECK = AVAILABLE
CROSSREF_METADATA_RECHECK = AVAILABLE
COMPUTER_USE_BROWSER = NOT_AVAILABLE
```

证据等级：

1. `PUBLISHER_OFFICIAL`：Springer EMSE journal home、submission guidelines、open collections；JSS 官方 Editorial Manager 入口及其官方 Guide for Authors 链接。
2. `EDITOR_REPORTED`：JSS 主编 Paris Avgeriou 公布的 2025 journal-performance 数据。
3. `CURRENT_INDEXING_SECONDARY`：Peeref 当前 JSS profile 中的 Web of Science Core Collection / SCIE 条目与 scope 镜像。
4. `BIBLIOGRAPHIC_METADATA`：Crossref 2024–2026 论文元数据、摘要与参考文献元数据。
5. `DECISION_SUPPORT_CARRY_FORWARD`：当日 submission-suggestion 文档中已检查的 ScienceDirect CFP 记录；因 ScienceDirect 本轮返回 HTTP 403，JSS CFP 未伪装成再次直接访问成功。

所有动态事实仍须在实际投稿日通过 `SUB-A02_TARGET_JOURNAL_REQUIREMENTS_MAPPING` 再核验。

## 4. SCIE hard gate

| Venue | SCIE status | Evidence | Hard-gate result |
|---|---|---|---|
| Journal of Systems and Software (JSS) | YES | 当前 Peeref journal profile 明列 Web of Science Core Collection 的 `Science Citation Index Expanded (SCIE)`；官方 Editorial Manager 同期可用。Clarivate MJL 入口可访问，但无浏览器环境下其动态检索结果未能独立提取。 | PASS |
| Empirical Software Engineering (EMSE) | YES | Springer 官方 journal home 的 Abstracted and indexed in 列表明确包含 `Science Citation Index Expanded (SCIE)`。 | PASS |

```text
JSS_SCIE_STATUS = YES
EMSE_SCIE_STATUS = YES
SCIE_HARD_GATE = PASS
```

## 5. 全维度证据矩阵

分类表示相对于当前 MS-R03 的适配/风险，而不是期刊质量评分。

| Dimension | JSS | EMSE | Evidence-based interpretation |
|---|---|---|---|
| SCIE_STATUS | NEUTRAL | NEUTRAL | 两刊均通过 hard gate。 |
| AIMS_AND_SCOPE_FIT | STRONG_ADVANTAGE | STRONG_ADVANTAGE | JSS scope 覆盖 empirical studies、open-source development、metrics/evaluation 与 software-development-resource mining；EMSE 官方 scope 明确强调 applied SE 与 strong empirical focus。 |
| CURRENT_MANUSCRIPT_STORY_FIT | STRONG_ADVANTAGE | MODERATE_ADVANTAGE | JSS 更自然承接 relation construction + ecosystem + structural network；EMSE 需要把同一科学内容更明确组织为 empirical design/reproducibility story。 |
| METHOD_FIT | MODERATE_ADVANTAGE | STRONG_ADVANTAGE | JSS 能容纳 construction/formalization + network characterization；EMSE 对可复查经验方法、统计分析和 validation contract 的期待更直接。 |
| EMPIRICAL_DESIGN_FIT | MODERATE_ADVANTAGE | STRONG_ADVANTAGE | EMSE 近期论文持续采用大规模 repository mining、manual validation、混合统计设计；MS-R03 的 five-RQ、sensitivity 与 threats 架构匹配。 |
| CONTRIBUTION_FIT | STRONG_ADVANTAGE | MODERATE_ADVANTAGE | RefQ 的 bounded methodological contribution 是 construction contract，而非新算法；JSS 对 systems/software-ecosystem relation representation 的读者预期更自然。EMSE 可接受，但需要持续避免把贡献写成纯结果论文或通用方法突破。 |
| SOFTWARE_ECOSYSTEM_FIT | STRONG_ADVANTAGE | MODERATE_ADVANTAGE | JSS 2024–2026 有直接的软件生态、跨组织协作、GitHub link/network 论文；EMSE 也有 NPM ecosystem-wide collaboration 研究。 |
| REPOSITORY_MINING_FIT | MODERATE_ADVANTAGE | STRONG_ADVANTAGE | 两刊均有先例；EMSE 的 large-scale repository-mining identity 更集中。 |
| NETWORK_ANALYSIS_FIT | STRONG_ADVANTAGE | MODERATE_ADVANTAGE | JSS 近期跨组织 OSS ecosystem 论文的参考与方法脉络明确包含 SNA、GitHub 与 community/network structure；EMSE 也发表 ecosystem SNA，但会更强调 empirical validation。 |
| REPRODUCIBILITY_FIT | MODERATE_ADVANTAGE | STRONG_ADVANTAGE | Appendix A、frozen P0-v3 provenance、release architecture 与 data-availability section 对 EMSE 是明显优势。 |
| PRACTITIONER_EXPECTATION_FIT | NEUTRAL | MODERATE_RISK | JSS 要求经验验证，当前稿件具备；EMSE 官方 scope 强调 researcher/practitioner relevance，当前 §5.3 的用途被谨慎限定为 candidate screening/inspection，需在英文 framing 中清晰但不能夸大。 |
| RECENT_PUBLISHED_ARTICLE_FIT | STRONG_ADVANTAGE | STRONG_ADVANTAGE | 两刊均有 2024–2026 的 OSS、GitHub、ecosystem、network 或 repository-mining 文章；JSS 更接近结构/生态叙事，EMSE 更接近经验设计。 |
| DESK_REJECT_RISK | MODERATE_ADVANTAGE | MODERATE_RISK | JSS 的 scope/story 对齐更直接；EMSE 不构成 scope mismatch，但更可能在编辑初筛中追问经验设计与 external validity。 |
| FIRST_DECISION_SPEED | MODERATE_RISK | STRONG_ADVANTAGE | JSS 2025 editor-reported median 76.5 days；EMSE 2025 publisher-reported median 24 days。 |
| EXPECTED_REVIEW_CYCLE | UNVERIFIED | UNVERIFIED | 两者都没有与“submission-to-first-decision”同定义、同年份的完整 submission-to-acceptance 官方比较数据；不得混用第三方 peer-review turnaround。 |
| FORMAT_CHANGE_COST | UNVERIFIED | NEUTRAL | JSS 精确 guide 页面本轮受限，不能把未知规则记作优势；现有证据只表明已知风险以包装为主。EMSE 官方格式要求更明确，仍属于可控转换。 |
| ABSTRACT_CHANGE_COST | UNVERIFIED | NEUTRAL | JSS exact word/keyword limits 待 SUB-A02；EMSE 明确 150–250 words、4–6 keywords，structured abstract 可选，预计不需要科学内容变化。 |
| MAIN_TEXT_CHANGE_COST | MODERATE_ADVANTAGE | MODERATE_RISK | JSS 主要是 journal-facing framing；EMSE 可能需要在引言/讨论中更前置 empirical design、validation 与 generalizability，但不改变 RQ/贡献。 |
| SUPPLEMENT_RELOCATION_COST | NEUTRAL | NEUTRAL | 两刊均支持 supplement；当前没有 verified hard limit 迫使立即移动 Appendix A、表 4.6f 或表 4.7。 |
| TRANSLATION_FRAMING_COST | MODERATE_ADVANTAGE | MODERATE_RISK | JSS 可直接沿现有 ecosystem/structural 叙事翻译；EMSE 需更明显的 empirical-study rhetoric，但仍是语义保持的英文 framing。 |
| SUBMISSION_ARTIFACT_COST | MODERATE_RISK | MODERATE_RISK | JSS 预计 highlights/声明等包装项需 SUB-A02 核验；EMSE 明确要求 title-page declarations 与 data availability，并提供 CRediT 格式。均不构成科学 blocker。 |

## 6. JSS fit 分析

### 6.1 自然投稿身份

```text
JSS_REGULAR_ARTICLE = RECOMMENDED
JSS_SPECIAL_ISSUE = NOT_RECOMMENDED
```

MS-R03 可自然定位为：

```text
software ecosystem empirical study
+ project-level relation construction
+ network / structural characterization
+ traceable evidence boundary
```

Peeref 当前 scope 镜像列出的主题包括 empirical studies、open-source/global software development、metrics and evaluation、data mining of software development resources，并要求通过 case studies、experiments 或 systematic comparisons 等方式验证观点。MS-R03 不只有形式定义：它以 294 个 seed DBMS projects、五个 RQ、角色化结构指标、统计检验、敏感性分析和 provenance package 对 RefQ construction contract 进行经验实例化，满足“构造 + validation”的文章形态。

### 6.2 叙事与贡献适配

- RefQ 把 heterogeneous fine-grained Reference evidence 提升为 project-level relation，适合 JSS 的 systems/software-ecosystem 与 repository analytics 读者。
- 贡献不是新 generic graph operator，而是 endpoint eligibility、semantic membership、aggregation、self-loop/non-project policy、observation completeness 与 interpretation boundary 的显式 contract；这一定位在 JSS 中不必强行转写为算法论文。
- DBMS 是 bounded vertical ecosystem，而非声称代表所有 OSS。JSS 近期发表的软件生态和 OSS 论文说明垂直生态/标准/组织边界研究可被容纳。
- §5.3 已给出 candidate screening、structural inspection、manual-review prioritization 等谨慎实践含义；其强度足以说明工程用途边界，但英文稿需保持“不构成自动维护决策”的限制。

### 6.3 变更成本

JSS 路线主要需要：英文标题/摘要/全文翻译、journal-facing terminology consistency、submission artifacts 与最终格式映射。无需重构五个 RQ、四项贡献、主要结果、讨论边界或 scientific package。

## 7. EMSE fit 分析

### 7.1 自然投稿身份

MS-R03 可在不改变科学内容的前提下定位为：

```text
large-scale empirical software engineering study
+ repository-derived evidence
+ reproducible construction contract
+ observation-aware statistical characterization
```

Springer 官方 scope 明确写明“applied software engineering research with a strong empirical focus”，并强调对研究者/实践者相关的 empirical results、research-practice connection 以及可 replicated/expanded 的研究。MS-R03 的 sampling/admission contract、five RQs、descriptive + Spearman + Kruskal-Wallis + BH-FDR、label-mode sensitivity、Threats to Validity、Appendix A 和 frozen provenance 与这些期待高度一致。

### 7.2 主要优势

- 规则化 extraction、membership/observation audits 和 package identity 为 replicability 提供实质性支撑。
- 角色化分析明确区分 source-complete seeds 与 source-incomplete expanded targets，降低常见 repository-mining 观测误读。
- RQ3 对 multiple testing、effect size、mixed-label modes 与结论边界已有约束，符合 empirical-reporting 习惯。
- Data and Code Availability 与 Appendix A 已存在，能直接响应 EMSE 的 data-availability 与 reproducibility expectations。

### 7.3 额外审稿压力

- 294 个 seed 仅来自 DBMS vertical，external validity 需保持 bounded claim。
- study year 为 2023，cross-sectional window 不能被写成长时段演化规律。
- extraction/membership resolution 没有被包装成分类模型性能评测；EMSE reviewer 可能要求更细的 validation rationale。
- RQ3 的局部显著性、label-mode sensitivity 和 non-significant results 会受到更强统计审查。
- RefQ 是 construction/formalization contribution；英文 framing 必须说明它如何服务 empirical inquiry，而不能让文章看起来在通用算法与经验结果之间摇摆。

这些项目在 MS-R03 中均已有回应，状态是 reviewer-scrutiny risk，而不是 scientific blocker。相较 JSS，EMSE 需要更明显的 journal-facing empirical framing，因此变更成本略高。

## 8. 近期论文 comparator evidence（2024–2026）

“相关”只按已核验内容维度使用，不把标题关键词等同于整篇相似。

### 8.1 JSS

1. **Schreiber & Wieland, “Inter-organizational collaborations in open-source software ecosystems” (2026), DOI `10.1016/j.jss.2025.112765`**
   Crossref 元数据确认其为 JSS 2026 article；其 130 条参考文献元数据系统覆盖 GitHub mining、social network analysis、OSS community structure、developer coordination、community detection、case-study research 与 inter-organizational affiliation。相关维度：`software ecosystem`、`OSS`、`GitHub/repository mining`、`network analysis`、`empirical design`。它证明 JSS 仍容纳“生态边界 + 网络结构 + 经验证据”的文章形态。

2. **Lima et al., “How are discussions linked? A link analysis study on GitHub Discussions” (2025), DOI `10.1016/j.jss.2024.112196`**
   Crossref 元数据与参考文献元数据确认文章围绕 GitHub Discussions link behavior，并连接 issue-unit linking、shared links、repository discussions 与 link-intention research。相关维度：`GitHub/repository mining`、`cross-artifact relation`、`empirical study design`。它与 RefQ 的共同点是可观测显式链接证据；不同点是 RefQ 进一步执行 artifact-to-project membership 与 project-level aggregation。

3. **“A comparative analysis of industrial involvement and licensing in the open source software ecosystems of four IoT standards” (2026), DOI `10.1016/j.jss.2025.112708`**
   Crossref 元数据确认其比较四个 IoT standards 的 OSS ecosystems；参考文献元数据覆盖 ecosystem governance/health、company contributions、GitHub bot detection、organization disambiguation、standards 与 OSS implementations。相关维度：`software ecosystem`、`OSS`、`bounded vertical comparison`、`empirical design`。它说明 JSS 接受以受限技术域/标准域为边界的比较研究，而非只接受全域 OSS 样本。

### 8.2 EMSE

1. **“Ecosystem-wide influences on pull request decisions: insights from NPM” (2025), DOI `10.1007/s10664-025-10706-1`**
   Crossref/Springer 摘要明确报告约 1.8 million PRs、2.1 million issues、20,052 GitHub projects，以 social network analysis 构建 ecosystem collaboration network，并结合 mixed-effects logistic regression、random forest 与 qualitative analysis。相关维度：`software ecosystem`、`OSS`、`GitHub/repository mining`、`cross-project relation`、`network analysis`、`empirical design`。这是一项对 RefQ 最有力的 EMSE scope precedent，但它也展示了 EMSE 对 validation breadth 与 mixed-method support 的高预期。

2. **“On the outliers of file-structure evolution: a mining study of GitHub software repositories” (2026), DOI `10.1007/s10664-026-10891-7`**
   摘要明确报告 94,247 repositories、12.2 million file-structure changes、quantitative baseline 与 3,049 manually inspected outliers。相关维度：`GitHub/repository mining`、`large-scale empirical design`、`manual validation`、`practitioner implications`。它与 RefQ 的主题不同，但可用于判断 EMSE 对大规模 mining study 的设计/验证期待。

3. **“Free open source communities sustainability: Does it make a difference in software quality?” (2024), DOI `10.1007/s10664-024-10529-6`**
   摘要明确报告 217 Apache Incubator OSS projects、16 sustainability metrics、8 quality metrics 与 Bayesian analysis。相关维度：`OSS`、`bounded project population`、`metric construction`、`empirical statistical design`。它说明 EMSE 可容纳受限 OSS population，但会期待清晰的 construct-to-metric contract 与统计论证。

Comparator 结论：两刊都不是因“有没有 OSS/GitHub 文章”而被区分；真正差异是 JSS 的 ecosystem/structural relation 叙事更自然，EMSE 的 empirical design/reproducibility 叙事更制度化。

## 9. First-decision timing

| Venue | Metric | Value | Evidence class | Interpretation |
|---|---|---:|---|---|
| JSS | median submission-to-first-decision, 2025 journal performance | 76.5 days | EDITOR_REPORTED | JSS EiC Paris Avgeriou 在 2026-03-30 的公开 journal-performance post 中同时报告 2025 submissions = 2,167、accepted = 308，且 76.5 days 从 2024 的 99 days 降低。不是 publisher SLA。 |
| EMSE | Submission to first decision (median), page currently displaying 2025 metric | 24 days | PUBLISHER_REPORTED | Springer 官方 EMSE home 当前展示。它是 first decision，不等于 external-review completion、acceptance 或 publication。 |

```text
FIRST_DECISION_SPEED_ADVANTAGE = EMSE
JSS_TIMING = 76.5_DAYS_EDITOR_REPORTED_2025
EMSE_TIMING = 24_DAYS_PUBLISHER_REPORTED_2025
SUBMISSION_TO_ACCEPTANCE_COMPARISON = UNVERIFIED
```

速度差异具有决策意义，但不足以推翻 JSS 在 scope/story 与 contribution fit 上的实质优势。

## 10. 45-day CFP eligibility（2026-09-21 至 2026-11-05）

### JSS

ScienceDirect 本轮直接访问受 HTTP 403 限制；当日 submission-suggestion 文档记录的两个窗口内 call 为：

- **AI Techniques for Performance, Reliability, and Sustainability of Modern Software Systems**，deadline 2026-09-30：对 RefQ 的核心 construction/ecosystem relation 主题不匹配。
- **Bridging AI, Automation, and Sustainability in Software Testing (AST 2026 Selected Papers)**，deadline 2026-10-15：selected-papers-only；当前稿件无相应资格。

因此即便沿用当日已查证列表，也不能把任一 call 视为合法优势。

### EMSE

Springer 官方 open collections 页面直接核验到窗口内：

- **Agentic Software Engineering: The Rise of AI Teammates**，deadline 2026-09-28：一般开放但主题不匹配。
- **By Invite Only - FORGE 2026**，deadline 2026-10-02：invite only。
- **By Invite Only - Evaluation and Assessment in Software Engineering (EASE) 2026**，deadline 2026-10-31：invite only。

窗口外的 Software Security Testing、Human-Centered AI、Prompt Engineering 等 collection 也不构成当前 RefQ 的主题优势。

```text
ELIGIBLE_MATCHED_JSS_CFP_WITHIN_45_DAYS = NO
ELIGIBLE_MATCHED_EMSE_CFP_WITHIN_45_DAYS = NO
CFP_DECISION = NO_CLEAR_SPECIAL_ISSUE_ADVANTAGE
RECOMMEND_REGULAR_SUBMISSION = YES
```

## 11. Author-guideline precheck

这不是 SUB-A02 的替代。JSS ScienceDirect guide 本轮不可直接读取，因此 exact limits 不被猜测；unknown 项被保留为 `UNVERIFIED`，但没有证据表明它们会迫使 scientific/MS-R03 restructuring。

| Item | JSS precheck | EMSE precheck | Likely impact |
|---|---|---|---|
| Article type | Regular Article route is compatible with current empirical/construction article; exact current type list awaits direct guide recheck. | Original empirical research is compatible with official scope and guidelines. | JSS `UNVERIFIED` detail / EMSE `NO_MANUSCRIPT_CHANGE` |
| Abstract type | Current paper supports a normal unstructured abstract; exact JSS requirement unavailable. | 150–250 words; structured abstract permitted but not required; optional sections Context/Objective/Method/Results/Conclusions. | JSS `UNVERIFIED`; EMSE `PACKAGING_ONLY` |
| Keywords | Required in current manuscript; exact JSS count unavailable. | 4–6 keywords. | JSS `UNVERIFIED`; EMSE `PACKAGING_ONLY` |
| Main-text/page limit | No verified hard limit extracted. | No explicit hard word/page limit identified on current official guideline page. | `UNVERIFIED`, no present MS-R04 trigger |
| Reference style at initial/final submission | Exact free-format/final-style rule awaits direct guide. | Official guideline uses author–year citations and alphabetical reference list. | `PACKAGING_ONLY` |
| Anonymous review | Exact current JSS review model awaits direct guide. | Single-blind peer review. | JSS `UNVERIFIED`; EMSE `NO_MANUSCRIPT_CHANGE` for anonymization |
| Figures/tables placement | Exact journal rule awaits direct guide. | Figures are placed within body unless upload size requires separation; tables/figures numbered and cited consecutively. | `PACKAGING_ONLY` |
| Supplementary material | Elsevier/JSS supports supplementary submission in current publication system, exact file rules await guide. | Official SI policy supported; files cited as Online Resource and published as received. | `PACKAGING_ONLY` |
| Data availability | Exact JSS journal wording awaits guide; existing §7 and Zenodo DOI reduce risk. | All original research must include a Data Availability Statement; public repository deposit is strongly encouraged. | JSS `UNVERIFIED`; EMSE `PACKAGING_ONLY`, already substantively supported |
| Code/data sharing | Existing release architecture is a strength; exact JSS requirement awaits guide. | Sharing/repository use encouraged; exceptions may be explained for privacy/rights. | `PACKAGING_ONLY` |
| CRediT/authorship contributions | Exact JSS requirement awaits guide. | Official guideline gives a CRediT taxonomy example and requires authors' contribution information in declarations/title page as applicable. | `PACKAGING_ONLY` |
| Conflict/funding/declarations | Elsevier submission packaging expected; exact JSS fields await SUB-A02. | Statements and Declarations required; missing relevant declarations may be returned as incomplete; title page consolidates Funding, Competing interests, Ethics, Data/Materials/Code, authors' contributions. | `PACKAGING_ONLY` |
| Highlights | Likely Elsevier submission artifact, but journal-specific current requirement was not directly readable. | No journal-specific highlights requirement found. | JSS `UNVERIFIED`; EMSE `NO_MANUSCRIPT_CHANGE` |
| Graphical abstract | Exact JSS optional/required status unavailable. | No graphical-abstract requirement found. | JSS `UNVERIFIED`; EMSE `NO_MANUSCRIPT_CHANGE` |
| Cover letter | Submission-system artifact; exact journal wording awaits guide. | Cover letter used for relevant disclosure/reuse information; otherwise standard submission packaging. | `PACKAGING_ONLY` |
| Word/LaTeX source | Exact JSS accepted-source rules await guide. | Word or LaTeX workflow supported; guideline text specifies Word formatting and a separate LaTeX submission workflow. | `PACKAGING_ONLY` |

结论：EMSE 的已验证要求更明确，但全部可由现有内容与投稿 artifacts 满足；JSS 的未验证项需要 SUB-A02 逐项关闭，当前没有“必须先改科学内容/五个 RQ/四项贡献”的迹象。

## 12. Appendix A、表 4.6f 与表 4.7

| Component | JSS | EMSE | Decision now |
|---|---|---|---|
| Appendix A: Reproducibility and Boundary Record | `UNDECIDED_UNTIL_AUTHOR_GUIDELINE_REVIEW`; JSS 若存在长度/appendix policy，可移为 supplement，但不能以猜测的节省空间作为 venue 决策。 | `KEEP_APPENDIX_A_IN_MAIN` is defensible because it directly supports reproducibility and boundary interpretation; final placement still checked in SUB-A02. | 不移动。 |
| Table 4.6f structural brokerage candidates | It is a bounded RQ2c result with explicit approximate-betweenness limitations. | It supports transparent reporting of a derived structural view. | 两刊均暂留主文。 |
| Table 4.7 subdomain composition | It is central to RQ3 and to the bounded DBMS comparison. | It is central empirical evidence for RQ3 and external-validity interpretation. | 两刊均留主文。 |

```text
TABLE_RELOCATION = 0
APPENDIX_RELOCATION = 0
```

## 13. English framing maps

### 13.1 JSS framing map

```text
observable cross-project explicit references
→ artifact-to-project semantic membership
→ project-level RefQ relation construction
→ software-ecosystem structural representation
→ source/target/first-order network characterization
```

```text
TITLE_CHANGE_NEEDED = NO
ABSTRACT_SEMANTIC_CHANGE_NEEDED = NO
INTRO_FRAMING_CHANGE_NEEDED = NO
DISCUSSION_FRAMING_CHANGE_NEEDED = NO
```

这里的 `NO` 表示无需改变现有语义结构；英文翻译仍需采用 JSS-facing terminology，并可在不改 RQ/贡献的情况下调整句序与强调。

### 13.2 EMSE framing map

```text
repository-derived observable evidence
→ explicit sampling/admission/membership contract
→ reproducible project-level relation construction
→ large-scale empirical study
→ observation-aware role and statistical characterization
```

```text
TITLE_CHANGE_NEEDED = NO
ABSTRACT_SEMANTIC_CHANGE_NEEDED = NO
INTRO_FRAMING_CHANGE_NEEDED = YES
DISCUSSION_FRAMING_CHANGE_NEEDED = YES
```

EMSE 所需的 `YES` 仅指未来英文稿中的 bounded emphasis：更前置 empirical design、validation、reproducibility 与 generalizability；不得改变四项贡献、五个 RQ 或科学值。

## 14. Desk-reject risk matrix

| Risk class | JSS | Treatment | EMSE | Treatment |
|---|---|---|---|---|
| SCOPE_MISMATCH | LOW | MS-R03 已直接采用 ecosystem/relation/network story。 | LOW | Official strong empirical focus 与 repository-derived study 匹配。 |
| CONTRIBUTION_MISMATCH | LOW | Construction contract + empirical instantiation 是自然 article shape。 | MODERATE | 必须把 RefQ 说明为支持经验研究的可复查 construction，而非未验证的通用新方法；`PACKAGING_FIX`。 |
| INSUFFICIENT_ENGINEERING_RELEVANCE | MODERATE | §5.3 已限定用途；英文 framing 需清楚说明 inspection/screening value；`PACKAGING_FIX`。 | MODERATE | EMSE 明确强调 researcher/practitioner relevance；不得把候选用途夸大为 validated tool；`PACKAGING_FIX`。 |
| EMPIRICAL_DESIGN_EXPECTATION | LOW | 当前 five-RQ、sensitivity、threats 与 package 足够支撑。 | MODERATE | 更可能追问 membership/extraction validation、RQ3 design 与 2023 window；`ALREADY_ADDRESSED_IN_MS_R03`，需英文呈现清晰。 |
| EXTERNAL_VALIDITY | MODERATE | DBMS vertical 与 seed-centered boundary 已明确；`ALREADY_ADDRESSED_IN_MS_R03`。 | MODERATE | 同一风险在 EMSE 更显著；`ALREADY_ADDRESSED_IN_MS_R03`。 |
| REPRODUCIBILITY | LOW | Appendix A、provenance 与 release architecture 是优势。 | LOW | 与 EMSE replicability expectation 高度匹配。 |
| FORMAT_NONCOMPLIANCE | MODERATE | ScienceDirect guide exact rules 未直接重验；`PACKAGING_FIX` via SUB-A02。 | LOW | 官方规则已大部分核验；仍需 submission checklist；`PACKAGING_FIX`。 |
| OVERLENGTH | LOW | MS-R03 已完成 venue-independent condensation；无 verified hard limit。 | MODERATE | Appendix/表 placement 要在 SUB-A02 复核，但没有当前 relocation mandate；`PACKAGING_FIX` if triggered。 |
| LANGUAGE | MODERATE | Final English manuscript pending；`PACKAGING_FIX` through LANG-A01/LANG-A02。 | MODERATE | 同上，且 empirical rhetoric 要更集中；`PACKAGING_FIX`。 |

```text
SCIENTIFIC_BLOCKER_COUNT = 0
```

## 15. Manuscript-change cost comparison

| Cost area | JSS | EMSE |
|---|---|---|
| Core story | Low：沿现有 ecosystem/structural story。 | Medium：需在英文引言/讨论中更前置 empirical design。 |
| RQs/contributions | None. | None. |
| Title/abstract science | None；直接语义保持翻译。 | None；structured abstract optional，不要求重定义内容。 |
| Main-text restructuring | No evidence of need. | No substantive restructuring; bounded emphasis likely. |
| Appendix/supplement | Deferred to SUB-A02. | Appendix A 可合理留主文；最终仍映射。 |
| Submission artifacts | Likely highlights/declarations/cover-letter checks; exact list pending direct guide. | Title-page declarations、data availability、contributions、funding/conflict packaging明确。 |
| Scientific recomputation | None. | None. |

```text
MS_R04_REQUIRED = NO
```

理由：当前比较没有发现任一期刊 hard requirement 会迫使改变五个 RQ、四项贡献、结果、表或科学资产。JSS 路线可在后续英文翻译与 submission packaging 中完成；若 SUB-A02 发现真正要求修改 authoritative Chinese semantic source 的 journal-specific hard rule，再单独重新决定是否启动 MS-R04，不能在本审计中预先制造 revision。

## 16. 最终推荐与备选

```text
TARGET_VENUE_RECOMMENDATION = JSS
ALTERNATE_VENUE = EMSE
PRIMARY_ROUTE = JSS_REGULAR_ARTICLE
SPECIAL_ISSUE_ROUTE = NO
```

决定性差异：

1. JSS 与 RefQ 的 software-ecosystem relation construction 和 structural-network story 更直接对齐，贡献无需额外转换身份。
2. JSS 近期论文对 OSS ecosystems、GitHub links、跨组织 collaboration 与 network analysis 提供了更近的 narrative precedents。
3. EMSE 在 empirical design、repository mining 和 reproducibility 上同样强，且 24-day publisher-reported first decision 是明显速度优势。
4. 但 EMSE 的优势伴随更高的 empirical-validation/external-validity/RQ3 scrutiny 和略高 framing cost；根据既定决策优先级，速度不覆盖 material fit difference。
5. 两刊在 45-day window 均无合法、开放且主题匹配的 special issue，故不改变 regular-submission 推荐。

短 fallback：若 JSS 拒稿且意见不要求 scientific rebuild，优先将同一 scientific baseline 经 bounded empirical reframing 转投 EMSE；IST 可继续作为次级 regular backup。本审计不扩展比较 JSEP/SPE/SCP。

## 17. 精确下一阶段

仅推荐以下一个顺序，不在本任务中启动：

```text
1. TARGET_VENUE_FREEZE
2. SUB-A02_TARGET_JOURNAL_REQUIREMENTS_MAPPING
```

`TARGET_VENUE_FREEZE` 应冻结 `JSS_REGULAR_ARTICLE`；随后 SUB-A02 必须直接重验 JSS 当前 Guide for Authors 的 article type、abstract/keyword limits、review model、highlights、graphical abstract、references-at-submission、figures/tables、supplement、data/code policy、CRediT、declarations 与 cover letter，并据此确认 `MS_R04_REQUIRED = NO` 是否继续成立。

## 18. No-change guards

```text
CURRENT_CHANGED = 0
MS_R03_SNAPSHOT_CHANGED = 0
SIDECAR_CHANGED = 0
MANIFEST_CHANGED = 0
ABS_R01_CHANGED = 0

NEW_MANUSCRIPT_CANDIDATE_CREATED = 0
NEW_ACCEPTED_REVISION_CREATED = 0

RQ_TEXT_CHANGED = 0
CONTRIBUTION_TEXT_CHANGED = 0
SCIENTIFIC_VALUE_CHANGED = 0

SCIENTIFIC_RECOMPUTATION = 0
FIGURE_RERENDER = 0
TABLE_RELOCATION = 0
```

四个预存 V3–V6 ZIP 未修改。原 submission-suggestion 文档未纳入本任务 commit。

## 19. 证据 URL

- JSS ScienceDirect journal page（直接访问本轮 HTTP 403）：<https://www.sciencedirect.com/journal/journal-of-systems-and-software>
- JSS Guide for Authors（官方链接由 Editorial Manager 暴露；直接访问本轮 HTTP 403）：<https://www.elsevier.com/journals/journal-of-systems-and-software/0164-1212/guide-for-authors>
- JSS official Editorial Manager：<https://www.editorialmanager.com/jssoftware/>
- JSS current indexing/scope secondary profile：<https://www.peeref.com/journals/5213/journal-of-systems-and-software>
- JSS 2025 editor-reported performance：<https://www.linkedin.com/posts/parisavgeriou_editorial-board-activity-7444366033177468928-zvpA>
- EMSE official journal home：<https://link.springer.com/journal/10664>
- EMSE official submission guidelines：<https://link.springer.com/journal/10664/submission-guidelines>
- EMSE official open collections：<https://link.springer.com/journal/10664/collections?filter=Open>
- Crossref works API：<https://api.crossref.org/>

```text
CH5_REFQ_SUB_A01_PASS_RECOMMEND_JSS
```
