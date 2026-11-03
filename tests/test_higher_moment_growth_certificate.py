"""Tests of the Jacobi-theta bilinear moment growth minorant, not of RH.

Run: python -m unittest discover -s tests -v
"""
from __future__ import annotations
import importlib.util
import pathlib
import unittest

import mpmath as mp
import numpy as np

PATH=(pathlib.Path(__file__).resolve().parents[1]
      /"experiments"/"higher_moment_growth_certificate.py")
SPEC=importlib.util.spec_from_file_location("higher_moment_growth_certificate",PATH)
M=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class GrowthMomentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lo,cls.hi=M.moment_bounds(nodes=180,max_order=9,terms=7)

    def test_moments_are_positive_and_upper_above_lower(self):
        for a,b in zip(self.lo,self.hi):
            self.assertGreater(a,0)
            self.assertGreaterEqual(b,a)

    def test_zeroth_lower_moment_factors(self):
        x,weights=np.polynomial.legendre.leggauss(180)
        v=1.5*(x+1)
        q=M.theta_phi_numpy(v,7)*weights*1.5
        expected=np.sum(q)*np.sum(q*v*v)
        self.assertAlmostEqual(self.lo[0],expected,places=13)

    def test_improved_strict_growth_root(self):
        r=M.first_numeric_root(9,self.lo,self.hi)
        self.assertGreater(r,7.18)
        self.assertLess(r,7.19)
        self.assertGreater(M.growth_minorant(7,9,self.lo,self.hi),0)

    def test_growth_direct_completed_zeta_exceeds_minorant(self):
        for x in ("4","6","7"):
            for y in ("0.1","0.5"):
                actual=M.direct_growth_form(x,y,digits=35)
                lower=mp.mpf(y)*M.growth_minorant(float(x),9,self.lo,self.hi)
                self.assertGreater(actual,lower)

    def test_convergence_under_node_refinement(self):
        a,b=M.moment_bounds(nodes=260,max_order=9,terms=7)
        r180=M.first_numeric_root(9,self.lo,self.hi)
        r260=M.first_numeric_root(9,a,b)
        self.assertLess(abs(r180-r260),1e-8)

    def test_invalid_orders(self):
        with self.assertRaises(ValueError):
            M.growth_minorant(2,2,self.lo,self.hi)
        with self.assertRaises(ValueError):
            M.moment_bounds(nodes=10)
        with self.assertRaises(ValueError):
            M.direct_growth_form("2","0",digits=30)


if __name__=="__main__":
    unittest.main()
