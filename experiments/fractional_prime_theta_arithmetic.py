#!/usr/bin/env python3
"""High precision finite numerical diagnostics for Chapter 29; no RH proof."""
import mpmath as mp

def theta(y):
    return mp.jtheta(3, 0, mp.exp(-mp.pi*y))

def odd_theta(y):
    return (theta(y)-theta(4*y))/2

def is_prime(n):
    return n>1 and all(n%d for d in range(2,int(n**0.5)+1))

def main():
    mp.mp.dps=40
    for y in map(mp.mpf, ("0.1","0.3","1","2")):
        rhs=(theta(1/y)-theta(1/(4*y))/2)/(2*mp.sqrt(y))
        assert abs(odd_theta(y)-rhs)<mp.mpf("1e-35")
    for s in (2,3):
        odd=mp.nsum(lambda k: (2*k+1)**(-s), [0,mp.inf])
        assert abs(odd-(1-mp.power(2,-s))*mp.zeta(s))<mp.mpf("1e-35")
    assert is_prime(79)
    assert mp.mpf(79)/2==mp.mpf("39.5")
    print("PASS: odd theta reciprocal-scale identity at 4 positive scales")
    print("PASS: odd Dirichlet series and Euler factor at s=2,3")
    print("PASS: 39.5 dyadic representative of prime 79")
    print("No new zero-exclusion theorem established")

if __name__=="__main__":
    main()
