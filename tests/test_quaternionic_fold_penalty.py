"""Tests for the exact S^3 fold penalty; passing does NOT prove RH."""
import importlib.util
import pathlib
import unittest

import mpmath as mp

PATH = (
    pathlib.Path(__file__).resolve().parents[1]
    / "experiments" / "quaternionic_fold_penalty.py"
)
SPEC = importlib.util.spec_from_file_location("quaternionic_fold_penalty", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class QuaternionicFoldPenaltyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps = 35

    def test_reflected_quartet_reduces_to_fold_at_a_zero(self):
        for t in ("1.5", "14.13"):
            for z in (mp.mpc("0.8", "0.4"), mp.mpc("-1.5", "0.1")):
                self.assertLess(
                    abs(M.reflected_quartet(z, 0, t)
                        - M.folded_reference(z, 0, t)),
                    mp.mpf("1e-30"),
                )

    def test_exact_folding_penalty_nonnegative_and_strict(self):
        for a in ("0.02", "0.20", "0.49"):
            for t in ("1.5", "14.13"):
                for R in ("0.8", "2", "10", "17"):
                    self.assertGreater(M.folding_penalty(R, a, t), 0)
                    self.assertEqual(M.folding_penalty(R, 0, t), 0)

    def test_numeric_sphere_integral_both_radius_regimes(self):
        for a, t, R in (
            ("0.25", "1.5", "0.8"),
            ("0.25", "1.5", "2.0"),
            ("0.20", "14.13", "10.0"),
            ("0.20", "14.13", "17.0"),
        ):
            off = M.spherical_mean_log(
                lambda z: M.reflected_quartet(z, a, t), R
            )
            folded = M.spherical_mean_log(
                lambda z: M.folded_reference(z, a, t), R
            )
            self.assertLess(
                abs(off-folded-M.folding_penalty(R, a, t)),
                mp.mpf("1e-27"),
            )

    def test_actual_centered_xi_small_radius_mean(self):
        for R in ("1", "3"):
            observed = M.spherical_mean_log(M.xi_centered, R)
            exact = M.small_radius_xi_mean(R)
            self.assertLess(abs(observed-exact), mp.mpf("1e-26"))

    def test_bad_inputs(self):
        with self.assertRaises(ValueError):
            M.folding_penalty(0, "0.2", "1.5")
        with self.assertRaises(ValueError):
            M.reflected_quartet(mp.mpc(0, 1), 0, 0)
        with self.assertRaises(ValueError):
            M.spherical_mean_log(lambda z: z, 0)
        with self.assertRaises(ValueError):
            M.run(20)


if __name__ == "__main__":
    unittest.main()
