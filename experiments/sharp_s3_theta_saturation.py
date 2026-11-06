#!/usr/bin/env python3
"""Sharp S3 radial Jensen bound: exact equalities and numerical stress tests.

The full theta-only saturation identity is equivalent to RH and is UNPROVED.
This script computes xi's local second moment, verifies an off-axis toy
quartet using an independently integrated radial Jensen expression,
and computes an exact extra deficit for a positive even theta perturbation.

Run: python experiments/sharp_s3_theta_saturation.py --digits 40
Requires: mpmath
"""
from __future__ import annotations

import argparse
import json
import mpmath as mp


def xi(s):
    return (s * (s - 1) / 2) * mp.power(mp.pi, -s/2) * mp.gamma(s/2) * mp.zeta(s)


def xi_theta_local_moment():
    """For f(w)=xi(1/2+w), return f''(0)/(4 f(0))."""
    center = mp.mpf("0.5")
    return mp.diff(xi, center, 2) / (4 * xi(center))


def quartic(z, a, t):
    """Intrinsic real polynomial normalized to one at z=0."""
    a, t = mp.mpf(a), mp.mpf(t)
    r2 = a*a + t*t
    if r2 <= 0:
        raise ValueError("zero radius")
    return 1 + 2*(t*t-a*a)*z*z/(r2*r2) + z**4/(r2*r2)


def quartet_radial_jensen(radius, a, t):
    """M2(R)-log f(0) for the complete off-axis quartet, f(0)=1."""
    a, t = mp.mpf(a), mp.mpf(t)
    r = mp.sqrt(a*a+t*t)
    radius = mp.mpf(radius)
    return 4*mp.log(radius/r) if radius > r else mp.mpf("0")


def toy_radial_integral(a, t):
    """Independent quadrature of radial Jensen I for one off-axis quartet."""
    a, t = mp.mpf(a), mp.mpf(t)
    r = mp.sqrt(a*a+t*t)
    return mp.quad(
        lambda R: quartet_radial_jensen(R, a, t)/R**3,
        [r, 2*r, 4*r, mp.inf],
    )


def toy_local_moment(a, t):
    """quartic''(0)/(4 quartic(0))."""
    a, t = mp.mpf(a), mp.mpf(t)
    r2 = a*a+t*t
    return (t*t-a*a)/(r2*r2)


def theta_perturbation_extra_gap(epsilon=mp.mpf("0.49")):
    """Explicit off-line contribution of Xi(z)*(1+2eps*cos(z)).

    theta perturbation: Phi_eps(u)=Phi(u)+eps[Phi(u-1)+Phi(u+1)].
    Does NOT establish any off-line zero of original Xi.
    """
    epsilon = mp.mpf(epsilon)
    if not 0 < epsilon < mp.mpf("0.5"):
        raise ValueError("require 0<epsilon<1/2")
    b = mp.acosh(1/(2*epsilon))
    series = mp.nsum(
        lambda k: 2*b*b/(b*b+(2*k+1)**2*mp.pi**2)**2,
        [0, mp.inf],
    )
    closed_form = mp.tanh(b/2)/(4*b)-mp.sech(b/2)**2/8
    return b, series, closed_form


def run(digits=40):
    if digits < 25:
        raise ValueError("digits >= 25 required")
    mp.mp.dps = digits
    a, t = mp.mpf("0.2"), mp.mpf("14.13")
    I = toy_radial_integral(a, t)
    local = toy_local_moment(a, t)
    gap = 2*a*a/(a*a+t*t)**2
    b, series, closed = theta_perturbation_extra_gap()
    return {
        "status": "RH-equivalent theta equality remains UNPROVED",
        "precision_digits": digits,
        "original_xi_fpp_over_4f": mp.nstr(xi_theta_local_moment(), 35),
        "toy_quartet": {
            "a": "0.2", "t": "14.13",
            "independent_radial_Jensen_integral": mp.nstr(I, 35),
            "local_quadratic_coefficient": mp.nstr(local, 35),
            "observed_difference": mp.nstr(I-local, 35),
            "exact_positive_fold_penalty_coefficient": mp.nstr(gap, 35),
            "difference_minus_formula": mp.nstr(I-local-gap, 10),
        },
        "modified_positive_even_theta_kernel": {
            "epsilon": "0.49",
            "off_axis_parameter_b": mp.nstr(b, 35),
            "extra_gap_from_zero_sum": mp.nstr(series, 35),
            "extra_gap_closed_formula": mp.nstr(closed, 35),
            "cross_check_difference": mp.nstr(series-closed, 10),
            "warning": "Modified kernel only; NOT a counterexample to RH.",
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--digits", type=int, default=40)
    args = parser.parse_args()
    print(json.dumps(run(args.digits), indent=2))
