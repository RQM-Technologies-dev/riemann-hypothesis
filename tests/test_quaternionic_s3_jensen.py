"""Regression tests for quaternionic S^3 Jensen harmonic identity.

The tested mathematical formula is exact; numerical quadrature is not
certified and passing tests does not prove RH.
"""
import importlib.util
import pathlib
import unittest

import mpmath as mp

PATH=pathlib.Path(__file__).resolve().parents[1]/"experiments"/"quaternionic_s3_jensen.py"
SPEC=importlib.util.spec_from_file_location("quaternionic_s3_jensen",PATH)
M=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class QuaternionicS3JensenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps=35

    def test_zero_free_center_exact_coefficient(self):
        x0=mp.mpf("0.5")
        val=mp.re(M.xi(x0))
        ratio=mp.re(mp.diff(M.xi,x0,2)/val)
        self.assertLess(abs(val-mp.mpf("0.497120778188314109912773739685")),mp.mpf("1e-27"))
        self.assertLess(abs(ratio-mp.mpf("0.0462099862308379415778676208607")),mp.mpf("1e-27"))

    def test_S3_mean_is_second_harmonic_corrected_circle_mean(self):
        for radius in ("1","5"):
            m2,k2=M.circle_harmonics(radius)
            m4=M.quaternionic_s3_mean(radius)
            self.assertLess(abs(m4-(m2-k2)),mp.mpf("1e-27"))
            self.assertLess(abs(m4-M.zero_free_formula(radius)),mp.mpf("1e-27"))

    def test_example_with_spherical_zero_inside_and_outside(self):
        gamma=mp.mpf(5)
        poly=lambda z: 1+(z/gamma)**2
        for radius in ("2","7"):
            observed=M.quaternionic_s3_mean(radius,poly)
            formula=M.polynomial_sphere_formula(radius,gamma)
            self.assertLess(abs(observed-formula),mp.mpf("1e-27"))

    def test_wrong_inputs_fail(self):
        with self.assertRaises(ValueError):
            M.quaternionic_s3_mean(0)
        with self.assertRaises(ValueError):
            M.polynomial_sphere_formula(5,5)
        with self.assertRaises(ValueError):
            M.run(20)
        with self.assertRaises(ValueError):
            M.run(30,("15",))


if __name__=="__main__":
    unittest.main()
