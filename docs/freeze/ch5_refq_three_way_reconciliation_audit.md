# Chapter 5 RefQ — Final Conservative Three-Way Reconciliation Audit

## Final decision

`CH5_REFQ_THREE_WAY_RECONCILIATION_PASS`

The authoritative manuscript, frozen scientific outputs, and accepted V6
publication figures express the same scientific object. All checked quantities,
denominators, units, graph views, observation boundaries, statistical status,
and interpretation limits close. No manuscript edit was required in this
audit. A non-blocking publication-composition TODO is recorded because the
external manuscript source does not embed final figure captions.

## 1. Purpose and scope

This is a read-and-compare audit across three layers:

1. the authoritative external manuscript;
2. frozen corrected P0-v3 and supplemental v2 scientific authorities; and
3. accepted V6 publication figures, manifests, tables, and acceptance records.

No scientific pipeline, statistic recomputation, figure rerender, second-order
projection, or broad stylistic rewrite was performed. Arithmetic checks below
are verification of already frozen values only.

## 2. Starting identity

```text
repository = D:/github_repo/OSDB_RefQ
branch = ch5-refq-repository-identity-correction-v1
repository_HEAD_before = 45aad05a0d2df746fe56e1547b4910ee5fc217fc
remote_HEAD_before = 45aad05a0d2df746fe56e1547b4910ee5fc217fc
working_tree_before = four pre-existing untracked V3/V4/V5/V6 ZIP archives only
```

Authoritative manuscript:

`C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md`

```text
authoritative_manuscript_SHA_before = 13C36E377AA4EA329CF96825F09D93466925D86FCEC15636D53E7ABDBE080309
authoritative_manuscript_SHA_after  = 13C36E377AA4EA329CF96825F09D93466925D86FCEC15636D53E7ABDBE080309
manuscript_files_changed = 0
```

The three bounded Figure 2 wording edits from the preceding closure audit are
already present and were not reverted. Historical manuscript snapshots remain
untouched.

## 3. Three-way authority definition

### Manuscript authority (A)

The external reconciled/composition manuscript above is the sole current prose
authority. Its tables 4.1–4.8, abstract, methods, results, discussion,
conclusion, and Appendix A were inspected.

### Scientific authority (B)

Only the corrected roots were used:

- `outputs/reference_quotient_p0_corrected_v3/`
- `supplemental/reference_quotient_v2/outputs_p0v3/`

Key authority manifests are P0-v3 manifest SHA
`be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776` and final
supplemental package manifest SHA
`78d07fbda2a045ba309a1cfcb23a68ca2baafa910008b6483c0c4e0acf9211bd`.

### Publication authority (C)

The accepted root is `figures/ch5_refq/p0v3_final_v6/`, with final acceptance
record `docs/freeze/ch5_refq_p0v3_figure_rendering_final_acceptance.md` and
decision `P0V3_FIGURE_RENDER_FINAL_ACCEPTED`. The V6 render-stage manifest
retains an intermediate `READY_FOR_FINAL_HUMAN_VISUAL_QA` status; the explicit
acceptance record supersedes that stage status and is the final publication
decision. V3–V6 assets and their provenance remain immutable.

## 4. Files inspected

- authoritative manuscript and its prior OLD/QA snapshots (read-only);
- P0-v3 `rq1_project_reference_profiles.csv`, `rq1_descriptive_statistics.csv`,
  entity distributions, project-age association, membership and quotient audits;
- P0-v3 RQ2a source-role, RQ2b target-role/concentration, and RQ2c structural
  summary/brokerage outputs;
- P0-v3 RQ3 descriptive and Kruskal/FDR outputs;
- supplemental v2 S1 evidence-universe flow and S6 figure-ready tables;
- supplemental v2 S3/S4/S5 stability outputs;
- V6 render manifest, Figure 1–4 source manifests, accepted V6 figures, V6
  caption draft, and V6 acceptance/review records;
- prior Figure 2 manuscript-text closure audit.

## 5. Internal issue table

| ID | location | authority A (manuscript) | authority B (frozen science) | authority C (publication) | issue | severity | action |
|---|---|---|---|---|---|---|---|
| I-01 | Abstract / RQ1 | discussion/external-reference summary | admitted universe and entity distributions | Figure 1 and tables 4.1–4.2 | `NO_CHANGE_REQUIRED` | INFO | closed |
| I-02 | Tables 4.1–4.2 | counts, percentages, Other rows | S6 entity-distribution CSVs | Figure 1 source manifest | `NO_CHANGE_REQUIRED` | INFO | closed |
| I-03 | Tables 4.3–4.5 | means, medians, SD, skewness/kurtosis | P0 descriptive statistics | RQ1 publication outputs | `NO_CHANGE_REQUIRED` | INFO | retain descriptive right-skew wording |
| I-04 | Table 4.6a | n=291 and rounded rho/p pairs | project-age authority | RQ1 publication context | `NO_CHANGE_REQUIRED` | INFO | closed |
| I-05 | RQ2a | source quantiles, relation partition, top-source examples | S6/P0 source-role outputs | Figure 2A/B | `NO_CHANGE_REQUIRED` | INFO | closed |
| I-06 | RQ2b / Table 4.6d | target counts, medians/maxima, shares, denominator | S6 quantiles and concentration JSON | Figure 2 target panels | `NO_CHANGE_REQUIRED` | INFO | closed |
| I-07 | RQ2c / Tables 4.6e–f | directed/undirected/LCC units and structural limits | P0 RQ2c summary and S4/S5 | Figure 3 | `NO_CHANGE_REQUIRED` | INFO | closed |
| I-08 | RQ3 / Table 4.8 | descriptive-vs-FDR and label-mode language | P0 Kruskal/FDR outputs | Figure 4 | `NO_CHANGE_REQUIRED` | INFO | closed |
| I-09 | Sections 1.2, 3.4 | (Q=M^\top R_PM), membership and view limits | quotient construction audit | Figure 3/operator provenance | `NO_CHANGE_REQUIRED` | INFO | closed |
| I-10 | Cross-section summaries | abstract/results/discussion/conclusion | all frozen RQ authorities | figures and tables | `CROSS_SECTION_SUMMARY_DRIFT` checked | INFO | no drift found |
| I-11 | Terminology and units | source/target/seed/expanded and record/edge/weight terms | membership/quotient contracts | V6 source manifests | `NO_CHANGE_REQUIRED` | INFO | closed |
| I-12 | External manuscript caption composition | no embedded final Figure 1–4 captions | V6 caption draft is artifact-only | accepted V6 figures have immutable provenance | `CAPTION_AUTHORITY` | P2 | record `PUBLICATION_COMPOSITION_TODO`; do not fabricate caption |
| I-13 | V6 render-stage status | no manuscript claim | manifest says stage-ready | acceptance record says final accepted | `NO_CHANGE_REQUIRED` | INFO | acceptance record is final authority |

No P0 or P1 issue was found. The sole P2 item is publication composition, not
a scientific inconsistency.

## 6. Global denominator and unit audit

| quantity | manuscript role | frozen value | closure |
|---|---|---:|---|
| analysis seed projects | source-complete observation set | 294 | PASS |
| scanned input Reference records | pre-admission input records | 3,748,078 | PASS |
| admitted source-observation records | post-admission record universe | 3,747,958 | PASS |
| out-of-seed source records | admission exclusion branch | 120 | PASS |
| quotient-eligible records | project-mappable Reference-record/weight universe | 1,586,047 | PASS |
| RefQN node domain | all project nodes | 6,506 | PASS |
| edge-observed nodes | complete directed RefQN | 6,505 | PASS |
| zero-edge node | complete directed RefQN | 1 | PASS |
| directed edges including self-loops | EDGE_COUNT | 9,884 | PASS |
| self-loops | EDGE_COUNT subset | 289 | PASS |
| directed cross-project edges | EDGE_COUNT after self-loop exclusion | 9,595 | PASS |
| total directed weight including self-loops | aggregated Reference-record weight | 1,586,047 | PASS |
| cross-project weight | aggregated Reference-record weight | 138,974 | PASS |
| U(G_RefQ) edges | undirected EDGE_COUNT | 9,547 | PASS |
| U(G_RefQ) components / isolates | undirected node-view counts | 55 / 30 | PASS |
| LCC nodes / undirected edges | LCC node and EDGE_COUNT | 6,367 / 9,462 | PASS |
| LCC directed sensitivity edges | directed sensitivity EDGE_COUNT | 9,510 | PASS |

The manuscript does not call `1,586,047` edges, `9,595` records, or `138,974`
edges. It does not treat `6,322` observable targets as the 6,506-node RefQN
domain or imply that 6,506 nodes are source-complete. Percentages are displayed
as percentages; underlying coverage values remain fractions in the scientific
files.

## 7. RQ1 reconciliation

### Entity distributions

The admitted denominator is `3,747,958`. Table 4.1 matches the frozen counts and
two-decimal shares: IssueComment `1,816,696 / 48.47%`, Push `1,165,990 /
31.11%`, PullRequest `335,530 / 8.95%`, Issue `168,876 / 4.51%`, Release
`96,690 / 2.58%`, and display-only Other `164,176 / 4.38%`. Table 4.2 matches
GitHub_Service_External_Links `1,629,327 / 43.47%`, PullRequest `671,986 /
17.93%`, Actor `475,651 / 12.69%`, Issue `281,648 / 7.51%`, Commit `255,009 /
6.80%`, GitHub_Files_FileChanges `193,391 / 5.16%`, Repo `74,468 / 1.99%`, and
Other `166,478 / 4.44%`. Exact shares round to the displayed values under the
declared convention; component sums equal `3,747,958`.

### Self-reference

The manuscript reports mean `41.82%`, median `39.47%`, SD `23.89%`, Q1
`25.75%`, and Q3 `59.06%`, matching `rq1_descriptive_statistics.csv` and
`rq1_profile_quantiles.csv`. WiredTiger is `12,891 / 15,332 = 84.08%`; GreatSQL
and `ideawu/ssdb` are `0.00%`; H2 is `235 / 590 = 39.83%`. These examples are
descriptive profile positions, not quality or mechanism claims.

### Collaboration metrics and project age

Tables 4.3–4.5 match the frozen means, medians, standard deviations,
quartiles, maxima, skewness, and kurtosis. Their right-skew wording is
supported by explicitly reported skewness/kurtosis and is unrelated to the
Figure 2 quantile-only restriction. Project-age analysis uses `n=291` and the
rounded pairs `(-0.1182, 0.0440)`, `(0.1182, 0.0440)`, `(0.1574, 0.0072)`, and
`(0.1417, 0.0155)`, all marked cross-sectional 2023 with no longitudinal or
causal interpretation.

`RQ1 = PASS`.

## 8. RQ2a source-role reconciliation

The manuscript and frozen S6/P0 authority agree on 262 positive-out-degree seeds,
32 zero-out-degree seeds, out-degree Q1/median/Q3/max `3/11/39/352`, and
out-strength Q1/median/Q3/max `5/26.5/192.75/43,574`. Relation partitions close:

```text
418 + 9,177 = 9,595 directed cross-project edges
7,630 + 131,344 = 138,974 cross-project weight
```

The text defines out-degree as unique target-project count and out-strength as
aggregated cross-project Reference weight. It states that expanded targets are
non-seed memberships and are not source-complete. OpenSearch, qdrant, Hazelcast,
Velox, and CockroachDB values match `rq2a_source_role_metrics.csv`; no influence,
quality, knowledge-output, or complete-ecosystem ranking is asserted.

`RQ2a = PASS`.

## 9. RQ2b target-role reconciliation

The manuscript, Table 4.6d, Figure 2 V6 source manifest, and frozen outputs agree:

```text
observable targets = 6,322
seed-project targets = 110
expanded-project targets = 6,212
in-degree Q1/median/Q3/max = 1 / 1 / 1 / 42
in-strength Q1/median/Q3/max = 1 / 2 / 5 / 3,430
target coverage Q1/median/Q3/max = 0.34% / 0.34% / 0.34% / 14.29%
cross-project weight denominator = 138,974
Top-1 / Top-10 / Top-50 = 2.47% / 16.00% / 48.99%
```

`42/294 = 0.1428571428571428 = 14.29%`; the lower quartile, median, and upper
quartile coverage fraction is `0.0034013605442176 = 0.34%`. Exact concentration
shares are `0.024680875559457166`, `0.15998676011340252`, and
`0.4899261732410379`. The manuscript uses the permitted typical/max separation
and observed concentration interpretation only; it makes no power-law,
heavy-tail, scale-free, preferential-attachment, or causal claim.

`RQ2b = PASS`.

## 10. RQ2c undirected-view reconciliation

The manuscript consistently distinguishes:

```text
directed cross-project RefQ = 9,595 edges
U(G_RefQ) = 9,547 undirected edges
LCC = 6,367 nodes / 9,462 undirected edges
LCC directed sensitivity = 9,510 edges
```

It defines (U(G_{\mathrm{RefQ}})) as a first-order direction-ignored view and
explicitly excludes bibliographic coupling, shared-reference/shared-neighbor
projection, (QQ^\top), (Q^\top Q), and (X\Phi X^\top). Structural values
match the frozen summary: average clustering `0.04225758251235413`, transitivity
`0.008047960961122938`, 35 canonical Louvain communities, modularity
`0.7969220043681785`, community range `32–37`, 42/50 ARI below 0.9, minimum ARI
`0.6823671359861659`, and minimum pairwise ARI `0.6092441840471735`.

The five brokerage candidates and values match the frozen output. The manuscript
uses only bridge-like structural-position language and explicitly rejects
knowledge-broker, organizational-coordinator, causal-intermediary, and ecosystem
importance interpretations.

`RQ2c = PASS`.

## 11. RQ3 reconciliation

Table 4.8 and the frozen Kruskal/FDR output agree that no Reference-composition
feature is FDR-supported under both label modes. Under `include_mixed`, exactly
six role/local-structure/project-age features cross FDR (`out_degree`,
`out_strength`, `in_degree`, `in_strength`, `local_clustering`,
`project_age_years_at_2023_end`); under `exclude_mixed_or_multilabel`, none do.
Thus the cross-mode robust feature count is zero. Abstract, Results, Discussion,
RQ synthesis, and Conclusion all retain the required `label-mode sensitive`
interpretation and do not call the differences universal, robust, or taxonomic.

`RQ3 = PASS`.

## 12. RefQ operator and semantic reconciliation

The manuscript defines:

```text
Q = M^T R_P M
```

and consistently specifies unique semantic project membership, project-mappable
endpoint eligibility, directed unnormalized block-sum aggregation, preserved
self-loops in the general RefQ definition, optional self-loop removal only in
cross-project views, and seed-centered source observation. It distinguishes the
paper-defined first-order relation from (QQ^\top), (Q^\top Q), and
`K = X Phi X^T`, and states that the latter were not part of the experiment.

```text
FIRST_ORDER_REFQ = PASS
SECOND_ORDER_PROJECTION_EXECUTED = FALSE
UNDIRECTED_VIEW_IS_NOT_PROJECTION = PASS
```

## 13. Novelty and contribution reconciliation

Across Abstract, Introduction, Related Work, Discussion, and Conclusion, the
paper claims only formalization/reframing, semantic membership quotient and
construction contract, endpoint eligibility, observable-vs-eligible universe
separation, observation-aware role separation, a weaker-semantic evidence layer,
and DBMS instantiation. It explicitly disclaims invention of project-reference
aggregation, directed/count-weighted networks, graph quotient/coarsening, a new
generic graph algorithm, replacement of Reference Coupling, dependency ground
truth, task-resolution semantics, and causal knowledge flow.

`NOVELTY_CLOSURE = PASS`.

## 14. Terminology and citation-claim boundaries

RQ2a, RQ2b, and RQ2c are used as distinct roles; no legacy undifferentiated RQ2
claim was found. Seed/source/target/expanded terminology is consistent with the
observation contract. Reference Coupling, IREL, Loukas, Sánchez-García, Xiao,
and Kessler are used as prior-work or mathematical-boundary references rather
than as sources of stronger claims than the manuscript accepts. Bibliographic
coupling is correctly described as a second-order shared-cited-object relation.

`TERMINOLOGY_CLOSURE = PASS` and `CITATION_BOUNDARY_CLOSURE = PASS`.

## 15. Cross-section summary matrix

| finding | Abstract | Results | Discussion | Conclusion | status |
|---|---|---|---|---|---|
| RQ1 evidence composition | discussion/external resources | Tables 4.1–4.2 and RQ1 prose | bounded observable evidence | same bounded summary | PASS |
| RQ2a source range/strength | typical/max separation | quantiles and relation partition | same bounded contrast | source-role range/strength | PASS |
| RQ2b target concentration | target weight concentrated | medians/maxima and Top-k shares | same observed concentration | target coverage/concentration | PASS |
| RQ2c undirected structure | structural observation | first-order view and sensitivity | algorithmic modular neighborhood | same qualified view | PASS |
| RQ3 label-mode sensitivity | no cross-mode FDR support | Table 4.8 | local and label-mode sensitive | no robust cross-mode feature | PASS |
| methodological contribution | formalization/reframing | construction contract | weaker-semantic evidence layer | same scope | PASS |
| observation boundary | seed-centered observed RefQN | 294 source-complete seeds; expanded targets incomplete | not full ecosystem | same limitation | PASS |

No summary drift was found.

## 16. Figure/table publication closure

| publication object | scientific authority | publication authority | text linkage | closure |
|---|---|---|---|---|
| Figure 1 | S1 flow/entity distributions | V6 Figure 1 root and source manifest | RQ1, Tables 4.1–4.2 | PASS |
| Figure 2 | P0 RQ2b concentration + S6 RQ2a/RQ2b figure-ready tables | V6 Figure 2 root, linear Figure 2C acceptance | RQ2a/RQ2b, Tables 4.6b–d | PASS |
| Figure 3 | P0 RQ2c + S3/S4/S6 | V6 Figure 3 root | RQ2c, Tables 4.6e–f | PASS |
| Figure 4 | P0/S6 RQ3 descriptive and FDR tables | V6 Figure 4 root | RQ3, Tables 4.7–4.8 | PASS |
| Tables 4.1–4.8 | corrected P0/S6 authorities | manuscript tables | corresponding RQ sections | PASS |
| final captions in external manuscript | V6 caption draft exists as artifact | not embedded in manuscript | submission composition | `PUBLICATION_COMPOSITION_TODO` |

The V6 caption draft is explicitly a rendering artifact. Its historical
intermediate log-axis sentence is not promoted to manuscript authority and no
V3–V6 file was edited. Final caption insertion should be handled as a separate
submission-composition step using the accepted V6 semantics.

## 17. Exact manuscript edits in this audit

None.

```text
authoritative_manuscript_SHA_before = 13C36E377AA4EA329CF96825F09D93466925D86FCEC15636D53E7ABDBE080309
authoritative_manuscript_SHA_after  = 13C36E377AA4EA329CF96825F09D93466925D86FCEC15636D53E7ABDBE080309
```

The preceding Figure 2 closure edits remain accepted; this audit did not alter
them or any historical manuscript snapshot.

## 18. Guards and immutability

```text
NEW_SCIENTIFIC_VALUES = 0
CHANGED_SCIENTIFIC_VALUES = 0
SCIENTIFIC_RECOMPUTATION = 0
P0_RUN = 0
S1_RUN = 0
S2_RUN = 0
S3_RUN = 0
S4_RUN = 0
S5_RUN = 0
S6_RUN = 0
S7_RUN = 0
GH_CORE_RUN = 0
EVENT_REJOIN = 0
SECOND_ORDER_PROJECTION_RUN = 0
FIGURE_RERENDER = 0
figure_assets_changed = 0
scientific_assets_changed = 0
manuscript_files_changed = 0
```

The four pre-existing untracked ZIP archives were preserved. V3/V4/V5/V6
render roots, all manifests, supplemental outputs, corrected P0-v3 outputs,
historical receipts, and scientific code remain byte-identical.

## 19. Final counts and readiness

```text
P0_ISSUES = 0
P1_ISSUES = 0
P2_ISSUES = 1 (caption composition TODO only)
INFO_ITEMS = 12

NUMERIC_MISMATCH = 0
DENOMINATOR_MISMATCH = 0
UNIT_MISMATCH = 0
RECORD_EDGE_WEIGHT_CONFLATION = 0
NODE_UNIVERSE_MISMATCH = 0
SOURCE_TARGET_ROLE_MISMATCH = 0
GRAPH_VIEW_MISMATCH = 0
RQ_TERMINOLOGY = 0
STATISTICAL_STATUS_MISMATCH = 0
OVERCLAIM = 0
NOVELTY_OVERCLAIM = 0
OBSERVATION_BOUNDARY = 0
FIGURE_TABLE_MISMATCH = 0
CAPTION_AUTHORITY = 1 non-blocking TODO
CROSS_SECTION_SUMMARY_DRIFT = 0

RQ1 = PASS
RQ2a = PASS
RQ2b = PASS
RQ2c = PASS
RQ3 = PASS
reconciliation_readiness = READY
```

`PUBLICATION_COMPOSITION_TODO` is the only open item and does not block the
scientific three-way reconciliation.

