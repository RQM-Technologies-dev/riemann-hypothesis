# 17 — Clay Millennium Problem: exact proof target and investigation roadmap

**Date:** 2026-11-06  
**Repository goal:** a rigorous proof or disproof of the Riemann hypothesis (RH) as officially stated by the Clay Mathematics Institute (CMI).  
**Present status:** **UNSOLVED; NO PROOF CLAIMED.** This document prioritizes open proof obligations and clearly separates established reformulations from new theorems.

## 1. Start from the official problem, not from the geometry

Enrico Bombieri's official CMI problem description, *Problems of the Millennium: the Riemann Hypothesis*, section I, page 1, states:

> Riemann hypothesis. The nontrivial zeros of ζ(s) have real part equal to 1/2.

Official source: https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf  
CMI problem page (lists RH as unsolved): https://www.claymath.org/millennium/Riemann-Hypothesis/

In symbols, the theorem to prove is

\[
\boxed{
\forall \rho\in\mathbb C,\quad
[\zeta(\rho)=0\ \wedge\ 0<\Re\rho<1]
\Longrightarrow \Re\rho=\tfrac12.
}
\]

The trivial zeros \(-2,-4,\ldots\) are excluded. The zeta Dirichlet series \(\sum_{n\ge1}n^{-s}\) converges absolutely only for \(\Re s>1\); its meromorphic continuation to \(\mathbb C\setminus\{1\}\) **already exists**, and constructing a new higher-dimensional continuation is **not** the Clay objective.

Bombieri uses \(\xi(t)\) for the completed zeta function evaluated at \(s=\tfrac12+it\). **Notation in this repository differs**, so we keep these distinct:

\[
\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad
\Xi(z)=\xi(\tfrac12+iz).
\]

The equivalent exact Clay target is

\[
\boxed{\Xi(z)=0\ \Longrightarrow z\in\mathbb R.}
\]

Indeed, for any nontrivial zero \(\rho=\beta+i\gamma\), the corresponding Xi zero is
\(z=\gamma-i(\beta-\tfrac12)\). Thus \(z\) real if and only if \(\beta=\tfrac12\).

**Success criterion:** provide an unconditional, noncircular mathematical proof that rules out **every** off-critical-line zero, including arbitrarily high spectral heights, without assuming RH in an auxiliary lemma. No requirement to establish simplicity, spacing, or any particular spectral multiplicity. Independent expert scrutiny is essential before any public proof claim.

## 2. Translate the higher symmetry observation into Clay's target

With \(w=s-\tfrac12\), conjugation and functional reflection give the orbit

\[
w,\quad \bar w,\quad -w,\quad-\bar w.
\]

For \(w=a+it\), the associated orbit polynomial is

\[
P(X)=X^4+2(t^2-a^2)X^2+(a^2+t^2)^2.
\]

On the critical line (\(a=0\)) it becomes \((X^2+t^2)^2\). The intrinsic slice-regular quaternionic extension of the centered completed xi function produces spherical zero sets

\[
\mathcal S_{a,t}=\{a+ut:u^2=-1\}\simeq S^2
\]

and their functional-reflection partners \(\mathcal S_{-a,t}\). They coincide **exactly when \(a=0\)**.

This is a rigorous, useful **equivalent geometric translation** of the zero-location problem. It does not prove coincidence: two mirrors can map a zero to several distinct points. Likewise the Cayley/compactified *unit quaternion* \(S^3\) model of [08](08-theta-kernel-zero-latitudes.md) and [12](12-symbolic-scale-and-defect.md) is a separate coordinate system and puts **every critical-line coordinate** on its sphere, regardless of being a zeta zero. Do not conflate the quaternionic \(S^2\) zero-spheres with the Cayley \(S^3\) ambient hypersphere.

**Correct use of the phrase "one zero-sphere at each height":** at any *actual zero height*, all zero-spheres must be centered on the critical-line slice \(a=0\); RH does **not** imply there is a zero at every height, nor that zeros are simple. This is **not** a new analytic continuation theorem or automatically a four-spatial-dimensional law.

The quartic, unit-circle folding, and Dirac/spinor phase analogy remain useful conceptual tools **only if** they help derive an independent analytic restriction on zeros. See [16](16-two-fold-zero-spheres-and-theta-positivity.md).

## 3. Choose a precisely stated analytic theorem that would settle Clay's task

### Primary target: strict outward Xi growth from the **actual** theta kernel

The positive, even Jacobi-theta kernel \(\Phi\) provides

\[
\Xi(z)=2\int_0^\infty\Phi(u)\cos(zu)\,du.
\]

For real spectral height \(x\), and transverse coordinate \(y>0\), define

\[
C(x,y)=\int_0^\infty\Phi(u)\cos(xu)\cosh(yu)\,du,
\quad
S(x,y)=\int_0^\infty\Phi(u)\sin(xu)\sinh(yu)\,du.
\]

Then, exactly,

\[
\Xi(x+iy)=2[C(x,y)-iS(x,y)],
\quad
\frac18\,\partial_y|\Xi(x+iy)|^2
=CC_y+SS_y=:G(x,y).
\]

**Proposed proof obligation A** is the unconditional inequality

\[
\boxed{G(x,y)>0
\quad \text{for every }x\in\mathbb R,\ 0<y\le\tfrac12.}
\tag{A}
\]

This would immediately prohibit a zero off the line in the critical strip: a zero of a squared modulus is a nonnegative interior minimum, where its derivative in \(y\) vanishes; (A) forbids that. Combining with the classical exclusion of nontrivial zeros outside the critical strip proves RH. The all-\(y>0\) version is a known RH-equivalent horizontal-modulus growth criterion (see Sondow–Dumitrescu); **we have not established (A)**.

Crucially, the exact signed bilinear theta representation is (see [15](15-higher-moment-growth-certificate.md))

\[
\begin{aligned}
G(x,y)&=\frac14\int_0^\infty\int_0^\infty
\Phi(u)\Phi(v)\Big[
(u+v)\sinh(y(u+v))\cos(x(u-v))\\
&\qquad\qquad\qquad +(u-v)\sinh(y(u-v))\cos(x(u+v))
\Big]\,du\,dv.
\end{aligned}
\tag{B}
\]

Both hyperbolic amplitudes are nonnegative for \(y>0\), but the cosine factors change sign. **Therefore \(\Phi>0\) by itself cannot imply (A).** We must exploit theta-specific modular or arithmetic identities to control the negative oscillatory contributions for **every** \(x\), rather than merely showing a finite rectangle is positive.

### Alternative target: infinite-order Pólya-frequency positivity

Write

\[
\Xi(z)=\sum_{n=0}^{\infty}(-1)^na_nz^{2n},\qquad
a_n=\frac{2}{(2n)!}\int_0^\infty\Phi(u)u^{2n}\,du>0.
\]

The function \(F(v)=\Xi(i\sqrt v)=\sum a_nv^n\) is entire; RH says its zeros all lie on the negative real axis. A classical Pólya-frequency characterization gives the equivalent condition

\[
\boxed{\det(a_{r_i-c_j})_{1\le i,j\le k}\ge0
\ \text{for all }k,\text{ and all strictly increasing nonnegative index sets},}
\tag{C}
\]

with \(a_m=0\) for \(m<0\). Equivalently, the infinite Toeplitz matrix \(T_{ij}=a_{i-j}\) must be totally nonnegative.

This is **proof obligation B**, not an already-established property of the theta moments. Finite-order minor positivity is only a diagnostic. Any useful attack must generate a uniform, all-orders inequality or factorization from the exact theta kernel.

### Operator alternative: exact spectral identity, not merely self-adjoint overlap

The known identity \(\Xi(x)=\langle\mathbf1,e^{ixD}\mathbf1\rangle\), with \(D\) the self-adjoint multiplication operator in \(L^2(\mathbb R,\Phi(u)\,du)\), gives a conserved norm **but does not identify Xi zeros as eigenvalues**. Positive measures can have Fourier transforms with nonreal zeros (e.g. \(2+\cos z\)).

A genuine operator proof would require independently constructing a self-adjoint operator or positive canonical system with a **proved exact correspondence** between its real spectrum and **every** Xi zero, accounting for possible multiplicities and excluding extra/missing spectral solutions. Numerical matching, formal determinants, or quaternionic symmetry alone are not sufficient.

## 4. Prioritized route of investigation — with failure gates

### Track A (PRIMARY): prove a new theta-specific global oscillation inequality

**A1. Reproduce, audit, and isolate the exact inequality.** Use [13–15](13-theta-kernel-local-growth-certificate.md) (and the direct extension in [15](15-higher-moment-growth-certificate.md)) to confirm (B), all constants, allowed changes of variables, interchange of limits and integrals, and boundary \(y\to0^+\). Verify the known near-origin growth certificates with independent code. Separate symbolic theorems from approximate decimals.

**A2. Analyze the theta modular relation rather than mere positivity.** Starting from \(\Theta(t)=t^{-1/2}\Theta(1/t)\), derive identities for \(\Phi(u)\), its transforms, derivatives and any genuinely sign-definite quadratic expressions. Try to isolate the signed cosine terms in (B) into modularly linked families, or establish a **uniform coercive estimate** for their sum. Keep all spectral heights \(x\) in scope; any bound that holds only for fixed finite \(x\) is a partial theorem.

**A3. Build minimal candidate lemmas.** For each claimed inequality record (i) precise hypotheses, (ii) the modular identity used, (iii) why it **fails** for a generic positive even super-exponentially decaying kernel, (iv) whether the estimate is uniform in \(x\) and \(0<y\le1/2\), and (v) whether it becomes circular by assuming no off-line zeros. A successful lemma should produce a provable lower bound \(G(x,y)\ge y\,B(x,y)\) with \(B(x,y)>0\) globally (or another exact inequality strong enough to imply (A)).

**A4. Counterexample suite and numerical stress test.** Test candidates against explicit positive measures with nonreal Fourier zeros; smooth those measures to positive rapidly decreasing kernels where possible. Also test the actual theta kernel at increasingly high \(x\) and small \(y\). These are **falsification and conjecture discovery tools, not RH verification**. Interval arithmetic can certify finite rectangles, but can never certify all \(x\in\mathbb R\) by itself.

**A5. Stop/continue gate.** If the special modular relation yields no new globally uniform sign information, report that failure explicitly. Do not repeat finite Taylor-cosine minorants as if increasing numerical order could silently solve the all-height obstruction.

**Required deliverable:** a stand-alone lemma with proof from \(\Theta\)'s modular relation to (A), or a precisely described failed step and counterexample. This is the central unsolved item.

### Track B (PARALLEL): find a structural all-orders Toeplitz factorization

**B1.** Re-derive the exact \(a_n\) from theta moments and the xi derivatives, with independent numerical agreement and consistent normalization.

**B2.** Express arbitrary Toeplitz minors in integral/determinantal form where possible. Check whether the special theta structure gives a variation-diminishing kernel, a canonical factorization, or a sign-preserving recurrence valid for **every order**. Avoid confusing Hankel moment total positivity (often automatic for nonnegative measures) with the harder **Toeplitz** total nonnegativity in (C).

**B3.** Track failure of candidate inequalities at higher order and compare them to generic positive kernels and standard PF finite-order examples.

**Required deliverable:** a fully quantified all-minors theorem or an independently proved new infinite family beyond existing finite-order results. Finite tests by themselves cannot certify (C).

### Track C (EXPLORATORY): theta heat deformation / de Bruijn–Newman boundary

For a normalized theta Fourier representation, define

\[
H_\lambda(z)=\int_{\mathbb R}\Phi(u)e^{\lambda u^2}e^{izu}\,du,
\quad
\partial_\lambda H_\lambda=-\partial_z^2H_\lambda.
\]

The classical de Bruijn–Newman constant \(\Lambda\) is the boundary between deformed transforms with exclusively real zeros and those with nonreal zeros. In standard normalization, RH is equivalent to \(\Lambda\le0\), while Rodgers–Tao proved \(\Lambda\ge0\); consequently RH is equivalent to \(\Lambda=0\).

This is **another equivalence, not a shortcut**. A substantive result would be a noncircular theorem about how the special theta kernel constrains zero motion at or across \(\lambda=0\). The deformation parameter \(\lambda\) is mathematical, **not Dirac physical time**.

**Required deliverable:** a new checked estimate on heat-flow zero motion at \(\lambda=0\), compared against known de Bruijn–Newman results, or a falsification of the proposed mechanism.

### Track D (INTERPRETIVE): quaternionic translation of an actual analytic result

Translate any independently proved zero-exclusion lemma into the statement that \(\mathcal S_{a,t}\) and \(\mathcal S_{-a,t}\) cannot be distinct. Retain the quartic \((X^2+t^2)^2\) as a *consequence* of \(a=0\); do not use the squared factor as proof that \(a=0\).

The repo's free geometric scale \(L>0\) must remain symbolic. Its scale-family deficiency \(D(L)\) and scale-free defect \(\mathcal E\) from [12](12-symbolic-scale-and-defect.md) are RH-equivalent but **not proved to vanish**.

## 5. Specific next work package and acceptance tests

**First research work package:** an auditable theta-modular obstruction map and uniform-sign lemma search.

1. Build a claim/assumption ledger: every identity from [12–16], its exact hypotheses, an external citation or independently reproducible derivation, and whether it already assumes a statement equivalent to RH.
2. Independently rederive the signed double integral (B) from \(\Phi\); check constants using differentiation and high-precision numerical integration at selected \(x,y\).
3. Write the theta modular transformation and derivative consequences in a normalization-consistent way; identify which identities are genuinely special to the Riemann kernel.
4. Test **one proposed global lower bound** against a smooth positive-kernel counterexample and the actual theta kernel, and explicitly record where the sign argument needs additional arithmetic information.
5. Either prove an incremental lemma valid **uniformly for all heights**, or publish a clear obstruction report stating why the tested idea does not advance the proof.

**Acceptance test for a RH-proof claim:** a formal theorem and complete argument showing (A), (C), or an equivalent exact all-zero spectral property **without assuming the conclusion**, with rigorous treatment of all unbounded parameters; then independent mathematical review. Existing finite-height numerical verifications and near-origin local bounds are not enough.

## 6. Rigor checklist — prohibited shortcuts

- Never infer a zero is fixed by a reflection merely because the set of zeros is reflection-invariant.
- Never infer the critical line from the quartic, its symmetry group, its perfect square **under \(a=0\)**, or the quaternionic lift.
- Never treat the constant \(S^3\) polar radius as a zero-exclusion theorem.
- Never conflate a positive Fourier kernel, a conserved Hilbert-space norm, or self-adjointness of an *overlap* operator with real-zero spectral identification.
- Never infer PF-infinity from any finite matrix order, or positivity for all spectral heights from finite computational ranges.
- Never silently equate \(t\) (spectral height) with physical time or heat parameter \(\lambda\).
- Never treat analytic continuation as still missing: it is classical and already available.
- Keep even a small off-line possibility open until excluded mathematically; a tiny numerical upper bound on a defect is **not zero**.

## 7. Read next: authoritative source and repository lineage

**Official CMI:**
- Enrico Bombieri, *Problems of the Millennium: the Riemann Hypothesis*, https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf (the exact target is on page 1).
- CMI Riemann Hypothesis status, https://www.claymath.org/millennium/Riemann-Hypothesis/

**Equivalent analytic conditions and context:**
- J. Sondow & C. Dumitrescu, *A monotonicity property of Riemann's xi function and a reformulation of the Riemann Hypothesis*, https://arxiv.org/abs/1005.1104.
- C. M. Newman & W. Wu, *Constants of de Bruijn–Newman Type in Analytic Number Theory and Statistical Physics*, Bull. AMS 57 (2020), https://doi.org/10.1090/bull/1668.
- DLMF, Riemann zeta function and zero distribution, https://dlmf.nist.gov/25.10.

**This repository:**
- [08 — theta kernel](08-theta-kernel-zero-latitudes.md)
- [12 — symbolic-scale zero defect](12-symbolic-scale-and-defect.md)
- [13 — local kernel growth](13-theta-kernel-local-growth-certificate.md)
- [14 — higher cosine minorants](14-higher-moment-cosine-certificate.md)
- [15 — signed bilinear growth form](15-higher-moment-growth-certificate.md)
- [16 — two reflections and quaternionic zero-spheres](16-two-fold-zero-spheres-and-theta-positivity.md)

**Project operating principle:** the Clay theorem is the deliverable; quaternionic geometry is an explanatory and hypothesis-generating instrument. An independently proved global analytic restriction on xi zeros, not the beauty of the geometry, decides success.
