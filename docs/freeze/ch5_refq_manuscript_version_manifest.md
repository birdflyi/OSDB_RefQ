# Chapter 5 RefQ Manuscript Version Manifest

## 1. Current authority

```text
MANUSCRIPT_REVISION = MS-R04
SCIENTIFIC_BASELINE = P0-v3
STAGE = OBSERVATION_FRAMING_ACCEPTED
DECISION = CH5_REFQ_MS_R04_PROMOTION_PASS
ACCEPTED_MANUSCRIPT_SHA = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
REPOSITORY_AUDIT_HEAD = 0bc8e04adace4934216208f5271f149b8ab0605f
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
| Accepted MS-R04 snapshot | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/versions/MS-R04_POST_OBSERVATION_FRAMING_F8071504.md` | Immutable |
| Historical accepted MS-R03 snapshot | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/versions/MS-R03_POST_SUBMISSION_CONDENSED_E59F96FF.md` | Immutable |
| Historical accepted MS-R02 snapshot | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/versions/MS-R02_EDITORIAL_COMPLETE_B1494BA3.md` | Immutable |
| Historical accepted MS-R01 snapshot | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/versions/MS-R01_POST_G1_CF488538.md` | Immutable |
| Compatibility copy | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md` | Retained, but not a future implicit diff baseline |
| Working identity sidecar | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_CURRENT.identity.txt` | Update only during accepted revision promotion |

## 2. Accepted lineage

| Revision | Stage | Parent manuscript SHA | Accepted manuscript SHA | Repository HEAD after audit | Decision |
|---|---|---|---|---|---|
| HIST-C | Batch C Methods | `2ADF5AC63C1EC696EC2EC411444FC04B5588D3BC539CECD5A7C8F01976C9B2E1` | `BEB6E89127032EA93843AB2385573EE1306C087A06B182753A24AB9E74ED1761` | `909bf6faaa0b0e7a78421e28ee93d6342f47ec5e` | `CH5_REFQ_SUBMISSION_EDIT_BATCH_C_METHODS_PASS` |
| HIST-RQ1 | RQ1 terminology reconciliation | `BEB6E89127032EA93843AB2385573EE1306C087A06B182753A24AB9E74ED1761` | `07F0C28A9F6A10679C2AFB3FC16836CE19FD65CCF9498ED35066F2A175C07255` | `5b8a6f4965215ed8a7966e49b036070399aae303` | historical reconciliation pass |
| HIST-I | Post-interruption integrity repair | `07F0C28A9F6A10679C2AFB3FC16836CE19FD65CCF9498ED35066F2A175C07255` | `8BF9F6225FF160CFE661D30C9D2A7F9A1656A4BE34A0F244F70072957F526B18` | `695b7c4e18351066c2917d359b115d00573c2657` | `CH5_REFQ_POST_INTERRUPTION_INTEGRITY_REPAIR_PASS` |
| MS-R01 | G1 final bounded edit | `8BF9F6225FF160CFE661D30C9D2A7F9A1656A4BE34A0F244F70072957F526B18` | `CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE` | `603a63d793c870ebc4bbd6719eff6f2af60efcea` | `CH5_REFQ_FINAL_SUBMISSION_EDIT_G1_PASS` |
| MS-R02 | Editorial-complete promotion | `CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE` | `B1494BA3133713CAA34D3A62D99DF94878028560CD065FBCC01F0E5A897479AC` | `06371e41c66801cd948fea73cb066f30f421e4d4` | `CH5_REFQ_MS_R02_PROMOTION_PASS` |
| MS-R03 | Submission-condensed promotion | `B1494BA3133713CAA34D3A62D99DF94878028560CD065FBCC01F0E5A897479AC` | `E59F96FF05279797BD047B127B537FEA2D1FB618478DBB5455C36EA2A83777F9` | `2384b46922f44199e2e3d9d7a54cc7017c9a53b5` | `CH5_REFQ_MS_R03_PROMOTION_PASS` |
| MS-R04 | Bounded observation framing promotion | `E59F96FF05279797BD047B127B537FEA2D1FB618478DBB5455C36EA2A83777F9` | `F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549` | `0bc8e04adace4934216208f5271f149b8ab0605f` | `CH5_REFQ_MS_R04_PROMOTION_PASS` |

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

## 6. MS-R02 accepted identity closure

```text
MANUSCRIPT_REVISION = MS-R02
SCIENTIFIC_BASELINE = P0-v3
SHA256 = B1494BA3133713CAA34D3A62D99DF94878028560CD065FBCC01F0E5A897479AC
SNAPSHOT = versions/MS-R02_EDITORIAL_COMPLETE_B1494BA3.md

PREVIOUS_ACCEPTED_REVISION = MS-R01
PREVIOUS_ACCEPTED_SHA = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
PROMOTION_BASE_REPO_HEAD = bf74defb3dbfca885f2d4d7633b4ef07c2d10bea

EDITORIAL_COMPLETE = YES
FINAL_EDITORIAL_QA = docs/freeze/ch5_refq_ms_r02_candidate_final_editorial_qa_rerun.md
FINAL_EDITORIAL_QA_DECISION = CH5_REFQ_MS_R02_CANDIDATE_FINAL_QA_RERUN_PASS_READY_FOR_PROMOTION
MS_R02_PROMOTION_COMMIT = 06371e41c66801cd948fea73cb066f30f421e4d4
```

The accepted MS-R02 bytes are identical across CURRENT, the immutable MS-R02
snapshot, and the retained working candidate. MS-R01 remains an immutable
historical accepted revision and is not deleted, renamed, or rewritten.

Figure authority for MS-R02:

```text
FIGURE1_3_AUTHORITY = accepted V6 assets under figures/ch5_refq/p0v3_final_v6
FIGURE4_AUTHORITY_ROOT = figures/ch5_refq/p0v3_final_v6_e01_eta_label
FIGURE4_SVG_SHA256 = 6EC08F8462BB13F46395678A5BFB1B5E753377399D5CFA612F85FD273B34E17A
FIGURE4_PDF_SHA256 = DAF4F9C486B19F229D0D13586CFCEABA774BF7212466D7174877C57F07307C0C
FIGURE4_PNG_SHA256 = 6A279AE45570C06E745DB65D3B14503B30F2AD98DAAC5C64DD8611A082FC44EA
```

Figure 1-3 retain the accepted V6 authority. Figure 4 uses the V6 E-01
terminology-corrected derivative. Historical V6 assets remain unchanged.

## 7. MS-R03 accepted identity closure

```text
MANUSCRIPT_REVISION = MS-R03
SCIENTIFIC_BASELINE = P0-v3
STAGE = SUBMISSION_CONDENSED_ACCEPTED
SHA256 = E59F96FF05279797BD047B127B537FEA2D1FB618478DBB5455C36EA2A83777F9
SNAPSHOT = versions/MS-R03_POST_SUBMISSION_CONDENSED_E59F96FF.md

PREVIOUS_ACCEPTED_REVISION = MS-R02
PREVIOUS_ACCEPTED_SHA = B1494BA3133713CAA34D3A62D99DF94878028560CD065FBCC01F0E5A897479AC
PROMOTION_BASE_REPO_HEAD = 67791ef9af4e856b8af9f3b0faaaedf10d30ccdb

EDITORIAL_COMPLETE = YES
VENUE_INDEPENDENT_CONDENSATION_COMPLETE = YES
JOURNAL_SPECIFIC_PREPARATION_PENDING = YES
FINAL_ENGLISH_ABSTRACT_PENDING = YES

FINAL_QA = docs/freeze/ch5_refq_ms_r03_submission_condensation_final_qa.md
FINAL_QA_DECISION = CH5_REFQ_MS_R03_SUBMISSION_CONDENSATION_FINAL_QA_PASS_READY_FOR_PROMOTION
MS_R03_PROMOTION_COMMIT = 2384b46922f44199e2e3d9d7a54cc7017c9a53b5
```

The accepted MS-R03 bytes are identical across CURRENT, the immutable MS-R03
snapshot, and the retained MS-R03 working candidate. MS-R01 and MS-R02 remain
immutable historical accepted revisions and are not deleted, renamed, or
rewritten. MS-R03 is editorially complete for venue-independent condensation;
journal-specific preparation and a fresh authoritative English Abstract remain
pending.

Figure authority for MS-R03 remains:

```text
FIGURE1_3_AUTHORITY = accepted V6 assets under figures/ch5_refq/p0v3_final_v6
FIGURE4_AUTHORITY_ROOT = figures/ch5_refq/p0v3_final_v6_e01_eta_label
FIGURE4_SVG_SHA256 = 6EC08F8462BB13F46395678A5BFB1B5E753377399D5CFA612F85FD273B34E17A
FIGURE4_PDF_SHA256 = DAF4F9C486B19F229D0D13586CFCEABA774BF7212466D7174877C57F07307C0C
FIGURE4_PNG_SHA256 = 6A279AE45570C06E745DB65D3B14503B30F2AD98DAAC5C64DD8611A082FC44EA
```

## 8. MS-R04 accepted identity closure

```text
MANUSCRIPT_REVISION = MS-R04
SCIENTIFIC_BASELINE = P0-v3
STAGE = OBSERVATION_FRAMING_ACCEPTED
SHA256 = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
SNAPSHOT = versions/MS-R04_POST_OBSERVATION_FRAMING_F8071504.md

PREVIOUS_ACCEPTED_REVISION = MS-R03
PREVIOUS_ACCEPTED_SHA = E59F96FF05279797BD047B127B537FEA2D1FB618478DBB5455C36EA2A83777F9
PROMOTION_BASE_REPO_HEAD = 9a37b7fec667ef4aa98d8a4d2afcc5a21f01753a

EDITORIAL_COMPLETE = YES
VENUE_INDEPENDENT_CONDENSATION_COMPLETE = YES
OBSERVATION_FRAMING_COMPLETE = YES
JOURNAL_SPECIFIC_PREPARATION_PENDING = YES
FINAL_ENGLISH_ABSTRACT_PENDING = YES
READY_FOR_JOURNAL_SPECIFIC_PREPARATION = YES
FINAL_SUBMISSION_READY = NO

FINAL_QA = docs/submission_suggestion/ch5_refq_ms_r04_bounded_observation_framing_final_qa.md
FINAL_QA_DECISION = CH5_REFQ_MS_R04_BOUNDED_OBSERVATION_FRAMING_FINAL_QA_PASS_READY_FOR_PROMOTION
MS_R04_PROMOTION_COMMIT = 0bc8e04adace4934216208f5271f149b8ab0605f
MS_R04_PROVENANCE_REGISTRATION_COMMIT = 6c54e4568a0341e0057bfc26c226bde0317604d4
```

The accepted MS-R04 bytes are identical across CURRENT, the immutable MS-R04
snapshot, and the verified MS-R04 candidate. MS-R01, MS-R02, and MS-R03 remain
immutable historical accepted revisions and are not deleted, renamed, or
rewritten. MS-R04 adds only the bounded observation-framing closure recorded
by its candidate and Final QA; no scientific values or assets were changed.

Figure authority remains the accepted V6 assets:

```text
FIGURE1_3_AUTHORITY = figures/ch5_refq/p0v3_final_v6
FIGURE4_AUTHORITY_ROOT = figures/ch5_refq/p0v3_final_v6_e01_eta_label
FIGURE4_SVG_SHA256 = 6EC08F8462BB13F46395678A5BFB1B5E753377399D5CFA612F85FD273B34E17A
FIGURE4_PDF_SHA256 = DAF4F9C486B19F229D0D13586CFCEABA774BF7212466D7174877C57F07307C0C
FIGURE4_PNG_SHA256 = 6A279AE45570C06E745DB65D3B14503B30F2AD98DAAC5C64DD8611A082FC44EA
```
