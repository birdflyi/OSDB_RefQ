# Chapter 5 RefQ Composite Numeric Provenance Forensics v2 Review

Repository: `D:/github_repo/OSDB_RefQ`  
Branch: `ch5-refq-repository-identity-correction-v1`  
Starting HEAD: `58e94c115de840736b05573c84366125eb50a578`

This is a docs-only correction pass. The v1 artifacts and commit remain immutable historical evidence. The v1 artifacts are classified as:

`SUPERSEDED_BY_V2_FOR_RECONCILIATION_CONTROL`

No manuscript, figure, scientific output, supplemental package, manifest, receipt, code, or scientific logic was changed.

## 1. Frozen scientific anchors

The current WiredTiger authority is P0-v3 row `project_id=2944302`, `wiredtiger/wiredtiger`: `15,332` total Reference records, `12,891` self-reference records, `19` external-project records, `1,096` non-project records, `1,326` unresolved-target records, and exact ratio `0.8407905035220454` (`84.08%`). The row closure is:

`12,891 + 19 + 1,096 + 1,326 = 15,332` and `12,891 / 15,332 = 0.8407905035220454`.

The frozen L8 semantics remain:

> 经 source-admission 后保留 3,747,958 条 Reference records，其中 1,586,047 条具有可唯一映射到项目的 target endpoint，因而满足 quotient eligibility 并进入 Project-level RefQ aggregation。

The flow closure is:

`3,748,078 - 120 = 3,747,958`

`1,586,047 + 1,686,729 + 475,182 = 3,747,958`

`1,447,073 + 138,974 = 1,586,047`.

## 2. LCC factual correction

The v1 statement that old LCC edge count `9,472` was unchanged is false and is withdrawn. Exact values are:

| quantity | OLD | QA/current |
|---|---:|---:|
| node domain | 6,515 | 6,506 |
| undirected edges | 9,557 | 9,547 |
| LCC nodes | 6,376 | 6,367 |
| LCC edges | 9,472 | 9,462 |

Therefore:

`LCC_EDGE_COUNT_UNCHANGED = FALSE`

The v2 atomic records do not classify `9,472` as a display-unchanged current value.

## 3. Atomic relation rule

The v2 CSV has one row per atomic numeric relation. A row receives `arithmetic_closure=PASS` only when the exact relation in that row closes. Paragraphs containing several relationships are split into separate rows, including:

- source-admission subtraction;
- target membership partition;
- self-loop/cross-project weight partition;
- directed edge partition;
- target seed/expanded partition;
- target top-1, top-10, and top-50 shares;
- LCC coverage;
- WiredTiger ratio and component sum;
- compact-table `Other` aggregation;
- category share complements and age-correlation sign complement.

The v2 inventory contains 78 atomic records with complete 26-column structure. Historical rows may have `population_closure=FAIL` because their universe is superseded; this does not turn a closed historical equality into a current authority.

## 4. Top-1 / top-10 / top-50 recheck

The target concentration denominator is `total_cross_project_weight`, not observable-target count.

| share | OLD support | OLD exact | OLD display | QA/current support | QA exact | QA display |
|---|---:|---:|---:|---:|---:|---:|
| top-1 | 3,430 / 139,044 | 0.0246684502747331779868243146 | 2.47% | 3,430 / 138,974 | 0.0246808755594571646495027847 | 2.47% |
| top-10 | 22,234 / 139,044 | 0.15990621673714794 | 15.99% | 22,234 / 138,974 | 0.15998676011340252 | 16.00% |
| top-50 | 68,087 / 139,044 | 0.48967952590546876 | 48.97% | 68,087 / 138,974 | 0.4899261732410379 | 48.99% |

Only top-1 satisfies `UNCHANGED_DISPLAY_CHANGED_SUPPORT`: its denominator changes while displayed `2.47%` remains. Top-10 and top-50 have changed displays and are stale OLD values, not unchanged-display cases. The prior observable-target change `6,332 -> 6,322` is not used as weight-share support.

## 5. Corrected analogous-case count

Independent recomputation gives:

- total `unchanged_display_changed_support_claims_v2 = 11` semantic OLD-to-QA cases: WiredTiger (1), four source-event shares, five target-entity shares, and target top-1 weight share (1);
- `additional_cases_similar_to_wiredtiger_v2 = 10` excluding WiredTiger.

The count remains numerically 11/10 only because the actual frozen top-1 weight denominator change confirms the case. It is not carried forward by parity. The LCC edge-count case is excluded because its displayed LCC edge total changes `9,472 -> 9,462`.

## 6. Event and target distribution checks

The four event shares IssueComment, Push, PullRequest, and Issue each retain the same two-decimal display between OLD and QA while both numerator and admitted denominator change. Their v2 atomic rows record exact fractions and rounding closure.

The five target shares GitHub_Service_External_Links, PullRequest, Actor, Issue, and Commit behave the same way. OLD compact rows close as `top rows + Other = 3,748,078` in their historical distribution; current full rows close as `sum = 3,747,958` admitted records.

## 7. Compact-table neutrality

The forensic gate does not decide the final main-text schema. Both OLD compact schemas remain technically reconstructible:

- Table 4.1 current display-only `Other = 260,866`, the exact sum of current non-top-four event rows;
- Table 4.2 current display-only `Other = 434,337`, the exact sum of current non-top-five target rows.

Both aggregation closures are `PASS`. Final compact-versus-full presentation is deferred:

`PRESENTATION_DECISION_DEFERRED_TO_THREE_WAY_AUDIT`

## 8. WiredTiger finding

OLD `84,239 / 100,190` equals `0.8407924942609042818644575307`, while current `12,891 / 15,332` equals `0.8407905035220453952517610227`. The difference is `0.0001990738858886613` percentage points, and both round to `84.08%`. `100,190` has a historical relation-row field origin; `84,239` is manuscript/transcription-only. The OLD pair is therefore historical mixed authority and must not be restored.

## 9. Phase-A hard gate

All current QA atomic records close:

```text
current_QA_atomic_arithmetic_failures = 0
current_QA_atomic_population_failures = 0
current_QA_atomic_mixed_authority_failures = 0
current_QA_atomic_unit_failures = 0
WIREDTIGER_CURRENT_CLOSURE = PASS
L8_FLOW_CLOSURE = PASS
LCC_CURRENT_CLOSURE = PASS
```

Phase A passes. No current QA atomic defect was found, so Phase B is authorized to proceed. This authorization is limited to the three-way audit documents specified by the Phase-A/B instruction; it does not authorize manuscript editing or scientific reruns.

## 10. Phase-A status

```text
FORENSICS_V1_STATUS = SUPERSEDED_BY_V2_FOR_RECONCILIATION_CONTROL
LCC_old_edges = 9472
LCC_current_edges = 9462
LCC_edge_unchanged_claim_corrected = YES
top1_same_display_changed_support = YES
unchanged_display_changed_support_claims_v1 = 11
unchanged_display_changed_support_claims_v2 = 11
additional_cases_similar_to_wiredtiger_v2 = 10
Table_4_1_compact_reconstructible = YES
Table_4_1_current_Other = 260866
Table_4_2_compact_reconstructible = YES
Table_4_2_current_Other = 434337
scientific_logic_change_count = 0
decision = PHASE_A_PASS_CONTINUE_TO_PHASE_B
```
