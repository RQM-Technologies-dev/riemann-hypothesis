# 16 — Two folds, quaternionic zero-spheres, and a theta-kernel positivity program

**Date:** 2026-11-06  
**Status:** Research synthesis and exact RH-equivalent criteria; **NOT a proof of the Riemann hypothesis**.  
**Continues:** [08](08-theta-kernel-zero-latitudes.md), [12](12-symbolic-scale-and-defect.md), [13](13-theta-kernel-local-growth-certificate.md), [14](14-higher-moment-cosine-certificate.md), and [15](15-higher-moment-growth-certificate.md).

## 0. Research question and the "folding a page" picture

The proposed insight is that the Riemann hypothesis (RH) may be viewed as a collapse of **two independent reflection symmetries**. The two reflections create an orbit of up to four complex zero locations; after a natural quaternionic extension, those locations organize into up to **two spherical zero sets**. On the critical line the two spheres coincide.

This picture is exact. What is **not** established is a new kernel-derived constraint forcing coincidence at every zero. The research goal is to derive such a constraint from the **specific Jacobi-theta kernel** of the completed zeta function rather than to assume RH.

At a glance:

| Statement | Status |
| --- | --- |
| Xi has conjugation and functional-reflection symmetries | Exact, classical |
| The off-line quartet obeys an even quartic equation | Exact algebra |
| Slice-regular quaternionic extension has spherical zero sets | Exact construction |
| RH iff the reflected spherical zero sets coincide | Exact restatement |
| RH iff strict outward growth of the xi modulus | Known equivalent criterion |
| RH iff a particular theta-moment Toeplitz matrix is totally nonnegative | Follows from classical Pólya-frequency characterization and Xi product theory |
| The theta kernel meets the global condition | **Open** |
| A self-adjoint overlap representation alone enforces RH | **False** |
| This gives a new proof of RH | **No** |

## 1. Shared phase structure with Dirac wavefunctions (analogy, not identity)

Euler's complex exponential, rather than only its special value \(e^{i\pi}=-1\), supplies the common language:

\[
e^{i\vartheta}=\cos\vartheta+i\sin\vartheta.
\]

A stationary Dirac energy mode has phase evolution \(\psi(\tau)=e^{-iE\tau/\hbar}\psi(0)\), where \(\tau\) is **physical time**. In contrast, a zeta Dirichlet-series term in its region of absolute convergence \(\Re s>1\) is

\[
n^{-s}=n^{-\sigma}e^{-it\log n},\quad s=\sigma+it.
\]

The variable \(t\) is a **spectral height**, and \(\log n\) plays the logarithmic Fourier coordinate. The Dirichlet series **does not converge** at the nontrivial zeros, so it cannot be inserted there without analytic continuation or an appropriate alternate formula. The Mellin/Fourier connection is genuine; identifying spectral height with physical time is not.

Spin-\(\tfrac12\) states change sign under a full \(2\pi\) spatial rotation and return after \(4\pi\) because \(SU(2)\) double-covers \(SO(3)\). Charge conjugation of Dirac spinors involves complex conjugation **and** a matrix transformation; it is not identical to the two zeta reflections or quaternionic conjugation. These are structurally suggestive comparisons, not an operator-level equivalence.

## 2. The two reflections and the quartic orbit

Let the completed xi function and centered coordinate be

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad w=s-\tfrac12.
\]

The xi function satisfies

\[
\xi(1-s)=\xi(s),\qquad
\xi(\bar s)=\overline{\xi(s)}.
\]

For a nontrivial zero \(\rho=\tfrac12+a+it\), with \(t>0\), the four symmetry-related positions are

\[
\rho,\quad \bar\rho,\quad 1-\rho,\quad 1-\bar\rho.
\]

In the centered coordinate they are \(w,\bar w,-w,-\bar w\), with \(w=a+it\). The polynomial having that orbit as roots is

\[
\begin{aligned}
P(X)&=(X-w)(X+w)(X-\bar w)(X+\bar w)\\
&=X^4-2\operatorname{Re}(w^2)X^2+|w|^4\\
&=X^4+2(t^2-a^2)X^2+(a^2+t^2)^2.
\end{aligned}
\]

The two involutions form the **Klein four-group** when independent, not a cyclic group of quarter-turns. Having a quartic relation does **not** establish an independent four-dimensional analytic law or a fourth-root law. A reflection orbit can be off the fold.

When \(a=0\), the quartet reduces to the conjugate pair and the polynomial becomes

\[
\boxed{P(X)=(X^2+t^2)^2.}
\]

The repeated algebraic factor encodes collision of reflected orbits; it does **not** show that a zeta zero has multiplicity two.

A related exact formulation follows because \(f(w)=\xi(\tfrac12+w)\) is a real, even entire function:

\[
f(w)=G(w^2)
\]

for an entire function \(G\) with real coefficients. RH is equivalent to **all zeros of \(G\) being negative real numbers**. Reflection guarantees the even form; it does not prove the real-negative zero property.

### Unit-circle version of the two folds

Set \(h(s)=(s-1)/s\). Then

\[
h(1-s)=h(s)^{-1},\qquad h(\bar s)=\overline{h(s)},
\]

and

\[
\Re s=\tfrac12 \iff |h(s)|=1.
\]

On that circle, inversion equals complex conjugation: \(1/h=\bar h\). Hence two distinct reflections **coincide on the critical circle**. This is again an exact reformulation, not a proof that every zero lies there.

## 3. Canonical slice-regular quaternionic lift and spherical zero sets

With \(\mathbb H\) the real quaternions, let \(q=x+uy\) where \(u^2=-1\) and \(u\) ranges over the unit imaginary quaternions \(S^2\). Since the centered xi Taylor series has real coefficients and is even,

\[
f(w)=\sum_{n=0}^\infty c_nw^{2n},\qquad c_n\in\mathbb R,
\]

it admits the whole-space, intrinsic, slice-regular extension

\[
\mathcal X(q)=\sum_{n=0}^\infty c_nq^{2n}.
\]

On every complex slice \(\mathbb R+\mathbb R u\), this is the original centered holomorphic function under the corresponding identification of \(u\) with \(i\). A nonreal complex zero at \(a+it\) and its conjugate extend to the spherical zero set

\[
\mathcal S_{a,t}=\{a+ut:u^2=-1\}\cong S^2.
\]

The functional reflection produces \(\mathcal S_{-a,t}\). Their equality is completely characterized:

\[
\boxed{\mathcal S_{a,t}=\mathcal S_{-a,t}\iff a=0.}
\]

Thus RH is equivalent to every nontrivial spherical zero set being fixed individually by centered reflection \(q\mapsto -q\), or equivalently to the absence of distinct off-center reflected sphere pairs.

The quartic above factors into the two real-coefficient spherical factors:

\[
P(q)=[q^2-2aq+(a^2+t^2)]\,
[q^2+2aq+(a^2+t^2)].
\]

At \(a=0\) the two spheres coincide and \(P(q)=(q^2+t^2)^2\).

**Geometric guardrail:** these zero sets are \(S^2\) subsets of **four-real-dimensional quaternionic space**. They are not themselves the unit quaternion group \(S^3\). The repo's separate, global Cayley mapping \(Q_L(t,u)\in S^3\) from [12](12-symbolic-scale-and-defect.md) is a **coordinate representation of critical-line heights**; it is not the same as the slice-regular zero-sphere lift. Do not conflate their radii, dimensions, or analyticity classes. The Cayley scale \(L>0\) stays symbolic and cannot change zero locations.

**Symmetry-alone counterexample:** \(p(q)=q^4+4\) is intrinsic, even, real-coefficient and has the same reflection pattern, but its zeros include \(q=1+i\) and \(q=-1+i\). Its zero-spheres sit at \(a=\pm1\), not on the fold \(a=0\). An additional analytic/arithmetic input is necessary.

## 4. The actual Jacobi-theta Fourier kernel

Set

\[
\Xi(z)=\xi(\tfrac12+iz).
\]

Use the standard real, even, strictly positive, super-exponentially decreasing kernel (as in [08](08-theta-kernel-zero-latitudes.md)):

\[
\Xi(z)=2\int_0^\infty\Phi(u)\cos(zu)\,du
=\int_{-\infty}^{\infty}\Phi(u)e^{izu}\,du,
\]

\[
\Phi(u)=\sum_{n=1}^\infty
\left(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2}\right)
e^{-\pi n^2e^{2u}}.
\]

The theta modular relation ensures evenness; the precise combination of derivatives yields this specific xi kernel. The integrals and all moment derivatives converge for arbitrary complex \(z\).

Write \(z=t+ia\) with \(t\in\mathbb R\) and \(a\ge0\), and set

\[
C(t,a)=\int_0^\infty\Phi(u)\cos(tu)\cosh(au)\,du,
\]

\[
S(t,a)=\int_0^\infty\Phi(u)\sin(tu)\sinh(au)\,du.
\]

Then

\[
\Xi(t+ia)=2[C(t,a)-iS(t,a)]
\]

and, because of xi's symmetries,

\[
W(t,a)=|\Xi(t+ia)|^2
=\left|\xi(\tfrac12+a+it)\right|^2
=4(C^2+S^2).
\]

Consequently

\[
\boxed{\mathcal P(t,a)=\partial_aW(t,a)
=8(CC_a+SS_a).}
\]

This is an **exact identity from the theta kernel**, not an assertion of its global sign. The full signed bilinear double integral for \(CC_a+SS_a\), with its sign-changing cosine factors and positive amplitudes, is already derived in [15](15-higher-moment-growth-certificate.md).

## 5. Strict outward growth: an exact RH equivalence

The proposed global constraint is

\[
\boxed{\mathcal P(t,a)>0\quad
(t\in\mathbb R,\ a>0).}
\]

**It is equivalent to RH.**

**Sufficiency:** If an off-line zero existed at \(s=\tfrac12+a_0+it_0\), with \(a_0>0\) after using the xi symmetry, then \(W(t_0,a_0)=0\). As a smooth nonnegative function of \(a\), \(W\) must have \(\partial_aW(t_0,a_0)=0\), contradicting strict positivity.

**Necessity:** Under RH, the paired Hadamard product of \(\Xi\) can be written

\[
\Xi(z)=\Xi(0)\prod_{\gamma>0}\left(1-\frac{z^2}{\gamma^2}\right)
\]

with multiplicity and an appropriate canonical pairing. The corresponding sum of reciprocal squares converges. For \(z=t+ia\), \(a>0\),

\[
\partial_a\log W(t,a)
=2a\sum_{\gamma>0}\left(
\frac1{(t-\gamma)^2+a^2}
+\frac1{(t+\gamma)^2+a^2}
\right)>0.
\]

Thus \(\partial_aW>0\). This criterion is a classical Hinkkanen–Lagarias positivity reformulation, related to the Sondow–Dumitrescu horizontal-modulus monotonicity theorem.

**What is proved unconditionally?** The positive theta kernel supplies the exact formula for \(\mathcal P\), and existing work [13–15] proves *local* positive regions using moments and global cosine minorants. The sign of the cosine factors prevents inferring \(\mathcal P>0\) for all spectral heights merely from \(\Phi>0\). The global all-height result remains RH-equivalent and **unproved**.

## 6. Self-adjoint overlap and conserved norm: useful but insufficient

Let

\[
\mathcal H=L^2(\mathbb R,\Phi(u)\,du),\qquad
(Dg)(u)=u\,g(u)
\]

with the natural domain for the self-adjoint multiplication operator \(D\).
For real parameter \(t\), \(U(t)=e^{itD}\) is unitary and

\[
\|U(t)g\|=\|g\|,\qquad
\Xi(t)=\langle \mathbf 1,U(t)\mathbf 1\rangle
\]

with the inner-product convention linear in the second argument.

This establishes an exact **mathematical unitary-overlap representation**, and thus a conserved norm. The parameter \(t\) is xi spectral height, **not a claim of physical time evolution**. Importantly, the zeros of this overlap are *not* eigenvalues of \(D\); the spectrum of \(D\) is continuous.

Positivity of a spectral measure and self-adjointness alone do **not** force the Fourier-transform zeros to be real. For example the positive finite measure \(2\delta_0+\frac12(\delta_{-1}+\delta_{+1})\) has Fourier transform \(2+\cos z\), which vanishes at

\[
z=(2k+1)\pi\pm i\,\operatorname{arcosh}(2).
\]

A genuine Hilbert–Pólya-type result must supply a **new, justified spectral determinant/eigenvalue identification** or a stronger positivity property than mere unitary evolution.

## 7. Theta moments and total nonnegativity: a stronger exact criterion

Expand

\[
\Xi(z)=\sum_{n=0}^\infty(-1)^na_nz^{2n},
\]

where the *positive* coefficients are the actual theta moments

\[
\boxed{
a_n=\frac{2}{(2n)!}\int_0^\infty
u^{2n}\Phi(u)\,du
=\frac{\xi^{(2n)}(1/2)}{(2n)!}>0.}
\]

Define the entire function

\[
F(v)=\sum_{n=0}^\infty a_nv^n
=\Xi(i\sqrt v)=\xi(\tfrac12+\sqrt v).
\]

The square root notation is harmless: by xi evenness the expression is a single-valued entire function of \(v\). RH is equivalent to all zeros of \(F\) being **negative real** (the zero at \(\tfrac12\) is absent). Because \(F\) has order at most \(1/2\), its Hadamard factorization under RH is a genus-zero product of factors \(1+\alpha_jv\), with \(\alpha_j\ge0\) and \(\sum_j\alpha_j<\infty\).

Let \(a_k=0\) for \(k<0\) and construct the infinite Toeplitz matrix

\[
T_{ij}=a_{i-j},\quad i,j\ge0.
\]

By the Aissen–Schoenberg–Whitney–Edrei characterization of Pólya-frequency (\(\mathrm{PF}_\infty\)) sequences and the entire nature of \(F\),

\[
\boxed{\mathrm{RH}\iff
\text{every finite minor of }T\text{ is nonnegative}.}
\]

Why this is an equivalence: RH implies a product with only real negative zeros, whose coefficient Toeplitz matrix is totally nonnegative. Conversely the PF-infinity factorization, combined with the fact that \(F\) is entire (and has no positive-axis poles), forces every zero to be real and nonpositive, hence RH.

The first informative \(2\times2\) inequality is

\[
\boxed{a_1^2-a_0a_2\ge0.}
\]

Numerical values from the actual theta moments (not certified intervals) are:

| Quantity | Numerical value |
| --- | ---: |
| \(a_0\) | \(0.497120778188314109912774\) |
| \(a_1\) | \(0.011485972157572718767625\) |
| \(a_2\) | \(0.000123452018070318006890346\) |
| \(a_3\) | \(0.000000832355481385527072005\) |
| \(a_1^2-a_0a_2\) | \(0.0000705569931125013930942051>0\) |

**Important:** one minor, finitely many minors, ordinary moment positivity, or even finite-order \(\mathrm{PF}_r\) results cannot establish all minors of the infinite matrix are nonnegative. Existing finite-order positivity studies remain partial progress, not RH.

The accompanying [numerical experiment](../experiments/two_fold_theta_positivity.py), [regression tests](../tests/test_two_fold_theta_positivity.py), and [recorded output](../results/two_fold_theta_positivity.json) reproduce the first moments independently from (i) theta-kernel quadrature and (ii) xi derivatives. These numerical comparisons check formulas; they cannot establish the infinite statement.

## 8. The precise proof gap and a research program

The desired implication is

\[
\text{specific Jacobi modular/arithmetic structure}
\quad\Longrightarrow\quad
\begin{cases}
\partial_a|\Xi(t+ia)|^2>0
&\forall t\in\mathbb R,\ a>0,\\
\text{or equivalently }\mathrm{PF}_\infty\text{ for }(a_n).
\end{cases}
\]

This implication is not proved; either successful route would establish RH.

Suggested work:

1. Derive a **global** signed-oscillation estimate for the exact double integral in [15], using the modular identity rather than the bare assertion \(\Phi>0\). Test the estimate against positive-kernel counterexamples before claiming a universal positivity theorem.
2. Seek a recurrence, integral factorization, or variation-diminishing mechanism that proves **every** finite Toeplitz minor is nonnegative, uniformly in its indices and order. Existing finite-order certificates can serve as checks.
3. Seek an operator whose **spectrum or Fredholm determinant** is rigorously identified with *all* xi zeros; do not substitute the already-known multiplication-operator overlap for such an identification.
4. Translate any theorem back to the zero-sphere statement: no pair \(\mathcal S_{a,t},\mathcal S_{-a,t}\) with \(a\ne0\). Preserve the distinction between the \(S^2\) zero sets and the repo's common \(S^3\) meridian.
5. Compare with the existing **scale-free defect** \(\mathcal E\) and \(D(L)\) in [12]. Those are separate RH-equivalent formulations. Keep \(L>0\) symbolic; numerical agreement over finite heights or a vanishing coordinate-scale limit is not a proof of exhaustion.

**Falsification tests:** the polynomial \(q^4+4\) refutes a proof from reflection symmetry alone; \(2+\cos z\) refutes one from positive measures / unitarity alone. A legitimate proof must use something special about xi beyond these shared structures.

## 9. References and lineage

- Riemann xi definitions and zeros: NIST DLMF §25.10, https://dlmf.nist.gov/25.10 ; Wolfram MathWorld, https://mathworld.wolfram.com/Xi-Function.html.
- Riemann theta-kernel Fourier formula: J. C. Lagarias and D. Montague, *The Integral of the Riemann xi-function*; see [08](08-theta-kernel-zero-latitudes.md) for the adopted normalization.
- J. C. Lagarias, *On a positivity property of the Riemann ξ-function*, Acta Arithmetica 89 (1999), 217–234, https://doi.org/10.4064/aa-89-3-217-234.
- J. Sondow and C. Dumitrescu, *A monotonicity property of Riemann's xi function and a reformulation of the Riemann Hypothesis*, https://arxiv.org/abs/1005.1104.
- M. Planat, *A Theta-Kernel Reformulation of Riemann-Xi Growth and the Obstruction to Blockwise Positivity*, Symmetry 18 (2026), 1283, https://doi.org/10.3390/sym18081283.
- G. Gentili, C. Stoppato, D. C. Struppa, *Regular Functions of a Quaternionic Variable* (Springer, 2013), https://doi.org/10.1007/978-3-642-33871-7; Gentili and Stoppato on spherical zero sets, https://arxiv.org/abs/0907.5565.
- Aissen–Schoenberg–Whitney–Edrei/Pólya-frequency criterion: exposition in *Totally Positive Toeplitz Matrices: Classical and Modern*, https://doi.org/10.1137/25M1806727.
- RQM predecessor notes: [00 research lineage](00-research-lineage.md), [08 theta zero-latitudes](08-theta-kernel-zero-latitudes.md), [12 symbolic-scale defect](12-symbolic-scale-and-defect.md), and [13–15 partial moment growth certificates](13-theta-kernel-local-growth-certificate.md).

**Bottom line:** the double fold produces an exact quartet and a quaternionic pair of zero-spheres; RH is their merger at the centered slice. The theta kernel supplies exact growth and moment expressions, but neither symmetry, positivity of \(\Phi\), nor self-adjoint overlap alone proves that the spheres must merge. The missing result is an unconditional, *global* positivity/real-rootedness theorem specific to xi.
