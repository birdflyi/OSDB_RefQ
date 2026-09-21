# Chapter 5 RefQ 本文升维叙事与修改边界（冻结建议稿）

## 0. 文档定位

本文件只服务当前 RefQ/JSS 论文。它冻结后续英文翻译与 journal-facing framing 的核心逻辑，并用于判断哪些内容只需重新强调、哪些需要 Related Work / Discussion / Threats 增补、是否需要触发 MS-R04，以及哪些未来平台/AI 贡献不得混入本文。

## 1. 升维后的论文中心

当前论文不再表述为“一个引用网络及其若干统计结果”。

推荐中心：

> 面向显式跨项目 Reference evidence 的可追溯、观测感知的项目级操作化与度量框架。

建议英文核心定位：

> a traceable and observation-aware operationalization of project-level explicit-reference structure

其中：traceable = project-level relations can be linked back to observable fine-grained evidence；observation-aware = metric validity depends on which source/target behavior is actually observed；operationalization = explicit evidence is transformed into a reproducible project-level measurement object；project-level explicit-reference structure = weaker-semantic structural relation, not dependency/task/causal ground truth。

## 2. 核心主逻辑

```text
Problem
fine-grained explicit Reference evidence is observable,
but cannot be directly interpreted as a project-level network.
        ↓
Operationalization
endpoint eligibility + semantic membership + aggregation + provenance
→ RefQ / RefQN
        ↓
Observation asymmetry
294 seed projects are source-complete,
expanded targets are source-incomplete.
        ↓
Measurement validity
source role ≠ target role ≠ first-order direction-ignored structural position
        ↓
Empirical demonstration
composition + role heterogeneity + connectivity/modularity + subdomain comparison
        ↓
Meta-finding
explicit-reference structure is measurable,
but its interpretation is role-dependent,
observation-bounded, metric-dependent,
and for RQ3 partly label-operationalization-dependent.
        ↓
Use
structural inspection + candidate screening + evidence-guided qualitative follow-up
        ↓
Boundary
stronger dependency/task/causal semantics require additional validation.
```

## 3. Source observation asymmetry 应提升为主逻辑

当前场景：294 analysis seed projects = source-complete under current observation contract；expanded targets = entered because seeds referenced them = source-incomplete。

这不是普通 limitation，它直接决定哪些 metric 可以计算、哪些 population 可解释、哪些指标不可跨 role 比较。

因此应在以下位置形成闭环：

- Introduction：project-level relation construction is insufficient unless observation completeness is made explicit.
- Methods：正式定义 source-complete seed population、observable target population、direction-ignored structural view。
- Results：对应 RQ2a source role、RQ2b target role、RQ2c structural view。
- Discussion：提升为 role-specific metric validity follows from asymmetric observation.
- Threats：RefQN is a seed-centered observed network rather than a closed ecosystem network.
- Conclusion：project-level explicit-reference measurements remain meaningful when interpreted under their corresponding observation roles.

## 4. 三层核心贡献结构

### 4.1 Operationalization contribution

heterogeneous Reference evidence → reproducible project-level measurement object。

构造条件：endpoint eligibility、semantic membership、aggregation、self-loop/non-project policy、provenance。

不是 new generic quotient operator 或 new generic graph algorithm。

### 4.2 Observation-aware measurement contribution

现有 degree / HHI / Louvain / clustering / betweenness 都不是新算法。贡献是 existing network measures are assigned valid populations, denominators, and interpretation semantics under asymmetric observation。

推荐表述：`a role-aware measurement scheme for a seed-centered Reference Quotient network` 或 `observation-aware measurement semantics for project-level explicit-reference structures`。

### 4.3 Empirical knowledge contribution

DBMS 实验形成 evidence、structure、validity/sensitivity 三类知识。Louvain partition 对 random seed 敏感，subdomain differences 对 label mode 敏感，没有 cross-mode robust RQ3 feature。它们共同支持：measurement interpretation is conditional on algorithmic and metadata operationalization。

## 5. 更积极但仍客观的结果解释框架

### RQ2c — Louvain sensitivity

不要写成“community result 不稳定，因此贡献有限”。

提升为：

> The direct-reference structure exhibits modular organization, but a single algorithmic partition should not be interpreted as a stable semantic taxonomy.

### RQ3 — no cross-mode robust feature

不要写成“没有稳健显著结果”。

提升为：

> subdomain effects are not invariant to label operationalization.

这说明 metadata construction is part of measurement validity。

### Expanded target source incompleteness

不要只作为 limitation。

提升为：

> observation completeness determines the admissible interpretation of node roles.

expanded-target low out-degree cannot be interpreted as low source activity。

## 6. 核心 meta-finding

推荐冻结：

> explicit-reference structure is measurable, but its interpretation is role-dependent, observation-bounded, and metric-dependent.

对于 RQ3 可扩展：category-level conclusions are additionally sensitive to label operationalization。

中文：

> 显式引用结构可以被操作化和量化，但其解释依赖于观测角色、观测边界与具体度量；涉及子领域比较时，还受到标签操作化口径的影响。

## 7. 与既有高质量文献的关系：建议做“探究—回答”而不是攻击

不建议写成 existing studies are subjective/wrong。

推荐：

> prior work demonstrates the analytical value of repository-derived networks, while also motivating a closer examination of how data boundaries, relation semantics, and observation completeness constrain metric interpretation.

### Literature A — Kalliamvakou et al., MSR 2014

**The Promises and Perils of Mining GitHub**，DOI `10.1145/2597073.2597074`。

关键支持：GitHub 是丰富研究数据源，但 repository population、platform usage 和 event interpretation 存在系统性 pitfalls；研究者应对 sample/data interpretation 做显式控制。

与本文关系：GitHub-derived evidence does not become valid measurement merely by being observable。本文进一步把这一原则落实到 source admission、membership、observation completeness、role-specific metric interpretation。

### Literature B — McClean et al., IST 2021

**Social network analysis of open source software: A review and categorisation**，Information and Software Technology 130, 106442，DOI `10.1016/j.infsof.2020.106442`。

关键支持：OSS SNA 使用的 data sources 和 network constructions 差异很大；network analysis 被用于 structure / lifecycle / communication 等不同问题；network construction 是结果解释的重要前提。

与本文关系：relation construction + observation boundary must precede structural interpretation。

### Literature C — Blincoe et al., IST 2019

**Reference Coupling: An exploration of inter-project technical dependencies and their characteristics within large software ecosystems**，Information and Software Technology 110, 174–189，DOI `10.1016/j.infsof.2019.03.005`。

该研究通过 cross-project references 构建 project-level directed relation，对抽样 cross-references 进行人工验证，并将其解释为 technical dependencies，之后做 ecosystem/community analysis。

本文不否定其结论。建议表述：

> Reference Coupling demonstrates that cross-references can support useful project-level dependency-oriented analysis under its validated sampling and relation definition. RefQ asks a complementary measurement question: when heterogeneous explicit Reference evidence is retained beyond a dependency-oriented subset, what construction and observation contracts are required before project-level metrics can be interpreted?

差异：Blincoe = validated dependency-oriented conceptualization；RefQ = broader explicit-reference evidence + traceable semantic membership quotient + observation-aware role separation。

不应写 `Reference Coupling incorrectly equates references with dependencies`。应写：its stronger dependency interpretation is supported under its own manually validated relation scope; the current study intentionally retains a broader evidence universe and therefore adopts weaker project-level semantics。

## 8. Related Work 的建议修改方式

新增一个窄段，不需要重写整章。

目标逻辑：

```text
已有研究展示 network/repository evidence 的价值
→ 数据与 network boundary 会影响可解释性
→ Reference Coupling 展示 stronger-semantic validation 路线
→ 本文选择 broader evidence + weaker semantics
→ 因此需要 explicit observation/measurement contract
```

推荐位置：§2.2 或 §2.5 研究缺口收束之前。

避免大篇幅批评既有研究、“其他论文结论主观”、“已有 network metrics 不可信”。

## 9. Threats to Validity 的建议增强

建议增加明确维度：**Observation / Network Boundary Validity**。

核心：source completeness、target inclusion mechanism、seed-centered boundary、platform observability、metric population。

说明：network boundary 由 research design 决定；source 和 target observability 不对称；metrics 只在其声明 population 中成立；expanded nodes 的 missing source behavior 不是观测到的 0；direction-ignored view 是 derived first-order view，不补全 missing source observations。

这不是承认方法错误，而是在定义 estimand。

## 10. Conclusion 的建议回答方式

结论形成四句功能：
1. What became measurable?
2. What did the empirical study reveal?
3. Under what conditions are those measurements interpretable?
4. What can they support, and what requires stronger evidence?

## 11. 核心学术句冻结

**Core sentence 1 — construct**

> RefQ provides a traceable and observation-aware operationalization of project-level explicit-reference structure.

**Core sentence 2 — measurement**

> It separates evidence construction from role-specific structural measurement by making endpoint eligibility, semantic membership, observation completeness, and metric semantics explicit.

**Core sentence 3 — empirical knowledge**

> The DBMS study shows substantial structural heterogeneity, while the interpretation of the resulting measurements depends on observation roles, algorithmic choices, and label operationalization.

**Core sentence 4 — use**

> RefQ therefore provides a reproducible substrate for structural inspection, candidate screening, and follow-up empirical analysis rather than a ground-truth representation of dependency, task resolution, or causal knowledge flow.

## 12. 当前论文不吸收的平台主张

不得加入 general plug-and-play platform、fully automated empirical research、AI end-to-end research system、cross-domain validated framework、research-efficiency improvement。

可保留一句 bounded future-facing statement：

> The staged construction and measurement workflow also provides a reusable substrate for extending the analysis with additional metrics or relation views under the same evidence and observation contracts.

仅作 extensibility implication，不作为已验证贡献。

## 13. 是否需要 MS-R04 的判断标准

只有以下情况才触发：

A. Related Work 缺乏 observation/network-boundary literature bridge；
B. Introduction 未把 source observation asymmetry 放入核心 problem；
C. Discussion 未形成 measurement-validity synthesis；
D. Threats 缺乏 observation/network-boundary validity；
E. Conclusion 无法回答 measurement conditions。

若这些内容已经实质存在，只需 English/JSS framing：`MS_R04_REQUIRED = NO`。

若至少 A–E 中存在明显 semantic-source 缺口：`MS_R04_REQUIRED = YES_BOUNDED_FRAMING_REVISION`。

任何 MS-R04 都不得 change scientific values、change RQs、change contribution count、rerun experiments、add platform claims。

## 14. 下一步建议任务

执行只读：

```text
CH5_REFQ_JSS_CONTRIBUTION_FRAMING_AND_OBSERVATION_VALIDITY_AUDIT
```

目标：
1. 对照 MS-R03 判断上述升维是否已被现有文本支持；
2. 定位缺口；
3. 核验 2–3 篇代表文献是否足以支撑 Related Work bridge；
4. 判断是否需要 MS-R04；
5. 如果需要，只生成 bounded edit plan，不直接改正文。

## 15. 冻结结论

```text
PAPER_CENTER = TRACEABLE_OBSERVATION_AWARE_OPERATIONALIZATION_AND_MEASUREMENT
SOURCE_OBSERVATION_ASYMMETRY = CORE_SCENARIO_FEATURE
ROLE_AWARE_MEASUREMENT = CORE_METHODOLOGICAL_ADVANTAGE
META_FINDING = EXPLICIT_REFERENCE_STRUCTURE_IS_MEASURABLE_BUT_INTERPRETATION_IS_ROLE_DEPENDENT_OBSERVATION_BOUNDED_AND_METRIC_DEPENDENT
RELATED_WORK_POSITION = COMPLEMENTARY_AND_CRITICAL_NOT_ADVERSARIAL
PLATFORM_CLAIM = DEFER_TO_PAPER_B
NEXT_STEP = READ_ONLY_FRAMING_AND_OBSERVATION_VALIDITY_AUDIT
```
