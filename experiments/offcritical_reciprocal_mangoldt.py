import cmath, math
ell=math.log(2)
A=ell/math.sqrt(2)
B=ell/2
u=(-A-math.sqrt(A*A+8*B*B))/(4*B)
assert u < -1
b=math.acosh(-u)
for sign in (-1,1):
    z=(sign*b+1j*math.pi)/ell
    F=2*A*cmath.cosh(z*ell)+2*B*cmath.cosh(2*z*ell)
    assert abs(F)<1e-12
    print('off-axis zero of finite prime-power field:',z,'residual:',abs(F))
assert A>B>0
print('PASS: genuine von Mangoldt weights for 2 and 4 yield off-axis zeros in finite reciprocal harmonic model')
print('Not zeros of Riemann xi; no RH conclusion.')
