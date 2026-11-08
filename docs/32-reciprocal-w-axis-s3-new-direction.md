# 32 — New research direction: reciprocal number line as the scalar coordinate of S³

**Milestone recorded:** 2026-11-08
**Priority:** New geometric research direction for the Riemann-hypothesis program, not a proof of RH.

## Central proposal

Treat the interval \(0<n<1\) as the reciprocal counterpart to \(n>1\), and represent both through the scalar coordinate \(w\) of the unit-quaternion 3-sphere
\[
q=w+xi+yj+zk,\qquad w^2+x^2+y^2+z^2=1.
\]
The reciprocal number line is **not** an extra imaginary unit: \(w\) is a real scalar coordinate; \(i,j,k\) remain the quaternionic imaginary basis.

For \(n>0\), define
\[
t=\log n,\qquad
w(n)=\tanh t=\frac{n^2-1}{n^2+1}.
\]
Then
\[
w(1/n)=-w(n),\quad w(1)=0,\quad
\lim_{n\to0^+}w(n)=-1,\quad\lim_{n\to\infty}w(n)=+1.
\]
Choose a pure unit quaternion \(u=ai+bj+ck\), \(a^2+b^2+c^2=1\), and lift
\[
q(n,u)=w(n)+\sqrt{1-w(n)^2}\,u
=\tanh(\log n)+\operatorname{sech}(\log n)\,u.
\]
This is a point on \(S^3\), with \(q(1,u)=u\) and reciprocal reflection
\[
q(1/n,u)=-\overline{q(n,u)}.
\]
The two ends approach **distinct poles**, \(-1\) and \(+1\). This is different from the earlier Cayley compactification, in which both ends map to the *same* pole \(-1\). Neither model may be silently substituted for the other.

## New exact multiplication law

Let \(a=w(m)\) and \(b=w(n)\). By \(\tanh(A+B)\),
\[
\boxed{w(mn)=a\oplus b:=\frac{a+b}{1+ab}.}
\]
For \(a,b\in(-1,1)\), this is a well-defined commutative associative group operation with identity 0 and inverse \(-a\). It is isomorphic to multiplication of positive reals via \(\operatorname{artanh}\), not ordinary coordinate multiplication. It extends to the poles only partially: \(+1\oplus(-1)\) is undefined (reflecting \(0\cdot\infty\)). The lifted \(q(n,u)\) generally **does not** preserve multiplication under ordinary quaternion multiplication: its phase is \(\arccos(\tanh\log n)\), not additive in \(\log n\). If needed, transport the \(\oplus\) law to the selected meridian rather than claiming quaternion multiplicativity.

## Prime-factorization coordinate

For a positive rational \(r=\prod_p p^{v_p(r)}\), with finitely many nonzero integer valuations,
\[
\operatorname{artanh}w(r)=\log r=\sum_p v_p(r)\log p.
\]
Thus multiplication and division are positive and negative prime-valuation directions in one bounded coordinate. The earlier example \(39.5=79/2\) has \(v_{79}=+1,v_2=-1\) and is prime in the dyadic ring \(\mathbb Z[1/2]\), but not an ordinary prime integer. No new zeta Euler factor at 39.5 is implied.

## Connection to the RH program: hypothesis and tests

The new geometric hypothesis is that this *two-pole* scalar-coordinate model might enable a nontrivial arithmetic/spectral operator using the exact von Mangoldt prime-power measure and the Jacobi-theta kernel, potentially revealing a condition stronger than symmetry alone.

**Do not claim:** the mapping proves RH; scalar coordinate \(w\) is a fourth imaginary unit; an arbitrary \(S^3\) embedding is quaternionic analytic continuation; endpoint matching forces Weil positivity; or the new map is equivalent to the previous shared-pole map.

**Next tests, in order:**
1. Prove algebraic associativity, reciprocal inversion, endpoint behavior and meridian-lift consistency. Compare \(q(mn,u)\) with \(q(m,u)q(n,u)\) to identify the exact non-homomorphism.
2. Map prime powers and von Mangoldt weights through \(w\); identify whether a canonical, measure-preserving or unitary representation exists, rather than inserting weights ad hoc.
3. Transport a rigorously defined test-function space and the **complete** Weil explicit-formula quadratic functional, including archimedean terms, into the bounded coordinate. Check whether this is merely unitary equivalence.
4. Test candidate boundary conditions against the shifted positive-even theta-kernel off-axis-zero negative control from Chapter 24, and the raw Mangoldt pole obstruction from Chapter 31.
5. Pursue a genuinely new arithmetic-specific operator inequality only if it adds information beyond the original complex formula. No circular assumption of RH or positivity.

## Relationship to prior work

- Chapter 04: shared-pole Cayley compactification and smooth completed-xi return.
- Chapters 24, 29–31: sharp quaternionic Jensen obstruction; odd-prime theta identity; Weil reciprocal Mangoldt pairing; failure of boundary matching alone.
- This chapter intentionally changes geometry to a **distinct two-pole \(w\)-axis** and prioritizes deriving its precise algebraic composition law before any new spectral claims.

**Milestone:** reciprocal number-line geometry has an exact, associative multiplication law on the scalar coordinate of the unit-quaternion sphere. Whether it offers an independent RH constraint remains an open research question.
