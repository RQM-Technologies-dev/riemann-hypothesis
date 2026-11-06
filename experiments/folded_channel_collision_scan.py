#!/usr/bin/env python3
"""Finite-height mirror-channel diagnostics for Riemann Xi.

Exact definition: Xi(t+ia)=2[C(t,a)-1j*S(t,a)] with real C,S.
The code checks parity, root separation, the phase/Wronskian law, and
a positive-kernel counterexample. Finite scans CANNOT establish RH.

Run: python experiments/folded_channel_collision_scan.py --digits 45
Dependency: mpmath.
"""
from __future__ import annotations

import argparse
import json
import mpmath as mp


def xi(z):
    """Analytic continuation of the completed zeta function."""
    s = mp.mpf("0.5") + 1j * mp.mpc(z)
    return mp.mpf("0.5") * s * (s-1) * mp.power(
        mp.pi, -s / 2
    ) * mp.gamma(s / 2) * mp.zeta(s)


def phi(u, terms=8):
    """Numerical truncation of the exact Jacobi-theta Fourier kernel."""
    u = abs(mp.mpf(u))
    exp2u = mp.exp(2*u)
    return mp.fsum(
        (
            4*mp.pi**2*n**4*mp.exp(mp.mpf("4.5")*u)
            - 6*mp.pi*n**2*mp.exp(mp.mpf("2.5")*u)
        ) * mp.exp(-mp.pi*n*n*exp2u)
        for n in range(1, terms+1)
    )


def channels(t, a):
    """Returns C,S; not two independent wavefunctions."""
    value = xi(mp.mpc(t, a)) / 2
    return mp.re(value), -mp.im(value)


def theta_channels(t, a, terms=8):
    """Independent numerical integral with upper integration cutoff 6."""
    t, a = mp.mpf(t), mp.mpf(a)
    cuts = [0, mp.mpf("0.5"), 1, 2, 3, 6]
    C = mp.quad(
        lambda u: phi(u, terms)*mp.cos(t*u)*mp.cosh(a*u), cuts
    )
    S = mp.quad(
        lambda u: phi(u, terms)*mp.sin(t*u)*mp.sinh(a*u), cuts
    )
    return C, S


def phase_wronskian(t, a, function=xi):
    """W=C*S_t-S*C_t; W_a=|F'|^2-Re(F*conj(F'')), F=Xi/2.

    The ordinary z derivatives are used; partial derivatives C_t, S_t
    follow from the real and imaginary parts of F'.
    """
    z = mp.mpc(t, a)
    F = function(z)/2
    Fp = mp.diff(function, z)/2
    Fpp = mp.diff(function, z, 2)/2
    C, S = mp.re(F), -mp.im(F)
    Ct, St = mp.re(Fp), -mp.im(Fp)
    W = C*St-S*Ct
    W_a = abs(Fp)**2-mp.re(F*mp.conj(Fpp))
    modulus = C*C+S*S
    if modulus == 0:
        phase_slope = None
        outward_log_slope = None
    else:
        phase_slope = -W/modulus
        outward_log_slope = 2*W/modulus
    return {
        "W": W, "W_a": W_a, "phase_slope": phase_slope,
        "outward_log_slope": outward_log_slope,
    }


def scan_roots(a, component, start="8", end="45", step="0.25"):
    """Heuristic sign-bracket scan; not guaranteed to find all roots."""
    if component not in ("C", "S"):
        raise ValueError("component must be C or S")
    a = mp.mpf(a)
    start, end, step = mp.mpf(start), mp.mpf(end), mp.mpf(step)
    if not 0 < a <= mp.mpf("0.5") or start >= end or step <= 0:
        raise ValueError("invalid domain")
    index = 0 if component == "C" else 1
    previous = start
    old = channels(start, a)[index]
    roots = []
    x = start
    while x < end:
        x = min(x+step, end)
        current = channels(x, a)[index]
        if old*current < 0:
            root = mp.findroot(
                lambda t: channels(t, a)[index], (previous, x)
            )
            if (start < root < end and
                    (not roots or abs(root-roots[-1]) > mp.mpf("0.01"))):
                roots.append(root)
        previous, old = x, current
    return roots


def perturbation(z, epsilon=mp.mpf("0.49")):
    """Fourier transform of a shifted positive even kernel:
    Phi_e=Phi+e[Phi(u-1)+Phi(u+1)].
    """
    return xi(z)*(1+2*epsilon*mp.cos(z))


def run(digits=45, terms=8, end="45"):
    if digits < 25 or terms < 2:
        raise ValueError("at least 25 digits and 2 kernel terms required")
    mp.mp.dps = digits
    scans = []
    for a in ("0.05", "0.20", "0.49", "0.50"):
        roots_c = scan_roots(a, "C", end=end)
        roots_s = scan_roots(a, "S", end=end)
        merged = sorted(
            [(r, "C") for r in roots_c]+[(r, "S") for r in roots_s]
        )
        scans.append({
            "a": a,
            "C_roots": [mp.nstr(r, 18) for r in roots_c],
            "S_roots": [mp.nstr(r, 18) for r in roots_s],
            "observed_alternation": all(
                merged[i][1] != merged[i+1][1]
                for i in range(len(merged)-1)
            ),
            "smallest_nearest_C_S_root_gap": mp.nstr(
                min(abs(x-y) for x in roots_c for y in roots_s), 15
            ),
        })
    checks = []
    for t, a in (("3.3", "0.15"), ("14.1", "0.20"),
                 ("25.3", "0.49")):
        by_xi = channels(t, a)
        by_phi = theta_channels(t, a, terms)
        checks.append({
            "t": t, "a": a,
            "C_kernel_minus_xi": mp.nstr(by_phi[0]-by_xi[0], 8),
            "S_kernel_minus_xi": mp.nstr(by_phi[1]-by_xi[1], 8),
        })
    phases = []
    for t, a in (("13.7", "0.05"), ("21.5", "0.20"),
                 ("40", "0.49")):
        data = phase_wronskian(t, a)
        phases.append({
            "t": t, "a": a,
            "W": mp.nstr(data["W"], 18),
            "W_a": mp.nstr(data["W_a"], 18),
            "phase_slope": mp.nstr(data["phase_slope"], 18),
            "outward_log_slope": mp.nstr(
                data["outward_log_slope"], 18
            ),
            "phase_plus_half_growth": mp.nstr(
                data["phase_slope"]+data["outward_log_slope"]/2, 8
            ),
        })
    epsilon = mp.mpf("0.49")
    off_line_a = mp.acosh(1/(2*epsilon))
    z0 = mp.pi + 1j*off_line_a
    fake = lambda z: perturbation(z, epsilon)
    return {
        "status": "Numerical finite-height experiment, NOT RH proof",
        "digits": digits, "kernel_terms": terms,
        "t_domain": ["8", str(end)], "scan_step": "0.25",
        "theta_integral_upper_cutoff": 6,
        "scans": scans,
        "kernel_cross_checks": checks,
        "phase_identity_checks": phases,
        "positive_even_kernel_counterexample": {
            "epsilon": "0.49",
            "nonreal_zero_t": mp.nstr(mp.pi, 18),
            "nonreal_zero_a": mp.nstr(off_line_a, 18),
            "factor_at_zero": mp.nstr(
                1+2*epsilon*mp.cos(z0), 8
            ),
            "W_at_t_pi": [{
                "a": a,
                "W": mp.nstr(phase_wronskian(mp.pi, a, fake)["W"], 18)
            } for a in ("0.10", "0.20", "0.21", "0.25")],
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--digits", type=int, default=45)
    parser.add_argument("--terms", type=int, default=8)
    parser.add_argument("--end", default="45")
    args = parser.parse_args()
    print(json.dumps(run(args.digits, args.terms, args.end), indent=2))
