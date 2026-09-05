import unittest

from engineering.nvh import (
    generate_order_map,
    load_nvh_targets,
    maximum_tracked_excitation_hz,
    recommended_modal_screening_upper_hz,
    resolve_operating_envelope,
)


class NVHBaselineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.targets = load_nvh_targets()

    def test_unknown_operating_envelope_uses_screening_values(self):
        envelope = resolve_operating_envelope(self.targets)
        self.assertEqual(envelope.authority, "SCREENING_ONLY")
        self.assertEqual(envelope.rpm_min, 600)
        self.assertEqual(envelope.rpm_max, 7000)

    def test_v8_4x_firing_line_at_6000_rpm(self):
        rows = generate_order_map(self.targets)
        match = [row for row in rows if row.rpm == 6000 and row.order == 4.0]
        self.assertEqual(len(match), 1)
        self.assertAlmostEqual(match[0].frequency_hz, 400.0, places=6)

    def test_order_map_includes_unaligned_maximum_rpm(self):
        targets = {
            **self.targets,
            "operating_envelope": {
                **self.targets["operating_envelope"],
                "rpm_min": {"value": 650},
                "rpm_max": {"value": 7000},
                "screening_step": {"value": 100},
            },
        }

        rows = generate_order_map(targets)
        maximum_rows = [row for row in rows if row.rpm == 7000]

        self.assertEqual(len(maximum_rows), len(self.targets["engine_orders"]["tracked_orders"]["value"]))

    def test_highest_tracked_screening_line(self):
        self.assertAlmostEqual(maximum_tracked_excitation_hz(self.targets), 933.3333333333, places=6)

    def test_modal_screening_band_extends_above_excitation(self):
        max_excitation = maximum_tracked_excitation_hz(self.targets)
        upper = recommended_modal_screening_upper_hz(self.targets)
        self.assertGreater(upper, max_excitation)
        self.assertAlmostEqual(upper, 1400.0, places=6)


if __name__ == "__main__":
    unittest.main()
