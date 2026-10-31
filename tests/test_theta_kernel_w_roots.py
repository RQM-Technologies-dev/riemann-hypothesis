"""Regression checks for the exact theta-kernel hyperspherical zero equation."""
import importlib.util
import pathlib
import unittest

import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "experiments" / "theta_kernel_w_roots.py"
SPEC = importlib.util.spec_from_file_location("theta_kernel_w_roots", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class ThetaKernelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps = 40

    def test_kernel_is_positive_at_samples(self):
        for v in [mp.mpf("0"), mp.mpf(".3"), mp.mpf("1"), mp.mpf("2")]:
            self.assertGreater(M.theta_kernel(v), 0)

    def test_xi_cosine_equivalence(self):
        for t in (mp.mpf("0"), mp.mpf("5"), mp.mpf("20")):
            self.assertLess(
                abs(M.cosine_integral(t)-M.xi_direct(t)),
                mp.mpf("1e-35")
            )

    def test_first_w_root_from_integral(self):
        point = M.solve(count=1, digits=35, scale_L="20")["results"][0]
        self.assertLess(
            abs(mp.mpf(point["known_zero_validation_error"])),
            mp.mpf("1e-30")
        )
        self.assertLess(
            abs(mp.mpf(point["w_from_global_mapping"])
                - mp.mpf("0.33379915194476088")),
            mp.mpf("1e-16")
        )

    def test_compactified_infinity_is_not_a_finite_zero(self):
        L = mp.mpf("20")
        for t in (mp.mpf("1"), mp.mpf("100"), mp.mpf("10000")):
            w = (L**2-t**2)/(L**2+t**2)
            self.assertGreater(w, -1)
            self.assertLess(w, 1)


if __name__ == "__main__":
    unittest.main()
