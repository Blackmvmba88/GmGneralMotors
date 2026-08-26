# Phase 1 Handoff to Phase 2

This document defines the contract between dimensional reconstruction and the master skeleton.

Phase 1 does **not** need final production fillets, casting detail, fasteners, textures, or aesthetic surfaces.

It must instead hand Phase 2 a compact, authoritative set of values sufficient to place:

- crank axis;
- cam axis;
- eight cylinder axes;
- deck planes;
- crank station planes;
- front/rear package planes.

## Handoff package

```text
DIMENSIONAL_BASELINE_ID
BANK_ANGLE
BORE
STROKE
CYLINDER_CENTER_SPACING
BANK_LONGITUDINAL_OFFSET
DECK_HEIGHT
CAM_AXIS_LOCATION
CRANK_STATION_MAP
CRANK_PHASING_STATUS
FLYWHEEL_PLANE
PULLEY_PLANE
PISTON_ROD_STACK_REFERENCE
SOURCE/STATUS FOR EACH INPUT
```

## Acceptance

Phase 2 rejects the handoff if any required skeleton entity needs to be positioned by eye.
