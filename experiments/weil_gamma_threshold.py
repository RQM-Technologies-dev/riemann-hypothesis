import mpmath as mp
mp.mp.dps=35
b=lambda t:mp.re(mp.digamma(mp.mpf(1)/4+1j*t/2))-mp.log(mp.pi)
T=mp.findroot(b,(6,7))
assert abs(b(T))<mp.mpf('1e-30')
assert all(b(t)<0 for t in [0,1,3,6])
assert all(b(t)>0 for t in [7,10,20])
assert abs(b(0)-(-mp.euler-mp.pi/2-3*mp.log(2)-mp.log(mp.pi)))<mp.mpf('1e-30')
print('PASS gamma threshold:',mp.nstr(T,28))
print('PASS b(0):',mp.nstr(b(0),28))
print('Prime-free concentration crude bound at maximal a:',mp.nstr(mp.log(2)*T/mp.pi,15))
