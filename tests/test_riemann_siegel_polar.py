"""Check completed-xi/Hardy-Z Gamma identity and needed RS remainder.

Run: python -m unittest discover -s tests -v
"""
import importlib.util
import pathlib
import unittest
import mpmath as mp

PATH = pathlib.Path(__file__).resolve().parents[1] / "experiments" / "riemann_siegel_polar.py"
SPEC = importlib.util.spec_from_file_location("riemann_siegel_polar", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RiemannSiegelPolarTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps = 50

    def test_gamma_envelope_identity(self):
        for t in [mp.mpf("0"), mp.mpf("30"), mp.mpf("50")]:
            s = mp.mpc(mp.mpf("0.5"), t)
            xi = (
                mp.mpf("0.5")*s*(s-1)*mp.power(mp.pi, -s/2)
                * mp.gamma(s/2)*mp.zeta(s)
            )
            A = (
                mp.mpf("0.5")*(t*t+mp.mpf("0.25"))
                * mp.power(mp.pi, -mp.mpf("0.25"))
                * abs(mp.gamma(mp.mpf("0.25")+1j*t/2))
            )
            self.assertLess(abs(xi+A*mp.siegelz(t)), mp.mpf("1e-40"))

    def test_hardy_z_even(self):
        for t in [mp.mpf("14.1"), mp.mpf("30")]:
            self.assertLess(
                abs(mp.siegelz(t) - mp.siegelz(-t)),
                mp.mpf("1e-40")
            )

    def test_leading_pair_needs_remainder(self):
        t = mp.im(mp.zetazero(1))
        Z = mp.siegelz(t)
        N = int(mp.floor(mp.sqrt(t/(2*mp.pi))))
        B = 2*mp.fsum(
            mp.cos(mp.siegeltheta(t)-t*mp.log(n))/mp.sqrt(n)
            for n in range(1, N+1)
        )
        self.assertLess(abs(Z), mp.mpf("1e-40"))
        self.assertGreater(abs(B), mp.mpf("0.1"))


if __name__ == "__main__":
    unittest.main()
