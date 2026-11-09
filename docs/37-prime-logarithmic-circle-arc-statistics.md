# 37 — Do primes trace a circle? Logarithmic angular statistics

**Date:** 2026-11-08. **Research direction:** Prime angular arcs on the quaternionic \(w\)-\(k\) circle; distinguish exact algebra from asymptotic prime statistics. **No RH proof.**

## The geometric encoding

For any fixed \(\alpha>0\), define
\[
q_\alpha(n)=e^{k\alpha\log n}=\cos(\alpha\log n)+k\sin(\alpha\log n).
\]
Then \(q_\alpha(mn)=q_\alpha(m)q_\alpha(n)\) and \(q_\alpha(1/n)=q_\alpha(n)^{-1}\). Prime powers correspond to repeated angular rotations. Unlike the unwrapped signed k-axis \(K(n)=k\log n\), the circle is periodic and not injective on all positive reals. The circle is a fixed complex slice of \(S^3\), not the full 3-sphere.

## Theorem A: Equal-count prime angles are not equidistributed

For fixed nonzero real \(\alpha\), the prime number theorem and partial summation yield
\[
\frac{1}{\pi(X)}\sum_{p\le X}p^{i\alpha}
=\frac{X^{i\alpha}}{1+i\alpha}+o(1)\quad(X\to\infty).
\]
Indeed \(\sum_{p\le X}p^{i\alpha}\sim\int_2^X t^{i\alpha}dt/\log t
\sim X^{1+i\alpha}/((1+i\alpha)\log X)\), and \(\pi(X)\sim X/\log X\). Hence the first angular Fourier moment has asymptotic modulus \(1/\sqrt{1+\alpha^2}\), not zero. The phase rotates with \(\log X\), so the equal-count angular distribution has no uniform limit. This **does not** contradict standard equidistribution theorems for other sequences, other orderings, or other weights.

For higher Fourier modes \(m\ne0\), the analogous moment is \(X^{im\alpha}/(1+im\alpha)+o(1)\). Along subsequences with \(\alpha\log X\bmod2\pi\to\phi\), the measures have a nonuniform limiting profile (Fourier moments \(e^{im\phi}/(1+im\alpha)\)). The density is the wrapped exponential distribution obtained from the recent-prime logarithmic gap \(u=\log(X/p)\ge0\) with limiting density \(e^{-u}\).

## Theorem B: Reciprocal-prime-weighted angles ARE asymptotically equidistributed

For \(\alpha\ne0\),
\[
\frac{\sum_{p\le X}p^{-1}p^{i\alpha}}{\sum_{p\le X}1/p}\longrightarrow0.
\]
Reason: Mertens' theorem gives \(\sum_{p\le X}1/p=\log\log X+B+o(1)\to\infty\). The numerator \(\sum_p p^{-1+i\alpha}\) converges conditionally for each fixed \(\alpha\ne0\), by partial summation and a sufficiently strong classical prime number theorem error bound (the integral \(\int e^{i\alpha u}du/u\) converges at infinity). Thus all nonzero integer Fourier modes of the normalized reciprocal-weighted prime angular measure vanish; Weyl's criterion yields weak convergence to uniform angular measure. **This is a known-theorem consequence, not a new RH constraint.** Convergence is extremely slow due to the denominator \(\log\log X\).

A prime power's von Mangoldt weight \(\Lambda(p^r)\) is not the same as a \(1/p\) prime weight. Do not substitute the latter into Weil's explicit formula without justification.

## Numerical finite-cutoff check (\(\alpha=1\), Python sieve)

| cutoff X | # primes | magnitude equal-count first Fourier moment | magnitude reciprocal-weighted moment | distance to equal-count PNT asymptotic |
|---:|---:|---:|---:|---:|
| 10,000 | 1,229 | 0.655738 | 0.383375 | 0.065741 |
| 100,000 | 9,592 | 0.666912 | 0.294891 | 0.052192 |
| 1,000,000 | 78,498 | 0.675006 | 0.289480 | 0.042655 |

These numbers were computed directly by a sieve and finite complex sums. They do not show the slow reciprocal-weighted limit numerically at these modest cutoffs; the asymptotic statement is analytic.

## Stronger interpretation and next test

There are two geometrically distinct measures on the *same* prime circle:
- counting measure gives a rotating wrapped-exponential profile;
- reciprocal-prime measure gives uniform Haar measure asymptotically.

The difference comes from sampling and the prime number theorem, not an independently discovered geometric law. To seek new RH leverage, use the **correct** von Mangoldt prime-power measure, the complete archimedean terms, and a fixed arithmetic test space; test a proposed circle operator against a modified positive-even theta kernel with known off-axis zeros (Chapter 24). No proof that any angular arc property excludes off-critical zeros has been found.

**Prior context:** Chapters 32–36, including the exact signed k-axis and its noninjective circle exponential; the dyadic prime example \(39.5=79/2\) remains prime in \(\mathbb Z[1/2]\), while zeta's ordinary prime index is 79.
