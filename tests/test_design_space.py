import unittest

from engineering.design_space import (
    cylinder_spacing_from_bridge,
    engine_order_frequency_hz,
    four_cylinder_bank_span_mm,
    mean_piston_speed_mps,
    rod_length_from_ratio,
)


class DesignSpaceTests(unittest.TestCase):
    def test_mean_piston_speed_7000_rpm(self):
        self.assertAlmostEqual(mean_piston_speed_mps(88.9, 7000), 20.7433333333, places=8)

    def test_rod_length_from_ratio(self):
        self.assertAlmostEqual(rod_length_from_ratio(88.9, 1.70), 151.13, places=6)

    def test_spacing_from_bridge(self):
        self.assertAlmostEqual(cylinder_spacing_from_bridge(101.6, 10.0), 111.6)

    def test_four_cylinder_span(self):
        self.assertAlmostEqual(four_cylinder_bank_span_mm(111.6), 334.8)

    def test_v8_firing_order_frequency_at_6500(self):
        self.assertAlmostEqual(engine_order_frequency_hz(6500, 4.0), 433.3333333333, places=8)

    def test_invalid_values_raise(self):
        with self.assertRaises(ValueError):
            mean_piston_speed_mps(0.0, 1000)
        with self.assertRaises(ValueError):
            rod_length_from_ratio(88.9, 0.0)
        with self.assertRaises(ValueError):
            cylinder_spacing_from_bridge(101.6, -1.0)


if __name__ == "__main__":
    unittest.main()
