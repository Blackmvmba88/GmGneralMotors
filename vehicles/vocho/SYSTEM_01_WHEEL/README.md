# SYSTEM_01_WHEEL — Vocho Wheel Assembly

Status: `SPECIFICATION_OPEN`

System ID: `BM-VOCHO-WHEEL-001`

## Purpose

Define the first complete BlackMamba vehicle modeling unit: one wheel corner assembly with enough structure to support dimensional modeling, blueprint generation, Blender construction, and later WARPBLACK evidence certification.

## Assembly hierarchy

```text
SYSTEM_01_WHEEL
├── tire
├── rim
├── hub
├── studs
├── brake_interface
├── valve
└── reference_axes
```

Brake disc/drum and caliper/backing-plate geometry belong to the brake system, but their wheel-facing interfaces may be referenced here.

## Blender object contract

Recommended object names:

```text
BMV_WHEEL_ROOT
BMV_TIRE
BMV_RIM
BMV_HUB
BMV_STUD_01
BMV_STUD_02
BMV_STUD_03
BMV_STUD_04
BMV_VALVE
BMV_AXIS_ROTATION
BMV_PLANE_MOUNT
```

Object names are part of the machine-readable interface. Renaming them after certification requires a new certificate.

## Coordinate contract

Use the repository coordinate-system convention. The wheel must expose:

- wheel rotation axis,
- mounting plane,
- wheel center,
- outboard direction,
- ground-contact reference plane.

No downstream suspension geometry should depend on viewport position or eyeballed transforms.

## Required blueprint views

Every certifiable wheel revision must support:

1. front elevation,
2. side elevation,
3. section through rotation axis,
4. mounting-face detail,
5. bolt/stud pattern detail,
6. exploded assembly view.

Blueprint annotations should be generated from the parameter source whenever possible.

## Minimum dimensions

The model cannot reach `DIMENSIONALLY_CLOSED` until these values are confirmed or explicitly classified:

- nominal rim diameter,
- rim width,
- tire outer diameter,
- tire section width,
- hub bore / center interface,
- bolt/stud count,
- pitch-circle diameter,
- stud diameter,
- mounting-plane offset,
- tire centerline offset,
- valve location convention.

See `dimensions.json`.

## Validation gates

### G0 — structure
- expected object hierarchy exists,
- no unnamed production objects,
- root object is deterministic.

### G1 — dimensions
- every required dimension has provenance,
- units are explicit,
- derived values declare inputs,
- no `tbd` value is treated as certified.

### G2 — geometry
- tire and rim are coaxial,
- mounting plane is defined,
- wheel center is reproducible,
- stud pattern is rotationally consistent,
- visible intersections are intentional.

### G3 — visual
- front/side/section renders exist,
- silhouette matches blueprint references,
- topology is inspectable,
- shading does not hide geometric defects.

### G4 — evidence
Target integration with WARPBLACK/BM-BLENDER evidence flow:

```text
READ
→ IDENTIFY TARGET .blend
→ IDENTIFY OBJECTS
→ CAPTURE BEFORE
→ CONTROLLED ACTION / INSPECTION
→ READ BACK
→ CAPTURE EVIDENCE
→ HASH
→ CERTIFY
```

### G5 — artifact
Expected production evidence:

```text
evidence/
├── front.png
├── side.png
├── section.png
├── exploded.png
├── certificate.json
└── certificate.sha256
```

## Definition of done

`BM-VOCHO-WHEEL-001` is done only when:

- dimensions are closed,
- blueprint and Blender scene agree,
- object contract passes,
- evidence exists,
- certificate identifies the exact source artifact,
- read-back confirms the scene has the expected hierarchy and dimensions.

A visually attractive wheel without those checks is a work-in-progress, not a certified system.
