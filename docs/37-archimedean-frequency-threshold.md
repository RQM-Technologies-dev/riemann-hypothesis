# 37 — Archimedean sign threshold and the missing band-limited coercivity

**Date:** 2026-11-08. **Status:** exact sign theorem for the Gamma multiplier, explicit support-dependent uncertainty bound, and an identified gap. No RH proof.

## 1. Starting point

For real even \(g\in C_c^\infty((-a,a))\), \(0<a<\log2/2\), let \(G(t)=\int g(x)e^{itx}dx\). Chapter 36 gives the complete prime-free Guinand–Weil form
\[
W(g)=2G(i/2)^2+\frac1{2\pi}\int_{\mathbb R}b(t)|G(t)|^2dt,
\quad b(t)=\Re\psi(\tfrac14+\tfrac{it}{2})-\log\pi.
\tag{37.1}
\]
This is an exact identity, not a positivity claim. The support restriction removes every prime-power term.

## 2. Exact sign structure of the Gamma term

The digamma expansion for \(a_0>0\) gives
\[
\Re\psi(a_0+iy)-\psi(a_0)
=\sum_{k=0}^\infty
\frac{y^2}{(k+a_0)((k+a_0)^2+y^2)}.
\tag{37.2}
\]
Every summand is positive for \(y\ne0\), and its derivative with respect to \(y>0\) is strictly positive. Thus \(b(t)\) is even and **strictly increasing** for \(t>0\). Also \(b(0)=\psi(1/4)-\log\pi=-\gamma-\pi/2-3\log2-\log\pi\approx-5.37218341922566558\), using \(\psi(1/4)=-\gamma-\pi/2-3\log2\). Stirling gives \(b(t)\sim\log(|t|/(2\pi))\to+\infty\). Therefore a unique \(T_*>0\) exists with \(b(T_*)=0\), numerically \(T_*\approx6.28983598883690278\). In particular
\[
b(t)<0\ (|t|<T_*),\qquad b(t)>0\ (|t|>T_*).
\tag{37.3}
\]
This is a **proved global sign classification**, not a proof that its weighted integral is nonnegative.

## 3. Exact low-frequency obstruction and an uncertainty bound

Split
\[
W(g)=2G(i/2)^2+
\frac1{2\pi}\left(
-\int_{|t|<T_*}|b(t)||G(t)|^2dt+
\int_{|t|>T_*}b(t)|G(t)|^2dt
\right).
\tag{37.4}
\]
The negative Gamma contribution is confined to a **finite frequency interval**; all sufficiently high frequencies contribute positively. This is an exact reformulation of the support-restricted proof target.

By Cauchy–Schwarz,
\[
|G(t)|^2\le2a\int_{-a}^a|g(x)|^2dx.
\]
Hence
\[
\frac1{2\pi}\int_{-T}^T|G(t)|^2dt
\le\frac{2aT}{\pi}\|g\|_2^2,\qquad T>0.
\tag{37.5}
\]
This is a rigorous Paley–Wiener low-frequency concentration bound. At the prime-free maximum \(a<\log2/2\) and \(T=T_*\), the prefactor \(2aT_*/\pi\) can exceed 1, so the estimate alone does **not** control the negative band by the positive tail. The sharper concentration operator (prolate spheroidal) has largest eigenvalue strictly below 1 for finite \(a,T\), but that alone still lacks a quantified lower bound on the *weighted* positive tail sufficient to dominate the negative band and the pole term.

The rank-one pole term is not universally coercive: nonzero real even smooth \(g\) can be chosen with \(\int g(x)\cosh(x/2)dx=G(i/2)=0\) by taking a nontrivial linear combination of two independent even bumps. Thus it cannot by itself dominate the negative Gamma integral for all \(g\).

## 4. A precise candidate theorem

For all real even \(g\in C_c^\infty((-a,a))\), \(0<a<\log2/2\), prove
\[
\boxed{
\int_{|t|>T_*}b(t)|G(t)|^2dt+4\pi G(i/2)^2
\ \ge\
\int_{|t|<T_*}|b(t)||G(t)|^2dt.
}
\tag{37.6}
\]
This is exactly \(W(g)\ge0\) on the prime-free restricted class, and **remains unproved here**. The restriction is crucial: even if (37.6) were proved, it would not imply RH for all admissible tests.

## 5. Threshold crossing to prime 2

As \(a\) passes \(\log2/2\), the convolution \(f=g*g\) can reach \(\pm\log2\). The full form acquires
\[
-\frac{\log2}{\sqrt2}[f(\log2)+f(-\log2)]
=-\sqrt2\log2\,f(\log2)
\]
for real even \(g\). Importantly, \(f(\log2)=\int g(u)g(\log2-u)du\) is **not necessarily nonnegative** if \(g\) changes sign. It is an autocorrelation at a shift, not a squared norm. More prime-power thresholds enter at \(2a=\log n\).

An eventual full Weil positivity proof must handle these signed autocorrelations, the Gamma band, and the pole term simultaneously for every admissible test function.

## 6. Interpretation

The complete formula has a definite low-frequency negative Gamma band and a high-frequency positive band. This is a more concrete analytic target than generic quaternionic Gram positivity. The nontrivial step is a **support-dependent weighted uncertainty/coercivity theorem** with constants strong enough to dominate the low band; neither simple Cauchy–Schwarz nor the quaternionic pole geometry provides it. A future theorem must also extend across all prime thresholds.

References: Chapter 36; standard digamma partial fractions and asymptotics (DLMF §§5.7, 5.11).
