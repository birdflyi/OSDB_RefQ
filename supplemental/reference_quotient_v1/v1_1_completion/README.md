# RefQ Supplemental v1.1 Material Completion

This additive directory completes the evidence materials required by the
human-decision audit. It does not replace or mutate Supplemental v1 outputs.

The completion scan reads the frozen 2023 Reference inputs once with a
100,000-row chunk size and emits only:

- eligible-edge-class cross-tabs for S1;
- fixed canonical top-source target-entity composition for S7.

S5 inclusion frequency is derived from the existing full ranking table. The
S6 structural summary is copied from the existing CSV-content file to a file
with the correct `.csv` extension. No network algorithm is rerun.
