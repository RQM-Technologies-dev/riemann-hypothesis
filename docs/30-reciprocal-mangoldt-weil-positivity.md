# 30 — Reciprocal von Mangoldt pairing meets Weil's explicit formula

**Date:** 2026-11-08. **Result:** Exact bridge to a classical RH-equivalent positivity criterion; no new RH proof.

## 1. Inward/outward prime-power measure

For \(\Re s>1\), \(-\zeta'(s)/\zeta(s)=\sum_{n\ge1}\Lambda(n)n^{-s}\). On the critical line formal oscillatory prime-power terms have phase \(e^{-it\log n}\), and the reciprocal direction \(1/n\) has phase \(e^{+it\log n}\). Define a **finite** symmetric distribution
\[
\mu_N=\sum_{2\le n\le N}\frac{\Lambda(n)}{\sqrt n}\bigl(\delta_{\log n}+\delta_{-\log n}\bigr).
\]
Its Fourier transform is the exact trigonometric polynomial
\[
\widehat\mu_N(t)=2\sum_{2\le n\le N}\frac{\Lambda(n)}{\sqrt n}\cos(t\log n).
\]
For any fixed imaginary quaternion \(u^2=-1\), the quaternionic exponential pair obeys \(e^{ut\log n}+e^{-ut\log n}=2\cos(t\log n)\). Hence this paired expression is **real scalar**; no noncommuting quaternionic information survives the pairing.

Important: as \(N\to\infty\), the displayed cosine sum does **not** converge as an ordinary series on the critical line. Any infinite limit requires smoothing/distributional interpretation and the archimedean terms of the completed explicit formula.

## 2. Weil explicit formula is the established full bridge

The explicit formula for suitable test functions links the nontrivial zeros to prime powers with both \(f(n)\) and \(n^{-1}f(1/n)\), alongside archimedean/Gamma and pole terms. Thus the user's reciprocal-prime symmetry is **already present in the classical explicit formula**. Reference: Clay Mathematics Institute, *The Riemann Hypothesis*, https://www.claymath.org/library/monographs/MPPc.pdf (Weil formula); and https://openmaths.org/courses/NT-EXPF/NT-EXPF-04.html (positivity).

For suitable test functions \(g\), RH is equivalent to positive semidefiniteness of the Weil zero functional on \(g*\widetilde g\), with the appropriate Mellin normalization. Under RH this is a sum of squares of transformed test functions at zeros. Without RH, the positivity of the **complete** prime-plus-archimedean expression is not known for all admissible tests. This is the actual all-height inequality to investigate.

## 3. Explicit obstruction to naive positivity

Despite \(\Lambda(n)\ge0\), the symmetric Fourier sum has cosine factors of either sign. Example at \(N=2\):
\[
\widehat\mu_2(t)=\sqrt2\log2\cos(t\log2).
\]
At \(t=\pi/\log2\) it is \(-\sqrt2\log2<0\). Thus reciprocal pairing and nonnegative Mangoldt weights do not yield pointwise nonnegative spectral response. Even a positive-definite distribution need not have pointwise nonnegative Fourier transform under arbitrary interpretations; specify the actual Weil quadratic form.

## 4. 39.5 arithmetic target

The prime \(79\) contributes \(\Lambda(79)=\log79\) to the ordinary explicit formula; \(39.5=79/2\) remains a prime element in \(\mathbb Z[1/2]\). Replacing \(\log79\) by \(\log39.5\) or relocating its spectral frequency changes the original zeta function. The dyadic label is arithmetic association, not an independent new Euler factor.

## 5. Conclusions and falsification gates

- **Proved:** finite reciprocal Mangoldt pairing gives a cosine transform and fixed-axis quaternionic conjugate cancellation.
- **Established prior art:** Weil's explicit formula already contains outward/inward \(n\) and \(1/n\) terms; RH-equivalent positivity is known as a *criterion*, not a proved property.
- **Counterexample:** a single prime-power paired mode has negative values at some heights; termwise Mangoldt positivity does not imply the desired global inequality.
- **Open:** establish positivity of the complete Weil functional from a new independent theorem about the genuine Jacobi theta / arithmetic coefficients, for every admissible test function; any candidate must survive the negative control of Chapter 24.

This result narrows the research: a quaternionic version must contribute a new operator, inequality or representation beyond the scalar conjugate cosine pair. No proof of RH is claimed.
