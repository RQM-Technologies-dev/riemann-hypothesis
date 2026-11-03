# 13 — Jacobi-theta local growth certificate: what positivity really proves

**2026-11-02. Status:** a mathematically rigorous, unconditional *partial* positivity theorem using the actual Jacobi-theta kernel. It is **not a proof of RH**, and its zero-free range is weaker than the classical verified zero-free range. The global growth criterion itself is classical (Hinkkanen–Lagarias), with a recent theta-kernel double-integral presentation by Michel Planat (2026).

## 0. Why this note exists

The scale-free exhaustion deficit established in [12](12-symbolic-scale-and-defect.md) is
\[
\mathcal E=
\frac{\xi''(1/2)}{\xi(1/2)}
-2\sum_{\gamma>0,\ \xi(1/2+i\gamma)=0}\frac1{\gamma^2}\ge0,
\quad \mathrm{RH}\iff\mathcal E=0.
\]
The user requested a kernel-only derivation of \(\mathcal E=0\). No such derivation was found. Instead we derive two honest partial theorems directly from the kernel's moment structure, quantify where strict growth follows, and isolate the oscillatory obstruction beyond that region.

All complex variables are mathematical; the spectral height is **not physical time**. The stereographic parameter \(L\) remains arbitrary and does not occur in the analytic kernel inequalities.

## 1. The standard completed zeta kernel

Let
\[
X(z)=\xi(1/2+iz)=2\int_0^\infty\Phi(v)\cos(zv)\,dv.
\]
Here \(z=x+iy\) and \(\Phi(v)>0\) is the positive, even, super-exponentially decaying Jacobi-theta kernel documented in [08](08-theta-kernel-zero-latitudes.md). The relevant critical strip \(0\le\Re s\le1\) becomes \(|y|\le1/2\) under \(s=1/2+iz\). The real coordinate \(x\) is zeta height.

Introduce
\[
A(y)=\int_0^\infty\Phi(v)\cosh(yv)\,dv
=\frac12\,\xi(1/2+y)
\]
(the last equality follows from the functional equation). The moment derivatives are
\[
A^{(2k)}(y)=\int_0^\infty v^{2k}\Phi(v)\cosh(yv)\,dv,\quad
A^{(2k+1)}(y)=\int_0^\infty v^{2k+1}\Phi(v)\sinh(yv)\,dv.
\]
These formulas converge and permit differentiating under the integral. The \(A^{(n)}\) are y-derivatives, **not differentiation in physical time**.

## 2. A theta-only zero-free rectangle

For real \(x\), \(\cos(xv)\ge1-x^2v^2/2\). Thus
\[
\begin{aligned}
\Re X(x+iy)
&=2\int_0^\infty\Phi(v)\cos(xv)\cosh(yv)\,dv\\
&\ge2\bigl[A(y)-\tfrac12 x^2 A''(y)\bigr].
\end{aligned}
\]
Define \(\mu_2(y)=A''(y)/A(y)\), the second moment of the probability density proportional to \(\Phi(v)\cosh(yv)\), \(v\ge0\).

For \(y\ge0\),
\[
\mu_2'(y)=\mathrm{Cov}_{p_y}\bigl(v^2,v\tanh(yv)\bigr)\ge0,
\]
because both functions of \(v\) are increasing and the covariance of two increasing functions of one real random variable is nonnegative.

For \(0\le y\le1/2\),
\[
\mu_2(y)\le\mu_2(1/2)=\frac{\xi''(1)}{\xi(1)}.
\]
Hence \(\Re X(x+iy)>0\), and therefore \(X(x+iy)\ne0\), whenever
\[
\boxed{
|x|<x_{\rm zero}:=\sqrt{\frac{2\,\xi(1)}{\xi''(1)}}
=6.54505985926647684\ldots,\qquad |y|\le1/2.
}
\]
Evenness/conjugation gives the negative-\(y\) case. This is a completely unconditional theta-kernel argument, but much weaker than the already known zero-free region below the first zeta ordinate \(\gamma_1\approx14.134725\).

For independently reproducing \(\xi''(1)/\xi(1)\), put \(\gamma_{\!E}\) for Euler's constant, \(\gamma_1\) for the first Stieltjes constant:
\[
\frac{\xi'(1)}{\xi(1)}
=1+\frac{\gamma_{\!E}}2-\log2-\frac12\log\pi,
\]
\[
\frac{\xi''(1)}{\xi(1)}
=\left(\frac{\xi'(1)}{\xi(1)}\right)^2
-1+\frac{\pi^2}{8}-2\gamma_1-\gamma_{\!E}^2.
\]
This avoids numerical cancellation at the removable \(\zeta(s)\) pole.

## 3. The global growth criterion, in one exact double integral

For \(x,y\in\mathbb R\), write
\[
C(x,y)=\int_0^\infty\Phi(v)\cos(xv)\cosh(yv)\,dv,
\]
\[
S(x,y)=\int_0^\infty\Phi(v)\sin(xv)\sinh(yv)\,dv.
\]
Then
\[
X(x+iy)=2(C-iS),\qquad
\partial_y|X(x+iy)|^2=8(CC_y+SS_y).
\]

Expanding the products, symmetrizing \(u\leftrightarrow v\), and applying the usual product-to-sum trigonometric/hyperbolic identities yields
\[
\boxed{
CC_y+SS_y
=\frac14\int_0^\infty\int_0^\infty\Phi(u)\Phi(v)
\left[
(u+v)\sinh(y(u+v))\cos(x(u-v))+
(u-v)\sinh(y(u-v))\cos(x(u+v))
\right]\,du\,dv.
}
\]
For \(y>0\), the two amplitudes \((u+v)\sinh(y(u+v))\) and \((u-v)\sinh(y(u-v))\) are **nonnegative**. But the cosines can have either sign. **This is the exact obstruction**: positivity of the kernel and of these amplitudes does not settle the oscillatory double integral for all \(x\). This general criterion, and the difficulty of individual blockwise positivity, are treated by Planat (Symmetry 2026, 18(8), 1283).

## 4. A direct rigorous lower bound for the growth form

Apply \(\cos z\ge1-z^2/2\) to each cosine of the double integral in §3. Since both amplitudes are nonnegative for \(y>0\), this gives
\[
\boxed{
CC_y+SS_y\ge
A(y)A'(y)-\frac{x^2}{2}
\left(A(y)A'''(y)-A'(y)A''(y)\right).
}
\]
The bracket is nonnegative because
\[
\frac{A'''(y)}{A'(y)}-\frac{A''(y)}{A(y)}
=\mathbb E_{v\Phi\sinh(yv)}[v^2]
-\mathbb E_{\Phi\cosh(yv)}[v^2]\ge0.
\]
The first normalized measure is an increasing tilt of the second by \(v\tanh(yv)\), so this difference is nonnegative. It is strictly positive for this nondegenerate kernel and \(y>0\).

For a **fixed \(y>0\)**, we obtain strict growth whenever
\[
|x|<
\sqrt{\frac{2 A(y)A'(y)}
{A(y)A'''(y)-A'(y)A''(y)}}.
\]
The point of the next step is a clean **uniform** bound over \(0<y\le1/2\).

## 5. Uniform theta-only strict growth in a critical-strip subregion

For \(0<y\le1/2\), use the elementary inequalities
\[
\sinh(yv)\ge yv,\quad
\sinh(yv)\le yv\cosh(yv).
\]
It follows that
\[
A'(y)\ge y A''(0),\qquad
A'''(y)\le y A^{(4)}(1/2).
\]
Moreover, by the monotonicity of the normalized second moment from §2,
\[
\frac{A''(y)}{A(y)}\ge\frac{A''(0)}{A(0)}.
\]
Consequently,
\[
\frac{A'''(y)}{A'(y)}-\frac{A''(y)}{A(y)}
\le \frac{A^{(4)}(1/2)}{A''(0)}
-\frac{A''(0)}{A(0)}
=:\Delta_*.
\]
For the actual Riemann theta kernel, \(\Delta_*>0\). Define
\[
\boxed{
x_{\rm growth}:=\sqrt{\frac{2}{\Delta_*}}
=4.82113461383647972\ldots.
}
\]
Then the lower bound from §4 is strictly positive, proving
\[
\boxed{
\partial_y|X(x+iy)|^2>0,\quad
|x|<x_{\rm growth},\quad 0<y\le1/2.
}
\]
This is a **kernel-only, unconditional** strict-growth theorem in a proper subset of the critical strip. Nothing about zero locations was assumed.

Useful values, evaluated independently either via Stieltjes-constant series at \(s=1\) or theta moments:
\[
A(0)=0.24856038909415705495639,
\quad A''(0)=0.01148597215757271876762,
\]
\[
A^{(4)}(1/2)=0.00151909038189916203034,
\quad\Delta_*\approx0.08604615726831\ldots.
\]
The decimal thresholds shown are ordinary high-precision approximations, **not machine-checked outward-rounded interval certificates**. The theorem is the exact symbolic inequality.

**Outside the critical strip:** for \(y>1/2\), the completed zeta function has no zeros; the known symmetric Hadamard product with all roots in \(|\Im z|<1/2\) also yields strict outward growth, since the derivative of the logarithm of each paired root-distance factor is positive. That outside-strip fact uses the standard zero strip rather than this theta-only estimate.

## 6. Why this still does not prove the scale-free exhaustion identity

We have not shown the growth inequality for every real \(x\) in \(0<y\le1/2\). Precisely there, arbitrary large \(x\) causes the cosine oscillations in §3. The inequality \(\cos z\ge1-z^2/2\) becomes useless for large \(|x|\).

The prior negative controls in [10](10-jacobi-theta-jensen-tail.md) show positive/even kernels can have off-real zeros; a new property unique to the Jacobi arithmetic kernel is necessary.

The result here is a limited **domain certificate**. It must not be extrapolated to all \(x\), all zero heights, or \(\mathcal E=0\). Since the theta-kernel growth criterion is already equivalent to RH (Hinkkanen–Lagarias and Planat), proving its global form is precisely the original unsolved problem, not a separate easier theorem.

## 7. Relevant current research: finite-order versus infinite-order positivity

Suvrit Sra, *On some positivity properties of the Riemann Xi function*, **version v3, released 2 November 2026**, establishes substantial **finite-order** Pólya-frequency positivity for transform-related densities using finite-height RH verification. Its page reports order \(1,810,540,931,075\), but not an infinite-order theorem, and hence not RH. These results concern different functions/densities than the simple cosine-kernel moment estimate above. Do not conflate them.

- https://suvrit.github.io/papers/riem-xi/ (v3, 2 Nov 2026).
- Michel Planat, *A Theta-Kernel Reformulation of Riemann-Xi Growth and the Obstruction to Blockwise Positivity*, *Symmetry* **18**(8), 1283 (2026): https://doi.org/10.3390/sym18081283
- Csordas, *The Laguerre inequalities and the zeros of the Riemann ξ-function* (2010/2011): https://doi.org/10.1080/17476930903394820
- [Previously proved symbolic-L exhaustion equivalence](12-symbolic-scale-and-defect.md).

## 8. Precise next proof obligation

Find an independently justified arithmetic inequality—derived from the **special modular and prime-related structure** of \(\Phi\), not merely \(\Phi>0\)—that controls the *signed*, oscillatory \(\cos(x(u\pm v))\) contributions for all real \(x\) with \(0<y\le1/2\).

Such a global estimate would establish the known growth criterion and therefore RH. No such estimate is established in this note.

The conjectured angular/perfect-closure viewpoint is compatible with this analysis, but the stereographic parameter \(L\) is not used in the kernel inequality and remains fully symbolic as required.
