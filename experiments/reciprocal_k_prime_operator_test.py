import math
P=[2,3,5,7,11,13,17,19]
def a(n): return (n*n-1)/(n*n+1)
def op(x,y): return (x+y)/(1+x*y)
for m,n in [(2,3),(79,0.5),(0.5,2),(3,7)]:
    assert abs(op(a(m),a(n))-a(m*n))<1e-12
for t in [0,1,5,10,20]:
    val=sum(2*math.log(p)/math.sqrt(p)*(1-math.cos(t*math.log(p))) for p in P)
    assert val>=-1e-12
    print(f't={t:2} lambda={val:.12f}')
for t in [0,1,5,10,20]:
    val=sum(2*(1+0.98*math.cos(math.log(p)))**2*(1-math.cos(t*math.log(p))) for p in P)
    assert val>=-1e-12
print('PASS: group law, prime spectral positivity, arbitrary-weight control')
