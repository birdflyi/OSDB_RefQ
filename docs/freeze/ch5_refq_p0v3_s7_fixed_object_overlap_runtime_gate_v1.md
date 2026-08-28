# Chapter 5 RefQ S7 Fixed-Object G09 Overlap Runtime Gate v1

## Decision

`S7_STATUS = KEPT_FIXED_OBJECT`

`G09 = PASS`
`S7_SCIENTIFIC_RUN = 0`

The accepted corrected P0-v3 baseline has no overlap between the historical
S7 fixed objects and the accepted correction-impact sets. Historical S7 files
were read-only and remained byte-identical.

## Fixed-object provenance

The fixed sets were derived only from immutable historical authorities; no
corrected P0 top-N reselection was performed.

- Fixed source objects: the 50 rows in
  `outputs/reference_quotient_p0_frozen/rq2a_source_role_top50.csv`, selected
  by the historical out-strength descending operator (with the historical
  deterministic tie-break), and cross-checked against the unique
  `source_project_id` values in
  `supplemental/reference_quotient_v1/outputs/S7_top_evidence_composition/top_source_evidence_composition.csv`.
- Fixed target objects: the 50 rows in
  `outputs/reference_quotient_p0_frozen/rq2b_target_role_top50.csv`, selected
  by the historical in-strength descending operator (with the historical
  deterministic tie-break), and cross-checked against the unique
  `target_project_id` values in
  `supplemental/reference_quotient_v1/outputs/S7_top_evidence_composition/top_target_evidence_composition.csv`.
- Fixed directed edge objects: the historical
  `outputs/reference_quotient_p0_frozen/reference_quotient_cross_project_edges.csv`
  sorted by `weight DESC, source_project_id ASC, target_project_id ASC`,
  taking the first 100 cross-project pairs. The resulting pairs were
  cross-checked against the 100 unique `directed_edge` values in
  `top_edge_evidence_composition.csv`.

The cross-check closed exactly: 50/50 source objects, 50/50 target objects,
and 100/100 directed edge objects. The complete membership is recorded one
row per object in `ch5_refq_p0v3_s7_fixed_object_overlap_sets_v1.csv`; source
and target IDs and all affected IDs/pairs are numerically sorted, while fixed
edge rows retain the historical weight/tie-break selection order.

## Affected-object provenance

Affected sets were derived from accepted correction evidence and the
historical-vs-official-corrected P0 directed edge difference, not from a new
ranking. The comparison was between
`outputs/reference_quotient_p0_frozen/reference_quotient_edges.csv` and
`outputs/reference_quotient_p0_corrected_v3/reference_quotient_edges.csv`.
Only numeric project IDs are used; repository names are deliberately excluded.

The accepted correction changes ten directed pairs (removed) and reduces one
pair's weight/multiplicity from 59 to 2. All affected pairs have source
`679889516`; no self-loop changed. Therefore:

- affected source set (1): `{679889516}`;
- affected target set (11):
  `{33999965, 238372891, 240147659, 315520343, 322195640, 593957637,
  600271677, 607441698, 623716378, 647017093, 654343821}`;
- affected edge set (11 cross-project pairs):
  `{679889516->33999965, 679889516->238372891,
  679889516->240147659, 679889516->315520343,
  679889516->322195640, 679889516->593957637,
  679889516->600271677, 679889516->607441698,
  679889516->623716378, 679889516->647017093,
  679889516->654343821}`.

Self-loop consequences were included when deriving source and target sets; the
edge comparison for G09 is restricted to directed cross-project pairs. The
full exact fixed and affected sets, sorted numerically, are encoded in the
companion CSV with `membership_role` values `FIXED` and `AFFECTED`. No
`OVERLAP` row exists because every intersection is empty.

## Numeric-ID overlap calculation

The frozen operator is exact set intersection (no approximate matching, no
repository-name matching, and no ranking comparison substitution):

| set class | fixed size | affected size | intersection size | intersection |
|---|---:|---:|---:|---|
| source project | 50 | 1 | 0 | `{}` |
| target project | 50 | 11 | 0 | `{}` |
| directed cross-project edge | 100 | 11 | 0 | `{}` |

Because all three intersections are zero, the KEEP disposition is valid for
the historical fixed-object definition. This does not claim that corrected
P0 top-50/top-100 rankings are identical and does not authorize reselection.

## S7 side-effect and immutability gate

This review performed no S7 writes, no S7 reselection from corrected P0, and no
raw scientific S7 rerun:

```text
S7_WRITES = 0
S7_RESELECTION = 0
S7_SCIENTIFIC_RUN = 0
```

Before/after SHA-256 values for every frozen historical S7 artifact are equal:

| artifact | bytes | before SHA-256 | after SHA-256 | result |
|---|---:|---|---|---|
| `supplemental/reference_quotient_v1/outputs/S7_top_evidence_composition/top_edge_evidence_composition.csv` | 66775 | `70e13c9d2a50ce97cedf58791e1eebddbc09073bd55cad938ef2814a1c258d00` | `70e13c9d2a50ce97cedf58791e1eebddbc09073bd55cad938ef2814a1c258d00` | PASS |
| `supplemental/reference_quotient_v1/outputs/S7_top_evidence_composition/top_source_evidence_composition.csv` | 45342 | `345786fc4058406c605f2fdee5d97ebc38fa04014643e0b234e9d25d3fb60b2c` | `345786fc4058406c605f2fdee5d97ebc38fa04014643e0b234e9d25d3fb60b2c` | PASS |
| `supplemental/reference_quotient_v1/outputs/S7_top_evidence_composition/top_target_evidence_composition.csv` | 37694 | `0f925153fa44f0a56161c50346a34adca2bfec3f75f9c8e32f7f1675d45e378a` | `0f925153fa44f0a56161c50346a34adca2bfec3f75f9c8e32f7f1675d45e378a` | PASS |
| `supplemental/reference_quotient_v1/v1_1_completion/outputs/S7_top_evidence_composition/top_source_target_entity_composition.csv` | 40111 | `c454251e274b0fa19710628a00fc42aaf9fbfa3cfac4c4a162282da9ea5a0792` | `c454251e274b0fa19710628a00fc42aaf9fbfa3cfac4c4a162282da9ea5a0792` | PASS |

The historical provenance baseline identifies tag
`chapter5-refq-freeze-v1.0` at commit
`68d001551359d120bf2a06cc5e571742df7e7822`; the tag and all listed artifacts
remain unchanged.

## Boundary and disposition

S7 remains outside the S1-S6 DAG. The result means only that the historical
fixed-object composition remains valid for the corrected baseline because none
of its fixed source, target, or directed-edge objects intersects the accepted
correction impact set. No scientific S7 result was regenerated. G20 remains
`NOT_FINALIZED`; figures, manuscript edits, merge, and final tagging remain
unauthorized.
