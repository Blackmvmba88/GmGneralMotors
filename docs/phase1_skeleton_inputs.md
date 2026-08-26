# Phase 1 Spatial Skeleton Inputs

**Purpose:** Define exactly which dimensional outputs Phase 1 must hand to Phase 2.

The master skeleton shall consume only the following spatial inputs or relations.

## Global

- bank angle
- engine origin convention
- front datum
- rear/flywheel plane
- front pulley plane
- crankshaft axis
- camshaft axis location

## Cylinder banks

- cylinder center spacing
- longitudinal bank stagger
- deck height along each cylinder axis
- left/right cylinder-axis orientation derived from bank half-angle

For the current 90° bank reference, each bank axis is offset by 45° in the XZ cross-section. Numeric axis origins still require spacing/stagger/deck inputs.

## Crank stations

- crank station count
- station spacing or explicit station positions
- crankpin phase map
- main-bearing station positions when architecture is frozen

## Derived, not manually entered

The skeleton should derive rather than duplicate:

- crank radius from stroke
- half-bank angle from bank angle
- piston operating OD from bore and clearance
- deck plane from deck-stack closure

## Phase boundary rule

Phase 2 may create construction geometry only after the above inputs are either:

- `LOCKED`, or
- explicitly accepted as a versioned design target with no hidden visual adjustment.
