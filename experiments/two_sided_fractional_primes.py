#!/usr/bin/env python3
"""Finite exact checks for Chapter 26; no RH proof."""
from fractions import Fraction
from math import isqrt, log, atan2, cos, sin

def prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))

def reciprocal_irreducibles(limit=100):
    # 1/n decomposes in the reciprocal monoid iff n decomposes in N.
    return [n for n in range(2, limit+1) if not any(n % a == 0 for a in range(2,n))]

def main():
    assert reciprocal_irreducibles() == [n for n in range(2,101) if prime(n)]
    assert Fraction(79,2)*2 == 79
    assert 39 == 3*13
    assert Fraction(79)*Fraction(1,79) == 1  # both in one ring -> 79 is unit
    # fixed-slice Cayley angle: x and reciprocal have opposite angles
    L=2.0
    for n in [2,3,5,79]:
        a=2*atan2(log(n),L)
        b=2*atan2(log(1/n),L)
        assert abs(a+b)<1e-12
        assert abs(cos(a)-cos(b))<1e-12
        assert abs(sin(a)+sin(b))<1e-12
    print("PASS reciprocal-monoid irreducibles through n=100")
    print("PASS dyadic representative 39.5 = 79/2; 39 composite")
    print("PASS reciprocal 1/79 makes 79 a unit if admitted to same ring")
    print("PASS quaternionic log-Cayley conjugation for sampled n")
    print("NOT ESTABLISHED: new theta identity or RH zero restriction")

if __name__ == "__main__":
    main()
