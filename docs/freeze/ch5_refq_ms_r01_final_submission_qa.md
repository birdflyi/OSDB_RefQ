# Chapter 5 RefQ — MS-R01 Read-Only Final Submission QA

## Decision

`CH5_REFQ_MS_R01_FINAL_QA_PASS_SUBMISSION_READY`

MS-R01 is submission-ready as-is.  This QA found no factual/scientific blocker
and no submission-blocking manuscript issue.  The manuscript, accepted
snapshot, identity sidecar, and version manifest were read-only throughout.
No MS-R02 revision was created.

## 1. Version identity and immutability

| Item | Value |
|---|---|
| Repository | `D:/github_repo/OSDB_RefQ` |
| Branch | `ch5-refq-repository-identity-correction-v1` |
| Repository HEAD before QA | `7ba2b581a5f7452d6918e2638e89a12a407d3987` |
| Manuscript revision | `MS-R01` |
| Scientific baseline | `P0-v3` |
| CURRENT | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_CURRENT.md` |
| Immutable snapshot | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/versions/MS-R01_POST_G1_CF488538.md` |
| CURRENT SHA-256 before/after | `CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE` |
| Snapshot SHA-256 before/after | `CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE` |
| Manifest accepted SHA | `CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE` |
| Bytes | 114,716 for CURRENT and snapshot |
| Snapshot filesystem status | read-only |

The required identity equality holds:

```text
CURRENT_SHA == SNAPSHOT_SHA == MANIFEST_ACCEPTED_SHA
CURRENT_EQUALS_SNAPSHOT = YES
```

Repository-head semantics are coherent rather than conflicting:

```text
MANUSCRIPT_ACCEPTANCE_REPO_HEAD = 603a63d793c870ebc4bbd6719eff6f2af60efcea
VERSION_CONTROL_METADATA_HEAD = 7ba2b581a5f7452d6918e2638e89a12a407d3987
```

The first commit records G1 manuscript acceptance.  The second records the
later version-control registry bootstrap.  For future promoted revisions, the
sidecar should replace the generic `repo_head` field with explicit fields such
as `manuscript_acceptance_repo_head` and `metadata_registry_repo_head`.  The
current sidecar was not modified in this QA.

Pre/post metadata hashes:

```text
SIDECAR_SHA = F6E76D4D9C496148B3FB78C897AC4A72A9467E8B8A404F188932FC8CBB3E0688
MANIFEST_SHA = 1CAEE8CF8D8A27451A76C9529BF449D4DB5107677C6A69BECF6ECCAA39B5B8D7
MANUSCRIPT_CHANGED = 0
CURRENT_CHANGED = 0
SNAPSHOT_CHANGED = 0
SIDECAR_CHANGED = 0
MANIFEST_CHANGED = 0
MS_R01_CHANGED = 0
NEW_REVISION_CREATED = 0
```

## 2. Scientific consistency closure

### 2.1 Evidence flow

| Contract | Manuscript state | Result |
|---|---|---|
| Candidate → analysis seeds | 301 candidates; 294 analysis seeds; 7 exclusions due to frozen-2023-evidence unavailability | `PASS` |
| Source admission | 3,748,078 scanned; 120 out-of-seed source records; 3,747,958 admitted | `PASS` |
| Admitted target partition | 1,586,047 project-mappable; 1,686,729 non-project; 475,182 unresolved | `PASS` |
| Unit meaning | Figure 1 and Methods explicitly identify all flow counts as Reference records | `PASS` |

Every repeated occurrence uses the same population and stage meaning.  No
project/entity/edge interpretation is substituted for the record counts.

### 2.2 RefQN scale

| Quantity | Accepted value | Result |
|---|---:|---|
| Node domain | 6,506 | `PASS` |
| Edge-observed nodes | 6,505 | `PASS` |
| Zero-edge nodes | 1 | `PASS` |
| Directed edges including self-loops | 9,884 | `PASS` |
| Self-loops | 289 | `PASS` |
| Directed cross-project edges | 9,595 | `PASS` |
| Cross-project total weight | 138,974 | `PASS` |
| First-order undirected edges | 9,547 | `PASS` |
| Components / isolates | 55 / 30 | `PASS` |
| LCC nodes / undirected edges | 6,367 / 9,462 | `PASS` |
| LCC directed sensitivity edges | 9,510 | `PASS` |

Methods mapping, §4.2.0, Tables 4.6b–4.6f, and Figure 2/3 captions retain
compatible units and denominators.  Directed edge counts, evidence weight, and
undirected edge counts are not conflated.

### 2.3 Observation and RefQ contracts

| Contract | Evidence in MS-R01 | Result |
|---|---|---|
| Source completeness | 294 analysis seeds are source-complete; expanded targets are source-incomplete | `PASS` |
| Strict admission | `event_repo_id == frozen annotated seed github_repo_id` | `PASS` |
| Ordering | source admission precedes membership registry, profile accumulation, and edge aggregation | `PASS` |
| Target domain | project-mappable targets need not belong to the 294 seeds | `PASS` |
| Membership | quotient eligibility requires a project-mappable endpoint with unique project membership | `PASS` |
| Weight | each retained quotient-eligible Reference row contributes one current implementation weight unit | `PASS` |
| Formula | `Q = M^T R_P M` | `PASS` |
| Self-loop policy | general RefQ retains self-loops; cross-project views exclude them | `PASS` |
| Undirected view | `U(G_RefQ)` is a first-order direction-ignored view | `PASS` |

No later Results, Discussion, Conclusion, or Appendix statement silently
redefines these contracts.

### 2.4 Second-order exclusion

`QQ^T`, `Q^T Q`, `K=XΦX^T`, shared-reference, and shared-neighbor projections
remain explicitly distinct from first-order RefQ.  They are described as
excluded or future-work relations; no passage claims that they were executed
as the primary analysis.

```text
SECOND_ORDER_PRIMARY_ANALYSIS_CLAIM = 0
SECOND_ORDER_REMAINS_FUTURE_OR_EXCLUDED = PASS
```

## 3. RQ and contribution hierarchy closure

The exact five-item RQ list remains present and unchanged:

```text
RQ1
RQ2a
RQ2b
RQ2c
RQ3
```

The narrative hierarchy is consistent across Introduction, Results,
Discussion, Conclusion, and Appendix mapping:

- RQ1 supplies evidence/input/composition and construction-boundary support;
- RQ2a/RQ2b/RQ2c form the Project-level RefQN structural empirical center;
- RQ3 is a bounded, label-mode-sensitive DBMS subdomain comparison.

The paper does not present the five RQs as five co-equal contributions.

Exactly four ordered contributions remain:

1. relation construction/formalization contract;
2. boundary-aware evidence instantiation;
3. observation-aware role-aware empirical characterization;
4. traceable weaker-semantic structural evidence positioning.

The Abstract preserves the same four-part order in compressed form;
Introduction §1.4 remains the full authority; the Conclusion remains
structure-first and consistent with that hierarchy.

```text
RQ_COUNT = 5
RQ_TEXT_CLOSURE = PASS
RQ_HIERARCHY_CLOSURE = PASS
CONTRIBUTION_COUNT = 4
CONTRIBUTION_ORDER_CLOSURE = PASS
```

## 4. RQ1 operational-metric closure

| Field | Current operational meaning | Regression check | Result |
|---|---|---|---|
| `active_issue_pr_count` | unique Reference-bearing Issue/PR context keys | explicitly not all repository active Issues/PRs | `PASS` |
| `comment_per_issue` | unique issue/PR-related source entities divided by Reference-bearing context count | explicitly not comment count or discussion depth | `PASS` |
| `comment_reference_density` | admitted Reference rows divided by unique issue/PR-related source entities | explicitly not references per comment | `PASS` |
| `external_reference_share` | complete non-self share: external-project + non-project + unresolved over total | explicitly not non-project-only share | `PASS` |
| `non_project_reference_share` | non-project target records over total | explicitly one component of the non-self side | `PASS` |

Residual phrases such as “all repository active issues,” “discussion depth,”
and “references per comment” occur only in negative semantic guards.  No
positive operational regression was found.

## 5. Network-method and RQ3 statistical closure

### 5.1 Network methods

```text
Louvain = weighted, weight="weight", seed=20260731
modularity = weighted
local clustering = unweighted, weight=None
approximate betweenness = unweighted, weight=None
approximate betweenness k = 500
approximate betweenness seed = 20260731
approximate betweenness normalized = True
```

Methods state these settings exactly.  Results describe Louvain communities as
algorithmic partitions and betweenness outputs as structural brokerage
candidates, without upgrading either to semantic or causal roles.

### 5.2 RQ3 statistics

```text
MINIMUM_ELIGIBLE_GROUP_N = 5
LABEL_MODES = include_mixed / exclude_mixed_or_multilabel
FDR_FAMILY = all actually computed feature-level KW p-values within each label mode
CROSS_MODE_ROBUST_FEATURE_COUNT = 0
```

The Abstract, Figure 4 caption, §4.3, §5.1/§5.4, §6.4, and Conclusion agree:
Reference-composition metrics are not FDR-supported in either mode; selected
role/local-structure/project-age features pass only under `include_mixed`; no
feature is robust across both modes.

## 6. Figure, table, and citation closure

### 6.1 Figures and tables

Figures 1–4 each occur once with one caption in the corresponding Results
context.  Their terminology and denominators agree with adjacent text:

- Figure 1: Reference-record evidence flow and target partition;
- Figure 2: source/target roles, coverage denominator 294, and target-weight
  shares over cross-project total weight 138,974;
- Figure 3: first-order `U(G_RefQ)`, LCC, and algorithmic Louvain partitions;
- Figure 4: two label modes, FDR status, and zero cross-mode robust features.

Tables 4.1–4.8 are present and ordered, including 4.6a–4.6f.  Each caption
occurs once; table mentions and reported values are consistent with the
surrounding prose.  Table 4.6c's continuation is correctly labeled as a
continuation rather than a new table number.

```text
FIGURE_CAPTION_COUNT = 4
FIGURE_NUMBERING_CLOSURE = PASS
TABLE_4_1_TO_4_8_CLOSURE = PASS
TABLE_4_6A_TO_4_6F_CLOSURE = PASS
FIGURE_TABLE_DENOMINATOR_CLOSURE = PASS
```

### 6.2 Citations and bibliography

```text
CITATION_TOKEN_COUNT = 68
UNIQUE_CITATION_KEY_COUNT = 31
BIBLIOGRAPHY_ENTRY_COUNT = 31
MISSING_KEYS = 0
ORPHAN_BIBLIOGRAPHY_ENTRIES = 0
MALFORMED_CITATION_SYNTAX = 0
```

No literature search or citation edit was performed.

## 7. Availability and reproducibility closure

The manuscript keeps the required states distinct:

| State | Manuscript statement | Result |
|---|---|---|
| Existing public relation/data release | available through project README | `PASS` |
| Zenodo DOI | `10.5281/zenodo.18817348` | `PASS` |
| Final submission replication package | not automatically identical to the existing release; scope/version reconciliation remains required | `PASS` |
| Raw GitHub user-generated content | no unconditional redistribution commitment | `PASS` |
| Full GH-CoRE/code release | not established by the existing data DOI | `PASS` |
| Appendix A | reproducibility/provenance authority, not an independent availability promise | `PASS` |

No new public-release state or promise was inferred.

## 8. Publication-language residual inventory

Main-text counts exclude Appendix A.  Appendix counts are shown to distinguish
intentional provenance fields from publication prose.

| Term | Main text | Appendix A | Classification |
|---|---:|---:|---|
| bare `P0` | 3 literals on 2 lines (§3.1.2 and §3.1.3) | 0 | `P2_STYLE_RESIDUAL`; deliberately outside G1 scope and scientifically unambiguous |
| `P0-v3` | 0 | 7 | `ACCEPTABLE_REPRODUCIBILITY_TERM` |
| `S4` | 0 | 1 | `ACCEPTABLE_REPRODUCIBILITY_TERM` |
| `S5` | 0 | 1 | `ACCEPTABLE_REPRODUCIBILITY_TERM` |
| `S7` | 0 | 1 | `ACCEPTABLE_REPRODUCIBILITY_TERM` |
| `robustness_alert` | 0 | 1 | `ACCEPTABLE_REPRODUCIBILITY_TERM` |
| `RELEASE_READY` | 0 | 1 | `ACCEPTABLE_REPRODUCIBILITY_TERM` |
| `audit` family | 1 (§8 `audits`) | 4 | `ACCEPTABLE_REPRODUCIBILITY_TERM` |
| `guard` | 0 | 0 | no occurrence |
| `stage` family | 0 | 1 (`STAGE_PACKAGE_COMPLETE`) | `ACCEPTABLE_REPRODUCIBILITY_TERM` |

The remaining main-text `P0` instances distinguish upstream materialization
from P0/current-analysis multiplicity handling.  They do not create a factual
or operational ambiguity and are not a submission blocker.

## 9. Readability diagnostics

Heuristic: paragraphs are contiguous prose blocks after excluding headings,
lists, Markdown tables, fenced code, and display math; sentences are split on
Chinese terminal punctuation and terminal English punctuation followed by an
uppercase letter/digit.  `very-long` means more than 240 characters.  The
numbers are diagnostics, not an editing rule.

| Section | Paragraphs | Sentences | Very-long | Max sentence chars |
|---|---:|---:|---:|---:|
| Abstract | 6 | 16 | 1 | 728 |
| §1 Introduction | 20 | 46 | 7 | 373 |
| §2 Related Work | 15 | 50 | 6 | 452 |
| §3 Methods | 56 | 100 | 4 | 335 |
| §4 Results | 59 | 132 | 8 | 619 |
| §5 Discussion | 12 | 33 | 2 | 295 |
| §6 Validity | 10 | 30 | 1 | 248 |
| §7 Availability | 3 | 7 | 0 | 163 |
| §8 Supplement | 1 | 2 | 0 | 181 |
| §9 Conclusion | 4 | 9 | 1 | 274 |
| Appendix A | 8 | 22 | 3 | 352 |

The longest Abstract sentence is the explicitly enumerated four-part
contribution hierarchy.  The longest Results blocks are figure captions or
dense metric descriptions whose units are clearer when kept together.  Some
remaining long, mixed-language sentences are optional P2 readability surfaces,
but none materially obstructs the accepted scientific meaning or requires a
submission-blocking edit.  Another global sentence-length sweep is not
recommended.

## 10. Overclaim closure

Searches for power law, scale-free, heavy tail, dependency/task ground truth,
causality, importance, collaboration quality, problem complexity, stable
semantic communities, complete GitHub/OSS ecosystem, and longitudinal claims
found only negative guards, cross-sectional limitations, bibliography text, or
future-work requirements.

```text
POSITIVE_OVERCLAIM_COUNT = 0
NEGATIVE_GUARD_CLOSURE = PASS
```

## 11. Version-control integrity

- `MS-R01_POST_G1_CF488538.md` is the only `MS-Rxx` file in `versions/` and is
  filesystem read-only.
- CURRENT is byte-identical to the MS-R01 snapshot.
- No MS-R02 file or manifest revision exists.
- Historical `finalqa*.md` and `composition*.md` files remain compatibility or
  historical files; the manifest explicitly forbids treating them as adjacent
  baselines by filename alone.
- The HIST-C → HIST-RQ1 → HIST-I → MS-R01 lineage is internally coherent.
- `0E39E2FF8D80DCD72E883F5A9141F4F003D5A3C2C6F2A28E46D2B0809D23F125`
  remains interrupted/unaccepted provenance only.

```text
CURRENT_EQUALS_SNAPSHOT = YES
MS_R01_CHANGED = 0
NEW_REVISION_CREATED = 0
MANIFEST_LINEAGE_CLOSURE = PASS
INTERRUPTED_SHA_ACCEPTED = NO
```

## 12. Severity table

```text
P0_COUNT = 0
P1_COUNT = 0
P2_COUNT = 2
INFO_COUNT = 8
```

| ID | Surface | Finding | Severity | Submission effect |
|---|---|---|---|---|
| P2-01 | §3.1.2 / §3.1.3 | Three bare `P0` literals remain in two deliberately excluded Methods lines | P2 | None; meaning is operationally clear |
| P2-02 | Abstract/§§1–6/§9 | A bounded set of long, mixed-language technical sentences remains | P2 | None; no global rewrite recommended |
| INFO-01 | Scientific flow and scale | All frozen values and units agree | INFO | Ready |
| INFO-02 | Observation/RefQ contract | Admission, membership, weight, loop, and first-order semantics close | INFO | Ready |
| INFO-03 | RQ/contribution hierarchy | Five RQs and four ordered contributions remain coherent | INFO | Ready |
| INFO-04 | Metrics/network/statistics | RQ1 metrics, network settings, and RQ3 FDR contract close | INFO | Ready |
| INFO-05 | Figures/tables/citations | Numbering, denominators, captions, and bibliography close | INFO | Ready |
| INFO-06 | Availability | DOI, release scope, raw-data, code, and Appendix states remain distinct | INFO | Ready |
| INFO-07 | Overclaim | All sensitive terms are negative guards or future scope | INFO | Ready |
| INFO-08 | Version registry | Future sidecars should use two explicit repository-head field names | INFO | No MS-R01 change required |

## 13. Scientific execution and read-only guards

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
SCIENTIFIC_ASSETS_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
MANUSCRIPT_CHANGED = 0
CURRENT_CHANGED = 0
SNAPSHOT_CHANGED = 0
SIDECAR_CHANGED = 0
MANIFEST_CHANGED = 0
```

Only this final QA record is authorized for the repository commit.

## 14. Final status

```text
MANUSCRIPT_REVISION = MS-R01
SCIENTIFIC_BASELINE = P0-v3
CURRENT_SHA = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
SNAPSHOT_SHA = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
P0_COUNT = 0
P1_COUNT = 0
P2_COUNT = 2
INFO_COUNT = 8
SUBMISSION_READY = YES
```

The exact final decision is:

`CH5_REFQ_MS_R01_FINAL_QA_PASS_SUBMISSION_READY`
