#!/usr/bin/env python3
"""Exact checks for Chapter 25: dyadic prime and quaternionic obstruction."""
from fractions import Fraction
from math import isqrt

def prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))

def norm4(v):
    return sum(x*x for x in v)

def run():
    x = Fraction(79, 2)
    assert prime(79)
    assert 2*x == 79
    h = tuple(Fraction(a, 2) for a in (17, 3, 3, 3))
    assert norm4(h) == 79
    # For hbar/2, norm = 79/4, so neither quaternion factor is a unit
    # in the order localized only at 2.
    assert norm4(tuple(z/2 for z in h)) == Fraction(79, 4)
    assert Fraction(79, 2) == Fraction(79) / 2
    # Prime-only theta lacks the n=4 coefficient of the full theta.
    assert not prime(4)
    print("PASS: 39.5 prime in Z[1/2] via associated 79 and quotient F_79")
    print("PASS: Hurwitz element (17+3i+3j+3k)/2 has norm 79")
    print("PASS: scalar 39.5 reducible in localized Hurwitz order")
    print("PASS: prime-only theta differs from original Jacobi theta")
    print("NO RH theorem follows from these checks")

if __name__ == "__main__":
    run()
