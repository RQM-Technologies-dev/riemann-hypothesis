"""Checks for finite folded-channel diagnostics. No test can prove RH."""
import importlib.util
import pathlib
import unittest

import mpmath as mp

PATH = (
    pathlib.Path(__file__).resolve().parents[1]
    / "experiments" / "folded_channel_collision_scan.py"
)
SPEC = importlib.util.spec_from_file_location("folded_channel_collision_scan", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class FoldedChannelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps = 40

    def test_theta_kernel_vs_analytic_continuation(self):
        for t, a in (("3.3", "0.15"), ("14.1", "0.20"),
                     ("25.3", "0.49")):
            C, S = M.channels(t, a)
            Ci, Si = M.theta_channels(t, a)
            self.assertLess(abs(C-Ci), mp.mpf("1e-29"))
            self.assertLess(abs(S-Si), mp.mpf("1e-29"))

    def test_mirror_parity(self):
        for t in ("1.1", "14.1", "25.0"):
            C, S = M.channels(t, "0.2")
            Cneg, Sneg = M.channels(t, "-0.2")
            self.assertLess(abs(C-Cneg), mp.mpf("1e-32"))
            self.assertLess(abs(S+Sneg), mp.mpf("1e-32"))
            self.assertLess(abs(M.channels(t, 0)[1]), mp.mpf("1e-32"))

    def test_phase_identity_independently(self):
        for t, a in (("13.7", "0.05"), ("21.5", "0.20"),
                     ("40", "0.49")):
            data = M.phase_wronskian(t, a)
            z = mp.mpc(t, a)
            phase_from_log_derivative = mp.im(mp.diff(M.xi, z)/M.xi(z))
            a0 = mp.mpf(a)
            growth_from_direct_modulus = mp.diff(
                lambda y: mp.log(abs(M.xi(mp.mpc(t, y)))**2), a0
            )
            self.assertLess(
                abs(phase_from_log_derivative-data["phase_slope"]),
                mp.mpf("1e-28")
            )
            self.assertLess(
                abs(growth_from_direct_modulus-data["outward_log_slope"]),
                mp.mpf("1e-28")
            )
            self.assertLess(
                abs(data["phase_slope"]+data["outward_log_slope"]/2),
                mp.mpf("1e-28")
            )

    def test_sampled_channel_roots_alternate(self):
        a = mp.mpf("0.20")
        cr = M.scan_roots(a, "C")
        sr = M.scan_roots(a, "S")
        self.assertEqual(len(cr), 8)
        self.assertEqual(len(sr), 8)
        self.assertLess(abs(cr[0]-mp.mpf("14.1115014798863001")),
                        mp.mpf("1e-14"))
        self.assertLess(abs(sr[0]-mp.mpf("15.5781086313887788")),
                        mp.mpf("1e-14"))
        events = sorted([(t, "C") for t in cr]+[(t, "S") for t in sr])
        self.assertTrue(all(events[i][1] != events[i+1][1]
                            for i in range(len(events)-1)))
        self.assertGreater(min(abs(c-s) for c in cr for s in sr),
                           mp.mpf("0.8"))

    def test_positive_kernel_counterexample_has_collision(self):
        eps = mp.mpf("0.49")
        y0 = mp.acosh(1/(2*eps))
        z0 = mp.pi+1j*y0
        perturbed = lambda z: M.perturbation(z, eps)
        self.assertLess(abs(perturbed(z0)), mp.mpf("1e-32"))
        self.assertLess(y0, mp.mpf("0.5"))
        self.assertLess(
            M.phase_wronskian(mp.pi, "0.20", perturbed)["W"], 0
        )
        self.assertGreater(
            M.phase_wronskian(mp.pi, "0.21", perturbed)["W"], 0
        )
        # At a simple common channel zero: W_a=|F'(z0)|^2/4.
        W_a = M.phase_wronskian(mp.pi, y0, perturbed)["W_a"]
        expected = abs(mp.diff(perturbed, z0))**2/4
        self.assertGreater(expected, 0)
        self.assertLess(abs(W_a-expected), mp.mpf("1e-30"))

    def test_reject_invalid_scan(self):
        with self.assertRaises(ValueError):
            M.scan_roots("0.2", "Q")
        with self.assertRaises(ValueError):
            M.scan_roots("0.6", "C")


if __name__ == "__main__":
    unittest.main()
