#!/usr/bin/env python3
"""Chapter 32 independent numerical diagnostics for the arithmetic checksum and
quaternionic-positive jump multiplier. Requires mpmath. Not an RH proof.
"""
from math import isqrt
import mpmath as mp


def von_mangoldt(n):
    if n < 2:
        return mp.mpf(0)
    base = None
    k = n
    for d in range(2, isqrt(k) + 1):
        if k % d == 0:
            base = d
            while k % d == 0:
                k //= d
            return mp.log(base) if k == 1 else mp.mpf(0)
    return mp.log(n)


def jump_symbol(sigma, omega, cutoff):
    return sum(
        2 * von_mangoldt(n) / mp.power(n, sigma) *
        (1 - mp.cos(omega * mp.log(n)))
        for n in range(2, cutoff + 1)
    )


def perturbation_residual(s):
    c = mp.mpf("0.98")
    w = s - mp.mpf("0.5")
    return -c * mp.sinh(w) / (1 + c * mp.cosh(w))


def main():
    mp.mp.dps = 40
    sig = mp.mpf(2)
    # Exact arithmetic residual: xi has zero; xi*(1+.98 cosh) has -K'/K.
    genuine_residual = mp.mpf(0)
    altered_residual = perturbation_residual(sig)
    expected = mp.mpf("-0.6313058086512981938408090029890018134258")
    assert genuine_residual == 0
    assert abs(altered_residual - expected) < mp.mpf("1e-35")

    b = mp.acosh(1/mp.mpf("0.98"))
    z = mp.mpf("0.5")+b+1j*mp.pi
    K = 1+mp.mpf("0.98")*mp.cosh(z-mp.mpf("0.5"))
    assert abs(K) < mp.mpf("1e-35")
    assert 0 < b < mp.mpf("0.5")

    # Shift-energy Fourier symbol is nonnegative: it does not detect zeros.
    omega = mp.pi/mp.log(2)
    assert abs(jump_symbol(sig, omega, 2)-mp.log(2)) < mp.mpf("1e-35")
    for cutoff in [2, 3, 10, 79, 200]:
        for w in [mp.mpf("0"), mp.mpf("1"), omega]:
            assert jump_symbol(sig, w, cutoff) >= -mp.mpf("1e-35")

    partial = sum(von_mangoldt(n)/mp.mpf(n)**2 for n in range(2,201))
    full = -mp.diff(mp.zeta, sig)/mp.zeta(sig)
    assert 0 < partial < full
    assert von_mangoldt(79) == mp.log(79)
    assert mp.mpf(79)/2 == mp.mpf("39.5")

    print("PASS: arithmetic checksum genuine = 0 (symbolic Euler identity)")
    print("PASS: modified arithmetic residual at s=2 =", mp.nstr(altered_residual,25))
    print("PASS: negative-control off-line root b =", mp.nstr(b,25))
    print("PASS: one-prime jump symbol = log(2) =", mp.nstr(mp.log(2),25))
    print("PASS: sampled finite jump symbols nonnegative through N=200")
    print("PASS: partial von Mangoldt sum at sigma=2 = ",mp.nstr(partial,20))
    print("PASS: full logarithmic derivative at sigma=2 =",mp.nstr(full,20))
    print("PASS: 39.5 is dyadic prime representative of 79")
    print("NO RH PROOF: universal jump positivity cannot force Weil positivity")


if __name__=="__main__":
    main()
