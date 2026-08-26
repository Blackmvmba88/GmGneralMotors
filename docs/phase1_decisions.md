# Phase 1 Decision Register

**Baseline:** 0.3.0  
**Status:** ACTIVE

This register contains only decisions that materially block the dimensional model or master skeleton.

| ID | Decision | Current state | Blocks |
|---|---|---|---|
| D-001 | Displacement authority mode | DECISION_PENDING | bore/stroke lock |
| D-002 | Cylinder center spacing | UNKNOWN | cylinder-axis stations |
| D-003 | Longitudinal bank stagger | UNKNOWN | left/right cylinder station map |
| D-004 | Rod length / compression height / deck clearance stack | UNKNOWN | deck plane |
| D-005 | Piston operating clearance | UNKNOWN | piston OD / bore interface |
| D-006 | Crank station spacing | UNKNOWN | crank skeleton |
| D-007 | Crank phasing | UNKNOWN | kinematics / firing map |
| D-008 | Camshaft axis location | UNKNOWN | cam skeleton / valvetrain |
| D-009 | Chamber/gasket/deck/piston crown volume model | UNKNOWN | compression ratio |
| D-010 | Flywheel reference plane | UNKNOWN | rear package skeleton |
| D-011 | Pulley reference plane | UNKNOWN | front package skeleton |

## D-001 candidates

### A — Preserve blueprint geometry

- bore: 101.6 mm
- stroke: 88.9 mm
- derived: 5.765925746 L / 351.858377 CID

### B — Exact 350 CID, bore fixed

- bore: 101.6 mm
- stroke: 88.430465 mm

### C — Exact 5.700 L, bore fixed

- bore: 101.6 mm
- stroke: 87.883546 mm

No candidate is preferred by this register. Selection requires explicit design intent.

## Rule

A decision may only transition from `UNKNOWN` / `DECISION_PENDING` to `VERIFIED` or `LOCKED` when its source, derivation, or approved target is recorded.
