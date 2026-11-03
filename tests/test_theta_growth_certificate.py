"""Targeted tests for partial Jacobi-theta growth certificate.

Run: python -m unittest discover -s tests -v
A passing test is not a proof of RH.
"""
import importlib.util
import pathlib
import unittest

import mpmath as mp

PATH = pathlib.Path(__file__).resolve().parents[1] / "experiments" / "theta_growth_certificate.py"
SPEC = importlib.util.spec_from_file_location("theta_growth_certificate", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class ThetaGrowthCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps = 40

    def test_exact_constants(self):
        vals = M.exact_moment_thresholds()
        self.assertLess(abs(vals["xi2one_over_xi1"] -
                            mp.mpf("0.0466877290684523662697647137716")),
                        mp.mpf("1e-28"))
        self.assertLess(abs(vals["zero_free_x_bound"] -
                            mp.mpf("6.54505985926647684370822")),
                        mp.mpf("1e-20"))
        self.assertLess(abs(vals["strict_growth_x_bound"] -
                            mp.mpf("4.82113461383647972211890")),
                        mp.mpf("1e-20"))

    def test_independent_theta_kernel_moments(self):
        vals = M.exact_moment_thresholds()
        self.assertLess(abs(M.moment(0, 0) - vals["A0"]), mp.mpf("1e-30"))
        self.assertLess(abs(M.moment(2, 0) - vals["A20"]), mp.mpf("1e-30"))
        self.assertLess(abs(M.moment(4, mp.mpf("0.5")) -
                            vals["A4half"]), mp.mpf("1e-30"))

    def test_growth_is_above_derived_lower_bound(self):
        for y in ("0.01", "0.1", "0.49"):
            row = M.local_growth_lower_bound(mp.mpf("4.82"), mp.mpf(y))
            self.assertTrue(row["is_lower_bound_verified_numerically"])
            self.assertGreater(row["quadratic_lower_bound"], 0)

    def test_half_strip_second_moment_monotone(self):
        old = None
        for y in ("0", "0.1", "0.25", "0.5"):
            mu = M.moment(2, mp.mpf(y))/M.moment(0, mp.mpf(y))
            if old is not None:
                self.assertGreater(mu, old)
            old = mu

    def test_reject_invalid_parameters(self):
        with self.assertRaises(ValueError):
            M.moment(-1, 0)
        with self.assertRaises(ValueError):
            M.local_growth_lower_bound(0, mp.mpf("0.6"))
        with self.assertRaises(ValueError):
            M.run(20, 8)


if __name__ == "__main__":
    unittest.main()
