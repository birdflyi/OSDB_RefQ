# Chapter 5 RefQ Target-Venue Freeze: JSS Research Paper

## Decision

`CH5_REFQ_TARGET_VENUE_FREEZE_JSS_RESEARCH_PAPER_PASS`

This is a read-only venue-decision freeze and metadata documentation record.
It does not perform journal-specific manuscript preparation.

## 1. Task and repository authority

```text
TASK = CH5_REFQ_TARGET_VENUE_FREEZE_JSS_RESEARCH_PAPER
TASK_MODE = READ_ONLY_VENUE_DECISION_FREEZE
REPOSITORY = D:/github_repo/OSDB_RefQ
BRANCH = ch5-refq-repository-identity-correction-v1
TASK_BASE_REPOSITORY_HEAD = 56defd6fcb52e2cc725d64fd288cf55629c9447c
```

The task started with local and remote HEAD equal to the required base and no
ahead/behind divergence. The pre-existing V3-V6 figure ZIP files remain
untracked and untouched.

## 2. Accepted MS-R04 authority

```text
TASK_BASE_REVISION = MS-R04
TASK_BASE_SHA = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
SCIENTIFIC_BASELINE = P0-v3
STAGE = OBSERVATION_FRAMING_ACCEPTED

CURRENT_SHA = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
MS_R04_SNAPSHOT_SHA = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
CURRENT_EQUALS_MS_R04_SNAPSHOT = YES
CURRENT_PATH = C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_CURRENT.md
MS_R04_SNAPSHOT = versions/MS-R04_POST_OBSERVATION_FRAMING_F8071504.md
```

The accepted manuscript, candidate, and snapshot are not changed by this
freeze. MS-R03 remains an immutable historical accepted revision.

## 3. Current-version and promotion authority

```text
MANUSCRIPT_REVISION = MS-R04
ACCEPTED_MANUSCRIPT_SHA = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
REPOSITORY_AUDIT_HEAD = 0bc8e04adace4934216208f5271f149b8ab0605f
CURRENT_ACCEPTED_SNAPSHOT = versions/MS-R04_POST_OBSERVATION_FRAMING_F8071504.md
MS_R03_ROLE = HISTORICAL_ACCEPTED_SNAPSHOT

P1_PROMOTION_COMMIT = 0bc8e04adace4934216208f5271f149b8ab0605f
P2_PROVENANCE_REGISTRATION_COMMIT = 6c54e4568a0341e0057bfc26c226bde0317604d4
METADATA_REPAIR_COMMIT = 56defd6fcb52e2cc725d64fd288cf55629c9447c
```

P1 remains the acceptance-decision audit commit; P2 and the metadata repair
are provenance/documentation successors.

## 4. Prior venue-decision authority

The prior comparative audit
`docs/submission_suggestion/ch5_refq_sub_a01_jss_vs_emse_target_venue_audit_2026-09-21.md`
is authoritative for the venue ranking:

```text
DECISION = CH5_REFQ_SUB_A01_PASS_RECOMMEND_JSS
PRIMARY_RECOMMENDATION = JSS
PRIMARY_ROUTE = JSS_REGULAR_ARTICLE
BACKUP = EMSE
```

The MS-R04 observation-framing revision closed bounded semantic-source gaps;
it did not change the JSS-versus-EMSE ranking.

## 5. Current paper characterization

```text
PAPER_CHARACTERIZATION = empirical software engineering study;
project-level explicit-reference relation operationalization;
observation-aware structural measurement;
reproducible empirical relation asset
```

Core positioning:

> RefQ provides a traceable and observation-aware operationalization of
> project-level explicit-reference structure.

Methodological chain:

```text
fine-grained explicit Reference evidence
-> endpoint eligibility
-> semantic membership
-> aggregation
-> RefQ / RefQN
-> asymmetric source observation
-> role-aware measurement
-> empirical characterization
-> bounded interpretation
```

The empirical setting is 294 open-source DBMS analysis seed projects on GitHub
in the 2023 observation window, using a seed-centered project-level RefQN.
RQ2a uses the source-complete seed population; RQ2b uses the observable target
population; RQ2c uses a first-order direction-ignored derived structural view.
The current meta-finding is that explicit-reference structure is measurable,
but interpretation is role-dependent, observation-bounded, and
metric-dependent. RQ3 conclusions are additionally sensitive to label
operationalization.

RefQ is not presented as a generic knowledge-flow, dependency, causal,
task-resolution, or fully observed OSS-ecosystem ground truth.

## 6. Frozen target journal

```text
TARGET_JOURNAL = Journal of Systems and Software
ABBREVIATION = JSS
PUBLISHER = Elsevier
ISSN = 0164-1212
PRIMARY_TARGET_STATUS = FROZEN
```

## 7. Direct Editorial Manager article-type evidence

The author directly inspected the currently accessible JSS Editorial Manager
submission interface. The observed selector was:

```html
<select name="ddlArticleType" id="ddlArticleType" aria-labelledby="acrdHeaderText">
  <option selected="selected" value="1">Research Paper</option>
  <option value="185">Review Article</option>
  <option value="131">In Practice</option>
  <option value="172">Trends - Long Article</option>
  <option value="173">Trends - Short Article</option>
  <option value="203">VSI:AI4MSS</option>
  <option value="206">VSI:AST 2026 Selected Papers</option>
  <option value="205">VSI:ECSA2026</option>
  <option value="207">VSI: Trustworthy SE&amp;Adv. Apps</option>
</select>
```

The semantic article-type identity is the visible label, not the internal HTML
value:

```text
TARGET_TRACK = RESEARCH_PAPER
EDITORIAL_MANAGER_EXACT_ARTICLE_TYPE_LABEL = Research Paper
EDITORIAL_MANAGER_EXACT_ARTICLE_TYPE_LABEL_VERIFIED = YES
EDITORIAL_MANAGER_ARTICLE_TYPE_VALUE_OBSERVED = 1
SUBMISSION_ROUTE = standard JSS Research Paper submission
```

The numeric value `1` is retained only as current interface provenance and is
not treated as a permanent semantic identifier.

## 8. Excluded article types and special tracks

```text
RESEARCH_PAPER_SELECTED_AS_TARGET = YES
SPECIAL_TRACK_SELECTED = NO
SPECIAL_ISSUE_SELECTED = NO
VSI_SELECTED = NO
```

The manuscript is not frozen to Review Article, In Practice, Trends - Long
Article, Trends - Short Article, or any displayed VSI route. The Editorial
Manager special-issue instruction is therefore recorded as a boundary, not as
a current route selection. A materially relevant future special issue may be
evaluated separately before actual submission.

## 9. Compact JSS fit rationale

JSS is the primary target because the paper combines empirical software
engineering, open-source software development, repository-derived evidence,
project-level relation construction, metrics and structural evaluation, and
software-ecosystem analysis. The DBMS domain is a bounded empirical vertical,
not the sole identity of the contribution.

The contribution form is:

1. traceable project-level operationalization of explicit Reference evidence;
2. explicit endpoint, membership, aggregation, and observation contracts;
3. observation-aware role-specific structural measurement;
4. bounded empirical knowledge about source roles, target roles, first-order
   organization, and subdomain sensitivity;
5. a reproducible weak-semantic project-level relation asset.

This remains four manuscript contributions, not a fifth platform contribution.
The paper contains explicit sampling, RefQ construction, source-admission and
membership contracts, role separation, structural analysis, sensitivity and
robustness checks, Threats to Validity, and provenance records. Bounded or
negative findings, including Louvain sensitivity, RQ3 label-mode sensitivity,
zero cross-mode robust RQ3 features, and expanded-target source incompleteness,
remain valid empirical knowledge.

## 10. MS-R04 framing status

```text
RELATED_WORK_OBSERVATION_BRIDGE = SUFFICIENT
INTRO_OBSERVATION_PROBLEM = EXPLICIT
DISCUSSION_MEASUREMENT_VALIDITY_SYNTHESIS = SUFFICIENT
OBSERVATION_NETWORK_BOUNDARY_VALIDITY = SUFFICIENT
CONCLUSION_MEASUREMENT_CONDITION_CLOSURE = SUFFICIENT
LITERATURE_POSITIONING = COMPLEMENTARY_CRITICAL
ADVERSARIAL_PRIOR_WORK_CLAIM_COUNT = 0
```

MS-R04 closed the previously identified Related Work and observation/network-
boundary framing gaps. The target freeze introduces no manuscript gap.

## 11. Backup journal

```text
BACKUP_JOURNAL = Empirical Software Engineering
BACKUP_JOURNAL_ABBREVIATION = EMSE
BACKUP_STATUS = BACKUP_ONLY
```

The JSS/EMSE ranking is not reopened here.

## 12. Manuscript-change and MS-R05 gate

```text
TARGET_FREEZE_REQUIRES_MANUSCRIPT_CHANGE = NO
MS_R05_REQUIRED_BY_TARGET_FREEZE = NO
ARTICLE_TYPE_LABEL_VERIFICATION_PENDING = NO

EDITORIAL_COMPLETE = YES
VENUE_INDEPENDENT_CONDENSATION_COMPLETE = YES
OBSERVATION_FRAMING_COMPLETE = YES
JOURNAL_SPECIFIC_PREPARATION_PENDING = YES
FINAL_ENGLISH_ABSTRACT_PENDING = YES
FINAL_SUBMISSION_READY = NO
MS_R05_DECISION = DEFER_TO_SUB_A02_REQUIREMENTS_MAPPING
```

Selecting JSS/Research Paper is a venue and submission-route decision, not a
semantic manuscript revision. No MS-R05 is created by this freeze.

## 13. Public-source verification record

Public sources were used only for broad journal identity, scope, and route
context. The exact current article-type label is controlled by the direct
Editorial Manager inspection above.

| Source title | URL | Access date | Claim supported |
|---|---|---|---|
| JSS Editorial Manager | https://www.editorialmanager.com/jssoftware/ | 2026-09-22 | Official submission-system entry; current interface is reachable. |
| Journal of Systems and Software, ScienceDirect journal page | https://www.sciencedirect.com/journal/journal-of-systems-and-software | 2026-09-22 | Official journal identity and publisher context; direct automated access was restricted in this environment. |
| JSS Guide for Authors | https://www.elsevier.com/journals/journal-of-systems-and-software/0164-1212/guide-for-authors | 2026-09-22 | Official author-guideline URL; detailed requirements remain for SUB-A02 because direct access was restricted. |
| SUB-A01 comparative venue audit | `docs/submission_suggestion/ch5_refq_sub_a01_jss_vs_emse_target_venue_audit_2026-09-21.md` | 2026-09-22 | Prior JSS recommendation, EMSE backup, and evidence boundary. |

No unavailable author-guideline detail is presented as verified in this
freeze. Detailed requirement mapping is deferred to SUB-A02.

## 14. No-change guards

```text
CURRENT_CHANGED = 0
MS_R04_SNAPSHOT_CHANGED = 0
MS_R03_SNAPSHOT_CHANGED = 0
MS_R02_SNAPSHOT_CHANGED = 0
MS_R01_SNAPSHOT_CHANGED = 0
CANDIDATE_CHANGED = 0
SIDECAR_CHANGED = 0
MANUSCRIPT_VERSION_MANIFEST_CHANGED = 0
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
```

## 15. Next-task contract

```text
NEXT_TASK = CH5_REFQ_SUB_A02_JSS_AUTHOR_GUIDELINE_AND_ARTIFACT_MAPPING
```

SUB-A02 must map current JSS Research Paper requirements for article type,
structure, title page, abstract, keywords, limits, highlights, graphical
abstract, source files, figures, tables, references, supplements, data/code,
Data Availability, Open Science, CRediT, funding, competing interests,
generative-AI declaration, ethics/declarations, cover letter, review model,
author metadata, and submission-system fields. Each item must be classified
as `NO_CHANGE`, `PACKAGING_ONLY`, `ENGLISH_TRANSLATION_STAGE`,
`POTENTIAL_MS_R05`, or `UNVERIFIED`. SUB-A02 must not automatically edit the
manuscript.

## 16. Final freeze state

```text
TARGET_JOURNAL = Journal of Systems and Software
TARGET_TRACK = RESEARCH_PAPER
PRIMARY_TARGET_STATUS = FROZEN
RESEARCH_PAPER_SELECTED_AS_TARGET = YES
SPECIAL_TRACK_SELECTED = NO
SPECIAL_ISSUE_SELECTED = NO
VSI_SELECTED = NO
TARGET_FREEZE_REQUIRES_MANUSCRIPT_CHANGE = NO
MS_R05_REQUIRED_BY_TARGET_FREEZE = NO
ARTICLE_TYPE_LABEL_VERIFICATION_PENDING = NO
FREEZE_COMMIT = METADATA_ONLY_SUCCESSOR_NOT_SELF_REFERENCED
```

