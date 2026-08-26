# Chapter 5 RefQ C3 Execution Provenance Reconstruction Audit v1

Audit date: 2026-08-25

Decision: `C3_PROVENANCE_RECONSTRUCTED_WITH_LIMITATIONS`

Scope: reconstruct whether the existing corrected P0 bundle is equivalent to
the authorized C3 protocol execution. This audit is read-only with respect to
the corrected P0 output, historical freeze, data inputs, figures, supplements,
and manuscript. P0, C3, S1-S7, figure rendering, and manuscript updates were
not run.

## 1. Executive finding

The corrected P0 bundle is present, internally consistent, and linked to the
authorized candidate input chain. Its output files, config, candidate input
hashes, and historical P0 input hashes are reproducible from the current
files. The bundle manifest reports `PASS` and all five P0 validation fields
pass.

The execution boundary is not independently documented. There is no dedicated
C3 execution manifest, stdout/stderr capture, run log, authorization record,
or old/new scientific comparison record. The corrected output manifest is
therefore evidence that one valid-looking output bundle exists, but it cannot
prove that exactly one authorized C3 invocation occurred, that no external API
call occurred during that invocation, or that no transient rerun was later
overwritten. The candidate manifest is explicitly `CANDIDATE` and its zero-run
controls are declarations from the pre-C3 input-control phase, not an
independent execution trace.

The output manifest also records a legacy entry-point string ending in
`configs/ch5_reference_quotient_p0.yaml`, while its recorded config is the v2
config `configs/ch5_reference_quotient_p0_v2.yaml`. The pipeline source
hard-codes that legacy string when writing the manifest. This is a provenance
metadata defect, not evidence of output-file or input-hash corruption.

## 2. Corrected output inventory

Path: `outputs/reference_quotient_p0_corrected_v2`

The manifest exists and has SHA-256
`21699353d5dc9476547ee7f56881ba0a1ccc842a6d3c95adad9a28dedfd656d7`.

Manifest status is `PASS`; schema is
`reference_quotient_p0_frozen_manifest_v1`; 30 output files and 296 input
files are recorded. The recorded run window is
`2026-08-25T12:28:46.800444+00:00` through
`2026-08-25T12:34:45.278799+00:00`.

The v2 config SHA-256 is
`e19c0937e0d6f72fa84ad135b55a4056357d132d3a3df4ae5455bda7bc3de658`, and the
current `configs/ch5_reference_quotient_p0_v2.yaml` matches it exactly. The
manifest records implementation commit
`68054dceaebc14ecdf29ac9d0b209f28301fd7a4` on branch
`ch5-refq-repository-identity-correction-v1`, with a clean implementation
worktree at observation time.

Runtime metadata recorded in the manifest:

```text
Python 3.9.13
GH-CoRE 2.3.1
networkx 3.1
numpy 1.26.4
pandas 1.4.4
scipy 1.13.1
```

Manifest validation fields:

```text
membership_audit = PASS
quotient_construction_audit = PASS
rq_role_separation = PASS
seed_observability_audit = PASS
single_run_output_chain = PASS
```

All 30 non-manifest files exist with the recorded byte count and SHA-256:

```text
analysis_seed_manifest_294.csv|77126|dbf33e612c19976b406a3e5b19dfb781faf5e8a36afbbf13582dbe609ffa53e2
candidate_seed_observation_audit.csv|79836|e27f3a81e34cf5ac88a89858a85e03d989a5d64897aea8de1e5751788b712a44
membership_audit.json|1579|4455a6af6d022b3208db9198373a948b31a041e75a1ec85338898c9ca0b4259f
quotient_construction_audit.json|990|b54e21be796bb513b8108e2c4043290393503ead743eedacaef85f0b789ee6b0
reference_quotient_cross_project_edges.csv|392762|a73b410753d66ea5d2e7378bc496095e0617432f3463819050159417a3a101bd
reference_quotient_edges.csv|404998|65974328f6db459b7f4ae34d2afd9a93cc81ab2fe3411b635f493740bfbbd6a1
reference_quotient_node_registry.csv|293129|0e6095341d207ff3c096d759cdd86be172241668b5f8f0f68be460063397571a
refq_provenance_sample.csv|20417|860bfd2aa1670606302b0e4417f3c2a2d49e05df0c866bc90deafe75f6bf3877
rq1_descriptive_statistics.csv|1416|680911e7437a42c540a29dd3ae0b365b31f11668ee2bdf99ea6e1baee924c27a
rq1_event_type_distribution.csv|392|90d72fde449e5b193fabc1930c9ca1de6e6f10de2a89c1f3c0a741cf3d40edee
rq1_project_age_cross_sectional_association.csv|403|a6ce40b4005feb5b763513afba7ba4bd6d2455b5140d2f0c572db816939b2c8c
rq1_project_reference_profiles.csv|51757|da5a1ff86bbe95e9655060c8be51f0a57a0a621fac7425c94089aecadadd8813
rq1_referenced_entity_distribution.csv|819|483581ef070895ba4d222f6c285f6ffb35b84defc6252f0f026926ac7f0c5b04
rq1_referencing_entity_distribution.csv|364|c8730d77f637b95b0a7527b65030c87dcda4cf12da2e50f8fa2bdc7538a2c2fa
rq2a_source_role_metrics.csv|22467|895d67b236afacd936f16c593f8cd32457ad27770d53f24ff1593b15ce2c84bc
rq2a_source_role_top50.csv|4830|7bc346136fd591b2556d1bfc891048f2163b7a9aa8769bfab1f6cf878a175b78
rq2b_target_category_type_breakdown.csv|3078|c7cdc5f264e24d3619c17350d777b33f15a8e76c127f35cfcd4ce4f12dcb0ee0
rq2b_target_concentration.json|215|1deed3aa5492d92ac4ce2f0d93ee7aa5e6897be10ccf528cb9b0c1f81f58a9b6
rq2b_target_role_metrics.csv|703965|1348f0aadc8a53d9122f95de0000129a2ebafa7ada778df9d3f63a8def166e24
rq2b_target_role_top50.csv|5859|fe140d55eabbc0b573a5272a1b86e22670a4fb66f4eb4703788b65c4b20bfd4b
rq2c_algorithmic_communities.csv|103968|b2a0630cd54f9c0e775b93a91524e49affb18e22f3d7089a2c16077226c06704
rq2c_structural_brokerage_candidates.csv|197701|723a5608f6b837585aed8354720ffa0074b4f0e5ec5628aaa1b6966dd2bb0f6e
rq2c_structural_brokerage_top50.csv|3216|198be0915086ed495fe2daf56daf67fc5671ad341d7b7e57b5e64be966ae9d6c
rq2c_undirected_view_edges.csv|227205|3ae36a7e6d357d250052288f9ca62dac865ab3590dd02189b19ba957113db254
rq2c_undirected_view_lcc_edges.csv|225181|67f71f3feb399425546c5ae8dc12b07c47f94a50578324e0abb8d14379ebadc3
rq2c_undirected_view_summary.json|836|489cc280b1f8d835032de7e06b9ed2acd85e97fab799476cfcbdffc844017446
rq3_kruskal_fdr_effect_sizes.csv|4903|3ba3257c7a0060c95737d57065bea55e5e0d1d8e6a6b40493b6a24ad9b4c7363
rq3_seed_role_aware_features.csv|83163|3f4c3ca2ca9ee33765f669bafbfdff11e4c12bbe01ed35e750bac74212d9cb82
rq3_subdomain_descriptive_comparison.csv|18976|89a7330959bca41b011a349f424b67dad5106e8d6fa6801664532d402d632277
seed_observability_audit.json|515|e4db9864d998e4099fc43e03f9acb82691dbeefd7ce3a5f6b6f5990866f172de
```

## 3. Input lineage

The corrected P0 manifest records 296 inputs: the frozen annotation snapshot,
the activity-statistics file, and 294 v2 corrected aggregate partitions. The
P0 output manifest does not consume the 294 v2 relation partitions directly;
those relation partitions are captured by the candidate-input manifest.

The candidate manifest is
`docs/freeze/ch5_refq_repository_identity_correction_candidate_manifest_v1.json`
with status `CANDIDATE`. Its recorded input groups and current-file checks are:

| group | recorded | missing | hash mismatches | byte mismatches |
|---|---:|---:|---:|---:|
| candidate relation partitions | 294 | 0 | 0 | not recorded |
| candidate aggregate partitions | 294 | 0 | 0 | not recorded |
| historical P0 input files | 296 | 0 | 0 | 0 |

The candidate controls additionally report candidate seeds 301, analysis seeds
294, one affected source seed, 293 unaffected source seeds, unique full-event
join count 12,518,072, zero repository-ID conflicts, and zero post-admission
source-seed membership mismatches. These controls are consistent with the
corrected output audits, including 120 excluded out-of-seed source rows.

## 4. Execution evidence search

Search scope included the implementation repository, the source-data workspace,
and the thesis workspace for `C3`, the corrected output root, execute/run-log
terms, stdout/stderr, pytest, network algorithm terms, and S1-S7 terms.

Found:

- the v2 config, candidate manifest, correction protocol, C1/C2/C2.5 review
  documents, and the corrected output manifest;
- older source-data `run_time-2.2.4*.log` files containing historical
  `api.github.com` error chatter.

Not found:

- a dedicated corrected-P0/C3 execution log;
- a corrected-P0 stdout or stderr capture;
- a C3 authorization record;
- a C3 old/new comparison report;
- corrected S1-S7 or C4 output roots.

The older runtime logs are not attributable to the corrected P0 run. Their
GitHub API messages therefore prevent treating the workspace-wide absence of
an API-call trace as proof of zero calls, while not providing evidence that the
corrected P0 run itself made a call.

## 5. Boundary classification

| control | classification | basis |
|---|---|---|
| corrected P0 output exists and is complete | VERIFIED | manifest exists; 30/30 files present and hash/byte matched |
| manifest status and validation | VERIFIED | manifest `PASS`; all five validation fields `PASS` |
| P0 execution count equals 1 | INFERRED | one output run window and one output manifest; no independent run ledger |
| GH-CoRE semantic rerun equals 0 | INFERRED | candidate control says 0 and P0 inputs are frozen v2 aggregates; no execution trace |
| GitHub API calls equals 0 | UNKNOWN | candidate declaration says 0, but no attributable call log or process trace |
| raw external query equals 0 | UNKNOWN | protocol requires false and candidate says 0, but no independent execution trace |
| S1-S7 rerun equals 0 | INFERRED | no corrected supplemental outputs and historical S1-S7 roots are unchanged; transient runs cannot be excluded |
| network algorithm configuration unchanged | VERIFIED | common v1/v2 algorithm controls match; `network_views.py` matches historical tag and main |
| exact authorized C3 invocation | UNKNOWN | protocol records `AUTHORIZE_C3_P0_EXECUTION = NO`; no later authorization artifact exists |

## 6. Contamination checks

The implementation worktree is clean on branch
`ch5-refq-repository-identity-correction-v1`. `main` remains at
`dc88221ae6e0bb72f2c142b2811a4552c5ec2388` and the branch diff contains no
figure, manuscript, paper, TeX, DOCX, C4, or output paths. The corrected output
is ignored by the source-data repository and was checked directly on disk.

The annotated historical tag `chapter5-refq-freeze-v1.0` dereferences to
`68d001551359d120bf2a06cc5e571742df7e7822`; the tag and historical v1 config
remain unchanged. Historical supplemental S6 figure-ready files do exist in
the repository, but no corrected figure artifacts were added or modified and
no figure was rendered by this audit. No C4 artifact root or corrected
manuscript artifact was found.

The source-data checkout itself has pre-existing untracked directories and
logs, including the candidate data roots. That checkout state is reported for
transparency; the complete hash comparison above is the relevant input
lineage control, and this audit did not modify it.

## 7. Rerun determination and final decision

No rerun was performed or is necessary to establish the current bundle's file
and input-hash integrity. The existing corrected P0 output can be retained as
a candidate result with the limitations above.

An authorized, independently logged C3 rerun would be required only if the
release gate requires unrestricted proof of exact invocation count, zero API
calls, zero raw external queries, and explicit C3 authorization. This audit
cannot manufacture that evidence, and the protocol explicitly prohibited C3
execution. Therefore the appropriate decision for the existing artifacts is:

```text
C3_PROVENANCE_RECONSTRUCTED_WITH_LIMITATIONS
```

## 8. Source records

- `outputs/reference_quotient_p0_corrected_v2/manifest.json`
- `docs/freeze/ch5_refq_repository_identity_correction_candidate_manifest_v1.json`
- `docs/freeze/ch5_refq_versioned_repository_identity_correction_protocol_v1.md`
- `docs/freeze/ch5_refq_repository_identity_correction_c2_5_p0_integration_review_v1.md`
- `script/ch5_reference_quotient/pipeline.py`
- `outputs/reference_quotient_p0_frozen/` and historical supplemental roots,
  inspected only for contamination comparison
