# 29 — Fractional-prime arithmetic signature and theta reciprocity audit

**Date:** 2026-11-08
**Question:** Does the dyadic outward/inward prime structure yield an *independent* arithmetic constraint on the genuine Jacobi-theta kernel, sufficient to force the Riemann xi zeros onto the critical fold? Preserve the goal: \(39.5=79/2\) is prime in \(A=\mathbb Z[1/2]\).

## 1. Exact odd-prime arithmetic signature

For \(\Re s>1\), put
\[
A(s)=\sum_{m\ge1,\ m\ {\rm odd}}m^{-s}
=(1-2^{-s})\zeta(s)
=\prod_{p\ {\rm odd\ prime}}(1-p^{-s})^{-1}.
\]
Logarithmic differentiation gives the *exact* von Mangoldt series
\[
-\frac{A'(s)}{A(s)}
=\sum_{\substack{n\ge1\\n\ {\rm odd}}}\frac{\Lambda(n)}{n^s},
\quad \Lambda(p^k)=\log p,\quad \Lambda(n)=0\ \text{otherwise}.
\]
Thus odd prime 79 appears with coefficient \(\log79\), and its dyadic prime representative is \(79/2=39.5\). The index is still 79, **not** a new Gaussian index 39.5. The logarithmic derivative encodes prime powers, not only primes.

## 2. Exact odd-theta reciprocal-scale transformation

Let \(\Theta(y)=\sum_{n\in\mathbb Z}e^{-\pi n^2y}\) and \(O(y)=\sum_{m\ge1,\ m\ {\rm odd}}e^{-\pi m^2y}\). Since \(2O(y)=\Theta(y)-\Theta(4y)\), the Jacobi identity \(\Theta(y)=y^{-1/2}\Theta(1/y)\) gives
\[
\boxed{
O(y)=\frac1{2\sqrt y}\left[\Theta(1/y)-\frac12\Theta(1/(4y))\right].
}
\]
This is an **exact** inward/outward reciprocal-scale identity, retaining all odd composite indices. It is not the false statement that individual terms \(n\) map to \(1/n\). It is an arithmetic-specific identity of the *full* Gaussian lattice, inherited from Poisson summation.

The odd-theta Mellin transform for \(\Re s>1\) is
\[
\int_0^\infty O(y)y^{s/2-1}\,dy
=\pi^{-s/2}\Gamma(s/2)A(s).
\]
All of these are classical identities in a dyadic presentation.

## 3. Critical-strip zero audit

For \(0<\sigma=\Re s<1\), \(|2^{-s}|=2^{-\sigma}<1\), so
\[
|1-2^{-s}|\ge 1-2^{-\sigma}>0.
\]
Thus \(A(s)\) and \(\zeta(s)\) have exactly the same zeros and multiplicities in the critical strip. Their logarithmic derivatives have the same zero-related poles there. Neither the odd-theta reciprocal identity nor the odd-prime von Mangoldt signature removes hypothetical off-line zeros.

In a fixed quaternionic slice \(s=\sigma+ut\), \(u^2=-1\), the identical modulus bound holds, so the slice lift inherits the same zeros. A noncommutative prime-axis coupling is not furnished by this calculation.

## 4. Testing the theta-specific mechanism against Chapter 24

The genuine theta series has arithmetic coefficients at **all integer squares** and the exact modular transformation above. The positive-even shifted Fourier kernel from Chapter 24 is a different kernel with demonstrable extra off-axis zeros. This shows generic positivity/evenness alone cannot prove RH. It does **not** by itself prove that the original theta's modularity or prime-power signature forces RH: that would require a new all-height sign theorem. The arithmetic specificity is real, but the required zero exclusion is not derived.

## 5. Results

- **PASS (exact):** odd theta reciprocal-scale identity.
- **PASS (exact):** odd-prime Euler product and von Mangoldt logarithmic derivative on \(\Re s>1\).
- **PASS (exact):** \(39.5\) is a dyadic prime representative of 79.
- **PASS (exact):** odd-indexed continuation has the same critical-strip zero multiset as zeta.
- **NOT PROVED:** a new sign, spectral, or Jensen saturation constraint forcing RH.

**Decision:** The proposed prime-arithmetic coupling is mathematically valid but is not an independent zero-exclusion mechanism. Future work must derive a theta-specific *new inequality* (not another equality/reindexing) that fails for the shifted-kernel negative control and holds at every spectral height. Do not claim RH or a quaternionic continuation of integer primality.
