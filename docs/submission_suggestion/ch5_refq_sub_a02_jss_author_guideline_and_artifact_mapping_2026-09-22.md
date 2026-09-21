# Chapter 5 RefQ SUB-A02: JSS Research Paper Author-Guideline and Submission-Artifact Mapping

## 1. Decision

`CH5_REFQ_SUB_A02_PASS_NO_MS_R05_REQUIRED`

This is a read-only JSS requirement audit and submission-artifact mapping for
the frozen `Research Paper` route. It does not edit the manuscript, create an
English manuscript, create submission artifacts, or change scientific state.

All public-web findings are `VERIFIED_AS_OF = 2026-09-22`.

## 2. Task and repository authority

```text
TASK = CH5_REFQ_SUB_A02_JSS_AUTHOR_GUIDELINE_AND_ARTIFACT_MAPPING
TASK_MODE = READ_ONLY_JOURNAL_REQUIREMENT_AUDIT
REPOSITORY = D:/github_repo/OSDB_RefQ
BRANCH = ch5-refq-repository-identity-correction-v1
TASK_BASE_REPOSITORY_HEAD = 89740b0216b45abca23fab4f4af5d954fc02d839
LOCAL_HEAD_BEFORE = 89740b0216b45abca23fab4f4af5d954fc02d839
REMOTE_HEAD_BEFORE = 89740b0216b45abca23fab4f4af5d954fc02d839
AHEAD_BEHIND_BEFORE = 0 / 0
```

The JSS target was frozen by
`docs/submission_suggestion/ch5_refq_target_venue_freeze_jss_2026-09-22.md`.
The four pre-existing V3-V6 figure ZIP files remain untracked and untouched.

## 3. MS-R04 manuscript authority

```text
TASK_BASE_REVISION = MS-R04
TASK_BASE_SHA = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
SCIENTIFIC_BASELINE = P0-v3
STAGE = OBSERVATION_FRAMING_ACCEPTED
CURRENT_SHA = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
MS_R04_SNAPSHOT_SHA = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
CURRENT_EQUALS_MS_R04_SNAPSHOT = YES
```

The accepted CURRENT and immutable snapshot were read directly. Neither was
written. MS-R04 retains `RQ_COUNT = 5`, `CONTRIBUTION_COUNT = 4`, and the
frozen paper centre:

> RefQ provides a traceable and observation-aware operationalization of
> project-level explicit-reference structure.

Its interpretation remains role-dependent, observation-bounded, and
metric-dependent, with additional RQ3 sensitivity to label operationalization.
No dependency, task-resolution, causal, platform, or AI claim is introduced.

## 4. JSS Research Paper target authority

```text
TARGET_JOURNAL = Journal of Systems and Software
TARGET_TRACK = RESEARCH_PAPER
EDITORIAL_MANAGER_EXACT_ARTICLE_TYPE_LABEL = Research Paper
EDITORIAL_MANAGER_EXACT_ARTICLE_TYPE_LABEL_VERIFIED = YES
EDITORIAL_MANAGER_ARTICLE_TYPE_VALUE_OBSERVED = 1
PRIMARY_TARGET_STATUS = FROZEN
SPECIAL_TRACK_SELECTED = NO
SPECIAL_ISSUE_SELECTED = NO
VSI_SELECTED = NO
BACKUP_JOURNAL = Empirical Software Engineering
```

The prior venue decision remains
`CH5_REFQ_SUB_A01_PASS_RECOMMEND_JSS`. JSS-versus-EMSE ranking is not reopened.

## 5. Source hierarchy and access log

| Source ID | Source title | URL/path | Access date | Source level | Access status | Claims supported |
|---|---|---|---|---|---|---|
| S1 | JSS Editorial Manager | https://www.editorialmanager.com/jssoftware/ | 2026-09-22 | EDITORIAL_MANAGER | AVAILABLE | Current submission-system entry and frozen `Research Paper` article-type evidence. |
| S2 | JSS Guide for Authors | https://www.elsevier.com/journals/journal-of-systems-and-software/0164-1212/guide-for-authors | 2026-09-22 | JSS_OFFICIAL | BLOCKED | Official guide URL; redirected to the ScienceDirect publish guide and returned HTTP 403. No detailed rule is inferred. |
| S3 | Journal of Systems and Software journal page | https://www.sciencedirect.com/journal/journal-of-systems-and-software | 2026-09-22 | JSS_OFFICIAL | BLOCKED | Official journal identity URL; automated access was blocked. |
| S4 | Elsevier CRediT author statement policy | https://www.elsevier.com/researcher/author/policies-and-guidelines/credit-author-statement | 2026-09-22 | ELSEVIER_GENERAL | AVAILABLE | Publisher-level CRediT policy exists; exact JSS placement remains journal-guide dependent. |
| S5 | MS-R04 target freeze | `docs/submission_suggestion/ch5_refq_target_venue_freeze_jss_2026-09-22.md` | 2026-09-22 | PROJECT_AUTHORITY | AVAILABLE | Frozen venue, route, article-type label, and no-manuscript-change gate. |
| S6 | SUB-A01 comparative audit | `docs/submission_suggestion/ch5_refq_sub_a01_jss_vs_emse_target_venue_audit_2026-09-21.md` | 2026-09-22 | PROJECT_AUTHORITY | AVAILABLE | Prior JSS recommendation, EMSE backup, and evidence boundary. |
| S7 | MS-R04 Final QA | `docs/submission_suggestion/ch5_refq_ms_r04_bounded_observation_framing_final_qa.md` | 2026-09-22 | PROJECT_AUTHORITY | AVAILABLE | MS-R04 semantic and scientific readiness. |

An official source that is blocked is recorded as `UNVERIFIED` for its specific
requirement details. Older SUB-A01 observations are not promoted to current
JSS rules.

## 6. Current manuscript and asset inventory

| Asset ID | Path | Status | Role | Authority | Relevant JSS requirements |
|---|---|---|---|---|---|
| AS-M01 | `.../第5章-paper1_CURRENT.md` | 633 lines; immutable for this task | Accepted Chinese semantic source | AUTHORITATIVE | Main manuscript, title, abstract, keywords, sections, tables, figures, references |
| AS-M02 | `.../versions/MS-R04_POST_OBSERVATION_FRAMING_F8071504.md` | Immutable snapshot | Accepted revision | AUTHORITATIVE | Identity and byte-level source closure |
| AS-M03 | `.../working/MS-R04_BOUNDED_OBSERVATION_FRAMING_CANDIDATE.md` | External candidate | Candidate provenance | HISTORICAL/WORKING | Adjacent revision comparison only |
| AS-M04 | `figures/ch5_refq/p0v3_final_v6` | Accepted render root | Figures 1-3 | AUTHORITATIVE | Figure upload/export mapping |
| AS-M05 | `figures/ch5_refq/p0v3_final_v6_e01_eta_label` | Accepted derivative root | Figure 4 | AUTHORITATIVE | Figure upload/export mapping |
| AS-M06 | `outputs/reference_quotient_p0_corrected_v3/` | Frozen P0-v3 outputs | Scientific result authority | AUTHORITATIVE | Data/result provenance; not regenerated |
| AS-M07 | `supplemental/reference_quotient_v2/outputs_p0v3/` | Final supplemental outputs | Reproducibility package | AUTHORITATIVE | Supplement/data/reproducibility mapping |
| AS-M08 | Zenodo DOI `10.5281/zenodo.18817348` | Existing public relation/data release | Public availability | AUTHORITATIVE | Data availability and repository link |
| AS-M09 | `docs/freeze/ch5_refq_manuscript_version_manifest.md` | Accepted lineage manifest | Version identity | AUTHORITATIVE | Accepted revision provenance |
| AS-M10 | `docs/freeze/ch5_refq_ms_r04_promotion.md` | Promotion record | Promotion provenance | AUTHORITATIVE | Accepted state and guards |

The manuscript inventory is: five RQs, four contributions, 14 main-text table
blocks, four figure captions, seven keywords, a 297-Chinese-character abstract
with zero citations, and 70 citation-token occurrences over 33 bibliography
entries. Sections 7-8 cover data/code availability and supplements; Appendix A
records reproducibility identity, audits, RQ coverage, and semantic/statistical
boundaries. No author, CRediT, funding, competing-interest, ethics, or cover-
letter artifact is currently authoritative in the manuscript tree.

## 7. Atomic JSS requirement matrix

`SOURCE_ACCESS_STATUS` is the access status of the cited source. `VERIFICATION_STATUS`
is `VERIFIED`, `PARTIALLY_VERIFIED`, or `UNVERIFIED`. Action classes follow the
task taxonomy. `Finding` is the severity contribution used in the final counts.

| Req ID | Domain | Requirement | Strength | Source | Access | Verification | Current MS-R04 or asset state | Gap | Action class | Target artifact | Stage | Block translation | Block submission | Finding |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A01 | Article type | Select current `Research Paper` route | HARD_REQUIREMENT | S1 | AVAILABLE | VERIFIED | Frozen and directly observed | None | PACKAGING_ONLY | Editorial Manager field | Submission | NO | YES | E2 |
| A02 | Source format | Current editable/PDF/Word/LaTeX upload rules | UNVERIFIED | S2 | BLOCKED | UNVERIFIED | Chinese source exists; no current JSS format rule established | Exact accepted format unknown | UNVERIFIED | Main manuscript upload | SUB-A02 follow-up | NO | YES | INFO |
| A03 | Title | English title, title-page placement, title constraints | HARD_REQUIREMENT | S2 | BLOCKED | PARTIALLY_VERIFIED | Chinese title exists; English title pending | Translation and exact constraints | ENGLISH_TRANSLATION_STAGE | English manuscript/title page | Translation | NO | YES | E2 |
| A04 | Abstract | Research Paper abstract form, limit, citation/abbreviation rules | HARD_REQUIREMENT | S2 | BLOCKED | PARTIALLY_VERIFIED | 297 Chinese characters, zero citations; English abstract pending | Exact current limit/form unknown | ENGLISH_TRANSLATION_STAGE | English abstract | Translation | NO | YES | E2 |
| A05 | Keywords | Required count, format, and English form | HARD_REQUIREMENT | S2 | BLOCKED | PARTIALLY_VERIFIED | Seven Chinese/English technical keywords present | Exact count/format unknown | ENGLISH_TRANSLATION_STAGE | English keyword field | Translation | NO | YES | E2 |
| A06 | Length | Research Paper word/page/reference limits | UNVERIFIED | S2 | BLOCKED | UNVERIFIED | No limit asserted in MS-R04 | Current limit unknown | UNVERIFIED | Submission manuscript | SUB-A02 follow-up | NO | YES | INFO |
| A07 | Structure | Required/recommended section architecture | UNVERIFIED | S2 | BLOCKED | UNVERIFIED | Sections 1-9 plus Appendix A exist; no rule verified | Do not impose IMRaD by assumption | UNVERIFIED | Main manuscript | Translation/packaging | NO | YES | INFO |
| A08 | Title page | Separate title page and author/contact fields | CONDITIONAL | S2 | BLOCKED | UNVERIFIED | No authoritative title-page artifact | Build only if required | PACKAGING_ONLY | Title page file | Packaging | NO | YES | INFO |
| A09 | Review model | Anonymous/single-blind/double-anonymous handling | CONDITIONAL | S2 | BLOCKED | UNVERIFIED | No anonymization action taken | Review model and identity rules unknown | PACKAGING_ONLY | Main manuscript/title page | Packaging | NO | YES | INFO |
| A10 | Highlights | Whether required, bullet count, character limit, file category | OPTIONAL | S2 | BLOCKED | UNVERIFIED | No highlights created | Rule unknown | PACKAGING_ONLY | Highlights file if required | Packaging | NO | YES | INFO |
| A11 | Graphical abstract | Required/recommended/optional status and format | OPTIONAL | S2 | BLOCKED | UNVERIFIED | No graphical abstract created | Rule unknown | PACKAGING_ONLY | Graphical abstract if required | Packaging | NO | YES | INFO |
| A12 | Figures | Formats, resolution, vector/color/font and separate-file rules | HARD_REQUIREMENT | S2 | BLOCKED | UNVERIFIED | Accepted V6/V6-E01 assets exist | Exact JSS export rules unknown | PACKAGING_ONLY | Figure files/captions | Packaging | NO | YES | INFO |
| A13 | Tables | Editable text, placement, captions, footnotes, image restrictions | HARD_REQUIREMENT | S2 | BLOCKED | UNVERIFIED | 14 editable Markdown table blocks | Exact JSS table rule unknown | PACKAGING_ONLY | Table source/placement | Packaging | NO | YES | INFO |
| A14 | References | Free-format/style, DOI, and consistency rules | HARD_REQUIREMENT | S2 | BLOCKED | UNVERIFIED | 70 tokens, 33 entries, DOI-rich bibliography | Exact initial-submission style unknown | PACKAGING_ONLY | Reference list | Packaging | NO | YES | INFO |
| A15 | Supplement | Allowed files, naming, linking, and publication behavior | CONDITIONAL | S2 | BLOCKED | UNVERIFIED | Supplemental P0-v3 package exists | Exact JSS supplement policy unknown | PACKAGING_ONLY | Supplement package | Packaging | NO | YES | INFO |
| A16 | Research data | Data statement, repository link, exceptions | RECOMMENDED | S4/S2 | PARTIAL/BLOCKED | PARTIALLY_VERIFIED | §7 states Zenodo DOI and release/package distinction | Final statement and version mapping need packaging | PACKAGING_ONLY | Data Availability Statement + DOI | Packaging | NO | YES | E2 |
| A17 | Code/software | Code disclosure/share/exception policy | RECOMMENDED | S2/S4 | BLOCKED | UNVERIFIED | §7 explicitly avoids blanket GH_CoRE release claim | Current policy unknown | PACKAGING_ONLY | Code statement/repository link | Packaging | NO | YES | INFO |
| A18 | Open Science | Badges, artifact evaluation, research objects, linked assets | OPTIONAL | S2/S3 | BLOCKED | UNVERIFIED | Provenance and supplemental assets exist; no badge claim | No verified JSS process | PACKAGING_ONLY | Optional linked artifacts | Packaging | NO | NO | INFO |
| A19 | CRediT | CRediT taxonomy and placement | RECOMMENDED | S4 | AVAILABLE | VERIFIED | No CRediT statement yet | Author-specific statement needed later | PACKAGING_ONLY | CRediT statement | Packaging | NO | YES | E2 |
| A20 | Authorship | Eligibility/order/authorship policy | CONDITIONAL | S2/S4 | BLOCKED/PARTIAL | UNVERIFIED | Author metadata not part of MS-R04 source | Author confirmation required | PACKAGING_ONLY | Author metadata/declarations | Packaging | NO | YES | INFO |
| A21 | Funding | Funding declaration and location | CONDITIONAL | S2/S4 | BLOCKED | UNVERIFIED | No authoritative funding statement | Author fact required | PACKAGING_ONLY | Funding declaration | Packaging | NO | YES | INFO |
| A22 | Interests | Competing-interest/declaration tool or statement | HARD_REQUIREMENT | S2/S4 | BLOCKED | UNVERIFIED | No authoritative declaration artifact | Author fact and exact location unknown | PACKAGING_ONLY | Declaration of interests | Packaging | NO | YES | INFO |
| A23 | Generative AI | AI-assisted writing/figure/author policy | RECOMMENDED | S4/S2 | BLOCKED | UNVERIFIED | No author-specific declaration made | Policy and factual use record require follow-up | PACKAGING_ONLY | AI-use declaration | Packaging | NO | YES | INFO |
| A24 | Ethics | Human subjects/informed consent/IRB trigger | NOT_APPLICABLE | PROJECT_AUTHORITY | AVAILABLE | VERIFIED | Repository-mining study uses public project records; no human-subject intervention | No triggered ethics semantic | NO_CHANGE | None unless journal form asks | Packaging check | NO | NO | INFO |
| A25 | Permissions | Third-party reproduced material/permissions | CONDITIONAL | S2/S4 | BLOCKED | UNVERIFIED | Figures/tables are project outputs; exhaustive rights audit not done | Confirm no third-party reproduction | PACKAGING_ONLY | Permissions record if needed | Packaging | NO | YES | INFO |
| A26 | Acknowledgements | Placement and timing | OPTIONAL | S2 | BLOCKED | UNVERIFIED | No new acknowledgements drafted | Rule/author text unknown | PACKAGING_ONLY | Acknowledgements field | Packaging | NO | NO | INFO |
| A27 | Cover letter | Required/recommended/optional contents | RECOMMENDED | S2/S3 | BLOCKED | UNVERIFIED | No cover letter created | Current JSS instruction unknown | PACKAGING_ONLY | Cover letter | Packaging | NO | YES | INFO |
| A28 | Reviewers | Suggested/opposed reviewer fields | CONDITIONAL | S1/S2 | PARTIAL/BLOCKED | UNVERIFIED | No names selected | Current field behavior not audited | PACKAGING_ONLY | Editorial Manager metadata | Submission | NO | YES | INFO |
| A29 | Author metadata | Names, affiliations, country, email, corresponding author, ORCID | HARD_REQUIREMENT | S1/S2 | PARTIAL/BLOCKED | UNVERIFIED | No author metadata artifact in repository | Personal data must be supplied later | PACKAGING_ONLY | Editorial Manager/title page | Submission | NO | YES | INFO |
| A30 | Submission metadata | Title, abstract, keywords, declarations, funding, data, comments | HARD_REQUIREMENT | S1/S2 | PARTIAL/BLOCKED | UNVERIFIED | Article type is verified; other fields not exhaustively inspected | Current field set unknown | PACKAGING_ONLY | Editorial Manager forms | Submission | NO | YES | INFO |
| A31 | Classifications | Subject areas/categories in Editorial Manager | CONDITIONAL | S1/S2 | PARTIAL/BLOCKED | UNVERIFIED | No selections made | Field/options unknown | PACKAGING_ONLY | Editorial Manager classification | Submission | NO | YES | INFO |
| A32 | File categories | Manuscript/title page/figures/supplement/declarations categories | CONDITIONAL | S1/S2 | PARTIAL/BLOCKED | UNVERIFIED | No upload package created | Category names unknown | PACKAGING_ONLY | Upload metadata | Packaging | NO | YES | INFO |
| A33 | Preprint | Prior dissemination and disclosure policy | CONDITIONAL | S2/S4 | BLOCKED | UNVERIFIED | No preprint decision recorded in MS-R04 | Verify only if applicable | PACKAGING_ONLY | Submission disclosure | Packaging | NO | YES | INFO |
| A34 | Copyright/OA | Copyright, license, and open-access timing/options | CONDITIONAL | S2/S4 | BLOCKED | UNVERIFIED | No OA choice made | Do not choose in this audit | PACKAGING_ONLY | Submission/license forms | Packaging | NO | YES | INFO |
| A35 | Templates | Word/LaTeX template required/recommended/optional | RECOMMENDED | S2 | BLOCKED | UNVERIFIED | Chinese Markdown source; no template conversion | Current template rule unknown | UNVERIFIED | English source format | SUB-A02 follow-up | NO | YES | INFO |
| A36 | Language quality | English submission and language quality expectations | HARD_REQUIREMENT | S2/S3 | BLOCKED | PARTIALLY_VERIFIED | Chinese semantic source is accepted; English manuscript pending | Translation and language QA required | ENGLISH_TRANSLATION_STAGE | English manuscript | Translation | NO | YES | E2 |

### Requirement-count summary

```text
TOTAL_ATOMIC_REQUIREMENTS = 36
VERIFIED_REQUIREMENT_COUNT = 3
PARTIALLY_VERIFIED_REQUIREMENT_COUNT = 5
UNVERIFIED_REQUIREMENT_COUNT = 28

HARD_REQUIREMENT_COUNT = 11
RECOMMENDED_REQUIREMENT_COUNT = 6
OPTIONAL_REQUIREMENT_COUNT = 4
CONDITIONAL_REQUIREMENT_COUNT = 11
NOT_APPLICABLE_REQUIREMENT_COUNT = 1
UNVERIFIED_STRENGTH_COUNT = 3

NO_CHANGE_COUNT = 1
PACKAGING_ONLY_COUNT = 27
ENGLISH_TRANSLATION_STAGE_COUNT = 4
POTENTIAL_MS_R05_COUNT = 0
UNVERIFIED_ACTION_COUNT = 4
```

## 8. Submission-artifact matrix

| Artifact ID | Artifact name | Required status | Source | Current state | Source asset | Work needed | Action class | Dependency | Future task |
|---|---|---|---|---|---|---|---|---|---|
| JSS-A01 | Main manuscript | REQUIRED for route | S1/S2 | Chinese MS-R04 only | AS-M01/AS-M02 | English translation and journal formatting | ENGLISH_TRANSLATION_STAGE | Semantic-source freeze | Translation stage |
| JSS-A02 | Title page | UNVERIFIED | S2 | Not created | Author metadata | Build if guide/UI requires separate file | PACKAGING_ONLY | Author information | Submission packaging |
| JSS-A03 | Highlights | UNVERIFIED | S2 | Not created | None | Build only if required | PACKAGING_ONLY | Exact JSS rule | Submission packaging |
| JSS-A04 | Graphical abstract | UNVERIFIED | S2 | Not created | Accepted figures are not a graphical abstract | Build only if required | PACKAGING_ONLY | Exact JSS rule | Submission packaging |
| JSS-A05 | Figures | REQUIRED upload set; details unverified | S2 | V6/V6-E01 accepted renders | AS-M04/AS-M05 | Export/upload per verified JSS rules | PACKAGING_ONLY | Figure guide | Submission packaging |
| JSS-A06 | Tables | REQUIRED within manuscript or upload; details unverified | S2 | 14 editable table blocks | AS-M01 | Preserve/editable source during translation | PACKAGING_ONLY | Source-file rule | Translation/packaging |
| JSS-A07 | Supplementary material | CONDITIONAL | S2 | P0-v3 supplemental package exists | AS-M07 | Map files and in-text links if accepted | PACKAGING_ONLY | Supplement policy | Submission packaging |
| JSS-A08 | Data Availability Statement | RECOMMENDED/possibly required | S2/S4 | §7 has Zenodo DOI and scope caveat | AS-M08/AS-M01 | Finalize statement and version mapping | PACKAGING_ONLY | Data freeze | Packaging |
| JSS-A09 | Code/software statement | UNVERIFIED | S2/S4 | §7 explicitly limits code-release claim | AS-M01 | State actual public scope and exceptions | PACKAGING_ONLY | Code inventory | Packaging |
| JSS-A10 | CRediT statement | RECOMMENDED/possibly required | S4 | Not created | Author records | Draft author-confirmed taxonomy | PACKAGING_ONLY | Author confirmation | Packaging |
| JSS-A11 | Funding declaration | CONDITIONAL | S2/S4 | Not created | Author records | Obtain factual declaration | PACKAGING_ONLY | Author confirmation | Packaging |
| JSS-A12 | Declaration of interests | REQUIRED/conditional detail unverified | S2/S4 | Not created | Author records | Obtain factual statement and location | PACKAGING_ONLY | Author confirmation | Packaging |
| JSS-A13 | AI-use declaration | Current policy unverified | S4/S2 | Not created | Author workflow record | Determine whether disclosure applies; do not infer | PACKAGING_ONLY | Policy and author record | Packaging |
| JSS-A14 | Cover letter | UNVERIFIED/recommended | S2/S3 | Not created | None | Draft after requirement mapping | PACKAGING_ONLY | Target package | Packaging |
| JSS-A15 | Author metadata | REQUIRED submission metadata | S1/S2 | Not recorded in repository | Author records | Enter names, affiliations, email, corresponding author, ORCID if applicable | PACKAGING_ONLY | Author confirmation | Submission |
| JSS-A16 | Keywords | REQUIRED/limit unverified | S1/S2 | Seven keywords in MS-R04 | AS-M01 | Translate and adapt count if required | ENGLISH_TRANSLATION_STAGE | English manuscript | Translation |
| JSS-A17 | Research-data repository link | RECOMMENDED/possibly required | S2/S4 | Zenodo DOI exists | AS-M08 | Verify final release/version mapping | PACKAGING_ONLY | Final package | Packaging |
| JSS-A18 | Replication package | CONDITIONAL | Project authority/S2 | Supplemental P0-v3 package exists | AS-M07 | Map package to submission and release scope | PACKAGING_ONLY | Data/code policy | Packaging |
| JSS-A19 | Reviewer metadata | CONDITIONAL | S1/S2 | No reviewer names selected | None | Fill only if current EM asks | PACKAGING_ONLY | Live form | Submission |
| JSS-A20 | Other JSS-specific artifact | UNVERIFIED | S2 | No other artifact established | None | Recheck guide/UI in SUB-A02 closure | UNVERIFIED | Official guide access | SUB-A02 follow-up |

## 9. JSS-specific manuscript checks

The accepted source already contains a title, abstract, keywords, Introduction,
Related Work, Methods, Results, Discussion, Threats to Validity, data/code
availability, supplement explanation, Conclusion, Appendix A, tables, figure
captions, and references. The current source is semantically complete for the
frozen paper centre and observation contracts. No verified JSS rule was found
that requires a new scientific section, RQ, contribution, result, metric, or
semantic contract.

The following remain translation or packaging work: English title and abstract,
English keywords, journal-facing section wording, title-page metadata,
declarations, figure/table source mapping, and upload categories. Exact JSS
limits and formatting must be checked when S2 becomes accessible or at live
submission; they are not guessed here.

## 10. Translation-stage requirements

```text
ENGLISH_TITLE = REQUIRED_FOR_ENGLISH_SUBMISSION; semantic content exists
ENGLISH_ABSTRACT = REQUIRED_FOR_ENGLISH_SUBMISSION; 297-character Chinese source exists; 0 citations
ENGLISH_KEYWORDS = REQUIRED_FOR_ENGLISH_SUBMISSION; 7 source keywords exist
ENGLISH_MAIN_TEXT = REQUIRED_FOR_ENGLISH_SUBMISSION; all five RQs and four contributions preserved
ENGLISH_FIGURE_TABLE_CAPTIONS = REQUIRED_IF_SUBMISSION_LANGUAGE_REQUIRES; captions already semantically present
LANGUAGE_QA = REQUIRED_AS_SUBMISSION_QUALITY; no Chinese-source edit implied
```

These are `ENGLISH_TRANSLATION_STAGE`, not MS-R05 semantic gaps.

## 11. Packaging-only requirements

Title page, author metadata, Editorial Manager fields, declarations, CRediT,
funding, competing interests, AI-use record, cover letter, highlights,
graphical abstract if required, figure/table file separation, supplement
uploads, repository links, reference formatting, and reviewer/classification
fields are outside the Chinese semantic source. They remain future packaging
work even where the exact current JSS rule is unverified.

## 12. Potential MS-R05 audit

```text
POTENTIAL_MS_R05_COUNT = 0
```

Gate review:

```text
G1_VERIFIED_CURRENT_REQUIREMENT = NO_ITEM_PASSES_ALL_GATES
G2_SEMANTIC_CONTENT_MISSING = NO
G3_NOT_SOLVABLE_BY_TRANSLATION = NO
G4_NOT_SOLVABLE_BY_PACKAGING = NO
```

No item satisfies all four conditions. In particular, no MS-R05 is justified
for English wording, abstract limits, keywords, references, title page,
CRediT, declarations, AI disclosure, cover letter, highlights, graphical
abstract, metadata, file conversion, or figure export.

```text
MS_R05_REQUIRED = NO
```

## 13. Unverified requirements

The following remain explicitly unverified because the current official JSS
Guide/journal page could not be reliably parsed: source-file format, word/page
limits, abstract/keyword limits, section prescriptions, review model,
highlights, graphical abstract, figure/table specifications, reference style,
supplement rules, code policy, Open Science/badges, funding/interests/AI
placement, cover letter, reviewer/classification fields, upload categories,
preprint/OA rules, and template requirements. These are not blockers for the
Chinese semantic-source decision. SUB-A02 records them for later closure and
does not convert them into manuscript edits.

## 14. Data, code, and reproducibility mapping

```text
ZENODO_DOI = 10.5281/zenodo.18817348
P0V3_OUTPUT_ROOT = outputs/reference_quotient_p0_corrected_v3/
SUPPLEMENTAL_P0V3_ROOT = supplemental/reference_quotient_v2/outputs_p0v3/
SUPPLEMENTAL_MANIFEST_SHA = 78d07fbda2a045ba309a1cfcb23a68ca2baafa910008b6483c0c4e0acf9211bd
```

The public relation/data release is distinct from the final-submission
replication package. The DOI does not imply blanket publication of the full
GH_CoRE codebase. Section 7 and Appendix A already state the public scope,
platform/rights caveats, processed/derived-output provenance, and
source-incomplete target observation boundary. Final release/version matching
is packaging work.

## 15. Figures, tables, and references mapping

```text
FIGURE_1_3_AUTHORITY = figures/ch5_refq/p0v3_final_v6
FIGURE_4_AUTHORITY = figures/ch5_refq/p0v3_final_v6_e01_eta_label
FIGURE_CAPTION_COUNT = 4
MAIN_TEXT_TABLE_BLOCK_COUNT = 14
CITATION_TOKEN_COUNT = 70
UNIQUE_CITATION_KEY_COUNT = 33
BIBLIOGRAPHY_ENTRY_COUNT = 33
```

No figure rerender, table redesign, or bibliography reformat is authorized in
this audit. Exact JSS file formats, resolution, placement, and initial-
submission reference style remain unverified until the official guide is
available.

## 16. Declarations and author-metadata mapping

No author-specific factual declarations are invented. The future package must
obtain, as applicable, author names, affiliations, country, email,
corresponding-author designation, ORCID, authorship confirmation, CRediT,
funding, competing interests, AI-use disclosure, permissions, ethics response,
acknowledgements, and reviewer/classification metadata. These are packaging or
submission-system actions, not Chinese semantic-source edits.

The repository-mining design does not itself trigger human-subject or informed-
consent semantics; any journal form requiring an applicability response should
be completed from the actual study design and author confirmation.

## 17. Translation-readiness gate

```text
SEMANTIC_SOURCE_READY_FOR_ENGLISH_TRANSLATION = YES
PACKAGING_CAN_PROCEED_AFTER_TRANSLATION = YES
```

The gate is YES because no MS-R05 semantic revision is required and no
submission-critical verified semantic requirement is missing. Packaging-only
artifacts may remain outstanding.

## 18. MS-R05 decision

```text
MS_R05_REQUIRED = NO
MS_R05_DECISION = DEFER; NO_BOUNDED_EDIT_PLAN_REQUIRED
```

The next manuscript-related work is not an automatic MS-R05. It is a final
Chinese semantic-source freeze check followed by the separately authorized
English translation and JSS packaging stages.

## 19. No-change guards

```text
CURRENT_CHANGED = 0
MS_R04_SNAPSHOT_CHANGED = 0
MS_R03_SNAPSHOT_CHANGED = 0
MS_R02_SNAPSHOT_CHANGED = 0
MS_R01_SNAPSHOT_CHANGED = 0
CANDIDATE_CHANGED = 0
SIDECAR_CHANGED = 0
MANUSCRIPT_VERSION_MANIFEST_CHANGED = 0
TARGET_VENUE_FREEZE_DOCUMENT_CHANGED = 0
MANUSCRIPT_TEXT_CHANGED = 0
TITLE_CHANGED = 0
ABSTRACT_CHANGED = 0
KEYWORDS_CHANGED = 0
RQ_TEXT_CHANGED = 0
CONTRIBUTION_TEXT_CHANGED = 0
SCIENTIFIC_VALUE_CHANGED = 0
UNDERLYING_NUMERIC_VALUE_CHANGE_COUNT = 0
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
FIGURE_ASSETS_CHANGED = 0
FIGURE_RERENDER = 0
TABLE_CONTENT_CHANGED = 0
TABLE_RELOCATION_COUNT = 0
CITATION_STATE_CHANGED = 0
BIBLIOGRAPHY_CHANGED = 0
OTHER_TRACKED_FILE_CHANGE_COUNT = 0

E0_COUNT = 0
E1_COUNT = 0
E2_COUNT = 7
INFO_COUNT = 29
```

## 20. Next-task decision

```text
NEXT_TASK = CH5_REFQ_FINAL_CHINESE_SEMANTIC_SOURCE_FREEZE
```

After that freeze, the JSS English translation and packaging workflow may
proceed. The JSS-specific requirement closure recorded here remains the input
to later submission preparation; no English text or artifact is created here.

## 21. Final decision

```text
DECISION = CH5_REFQ_SUB_A02_PASS_NO_MS_R05_REQUIRED
VERIFIED_AS_OF = 2026-09-22
```
