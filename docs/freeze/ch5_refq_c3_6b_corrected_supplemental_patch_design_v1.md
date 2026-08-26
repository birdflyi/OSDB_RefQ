# Chapter 5 RefQ C3.6-B.1
# Corrected Supplemental v2 Patch Design Errata and Finalization

## 0. 审计边界

这是 design-only、read-only 勘误与定稿，不是实现结果，也不是再生成授权。
本次没有运行 P0、S1-S7 或网络算法；没有生成 figures；没有修改代码、
配置、corrected P0、历史 P0、历史 supplemental 或 manuscript；没有 commit/push。

repository = D:/github_repo/OSDB_RefQ
branch = ch5-refq-repository-identity-correction-v1
baseline_commit = 68054dceaebc14ecdf29ac9d0b209f28301fd7a4
corrected_p0_root = outputs/reference_quotient_p0_corrected_v2/
historical_p0_root = outputs/reference_quotient_p0_frozen/
historical_supplemental_root = supplemental/reference_quotient_v1/
proposed_v2_root = supplemental/reference_quotient_v2/

### 0.1 文档版本策略

三份 C3.6-B 设计文件在本次开始时均为 untracked draft，Git 历史中没有提交
记录。因此采用“未提交草稿原地勘误”策略，不新建 superseding v1 文件。
本次原地修订会在 Git 首次提交时形成单一、无歧义的 C3.6-B 最终设计版本。

## 1. 最终设计结论

C3_6B_CORRECTED_SUPPLEMENTAL_PATCH_DESIGN = PASS_READY_FOR_HUMAN_REVIEW
corrected_aggregate_is_S1_authority = YES
event_rejoin_required = NO
historical_v1_executable_authority = NO
historical_v1_write_target = NO
proposed_v2_root = supplemental/reference_quotient_v2/
S1_S7_side_effect_removed_by_design = YES
S3_shared_canonical_network_authority = YES
S5_inclusion_frequency_authority = brokerage_topk_inclusion_frequency.csv
S6_structural_summary_authority = structural_summary.csv
deprecated_S5_frequency_excluded = YES
deprecated_S6_JSON_excluded = YES
scientific_logic_change_count = 0
implementation_phases_defined = YES
acceptance_gates_defined = YES
prior_design_state = C3_6B_PATCH_DESIGN_READY_FOR_IMPLEMENTATION_REVIEW

C3_6B_1_STATUS = PASS_READY_FOR_HUMAN_REVIEW
S7_KEEP_OPERATOR = SET_INTERSECTION_EMPTY
audit_staging_contains_rejected_rows = YES
analytical_membership_can_receive_rejected_rows = NO
C3_6B_1_decision = C3_6B_DESIGN_FINALIZED_READY_FOR_C3_7A

这表示设计可以交给人工评审，不能据此直接执行 C3.7 或 C4-S1...C4-S6。

## 2. corrected P0 输入核对

当前 outputs/reference_quotient_p0_corrected_v2/manifest.json 记录：

| 项目 | 值 |
|---|---|
| status | PASS |
| data_version | refq_p0_2023_seed_observation_v2_strict_identity |
| output root | outputs/reference_quotient_p0_corrected_v2 |
| config SHA-256 | e19c0937e0d6f72fa84ad135b55a4056357d132d3a3df4ae5455bda7bc3de658 |
| implementation commit | 68054dceaebc14ecdf29ac9d0b209f28301fd7a4 |
| analysis seeds | 294 |
| input boundary fixture | 3,748,078 Reference rows |
| admitted fixture | 3,747,958 Reference rows |
| out-of-seed fixture | 120 rows |
| missing/invalid event repo ID fixture | 0 / 0 |

corrected aggregate 已含 event_id、event_repo_id、event_repo_name、
event_repo_provenance_status、expected_source_context_repo_id、
source_admission_status、source_provenance_mismatch、aggregate_schema_version。

C3.6-A 结论继续成立：corrected aggregate 是 S1 首选行级 authority，标准路径
不需要再次 event rejoin，也不需要新的 owner/repo name 到 repo_id 恢复机制。

兼容性限制：当前 corrected P0 manifest 的 schema 仍写为
reference_quotient_p0_frozen_manifest_v1，entry_point 仍显示旧的
configs/ch5_reference_quotient_p0.yaml --execute。因此 v2 必须显式校验
corrected config、config SHA、corrected root、manifest SHA 和 aggregate root，
不能把 stale entry_point 当作 executable authority。

## 3. 当前实现阻断点

| 位置 | 当前事实 | v2 要求 |
|---|---|---|
| supplemental/reference_quotient_v1/scripts/run_supplemental.py:34-39 | roots、旧 P0 config/manifest 硬编码 | 显式 corrected roots 和 hashes |
| run_supplemental.py:53-81 | evidence root 固定为旧 aggregate root | 只读取 corrected aggregate root |
| run_supplemental.py:178-300 | 旧 RAW_USECOLS，且 S1 内写 S7 | provenance adapter，移除 S7 side effect |
| run_supplemental.py:284-289 | S1 使用历史数值常量 | 数值来自 corrected fixture/manifest |
| run_supplemental.py:306-403 | S2/S4 读取历史 P0，写死 34 和历史 modularity | corrected P0 和 corrected summary |
| run_supplemental.py:451-499 | S6 历史读取/fallback，输出 structural_summary.json | corrected-source-only，CSV authority |
| v1_1_completion/run_completion.py:15-31 | 历史 root 和旧 RAW_USECOLS 硬编码 | 仅作为历史证据 |
| v1_1_completion/run_completion.py:240-320 | 从历史 S5/S6 文件派生补充 authority | v2 从 corrected S5 派生 |
| v1_2_s3_reproducibility_patch/patch_s3.py:12-20 | 共享 network views 但输入历史 P0 | 仅 comparison evidence |
| tests/test_supplemental.py:7-62 | 历史数值被当作 validity | 拆成语义、corrected fixture、历史 comparison |

## 4. 架构和执行边界

采用新 v2 package 加共享 canonical helper，不原地参数化 v1。

建议结构：

supplemental/reference_quotient_v2/
  configs/supplemental_v2_corrected.yaml
  scripts/paths.py, schema.py, s1_adapter.py
  scripts/s1_evidence_universe.py
  scripts/s2_weight_sensitivity.py
  scripts/s3_observation_sensitivity.py
  scripts/s4_community_stability.py
  scripts/s5_brokerage_stability.py
  scripts/s6_figure_ready.py
  scripts/manifest.py, run_supplemental_v2.py
  tests/test_supplemental_v2.py
  outputs/                         后续获授权执行时才创建

可复用 active authority：

- script/ch5_reference_quotient/network_views.py 的 directed_to_undirected_edges
  和 analyze_undirected_view；
- script/build_dataset/repository_identity_provenance.py 的 ID normalization
  和 admission contract；
- script/ch5_reference_quotient 的 membership、edge、统计语义；
- corrected P0 已 materialize 的 aggregate、edge、role、graph 和 manifest。

v2 不应 import 或调用 v1 executable orchestrator。v1 common.py 如需复用，
应抽取为无历史路径、无历史 numeric constants、无输出副作用的 shared helper。

配置必须显式表达 corrected_p0_root、corrected_p0_manifest、corrected_p0_config、
corrected_aggregate_root、corrected_output_root；corrected_relation_root 仅作为
可选 comparison input，标准 S1 路径不需要 event rejoin。历史 P0/supplemental
root 只能标记 comparison-only。

fail-closed 条件：

1. v2 output root 等于历史 v1 output root；
2. corrected P0 root/manifest 缺失或 manifest status 非 PASS；
3. aggregate root 等于历史 v1 aggregate root；
4. config SHA、manifest SHA、output root 或 aggregate root 不闭合；
5. corrected schema/version 缺少 provenance/admission contract；
6. v2 root 已有内容且实现会覆盖、清理或自动 retry；
7. source authority 解析到 supplemental/reference_quotient_v1/；
8. stale P0 entry_point 被当作 executable command。

## 5. corrected S1 数据流和 staging

corrected P0 PASS manifest
  -> corrected config/root/hash guards
  -> corrected aggregate schema/version and 294 partition checks
  -> Reference filter
  -> reference_provenance_staging (all Reference rows)
  -> status-aware context/admission consistency validation
  -> admission/rejection counters by status
  -> admitted_reference_records SQL VIEW
  -> membership, analytical cross-tabs, eligibility, edge classes
  -> S2 -> S3 -> S4 -> S5 -> S6
  -> v2 manifest and SHA closure

S1 必须读取并保留：

event_id
event_repo_id
expected_source_context_repo_id
source_admission_status
source_provenance_mismatch

建议保留 event_repo_name、event_repo_provenance_status、aggregate_schema_version，
但 repo_name 不是 identity authority。

### 5.1 status vocabulary 与一致性条件

允许的 source_admission_status 词汇严格来自
script/build_dataset/repository_identity_provenance.py:26-29：

1. ADMITTED_SOURCE_OBSERVATION
2. OUT_OF_SEED_SOURCE_OBSERVATION
3. MISSING_EVENT_REPOSITORY_ID
4. INVALID_EVENT_REPOSITORY_ID

所有状态都要求 expected_source_context_repo_id 是有效 numeric repository ID，
且等于当前 seed repo ID。逐状态条件如下：

| status | event_repo_id | 与 expected context 关系 | source_provenance_mismatch |
|---|---|---|---|
| ADMITTED_SOURCE_OBSERVATION | 有效 numeric ID | 相等 | False |
| OUT_OF_SEED_SOURCE_OBSERVATION | 有效 numeric ID | 不相等 | True |
| MISSING_EVENT_REPOSITORY_ID | null/missing | 不作数值比较 | True |
| INVALID_EVENT_REPOSITORY_ID | materialized normalized value 为 null；状态保留原始值非法的分类 | 不作数值比较 | True |

INVALID 与 MISSING 在 materialized event_repo_id 上都可能是 null；二者的区别由
已物化的 source_admission_status 保留。v2 adapter 不重新推断原始非法 lexeme，
也不做 event rejoin。未知状态、空状态、无效 expected context，或任一
status/identity/mismatch 矛盾都必须 FAIL CLOSED。

当前 corrected aggregate 的实际状态证据为：294/294 分区包含 admitted；
1/294 分区包含 out-of-seed；missing/invalid 分区均为 0。Fireproof corrected
aggregate 中 120 行是
OUT_OF_SEED_SOURCE_OBSERVATION, event_repo_id=600271677,
expected_source_context_repo_id=679889516, mismatch=True；58 行是 admitted、
IDs 相等、mismatch=False。被拒绝的 120 行是有效审计行，不是 schema failure。

### 5.2 audit staging 与 analytical universe

SQLite 使用一个物理审计表和一个只读过滤 view，不要求物理复制：

reference_provenance_staging：

- 包含所有 relation_type == Reference 的行，包括 admitted 和全部 rejected statuses；
- 保留 event/source/target/provenance/admission fields；
- status-aware consistency validation 在该层执行；
- admission/rejection counters 从该层按 status 生成。

admitted_reference_records VIEW：

SELECT * FROM reference_provenance_staging
WHERE source_admission_status = 'ADMITTED_SOURCE_OBSERVATION'
  AND source_provenance_mismatch = 0
  AND event_repo_id = expected_source_context_repo_id
  AND expected_source_context_repo_id = seed_project

membership、source profile、event/entity analytical cross-tabs、quotient
eligibility、edge classes 和所有 S2-S6 analytical dependencies 只能读取
admitted_reference_records。任何 rejected row 到达这些消费者都属于 fail-closed
gate failure。rejected rows 始终保留在审计表中，可计数、可追踪。

reference_provenance_staging 至少包含：

seed_project TEXT NOT NULL
event_id TEXT NOT NULL
event_repo_id TEXT NULL
expected_source_context_repo_id TEXT NOT NULL
source_admission_status TEXT NOT NULL
source_provenance_mismatch INTEGER NOT NULL CHECK (source_provenance_mismatch IN (0,1))
src_entity_id/src_entity_type/tar_entity_id/tar_entity_type TEXT NULL
src_entity_id_agg/src_entity_type_agg TEXT NULL
tar_entity_id_agg/tar_entity_type_agg/tar_entity_type_fine_grained TEXT NULL
relation_type TEXT NOT NULL
event_type TEXT NULL

repo ID normalize 为无小数点的十进制字符串；非整数、负值和非法值不得静默
转换。admitted row 的 event_repo_id 不得为空，mismatch 必须为 false。
建议索引 seed_project,event_id、source_admission_status、event_repo_id、
seed_project,relation_type。独立记录 REFERENCE_RECORD、AGGREGATED_EDGE_WEIGHT、
EDGE_COUNT；directed_edge_count 不得解释为 Reference-record multiplicity。

固定顺序：

read corrected aggregate
  -> validate schema/version
  -> relation_type == Reference
  -> insert all Reference rows into reference_provenance_staging
  -> validate expected context and allowed status vocabulary
  -> validate each row against its status-specific consistency conditions
  -> record admitted/rejected counters by status
  -> expose admitted_reference_records VIEW
  -> membership
  -> cross-tabs/event distributions
  -> eligibility/edge classes
  -> S1 outputs

禁止 membership -> admission later，也禁止对全部 Reference rows无差别应用
event_repo_id == expected context。这个相等条件只属于 admitted status；
out-of-seed 的合法审计条件恰好是不相等。

S1 fixture：before admission 3,748,078；admitted 3,747,958；out-of-seed 120；
missing 0；invalid 0；source mismatch after admission 0。以上是未来
comparison gate 的候选 fixture，不是本次实际 PASS。

## 6. S2-S7 设计

S2：读取 corrected directed RefQ edge table；保持每条保留 Reference record
对 ordered source/target membership pair 贡献一单位 weight 的 P0-specific
contract；threshold 先作用于 directed weight，再做 undirected collapse；
不得写死历史 9557、6376 或历史 modularity。

S3：使用 shared script/ch5_reference_quotient/network_views.py；保留 node
registry、seed node presence、deterministic order、random_seed 20260731 和
first-order semantics。v1.2 patch 仅作 comparison evidence。

S4：读取 corrected canonical graph；配置 Louvain seeds/runs 和 partition
closure；不得硬编码 historical community count 34 或 modularity
0.7973095950243088。

S5：保持 unweighted approximate betweenness、weight=None、sample/k、seed 和
tie-break。v2 human-use authority 必须是
supplemental/reference_quotient_v2/outputs/S5_brokerage_stability/
brokerage_topk_inclusion_frequency.csv，由 corrected brokerage_rank_stability.csv
派生，并闭合 sum(inclusion_count) = run_count * top_k。历史
brokerage_topk_frequency.csv 标记 DEPRECATED_SEMANTICS，不得消费或发出。

S6：只在 S1-S5 gates 通过后执行。P0-derived source 只能来自 corrected P0；
S4/S5 source 只能来自 v2 outputs。每项记录 source path、source SHA、root/version、
transformation、row count、output SHA。authority 为 structural_summary.csv，
manifest 为 figure_ready_manifest_v2.json。旧 JSON 和历史 manifests 仅作 archive。

S7：不在 S1-S6 DAG 中运行。只做 read-only zero-overlap KEEP gate：

fixed_source_set ∩ affected_source_set = ∅
fixed_target_set ∩ affected_target_set = ∅
fixed_edge_set ∩ affected_edge_set = ∅

可执行等价条件：

len(fixed_source_set & affected_source_set) == 0
len(fixed_target_set & affected_target_set) == 0
len(fixed_edge_set & affected_edge_set) == 0

三个交集都为空时 S7_STATUS = KEPT_FIXED_OBJECT；任一交集非空时
S7_STATUS = REGENERATE_REQUIRED。本任务不执行该 gate。

## 7. 文件级决策

完整 machine-readable matrix 见 ch5_refq_c3_6b_corrected_supplemental_patch_matrix_v1.csv。

CREATE：

- supplemental/reference_quotient_v2/configs/supplemental_v2_corrected.yaml
- supplemental/reference_quotient_v2/scripts/paths.py
- supplemental/reference_quotient_v2/scripts/schema.py
- supplemental/reference_quotient_v2/scripts/s1_adapter.py
- supplemental/reference_quotient_v2/scripts/s1_evidence_universe.py
- supplemental/reference_quotient_v2/scripts/s2_*.py 到 s6_*.py
- supplemental/reference_quotient_v2/scripts/run_supplemental_v2.py
- supplemental/reference_quotient_v2/scripts/manifest.py
- supplemental/reference_quotient_v2/tests/test_supplemental_v2.py

KEEP：

- script/ch5_reference_quotient/network_views.py
- script/build_dataset/repository_identity_provenance.py
- script/ch5_reference_quotient/pipeline.py 和 config.py
- configs/ch5_reference_quotient_p0_v2.yaml
- outputs/reference_quotient_p0_corrected_v2/
- outputs/reference_quotient_p0_frozen/
- supplemental/reference_quotient_v1/ 全部历史文件

DEPRECATE_AS_ACTIVE_AUTHORITY：

- supplemental/reference_quotient_v1/outputs/S5_brokerage_stability/brokerage_topk_frequency.csv
- supplemental/reference_quotient_v1/outputs/S6_figure_ready/structural_summary.json
- supplemental/reference_quotient_v1/outputs/S6_figure_ready/figure_ready_manifest.json
- supplemental/reference_quotient_v1/v1_1_completion/outputs/S6_figure_ready/figure_ready_manifest_v1_1.json

以上历史文件不得删除、覆盖或修改。

## 8. 测试、验收和阶段

测试分为 semantic invariants、corrected-baseline fixtures、historical comparison。
最低覆盖 schema required fields、历史 aggregate reject、status-aware validation、
审计 staging 保留 rejected、analytical view 排除 rejected、out-of-seed audit row
合法、admitted mismatch reject、unknown status fail-closed、historical write
block、S1 cannot write/reselect S7、S7 intersection KEEP gate、
S2 weight/multiplicity、S3 shared authority、S4 no hard-code、S5 frequency authority、
S6 no cross-root mixing、deprecated S6 JSON exclusion、manifest SHA closure 和
v1 byte immutability。

20 个 machine-readable gates 见 acceptance_gates_v1.csv；本审计不把任何 gate
标为 runtime PASS，当前状态统一为 DESIGN_ONLY_NOT_EXECUTED。上游 gate 失败必须
阻止下游，不自动 cleanup/retry。

| 阶段 | 范围 | 下一阶段条件 |
|---|---|---|
| C3.7-A | v2 scaffold/config/orchestration/path guards；无科学运行 | 人工审查隔离结构 |
| C3.7-B | S1 adapter/schema/tests/read-only preflight | G01-G09 implementation tests |
| C3.7-C | S2/S3 adaptation/tests | G10-G11 review |
| C3.7-D | S4/S5 adaptation/tests | G12-G14 review |
| C3.7-E | S6/manifest adaptation/tests | G15-G17 review |
| C3.7-F | full implementation/cross-root review；仍不运行 S1-S6 | G18-G20 review |
| C4-S1...C4-S6 | 单独授权后的 corrected regeneration | 每阶段独立 gate |

阶段应支持单独调用；失败 stage 必须阻止下游，不自动 cleanup/retry。

## 9. 科学逻辑分类、限制与 Final Status

全部拟议变化属于 IMPLEMENTATION_ONLY、PROVENANCE_BOUNDARY_ENFORCEMENT、
AUTHORITY_CLEANUP、VERSIONING_ONLY 或 TEST_ONLY。不会改变 Q = M^T R_P M、
numeric repository identity、membership、target policy、self-loop、weight
contract 或 S2-S6 scientific semantics。

SCIENTIFIC_LOGIC_CHANGE_COUNT = 0

若 coding phase 必须改变上述科学规则，应停止并返回 C3_6B_REQUIRES_SCIENTIFIC_REVIEW。

本审计没有执行 adapter、tests、preflight 或 regeneration；没有重新计算
corrected S1-S6 数字；S7 set-intersection 需要未来 read-only preflight 实测。

C3_6B_CORRECTED_SUPPLEMENTAL_PATCH_DESIGN = PASS_READY_FOR_HUMAN_REVIEW
corrected_aggregate_is_S1_authority = YES
event_rejoin_required = NO
S1_adapter_scope = corrected aggregate schema + all-Reference audit staging + status-aware validation + admitted-only analytical view + counters
historical_v1_executable_authority = NO
historical_v1_write_target = NO
proposed_v2_root = supplemental/reference_quotient_v2/
S1_S7_side_effect_removed_by_design = YES
S3_shared_canonical_network_authority = YES
S5_inclusion_frequency_authority = supplemental/reference_quotient_v2/outputs/S5_brokerage_stability/brokerage_topk_inclusion_frequency.csv
S6_structural_summary_authority = supplemental/reference_quotient_v2/outputs/S6_figure_ready/structural_summary.csv
deprecated_S5_frequency_excluded = YES
deprecated_S6_JSON_excluded = YES
scientific_logic_change_count = 0
implementation_phases_defined = YES
acceptance_gates_defined = YES
prior_design_state = C3_6B_PATCH_DESIGN_READY_FOR_IMPLEMENTATION_REVIEW
P0_RUN = 0
S1_S7_RUN = 0
NETWORK_ALGORITHMS_RUN = 0
FIGURES_GENERATED = 0
MANUSCRIPT_MODIFIED = NO
HISTORICAL_OUTPUTS_MODIFIED = NO
CODE_MODIFIED = NO

C3_6B_1_STATUS = PASS_READY_FOR_HUMAN_REVIEW
S7_KEEP_OPERATOR = SET_INTERSECTION_EMPTY
S7_fixed_source_overlap_gate = len(fixed_source_set & affected_source_set) == 0
S7_fixed_target_overlap_gate = len(fixed_target_set & affected_target_set) == 0
S7_fixed_edge_overlap_gate = len(fixed_edge_set & affected_edge_set) == 0
source_admission_status_vocabulary = ADMITTED_SOURCE_OBSERVATION | OUT_OF_SEED_SOURCE_OBSERVATION | MISSING_EVENT_REPOSITORY_ID | INVALID_EVENT_REPOSITORY_ID
admitted_contract = valid event_repo_id; valid expected context/current seed; IDs equal; mismatch False
out_of_seed_contract = valid event_repo_id; valid expected context/current seed; IDs unequal; mismatch True
unknown_status_policy = FAIL_CLOSED
audit_staging_contains_rejected_rows = YES
analytical_membership_can_receive_rejected_rows = NO
runtime_gates_executed = 0
decision = C3_6B_DESIGN_FINALIZED_READY_FOR_C3_7A
