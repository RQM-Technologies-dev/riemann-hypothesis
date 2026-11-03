#!/usr/bin/env python3
"""Higher-order cosine minorants of the genuine Riemann Jacobi-theta kernel.

The symbolic inequality (docs/14) holds exactly. Numeric moments and computed
root locations are illustrative mpmath quadrature, NOT certified intervals,
and are NOT a proof of RH.

Run:
 python experiments/higher_moment_cosine_certificate.py --digits 40 --terms 7
"""
from __future__ import annotations

import argparse
import json
import mpmath as mp


def theta_phi(v: mp.mpf, terms: int=7) -> mp.mpf:
    """Numerically truncate the classical positive even Riemann kernel."""
    v=abs(mp.mpf(v))
    e2=mp.exp(2*v)
    return mp.fsum(
        (4*mp.pi**2*n**4*mp.exp(mp.mpf("4.5")*v)
         -6*mp.pi*n**2*mp.exp(mp.mpf("2.5")*v))
        * mp.exp(-mp.pi*n*n*e2)
        for n in range(1, terms+1)
    )


def raw_even_moment(k: int, y: mp.mpf, terms: int=7) -> mp.mpf:
    """Integral of v^(2k) Phi(v) cosh(yv), using numerical tail cutoffs."""
    if k<0 or abs(mp.mpf(y))>mp.mpf("0.5") or terms<1:
        raise ValueError("k>=0, |y|<=1/2, terms>=1")
    y=mp.mpf(y)
    return mp.quad(lambda v: v**(2*k)*theta_phi(v,terms)*mp.cosh(y*v),
                   [0,mp.mpf("0.5"),1,2,3])


def endpoint_moments(max_k: int=9, terms: int=7) -> dict:
    """Compute normalized theta moments, without any zero ordinates."""
    if max_k<1:
        raise ValueError("max_k>=1")
    out={}
    for y in (mp.mpf(0),mp.mpf("0.5")):
        raw=[raw_even_moment(k,y,terms) for k in range(max_k+1)]
        out[str(y)]=[a/raw[0] for a in raw]
    return out


def polynomial_lower(x: mp.mpf, n_odd: int, moments: dict) -> mp.mpf:
    """Uniform lower bound on Re X(x+iy)/(2A(y)), for |y|<=1/2."""
    if n_odd<1 or n_odd%2!=1:
        raise ValueError("n_odd must be a positive odd integer")
    x=mp.mpf(x)
    low=moments["0.0"]
    high=moments["0.5"]
    if len(low)<=n_odd or len(high)<=n_odd:
        raise ValueError("missing endpoint moments")
    return mp.fsum(
        (-1)**k*x**(2*k)*(low[k] if k%2==0 else high[k])
        /mp.factorial(2*k) for k in range(n_odd+1)
    )


def first_positive_root(n_odd: int, moments: dict) -> mp.mpf:
    """Find first numeric sign change via scanning, then bisection.

    Numeric root is not formally certified. Exact theorem is conditional
    on strict positivity of the explicitly defined polynomial.
    """
    step=mp.mpf("0.05")
    left=mp.mpf(0)
    fleft=polynomial_lower(left,n_odd,moments)
    for k in range(1,801):
        right=k*step
        fright=polynomial_lower(right,n_odd,moments)
        if fleft>0 and fright<=0:
            for _ in range(85):
                middle=(left+right)/2
                fmiddle=polynomial_lower(middle,n_odd,moments)
                if fmiddle>0:
                    left=middle
                else:
                    right=middle
            return (left+right)/2
        left,fleft=right,fright
    raise ValueError("no positive sign-change root found in scan 0..40")


def xi(s: mp.mpc) -> mp.mpc:
    s=mp.mpc(s)
    return mp.mpf("0.5")*s*(s-1)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)


def direct_normalized_real(x: mp.mpf,y: mp.mpf, terms: int=7) -> mp.mpf:
    """Direct check of the Re X bound: s=1/2 - y + i*x."""
    x,y=mp.mpf(x),mp.mpf(y)
    if not 0<=abs(y)<=mp.mpf("0.5"):
        raise ValueError("|y|<=1/2 required")
    X=xi(mp.mpc(mp.mpf("0.5")-y,x))
    A=raw_even_moment(0,y,terms)
    return mp.re(X)/(2*A)


def run(digits: int=40, terms: int=7, max_order: int=9) -> dict:
    if digits<25 or terms<2 or max_order<1 or max_order%2==0:
        raise ValueError("digits>=25, terms>=2, max_order odd positive")
    mp.mp.dps=digits
    moments=endpoint_moments(max_order,terms)
    results=[]
    for n in range(1,max_order+1,2):
        rt=first_positive_root(n,moments)
        results.append({
            "odd_n":n,
            "polynomial_degree":2*n,
            "first_numeric_positive_root":mp.nstr(rt,25),
            "lower_at_x9":mp.nstr(polynomial_lower(9,n,moments),25),
            "not_certified":True,
        })

    samples=[]
    for y in (mp.mpf(0),mp.mpf("0.25"),mp.mpf("0.5")):
        for x in (mp.mpf(5),mp.mpf(9),mp.mpf("9.9")):
            v=direct_normalized_real(x,y,terms)
            lower=polynomial_lower(x,max_order,moments)
            samples.append({
                "x":mp.nstr(x,6),"abs_y":mp.nstr(y,6),
                "direct_re_X_over_2A":mp.nstr(v,20),
                "uniform_minorant":mp.nstr(lower,20),
                "inequality_numerically_satisfied":bool(v>=lower),
            })

    return {
        "title":"Jacobi theta moment cosine minorants with symbolic stereographic L",
        "status":"rigorous symbolic lower-bound hierarchy; numeric thresholds not interval certified; RH unproved",
        "digits":digits,
        "theta_terms_numerical":terms,
        "integration_upper_v_numerical":3,
        "scale_L":"symbolic, not used in analytic bound",
        "endpoint_normalized_moments":{
            key:[mp.nstr(v,32) for v in values] for key,values in moments.items()
        },
        "results":results,
        "direct_integral_checks":samples,
        "interpretation":"Any fixed finite cosine minorant eventually becomes negative as |x| increases; a global proof needs a different arithmetic growth argument."
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--digits",type=int,default=40)
    parser.add_argument("--terms",type=int,default=7)
    parser.add_argument("--max-order",type=int,default=9)
    args=parser.parse_args()
    print(json.dumps(run(args.digits,args.terms,args.max_order),indent=2))
