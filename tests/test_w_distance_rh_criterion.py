"""Regression tests for the w-distance criterion; no assertion of RH."""
import importlib.util
import pathlib
import unittest

import mpmath as mp

PATH = pathlib.Path(__file__).resolve().parents[1] / "experiments" / "w_distance_rh_criterion.py"
SPEC = importlib.util.spec_from_file_location("w_distance_rh_criterion", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class WDistanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps = 45
        cls.L = mp.mpf(20)
        cls.target = cls.L * M.xi_log_derivative_real(cls.L + mp.mpf("0.5"))

    def test_distance_is_polar_half_angle(self):
        for g in (mp.mpf(0), mp.mpf("14.134725"), mp.mpf(100)):
            theta = 2 * mp.atan(g / self.L)
            self.assertLess(abs(M.w_distance(g,self.L) - (1 + M.w_coordinate(g,self.L))),mp.mpf("1e-40"))
            self.assertLess(abs(M.w_distance(g,self.L) - 2*mp.cos(theta/2)**2),mp.mpf("1e-40"))

    def test_log_derivative_independent_expression(self):
        s = self.L + mp.mpf("0.5")
        def xi(x):
            return mp.mpf("0.5")*x*(x-1)*mp.pi**(-x/2)*mp.gamma(x/2)*mp.zeta(x)
        self.assertLess(abs(self.target/self.L - mp.diff(xi,s)/xi(s)),mp.mpf("1e-40"))

    def test_target_known_digits(self):
        self.assertLess(abs(self.target - mp.mpf("13.33099047799700248726506126")),mp.mpf("1e-23"))

    def test_finite_partial_sums_remain_positive_gap(self):
        acc = mp.mpf(0)
        for n in range(1,9):
            t = mp.im(mp.zetazero(n))
            term = M.w_distance(t,self.L)
            self.assertGreater(term,0)
            acc += term
            self.assertLess(acc,self.target)
        self.assertLess(abs(acc - mp.mpf("5.38465888169121402740288172522")),mp.mpf("1e-25"))

    def test_hypothetical_off_line_quartet_is_positive(self):
        delta = mp.mpf("0.125")
        g = mp.mpf("14.13472514173469379")
        expected = M.off_line_pair_weight(delta,g,self.L)
        z = delta + 1j*g
        other = -delta + 1j*g
        centered = self.L * (2*self.L/(self.L**2-z**2)+2*self.L/(self.L**2-other**2))
        self.assertGreater(expected,0)
        self.assertLess(abs(centered-expected),mp.mpf("1e-40"))

    def test_off_line_cayley_reciprocal(self):
        delta = mp.mpf("0.125")
        g = mp.mpf("14")
        a = M.off_line_cayley_radius_squared(delta,g,self.L)
        b = M.off_line_cayley_radius_squared(-delta,g,self.L)
        self.assertGreater(a,1)
        self.assertLess(b,1)
        self.assertLess(abs(a*b-1),mp.mpf("1e-40"))

    def test_invalid_numerical_scale(self):
        with self.assertRaises(ValueError):
            M.xi_log_derivative_real(mp.mpf(1))
        with self.assertRaises(ValueError):
            M.off_line_pair_weight(mp.mpf("0.6"),mp.mpf("14"),self.L)


if __name__ == "__main__":
    unittest.main()
