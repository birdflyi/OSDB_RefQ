# Chapter 5 RefQ — Framework-Derived Research Hierarchy Rewrite

## Decision

CH5_REFQ_FRAMEWORK_DERIVED_HIERARCHY_REWRITE_PASS

This is the documentation record for the separately authorized
CH5_REFQ_THESIS_FRAMEWORK_RECONCILIATION_PASS_RECONSTRUCT_HIERARCHY.  The
authoritative manuscript is external to this repository.  Exactly five
manuscript regions were edited: §1.3, §1.4, the §4 opening roadmap, §5.4, and
§9.  No result subsection, table, figure caption, figure, scientific output,
code, manifest, receipt, or experiment was changed or run.

## 1. Starting identities and protected state

| Item | Value |
|---|---|
| Repository | D:/github_repo/OSDB_RefQ |
| Branch | ch5-refq-repository-identity-correction-v1 |
| repository_HEAD_before | c4dedeb0ff718ea09ad7203abedabeb8be76bcdd |
| remote_HEAD_before | c4dedeb0ff718ea09ad7203abedabeb8be76bcdd |
| Authoritative manuscript | C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md |
| Manuscript SHA before | 8D2C8F0A8E3D57B98F388D1B84E7AEAC3192A6D16B79BB087F6202D53420CB9B |
| Manuscript SHA after | 8ABC48751979461E2E8CC7389731FEB6BA5A6335CDF05706265BD1B4ED50248B |
| Read-only baseline copy | C:/Users/10651/AppData/Local/Temp/ch5_refq_framework_rewrite_baseline_20260831.md |
| Baseline-copy SHA | 8D2C8F0A8E3D57B98F388D1B84E7AEAC3192A6D16B79BB087F6202D53420CB9B |
| Manuscript location in Git | External; not tracked by OSDB_RefQ |

The four pre-existing untracked rendering archives were preserved and were
not staged:

~~~text
figures/ch5_refq/p0v3_final_v3.zip
figures/ch5_refq/p0v3_final_v4.zip
figures/ch5_refq/p0v3_final_v5.zip
figures/ch5_refq/p0v3_final_v6.zip
~~~

Read-only SHA checks for those archives were unchanged during this task:

~~~text
p0v3_final_v3.zip = 23A6694AE906702098AC347D09803F4F295180A1BE9FD8E0541B88595C25B144
p0v3_final_v4.zip = A72E698E3161E67C3A3AC28FBD529F24DDF86D7B02BBF37DE3DB40105CAFE363
p0v3_final_v5.zip = B67FD1231B9148CC66A2E0FB74C93A98D8FD02EBA09BB1FFA9A43D6AA262E83D
p0v3_final_v6.zip = 3E57FDE584D702E1D7C99ECEBEF825EECD152DD8C2E793976AD3124180D8E2A3
~~~

## 2. Governing authority and relation-asset hierarchy

The conflict-resolution order used for this L3–L4 task is:

~~~text
L0 — doctoral research scenario and chapter task allocation
L1 — cross-chapter construct / relation-asset hierarchy
L2 — Chapter-5 theoretical scope and semantic boundary
L3 — paper core research problem and contribution hierarchy
L4 — RQ organization
L5 — frozen empirical outputs and admissible claims
L6 — figure/table composition and presentation
L7 — local manuscript wording and style
~~~

The self-contained paper relation chain is:

~~~text
observable fine-grained Reference evidence
        ↓
not every observable endpoint is project-mappable
        ↓
explicit endpoint eligibility + semantic membership
        ↓
membership-induced block aggregation / quotient construction
        ↓
Project-level RefQ / RefQN
        ↓
seed-centered observation requires role-aware interpretation
        ↓
empirical characterization in the DBMS vertical setting
~~~

The cross-layer asset allocation remains:

~~~text
FACT layer     fine-grained Reference evidence
STRUCTURE layer artifact-to-project membership → graph coarsening
               → Reference Quotient → Project-level RefQN
TASK layer     strict Issue–PR RESOLVES candidate
ACCESS layer   controlled relation access / query
~~~

RefQ remains a project–project, first-order, traceable, weak-semantic
structural relation: directed evidence is constructed first and
direction-ignored views are derived afterward.  It is not dependency ground
truth, task resolution, causal knowledge transfer, RESOLVES, a controlled
access/query implementation, or a second-order shared-reference projection.

## 3. Authorized scope

Only these regions were authorized:

1. §1.3 research gap and objective;
2. §1.4 RQ lead-in and contribution hierarchy;
3. the opening roadmap paragraph after ## 4 结果;
4. §5.4 RQ synthesis;
5. §9 Conclusion.

The five RQ bullet texts, all result subsections, and all scientific values
remain protected.  The manuscript-facing prose contains no dissertation
chapter labels, L0–L7 governance terms, or working-note hierarchy jargon.

## 4. Exact bounded edits

The following blocks reproduce the relevant before and after manuscript text.
The after text is the external manuscript whose SHA is recorded in Section 1.

### 4.1 §1.3 研究缺口与目标

Before:

~~~text
### 1.3 研究缺口与目标
在上述概念定位基础上，本文将研究缺口具体化为三个方面：领域适用性、关系构造透明度和观测角色分离。

第一，软件生态系统研究虽然已经关注跨项目依赖和社会技术网络，但开源 DBMS 这一垂直基础设施场景仍需要对 Reference evidence composition 和项目级结构关系进行专门检验。直接将一般 OSS 结论外推到 DBMS 场景，可能忽略数据库系统在数据模型、扩展机制、可靠性治理和长期维护方面的约束。

第二，既有 project-reference work 已经证明 cross-project references 可以支持 directed and count-weighted project-level analysis；然而，project-pair edge representation 本身并不完整表达本文从 heterogeneous artifact-level evidence 提升到项目级关系时所需的 endpoint eligibility、project identity/membership、internal 与 non-project reference handling、edge evidence semantics 以及 source observation completeness。本文因此将这些 construction and observation decisions 显式写成 contract，而不是把它们包装成 prior work 从未处理的字段，并据此避免把项目级边误读为依赖、重要性或完整知识传递 [@blincoe2015ecosystems; @blincoe2019referencecoupling; @liu2022irel]。

第三，seed-centered source observation 与 expanded target observation 容易导致 source/target role 混用。本文只完整观测 294 个 seed DBMS projects 的 source 行为；expanded target nodes 主要因为被 seed projects 引用而进入网络。若不分离 source role、target role 和 undirected structural view，就可能把 target 节点的低 out-degree 错误解释为项目行为特征。

归结而言，本文关注的研究问题并非简单的记录分组统计，而是如何在异质细粒度 Reference evidence 上，依据显式 construction contract 构造可追溯且可解释的项目级关系。membership、project-mappable endpoint rule、direction、weight aggregation、self-loop policy、non-project target handling 和 seed-centered source observation 都会改变关系的解释方式。

基于这一研究问题，本文的目标是在开源 DBMS 垂直生态中定义并实例化 Project-level RefQN，进而分析其细粒度 Reference behavior、source role、target role、无向结构视图和子领域差异。本文不将更强语义的 task-level relation identification 或下游关系分析作为主贡献；这些方向仅作为后续扩展，用于说明 RefQ relation 与其他关系资产之间的层级接口。RefQ 作为具有明确 membership 与 aggregation contract 的可追溯项目级结构关系，为需要更强语义验证的后续分析提供证据层，但本文不执行或验证这些分析。
~~~

After:

~~~text
### 1.3 研究缺口与目标
在上述概念定位基础上，本文首先关注一个项目级关系构造问题：如何在保留细粒度 Reference evidence 可追溯性的同时，通过明确的 endpoint eligibility、semantic membership、aggregation、self-loop/non-project policy 和 interpretation boundaries，将其中满足项目映射条件的 evidence 严格商化为可解释的项目级结构关系。该问题并非简单的记录分组统计；membership、project-mappable endpoint rule、direction、weight aggregation、self-loop policy、non-project target handling 和 observation completeness 共同决定关系的构造与解释。

既有 project-reference work 已经证明 cross-project references 可以支持 directed and count-weighted project-level analysis；然而，project-pair edge representation 本身并不完整表达本文从 heterogeneous artifact-level evidence 提升到项目级关系时所需的 endpoint eligibility、project identity/membership、internal 与 non-project reference handling、edge evidence semantics 以及 source observation completeness。本文因此将这些 construction and observation decisions 显式写成 contract，而不是把它们包装成 prior work 从未处理的字段，并据此避免把项目级边误读为依赖、重要性或完整知识传递 [@blincoe2015ecosystems; @blincoe2019referencecoupling; @liu2022irel]。

这一构造问题还受到观测边界的约束。本文只完整观测 294 个 seed DBMS projects 的 source 行为；expanded target nodes 主要因为被 seed projects 引用而进入网络，其 source behavior 并未完整观测。因此，必须分离 source role、target role 和 direction-ignored first-order structural view，避免将 expanded targets 的低 out-degree 误读为项目行为特征。

在上述构造与观测边界下，本文以开源 DBMS 垂直生态作为经验实例，考察该关系资产的 evidence composition、role/structure patterns 和受边界约束的子领域差异。开源 DBMS 这一垂直基础设施场景仍需要对 Reference evidence composition 和项目级结构关系进行专门检验；直接将一般 OSS 结论外推到 DBMS 场景，可能忽略数据库系统在数据模型、扩展机制、可靠性治理和长期维护方面的约束。基于这一研究问题，本文旨在定义并实例化 Project-level RefQN，进而分析其细粒度 Reference behavior、source role、target role、无向结构视图和子领域差异。本文不将更强语义的 task-level relation identification 或下游关系分析作为主贡献；这些方向仅作为后续扩展，用于说明 RefQ relation 与其他关系资产之间的层级接口。RefQ 作为具有明确 membership 与 aggregation contract 的可追溯项目级结构关系，为需要更强语义验证的后续分析提供证据层，但本文不执行或验证这些分析。
~~~

The first paragraph now makes construction the core problem, the third
paragraph states the seed-centered observation constraint, and the fourth
paragraph makes open-source DBMS the bounded empirical instantiation.

### 4.2 §1.4 研究问题与贡献

Before:

~~~text
### 1.4 研究问题与贡献
在上述研究目标下，本文以 GitHub 平台 294 个开源 DBMS 项目作为征引侧种子样本，并基于 GH_CoRE 处理链抽取和组织协作 Reference evidence，通过 artifact-to-project membership-induced graph coarsening 构建 Project-level RefQN；围绕这一对象，本文提出以下研究问题：

- **RQ1**：开源 DBMS 项目的细粒度 Reference 事实从哪些协作场景产生、指向哪些类型的对象，项目内部与外部 Reference 如何分化？
- **RQ2a**：在 Project-level Reference Quotient Network 中，294 个 seed DBMS projects 的主动引用范围和聚合引用强度如何分布，seed-to-seed 与 seed-to-expanded RefQ relations 呈现何种差异？
- **RQ2b**：在 Project-level Reference Quotient Network 中，哪些项目被多个 seed DBMS projects 指向，其被引覆盖与聚合引用强度呈现何种集中结构？
- **RQ2c**：忽略 RefQ relation 的方向后，由 Project-level Reference Quotient Network 派生的无向结构视图呈现何种连通性、局部聚集、模块化邻域和桥接结构？
- **RQ3**：在控制多标签口径、多重检验与观测边界后，不同 DBMS 子领域在细粒度 Reference 构成、RefQ source/target role 及可定义的局部结构指标上呈现哪些稳健差异？

本文的贡献主要体现在四个方面。

第一，**explicit relation formalization / construction contract**：本文将已有 project-level cross-reference aggregation 中通常由数据处理隐含承担的 project mapping 与 aggregation assumptions，显式形式化为 semantic membership quotient，并以 paper-defined RefQ/RefQN 表示；贡献在于 relation semantics、endpoint eligibility、membership、aggregation 和 interpretation contract，而不是新的 graph operator。

第二，**boundary-aware evidence instantiation**：本文在 DBMS 垂直生态中区分 observable fine-grained Reference evidence universe 与 quotient-eligible project-mappable subset，明确 non-project evidence、self-loop、membership-resolution、seed-centered source observation 和 expanded-target asymmetry；“更多实体类型”本身不是贡献。

第三，**observation-aware role-aware empirical characterization**：由于 294 个 seed projects 的 source observation 与 expanded targets 的 source-incomplete 状态不对称，本文将 source role、target role 和 undirected structural view 作为避免抽样诱发误读的分析设计，并结合 RQ1 与 RQ3 形成经验刻画。

第四，**traceable weaker-semantic structural evidence layer**：RefQ 保留 observable Reference evidence 的来源可追溯性和边界，采用比 technical-dependency 或 task-resolution 更弱的推断承诺，为软件生态研究、引用感知工具和需要更强语义验证的后续关系分析提供可复用接口。

总体而言，这五个研究问题依次从细粒度 Reference evidence 的构成出发，进入角色化的项目级 RefQ 结构分析，并进一步考察 DBMS 子领域中受边界约束的异质性。
~~~

After:

~~~text
### 1.4 研究问题与贡献
在上述构造与观测边界下，本文以 GitHub 平台 294 个开源 DBMS 项目作为征引侧种子样本，并基于 GH_CoRE 处理链抽取和组织协作 Reference evidence，通过 artifact-to-project membership-induced graph coarsening 构建 Project-level RefQN。围绕这一关系资产，本文首先通过 RQ1 刻画输入 evidence universe 及其项目可映射边界；随后以 RQ2a–RQ2c 为核心，分别考察 Project-level RefQN 的 source、target 与无向结构视图；最后通过 RQ3 检验该关系资产在 DBMS 子领域划分下的局部差异及其标签敏感性。基于这一层级组织，本文提出以下研究问题：

- **RQ1**：开源 DBMS 项目的细粒度 Reference 事实从哪些协作场景产生、指向哪些类型的对象，项目内部与外部 Reference 如何分化？
- **RQ2a**：在 Project-level Reference Quotient Network 中，294 个 seed DBMS projects 的主动引用范围和聚合引用强度如何分布，seed-to-seed 与 seed-to-expanded RefQ relations 呈现何种差异？
- **RQ2b**：在 Project-level Reference Quotient Network 中，哪些项目被多个 seed DBMS projects 指向，其被引覆盖与聚合引用强度呈现何种集中结构？
- **RQ2c**：忽略 RefQ relation 的方向后，由 Project-level Reference Quotient Network 派生的无向结构视图呈现何种连通性、局部聚集、模块化邻域和桥接结构？
- **RQ3**：在控制多标签口径、多重检验与观测边界后，不同 DBMS 子领域在细粒度 Reference 构成、RefQ source/target role 及可定义的局部结构指标上呈现哪些稳健差异？

本文的贡献主要体现在四个方面。

第一，定义 **explicit relation formalization / construction contract**：本文将已有 project-level cross-reference aggregation 中通常由数据处理隐含承担的 project mapping 与 aggregation assumptions，显式形式化为 semantic membership quotient，并以 paper-defined RefQ/RefQN 表示；贡献在于 relation semantics、endpoint eligibility、membership、aggregation 和 interpretation contract，而不是新的 graph operator。

第二，为保证上述构造的边界可解释性，提出 **boundary-aware evidence instantiation**：本文在 DBMS 垂直生态中区分 observable fine-grained Reference evidence universe 与 quotient-eligible project-mappable subset，明确 non-project evidence、self-loop、membership-resolution、seed-centered source observation 和 expanded-target asymmetry；“更多实体类型”本身不是贡献。

第三，在此基础上，形成 **observation-aware role-aware empirical characterization**：由于 294 个 seed projects 的 source observation 与 expanded targets 的 source-incomplete 状态不对称，本文以 RQ2a、RQ2b 和 RQ2c 为 Project-level RefQN 的结构经验中心，分别分析 source role、target role 和 undirected structural view；RQ1 提供 evidence-boundary 支撑，RQ3 提供受边界约束的 DBMS 子领域比较，并以此避免抽样诱发误读。

第四，由此得到的 RefQ 被定位为 **traceable weaker-semantic structural evidence layer**：RefQ 保留 observable Reference evidence 的来源可追溯性和边界，采用比 technical-dependency 或 task-resolution 更弱的推断承诺，为软件生态研究、引用感知工具和需要更强语义验证的后续关系分析提供可复用接口。

总体而言，上述贡献以项目级 RefQ 构造为核心，以 evidence boundary 与 observation-aware analysis 支撑 Project-level RefQN 的经验刻画，并以 DBMS 子领域比较检验其局部性与标签敏感性。
~~~

The five RQ bullets are byte-identical.  The lead-in makes RQ1 the
input/boundary characterization, RQ2a–RQ2c the structural center, and RQ3 the
bounded DBMS comparison.  The four contributions remain exactly four and are
ordered as core construct, boundary support, empirical validation, and
relation-asset positioning.

### 4.3 §4 opening roadmap

Before:

~~~text
## 4 结果

本节按 RQ1、RQ2a、RQ2b、RQ2c 和 RQ3 的结构组织实证结果。RQ1 以种子 DBMS 项目的有效直接 Reference 记录为基础，分析征引实体、被引实体、自引用、协作指标和 external-reference orientation，而不是扩展网络全部节点；RQ2a 聚焦征引侧 source-role，即 294 个分析种子项目的 out-degree、out-strength、主动引用范围和 seed-to-seed / seed-to-expanded RefQ relations 差异；RQ2b 聚焦被引侧 target-role，即全部可识别目标项目的 in-degree、in-strength、覆盖率和集中结构；RQ2c 聚焦由直接有向引用关系派生出的无向结构视图，用于连通性、局部聚集、Louvain 算法社区结构和 structural brokerage 候选分析，且不构建 shared-reference projection；RQ3 以种子项目的子领域标签、引用类型、项目级网络特征和项目年龄关联变量为基础，重点考察局部性与非均质性差异。
~~~

After:

~~~text
## 4 结果

本节按“证据边界—结构关系—领域比较”的层级组织实证结果。首先，RQ1 以种子 DBMS 项目的有效直接 Reference 记录为基础，刻画 observable evidence universe 及其与 project-level construction 的边界，分析征引实体、被引实体、自引用、协作指标和 external-reference orientation，而不是扩展网络全部节点；其次，RQ2a、RQ2b 和 RQ2c 构成 Project-level RefQN 的核心结构分析，分别聚焦征引侧 source-role，即 294 个分析种子项目的 out-degree、out-strength、主动引用范围和 seed-to-seed / seed-to-expanded RefQ relations 差异，被引侧 target-role，即全部可识别目标项目的 in-degree、in-strength、覆盖率和集中结构，以及由直接有向引用关系派生出的无向结构视图，用于连通性、局部聚集、Louvain 算法社区结构和 structural brokerage 候选分析，且不构建 shared-reference projection；最后，RQ3 以种子项目的子领域标签、引用类型、项目级网络特征和项目年龄关联变量为基础，评估受观测与标签边界约束的局部性与非均质性差异。
~~~

Only the roadmap paragraph changed; all §4.1–§4.3 result subsections are
byte-identical.

### 4.4 §5.4 RQ 归纳与解释边界

Before:

~~~text
### 5.4 RQ 归纳与解释边界

- **RQ1：讨论驱动与内外部 Reference evidence 分化**。DBMS Reference behavior 表现为讨论场景中的 Reference evidence、外部资源指向、项目内部与外部 Reference 并存，以及协作规模、讨论深度和引用密度互补。这一归纳由当前 RQ1 artifacts 与表 4.1 至表 4.6a 支持；external-reference share 只表示可观测证据比例，不直接测量 dependency 或组织开放性。
- **RQ2a/RQ2b/RQ2c：source-role、target-role 与无向派生结构**。RQ2 输出分别给出 source-side range/strength、target-side coverage/concentration 和 undirected structural view。9,595 条 directed cross-project edges 与 9,547 条 undirected edges 具有不同 operator/view provenance，不能混用；canonical 35-community result 只是一个确定性 reference realization，50-seed sensitivity 将其限定为 algorithmic modular neighborhood view；Louvain communities 和 brokerage candidates 也只作算法结构观察。
- **RQ3：子领域差异的局部性与非均质性**。Reference composition 指标未在两种标签口径下通过 FDR；若干 role/local-structure 指标只在 include_mixed 下通过，因此 RQ3 的结论是局部、非均质且 label-mode sensitive，不泛化为所有指标的稳健显著差异。项目年龄始终按 cross-sectional 2023 association 解释。

总体而言，本文的结果为 RefQ 在开源 DBMS 垂直技术生态中的适用性提供了边界化经验依据，也刻画了 DBMS Reference behavior 在协作讨论、外部生态资源、Project-level RefQN 结构和子领域差异上的多层次特征。上述归纳仅依据本文定义的分析范围和报告结果。
~~~

After:

~~~text
### 5.4 RQ 归纳与解释边界

本节按“构造边界—结构刻画—领域比较”归纳结果。首先，**RQ1：构造边界与内外部 Reference evidence 分化**。DBMS Reference behavior 表现为讨论场景中的 Reference evidence、外部资源指向、项目内部与外部 Reference 并存，以及协作规模、讨论深度和引用密度互补；RQ1 由此界定 observable evidence universe 的组成及其进入 project-level construction 的边界，这一归纳由当前 RQ1 artifacts 与表 4.1 至表 4.6a 支持。external-reference share 只表示可观测证据比例，不直接测量 dependency 或组织开放性。

其次，**RQ2a/RQ2b/RQ2c：Project-level RefQN 的核心结构刻画**。三项 RQ 分别给出 source-side range/strength、target-side coverage/concentration 和 undirected structural view。9,595 条 directed cross-project edges 与 9,547 条 undirected edges 具有不同 operator/view provenance，不能混用；canonical 35-community result 只是一个确定性 reference realization，50-seed sensitivity 将其限定为 algorithmic modular neighborhood view；Louvain communities 和 brokerage candidates 也只作算法结构观察。

最后，**RQ3：受边界约束的子领域比较**。Reference composition 指标未在两种标签口径下通过 FDR；若干 role/local-structure 指标只在 include_mixed 下通过，因此 RQ3 的结论是局部、非均质且 label-mode sensitive，不泛化为所有指标的稳健显著差异。项目年龄始终按 cross-sectional 2023 association 解释。

由此，RQ1 提供 evidence-boundary 支撑，RQ2a/RQ2b/RQ2c 构成 Project-level RefQN 的结构经验中心，RQ3 则在 DBMS 垂直场景中检验该关系资产的局部差异及标签敏感性。RefQ 仍是可追溯、弱语义的项目级结构关系，以上归纳仅依据本文定义的分析范围和报告结果。
~~~

The synthesis now follows construction/boundary → structural characterization
→ bounded vertical comparison and returns to the weak-semantic relation asset.
The frozen label-mode-sensitive limitation and all supporting result numbers are
retained.

### 4.5 §9 结论

Before:

~~~text
## 9 结论

本文以 GitHub 平台上的开源 DBMS 项目为征引侧种子样本，基于可观测 fine-grained Reference records，通过 artifact-to-project membership-induced graph coarsening 构建 Project-level RefQN。围绕 RQ1，报告结果显示讨论场景、外部资源指向和项目间 evidence composition 差异。围绕 RQ2a、RQ2b 和 RQ2c，报告结果分别给出 source role 主动引用及 seed-to-seed / seed-to-expanded 差异、target role 覆盖集中和 \(U(G_{\mathrm{RefQ}})\) 无向派生结构结果。围绕 RQ3，Reference composition 仅呈现 descriptive differences，在两种 label mode 下均无 FDR-supported group difference；selected RefQ role/local-structure/project-age features 仅在 include_mixed 下达到阈值，且没有跨 label mode 稳健的 feature。因此，RQ3 的总体结果是局部且 label-mode sensitive。

本文的学术价值不在于重新发明 directed/count-weighted project-reference aggregation 或提出新的 graph algorithm，而在于对这一已有经验操作进行 formalization/reframing。本文将 observable fine-grained Reference evidence universe 与 quotient-eligible project-mappable subset 分开，以 unique semantic membership、endpoint eligibility、block aggregation、self-loop/non-project policy 和 seed-centered observation 共同定义 paper-specific Reference Quotient，并在 DBMS 场景中实例化 Project-level RefQN。该 construction and observation contract 进一步导出 source/target/undirected role separation，支持 Reference behavior、RefQ structure 和子领域差异的边界化经验描述。通过将 fine-grained observable Reference evidence 转换为可追溯、较弱语义的项目级结构关系，RefQ 为软件生态研究、引用感知工具和需要更强语义验证的后续关系分析提供 reusable evidence layer。

RefQ relation 保留引用方向、项目归属和聚合证据强度，但不判定具体引用究竟表示方案参考、问题比较、依赖说明、上下文补充还是实际任务解决。未来工作可以在更严格的证据条件下研究 task-level relation semantics；本文不执行、不验证这些更强语义关系或因果知识流分析。

本文结论受到 GitHub 可观测数据、Reference extraction 规则、membership mapping、quotient construction 口径、时间窗口和统计方法边界的限制。未来研究可进一步结合跨年份数据、引用语义分类、节点 / 边删除仿真和多源协作数据，对算法社区进行人工主题标注，并开展跨年份算法分区稳定性与演化分析，以检验 DBMS Project-level RefQN 结构如何随技术生态变化而演化。shared-reference projection、\(QQ^\top\)、\(Q^\top Q\) 或 \(K=X\Phi X^\top\) 可作为未来工作中的二阶关系方向，但不属于本文当前主实验。
~~~

After:

~~~text
## 9 结论

本文的核心产出是一个可追溯的项目级 RefQ relation：本文不重新发明 directed/count-weighted project-reference aggregation 或提出新的 graph algorithm，而是对这一已有经验操作进行 formalization/reframing。本文将 observable fine-grained Reference evidence universe 与 quotient-eligible project-mappable subset 分开，以 unique semantic membership、endpoint eligibility、block aggregation、self-loop/non-project policy 和 seed-centered observation 共同定义 paper-specific Reference Quotient，并在 DBMS 场景中实例化 Project-level RefQN。该 construction and observation contract 将细粒度证据组织为可解释的项目级结构关系，同时保留 source/target/undirected role separation。

在这一关系资产上，RQ1 提供 evidence composition 及其 project-level construction boundary 的支持；RQ2a、RQ2b 和 RQ2c 构成核心结构刻画，分别考察 source role 的主动引用与 seed-to-seed / seed-to-expanded 差异、target role 的覆盖集中和 \(U(G_{\mathrm{RefQ}})\) 无向派生结构；RQ3 则在 DBMS 垂直场景中比较受边界约束的子领域差异。Reference composition 仅呈现 descriptive differences，在两种 label mode 下均无 FDR-supported group difference；selected RefQ role/local-structure/project-age features 仅在 include_mixed 下达到阈值，且没有跨 label mode 稳健的 feature。因此，RQ3 的总体结果仍是局部且 label-mode sensitive。

RefQ relation 保留引用方向、项目归属和聚合证据强度，但不判定具体引用究竟表示方案参考、问题比较、依赖说明、上下文补充还是实际任务解决。它不等同于 dependency ground truth、task-resolution semantics、knowledge-flow causality 或受控访问/查询功能；需要更强语义验证的后续关系分析不由 RefQ 自动导出。通过将 fine-grained observable Reference evidence 转换为可追溯、较弱语义的项目级结构关系，RefQ 为软件生态研究、引用感知工具和后续关系分析提供 reusable evidence layer。

本文结论受到 GitHub 可观测数据、Reference extraction 规则、membership mapping、quotient construction 口径、时间窗口和统计方法边界的限制。未来研究可进一步结合跨年份数据、引用语义分类、节点 / 边删除仿真和多源协作数据，对算法社区进行人工主题标注，并开展跨年份算法分区稳定性与演化分析，以检验 DBMS Project-level RefQN 结构如何随技术生态变化而演化。shared-reference projection、\(QQ^\top\)、\(Q^\top Q\) 或 \(K=X\Phi X^\top\) 可作为未来工作中的二阶关系方向，但不属于本文当前主实验。
~~~

The conclusion now begins with the constructed relation asset, then identifies
RQ2a–RQ2c as the empirical center, retains RQ1/RQ3 support and limits, and
keeps second-order projections as future work only.

## 5. Diff review and claim-preservation matrix

| Region | Before hierarchy | After hierarchy | Scientific claims changed? | Risk |
|---|---|---|---|---|
| §1.3 | Three co-equal gaps foregrounded domain, construction, and observation | Core construction → observation constraint → DBMS instantiation | No | LOW |
| §1.4 | RQ lead-in and four contributions were largely parallel | RQ1 boundary → RQ2a/b/c structural center → RQ3 bounded evaluation; four contribution roles made sequential | No | LOW |
| §4 opening | RQ1–RQ3 listed in a flat roadmap | Evidence boundary → core RefQN structure → bounded DBMS comparison | No | LOW |
| §5.4 | RQ synthesis was a flat inventory | Construction/boundary → structural characterization → bounded comparison → relation asset | No | LOW |
| §9 | Conclusion opened with a result inventory | Relation construction first, empirical tiers second, boundaries and future work retained | No | LOW |

| Claim / boundary | Before | After | Status |
|---|---|---|---|
| RefQ formalization/reframing | Present | Present | PASS |
| Two-universe boundary | Present | Present | PASS |
| Seed-centered asymmetry | Present | Present | PASS |
| RQ2 structural center | Implicit | Explicit | PASS |
| RQ3 label sensitivity | Present | Present | PASS |
| Weak-semantic relation | Present | Present | PASS |
| Second-order excluded from current study | Present | Present | PASS |
| No task/dependency/causal overclaim | Present | Present | PASS |

## 6. RQ, citation, numeric, and byte closure

The five RQ bullets were extracted by matching the five lines beginning with
RQ1, RQ2a, RQ2b, RQ2c, and RQ3.  The before and after blocks each contain five
lines and are byte-identical:

~~~text
RQ_TEXT_BYTE_IDENTICAL = PASS
RQ_TEXT_CHANGED = 0
RQ_COUNT = 5
RQ_BLOCK_SHA256_BEFORE = 8F4C9079355880F31FBD05C0CCF4A58993D47E74806813595CA99D63D980AE65
RQ_BLOCK_SHA256_AFTER  = 8F4C9079355880F31FBD05C0CCF4A58993D47E74806813595CA99D63D980AE65
~~~

All four figure-caption lines and all 126 Markdown table rows are identical:

~~~text
FIGURE_CAPTION_EDIT_COUNT = 0
FIGURE_CAPTION_CHANGED = 0
FIGURE_CAPTION_BLOCK_SHA256 = 42A03182BADAC2D509D0140CB9B55D427B8C2DC8C160D18F9DC4164A4FA82E38
TABLE_CONTENT_CHANGED = 0
TABLE_ROW_COUNT = 126
TABLE_ROW_BLOCK_SHA256 = 51E43170B2E8C5AD7F7BCF2DFFC55D13272B1E904AB1B4B1C753F7105902A546
~~~

The citation-key multiset is unchanged: 68 occurrences over 31 unique keys,
including the Blincoe and IREL attribution.  A boundary-aware numeric-token
scan (ASCII alphanumeric exclusion on both sides of each numeric token) found
991 tokens before and after, with empty multiset differences.  In particular,
the table-reference tokens retained in §5.4 are not silently dropped.

~~~text
CITATION_SET_CHANGED = 0
CITATION_MULTISET_CHANGED = 0
CITATION_OCCURRENCES_BEFORE = 68
CITATION_OCCURRENCES_AFTER = 68
SCIENTIFIC_NUMERIC_TOKEN_MULTISET_CHANGED = 0
EDITED_REGION_NUMERIC_VALUE_CHANGE_COUNT = 0
NEW_SCIENTIFIC_VALUES = 0
CHANGED_SCIENTIFIC_VALUES = 0
~~~

Working-note and transition checks:

~~~text
WORKING_NOTE_TERM_academic_problem = 0
WORKING_NOTE_TERM_group_by = 0
DUPLICATE_TRANSITION_REINTRODUCED = 0
~~~

## 7. Non-authorized-region byte guard

The five allowed intervals were removed from each UTF-8 manuscript snapshot
using the same heading boundaries, and the concatenated protected bytes were
hashed.  The protected byte stream is identical:

~~~text
PROTECTED_CONCATENATED_UTF8_BYTES_BEFORE = 108731
PROTECTED_CONCATENATED_UTF8_BYTES_AFTER  = 108731
PROTECTED_CONCATENATED_CHAR_COUNT_BEFORE = 71799
PROTECTED_CONCATENATED_CHAR_COUNT_AFTER  = 71799
PROTECTED_CONCATENATED_SHA256_BEFORE = F350B5EA8D067FFF921BDE5E968A4623440A82C4F72C01FD2221C4168ADA89D7
PROTECTED_CONCATENATED_SHA256_AFTER  = F350B5EA8D067FFF921BDE5E968A4623440A82C4F72C01FD2221C4168ADA89D7
UNAUTHORIZED_MANUSCRIPT_REGION_CHANGE_COUNT = 0
~~~

Independent section checks also found zero mismatches outside the authorized
regions.  Frozen section hashes include:

~~~text
ABSTRACT_CHANGED = 0
ABSTRACT_SHA256 = 4F0A4D18C1D870FB0F94944F7F16BE5EE574F7F6EDCAF0B1FD4AAD7D2F32A5F3
SECTION_1_1_CHANGED = 0
SECTION_1_1_SHA256 = 531D82E0FE52E0EF7B087347A28F88A5A789EA2E3B6798F95D3701C6BAAEECB4
SECTION_1_2_CHANGED = 0
SECTION_1_2_SHA256 = 6238C2C99348A50073334CD721E778AD47BB37CC93C2B779A69B3A4ACBFFCC77
RELATED_WORK_CHANGED = 0
METHODS_CHANGED = 0
RESULT_VALUES_CHANGED = 0
RESULT_SUBSECTIONS_AFTER_ROADMAP_CHANGED = 0
DISCUSSION_5_1_TO_5_3_CHANGED = 0
THREATS_CHANGED = 0
AVAILABILITY_CHANGED = 0
APPENDIX_CHANGED = 0
REFERENCES_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
SCIENTIFIC_ASSETS_CHANGED = 0
TABLES_CHANGED = 0
TABLE_CONTENT_CHANGED = 0
FIGURE_CAPTION_CHANGED = 0
FIGURE_CAPTION_EDIT_COUNT = 0
~~~

The repository-side path check at this point showed no tracked-file
modification other than the new freeze record; the four ZIPs remained
untracked and unstaged.  The external manuscript is the single manuscript
file changed, and every changed line falls within the five authorized
intervals.

## 8. Hierarchy and semantic closure

~~~text
CORE_ACADEMIC_PROBLEM = PASS
METHOD_CONSTRAINT = PASS
EMPIRICAL_INSTANTIATION = PASS

RQ_FUNCTIONAL_HIERARCHY_EXPLICIT = PASS
RQ1_BOUNDARY_ROLE = PASS
RQ2ABC_STRUCTURAL_CENTER = PASS
RQ3_BOUNDED_EVALUATION = PASS
RQ3_LABEL_MODE_BOUNDARY = PASS
RESULTS_ROADMAP_STRUCTURE_CENTER = PASS

CONTRIBUTION_COUNT = 4
CONTRIBUTION_1_CORE_CONSTRUCT = PASS
CONTRIBUTION_2_BOUNDARY_SUPPORT = PASS
CONTRIBUTION_3_EMPIRICAL_VALIDATION = PASS
CONTRIBUTION_4_RELATION_ASSET_POSITIONING = PASS
NOVELTY_STRENGTHENING = 0

FACT_LAYER_LEAKAGE = NO
STRUCTURE_LAYER_DILUTION = NO
TASK_LAYER_LEAKAGE = NO
ACCESS_LAYER_LEAKAGE = NO

CONCLUSION_STRUCTURE_FIRST = PASS
CONCLUSION_RQ2_EMPIRICAL_CENTER = PASS
CONCLUSION_WEAK_SEMANTIC_BOUNDARY = PASS
SECOND_ORDER_REMAINS_FUTURE_WORK = PASS
~~~

The preferred self-contained Chapter-5 story is:

~~~text
fine-grained Reference evidence
→ observable evidence is not identical to quotient-eligible evidence
→ endpoint eligibility + semantic membership
→ membership-induced aggregation
→ Project-level RefQ / RefQN
→ seed-centered role and view separation
→ RQ2a/b/c structural characterization
→ RQ1 boundary support + RQ3 bounded DBMS comparison
→ traceable weaker-semantic structural relation asset
~~~

~~~text
PREFERRED_CHAPTER5_STORY = PASS
~~~

No manuscript-facing prose claims that RefQ is a dependency, task, causal, or
access relation.  No dissertation chapter numbers or internal framework terms
were introduced into the manuscript.

## 9. Experiment and scientific immutability guards

This was a narrative role-assignment task only.  Reframing is required for the
paper story; a new experiment is not required.

~~~text
EXPERIMENT_REFRAMING_NEEDED = YES
NEW_EXPERIMENT_NEEDED = NO
SCIENTIFIC_RECOMPUTATION = 0

P0_RUN = 0
S1_RUN = 0
S2_RUN = 0
S3_RUN = 0
S4_RUN = 0
S5_RUN = 0
S6_RUN = 0
S7_RUN = 0
GH_CORE_RUN = 0
EVENT_REJOIN = 0
SECOND_ORDER_PROJECTION_RUN = 0
FIGURE_RERENDER = 0

manuscript_files_changed = 1
figure_assets_changed = 0
scientific_assets_changed = 0
tables_changed = 0
figure_caption_changed = 0
RQ_TEXT_CHANGED = 0
NEW_SCIENTIFIC_VALUES = 0
CHANGED_SCIENTIFIC_VALUES = 0
~~~

## 10. Final status fields

~~~text
SECTION_1_3 = CHANGED
SECTION_1_4 = CHANGED
RESULTS_ROADMAP = CHANGED
DISCUSSION_5_4 = CHANGED
CONCLUSION_9 = CHANGED

ABSTRACT_CHANGED = 0
SECTION_1_1_CHANGED = 0
SECTION_1_2_CHANGED = 0
RELATED_WORK_CHANGED = 0
METHODS_CHANGED = 0
RESULT_VALUES_CHANGED = 0
DISCUSSION_5_1_TO_5_3_CHANGED = 0
THREATS_CHANGED = 0
AVAILABILITY_CHANGED = 0
APPENDIX_CHANGED = 0
FIGURE_CAPTION_EDIT_COUNT = 0
TABLE_CONTENT_CHANGED = 0

UNAUTHORIZED_MANUSCRIPT_REGION_CHANGE_COUNT = 0
RQ_TEXT_BYTE_IDENTICAL = PASS
RQ_FUNCTIONAL_HIERARCHY_EXPLICIT = PASS
PREFERRED_CHAPTER5_STORY = PASS

repository_HEAD_before = c4dedeb0ff718ea09ad7203abedabeb8be76bcdd
remote_HEAD_before = c4dedeb0ff718ea09ad7203abedabeb8be76bcdd
manuscript_SHA_before = 8D2C8F0A8E3D57B98F388D1B84E7AEAC3192A6D16B79BB087F6202D53420CB9B
manuscript_SHA_after = 8ABC48751979461E2E8CC7389731FEB6BA5A6335CDF05706265BD1B4ED50248B
audit_record = docs/freeze/ch5_refq_framework_derived_hierarchy_rewrite.md
commit_message = docs(ch5): record framework-derived hierarchy rewrite
commit_hash = reported from the final repository HEAD after this docs-only commit
push_status = reported after remote verification
~~~

The only repository file authorized for the resulting commit is this
documentation record.  The final commit hash and push status are filled after
the docs-only commit is created and verified.
