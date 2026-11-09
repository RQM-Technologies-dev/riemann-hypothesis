import math
def K(n): return math.log(n)
for m,n in [(2,3),(79,0.5),(0.5,2),(4,0.25),(39.5,2)]:
    assert math.isclose(K(m*n),K(m)+K(n),abs_tol=1e-12)
    assert math.isclose(K(m/n),K(m)-K(n),abs_tol=1e-12)
    assert math.isclose(K(1/n),-K(n),abs_tol=1e-12)
assert K(1)==0
assert math.isclose(K(79/2),K(79)-K(2))
# q(n)=1+k log(n), multiplication of two such quaternions
a=math.log(2)
real_product=1-a*a
imag_product=2*a
assert not math.isclose(real_product,1)
assert math.isclose(imag_product,math.log(4))
print("PASS: signed k-axis addition, division, reciprocal inversion, 39.5 valuation")
print("PASS: shifted quaternion representation is not multiplicative")
print("The additive origin encodes numerical 1, not numerical 0.")
