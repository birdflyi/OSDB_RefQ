# Chapter 5 RefQ S2 Reference-Weight Observational Semantics Audit

## Audit status

This is a read-only lineage and semantics audit. It does not rerun P0 or
S2, rescan frozen input rows, modify source code or data, modify any
supplemental output, commit, or push.

```text
repository = birdflyi/OSDB_RefQ
audited_branch = ch5-refq-supplemental-evidence-v1
audited_head = 3720b76e863261afd520113bf5ce5bfda46df4ea
canonical_parent = 920286e134ca459c8e155942eabc6798ceab8b65
runtime_GH_CoRE = 2.3.1
```

## Executive determination

```text
P0_REFERENCE_DEDUP_RULE = NONE
EVENT_SOURCE_TARGET_DEDUP_PRESENT = NO in the canonical P0/S2 path
IMPLEMENTATION_WEIGHT_UNIT = REFERENCE_RECORD_MULTIPLICITY
MATCH_OCCURRENCE_SEMANTICS = MATCH_OCCURRENCE_MULTIPLICITY after matcher-level filtering
SAME_EVENT_SAME_PAIR_CAN_CONTRIBUTE_MULTIPLE_UNITS = YES (possible and permitted by the code path)
W_GE_2_MEANS = at least two retained Reference-record occurrences aggregated for one directed project pair
BLINCOE_COMPARABILITY = PARTIALLY_COMPARABLE
P0_RECALC_REQUIRED = NO
S2_RECALC_REQUIRED = NO
WORDING_CORRECTION_REQUIRED = YES
```

The current P0/S2 implementation is internally consistent with a
record-level weight definition. The semantic limitation is that the weight
must not be described as a distinct-event count, an independent-match count,
or a count of semantically independent citations.

## 1. Data lineage

The inspected construction lineage is:

```text
GitHub event snapshot
  -> raw per-repository event CSVs
  -> GH_CoRE content preprocessing
  -> GH_CoRE Reference extraction
  -> fine-grained collaboration records
  -> source/target aggregate project identity enrichment
  -> frozen repos_GH_CoRE_ref_node_agg CSVs
  -> P0 Reference filtering and membership resolution
  -> ordered (source_project, target_project) record aggregation
  -> project-level RefQ edge table Q
```

The repository-side preparation code supports this interpretation:

* `script/build_dataset/collaboration_relation_extraction.py:50-60` calls
  GH_CoRE `dedup_content` before extraction. This is content preprocessing,
  not event-row or Reference-record deduplication.
* `script/build_dataset/collaboration_relation_extraction.py:106-118`
  processes each input event row, calls
  `get_obj_collaboration_tuples_from_record`, converts every returned tuple
  to a collaboration row, and appends it to the output CSV.
* `script/build_dataset/collaboration_relation_extraction.py:167-180`
  shows the preparation sequence: content preprocessing, reading the
  processed event files, then extracting `EventAction` and `Reference`.
* `reference_descriptive_analysis.py:5754-5769` shows the historical
  preparation path that filters `relation_type == "Reference"`, leaves
  `ref_dedup_by_event_id = False`, then applies `granu_agg` and
  `set_entity_type_fine_grained` to create the aggregate-node snapshot.
* The P0 configuration points directly to the frozen
  `repos_GH_CoRE_ref_node_agg` directory. P0 consumes those prepared rows;
  it does not regenerate the matcher output.

### Distinguishing the four kinds of duplicate handling

1. **Raw event-log duplication:** no active `(event_id, ...)` collapse was
   found in the canonical P0 consumer. The audit did not scan raw inputs.
2. **Body/content preprocessing:** GH_CoRE `dedup_content` adjusts redundant
   content fields for event types. It copies rows and changes selected
   fields; it does not call `drop_duplicates` or group events by `event_id`.
3. **Matcher occurrence generation:** regex matching returns lists of
   occurrences. Those occurrences are subsequently converted to individual
   collaboration tuples unless the matcher marks a fallback object as a
   duplicate match.
4. **Same-event source/target project deduplication:** no such operation is
   active in the canonical P0 or S2 path. The optional helper exists, but the
   canonical configuration and call path do not use it.

## 2. Canonical deduplication policy

`configs/ch5_reference_quotient_p0.yaml:8-14` declares:

```text
relation_type = Reference
reference_dedup_rule = none
edge_aggregation_rule = sum one unit per retained fine-grained Reference record by ordered source/target membership pair
```

`script/ch5_reference_quotient/config.py:66-79` validates that
`reference_dedup_rule` must equal `none`; an event/source/target rule is not
accepted by the frozen P0 configuration validator.

`script/ch5_reference_quotient/reference_filtering.py:32-46` contains an
optional `deduplicate_references` helper. Its `event_source_target` branch
would drop duplicates using `(event_id, source_repo, target_repo)`, but the
canonical pipeline does not import or call this helper. A repository-wide
call-site search found no P0 call to it.

The legacy preparation code also sets `ref_dedup_by_event_id = False`
(`reference_descriptive_analysis.py:5703-5704`); the conditional
event-level dedup block at lines 5757-5759 is therefore inactive in that
preparation route.

## 3. Actual P0 aggregation key

`script/ch5_reference_quotient/pipeline.py:140-158` reads the fine-grained
columns, retains rows whose `relation_type` is `Reference`, and increments
the retained-record audit count. `event_id` is read at line 143, but it is
not used as a filtering or aggregation key.

At `pipeline.py:164-200`, source and target aggregate identities are mapped
to unique project memberships and only quotient-eligible rows are retained.
At `pipeline.py:203-207`, the actual edge aggregation is:

```python
grouped = pd.DataFrame(
    {"source": source_project[eligible].astype(str),
     "target": target_project[eligible].astype(str)}
).value_counts()
for (source, target), count in grouped.items():
    self.edge_weights[(str(source), str(target))] += int(count)
```

Thus the aggregation key is exactly:

```text
(source_project, target_project)
```

with one unit for each eligible retained `Reference` row. `event_id` is not
part of this key. `script/ch5_reference_quotient/edge_table.py:26-31` gives
the same row-wise Counter semantics for the reusable quotient helper, and
`edge_table.py:41-53` serializes both `weight` and `multiplicity` from that
integer count.

The canonical `reference_quotient_cross_project_edges.csv` confirms the
output representation: `weight` and `multiplicity` are the same aggregated
record count. This is an output-schema observation only; no frozen raw input
was rescanned for this audit.

## 4. GH_CoRE matcher semantics

The inspected installed package is the locked GH_CoRE 2.3.1 source under:

```text
D:/github_repo/OSDB_RefQ/venv/lib/site-packages/GH_CoRE
```

The relevant behavior is:

* `working_flow/identify_reference.py:67-72` implements `strs_regex` with
  `re.findall`, returning all matches for each string.
* `identify_reference.py:87-115` stores the match list for each message
  column. It does not reduce the list to a Boolean.
* `identify_reference.py:118-183` groups regex results by event `id` only
  to union list-valued matches from the configured patterns and message
  columns. `df_sum_series_values.py:14-32` concatenates lists; it does not
  convert them to a set.
* `identify_reference.py:233-240` applies this extraction separately to
  each configured reference-pattern family.
* `model/Entity_recognition.py:25-35` merges the link lists from the
  message columns without a project-pair deduplication step.
* `model/Relation_extraction.py:122-165` iterates over every retained
  `link_text` and appends a collaboration tuple for that occurrence.
  `Relation_extraction.py:178-201` then emits one DataFrame row per tuple.
* `model/Relation_extraction.py:145-153` uses the cache for entity lookup,
  not for collapsing output tuples. `Entity_search.py:379-383` marks a
  fallback generic URL object as `duplicate_matching`; the extractor skips
  that specific fallback duplicate. This matcher-level suppression does not
  implement event/source/target project-pair deduplication.

Consequently, the safe implementation label is
`MATCH_OCCURRENCE_MULTIPLICITY after matcher-level filtering`: multiple
retained matcher occurrences can become multiple fine-grained Reference
records. The semantic label is deliberately weaker than “independent
semantic references.” The code does not establish semantic independence.

## 5. Same-event, same-project-pair question

### Determination

```text
SAME_EVENT_SAME_PAIR_CAN_CONTRIBUTE_MULTIPLE_UNITS = YES
```

This is a permitted possibility, not a claim that every event containing
several textual mentions produces that exact pair. The evidence is:

1. GH_CoRE generates one tuple per retained match occurrence.
2. P0 retains each eligible Reference row.
3. P0 aggregates only by `(source_project, target_project)`.
4. No `event_id` is included in the aggregation key and no canonical
   event/source/target dedup call exists.

Therefore, if two retained occurrences from one event resolve to the same
source and target projects, both contribute to the project-pair weight. A
future event-level diagnostic could collapse
`(event_id, source_project, target_project)`, but that would be a different
operationalization and would not become semantic ground truth merely by
using event IDs.

## 6. S2 threshold semantics

`supplemental/reference_quotient_v1/scripts/run_supplemental.py:306-321`
loads the frozen cross-project edge table and applies
`cross["weight"] >= threshold` before undirected collapse. It does not
reconstruct weights from events.

The precise interpretation is:

```text
w >= 2 = retain directed project pairs whose aggregated retained
         Reference-record multiplicity is at least two.
```

This does not mean that the pair was supported by two different events,
two independent matcher matches in a semantic sense, or two independent
citations. The S2 structural changes are valid sensitivity results for the
record-level weight definition.

### Wording safety table

| Candidate wording | Status | Reason |
|---|---|---|
| “at least two Reference records” | SAFE | Directly matches the frozen unit. |
| “at least two matches” | UNSAFE as an unqualified phrase | “Match” can be read as an independent semantic match; use “retained matcher occurrences” only when that detail is intended. |
| “at least two independent citation events” | UNSAFE | `event_id` is not the P0 aggregation unit. |
| “at least two semantically independent references” | UNSAFE | Semantic independence is not encoded or validated. |
| “repeatedly supported by multiple events” | UNSAFE | Multiple-event support was not computed by S2. |
| “higher record-level evidence multiplicity” | SAFE | Correctly states the observational level. |

Recommended main terms are `Reference-record multiplicity`,
`record-level aggregated Reference weight`, and `record-multiplicity
threshold`.

Recommended S2 interpretation:

> After retaining only cross-project RefQ relations with record-level
> Reference weight at least two, network coverage and connectivity contract
> relative to the threshold-one view; this sensitivity concerns retained
> Reference-record multiplicity and does not establish multi-event or
> semantically independent support.

## 7. Blincoe comparability

The local prior-work decision material
`assets/related_work_comparison/ch5_refq_literature_comparison_decision_preparation_v1.0.md:100-101`
records Blincoe et al. as using a pair cross-reference count and a
`count >= 2` network filter, with a comment-centered Issue/PR/Commit
observation scope.

The numerical threshold and broad idea of filtering low-count directed
project pairs are therefore comparable. The observation units are not
identical enough to call the thresholds equivalent: the current P0 count is
the multiplicity of retained GH_CoRE Reference records over a broader
event/entity/resource evidence universe, with the matcher and membership
contract documented above. The correct classification is:

```text
BLINCOE_COMPARABILITY = PARTIALLY_COMPARABLE
```

The manuscript may say that both analyses use a threshold of two on a
project-pair count only with an explicit observation-unit qualifier. It
should not imply that the two thresholds measure the same event frequency or
semantic dependency strength.

## 8. Recalculation decision

```text
CURRENT_P0_RECALC_REQUIRED = NO
CURRENT_S2_RECALC_REQUIRED = NO
WORDING_CORRECTION_REQUIRED = YES
```

No code or result discrepancy was found. The P0 output and S2 threshold
operation are consistent with the frozen record-level definition. A rerun
would not resolve the semantic distinction between records, occurrences,
events, and independent semantic references. The needed action is to use
record-level wording and retain the boundary statement.

## 9. Optional future diagnostics (not executed)

If a reviewer later requests an event-level sensitivity, it can be defined
as a separate, explicitly labeled operationalization using
`(event_id, source_project, target_project)` before aggregation. It should
be described as an event-level lower-granularity diagnostic, not as a
semantic ground-truth weight.

A second diagnostic could report the share of current cross-project records
where the same event and project pair has multiplicity greater than one,
and the share of current `w >= 2` edges whose distinct-event support is one.
Neither diagnostic was run in this audit.

## 10. Audit controls

```text
raw_scan_count = 0
experiments_rerun = 0
P0_rerun = 0
S2_rerun = 0
source_or_output_modifications = 0
```

The existing supplemental S2 files were read only for schema and reported
threshold semantics. They were not regenerated or edited. The existing
supplemental execution report's prior raw scan belongs to that earlier
package run and is not part of this audit.

## Final decision

```text
S2_WEIGHT_SEMANTICS_AUDIT = PASS_READY_FOR_HUMAN_REVIEW
```
