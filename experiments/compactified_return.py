#!/usr/bin/env python3
"""Conjugate return under a single inverse-stereographic/Cayley mapping.

A coordinate/analytic experiment, NOT an RH proof or physical Dirac dynamics.
Usage:
    python experiments/compactified_return.py --digits 60 --zeros 8 --scale 20
Dependency: mpmath (Python standard library otherwise).
"""
from __future__ import annotations

import argparse
import json
import mpmath as mp


def xi(s: mp.mpc) -> mp.mpc:
    """The entire completed Riemann zeta function."""
    return (
        mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2) * mp.zeta(s)
    )


def theta(t: mp.mpf, length: mp.mpf) -> mp.mpf:
    """Return polar meridian angle in [0,2*pi). Negative heights are return."""
    if length <= 0:
        raise ValueError("length must be positive")
    a = 2 * mp.atan(t / length)
    return a if a >= 0 else a + 2 * mp.pi


def q_polar(t: mp.mpf, length: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    """Coefficients in arbitrary quaternion slice: q/R = scalar + u*imag."""
    den = length * length + t * t
    return ((length * length - t * t) / den, 2 * length * t / den)


def polar_mirror_error(t: mp.mpf, length: mp.mpf) -> mp.mpf:
    a, b = q_polar(t, length)
    am, bm = q_polar(-t, length)
    return max(abs(a - am), abs(b + bm))


def xi_at_t(t: mp.mpf) -> mp.mpc:
    return xi(mp.mpc(mp.mpf("0.5"), t))


def run(digits: int = 60, zeros: int = 8, length: str = "20") -> dict:
    mp.mp.dps = digits
    L = mp.mpf(length)
    if L <= 0 or zeros < 1:
        raise ValueError("length > 0 and zeros >= 1 required")

    data = []
    for k in range(1, zeros + 1):
        t = mp.im(mp.zetazero(k))
        th = theta(t, L)
        q0, q1 = q_polar(t, L)
        z = xi_at_t(t)
        data.append({
            "index": k,
            "height": mp.nstr(t, 20),
            "theta_deg": mp.nstr(mp.degrees(th), 16),
            "conjugate_theta_deg": mp.nstr(mp.degrees(theta(-t, L)), 16),
            "unit_radius_squared_error": mp.nstr(abs(q0*q0 + q1*q1 - 1), 8),
            "xi_abs_at_zero": mp.nstr(abs(z), 8),
            "polar_conjugation_error": mp.nstr(polar_mirror_error(t, L), 8),
            "completed_conjugation_error": mp.nstr(
                abs(xi_at_t(-t) - mp.conj(z)), 8),
        })

    decay = []
    for t in (20, 40, 80, 160):
        decay.append({
            "height": t,
            "xi_abs": mp.nstr(abs(xi_at_t(mp.mpf(t))), 16),
            "distance_from_pole_degrees": mp.nstr(
                mp.degrees(mp.pi - theta(mp.mpf(t), L)), 12),
        })

    # Along TWO subsequences to infinity, n=2 harmonic tends to opposite signs.
    m = 20
    tplus = 2 * mp.pi * m / mp.log(2)
    tminus = (2*m + 1) * mp.pi / mp.log(2)
    hplus = mp.exp(-1j * tplus * mp.log(2)) / mp.sqrt(2)
    hminus = mp.exp(-1j * tminus * mp.log(2)) / mp.sqrt(2)
    harmonic = {
        "index": m,
        "plus_height": mp.nstr(tplus, 18),
        "minus_height": mp.nstr(tminus, 18),
        "plus_phase": [
            mp.nstr(mp.re(hplus), 16), mp.nstr(mp.im(hplus), 6)],
        "minus_phase": [
            mp.nstr(mp.re(hminus), 16), mp.nstr(mp.im(hminus), 6)],
        "claim": "The n=2 harmonic has no limiting phase at infinity",
    }

    samples = [
        mp.mpf("0"), mp.mpf("4"), mp.mpf("13"), mp.mpf("30")]
    symmetry = {
        "max_xi_even_error": mp.nstr(
            max(abs(xi_at_t(t)-xi_at_t(-t)) for t in samples), 8),
        "max_xi_imaginary_part": mp.nstr(
            max(abs(mp.im(xi_at_t(t))) for t in samples), 8),
        "max_polar_radius_error": mp.nstr(
            max(abs(sum(x*x for x in q_polar(t, L)) - 1)
                for t in samples), 8),
    }

    return {
        "experiment": "compactified_conjugate_return",
        "digits": digits,
        "scale_L": mp.nstr(L, 20),
        "symmetry": symmetry,
        "first_zeros": data,
        "pole_decay": decay,
        "single_harmonic_nonlimit": harmonic,
        "boundaries": [
            "This angular change of coordinates does not locate zeros.",
            "The completed xi decays at infinity, individual harmonic phases do not.",
            "No analytic passage through infinity or RH proof is claimed.",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--digits", type=int, default=60)
    parser.add_argument("--zeros", type=int, default=8)
    parser.add_argument("--scale", type=str, default="20")
    args = parser.parse_args()
    print(json.dumps(run(args.digits, args.zeros, args.scale), indent=2))
