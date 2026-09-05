import unittest

from engineering.kinematics import (
    cross_plane_throw_phases_deg,
    normalize_angle_deg,
    piston_travel_from_tdc_mm,
    slider_crank_center_position_mm,
)


class KinematicsTests(unittest.TestCase):
    def setUp(self):
        self.r = 44.45
        self.l = 150.0  # test geometry only; not an authoritative engine dimension

    def test_cross_plane_throw_phases(self):
        self.assertEqual(cross_plane_throw_phases_deg(), (0.0, 90.0, 180.0, 270.0))

    def test_normalize_angle(self):
        self.assertAlmostEqual(normalize_angle_deg(450.0), 90.0)

    def test_tdc_travel_is_zero(self):
        self.assertAlmostEqual(piston_travel_from_tdc_mm(0.0, self.r, self.l), 0.0, places=9)

    def test_bdc_travel_equals_stroke(self):
        self.assertAlmostEqual(
            piston_travel_from_tdc_mm(180.0, self.r, self.l),
            2.0 * self.r,
            places=9,
        )

    def test_mechanical_position_repeats_every_360_degrees(self):
        p0 = slider_crank_center_position_mm(37.0, self.r, self.l)
        p1 = slider_crank_center_position_mm(397.0, self.r, self.l)
        self.assertAlmostEqual(p0, p1, places=9)

    def test_throw_phase_offsets_geometry(self):
        p0 = slider_crank_center_position_mm(0.0, self.r, self.l, phase_deg=0.0)
        p180 = slider_crank_center_position_mm(0.0, self.r, self.l, phase_deg=180.0)
        self.assertGreater(p0, p180)

    def test_invalid_rod_length_rejected(self):
        with self.assertRaises(ValueError):
            slider_crank_center_position_mm(0.0, self.r, self.r)


if __name__ == "__main__":
    unittest.main()
