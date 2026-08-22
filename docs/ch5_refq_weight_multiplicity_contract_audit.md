# Chapter 5 RefQ Weight / Multiplicity Field Contract Audit

## Audit status

```text
WEIGHT_MULTIPLICITY_CONTRACT_AUDIT = PASS_READY_FOR_HUMAN_REVIEW
audited_branch = ch5-refq-supplemental-evidence-v1
audited_head = 82e992aadd6c8e63ca699d766148d11f35ef7d0a
canonical_parent = 920286e134ca459c8e155942eabc6798ceab8b65
raw_scan_count = 0
experiments_rerun = 0
commit = NONE
push = NONE
```

This is a strictly read-only code, schema, call-site, and existing-output
contract audit. No raw input rows were scanned, no P0 or supplemental result
was recalculated, and no existing file was modified.

## Executive determination

```text
P0_WEIGHT_SEMANTICS = aggregated retained eligible Reference-record count
P0_MULTIPLICITY_SEMANTICS = the same record count, exposed on the canonical directed edge row
P0_WEIGHT_MULTIPLICITY_EQUALITY = PROVEN_BY_CONSTRUCTION
UNDIRECTED_WEIGHT_SEMANTICS = sum of analytical directed edge weights over the unordered pair
UNDIRECTED_DIRECTED_EDGE_COUNT_SEMANTICS = number of directed edge-table rows contributing to the unordered pair
MULTIPLICITY_NAME_OVERLOADING = PARTIAL
CURRENT_RESULT_INTERPRETATION_ERROR = NO
P0_RECALC_REQUIRED = NO
SUPPLEMENTAL_RECALC_REQUIRED = NO
CODE_BEHAVIOR = PARTIALLY_AMBIGUOUS
DOCUMENTATION = PARTIALLY_AMBIGUOUS
VALIDATION_CONTRACT = PARTIAL
FREEZE_DECISION = KEEP_FREEZE_DOC_PATCH_BEFORE_PUSH
```

The last decision is a documentation/API clarity recommendation, not a
scientific blocker. The existing freeze can remain scientifically valid. The
recommended pre-push patch should make the field contract explicit and remove
the stale `EDGE` unit label from the S1 evidence-weight presentation; it does
not require a P0 or supplemental recomputation.

## A. Fine-grained and multigraph levels

### A.1 Fine-grained Reference evidence

The canonical P0 configuration declares:

```text
reference_dedup_rule = none
edge_aggregation_rule = sum one unit per retained fine-grained Reference record by ordered source/target membership pair
```

In `script/ch5_reference_quotient/pipeline.py:153-158`, rows are filtered to
the configured `Reference` relation and retained rows are counted. At
`pipeline.py:196-207`, quotient-eligible rows are grouped by ordered
`(source_project, target_project)` and each group count is added to the
pipeline `Counter`.

Accordingly, before project-pair aggregation:

```text
one retained eligible Reference record = one contribution unit
```

At this stage, `multiplicity` is naturally the number of underlying retained
record instances represented by an aggregate edge. `weight` is not a separate
fine-grained field in the canonical input contract. It is assigned when the
project-level edge table is materialized.

### A.2 Generic graph-library level

The shared graph builder supports separate `weight` and `multiplicity`
attributes. In `build_Graph.py:358-398`, `MDG2DG` independently supplies
defaults and sums `weight` and `multiplicity` while collapsing parallel
directed edges. In `build_Graph.py:401-436`, `DG2G` independently sums both
attributes while collapsing reciprocal directed edges. Self-loop doubling,
when enabled, also doubles the two attributes independently at
`build_Graph.py:428-433`.

This means the lower-level graph API does not require:

```text
weight == multiplicity
```

The equality is therefore not a theorem-level invariant or a generic graph
API invariant. It is the current RefQ P0 operationalization.

`Graph_edge_filter` at `build_Graph.py:297-307` filters by `weight` only. It
does not filter or validate `multiplicity`.

## B. Canonical directed RefQ edge tables

The two canonical files have the schema:

```text
source_project_id,target_project_id,weight,multiplicity,is_self_loop,source_is_seed,target_is_seed
```

This schema is present in both:

```text
outputs/reference_quotient_p0_frozen/reference_quotient_edges.csv
outputs/reference_quotient_p0_frozen/reference_quotient_cross_project_edges.csv
```

### B.1 Construction path

The production pipeline accumulates record counts in
`pipeline.py:203-207`, then calls `edge_frame` at `pipeline.py:251-255`.
`edge_table.py:41-54` emits each row as:

```python
"weight": int(weight),
"multiplicity": int(weight),
```

The `edge_frame` input is the project-pair counter, so both fields equal the
number of retained eligible Reference records for that ordered project pair.
The cross-project table is a row filter of the same frame and does not change
either field.

The compatibility helper `build_direct_edge_table` uses the shared builder at
`edge_table.py:81-94`. Each input source-target row receives the builder's
default unit weight and the shared graph aggregation sums those units. It then
also passes the resulting counter through `edge_frame`, so this helper has the
same equality behavior for its own row-instance operationalization. It does
not consume a pre-existing input `multiplicity` column because only the source
and target columns are passed to `build_Graph`.

### B.2 Exact semantic answer

For canonical directed RefQ rows:

```text
weight = analytical edge weight used by current RefQ analyses
        = aggregated retained eligible Reference-record count

multiplicity = number of retained eligible Reference-record instances
               represented by that ordered project pair

weight == multiplicity = YES in current P0
```

This equality is proven by the construction path, not merely expected from
the documentation. It is not required by `Q = M^T R_P M`; the formalization
determines relation construction, while the choice to use unit record counts
as analytical weights is the current operationalization.

The helper `result_validation.py:10-32` requires both columns and checks that
each is positive, but it does not assert equality, integer type, or equality
to an independent retained-record count. A repository call-site search found
the validation helper definition but no production P0 call that applies it.
Thus equality is strong in the canonical builder and weak as a separately
declared validation assertion.

## C. Derived undirected view

### C.1 `directed_to_undirected_edges`

`network_views.py:17-36` selects only source, target, and the configured
`weight_col`. It groups by ordered pair and computes:

```text
weight = sum(input weight_col)
directed_edge_count = size of the grouped input rows
```

It does not select, read, or propagate an input `multiplicity` column.

For each grouped directed row, it creates a local `nx.DiGraph` with:

```text
weight = grouped analytical weight
multiplicity = grouped row count
```

at `network_views.py:37-44`. It then calls `DG2G` with
`multiplicity=True` and `double_self_loop=False` at lines 46-47. The output
renames the converted graph's temporary `multiplicity` attribute to
`directed_edge_count` at lines 49-57.

Therefore, the output is externally clear enough when interpreted by its
actual name:

```text
undirected weight = sum of directed analytical weights
directed_edge_count = number of directed edge-table rows, usually one per
                       ordered project pair in the canonical table
```

The temporary reuse of the generic graph attribute `multiplicity` is
internally ambiguous because it no longer means evidence multiplicity. It is
structurally safe for the current output because the value is immediately
renamed to `directed_edge_count`, and because the output contract does not
claim that this field counts Reference records. It would not be safe to treat
that temporary graph attribute as propagated evidence multiplicity.

### C.2 Canonical current interpretation

The canonical directed table has one row per ordered project pair. Therefore,
in the normal P0 path, a reciprocal pair contributes two to an undirected
`directed_edge_count`, while one directional project pair contributes one.
The value is not the pair's Reference-record weight. In particular, a
directed pair with `weight = multiplicity = 37` contributes one directed row,
not 37, to this structural count.

The same behavior is used by the supplemental `common.py:117-131` helper and
by S2/S3. The corrected S3 patch calls the RefQ `directed_to_undirected_edges`
implementation at `patch_s3.py:109-117`.

## D. Call-site matrix

| module/function | reads weight | writes weight | reads multiplicity | writes multiplicity | semantic role |
|---|---:|---:|---:|---:|---|
| `pipeline.RefQPipeline._scan_evidence` | no | counter contribution | no | no | counts retained eligible Reference records by ordered project pair |
| `edge_table.edge_frame` | counter value | yes | no | yes | materializes current P0 `weight == multiplicity` |
| `pipeline._write_quotient_outputs` | via `edge_frame` | CSV | no | CSV | writes canonical directed and cross-project tables |
| `edge_table.build_direct_edge_table` | shared-builder edge weight | counter/frame | no input field | frame | compatibility aggregation of input row instances |
| `build_Graph._build_MDG_edges` | edge attribute/default | edge attribute/default | arbitrary edge attribute | arbitrary edge attribute | creates multigraph edges and defaults |
| `build_Graph.MDG2DG` | yes, summed | yes | yes, summed when enabled | yes, summed when enabled | directed parallel-edge contraction |
| `build_Graph.DG2G` | yes, summed | yes | yes, summed when enabled | yes, summed when enabled | reciprocal directed-edge contraction |
| `build_Graph.Graph_edge_filter` | yes | removes by weight | no | no | weight threshold filter |
| `rq2a_source_view.summarize_source_view` | yes, sum | summary `out_strength` | no | no | source out-strength and degree |
| `rq2b_target_view.summarize_target_view` | yes, sum | summary `in_strength` | no | no | target in-strength and degree |
| `pipeline._write_role_outputs` | yes, sum/share | role metrics | no | no | RQ2a/RQ2b role summaries |
| `network_views.directed_to_undirected_edges` | yes, sum | undirected `weight` | no input read | temporary graph attribute only | first-order directed-to-undirected conversion |
| `network_views.analyze_undirected_view` | yes | node strength/summary through graph | no | no | Louvain weight, modularity weight, weighted strength |
| `network_views.analyze_undirected_view` brokerage | no (`weight=None`) | brokerage values | no | no | unweighted approximate betweenness |
| `supplemental.run_s2` | yes, threshold/sum | S2 summaries | no | no | thresholds are applied to directed `weight` |
| `supplemental.run_s3` / corrected `patch_s3` | yes, sum | S3 summaries | no | no | observation views and directed-weight summaries |
| `supplemental.common.undirected_edges_from_directed` | yes, sum | undirected `weight` | no | no | duplicate implementation of row-count conversion |
| `result_validation.validate_edge_table` | positivity only | no | positivity only | no | partial schema/positivity validation |
| `tests.test_network_views` | test inputs/expected outputs | expected output fields | only monkeypatch keyword | expected directed count | verifies row-count conversion, not evidence propagation |
| `tests.test_reference_pipeline` | test inputs/expected weights | expected weights | no | no | verifies aggregation weight, not equality field |
| `supplemental/tests/test_supplemental` | existing S2 weights | expected summaries | no | no | verifies arithmetic and canonical structural recovery |

## E. Current P0 invariant

The current P0 satisfies, by construction, for every canonical directed row:

```text
weight == multiplicity
                     == aggregated retained eligible Reference-record count
```

The evidence is the single counter path in `pipeline.py:203-207` followed by
the two assignments in `edge_table.py:41-50`. The canonical output schema and
existing immutability/hash records preserve this schema; this audit did not
rescan the 296 inputs or recompute any output.

```text
P0_WEIGHT_MULTIPLICITY_EQUALITY = PROVEN_BY_CONSTRUCTION
```

The qualification is important: it means proven for the current P0 producer,
not enforced as a generic invariant by every RefQ helper or by the shared
graph library.

## F. Future transformed-weight scenarios

### F.1 `multiplicity = 37`, `weight = 1`

The lower-level `MDG2DG` and `DG2G` APIs can carry these values separately.
The current canonical `edge_frame` cannot generate the pair because it writes
both fields from one counter. A manually supplied/directly transformed edge
table would behave as follows:

| consumer | behavior |
|---|---|
| S2 | thresholds `cross["weight"] >= threshold`; it ignores multiplicity, so a record-multiplicity threshold would no longer mean what the current S2 documentation says |
| RQ2a/RQ2b | strength sums weight and ignores multiplicity; this is conceptually correct for analytical weights, subject to current integer casts in the pipeline |
| directed-to-undirected conversion | sums weight but ignores input multiplicity; `directed_edge_count` reports rows, not 37 |
| Louvain/modularity | consumes weight and can use 1 as the analytical edge weight |
| brokerage | current implementation is unweighted (`weight=None`) and therefore ignores both fields |
| validation | positivity passes; equality and integer/field-role checks do not exist |

Thus the code is technically able to carry different values in the shared
graph layer, but the current RefQ/S2 semantics are not automatically preserved
if the values are transformed.

### F.2 `multiplicity = 37`, `weight = log1p(37)`

The graph and NetworkX paths can carry a floating-point analytical weight.
However, the end-to-end RefQ pipeline has integer-oriented assumptions:

* `pipeline._write_role_outputs` casts source strengths and weight totals to
  `int` at lines 288-292 and 336-363;
* the supplemental S1/S2/S3 summary writers similarly cast directed weight
  totals to `int` at `run_supplemental.py:317` and `340`;
* S2 thresholds would operate on the transformed weight rather than on
  Reference-record multiplicity;
* undirected conversion retains the transformed weight but does not retain
  the input evidence multiplicity field;
* `result_validation` accepts positive values without checking numerical type
  or the intended field relationship.

So this scenario is technically supported by selected graph operations, but
not a safe drop-in change to the current analysis contract. It requires an
explicit transformation mode, field semantics, threshold semantics, output
typing policy, and tests before use.

## G. Terminology contract

The proposed terminology is compatible with the audit:

```text
REFERENCE_RECORD_COUNT / EVIDENCE_MULTIPLICITY
    number of retained fine-grained Reference records represented by an
    aggregate directed project pair

WEIGHT
    numerical analytical edge weight consumed by graph algorithms

CURRENT_P0
    weight := evidence multiplicity

GRAPH_CONVERSION_MULTIPLICITY
    number of graph edge instances collapsed by MDG2DG or DG2G
```

The generic name `multiplicity` is overloaded between evidence multiplicity
and graph-conversion multiplicity in the current repository:

```text
MULTIPLICITY_NAME_OVERLOADING = PARTIAL
```

It is partial rather than a fully unsafe collision because the final RefQ
undirected output uses the explicit `directed_edge_count` name, and the
shared graph converter independently carries both attributes. It remains an
API ambiguity because `network_views.py` deliberately writes graph attribute
`multiplicity` from row count and does not propagate an input evidence
`multiplicity` column.

## H. Scientific interpretation audit

The current frozen scientific interpretation separates the quantities as
follows:

```text
139,044 = cross-project Reference-record weight/multiplicity
9,605   = cross-project directed edge count
9,557   = first-order undirected edge count
```

The current final human-decision summary explicitly distinguishes the
`139,044` record-level aggregated weight from the `9,605` directed edge count.
The RefQ S2 semantics audit also defines thresholds as record-level
multiplicity and does not interpret them as independent events or transformed
weights.

There is one stale non-numeric unit label in the immutable supplemental S1
artifact and its producer: `S1_evidence_universe/evidence_universe_flow.csv`
and `run_supplemental.py:264-265` label the two evidence-weight rows as
`EDGE`. Their values are the record-level aggregated weights, as confirmed by
the closure fields and the current code path. This is a documentation/schema
clarity defect, not a change in the scientific numbers or in the current
manuscript interpretation. The final freeze summary has already corrected its
own presentation, but the frozen artifact itself was intentionally not
rewritten in this read-only audit.

Therefore:

```text
CURRENT_RESULT_INTERPRETATION_ERROR = NO
P0_RECALC_REQUIRED = NO
SUPPLEMENTAL_RECALC_REQUIRED = NO
```

The stale unit label should be handled by a versioned docs/schema clarification
or an explicitly governed supplemental artifact patch. It should not be
silently changed as part of this audit.

## I. Contract-gap classification

### Code behavior: PARTIALLY_AMBIGUOUS

The canonical builder is precise and proves current P0 equality. The shared
graph converters independently support weight and multiplicity. Ambiguity
arises because the RefQ undirected adapter ignores input multiplicity and
reuses the generic graph attribute `multiplicity` for a structural row count
before renaming it.

### Documentation: PARTIALLY_AMBIGUOUS

The P0 configuration and the current freeze/S2 reports clearly describe
record-level weight semantics. The README says that Reference multiplicity and
edge weight are preserved but does not define the equality as a current
operational special case. The immutable S1 flow artifact and its producer
retain the stale `EDGE` unit label for evidence weights.

### Validation contract: PARTIAL

The direct edge validator requires both fields and positivity, and supplemental
tests cover S1 arithmetic, S2 threshold ordering, and canonical structural
recovery. There is no explicit assertion that `weight == multiplicity`, no
check that `directed_edge_count` is row-count rather than evidence-count, and
no transformed-weight mode test. The validator also does not appear to be
called by the production P0 pipeline.

## J. Recommended future docs/API contract patch

No patch is applied in this audit. For a future version:

1. Retain `weight` as the analytical edge-weight field.
2. Retain `multiplicity` only if it is explicitly documented as evidence
   multiplicity on the canonical directed RefQ table.
3. Prefer an immutable, unambiguous field such as
   `reference_record_count` or `evidence_multiplicity` for the canonical
   evidence count. If retained, assert `weight == evidence_multiplicity` in
   current P0 tests rather than making it universal for future transforms.
4. Keep `directed_edge_count` as the explicit output name for the number of
   directed rows collapsed into an undirected edge.
5. Make the undirected adapter either ignore evidence multiplicity explicitly
   by contract or propagate it under a separate name; do not pass it through
   the generic graph attribute `multiplicity` without renaming/documenting the
   intermediate meaning.
6. Define S2 thresholds against either analytical `weight` or evidence
   multiplicity, but do not preserve the current record-multiplicity wording
   after changing the threshold field.
7. Add tests covering both the current invariant and a transformed case:

```text
current P0: weight == evidence_multiplicity
future transformed mode: weight may differ from evidence_multiplicity
undirected conversion: directed_edge_count != evidence_multiplicity by definition
```

## Final fields

```text
WEIGHT_MULTIPLICITY_CONTRACT_AUDIT = PASS_READY_FOR_HUMAN_REVIEW
P0_WEIGHT_SEMANTICS = aggregated retained eligible Reference-record count
P0_MULTIPLICITY_SEMANTICS = aggregated retained eligible Reference-record count represented by the canonical directed edge
P0_WEIGHT_MULTIPLICITY_EQUALITY = PROVEN_BY_CONSTRUCTION
UNDIRECTED_WEIGHT_SEMANTICS = sum of directed analytical edge weights
UNDIRECTED_DIRECTED_EDGE_COUNT_SEMANTICS = count of directed edge-table rows collapsed into the unordered pair
MULTIPLICITY_NAME_OVERLOADING = PARTIAL
CURRENT_RESULT_INTERPRETATION_ERROR = NO
P0_RECALC_REQUIRED = NO
SUPPLEMENTAL_RECALC_REQUIRED = NO
CODE_BEHAVIOR = PARTIALLY_AMBIGUOUS
DOCUMENTATION = PARTIALLY_AMBIGUOUS
VALIDATION_CONTRACT = PARTIAL
FREEZE_DECISION = KEEP_FREEZE_DOC_PATCH_BEFORE_PUSH
raw_scan_count = 0
experiments_rerun = 0
commit = NONE
push = NONE
```
