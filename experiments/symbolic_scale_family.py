#!/usr/bin/env python3
"""Scale-covariant RH-equivalent zero-distance diagnostics, NOT a proof of RH.

All mathematical formulas use free symbolic L>0. The CLI merely selects a
few demonstration values; zero heights never change when L changes.

python experiments/symbolic_scale_family.py --scales 0.1,0.5,1,5,20,100 --count 40
Dependency: mpmath.
"""
from __future__ import annotations

import argparse
import json
import mpmath as mp

A = mp.mpf("0.10076")
B = mp.mpf("0.24460")
C = mp.mpf("8.08344")
VERIFIED_HEIGHT = mp.mpf("3e12")


def xi(s: mp.mpf) -> mp.mpf:
    """Completed xi on real axis; removable s=1 singularity resolved."""
    s = mp.mpf(s)
    if s == 1:
        return mp.mpf("0.5")
    return mp.mpf("0.5")*s*(s-1)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)


def log_derivative(s: mp.mpf) -> mp.mpf:
    """xi'(s)/xi(s) for s>1/2; valid on BOTH sides of the zeta pole."""
    s = mp.mpf(s)
    if s <= mp.mpf("0.5"):
        raise ValueError("must have s>1/2, equivalent to L>0")
    if s == 1:
        # Laurent series for zeta near 1 cancels the 1/(s-1) term.
        # xi'(1)/xi(1)=1+EulerGamma/2-log(2)-log(pi)/2.
        return 1 + mp.euler/2 - mp.log(2) - mp.log(mp.pi)/2
    return (1/s + 1/(s-1) - mp.log(mp.pi)/2
            + mp.digamma(s/2)/2 + mp.diff(mp.zeta,s)/mp.zeta(s))


def total_target(L: mp.mpf) -> mp.mpf:
    L=mp.mpf(L)
    if L <= 0:
        raise ValueError("L must be positive")
    return L*log_derivative(mp.mpf("0.5")+L)


def w(L: mp.mpf, gamma: mp.mpf) -> mp.mpf:
    L,gamma=mp.mpf(L),mp.mpf(gamma)
    if L <= 0:
        raise ValueError("L must be positive")
    return (L*L-gamma*gamma)/(L*L+gamma*gamma)


def on_line_weight(L: mp.mpf, gamma: mp.mpf) -> mp.mpf:
    L,gamma=mp.mpf(L),mp.mpf(gamma)
    if L <= 0:
        raise ValueError("L must be positive")
    return 2*L**2/(L**2+gamma**2)


def quartet_factor(L: mp.mpf, delta: mp.mpf, gamma: mp.mpf) -> mp.mpf:
    """Conjugate off-line 4-zero product factor, greater than 1 for gamma>|delta|."""
    L,delta,gamma=map(mp.mpf,(L,delta,gamma))
    if L <= 0 or not 0 < abs(delta) < mp.mpf("0.5") or gamma <= abs(delta):
        raise ValueError("Need L>0, 0<|delta|<1/2, gamma>|delta|")
    return 1+(2*(gamma**2-delta**2)*L**2+L**4)/(gamma**2+delta**2)**2


def quartet_weight(L: mp.mpf, delta: mp.mpf, gamma: mp.mpf) -> mp.mpf:
    """Whole positive-height off-axis reflected PAIR contribution to D(L)."""
    L,delta,gamma=map(mp.mpf,(L,delta,gamma))
    if L <= 0 or not 0 < abs(delta) < mp.mpf("0.5") or gamma <= abs(delta):
        raise ValueError("Need L>0, 0<|delta|<1/2, gamma>|delta|")
    return 4*L**2*(L**2+gamma**2-delta**2)/(
        ((L-delta)**2+gamma**2)*((L+delta)**2+gamma**2)
    )


def inverse_square_count_upper(H: mp.mpf) -> mp.mpf:
    H=mp.mpf(H)
    if H < mp.e:
        raise ValueError("H must be >= e for published bound")
    main=(mp.log(H/(2*mp.pi))+1)/(2*mp.pi*H)
    error=(2*A*mp.log(H)+A/2+2*B*mp.log(mp.log(H))
           +B/(2*mp.log(H))+2*C)/H**2
    return main+error


def scale_family(scales: list[str], count: int=40, digits: int=40) -> dict:
    if count < 1 or digits < 20:
        raise ValueError("count>=1, digits>=20")
    mp.mp.dps=digits
    gammas=[mp.im(mp.zetazero(n)) for n in range(1,count+1)]
    H=VERIFIED_HEIGHT
    P=inverse_square_count_upper(H)
    rows=[]
    for text in scales:
        L=mp.mpf(text)
        if L <= 0:
            raise ValueError("all scales must be positive")
        T=total_target(L)
        S=mp.fsum(on_line_weight(L,g) for g in gammas)
        tail=T-S
        g=gammas[0]
        theta=2*mp.atan(g/L)
        delta=mp.mpf("0.125")
        quartet=quartet_weight(L,delta,g)
        quartet_F=quartet_factor(L,delta,g)
        fmt=lambda x,n=25:mp.nstr(x,n)
        rows.append({
            "L":fmt(L),
            "first_zero_height_unchanged":fmt(g),
            "first_zero_theta_degrees":fmt(mp.degrees(theta),18),
            "first_zero_w":fmt(w(L,g),18),
            "target_T_L":fmt(T),
            "known_on_line_partial_sum":fmt(S),
            "finite_residual_not_offline_defect":fmt(tail),
            "normalized_total_T_over_L2":fmt(T/L**2),
            "hypothetical_quartet_factor_greater_than_one":fmt(quartet_F),
            "hypothetical_quartet_weight_positive":fmt(quartet),
            "uniform_normalized_defect_upper":fmt(2*P),
            "scale_dependent_defect_upper":fmt(2*L**2*P),
        })
    centered_xi_second_ratio=mp.diff(xi,mp.mpf("0.5"),2)/xi(mp.mpf("0.5"))
    return {
        "experiment":"symbolic_scale_family",
        "status":"RH-equivalent formulas, not an RH proof",
        "zero_count":count,"precision_digits":digits,
        "verified_height":mp.nstr(H,15),
        "small_L_total_normalized_limit_xi_second_over_xi":
            mp.nstr(centered_xi_second_ratio,30),
        "published_uniform_normalized_defect_upper":
            mp.nstr(2*P,25),
        "scale_examples":rows,
        "mathematical_warning":(
            "Zero heights do not depend on L. A finite residual includes uncounted "
            "critical-line roots. D(L)->0 as L->0 even if RH is false; "
            "the normalized limit must be shown zero, which is still unproved."
        )
    }


if __name__ == "__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--scales",default="0.1,0.5,1,5,20,100")
    p.add_argument("--count",type=int,default=40)
    p.add_argument("--digits",type=int,default=40)
    args=p.parse_args()
    print(json.dumps(scale_family(
        [s.strip() for s in args.scales.split(",") if s.strip()],
        count=args.count,digits=args.digits
    ),indent=2))
