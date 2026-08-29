# Chapter 5 RefQ Final Conservative Manuscript Reconciliation Review v1

Repository: `D:/github_repo/OSDB_RefQ`  
Branch: `ch5-refq-repository-identity-correction-v1`  
Repository HEAD before final audit: `2b1a43af8d1125b079adc311f6732e4a9a459a16`  
Forensics-v2 serialization repair commit: `2b1a43af8d1125b079adc311f6732e4a9a459a16`

## Scope and immutability

This is the final conservative reconciliation of one new external manuscript sibling. The OLD manuscript, migrated-v1 manuscript, QA manuscript, P0-v3 outputs, supplemental package, manifests, receipts, scientific code, and figures were read-only. No P0/S1-S7/GH-CoRE/event-rejoin run, statistic recomputation, or figure rendering was performed.

The final sibling was already an exact byte-copy of OLD before editing. Its initial SHA-256 was `4BA2DB1B45C97D0823C4909C705FC307AA3A992E4B2C2E59096FC630A871FD88`. Only the sibling was patched.

## Manuscript identities

| artifact | path | SHA-256 | bytes |
|---|---|---|---:|
| OLD | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean.md` | `4BA2DB1B45C97D0823C4909C705FC307AA3A992E4B2C2E59096FC630A871FD88` | 119739 |
| MIGRATED_V1 | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_migrated.md` | `4BA0322DD577090FF7E063A7641AFBDED44150B42825EFB343BE265F141FA56C` | 112360 |
| QA | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_migrated_qa.md` | `D353BB462BC3D4D0C07FA572AAF5B4DF64805B7E032C0A1587F641D0F3214831` | 112891 |
| FINAL_RECONCILED | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled.md` | `2CFA7B6E72669352EEE24B9D7A79B49063A50A967CFF1C828CE910B12F9025C1` | 120648 |

## Frozen scientific authority

Current WiredTiger authority is P0-v3 row `project_id=2944302`, `wiredtiger/wiredtiger`: 15,332 total records, 12,891 self-reference records, 19 external-project records, 1,096 non-project records, 1,326 unresolved-target records, ratio `0.8407905035220454` displayed as `84.08%`. The OLD pair `100,190 / 84,239` is absent from FINAL and is not restored.

The frozen L8 wording is retained exactly in the final sibling:

> 经 source-admission 后保留 3,747,958 条 Reference records，其中 1,586,047 条具有可唯一映射到项目的 target endpoint，因而满足 quotient eligibility 并进入 Project-level RefQ aggregation。

The flow closes as `3,748,078 - 120 = 3,747,958`, `1,586,047 + 1,686,729 + 475,182 = 3,747,958`, and `1,447,073 + 138,974 = 1,586,047`.

## Human presentation decisions

- Table 4.1 restores the OLD compact schema with current admitted-record values and `Other=260,866`, `Total=3,747,958`.
- Table 4.2 restores the OLD compact schema with current admitted-record values and `Other=434,337`, `Total=3,747,958`.
- Table 4.6c is a compact merged quantile-plus-relation-partition table. OLD mean fields were not restored and no new means were computed.
- Table 4.6d restores the OLD compact target-role schema with current counts and `2.47% / 16.00% / 48.99%` concentration shares.
- Table 4.6e retains the compact structural schema, canonical 35-community modularity, and places S4 sensitivity in surrounding prose as `ACCEPT_WITH_LIMITATION`.
- Table 4.6f restores the OLD brokerage schema with current top-five values and an explicit algorithmic community label.
- Table 4.7 uses all 10 current `include_mixed` category rows, including Object Oriented and RDF.
- Table 4.8 restores the compact inferential schema with current FDR p and epsilon-squared values rounded to four decimals.

## Result-keypoint disposition

All five OLD result-keypoint findings are retained semantically exactly once. RK001 and RK002 are merged with the adjacent Table 4.1/4.2 interpretation; RK003 is retained with the corrected WiredTiger row; RK004 and RK005 remain explicit result-keypoint bullets. The disposition ledger records `5/5 = RETAINED_SEMANTICALLY`.

## Structural and terminology closure

The final manuscript consistently uses RQ1, RQ2a, RQ2b, RQ2c and RQ3. It retains Reference Quotient (RefQ), Reference Quotient Network (RefQN), Project-level Reference Quotient Network, membership-induced graph coarsening and weighted directed quotient network. `协作规模` and `协作互动强度` replace the stale community-scale labels.

Louvain results are described as an algorithmic modular neighborhood view. The canonical 35-community partition is one deterministic reference realization; S4 reports community count 32--37, 42/50 ARI-to-canonical values below 0.9, minimum ARI `0.6823671359861659`, and minimum pairwise ARI `0.6092441840471735`. S5 reports minimum Spearman `0.9998339514284217`, minimum top-50 overlap `0.82`, and `robustness_alert=FALSE`. S7 remains `KEPT_FIXED_OBJECT (G09 = PASS)`. Expanded targets remain not source-complete, and no second-order projection is claimed.

No final result sentence uses record count as entity count, aggregated edge weight as edge count, or category metadata as Louvain community identity. No causal brokerage, knowledge-flow, stable-community, or true-community conclusion was added.

## Audit closure

- Markdown tables detected: 16 physical tables; 13 scientific table decisions audited in `ch5_refq_p0v3_final_reconciled_table_audit_v1.csv`.
- Table audit: 13/13 PASS.
- Final numeric-authority audit: 28 mapped rows; 22 scientific-result rows, 2 method-configuration rows, 3 provenance-identity rows, and 1 closure row; unmapped scientific numeric claims: `0`; verification failures: `0`.
- Composite closure: WiredTiger PASS; L8 flow PASS; Table 4.1 Other PASS; Table 4.2 Other PASS; top concentration support PASS; LCC PASS; record/entity/edge semantics PASS.
- Stale-value sweep: known old values (`100190`, `84239`, `1,586,117`, `139,044`, `9,605`, `9,557`, `9,472`, `6,515`, `6,376`, `6,221`, `6,332`, `15.99`, `48.97`, `0.797309595`, and related unformatted forms) have zero unexplained occurrences in FINAL.
- Forensics-v2 CSV remains 26 columns, 78 logical rows, every data row 26 fields, `csv.DictReader=PASS`, `pandas.read_csv=PASS`, no unnamed columns, no shifted fields, and no semantic drift.

## Execution zeros and source checks

`P0_RUN=0`, `S1_RUN=0`, `S2_RUN=0`, `S3_RUN=0`, `S4_RUN=0`, `S5_RUN=0`, `S6_RUN=0`, `S7_RUN=0`, `GH_CORE_RUN=0`, `EVENT_REJOIN=0`, `FIGURES_GENERATED=0`, `scientific_logic_change_count=0`.

P0-v3 manifest SHA: `be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776`. Final supplemental package manifest SHA: `78d07fbda2a045ba309a1cfcb23a68ca2baafa910008b6483c0c4e0acf9211bd`. Both source manifests and the scientific assets remained unchanged.

## Decision

`P0V3_FINAL_RECONCILED_MANUSCRIPT_PASS_READY_FOR_FIGURE_RENDERING`

The next authorized task is figure rendering and figure-level QA. This review does not perform that task.

`FINAL_RECONCILIATION_AUDIT_COMMIT` and `push_status` are recorded after the docs-only commit is created.
