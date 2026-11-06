#!/usr/bin/env python3
"""Numerical checks for Chapter 16: two folds and theta-moment positivity.

No RH proof: verifies selected finite theta-moment coefficients and minors.
Uses finite theta sums and quadrature; output is not interval-certified.

Run: python experiments/two_fold_theta_positivity.py --digits 40
Dependency: mpmath
"""
from __future__ import annotations

import argparse
import json
import mpmath as mp


def xi(s):
    """Completed Riemann xi function (used only away from s=0,1)."""
    return mp.mpf("0.5") * s * (s - 1) * mp.power(
        mp.pi, -s / 2
    ) * mp.gamma(s / 2) * mp.zeta(s)


def phi(u, terms=8):
    """Numerically truncated, exact-form Jacobi-theta Fourier kernel."""
    u = abs(mp.mpf(u))
    a = mp.exp(2 * u)
    return mp.fsum(
        (
            4 * mp.pi**2 * k**4 * mp.exp(mp.mpf("4.5") * u)
            - 6 * mp.pi * k**2 * mp.exp(mp.mpf("2.5") * u)
        ) * mp.exp(-mp.pi * k * k * a)
        for k in range(1, terms + 1)
    )


def kernel_coefficient(n, terms=8):
    """a_n=2/(2n)! integral_0^infty u^(2n)*Phi(u) du.

    Integration ends at 6 for numerical efficiency. The exact defining
    formula is over [0,infinity); these are NOT rigorously enclosed values.
    """
    if n < 0 or terms < 1:
        raise ValueError("n >= 0 and terms >= 1 required")
    return 2 * mp.quad(
        lambda u: phi(u, terms) * u ** (2 * n),
        [0, mp.mpf("0.5"), 1, 2, 3, 6],
    ) / mp.factorial(2 * n)


def xi_coefficient(n):
    """Independent analytic-continuation derivative of xi at 1/2."""
    if n < 0:
        raise ValueError("n >= 0 required")
    return mp.diff(xi, mp.mpf("0.5"), 2 * n) / mp.factorial(2 * n)


def quartet_polynomial(q, a, t):
    """Quartic with the centered symmetry orbit +/-a +/-it as roots."""
    return q**4 + 2 * (t * t - a * a) * q**2 + (a * a + t * t)**2


def toeplitz_minor(coefficients, rows, columns):
    """Finite Toeplitz minor T[i,j]=a_(i-j), where a_k=0 for k<0."""
    if len(rows) != len(columns) or not rows:
        raise ValueError("row and column index lists must be equally sized")
    if min(rows + columns) < 0:
        raise ValueError("indices must be nonnegative")
    entries = []
    for i in rows:
        row = []
        for j in columns:
            k = i - j
            row.append(
                mp.mpf("0") if k < 0
                else coefficients[k] if k < len(coefficients)
                else (_ for _ in ()).throw(ValueError("more coefficients needed"))
            )
        entries.append(row)
    return mp.det(mp.matrix(entries))


def run(digits=40, max_n=3, terms=8):
    if digits < 25 or max_n < 3 or terms < 2:
        raise ValueError("require digits>=25, max_n>=3, terms>=2")
    mp.mp.dps = digits
    ak = [kernel_coefficient(n, terms) for n in range(max_n + 1)]
    cross_checks = [ak[n] - xi_coefficient(n) for n in range(max_n + 1)]
    a0, a1, a2, a3 = ak[:4]
    two_by_two = toeplitz_minor(ak, [1, 2], [0, 1])
    three_by_three = toeplitz_minor(ak, [1, 2, 3], [0, 1, 2])
    return {
        "status": "Finite numerical diagnostics; NOT proof of RH or PF_infinity",
        "digits": digits,
        "kernel_terms": terms,
        "quadrature_upper_endpoint": "6 (infinity in exact formula)",
        "theta_coefficients": [mp.nstr(c, 30) for c in ak],
        "kernel_minus_xi_derivative": [mp.nstr(x, 8) for x in cross_checks],
        "a1_squared_minus_a0_a2": mp.nstr(two_by_two, 30),
        "a2_squared_minus_a1_a3": mp.nstr(a2 * a2 - a1 * a3, 30),
        "three_by_three_minor": mp.nstr(three_by_three, 30),
        "quartic_merges_at_a_zero": bool(
            quartet_polynomial(1 + 2j, 0, 2)
            == ((1 + 2j) ** 2 + 4) ** 2
        ),
        "counterexample_q4_plus4_at_1_plus_i": mp.nstr(
            quartet_polynomial(1 + 1j, 1, 1), 5
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--digits", type=int, default=40)
    parser.add_argument("--max-n", type=int, default=3)
    parser.add_argument("--terms", type=int, default=8)
    args = parser.parse_args()
    print(json.dumps(run(args.digits, args.max_n, args.terms), indent=2))
