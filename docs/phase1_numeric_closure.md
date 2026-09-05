# Phase 1 Numeric Closure Strategy

**Baseline:** 0.7.0  
**Status:** ACTIVE  
**Gate:** `DIMENSIONAL_MODEL_VALIDATED`

## Purpose

The relation layer is now mature enough that the remaining Phase 1 work can be treated as a finite closure problem instead of open-ended modeling.

The goal is not to fill every `UNKNOWN` immediately. The goal is to close them in the order that unlocks the master skeleton and rotating system with the least risk of rework.

## Closure order

### Tier A — skeleton placement blockers

These inputs directly control authoritative datum placement:

- inter-cylinder bridge / cylinder center spacing;
- front cylinder Y datum;
- bank longitudinal stagger;
- bore-axis offset mode and value;
- deck height;
- crank station positions;
- cam X/Z position;
- flywheel plane Y;
- pulley plane Y.

Until these are governed, `V8_MASTER_SKELETON` remains unlocked.

### Tier B — piston / deck-stack closure

The deck stack is governed by:

```text
deck_height = crank_radius + rod_length + compression_height + deck_clearance
```

Required independent choices/evidence:

- connecting-rod center-to-center length;
- piston compression height;
- deck clearance;
- wrist-pin geometry;
- piston-to-wall diametral clearance.

Piston clearance must be tied to material and temperature assumptions. A visual piston diameter is not sufficient.

### Tier C — crank / rotating-system closure

Required before deterministic 720° operation:

- cylinder-to-throw mapping;
- rod-journal pairing;
- firing order;
- crank station geometry;
- journal diameters;
- rotating and reciprocating mass model;
- torsional damper strategy.

The selected cross-plane development direction constrains this work but does not complete it.

### Tier D — NVH authority closure

Required to convert screening into authoritative dynamic design:

- operating RPM envelope;
- force/order amplitudes;
- valvetrain event families;
- accessory speed/tooth/blade-pass families;
- sourced material set;
- modal boundary conditions;
- benchmark-derived acoustic targets.

## Status semantics

`REFERENCE` is not enough to pass an authoritative gate.

Accepted Phase 1 closure states are:

- `DESIGN_TARGET` — deliberate engineering choice with rationale;
- `CALCULATED` — derived from governed inputs and an explicit relation;
- `VERIFIED` — supported by source/evidence;
- `LOCKED` — approved authority for the current baseline.

`UNKNOWN`, `DECISION_PENDING`, `SCREENING_ONLY` and raw `REFERENCE` remain blockers for authoritative placement.

## Provenance rule

Every accepted numeric input must be traceable:

```text
DESIGN_TARGET → rationale
CALCULATED    → relation + governed inputs
VERIFIED      → source or relation/evidence
LOCKED        → approved source / decision record
```

## No fake progress

The project must not:

- copy arbitrary production-engine dimensions just to complete the skeleton;
- infer crankpin stations from cylinder center positions;
- silently assume zero bore offset;
- select piston clearance without thermal/material reasoning;
- use generic solver material defaults;
- treat the screening RPM range as the final engine envelope.

## Deliverable

`parameters/phase1_closure.yaml` is the machine-readable closure ledger.

`scripts/phase1_gate_report.py` reports the current blocking set. The report intentionally returns success in CI while Phase 1 is active: explicit unresolved engineering inputs are tracked work, not software failure.

## Exit condition

Phase 1 passes only when the numeric handoff can generate every required skeleton datum without visual placement, undocumented defaults, or manual nudging.
