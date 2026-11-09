#!/usr/bin/env python3
"""Numerical Guinand-Weil Gaussian test: no RH assumption or proof."""
import mpmath as mp

def mangoldt(n):
    for p in range(2, int(n**0.5)+1):
        if n%p==0:
            m=n
            while m%p==0:
                m//=p
            return mp.log(p) if m==1 else mp.mpf(0)
    return mp.log(n)

def test(sigma, max_n=10000, zero_count=24):
    h=lambda t: mp.exp(-t*t/(2*sigma*sigma))
    hat=lambda u: mp.sqrt(2*mp.pi)*sigma*mp.exp(-sigma*sigma*u*u/2)
    pole=2*mp.exp(1/(8*sigma*sigma))
    arch=mp.quad(lambda t: h(t)*(mp.re(mp.digamma(mp.mpf('0.25')+1j*t/2))-mp.log(mp.pi)),[-mp.inf,mp.inf])/(2*mp.pi)
    prime=sum(mangoldt(n)*hat(mp.log(n))/mp.sqrt(n) for n in range(2,max_n))/mp.pi
    arithmetic=pole+arch-prime
    zero_side=sum(2*h(mp.im(mp.zetazero(j))) for j in range(1,zero_count+1))
    return arithmetic,zero_side

def main():
    mp.mp.dps=35
    for s in [3,5,8]:
        a,z=test(s)
        print(f'sigma={s}: arithmetic={mp.nstr(a,20)}, zeros={mp.nstr(z,20)}, residual={mp.nstr(a-z,8)}')
        assert abs(a-z)<mp.mpf('1e-12')
    for m,n in [(2,3),(79,mp.mpf('0.5'))]:
        a=lambda x: mp.tanh(mp.log(x))
        assert abs((a(m)+a(n))/(1+a(m)*a(n))-a(m*n))<mp.mpf('1e-30')
    print('PASS: Gaussian explicit formula and k-axis group law (numerical only)')

if __name__=='__main__':
    main()
