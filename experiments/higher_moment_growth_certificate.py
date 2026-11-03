#!/usr/bin/env python3
"""Higher Jacobi-theta moment *growth* certificate, not an RH proof.

The mathematical lower bound in docs/15 is exact. This script uses floating
Gauss-Legendre quadrature and a truncated theta kernel; reported decimal roots
are NOT interval certified.

Run: python experiments/higher_moment_growth_certificate.py --nodes 220
Requires numpy, mpmath.
"""
from __future__ import annotations

import argparse
import json
from math import factorial
import numpy as np
import mpmath as mp


def theta_phi_numpy(v: np.ndarray, terms: int=7) -> np.ndarray:
    """Truncated classical positive Jacobi-theta kernel for v>=0."""
    if terms < 1 or np.any(v<0):
        raise ValueError("terms>=1, v>=0 required")
    ev=np.exp(2*v)
    return sum(
        (4*np.pi**2*n**4*np.exp(4.5*v)-6*np.pi*n**2*np.exp(2.5*v))
        *np.exp(-np.pi*n*n*ev)
        for n in range(1,terms+1)
    )


def moment_bounds(nodes: int=220, max_order: int=9,
                  terms: int=7) -> tuple[list[float],list[float]]:
    """Numerical moments J_k^- and J_k^+ from the exact formulas of docs/15."""
    if nodes<30 or max_order<1 or terms<1:
        raise ValueError("nodes>=30, max_order>=1, terms>=1")
    abscissa,weights=np.polynomial.legendre.leggauss(nodes)
    v=1.5*(abscissa+1)
    weights=1.5*weights
    q=theta_phi_numpy(v,terms)*weights
    W=q[:,None]*q[None,:]/4
    a=v[:,None]+v[None,:]
    b=v[:,None]-v[None,:]
    al=a*a
    bl=b*b
    c_alo=np.cosh(a/2)
    c_blo=np.cosh(b/2)
    lower=[]
    upper=[]
    for k in range(max_order+1):
        ak=a**(2*k)
        bk=b**(2*k)
        lower.append(float(np.sum(W*(al*bk+bl*ak))))
        upper.append(float(np.sum(W*(al*c_alo*bk+bl*c_blo*ak))))
    return lower,upper


def growth_minorant(x: float, n_odd: int,
                   lower: list[float], upper: list[float]) -> float:
    """An exact polynomial in x with numerically approximated coefficients."""
    if n_odd<1 or n_odd%2!=1 or n_odd>=len(lower) or n_odd>=len(upper):
        raise ValueError("n_odd positive, odd, and within computed range")
    return sum(
        (-1)**k * x**(2*k)/factorial(2*k)
        * (lower[k] if k%2==0 else upper[k])
        for k in range(n_odd+1)
    )


def first_numeric_root(n_odd: int,lower: list[float],upper: list[float]) -> float:
    """First sign-changing positive root; float diagnostic, NOT certification."""
    prev=0.0
    fprev=growth_minorant(prev,n_odd,lower,upper)
    for j in range(1,1201):
        next_x=j*0.02
        fnext=growth_minorant(next_x,n_odd,lower,upper)
        if fprev>0 and fnext<=0:
            low,high=prev,next_x
            for _ in range(65):
                mid=(low+high)/2
                if growth_minorant(mid,n_odd,lower,upper)>0:
                    low=mid
                else:
                    high=mid
            return (low+high)/2
        prev,fprev=next_x,fnext
    raise ValueError("no positive root found over scanned interval")


def xi(s: mp.mpc) -> mp.mpc:
    return mp.mpf("0.5")*s*(s-1)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)


def direct_growth_form(x: str,y: str,digits: int=45) -> mp.mpf:
    """G=Re(xi' conj xi)/4 evaluated at s=1/2+y+i*x.

    Uses reflection symmetry to match G(x,y)=1/8 d_y |Xi(x+iy)|^2.
    """
    mp.mp.dps=digits
    yy=mp.mpf(y)
    if not 0<yy<=mp.mpf("0.5"):
        raise ValueError("require 0<y<=1/2")
    s=mp.mpc(mp.mpf("0.5")+yy,mp.mpf(x))
    z=xi(s)
    return mp.re(mp.diff(xi,s)*mp.conj(z))/4


def run(nodes: int=220,max_order: int=9,terms: int=7,digits: int=45) -> dict:
    if max_order<1 or max_order%2==0:
        raise ValueError("max_order must be positive odd")
    lower,upper=moment_bounds(nodes,max_order,terms)
    results=[]
    for n in range(1,max_order+1,2):
        root=first_numeric_root(n,lower,upper)
        results.append({
            "odd_n":n,
            "degree":2*n,
            "first_positive_root_numerical":f"{root:.13f}",
            "H_n_at_x7":f"{growth_minorant(7.0,n,lower,upper):.16e}",
        })
    checks=[]
    for xs in ("4","6","7"):
        for ys in ("0.01","0.1","0.5"):
            g=direct_growth_form(xs,ys,digits=digits)
            bound=mp.mpf(ys)*growth_minorant(float(xs),max_order,lower,upper)
            checks.append({
                "x":xs,"y":ys,
                "exact_growth_G_numerical":mp.nstr(g,24),
                "lower_bound_y_H_n_numerical":mp.nstr(bound,24),
                "inequality_sample_passes":bool(g>=bound),
            })
    return {
        "title":"Jacobi-theta bilinear growth moment polynomial hierarchy",
        "status":"Exact analytic sufficient inequality; numeric roots not certified; RH unproved",
        "scale_L":"symbolic arbitrary; not used to choose any moment",
        "quadrature_nodes":nodes,
        "theta_terms_numerical":terms,
        "integration_v_range":[0,3],
        "max_odd_order":max_order,
        "kernel_moments_lower":[f"{v:.16e}" for v in lower],
        "kernel_moments_upper":[f"{v:.16e}" for v in upper],
        "roots":results,
        "direct_completed_zeta_checks":checks,
        "no_go":"Every fixed odd polynomial H_n has negative leading coefficient, so cannot remain positive for all spectral heights."
    }


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--nodes",type=int,default=220)
    p.add_argument("--max-order",type=int,default=9)
    p.add_argument("--terms",type=int,default=7)
    p.add_argument("--digits",type=int,default=45)
    a=p.parse_args()
    print(json.dumps(run(a.nodes,a.max_order,a.terms,a.digits),indent=2))
