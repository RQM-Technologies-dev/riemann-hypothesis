# 34 — First reciprocal k-axis prime operator: positivity test and obstruction

**Date:** 2026-11-08. **Result:** A natural prime-translation Laplacian is positive and reciprocal-symmetric, but this positivity is automatic for *arbitrary* nonnegative weights and is **not** a new RH criterion.

## Definition and precise Hilbert space

Let \(a(n)=\tanh(\log n)\) and \(a\oplus b=(a+b)/(1+ab)\). On the quaternionic Hilbert space
\[
\mathscr H=L^2((-1,1),da/(1-a^2);\mathbb H),
\]
define for \(p>1\)
\[
(T_p f)(a)=f(a\oplus a(p)).
\]
These are right-quaternion-linear unitary operators because \(dt=da/(1-a^2)\) with \(t=\operatorname{artanh}a\), and \(T_p\) is translation \(t\mapsto t+\log p\). Its adjoint is \(T_p^*=T_p^{-1}\), division by \(p\). The operators commute with one another and with constant left quaternion multiplication.

For a finite prime cutoff \(N\), define
\[
\boxed{\mathcal L_N=\sum_{p\le N}\frac{\log p}{\sqrt p}(2I-T_p-T_p^{-1})
=\sum_{p\le N}\frac{\log p}{\sqrt p}(I-T_p)^*(I-T_p).}
\]
Thus for every \(f\in\mathscr H\),
\[
\langle f,\mathcal L_Nf\rangle
=\sum_{p\le N}\frac{\log p}{\sqrt p}\|(I-T_p)f\|^2\ge0.
\]
This is rigorous and independent of RH. Since the \(T_p\) are scalar translations, no specifically noncommutative quaternionic effect appears.

## Spectral multiplier

Under Fourier transformation in \(t\), the multiplier is
\[
\lambda_N(\tau)=2\sum_{p\le N}\frac{\log p}{\sqrt p}[1-\cos(\tau\log p)]\ge0.
\]
Numerical checks with primes \(2,3,5,7,11,13,17,19\):
- \(\lambda_N(0)=0\)
- \(\lambda_N(1)=14.908123529720\)
- \(\lambda_N(5)=10.667669755929\)
- \(\lambda_N(10)=10.187700445652\)
- \(\lambda_N(20)=10.036979457026\).

The values are illustrative and not eigenvalue locations of xi. For the \(L^2(\mathbb R)\) operator, Fourier multipliers describe continuous spectrum, and the zero at \(\tau=0\) does not yield an \(L^2\) eigenvector. This operator does not select zeta zero ordinates.

## Critical negative controls

The same sum-of-squares proof holds for **any** coefficients \(c_p\ge0\), even with no relationship to primes:
\[
\sum_p c_p(2I-T_p-T_p^{-1})\succeq0.
\]
For example \(c_p=(1+0.98\cos(\log p))^2\) gives the same positivity, regardless of the Chapter 24 shifted-theta off-axis-zero control. This does **not** mean that these weights encode that modified theta function; it proves only that the positivity mechanism fails to distinguish original arithmetic from arbitrary positive data.

Moreover \(\Lambda(p^r)=\log p\) for all prime powers \(p^r\), whereas \(\mathcal L_N\) includes primes only. Including prime powers with any nonnegative cutoff/decay weights preserves the same automatic positivity, and therefore does not cure the nonselectivity.

## Full Weil criterion versus this operator

Weil's explicit formula is a completed distributional identity involving prime powers, test functions, Gamma/archimedean terms, and poles. The RH-equivalent Weil quadratic form is **not** equal to the positive prime-translation Laplacian above. The negative cosine response in Chapter 30 is transformed into \(1-\cos\) by adding a large positive diagonal term \(2I\) per mode; that added term is not derived from the completed explicit formula. One must not infer RH from this construction.

A quaternionic matrix coupling between \(i,j,k\) can be made noncommutative, but without a canonical coefficient/operator derived from the exact theta/von Mangoldt arithmetic, such a coupling is arbitrary. Coordinate transport alone is unitarily equivalent to the original log-line translation representation and preserves positivity/spectrum.

## Reproducibility

Run \`python experiments/reciprocal_k_prime_operator_test.py\` (Python standard library). It checks the group law, nonnegative spectral multiplier, and arbitrary-weight negative control. It is a finite diagnostic, not an RH proof.

## Next research gate

Derive the **full** completed Weil form in \(a\)-coordinates with its exact prime-power, archimedean and pole terms, then test whether a canonical quaternionic off-axis coupling emerges from those coefficients. Require a new independently proved sign property that fails the Chapter 24 shifted-theta control. Without this, the k-axis yields a faithful and useful representation but not an independent RH constraint.

**Arithmetic target retained:** \(39.5=79/2\) is prime in \(\mathbb Z[1/2]\); the usual zeta Euler product still indexes prime 79, not 39.5.
