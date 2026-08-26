# Phase 1 — Dimensional Reconstruction Baseline

**Baseline:** 0.3.0  
**Status:** ACTIVE  
**Gate:** `DIMENSIONAL_MODEL_VALIDATED`  
**CAD / Blender:** LOCKED

## 1. Purpose

Convert the current blueprint from a visual reference into a coherent dimensional system where every accepted dimension is either:

- directly sourced;
- mathematically derived;
- explicitly selected as a design target;
- or left `UNKNOWN`.

The objective is not to make missing geometry disappear. The objective is to make uncertainty visible and computationally traceable.

## 2. Current hard calculations

Using the blueprint values:

- bore = `101.6 mm`
- stroke = `88.9 mm`
- cylinders = `8`
- bank angle = `90°`

we obtain:

### Crank radius

`r = stroke / 2 = 44.45 mm`

### Bank half-angle

Each cylinder-bank axis is offset by:

`90° / 2 = 45°`

from the engine center plane in the XZ cross-section.

### Swept volume

`V = (π/4) × bore² × stroke × cylinders`

Result:

- total = `5.765925746 L`
- total = `351.858377 CID`
- per cylinder = `720.740718 cc`

Therefore the visible `5.7 L / 350 CID` labeling cannot simultaneously be interpreted as exact dimensional authority while preserving both the shown bore and stroke.

## 3. Displacement authority decision matrix

No option is silently selected.

| Candidate | Bore | Stroke | Result | Status |
|---|---:|---:|---:|---|
| Preserve blueprint geometry | 101.6 mm | 88.9 mm | 5.765926 L / 351.858 CID | CANDIDATE |
| Exact 350 CID, bore fixed | 101.6 mm | 88.430465 mm | 350.000 CID | CANDIDATE |
| Exact 5.700 L, bore fixed | 101.6 mm | 87.883546 mm | 5.700000 L | CANDIDATE |

Until an authority mode is selected, the project preserves the visible bore/stroke as `REFERENCE` and treats the displacement label as nominal.

## 4. Relations we can freeze before dimensions are known

A numeric parameter can remain unknown while its governing relation becomes authoritative.

### Deck stack

Along each cylinder axis at TDC:

`deck_height = crank_radius + rod_length + piston_compression_height + deck_clearance`

This turns four unknown dimensions into one controlled stack rather than independent guesses.

### Piston / bore relation

`piston_operating_OD = bore - diametral_piston_clearance`

`radial_clearance = diametral_piston_clearance / 2`

The current blueprint piston label of `101.6 mm` therefore remains ambiguous and cannot be treated as final operating OD while the bore is also `101.6 mm`.

### Static compression ratio

`CR = (swept_volume + clearance_volume) / clearance_volume`

Clearance volume must eventually include the complete geometric volume above the piston at TDC, including the effects of:

- combustion chamber;
- head gasket;
- deck clearance;
- piston crown dish/dome/reliefs.

The blueprint `10.0:1` value is therefore a target/reference until those volumes exist.

## 5. Spatial unknowns blocking the master skeleton

The following cannot be guessed from the current blueprint without additional evidence or an explicit design decision:

- cylinder center spacing;
- longitudinal bank offset/stagger;
- deck height;
- crank station locations/spacing;
- flywheel plane;
- front pulley plane;
- camshaft axis location;
- connecting-rod length;
- piston compression height;
- wrist-pin location and diameter;
- main-journal diameter;
- rod-journal diameter;
- crank phasing.

These directly block `SKELETON_LOCKED`.

## 6. Head / combustion unknowns

Before a true 10:1 compression target can be validated:

- chamber volume;
- gasket bore;
- compressed gasket thickness;
- deck clearance;
- piston crown volume;
- valve relief volume;
- head deck geometry

must be specified.

## 7. Dimensional dependency graph

```text
BORE ───────────────┐
                    ├─→ SWEPT VOLUME ──────┐
STROKE ─→ CRANK R ──┘                      ├─→ COMPRESSION RATIO
                                           │
CHAMBER + GASKET + DECK + PISTON CROWN ───┘

STROKE ─→ CRANK R ───────────────┐
ROD LENGTH ──────────────────────┤
COMPRESSION HEIGHT ──────────────┼─→ DECK HEIGHT
DECK CLEARANCE ──────────────────┘

BORE + PISTON CLEARANCE ───────────→ PISTON OPERATING OD

BANK ANGLE ─→ HALF ANGLE ──────────→ CYLINDER AXIS DIRECTIONS

CYLINDER SPACING + BANK STAGGER ───→ CYLINDER AXIS STATIONS

CRANK STATIONS + PHASING ───────────→ ROTATING-ASSEMBLY SKELETON
```

## 8. Automation

The dimensional layer now has executable relations in:

`engineering/dimensional.py`

Run the audit with:

`python scripts/dimensional_audit.py`

Generate the candidate table with:

`python scripts/dimensional_audit.py --csv validation/dimensional_candidates.csv`

Unit tests protect the arithmetic and prevent accidental drift.

## 9. Exit criteria for Phase 1

`DIMENSIONAL_MODEL_VALIDATED` requires:

1. displacement authority mode selected;
2. piston/bore clearance semantics resolved;
3. deck stack numerically closed;
4. cylinder spacing and bank stagger resolved;
5. crank stations and phasing resolved;
6. camshaft axis resolved;
7. journal and wrist-pin geometry resolved;
8. head/chamber volume model resolved;
9. flywheel and pulley planes resolved;
10. all critical dimensions have provenance/status;
11. dimensional test suite passes.

Only then may Phase 2 promote the skeleton from draft to authoritative geometry.

## 10. Rule

> A missing dimension is an engineering question, not an invitation to move geometry until it looks right.
