#!/usr/bin/env python3
"""Rigorous symbolic tail inequalities, with illustrative mpmath evaluations.

The proofs are in docs/10 and docs/11. Numerical quadrature is NOT certified
interval arithmetic. Published external inputs: Platt/Trudgian (2021) and
Bellotti/Wong (2025). This does NOT prove RH.

Run:
  python experiments/theta_tail_and_defect_bound.py --digits 40 --scale 20
  python experiments/theta_tail_and_defect_bound.py --digits 40 --scale 20 --count 200
"""
from __future__ import annotations

import argparse
import json
import mpmath as mp

A = mp.mpf("0.10076")
B = mp.mpf("0.24460")
C = mp.mpf("8.08344")
VERIFIED_H = mp.mpf("3e12")


def xi(s: mp.mpf) -> mp.mpf:
    s = mp.mpf(s)
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s/2) * mp.gamma(s/2) * mp.zeta(s)


def logxi_at_h(h: mp.mpf) -> mp.mpf:
    """log xi(1/2+2h), h>1/4, evaluated without overflowing Gamma."""
    h = mp.mpf(h)
    s = mp.mpf("0.5") + 2*h
    if s <= 1:
        raise ValueError("require xi real evaluation point >1")
    return (mp.log(s*(s-1)/2) - (s/2)*mp.log(mp.pi)
            + mp.loggamma(s/2) + mp.log(mp.zeta(s)))


def target_from_real_axis(L: mp.mpf) -> mp.mpf:
    """L xi'(1/2+L)/xi(1/2+L), with no zero input."""
    L = mp.mpf(L)
    if L <= mp.mpf("0.5"):
        raise ValueError("numerical formula uses L>1/2")
    s = mp.mpf("0.5") + L
    return L * (1/s + 1/(s-1) - mp.log(mp.pi)/2
                + mp.digamma(s/2)/2 + mp.diff(mp.zeta, s)/mp.zeta(s))


def phi_positive(v: mp.mpf, harmonic_cutoff: int = 8) -> mp.mpf:
    """First harmonic_cutoff positive terms of the true Jacobi-theta kernel."""
    v = mp.mpf(v)
    if v < 0:
        v = -v
    ev = mp.exp(2*v)
    return mp.fsum(
        (4*mp.pi**2*n**4*mp.exp(mp.mpf("4.5")*v)
         - 6*mp.pi*n**2*mp.exp(mp.mpf("2.5")*v))
        * mp.exp(-mp.pi*n*n*ev)
        for n in range(1, harmonic_cutoff+1)
    )


def theta_moment_target(L: mp.mpf, harmonic_cutoff: int = 8) -> mp.mpf:
    """Numerical check of exact theta hyperbolic moment; truncated for speed.

    Kernel harmonic sum truncated at n=harmonic_cutoff, integration to v=3;
    this value is not a certified enclosure.
    """
    L = mp.mpf(L)
    pieces = [0, mp.mpf("0.5"), 1, mp.mpf("1.5"), 2, 3]
    den = mp.quad(lambda v: phi_positive(v, harmonic_cutoff) * mp.cosh(L*v), pieces)
    num = mp.quad(lambda v: phi_positive(v, harmonic_cutoff) * v * mp.sinh(L*v), pieces)
    return L * num/den


def theta_jensen_tail_bound(T: mp.mpf, L: mp.mpf) -> mp.mpf:
    """Numerically evaluate the exact analytic B_Theta(T,L) upper-bound integral.

    Direct proof: Jensen + positive even Jacobi theta kernel; numerical
    integral value is illustrative, not interval certified.
    """
    T, L = mp.mpf(T), mp.mpf(L)
    if T <= 0 or L <= 0:
        raise ValueError("T,L positive")
    xizero = xi(mp.mpf("0.5"))
    cutoff = 1/T

    def f(u):
        if u == 0:
            return mp.mpf(0)
        return (u/(1+(L*u)**2)**2
                * (logxi_at_h(1/u) - mp.log(xizero)))
    return (2*L**2/mp.log(2)) * mp.quad(
        f, [0,cutoff/100,cutoff/10,cutoff]
    )


def zero_inverse_square_bound(H: mp.mpf) -> mp.mpf:
    """Exact upper formula from explicit published |N(T)-M(T)| theorem."""
    H = mp.mpf(H)
    if H < mp.e:
        raise ValueError("requires H>=e")
    main = (mp.log(H/(2*mp.pi))+1)/(2*mp.pi*H)
    error = (
        2*A*mp.log(H)+A/2 + 2*B*mp.log(mp.log(H))
        + B/(2*mp.log(H)) + 2*C
    ) / H**2
    return main + error


def w_distance(gamma: mp.mpf, L: mp.mpf) -> mp.mpf:
    gamma, L = mp.mpf(gamma), mp.mpf(L)
    return 2*L**2/(L**2+gamma**2)


def positive_kernel_countermodel(t: mp.mpc, a: mp.mpf = 1,
                                 sigma1: mp.mpf = 1,
                                 sigma2: mp.mpf = 2) -> mp.mpc:
    """Fourier transform of positive even [box * mixture-of-Gaussians] kernel."""
    a, sigma1, sigma2 = mp.mpf(a), mp.mpf(sigma1), mp.mpf(sigma2)
    return (mp.sin(a*t)/(a*t) if t else mp.mpf(1)) * (
        mp.exp(-sigma1**2*t**2/2) + mp.exp(-sigma2**2*t**2/2)
    )/2


def run(digits: int=40, scale: str="20", count: int=8) -> dict:
    if digits < 25 or count < 1:
        raise ValueError("need digits>=25 and count>=1")
    mp.mp.dps = digits
    L=mp.mpf(scale)
    if L <= mp.mpf("0.5"):
        raise ValueError("require scale > 1/2")
    target=target_from_real_axis(L)
    theta_val=theta_moment_target(L)
    gammas=[mp.im(mp.zetazero(n)) for n in range(1,count+1)]
    last=gammas[-1]
    partial=mp.fsum(w_distance(g,L) for g in gammas)
    remaining=target-partial
    p_finite=zero_inverse_square_bound(last)
    p_verified=zero_inverse_square_bound(VERIFIED_H)
    j_finite=theta_jensen_tail_bound(last,L)
    j_verified=theta_jensen_tail_bound(VERIFIED_H,L)
    off_max=2*L*(L+mp.mpf("0.5"))*p_verified
    sig1,sig2=mp.mpf(1),mp.mpf(2)
    offroot=mp.sqrt(-2j*mp.pi/(sig2**2-sig1**2))
    def fmt(v,n=28):return mp.nstr(v,n)
    return {
        "title":"Jacobi theta Jensen + published finite-height zero-defect bounds",
        "status":"Exact inequalities from published facts; numerical evaluation NOT interval-certified; NOT RH proof",
        "precision_digits":digits, "scale_L":fmt(L), "count":count,
        "last_known_critical_zero_height":fmt(last),
        "xi_log_derivative_target":fmt(target),
        "theta_hyperbolic_moment_approximation":fmt(theta_val),
        "theta_moment_vs_target_error":fmt(abs(theta_val-target),8),
        "first_n_on_line_w_distance_sum":fmt(partial),
        "target_minus_first_n":fmt(remaining),
        "jensen_theta_bound_after_n":fmt(j_finite),
        "published_all_zero_inverse_square_bound_after_n":fmt(p_finite),
        "published_on_line_tail_bound_after_n":fmt(2*L**2*p_finite),
        "verified_height":fmt(VERIFIED_H),
        "jensen_theta_tail_bound_after_verified_height":fmt(j_verified),
        "published_all_zero_inverse_square_bound_after_verified_height":fmt(p_verified),
        "on_line_tail_above_verified_height_upper":fmt(2*L**2*p_verified),
        "off_line_defect_upper":fmt(off_max),
        "on_line_tail_after_n_lower":fmt(max(mp.mpf(0),remaining-off_max)),
        "on_line_tail_after_n_upper":fmt(remaining),
        "positive_even_kernel_counterexample": {
            "nonreal_zero": [fmt(mp.re(offroot),18),fmt(mp.im(offroot),18)],
            "fourier_value_at_nonreal_zero_abs":fmt(
                abs(positive_kernel_countermodel(offroot)),12),
            "real_zero_at_pi_abs":fmt(
                abs(positive_kernel_countermodel(mp.pi)),12)
        },
        "interpretation":(
            "The positivity/Jensen tail bound proves convergence, not RH. "
            "The extremely small possible off-line defect comes from previously "
            "published zero verification to 3e12 and explicit total zero counts. "
            "Unknown heights above 3e12 cannot be assumed zero-free."
        ),
        "sources": [
            "https://math.ucdavis.edu/~romik/data/uploads/papers/riemannxi.pdf",
            "https://doi.org/10.1112/blms.12460",
            "https://doi.org/10.1090/mcom/4133"
        ]
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--digits",type=int,default=40)
    parser.add_argument("--scale",type=str,default="20")
    parser.add_argument("--count",type=int,default=8)
    args=parser.parse_args()
    print(json.dumps(run(args.digits,args.scale,args.count),indent=2))
