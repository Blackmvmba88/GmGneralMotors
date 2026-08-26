# Phase 1 Dimensional Gate Checklist

## `DIMENSIONAL_MODEL_VALIDATED`

This gate is PASS only when all items below are satisfied.

### Core geometry

- [ ] displacement authority selected
- [ ] bore and stroke status promoted appropriately
- [ ] cylinder center spacing resolved
- [ ] longitudinal bank stagger resolved
- [ ] deck height stack closed
- [ ] crank station spacing resolved
- [ ] flywheel plane resolved
- [ ] pulley plane resolved
- [ ] camshaft axis resolved

### Piston / rod / crank interfaces

- [ ] connecting-rod center length resolved
- [ ] piston compression height resolved
- [ ] piston-to-wall clearance resolved
- [ ] piston operating OD derived
- [ ] wrist-pin diameter/location resolved
- [ ] main-journal diameter resolved
- [ ] rod-journal diameter resolved
- [ ] crank phasing resolved or formally delegated to Phase 3 with skeleton-compatible station geometry

### Combustion volume

- [ ] chamber volume resolved
- [ ] gasket bore resolved
- [ ] compressed gasket thickness resolved
- [ ] deck clearance resolved
- [ ] piston crown volume resolved
- [ ] 10.0:1 reference compression ratio either verified or explicitly superseded

### Provenance / automation

- [ ] all critical numeric inputs have provenance
- [ ] no critical parameter remains implicitly guessed
- [ ] `python scripts/validate_parameters.py` passes when runner is available
- [ ] `python -m unittest discover -s tests -p "test_*.py"` passes
- [ ] `python scripts/dimensional_audit.py --csv validation/dimensional_candidates.csv` passes
- [ ] generated audit contains no undocumented authority switch

### Gate result

Current result: **FAIL / EXPECTED — PHASE 1 ACTIVE**

Failure at this stage is not a defect. It is the explicit representation of unresolved engineering work.
