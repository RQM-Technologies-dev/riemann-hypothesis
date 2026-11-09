#!/usr/bin/env python3
"""Chapter 39: actual Hardy Z versus leading Riemann-Siegel sum. Requires mpmath."""
import mpmath as mp
mp.mp.dps = 35
for t in [50,100,200,500,1000]:
    t=mp.mpf(t)
    theta=mp.siegeltheta(t)
    N=int(mp.floor(mp.sqrt(t/(2*mp.pi))))
    Z=mp.re(mp.exp(1j*theta)*mp.zeta(mp.mpf('0.5')+1j*t))
    leading=2*sum(mp.cos(theta-t*mp.log(n))/mp.sqrt(n) for n in range(1,N+1))
    print(f"t={int(t)} N={N} Z={mp.nstr(Z,14)} leading={mp.nstr(leading,14)} residual={mp.nstr(Z-leading,14)}")
    assert abs(mp.im(mp.exp(1j*theta)*mp.zeta(mp.mpf('0.5')+1j*t)))<mp.mpf('1e-25')
print("PASS: actual Hardy Z and leading Riemann-Siegel sum evaluated; residual retained.")
