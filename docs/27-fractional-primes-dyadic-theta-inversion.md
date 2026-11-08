# 27 — Fractional primes, theta inversion, and a dyadic arithmetic test

**Date:** 2026-11-08
**User objective:** retain the mathematically precise statement “39.5 is prime” in the dyadic ring \(A=\mathbb Z[1/2]\), and test whether the inward division sequence \(1/n\) gives a new analytic constraint on the Riemann xi function.

## 1. Distinguish three inversions

- **Arithmetic inversion:** \(n\mapsto 1/n\). It maps the multiplicative monoid \(\mathbb N_{>0}\) isomorphically to the reciprocal monoid \(M_-=\{1/n\}\); primes \(p\) correspond to irreducibles \(1/p\).
- **Dyadic localization:** \(A=\mathbb Z[1/2]\) makes 2 a unit. Its nonunit primes, up to association, are odd integer primes. Thus \(79/2=39.5\) is prime, but \(1/79\notin A\).
- **Theta scale inversion:** \(\Theta(y)=y^{-1/2}\Theta(1/y)\), \(y>0\), for \(\Theta(y)=\sum_{n\in\mathbb Z}\exp(-\pi n^2y)\). This is Poisson summation / Fourier self-duality of a Gaussian; it is **not** the termwise map \(n\mapsto1/n\). In particular, the \(n=0\) term has no reciprocal integer.

These operations must not be conflated. The theta identity is the established bridge between the two scales, not a new consequence of the fractional-prime definition.

## 2. A two-sided multiplicative prime coordinate

For positive rationals \(r\), unique factorization yields
\[
r=\prod_p p^{v_p(r)},\qquad v_p(r)\in\mathbb Z,\quad \text{finite support}.
\]
The outward direction is positive valuation \(v_p>0\); the inward direction is negative valuation \(v_p<0\). Reciprocal inversion sends the valuation vector \(v_p\mapsto-v_p\). For \(39.5=79/2\), the only nonzero valuations are \(v_{79}=1,\ v_2=-1\). Dyadic localization regards \(v_2\) as a unit coordinate and preserves the \(v_{79}=1\) prime component.

This yields a precise **two-sided coordinate system** without claiming that positive rationals form a ring with nonunit prime elements (they form a multiplicative group, where all elements are units).

## 3. Exact dyadic theta decomposition

Partition the nonzero integers by their 2-adic valuation:
\[
\Theta(y)-1
=2\sum_{k=0}^{\infty}\sum_{\substack{m\ge1\\m\ {\rm odd}}}
\exp(-\pi\,4^k m^2 y).
\]
This identity follows from unique \(n=2^km\) with \(m\) odd. It is exact, nonnegative, and absolutely convergent for \(y>0\). It shows where powers of 2 enter the **original** theta kernel without replacing all integers by primes.

Define the odd-indexed theta
\[
O(y)=\sum_{\substack{m\ge1\\m\ {\rm odd}}}e^{-\pi m^2 y}.
\]
Then
\[
\Theta(y)-1=2\sum_{k\ge0}O(4^ky),\qquad
2O(y)=\Theta(y)-\Theta(4y).
\]
Thus the dyadic scale decomposition is exact. It does not select the odd primes: the odd index \(m\) includes composites such as 9 and 15.

The prime 79 occurs in the \(k=0,m=79\) term, and its dyadic representative 39.5 labels the same odd prime class in \(A\). It does not create a new theta term or a second prime at a distinct location.

## 4. Why prime-only theta inversion fails

Let \(P_\Theta(y)=\sum_{p\text{ prime}}e^{-\pi p^2 y}\). This is a perfectly well-defined prime-indexed Gaussian series, but it is not \(\Theta\). For large \(y\), \(P_\Theta(y)\sim e^{-4\pi y}\); as \(y\to0^+\), \(P_\Theta(y)\) grows on the order of \(y^{-1/2}/\log(1/y)\), by the prime number theorem. Therefore a simple Gaussian modular self-duality \(P_\Theta(y)=y^{-1/2}P_\Theta(1/y)\) cannot hold: the two asymptotic sides have incompatible behavior. This is a structural obstruction, not merely a finite numerical mismatch.

## 5. Quaternionic lift and limits

For fixed \(u^2=-1\), set \(Q_L(x,u)=(L+u\log x)/(L-u\log x)\). Then \(Q_L(1/x,u)=\overline{Q_L(x,u)}\), exactly. Applied to dyadic \(x=79/2\), this is a geometric inversion of the coordinate, not a statement that \(2/79\) is a prime element in the same dyadic ring.

A quaternionic-valued theta extension built by replacing the real Gaussian scalar with fixed-slice quaternionic phases still needs a separately proved arithmetic or positivity identity. The original Riemann xi function already arises from the complete theta kernel; rewriting its indices cannot by itself constrain off-critical zeros.

## 6. Falsifiable next objective

Seek a new operator on the **full** dyadically decomposed theta kernel, not on a prime-only surrogate, with all of:
1. A proved exact relation to the original \(\xi(s)\), including normalization.
2. A nontrivial arithmetic dependence on odd-prime valuations beyond reindexing.
3. A rigorous inequality valid at all spectral heights that is **not** implied by generic evenness, positivity, or modular inversion.
4. Failure on the explicit positive-even shifted-kernel negative control in Chapter 24.

**Status:** the dyadic theta decomposition and reciprocal valuation symmetry are exact. The hoped-for theta-specific inequality and RH implication are open.
