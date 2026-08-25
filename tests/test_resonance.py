import unittest

from engineering.resonance import (
    engine_order_frequency,
    helmholtz_resonator_frequency,
    modal_separation_percent,
    quarter_wave_frequency,
    rectangular_cavity_modes,
    sdof_natural_frequency,
    strouhal_frequency,
    v8_firing_frequency,
)


class ResonanceCoreTests(unittest.TestCase):
    def test_v8_firing_frequency_at_6000_rpm_is_400_hz(self):
        self.assertAlmostEqual(v8_firing_frequency(6000), 400.0)

    def test_first_order_at_3000_rpm_is_50_hz(self):
        self.assertAlmostEqual(engine_order_frequency(3000, 1.0), 50.0)

    def test_quarter_wave_one_meter(self):
        self.assertAlmostEqual(quarter_wave_frequency(1.0), 85.75, places=2)

    def test_rectangular_cavity_first_axial_mode(self):
        modes = rectangular_cavity_modes(1.0, 2.0, 3.0, max_index=1)
        self.assertAlmostEqual(modes[0].frequency_hz, 343.0 / 6.0, places=6)

    def test_helmholtz_frequency_positive(self):
        f = helmholtz_resonator_frequency(0.001, 0.01, 0.05)
        self.assertGreater(f, 0.0)

    def test_strouhal_frequency(self):
        self.assertAlmostEqual(strouhal_frequency(20.0, 0.05, 0.2), 80.0)

    def test_sdof_frequency(self):
        f = sdof_natural_frequency(1.0, (2.0 * 3.141592653589793 * 100.0) ** 2)
        self.assertAlmostEqual(f, 100.0, places=6)

    def test_modal_separation(self):
        self.assertAlmostEqual(modal_separation_percent(90.0, 100.0), 10.0)


if __name__ == "__main__":
    unittest.main()
