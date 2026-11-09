import mpmath as mp
mp.mp.dps=35
primes=[2,3,5,7,11,13,17,19,23,29]
def theta(t): return mp.im(mp.loggamma(mp.mpf('.25')+1j*t/2))-t*mp.log(mp.pi)/2
def vel(t): return (mp.re(mp.digamma(mp.mpf('.25')+1j*t/2))-mp.log(mp.pi))/2
for t in [10,14.134725141734693,21.022039638771555,25.01085758014569,50,100]:
    S=sum(mp.exp(1j*t*mp.log(p)) for p in primes)/len(primes)
    rotated=mp.exp(1j*theta(t))*S
    assert abs(abs(S)-abs(rotated))<mp.mpf('1e-30')
    Z=mp.exp(1j*theta(t))*mp.zeta(mp.mpf('.5')+1j*t)
    assert abs(mp.im(Z))<mp.mpf('1e-25')
    print(mp.nstr(t,11),mp.nstr(vel(t),14),mp.nstr(abs(S),12))
print('PASS: common Gamma phase preserves prime-circle concentration; Hardy Z real')
