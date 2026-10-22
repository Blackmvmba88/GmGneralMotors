import unittest

from engineering.firing_candidates import (
    DEFAULT_PAIRS,
    PHASE_FAMILIES_DEG,
    STATION_ORDER,
    bank_pulse_gaps_deg,
    build_candidate,
    circular_gaps_deg,
    enumerate_candidates,
    event_sequence,
)


class FiringCandidateTests(unittest.TestCase):
    def test_complete_candidate_count(self):
        self.assertEqual(len(enumerate_candidates()), 384)

    def test_every_candidate_is_evenly_firing(self):
        for candidate in enumerate_candidates():
            angles = [event.angle_deg for event in candidate.events]
            self.assertEqual(circular_gaps_deg(angles), (90,) * 8)

    def test_each_cylinder_appears_once(self):
        expected = {"L1", "R1", "L2", "R2", "L3", "R3", "L4", "R4"}
        candidate = enumerate_candidates()[0]
        self.assertEqual(set(event_sequence(candidate)), expected)

    def test_common_pin_pair_members_are_360_degrees_apart(self):
        candidate = enumerate_candidates()[0]
        by_cylinder = {event.cylinder: event.angle_deg for event in candidate.events}
        for left, right in DEFAULT_PAIRS.values():
            delta = abs(by_cylinder[left] - by_cylinder[right])
            self.assertEqual(delta, 360)

    def test_each_bank_has_four_pulses_covering_720_cycle(self):
        candidate = enumerate_candidates()[0]
        self.assertEqual(sum(bank_pulse_gaps_deg(candidate.events, "L")), 720)
        self.assertEqual(sum(bank_pulse_gaps_deg(candidate.events, "R")), 720)

    def test_invalid_phase_map_rejected(self):
        phase_map = dict(zip(STATION_ORDER, PHASE_FAMILIES_DEG))
        phase_map["S4"] = 180
        leads = {station: DEFAULT_PAIRS[station][0] for station in STATION_ORDER}
        with self.assertRaises(ValueError):
            build_candidate(phase_map, leads)


if __name__ == "__main__":
    unittest.main()
