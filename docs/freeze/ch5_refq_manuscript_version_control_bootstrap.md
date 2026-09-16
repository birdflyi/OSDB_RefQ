# Chapter 5 RefQ — Manuscript Version-Control Bootstrap

## Decision

`CH5_REFQ_MANUSCRIPT_VERSION_CONTROL_BOOTSTRAP_PASS`

This task established manuscript revision identity and immutable local
snapshots without editing manuscript content or running scientific workflows.

## 1. Source identity

| Item | Value |
|---|---|
| Repository | `D:/github_repo/OSDB_RefQ` |
| Branch | `ch5-refq-repository-identity-correction-v1` |
| Repository HEAD before | `603a63d793c870ebc4bbd6719eff6f2af60efcea` |
| Remote HEAD before | `603a63d793c870ebc4bbd6719eff6f2af60efcea` |
| Source manuscript | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md` |
| Revision | `MS-R01` |
| Scientific baseline | `P0-v3` |
| Stage | `POST_G1_FINAL_EDIT` |
| Accepted decision | `CH5_REFQ_FINAL_SUBMISSION_EDIT_G1_PASS` |

The source identity was verified before copying:

```text
SOURCE_SHA = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
SOURCE_BYTES = 114716
SOURCE_LF = 861
SOURCE_CRLF = 0
SOURCE_CR_ONLY = 0
SOURCE_BOM = False
SOURCE_FINAL_LF = True
```

## 2. Created local revision objects

| Role | Path | SHA-256 | Bytes |
|---|---|---|---:|
| Immutable snapshot | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/versions/MS-R01_POST_G1_CF488538.md` | `CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE` | 114716 |
| Editable CURRENT alias | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_CURRENT.md` | `CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE` | 114716 |
| CURRENT identity sidecar | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_CURRENT.identity.txt` | metadata file | n/a |

The snapshot and CURRENT alias were created using byte copies of the verified
source.  Neither copy was decoded, normalized, or re-saved during creation.

```text
SNAPSHOT_BYTE_IDENTICAL = YES
CURRENT_ALIAS_BYTE_IDENTICAL = YES
ORIGINAL_AUTHORITATIVE_SHA = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
ORIGINAL_AUTHORITATIVE_SHA_AFTER = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
CURRENT_ALIAS_SHA = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
MS_R01_SNAPSHOT_SHA = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
MANUSCRIPT_SEMANTIC_CHANGE_COUNT = 0
```

## 3. Manifest and lineage

Manifest:

`docs/freeze/ch5_refq_manuscript_version_manifest.md`

It records the accepted HIST-C → HIST-RQ1 → HIST-I → MS-R01 lineage, the
unaccepted interrupted SHA
`0E39E2FF8D80DCD72E883F5A9141F4F003D5A3C2C6F2A28E46D2B0809D23F125`,
and Rules V1–V7 governing immutable snapshots, one editable CURRENT path,
exact task parents, resume semantics, adjacent diffs, hunk authorization, and
revision promotion.

The manifest distinguishes:

- scientific baseline: frozen scientific authority (`P0-v3`);
- manuscript revision: accepted text identity (`MS-R01`);
- task baseline: explicit parent revision and SHA for one task;
- interrupted intermediate state: observed but unaccepted SHA;
- accepted manuscript state: PASS decision plus exact manuscript SHA;
- repository audit HEAD: Git commit recording the accepted audit/provenance.

## 4. Future working rule

Future Codex manuscript tasks must edit only `第5章-paper1_CURRENT.md`, state
`TASK_BASE_REVISION` and `TASK_BASE_SHA`, and stop on a mismatch.  Immutable
`versions/MS-Rxx...` files must never be edited.  Historical long filenames
are compatibility artifacts, not implicit diff baselines.

## 5. No-content-change and scientific guards

```text
MANUSCRIPT_SEMANTIC_CHANGE_COUNT = 0
SCIENTIFIC_RECOMPUTATION = 0
SCIENTIFIC_ASSETS_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
TABLE_CHANGED = 0
RQ_CHANGED = 0
APPENDIX_CHANGED = 0
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
```

Only the two repository-side documentation files created by this task are
authorized for the Git commit.  The external source manuscript, snapshot,
CURRENT alias, and identity sidecar remain outside the repository.

## 6. Final status

```text
MANUSCRIPT_REVISION = MS-R01
SCIENTIFIC_BASELINE = P0-v3
STAGE = POST_G1_FINAL_EDIT
SOURCE_SHA = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
SNAPSHOT_SHA = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
CURRENT_ALIAS_SHA = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
SNAPSHOT_BYTE_IDENTICAL = YES
CURRENT_ALIAS_BYTE_IDENTICAL = YES
```

The exact decision is:

`CH5_REFQ_MANUSCRIPT_VERSION_CONTROL_BOOTSTRAP_PASS`
