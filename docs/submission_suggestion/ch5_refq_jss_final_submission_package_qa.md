# Chapter 5 RefQ JSS Final Submission Package QA

```text
TASK = CH5_REFQ_JSS_FINAL_SUBMISSION_PACKAGE_QA
MODE = FINAL_PRIVATE_PACKAGE_ASSEMBLY_AND_OFFLINE_QA
TASK_BASE_REPOSITORY_HEAD = 0fa1127b179116cc58ea77cff749cd81bcc92b14
```

## Authority and protection checks

```text
MS_R05_SHA_CHECK = PASS
MS_R05_SHA = 30491279BC31CC5012042F72E3BA8159DCF182CECEEB62EFF5C865C78B059B22
EN_R03_SHA_CHECK = PASS
EN_R03_SHA = B61683132DCAD3B6BB4D5ACCA4B49AE4FCAB0CC0B9A2D57FFCC06CF359AFBFE4
P0_MAIN_DERIVATIVE_SHA_CHECK = PASS
P0_MAIN_DERIVATIVE_SHA = D75409CFE976EB04DA7B192DCD9C064B559A56D7699B03512A65E27ADC08A080
JSS_GUIDE_SHA_CHECK = PASS
JSS_GUIDE_SHA = FB0DF4849E71A4531E22EED7B43034ACA53BD6CDED215AD469CA9BD0CA5E16D3
```

The semantic authorities and P0 derivative were not modified. The private
package was assembled outside the repository.

The P1 main-manuscript packaging derivative is the bounded final upload source:

```text
P1_MAIN_MANUSCRIPT_SHA = 597CCE7A9B2417901F3C14BC64822A93A650C73AC6591004A7CB4D86405F3E87
P1_MAIN_MANUSCRIPT_SIZE_BYTES = 125499
P1_ASSEMBLY_SCOPE = §7 Data/Code Availability replacement + confirmed declarations before References
P1_SEMANTIC_RISK_CHANGE_COUNT = 0
P1_SCIENTIFIC_RESULT_SENTENCE_CHANGE_COUNT = 0
P1_METHOD_SENTENCE_CHANGE_COUNT = 0
P1_RQ_CHANGE_COUNT = 0
P1_CONTRIBUTION_CHANGE_COUNT = 0
```

The P1 control records were refreshed after assembly and their payload rows
match the private package byte-for-byte:

```text
JSS_UPLOAD_SET_SHA = 8956A9A42A506382E8DC5F38FBFF5F718677F8CABE233ECA68A75B58A1387AD5
JSS_FINAL_PACKAGE_TREE_SHA = D230D0E60F92718CAC1F3EDDBE4E061690A5B1A3E69420E172F8438E48425C7A
MANIFEST_PAYLOAD_CLOSURE = PASS
```

## Package QA

```text
GRAPHICAL_ABSTRACT_VERSION = V1.1
GRAPHICAL_ABSTRACT_SHA_CHECK = PASS
GRAPHICAL_ABSTRACT_SHA = 5BEEE20ACCC765F15BCA7A374493CA320672553F603575CDF4E8C129C576EA33
GRAPHICAL_ABSTRACT_QA = PASS
GRAPHICAL_ABSTRACT_CONTENT_CHANGE = 0
HISTORICAL_V1_0_IN_UPLOAD_SET = NO

HIGHLIGHTS_BULLET_COUNT = 4
HIGHLIGHTS_CHAR_LIMIT_CHECK = PASS (all <=85 characters)
TITLE_PAGE_CHECK = PASS
DECLARATIONS_CHECK = PASS (confirmed offline reference copy; live placement check remains)
FUNDING_CHECK = PASS
CREDIT_CHECK = PASS
COMPETING_INTEREST_CHECK = PASS
DATA_AVAILABILITY_CHECK = PASS (scope-limited Zenodo statement)
CODE_AVAILABILITY_CHECK = PASS (public constituent repositories; no monolithic bundle claim)
AI_DECLARATION_CHECK = PASS
ETHICS_CHECK = PASS
PUBLICATION_STATUS_CHECK = PASS (NO / NO / NO)

SCIENTIFIC_FIGURE_COUNT = 4
SCIENTIFIC_FIGURE_HASH_CHECK = PASS
SUPPLEMENTARY_PACKAGE_CHECK = PASS (26 S1-S4 payload files; internal stage receipts excluded from upload set)
COVER_LETTER_STATUS = PREPARED; LIVE_REQUIREMENT_CHECK_PENDING
```

The four accepted scientific figure PDFs are byte-identical copies of the
frozen V6/V6-E01 authorities. No figure was rendered, converted, or edited.
The graphical abstract is the accepted V1.1 packaging authority. The upload
set excludes historical graphical-abstract V1.0 files, prompts, internal
receipts, private metadata working files, and V3-V6 repository ZIP archives.

## Semantic and numeric invariants

```text
RQ_COUNT = 5
CONTRIBUTION_COUNT = 4
CITATION_KEYS = 33 / 33
DISPLAY_FORMULAS = 12 / 12
SCIENTIFIC_VALUE_CHANGE = 0
FORMULA_SEMANTIC_CHANGE = 0
CITATION_KEY_SET_CHANGE = 0
OBSERVATION_SEMANTIC_DRIFT = 0
CLAIM_STRENGTHENING = 0
SOURCE_COMPLETE_SEEDS_PRESERVED = YES
SOURCE_INCOMPLETE_EXPANDED_TARGETS_PRESERVED = YES
MISSING_AS_ZERO_DRIFT = 0
FIRST_SECOND_ORDER_DRIFT = 0
KNOWLEDGE_FLOW_MEASURE_CLAIM = 0
DEPENDENCY_GROUND_TRUTH_CLAIM = 0
PROJECT_IMPORTANCE_CLAIM = 0
CAUSAL_DRIFT = 0
UNQUALIFIED_OSS_GENERALIZATION = 0
```

The private P1 main manuscript is a bounded packaging assembly from the P0
derivative. Its only changes are (1) replacing the provisional Data/Code
Availability text in Section 7 with the author-confirmed P2 statements, and (2)
inserting the confirmed Funding, competing-interest, CRediT, and generative-AI
declarations before References. Those statements are reproduced from the
confirmed declaration source; no scientific or method prose was changed. The
separate declaration file is retained as an internal reference copy and is not
in the upload set. Current P1 main-manuscript SHA-256 is
`597CCE7A9B2417901F3C14BC64822A93A650C73AC6591004A7CB4D86405F3E87` (125,499
bytes). Package controls were refreshed to this assembled artifact before the
offline gate was closed.

## Independent gates

```text
SEMANTIC_GATE = PASS
OFFLINE_PACKAGE_GATE = PASS
REQUIREMENT_COMPLETENESS_GATE = PASS
LIVE_SYSTEM_GATE = PENDING
OFFLINE_SUBMISSION_PACKAGE_READY = YES
READY_FOR_LIVE_EDITORIAL_MANAGER_ENTRY = YES
```

The remaining live checks are the exact article-type label, account/address
fields, ORCID linking, declaration and data-link controls, optional/recommended
cover-letter handling, suggested-reviewer request, upload categories, open-
access choice, and generated-PDF preview. No Editorial Manager submission was
made and no final approval button was clicked.

## Private package records

The complete package, manifests, tree, and live checklist are maintained in the
private submission workspace under `EN-R03_P1_FINAL_QA`. They are intentionally
not committed to the public repository. This public audit records only the
offline gate and provenance result.

```text
DECISION = CH5_REFQ_JSS_FINAL_SUBMISSION_PACKAGE_QA_PASS_READY_FOR_LIVE_EDITORIAL_MANAGER_ENTRY
NEXT_TASK = CH5_REFQ_JSS_LIVE_EDITORIAL_MANAGER_ENTRY_QA
```
