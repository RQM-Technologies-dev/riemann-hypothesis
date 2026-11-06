"""Regression tests for Chapter 16 numerical examples, NOT an RH proof."""
import importlib.util
import pathlib
import unittest

import mpmath as mp

PATH = (
    pathlib.Path(__file__).resolve().parents[1]
    / "experiments" / "two_fold_theta_positivity.py"
)
SPEC = importlib.util.spec_from_file_location("two_fold_theta_positivity", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class TwoFoldThetaPositivityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps = 40

    def test_theta_coefficients_agree_with_xi_derivatives(self):
        for n in range(4):
            from_kernel = M.kernel_coefficient(n)
            from_xi = M.xi_coefficient(n)
            self.assertLess(abs(from_kernel - from_xi), mp.mpf("1e-29"))

    def test_first_finite_toeplitz_minors_are_positive(self):
        coeffs = [M.kernel_coefficient(n) for n in range(4)]
        self.assertGreater(M.toeplitz_minor(coeffs, [1, 2], [0, 1]), 0)
        self.assertGreater(
            M.toeplitz_minor(coeffs, [1, 2, 3], [0, 1, 2]), 0
        )
        self.assertLess(
            abs(coeffs[1] ** 2 - coeffs[0] * coeffs[2]
                - mp.mpf("0.0000705569931125013930942051386994")),
            mp.mpf("1e-28"),
        )

    def test_two_fold_quartic_and_counterexample(self):
        a, t = mp.mpf("1"), mp.mpf("1")
        for q in (mp.mpc(1, 1), mp.mpc(-1, 1),
                  mp.mpc(1, -1), mp.mpc(-1, -1)):
            self.assertLess(abs(M.quartet_polynomial(q, a, t)),
                            mp.mpf("1e-35"))
        for q in (mp.mpc(1, 2), mp.mpc(-3, 1)):
            self.assertLess(
                abs(M.quartet_polynomial(q, 0, 2) - (q*q+4)**2),
                mp.mpf("1e-35"),
            )

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            M.kernel_coefficient(-1)
        with self.assertRaises(ValueError):
            M.toeplitz_minor([mp.mpf(1)], [1], [0])
        with self.assertRaises(ValueError):
            M.run(20, 3, 8)


if __name__ == "__main__":
    unittest.main()
