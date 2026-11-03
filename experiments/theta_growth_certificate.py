#!/usr/bin/env python3
"""Jacobi-theta moment certificate for a partial Xi growth positivity region.

Computes a *rigorous symbolic sufficient condition* numerically (not with
interval arithmetic). It does NOT prove RH or global theta positivity.

Run: python experiments/theta_growth_certificate.py --digits 45
Dependency: mpmath
"""
from __future__ import annotations

import argparse
import json
import mpmath as mp


def phi(v: mp.mpf, terms: int = 8) -> mp.mpf:
    """Truncated numerical version of the exact Jacobi-theta kernel."""
    v = mp.mpf(v)
    if v < 0:
        v = -v
    a = mp.exp(2*v)
    return mp.fsum(
        (4*mp.pi**2*n**4*mp.exp(mp.mpf("4.5")*v)
         - 6*mp.pi*n**2*mp.exp(mp.mpf("2.5")*v))
        * mp.exp(-mp.pi*n*n*a)
        for n in range(1, terms+1)
    )


def moment(k: int, y: mp.mpf, terms: int=8) -> mp.mpf:
    """A^(k)(y), using exact Fourier-kernel integral truncated for numerics."""
    if k < 0:
        raise ValueError("k >= 0 required")
    y = mp.mpf(y)
    fn = mp.cosh if k % 2 == 0 else mp.sinh
    return mp.quad(lambda v: phi(v, terms)*v**k*fn(y*v),
                   [0, mp.mpf("0.5"), 1, 2, 3])


def xi(s: mp.mpf) -> mp.mpf:
    """Completed xi on real s away from the removable pole at 1."""
    return mp.mpf("0.5")*s*(s-1)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)


def xi_regular(s: mp.mpf) -> mp.mpf:
    """Taylor-regularized xi near s=1 using the first four Stieltjes constants.

    The polynomial equals the Taylor expansion of (s-1)*zeta(s) through degree 4.
    This permits rigorous algebraic evaluation of the first 4 derivatives at 1.
    """
    e=s-1
    h=1+mp.fsum(((-1)**k)*mp.stieltjes(k)*e**(k+1)/mp.factorial(k)
                  for k in range(4))
    return s/2*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*h


def exact_moment_thresholds() -> dict[str, mp.mpf]:
    """Independent analytic constants from xi derivatives, no zeros supplied."""
    x0=mp.mpf("0.5")
    xi0=xi(x0)
    xi2center=mp.diff(xi,x0,2)
    xi2one=(
        (1+mp.euler/2-mp.log(2)-mp.log(mp.pi)/2)**2
        -1 + mp.pi**2/8 -2*mp.stieltjes(1)-mp.euler**2
    ) / 2  # xi(1)=1/2
    xi4one=mp.diff(xi_regular,mp.mpf(1),4)
    A0=xi0/2
    A20=xi2center/2
    A4half=xi4one/2
    growth_delta=A4half/A20-A20/A0
    if not growth_delta>0:
        raise ArithmeticError("expected strictly positive growth-moment gap")
    return {
        "xi0":xi0, "xi2center":xi2center,
        "xi2one_over_xi1":2*xi2one,
        "xi4one":xi4one,
        "A0":A0,"A20":A20,"A4half":A4half,
        "growth_delta_upper":growth_delta,
        "zero_free_x_bound":mp.sqrt(2/(2*xi2one)),
        "strict_growth_x_bound":mp.sqrt(2/growth_delta),
    }


def local_growth_lower_bound(x: mp.mpf,y: mp.mpf,terms:int=8) -> dict:
    """Numerical bilinear inequality on (0<y<=1/2); not a proof for all x."""
    x,y=mp.mpf(x),mp.mpf(y)
    if not 0<y<=mp.mpf("0.5"):
        raise ValueError("require 0<y<=1/2")
    A=moment(0,y,terms)
    Ap=moment(1,y,terms)
    App=moment(2,y,terms)
    Appp=moment(3,y,terms)
    C=mp.quad(lambda v:phi(v,terms)*mp.cos(x*v)*mp.cosh(y*v),
              [0,mp.mpf("0.5"),1,2,3])
    S=mp.quad(lambda v:phi(v,terms)*mp.sin(x*v)*mp.sinh(y*v),
              [0,mp.mpf("0.5"),1,2,3])
    Cy=mp.quad(lambda v:phi(v,terms)*v*mp.cos(x*v)*mp.sinh(y*v),
              [0,mp.mpf("0.5"),1,2,3])
    Sy=mp.quad(lambda v:phi(v,terms)*v*mp.sin(x*v)*mp.cosh(y*v),
              [0,mp.mpf("0.5"),1,2,3])
    actual=C*Cy+S*Sy
    lower=A*Ap-x*x/2*(A*Appp-Ap*App)
    return {
        "actual_growth_form":actual,
        "quadratic_lower_bound":lower,
        "is_lower_bound_verified_numerically":bool(actual>=lower),
    }


def run(digits:int=45,terms:int=8) -> dict:
    if digits < 25 or terms < 2:
        raise ValueError("digits >=25 and kernel terms >=2 required")
    mp.mp.dps=digits
    a=exact_moment_thresholds()
    # independent Fourier-integral computation at y=0 and y=1/2
    m0=moment(0,0,terms); m20=moment(2,0,terms)
    m2half=moment(2,mp.mpf("0.5"),terms)
    m4half=moment(4,mp.mpf("0.5"),terms)
    checks={
        "A0_kernel_minus_xi":m0-a["A0"],
        "A2_0_kernel_minus_xi":m20-a["A20"],
        "A2_half_kernel_minus_xi":
            m2half-mp.mpf("0.25")*a["xi2one_over_xi1"],
        "A4_half_kernel_minus_xi":m4half-a["A4half"],
    }
    samples=[]
    for y in ("0.01","0.1","0.49"):
        row=local_growth_lower_bound(mp.mpf("4.82"),mp.mpf(y),terms)
        samples.append({"x":"4.82","y":y,**{
            k:(bool(v) if isinstance(v,bool) else mp.nstr(v,25))
            for k,v in row.items()
        }})
    return {
        "status":"Unconditional partial theta positivity, not RH proof",
        "precision_digits":digits,
        "kernel_terms_numerical_truncation":terms,
        "finite_integration_upper_v":3,
        "analytic_constants":{k:mp.nstr(v,32) for k,v in a.items()},
        "kernel_vs_analytic_checks":{k:mp.nstr(v,8) for k,v in checks.items()},
        "sample_growth_checks":samples,
        "interpretation":(
            "The inequalities are rigorous symbolically for the exact positive "
            "kernel. The reported decimal constants and integrals are high-precision "
            "illustrations, not interval-certified bounds. Global x remains open."
        )
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--digits",type=int,default=45)
    parser.add_argument("--terms",type=int,default=8)
    args=parser.parse_args()
    print(json.dumps(run(args.digits,args.terms),indent=2))
