# Chapter 5 RefQ C3 Scientific Impact Review v1

Review date: 2026-08-25

Final decision: `C3_IMPACT_REQUIRES_EXPERIMENT_RERUN`

This is a read-only comparison of the historical frozen P0 bundle and the
existing corrected candidate P0 bundle. No P0 rerun, GH-CoRE extraction,
GitHub API call, raw external rescan, S1-S7 rerun, figure render, manuscript
edit, frozen-output edit, or main-branch edit was performed.

## 1. Executive conclusion

The repository identity correction is source-localized: every changed directed
edge originates at Fireproof source project `679889516`, and the existing C2
diff artifact identifies the same seed as the expected source-provenance change.
There are 10 removed edge pairs and one reduced edge pair; no edge pair is
added or increased.

The correction is not scientifically null. Most RQ1 and RQ2a/RQ2b changes are
small or confined to Fireproof and low-weight target leaves, with the RQ2a
source top-50 and RQ2b target top-50 sets and order unchanged. However:

- the RQ1 project-age association for `self_reference_ratio` and its
  complementary `external_reference_share` crosses the nominal `p < 0.05`
  threshold, from `0.070299` to `0.043982`;
- RQ2c changes the community count from 34 to 35 and changes the brokerage
  top-50 by two removed and two added projects;
- corrected S1-S6 dependencies are changed and require corrected reruns or
  corrected derivations before those results can support a new freeze.

The result is therefore a localized but analysis-relevant impact, not a
network-wide source contamination finding and not an interpretation-preserving
no-op.

## 2. Bundle inventory and hash validation

| bundle | manifest SHA-256 | status | output files | manifest inputs | output validation |
|---|---|---|---:|---:|---|
| historical frozen v1 | `a3089fd8a6a58c0a15d2192a7b5f3388868ef0f1358c803be3aa4f27314c59f6` | `PASS` | 30 | 296 | 30/30 present, bytes and hashes match |
| corrected candidate v2 | `21699353d5dc9476547ee7f56881ba0a1ccc842a6d3c95adad9a28dedfd656d7` | `PASS` | 30 | 296 | 30/30 present, bytes and hashes match |

Both manifests use schema `reference_quotient_p0_frozen_manifest_v1` and record
294 analysis seeds. The historical run window is
`2026-08-18T14:57:25.119552+00:00` to
`2026-08-18T14:59:10.993412+00:00`; the corrected run window is
`2026-08-25T12:28:46.800444+00:00` to
`2026-08-25T12:34:45.278799+00:00`.

The output roots are:

```text
outputs/reference_quotient_p0_frozen
outputs/reference_quotient_p0_corrected_v2
```

The corrected manifest and output hashes were checked directly against current
files. No output was regenerated or rewritten.

## 3. Global metric comparison

The classification vocabulary is:

```text
UNCHANGED
NUMERIC_DRIFT_ONLY
INTERPRETATION_RELEVANT
```

### RQ1

| metric | frozen v1 | corrected v2 | delta | classification |
|---|---:|---:|---:|---|
| analysis seed count | 294 | 294 | 0 | UNCHANGED |
| candidate seed count | 301 | 301 | 0 | UNCHANGED |
| profile rows / observed project rows | 294 / 262 positive-out-degree seeds | 294 / 262 positive-out-degree seeds | 0 | UNCHANGED |
| fine-grained Reference records | 3,748,078 | 3,747,958 | -120 | NUMERIC_DRIFT_ONLY |
| quotient-eligible Reference records | 1,586,117 | 1,586,047 | -70 | NUMERIC_DRIFT_ONLY |
| target project-mappable records | 1,586,121 | 1,586,047 | -74 | NUMERIC_DRIFT_ONLY |
| target non-project records | 1,686,763 | 1,686,729 | -34 | NUMERIC_DRIFT_ONLY |
| target unresolved records | 475,194 | 475,182 | -12 | NUMERIC_DRIFT_ONLY |
| target observable rows | 6,332 | 6,322 | -10 | NUMERIC_DRIFT_ONLY |

All eight event-type counts change only by the removed 120 records. The largest
count changes are `IssueCommentEvent -55`, `PushEvent -37`, `IssuesEvent -16`,
and `PullRequestEvent -8`. Referenced-entity and referencing-entity counts show
the same localized numeric drift.

The only changed row in `rq1_project_reference_profiles.csv` is Fireproof:

```text
total_reference_records       178 -> 58
external_project_reference_records 83 -> 9
non_project_reference_records 44 -> 10
unresolved_target_reference_records 16 -> 4
self_reference_ratio         0.196629 -> 0.603448
external_reference_share     0.803371 -> 0.396552
```

The project-age association table changes as follows:

| metric | frozen rho | corrected rho | frozen p | corrected p | classification |
|---|---:|---:|---:|---:|---|
| self-reference ratio | -0.106260 | -0.118173 | 0.070299 | 0.043982 | INTERPRETATION_RELEVANT |
| external reference share | 0.106260 | 0.118173 | 0.070299 | 0.043982 | INTERPRETATION_RELEVANT |
| non-project reference share | 0.154217 | 0.157359 | 0.008409 | 0.007155 | NUMERIC_DRIFT_ONLY |
| comment reference density | 0.142259 | 0.141747 | 0.015154 | 0.015527 | NUMERIC_DRIFT_ONLY |

### RQ2a

| metric | frozen v1 | corrected v2 | classification |
|---|---:|---:|---|
| source node rows | 294 | 294 | UNCHANGED |
| changed source-role rows | 0 | 1, Fireproof | NUMERIC_DRIFT_ONLY |
| source top-50 overlap | - | 50/50; order unchanged | UNCHANGED |

Fireproof source role metrics change from out-degree 17 and out-strength 79 to
out-degree 7 and out-strength 9. The source top-50 ranking is unchanged in set
membership and order, so the source-role headline ranking is stable even though
the corrected Fireproof row must be used for any complete table.

### RQ2b

| metric | frozen v1 | corrected v2 | delta | classification |
|---|---:|---:|---:|---|
| observable target rows | 6,332 | 6,322 | -10 | NUMERIC_DRIFT_ONLY |
| target-role rows removed | 0 | 10 | +10 removed | NUMERIC_DRIFT_ONLY |
| top-1 weight share | 0.024668 | 0.024681 | +0.000012 | NUMERIC_DRIFT_ONLY |
| top-10 weight share | 0.159906 | 0.159987 | +0.000081 | NUMERIC_DRIFT_ONLY |
| top-50 weight share | 0.489680 | 0.489926 | +0.000247 | NUMERIC_DRIFT_ONLY |
| target top-50 overlap | - | 50/50; order unchanged | 0 | UNCHANGED |

The ten removed targets are low-weight single-source leaves. The target-role
table has numeric cumulative-share drift across common rows because the total
cross-project denominator changes, but the top target set and order do not
change.

### RQ2c

| metric | frozen v1 | corrected v2 | delta | classification |
|---|---:|---:|---:|---|
| directed edges including self-loops | 9,894 | 9,884 | -10 | NUMERIC_DRIFT_ONLY |
| total edge weight | 1,586,117 | 1,586,047 | -70 | NUMERIC_DRIFT_ONLY |
| self-loop edges | 289 | 289 | 0 | UNCHANGED |
| cross-project directed edges | 9,605 | 9,595 | -10 | NUMERIC_DRIFT_ONLY |
| cross-project weight | 139,044 | 138,974 | -70 | NUMERIC_DRIFT_ONLY |
| node domain | 6,515 | 6,506 | -9 | NUMERIC_DRIFT_ONLY |
| edge-observed nodes | 6,514 | 6,505 | -9 | NUMERIC_DRIFT_ONLY |
| connected components | 55 | 55 | 0 | UNCHANGED |
| isolates | 30 | 30 | 0 | UNCHANGED |
| LCC nodes | 6,376 | 6,367 | -9 | NUMERIC_DRIFT_ONLY |
| LCC edges | 9,472 | 9,462 | -10 | NUMERIC_DRIFT_ONLY |
| algorithmic communities | 34 | 35 | +1 | INTERPRETATION_RELEVANT |
| modularity | 0.797310 | 0.796922 | -0.000388 | NUMERIC_DRIFT_ONLY |
| brokerage top-50 overlap | - | 48/50 | 2 removed, 2 added | INTERPRETATION_RELEVANT |

The brokerage top-50 removals are project IDs `105944401` and `724712`; the
additions are `341631350` and `99919302`. The community count changes despite
the broad component and LCC coverage conclusions remaining stable.

### RQ3

The role-aware feature table remains 294 rows. Numeric changes are localized in
the Fireproof source-role and evidence fields, while betweenness values change
for 228 network-observed rows because the graph is recomputed after the local
edge correction. The subdomain table remains 185 rows; 34 mean fields, 26
median fields, and 34 standard-deviation fields change.

The 22-row Kruskal/FDR table has numeric p-value and effect-size drift, but:

```text
uncorrected p < 0.05 significance flips = 0
FDR reject-at-0.05 flips = 0
```

RQ3 statistical conclusions are therefore unchanged, although corrected
numeric tables would be required for a corrected baseline.

## 4. Edge localization

The directed edge comparison gives:

| change type | count |
|---|---:|
| removed edge pairs | 10 |
| reduced-weight edge pairs | 1 |
| added edge pairs | 0 |
| increased-weight edge pairs | 0 |
| affected edge pairs | 11 |
| affected source projects | 1 |
| affected target projects | 11 |

All changed pairs have source project `679889516` (Fireproof). Nine pairs are
removed entirely. The remaining pair `679889516 -> 600271677` is reduced from
weight 59 to weight 2. The other ten affected targets are
`238372891`, `240147659`, `315520343`, `322195640`, `33999965`, `593957637`,
`607441698`, `623716378`, `647017093`, and `654343821`. Nine of those ten are
removed from the node registry; `607441698` remains because it has other
network evidence beyond the removed Fireproof edge.

Required conclusion:

```text
SOURCE_LOCALIZED
```

This conclusion applies to source-observation contamination. It does not mean
that derived network measures remain byte-identical: centrality and Louvain
outputs are functions of the changed graph and therefore show downstream
numeric drift.

## 5. Removed-node impact

The nine removed node IDs are:

```text
238372891, 240147659, 315520343, 322195640, 33999965,
593957637, 623716378, 647017093, 654343821
```

For every removed node in the frozen graph:

- there is exactly one incoming edge, from Fireproof;
- there are no outgoing edges;
- undirected degree is 1;
- brokerage is 0.0;
- the nodes occur in frozen community 12 but none is in the target top-50;
- none is in the brokerage top-50 or RQ3 feature rows.

Classification: all nine are `isolated target introduced only by erroneous
source records`; none is a multi-source node or an important network node.
They are present in the frozen community/brokerage candidate universe only as
degree-one leaves, not as top-ranked structural actors.

## 6. Research-question impact

| research question | impact | basis |
|---|---|---|
| RQ1 | `MINOR` | localized descriptive drift plus an age-association nominal significance flip |
| RQ2 | `MINOR` | RQ2a/RQ2b headline top-50 sets remain stable; RQ2c community and brokerage outputs change |
| RQ3 | `NONE` | numeric feature/effect tables drift, but uncorrected and FDR significance decisions do not change |

RQ1 requires a focused interpretation review because the corrected p-value for
the age association crosses the nominal threshold. RQ2c requires corrected
structural tables and review of any prose naming communities or brokerage
candidates. RQ3 does not require a change to the statistical conclusion, but
its numeric tables are stale relative to corrected P0.

## 7. Figure dependency impact

The existing supplemental decision record maps the four main figures as:

```text
Figure 1: evidence-universe flow and RQ1 composition
Figure 2: RQ2a source role and RQ2b target concentration
Figure 3: RQ2c structural summary and community robustness
Figure 4: RQ3 effect sizes and FDR results
```

No figure was rendered and no figure-ready artifact was modified. The existing
S6 figure-ready manifest points to frozen P0 inputs, so the following is a
dependency assessment only:

| figure | assessment | reason |
|---|---|---|
| Figure 1 | `DATA_UPDATE_REQUIRED` | RQ1 event/entity distributions and age-association data changed |
| Figure 2 | `DATA_UPDATE_REQUIRED` | source/target tables and concentration denominators changed, even though both top-50 sets are stable |
| Figure 3 | `INTERPRETATION_UPDATE_REQUIRED` | community count and brokerage top-50 membership changed |
| Figure 4 | `DATA_UPDATE_REQUIRED` | effect-size and p-value tables changed, while significance status remained stable |

These assessments do not authorize figure regeneration.

## 8. S1-S7 impact

| supplement | decision | reasoning |
|---|---|---|
| S1 | `RERUN_REQUIRED` | retained Reference record universe and source-admission counts changed by 120 records |
| S2 | `RERUN_REQUIRED` | directed edge weights and multiplicities changed, including a 59-to-2 edge reduction |
| S3 | `RERUN_REQUIRED` | corrected network views, node domain, and LCC edge set changed |
| S4 | `RERUN_REQUIRED` | corrected graph has 35 rather than 34 Louvain communities |
| S5 | `RERUN_REQUIRED` | brokerage candidate values and top-50 membership changed |
| S6 | `RERUN_REQUIRED` | figure-ready derivations point to frozen P0 source hashes and must be regenerated for corrected data |
| S7 | `NO_RERUN_REQUIRED` | fixed top source, target, and edge evidence sets have zero overlap with the 679889516 affected source, target, or edge IDs |

S7's decision is conditional on retaining its existing fixed-object definition.
If corrected P0 selection changes the fixed top-object sets, S7 must be
recomputed. No S1-S7 output was changed in this review.

## 9. Contamination and scope checks

The implementation branch remains
`ch5-refq-repository-identity-correction-v1`. The historical frozen output,
historical v1 config, historical tag, supplemental outputs, figures, and
manuscript were not modified. No C4 work was started. The only new file from
this task is this report; the pre-existing provenance reconstruction report
remains separate and unchanged.

## 10. Final decision

The correction is source-localized and mostly produces small or low-rank
numeric drift, but it changes one RQ1 nominal significance result, RQ2c
community/brokerage outputs, all corrected S1-S6 dependencies, and the data
required by the main figure derivations. Existing frozen S1-S6 results cannot
be treated as corrected-baseline evidence.

```text
C3_IMPACT_REQUIRES_EXPERIMENT_RERUN
```

No C4 action, figure update, or manuscript update is authorized by this review.

## Source records

- `outputs/reference_quotient_p0_frozen/manifest.json`
- `outputs/reference_quotient_p0_corrected_v2/manifest.json`
- `outputs/reference_quotient_p0_frozen/quotient_construction_audit.json`
- `outputs/reference_quotient_p0_corrected_v2/quotient_construction_audit.json`
- `outputs/reference_quotient_p0_frozen/membership_audit.json`
- `outputs/reference_quotient_p0_corrected_v2/membership_audit.json`
- `docs/freeze/ch5_refq_repository_identity_correction_c2_relation_diff_v1.csv`
- `docs/freeze/ch5_refq_repository_identity_correction_c2_aggregate_diff_v1.csv`
- `docs/ch5_refq_final_supplemental_human_decision_summary_v2.md`
- `supplemental/reference_quotient_v1/v1_1_completion/outputs/S6_figure_ready/figure_ready_manifest_v1_1.json`
- `supplemental/reference_quotient_v1/outputs/S7_top_evidence_composition/`
