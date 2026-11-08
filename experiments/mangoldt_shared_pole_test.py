#!/usr/bin/env python3
"""Chapter 31: reproducible numerical checks of pole field and off-line negative control.

Requires mpmath. Exact non-convergence and smoothness proofs are in the chapter.
"""
import mpmath as mp

def xi(s):
    return (s*(s-1)/2)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)

def main():
    mp.mp.dps = 50
    L=mp.mpf(2)
    omega=mp.log(2)
    A=mp.sqrt(2)*omega
    for k in (1, 3, 10, 100):
        tp=2*mp.pi*k/omega
        tm=(2*k+1)*mp.pi/omega
        assert abs(A*mp.cos(tp*omega)-A) < mp.mpf("1e-45")
        assert abs(A*mp.cos(tm*omega)+A) < mp.mpf("1e-45")
        assert 2*mp.atan(tp/L) < mp.pi
        assert 2*mp.atan(tm/L) < mp.pi
    b=mp.acosh(1/mp.mpf("0.98"))
    z=mp.pi+1j*b
    assert abs(1+mp.mpf("0.98")*mp.cos(z)) < mp.mpf("1e-45")
    assert b < mp.mpf("0.5")
    for t in (10,20,40,80):
        true=xi(mp.mpf("0.5")+1j*t)
        modified=true*(1+mp.mpf(".98")*mp.cos(t))
        print("t=",t,"|Xi|=",mp.nstr(abs(true),9),"|modified Xi|=",mp.nstr(abs(modified),9))
    print("PASS: prime 2 field has two incompatible subsequential pole values ±",mp.nstr(A,18))
    print("PASS: modified Xi factor has nonreal zero z=pi+i*b, b=",mp.nstr(b,20))
    print("PASS: b < 1/2 so the *modified* Xi has extra off-critical zeros")
    print("Analytic proof: both the original and modified Xi have smooth flat pole closure.")
    print("CONCLUSION: pole matching alone does not force RH.")

if __name__ == "__main__":
    main()
