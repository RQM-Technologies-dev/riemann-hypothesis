"""Regression tests for Chapter 18. Passing tests do not prove RH."""
import importlib.util
import pathlib
import unittest
import mpmath as mp

PATH = pathlib.Path(__file__).resolve().parents[1] / "experiments" / "modular_symmetry_obstruction.py"
SPEC = importlib.util.spec_from_file_location("modular_symmetry_obstruction", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class ModularSymmetryObstructionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps = 35

    def test_explicit_nonreal_zero_inside_strip(self):
        z0 = M.explicit_offaxis_zero()
        self.assertLess(abs(mp.re(z0) - mp.pi), mp.mpf("1e-30"))
        self.assertTrue(0 < mp.im(z0) < mp.mpf("0.5"))
        self.assertLess(abs(M.shift_factor(z0)), mp.mpf("1e-30"))
        self.assertLess(abs(M.Xi(z0)*M.shift_factor(z0)), mp.mpf("1e-30"))

    def test_even_kernel_and_mellin_inversion(self):
        for u in (mp.mpf("0.1"), mp.mpf("1.3")):
            self.assertLess(abs(M.shifted_phi(u)-M.shifted_phi(-u)),
                            mp.mpf("1e-32"))
            self.assertGreater(M.shifted_phi(u), 0)
        for t in (mp.mpf("0.5"), mp.mpf(2), mp.mpf(5)):
            residual = (M.omega_from_shifted_phi(1/t)
                        - mp.sqrt(t)*M.omega_from_shifted_phi(t))
            self.assertLess(abs(residual), mp.mpf("1e-30"))

    def test_fourier_shift_factorization(self):
        z = mp.mpc("3.5", "0.23")
        residual = M.theta_psi_fourier(z) - M.Xi(z)*M.shift_factor(z)
        self.assertLess(abs(residual), mp.mpf("1e-30"))

    def test_gaussian_logconcavity_and_first_laguerre_not_sufficient(self):
        self.assertLess(M.gaussian_log_concavity_upper(), 0)
        self.assertGreater(M.gaussian_laguerre_bracket_min(),
                           mp.mpf("0.0059"))
        self.assertTrue(0 < mp.im(M.explicit_offaxis_zero()) < mp.mpf("0.5"))

    def test_spectral_average_strictly_increases(self):
        E0 = M.spectral_average_energy(0)
        E02 = M.spectral_average_energy(mp.mpf("0.2"))
        E05 = M.spectral_average_energy(mp.mpf("0.5"))
        self.assertTrue(0 < E0 < E02 < E05)
        self.assertGreater(M.spectral_average_growth(mp.mpf("0.2")), 0)
        self.assertGreater(M.spectral_average_growth(mp.mpf("0.5")), 0)
        self.assertLess(abs(E0-mp.mpf("2.00905988686130880796437343432")),
                        mp.mpf("1e-26"))

    def test_parameter_validation(self):
        with self.assertRaises(ValueError):
            M.explicit_offaxis_zero(mp.mpf("0.5"))
        with self.assertRaises(ValueError):
            M.shifted_phi(0, mp.mpf(0))
        with self.assertRaises(ValueError):
            M.omega_from_shifted_phi(-1)
        with self.assertRaises(ValueError):
            M.run(10)


if __name__ == "__main__":
    unittest.main()
