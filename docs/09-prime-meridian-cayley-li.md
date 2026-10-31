# 09 — Prime Meridian: a Cayley–Li constraint beyond conjugate symmetry

**Date:** 2026-10-30. **Status:** research formulation, elementary deductions, and numerical controls; not an RH proof. “Prime Meridian” is the user's working name for this research track, not a claim of a new established theorem. Li's criterion, the theta transform, and earlier theta–Li research are credited below.

## Executive result

The global quaternionic map already in this repository is directly related to **Li's positivity criterion**, an established theorem equivalent to RH. This gives a genuine all-orders constraint stronger than ordinary conjugate symmetry. The constraint can be computed from the fixed Jacobi-theta kernel without supplying zero locations.

This investigation derives the first two positivity conditions from kernel positivity, computes the first twelve from kernel integrals at two precisions, and constructs a positive symmetric kernel that passes the first eight but fails the ninth. Thus finite success and symmetry are demonstrably insufficient. The missing step is an all-orders inequality specific to the actual Jacobi arithmetic kernel.

No coordinate is physical time, mass, or energy. No zero sphere is normalized individually.

## 1. One global polar chart with a useful fixed scale

Our earlier map, with one fixed scale L, was

\[
q_L(s)=\frac{L+(s-1/2)}{L-(s-1/2)}.
\]

Choosing **L=1/2 once for the entire space** gives

\[
q(s)=\frac{s}{1-s}.
\]

This choice aligns the chart with the distinguished points s=0 and s=1. It does not prove that nature or the kernel selects a physical scale. The old L=20 illustration remains valid; its numerical latitude coordinates simply differ globally.

On a fixed complex slice, at s=1/2+it,

\[
q=\cos\theta+i\sin\theta,
\qquad \theta=2\arctan(2t)\pmod{2\pi}.
\]

Replacing i by a unit imaginary quaternion u, u²=-1, gives

\[
q=\cos\theta+\mathbf u\sin\theta,
\qquad w=\cos\theta,
\qquad w^2+x^2+y^2+z^2=1.
\]

Here w is the ambient fourth coordinate and sqrt(1-w²) is the radius of its three-imaginary-coordinate slice. All four coordinates are mathematical, not spacetime coordinates.

Introduce a separate complex chart variable

\[
\boxed{\eta(s)=1-\frac1s=-q(s)^{-1}.}
\]

This is NOT an individual normalization. It is a single Möbius transformation of the whole complex plane. Directly,

\[
|\eta(s)|^2=\frac{(\sigma-1)^2+t^2}{\sigma^2+t^2},
\qquad |\eta(s)|=1\iff\sigma=1/2.
\]

On the critical line its polar angle is

\[
\eta=e^{i\varphi},\qquad \varphi=\pi-\theta
\]

for the positive-height branch. Infinity remains a common limiting point: q approaches -1 while eta approaches +1. There is no need to treat infinity as an additional zeta zero.

## 2. The established all-harmonics theorem

Li's coefficients are defined WITHOUT knowledge of zeros by

\[
\boxed{\lambda_n=\frac1{(n-1)!}
\left.\frac{d^n}{ds^n}\left[s^{n-1}\log\xi(s)\right]\right|_{s=1},
\quad n\ge1.}
\]

The branch of log xi is chosen locally near s=1, where xi(1)=1/2 is nonzero. Li's theorem says

\[
\boxed{\mathrm{RH}\iff\lambda_n\ge0\text{ for every }n\ge1.}
\]

Equivalently, with the usual symmetric ordering and multiplicities,

\[
\lambda_n=\sum_\rho\left[1-\left(1-\frac1\rho\right)^n\right].
\]

This zero sum is used here to INTERPRET the geometry, not to calculate the coefficients. The numerical experiment uses theta integrals and a separate derivative check at s=1.

If a conjugate zero pair lies on the critical line, its two eta images are exp(±i phi). Its contribution is

\[
2[1-\cos(n\varphi)]=4\sin^2(n\varphi/2)\ge0.
\]

Thus, **conditional on RH**,

\[
\lambda_n=4\sum_{\gamma>0}\sin^2\!\left(\frac n2[\pi-\theta_\gamma]\right).
\]

The conditional label is essential: using this formula to prove positivity while assuming every zero already lies on the meridian would be circular.

In latitude notation, cos(n theta)=T_n(w), the degree-n Chebyshev polynomial. The same conditional expression is

\[
\lambda_n=2\sum_{\gamma>0}[1-(-1)^n T_n(w_\gamma)].
\]

This links the user's polar geometry to all angular harmonics, not just the first visible conjugation symmetry.

For an off-line quartet, the eta images have radii r and 1/r. Their combined contribution can be written

\[
4-2(r^n+r^{-n})\cos(n\varphi).
\]

Unlike the unit-radius expression, it can become negative. Bombieri–Lagarias prove the required global implication, including domination and convergence; a single quartet calculation alone is not the full theorem.

## 3. Derive the coefficients from the fixed theta kernel

Use exactly the repository's convention

\[
\Phi(v)=\sum_{m\ge1}(4\pi^2m^4e^{9v/2}-6\pi m^2e^{5v/2})
 e^{-\pi m^2e^{2v}},\quad v\ge0,
\]

extended evenly to real v. The classical transform gives

\[
\xi(s)=\int_{\mathbb R}\Phi(v)e^{(s-1/2)v}\,dv,
\qquad \Xi(t)=\int_{\mathbb R}\Phi(v)e^{itv}\,dv.
\]

Its double-exponential decay permits differentiation under the integral for every finite order.

Define the tilted probability density

\[
\boxed{p_1(v)=\frac{e^{v/2}\Phi(v)}{\xi(1)}=2e^{v/2}\Phi(v).}
\]

This normalizes the **integration weight**, not any zero sphere. Its integral is 1. If V has this density, then

\[
\mathbb E[e^{hV}]=\frac{\xi(1+h)}{\xi(1)}.
\]

Define cumulants by their generating equation

\[
\log\mathbb E[e^{hV}]=\sum_{j\ge1}\kappa_j\frac{h^j}{j!}
\]

near h=0. A cumulant is a coefficient of the logarithm of the moment-generating function: kappa_1 is the mean, kappa_2 the variance, kappa_3 the third central moment, and higher orders subtract lower-order combinations from moments.

Leibniz differentiation now gives the exact relation

\[
\boxed{\lambda_n=\sum_{j=1}^n\binom nj\frac{\kappa_j}{(j-1)!}.}
\]

Every term is defined by the actual kernel. No zero ordinate is an input.

## 4. What can be proved immediately, rather than just sampled

Evenness and positivity give

\[
\kappa_1=\mathbb E[V]
=\frac{2}{\xi(1)}\int_0^\infty v\Phi(v)\sinh(v/2)\,dv>0.
\]

Also kappa_2=Var(V)>0 because this is not a point mass. Therefore

\[
\boxed{\lambda_1=\kappa_1>0,
\qquad \lambda_2=2\kappa_1+\kappa_2>0.}
\]

These are elementary consequences, not claimed as novel discoveries. They are valid for a much wider class of even positive kernels and therefore do not distinguish the exact Jacobi kernel enough to prove RH.

Already at order three,

\[
\lambda_3=3\kappa_1+3\kappa_2+\tfrac12\kappa_3.
\]

The actual theta kernel has negative kappa_3 and kappa_4 in this computation. Thus the shortcut 'every cumulant is positive' is false even for the real kernel. The required weighted combination can remain positive despite negative components.

## 5. Reproducible numerical investigation

The new experiment folds the integral to v>=0. For raw tilted moments m_j,

\[
m_j=\frac2{\xi(1)}\int_0^\infty v^j\Phi(v)
\begin{cases}\cosh(v/2),&j\text{ even},\\\sinh(v/2),&j\text{ odd}\end{cases}dv.
\]

Cumulants are computed recursively:

\[
\kappa_n=m_n-\sum_{j=1}^{n-1}\binom{n-1}{j-1}\kappa_jm_{n-j}.
\]

Two runs used (50 digits, 8 theta terms, cutoff 2.5) and (65 digits, 10 terms, cutoff 3). A separate logarithmic-derivative calculation of xi at s=1 checks the result. There are no zero lists in either calculation.

| n | Theta-derived lambda_n | Altered positive-kernel control |
|---:|---:|---:|
| 1 | 0.0230957089661210 | 5.00394863519903 |
| 2 | 0.0923457352280467 | 15.2787970262975 |
| 3 | 0.207638920554325 | 19.6595229749905 |
| 4 | 0.368790479492242 | 15.4812178893436 |
| 5 | 0.575542714461177 | 22.3365728280712 |
| 6 | 0.827566012282379 | 54.3783005582673 |
| 7 | 1.12446011757096 | 72.4454496549170 |
| 8 | 1.46575567714706 | 26.2570558161606 |
| 9 | 1.85091604838253 | **-17.8604752176347** |
| 10 | 2.27933936319316 | 81.5433046902955 |
| 11 | 2.75036083822020 | 235.897985326342 |
| 12 | 3.26325532062462 | 93.2550876111465 |

Maximum change between runs: 3.4514654e-51. The second run and derivative reference agreed at the working precision. These are finite-precision agreement checks, **not interval-certified bounds or an infinite-order proof**.

Nine new focused regression tests were actually run and passed. Earlier repository test suites were not rerun and are not included in this count.

## 6. Exact negative control: symmetry, positivity, rapid decay, yet off-line zeros

Define a different kernel

\[
K(v)=\Phi(v-6)+\Phi(v+6)+4\Phi(v).
\]

It remains positive, even, smooth, and double-exponentially decaying at infinity. It is deliberately **not the exact Jacobi theta kernel**; no preservation of its detailed arithmetic structure, monotonicity, or log-concavity is asserted.

Its transform is exactly

\[
\Xi_K(z)=[4+2\cos(6z)]\Xi(z).
\]

The multiplier vanishes at

\[
z=\frac{(2k+1)\pi}{6}\ \pm\ i\frac{\operatorname{arcosh}2}{6}.
\]

The first added quartet in s-coordinates includes

\[
s=0.2805070171791972\ \pm\ 0.5235987755982989 i
\]

and its reflection at real part 0.7194929828208028. These are inside the critical strip and off the critical line. This assertion follows algebraically, independently of numerical root finding.

For one of these points, |eta|≈1.49804896566 and |q|≈0.66753492237, so it is genuinely off the common-radius meridian. The corresponding coefficient test passes n=1,...,8 but fails at n=9 as shown above.

This control preserves entire order one (multiplication by an exponential-type factor) and the reflection/conjugation symmetries. It demonstrates why finite positivity and a positive symmetric kernel cannot finish the proof. The original theta kernel is not refuted by altering it.

## 7. A precise remaining coefficient inequality

Let z be a generating-series variable, distinct from the hypersphere's Cartesian component z. Define locally around z=0

\[
G(z)=\frac{\xi(1/(1-z))}{\xi(1)}
=\mathbb E\!\left[\exp\left(\frac{zV}{1-z}\right)\right]
=\sum_{n\ge0}g_nz^n.
\]

Then g_0=1 and

\[
g_n=\sum_{j=1}^n\binom{n-1}{j-1}\frac{m_j}{j!}>0.
\]

The strict positivity of all m_j follows from the same cosh/sinh folding. Nevertheless positive coefficients of G do NOT imply positive coefficients of log G.

Locally,

\[
\log G(z)=\sum_{n\ge1}\frac{\lambda_n}{n}z^n.
\]

Its convergence must not be asserted throughout the unit disk without proving the requisite zero exclusion. Comparing G'=G(log G)' gives

\[
\boxed{\lambda_n=n g_n-\sum_{j=1}^{n-1}\lambda_jg_{n-j}.}
\]

A concrete sufficient-and-necessary target, once the previous coefficients are fixed, is

\[
\boxed{n g_n\ \ge\ \sum_{j=1}^{n-1}\lambda_j g_{n-j}
\quad\text{for every }n\ge1.}
\]

The target is stated from the fixed theta-integral moments, not from a list of presumed on-line zeros. Proving it uniformly is equivalent to completing this Li route to RH. It has NOT been established here for all n. The recurrence was separately checked against the cumulant formula through order 12.

## Equation dictionary

| Symbol | Meaning |
|---|---|
| s=σ+it | Complex zeta argument; t is spectral height, not time |
| xi(s), Xi(t) | Completed zeta and its critical-line-centered form |
| Phi(v) | Fixed even positive Jacobi-theta Fourier kernel |
| v | Real integration coordinate; no physical interpretation required |
| L | One global stereographic scale, chosen as 1/2 for the Li chart |
| q | Global Cayley image, unit quaternion on the critical line |
| theta | Polar angle of q on a fixed quaternionic meridian |
| w=cos(theta) | Fourth-coordinate latitude in the unit S3 |
| eta=-1/q | Li's complex unit-circle coordinate on the critical line |
| phi=pi-theta | Angle of eta for the positive-height branch |
| rho | A nontrivial zero, not assumed on the line in unconditional formulas |
| n | Positive integer harmonic/coefficient order, not a zero index |
| p_1, V | Exponentially tilted theta density and its integration variable viewed probabilistically |
| m_j | Raw moment E[V^j] |
| kappa_j | Cumulant, defined by log E[exp(hV)] |
| lambda_n | Li coefficient, with all-orders nonnegativity equivalent to RH |
| g_n | Coefficient of G; positivity alone is weaker than Li positivity |
| K | Altered negative-control kernel, not the actual Jacobi kernel |

## Scope and attribution

This is a connection of the project's polar interpretation to established Li/Keiper mathematics, with new repository calculations and an explicit control. No priority claim is made for the cumulant identity, which follows by elementary generating-function algebra. Theta-based Li representations have substantial prior literature. The first twelve coefficients are known quantities, not newly discovered numbers.

The next proof obligation is kernel-specific all-orders control of the signed cumulant combination or the equivalent recurrence. A proof cannot use the unit-circle zero sum while assuming its desired conclusion. Neither a constant quaternion norm nor an infinity-pole continuation supplies this missing inequality.

## Primary sources

1. X.-J. Li, The Positivity of a Sequence of Numbers and the Riemann Hypothesis (1997), Journal of Number Theory 65, 325–333. https://doi.org/10.1006/jnth.1997.2137
2. E. Bombieri and J. C. Lagarias, Complements to Li's Criterion for the Riemann Hypothesis (1999). https://websites.umich.edu/~lagarias/doc/bombieri.pdf
3. D. Romik, Orthogonal polynomial expansions for the Riemann xi function, equations (1.6)–(1.11). https://math.ucdavis.edu/~romik/data/uploads/papers/riemannxi.pdf
4. M. W. Coffey, The theta-Laguerre calculus formulation of the Li/Keiper constants (2007). https://doi.org/10.1016/j.jat.2006.10.006
5. G. Csordas, Fourier transforms of positive definite kernels and the Riemann xi-function. https://arxiv.org/abs/1309.0055

## Reproduce

```bash
python -m pip install mpmath
python experiments/prime_meridian.py --output results/prime_meridian.json
python -m unittest discover -s tests -p 'test_prime_meridian.py' -v
```

Artifacts: experiment, JSON output, focused tests, and recorded test log in this branch. Main remains unchanged pending review.
