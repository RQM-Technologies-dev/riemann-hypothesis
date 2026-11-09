# 35 — Full Weil explicit formula transported to the reciprocal k-axis

**Date:** 2026-11-08. **Status:** Exact coordinate transport and numerical cross-check; no new RH proof.

## 1. A precise completed explicit formula

Let \(h\) be even, entire, rapidly decaying in suitable horizontal strips, with Fourier transform \(\widehat h(u)=\int_{\mathbb R}h(t)e^{-itu}\,dt\). With the usual analytic continuation of the zero sum and sufficient admissibility, the classical Weil/Guinand explicit formula in the standard normalization is
\[
\boxed{
\sum_{\rho}h\bigl((\rho-\tfrac12)/i\bigr)
=h(i/2)+h(-i/2)
+\frac1{2\pi}\int_{\mathbb R}h(t)\left[\Re\psi(\tfrac14+\tfrac{it}{2})-\log\pi\right]dt
-\frac1\pi\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\widehat h(\log n).
}
\tag{1}
\]
Here the sum counts nontrivial zeros with multiplicities. The formula is written for even real-on-real \(h\); the archimedean term is \(\Re\psi\) on the real integration line. Its equality is unconditional and does not assume RH. For arbitrary off-line zeros the zero-side arguments \((\rho-1/2)/i\) are complex, so positivity of individual \(h\) terms is **not** automatic.

The prime-power sum is essential: \(\Lambda(p^r)=\log p\), \(r\ge1\), and is not restricted to primes.

## 2. Exact k-axis coordinate transport

Set \(a=\tanh t\in(-1,1)\), \(t=\operatorname{artanh}a\), and \(a_n=\tanh(\log n)=(n^2-1)/(n^2+1)\). Then \(dt=da/(1-a^2)\), and the archimedean term in (1) is exactly
\[
\frac1{2\pi}\int_{-1}^1
\frac{h(\operatorname{artanh}a)}{1-a^2}
\left[\Re\psi\left(\tfrac14+\tfrac i2\operatorname{artanh}a\right)-\log\pi\right]da.
\tag{2}
\]
The prime-power transform becomes
\[
\widehat h(\log n)=\int_{-1}^1
\frac{h(\operatorname{artanh}a)}{1-a^2}
e^{-i\,\operatorname{artanh}a\,\operatorname{artanh}a_n}\,da.
\tag{3}
\]
For even \(h\), its imaginary part cancels and the kernel is a cosine of the two hyperbolic coordinates. The same expression can be written in the fixed quaternionic \(k\)-slice with \(i\) replaced by \(k\); the integral is real scalar for even real \(h\).

The group law \(a\oplus b=(a+b)/(1+ab)\) makes \(a_n\) the reciprocal multiplication coordinate. The measure \(da/(1-a^2)\) is Haar measure of this group. Thus (2)–(3) are **exact** and retain all terms of the completed formula.

## 3. Numerical independent check with Gaussian tests

Take \(h_\sigma(t)=\exp[-t^2/(2\sigma^2)]\) with \(\widehat h_\sigma(u)=\sqrt{2\pi}\sigma\exp[-\sigma^2u^2/2]\). The pole contribution is \(2\exp[1/(8\sigma^2)]\). Numerically evaluating the arithmetic side of (1), and independently summing \(2h_\sigma(\gamma)\) over the first 24 known positive critical-line zero ordinates \(\gamma\) (not assuming there are no others), gives:

| \(\sigma\) | arithmetic side | first-24-known-zero side |
|---|---:|---:|
| 3 | 0.00003024072313018154 | 0.000030240723130183105 |
| 5 | 0.037082583462638964 | 0.037082583462638964 |
| 8 | 0.5002277175357088 | 0.5002277175357088 |

The Gaussian suppresses high zeros; this is a **numerical consistency check**, not a certification of the complete zero sum. The arithmetic computation includes prime powers to 9999, with negligible tail for these Gaussian widths. The script computes rather than hard-codes the values.

## 4. Does quaternionic transport add a new spectral constraint?

**No independent constraint has been found.** The substitution \(t\leftrightarrow a\) is invertible and the appropriate \(L^2\) spaces are unitarily equivalent. For the fixed \(k\)-slice, the quaternionic Fourier kernel commutes and is algebraically the same as the complex kernel. In particular:
- Equation (1) and the transformed equations (2)–(3) contain precisely the same information.
- The archimedean term is not a positive diagonal correction of the Chapter 34 prime Laplacian.
- Positive Gaussian tests at selected widths cannot prove positivity for all Weil test functions.
- Off-axis-zero counterexamples of the Chapter 24 modified theta kernel remain valid negative controls against deriving RH from symmetry, flatness, or coordinate compactification alone.

The next viable step is a **canonical noncommuting** \(i,j,k\) arithmetic coupling, if one can derive it from the exact theta coefficients and establish an operator property not unitarily equivalent to (1). Adding arbitrary quaternionic matrices would not qualify.

**Retained arithmetic goal:** \(39.5=79/2\) is prime in \(\mathbb Z[1/2]\), while the zeta formula's von Mangoldt index remains 79.

## References
- Classical Guinand–Weil explicit formula (normalization as written in (1)); NIST DLMF §§25.4, 25.10.
- Prior chapters 24, 30, 31, 33, 34.
