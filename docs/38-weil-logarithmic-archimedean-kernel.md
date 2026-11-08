# 38 — Exact logarithmic-coordinate Gamma kernel in the Weil form

**Date:** 2026-11-08. **Status:** exact integral representation and an arithmetic threshold decomposition. No proof of RH.

## 1. Conventions

Retain Chapter 36's restricted real-even \(g\in C_c^\infty((-a,a))\), \(f=g*g\), \(G(t)=\int_{\mathbb R}g(x)e^{itx}dx\), \(h(t)=G(t)^2=\widehat f(t)\). Let
\[
b(t)=\Re\psi(\tfrac14+\tfrac{it}{2})-\log\pi.
\]
The complete Guinand–Weil form is
\[
W(g)=2G(i/2)^2-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}f(\log n)+\frac1{2\pi}\int_{\mathbb R}b(t)h(t)dt.
\tag{38.1}
\]
The prime sum is finite for each compactly supported \(f\), since \(f(\log n)=0\) for \(\log n>2a\). This is an identity without RH, not a positivity assertion.

## 2. Gamma term exactly in the logarithmic coordinate

For \(\Re z>0\), the digamma integral is
\[
\psi(z)=-\gamma+\int_0^\infty\frac{e^{-v}-e^{-zv}}{1-e^{-v}}dv.
\]
Consequently,
\[
b(t)=-\gamma-\log\pi+\int_0^\infty
\frac{e^{-v}-e^{-v/4}\cos(tv/2)}{1-e^{-v}}dv.
\]
Fourier inversion with \(h=\widehat f\) gives
\[
\frac1{2\pi}\int h(t)dt=f(0),\quad
\frac1{2\pi}\int h(t)\cos(tv/2)dt=f(v/2)
\]
because \(f\) is even. The cancellation at \(v=0\) permits interchanging after a cutoff and dominated-convergence justification for Schwartz \(h\). Therefore
\[
\boxed{
\frac1{2\pi}\int b(t)h(t)dt
=(-\gamma-\log\pi)f(0)
+\int_0^\infty
\frac{e^{-v}f(0)-e^{-v/4}f(v/2)}{1-e^{-v}}dv.
}
\tag{38.2}
\]
This is a rigorous **archimedean log-coordinate formula**. It retains a subtraction of two terms: neither term is independently integrable at \(v=0\); never split them without regularization.

With \(v=2x\), the same identity is
\[
(-\gamma-\log\pi)f(0)+2\int_0^\infty
\frac{e^{-2x}f(0)-e^{-x/2}f(x)}{1-e^{-2x}}dx.
\tag{38.3}
\]
The exact complete quadratic form becomes
\[
\boxed{\begin{aligned}
W(g)={}&2\left(\int_{\mathbb R}g(x)\cosh(x/2)dx\right)^2
+(-\gamma-\log\pi)f(0)\\
&+2\int_0^\infty
\frac{e^{-2x}f(0)-e^{-x/2}f(x)}{1-e^{-2x}}dx
-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}f(\log n).
\end{aligned}}
\tag{38.4}
\]
All pieces are explicitly expressed in terms of the same \(f=g*g\) and its values at logarithmic shifts. The pole term is a square; the archimedean term is a **signed integral**, and the prime terms are **signed samples**. Their sum is not manifestly nonnegative.

## 3. Prime-free support window and the threshold

For \(0<a<\log2/2\), \(f\) vanishes at all \(\log n\), \(n\ge2\), and (38.4) contains no primes. Once \(2a>\log2\), the first prime contribution is
\[
-\sqrt2\log2\,f(\log2).
\]
The next threshold is \(2a=\log3\), then \(\log4\) (prime power \(2^2\)), etc. This gives a sequence of exact, finite-support arithmetic tests without truncating the infinite explicit formula artificially.

## 4. What can and cannot be concluded

The integrand in (38.3) is not automatically positive. For a sign-changing even \(g\), the convolution \(f(x)=\int g(y)g(x-y)dy\) can have either sign at nonzero \(x\). The pole term vanishes for some nonzero \(g\) orthogonal to \(\cosh(x/2)\). Thus neither the square nor the integral supplies a universal coercivity theorem.

The exact Jacobi-theta/von Mangoldt arithmetic enters the full Weil form through the **specific samples** \(\Lambda(n)f(\log n)/\sqrt n\), not through an arbitrary nonnegative translation energy. A genuinely new proof would need a global inequality for the full combination (38.4), on the correct full admissible test class, rather than just its prime-free restriction.

The shifted-kernel off-axis negative control in Chapter 24 does not share the original zeta explicit formula; a proof must not apply (38.4) to it with the same von Mangoldt weights.

## 5. Next mathematical gate

Investigate a lower bound on the archimedean integral plus pole term that compensates for all the signed prime samples for every compactly supported admissible \(g\), with constants independent of support \(a\). The bound must survive arbitrarily large \(\log n\) thresholds and the complete test class. Any proof for bounded support is only a partial theorem; no RH proof is obtained here.

**References:** Guinand–Weil explicit formula (Chapter 36); digamma integral DLMF §5.9; Chapters 17, 18, 24, 32–37.
