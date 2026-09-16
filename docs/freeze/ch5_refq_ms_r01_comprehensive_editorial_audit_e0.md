# Chapter 5 RefQ MS-R01 Comprehensive Editorial Completion Audit (E0)

## Decision

`CH5_REFQ_MS_R01_EDITORIAL_AUDIT_E0_PASS_READY_FOR_EDITORIAL_CONVERGENCE`

This is a read-only audit of the externally maintained MS-R01 manuscript.
No manuscript, snapshot, sidecar, manifest, figure, table, scientific output,
or analysis code was changed. The result is ready for bounded editorial
convergence; it is not an authorization to create MS-R02 in this audit.

## 1. Identity, scope, and immutability

| Item | Result |
|---|---|
| Repository | `D:/github_repo/OSDB_RefQ` |
| Branch | `ch5-refq-repository-identity-correction-v1` |
| Repository HEAD before E0 | `46bb214dfabca49a50caa8ca0542df6e931193b4` |
| Remote HEAD before E0 | `46bb214dfabca49a50caa8ca0542df6e931193b4` |
| Manuscript CURRENT | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_CURRENT.md` |
| Accepted snapshot | `versions/MS-R01_POST_G1_CF488538.md` |
| CURRENT SHA-256 | `CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE` |
| Snapshot SHA-256 | `CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE` |
| Size/encoding | 114,716 bytes; LF; no BOM; final LF present |
| CURRENT = snapshot | `YES` |
| MS-R02/SUB-A01 created | `NO` |
| Existing untracked files | only `p0v3_final_v3.zip` through `p0v3_final_v6.zip` |

The identity sidecar and version manifest were read-only and unchanged. Their
recorded manuscript SHA remains the value above. The sidecar's historical
`repo_head` is the post-G1 acceptance head and is not rewritten by E0.

## 2. Scientific and structural closure

The accepted P0-v3 contracts close without recomputation:

* 301 candidates -> 294 analysis seeds -> 7 unavailable frozen-2023 evidence
  exclusions.
* 3,748,078 scanned Reference records - 120 out-of-seed = 3,747,958 admitted.
* Admitted partition: 1,586,047 project-mappable/quotient-eligible,
  1,686,729 non-project, and 475,182 unresolved.
* RefQN domain: 6,506 nodes (6,505 edge-observed, one zero-edge), 9,884
  directed edges including 289 self-loops, 9,595 cross-project directed
  edges, cross-project weight 138,974, 9,547 first-order undirected edges,
  55 components, 30 isolates, and an LCC of 6,367 nodes/9,462 undirected
  edges (9,510 directed sensitivity edges).

Source-complete seeds, source-incomplete expanded targets, strict source
admission, unique-membership quotient eligibility, unit-weight evidence,
`Q = M^T R_P M`, self-loop handling, and first-order versus second-order
boundaries are stated consistently. The five RQs remain `RQ1`, `RQ2a`,
`RQ2b`, `RQ2c`, and `RQ3`; the four ordered contributions remain unchanged.

RQ1 terminology is closed: `active_issue_pr_count` means Reference-bearing
Issue/PR contexts; `comment_per_issue` uses unique source entities over those
contexts; `comment_reference_density` is Reference rows per unique source
entity; `external_reference_share` is the complete non-self share; and
`non_project_reference_share` is its non-project component. Network settings
remain weighted Louvain (seed 20260731), unweighted local clustering,
unweighted approximate betweenness (`k=500`, seed 20260731,
`normalized=True`). RQ3 retains minimum eligible group size 5, the two label
modes, within-mode feature-level BH-FDR, and zero cross-mode robust features.

Figures 1--4 and Tables 4.1--4.8 (including 4.6a--4.6f) are present and
numbered once. Figure/table denominators and units are consistent; no edge
count, evidence-weight, record-count, entity-count, or semantic-community
substitution was found.

## 3. Literature authenticity matrix

All 31 unique citation keys are used, and all 31 bibliography entries have an
identified authoritative record. Metadata was checked on 2026-09-17 using
Crossref DOI records where available, publisher/ACM/JMLR/PNAS/MIT Press
pages, the EDBT/OpenProceedings record for `10.48786/EDBT.2023.03`, and the
cited GitHub/dbDB/DB-Engines official pages. `MATCH` means title, author set,
year, and venue/type agree with the manuscript entry. `PARTIAL` means the
canonical record or dynamic official page was identified but automated
metadata retrieval was limited; it is not a bibliographic contradiction.

Verification breakdown: 24 DOI records were matched through Crossref; the
Vassiliadis DOI was verified through DataCite and its official OpenProceedings
PDF; Loukas was verified on the JMLR page; and the remaining five entries are
the partial official-record/dynamic-page cases listed below.

| Key | Existence / authority | Metadata | Manuscript use |
|---|---|---|---|
| `benats2021multidatabasemodels` | DOI/Crossref | MATCH | DIRECT_SUPPORT |
| `benjamini1995fdr` | DOI/Crossref | MATCH | METHOD_PRECEDENT |
| `bird2009sociotechnical` | DOI/Crossref/IEEE | MATCH | BACKGROUND_SUPPORT |
| `blincoe2015ecosystems` | DOI/Crossref/IEEE | MATCH | DIRECT_SUPPORT, CONTRAST |
| `blincoe2019referencecoupling` | DOI/Crossref/Elsevier | MATCH | DIRECT_SUPPORT, CONTRAST |
| `blondel2008louvain` | DOI/Crossref/JSTAT | MATCH | METHOD_PRECEDENT |
| `bosch2009spltoecosystems` | ACM canonical record | PARTIAL (record fetch returned 403) | BACKGROUND_SUPPORT |
| `dbdb2026databaseofdatabases` | dbDB official site | PARTIAL (dynamic snapshot) | BACKGROUND_SUPPORT |
| `dbengines2026ranking` | DB-Engines official site | PARTIAL (dynamic snapshot) | BACKGROUND_SUPPORT |
| `francobedoya2017ossecosystems` | DOI/Crossref/Elsevier | MATCH | BACKGROUND_SUPPORT |
| `githubdocs2026autolinked` | GitHub Docs | PARTIAL (dynamic snapshot) | DEFINITION_PRECEDENT, LIMITATION |
| `githubdocs2026linkingprissue` | GitHub Docs | PARTIAL (dynamic snapshot) | DEFINITION_PRECEDENT, LIMITATION |
| `jansen2013softwareecosystemsbook` | DOI/Crossref/Edward Elgar | MATCH | BACKGROUND_SUPPORT |
| `kessler1963bibliographiccoupling` | DOI/Crossref/Wiley | MATCH | DEFINITION_PRECEDENT, CONTRAST |
| `kim2025dbmsextensibility` | DOI/Crossref/VLDB Endowment | MATCH | DIRECT_SUPPORT, BACKGROUND_SUPPORT |
| `kruskal1952ranks` | DOI/Crossref/JASA | MATCH | METHOD_PRECEDENT |
| `lima2025discussionlinks` | DOI/Crossref/Elsevier | MATCH | DIRECT_SUPPORT |
| `liu2022irel` | DOI/Crossref/Elsevier | MATCH | METHOD_PRECEDENT, CONTRAST |
| `manikas2013ecosystemslr` | DOI/Crossref/Elsevier | MATCH | BACKGROUND_SUPPORT |
| `manikas2016revisitingecosystems` | DOI/Crossref/Elsevier | MATCH | BACKGROUND_SUPPORT |
| `mcclean2021ossocialnetwork` | DOI/Crossref/Elsevier | MATCH | BACKGROUND_SUPPORT |
| `loukas2019graphreduction` | JMLR official page | MATCH | METHOD_PRECEDENT, CONTRAST |
| `messerschmitt2003softwareecosystem` | DOI/Crossref/MIT Press | MATCH | BACKGROUND_SUPPORT |
| `newman2006modularity` | DOI/Crossref/PNAS | MATCH | METHOD_PRECEDENT |
| `paiva2025dbmsadoption` | DOI/Crossref/Springer | MATCH | DIRECT_SUPPORT, BACKGROUND_SUPPORT |
| `sanchezgarcia2020quotientnetwork` | DOI/Crossref/Nature | MATCH | DEFINITION_PRECEDENT, CONTRAST |
| `vassiliadis2023sourceschemaevolution` | DOI resolver -> EDBT/OpenProceedings | MATCH | DIRECT_SUPPORT, BACKGROUND_SUPPORT |
| `wang2021sharedlinks` | DOI/Crossref/Springer | MATCH | DIRECT_SUPPORT |
| `xiao2008networkquotients` | DOI/Crossref/APS | MATCH | DEFINITION_PRECEDENT, CONTRAST |
| `xiao2023commitlinks` | DOI/Crossref/Springer | MATCH | DIRECT_SUPPORT |
| `zhang2014developersocialnetworks` | DOI/Crossref/Sci China | MATCH | BACKGROUND_SUPPORT |

Citation accounting is closed:

```text
CITATION_TOKEN_COUNT = 68
UNIQUE_CITATION_KEY_COUNT = 31
BIBLIOGRAPHY_ENTRY_COUNT = 31
MISSING_KEYS = 0
ORPHAN_BIBLIOGRAPHY_ENTRIES = 0
MALFORMED_CITATION_SYNTAX = 0
LITERATURE_EXISTENCE_UNVERIFIED = 0
LITERATURE_METADATA_PARTIAL = 5
```

The five partial entries are one canonical ACM record whose automated request
returned 403 and four dynamic official web resources. Their identity and
relevance were still established; none is treated as a source mismatch.

## 4. Citation-use and claim-source entailment

The 24 citation-bearing lines (68 tokens) were read in context. Uses are
limited to direct empirical precedent, background, method precedent,
definition precedent, contrast, and limitation. No `OVEREXTENDED_CLAIM` or
`SOURCE_MISMATCH` was found. Grouped citations in Introduction/Related Work
support the prior-work context; the formalization gap and contribution claims
are explicitly the manuscript's synthesis rather than attributed findings.

Two bounded notes are retained for a later editorial pass:

1. The Kruskal citation supports the Kruskal-Wallis test. The exact
   epsilon-squared effect-size formula at Methods line 234 is not established
   by that 1952 paper alone; classify that formula support as
   `UNVERIFIED_METHOD_DETAIL`, not as a scientific result.
2. GitHub Docs establish link syntax and mechanics. They do not provide
   empirical false-positive/false-negative rates; the manuscript uses them
   only as a bounded limitation/method rationale.

Neither note blocks the accepted methods or results, but both are E1 editorial
items for any future convergence edit.

## 5. A--F editorial completion audit

### A. Research logic and RQ chains

Each RQ has a visible motivation -> method -> artifact -> result ->
interpretation -> limitation -> conclusion path. RQ1 supplies evidence
composition and construction-boundary support; RQ2a/RQ2b/RQ2c are the
Project-level RefQN structural center; RQ3 is a label-mode-sensitive,
cross-sectional comparison. No RQ is presented as an unsupported causal or
semantic claim.

### B. Section architecture and transitions

Introduction establishes the observation gap and five RQs; Related Work
separates ecosystem, reference-coupling, quotient, and DBMS-domain strands;
Methods defines data, extraction, metrics, statistics, and RefQN in dependency
order; Results follows RQ1 -> RQ2 -> RQ3; Discussion and Validity narrow the
interpretation before the Conclusion. No duplicated result block or missing
section exit was found.

### C. Evidence architecture

Figure 1 carries the Reference-record flow; Figure 2 carries role and weight
views; Figure 3 carries first-order undirected structure and algorithmic
partitions; Figure 4 carries label modes and FDR status. Tables 4.1--4.8
provide the corresponding complete/compact distributions and structural
summaries. Captions, adjacent prose, and units agree.

### D. Terminology, notation, and style

Record/entity/edge and weight/count distinctions are explicit. `Q = M^T R_P
M`, self-loop policy, first-order boundary, and source/target observation
asymmetry are stable across Methods, Results, Discussion, and Appendix A.
Heuristic readability diagnostics found some long mixed-language technical
sentences (most notably the Abstract contribution sentence and dense Results
descriptions), but no E0/E1 comprehension blocker. Residual bare `P0`
literals occur only on two deliberately excluded Methods lines and are
scientifically unambiguous (`P2_STYLE_RESIDUAL`).

### E. Submission and dissertation migration fitness

The manuscript preserves a four-part contribution hierarchy, five-RQ mapping,
bounded availability language, DOI/release distinctions, and Appendix A as a
provenance record rather than a new availability promise. No complete-ecosystem,
dependency-ground-truth, causal, stable-semantic-community, power-law, or
longitudinal claim is made positively. `POSITIVE_OVERCLAIM_COUNT = 0`.

### F. Editorial residuals

No P0/P1 scientific or submission blocker was found. Remaining bounded work is
optional/conservative: review the two citation-scope notes above, decide
whether to split a small number of long sentences, and optionally normalize
the two bare `P0` literals in a separately authorized edit. No such edits are
performed here.

## 6. Guard and blocker assessment

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
NEW_SCIENTIFIC_VALUES = 0
CHANGED_SCIENTIFIC_VALUES = 0
SCIENTIFIC_ASSETS_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
MANUSCRIPT_CHANGED = 0
TABLE_CONTENT_CHANGED = 0
FORMULA_CHANGED = 0
REFERENCE_CHANGED = 0
SIDECAR_CHANGED = 0
MANIFEST_CHANGED = 0
CURRENT_EQUALS_SNAPSHOT = YES
```

Current QA arithmetic failures, population failures, mixed-authority failures,
and unit-semantics failures are all zero. The quotient-eligible record versus
entity distinction and edge-weight versus edge-count distinction are `CLEAR`.

## 7. Recommendation and final status

The accepted scientific baseline is internally coherent and the manuscript is
fit for a bounded editorial convergence pass. Historical/provenance notes are
non-blocking where the current replacement is unambiguous. Do not treat this
E0 record as permission to alter MS-R01; any future wording edits require a
separate authorized revision and hash/guard cycle.

```text
MANUSCRIPT_REVISION = MS-R01
SCIENTIFIC_BASELINE = P0-v3
CURRENT_SHA = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
SNAPSHOT_SHA = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
P0_COUNT = 0
P1_COUNT = 0
P2_COUNT = 2
INFO_COUNT = 8
RECONCILIATION_READINESS = READY_FOR_EDITORIAL_CONVERGENCE
COMMIT_SCOPE = docs/freeze/ch5_refq_ms_r01_comprehensive_editorial_audit_e0.md only
```

Final decision:

`CH5_REFQ_MS_R01_EDITORIAL_AUDIT_E0_PASS_READY_FOR_EDITORIAL_CONVERGENCE`
