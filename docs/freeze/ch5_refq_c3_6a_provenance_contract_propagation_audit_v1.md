# Chapter 5 RefQ C3.6-A Provenance Contract Propagation Audit v1

审计日期：2026-08-26
Repository：`D:\github_repo\OSDB_RefQ`
Branch：`ch5-refq-repository-identity-correction-v1`
HEAD：`68054dceaebc14ecdf29ac9d0b209f28301fd7a4`

## 1. 审计范围与直接回答

本审计只检查 repository identity provenance 从 raw event 到 supplemental
S1-S6 的传播。没有修改代码，没有运行 P0/S1-S7，没有生成 figures，没有
修改 historical outputs 或 manuscript，也没有 commit/push。

| 问题 | 结论 |
|---|---|
| `repository_identity_provenance.py` 和 P0 v2 pipeline 是否足够？ | **对 corrected P0 的身份 join、schema 校验和 source admission：足够。对 supplemental：尚未接入。** |
| supplemental S1 能否直接消费 corrected aggregate？ | **能，在最小 schema/adapter patch 后可以直接消费；当前 v1 S1 代码不能直接消费。** |
| 是否需要再次 event rejoin？ | **不需要作为 corrected aggregate 的最小路径。** corrected aggregate 已经包含 provenance join 结果和 admission 字段；只有在直接消费 v2 relation、或需要独立复核 aggregate provenance 时才需要 rejoin。 |
| 最小 patch 是什么？ | 把 corrected aggregate 的 provenance/admission 字段加入 S1 读取和 staging schema，在 membership/eligibility 前执行 admission filter，并记录 rejected counters。 |
| 科学逻辑是否改变？ | **不改变。** `Q=M^T R_P M`、target parsing、membership rule、weight/multiplicity semantics 和 S2-S6 的分析逻辑不变；变化仅是把 S1 输入边界与 corrected P0 对齐。 |

## 2. Current data flow diagram / 当前数据流图

### 2.1 已有 corrected P0 传播

```text
raw event CSV
  repos_dedup_content/<seed>_2023.csv
  fields: id, repo_id, repo_name
        |
        | event_id == raw id
        v
repository_identity_provenance.attach_event_repository_provenance()
  script/build_dataset/repository_identity_provenance.py:160-240
  adds: event_repo_id, event_repo_name,
        event_repo_provenance_status
        |
        v
corrected v2 relation
  repos_GH_CoRE_v2_identity_corrected/
  relation schema v2
        |
        | aggregate materialization derives source aggregate from event_repo_id
        v
corrected v2 aggregate
  repos_GH_CoRE_ref_node_agg_v2_identity_corrected/
  adds/retains:
    event_repo_id
    expected_source_context_repo_id
    source_admission_status
    source_provenance_mismatch
    src_entity_id_agg / target aggregate fields
        |
        v
P0 v2 strict source observation boundary
  script/ch5_reference_quotient/pipeline.py:78-159
  filter before MembershipRegistry and _scan_evidence()
        |
        v
outputs/reference_quotient_p0_corrected_v2/
  quotient tables, RQ tables, audits, manifest
```

这条 corrected P0 链路已经存在。C2/C2.5 records 表明 294 个 aggregate
partitions完成 provenance join，`MATCHED_UNIQUE = 12,518,072`，没有
`RAW_REPO_ID_MISSING`、`RELATION_EVENT_UNMATCHED` 或
`RELATION_EVENT_MULTI_MATCH`；corrected P0 manifest 和 membership/quotient
audits 为 `PASS`。

### 2.2 Missing propagation boundary / 当前 supplemental S1 的断点

```text
corrected v2 aggregate exists
        |
        X  current S1 does not read the v2 provenance columns
        |
supplemental/reference_quotient_v1/scripts/run_supplemental.py
  imports RAW_USECOLS from common.py:22-26
  reads historical v1 aggregate directory: run_supplemental.py:53-57
  reads only selected entity/target/event columns: run_supplemental.py:102
  stores seed_project/source_agg/target_agg but not admission fields
        |
        X  source membership is computed from source_agg before a v2 admission gate
        |
S1 -> S2/S3/S4/S5 -> S6
```

这里的断点是 **supplemental propagation boundary**，不是 raw data identity
缺失，也不是 corrected P0 identity pipeline 失败。

## 3. 分层字段审计

| layer | current path | relevant fields | propagation status | finding |
|---|---|---|---|---|
| raw event | `D:\github_repo\OSDB_RefQ_source_data\data\github_osdb_data\repos_dedup_content\<seed>_2023.csv` | `id`, `repo_id`, `repo_name` | `PRESENT` | raw event 的实际仓库 numeric ID 可用；`repo_name` 仅作描述，不是最终 identity key |
| historical relation | `.../repos_GH_CoRE/<seed>_2023.csv` | `event_id`，实体和 relation fields | `MISSING_PROVENANCE` | 可通过 `event_id` 定位 raw event，但 v1 relation 本身没有 `event_repo_id` |
| corrected relation | `.../repos_GH_CoRE_v2_identity_corrected/<seed>_2023.csv` | `event_id`, `event_repo_id`, `event_repo_name`, `event_repo_provenance_status`, `relation_schema_version` | `PRESENT` | 已完成 raw event provenance attachment；此层还没有 seed-specific admission context 的全部字段 |
| corrected aggregate | `.../repos_GH_CoRE_ref_node_agg_v2_identity_corrected/<seed>_2023.csv` | 四个 explicit contract fields，加 aggregate/source/target fields | `PRESENT` | S1 可以直接消费的正确输入层；保留 admitted 与 rejected rows供审计 |
| P0 v2 input reader | `script/ch5_reference_quotient/pipeline.py:202-256,307-359` | strict v2 usecols 显式读取前三个 admission fields；`source_provenance_mismatch` 在 corrected aggregate 中存在，但 P0 通过 event/context/status 重新验证等价条件 | `PRESENT_AND_ENFORCED` | `_prepare_reference_evidence_chunk()` 在 membership 和 evidence scan 前过滤 |
| P0 v2 output tables | `outputs/reference_quotient_p0_corrected_v2/` | aggregate-level counts/audits、project/network/RQ outputs | `DERIVED_SUMMARY` | 正确性已反映在 output；多数 P0 output 不保存每条记录的四个 admission fields |
| P0 v2 provenance sample | `outputs/reference_quotient_p0_corrected_v2/refq_provenance_sample.csv` | source/target project、entity、`event_id`、event time、source evidence file | `PARTIAL_TRACE` | 可以追溯部分 admitted evidence，但不能代替完整 corrected aggregate 的 row-level admission source |
| current supplemental S1 | `supplemental/reference_quotient_v1/scripts/run_supplemental.py:91-143,178-230` | `seed_project`, source/target aggregate、event/type fields | `NOT_PROPAGATED` | `event_repo_id` 等没有进入 RAW_USECOLS、SQLite staging 或 admission filter |
| current S2-S6 | `run_supplemental.py:306-494` | P0 edge/role/network tables and same-run S4/S5 outputs | `DOWNSTREAM_ONLY` | 只要 corrected P0-derived inputs和corrected S4/S5 root正确，通常不需要逐行 event provenance；它们依赖 S1/P0 已经正确完成边界过滤 |

## 4. 四个 explicit contract fields

### 4.1 字段含义

| field | origin | meaning | S1 retention requirement | admission invariant |
|---|---|---|---|---|
| `event_repo_id` | raw event `repo_id`，经 `event_id` join 后规范化为 decimal string | 事件实际所属仓库；事实字段 | 必须在 S1 staging/provenance audit 中保留；不允许用 filename、repo_name lookup 或 caller seed ID 填充 | admitted row 必须满足 `event_repo_id == expected_source_context_repo_id` |
| `expected_source_context_repo_id` | 当前 seed 的 numeric repo ID，由 seed manifest/context 生成 | 当前分析上下文的断言字段，不是事件事实 | 必须保留并写入 S1 audit；用于证明每行比较的是哪个 seed | 必须等于当前 seed repo ID；缺失/invalid/context mismatch 应阻断 |
| `source_admission_status` | 由 `admit_source_record()` 或等价逻辑根据 event/context 比较生成 | source row 是否属于当前 seed observation | 必须保留 status counts；只有 `ADMITTED_SOURCE_OBSERVATION` 进入 S1 analytical universe | admitted status 必须与 `event_repo_id == expected...` 一致 |
| `source_provenance_mismatch` | admission comparison 的布尔审计结果 | 是否发生 source provenance mismatch | 必须保留或至少汇总；admitted rows 的值必须全为 `False` | `True` 行不得进入 membership、profile、quotient 或 network |

### 4.2 S1 还必须保留的追溯字段

四个 explicit contract fields 之外，S1 row-level staging 至少还需要：

```text
event_id
relation_type
event_type
src_entity_id
src_entity_type
tar_entity_id
tar_entity_type
src_entity_id_agg
src_entity_type_agg
tar_entity_id_agg
tar_entity_type_agg
tar_entity_type_fine_grained
```

原因如下：

- `event_id` 是 provenance join 和 row-level audit 的追踪键；
- `relation_type` 用于先筛选 `Reference`；
- source/target entity 与 aggregate fields 是 S1 的 membership、entity-type
  cross-tab 和 edge-class 计算输入；
- `event_type` 是 S1 event-type cross-tab 的输入。

以下字段不是 S1 数值计算的最低必要字段，但建议保存在 provenance audit
或 manifest 中：

```text
event_repo_name
event_repo_provenance_status
aggregate_schema_version
```

其中 `event_repo_name` 是描述性字段，不能用作 identity；
`event_repo_provenance_status` 是 raw/relation join 状态，不能与
`source_admission_status` 混为一谈。

## 5. `repository_identity_provenance.py` 与 P0 v2 是否足够

### 5.1 已经足够的部分

[`repository_identity_provenance.py`](D:/github_repo/OSDB_RefQ/script/build_dataset/repository_identity_provenance.py:36)
已经提供：

1. `normalize_repository_id()`：将 numeric ID 规范化为 canonical decimal string；
2. `attach_event_repository_provenance()`：通过 relation `event_id` 与 raw event
   `id` join，取 raw `repo_id/repo_name`；
3. `assert_provenance_join_pass()`：阻断 unmatched、multi-match 和 conflict；
4. `annotate_source_admission()`：生成 `expected_source_context_repo_id`、
   `source_admission_status` 和 `source_provenance_mismatch`；
5. `require_corrected_relation_schema()`：拒绝 legacy relation schema。

[`pipeline.py`](D:/github_repo/OSDB_RefQ/script/ch5_reference_quotient/pipeline.py:42)
已经定义 v2 admission schema，并在
[`pipeline.py`](D:/github_repo/OSDB_RefQ/script/ch5_reference_quotient/pipeline.py:78)
的 `_prepare_reference_evidence_chunk()` 中：

- 检查三项 admission schema；
- 规范化 `event_repo_id` 和 expected context；
- 检查 `source_admission_status` 是否与 event identity 一致；
- 检查 admitted row 是否真的属于当前 seed；
- 只把 admitted `Reference` rows 返回给 downstream。

`_audit_memberships()` 和 `_scan_evidence()` 都调用该 boundary，因此过滤
发生在 membership 和 quotient evidence processing 之前。

### 5.2 尚未足够的部分

这些能力尚未被 supplemental S1 调用。当前 S1：

- 读取 historical v1 aggregate path；
- `RAW_USECOLS` 不包含四个 explicit contract fields；
- SQLite staging 不保存四个 fields；
- 直接从 `src_entity_id_agg` 推断 source project；
- 没有在 membership collection 前执行 v2 admission。

所以结论是：

```text
P0_v2_identity_contract = SUFFICIENT
P0_v2_source_admission = ENFORCED
supplemental_S1_propagation = NOT_CONNECTED
```

## 6. corrected aggregate 能否被 S1 直接消费

### 6.1 结论：可以，但不是当前实现的“直接”

corrected aggregate 的 header 已包含：

```text
event_repo_id
event_repo_name
event_repo_provenance_status
expected_source_context_repo_id
source_admission_status
source_provenance_mismatch
aggregate_schema_version
```

因此 S1 不需要再次读取 raw event 或重新做 `event_id -> raw.id` join，前提是：

1. corrected aggregate manifest/partition audit 已证明 provenance join 是
   `MATCHED_UNIQUE`；
2. aggregate schema version 是 corrected v2；
3. S1 对四个 fields 做 schema、type、status 和 context validation；
4. S1 仅将 admitted rows 纳入 analytical universe，同时记录 rejected counts。

### 6.2 什么时候 event rejoin 才是必需的

event rejoin 只在以下情况下成为必需：

- S1 直接读取 corrected v2 relation，而 relation 中只有
  `event_repo_id`/provenance status，尚未生成 seed-specific admission fields；
- corrected aggregate 缺少四个字段或其 provenance manifest 不可验证；
- 需要独立复核 aggregate 内的 `event_repo_id` 是否确实等于 raw event 的
  `repo_id`；
- 发现 `event_repo_provenance_status` 不是全部 safe/matched，或出现 schema
  mismatch。

在当前仓库状态下，C2 candidate review 已记录全量 event join gate：

```text
MATCHED_UNIQUE = 12,518,072
RAW_REPO_ID_MISSING = 0
RELATION_EVENT_UNMATCHED = 0
RELATION_EVENT_MULTI_MATCH = 0
```

所以“为 S1 corrected aggregate 消费而再次 rejoin”不是最小方案；“保留
event_id 并在 manifest 中引用既有 join audit”是必要的 provenance trace。

## 7. Minimal adapter/schema patch proposal / 最小 adapter/schema patch proposal

本节是设计审计，不是实现授权。

### 7.1 Input path

将 S1 输入从：

```text
repos_GH_CoRE_ref_node_agg/
```

切换为：

```text
repos_GH_CoRE_ref_node_agg_v2_identity_corrected/
```

该路径已在 `configs/ch5_reference_quotient_p0_v2.yaml` 的
`gh_core_ref_node_agg_dir` 中定义。S1 不能依赖文件名隐含 source identity。

### 7.2 Read schema

`RAW_USECOLS` 及等价 v1.1 列表至少扩展为 current S1 columns 加：

```text
event_repo_id
expected_source_context_repo_id
source_admission_status
source_provenance_mismatch
```

建议同时读取：

```text
event_repo_name
event_repo_provenance_status
aggregate_schema_version
```

`event_id` 当前已经在 relation/aggregate header 和 S1 usecols 中，必须继续保留。

### 7.3 Staging schema

当前 S1 SQLite `raw_records` 表需要新增四个 explicit contract columns，
并保留 `event_id`。不要只在 pandas 临时 frame 中读取后丢弃，否则后续
validation 无法审计实际 admitted rows。

### 7.4 Filter boundary

S1 的 logical view 应采用以下顺序：

```text
read corrected aggregate row
  -> validate relation_type == Reference
  -> validate expected_source_context_repo_id == current seed repo_id
  -> validate source_admission_status contract
  -> validate event_repo_id == expected_source_context_repo_id for admitted rows
  -> validate source_provenance_mismatch == False for admitted rows
  -> retain admitted rows for membership/cross-tabs/edge-class tables
  -> count rejected rows by admission status for provenance audit
```

禁止的顺序是：

```text
build membership from src_entity_id_agg
  -> build source profile or edge
  -> later inspect source admission
```

这会使 out-of-seed rows先污染 S1 的 membership 或 source denominators。

### 7.5 Output and manifest

S1 output 应至少记录：

```text
input aggregate root
input aggregate schema version
corrected P0 manifest SHA-256
per-partition source admission counts
admitted Reference rows
out-of-seed Reference rows
missing event_repo_id rows
invalid event_repo_id rows
source_provenance_mismatch after admission
```

`source_provenance_mismatch_after_admission` 必须为 0；拒绝行不进入 S1
analytical totals，但不能从 provenance audit 中物理消失。

## 8. Scientific logic impact / 对科学逻辑的影响

### 8.1 不改变的内容

最小 adapter 不改变：

- `Reference` relation filtering semantics；
- target entity parsing 和 target project expansion；
- unique membership rule；
- `Q=M^T R_P M` 和 first-order directed quotient；
- self-loop policy；
- `weight`/Reference-record multiplicity contract；
- S2 threshold values、S3 view definitions、S4 seeds、S5 brokerage parameters；
- S6 transformations。

### 8.2 会改变的内容

它会使 S1 与 corrected P0 使用相同的 source observation universe，因此：

- Fireproof 的 120 个 out-of-seed rows 不再进入 S1 admitted universe；
- source/target/event cross-tabs、eligible totals 和 edge-class tables 会变化；
- S2-S6 如果基于 corrected P0 或 corrected S1/S3/S4/S5 派生，也会使用 corrected
  baseline 数值。

这属于 corrected input boundary 的既定影响，不是新增的科学模型或第二阶网络
逻辑。当前 corrected P0 的 `quotient_construction_audit.json` 已记录：

```text
source_out_of_seed_reference_rows = 120
source_mismatch_after_admission = 0
source_seed_membership_mismatch = 0
quotient_eligible_records = 1,586,047
```

## 9. 最小验证清单

在未来任何 S1-S6 regeneration 授权前，adapter 至少需要通过：

1. 每个 294 aggregate partition 都具备四个 explicit contract fields；
2. corrected aggregate schema/version 与 v2 manifest 一致；
3. `event_repo_id` 可以规范化为 non-negative decimal ID 或明确记录 missing/invalid；
4. admitted rows 的 `event_repo_id == expected_source_context_repo_id`；
5. admitted rows 的 `source_admission_status == ADMITTED_SOURCE_OBSERVATION`；
6. admitted rows 的 `source_provenance_mismatch == False`；
7. rejected rows按 status 计数，不能静默丢失；
8. `event_id`、source/target aggregate fields 和 relation type 保持可追溯；
9. S1 analytical rows 与 corrected P0 的 admitted/reference counters 对齐；
10. historical P0、historical supplemental roots 和 manuscript 没有字节变化。

## 10. 最终状态

```text
C3_6A_PROVENANCE_CONTRACT = P0_V2_SUFFICIENT
CORRECTED_AGGREGATE_DIRECT_S1_CONSUMPTION = YES_AFTER_MINIMAL_ADAPTER
CURRENT_SUPPLEMENTAL_S1_READY = NO
EVENT_REJOIN_REQUIRED_FOR_CORRECTED_AGGREGATE = NO
EVENT_REJOIN_REQUIRED_FOR_INDEPENDENT_PROVENANCE_RECHECK = CONDITIONAL
MINIMUM_PATCH = READ_SCHEMA_PLUS_STAGING_FIELDS_PLUS_PRE_MEMBERSHIP_ADMISSION_FILTER
SCIENTIFIC_LOGIC_CHANGE = NO
P0_RUN_THIS_AUDIT = 0
S1_S7_RUN_THIS_AUDIT = 0
FIGURES_GENERATED_THIS_AUDIT = 0
MANUSCRIPT_MODIFIED_THIS_AUDIT = NO
HISTORICAL_OUTPUTS_MODIFIED_THIS_AUDIT = NO
COMMIT_OR_PUSH = NONE
```

## 11. 证据来源

- `script/build_dataset/repository_identity_provenance.py`
- `script/ch5_reference_quotient/pipeline.py`
- `script/ch5_reference_quotient/source_observation.py`
- `configs/ch5_reference_quotient_p0_v2.yaml`
- `outputs/reference_quotient_p0_corrected_v2/manifest.json`
- `outputs/reference_quotient_p0_corrected_v2/membership_audit.json`
- `outputs/reference_quotient_p0_corrected_v2/quotient_construction_audit.json`
- `outputs/reference_quotient_p0_corrected_v2/refq_provenance_sample.csv`
- `docs/freeze/ch5_refq_repository_identity_correction_c2_candidate_review_v1.md`
- `docs/freeze/ch5_refq_repository_identity_correction_c2_5_p0_integration_review_v1.md`
- `docs/freeze/ch5_refq_versioned_repository_identity_correction_protocol_v1.md`
- `supplemental/reference_quotient_v1/scripts/common.py`
- `supplemental/reference_quotient_v1/scripts/run_supplemental.py`
- `supplemental/reference_quotient_v1/v1_1_completion/run_completion.py`
