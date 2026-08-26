# Chapter 5 RefQ C3.7-B
# Corrected Supplemental V2 S1 Source-Observation Boundary Adapter Review v1

审查日期：2026-08-26

Repository：`D:\github_repo\OSDB_RefQ`

Branch：`ch5-refq-repository-identity-correction-v1`

## 1. 授权范围和基线

本记录仅覆盖 C3.7-B 已授权的 corrected aggregate S1 source-observation
boundary adapter、状态/模式验证、瞬态审计 staging/view、全量只读预检、测试及
文档。它不授权完整 S1 科学再生，也不授权 P0、GH-CoRE、event-to-raw rejoin、
S2-S7、network algorithms、图表、manuscript 或历史产物操作。

```text
base_commit = 65daeb92d4e75a80ab47b7d5a1e9c23cffc4a991
HEAD_before = 65daeb92d4e75a80ab47b7d5a1e9c23cffc4a991
implementation_commit = PENDING_SINGLE_C3_7B_COMMIT
```

本审查中的 `implementation_commit` 是待创建的单一 C3.7-B 提交；其最终 SHA
将在提交与 push 后的最终状态中记录。预检 JSON 中的 commit candidate 是预检
发生时的 `HEAD_before`，不应被误读为实现提交。

## 2. 实现范围

| path | classification | C3.7-B purpose |
|---|---|---|
| `supplemental/reference_quotient_v2/scripts/schema.py` | modified | 定义 S1 source-boundary 必需字段并 fail-closed 验证 header |
| `supplemental/reference_quotient_v2/scripts/s1_adapter.py` | created | 校正 aggregate 适配、状态契约验证、瞬态 SQLite staging 及 admitted-only view、只读预检 |
| `supplemental/reference_quotient_v2/tests/test_s1_adapter.py` | created | C3.7-B contract/isolation/staging tests |
| `docs/freeze/ch5_refq_c3_7b_s1_boundary_preflight_v1.json` | created | 只读预检元数据，不是科学 supplemental output |
| this review | created | C3.7-B implementation and boundary review |

适配器从 corrected P0 `analysis_seed_manifest_294.csv` 读取唯一的
`partition -> repo_id` 权威映射。partition 文件名只可作为映射 lookup key；它不能
独立授权 source identity。每个 Reference row 均验证：

```text
expected_source_context_repo_id == authoritative current seed repository ID
```

并复用 `script/build_dataset/repository_identity_provenance.py` 的
`normalize_repository_id()`。没有 raw-event 读取、join 或 owner/repo-to-ID recovery。

四个状态严格为：

```text
ADMITTED_SOURCE_OBSERVATION
OUT_OF_SEED_SOURCE_OBSERVATION
MISSING_EVENT_REPOSITORY_ID
INVALID_EVENT_REPOSITORY_ID
```

适配器保留全部 Reference rows 作为 audit rows。只有 status 为 admitted、mismatch
为 false、event/context ID 相等且 context/seed ID 相等的 rows 才进入
`admitted_reference_records`。`OUT_OF_SEED`、`MISSING` 和 `INVALID` 均保留在
审计表中但无法从 admitted view 读取。

`INVALID_EVENT_REPOSITORY_ID` 的校正物化契约是：无效 raw lexical value 已在 P0
校正链中规范化为 null，分类由 status 保留；适配器拒绝重新接受或恢复非法 lexical
value。这与 frozen corrected aggregate contract 一致。

## 3. 测试

执行命令：

```text
venv\Scripts\python.exe -m pytest supplemental\reference_quotient_v2\tests -q
```

```text
tests_collected = 33
tests_passed = 33
tests_failed = 0
C3_7A_regression_tests = PASS (20 passed)
```

新增测试覆盖 required fields、未知 status fail-closed、四种状态的 materialized
contract、admitted/out-of-seed/missing/invalid 隔离、authoritative seed context、
repo name 与 filename 不能作为 identity authority、historical schema reject、
corrected schema accept、Reference-only boundary、SQLite staging/view separation、
Fireproof-like rejected audit row 和不创建 v2 output root。

## 4. 全量只读预检

执行命令：

```text
venv\Scripts\python.exe -m supplemental.reference_quotient_v2.scripts.s1_adapter \
  --preflight \
  --report docs/freeze/ch5_refq_c3_7b_s1_boundary_preflight_v1.json
```

预检逐块读取 294 个 corrected aggregate partitions 的必要列，只验证 header、
partition/seed context、Reference status 和 admission consistency。它没有创建
membership、quotient、edge、publication table 或任何 supplemental output。

| check | observed | fixture | result |
|---|---:|---:|---|
| corrected aggregate partitions | 294 | 294 | PASS |
| Reference rows before admission | 3,748,078 | 3,748,078 | PASS |
| `ADMITTED_SOURCE_OBSERVATION` | 3,747,958 | 3,747,958 | PASS |
| `OUT_OF_SEED_SOURCE_OBSERVATION` | 120 | 120 | PASS |
| `MISSING_EVENT_REPOSITORY_ID` | 0 | 0 | PASS |
| `INVALID_EVENT_REPOSITORY_ID` | 0 | 0 | PASS |
| affected source seeds | 1 | 1 | PASS |
| unknown statuses | 0 | 0 | PASS |
| status/identity contradictions | 0 | 0 | PASS |
| admitted identity contradictions | 0 | 0 | PASS |
| Fireproof context `679889516` rejected rows | 120 | 120 | PASS |
| Fireproof event repo `600271677` rejected rows | 120 | 120 | PASS |

观察到的 aggregate schema version 是：

```text
reference_aggregate_schema_v2_event_repository_provenance
```

观察到的非零 status 是 admitted 和 out-of-seed；四状态 vocabulary 仍由 schema
contract 定义并在 tests 中验证。预检 JSON SHA-256：

```text
cd08d9b39bb1ced29707454558a59a1492e3c5a2d302011e6dde08d728668929
```

输入 provenance closure：

```text
corrected P0 manifest SHA-256 = 21699353d5dc9476547ee7f56881ba0a1ccc842a6d3c95adad9a28dedfd656d7
corrected P0 config SHA-256   = e19c0937e0d6f72fa84ad135b55a4056357d132d3a3df4ae5455bda7bc3de658
```

## 5. 隔离、不可变性和污染检查

```text
supplemental/reference_quotient_v2/outputs/ exists = NO
s1_evidence_universe.py exists = NO
s2_to_s6_modules_created = 0
event_rejoin_performed = NO
membership_build_run = 0
quotient_build_run = 0
network_algorithms_run = 0
```

工作树差异只包含本 C3.7-B 允许的 v2 实现、测试和 `docs/freeze/ch5_refq_c3_7b_*`
文档。下列受保护路径在当前 diff 中均为零修改：

```text
outputs/reference_quotient_p0_frozen/
outputs/reference_quotient_p0_corrected_v2/
supplemental/reference_quotient_v1/
script/ch5_reference_quotient/
script/build_dataset/repository_identity_provenance.py
manuscript/ paper/ thesis/ (when present)
```

只读复核值：

| protected reference | observed value |
|---|---|
| `main` | `dc88221ae6e0bb72f2c142b2811a4552c5ec2388` |
| `chapter5-refq-freeze-v1.0` peeled commit | `68d001551359d120bf2a06cc5e571742df7e7822` |
| historical P0 manifest SHA-256 | `a3089fd8a6a58c0a15d2192a7b5f3388868ef0f1358c803be3aa4f27314c59f6` |
| corrected P0 manifest SHA-256 | `21699353d5dc9476547ee7f56881ba0a1ccc842a6d3c95adad9a28dedfd656d7` |
| corrected P0 config SHA-256 | `e19c0937e0d6f72fa84ad135b55a4056357d132d3a3df4ae5455bda7bc3de658` |

source-data repository 有既存的未跟踪数据与日志路径；C3.7-B 对其只做 aggregate
读取，未向该 repository 写入任何文件。本次预检也未写入 source-data root。

## 6. 门、计数和下一授权边界

```text
G01_G20_authoritative_runtime_status = DESIGN_ONLY_NOT_EXECUTED
P0_RUN = 0
S1_BOUNDARY_PREFLIGHT = 1
S1_SCIENTIFIC_RUN = 0
S2_S7_RUN = 0
NETWORK_ALGORITHMS_RUN = 0
FIGURES_GENERATED = 0
MANUSCRIPT_MODIFIED = NO
HISTORICAL_OUTPUTS_MODIFIED = NO
CORRECTED_P0_MODIFIED = NO
SHARED_P0_CODE_MODIFIED = NO
scientific_logic_change_count = 0
```

本次 PASS 仅说明 corrected S1 source-observation boundary 的实现与全量只读预检
通过。它不证明 S1 membership/edge/tables，也不构成 S2-S7、C3.7-C 或 C4 的执行
授权。

```text
C3_7C_authorized = NO
C4_authorized = NO
next_authorization_boundary = human review followed by separately authorized C3.7-C
```

## 7. Decision

```text
C3_7B_S1_BOUNDARY_PASS_READY_FOR_HUMAN_REVIEW
```
