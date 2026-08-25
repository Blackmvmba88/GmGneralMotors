# Master Skeleton Specification

**Object:** `V8_MASTER_SKELETON`  
**Status:** DRAFT / NOT FROZEN

## Purpose

The skeleton is the smallest geometric object from which the major engine assembly can be derived without visual guesswork.

## Required entities

### Global

- `AXIS_CRANK`
- `AXIS_CAM`
- `PLANE_ENGINE_CENTER`
- `PLANE_FRONT`
- `PLANE_REAR`
- `PLANE_FLYWHEEL`
- `PLANE_PULLEY`

### Left bank

- `AXIS_CYL_L1`
- `AXIS_CYL_L2`
- `AXIS_CYL_L3`
- `AXIS_CYL_L4`
- `PLANE_DECK_LEFT`

### Right bank

- `AXIS_CYL_R1`
- `AXIS_CYL_R2`
- `AXIS_CYL_R3`
- `AXIS_CYL_R4`
- `PLANE_DECK_RIGHT`

### Crank stations

At least four crankpin station planes must be represented once crank architecture is frozen.

## Required parameter inputs

- bank angle
- bore
- stroke
- cylinder center spacing
- deck height
- crank station spacing
- front/rear package references
- flywheel/pulley plane locations
- cam axis location

## Lock conditions

The skeleton cannot become `LOCKED` while any of the above critical spatial inputs remain `UNKNOWN`.

## Modeling prohibition

Do not use decorative engine surfaces as parents for skeleton entities. Surfaces are downstream of the skeleton, never the other way around.
