# 32 — Arithmetic-sensitive quaternionic pole operator: construction, discriminator, and no-go result

**Date:** 2026-11-08  
**Question:** Can a quaternionic boundary operator whose coefficients are the true von Mangoldt weights distinguish the original Riemann theta kernel from the Chapter 24 positive-even off-axis-zero control *and* force the complete Weil positivity criterion?  
**Status:** A rigorous arithmetic discriminator and a bounded nonlocal positive quaternionic operator are constructed. **The discriminator succeeds; the positive operator fails as an RH selector. No RH proof.**

**Context:** [24](24-sharp-angular-saturation-audit.md), [30](30-reciprocal-mangoldt-weil-positivity.md), [31](31-mangoldt-shared-pole-boundary-test.md). Do not replace ordinary xi with a modified function when making claims about RH.

## 1. The scalar analytic arithmetic discriminator

Let \(G(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\), so \(\xi(s)=G(s)\zeta(s)\). On the zero-free half-plane \(\Re s>1\) define for a candidate entire completed function \(F(s)\), when \(F/G\ne0\),
\[
\mathscr R_F(s)
=-\frac{d}{ds}\log\left(\frac{F(s)}{G(s)}\right)
-\sum_{n=2}^\infty\frac{\Lambda(n)}{n^s}.
\tag{32.1}
\]
Here \(\Lambda(p^k)=\log p\) and is otherwise zero. The series converges absolutely for \(\Re s>1\). The standard Euler product proves \(\mathscr R_\xi(s)=0\) throughout that half-plane. This is an arithmetic fidelity check, not a new theorem about zeros.

The Chapter 24 controlled alternative is
\[
F_\epsilon(s)=\xi(s)K(s),\qquad
K(s)=1+c\cosh(s-\tfrac12),\qquad c=0.98.
\]
Its extra off-critical zeros are \(s=\frac12\pm b+i(2k+1)\pi\), where \(b=\operatorname{arcosh}(1/c)\approx0.201688487798836\in(0,\frac12)\). These are zeros of \(F_\epsilon\), **not** of xi. For \(\Re s>1\), \(K\) has no zero and
\[
\boxed{
\mathscr R_{F_\epsilon}(s)
=-\frac{c\sinh(s-\tfrac12)}
{1+c\cosh(s-\tfrac12)}.}
\tag{32.2}
\]
At \(s=2\), this is approximately \(-0.63130580865129819\), versus precisely 0 for \(\xi\). Consequently, exact prime-power arithmetic detects the control's deformation.

**Uniqueness/no new theorem.** If \(\mathscr R_F(s)=0\) on a connected open subset of \(\Re s>1\), then \((F/G)'/(F/G)=\zeta'/\zeta\). Hence \(F/G=C\zeta\) there and by analytic continuation \(F=C\xi\), when candidate analyticity assumptions allow. Normalization fixes \(C=1\). Thus exact arithmetic fidelity already singles out the *known* Riemann function and says nothing new about whether its zeros all lie on the line. Checking a finite set of s-values does not establish the analytic identity.

The prime 79 contributes \(\Lambda(79)79^{-s}=(\log79)79^{-s}\). The user's precise arithmetic goal \(39.5=79/2\) is **true as a prime element of \(\mathbb Z[1/2]\)**. It is not an additional Euler factor or a shift of the logarithmic frequency to \(\log39.5\).

## 2. A true quaternionic Hilbert-space, arithmetic-weighted operator

Let \(\mathscr H=L^2(\mathbb R,\mathbb H)\), the right quaternionic Hilbert space. Let \(U_a f(t)=f(t+a)\) be the unitary right-linear translation by \(a\). For any fixed \(\sigma>1\) set
\[
a_n=\Lambda(n)n^{-\sigma}\ge0,\qquad
\boxed{
D_\sigma=\sum_{n=2}^\infty a_n(2I-U_{\log n}-U_{-\log n}).}
\tag{32.3}
\]
Since \(\sum_n a_n=-\zeta'(\sigma)/\zeta(\sigma)<\infty\) and \(\|2I-U_a-U_{-a}\|\le4\), the series converges in operator norm. Each \(U_{-\log n}=U_{\log n}^*\), so \(D_\sigma\) is bounded and self-adjoint. For all \(f\in\mathscr H\),
\[
\boxed{\langle f,D_\sigma f\rangle
=\sum_{n=2}^\infty a_n\|U_{\log n}f-f\|_{L^2}^2\ge0.}
\tag{32.4}
\]
The sum is real despite quaternion-valued f. On each fixed imaginary quaternionic slice, the Fourier multiplier is
\[
m_\sigma(\tau)=2\sum_{n=2}^\infty a_n[1-\cos(\tau\log n)]\ge0.
\tag{32.5}
\]
At the one-prime truncation \(n=2\), \(\sigma=2\), \(\tau=\pi/\log2\), its value is **exactly** \(\log2\).

**Crucial counterexample to usefulness:** (32.4) is true for *every* quaternion-valued \(L^2\) function. Both \(t\mapsto\Xi(t)=\xi(\frac12+it)\) and \(t\mapsto\Xi(t)[1+0.98\cos t]\) are square-integrable, and therefore both satisfy the same nonnegative quadratic-form inequality, even though the second has explicit off-axis zeros. Hence (32.4) is *not* Weil's RH-equivalent positivity. A quaternionic positive operator has been built; **it cannot distinguish the two candidates by its positivity**.

The translations are commuting; the operator is a direct quaternionic Hilbert extension of a real scalar convolution operator. No new noncommutative four-dimensional coupling follows from making its domain quaternion-valued.

## 3. Move the operator to the shared Cayley pole

Fix \(L>0\) and \(u^2=-1\). Compactify \(t\in\mathbb R\) via \(t=L\tan(\theta/2)\), \(-\pi<\theta<\pi\), with unit quaternion \(e^{u\theta}\). The two ends \(\theta\to\pm\pi\) represent the same pole \(-1\). The change of variables gives \(dt=(L/2)\sec^2(\theta/2)d\theta\). Thus the map
\[
(J_L f)(\theta)=f(L\tan(\theta/2))
\]
is unitary from \(L^2(\mathbb R,dt;\mathbb H)\) to \(L^2((-\pi,\pi), (L/2)\sec^2(\theta/2)\,d\theta;\mathbb H)\). The conjugate operator \(D_\sigma^{(L)}=J_LD_\sigma J_L^{-1}\) is therefore again bounded, self-adjoint and nonnegative.

Its shifts act nonlocally as
\[
\theta\longmapsto
2\arctan\left(\tan(\theta/2)+\frac{\log n}{L}\right).
\]
These preserve the common pole but impose **no independent boundary-value matching**: \(L^2\) functions need not have endpoint limits. The true and perturbed completed fields do have smooth infinitely flat limits (Chapter 31), so even imposing that separate condition cannot select RH.

The parameter \(L\) is an arbitrary coordinate scale. Conjugating by \(J_L\) cannot change the spectrum or create positivity absent in \(D_\sigma\).

## 4. Distinguishing data vs proving Weil positivity

The arithmetic residual \(\mathscr R\) *does* discriminate between \(\xi\) and the off-axis negative control, but it does so by **enforcing the original Euler product**. The positive jump operator \(D_\sigma\) has clean two-sided quaternionic geometry but is positive universally. Combining “\(\mathscr R=0\)” with “\(D_\sigma\ge0\)” recovers the original xi function together with a tautological inequality; this does **not** imply RH.

The classical Weil positivity form includes prime terms **and** archimedean Gamma and pole terms and is RH-equivalent under its full test-function hypotheses and sign conventions. Dropping or replacing those pieces with the positive jump energy changes the mathematical question. A proof requires a genuinely new global inequality for the *complete* Weil form, not positivity of (32.4).

## 5. Decision, falsification result and next research gate

| Candidate | Genuine xi | Positive-even control with extra off-line zeros | Selects RH? |
|---|---:|---:|---|
| Smooth matching at shared pole | Pass | Pass | No |
| Quaternionic \(D_\sigma\ge0\) | Pass | Pass | No |
| Exact Mangoldt logarithmic-derivative identity \(\mathscr R=0\) | Pass | Fail | Only enforces identity of candidate with xi; not RH |
| Complete Weil positivity for all admissible functions | Equivalent to RH | Fails as a zero-form criterion for off-line roots | Remains unproved for xi |

**New useful methodological gate:** Every proposed quaternionic prime-boundary operator must (i) reduce to the exact full Weil expression or prove a genuinely new comparison to it, (ii) reject the analytic negative control by its *zero-sensitive positivity* rather than solely by an Euler-product identity, and (iii) establish the sign for all admissible tests, all heights. Generic positive jump operators and finite-value arithmetic checksum tests cannot satisfy the gate.

**Bottom line:** exact von Mangoldt arithmetic recognizes the real zeta function, but the natural quaternionic reciprocal-boundary operator does not supply the missing RH positivity theorem. This is an explicit mathematical no-go result for this operator class, not a no-go for all future arithmetic/quaternionic strategies.

## References

- Chapter 24, original theta and positive-even off-axis negative control.
- Chapter 30, Weil criterion and paired von Mangoldt distribution.
- Chapter 31, smooth shared-pole matching obstruction.
- Jeffrey C. Lagarias, *The Riemann Hypothesis: Arithmetic and Geometry*, Theorem 3.2 (Weil positivity), https://dept.math.lsa.umich.edu/~lagarias/doc/mt-holyoke-rev.pdf
- Weil's explicit formula and positivity details, https://openmaths.org/courses/NT-EXPF/NT-EXPF-04.html
