#!/usr/bin/env python3
"""Chapter 37: prime circle Fourier moments. Standard library only."""
import cmath, math
N=1_000_000
s=bytearray(b'\x01')*(N+1)
s[:2]=b'\x00\x00'
for p in range(2, math.isqrt(N)+1):
    if s[p]:
        s[p*p::p]=b'\x00'*(((N-p*p)//p)+1)
primes=[p for p in range(2,N+1) if s[p]]
for X in (10_000,100_000,1_000_000):
    pp=[p for p in primes if p<=X]
    equal=sum(cmath.exp(1j*math.log(p)) for p in pp)/len(pp)
    reciprocal=sum(cmath.exp(1j*math.log(p))/p for p in pp)/sum(1/p for p in pp)
    asym=cmath.exp(1j*math.log(X))/(1+1j)
    print(X,len(pp),round(abs(equal),6),round(abs(reciprocal),6),round(abs(equal-asym),6))
assert len(primes)==78498
print("PASS: finite prime angular diagnostics; no RH claim")
