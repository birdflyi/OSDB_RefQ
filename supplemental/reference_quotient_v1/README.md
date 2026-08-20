# Reference Quotient Supplemental Evidence and Robustness Package v1

This package is supplemental to the canonical RefQ P0 run. It is based on
`920286e134ca459c8e155942eabc6798ceab8b65` and never overwrites
`outputs/reference_quotient_p0_frozen/`.

The package provides:

- S1 evidence-universe decomposition and frozen-input cross-tabs;
- S2 directed edge-weight sensitivity;
- S3 observation-boundary sensitivity;
- S4 Louvain stability under a predeclared seed range;
- S5 approximate-betweenness stability under predeclared `k` and seed ranges;
- S6 figure-ready derived tables;
- S7 composition of evidence behind fixed canonical top sources, targets and edges.

Run from the repository root with the locked P0 virtual environment:

```powershell
venv\Scripts\python.exe supplemental\reference_quotient_v1\scripts\run_supplemental.py
venv\Scripts\python.exe -m pytest supplemental\reference_quotient_v1\tests
```

All generated files are supplemental, sensitivity, figure-ready derivation or
fine-grained decomposition artifacts. They do not replace canonical outputs.
