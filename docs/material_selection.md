# Material Selection and Simulation Provenance

**Status:** DESIGN DEFINITION  
**Gate:** `SHORT_BLOCK_STRUCTURAL_PASS`

## Principle

No authoritative simulation may use an anonymous material such as `aluminum` or `steel`.

Every selected material must have an explicit material ID and a property set tied to source, revision and temperature.

## Minimum property set

Each material used in static, modal, harmonic or thermal analysis must define:

- density;
- elastic modulus;
- Poisson ratio;
- yield strength;
- fatigue evidence or explicit fatigue-data status;
- thermal conductivity;
- thermal expansion coefficient;
- damping/loss-factor status;
- temperature-dependency status.

## Evidence fields

Every numeric property must carry:

```text
value
unit
source
source_revision
temperature_c
status
```

Damping additionally requires a confidence field because damping is strongly dependent on material state, joints, coatings, interfaces and measurement method.

## Component families

The first authoritative material set must cover:

- block / bedplate;
- cylinder heads;
- crankshaft;
- connecting rods;
- pistons;
- covers / oil pan;
- intake structure;
- exhaust structure.

## Selection logic

Material selection must be multi-objective. A material is not accepted only because it is light or strong.

Review at minimum:

```text
mass
stiffness
fatigue
thermal conductivity
thermal expansion
casting / forging route
machinability
joint behavior
modal response
acoustic radiation
cost / serviceability
```

## Current state

`parameters/materials.yaml` intentionally contains no invented property values. All component assignments remain `UNKNOWN` until sourced candidates are introduced.

The validator allows an empty candidate registry during design definition, but once a material is assigned it requires an explicit non-generic ID and a complete provenance-aware property contract.

## Future FEA identity

Every simulation report must include:

```text
MATERIAL_SET_ID
MATERIAL_SET_REVISION
TEMPERATURE_ASSUMPTIONS
PROPERTY_SOURCES
DAMPING_CONFIDENCE
```

This makes modal and structural results reproducible instead of solver-default artifacts.
