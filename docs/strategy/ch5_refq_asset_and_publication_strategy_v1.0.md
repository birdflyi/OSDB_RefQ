# Chapter 5 RefQ 资产化与成果转化策略（冻结建议稿）

## 0. 文档定位

本文件用于把当前 RefQ/GH_CoRE 工作从“单篇论文资产”提升为“可持续产出的研究资产体系”，并明确：哪些内容属于当前 RefQ/JSS 论文；哪些内容属于博士论文其他章节；哪些内容应拆分为后续独立论文；哪些代码/架构技术债值得补；哪些潜在能力目前只能作为 future asset，而不能写成当前论文已验证贡献。

本文件不修改当前 MS-R03 manuscript authority，也不修改 P0-v3 scientific baseline。

## 1. 当前总体判断

当前 RefQ 工作已经形成两条互补但应解耦的成果线。

### 1.1 科学研究线

核心问题：

> 如何把 heterogeneous fine-grained explicit Reference evidence 操作化为可追溯、观测感知、可解释的 project-level structural relation，并在明确 observation boundary 下进行 role-aware measurement？

这一条已经足以支撑当前 JSS 论文。

### 1.2 Research infrastructure 线

当前 GH_CoRE / RefQ pipeline 已经具备以下基础：

```text
historical events
→ content normalization
→ candidate reference detection
→ object validation / enrichment
→ standardized Reference rows
→ source admission
→ membership / eligibility
→ RefQ construction
→ metric/statistical analysis
→ figures/tables
→ provenance / reproducibility manifests
```

这已经超过一次性脚本集合，接近“具有规范中间表示、阶段边界、provenance 和可重复输出的 empirical software engineering research pipeline”。但目前尚未通过跨领域复用、plugin extensibility、平台正确性/效率评测，因此：

```text
RESEARCH_PIPELINE_EXISTS = YES
GENERAL_PLUG_AND_PLAY_RESEARCH_PLATFORM_VALIDATED = NO
```

当前论文可以写 `reproducible/extensible analytical substrate`，但不宜宣称 `general plug-and-play research platform`。

## 2. 五层资产模型

### Layer A — Scientific Construct

核心资产：RefQ、Project-level RefQN、semantic membership quotient、`Q=M^T R_P M`。

科学价值：将 fine-grained Reference evidence 操作化为 project-level structural relation；明确 endpoint eligibility、membership、aggregation、self-loop/non-project semantics；区分 first-order relation 与 second-order projection。

主要承载成果：`Paper A — 当前 RefQ / JSS`。

### Layer B — Measurement Methodology

核心资产：source role、target role、first-order undirected structural view、role-specific population、denominator semantics、observation completeness、metric interpretation boundary。

科学价值：在 source observation 非对称的 seed-centered network 中，不同 metric 只能在相应 role/population 下解释。

核心 meta-finding：

> explicit-reference structure is measurable, but its interpretation is role-dependent, observation-bounded, and metric-dependent.

主要承载成果：`Paper A — 当前 RefQ / JSS`。

### Layer C — Research Infrastructure

当前资产：GH_CoRE extraction/validation chain、standardized Reference records、membership registry/audit、source admission、RefQ relation construction、analysis scripts、supplemental package、runtime/provenance manifests。

潜在价值：把 evidence construction 与 downstream analytical operators 解耦。

未来目标架构：

```text
Raw Platform Data
        ↓
Evidence Extraction
        ↓
Canonical Reference Schema
        ↓
Admission / Membership / Observation Contracts
        ↓
Relation Constructor
        ↓
Stable Analytical Boundary
        ↓
Metric / Analysis Plugins
        ↓
Statistics
        ↓
Visualization / Reporting
```

主要承载成果：`Paper B — Contract-Based Reference Analysis Workbench`。

### Layer D — Reusable Empirical Assets

包括 seed registry、Reference relation dataset、RefQN nodes/edges、role-aware feature tables、supplemental package、Zenodo relation/data release、reproducibility metadata。

作用：replication、benchmark、future cross-domain comparison、platform validation、downstream qualitative/semantic studies。

### Layer E — AI-Orchestrated Research

未来潜力：

```text
structured research context
→ experiment intent
→ controlled tool/plugin selection
→ executable analysis
→ evidence validation
→ failure diagnosis
→ report generation
```

潜在研究问题：Can an AI agent reliably compose, execute, validate, and report repository-mining studies over a contract-based empirical-analysis workbench?

这属于后续 Agentic Empirical SE / AI-for-SE 研究，不进入当前 RefQ 论文。

## 3. 资产—论文矩阵

| 成果 | 核心问题 | 使用资产 | 需要新增的实质工作 | 与当前 RefQ 竞争关系 |
|---|---|---|---|---|
| Paper A — RefQ/JSS | explicit Reference 如何被正确操作化、测量和解释？ | Layer A+B+D | 主要为 framing / journal packaging | 当前主论文 |
| Paper B — Reference Analysis Workbench | repository Reference research 如何模块化、复现、扩展？ | Layer C+D | 架构抽象 + plugin API + multi-study evaluation | 不竞争，复用当前资产 |
| Paper C — Cross-Ecosystem RefQ | RefQ findings 能否跨 ecosystem 推广？ | Layer A+B+C+D | 新领域数据 + cross-domain comparison | 增强 external validity |
| Artifact/Data Release | 如何形成可复用 relation/network/benchmark？ | Layer D | release scope / version / documentation | 支撑所有论文 |
| Paper D — Agentic Empirical SE | AI 能否可靠编排 empirical-SE research workflow？ | Layer C+D+E | agent task/eval framework | 后期独立成果 |

## 4. 当前 RefQ/JSS 论文吸收与不吸收边界

### 4.1 建议吸收

当前论文应明确强化：

1. RefQ 是 explicit-reference structure 的 project-level operationalization；
2. observation completeness 是 metric validity 的前置条件；
3. source role / target role / first-order structure 是三类 observation role，而不是普通指标组；
4. construction contract 使 evidence 和 measurement 可追溯；
5. 当前 staged pipeline 支持 reproducibility 和后续 analysis extension；
6. empirical results 应作为 measurement semantics 的验证/展示，而不是零散统计事实。

可接受表述：`reproducible analytical substrate`、`staged and traceable construction-and-measurement workflow`、`extensible to additional relation-level or network-level analyses under the same evidence and observation contracts`。

### 4.2 当前不宜吸收

不写成已验证主贡献：general plug-and-play research platform、fully automated research platform、metric plugin framework validated across domains、AI-driven end-to-end scientific automation、research-effort reduction、generic cross-ecosystem generalizability。

这些需要独立实验。

## 5. 对博士论文其他章节的吸收建议

### 5.1 第四章：FACT / fine-grained Reference evidence

建议吸收 canonical Reference representation、evidence provenance、fine-grained entity/relation normalization、为后续 relation construction 提供可执行事实基础。

不要吸收 RefQ metric semantics、source/target structural role、network-level conclusion。

### 5.2 第五章：STRUCTURE / RefQ

应吸收：`Operationalization + Observation-aware Measurement + Empirical Characterization + Traceability`。

### 5.3 第六章：TASK / Issue–PR strict relation

只吸收“关系资产层级”接口，不吸收 RefQ 平台叙事。第六章解决 stronger task-semantic GT fitting。

与第五章保持：

> 在同一开源协作事实基础上，形成两类粒度和证据强度不同、但相互补充的关系资产。

不要写成 RefQ 自动导致 RESOLVES。

### 5.4 第七章：ACCESS / controlled access/query

可吸收 contract-based relation access 思想：relation identity、semantic boundary、allowed operations、evidence traceability、controlled query。

## 6. Paper B — Research Workbench 策略

暂定题目方向：**A Contract-Based Workbench for Reproducible Cross-Project Reference Analysis**。

核心问题：empirical repository studies involving explicit references often entangle evidence extraction, relation construction, metric implementation, and reporting; can these concerns be separated through explicit contracts and reusable analysis plugins?

### 6.1 推荐 contract layer

- Dataset Contract：repository identity、observation window、source population、event/source coverage。
- Evidence Schema Contract：source/target entity、relation type、event/repository provenance、membership resolvability。
- Relation Contract：constructor、endpoint eligibility、membership、aggregation、self-loop policy、observation semantics。
- Metric Contract：name、input relation/view、population、denominator、required fields、output schema、interpretation boundary。
- Artifact Registry Contract：避免 metric 直接依赖固定文件路径。
- Provenance Contract：config、code revision、input identity、runtime、derived artifact hashes。

目标 API 示例：

```text
artifact_registry.get(
    relation="refq_cross_project",
    population="seed_sources",
    representation="edge_table"
)
```

## 7. 不建议以 AOP 作为主要架构隐喻

“关注点分离”的直觉正确，但 metric/analysis 更适合 plugin architecture + canonical schema + declarative registry + contract-based execution。

AOP 更适合 logging、tracing、caching、provenance capture、security。AOP 可作为实现手段，而不是研究平台主概念。

## 8. Paper B 需要补的评价

真正缺口主要在 evaluation，而不是代码数量。

### Portability
至少选择 DBMS、ML/AI libraries、Web frameworks、cloud-native/infrastructure 等不同 ecosystem，观察核心 pipeline 是否无需修改即可执行。

### Extensibility
增加此前不存在的 metric plugins，例如 temporal reciprocity、bridge persistence、ego-network concentration、reference-topic distribution；报告 LOC added、core modules changed、files changed、implementation effort。

### Correctness
新平台输出与 frozen P0-v3 accepted outputs 对齐。

### Reproducibility
相同 config 多次执行应得到 same admitted population、same relation counts、same metric outputs、same provenance manifest。

### Scalability
报告 records、repositories、runtime、memory、storage。

### Research-effort reduction
如宣称“快速/低成本研究”，应比较 ad-hoc workflow vs workbench workflow，并度量 steps、time、code modifications、failure count、reproduction success。

## 9. Paper C — Cross-Ecosystem RefQ

未来独立解决 Paper A 不应承担的 external-validity 问题。

可能设计：DBMS、ML、Web frameworks、cloud-native。

潜在 RQs：
1. explicit Reference evidence composition 是否跨 ecosystem 不同？
2. source/target role distributions 是否存在稳定模式？
3. first-order RefQ structural properties 是否可复现？
4. 哪些 Paper A findings 在跨域后仍稳定？
5. label/domain operationalization 对结果影响多大？

Paper C 的价值：test transportability and boundary conditions of RefQ measurements。

## 10. Agentic empirical-SE 作为后期成果

在 Workbench 完成之后再研究 user research intent → agent planning → dataset/relation/metric registry → controlled execution → result validation → provenance check → report generation。

评价包括 task completion、analysis correctness、metric-selection correctness、invalid inference rate、provenance completeness、failure recovery、human intervention、reproducibility。

不要把“现在 AI 能帮助自动跑流程”当成当前论文贡献。

## 11. 技术债优先级

### P0 — 当前 Paper A 投稿前
只做 contribution framing、JSS requirements、English translation、submission artifacts；不为了平台化重构代码。

### P1 — Paper B 启动前
优先 canonical schema、artifact registry、relation constructor interface、metric plugin interface、declarative config、provenance manifest normalization、tests against P0-v3 frozen outputs。

### P2 — Cross-domain / AI
再做 dataset adapters、multi-domain registry、semantic plugins、agent tool contracts、controlled execution。

## 12. 成果转化原则

### 原则 A：scientific question 与 infrastructure question 解耦

Paper A 回答：what is a valid project-level explicit-reference measurement object?

Paper B 回答：how can such empirical analyses be executed reproducibly and extensibly?

### 原则 B：平台作为“生产成果的资产”，而不是在第一篇论文中一次性消耗

一套 reusable pipeline 更大的价值是降低 Paper B/C/D 的边际成本，而不是给 Paper A 增加一句 `we built a platform`。

### 原则 C：只有被评价过的能力才能作为强贡献

```text
implemented ≠ validated
modular ≠ plug-and-play
automated ≠ reliable
AI-assisted ≠ autonomous scientific workflow
```

## 13. 当前冻结建议

```text
PAPER_A_REFQ_JSS =
operationalization
+ observation-aware measurement
+ empirical demonstration
+ reproducible artifact

PAPER_B =
contract-based reproducible reference-analysis workbench

PAPER_C =
cross-ecosystem RefQ transportability

PAPER_D =
agentic empirical-SE orchestration

PLATFORM_GENERALITY_CLAIM_IN_PAPER_A = NO
REUSABLE_ANALYTICAL_SUBSTRATE_CLAIM_IN_PAPER_A = YES
CODE_REFACTOR_BEFORE_PAPER_A_SUBMISSION = NO
```
