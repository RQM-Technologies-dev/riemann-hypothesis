# 08 — One Jacobi-theta harmonic equation for every zero latitude on the unit S³

**2026-10-30.** Exact reformulation of Riemann's completed-zeta Fourier-cosine transform in a single global quaternionic polar coordinate. This does not prove the Riemann Hypothesis or independently derive a new zeta function.

## 1. User's geometric target

The ambient four-real-dimensional unit hypersphere is
\[
w^2+x^2+y^2+z^2=1.
\]
Choose a unit pure-imaginary quaternion \(\mathbf u^2=-1\) and write
\[
q=\cos\theta+\mathbf u\sin\theta,\quad
w=\cos\theta,\quad
r_{xyz}=\sqrt{x^2+y^2+z^2}=\sin\theta
\quad(0<\theta<\pi).
\]

**Do not normalize each zero sphere separately.** Instead choose one fixed scale \(L>0\) for the entire critical line:
\[
t=L\tan(\theta/2)=L\sqrt{\frac{1-w}{1+w}},
\quad w=\frac{L^2-t^2}{L^2+t^2}.
\]
Here \(t\) is the imaginary *spectral height* of \(s=1/2+it\), not time. Every \(w\in(-1,1)\) is a latitude on the same \(S^3\), at ambient radius 1. The 2-sphere *within* a latitude has radius \(\sqrt{1-w^2}\), which varies with \(w\).

## 2. A zero-free-input harmonic kernel

Start from the Jacobi theta series:
\[
\Theta(a)=\sum_{m\in\mathbb Z}e^{-\pi m^2a}
=1+2\sum_{m\ge1}e^{-\pi m^2a},\quad a>0.
\]
Its ordinary real derivatives define
\[
\omega(a)=a^2\Theta''(a)+\frac32 a\Theta'(a).
\]
Define the fixed, positive, even theta kernel:
\[
\Phi(v)=2e^{v/2}\omega(e^{2v})
=\sum_{m=1}^\infty
\left(4\pi^2m^4e^{9v/2}-6\pi m^2e^{5v/2}\right)
e^{-\pi m^2e^{2v}}.
\]

The conventional completed zeta function
\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]
has the exact Fourier-cosine representation
\[
\boxed{
\Xi(t):=\xi(1/2+it)=2\int_0^\infty\Phi(v)\cos(tv)\,dv.
}
\]

The kernel is obtained from integer harmonic/theta data, not by supplying a list of zeros. \(\Phi(v)>0\) for \(v\ge0\) and is even in \(v\), by Jacobi theta modular symmetry. This is classical mathematical analysis (Riemann, Jacobi, Pólya, and many later authors).

## 3. The **one harmonic equation** for all zero latitudes

Substitute the ONE global inverse-stereographic relation \(t=t(w)\) into the known Fourier integral:
\[
\boxed{
\mathcal C_L(w)
=
2\int_0^\infty
\Phi(v)
\cos\!\left(
Lv\sqrt{\frac{1-w}{1+w}}
\right)\,dv
=0,\quad -1<w<1.
}
\]

For every solution \(w_n\in(-1,1)\), the associated hypersphere latitude is
\[
\mathcal S_{w_n}=
\{(w_n,x,y,z):x^2+y^2+z^2=1-w_n^2\},
\]
and the corresponding positive critical-line zero ordinate is
\[
\gamma_n=L\sqrt{\frac{1-w_n}{1+w_n}}.
\]
There is no per-zero scale or radius.

**Exact status:** this equation is \(\Xi(t(w))=0\). It *locates the critical-line zeros*, but it is NOT a theorem that *all* nontrivial zeta zeros lie on the critical line. Such an exclusion of off-axis zeros would be RH.

## 4. The quaternionic balanced-conjugate form

Since
\[
\Xi(0)=2\int_0^\infty\Phi(v)\,dv\approx0.4971207781883141099>0,
\]
define a probability weight on \(v\ge0\):
\[
p(v)=\frac{2\Phi(v)}{\Xi(0)},\qquad \int_0^\infty p(v)\,dv=1.
\]
For each pure quaternion unit \(\mathbf u\), use
\[
\frac{e^{\mathbf u\varphi}+e^{-\mathbf u\varphi}}2=\cos\varphi.
\]
The *same* zero equation becomes
\[
\boxed{
\int_0^\infty p(v)
\frac{
e^{\mathbf u v L\sqrt{(1-w)/(1+w)}}
+
e^{-\mathbf u v L\sqrt{(1-w)/(1+w)}}
}{2}\,dv=0.
}
\]
In elementary words, \(\mathbb E_{V\sim p}[\cos(V\,t(w))]=0\): zero latitude means the positively weighted, **paired conjugate harmonic phases have zero average**. The quaternionic axis cancels from this real scalar, so every imaginary direction carries the same balance condition.

This is the precise mathematical contact with the hypothesis of balanced spinorial return. It is an identity in quaternion algebra, **not** a new fermion/Dirac law.

## 5. Numerical experiment: root discovery WITHOUT known zero input

One reproducible routine:

1. Build a single float quadrature of the theta kernel (240 Gauss-Legendre nodes, \(v\in[0,3]\)) to find candidate sign changes of \(\mathcal C_L\) in a fixed scan of spectral height \(t\).
2. Refine each root with a 50-decimal-digit \(mpmath\) integral using \(\Phi(v)\), no known zero values supplied to the root solver.
3. Only *after root discovery*, compare the resulting \(t\)'s to \(\Im(\mathrm{zetazero}(n))\).
4. Convert each to \(w\) using \(L=20\), fixed for all eight.

| Index | Root height \(t_n\) | Allowed \(w_n\) |
|---:|---:|---:|
| 1 | 14.134725141734694 | +0.333799151944761 |
| 2 | 21.022039638771555 | -0.049797895629557 |
| 3 | 25.010857580145689 | -0.219925442012033 |
| 4 | 30.424876125859513 | -0.396532970549237 |
| 5 | 32.935061587739190 | -0.461177241626949 |
| 6 | 37.586178158825671 | -0.558674449459147 |
| 7 | 40.918719012147495 | -0.614335453105333 |
| 8 | 43.327073280915000 | -0.648696817871290 |

The refined roots agree to about 48–50 decimal places with the known critical-line ordinates. This validates the classical cosine-integral identity numerically; it is **not independent evidence for RH**.

## 6. The infinity pole and conjugate return

Under the global mapping,
\[
w(t)=\frac{L^2-t^2}{L^2+t^2}\to-1
\quad (t\to\pm\infty).
\]
The polar angular branches are \(\theta(t)\in(0,\pi)\) for \(t>0\) and \(\theta(-t)=2\pi-\theta(t)\) for the negative conjugates. Since \(\cos(vt)\) is even in \(t\), the full harmonic equation has the exact return symmetry. On the full quaternionic \(S^3\), the + and - branches trace the same **unoriented** latitude 2-spheres; they differ by orientation along a fixed meridian.

**Important pole exclusion:** \(\Xi(t)\to0\) as \(|t|\to\infty\), so setting \(\mathcal C_L(-1)=0\) by continuity would create an *extra limiting zero at infinity*. It is **not** a nontrivial zero of \(\zeta(s)\). Thus the root equation must use \(-1<w<1\) and keep the infinity pole as a limiting point, not a finite eigenvalue.

Close to the pole,
\[
1+w(t)=\frac{2L^2}{L^2+t^2}\sim\frac{2L^2}{t^2},
\]
so the allowed latitudes increasingly crowd around \(w=-1\). The 3D slice radii shrink, while the shared four-dimensional radius stays exactly 1.

## 7. Boundaries, next theorem, and connection to earlier work

- **What was established:** one fixed positive arithmetic theta kernel, a single exact cosine integral selecting the **known critical-line** root heights, a unit-\(S^3\) coordinate embedding, and quaternionic conjugate phase averaging.
- **What remains conjectural:** that every nontrivial zeta zero is represented by a real \(w\in(-1,1)\); a self-adjoint or positivity-based proof would have to exclude all off-critical zeros without assuming the conclusion.
- **Not a new physical theory:** all coordinates and phases here are mathematical, not physical time, energy, mass, or electron spin.
- **No separate gamma/prime identity:** the kernel is derived from the Jacobi theta sum over integers; the Euler product over primes is a separate equality for \(\Re s>1\).
- **Independent research objective:** find an additional structure on the **fixed** theta kernel (e.g. a provable total-positivity or spectral operator criterion) enforcing real zeros of its Fourier transform. Mere positivity and evenness of \(\Phi\) are not sufficient.

## References

- Dan Romik, *Orthogonal polynomial expansions for the Riemann xi function*, Chapter 1 equations (1.6)–(1.11): https://math.ucdavis.edu/~romik/data/uploads/papers/riemannxi.pdf
- Encyclopedia of Mathematics, Riemann xi function: https://encyclopediaofmath.org/wiki/Riemann_xi-function
- Prior RQM polar geometry: [01](01-polar-quaternionic-geometry.md)
- Prior RQM conjugate balancing: [07](07-riemann-siegel-conjugate-balance.md)


## 8. Follow-on result (2026-11-02): positive \(w\)-distance exhaustion criterion

The theta-kernel root equation identifies the positive **critical-line** heights. The follow-on question is whether *those* roots exhaust every nontrivial zeta zero.

For the same fixed \(L>1/2\) and the w-coordinate already used above, define
\[
d_w(\gamma)=1+w(\gamma)=\frac{2L^2}{L^2+\gamma^2}
\]
for every positive critical-line zero height (counting multiplicity).

Classical Hadamard factorization yields the exact criterion
\[
\boxed{\mathrm{RH}\ \Longleftrightarrow\
\sum_{\zeta(1/2+i\gamma)=0,\ \gamma>0}d_w(\gamma)
=L\frac{\xi'(1/2+L)}{\xi(1/2+L)}.}
\]
At \(L=20\), the right side is \(13.330990477997002487\ldots\).

The difference between this total and the **infinite sum** of on-line distances is a sum of *strictly positive contributions* from all off-line zeros. This supplies a precise, falsifiable **RH-equivalent** question, not the missing proof that the difference is zero.

The residual after *finitely many* on-line roots is not evidence of an off-line zero: it includes every uncounted on-line zero. See [09 — full derivation, variable glossary, and 200-zero numerical study](09-w-distance-rh-equivalence.md).
