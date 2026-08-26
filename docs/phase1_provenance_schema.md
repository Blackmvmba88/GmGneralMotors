# Phase 1 Parameter Provenance Schema

**Status:** Draft operational schema

Every critical dimensional parameter should eventually conform to this semantic record:

```yaml
parameter_name:
  value: null
  unit: mm
  status: UNKNOWN
  source_class: null
  source: null
  derivation: null
  uncertainty: null
  revision: 0.3.0
  notes: null
```

Allowed `source_class` values:

- `BLUEPRINT_REFERENCE`
- `ENGINEERING_DRAWING`
- `DATASHEET`
- `STANDARD`
- `MEASURED`
- `DERIVED`
- `DESIGN_TARGET`
- `EXTERNAL_REFERENCE`

Allowed lifecycle states:

- `UNKNOWN`
- `ESTIMATED`
- `REFERENCE`
- `CALCULATED`
- `VERIFIED`
- `LOCKED`
- `DECISION_PENDING`

## Promotion rules

### `UNKNOWN → REFERENCE`

Requires a named source or clearly identified visual/reference origin.

### `REFERENCE → VERIFIED`

Requires independent confirmation, authoritative documentation, or measurement.

### `CALCULATED`

Requires explicit upstream inputs and equation.

### `VERIFIED → LOCKED`

Requires design approval and downstream-impact review.

### `DESIGN_TARGET`

A chosen value does not pretend to be historical fact. It remains labeled as a design decision and must carry the rationale that selected it.

## Principle

Traceability is part of the geometry. A number without provenance is not yet an engineering parameter.
