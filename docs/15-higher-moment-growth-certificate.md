# 15 — A higher-moment kernel certificate for **outward Xi growth**

**2026-11-02.** Continues [13](13-theta-kernel-local-growth-certificate.md) and [14](14-higher-moment-cosine-certificate.md). Exact *symbolic* theorem, **not** a proof of the Riemann hypothesis. Decimal roots are illustrative numerical quadrature, not validated interval enclosures. The central open problem still concerns **arbitrarily large** spectral heights.

## 1. The correct global problem

Define \(X(z)=\xi(\tfrac12+iz)\), with \(z=x+iy\). The global Hinkkanen–Lagarias criterion (also discussed by Planat, 2026) says RH is equivalent to strict positivity of
\[
\partial_y|X(x+iy)|^2>0 \quad (x\in\mathbb R,\ y>0).
\]
Our model requires no physical time, particle mass, or fixed stereographic parameter \(L\).

Let \(\Phi\) be the usual positive, even, super-exponentially decaying Riemann Jacobi-theta kernel with
\[
X(z)=2\int_0^\infty\Phi(v)\cos(zv)\,dv.
\]
For \(x\in\mathbb R\), \(y\ge0\), put
\[
C(x,y)=\int_0^\infty\Phi(v)\cos(xv)\cosh(yv)\,dv,
\]
\[
S(x,y)=\int_0^\infty\Phi(v)\sin(xv)\sinh(yv)\,dv,\quad
G(x,y)=CC_y+SS_y=\tfrac18\partial_y|X(x+iy)|^2.
\]
Subscripts denote partial derivatives in y, not physical time.

## 2. The exact *signed* double integral

Expand products and use standard trigonometric/hyperbolic identities:
\[
G(x,y)=\frac14\int_0^\infty\!\!\int_0^\infty\Phi(u)\Phi(v)
\left[
a\sinh(ya)\cos(xb)+b\sinh(yb)\cos(xa)
\right]du\,dv,
\quad a=u+v,\quad b=u-v.
\]
The amplitudes \(a\sinh(ya)\) and \(b\sinh(yb)\) are **nonnegative for y>0**, including b<0. The difficulty is entirely in the cosines.

## 3. A global cosine polynomial minorant

For each odd integer \(n=2m+1\ge1\), define
\[
P_{2n}(z)=\sum_{k=0}^n \frac{(-1)^kz^{2k}}{(2k)!}.
\]
The integral Taylor identity in [14](14-higher-moment-cosine-certificate.md) gives \(\cos z\ge P_{2n}(z)\) for **every real z**.

Insert this in both cosine terms above. Each multiplier is nonnegative, so inequality direction is preserved:
\[
G(x,y)\ge\sum_{k=0}^n\frac{(-1)^kx^{2k}}{(2k)!}J_k(y),
\]
with exact nonnegative moments
\[
\boxed{
J_k(y)=\frac14\int_0^\infty\!\!\int_0^\infty
\Phi(u)\Phi(v)
\left[a\sinh(ya)b^{2k}+b\sinh(yb)a^{2k}\right]du\,dv.
}
\]

## 4. Make the bound **uniform over the entire critical-strip width**

For every real q and \(0<y\le\tfrac12\),
\[
yq^2\le q\sinh(yq)\le yq^2\cosh(q/2).
\]
This is valid for negative q as well, because both sides are even in q. Thus
\[
yJ_k^-\le J_k(y)\le yJ_k^+
\]
where the positive, fixed theta-kernel moments are
\[
\boxed{
J_k^-=\frac14\int_0^\infty\!\!\int_0^\infty\Phi(u)\Phi(v)
\left[a^2b^{2k}+b^2a^{2k}\right]du\,dv,
}
\]
\[
\boxed{
J_k^+=\frac14\int_0^\infty\!\!\int_0^\infty\Phi(u)\Phi(v)
\left[
a^2\cosh(a/2)b^{2k}
+b^2\cosh(b/2)a^{2k}
\right]du\,dv.
}
\]
Use the smaller \(J_k^-\) in positive Taylor terms (even k) and larger \(J_k^+\) in negative terms (odd k). The **entirely y-independent** polynomial is
\[
\boxed{
H_n(x):=
\sum_{k=0}^n\frac{(-1)^k x^{2k}}{(2k)!}
\begin{cases}
J_k^-,&k\text{ even},\\
J_k^+,&k\text{ odd}.
\end{cases}
}
\]

### Theorem (exact partial growth certificate)

For every odd n, every real x and \(0<y\le\tfrac12\),
\[
\boxed{
G(x,y)\ge yH_n(x).
}
\]
Therefore
\[
\boxed{
H_n(x)>0\implies\partial_y|X(x+iy)|^2>0
\quad\text{for all }0<y\le\tfrac12.
}
\]
Define the exact first-root boundary
\[
r_n:=\inf\{r>0:H_n(r)\le0\}.
\]
Because \(H_n(0)=J_0^->0\), the implication holds rigorously for every \(|x|<r_n\), irrespective of whether its decimal value has been certified.

**This extends a local theorem, not RH.** Every odd n gives a polynomial with negative highest-degree coefficient, so \(H_n(x)\to-\infty\) for \(|x|\to\infty\). A fixed truncation cannot reach all heights.

## 5. Numerical diagnostics using only the theta kernel

For reproducibility, [the numerical experiment](../experiments/higher_moment_growth_certificate.py) integrates \(\Phi\) on \(v\in[0,3]\), truncates its theta sum after n=7, and computes the two-dimensional moments with Gauss–Legendre nodes. Changing the numerical node count from 160 to 350 stabilized the listed roots to the quoted digits; this is **not certified interval analysis**.

| odd n | polynomial degree | first-root estimate \(r_n\) | \(H_n(7)\), approx |
|---:|---:|---:|---:|
| 1 | 2 | 4.842068639 | negative |
| 3 | 6 | 6.063465859 | negative |
| 5 | 10 | 6.855327469 | negative |
| 7 | 14 | 7.151018041 | \(6.04\times10^{-5}\) |
| 9 | 18 | 7.184398593 | \(6.94\times10^{-5}\) |

The earlier simpler strict-growth result was \(|x|<4.821134614\ldots\) ([13](13-theta-kernel-local-growth-certificate.md)). This finite-order theta-moment method gives a **stronger numerically estimated** local range.

An independent check from the completed zeta function uses
\[
G(x,y)=\frac14\Re\bigl[\xi'(\tfrac12+y+ix)\overline{\xi(\tfrac12+y+ix)}\bigr].
\]
At \(x=7\), high-precision direct evaluation of \(G/y\) is approximately \(0.0003600\) at y=0.01, \(0.0003602\) at y=0.1, and \(0.0003650\) at y=0.5. The order-9 theta minorant gives \(H_9(7)\approx0.00006940\). This is a nontrivial numerical check of the exact inequality, but it is not a formal verification of the numerical first root.

## 6. Remain faithful to the user's quaternionic geometry

For **every** scale \(L>0\),
\[
\theta_L(x)=2\arctan(x/L),\qquad
w_L(x)=\frac{L^2-x^2}{L^2+x^2}.
\]
The theorem \(|x|<r_n\) maps to the polar cap
\[
\boxed{0\le\theta_L(x)<2\arctan(r_n/L),}
\]
and its conjugate return. The spectral condition, the zero positions, and any truth about RH are **independent of L**. This is a coordinate change, not separate normalization of each sphere.

## 7. What this teaches us about the final proof

We now have TWO explicit moment hierarchies:
- [14](14-higher-moment-cosine-certificate.md): stronger zero exclusion (approximate numerical boundary 9.913);
- this note: stronger **strict-growth** exclusion (approximate numerical boundary 7.184).

Both are mathematically rigorous *sufficient conditions* via exact moment integrals; the decimals are approximate. Neither covers all x. In particular, the signed cosines cannot be made globally positive by any single fixed-degree polynomial.

We have **not** proved \(\mathcal E=0\), nor proved RH. A genuinely global theorem must exploit theta modular/arithmetic structure beyond positive moments to control arbitrarily high oscillatory frequencies. Recent higher-order theta-kernel concavity and finite-order Pólya frequency results reinforce why finite inequalities, even very strong ones, are not a substitute for the infinite-order real-zero criterion.

## References

- Hinkkanen–Lagarias criterion and theta decomposition: Michel Planat, *A Theta-Kernel Reformulation of Riemann-Xi Growth and the Obstruction to Blockwise Positivity*, *Symmetry* 18(8), 1283 (2026): https://doi.org/10.3390/sym18081283
- M. Planat & P. Solé, *Second-Level Concavity of the Riemann Xi Kernel*, arXiv:2608.19160 (2026): https://arxiv.org/abs/2608.19160
- Suvrit Sra, *On some positivity properties of the Riemann Xi function*, v3 (2 Nov 2026): https://suvrit.github.io/papers/riem-xi/
- [Reproducible script](../experiments/higher_moment_growth_certificate.py), [tests](../tests/test_higher_moment_growth_certificate.py), [numerical summary](../results/higher_moment_growth_certificate.json).
