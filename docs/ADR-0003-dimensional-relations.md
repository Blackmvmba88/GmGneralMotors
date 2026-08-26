# ADR-0003 — Dimensional Relations Precede Geometry

**Status:** Accepted  
**Date:** 2026-08-25

## Context

Phase 1 exposed a common CAD failure mode: unresolved dimensions can be hidden by visually fitting parts together. That creates geometry which appears coherent but cannot be reproduced, audited or safely propagated when a master dimension changes.

The current V8 blueprint also contains a concrete example: the displayed bore and stroke mathematically produce a displacement different from the nominal displacement label.

## Decision

The project will allow a governing dimensional relation to become authoritative before every numeric input is known.

Examples:

- `crank_radius = stroke / 2`
- `deck_height = crank_radius + rod_length + compression_height + deck_clearance`
- `piston_operating_OD = bore - diametral_clearance`
- `compression_ratio = (swept_volume + clearance_volume) / clearance_volume`

Unknown numeric inputs remain `UNKNOWN` and cannot be replaced by visually convenient defaults.

When multiple coherent interpretations exist, they are represented as explicit authority candidates until one is selected.

## Consequences

### Positive

- unresolved geometry remains traceable;
- stack-up errors become visible before CAD;
- blueprint inconsistencies become design decisions rather than hidden corrections;
- parameter changes propagate deterministically;
- skeleton geometry receives a cleaner contract.

### Cost

- authoritative CAD starts later;
- more engineering decisions are visible and must be resolved explicitly.

## Rejected alternative

Choose whichever dimensions make the first CAD model look closest to the blueprint and backfill documentation later.

Reason for rejection: visual convergence is not dimensional authority.
