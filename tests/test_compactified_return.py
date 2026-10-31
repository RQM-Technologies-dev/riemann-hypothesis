"""Regression checks for the one-map compactified zeta-return model.

Run: python -m unittest discover -s tests -v
Requires: mpmath
"""
import importlib.util
import pathlib
import unittest

import mpmath as mp

PATH = pathlib.Path(__file__).resolve().parents[1] / "experiments" / "compactified_return.py"
SPEC = importlib.util.spec_from_file_location("compactified_return", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PolarReturnTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps = 50
        cls.L = mp.mpf("20")

    def test_unit_hypersphere(self):
        for t in (
            mp.mpf("0"), mp.mpf("1"), mp.mpf("20"),
            mp.mpf("100"), mp.mpf("-100")
        ):
            a, b = MODULE.q_polar(t, self.L)
            self.assertLess(abs(a*a + b*b - 1), mp.mpf("1e-45"))

    def test_polar_conjugation(self):
        for t in (mp.mpf("1"), mp.mpf("14.1347"), mp.mpf("100")):
            self.assertLess(
                MODULE.polar_mirror_error(t, self.L), mp.mpf("1e-45"))
            self.assertLess(
                abs(MODULE.theta(t, self.L) +
                    MODULE.theta(-t, self.L) - 2*mp.pi),
                mp.mpf("1e-45"))

    def test_xi_even_real(self):
        for t in (
            mp.mpf("0"), mp.mpf("5"),
            mp.mpf("14.1347"), mp.mpf("30")
        ):
            z = MODULE.xi_at_t(t)
            self.assertLess(
                abs(z - MODULE.xi_at_t(-t)), mp.mpf("1e-44"))
            self.assertLess(abs(mp.im(z)), mp.mpf("1e-44"))

    def test_known_first_zero_maps_to_same_radius(self):
        t = mp.im(mp.zetazero(1))
        a, b = MODULE.q_polar(t, self.L)
        self.assertLess(abs(MODULE.xi_at_t(t)), mp.mpf("1e-45"))
        self.assertLess(abs(a*a + b*b - 1), mp.mpf("1e-45"))

    def test_harmonic_has_no_pole_limit(self):
        m = 60
        tp = 2*mp.pi*m/mp.log(2)
        tm = (2*m+1)*mp.pi/mp.log(2)
        zp = mp.exp(-1j*tp*mp.log(2))
        zm = mp.exp(-1j*tm*mp.log(2))
        self.assertLess(abs(zp-1), mp.mpf("1e-43"))
        self.assertLess(abs(zm+1), mp.mpf("1e-43"))
        self.assertLess(
            abs(mp.pi - MODULE.theta(tp, self.L)), mp.mpf("0.1"))
        self.assertLess(
            abs(mp.pi - MODULE.theta(tm, self.L)), mp.mpf("0.1"))

    def test_xi_decay(self):
        vals = [
            abs(MODULE.xi_at_t(mp.mpf(t)))
            for t in (40, 80, 160)
        ]
        self.assertTrue(vals[0] > vals[1] > vals[2])
        self.assertLess(vals[-1], mp.mpf("1e-45"))

    def test_two_cover_spinor(self):
        # In a fixed quaternionic slice: +1 -> -1 -> +1.
        self.assertLess(
            abs(mp.cos(mp.pi) + 1), mp.mpf("1e-45"))
        self.assertLess(
            abs(mp.cos(2*mp.pi) - 1), mp.mpf("1e-45"))


if __name__ == "__main__":
    unittest.main()
