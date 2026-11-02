#!/usr/bin/env python3
"""Exact positive distance sum at the zeta critical line; NOT a proof of RH.

Run: python experiments/w_distance_rh_criterion.py --scale 20 --count 200 --digits 40
Dependency: mpmath.
"""
from __future__ import annotations

import argparse
import json
import mpmath as mp


def xi_log_derivative_real(x: mp.mpf) -> mp.mpf:
    """Log derivative of completed xi, computed without zero locations; x > 1."""
    x = mp.mpf(x)
    if x <= 1:
        raise ValueError("numerical formula requires x > 1; use scale > 1/2")
    zeta_x = mp.zeta(x)
    return (
        1 / x + 1 / (x - 1) - mp.log(mp.pi) / 2
        + mp.digamma(x / 2) / 2 + mp.diff(mp.zeta, x) / zeta_x
    )


def w_coordinate(gamma: mp.mpf, L: mp.mpf) -> mp.mpf:
    """Global Cayley fourth-coordinate of an on-critical-line height."""
    L = mp.mpf(L)
    g = mp.mpf(gamma)
    if L <= 0:
        raise ValueError("scale must be positive")
    return (L**2 - g**2) / (L**2 + g**2)


def w_distance(gamma: mp.mpf, L: mp.mpf) -> mp.mpf:
    """Projection distance along w to the infinity pole; not geodesic distance."""
    L = mp.mpf(L)
    g = mp.mpf(gamma)
    return 2 * L**2 / (L**2 + g**2)


def off_line_pair_weight(delta: mp.mpf, gamma: mp.mpf, L: mp.mpf) -> mp.mpf:
    """Positive weight of an off-line reflection pair at fixed positive height."""
    L, delta, g = map(mp.mpf, (L, delta, gamma))
    if L < mp.mpf("0.5") or abs(delta) >= mp.mpf("0.5") or g <= 0:
        raise ValueError("need L >= 1/2, |delta| < 1/2, gamma > 0")
    return 2 * L * (
        (L - delta) / ((L - delta)**2 + g**2)
        + (L + delta) / ((L + delta)**2 + g**2)
    )


def off_line_cayley_radius_squared(delta: mp.mpf, gamma: mp.mpf, L: mp.mpf) -> mp.mpf:
    """Ambient |Q|^2/R^2 at s=1/2+delta+i gamma; not fixed to one off line."""
    L, delta, g = map(mp.mpf, (L, delta, gamma))
    return ((L + delta)**2 + g**2) / ((L - delta)**2 + g**2)


def run(digits: int = 40, count: int = 200, scale: str = "20") -> dict:
    if digits < 20 or count < 1:
        raise ValueError("need digits >=20, count >=1")
    mp.mp.dps = digits
    L = mp.mpf(scale)
    if L <= mp.mpf("0.5"):
        raise ValueError("evaluation requires scale > 1/2; theorem holds at 1/2")
    x = L + mp.mpf("0.5")
    target = L * xi_log_derivative_real(x)
    partial = mp.mpf(0)
    checkpoints = {1, 2, 4, 8, 16, 40, 100, 200, count}
    snapshots = []
    for n in range(1, count + 1):
        gamma = mp.im(mp.zetazero(n))
        partial += w_distance(gamma, L)
        if n in checkpoints:
            snapshots.append({
                "count": n,
                "last_height": mp.nstr(gamma, 24),
                "partial_w_distance": mp.nstr(partial, 32),
                "remaining_target_minus_partial": mp.nstr(target - partial, 32),
            })
    # Synthetic off-axis quartet demonstrates positive contribution, not an actual zeta zero.
    delta, gamma = mp.mpf("0.125"), mp.mpf("14.13472514173469379")
    positive_quartet = off_line_pair_weight(delta, gamma, L)
    centered_pair_form = L * (
        2 * L / (L**2 - (delta + 1j * gamma)**2)
        + 2 * L / (L**2 - (-delta + 1j * gamma)**2)
    )
    return {
        "experiment": "w_distance_critical_line_exhaustion",
        "status": "exact RH equivalence; NOT an RH proof",
        "working_digits": digits,
        "global_scale_L": mp.nstr(L, 20),
        "evaluation_point_x": mp.nstr(x, 20),
        "target_L_xi_prime_over_xi": mp.nstr(target, 36),
        "partial_sums_on_known_critical_line": snapshots,
        "hypothetical_off_line_quartet": {
            "is_actual_zeta_zero": False,
            "delta": mp.nstr(delta, 12),
            "gamma": mp.nstr(gamma, 20),
            "total_positive_weight": mp.nstr(positive_quartet, 30),
            "centered_product_form_difference": mp.nstr(abs(centered_pair_form - positive_quartet), 8),
            "paired_cayley_radius_squared_product": mp.nstr(
                off_line_cayley_radius_squared(delta, gamma, L)
                * off_line_cayley_radius_squared(-delta, gamma, L), 18
            ),
        },
        "critical_warning": (
            "A positive residual after any finite number of line zeros includes "
            "uncounted line zeros; it cannot be called an off-line contribution. "
            "The infinite residual is zero if and only if RH."
        ),
    }


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--scale", type=str, default="20")
    p.add_argument("--count", type=int, default=200)
    p.add_argument("--digits", type=int, default=40)
    args = p.parse_args()
    print(json.dumps(run(args.digits, args.count, args.scale), indent=2))
