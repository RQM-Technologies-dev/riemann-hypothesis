#!/usr/bin/env python3
"""Find critical-line zero latitudes using the exact Jacobi-theta cosine integral.

This solves xi(1/2+it)=0 in a SINGLE global polar coordinate w (L=20).
The known zero list is NOT given to the root finder; it is used only after
solution for verification. This does not prove RH or exclude off-axis zeros.

pip install numpy mpmath
python experiments/theta_kernel_w_roots.py --count 3
python experiments/theta_kernel_w_roots.py --count 8 --digits 50
"""
from __future__ import annotations

import argparse
import json
from math import pi

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss


def theta_kernel(v: mp.mpf, nterms: int = 8) -> mp.mpf:
    """Phi(v) in xi(1/2+it) = 2 int_0^infinity Phi(v) cos(tv) dv."""
    exp2v = mp.exp(2*v)
    a = mp.exp(mp.mpf("4.5")*v)
    b = mp.exp(mp.mpf("2.5")*v)
    return mp.fsum(
        (4*mp.pi**2*n**4*a - 6*mp.pi*n**2*b)
        * mp.exp(-mp.pi*n**2*exp2v)
        for n in range(1, nterms+1)
    )


def cosine_integral(t: mp.mpf, nterms: int = 8) -> mp.mpf:
    """High-precision theta Fourier cosine integral.

    At v=0, the omitted n>=9 terms have exp(-81*pi) suppression.
    Past v=2.5, the kernel is super-exponentially small.
    """
    breaks = (mp.mpf("0"), mp.mpf(".5"), mp.mpf("1"),
              mp.mpf("1.75"), mp.mpf("2.5"))
    return 2*mp.fsum(
        mp.quad(lambda v: theta_kernel(v, nterms)*mp.cos(t*v),
                [breaks[i], breaks[i+1]])
        for i in range(len(breaks)-1)
    )


def xi_direct(t: mp.mpf) -> mp.mpc:
    s = mp.mpc(mp.mpf(".5"), t)
    return s*(s-1)/2 * mp.power(mp.pi, -s/2)*mp.gamma(s/2)*mp.zeta(s)


def fast_brackets(roots: int, upper: float = 46, step: float = .2):
    """Float quadrature ONLY for initial sign brackets: no zero list."""
    z, weights = leggauss(240)
    v = 1.5*(z+1)  # [0,3]
    weights = 1.5*weights
    n = np.arange(1, 9, dtype=np.float64)[:,None]
    exp2v = np.exp(2*v)[None,:]
    terms = (
        (4*pi*pi*n**4*np.exp(4.5*v)[None,:]
         - 6*pi*n**2*np.exp(2.5*v)[None,:])
        * np.exp(-pi*n**2*exp2v)
    )
    weighted = weights*np.sum(terms, axis=0)

    def f_float(t: float) -> float:
        return 2*float(np.dot(weighted, np.cos(t*v)))

    samples = np.arange(0, upper+step/2, step)
    vals = [f_float(t) for t in samples]
    brackets = []
    for k in range(len(samples)-1):
        if vals[k]*vals[k+1] < 0:
            brackets.append((float(samples[k]), float(samples[k+1])))
            if len(brackets) >= roots:
                break
    if len(brackets) < roots:
        raise ValueError("Not enough sign changes; increase scan upper bound")
    return brackets


def solve(count: int = 3, digits: int = 50, scale_L: str = "20") -> dict:
    if not (1 <= count <= 8):
        raise ValueError("Validated root-discovery window: count 1..8")
    if digits < 25:
        raise ValueError("Use >=25 digits to resolve high-frequency small zeros")
    mp.mp.dps = digits
    L = mp.mpf(scale_L)
    if L <= 0:
        raise ValueError("Global stereographic scale L must be positive")
    data = []
    for k, (aa, bb) in enumerate(fast_brackets(count), 1):
        mid = mp.mpf(str((aa+bb)/2))
        # Root finder receives a sign bracket, NEVER an observed zero height.
        t = mp.findroot(
            cosine_integral,
            (mid-mp.mpf(".06"), mid+mp.mpf(".06")),
            solver="secant",
            tol=mp.mpf(10)**(-digits+8),
            maxsteps=20
        )
        w = (L*L-t*t)/(L*L+t*t)
        theta = 2*mp.atan(t/L)
        r = mp.sin(theta)
        reference = mp.im(mp.zetazero(k))  # POST HOC verification only
        data.append({
            "index": k,
            "height_solved_from_integral": mp.nstr(t, digits-5),
            "w_from_global_mapping": mp.nstr(w, digits-5),
            "theta_degrees": mp.nstr(mp.degrees(theta), 17),
            "return_theta_degrees": mp.nstr(mp.degrees(2*mp.pi-theta), 17),
            "three_coordinate_sphere_radius": mp.nstr(r, 17),
            "ambient_unit_sphere_error": mp.nstr(abs(w*w+r*r-1), 6),
            "integral_residual": mp.nstr(cosine_integral(t), 7),
            "known_zero_validation_error": mp.nstr(t-reference, 7),
        })
    return {
        "title": "Fixed Jacobi-theta kernel selects critical-line zero latitudes",
        "digits": digits,
        "global_L": mp.nstr(L, 12),
        "root_count": count,
        "results": data,
        "claim_boundary":
            "This is xi(1/2+it) in different coordinates; it does not "
            "rule out off-axis zeros and does not prove RH.",
        "pole_boundary":
            "w=-1 is excluded: the compactified infinity pole is a "
            "spurious limiting zero of the completed amplitude."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--count", type=int, default=3)
    parser.add_argument("--digits", type=int, default=50)
    parser.add_argument("--scale", type=str, default="20")
    args = parser.parse_args()
    print(json.dumps(solve(args.count, args.digits, args.scale), indent=2))
