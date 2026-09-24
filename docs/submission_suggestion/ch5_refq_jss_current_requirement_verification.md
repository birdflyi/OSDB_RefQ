# Chapter 5 RefQ JSS Current Requirement Verification

## Scope and authority

This is a documentation-only verification record for the Journal of Systems
and Software (JSS) regular research-article target. It does not modify either
semantic manuscript authority, create a publication PDF, submit to Editorial
Manager, or alter scientific assets.

```text
TASK = CH5_REFQ_JSS_PACKAGING_REQUIREMENT_VERIFICATION_AND_SUBMISSION_DERIVATIVE_PREP
EXECUTION_DATE = 2026-09-24
JOURNAL = Journal of Systems and Software
PUBLISHER = Elsevier
ISSN = 0164-1212
TARGET_TRACK = regular research article / regular research paper
SPECIAL_ISSUE = NO
VSI = NO
```

The frozen semantic authorities remain external to this repository:

```text
MS-R05_SHA = 30491279BC31CC5012042F72E3BA8159DCF182CECEEB62EFF5C865C78B059B22
EN-R03_SHA = B61683132DCAD3B6BB4D5ACCA4B49AE4FCAB0CC0B9A2D57FFCC06CF359AFBFE4
TASK_BASE_REPOSITORY_HEAD = 4c62effcd693026acbd37d7a99992ddbe1559a9f
```

## Current official JSS Guide snapshot

```text
OFFICIAL_JSS_GFA_SOURCE_URL = https://www.sciencedirect.com/journal/journal-of-systems-and-software/publish/guide-for-authors
OFFICIAL_JSS_GFA_LOCAL_PATH = C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/assets/about_journal_and_conference/JSS-Guide_for_authors.pdf
AUTHOR_REPORTED_CAPTURE_DATE = 2026-09-24
JSS_GFA_LOCAL_FILE_EXISTS = YES
JSS_GFA_LOCAL_FILE_SIZE_BYTES = 5377923
JSS_GFA_LOCAL_SHA256 = FB0DF4849E71A4531E22EED7B43034ACA53BD6CDED215AD469CA9BD0CA5E16D3
JSS_GFA_PDF_PARSE_STATUS = PASS
JSS_GFA_IDENTITY_CHECK = PASS
JSS_GFA_LOCAL_SNAPSHOT_STATUS = VERIFIED_CURRENT_JSS_OFFICIAL_SNAPSHOT
JSS_CURRENT_GFA_ACCESS = LOCAL_OFFICIAL_PDF_SNAPSHOT_VERIFIED
LIVE_AUTOMATED_GFA_ACCESS = BLOCKED_403
```

The PDF is a 20-page image-only official-looking ScienceDirect JSS Guide for
Authors snapshot. Standard text extraction returned no text, so pages were
rendered with PyMuPDF and visually inspected. The identity is established by
the PDF's title/branding and its JSS-specific headings, including “Guide for
authors”, “About the journal”, “Writing and formatting”, and “Submitting your
manuscript”. The automated 403 is recorded only as a fetch limitation; it does
not downgrade the verified local snapshot.

## Requirement findings

The detailed row-level matrix is in the external derivative directory at
`submission/jss/EN-R03_P0/JSS_REQUIREMENT_MATRIX.csv`. The following are the
current JSS-specific findings used for packaging:

| Requirement | Evidence | Initial-submission consequence |
|---|---|---|
| Scope | Guide pp. 2–3: software-engineering research, evidence-supported claims, open-source/global development and empirical methods are in scope | Target venue remains compatible; no framing change |
| Peer review | Guide pp. 3–4: single anonymized review, typically at least two reviewers | `JSS_REVIEW_MODEL = SINGLE_ANONYMIZED`; no double-anonymization applied |
| Source format | Guide p. 9 and p. 19: editable source files; online system creates a review PDF | No PDF created here; derivative remains a source-level working file |
| Abstract | Guide p. 10: concise factual abstract, maximum 250 words | EN-R03 abstract = 228 words; pass |
| Keywords | Guide pp. 10–11: 1–7 English keywords | EN-R03 keywords = 7; pass |
| Highlights | Guide p. 11: required, separate editable file, 3–5 bullets, at most 85 characters each | `JSS_HIGHLIGHTS.txt` prepared; all four bullets satisfy the length limit |
| Graphical abstract | Guide p. 11: required separate file; 531 × 1328 px or proportional; TIFF/EPS/PDF/MS Office preferred | Requirement verified; no graphic generated in this task; author input remains required |
| Title page | Guide p. 10: title, authors, affiliations, corresponding author and address fields | Metadata checklist prepared; no author facts invented |
| Declarations | Guide pp. 6–8 and 16–17: competing interests, funding, generative AI and CRediT guidance | Declaration checklist prepared; factual fields remain author input |
| Research data | Guide pp. 14–15: deposit/link data or explain why it cannot be shared; data statement required | Existing DOI is recorded precisely; archive/package scope still needs author confirmation |
| Tables | Guide p. 12: editable text, citations, consecutive numbering and captions | No table values or numbering changed |
| Figures | Guide pp. 12–13: separate files, logical names, captions, format/resolution guidance | Frozen V6/V6-E01 hashes recorded; no conversion or rerender |
| Supplementary material | Guide pp. 13–14: accurate, cited, submitted with manuscript, concise captions | Plan prepared; no files physically moved |
| References | Guide pp. 17–18: consistent style accepted at submission; journal style after acceptance | No bibliography restyle performed |
| Submission declarations | Guide p. 4 and p. 8: prior publication/concurrent-submission declaration; preprints permitted under policy | Author confirmation required; no prior-publication claim added |

The snapshot does not resolve the exact live Editorial Manager article-type
label, ORCID field behavior, suggested-reviewer restrictions, or whether a
cover-letter field is mandatory. These remain `UNVERIFIED_CURRENT_JSS` and do
not require semantic manuscript changes.

## Venue and Open Science anchors

The guide's Open Science section (p. 3) describes the JSS Open Science
Initiative and post-acceptance review of availability/usability. It does not
turn the initiative into a blanket claim that all project artifacts are
public. The derivative therefore distinguishes the existing relation/data
archive DOI (`10.5281/zenodo.18817348`) from the not-yet-verified final
replication package, processed outputs and analysis-code release.

## Status

```text
JSS_ARTICLE_TYPE = regular research article / regular research paper; exact live label UNVERIFIED_CURRENT_JSS
JSS_REVIEW_MODEL = SINGLE_ANONYMIZED
YOUR_PAPER_YOUR_WAY_STATUS = current guide requires editable source files and creates review PDF; named YPW label not shown
ABSTRACT_WORD_COUNT = 228
ABSTRACT_LIMIT_STATUS = PASS (<=250)
KEYWORD_COUNT = 7
HIGHLIGHTS_REQUIREMENT_STATUS = VERIFIED_CURRENT_JSS_MANDATORY; prepared
GRAPHICAL_ABSTRACT_STATUS = VERIFIED_CURRENT_JSS_REQUIRED_NOT_CREATED_AUTHOR_INPUT
TITLE_PAGE_REQUIREMENT_STATUS = VERIFIED_CURRENT_JSS; author metadata pending
ANONYMIZATION_STATUS = NOT_PERFORMED; single-anonymized review
CREDIT_STATUS = VERIFIED_CURRENT_JSS_REQUIRED; author roles pending
COMPETING_INTEREST_STATUS = VERIFIED_CURRENT_JSS_REQUIRED; author declaration pending
FUNDING_STATUS = VERIFIED_CURRENT_JSS_REQUIRED; author declaration pending
DATA_AVAILABILITY_STATUS = VERIFIED_CURRENT_JSS_REQUIRED; scope confirmation pending
CODE_AVAILABILITY_STATUS = precise scope required; no blanket public-code claim
GENERATIVE_AI_DECLARATION_STATUS = VERIFIED_CURRENT_JSS_REQUIRED_IF_APPLICABLE
OPEN_SCIENCE_STATUS = VERIFIED_CURRENT_JSS_OPTIONAL_INITIATIVE
REFERENCE_FORMAT_STATUS = VERIFIED_CURRENT_JSS_CONSISTENT_INITIAL_STYLE_ALLOWED
TABLE_FORMAT_STATUS = VERIFIED_CURRENT_JSS_EDITABLE_CONSECUTIVE_CAPTIONED
FIGURE_UPLOAD_STATUS = VERIFIED_CURRENT_JSS_SEPARATE_FILES_AND_CAPTIONS
SUPPLEMENTARY_MATERIAL_STATUS = VERIFIED_CURRENT_JSS_SUBMIT_AND_CITE
COVER_LETTER_STATUS = UNVERIFIED_CURRENT_JSS; draft prepared for system check
SUGGESTED_REVIEWER_STATUS = UNVERIFIED_CURRENT_JSS; live system check required
```

No current JSS hard rule affecting the semantic manuscript structure remains
unresolved after local-PDF review. The remaining upload blockers are author
metadata/declarations and the required graphical-abstract asset, not scientific
or semantic defects.
