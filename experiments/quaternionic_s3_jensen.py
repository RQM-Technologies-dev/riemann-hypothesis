#!/usr/bin/env python3
"""Quaternionic S^3 Jensen second-harmonic identity for centered xi.

The exact theorem is analytical: an intrinsic quaternionic xi lift has
S^3 logarithmic mean equal to the complex circular mean minus its
second Fourier coefficient. Below the first xi zero radius, this is
log(xi(1/2)) - R^2 xi''(1/2)/(4 xi(1/2)) EXACTLY.

This script checks finite radii with mpmath quadrature. It neither
proves RH nor interval-certifies the numerical integrals.

Usage: python experiments/quaternionic_s3_jensen.py --digits 40
Dependencies: mpmath
"""
from __future__ import annotations

import argparse
import json
import mpmath as mp


def xi(s):
    """Completed xi at s away from removable singularities 0 and 1."""
    s = mp.mpc(s)
    return mp.mpf("0.5")*s*(s-1)*mp.power(
        mp.pi,-s/2
    )*mp.gamma(s/2)*mp.zeta(s)


def centered_xi(z):
    return xi(mp.mpf("0.5")+z)


def circle_harmonics(radius, f=centered_xi):
    """Complex circular Jensen mean M2 and second angular coefficient K2.

    Real-coefficient f ensures the upper/lower semicircle symmetry.
    Quadrature is not interval-certified.
    """
    r = mp.mpf(radius)
    if r <= 0:
        raise ValueError("radius must be positive")
    cuts = [mp.mpf(0), mp.pi/2, mp.pi]
    def h(theta):
        return mp.log(abs(f(r*mp.exp(1j*theta))))
    m2 = mp.quad(h,cuts)/mp.pi
    k2 = mp.quad(lambda th: mp.cos(2*th)*h(th),cuts)/mp.pi
    return m2, k2


def quaternionic_s3_mean(radius, f=centered_xi):
    """Haar/SO(4) S^3 radius-R logarithmic modulus average.

    For intrinsic f, integration over imaginary quaternion directions
    is trivial. Polar angle on S^3 has density 2 sin(theta)^2 / pi.
    """
    r = mp.mpf(radius)
    if r <= 0:
        raise ValueError("radius must be positive")
    return 2/mp.pi*mp.quad(
        lambda theta: mp.sin(theta)**2 * mp.log(abs(
            f(r*mp.exp(1j*theta))
        )), [mp.mpf(0),mp.pi/2,mp.pi]
    )


def zero_free_formula(radius):
    """Exact analytic expression ONLY if |z|<=R is zero-free for xi."""
    r=mp.mpf(radius)
    x0=mp.mpf("0.5")
    v0=xi(x0)
    v2=mp.diff(xi,x0,2)
    return mp.log(v0)-r*r*v2/(4*v0)


def polynomial_sphere_formula(radius, gamma):
    """Exact M4 for f(z)=1+z^2/gamma^2, away from R=gamma."""
    r,g=mp.mpf(radius),mp.mpf(gamma)
    if r==g:
        raise ValueError("avoid a zero on the integration sphere")
    if r<g:
        return -r*r/(2*g*g)
    return 2*mp.log(r/g)-g*g/(2*r*r)


def run(digits=40, radii=("1","5","10","13")):
    if digits<28:
        raise ValueError("digits must be >=28")
    mp.mp.dps=digits
    f0=xi(mp.mpf("0.5"))
    ratio=mp.diff(xi,mp.mpf("0.5"),2)/f0
    entries=[]
    for R in radii:
        radius=mp.mpf(R)
        if not 0<radius<mp.mpf("14"):
            raise ValueError("default xi zero-free disk checks require 0<R<14")
        m2,k2=circle_harmonics(radius)
        m4=quaternionic_s3_mean(radius)
        predicted=zero_free_formula(radius)
        entries.append({
            "radius": str(R),
            "complex_circle_mean": mp.nstr(m2,28),
            "second_angular_harmonic": mp.nstr(k2,28),
            "quaternionic_s3_mean": mp.nstr(m4,28),
            "zero_free_exact_formula": mp.nstr(predicted,28),
            "M4_minus_M2_plus_K2": mp.nstr(m4-m2+k2,8),
            "M4_minus_formula": mp.nstr(m4-predicted,8),
        })
    gamma=mp.mpf(5)
    poly=lambda z:1+z*z/(gamma*gamma)
    poly_checks=[]
    for R in ("2","7"):
        r=mp.mpf(R)
        measured=quaternionic_s3_mean(r,poly)
        predicted=polynomial_sphere_formula(r,gamma)
        poly_checks.append({
            "radius": R,
            "s3_mean": mp.nstr(measured,26),
            "piecewise_Jensen_formula": mp.nstr(predicted,26),
            "residual": mp.nstr(measured-predicted,8),
        })
    return {
        "status":"Exact mathematical identity; finite non-certified numerical checks; NOT RH proof",
        "precision_digits":digits,
        "xi_center_value":mp.nstr(f0,30),
        "xi_second_derivative_divided_by_center":mp.nstr(ratio,30),
        "radii_below_first_zero":entries,
        "polynomial_inside_and_outside_zero_radius":poly_checks,
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--digits",type=int,default=40)
    args=parser.parse_args()
    print(json.dumps(run(args.digits),indent=2))
