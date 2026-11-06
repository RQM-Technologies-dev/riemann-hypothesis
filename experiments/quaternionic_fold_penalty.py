#!/usr/bin/env python3
"""Exact S^3 reflected-zero folding penalty and independent angular quadrature.

For an intrinsic real-coefficient quartet polynomial, normalized quaternionic
S^3 log-mean reduces to (2/pi) integral sin^2(theta) log|p(R exp(i theta))|.
The positive penalty compares an off-axis quartet to an artificial twice-folded
radial reference. This is NOT an RH proof or an interval certificate.

Run: python experiments/quaternionic_fold_penalty.py --digits 40
Dependency: mpmath
"""
from __future__ import annotations

import argparse
import json
import mpmath as mp


def folded_reference(z, a, t):
    """Double conjugate-pair placed at imaginary height r=sqrt(a*a+t*t)."""
    a, t = mp.mpf(a), mp.mpf(t)
    r2 = a*a + t*t
    if not r2 > 0:
        raise ValueError("nonzero radial distance required")
    return (1 + z*z/r2)**2


def reflected_quartet(z, a, t):
    """Real-coefficient quartic for +/-w and +/-conj(w), normalized at 0.

    Algebraic real coefficients ensure a well-defined intrinsic quaternionic
    extension. We do NOT interpret nonreal individual factors as H polynomials.
    """
    a, t = mp.mpf(a), mp.mpf(t)
    r2 = a*a + t*t
    if not r2 > 0:
        raise ValueError("nonzero radial distance required")
    z2 = z*z
    return 1 + 2*(t*t-a*a)*z2/(r2*r2) + z2*z2/(r2*r2)


def spherical_mean_log(f, R):
    """Normalized four-dimensional sphere average of intrinsic f.

    Assumes no zeros on the sphere; the angular integral has log singularities
    at zero radii, whose extension requires separate care.
    """
    R = mp.mpf(R)
    if not R > 0:
        raise ValueError("R must be positive")
    cuts = [0, mp.pi/4, mp.pi/2, 3*mp.pi/4, mp.pi]
    return (2/mp.pi)*mp.quad(
        lambda th: mp.sin(th)**2 * mp.log(abs(f(R*mp.exp(1j*th)))),
        cuts,
    )


def folding_penalty(R, a, t):
    """Analytic nonnegative S^3 log-mean difference for reflected quartet."""
    R, a, t = mp.mpf(R), mp.mpf(a), mp.mpf(t)
    r2 = a*a + t*t
    if not R > 0 or not r2 > 0:
        raise ValueError("require R>0 and a*a+t*t>0")
    if R*R <= r2:
        return 2*a*a*R*R/(r2*r2)
    return 2*a*a/(R*R)


def xi_centered(z):
    """f(z)=xi(1/2+z); evaluate away from removable poles in quadrature."""
    s = mp.mpf("0.5") + z
    return (s*(s-1)/2) * mp.power(
        mp.pi, -s/2
    ) * mp.gamma(s/2)*mp.zeta(s)


def small_radius_xi_mean(R):
    """Exact formula while the disk |z|<=R is zero-free."""
    R = mp.mpf(R)
    f0 = xi_centered(mp.mpf("0"))
    return mp.log(f0)-R*R*mp.diff(xi_centered, 0, 2)/(4*f0)


def run(digits=40):
    if digits < 25:
        raise ValueError("digits>=25 required")
    mp.mp.dps = digits
    cases = [
        ("0.25", "1.5", "0.8"),
        ("0.25", "1.5", "2.0"),
        ("0.20", "14.13", "10.0"),
        ("0.20", "14.13", "17.0"),
        ("0.0", "1.5", "0.8"),
    ]
    checks = []
    for sa, st, sR in cases:
        a, t, R = map(mp.mpf, (sa, st, sR))
        off = spherical_mean_log(
            lambda z: reflected_quartet(z, a, t), R
        )
        folded = spherical_mean_log(
            lambda z: folded_reference(z, a, t), R
        )
        observed = off-folded
        formula = folding_penalty(R, a, t)
        checks.append({
            "a": sa, "t": st, "R": sR,
            "integrated_difference": mp.nstr(observed, 30),
            "formula": mp.nstr(formula, 30),
            "quadrature_minus_formula": mp.nstr(observed-formula, 8),
        })
    xi_checks = []
    for sR in ("1", "3"):
        R = mp.mpf(sR)
        observed = spherical_mean_log(xi_centered, R)
        formula = small_radius_xi_mean(R)
        xi_checks.append({
            "R": sR,
            "integrated_mean": mp.nstr(observed, 30),
            "exact_expression": mp.nstr(formula, 30),
            "quadrature_minus_expression": mp.nstr(observed-formula, 8),
        })
    return {
        "status": "Finite precision checks of an exact fold-comparison identity; NOT RH proof",
        "digits": digits,
        "quaternionic_sphere_measure": "(2/pi)*sin(theta)^2 dtheta",
        "reflected_quartet_checks": checks,
        "actual_centered_xi_zero_free_radius_checks": xi_checks,
        "caution": (
            "Folded reference is artificially constructed from hypothetical "
            "quartet locations. Its existence and positive penalty do NOT "
            "imply theta forces those quartets to coalesce."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--digits", type=int, default=40)
    args = parser.parse_args()
    print(json.dumps(run(args.digits), indent=2))
