# Chapter 5 RefQ C3.7-E.2 Authority-Root / Stage-Root Binding Review

## 1. 审核结论

本审核针对 `C3.7-E.2` 的 provenance contract，不执行任何科学实验。

```text
repository = D:/github_repo/OSDB_RefQ
branch = ch5-refq-repository-identity-correction-v1
base_commit = 1f84a64795f6122beb7a90caba9d9fc8edd668b0
```

执行前基线测试为 `126 passed, 0 failed`。实现补丁后的完整测试为 `150 passed, 0 failed`，仅保留既存的 1 个 pandas 弃用警告。

最终决定：

```text
C3_7E2_AUTHORITY_BINDING_PASS_READY_FOR_C3_7F_REVIEW
```

## 2. E.1 缺口确认

在修改前使用系统临时目录进行了只读性质的 synthetic probe：

| 缺口 | 观察 | 分类 |
|---|---|---|
| authority class -> root | 任意临时文件可声明 `authority_class = CORRECTED_P0`，并以自己的临时目录作为 `root`，旧 validator 可以通过 | `AUTHORITY_CLASS_ROOT_BINDING_GAP = CONFIRMED` |
| stage/package output root | receipt 自声明临时 `output_root` 时，旧 package validator 可以使用该 root；`manifest.corrected_output_root` 与 receipt root 不一致未被强制拒绝 | `STAGE_OUTPUT_ROOT_BINDING_GAP = CONFIRMED` |

两个缺口都是 `PROVENANCE_CONTRACT_DEFECT`，不是 scientific logic change。

## 3. authority-root contract

实现位置：[`stage_io.py`](../../supplemental/reference_quotient_v2/scripts/stage_io.py)。

新增不可隐式切换的 `AuthorityRoots` context：

| authority class | production authority root | fixture authority root |
|---|---|---|
| `CORRECTED_AGGREGATE` | validated config 的 `corrected_aggregate_root` | 测试显式传入的 aggregate 临时 root |
| `CORRECTED_P0` | validated config 的 `corrected_p0_root` | 测试显式传入的 P0 临时 root |
| `CORRECTED_SUPPLEMENTAL_V2` | validated config 的 `corrected_output_root` | 测试显式传入的 supplemental 临时 root |

production context 由 `production_authority_roots(config)` 从 `validate_scaffold_config()` 的结果派生。`fixture_authority_roots(...)` 必须由调用方显式提供三个 root，并设置 `fixture=True`；不会根据 `tmp`、pytest 路径或环境变量推断 fixture 模式。

输入 artifact 的 `root` 现在只能作为声明证据，必须等于 authority class 所映射的 root。没有声明 `root` 的相对路径也按 class-implied root 解析。路径、canonical root、SHA 和历史路径禁用规则均继续 fail closed。

## 4. stage-specific authority matrix

| stage | 允许的 input authority class | 说明 |
|---|---|---|
| `S1_evidence_universe` | `CORRECTED_AGGREGATE`, `CORRECTED_P0` | aggregate 是 row-level authority；P0 可承载 metadata/seed authority |
| `S2_weight_sensitivity` | `CORRECTED_P0` | 不接受任意 supplemental-stage artifact |
| `S3_observation_sensitivity` | `CORRECTED_P0` | 不接受任意 supplemental-stage artifact |
| `S4_community_stability` | `CORRECTED_P0` | 不接受任意 supplemental-stage artifact |
| `S5_brokerage_stability` | `CORRECTED_P0` | 不接受任意 supplemental-stage artifact |
| `S6_figure_ready` | `CORRECTED_P0`, `CORRECTED_SUPPLEMENTAL_V2` | supplemental 输入受下一节的精确 source map 约束 |

这只是 provenance binding 收紧，不改变 `S1 -> S2 -> S3 -> S4/S5 -> S6` 的科学执行 DAG，也不制造 `S1 output -> S2 data` 等人工科学输入边。

## 5. S6 exact supplemental source map

共享 map 定义在 [`stage_io.py`](../../supplemental/reference_quotient_v2/scripts/stage_io.py)，由 [`s6_figure_ready.py`](../../supplemental/reference_quotient_v2/scripts/s6_figure_ready.py) 的 source resolver 和 manifest closure validator 复用：

| S6 logical key | 允许的相对路径 |
|---|---|
| `s4/louvain_stability_runs.csv` | `S4_community_stability/louvain_stability_runs.csv` |
| `s5/brokerage_stability_runs.csv` | `S5_brokerage_stability/brokerage_stability_runs.csv` |

因此以下来源被拒绝：

- `S1` 输出伪装为 `CORRECTED_SUPPLEMENTAL_V2`；
- S4/S5 目录中的任意未声明文件；
- historical v1 或 frozen P0 路径；
- authority class、declared root、manifest root 不一致的来源。

S6 manifest closure 继续验证 source SHA、output SHA、byte count、CSV row count 和 manifest schema，并额外验证其 authority roots 可与显式 production context 对齐。

## 6. output-root contract

实现位置：[`stage_io.py`](../../supplemental/reference_quotient_v2/scripts/stage_io.py) 和 [`manifest.py`](../../supplemental/reference_quotient_v2/scripts/manifest.py)。

production package 必须满足：

```text
canonical(manifest.corrected_output_root)
    == canonical(configured corrected_output_root)

canonical(receipt.output_root)
    == canonical(manifest.corrected_output_root)

receipt output artifacts
    ⊂ corrected_output_root/<canonical stage>/

durable marker
    == corrected_output_root/<canonical stage>/stage_receipt.json

S6 manifest
    == corrected_output_root/S6_figure_ready/figure_ready_manifest_v2.json
```

receipt 不能用自身声明的 root 覆盖 package root。production package 也不能由六个外部 fixture-root receipts 组成 `STAGE_PACKAGE_COMPLETE`。synthetic package 只有在调用方显式提供 fixture authority context 和 expected package root 时才可校验。

## 7. regression coverage

新增和迁移后的测试覆盖：

- arbitrary temporary P0/aggregate/supplemental roots 在 production context 被拒绝；
- 同一临时来源只有显式 fixture context 才能通过；
- record-declared root 不能覆盖 class-implied root；
- S2-S5 拒绝 supplemental authority；
- S6 接受 corrected P0、精确 S4、精确 S5 来源；
- S6 拒绝 arbitrary S4 文件和 S1-labeled supplemental 文件；
- receipt output root、package output root、S6 manifest path 和 durable marker path 的闭合；
- production build/validation 不能接受外部 fixture receipts 形成 complete package；
- explicit fixture package context 可验证 synthetic package；
- 历史 126 项 suite 保持通过。

测试结果：

```text
python -m pytest supplemental/reference_quotient_v2/tests -q
150 passed, 1 warning
```

## 8. scope and non-execution evidence

本次仅修改 `supplemental/reference_quotient_v2/` 下的实现与测试，以及本审核文档。未修改：

- `outputs/reference_quotient_p0_frozen/`；
- `outputs/reference_quotient_p0_corrected_v2/`；
- `supplemental/reference_quotient_v1/`；
- P0、GH-CoRE、event rejoin、source data；
- S1-S6 corrected-data execution；
- S7 overlap execution；
- figures 和 manuscript。

检查结果：

```text
real_v2_output_root_created = NO
corrected_data_S1_S6_run = NO
S7_overlap_run = NO
scientific_logic_change_count = 0
C3_7F_authorized = NO
```

G19/G20 的 authoritative runtime status 仍为：

```text
DESIGN_ONLY_NOT_EXECUTED
```

本补丁只建立了 root/path contract 和测试证据，不宣称已经执行真实历史 pre/post SHA inventory。

## 9. next boundary

建议下一阶段为 `C3.7-F`，单独审查 G18 stage-execution dependency closure，并设计真实 corrected-data regeneration 前的 G19 historical immutability snapshot。C3.7-E.2 本身不授权 C3.7-F 之外的科学执行。
