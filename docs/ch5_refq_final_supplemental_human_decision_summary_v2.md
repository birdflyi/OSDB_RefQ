# Chapter 5 RefQ Final Supplemental Human-Decision Summary v2

## Decision

```text
FINAL_SUPPLEMENTAL_HUMAN_DECISION = PASS_READY_FOR_FREEZE
```

This is a read-only synthesis of already available P0, S1-S7, S2 semantic
audit, S3 correction, and provenance materials. No experiment, raw scan,
P0/S1-S7 rerun, manuscript modification, commit, or push was performed for
this summary.

## 1. Frozen scientific status

| Package | Status | Human-use role |
|---|---|---|
| P0/P0.1 | FROZEN | Scientific and numerical reference |
| S1 | PASS | Main evidence-universe and boundary result |
| S2 | PASS under `REFERENCE_RECORD_MULTIPLICITY` | Threshold sensitivity; supplement/reviewer reserve |
| S3 | PASS after corrected reproducibility patch | Observation-boundary sensitivity; use corrected result only |
| S4 | PASS_WITH_PARTITION_SENSITIVITY | Community robustness reserve |
| S5 | PASS | Brokerage stability reserve/table |
| S6 | PASS | Figure-ready derivations |
| S7 | PASS | Supplementary/reviewer reserve |

The old S3 result is explicitly superseded:

```text
old S3 = SUPERSEDED_S3_NONCANONICAL_LOUVAIN_CONSTRUCTION_ORDER
corrected S3 = supplemental/reference_quotient_v1/v1_2_s3_reproducibility_patch/outputs/S3_observation_sensitivity_corrected/
```

## 2. S1: boundary-aware two-universe result

The observable Reference universe contains `3,748,078` retained Reference
records. The existing S1 flow closes exactly:

| Stage | Count | Unit |
|---|---:|---|
| Observable Reference records | 3,748,078 | RECORD |
| Project-mappable targets | 1,586,121 | RECORD |
| Non-project targets | 1,686,763 | RECORD |
| Unresolved targets | 475,194 | RECORD |
| Ambiguous targets | 0 | RECORD |
| Conflict-excluded occurrences | 4 | RECORD |
| Quotient-eligible records | 1,586,117 | RECORD |
| Self-loop evidence weight | 1,447,073 | REFERENCE_RECORD (aggregated edge weight) |
| Cross-project evidence weight | 139,044 | REFERENCE_RECORD (aggregated edge weight) |
| Self-loop edge count | 289 | EDGE COUNT |
| Cross-project directed edge count | 9,605 | EDGE COUNT |

The closure checks are all true: target-status partition, conflict
exclusion, edge-weight closure, cross-tab reconciliation, and exact P0
reconciliation.

The eligible edge-class tables use `REFERENCE_RECORD` as their unit. Their
main descriptive pattern is that Push and IssueComment are the largest
source-side contributors, while target-side project-mappable references are
dominated by PullRequest, Issue, Commit, FileChange, and Repo targets. The
cross-project and self-loop split is an observational boundary, not a
dependency or knowledge-flow classification.

S1 supports a two-universe presentation:

1. RQ1 retains project-mappable, non-project, and unresolved observable
   Reference evidence as distinct categories.
2. RefQN uses only quotient-eligible project-mappable evidence under the
   explicit membership contract.

No dependency, semantic intent, or knowledge-flow inference follows from
these counts.

## 3. S2: Reference-record multiplicity sensitivity

The S2 operation filters the frozen directed cross-project edge table using
`weight >= threshold` before undirected collapse. The weight semantics are:

```text
one unit per retained eligible fine-grained Reference record,
aggregated by ordered source/target project pair
```

Therefore `w >= 2` means **at least two retained Reference-record
occurrences for the directed project pair**. It does not mean two distinct
events, two independent citations, two semantically independent references,
or repeated support from multiple events.

| Threshold | Directed edges | Retained record weight | Weight share | Undirected edges | LCC nodes | LCC coverage | Isolates | Components | Clustering | Transitivity | Communities | Modularity |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 9,605 | 139,044 | 1.000000 | 9,557 | 6,376 | 0.978665 | 30 | 55 | 0.042198 | 0.008046 | 34 | 0.797310 |
| 2 | 4,865 | 134,304 | 0.965910 | 4,832 | 3,199 | 0.491021 | 3,155 | 3,199 | 0.036552 | 0.009226 | 32 | 0.796627 |
| 5 | 2,331 | 127,726 | 0.918601 | 2,313 | 1,546 | 0.237299 | 4,866 | 4,899 | 0.027413 | 0.008874 | 26 | 0.796403 |
| 10 | 1,447 | 121,937 | 0.876967 | 1,437 | 975 | 0.149655 | 5,409 | 5,448 | 0.022237 | 0.007724 | 21 | 0.785699 |

The human interpretation should remain separated into three sensitivities:

* **Connectivity sensitivity:** low record-multiplicity edges contribute
  strongly to observable coverage and connectivity. Removing them sharply
  reduces LCC coverage and increases isolates/components.
* **Record-weight-mass sensitivity:** higher-multiplicity relations retain a
  large share of aggregate Reference-record weight. Even `w >= 10` retains
  `87.6967%` of cross-project record weight.
* **Modularity sensitivity:** modularity changes modestly from `0.797310` at
  threshold 1 to `0.785699` at threshold 10, while the algorithmic community
  count decreases from 34 to 21.

Recommended wording is `record-multiplicity threshold` or
`Reference-record multiplicity threshold`. Do not call the removed edges
weak semantic links, single-event links, or one-off semantic references.

S2 role:

```text
S2_role = SUPPLEMENTARY_RESULT_RECOMMENDED
S2_weight_semantics = REFERENCE_RECORD_MULTIPLICITY
S2_recalculation_required = NO
```

## 4. S3: corrected observation-boundary sensitivity

Only the corrected S3 result is valid for human interpretation. The three
views are first-order undirected views under the corrected deterministic
construction rule.

| View | Nodes | Directed edges | Directed weight | Undirected edges | Components | Isolates | LCC nodes | LCC coverage | Clustering | Transitivity | Communities | Modularity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `CANONICAL_SEED_CENTERED_OBSERVED` | 6,515 | 9,605 | 139,044 | 9,557 | 55 | 30 | 6,376 | 0.978665 | 0.042198 | 0.008046 | 34 | 0.797310 |
| `SEED_ONLY_INDUCED` | 294 | 419 | 7,631 | 371 | 129 | 123 | 157 | 0.534014 | 0.176942 | 0.162566 | 13 | 0.764055 |
| `MULTI_SEED_TARGET_VIEW` | 1,299 | 4,349 | 69,670 | 4,310 | 63 | 62 | 1,237 | 0.952271 | 0.219723 | 0.034029 | 20 | 0.776438 |

The corrected canonical row exactly recovers the P0 structural reference:

```text
community_count = 34
modularity = 0.7973095950243088
random_seed = 20260731
```

The old canonical row (`33` communities and approximately `0.7962346034`)
was caused by a different graph-construction/node-insertion order and is
superseded. The corrected views show **observation-boundary sensitivity**;
they do not establish that a restricted view is more correct or more
complete than the seed-centered observed view.

S3 role:

```text
S3_role = BOUNDARY_SENTENCE_RECOMMENDED
S3_corrected_result_used = YES
```

Detailed S3 values are best retained as a supplementary result.

## 5. S4: community stability

The existing 50-run Louvain results use the predefined seed range beginning
at `20260731`. Community counts are distributed as follows:

```text
32 communities = 3 runs
33 communities = 9 runs
34 communities = 16 runs
35 communities = 14 runs
36 communities = 6 runs
37 communities = 2 runs
```

The canonical seed recovers 34 communities and modularity
`0.7973095950243088`. Across runs, modularity ranges from
`0.796486248799138` to `0.797575735271457`, with mean
`0.797113045325487`. ARI to the canonical partition has minimum
`0.7491365325189081`, mean `0.8739466232106914`, and maximum `1.0`.
Pairwise ARI has minimum `0.639377189055702`, mean
`0.8572026597530258`, and maximum `0.9949632521455954`.

The correct interpretation is:

```text
MODULAR_STRUCTURE_STRENGTH = STABLE
EXACT_COMMUNITY_PARTITION = PARTITION_SENSITIVE
```

Community IDs must not be treated as stable DBMS subdomains, semantic
communities, or substantive project categories.

S4 role:

```text
S4_role = SUPPLEMENTARY_RESULT_RECOMMENDED
community_exact_partition_stability = PARTITION_SENSITIVE
```

## 6. S5: brokerage stability

The corrected `brokerage_topk_inclusion_frequency.csv` is the authoritative
inclusion-frequency file. It covers `k = 250, 500, 1000`, with 20 predefined
seeds for each `k`.

The canonical top five structural brokerage candidates are:

```text
60246359
17165658
16563587
453068084
334274271
```

Each of these five has `20/20` inclusion in the top-10 for every one of
`k = 250`, `500`, and `1000`. This supports the cautious statement that the
canonical top-five **structural brokerage candidates** remain top-10 across
all predefined `k`/seed sensitivity runs.

Overall stability is strong but not uniform at every rank: Spearman
correlation to the canonical ranking ranges from `0.9998289911273206` to
`1.0`, while top-50 overlap has mean `0.91` and minimum `0.82`.

Use `structural brokerage candidates`, not most important projects,
influential projects, or knowledge brokers.

S5 role:

```text
S5_role = SUPPLEMENTARY_RESULT_RECOMMENDED
brokerage_candidate_stability = STABLE_FOR_CANONICAL_TOP-FIVE_TOP-10_INCLUSION
```

A compact table or supplementary figure is preferable to a large main-text
ranking.

## 7. S6: figure-ready evidence

S6 is a derivation layer with source-artifact SHA references. It includes
stable plotting tables for RQ1 composition, RQ1 profiles, RQ2a source role,
RQ2b target role/concentration, RQ3 descriptive and FDR/effect-size results,
edge-weight distributions, community-size distribution, structural summary,
brokerage candidates, and S4/S5 stability views.

The recommended main figure set is:

1. **Figure 1:** evidence-universe flow and RQ1 composition.
2. **Figure 2:** RQ2a source role and RQ2b target concentration.
3. **Figure 3:** RQ2c structural summary, with observation/community
   robustness shown in a bounded inset or companion panel where readable.
4. **Figure 4:** RQ3 effect sizes and FDR results for the two label modes.

Brokerage should use a compact table or supplementary figure. A full
6,376-node community-colored hairball is not recommended. S2 threshold
sensitivity is better placed in the supplement or reviewer reserve.

S6 role:

```text
S6_class = FIGURE_READY_DERIVATION
S6_role = MAIN_TEXT_FIGURE_SUPPORT
original_decision_label = MAIN_TEXT_RESULT_RECOMMENDED
```

The historical `MAIN_TEXT_RESULT_RECOMMENDED` label referred to main-text
use of selected derived data. S6 is classified here as a figure-ready
derivation layer, not as a new scientific result or as a requirement to
present every S6 derivative in the main text.

## 8. S7: fine-grained composition reserve

S7 should remain supplementary/reviewer reserve. It describes the event,
source-entity, and target-entity composition of fixed top source, target,
and edge sets. For example, the fixed top source composition is dominated by
PushEvent records, while the shown top edge is dominated by
IssueCommentEvent records. These are composition concentrations only.

S7 does not support claims about dependency, project importance, bots,
knowledge flow, or causal mechanisms. No additional raw scan is recommended
for this decision summary.

```text
S7_role = SUPPLEMENTARY_RESULT_RECOMMENDED
```

## 9. Manuscript impact without editing

| Package | Primary classification | Wording implication |
|---|---|---|
| S1 | `MAIN_TEXT_RESULT_RECOMMENDED` | Define the observable Reference universe and the project-mappable/non-project boundary. |
| S2 | `SUPPLEMENTARY_RESULT_RECOMMENDED` | State record-level multiplicity explicitly; do not imply event or semantic independence. |
| S3 | `BOUNDARY_SENTENCE_RECOMMENDED` | State that restricted observation views change coverage and structural summaries; use corrected S3 only. |
| S4 | `SUPPLEMENTARY_RESULT_RECOMMENDED` | Separate stable modular structure from partition-sensitive exact communities. |
| S5 | `SUPPLEMENTARY_RESULT_RECOMMENDED` | Report structural brokerage candidates and the canonical top-five top-10 stability, without importance/causality language. |
| S6 | `FIGURE_READY_DERIVATION` / `MAIN_TEXT_FIGURE_SUPPORT` | Use selected derivations to support the four main figures; the historical `MAIN_TEXT_RESULT_RECOMMENDED` label referred to this derived-data use. |
| S7 | `SUPPLEMENTARY_RESULT_RECOMMENDED` | Keep evidence composition as reviewer reserve and descriptive support. |

The following boundary sentences are recommended for any future manuscript
patch, but were not applied here:

* **Edge weight:** “RefQ edge weight denotes the aggregated multiplicity of
  retained eligible Reference records for an ordered project pair.”
* **S2:** “Threshold sensitivity is defined over Reference-record
  multiplicity, not distinct-event or semantically independent citation
  support.”
* **Observation boundary:** “Restricted views are sensitivity analyses of
  the observation boundary and do not constitute more complete or more
  correct ecosystem graphs.”
* **Louvain:** “The results support stable modular structure, while the
  exact community partition is sensitive to the seeded run.”
* **Brokerage:** “The reported entities are structural brokerage candidates
  under the defined graph and sampling boundary, not validated influential
  projects or knowledge brokers.”

## 10. Provenance residuals

The local history distinguishes implementation commits from result/report
commits:

```text
supplemental_v1_implementation_commit = 18717e7d8d269538872ab5a3bcb923234e52eecc
supplemental_v1_result_commit = ba72987adb2c2339bdf1f7a3b370278c88c29c3c
v1_1_completion_implementation_commit = d222654e2edfac07265f6a86f65c26c3d089d8e1
v1_1_completion_result_commit = d88c2f872f8fb2ec71261b7f1bdaa5423afff0e7
s3_patch_implementation_commit = 9cb5dbdd4ecebc93acfb892cf0c757de5d34b43e
s3_patch_result_commit/current_HEAD = 3720b76e863261afd520113bf5ce5bfda46df4ea
canonical_parent = 920286e134ca459c8e155942eabc6798ceab8b65
```

The S3 patch implementation commit contains the patch code/tests; the
current HEAD contains the corrected S3 generated outputs and patch report.
The current untracked S2 semantics audit report is intentionally not treated
as a result commit.

## 11. Controls

```text
raw_scan_count_this_task = 0
experiments_rerun = 0
P0_rerun = 0
S1-S7_rerun = 0
manuscript_modified = NO
P0_outputs_modified = NO
supplemental_existing_outputs_modified = NO
commit = NONE
push = NONE
```

## Final fields

```text
FINAL_SUPPLEMENTAL_HUMAN_DECISION = PASS_READY_FOR_FREEZE
S1_role = MAIN_TEXT_RESULT_RECOMMENDED
S2_role = SUPPLEMENTARY_RESULT_RECOMMENDED
S3_role = BOUNDARY_SENTENCE_RECOMMENDED
S4_role = SUPPLEMENTARY_RESULT_RECOMMENDED
S5_role = SUPPLEMENTARY_RESULT_RECOMMENDED
S6_class = FIGURE_READY_DERIVATION
S6_role = MAIN_TEXT_FIGURE_SUPPORT
original_decision_label = MAIN_TEXT_RESULT_RECOMMENDED
S7_role = SUPPLEMENTARY_RESULT_RECOMMENDED
S2_weight_semantics = REFERENCE_RECORD_MULTIPLICITY
S2_recalculation_required = NO
S3_corrected_result_used = YES
community_exact_partition_stability = PARTITION_SENSITIVE
brokerage_candidate_stability = STABLE_FOR_CANONICAL_TOP-FIVE_TOP-10_INCLUSION
raw_scan_count_this_task = 0
experiments_rerun = 0
report_path = docs/ch5_refq_final_supplemental_human_decision_summary_v2.md
```
