# 14 — Higher Jacobi-theta moment minorants: a stronger local certificate, not global RH

**Date:** 2026-11-02. **Status:** mathematically rigorous *symbolic* hierarchy of zero-free sufficient conditions derived from the actual positive Riemann theta kernel. Decimal boundaries are numerical estimates, **not interval-certified endpoints**. Neither the hierarchy nor any finite calculation proves RH or the scale-free exhaustion equality \(\mathcal E=0\).

## 1. Continue from the real obstruction, not the quaternion drawing

Previous work ([13](13-theta-kernel-local-growth-certificate.md)) proved:
- a zero-free vertical rectangle for \(|x|<6.545059859\ldots\), \(|y|\le1/2\);
- strict outward growth \(\partial_y|X(x+iy)|^2>0\) for \(|x|<4.821134613\ldots\), \(0<y\le1/2\).

Here \(X(z)=\xi(1/2+iz)\), \(z=x+iy\), so \(x\) is the ordinary zeta *height*, \(y\) encodes displacement from the critical line, and **neither is physical time**.

We extend the FIRST result (zero exclusion) by keeping more harmonic moments. This does **not** extend the SECOND result (outward growth) automatically. Distinguishing these two theorems matters.

## 2. Globally valid odd Taylor cosine minorants

For an odd positive integer \(n=2m+1\), define
\[
P_{2n}(z)=\sum_{k=0}^{n}\frac{(-1)^k z^{2k}}{(2k)!}.
\]
This is a true global lower bound on the cosine:
\[
\boxed{\cos z\ge P_{2n}(z)\quad(z\in\mathbb R,\quad n\text{ odd}).}
\]
For \(z\ge0\), an explicit proof is the identity
\[
P_{2n}(z)-\cos z
=\frac{(-1)^n}{(2n-1)!}
\int_0^z (z-r)^{2n-1}(1-\cos r)\,dr.
\]
The integral is nonnegative and \(n\) is odd, giving the inequality for \(z\ge0\); both sides are even so it holds for all real \(z\).

This global fact is stronger than merely saying a Taylor series approximates a cosine near the origin.

## 3. Exact kernel moments and their monotonicity

Let \(\Phi(v)>0\) be the standard even Jacobi-theta kernel, restricted to \(v\ge0\), and write
\[
A(y)=\int_0^\infty\Phi(v)\cosh(yv)\,dv>0.
\]
For \(k\ge0\), define the normalized even moments
\[
\boxed{
\mu_{2k}(y)=
\frac{\int_0^\infty v^{2k}\Phi(v)\cosh(yv)\,dv}
{A(y)}.
}
\]
The exact identity \(A(y)=\frac12\xi(\frac12+y)\) yields
\[
\boxed{\mu_{2k}(y)=
\frac{\xi^{(2k)}(\frac12+y)}{\xi(\frac12+y)}.}
\]
Derivatives are in the argument of the completed zeta function, not physical time.

Under the probability measure proportional to \(\Phi(v)\cosh(yv)\,dv\), differentiation gives
\[
\mu'_{2k}(y)
=\operatorname{Cov}_{p_y}\bigl(V^{2k},V\tanh(yV)\bigr)\ge0
\quad(y\ge0),
\]
as both factors are increasing functions of \(V\). Thus, uniformly over \(|y|\le\frac12\):
\[
\mu_{2k}(0)\le\mu_{2k}(y)\le\mu_{2k}(\frac12).
\]

## 4. The entire *unconditional* polynomial hierarchy

From the real part of Riemann's Fourier transform,
\[
\Re X(x+iy)=2\int_0^\infty\Phi(v)\cos(xv)\cosh(yv)\,dv,
\]
insert the global cosine minorant and divide by \(2A(y)>0\).

For odd \(n\), define an explicit, y-independent polynomial
\[
\boxed{
B_n(x)=
\sum_{k=0}^{n}\frac{(-1)^k x^{2k}}{(2k)!}
\begin{cases}
\mu_{2k}(0),&k\text{ even},\\
\mu_{2k}(1/2),&k\text{ odd}.
\end{cases}
}
\]
Positive coefficients are bounded below using \(y=0\); negative coefficients are bounded above using \(y=1/2\). It follows *without RH or a zero table* that
\[
\boxed{\frac{\Re X(x+iy)}{2A(y)}\ge B_n(x)
\quad(x\in\mathbb R,\ |y|\le1/2).}
\]
Therefore:
\[
\boxed{ B_n(x)>0\Longrightarrow X(x+iy)\ne0
\quad\text{for every }|y|\le1/2.}
\]

This is a real theorem with completely specified coefficients determined by the theta kernel. **An exact zero-free region** is
\[
|x|<r_n,\qquad r_n:=\inf\{r>0:B_n(r)\le0\}.
\]
By \(B_n(0)=1\), this region has positive width. The proof requires no numerical root certification; the decimal evaluations below only suggest the size of the region.

The first member \(B_1\) reduces to the earlier quadratic certificate of [13](13-theta-kernel-local-growth-certificate.md), so this is a mathematically consistent extension.

## 5. Numerical illustration, NOT interval-certified root locations

With \(\mu_{2k}\) evaluated by the *actual* theta kernel through 40-digit mpmath quadrature (the numerical theta sum was truncated after 7 terms and the v-integral after 3; both tails decay super-exponentially):

| Odd \(n\) | Degree \(2n\) | First positive root \(r_n\), approximate | \(B_n(9)\), approximate |
|---:|---:|---:|---:|
| 1 | 2 | 6.545059859 | −0.8908530 |
| 3 | 6 | 8.333952201 | −0.1761364 |
| 5 | 10 | 9.500409456 | +0.06266934 |
| 7 | 14 | 9.881883806 | +0.08194584 |
| 9 | 18 | 9.913093758 | +0.08260999 |

These are *diagnostic values*. A formally certified rational interval for \(r_9\) would require validated quadrature/error bounds plus polynomial root isolation. The exact conditional inequality \(\Re X/(2A)\ge B_9\) is rigorous independently of such numeric certification.

The first nontrivial zero is near height 14.1347, so even the most promising high-order bound stays below it. This is an improved partial certificate, not new evidence for RH.

## 6. What this means on the common quaternionic hypersphere

The stereographic geometry **still has arbitrary symbolic** \(L>0\). A fixed spectral height \(x\) maps to
\[
\theta_L(x)=2\arctan(x/L),\qquad w_L(x)=\frac{L^2-x^2}{L^2+x^2}.
\]
The exact root-defined band \(|x|<r_n\) translates into a *zero-free angular cap*
\[
0\le\theta_L(x)<2\arctan(r_n/L)\quad(x\ge0),
\]
with the conjugate cap on the returning half. Changing \(L\) shifts the angular latitude boundaries but never changes the underlying spectral-height bound or the zeta-zero locations.

**No per-zero normalization is used.** Geometry and analysis remain separate.

## 7. The no-go insight for a global proof

Every single polynomial \(B_n\) here has **negative leading coefficient** (since n is odd and \(\mu_{2n}(1/2)>0\)). Therefore
\[
B_n(x)\longrightarrow-\infty\qquad(|x|\to\infty)
\]
for every fixed finite n.

So **no one finite polynomial of this particular hierarchy can certify all spectral heights**. Increasing n with x could improve a *local* estimate, but a uniform theorem would need nontrivial control of the whole infinite moment expansion.

There is a more fundamental obstruction: on the real axis \(y=0\), the real completed \(\Xi(x)\) changes sign between its simple critical-line zeros. Thus no global proof can rely on \(\Re X(x+iy)>0\) for all \(x\).

The real global target from [13](13-theta-kernel-local-growth-certificate.md) remains
\[
\partial_y|X(x+iy)|^2>0
\quad\forall x\in\mathbb R,\ y>0,
\]
or equivalently the scale-free exhaustion \(\mathcal E=0\).
The cosine-moment hierarchy is a **local tool**, not a substitute for global arithmetic cancellation.

## 8. Context, attribution, and next proof target

- Hinkkanen–Lagarias' global growth condition (see Michel Planat, *Symmetry* 18(8), 1283, 2026) is RH-equivalent. Positive kernel amplitudes alone do not prove it because oscillatory cosines have both signs: https://doi.org/10.3390/sym18081283
- Planat and Solé, *Second-Level Concavity of the Riemann Xi Kernel* (Aug 2026), prove a more sophisticated theta-kernel log-concavity theorem, still without RH: https://arxiv.org/abs/2608.19160
- Suvrit Sra, *On some positivity properties of the Riemann Xi function*, **v3 (2 Nov 2026)**: major finite-order PF positivity and local generalized Laguerre inequalities, not PF∞ or RH. https://suvrit.github.io/papers/riem-xi/

The next target is to apply a similarly global cosine minorant **to the bilinear growth integral** \(CC_y+SS_y\), and to investigate whether the theta modular identity supplies additional information that survives the oscillatory signs for large heights. The bilinear finite-order certificate will also necessarily be local unless accompanied by a genuinely new uniform arithmetic estimate.

## Reproducibility

See [numerical script](../experiments/higher_moment_cosine_certificate.py), [unit tests](../tests/test_higher_moment_cosine_certificate.py), and [results](../results/higher_moment_cosine_certificate.json). The script computes the coefficients from \(\Phi\), not from known zeros.
