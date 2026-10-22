# Cross-Plane V8 Firing-Sequence Candidate Search

**Status:** SCREENING ONLY  
**Production firing order:** UNSELECTED

## Why this exists

The project deliberately does not copy a firing order from a production V8.
Baseline 0.9.0 already defines:

- four longitudinal common-pin stations;
- pairs `L1/R1` through `L4/R4`;
- four cross-plane phase families `0° / 90° / 180° / 270°`;
- an evenly firing four-stroke cadence of one combustion event every `90°`.

That is enough to enumerate the project's internal sequence space.

## Candidate-space size

There are:

- `4! = 24` ways to assign the four phase families to S1–S4;
- `2^4 = 16` ways to choose which member of each common-pin pair fires first.

Therefore:

`24 × 16 = 384`

internally coherent even-fire candidates exist before additional balance,
torsional, exhaust, thermal and acoustic constraints are applied.

## Hard constraints

Every generated candidate must satisfy:

1. exactly eight combustion events over 720 crank degrees;
2. global event cadence = 90 degrees;
3. every cylinder appears exactly once;
4. the two cylinders sharing a station fire 360 degrees apart;
5. no manufacturer cylinder numbering or firing order is imported.

## Screening metrics

The first report calculates:

- left-bank pulse gaps;
- right-bank pulse gaps;
- maximum single-bank pulse gap;
- minimum single-bank pulse gap;
- squared deviation of single-bank gaps from 180 degrees;
- number of adjacent global events from the same bank.

These metrics are **screening heuristics**, not an optimization proof.

The next evidence layer must add:

- crank torsional response;
- counterweight / balance implications;
- bearing-load sequence;
- intake/exhaust pulse interaction;
- exhaust-header topology;
- structural/NVH coincidence;
- thermal sequencing;
- idle and transient subjective targets.

## Deliverables

- `engineering/firing_candidates.py`
- `scripts/firing_candidate_report.py`
- `tests/test_firing_candidates.py`

No candidate becomes the project firing order merely because it ranks well in
the first screening report.
