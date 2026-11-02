"""All-scale symbolic-L tests: formula consistency, not an RH proof."""
from __future__ import annotations

import importlib.util
import pathlib
import unittest
import mpmath as mp

PATH=pathlib.Path(__file__).resolve().parents[1]/"experiments"/"symbolic_scale_family.py"
SPEC=importlib.util.spec_from_file_location("symbolic_scale_family",PATH)
M=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class SymbolicScaleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps=55

    def test_global_unit_sphere_for_all_scales(self):
        t=mp.im(mp.zetazero(1))
        for L in (mp.mpf("0.01"),mp.mpf("0.1"),mp.mpf("0.5"),mp.mpf(1),mp.mpf(20)):
            w=M.w(L,t)
            theta=2*mp.atan(t/L)
            self.assertLess(abs(w-mp.cos(theta)),mp.mpf("1e-49"))
            self.assertLess(abs(1+w-M.on_line_weight(L,t)),mp.mpf("1e-49"))
            self.assertLess(abs(w*w+mp.sin(theta)**2-1),mp.mpf("1e-49"))

    def test_zero_height_unaffected_by_scale(self):
        results=M.scale_family(["0.1","0.5","20"],count=2,digits=45)
        heights={r["first_zero_height_unchanged"] for r in results["scale_examples"]}
        self.assertEqual(len(heights),1)
        angles=[mp.mpf(r["first_zero_theta_degrees"]) for r in results["scale_examples"]]
        self.assertGreater(angles[0],angles[1])
        self.assertGreater(angles[1],angles[2])

    def test_log_derivative_removable_pole_at_s_one(self):
        h=mp.mpf("1e-13")
        finite_diff=(M.xi(1+h)-M.xi(1-h))/(2*h*M.xi(1))
        self.assertLess(abs(M.log_derivative(mp.mpf(1))-finite_diff),mp.mpf("1e-24"))
        self.assertEqual(M.xi(mp.mpf(1)),mp.mpf("0.5"))

    def test_real_axis_target_for_all_scales(self):
        for L in (mp.mpf("0.1"),mp.mpf("0.5"),mp.mpf("1"),mp.mpf("5"),mp.mpf("20")):
            x=mp.mpf("0.5")+L
            if x!=1:
                target_direct=L*mp.diff(M.xi,x)/M.xi(x)
                self.assertLess(abs(target_direct-M.total_target(L)),mp.mpf("1e-42"))
            self.assertGreater(M.total_target(L),0)

    def test_offline_quartet_factor_and_derivative(self):
        d,g=mp.mpf("0.125"),mp.mpf("14.13472514173469379")
        for L in (mp.mpf("0.1"),mp.mpf("0.5"),mp.mpf(1),mp.mpf(20),mp.mpf(100)):
            F=M.quartet_factor(L,d,g)
            self.assertGreater(F,1)
            weight=M.quartet_weight(L,d,g)
            self.assertGreater(weight,0)
            self.assertLess(abs(L*mp.diff(lambda v:mp.log(M.quartet_factor(v,d,g)),L)-weight),
                            mp.mpf("1e-43"))

    def test_normalized_quartet_uniform_bound(self):
        d,g=mp.mpf("0.4"),mp.mpf(14)
        for L in (mp.mpf("0.001"),mp.mpf("0.1"),mp.mpf("0.5"),mp.mpf(2),mp.mpf(20),mp.mpf("1e6")):
            self.assertLessEqual(M.quartet_weight(L,d,g)/L**2,4/g**2)

    def test_small_scale_limit_is_finite(self):
        L=mp.mpf("0.00001")
        lim=mp.diff(M.xi,mp.mpf("0.5"),2)/M.xi(mp.mpf("0.5"))
        self.assertLess(abs(M.total_target(L)/L**2-lim),mp.mpf("1e-9"))

    def test_published_uniform_bound_is_positive(self):
        P=M.inverse_square_count_upper(M.VERIFIED_HEIGHT)
        self.assertGreater(P,0)
        self.assertLess(2*P,mp.mpf("2.960e-12"))
        self.assertLess(2*mp.mpf(20)**2*P,mp.mpf("1.184e-9"))

    def test_reject_nonpositive_L(self):
        for L in [mp.mpf(0),mp.mpf(-1)]:
            with self.assertRaises(ValueError):
                M.total_target(L)
            with self.assertRaises(ValueError):
                M.w(L,mp.mpf(14))
            with self.assertRaises(ValueError):
                M.quartet_factor(L,mp.mpf("0.1"),mp.mpf(14))


if __name__=="__main__":
    unittest.main()
