# 22 — A rigorous S³ Jensen identity for quaternionic Riemann xi

**Date:** 2026-11-06  
**Status:** Exact 4D angular-average identity, an explicit zero-divisor expansion, and independent high-precision numerical checks. **Not a proof of the Riemann hypothesis.**  
**Primary research context:** [21 — quaternionic theta continuation and superposed zero-spheres](21-quaternionic-theta-superposed-zero-spheres.md).

## 1. Why calculate a four-dimensional spherical average?

The user's primary investigation is whether the **superposition and folding of quaternionic zeta zero-spheres** yields a useful *extra analytic constraint*, rather than simply restating complex conjugate symmetry.

Start from the intrinsic slice-regular entire function

\[
F(q)=\mathcal X(q)=\xi(\tfrac12+q)
=2\int_0^\infty\Phi(v)\cosh(qv)\,dv,
\]

where the final equation is the quaternionic theta-integral constructed in [21](21-quaternionic-theta-superposed-zero-spheres.md). Because the coefficients are real, its norm is independent of the imaginary direction on the conjugacy sphere at fixed \(\Re q\) and \(|\Im q|\).

We compute the **ordinary SO(4)-invariant surface average** of \(\log|F(q)|\) over the centered quaternionic radius-\(R\) three-sphere \(S^3_R\). This is not the same object as the spherical \(S^2\) zero divisor or the repo's free-scale Cayley map.

## 2. A new-to-this-repository exact geometric identity

Parameterize \(q\in S^3_R\) as

\[
q=R\cos\theta+uR\sin\theta,\quad
0\le\theta\le\pi,\quad u^2=-1,\ u\in S^2.
\]

Let \(f(z)=\xi(\tfrac12+z)\). For a radius \(R>0\) such that \(f\) has no zeros on \(|z|=R\), define

\[
h_R(\theta)=\log|f(Re^{i\theta})|.
\]

On the three-sphere, the normalized surface element is

\[
d\sigma_{S^3}=\frac{2}{\pi}\sin^2\theta\,d\theta\,d\omega(u),
\]

where \(d\omega\) is the normalized rotation-invariant probability measure on \(S^2\). Since \(|F(q)|=|f(Re^{i\theta})|\), the \(S^2\) orientation integral contributes 1.

Because \(f\) has real coefficients, \(h_R(\theta)=h_R(2\pi-\theta)\). Therefore the normalized quaternionic mean is

\[
\begin{aligned}
M_4(R)&:=\int_{S^3_R}\log|F(q)|\,d\sigma_{S^3}\\
&=\frac{2}{\pi}\int_0^\pi\sin^2\theta\,h_R(\theta)\,d\theta\\
&=\boxed{\frac1{2\pi}\int_0^{2\pi}
[1-\cos(2\theta)]h_R(\theta)\,d\theta.}
\end{aligned}
\tag{J1}
\]

Set

\[
M_2(R)=\frac1{2\pi}\int_0^{2\pi}h_R(\theta)\,d\theta,\qquad
K_2(R)=\frac1{2\pi}\int_0^{2\pi}\cos(2\theta)\,h_R(\theta)\,d\theta.
\]

Then

\[
\boxed{M_4(R)=M_2(R)-K_2(R).}
\tag{J2}
\]

**Interpretation:** the four-dimensional average subtracts exactly the **second angular Fourier harmonic** of the complex logarithmic modulus. This isolates information about the shape of the zero distribution that the ordinary circular Jensen mean \(M_2\) does not isolate. But the additional term is still determined by the same complex function: the quaternionic lift creates no independent zeros.

## 3. An exact theta-accessible formula inside a zero-free disk

Suppose the disk \(|z|\le R\) contains no Xi zeros. Then a holomorphic logarithm of \(f\) exists in a neighborhood of that disk, with real Taylor coefficients at zero; moreover \(f'(0)=0\) by centered xi evenness.

For the ordinary Jensen circle mean, \(M_2(R)=\log f(0)\). For the second Fourier harmonic, only the \(z^2\) coefficient in \(\log f(z)\) contributes:

\[
[z^2]\log f(z)=\frac{f''(0)}{2f(0)}.
\]

Hence

\[
\boxed{
K_2(R)=\frac{R^2}{4}\frac{f''(0)}{f(0)}.
}
\tag{J3}
\]

Combining with (J2) gives the **exact**, not asymptotic, four-dimensional identity

\[
\boxed{
M_4(R)=\log\xi(\tfrac12)
-\frac{R^2}{4}\frac{\xi''(\tfrac12)}{\xi(\tfrac12)}
}
\quad\text{for every zero-free radius }R.
\tag{J4}
\]

The first completed-xi zero radius is the first critical-line height \(14.134725\ldots\), known unconditionally from classical zero verification. In particular, the formula holds at \(R=1,5,10,13\).

The theta kernel computes the coefficient **without inserting any zero locations**:

\[
f(0)=2\int_0^\infty\Phi(v)\,dv,\qquad
f''(0)=2\int_0^\infty v^2\Phi(v)\,dv.
\tag{J5}
\]

Thus the quaternionic mean is directly calculable from the original modular/arithmetical theta data.

### High-precision cross-check (not interval-certified)

At 45-digit mpmath precision:

\[
\xi(\tfrac12)\approx0.49712077818831410991277374,\qquad
\frac{\xi''(\tfrac12)}{\xi(\tfrac12)}
\approx0.0462099862308379415778676209.
\]

| Radius \(R\) | Exact expression (J4) | Independently integrated \(S^3\) mean |
| ---: | ---: | ---: |
| 1 | -0.71047476450304090069 | -0.71047476450304090069 |
| 5 | -0.98773468188806855016 | -0.98773468188806855016 |
| 10 | -1.85417192371627995475 | -1.85417192371627995475 |
| 13 | -2.65129418619823444696 | -2.65129418619823444696 |

Each agreement is numerical and limited by quadrature/precision; (J1)–(J5) are mathematical identities.

## 4. The complete zero-divisor version, valid beyond the first zero

The even entire function \(f(z)=\xi(\tfrac12+z)\), of order one, has a convergent centered paired Hadamard product

\[
f(z)=f(0)\prod_{\alpha\in\mathcal P}
\left(1-\frac{z^2}{\alpha^2}\right),
\tag{J6}
\]

where \(\mathcal P\) selects **one representative from each \(\pm\alpha\) pair** of zeros, counted with multiplicity, and \(\sum_{\alpha\in\mathcal P}|\alpha|^{-2}<\infty\). For an off-line quartet, there are **two** \(\pm\) pairs, not one. On the critical line the \(\pm it\) conjugate pair is represented once per actual zero multiplicity; no artificial doubled factor is introduced.

For \(R>0\) with no zero on \(|z|=R\), the ordinary Jensen mean is

\[
M_2(R)=\log f(0)
+\sum_{\substack{\alpha\in\mathcal P\\|\alpha|<R}}
2\log\frac{R}{|\alpha|}.
\tag{J7}
\]

The angular coefficient of one paired factor is obtained from the two convergent logarithmic expansions:

\[
K_{2,\alpha}(R)=
\begin{cases}
-\dfrac{R^2}{2}\operatorname{Re}(\alpha^{-2}),
&|\alpha|>R,\\[6pt]
-\dfrac{1}{2R^2}\operatorname{Re}(\alpha^2),
&|\alpha|<R.
\end{cases}
\tag{J8}
\]

Therefore

\[
\boxed{
\begin{aligned}
M_4(R)=\log f(0)
&+\sum_{|\alpha|<R}
\left[
2\log\frac{R}{|\alpha|}
+\frac{\operatorname{Re}(\alpha^2)}{2R^2}
\right]\\
&+\sum_{|\alpha|>R}
\frac{R^2}{2}\operatorname{Re}(\alpha^{-2}).
\end{aligned}}
\tag{J9}
\]

This **explicit quaternionic Jensen-type expansion** contains a different weighting of zero locations from ordinary Jensen: it depends on the *second angular harmonic* \(\operatorname{Re}(\alpha^2)\) or \(\operatorname{Re}(\alpha^{-2})\).

For a representative \(\alpha=a+it\),

\[
\operatorname{Re}(\alpha^2)=a^2-t^2,\qquad
\operatorname{Re}(\alpha^{-2})
=\frac{a^2-t^2}{(a^2+t^2)^2}.
\tag{J10}
\]

Thus the 4D mean is **sensitive to the transverse distance \(a^2\)** of a hypothetical off-center sphere. This is why it may serve as a useful mathematical probe of the proposed superposed zero-sphere geometry.

The formula is *derived* from ordinary Hadamard/Jensen theory and the four-dimensional measure (J1), rather than claimed as a brand-new independent theorem; compare the more general quaternionic Jensen formulas of Altavilla–Bisi and Perotti.

### Important limitation

Even if \(M_4(R)\) and \(M_2(R)\) are both known from the theta kernel for every \(R\), **extracting the zero distribution is not automatically the same as proving all zeros have \(a=0\)**. The kernel identities could hold for an arbitrary symmetrical off-axis quartet, as the counterexample \(p(q)=q^4+4\) in [21](21-quaternionic-theta-superposed-zero-spheres.md) shows.

In the Riemann xi setting, all actual nontrivial zero heights are much larger than the maximum permitted off-line displacement, so \(t^2>a^2\). Consequently each zero-pair term in \(K_2(R)\) has the same sign, even off the line. Sign positivity of the second harmonic alone is **not** a proof of RH.

## 5. The next noncircular proof target using these four-dimensional observables

Use the **pair of exact theta-calculable observables**
\[
M_2(R)\quad\text{and}\quad M_4(R)
\]
to investigate whether the Jacobi theta/Poisson modular structure supplies **an independent relation among their radial derivatives or higher spherical harmonics** that cannot be satisfied by any reflected off-center spherical zero pair.

A successful theorem would show that the **spherical zero-divisor measure has support only at \(\Re q=0\)**. That statement is exactly RH in the quaternionic lift, so the proof must derive it from a new, justified arithmetic/analytic lemma rather than assuming it.

Concrete work items:

1. Compute \(M_2(R)\), \(M_4(R)\), and \(K_2(R)\) directly from (Q2) and compare with (J9) at radii above and below successive known zero heights, with rigorous treatment of circles containing zeros.
2. Derive 4D radial differentiation identities (with jumps/cusps across spherical zero radii). Determine what part depends on the off-center displacement \(a\) versus the zero height \(t\).
3. Compare the angular-moment hierarchy to the *exact* theta derivative identities and to the pre-existing all-scale defect \(D(L)\) from [12](12-symbolic-scale-and-defect.md). No equivalence to an RH criterion may be mislabeled as a proof of its vanishing.
4. Try to formulate an arithmetic/modular **closure inequality** making the off-center contribution impossible, and falsify it on the intrinsic even polynomial \(q^4+4\) and modified positive Fourier kernels from [20](20-inward-fold-normal-form-flux-and-jensen-obstruction.md).
5. If successful, transport that result to the \(S^2\) zero-spheres \(\mathcal S_{a,t},\mathcal S_{-a,t}\) and prove \(a=0\) for all nontrivial zeros. Keep the separate free-scale \(S^3\) Cayley coordinate \(L>0\) symbolic and out of the proof assumptions.

**Current finding:** A precise new-to-the-project 4D Jensen observable has been constructed and tied to the original theta kernel and the second angular harmonic. It is informative about sphere displacement, but does not by itself exclude off-center zeros.

## 6. Sources and reproducibility

- [21 — quaternionic theta lift and sphere superposition](21-quaternionic-theta-superposed-zero-spheres.md).
- [12 — all-scale missing-zero defect](12-symbolic-scale-and-defect.md).
- [08 — Jacobi-theta kernel](08-theta-kernel-zero-latitudes.md).
- A. Altavilla and C. Bisi, *Log-biharmonicity and a Jensen formula in the space of quaternions* (2019): https://www.acadsci.fi/mathematica/Vol44/vol44pp0805-0839.pdf.
- A. Perotti, *A four dimensional Jensen formula* (2020): https://www.rivmat.unipr.it/vols/2020-11-1/07-perotti.html.
- Existing executable numerical checks: [experiments/quaternionic_s3_jensen.py](../experiments/quaternionic_s3_jensen.py), [tests](../tests/test_quaternionic_s3_jensen.py), [sample results](../results/quaternionic_s3_jensen.json).

**Interpretation boundary:** the real mathematical novelty, if it exists, must occur in an unconditional **theta-specific constraint on these angular zero-distribution observables**. Neither the 4D measure identity nor quaternionic zero-sphere geometry alone supplies that constraint.
