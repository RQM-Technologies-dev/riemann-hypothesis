# 38 — Gamma phase versus prime-circle rotation: exact tests

**Date:** 2026-11-08. **Status:** Analytical and numerical diagnostic; no RH proof.

## Definitions

For real \(t\), define the continuous Riemann–Siegel phase
\[
\vartheta(t)=\Im\log\Gamma(1/4+it/2)-(t/2)\log\pi
\]
using a continuous branch. Its derivative is
\[
\vartheta'(t)=\tfrac12\Re\psi(1/4+it/2)-\tfrac12\log\pi
=\tfrac12\log(t/(2\pi))+O(t^{-2})\quad(t\to+\infty).
\]
The actual Hardy function is \(Z(t)=e^{i\vartheta(t)}\zeta(1/2+it)\), real on the real line.

For a **proposed diagnostic, not a canonical Euler-product phase**, put \(\Phi_p(t)=t\log p+\vartheta(t)\). Then \(\Phi_p'=\log p+\vartheta'(t)\). At any fixed height, \(\Phi_p-\Phi_q=t\log(p/q)\). Consequently
\[
\left|\sum_{p\in P}c_pe^{i\Phi_p(t)}\right|
=\left|\sum_{p\in P}c_pe^{it\log p}\right|
\]
for every finite set \(P\) and arbitrary fixed complex weights \(c_p\). Gamma is a **common phase rotation**; it cannot change any equal-height relative prime spacing or Fourier magnitude.

## Numeric test (mpmath, 35 digits; first ten primes)

| t | theta'(t) | absolute first moment before and after common Gamma rotation |
|---:|---:|---:|
| 10 | 0.232145313432 | 0.1286237939 |
| 14.134725141734693 | 0.405274372162 | 0.5422544573 |
| 21.022039638771555 | 0.603800002982 | 0.4046726321 |
| 25.01085758014569 | 0.690683169968 | 0.4432892311 |
| 50 | 1.03706463559 | 0.3068182003 |
| 100 | 1.38364447642 | 0.3272384209 |

The numerical Hardy-Z imaginary component was ~10^-34 or smaller at the sampled real heights, consistent with its exact real-valuedness. The zero heights are *reference values*, not fitted to the diagnostic. The prime moment values at the zero heights are not zero; no new zero-detection mechanism emerges from this common-phase statistic.

## Where Gamma really enters

The derivative \(\vartheta'(t)\) is related to the archimedean density of the completed explicit formula and the main term of the Riemann–von Mangoldt zero count. It is not an independent prime-frequency interaction. The full Guinand–Weil formula (Chapter 35) contains the **digamma integral** alongside all prime powers and pole terms; omitting any changes the arithmetic identity.

The phase sign matters: the genuine Dirichlet term \(n^{-it}\) is \(e^{-it\log n}\), so a term multiplied by the Hardy phase has angle \(\vartheta(t)-t\log n\), and instantaneous frequency \(\vartheta'(t)-\log n\), **not** \(\vartheta'(t)+\log n\). Formal stationary-phase matching occurs when \(\vartheta'(t)\approx\log n\), hence \(t\approx2\pi n^2\) at large \(t\). This is a standard saddle-scale relation related to Riemann–Siegel asymptotics, not a theorem identifying zeta zeros with individual prime angles. The Euler Dirichlet series does not converge on \(\Re s=1/2\); any termwise manipulation there requires a valid approximate functional equation or smoothed explicit formula.

## Verdict and next test

1. **Pass:** Gamma's phase and derivative have an exact formula.
2. **Pass:** Common Gamma rotation leaves prime-circle concentration unchanged, exactly.
3. **Pass:** Gamma correction is indispensable in the completed Weil explicit formula.
4. **Not established:** Any new quaternionic or prime-arc zero-exclusion condition.
5. **Next test:** Work with a rigorously controlled approximate functional equation, where the Gamma phase and the two *oppositely oriented* Dirichlet sums genuinely interact, then compare with a shifted-theta off-axis-zero negative control. Avoid claiming the artificial \(\Phi_p\) is itself the zeta phase.

The signed \(k\)-axis remains an exact additive logarithmic coordinate. \(39.5=79/2\) remains prime in \(\mathbb Z[1/2]\), but zeta's prime index is 79.
