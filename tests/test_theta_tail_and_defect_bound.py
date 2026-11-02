"""Mathematical regression tests for the theta-kernel tail and published counting bound.

Run: python -m unittest discover -s tests -v
No claim of interval-certified zero locations, and no RH proof.
"""
import importlib.util
import pathlib
import unittest

import mpmath as mp

ROOT=pathlib.Path(__file__).resolve().parents[1]
PATH=ROOT/"experiments"/"theta_tail_and_defect_bound.py"
SPEC=importlib.util.spec_from_file_location("theta_tail_and_defect_bound",PATH)
M=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class ThetaTailAndDefectTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps=40
        cls.L=mp.mpf("20")

    def test_real_axis_log_derivative_matches_direct_xi(self):
        x=cls_x=mp.mpf("20.5")
        direct=mp.diff(M.xi,x)/M.xi(x)
        self.assertLess(abs(M.target_from_real_axis(self.L)/self.L-direct),mp.mpf("1e-30"))

    def test_theta_hyperbolic_moment_matches_target(self):
        target=M.target_from_real_axis(self.L)
        moment=M.theta_moment_target(self.L)
        self.assertLess(abs(moment-target),mp.mpf("1e-24"))

    def test_kernel_positive(self):
        for v in [mp.mpf("0"),mp.mpf("0.3"),mp.mpf("1")]:
            self.assertGreater(M.phi_positive(v),0)

    def test_jensen_bound_dominates_known_line_tail(self):
        # Exact total minus first eight numerical on-line roots is an upper
        # bound on remaining on-line roots, even if RH fails.
        gs=[mp.im(mp.zetazero(i)) for i in range(1,9)]
        residual=M.target_from_real_axis(self.L)-mp.fsum(
            M.w_distance(g,self.L) for g in gs)
        self.assertGreater(M.theta_jensen_tail_bound(gs[-1],self.L),residual)

    def test_published_bound_decays(self):
        p200=M.zero_inverse_square_bound(mp.mpf("396.381854222592"))
        pbig=M.zero_inverse_square_bound(M.VERIFIED_H)
        self.assertGreater(p200,pbig)
        self.assertLess(pbig,mp.mpf("1.48e-12"))
        self.assertGreater(pbig,0)

    def test_off_line_bound_is_small_but_not_zero(self):
        bound=2*self.L*(self.L+mp.mpf("0.5"))*M.zero_inverse_square_bound(M.VERIFIED_H)
        self.assertGreater(bound,0)
        self.assertLess(bound,mp.mpf("1.214e-9"))

    def test_comparison_at_first_200_threshold(self):
        H=mp.mpf("396.381854222592")
        bound=2*self.L**2*M.zero_inverse_square_bound(H)
        self.assertLess(bound,mp.mpf("1.746"))
        self.assertGreater(bound,mp.mpf("1.74"))

    def test_positive_even_gaussian_kernel_has_nonreal_zero(self):
        # sigma1=1, sigma2=2; both Gaussian components positive.
        z=mp.sqrt(-2j*mp.pi/3)
        self.assertGreater(abs(mp.im(z)),mp.mpf("0.1"))
        self.assertLess(abs(M.positive_kernel_countermodel(z)),mp.mpf("1e-35"))
        self.assertLess(abs(M.positive_kernel_countermodel(mp.pi)),mp.mpf("1e-35"))

    def test_positive_scales_on_both_sides_of_one(self):
        for L in (mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("1")):
            self.assertGreater(M.target_from_real_axis(L), 0)
        L=mp.mpf("0.5")
        expected=L*(1+mp.euler/2-mp.log(2)-mp.log(mp.pi)/2)
        self.assertLess(abs(M.target_from_real_axis(L)-expected),mp.mpf("1e-30"))

    def test_reject_unphysical_scale(self):
        with self.assertRaises(ValueError):
            M.target_from_real_axis(mp.mpf("0"))
        with self.assertRaises(ValueError):
            M.zero_inverse_square_bound(mp.mpf("1"))


if __name__=="__main__":
    unittest.main()
