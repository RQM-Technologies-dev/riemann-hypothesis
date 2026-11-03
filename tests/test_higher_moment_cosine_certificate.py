"""Regression checks for the Jacobi-theta higher cosine minorant hierarchy.

They are numerical checks of rigorous symbolic formulas, not RH evidence.
Run: python -m unittest discover -s tests -v
"""
from __future__ import annotations

import importlib.util
import pathlib
import unittest
import mpmath as mp

PATH=(pathlib.Path(__file__).resolve().parents[1]
      /"experiments"/"higher_moment_cosine_certificate.py")
SPEC=importlib.util.spec_from_file_location("higher_moment_cosine_certificate",PATH)
M=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class HigherMomentCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps=35
        cls.moments=M.endpoint_moments(max_k=5,terms=7)

    def test_global_cosine_lower_polynomials(self):
        for n in (1,3,5):
            for x in (mp.mpf("0.3"),mp.mpf(2),mp.mpf(6),mp.mpf(20)):
                P=mp.fsum((-1)**k*x**(2*k)/mp.factorial(2*k)
                          for k in range(n+1))
                self.assertGreaterEqual(mp.cos(x)-P,mp.mpf("-1e-30"))

    def test_monotone_moments(self):
        for k in range(1,6):
            self.assertGreater(self.moments["0.5"][k],self.moments["0.0"][k])

    def test_higher_order_root_and_positive_lower_bound(self):
        r=M.first_positive_root(5,self.moments)
        self.assertGreater(r,mp.mpf("9.4"))
        self.assertLess(r,mp.mpf("9.6"))
        self.assertGreater(M.polynomial_lower(mp.mpf(9),5,self.moments),0)

    def test_direct_completed_xi_above_lower_bound(self):
        x=mp.mpf(9)
        B=M.polynomial_lower(x,5,self.moments)
        for y in ("0", "0.25", "0.5"):
            observed=M.direct_normalized_real(x,mp.mpf(y),7)
            self.assertGreater(observed,B)
            self.assertGreater(B,0)

    def test_symbolic_scale_mapping_does_not_move_heights(self):
        height=mp.mpf("9")
        for L in (mp.mpf("0.2"),mp.mpf(1),mp.mpf(5),mp.mpf(20)):
            theta=2*mp.atan(height/L)
            w=(L*L-height*height)/(L*L+height*height)
            self.assertLess(abs(mp.cos(theta)-w),mp.mpf("1e-30"))

    def test_invalid_order(self):
        with self.assertRaises(ValueError):
            M.polynomial_lower(mp.mpf(3),2,self.moments)


if __name__=="__main__":
    unittest.main()
