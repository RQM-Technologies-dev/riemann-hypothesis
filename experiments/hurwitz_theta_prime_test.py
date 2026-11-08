"""Hurwitz quaternion theta / 79-prime experiment; no RH claim. Requires mpmath."""
import mpmath as mp

def odd_divisor_sum(n):
    return sum(d for d in range(1, n + 1, 2) if n % d == 0)

def r_h(n):
    return 24 * odd_divisor_sum(n)

def theta_direct(y, cutoff=12):
    z = sum(mp.exp(-mp.pi*y*k*k) for k in range(-cutoff, cutoff+1))
    h = sum(mp.exp(-mp.pi*y*(mp.mpf(k)+mp.mpf('0.5'))**2) for k in range(-cutoff, cutoff+1))
    return z**4 + h**4

def theta_coeff(y, terms=100):
    return 1 + sum(r_h(n)*mp.exp(-mp.pi*y*n) for n in range(1, terms+1))

def main():
    mp.mp.dps = 40
    assert r_h(79) == 1920
    for n in (1,2,3,4,5,7,79):
        print('norm', n, 'Hurwitz elements', r_h(n))
    for y in (mp.mpf('0.7'),mp.mpf('1'),mp.mpf('2')):
        err = abs(theta_direct(y) - theta_coeff(y))
        print('theta y',y,'error',mp.nstr(err,8))
        assert err < mp.mpf('1e-24')
    s = mp.mpf(4)
    exact = 24*(1-mp.power(2,1-s))*mp.zeta(s)*mp.zeta(s-1)
    partial = sum(mp.mpf(r_h(n))/mp.power(n,s) for n in range(1,10001))
    print('Dirichlet at s=4: exact',mp.nstr(exact,20),'partial',mp.nstr(partial,20))
    assert abs(exact-partial) < mp.mpf('1e-6')
    x = mp.mpf(79)/2
    assert abs(mp.power(79,-s)-mp.power(2,-s)*mp.power(x,-s)) < mp.mpf('1e-35')
    print('PASS: arithmetic and theta checks. No Riemann-hypothesis implication.')
if __name__ == '__main__':
    main()
