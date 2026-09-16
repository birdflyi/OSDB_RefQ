# Chapter 5 RefQ Manuscript Version Manifest

## 1. Current authority

```text
MANUSCRIPT_REVISION = MS-R01
SCIENTIFIC_BASELINE = P0-v3
STAGE = POST_G1_FINAL_EDIT
DECISION = CH5_REFQ_FINAL_SUBMISSION_EDIT_G1_PASS
ACCEPTED_MANUSCRIPT_SHA = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
REPOSITORY_AUDIT_HEAD = 603a63d793c870ebc4bbd6719eff6f2af60efcea
```

The scientific baseline identifies the frozen scientific authority.  The
manuscript revision identifies an accepted text state.  A task baseline is the
exact revision/SHA from which one authorized task starts.  An interrupted
intermediate state is an observed but unaccepted SHA.  The repository audit
HEAD identifies the Git commit that records the acceptance decision; it is not
the manuscript content identity.

Current paths:

| Role | Path | Mutability |
|---|---|---|
| Editable working manuscript | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_CURRENT.md` | Editable only by an explicitly authorized future manuscript task |
| Accepted MS-R01 snapshot | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/versions/MS-R01_POST_G1_CF488538.md` | Immutable |
| Compatibility copy | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md` | Retained, but not a future implicit diff baseline |
| Working identity sidecar | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_CURRENT.identity.txt` | Update only during accepted revision promotion |

## 2. Accepted lineage

| Revision | Stage | Parent manuscript SHA | Accepted manuscript SHA | Repository HEAD after audit | Decision |
|---|---|---|---|---|---|
| HIST-C | Batch C Methods | `2ADF5AC63C1EC696EC2EC411444FC04B5588D3BC539CECD5A7C8F01976C9B2E1` | `BEB6E89127032EA93843AB2385573EE1306C087A06B182753A24AB9E74ED1761` | `909bf6faaa0b0e7a78421e28ee93d6342f47ec5e` | `CH5_REFQ_SUBMISSION_EDIT_BATCH_C_METHODS_PASS` |
| HIST-RQ1 | RQ1 terminology reconciliation | `BEB6E89127032EA93843AB2385573EE1306C087A06B182753A24AB9E74ED1761` | `07F0C28A9F6A10679C2AFB3FC16836CE19FD65CCF9498ED35066F2A175C07255` | `5b8a6f4965215ed8a7966e49b036070399aae303` | historical reconciliation pass |
| HIST-I | Post-interruption integrity repair | `07F0C28A9F6A10679C2AFB3FC16836CE19FD65CCF9498ED35066F2A175C07255` | `8BF9F6225FF160CFE661D30C9D2A7F9A1656A4BE34A0F244F70072957F526B18` | `695b7c4e18351066c2917d359b115d00573c2657` | `CH5_REFQ_POST_INTERRUPTION_INTEGRITY_REPAIR_PASS` |
| MS-R01 | G1 final bounded edit | `8BF9F6225FF160CFE661D30C9D2A7F9A1656A4BE34A0F244F70072957F526B18` | `CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE` | `603a63d793c870ebc4bbd6719eff6f2af60efcea` | `CH5_REFQ_FINAL_SUBMISSION_EDIT_G1_PASS` |

Known interrupted, unaccepted state:

```text
INTERRUPTED_INTERMEDIATE_SHA = 0E39E2FF8D80DCD72E883F5A9141F4F003D5A3C2C6F2A28E46D2B0809D23F125
ACCEPTED_REVISION = NO
```

The interrupted SHA is provenance evidence only.  It is not an accepted
revision, parent, or replacement task baseline.

## 3. Normative revision protocol

### Rule V1 — Immutable accepted snapshots

Once a revision receives PASS, its snapshot
`versions/MS-Rxx_POST_<stage>_<sha8>.md` must never be modified.

### Rule V2 — One editable path

Only `第5章-paper1_CURRENT.md` may be modified by future Codex manuscript
tasks.  Accepted `MS-Rxx` snapshots are read-only.

### Rule V3 — Exact parent

Every manuscript task must state:

```text
TASK_BASE_REVISION
TASK_BASE_SHA
```

The task must stop if `第5章-paper1_CURRENT.md` does not match the expected SHA.

### Rule V4 — Resume semantics

After interruption, record both:

```text
TASK_BASE_SHA
RESUME_OBSERVED_SHA
```

`RESUME_OBSERVED_SHA` never silently replaces the task baseline.

### Rule V5 — Adjacent diff

The default validation diff is `TASK_BASE_SHA -> candidate SHA` or
`MS-R(n-1) -> MS-R(n)`.  An arbitrary older `finalqa*.md` file must never be
used to judge a single editing batch.  A deliberately non-adjacent comparison
must be labeled `HISTORICAL_CUMULATIVE_DIFF`.

### Rule V6 — Hunk authorization

Every changed region must map to an authorized task edit ID:

```text
UNMAPPED_CHANGED_REGION_COUNT = 0
```

### Rule V7 — Promotion

After PASS:

1. compute the final manuscript SHA;
2. create the immutable `MS-Rxx_POST...` snapshot;
3. update this manifest and the CURRENT identity sidecar;
4. only then begin the next task.

## 4. Historical local-file warning

Files named like `...finalqa.md`, `...finalqa(1).md`, or
`...composition(...).md` may represent different historical states.  A
filename is not sufficient to establish parent-child lineage.  Only the exact
SHA together with this manifest's revision identity is authoritative.

## 5. MS-R01 identity closure

```text
SCIENTIFIC_BASELINE = P0-v3
MANUSCRIPT_REVISION = MS-R01
TASK_BASE_SHA = 8BF9F6225FF160CFE661D30C9D2A7F9A1656A4BE34A0F244F70072957F526B18
ACCEPTED_MANUSCRIPT_SHA = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
SNAPSHOT_SHA = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
CURRENT_ALIAS_SHA = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
```
