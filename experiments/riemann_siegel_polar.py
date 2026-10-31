#!/usr/bin/env python3
"""Verify exact Gamma-phase Hardy Z factorization and conjugate harmonic sum.

The RS remainder is calculated as Z(t)-leading_pair_sum. It is not an
independent numerical prediction of the remainder or the zeta zeros.
Requires mpmath; run: python experiments/riemann_siegel_polar.py
"""
from __future__ import annotations

import json
import mpmath as mp


def run(digits: int = 50) -> dict:
    mp.mp.dps = digits
    heights = [mp.im(mp.zetazero(1)), mp.im(mp.zetazero(2))]
    heights.extend(mp.mpf(v) for v in (30, 50, 100, 200, 500))
    rows = []
    for t in heights:
        s = mp.mpc(mp.mpf("0.5"), t)
        N = int(mp.floor(mp.sqrt(t/(2*mp.pi))))
        vartheta = mp.siegeltheta(t)
        z = mp.siegelz(t)
        paired = mp.mpf(2) * mp.fsum(
            mp.cos(vartheta - t*mp.log(n))/mp.sqrt(n)
            for n in range(1, N + 1)
        )
        xi = (
            mp.mpf("0.5") * s*(s-1) * mp.power(mp.pi, -s/2)
            * mp.gamma(s/2) * mp.zeta(s)
        )
        A = (
            mp.mpf("0.5") * (t*t + mp.mpf("0.25"))
            * mp.power(mp.pi, -mp.mpf("0.25"))
            * abs(mp.gamma(mp.mpf("0.25") + 1j*t/2))
        )
        rows.append({
            "height": mp.nstr(t, 18),
            "count": N,
            "hardy_z": mp.nstr(z, 16),
            "paired_harmonics": mp.nstr(paired, 16),
            "rs_remainder_difference": mp.nstr(z - paired, 16),
            "gamma_envelope": mp.nstr(A, 16),
            "completed_xi": mp.nstr(mp.re(xi), 16),
            "xi_plus_AZ_error": mp.nstr(abs(xi + A*z), 7),
        })
    return {
        "digits": digits, "rows": rows,
        "method_note":
            "Remainder is exact Z minus finite conjugate-pair sum; "
            "no independent remainder evaluation."
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
