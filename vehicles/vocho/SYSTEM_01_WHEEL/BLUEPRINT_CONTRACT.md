# Blueprint Contract — BM-VOCHO-WHEEL-001

## Goal

A blueprint is not decorative concept art. It is a dimensional projection of the same authoritative component definition used to build and validate the Blender artifact.

## Sheet set

### Sheet W-001 — Front
Must show:
- tire outer diameter,
- rim diameter,
- hub center,
- pitch circle,
- stud count and angular spacing,
- centerlines.

### Sheet W-002 — Side
Must show:
- total tire width,
- rim width,
- mounting plane,
- wheel centerline,
- inboard/outboard offsets.

### Sheet W-003 — Axial section
Must show:
- bead/rim relationship,
- hub interface,
- mounting plane,
- clearance envelope,
- principal thicknesses available from verified data.

### Sheet W-004 — Exploded assembly
Must identify:
- tire,
- rim,
- hub/interface,
- studs,
- valve,
- referenced brake interface.

## Annotation policy

Every numeric annotation must map to a key in `dimensions.json` or explicitly state that it is a measured/derived construction value.

Unknown dimensions must display as `TBD`; a plausible-looking number is not acceptable evidence.

## Revision identity

Each exported blueprint should include:

- system ID,
- revision,
- units,
- source dimensions file SHA-256 when available,
- Blender source SHA-256 when available,
- certificate SHA-256 when certified.

## Visual quality

Beauty matters, but it follows dimensional closure for early revisions. Once geometry constraints are stable, visual quality becomes a first-class gate rather than an afterthought.

The target is a blueprint that can be used by a human modeler and by an automated geometry pipeline without disagreement.
