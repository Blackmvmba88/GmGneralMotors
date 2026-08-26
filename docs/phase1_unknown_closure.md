# Phase 1 Unknown Closure Protocol

**Purpose:** Resolve missing dimensions without contaminating the master model with guesses.

## Evidence classes

A missing dimension may be closed only by one of these routes:

1. **SOURCE** — manufacturer drawing, datasheet, standard, measurement or trusted reference.
2. **DERIVED** — mathematically determined from already approved upstream parameters.
3. **DESIGN TARGET** — explicitly selected engineering value with rationale and revision ownership.
4. **MEASURED** — physical measurement with method, uncertainty and reference datum recorded.

## Required metadata

Every closed parameter must record:

```text
parameter_id
value
unit
status
source_class
source_or_derivation
revision
owner
notes
```

## Forbidden closures

The following do not qualify:

- copied from an unverified image because it looks plausible;
- moved until adjacent geometry fits;
- chosen from memory without provenance;
- rounded to match a marketing label;
- inherited from another engine without explicitly declaring it as a design target/reference.

## Dependency-first procedure

Before selecting a missing value:

1. identify every downstream entity it controls;
2. identify any equation that constrains it;
3. identify whether it can be derived instead of selected;
4. identify conflicts with NVH, packaging, fatigue, thermal or manufacturing constraints;
5. only then promote its state.

## Phase 1 closure order

Recommended order:

1. displacement authority;
2. cylinder spacing + bank stagger;
3. rod / piston / deck stack;
4. crank station geometry;
5. journal + wrist-pin interfaces;
6. cam axis;
7. head/chamber volume model;
8. front/rear package planes.

This sequence reduces rework because later dimensions depend on earlier geometry.
