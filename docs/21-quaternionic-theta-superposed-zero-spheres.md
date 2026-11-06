# 21 — Quaternionic theta continuation and superposed zero-sphere proof program

**Date:** 2026-11-06  
**Priority:** Primary proof-development tool: quaternionic slice-regular continuation of the completed Riemann xi function, with its reflected spherical zeros treated as a *coupled geometric system*.  
**Status:** Exact analytic and geometric identities, a sharp proof obligation, a generic-function no-go example, and a proposed four-dimensional Jensen route. **NOT an RH proof.**

**User's hypothesis (preserve accurately):** The intended argument is *not* "two reflection symmetries alone imply RH." Instead, investigate whether the **superposition / folding of reflected quaternionic zero-spheres**, applied to the **particular Riemann xi function and Jacobi-theta kernel**, creates a positive or conserved constraint that forces the reflected spheres to occupy the same critical hyperplane.

This note supersedes the use of the two complex channels as the primary model. The two-channel phase/Wronskian tests in [18–20](19-folded-channel-inward-deformation-and-wronskian.md) remain useful diagnostics. Clay's target from [17](17-clay-statement-and-proof-roadmap.md) is unchanged.

## 1. The exact quaternionic analytic continuation, not a metaphor

Use the usual entire completed Riemann xi function

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

and its centered even real-coefficient entire function

\[
f(w)=\xi(\tfrac12+w)=\sum_{n\ge0}c_nw^{2n},\qquad c_n\in\mathbb R.
\]

Define the canonical **intrinsic slice-regular** quaternionic lift by the same power series:

\[
\boxed{\mathcal X(q)=\sum_{n\ge0}c_nq^{2n},\quad q\in\mathbb H.}
\tag{Q1}
\]

This is a four-**real**-dimensional continuation of an existing entire function. It is not automatically a holomorphic function of two complex variables and supplies no extra independent zero-location data by itself (slice representation theorem).

Let \(\Phi(v)\) be the standard, positive, even Jacobi-theta xi kernel used in [08](08-theta-kernel-zero-latitudes.md), so \(\Xi(z)=\xi(\tfrac12+iz)=2\int_0^\infty\Phi(v)\cos(zv)dv\). Then the entire lift has the **direct quaternionic theta-integral formula**

\[
\boxed{\mathcal X(q)=2\int_0^\infty\Phi(v)\cosh(qv)\,dv.}
\tag{Q2}
\]

Here \(\cosh(qv)=\sum_{n=0}^\infty q^{2n}v^{2n}/(2n)!\), with scalar real \(v\). Superexponential decay of \(\Phi\) justifies uniform convergence on compact \(q\)-sets, termwise integration, and the equality with (Q1). On any complex slice \(\mathbb R+I\mathbb R\), (Q2) is the ordinary centered completed xi function under the identification \(I\leftrightarrow i\).

For \(a,t\in\mathbb R\), \(t>0\), and an arbitrary **unit imaginary quaternion** \(u^2=-1\),

\[
\cosh((a+ut)v)=\cosh(av)\cos(tv)+u\sinh(av)\sin(tv).
\]

Hence

\[
\boxed{\mathcal X(a+ut)=2[C(t,a)+uS(t,a)]}
\tag{Q3}
\]

with exact real scalar channel integrals

\[
C(t,a)=\int_0^\infty\Phi(v)\cos(tv)\cosh(av)\,dv,\qquad
S(t,a)=\int_0^\infty\Phi(v)\sin(tv)\sinh(av)\,dv.
\tag{Q4}
\]

**Coordinate warning:** the earlier \(\Xi(t+ia)=2[C(t,a)-iS(t,a)]\) uses the opposite sign in the centered \(w\)-coordinate, because \(s=\tfrac12+i(t+ia)=\tfrac12-a+it\). No physical time is being introduced.

## 2. Spherical zero-sets and the two mirror folds

Every quaternion \(q=a+ut\) belongs to the conjugacy-class sphere

\[
\mathcal S_{a,t}=\{a+ut:u\in S^2,\ u^2=-1\}.
\]

Since \(\mathcal X\) is intrinsic (its power-series coefficients are real), it is **slice preserving**, and the vanishing of (Q3) is independent of the orientation \(u\):

\[
\boxed{\mathcal X(a+ut)=0
\iff C(t,a)=S(t,a)=0.}
\tag{Q5}
\]

The simultaneous vanishing produces an entire \(S^2\) zero-sphere, not just a single point. Both the complex-conjugation and functional-reflection symmetries of xi then guarantee the reflected sphere \(\mathcal S_{-a,t}\).

Importantly, **unit quaternion conjugation preserves real part**:

\[
r(a+ut)r^{-1}=a+(rur^{-1})t,\qquad |r|=1.
\tag{Q6}
\]

It rotates the *orientation* on one \(S^2\) but cannot map the sphere centered at \(+a\) to that centered at \(-a\) unless \(a=0\). The functional reflection is a **different symmetry** from an \(SU(2)\) inner rotation.

Thus

\[
\boxed{\mathcal S_{a,t}=\mathcal S_{-a,t}\iff a=0.}
\tag{Q7}
\]

This is the exact geometric form of the desired fold. RH asserts that every nontrivial zero-sphere is already on this centered slice.

## 3. Mathematically define "superposition of reflected spheres"

For fixed \(u\), xi evenness and real coefficients give

\[
\mathcal X(-a+ut)=\mathcal X(a-ut)=\overline{\mathcal X(a+ut)}.
\]

Define the symmetric and antisymmetric **reflected field amplitudes**

\[
\Psi_{\mathrm{even}}(a,t;u)
=\frac{\mathcal X(a+ut)+\mathcal X(-a+ut)}2=2C(t,a),
\]

\[
\Psi_{\mathrm{odd}}(a,t;u)
=\frac{\mathcal X(a+ut)-\mathcal X(-a+ut)}2
=2uS(t,a).
\tag{Q8}
\]

This is a *rigorously defined* superposition of **function values**, not literally an addition of geometric subsets or a physical quantum state.

For normalized rotation-invariant measure \(d\omega(u)\) on the imaginary unit sphere \(S^2\), set

\[
\mathrm{Mean}(a,t)=\int_{S^2}\mathcal X(a+ut)\,d\omega(u)=2C(t,a),
\]

\[
\mathrm{Variance}(a,t)
=\int_{S^2}|\mathcal X(a+ut)-\mathrm{Mean}(a,t)|^2\,d\omega(u)
=4S(t,a)^2.
\tag{Q9}
\]

The quaternionic Pythagorean identity is then

\[
\boxed{
\int_{S^2}|\mathcal X(a+ut)|^2\,d\omega(u)
=|\mathrm{Mean}(a,t)|^2+\mathrm{Variance}(a,t)
=4[C(t,a)^2+S(t,a)^2].
}
\tag{Q10}
\]

The whole spherical orbit has the **same modulus**, so averaging is not secretly independent data: (Q10) equals the complex \(|f(a+it)|^2\). Scalar and imaginary components are orthogonal under the real Euclidean norm. They cannot cancel each other; a spherical zero requires both to vanish.

At \(a=0\), \(S(t,0)=0\) for every \(t\). As \(a\to0\), the normalized spherical variance obeys

\[
\mathrm{Variance}(a,t)
=a^2\left[\int_0^\infty 2v\Phi(v)\sin(tv)\,dv\right]^2+O(a^4)
=a^2[\Xi'(t)]^2+O(a^4),
\tag{Q11}
\]

with real \(\Xi'(t)\) and uniformity on compact real-height intervals. This exact local consequence of (Q2) links the imaginary-orientation spread to the spectral slope at the fold.

### First caution: folding does not itself force zero-spheres to coincide

At an **off-fold** zero, \(C=S=0\), so *both* reflected field values and both parity projections in (Q8) vanish. This is not a contradiction: superposing mirrored function values automatically vanishes at either member of an off-fold zero pair. To exclude the pair, one needs an **independently justified theorem** enforcing geometric coincidence (Q7), not simply the fact that their values can be superposed.

A bare symmetry counterexample is the intrinsic even quaternionic polynomial

\[
p(q)=q^4+4.
\]

For every \(u^2=-1\),

\[
(1+u)^2=2u,\qquad (1+u)^4=-4,
\]

so \(p(1+u)=0\). Equally \(p(-1+u)=0\). Thus the polynomial has distinct reflected spherical zero sets \(\mathcal S_{\pm1,1}\), even though it has every parity, conjugation, and spherical-orbit feature in (Q5)–(Q10).

**This refutes a generic mathematical claim that quaternionic continuation or superposition alone implies the fold.** It does **not** refute a *theta-specific* theorem for the actual Riemann xi function.

## 4. Distinguish the quartet's doubled orbit polynomial from actual zero multiplicity

Let \(\delta=a>0\), \(\gamma=t>0\). The real-coefficient spherical factor for a zero-sphere centered at \(a\) is

\[
\Delta_{a,t}(q)=q^2-2aq+(a^2+t^2).
\]

Its distinct reflected sphere has factor \(\Delta_{-a,t}(q)\), giving the quartet factor

\[
\boxed{
\Delta_{a,t}(q)\Delta_{-a,t}(q)
=[q^2+a^2+t^2]^2-4a^2q^2.
}
\tag{Q12}
\]

If one *formally* sets \(a=0\) in this **four-root bookkeeping polynomial**, it becomes \((q^2+t^2)^2\). This does **NOT** establish that the original xi function has a double zero on the critical line: the off-line quartet collapses to a **single conjugate pair**, and in the actual xi product the factor \(q^2+t^2\) is counted according to the true multiplicity, which could be one.

No **actual noncommutative mixing** occurs in (Q12), since the spherical factors have real coefficients and commute. If a proposed proof requires a new quaternionic coupling that cannot be expressed on a complex slice, the extra operator or constraint must be defined explicitly, and its effect on the true xi zero set must be proved.

## 5. Primary proposed proof route: four-dimensional Jensen / spherical zero measure

We now make **quaternionic continuation the primary analytical workspace** instead of treating it only as a final visualization.

Existing mathematics supplies quaternionic Jensen formulas for slice-regular functions. Such formulas relate spherical means of \(\log|\mathcal X|\), derivatives of the function, and *weighted contributions of its spherical zeros*. They provide a rigorous way to distinguish the distribution of true \(S^2\) zero sets from point zeros of a complex restriction.

**New research target (unproved):** Starting from the *specific* quaternionic theta integral (Q2), derive a nonnegative sphere-separation defect whose vanishing is forced by an independently established theta-specific identity or inequality. The desired conclusion is that its zero-divisor measure is supported on the centered slice \(a=0\).

More formally, seek a theorem of the form

\[
\boxed{
\Phi=\Phi_{\mathrm{Riemann\ theta}}\quad\Longrightarrow\quad
\mathcal X(q)=0\ \Longrightarrow\ \Re q=0
}
\tag{Q13: OPEN}
\]

where **the implication must be derived from a new intermediate inequality or 4D Jensen identity**, not inserted as a disguised assumption. Proving (Q13) would prove RH.

Candidate sequence:

1. **Rigorous spherical Jensen audit.** Express \(\mathcal X(q)\) using (Q2), verify global slice regularity, compute the spherical zero divisor and trace/variance (Q9), and apply a published four-dimensional Jensen formula to the correct normalization. Track all boundary and derivative terms. Do not infer sign or zero exclusion from Jensen's formula without separately proving them.
2. **A theta-specific spherical coupling estimate.** At a hypothetical trace zero \(C(t,a)=0\), look for a rigorously derived lower bound \(\mathrm{Variance}(a,t)>0\) for every \(a>0\) in the critical strip and all heights. This is RH-equivalent, so a genuine proof must supply a *new mechanism*, e.g. a special modular/prime-arithmetic decomposition or a positive quaternionic operator acting on both mirror sheets. Generic positive kernels and \(q^4+4\) must not satisfy that mechanism.
3. **Spherical zero-count audit.** Compare any new Jensen-type zero-distribution expression with the scale-free Hadamard exhaustion defect \(\mathcal E\) in [12](12-symbolic-scale-and-defect.md). That defect is **already RH-equivalent**, so showing that another zero-counting formula equals \(\mathcal E\) does not prove it vanishes. Search specifically for additional structure producing an unconditional equality or nonnegative term that must be zero.
4. **Four-real-dimensional numerical probes.** Visualize spherical zero sets and evaluate trace, variance, and Jensen residuals for the true theta function and explicit counterexamples on finite height windows. Independent complex-slice checks must match; finite numerical absence of off-fold spheres is not proof.
5. **Novel coupling gate.** Before claiming quaternionic superposition has added mathematical force, identify a statement not already equivalent to the original complex slice representation. Show it follows from the actual theta kernel and fails for the generic off-axis-sphere example.

### What counts as meaningful progress?

- An unconditional, **nontrivial theta-specific** inequality constraining a 4D spherical zero measure beyond the generic Jensen formula.
- A rigorously defined quaternionic operator with a new provable sign or spectral property, not simply a rewrite of the complex product.
- An explicit counterexample to one proposed coupling principle, allowing the program to reject a false proof.
- A first independently verified new theorem on an *unbounded* domain that can be used in an all-height argument.

**What does not count:** geometric identification of two distinct sets by declaration, a repeated factor in a symmetry polynomial, the fact that \(S^2\) or \(S^3\) has rotational symmetry, or successful finite numerical scans.

## 6. Relation to the existing \(S^3\) mapping and Dirac analogy

The repo's global inverse-stereographic map \(Q_L(t,u)\in S^3\) with symbolic scale \(L>0\) parameterizes the full **critical-line coordinate**, not just zeros. The spherical zero-divisor sets \(\mathcal S_{a,t}\cong S^2\) of the *different* slice-regular extension \(\mathcal X(q)\) are therefore not automatically the same as the \(S^2\) **latitudes** inside that unit \(S^3\). Keep both geometries explicitly defined, and do not assert that a new spectrum is introduced by changing coordinate \(L\).

The Dirac/spinor comparison motivates phase-sensitive operators, but neither the \(SU(2)\) double cover nor a 720-degree sign change is a proven property that pins the zeta spectrum to the critical fold.

## 7. Sources and prior work

- Clay Mathematics Institute, official status and Bombieri's problem statement: https://www.claymath.org/millennium/Riemann-Hypothesis/
- Colombo, Gentili, Sabadini & Struppa (2009), *Extension results for slice regular functions of a quaternionic variable*, Advances in Mathematics 222, 1793–1808, DOI https://doi.org/10.1016/j.aim.2009.06.015.
- G. Gentili et al., zero-sphere structure for slice-regular functions: https://doi.org/10.1016/j.aim.2012.05.023.
- A. Altavilla & C. Bisi (2019), *Log-biharmonicity and a Jensen formula in the space of quaternions*, Ann. Acad. Sci. Fenn. Math. 44, 805–839, https://www.acadsci.fi/mathematica/Vol44/vol44pp0805-0839.pdf.
- A. Perotti (2020), *A four dimensional Jensen formula*, Riv. Mat. Univ. Parma 11, 139–152, https://www.rivmat.unipr.it/vols/2020-11-1/07-perotti.html.
- Previous RQM: [12 — scale-free defect](12-symbolic-scale-and-defect.md), [16 — two spherical zero sets](16-two-fold-zero-spheres-and-theta-positivity.md), [17 — Clay target](17-clay-statement-and-proof-roadmap.md), [18 — mirror superposition](18-mirror-channel-folding-and-zero-collision.md), [19 — inward phase test](19-folded-channel-inward-deformation-and-wronskian.md), [20 — Jensen obstacle](20-inward-fold-normal-form-flux-and-jensen-obstruction.md).

**Bottom line:** Quaternionic continuation can be the main *proof-development language* and the reflected spherical divisor the primary geometric object. But it will constitute a proof only after a new, independently derived property of the actual theta kernel forces every spherical zero to lie on the centered fold \(a=0\). At present the exact four-dimensional formulas are a framework, not the missing theorem.
