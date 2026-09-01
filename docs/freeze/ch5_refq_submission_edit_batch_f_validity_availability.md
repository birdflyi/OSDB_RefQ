# Chapter 5 RefQ Submission Editing Batch F

## Validity, Reliability and Availability Audit Record

This is a documentation-only record for `BATCH_F_VALIDITY_AVAILABILITY`.
No scientific pipeline, data refresh, figure render, or test suite was run.
The authoritative manuscript is an external file; it is recorded by SHA-256
and is not treated as Git-tracked repository content.

## Decision

`CH5_REFQ_SUBMISSION_EDIT_BATCH_F_VALIDITY_AVAILABILITY_PASS`

The validity, reliability, and availability wording is internally coherent and
contains no fabricated release commitment. The public archival scope remains
explicitly pending platform/privacy/licensing review and author confirmation;
the manuscript records that conditional state without converting it into an
unconditional promise.

## 1. Starting identities

| Item | Value |
| --- | --- |
| Repository | `D:\github_repo\OSDB_RefQ` |
| Branch | `ch5-refq-repository-identity-correction-v1` |
| Repository HEAD before Batch F | `3802a052c253135799f8ee33a14df38e493eceb6` |
| Remote HEAD before Batch F | `3802a052c253135799f8ee33a14df38e493eceb6` |
| Expected manuscript SHA before Batch F | `C729D739F00757840B8F456C18A88327946127CBEB5635DE2E08662B5D3C462C` |
| Read-only baseline | `C:\Users\10651\AppData\Local\Temp\ch5_refq_batch_f_validity_availability_baseline_20260901.md` |
| Observed manuscript SHA at resume | `98A86B6D0AC39EC13FFBEAA2C311763272C2C090E72955AA7599FB862262536C` |
| Manuscript before final §7/§8 edit | `98A86B6D0AC39EC13FFBEAA2C311763272C2C090E72955AA7599FB862262536C` |
| Manuscript after Batch F | `6AC27FF254A7C902284158CC65C399EE61C7C380D3C6CE974516D1499526D533` |
| Authoritative manuscript | `C:\Users\10651\Documents\trae_projects\thesis\ch5_analysis_reference_coupling_for_osdbms\第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md` |

The resume SHA differs from the Batch F starting SHA because the previously
authorized §6, §6.1–§6.3 and §6.5 wording edits had already been applied before
the final continuation. The final SHA includes those edits and the §7/§8 edits
recorded below.

The repository worktree before and after the documentation commit retained only
the four pre-existing untracked archives:

```text
figures/ch5_refq/p0v3_final_v3.zip
figures/ch5_refq/p0v3_final_v4.zip
figures/ch5_refq/p0v3_final_v5.zip
figures/ch5_refq/p0v3_final_v6.zip
```

## 2. Authorized scope

Changed manuscript surfaces are limited to §6, §6.1–§6.3, §6.5, §7 and §8.
§6.4 was reviewed and retained. No other manuscript region was edited.

| Guard | Result |
| --- | --- |
| `THREATS_CHANGED` | `1` |
| `AVAILABILITY_CHANGED` | `1` |
| `SUPPLEMENTARY_NOTE_CHANGED` | `1` |
| `ABSTRACT_CHANGED` | `0` |
| `INTRODUCTION_CHANGED` | `0` |
| `RELATED_WORK_CHANGED` | `0` |
| `METHODS_CHANGED` | `0` |
| `RESULTS_CHANGED` | `0` |
| `DISCUSSION_CHANGED` | `0` |
| `CONCLUSION_CHANGED` | `0` |
| `APPENDIX_CHANGED` | `0` |
| `REFERENCES_CHANGED` | `0` |
| `RQ_TEXT_CHANGED` | `0` |
| `TABLE_CONTENT_CHANGED` | `0` |
| `FIGURE_CAPTION_CHANGED` | `0` |
| `FIGURE_ASSETS_CHANGED` | `0` |
| `SCIENTIFIC_ASSETS_CHANGED` | `0` |

## 3. State-model derivation

Appendix A remains the read-only technical provenance authority. It records the
P0-v3 and supplemental identities, manifests, runtime information, audits and
the status `STAGE_PACKAGE_COMPLETE / RELEASE_READY`. That status is interpreted
as technical readiness for internal reconstruction, not as proof of a public
archive, DOI, URL, license decision or persistent external availability.

The manuscript-facing state after editing is:

```text
INTERNAL_SUPPLEMENTAL_PACKAGE_TECHNICAL_STATE = RELEASE_READY
PUBLIC_ARCHIVAL_RELEASE_STATE = PENDING_SCOPE_AND_LICENSE_CONFIRMATION
RAW_LOG_PUBLIC_RELEASE_COMMITMENT = NO
UNCONDITIONAL_CODE_RELEASE_PROMISE = NO
PUBLIC_ARCHIVE_IDENTIFIER_AVAILABLE = NO
```

## 4. Edit record

### §6 and §6.1

The opening is neutral and describes interpretation boundaries and potential
threats without the defensive phrase “不削弱本文结果的经验价值”. Construct
validity now explicitly separates observable GitHub Reference evidence from the
complete knowledge-flow construct while retaining the dependency-ground-truth,
task-resolution and fine-grained-semantic limits with reduced repetition.

### §6.2

The extraction, regex/rule, API, entity-resolution, membership and quotient
construction threats and their mitigation categories remain. The replication-
package availability todo was removed; the section ends with the scientific
limitation that quality controls reduce but cannot eliminate extraction and
membership-resolution error and that provenance supports review.

### §6.3

The DBMS cross-domain statement is bounded as an external-validity limitation:
direct transfer to other OSS domains is limited by the DBMS technical and
maintenance context, and systematic cross-domain differences remain to be
tested by dedicated comparative work. The seed-centered observation boundary
and source-incomplete expanded targets remain explicit.

### §6.4

The descriptive, Spearman, Kruskal–Wallis, epsilon-squared, BH-FDR,
label-mode-sensitivity and approximate-betweenness limits were retained. No RQ
statistical status was changed.

### §6.5

Reliability now describes the conditions required for reconstruction:
sampling identity; extraction and membership rules; software/runtime identity;
statistical settings; and observation/semantic boundaries. It acknowledges that
Appendix A records these items and explains that API visibility, rate limits,
permissions and mutable external resources can prevent byte-identical future
recreation. It contains no public-material inventory and no “建议公开” advice.

### §7 final public-availability wording

§7 is the sole manuscript authority for public release status. Its three compact
parts state that the internal scientific/supplemental package exists and is
identified by Appendix A, while the external archive scope remains subject to
platform terms, user-generated content, external links, privacy/licensing
boundaries and author confirmation; list only potentially appropriate processed
materials and derived outputs; and keep code/GH-CoRE scope and the final archive
identifier pending the same review. The section explicitly says that raw logs
are not unconditionally promised and that no public archive identifier is yet
available.

### §8 final supplementary-material role

§8 only describes Appendix A as a reproducibility-and-boundary appendix covering
identity, membership/observation audits, analysis-to-RQ mapping and
statistical/semantic boundaries. It explicitly does not make a separate public
archive or data/code availability declaration.

## 5. Minimum issue table

| ID | Section | Issue | Treatment | Risk after edit |
| --- | --- | --- | --- | --- |
| F01 | §6 | Defensive opening | Replaced with neutral boundary wording | Closed |
| F02 | §6.1 | Repeated semantic disclaimers | Consolidated while retaining construct boundary | Closed |
| F03 | §6.2 | Replication-package todo in internal validity | Removed; retained scientific mitigation limit | Closed |
| F04 | §6.3 | Possible DBMS cross-domain implication | Recast as bounded external-validity concern | Closed |
| F05 | §6.5 | “仍需进一步整理 replication package” | Replaced by existing provenance/reconstructability account | Closed |
| F06 | §6.5 | “建议公开/附录化” advice voice | Removed from reliability section | Closed |
| F07 | §7 | Mixed public-release statuses | Replaced with one pending-scope state | Closed |
| F08 | §7 | Raw-data redistribution ambiguity | Explicitly no unconditional raw-log promise | Closed |
| F09 | §7 | GH_CoRE/code-release ambiguity | Scope remains subject to terms, privacy, licensing and confirmation | Closed |
| F10 | §7 | Missing final public identifier | States none is currently available; no identifier invented | Closed without fabrication |
| F11 | §8 | Availability/reproducibility overlap | §8 restricted to Appendix A role | Closed |
| F12 | Appendix A / §7 | `RELEASE_READY` versus public release | Technical and public states explicitly separated | Closed |

## 6. Role-separation matrix

| Surface | Primary role | Must contain | Must not contain | Result |
| --- | --- | --- | --- | --- |
| §6.5 Reliability | Reproducibility threats and conditions | Provenance and reconstructability limits | Public-release todo list | `PASS` |
| §7 Availability | Public-release status | Scope and release conditions | Invented URL/DOI | `PASS` |
| §8 Supplement | Appendix role | What Appendix A supports | Second availability statement | `PASS` |
| Appendix A | Technical provenance | Frozen package identity/status | Editorial promises | `PASS` |

`RELIABILITY_AVAILABILITY_APPENDIX_ROLE_SEPARATION = PASS`

## 7. Availability-status matrix

| Object | Technical state | Public state | Manuscript authority |
| --- | --- | --- | --- |
| Scientific result package | Frozen/existing | Not equivalent to publication state | Appendix A |
| Supplemental package | `RELEASE_READY` internally | Public archival release not inferred | Appendix A plus §7 distinction |
| Processed data/edges | Exist for analysis | Scope subject to review | §7 |
| Raw GitHub logs | Used internally | Redistribution not committed | §7 |
| Analysis code | Exists internally | Release scope pending review | §7 |
| GH_CoRE source | Exists internally | Release scope pending review | §7 |
| Public archive ID | None supplied | Pending final archive | §7 |

`TECHNICAL_VS_PUBLIC_STATE_SEPARATED = PASS`

## 8. Redundancy and authority audit

| Repeated material | Classification |
| --- | --- |
| Observable Reference evidence versus complete knowledge-flow construct in §6.1 | `NECESSARY_LOCAL_VALIDITY_BOUNDARY` |
| Extraction/membership/API threats and mitigations in §6.2 | `NECESSARY_LOCAL_VALIDITY_BOUNDARY` |
| Reconstructability and provenance limits in §6.5 | `REPRODUCIBILITY_AUTHORITY` |
| Public material scope and release conditions in §7 | `PUBLIC_AVAILABILITY_AUTHORITY` |
| Appendix identity/audit contents in §8 | `REPRODUCIBILITY_AUTHORITY` |
| §8 public-release inventory or promise | `REDUNDANT_CAN_REMOVE` (absent after edit) |

`PUBLIC_RELEASE_MATERIAL_LIST_AUTHORITIES = 1` (the single list is in §7).

## 9. Citation and numeric closure

No literature search was performed. The before/after citation totals are 68 and
68, with 31 unique keys in both versions; the unique citation-key set is
unchanged. The IREL and GitHub documentation citations in §6.2 remain.

The full-manuscript numeric-token multiset is unchanged: 1,167 tokens before
and 1,167 after. Therefore:

```text
UNIQUE_CITATION_KEY_SET_CHANGED = 0
NEW_SCIENTIFIC_VALUE_COUNT = 0
SCIENTIFIC_VALUE_CHANGE_COUNT = 0
UNIQUE_SCIENTIFIC_VALUE_LOSS_COUNT = 0
NUMERIC_TOKEN_CHANGE_COUNT = 0
```

## 10. Semantic and layer guards

```text
CONSTRUCT_VALIDITY_BOUNDARY = PASS
CONSTRUCT_BOUNDARY_REDUNDANCY_REDUCED = PASS
INTERNAL_VALIDITY_THREAT_MITIGATION_ROLE = PASS
DBMS_BOUNDED_GENERALIZATION = PASS
SEED_CENTERED_EXTERNAL_VALIDITY = PASS
CONCLUSION_VALIDITY_STATISTICAL_STATUS = PASS
RQ3_LABEL_MODE_BOUNDARY = PASS
BROKERAGE_SAMPLING_BOUNDARY = PASS
RELIABILITY_PROVENANCE_ROLE = PASS
RELIABILITY_APPENDIX_A_ACKNOWLEDGED = PASS
VALIDITY_ROLE_SEPARATION = PASS
AVAILABILITY_SINGLE_AUTHORITY = PASS
APPENDIX_PROVENANCE_AUTHORITY = PASS
SUPPLEMENTARY_ROLE = PASS
PUBLIC_RELEASE_STATUS_UNIFIED = PASS
DEPENDENCY_OVERCLAIM = 0
TASK_RESOLUTION_OVERCLAIM = 0
KNOWLEDGE_FLOW_CAUSAL_CLAIM = 0
COMPLETE_ECOSYSTEM_CLAIM = 0
CROSS_DOMAIN_EMPIRICAL_CLAIM = 0
FACT_LAYER_LEAKAGE = NO
STRUCTURE_LAYER_DILUTION = NO
TASK_LAYER_LEAKAGE = NO
ACCESS_LAYER_LEAKAGE = NO
```

## 11. Wording diagnostics for §§6–8

| Term | Before | After |
| --- | ---: | ---: |
| `建议` | 2 | 0 |
| `正在整理` | 1 | 0 |
| `拟整理` | 1 | 0 |
| `投稿前` | 2 | 0 |
| `最终提供` | 0 | 0 |
| `最终归档` | 1 | 0 |
| `需要作者` | 1 | 0 |
| `需要进一步` | 0 | 0 |
| `replication package` | 2 | 0 |
| `reproducibility` | 3 | 4 |
| `Appendix A` | 1 | 2 |
| `公开` | 7 | 2 |
| `归档` | 3 | 7 |

The remaining `公开` and `归档` occurrences describe the observed GitHub
scope and the explicitly conditional public archive state; they are not author
todo language. No URL, DOI, accession ID or unconditional release phrase was
introduced.

Readability diagnostics for the §6–§8 block use the established `>240`
character heuristic:

```text
VALIDITY_AVAILABILITY_SENTENCE_COUNT_BEFORE = 45
VALIDITY_AVAILABILITY_SENTENCE_COUNT_AFTER = 39
VERY_LONG_SENTENCE_COUNT_BEFORE = 1
VERY_LONG_SENTENCE_COUNT_AFTER = 0
MAX_SENTENCE_LENGTH_BEFORE = 263
MAX_SENTENCE_LENGTH_AFTER = 230
```

## 12. Exact immutability checks

The following comparisons were made against the read-only Batch F baseline:

```text
PREFIX_BEFORE_§6_BYTE_IDENTICAL = PASS
POST_§9_BYTE_IDENTICAL = PASS
APPENDIX_A_BYTE_IDENTICAL = PASS
APPENDIX_TECHNICAL_STATUS_CHANGED = 0
NON_VALIDITY_AVAILABILITY_PROSE_CHANGED = 0
UNAUTHORIZED_MANUSCRIPT_REGION_CHANGE_COUNT = 0
TABLE_CHANGE_COUNT = 0
FIGURE_CAPTION_EDIT_COUNT = 0
RQ_TEXT_CHANGED = 0
```

The four V3–V6 ZIP files remain untracked and untouched. No repository scientific
output, manifest, receipt, renderer, figure or code file was changed.

## 13. Scientific execution guards

```text
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
FIGURE_ASSETS_CHANGED = 0
SCIENTIFIC_ASSETS_CHANGED = 0
```

## 14. Recommendation

The manuscript wording is ready for conservative submission review on validity,
reliability and availability semantics. The eventual public archive scope,
licenses, privacy boundaries and identifier remain conditional author-level
release decisions; the manuscript does not claim that those decisions have
already been finalized. This is non-scientific and non-blocking for the present
wording audit.

The next review may proceed with the three-way manuscript reconciliation while
preserving the conditional public-archive state; a finalized archival record can
be inserted later without changing the scientific validity wording.

## 15. Commit scope

The only intended repository addition for this batch is this file:

`docs/freeze/ch5_refq_submission_edit_batch_f_validity_availability.md`

Suggested commit message:

```text
docs(ch5): record validity availability submission edit
```

The commit hash and push result are reported in the final handoff after the
documentation-only commit. No manuscript file is Git-tracked by this commit.
