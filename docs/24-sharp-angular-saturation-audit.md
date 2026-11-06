# 24 — Auditing the sharp S³ folding bound: what theta can and cannot prove

**Date:** 2026-11-06  
**Status:** Exact theorem and explicit theta-kernel stress test. **No proof of the Riemann hypothesis (RH)**, and no unconditional saturation theorem for the original Riemann theta kernel.  
**Question:** Can the exact Jacobi-theta kernel be proved to saturate the sharp quaternionic four-dimensional angular Jensen bound, thereby forcing all reflected \(S^2\) zero-spheres to merge on the critical fold?

Continues [21 — Quaternionic theta continuation](21-quaternionic-theta-superposed-zero-spheres.md), [22 — S³ Jensen harmonics](22-quaternionic-s3-jensen-second-harmonic.md), [23 — Positive per-quartet penalty](23-positive-quaternionic-folding-penalty.md). Original Clay goal: [17](17-clay-statement-and-proof-roadmap.md).

## 1. Exact definitions — no zeros inserted

Let \(f(z)=\xi(\tfrac12+z)\) and its intrinsic slice-regular lift be

\[
\mathcal X(q)=2\int_0^\infty\Phi(v)\cosh(qv)\,dv,\quad q\in\mathbb H.
\]

For \(R>0\), define the radial means of the **original**, unmodified \(f\):

\[
M_2(R)=\frac1{2\pi}\int_0^{2\pi}
\log|f(Re^{i\theta})|d\theta,\quad
M_4(R)=\frac1{2\pi}\int_0^{2\pi}
(1-\cos2\theta)\log|f(Re^{i\theta})|d\theta.
\tag{S1}
\]

The second expression is exactly the rotation-invariant \(S^3_R\) mean of \(\log|\mathcal X|\), since the quaternionic polar angular measure is \((2/\pi)\sin^2\theta\,d\theta\). Both are obtainable *in principle* from the theta integral, without supplying a zero table. This does **not** make a proposed equality between them automatic.

Write \(K_2(R)=M_2(R)-M_4(R)\) for the second angular cosine harmonic.

## 2. Sharp radial-only bound and its equality case

Use the even, real, order-one canonical product
\[
f(z)=f(0)\prod_{\alpha\in\mathcal P}(1-z^2/\alpha^2),
\tag{S2}
\]
where \(\mathcal P\) takes one member of each \(\pm\) zero pair with multiplicity, and \(\sum_{\alpha\in\mathcal P}|\alpha|^{-2}<\infty\). The two representatives of an off-axis quartet must both be included. Put \(r_\alpha=|\alpha|\).

For a radius \(R\) not meeting a zero modulus (and by continuous extension at a meeting radius), the second harmonic is
\[
K_2(R)=
-\frac{R^2}{2}\sum_{r_\alpha>R}\Re(\alpha^{-2})
-\frac1{2R^2}\sum_{r_\alpha<R}\Re(\alpha^2).
\tag{S3}
\]
Because \(-\Re(\alpha^{\pm2})\le r_\alpha^{\pm2}\), define the **radial-data-only sharp envelope**
\[
\boxed{
B(R)=\frac{R^2}{2}\sum_{r_\alpha>R}\frac1{r_\alpha^2}
+\frac1{2R^2}\sum_{r_\alpha<R}r_\alpha^2.
}
\tag{S4}
\]
Then
\[
\boxed{M_4(R)\ge M_2(R)-B(R).}
\tag{S5}
\]
The equality case is **all** nonzero zero locations \(\alpha\) purely imaginary; no cancellation between the nonnegative per-pair gaps is possible.

Critically, \(B(R)\) does **not** require knowing the angular positions of zeros. Ordinary Jensen gives
\[
M_2(R)=\log f(0)+2\sum_{r_\alpha<R}\log(R/r_\alpha)
\]
and hence the radial count \(N(R)=(R/2)M_2'(R)\) away from root radii, interpreted as a measure at the jumps. Equivalently,
\[
B(R)=\frac{R^2}{2}\int_{(R,\infty)}r^{-2}dN(r)
+\frac1{2R^2}\int_{(0,R)}r^2dN(r).
\tag{S6}
\]
Thus \(B\) is reconstructible from \(M_2\), which itself can be calculated from \(f\). **This is a sharp variational inequality, but its saturation is exactly an RH-equivalent property, not a theorem following from general theta positivity.**

For a single off-axis quartet at \(\alpha=a+it\), \(r^2=a^2+t^2\), the difference from the sharp bound is the penalty derived in [23]:
\[
M_4(R)-(M_2(R)-B(R))
=\begin{cases}
2a^2R^2/r^4,&R\le r,\\
2a^2/R^2,&R\ge r.
\end{cases}
\tag{S7}
\]
Summing over quartets with multiplicity produces a nonnegative gap. It equals zero for any \(R>0\) if and only if there is **no off-axis quartet**, i.e. RH. (At exactly a zero modulus, take the continuous extension.)

## 3. The proposed theta-only saturation equality

Define the inverse-square radial Jensen functional
\[
I[f]=\int_0^\infty\frac{M_2(R)-\log f(0)}{R^3}\,dR.
\tag{S8}
\]

The disk around \(0\) up to the first nontrivial xi zero is zero-free; therefore the integrand vanishes there. The entire order-one product and standard zero-count estimates justify the integral's convergence at infinity. For each \(\pm\) pair,
\[
\int_{r_\alpha}^\infty
\frac{2\log(R/r_\alpha)}{R^3}dR
=\frac1{2r_\alpha^2}.
\]
Tonelli applies because the Jensen summands are nonnegative. Hence
\[
\boxed{I[f]=\frac12\sum_{\alpha\in\mathcal P}|\alpha|^{-2}.}
\tag{S9}
\]

Independent of the zeros, differentiate the theta representation:
\[
\frac{f''(0)}{4f(0)}
=\frac14\frac{\int_0^\infty v^2\Phi(v)dv}
{\int_0^\infty\Phi(v)dv}.
\tag{S10}
\]
Also from (S2),
\[
\frac{f''(0)}{4f(0)}
=-\frac12\sum_{\alpha\in\mathcal P}\Re(\alpha^{-2}).
\tag{S11}
\]

Subtract (S11) from (S9):
\[
\boxed{
\begin{aligned}
\mathcal D_0
&=I[f]-\frac{f''(0)}{4f(0)}\\
&=\frac12\sum_{\alpha\in\mathcal P}
\left(\frac1{|\alpha|^2}+\Re\frac1{\alpha^2}\right)\\
&=\sum_{\alpha\in\mathcal P}
\frac{(\Re\alpha)^2}{|\alpha|^4}
=2\sum_{\text{off-axis quartets}}
\frac{a^2}{(a^2+t^2)^2}\ge0.
\end{aligned}}
\tag{S12}
\]

The middle equality uses
\(1/|\alpha|^2+\Re(\alpha^{-2})=2(\Re\alpha)^2/|\alpha|^4\).

**Exact theorem:**
\[
\boxed{\mathcal D_0=0\iff \mathrm{RH}.}
\tag{S13}
\]

This theorem is an **RH-equivalent positive criterion**. It is *not* a derivation that the left side is zero.

### Why the sharp angular bound does not independently saturate

For any zero-free radius \(R\) below the first xi zero, \(M_2(R)=\log f(0)\) and \(B(R)=R^2 I[f]\). Independently, the exact S³ mean is
\[
M_4(R)=\log f(0)-R^2\frac{f''(0)}{4f(0)}.
\]
Their sharp inequality becomes precisely
\[
\boxed{M_4(R)-(M_2(R)-B(R))=R^2\mathcal D_0\ge0.}
\tag{S14}
\]
So **claiming that the bound is saturated already assumes the very global inverse-square zero-distribution identity one wants to prove**. Passing from complex Jensen to quaternionic Jensen has made the obstacle visible, not removed it.

A direct zero-free-input formulation is
\[
\boxed{
\begin{aligned}
\int_0^\infty\frac{dR}{R^3}
\left[\frac1{2\pi}\int_0^{2\pi}
\log\left|2\int_0^\infty\Phi(v)\cosh(Re^{i\theta}v)\,dv\right|d\theta
-\log\left(2\int_0^\infty\Phi(v)dv\right)\right]\\
=\frac14
\frac{\int_0^\infty v^2\Phi(v)dv}{\int_0^\infty\Phi(v)dv}.
\end{aligned}}
\tag{S15: UNPROVED}
\]
Its equality is exactly (S13), hence RH. It is not justified by changing integration order or theta modular inversion alone. In particular, \(\log|\int \Phi\cosh|\) cannot be replaced by \(\int\Phi\log|\cosh|\).

For the actual xi kernel, the independent right-hand moment is approximately
\[
\frac{f''(0)}{4f(0)}=0.011552496557709485394466905215169507\ldots.
\]
**No unconditional exact evaluation of the full radial integral \(I[f]\) to this same value has been obtained.** Finite numerical agreement cannot imply equality over all radii.

## 4. An exact, quantitative negative control: positive even theta perturbation

Take the genuine positive even theta kernel \(\Phi\), but define a *different* positive even rapidly decaying kernel
\[
\Phi_\varepsilon(v)=\Phi(v)+\varepsilon[\Phi(v-1)+\Phi(v+1)],\quad
\varepsilon=0.49.
\]
This retains positivity and reflection in the logarithmic coordinate, though **not** the full original theta \(n^2\)-arithmetic structure.

Its Fourier transform is \(\Xi_\varepsilon(z)=\Xi(z)[1+0.98\cos z]\). Thus the centered hyperbolic form is
\[
f_\varepsilon(w)=f(w)[1+0.98\cosh w].
\]

The extra zeros are the off-axis quartets
\[
w=\pm b\pm i(2k+1)\pi,\qquad k=0,1,2,\ldots,
\quad b=\operatorname{arcosh}(1/0.98)
=0.201688487798836053\ldots.
\]

The extra folding deficit is **exactly**
\[
\boxed{
\begin{aligned}
\mathcal D_0[f_\varepsilon]-\mathcal D_0[f]
&=2b^2\sum_{k=0}^\infty
\frac1{(b^2+(2k+1)^2\pi^2)^2}\\
&=\frac{\tanh(b/2)}{4b}
-\frac{\operatorname{sech}^2(b/2)}8\\
&=0.000840611132743891910453500558192839\ldots>0.
\end{aligned}}
\tag{S16}
\]

The hyperbolic expression follows by differentiating
\(\sum_{k\ge0}[b^2+(2k+1)^2\pi^2]^{-1}=\tanh(b/2)/(4b)\).

**What this establishes:** Reflection, a positive even Fourier kernel, spherical means, the sharp variational inequality and a known theta-like starting kernel do **not**, by themselves, imply saturation. A valid proof must use a feature not preserved by this perturbation—something specific to the exact Jacobi theta series and its arithmetic coefficient structure.

The test is *not* a counterexample to RH: its additional off-axis zeros belong only to \(f_\varepsilon\), not to \(f\).

## 5. Concrete attempt at a noncircular theta-specific theorem — and stopping point

The following possible argument was tested and is **incomplete**:

1. From the original theta integral (Q2), calculate \(M_2(R)\), \(M_4(R)\) and the angular second harmonic exactly as observables. **Succeeded:** (S1), (S10), (S14).
2. Eliminate the unknown angular locations using the sharp radial envelope \(B(R)\). **Succeeded as an inequality:** (S4)–(S6), with a sharp equality criterion.
3. Infer that the actual kernel *attains* this bound from theta positivity, evenness or modular reflection. **Fails:** none of those ingredients determines the sign of \(\mathcal D_0\) beyond nonnegativity, and the explicit perturbation (S16) obeys analogous properties with strictly positive cost.
4. Look for a theta-specific exact identity evaluating the **global logarithmic angular integral** (S15) by the **local quadratic theta moment** (S10), without using the xi zero locations, an assumed real-zero property, or the desired saturation as a premise. **Still open.**

The central obstacle is **global control of the logarithm of an oscillatory transform**. Jensen detects zero locations; the small-radius theta moment does not, by itself, control their angular distribution.

A useful mathematically precise next lemma would be a theorem deriving from the *exact* theta \(n^2\)-series a new positive-definite/factorization/variational property that forces (S15). It must be (i) independently proved from modular/arithmetic data, (ii) valid for unbounded spectral height and all radii, and (iii) false for the shifted-kernel negative control. No such lemma is proved here.

## 6. Reproducibility and references

- [experiments/sharp_s3_theta_saturation.py](../experiments/sharp_s3_theta_saturation.py): independent evaluation of the xi second moment, a toy off-axis quartet radial Jensen integral, and the explicit perturbation gap.
- [tests/test_sharp_s3_theta_saturation.py](../tests/test_sharp_s3_theta_saturation.py): exact algebraic and numerical regression tests. These do not certify RH.
- [results/sharp_s3_theta_saturation.json](../results/sharp_s3_theta_saturation.json): numerical diagnostics, not interval-certified constants.
- NIST DLMF §25.10, https://dlmf.nist.gov/25.10.
- Jeffrey C. Lagarias, *On a Positivity Property of the Riemann ξ-Function* (1999), https://websites.umich.edu/~lagarias/doc/positivity.pdf (related known growth positivity criteria).
- O'Sullivan, *Zeros of Jensen polynomials and asymptotics for the Riemann xi function*, https://fsw01.bcc.cuny.edu/cormac.osullivan/Research/xi-revised.pdf (xi order, real-zero criteria).
- [22](22-quaternionic-s3-jensen-second-harmonic.md) and [23](23-positive-quaternionic-folding-penalty.md).

**Conclusion:** We have an exact, radial-data-only sharp S³ inequality and an independently specified **theta-only** equality criterion. The actual new proof step—**showing the theta function saturates that inequality**—remains unproved, and a close positive even perturbation fails saturation by an explicitly computable amount. The genuinely useful discovery is the precise obstruction and a quantitative falsification test for future candidate lemmas.
