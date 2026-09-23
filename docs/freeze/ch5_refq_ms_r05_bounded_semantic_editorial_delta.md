# MS-R05 Bounded Semantic Editorial Delta

## Identity

```text
TASK = CH5_REFQ_MS_R05_BOUNDED_SEMANTIC_EDITORIAL_CORRECTION
BASE_REVISION = MS-R04
BASE_SHA = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
NEW_REVISION = MS-R05
TRIGGER = STYLE-A02 source-level semantic adjudication
TRIGGER_ISSUES = R02-001, R02-043, R02-050, R02-054
SCIENTIFIC_BASELINE = P0-v3
SCIENTIFIC_RECOMPUTATION = 0
SOURCE_UNIT_PARTITION_CHANGED = NO
SOURCE_UNIT_COUNT = 222
MS_R05_SHA = 30491279BC31CC5012042F72E3BA8159DCF182CECEEB62EFF5C865C78B059B22
```

This is a bounded source-semantic delta. It preserves the existing source-unit
partition and records exact MS-R04 text before the authorized edits.

## Edited source units

### THREAT-U002 — R02-001

**MS_R04_TEXT (exact):**

> 本文使用 GitHub 协作日志中的 Reference relation 近似刻画项目间显式知识指向和协作上下文，但 observable Reference evidence 不等同于完整知识流动构念。部分知识流动可能发生在邮件列表、即时通讯、会议、设计文档、发布说明、论坛或私有讨论中，无法被 GitHub 引用日志覆盖。因此，本文结论应理解为基于可观测 GitHub Reference evidence 的项目关联证据，而不是 DBMS 生态全部知识流动的完整刻画。

**MS_R05_TEXT (target):**

> 本文使用 GitHub 协作日志中的 Reference relation 刻画可观测的显式引用指向及其协作上下文，并据其中满足 project-mappable 条件的 evidence 构造项目级 RefQ 关系。Reference evidence 的观测范围限于 GitHub 上可抽取的显式引用痕迹；邮件列表、即时通讯、会议、设计文档、发布说明、论坛或私有讨论中的信息交换不在当前观测范围内。因此，本文结论应理解为基于可观测 GitHub Reference evidence 的项目关联证据，而不是对知识流动过程的测量或完整刻画。

| Field | Value |
|---|---|
| CHANGE_TYPE | bounded construct-validity re-anchoring |
| WHY_REQUIRED | removes affirmative partial-knowledge-flow proxy residue while preserving observable-channel limits |
| SCIENTIFIC_VALUE_CHANGE | 0 |
| CITATION_CHANGE | 0 |
| FORMULA_CHANGE | 0 |
| OBSERVATION_CONTRACT_CHANGE | 0 |
| FIGURE_ASSET_CHANGE | 0 |
| ENGLISH_FOLLOWUP_REQUIRED | YES |

### INTRO-U011 — R02-054

**MS_R04_TEXT (exact):**

> 这一构造问题还受到观测边界的约束。本文只完整观测 294 个 seed DBMS projects 的 source 行为；expanded target nodes 主要因为被 seed projects 引用而进入网络，其 source behavior 并未完整观测。因此，必须分离 source role、target role 和 direction-ignored first-order structural view，避免将 expanded targets 的低 out-degree 误读为项目行为特征。

**MS_R05_TEXT (target):**

> 这一构造问题还受到观测边界的约束。本文只完整观测 294 个 seed DBMS projects 的 source 行为；expanded target nodes 因被 seed projects 引用而进入网络，其 source behavior 并未完整观测。因此，必须分离 source role、target role 和 direction-ignored first-order structural view，避免将 expanded targets 的低 out-degree 误读为项目行为特征。

| Field | Value |
|---|---|
| CHANGE_TYPE | formal admission-path wording correction |
| WHY_REQUIRED | removes an unsupported alternate-entry implication from the observation contract |
| SCIENTIFIC_VALUE_CHANGE | 0 |
| CITATION_CHANGE | 0 |
| FORMULA_CHANGE | 0 |
| OBSERVATION_CONTRACT_CHANGE | 0 |
| FIGURE_ASSET_CHANGE | 0 |
| ENGLISH_FOLLOWUP_REQUIRED | YES |

### RES-RQ1-U002 — R02-043

**MS_R04_TEXT (exact):**

> **图 1 Observable Reference evidence 与 project-mappable boundary。** (A) 294 个 analysis seed projects 的 Reference-record flow：从 3,748,078 条 scanned input records 经 source-admission，排除 120 条 out-of-seed records，保留 3,747,958 条 admitted source-observation records，并按 target membership 分为 1,586,047 条 project-mappable、1,686,729 条 non-project 和 475,182 条 unresolved records；(B) admitted-record universe 中八类 source event 的完整构成；(C) 各 event type 内 project-mappable、non-project 与 unresolved target 的比例。图中所有计数均为 Reference records；只有可唯一映射到项目的 project-mappable 子集进入 Project-level RefQN，外部或 non-project resource 不因此成为项目节点，图示也不等同于最终网络拓扑。

**MS_R05_TEXT (target):**

> **图 1 Observable Reference evidence 与 project-mappable boundary。** (A) 294 个 analysis seed projects 的 Reference-record flow：从 3,748,078 条 scanned input records 经 source-admission，排除 120 条 out-of-seed records，保留 3,747,958 条 admitted source-observation records，并按 target membership 分为 1,586,047 条 project-mappable、1,686,729 条 non-project 和 475,182 条 unresolved records；(B) admitted-record universe 中八类征引实体类型的完整构成；(C) 各 event type 内 project-mappable、non-project 与 unresolved target 的比例。图中所有计数均为 Reference records；只有可唯一映射到项目的 project-mappable 子集进入 Project-level RefQN，外部或 non-project resource 不因此成为项目节点，图示也不等同于最终网络拓扑。

| Field | Value |
|---|---|
| CHANGE_TYPE | source-category terminology harmonization |
| WHY_REQUIRED | aligns Figure 1B with the frozen source-side entity-type field and GH_CoRE schema distinction from event_type |
| SCIENTIFIC_VALUE_CHANGE | 0 |
| CITATION_CHANGE | 0 |
| FORMULA_CHANGE | 0 |
| OBSERVATION_CONTRACT_CHANGE | 0 |
| FIGURE_ASSET_CHANGE | 0 |
| ENGLISH_FOLLOWUP_REQUIRED | YES |

### RES-RQ1-U005 — R02-043

**MS_R04_TEXT (exact):**

> **表 4.1 征引实体类型分布统计**
>
> | 征引实体类型 | 引用次数 | 占比（%） |
> |---|---:|---:|

**MS_R05_TEXT (target):**

> **表 4.1 征引实体类型（referencing entity types）分布统计**
>
> | 征引实体类型（referencing entity type） | 引用次数 | 占比（%） |
> |---|---:|---:|

| Field | Value |
|---|---|
| CHANGE_TYPE | canonical source-category label clarification |
| WHY_REQUIRED | records the Chinese and English canonical name without changing table values or order |
| SCIENTIFIC_VALUE_CHANGE | 0 |
| CITATION_CHANGE | 0 |
| FORMULA_CHANGE | 0 |
| OBSERVATION_CONTRACT_CHANGE | 0 |
| FIGURE_ASSET_CHANGE | 0 |
| ENGLISH_FOLLOWUP_REQUIRED | YES |

### METH-U066 — R02-043

**MS_R04_TEXT (exact):**

> 1. **引用实体分布维度**：
>    - **征引实体（Referencing Entity）**：主动发起引用的行为载体，包括IssueComment、Push、PullRequest、Issue等，用于分析不同协作场景的引用发起特征；
>    - **被引实体（Referenced Entity）**：被引用的资源对象，除了征引实体的类型外，还包括GitHub_Service_External_Links、PullRequest、Actor、Commit、Issue等，用于刻画可观测的被引对象构成。

**MS_R05_TEXT (target):**

> 1. **引用实体分布维度**：
>    - **征引实体类型（referencing entity type）**：本文沿用 GH_CoRE 的 Entity 类型抽象，将可作为 Reference endpoint 参与关系抽取的 typed records/objects 统一表示为 ObjEntity 类型，其中包括 IssueComment、Push、PullRequest、Issue 和 Release 等；GH_CoRE 的关系输出同时区分 `src_entity_type`、`tar_entity_type` 与 `event_type`，本文的征引侧类别统计按冻结分析实际使用的 source-side entity-type 字段解释。征引实体类型是主动发起引用的行为载体，用于分析不同协作场景的引用发起特征；
>    - **被引实体类型（referenced entity type）**：被引用的资源对象，除了征引实体类型外，还包括GitHub_Service_External_Links、PullRequest、Actor、Commit、Issue等，用于刻画可观测的被引对象构成。

| Field | Value |
|---|---|
| CHANGE_TYPE | bounded GH_CoRE schema clarification and label harmonization |
| WHY_REQUIRED | explains schema-level Entity terminology and distinguishes source entity type from event type |
| SCIENTIFIC_VALUE_CHANGE | 0 |
| CITATION_CHANGE | 0 |
| FORMULA_CHANGE | 0 |
| OBSERVATION_CONTRACT_CHANGE | 0 |
| FIGURE_ASSET_CHANGE | 0 |
| ENGLISH_FOLLOWUP_REQUIRED | YES |

## R02-050 appendix-role corrections

### AVAIL-U004

**MS_R04_TEXT (exact):**

> 附录 A 作为 reproducibility and boundary appendix，记录 reproducibility identity、membership/observation audits、analysis-to-RQ mapping 以及 statistical/semantic boundaries，用于支撑主文发现的可追溯性与解释边界。其内容是技术 provenance 记录，不构成独立的公共归档或数据与代码可用性声明；详细 provenance 与复现细节不作为主文结果的解释依据。

**MS_R05_TEXT (target):**

> 附录 A 作为复现与边界记录，记录 reproducibility identity、membership/observation audits、analysis-to-RQ mapping 以及 statistical/semantic boundaries，用于支持结果复现、溯源与对正文既定解释边界的核查。其内容不新增经验解释，也不作为超出正文结论范围的独立解释依据。

| Field | Value |
|---|---|
| CHANGE_TYPE | appendix interpretive-role reconciliation |
| WHY_REQUIRED | separates reproduction/traceability/boundary verification from new empirical interpretation |
| SCIENTIFIC_VALUE_CHANGE | 0 |
| CITATION_CHANGE | 0 |
| FORMULA_CHANGE | 0 |
| OBSERVATION_CONTRACT_CHANGE | 0 |
| FIGURE_ASSET_CHANGE | 0 |
| ENGLISH_FOLLOWUP_REQUIRED | YES |

### APP-U001

**MS_R04_TEXT (exact):**

> 本附录记录运行身份、membership/observation records、artifact-to-RQ 映射和解释边界，用于支持结果复现与语义解释。

**MS_R05_TEXT (target):**

> 本附录记录运行身份、membership/observation records、artifact-to-RQ 映射和解释边界，用于支持结果复现、溯源与正文既定解释边界的核查；不新增正文之外的经验解释。

| Field | Value |
|---|---|
| CHANGE_TYPE | appendix transition-role clarification |
| WHY_REQUIRED | aligns the appendix introduction with the bounded role stated in Section 8 |
| SCIENTIFIC_VALUE_CHANGE | 0 |
| CITATION_CHANGE | 0 |
| FORMULA_CHANGE | 0 |
| OBSERVATION_CONTRACT_CHANGE | 0 |
| FIGURE_ASSET_CHANGE | 0 |
| ENGLISH_FOLLOWUP_REQUIRED | YES |

## GH_CoRE provenance for R02-043

```text
GH_CORE_MAIN_COMMIT = f4216351ffe62d71c571df08e80decc258d6125a
GH_CORE_ENTITY_MODEL_BLOB = 1c0604c8d062877889f662190ef03d39f961adaa
GH_CORE_RELATION_EXTRACTION_BLOB = b089c84a2214846e31b2722d1bb6f550d2ecf9ba
GH_CORE_MAIN_COMMIT_CHECK = PASS
GH_CORE_ENTITY_MODEL_BLOB_SHA_CHECK = PASS
GH_CORE_RELATION_EXTRACTION_BLOB_SHA_CHECK = PASS
SCHEMA_EVIDENCE = ObjEntity.E includes Push and Release; get_df_collaboration exports src_entity_type, tar_entity_type, and event_type separately.
DICTIONARY_ASSIGNMENT_NOTE = set_val() performs dictionary-backed setattr; apply_F() derives/fills missing fields according to F and is not the primary dictionary-ingestion operation.
TABLE41_CATEGORY_SOURCE_FIELD = src_entity_type
FIGURE1B_CATEGORY_SOURCE_FIELD = src_entity_type
SOURCE_ENTITY_AND_EVENT_TYPE_DISTINCT_IN_GH_CORE = YES
```

## Global delta guards

```text
RQ_COUNT = 5
CONTRIBUTION_COUNT = 4
CITATION_KEY_CHANGE = 0
FORMULA_CHANGE = 0
TABLE_NUMERIC_VALUE_CHANGE = 0
FIGURE_VALUES_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
SCIENTIFIC_RECOMPUTATION = 0
```
