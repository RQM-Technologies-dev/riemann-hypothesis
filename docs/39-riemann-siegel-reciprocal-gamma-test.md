# 39 — Actual Riemann–Siegel reciprocal-phase test

**Date:** 2026-11-08. **Status:** Numerical experiment with actual Hardy Z and the leading Riemann–Siegel sum. No RH proof.

## Formula and interpretation

For \(t>0\), put \(N=\lfloor\sqrt{t/(2\pi)}\rfloor\), \(\vartheta(t)=\arg\Gamma(1/4+it/2)-(t/2)\log\pi\) with continuous phase, and \(Z(t)=e^{i\vartheta(t)}\zeta(1/2+it)\in\mathbb R\). The classical leading Riemann–Siegel formula is
\[
Z(t)=2\sum_{n=1}^{N}n^{-1/2}\cos(\vartheta(t)-t\log n)+R(t).
\]
The remainder has a controlled asymptotic expansion, with leading order \(O(t^{-1/4})\) as \(t\to\infty\), under the standard Riemann–Siegel formula. This is **not** an exact finite sum. The terms include every integer \(n\le N\), not just primes.

In a fixed quaternionic \(k\)-slice,
\[
e^{k(\vartheta-t\log n)}+e^{-k(\vartheta-t\log n)}
=2\cos(\vartheta-t\log n).
\]
Thus the reciprocal-phase pairing reproduces the real Riemann–Siegel terms **exactly** but does not create a new noncommutative coupling. The \(\vartheta\) phase arises from the Gamma factor and functional equation. The saddle scale \(N\sim\sqrt{t/(2\pi)}\) is the canonical cutoff, not a new prime-angle selection rule.

## Computed results

Using mpmath high precision and \`mp.siegeltheta(t)\`, \`mp.zeta(1/2+it)\`:

| t | N | actual Z | leading sum | residual Z-leading |
|---:|---:|---:|---:|---:|
| 50 | 2 | -0.340735005955 | 0.005319997759 | -0.346055003714 |
| 100 | 3 | 2.69269705666 | 2.23945108212 | 0.453245974543 |
| 200 | 5 | 5.58978362315 | 5.41395992735 | 0.1758236958 |
| 500 | 8 | 1.47244785106 | 1.72369135765 | -0.251243506597 |
| 1000 | 12 | 0.997794637522 | 1.11210501672 | -0.114310379198 |

The residual is substantial at these moderate heights; it is not numerical noise and cannot be discarded for zero-location claims. An \(O(t^{-1/4})\) bound does not ensure relative accuracy near zeros.

## Negative control and scope

Replacing the complex imaginary unit by a single quaternionic \(k\) leaves the sum unchanged: it is a complex slice. The formula follows from established analytic continuation and functional equation without assuming RH; consequently it is compatible with hypothetical off-line zeros. It cannot by itself establish Weil positivity or exclude off-axis zeros.

This experiment is **not** the Chapter 24 shifted-theta negative control: the latter does not automatically inherit the original Riemann–Siegel formula. Do not claim to have tested that control here.

## Next rigorous gate

To add genuinely new structure, specify a canonical theta-derived coupling involving noncommuting quaternionic axes, prove it respects the exact completed zeta (including all correction terms), and establish an inequality that fails for a positive-even modified kernel with known off-line zeros. Otherwise the k-axis is an exact geometric restatement.

The earlier dyadic-prime result \(39.5=79/2\) remains prime in \(\mathbb Z[1/2]\), but 79 remains the ordinary zeta prime index.
