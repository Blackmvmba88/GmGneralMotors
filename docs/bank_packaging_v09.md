# Phase 1 Bank Packaging — Baseline 0.9.0

**Status:** DEVELOPMENT TARGETS / NOT PRODUCTION LOCKED  
**CAD authority:** LIMITED TO ACCEPTED PHASE-1 TARGETS

## Decisions

### Cylinder bridge and center spacing

The development bore remains:

`101.6 mm`

Phase 1 now selects:

`inter-cylinder bridge = 10.0 mm`

which derives:

`center spacing = 101.6 + 10.0 = 111.6 mm`

and a four-cylinder L1→L4 center span:

`3 × 111.6 = 334.8 mm`

The 10.0 mm bridge is a **DESIGN_TARGET**, not a verified production wall,
coolant-jacket or sealing dimension. It was selected from the existing
5–15 mm sensitivity sweep to let the skeleton advance from an explicit,
traceable midpoint candidate.

It must later pass:

- liner/bore architecture;
- coolant-jacket packaging;
- head-gasket sealing land;
- fastener corridor;
- casting/core feasibility;
- thermal-gradient review;
- local stiffness/modal review.

### Rod-journal pairing

The first cross-plane development baseline selects:

`SIDE_BY_SIDE_COMMON_PIN`

with longitudinal station pairs:

`S1 = L1/R1`  
`S2 = L2/R2`  
`S3 = L3/R3`  
`S4 = L4/R4`

This does **not** assign crank throw phase or firing order.

For each paired station:

`Y_station = (Y_left + Y_right) / 2`

The bank stagger remains numeric-UNKNOWN because it depends on rod big-end
widths and side clearance:

`bank_offset = left_width/2 + clearance + right_width/2`

Therefore the project has selected the architecture and relation without
inventing the physical rod dimensions.

## Result

Resolved:

- inter-cylinder bridge development target;
- cylinder center spacing;
- longitudinal cylinder-pair topology;
- common-pin station relation.

Still open:

- numeric bank stagger;
- rod big-end widths / side clearance;
- crank journal diameters;
- throw-phase assignment;
- firing order;
- deck/rod/piston stack.

Fusion/Blender remain locked.
