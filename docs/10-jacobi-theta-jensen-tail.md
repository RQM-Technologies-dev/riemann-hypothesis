# 10 — Direct Jacobi-theta tail bound via Jensen's formula

**Date:** 2026-11-02. **Status:** proved mathematical inequalities from standard Jacobi-theta/entire-function results; new application to our \(w\)-coordinate is a reformulation, **not** a proof of the Riemann Hypothesis. See [09](09-w-distance-rh-equivalence.md).

## A. Setup: fixed quaternionic geometry and the positive kernel

Choose one global scale \(L>0\), and no per-zero parameters:
\[
q=\cos\theta+\mathbf u\sin\theta,\qquad w=\cos\theta
=\frac{L^2-t^2}{L^2+t^2},\qquad \mathbf u^2=-1.
\]
For every positive critical-line zero ordinate \(\gamma\):
\[
d_L(\gamma)=1+w(\gamma)=\frac{2L^2}{L^2+\gamma^2}.
\]
This is **coordinate separation** from the infinity pole \(w=-1\), not a geodesic distance, and the fixed ambient four-dimensional radius is one.

The Jacobi theta function and the positive even Riemann kernel are
\[
\Theta(y)=\sum_{m\in\mathbb Z}e^{-\pi m^2 y},\quad
\omega(y)=y^2\Theta''(y)+\tfrac32 y\Theta'(y),\quad
\Phi(v)=2e^{v/2}\omega(e^{2v}).
\]
The classical identities are:
\[
\Phi(v)>0,\quad \Phi(-v)=\Phi(v),\qquad
X(z):=\xi(\tfrac12+iz)
=\int_{-\infty}^\infty \Phi(v)e^{izv}dv
=2\int_0^\infty\Phi(v)\cos(zv)\,dv.
\]
\(X\) is entire, even, real on the real axis, \(X(0)=\xi(1/2)>0\). This uses **the actual arithmetic theta kernel**, not an assumed sum of unknown zeros.

## B. The total-distance target is a hyperbolic theta moment

At \(z=-iL\), \(\cos(-iLv)=\cosh(Lv)\), so
\[
\xi(\tfrac12+L)=2\int_0^\infty\Phi(v)\cosh(Lv)\,dv.
\]
Differentiating in the real parameter \(L\) (permitted by super-exponential decay of \(\Phi\)) yields
\[
\xi'(\tfrac12+L)=2\int_0^\infty v\Phi(v)\sinh(Lv)\,dv.
\]
Thus
\[
\boxed{
T(L):=L\frac{\xi'(\frac12+L)}{\xi(\frac12+L)}
=L\frac{\int_0^\infty v\Phi(v)\sinh(Lv)\,dv}
{\int_0^\infty \Phi(v)\cosh(Lv)\,dv}.
}
\]
It may be read as a positive expectation \(T(L)=L\,\mathbb E_{p_L}[v\tanh(Lv)]\) under
\(p_L(v)=\Phi(v)\cosh(Lv)/\int_0^\infty\Phi(a)\cosh(La)\,da\). Every term is explicit, independent of zeta-zero heights.

With \(L=20\):
\[
T(20)=13.33099047799700248726506126097\ldots
\]
The real-axis Gamma/zeta expression and numerical theta-kernel quadrature agree to displayed digits. Floating-point agreement is a reproducibility check, not interval-certified proof; the mathematical equality above is analytic.

## C. An unconditional upper bound on critical-line zero counts

Let \(N_{\rm line}(T)\) be the number of *positive* real zeros of \(X(t)\) in \(0<t\le T\), counted with multiplicity. This counts only zeros **already on** the critical line; it is NOT assumed equal to the count of all nontrivial zeros.

For \(z=x+iy\), the identity
\[
|\cos((x+iy)v)|\le \cosh(|y|v)
\]
and the positivity of \(\Phi\) imply
\[
|X(z)|\le 2\int_0^\infty\Phi(v)\cosh(|y|v)\,dv
=\xi(\tfrac12+|y|).
\]
Therefore, for \(|z|\le2T\),
\[
\max_{|z|\le2T}|X(z)|\le\xi(\tfrac12+2T).
\]
Jensen's formula in the disk of radius \(2T\) centered at zero, with \(X(0)\ne0\), gives
\[
\#\{\text{zeros of }X:|z|\le T\}
\le
\frac{\log\bigl(\xi(\tfrac12+2T)/\xi(\tfrac12)\bigr)}
{\log2}.
\]
Each positive real zero \(\gamma\) has a negative real partner \(-\gamma\) with the same multiplicity; therefore
\[
\boxed{
N_{\rm line}(T)\le
J(T):=\frac{1}{2\log2}
\log\frac{\xi(\frac12+2T)}{\xi(\frac12)}.
}
\]
For boundary zeros at exactly the integration circle, use a limiting radius \(2T+\varepsilon\downarrow2T\). The inequality remains valid. It does **not** rely on RH.

## D. A rigorous upper bound on *all as-yet-unlisted line-zero distances*

Fix \(T>0\) and set \(f_L(t)=2L^2/(L^2+t^2)\), positive and decreasing, with
\[
-f_L'(t)=\frac{4L^2 t}{(L^2+t^2)^2}.
\]
The uncounted on-line tail above height \(T\) is
\[
S_{\rm line}^{>T}(L)=\sum_{\substack{\gamma>T\\X(\gamma)=0}}f_L(\gamma)
=\int_{(T,\infty)}f_L(t)\,dN_{\rm line}(t).
\]
Integrate by parts, use \(N_{\rm line}(t)\le J(t)\), and discard the nonpositive boundary term \(-f_L(T)N_{\rm line}(T)\). This proves the **fully explicit, theta-kernel-derived bound**
\[
\boxed{
0\le S_{\rm line}^{>T}(L)\le
B_\Theta(T,L):=
\frac{2L^2}{\log2}
\int_T^\infty
\frac{t}{(L^2+t^2)^2}
\log\frac{\xi(\frac12+2t)}{\xi(\frac12)}\,dt.
}
\]

Only one-dimensional integration of a known positive real-axis function remains; **no zero heights are needed to evaluate the right side**. Since the Gamma factor gives
\(\log\xi(\frac12+2t)=O(t\log t)\), the bound is \(O(L^2\log T/T)\) for fixed \(L\). In particular,
\[
\boxed{S_{\rm line}^{>T}(L)\to0\quad\text{as }T\to\infty}
\]
is rigorous and **unconditional**.

Numerical quadrature of the rigorous upper-bound expression (not a certified interval evaluation):
- \(L=20,\ T=\gamma_{200}\approx396.38185422:\quad B_\Theta\approx14.1143293542.\)
- \(L=20,\ T=3\times10^{12}:\quad B_\Theta\approx1.0612427603\times10^{-8}.\)

**This direct-Jensen bound is deliberately loose:** for \(T=\gamma_{200}\), the previous exact full-spectrum target minus the first 200 line terms already gives a stronger upper bound \(1.6474705367\). The achievement here is a rigorous *tail-decay theorem derived from the Jacobi kernel*, not an improvement of every finite numerical bound.

## E. Why tail decay DOES NOT prove the total exhausts the critical-line sum

Define the nonnegative off-line defect established in [09](09-w-distance-rh-equivalence.md):
\[
D(L)=T(L)-\sum_{\gamma\in\mathcal Z_{\rm line}^+}f_L(\gamma)\ge0.
\]
For a finite cutoff \(T\), the observable residual decomposes as
\[
R_T(L)=T(L)-\sum_{\substack{0<\gamma\le T\\X(\gamma)=0}}f_L(\gamma)
=D(L)+S_{\rm line}^{>T}(L).
\]
Thus
\[
\boxed{
\max(0,R_T-B_\Theta(T,L))\le D(L)\le R_T.
}
\]
As \(T\to\infty\), the tail disappears and the residual tends to \(D(L)\), **not necessarily zero**. To prove RH we would need an independent lower bound for the on-line tail (or an argument ruling out off-line contributions) strong enough to prove \(D(L)=0\). An upper bound alone cannot do that.

## F. Positive-even kernels do not force real zeros: a countermodel

Let \(g_\sigma(v)=(2\pi\sigma^2)^{-1/2}e^{-v^2/(2\sigma^2)}\), pick \(\sigma_1\ne\sigma_2>0\), and \(a>0\). Define the strictly positive, even, smooth kernel
\[
K(v)=\frac{1}{4a}\int_{-a}^a
\left[g_{\sigma_1}(v-y)+g_{\sigma_2}(v-y)\right]dy.
\]
Its Fourier transform is
\[
\widehat K(t)=\frac{\sin(at)}{at}
\,\frac{e^{-\sigma_1^2t^2/2}+e^{-\sigma_2^2t^2/2}}2.
\]
This has infinitely many **real** zeros \(t=k\pi/a\) (from the sine factor) *and* infinitely many **nonreal** zeros. Indeed, the Gaussian factor vanishes when
\[
e^{(\sigma_2^2-\sigma_1^2)t^2/2}=-1,
\quad\text{equivalently}\quad
t^2=\frac{2\pi i(2k+1)}{\sigma_2^2-\sigma_1^2}.
\]
The kernel is positive and even, and the real-axis Fourier transform rapidly tends to zero. Its compactified pullback likewise has an infinitely flat infinity pole, but **off-real zeros still exist**. This is a rigorous no-go example for a proof using *only* positivity, evenness, an infinite set of real zeros, and smooth polar return.

The **special arithmetic structure of the Jacobi theta kernel** must play a decisive role in any eventual RH proof; its positivity alone is insufficient.

## G. Next test

Combine the theta-Jensen bound with independently established explicit total-zero counts and verified finite-height RH. See [11](11-certified-distance-defect-bound.md) for a substantially sharper *weighted off-line defect bound* based on published mathematics. It still remains a strictly positive upper bound, so cannot prove RH.

## References

- Dan Romik, *Orthogonal polynomial expansions for the Riemann xi function*, equations (1.6)–(1.11): https://math.ucdavis.edu/~romik/data/uploads/papers/riemannxi.pdf
- Jensen's formula: https://mathworld.wolfram.com/JensensFormula.html
- Exact \(w\)-distance RH-equivalence: [09](09-w-distance-rh-equivalence.md)
