#!/usr/bin/env python3
"""Chapter 40: S3 critical-spine reflection and off-spine negative control."""
import mpmath as mp
mp.mp.dps=40
R=lambda q:(-q[0],q[1],q[2],q[3])
for q in [(0,1,0,0),(.6,.8,0,0),(-.3,.4,.5,mp.sqrt(.5))]:
    assert R(R(q))==q
    assert mp.almosteq(sum(x*x for x in R(q)),sum(x*x for x in q))
for q in [(0,1,0,0),(0,0,1,0),(0,0,0,-1)]:
    assert R(q)==q
b=mp.acosh(1/mp.mpf('0.98'))
for m in (0,1):
    z=b+1j*(2*m+1)*mp.pi
    residual=abs(1+mp.mpf('0.98')*mp.cosh(z))
    print('m',m,'residual',mp.nstr(residual,12))
    assert residual<mp.mpf('1e-35')
gap=mp.tanh(b/2)/(4*b)-mp.sech(b/2)**2/8
assert gap>0
print('b',mp.nstr(b,25),'folding deficit',mp.nstr(gap,25))
print('PASS: reflection symmetry allows off-spine zeros; no RH proof')
