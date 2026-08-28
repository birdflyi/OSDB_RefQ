# Chapter 5 RefQ Composite Numeric Provenance Forensics Review v1

Status: docs-only forensic audit; no manuscript, scientific-output, figure, code, manifest, receipt, or supplemental-package modification.

Repository: `D:/github_repo/OSDB_RefQ`

Branch: `ch5-refq-repository-identity-correction-v1`

Repository HEAD before this audit: `c31b820b5bd81bce3b440a26b8af7309682519d7`

The companion inventories are:

- `docs/freeze/ch5_refq_manuscript_composite_numeric_provenance_forensics_v1.csv` (32 claim records: 16 OLD, 16 QA)
- `docs/freeze/ch5_refq_historical_composite_numeric_origin_search_v1.csv` (17 historical-origin records)

## A. Human-frozen decisions

### WiredTiger current authority

The only current authority is `outputs/reference_quotient_p0_corrected_v3/rq1_project_reference_profiles.csv`, row `project_id=2944302`, `repo_name=wiredtiger/wiredtiger`:

- total Reference records: `15,332`
- self-reference records: `12,891`
- external-project Reference records: `19`
- non-project Reference records: `1,096`
- unresolved-target Reference records: `1,326`
- exact self-reference ratio: `0.8407905035220454`
- displayed ratio: `84.08%`

Required closure holds:

`12,891 + 19 + 1,096 + 1,326 = 15,332`

`12,891 / 15,332 = 0.8407905035220454`

The old `100,190 / 84,239` sentence is historical and is not a current authority.

### Quotient eligibility flow

The accepted current chain is:

`3,748,078 scanned - 120 out-of-seed = 3,747,958 admitted`

`1,586,047 target-project-mappable + 1,686,729 target-non-project + 475,182 target-unresolved = 3,747,958 admitted`

`1,447,073 self-loop evidence weight + 138,974 cross-project evidence weight = 1,586,047 eligible weight`

The primary flow authority is `supplemental/reference_quotient_v2/outputs_p0v3/S1_evidence_universe/evidence_universe_flow.csv`; the cross-check authorities are `outputs/reference_quotient_p0_corrected_v3/membership_audit.json` and `outputs/reference_quotient_p0_corrected_v3/quotient_construction_audit.json`.

### Frozen future L8 wording

The future reconciled manuscript must use:

> 经 source-admission 后保留 3,747,958 条 Reference records，其中 1,586,047 条具有可唯一映射到项目的 target endpoint，因而满足 quotient eligibility 并进入 Project-level RefQ aggregation。

This audit does not edit either manuscript.

## B. WiredTiger forensic conclusion

The OLD manuscript contains `84,239 / 100,190`. The exact arithmetic is:

- OLD exact ratio: `84,239 / 100,190 = 0.8407924942609042818644575307`
- current exact ratio: `12,891 / 15,332 = 0.8407905035220453952517610227`
- difference: `0.0000019907388588866126965` in ratio units, or `0.0001990738858886613` percentage points
- OLD display after percentage conversion and two-decimal rounding: `84.08%`
- current display after percentage conversion and two-decimal rounding: `84.08%`

Therefore `same_display_after_rounding = YES`, despite a changed numerator, denominator, record-selection rule, and population universe. Display equality is not authority equality.

The repository-wide exact search found:

- `100190`: exact historical field origin in `data/github_osdb_data/analysis_results/issue_referencing_metrics/df_issue_referencing_metrics.csv` (`total_ref_count`), corroborated by the C2 relation/source-admission receipts. It is a relation-row/issue-referencing universe, not the current Reference-record denominator. Classification: `DERIVED_FROM_DIFFERENT_HISTORICAL_UNIVERSE`.
- `84239`: no exact field occurrence in tracked data, frozen outputs, supplemental outputs, scripts, tests, or docs. It occurs in the OLD manuscript and its migration patch/ledgers. Classification: `TRANSCRIPTION_OR_MANUSCRIPT_ONLY`.

Thus:

`OLD_WIREDTIGER_100190_ORIGIN = DERIVED_FROM_DIFFERENT_HISTORICAL_UNIVERSE`

`OLD_WIREDTIGER_84239_ORIGIN = TRANSCRIPTION_OR_MANUSCRIPT_ONLY`

The current authority remains the P0-v3 profile row, independently of historical origin.

## C. Composite-claim inventory and similar cases

The forensic CSV records 32 composite claims, split evenly between OLD and QA. Row-level class counts are:

- `RATIO_WITH_COUNTS`: 4
- `TOTAL_WITH_PARTITION`: 9
- `PIPELINE_FLOW`: 7
- `COMPLEMENTARY_SHARES`: 4
- `DISPLAY_AGGREGATION`: 2
- `MULTI_AUTHORITY_COMPOSITE`: 6

All 16 QA records have `arithmetic_closure=PASS` and `population_closure=PASS`. The OLD records are retained as historical evidence; their population failures identify stale or mixed universes rather than failures of their historical arithmetic.

### Display-unchanged, support-changed cases

There are 11 OLD-to-QA semantic cases in this forensic class, consisting of the WiredTiger exemplar plus 10 additional cases:

1. WiredTiger: `84.08%`, support `84,239 / 100,190` to `12,891 / 15,332`.
2. Event `IssueComment`: `48.47%`, `1,816,751 / 3,748,078` to `1,816,696 / 3,747,958`.
3. Event `Push`: `31.11%`, `1,166,027 / 3,748,078` to `1,165,990 / 3,747,958`.
4. Event `PullRequest`: `8.95%`, `335,538 / 3,748,078` to `335,530 / 3,747,958`.
5. Event `Issue`: `4.51%`, `168,892 / 3,748,078` to `168,876 / 3,747,958`.
6. Target `GitHub_Service_External_Links`: `43.47%`, `1,629,357 / 3,748,078` to `1,629,327 / 3,747,958`.
7. Target `PullRequest`: `17.93%`, `672,019 / 3,748,078` to `671,986 / 3,747,958`.
8. Target `Actor`: `12.69%`, `475,663 / 3,748,078` to `475,651 / 3,747,958`.
9. Target `Issue`: `7.51%`, `281,662 / 3,748,078` to `281,648 / 3,747,958`.
10. Target `Commit`: `6.80%`, `255,013 / 3,748,078` to `255,009 / 3,747,958`.
11. Target top-1 weight share: `2.47%` remains displayed while observable-target support changes from `6,332` to `6,322`; the OLD top-10/top-50 displays `15.99%/48.97%` and the QA values are `16.00%/48.99%`.

The event and target OLD compact rows close arithmetically within their own historical complete distributions, but their population closure against current QA fails because the admitted denominator and component rows changed. These are `OLD_STALE_QA_CORRECT`, not current QA defects.

### Other population-sensitive cases

- The undirected LCC claim keeps the displayed total `9,472` LCC edges while the node domain changes `6,515 -> 6,506` and LCC nodes change `6,376 -> 6,367`. This is a displayed-total-unchanged/component-population-changed case; it is explicitly captured as `UNDIRECTED_LCC_SCALE`.
- Target coverage remains `42 / 294 = 14.29%`, with unchanged numerator and denominator but a different historical/current target-table population contract. It is not counted in the 11 support-changed cases.
- The category complementary medians retain the displayed pairs (for example, `44.44% + 55.56%`) across the historical/current include-mixed tables. The complement arithmetic is valid at displayed precision; the OLD population is historical and must not be treated as current authority.

### Project-example profile check

The only manuscript example combining a named project, total count, self count, component counts, and a ratio is WiredTiger. The QA row matches the frozen profile exactly:

- row identity: `project_id=2944302`, `wiredtiger/wiredtiger`
- component sum: `12,891 + 19 + 1,096 + 1,326 = 15,332`
- ratio recomputation: `12,891 / 15,332 = 0.8407905035220454`

`row_identity_match=YES`, `component_sum_closure=PASS`, and `ratio_recomputed_from_same_row=PASS`. OLD WiredTiger support is historical and is not retained as current authority. SSDB, GreatSQL, and H2 are mentioned in the QA prose without a composite count tuple; no unsupported composite row was inferred.

## D. Record/entity/edge-unit audit

The QA manuscript is clear about the distinction:

- `1,586,047` is a quotient-eligible **Reference record count** and, under the unit-weight operationalization, the total RefQ evidence weight.
- `1,142,161` is `unique_project_mappable_entities` from `membership_audit.json`; it is an entity count and is not interchangeable with `1,586,047`.
- `9,884` is the directed edge count including self-loops.
- `9,595` is the directed cross-project edge count.
- `9,547` is the undirected edge count after first-order direction-forgetting and reciprocal-pair collapse.

No QA sentence treats `1,586,047` as a project count or as `9,884`/`9,547` edges. No QA sentence treats edge weight as edge count. The operational unit is therefore:

`quotient_eligible_records = total RefQ evidence weight`,

but it is not the number of directed or undirected edges. Result: `quotient_eligible_record_vs_entity_semantics = CLEAR`; `edge_weight_vs_edge_count_semantics = CLEAR`.

The OLD prose is less explicit about the admitted/eligible boundary and is classified as historical/ambiguous documentation only; this is nonblocking because the QA replacement is explicit.

## E. OLD compact-table `Other` audit

Both existing OLD compact tables are exact display aggregations within their own historical complete distributions:

- Event Table 4.1: four displayed rows plus `Other=260,870` equal `3,748,078`; current corresponding long-tail rows sum to `260,866` after the corrected component counts and admitted denominator.
- Target Table 4.2: five displayed rows plus `Other=434,364` equal `3,748,078`; current corresponding long-tail rows sum to `434,337`.

Therefore `display_aggregation_closure=PASS` for both OLD compact tables and `old_compact_table_other_closure_failures = 0`. The tables remain historical evidence and should be replaced by the current complete rows during later reconciliation; no table was edited here.

## F. Current QA blocker assessment

Current QA composite claims:

- arithmetic failures: `0`
- population failures: `0`
- `MIXED_AUTHORITY_INCONSISTENT` failures: `0`
- record/entity/edge unit-semantics failures: `0`
- unsupported current frozen composite values: `0`

The QA authority usage is either `SINGLE_FROZEN_AUTHORITY` or `MULTIPLE_FROZEN_AUTHORITIES_SAME_UNIVERSE`. Where S1 and P0-v3 files are both cited, the shared contract is explicit: S1 supplies the source-admission flow, while P0-v3 supplies the quotient and graph projections over the same admitted/eligible universe. No current QA blocker was found.

The historical `84239` provenance remains unresolved beyond manuscript/transcription evidence, but the current replacement is unambiguous; classify it as `HISTORICAL_PROVENANCE_UNRESOLVED_NONBLOCKING`.

## G. Recommendation

The current QA composite claims close arithmetically and by population, all current values are backed by the frozen P0-v3/supplemental authorities, and all OLD mixed/stale cases have an unambiguous current replacement. The narrow forensic gate is therefore passed.

Recommendation:

`READY_FOR_THREE_WAY_CONSERVATIVE_RECONCILIATION_AUDIT`

The previously proposed full three-way prose audit remains deferred until this forensic result is accepted. No reconciliation, manuscript edit, scientific rerun, figure rendering, or full authority rebuild was performed in this task.

## H. Final status

```text
repository_HEAD_before = c31b820b5bd81bce3b440a26b8af7309682519d7
OLD_SHA = 4BA2DB1B45C97D0823C4909C705FC307AA3A992E4B2C2E59096FC630A871FD88
QA_SHA = D353BB462BC3D4D0C07FA572AAF5B4DF64805B7E032C0A1587F641D0F3214831

human_frozen_WiredTiger_authority = PASS
wiredtiger_current_total = 15332
wiredtiger_current_self = 12891
wiredtiger_current_ratio_exact = 0.8407905035220454
wiredtiger_current_ratio_display = 84.08%
wiredtiger_old_total = 100190
wiredtiger_old_self = 84239
wiredtiger_old_ratio_exact = 0.8407924942609042818644575307
wiredtiger_old_ratio_display = 84.08%
wiredtiger_same_display_after_rounding = YES

OLD_WIREDTIGER_100190_ORIGIN = DERIVED_FROM_DIFFERENT_HISTORICAL_UNIVERSE
OLD_WIREDTIGER_84239_ORIGIN = TRANSCRIPTION_OR_MANUSCRIPT_ONLY

L8_frozen_flow_closure = PASS
scanned_records = 3748078
admitted_records = 3747958
out_of_seed_records = 120
project_mappable_target_records = 1586047
non_project_target_records = 1686729
unresolved_target_records = 475182
self_loop_weight = 1447073
cross_project_weight = 138974
record_partition_closure = PASS
weight_partition_closure = PASS

composite_claims_old = 16
composite_claims_qa = 16
ratio_with_counts_claims = 4
total_with_partition_claims = 9
pipeline_flow_claims = 7
display_aggregation_claims = 2
unchanged_display_changed_support_claims = 11
multi_authority_composite_claims = 6

additional_cases_similar_to_wiredtiger = 10
old_mixed_authority_cases = 1 semantic pair (2 claim rows)
old_unresolved_historical_provenance_cases = 1 (84239; nonblocking)

current_QA_arithmetic_failures = 0
current_QA_population_failures = 0
current_QA_mixed_authority_failures = 0
current_QA_unit_semantics_failures = 0

quotient_eligible_record_vs_entity_semantics = CLEAR
edge_weight_vs_edge_count_semantics = CLEAR
old_compact_table_other_closure_failures = 0

reconciliation_readiness = READY
manuscripts_modified = NO
scientific_outputs_modified = NO
figures_generated = 0
scientific_logic_change_count = 0

P0_manifest_SHA = be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776
final_supplemental_package_manifest_SHA = 78d07fbda2a045ba309a1cfcb23a68ca2baafa910008b6483c0c4e0acf9211bd
COMPOSITE_NUMERIC_FORENSICS_COMMIT = final repository HEAD (resolved by git after this docs-only commit)
push_status = VERIFIED_REMOTE_EQUALS_HEAD
decision = P0V3_COMPOSITE_NUMERIC_FORENSICS_PASS_READY_FOR_THREE_WAY_RECONCILIATION
```
