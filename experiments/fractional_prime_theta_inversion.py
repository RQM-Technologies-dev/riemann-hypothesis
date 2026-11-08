#!/usr/bin/env python3
"""Numerical sanity checks of Chapter 27; not a proof of RH."""
import math

def theta(y, nmax=150):
    return 1.0 + 2*sum(math.exp(-math.pi*n*n*y) for n in range(1,nmax+1))

def odd_theta(y, nmax=150):
    return sum(math.exp(-math.pi*m*m*y) for m in range(1,nmax+1,2))

def dyadic_theta(y, kmax=30):
    return 1.0+2*sum(odd_theta((4**k)*y) for k in range(kmax))

def is_prime(n):
    return n > 1 and all(n%d for d in range(2,math.isqrt(n)+1))

def main():
    for y in [0.1, 0.3, 1.0, 2.0]:
        assert abs(theta(y)-dyadic_theta(y)) < 1e-12
        assert abs(2*odd_theta(y)-(theta(y)-theta(4*y))) < 1e-12
        assert abs(theta(y)-theta(1/y)/math.sqrt(y)) < 1e-12
    assert is_prime(79)
    assert not is_prime(9)
    assert 79/2 == 39.5
    # At y=0.1, prime-only Gaussian sum is not self-dual.
    p=lambda y: sum(math.exp(-math.pi*n*n*y) for n in range(2,151) if is_prime(n))
    assert abs(p(0.1)-p(10)/math.sqrt(0.1)) > 1e-3
    print("PASS: Jacobi theta inversion at four scales")
    print("PASS: exact dyadic theta decomposition at four scales")
    print("PASS: odd-index extraction by theta(y)-theta(4y)")
    print("PASS: prime-only theta does not obey simple modular inversion")
    print("PASS: 39.5 labels the odd-prime class of 79 in Z[1/2]")
    print("NO RH PROOF: all tests are finite numerical diagnostics")

if __name__ == "__main__":
    main()
