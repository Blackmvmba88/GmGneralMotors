# ADR-0001 — Authoritative Geometry Is Parameter-First

**Status:** Accepted  
**Date:** 2026-08-25

## Context

The project will use engineering CAD and later Blender. Both can create geometry, but allowing multiple independent geometric authorities would cause scale drift, manual alignment fixes and non-reproducible assemblies.

## Decision

Authoritative mechanical geometry is defined by:

1. master parameter registry
2. approved datums/interfaces
3. master skeleton
4. downstream engineering component geometry

Blender is a downstream visualization/animation environment unless a future ADR explicitly changes this policy for a specific class of non-critical geometry.

## Consequences

### Positive

- reproducible assembly
- traceable dimensional changes
- easier validation
- deterministic exports
- fewer visual-only fixes

### Cost

- more design work before first render
- unresolved dimensions remain visible instead of being hidden by artistic approximation

## Rejected alternative

Model the complete V8 directly in Blender from the blueprint and tune proportions by eye.

Reason for rejection: fast visually, weak as an engineering source of truth.
