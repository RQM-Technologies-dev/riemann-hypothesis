# 25 — Hurwitz prime-indexed theta test (79/2 = 39.5)

**Date:** 2026-11-08. **Status:** exact arithmetic identities plus numerical diagnostics; no proof of RH.

## Hypothesis and necessary distinctions
In the localized ring Z[1/2], 39.5 = 79/2 is a prime element associated to the ordinary prime 79 because 1/2 is a unit. In the full quaternion division algebra H, every nonzero element is invertible, so ordinary prime-element language does not apply. The scalar 39.5 is **not** a Hurwitz integer; the Hurwitz order contains integral-coordinate quaternions and quaternions whose four coordinates are all half-integers. Analytic continuation of a function does not itself preserve or define arithmetic primality.

The explicit Hurwitz integer q=(17+3i+3j+3k)/2 has norm N(q)=(289+27)/4=79 and is irreducible. Its scalar coordinate is 8.5, **not** 39.5; this example connects to the same prime norm, not to an identification of q with 39.5.

## Four-dimensional arithmetic theta kernel
Let H_H = Z^4 union (Z+1/2)^4 (Hurwitz integers in coordinate form). Define
```
Theta_H(y) = sum_{q in H_H} exp(-pi*y*N(q))
           = theta_3(y)^4 + theta_2(y)^4
           = 1 + sum_{n>=1} r_H(n)*exp(-pi*y*n)
r_H(n) = 24 * sum_{d|n, d odd} d.
```
Thus r_H(79)=24*(1+79)=1920. This is a count of norm-79 Hurwitz elements (not 1920 new rational primes or zero ordinates). The coefficient identity follows from Jacobi's four-square theorem and the all-half-integer coset contribution, or equivalently the theta identity for the Hurwitz lattice.

For Re(s)>2, the absolutely convergent norm Dirichlet series is
```
sum_{n>=1} r_H(n)/n^s
  = 24*(1-2^(1-s))*zeta(s)*zeta(s-1).
```
The right-hand side supplies its meromorphic continuation. This is **not** the completed Riemann xi function and is not a zero-free multiplier of it. In particular, zeta(s-1) brings a shifted zero set, while the 2-Euler factor has its own zeros in the continuation. Hence a claim that this construction preserves exactly the original nontrivial zeros is false.

## Relation to the actual Riemann theta kernel
The 1D Jacobi theta sum in the existing xi construction and the 4D Hurwitz theta are distinct modular/theta objects. The 4D arithmetic coefficients do not create an independent sign theorem for the existing Jacobi-theta Fourier kernel, do not force the 4D Jensen saturation D_0=0, and do not exclude off-critical xi zeros.

Changing the Euler product label p=2x with x=39.5 for p=79 yields p^-s = 2^-s*x^-s, an exact reparameterization only. Omitting 2^-s changes the function.

## Reproducible checks
Run `python experiments/hurwitz_theta_prime_test.py` (requires mpmath). Checks coefficients, the theta identity at three positive y values, a convergent Dirichlet partial sum at s=4, and the p=79 rescaling. Numerical tests verify algebra but do not certify RH.

## Verdict and useful next test
**Passed:** 39.5 is associated to 79 as a prime element in Z[1/2]; Hurwitz prime norm 79 exists; the four-dimensional theta has 1920 norm-79 elements and an exact Dirichlet factorization.

**Failed as an RH mechanism:** the new norm series is expressible in classical zeta factors and has different zeros. No additional zero-exclusion inequality for the original xi has been derived.

Any next proposal must state a theta-specific positive or operator inequality for the **original** xi kernel, prove it for all heights, and pass the off-axis-kernel negative controls of chapters 18 and 24.
