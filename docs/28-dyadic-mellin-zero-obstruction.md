# 28 — Dyadic Mellin audit: exact prime-2 factor, no automatic zero exclusion

**Date:** 2026-11-08
**Goal:** Determine whether the exact dyadic theta decomposition from Chapter 27 independently forces a zero-location constraint for the Riemann xi function. Preserve the separate rigorous objective that 39.5 is prime in \(\mathbb Z[1/2]\).

## Theorem: odd theta Mellin transform

For \(y>0\) let \(O(y)=\sum_{m\ge1,\ m\text{ odd}}e^{-\pi m^2 y}\). For \(\Re s>1\), termwise Mellin integration is absolutely justified and gives
\[
\int_0^\infty O(y)y^{s/2-1}\,dy
=\pi^{-s/2}\Gamma(s/2)\sum_{m\ge1,\ m\text{ odd}}m^{-s}
=\pi^{-s/2}\Gamma(s/2)(1-2^{-s})\zeta(s).
\]
The dyadic decomposition \((\Theta(y)-1)/2=\sum_{k\ge0}O(4^ky)\) yields
\[
\int_0^\infty\frac{\Theta(y)-1}{2}y^{s/2-1}dy
=\sum_{k\ge0}2^{-ks}\int_0^\infty O(y)y^{s/2-1}dy
=\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]
The cancellation \((1-2^{-s})\sum_{k\ge0}2^{-ks}=1\) holds for \(\Re s>1\). This is an exact arithmetic-to-analytic identity, but recovers the *existing* completed zeta ingredients, not a new independent condition on its zeros.

The odd-indexed Dirichlet series \(A(s)=(1-2^{-s})\zeta(s)\) extends meromorphically. In the open critical strip \(0<\Re s<1\), \(1-2^{-s}\ne0\) because \(|2^{-s}|=2^{-\Re s}<1\). Thus \(A\) and \(\zeta\) have exactly the same zeros in that strip, including multiplicities. The dyadic extraction does not eliminate hypothetical off-critical zeros. (Outside the strip, the factor has zeros on \(\Re s=0\); do not claim global zero-set equality.)

## Consequence for quaternionic extension

For any fixed imaginary quaternion \(u^2=-1\), the same scalar coefficients define a slice-valued function by substituting \(s=\sigma+ut\), using the commutative complex slice \(\mathbb C_u\). The factor \(1-2^{-s}\) remains invertible on \(0<\sigma<1\), since its norm is bounded below by \(1-2^{-\sigma}>0\). Therefore the slice-valued odd-indexed continuation has precisely the same critical-strip zeros as the slice zeta function. Varying \(u\) creates spherical orbits of existing zeros, not a new zero-exclusion theorem.

## Stronger obstruction: cannot infer theta-only saturation

Chapter 24's nonnegative Jensen defect \(\mathcal D_0\) is zero if and only if RH. The dyadic Mellin identity proves equality of two representations of the original function, but does not independently evaluate the global radial Jensen integral or prove \(\mathcal D_0=0\). One cannot substitute \((1-2^{-s})\zeta(s)\) and cancel the factor in a zero-location proof without using a new inequality. Any such inference would be circular.

This **does not rule out** discovering a genuinely new arithmetic inequality from the full Jacobi-theta \(n^2\)-structure. It rules out the claim that the dyadic rearrangement, the Mellin identity, or quaternionic fixed-slice continuation alone supplies it.

## 39.5 objective

\(39.5=79/2\) is a prime element in \(\mathbb Z[1/2]\) because 2 is a unit and 79 is prime. The theta odd-index \(m=79\) contains the same arithmetic prime class. This is an exact identification, not a new index in theta and not an ordinary integer-prime claim.

## Next possible genuinely independent approach

Seek a nontrivial theta-specific operator/inequality controlling the signed oscillatory transform at all heights, with a rigorous demonstration that it fails on Chapter 24's shifted positive-even theta-kernel negative control. A dyadic rearrangement is a useful bookkeeping basis but not itself the needed inequality.

**Result:** Exact prime-2 Mellin bridge established; no new RH zero constraint follows from it alone.
