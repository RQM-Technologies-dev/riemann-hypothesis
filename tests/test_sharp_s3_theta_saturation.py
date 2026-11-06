"""Finite checks of Chapter 24. These tests DO NOT prove RH."""
import importlib.util
import pathlib
import unittest

import mpmath as mp

PATH = pathlib.Path(__file__).resolve().parents[1] / "experiments" / "sharp_s3_theta_saturation.py"
SPEC = importlib.util.spec_from_file_location("sharp_s3_theta_saturation", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class SharpS3ThetaSaturationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps = 40

    def test_xi_moment(self):
        self.assertLess(
            abs(M.xi_theta_local_moment()
                -mp.mpf("0.011552496557709485394466905215169507")),
            mp.mpf("1e-32"),
        )

    def test_quartet_at_zero_and_reflected_roots(self):
        a, t = mp.mpf(".2"), mp.mpf("14.13")
        self.assertEqual(M.quartic(0, a, t), 1)
        for z in (mp.mpc(a,t),mp.mpc(-a,t),mp.mpc(a,-t),mp.mpc(-a,-t)):
            self.assertLess(abs(M.quartic(z, a, t)), mp.mpf("1e-35"))

    def test_radial_jensen_gap_without_using_angular_zeros(self):
        a, t = mp.mpf(".2"), mp.mpf("14.13")
        I = M.toy_radial_integral(a,t)
        local = M.toy_local_moment(a,t)
        penalty = 2*a*a/(a*a+t*t)**2
        self.assertLess(abs(I-local-penalty), mp.mpf("1e-32"))
        self.assertGreater(penalty, 0)

    def test_folded_quartet_zero_gap(self):
        t = mp.mpf("14.13")
        self.assertLess(abs(M.toy_radial_integral(0,t)
                            -M.toy_local_moment(0,t)), mp.mpf("1e-32"))

    def test_theta_perturbation_exact_positive_extra_gap(self):
        b, series, closed = M.theta_perturbation_extra_gap()
        self.assertLess(abs(series-closed), mp.mpf("1e-32"))
        self.assertGreater(series, 0)
        self.assertLess(abs(series-mp.mpf(
            "0.00084061113274389191045350055819283856")), mp.mpf("1e-32"))
        self.assertLess(b, mp.mpf(".5"))

    def test_invalid_parameters(self):
        with self.assertRaises(ValueError):
            M.toy_local_moment(0,0)  # only if method rejects zero radius
        with self.assertRaises(ValueError):
            M.theta_perturbation_extra_gap(mp.mpf(".5"))
        with self.assertRaises(ValueError):
            M.run(20)


if __name__ == "__main__":
    unittest.main()
