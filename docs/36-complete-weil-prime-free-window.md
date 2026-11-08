# 36 — Complete Weil explicit-formula test with a prime-free support window

**Date:** 2026-11-08. **Status:** exact prime-support reduction and a concrete sign-analysis gate. **No proof of RH.**

## 1. Fix conventions instead of assuming an abstract positive factorization

Take a real, even \(g\in C_c^\infty(\mathbb R)\), with \(\operatorname{supp}g\subset(-a,a)\). Define its convolution \(f=g*g\), which is even, real, smooth and supported in \((-2a,2a)\). Let
\[
G(z)=\int_{\mathbb R}g(x)e^{izx}\,dx,\quad
h(z)=\widehat f(z)=G(z)^2.
\]
Since \(g\) is real and even, \(G(t)\) is real for real \(t\), so \(h(t)=|G(t)|^2\ge0\) on the real axis. The full zero-side form is \(\sum_\rho h((\rho-\frac12)/i)\), with all nontrivial zeros counted with multiplicity. For this restricted even-real test family, the classical Guinand–Weil explicit formula gives
\[
\boxed{\begin{aligned}
W(g)={}&h(i/2)+h(-i/2)\\
&-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\left[f(\log n)+f(-\log n)\right]\\
&+\frac1{2\pi}\int_{\mathbb R}h(t)
\left[\Re\psi\left(\frac14+\frac{it}{2}\right)-\log\pi\right]dt.
\end{aligned}}\tag{36.1}
\]
Here \(\psi=\Gamma'/\Gamma\), the digamma function. The sign and normalization follow the classical Guinand–Weil formula; this is not the positive jump energy of Chapter 32. The pole terms are \(h(\pm i/2)\); the Gamma/archimedean term is the displayed real integral. This formula holds without RH. For a general complex-valued \(g\), the positivity criterion requires a sesquilinear involution and a more general explicit formula; the restricted family used here is **not** claimed to be dense enough to establish RH.

## 2. Exact prime-free window

If
\[
\boxed{0<a<\tfrac12\log2,}
\]
then \(\operatorname{supp}f\subset(-2a,2a)\subset(-\log2,\log2)\). Every \(n\ge2\) has \(\log n\ge\log2\), so \(f(\log n)=f(-\log n)=0\). The complete formula becomes
\[
\boxed{
W(g)=2G(i/2)^2+
\frac1{2\pi}\int_{\mathbb R}G(t)^2
\left[\Re\psi\left(\frac14+\frac{it}{2}\right)-\log\pi\right]dt.}
\tag{36.2}
\]
Here \(G(i/2)=\int g(x)\cosh(x/2)\,dx\) is real. This identity is unconditional, uses the exact complete Weil formula, and includes **no** prime-power approximation.

The archimedean multiplier
\[
b(t)=\Re\psi(1/4+it/2)-\log\pi
\]
is **not pointwise nonnegative**: \(b(0)=\psi(1/4)-\log\pi<0\). Therefore the right-hand side of (36.2) is not *manifestly* a norm square, even though the pole term is nonnegative for real even g. The missing issue is a rigorous lower bound on the signed Gamma integral relative to the pole term for this restricted test class.

## 3. A finite-support falsification and a non-circularity warning

The restricted family does not contain the arbitrary Mellin tests required by Weil's RH-equivalent positivity theorem. Establishing \(W(g)\ge0\) only when \(2a<\log2\) would be a **partial theorem**, not RH.

Further, since \(h(t)\) is the square of a real entire transform, under RH the zero side is a sum of nonnegative terms. That observation is conditional; it cannot justify a positivity claim without independently estimating the right side of (36.2).

The shifted positive-even theta negative control from Chapter 24 has its *own* zero distribution and modified explicit formula, and cannot be substituted into (36.1) while retaining the genuine von Mangoldt coefficients. The correct negative-control check for any proposed universal analytic argument is to verify that it does not falsely conclude all zeros of the shifted transform are real.

## 4. Next proof task

Derive a rigorous inequality for the signed archimedean multiplier on the Paley–Wiener class \(G=\widehat g\) with \(\operatorname{supp}g\subset(-a,a)\), including explicit dependence on \(a\), and compare it with the rank-one pole contribution. If this succeeds, enlarge support past \(2a=\log2\), where the first genuine prime term appears. At that threshold the formula acquires the explicit negative contribution
\[
-\frac{\log2}{\sqrt2}[f(\log2)+f(-\log2)].
\]
A full RH proof would still need uniform positivity over **all** admissible test functions and all prime thresholds, not merely a finite sequence of cutoffs.

## References

- Guinand–Weil explicit formula with the even-test Fourier convention: https://www.claymath.org/library/proceedings/cmip06.pdf (Lagarias, Theorem 3.2 and discussion).
- https://openmaths.org/courses/NT-EXPF/NT-EXPF-01.html (general-test formula and compact-support prime cutoff).
- Chapters 17, 24, 32–35 in this repository.

**Outcome:** An exact, complete, zero-sensitive quadratic-form formula on a restricted prime-free test class, and a precise signed Gamma-term obstruction. No factorization or RH proof is asserted.
