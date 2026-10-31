#!/usr/bin/env python3
"""Project known compactified xi onto zonal S^3 harmonics.

Projection is descriptive, NOT an independent derivation of zeros.
Requires: numpy, mpmath
Run: python experiments/s3_spectral_projection.py
"""
from __future__ import annotations

import argparse
import json

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss


def completed_xi_height(height: mp.mpf) -> mp.mpc:
    s = mp.mpc(mp.mpf("0.5"), height)
    return (
        mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s/2)
        * mp.gamma(s/2) * mp.zeta(s)
    )


def run(
    scale: float = 20.0,
    modes: int = 20,
    nodes: int = 140,
    digits: int = 45
) -> dict:
    if scale <= 0 or modes <= 0 or nodes <= 0:
        raise ValueError("Positive scale, modes, and quadrature nodes required")
    mp.mp.dps = digits
    x, weights = leggauss(nodes)
    angles = (x + 1) * np.pi / 2
    weights = weights * np.pi / 2
    values = []
    for theta in angles:
        height = mp.mpf(str(scale)) * mp.tan(mp.mpf(str(theta)) / 2)
        values.append(float(mp.re(completed_xi_height(height))))
    values = np.asarray(values)
    coeffs = [
        float(
            (2/np.pi) * np.sum(
                weights * values * np.sin(angles)
                * np.sin((K + 1) * angles)
            )
        ) for K in range(modes)
    ]
    expected_at_north = float(mp.re(completed_xi_height(mp.mpf("0"))))
    truncated_at_north = sum((K+1)*a for K, a in enumerate(coeffs))
    return {
        "scale_L": scale,
        "modes": modes,
        "quadrature_nodes": nodes,
        "mp_decimal_digits": digits,
        "coefficients": coeffs,
        "north_pole_exact": expected_at_north,
        "north_pole_truncated": truncated_at_north,
        "north_pole_absolute_error": abs(
            truncated_at_north - expected_at_north
        ),
        "interpretation":
            "Projection of the known xi field, not a prediction of zeta zeros",
    }


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--scale", type=float, default=20.0)
    p.add_argument("--modes", type=int, default=20)
    p.add_argument("--nodes", type=int, default=140)
    p.add_argument("--digits", type=int, default=45)
    args = p.parse_args()
    print(json.dumps(
        run(args.scale, args.modes, args.nodes, args.digits), indent=2
    ))
