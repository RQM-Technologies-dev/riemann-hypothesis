#!/usr/bin/env python3
"""Explicit no-go for RH inference from theta modular inversion alone.

The Jacobi-theta kernel is convolved with a positive even three-atom measure.
The resulting Fourier transform has explicitly known nonreal zeros despite
positivity, evenness, rapid decay, and the weight-1/2 inversion symmetry.

The Plancherel computation also gives an unconditional averaged growth law.
No RH proof; finite numerical checks are not interval-certified.

Run: python experiments/modular_symmetry_obstruction.py --digits 35
Dependency: mpmath
"""
from __future__ import annotations

import argparse
import json
import mpmath as mp


def xi(s):
    """Completed xi, used away from the removable endpoints 0 and 1."""
    return (mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2)
            * mp.gamma(s / 2) * mp.zeta(s))


def Xi(z):
    return xi(mp.mpf("0.5") + 1j * z)


def phi(u, terms=8):
    """Numerical theta sum, on u>=0 via exact evenness.

    The analytic theorem uses the infinite Jacobi-theta series.
    """
    u = abs(mp.mpf(u))
    a = mp.exp(2 * u)
    return mp.fsum(
        (4 * mp.pi**2 * k**4 * mp.exp(mp.mpf("4.5") * u)
         - 6 * mp.pi * k*k * mp.exp(mp.mpf("2.5") * u))
        * mp.exp(-mp.pi * k*k * a)
        for k in range(1, terms + 1)
    )


def shifted_phi(u, epsilon=mp.mpf("0.49"), b=mp.mpf(1), terms=8):
    epsilon, b = mp.mpf(epsilon), mp.mpf(b)
    if not 0 < epsilon < mp.mpf("0.5") or b <= 0:
        raise ValueError("require 0<epsilon<1/2 and b>0")
    return phi(u, terms) + epsilon * (phi(u-b, terms) + phi(u+b, terms))


def omega_from_shifted_phi(t, epsilon=mp.mpf("0.49"), b=1, terms=8):
    """Exact structural identity Omega(1/t)=sqrt(t)*Omega(t)."""
    t = mp.mpf(t)
    if t <= 0:
        raise ValueError("t>0")
    return (mp.mpf("0.5") * t**(-mp.mpf("0.25"))
            * shifted_phi(mp.log(t) / 2, epsilon, b, terms))


def shift_factor(z, epsilon=mp.mpf("0.49"), b=1):
    return 1 + 2 * mp.mpf(epsilon) * mp.cos(mp.mpf(b) * z)


def explicit_offaxis_zero(epsilon=mp.mpf("0.49"), b=1):
    epsilon, b = mp.mpf(epsilon), mp.mpf(b)
    if not 0 < epsilon < mp.mpf("0.5") or b <= 0:
        raise ValueError("invalid parameters")
    return mp.pi / b + 1j * mp.acosh(1 / (2 * epsilon)) / b


def theta_psi_fourier(z, epsilon=mp.mpf("0.49"), b=1, terms=8):
    return 2 * mp.quad(
        lambda u: shifted_phi(u, epsilon, b, terms) * mp.cos(z*u),
        [0, mp.mpf("0.5"), 1, 2, 3, 5],
    )


def gaussian_laguerre_bracket_min(epsilon=mp.mpf("0.49"), sigma=8):
    """Lower bound for (F'^2-F*F'')/exp(-sigma^2*x^2)."""
    epsilon, sigma = mp.mpf(epsilon), mp.mpf(sigma)
    if not 0 < epsilon < mp.mpf("0.5") or sigma <= 0:
        raise ValueError("invalid parameters")
    return 4*epsilon**2 - 2*epsilon + sigma**2 * (1-2*epsilon)**2


def gaussian_log_concavity_upper(sigma=8, b=1):
    """Uniform upper bound for second derivative of log Gaussian mixture."""
    sigma, b = mp.mpf(sigma), mp.mpf(b)
    if sigma <= 0 or b <= 0:
        raise ValueError("positive sigma and b required")
    return -1/sigma**2 + b**2/sigma**4


def spectral_average_energy(y, terms=8):
    """E(y)=integral_R |Xi(x+i*y)|^2 dx by Plancherel."""
    y = mp.mpf(y)
    return 4 * mp.pi * mp.quad(
        lambda u: phi(u, terms)**2 * mp.cosh(2*y*u),
        [0, mp.mpf("0.5"), 1, 2.5],
    )


def spectral_average_growth(y, terms=8):
    """E'(y), strictly positive for y>0 for the exact kernel."""
    y = mp.mpf(y)
    return 8 * mp.pi * mp.quad(
        lambda u: u*phi(u, terms)**2 * mp.sinh(2*y*u),
        [0, mp.mpf("0.5"), 1, 2.5],
    )


def run(digits=35, terms=8):
    if digits < 25 or terms < 3:
        raise ValueError("require digits>=25, terms>=3")
    mp.mp.dps = digits
    epsilon = mp.mpf("0.49")
    b = mp.mpf(1)
    z0 = explicit_offaxis_zero(epsilon, b)
    sample_z = mp.mpc("3.5", "0.23")
    fft_err = (theta_psi_fourier(sample_z, epsilon, b, terms)
               - Xi(sample_z)*shift_factor(sample_z, epsilon, b))
    modular_res = []
    for t_str in ("0.5", "1", "2", "5"):
        t = mp.mpf(t_str)
        residual = (omega_from_shifted_phi(1/t, epsilon, b, terms)
                    - mp.sqrt(t)*omega_from_shifted_phi(t, epsilon, b, terms))
        modular_res.append({"t": t_str, "residual": mp.nstr(residual, 10)})
    return {
        "status": "Rigorous obstruction and averaged positivity; NOT RH proof",
        "precision_digits": digits,
        "theta_terms_numerical": terms,
        "epsilon": "0.49",
        "shift_b": "1",
        "constructed_nonreal_zero": {
            "real": mp.nstr(mp.re(z0), 30),
            "imag": mp.nstr(mp.im(z0), 30),
            "inside_xi_half_strip": bool(0 < abs(mp.im(z0)) < mp.mpf("0.5")),
            "factor_at_zero_abs": mp.nstr(abs(shift_factor(z0,epsilon,b)), 10),
        },
        "shifted_fourier_factorization_error_abs": mp.nstr(abs(fft_err), 10),
        "mellin_inversion_residuals": modular_res,
        "spectral_average": {
            "E_y0": mp.nstr(spectral_average_energy(0,terms), 30),
            "E_y02": mp.nstr(spectral_average_energy(mp.mpf("0.2"),terms), 30),
            "dE_y02": mp.nstr(spectral_average_growth(mp.mpf("0.2"),terms), 30),
            "E_y05": mp.nstr(spectral_average_energy(mp.mpf("0.5"),terms), 30),
            "dE_y05": mp.nstr(spectral_average_growth(mp.mpf("0.5"),terms), 30),
            "meaning": "Unconditional spectral-height average growth, not pointwise RH growth",
        },
        "gaussian_counterexample": {
            "sigma": "8", "epsilon": "0.49", "shift_b": "1",
            "strict_log_concavity_upper_bound": mp.nstr(
                gaussian_log_concavity_upper(), 20),
            "global_first_laguerre_bracket_lower_bound": mp.nstr(
                gaussian_laguerre_bracket_min(), 20),
            "same_explicit_nonreal_zero": True,
            "caveat": "Gaussian Fourier entire function has order 2, unlike Xi.",
        },
        "interpretation": (
            "Positivity, evenness, theta-like decay and weight-1/2 inversion "
            "cannot force all Fourier zeros real; actual theta arithmetic "
            "structure is not captured by this counterexample."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--digits", type=int, default=35)
    parser.add_argument("--terms", type=int, default=8)
    args = parser.parse_args()
    print(json.dumps(run(args.digits, args.terms), indent=2))
