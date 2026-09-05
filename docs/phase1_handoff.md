# Phase 1 Handoff to Phase 2

This document defines the contract between dimensional reconstruction and the master skeleton.

Phase 1 does **not** need final production fillets, casting detail, fasteners, textures or aesthetic surfaces.

It must hand Phase 2 two distinct layers:

1. an executable **relation layer** that defines how skeleton entities are constructed;
2. a governed **numeric layer** containing every value needed to place those entities.

Baseline 0.6.0 establishes the relation layer. The numeric layer is still incomplete.

## Relation-layer package — READY

The project now defines:

```text
BANK_HALF_ANGLE = BANK_ANGLE / 2
LEFT_BANK_AXIS  = (-sin(alpha), 0, cos(alpha))
RIGHT_BANK_AXIS = (+sin(alpha), 0, cos(alpha))
CENTER_SPACING  = BORE + INTER_CYLINDER_BRIDGE
Y_i             = Y_FRONT + i * CENTER_SPACING
RIGHT_Y_FRONT   = LEFT_Y_FRONT + BANK_LONGITUDINAL_OFFSET
DECK_POINT      = CYLINDER_AXIS_BASE + DECK_HEIGHT * BANK_AXIS
DECK_NORMAL     = BANK_AXIS
FLYWHEEL_NORMAL = CRANK_AXIS_DIRECTION
PULLEY_NORMAL   = CRANK_AXIS_DIRECTION
CAM_DIRECTION   = CRANK_AXIS_DIRECTION
```

See:

- `parameters/skeleton_relations.yaml`
- `engineering/skeleton.py`
- `tests/test_skeleton.py`

## Numeric handoff package — NOT READY

```text
DIMENSIONAL_BASELINE_ID
BANK_ANGLE
BORE
STROKE
INTER_CYLINDER_BRIDGE or VERIFIED_CENTER_SPACING
LEFT_BANK_FRONT_CYLINDER_Y
BANK_LONGITUDINAL_OFFSET
BORE_AXIS_OFFSET_MODE / VALUE
DECK_HEIGHT
CAM_AXIS_X_Z
CRANK_STATION_MAP
CYLINDER_TO_THROW_MAPPING
ROD_JOURNAL_PAIRING
FLYWHEEL_PLANE_Y
PULLEY_PLANE_Y
PISTON_ROD_STACK_REFERENCE
SOURCE/STATUS FOR EACH INPUT
```

## Important separations

### Cylinder centers are not crankpin stations

The bank cylinder Y locations define bore/cylinder placement.

Crankpin station planes depend on rod-journal pairing, rod widths/architecture, bank stagger and the selected cylinder-to-throw map. They may not be copied from cylinder centers by convenience.

### Bank stagger is not hidden

Right-versus-left longitudinal offset is an explicit governed input.

If side-by-side common-pin rods are retained, rod-center separation can inform the bank offset. Other rod architectures require their own relation.

### Bore-axis offset is explicit

Phase 2 must not silently assume that cylinder axes intersect the crank centerline. Zero-offset versus deliberate offset is a design decision.

## Acceptance

Phase 2 rejects the handoff if:

- any required spatial numeric input is `UNKNOWN`;
- cylinder-center and crankpin-station semantics are mixed;
- bore-axis offset is implicit;
- a plane/axis requires visual positioning;
- geometry needs manual nudging after parameter-driven construction.

The relation layer being ready does **not** unlock CAD by itself.
