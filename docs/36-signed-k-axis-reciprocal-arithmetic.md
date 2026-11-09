# 36 — Signed k-axis reciprocal arithmetic, without forced S³ compactification

**Date:** 2026-11-08. **Status:** Exact algebraic construction; no RH proof.

## Proposed correction

Let \(k^2=-1\). Embed positive real multiplicative arithmetic in the **entire signed imaginary k-axis** of quaternion space:
\[
K(n)=k\log n,\qquad n>0.
\]
Then \(K(mn)=K(m)+K(n)\), \(K(m/n)=K(m)-K(n)\), and \(K(1/n)=-K(n)\). The image is the whole line \(\mathbb R k\), with \(K(1)=0\). This is an injective group isomorphism \((\mathbb R_{>0},\times)\cong(\mathbb R k,+)\).

**Crucial distinction:** the quaternionic origin \(K(1)=0\) represents numerical *one*, not numerical zero. A multiplicative-to-additive homomorphism must map the identity 1 to the additive identity 0. The original number zero has no multiplicative inverse and is not in the domain. \(n\to0^+\) corresponds to unbounded \(-k\) direction; \(n\to\infty\) to unbounded \(+k\). Neither is a finite quaternion.

The real \(w\) and imaginary \(k\) axes have the same ambient origin, but the unit 3-sphere \(w^2+x^2+y^2+z^2=1\) excludes that origin. This construction lives in \(\mathbb H\), **not** on \(S^3\), unless a further map is introduced.

## Relation to Chapter 33

Chapter 33 uses the bounded coordinate \(a(n)=\tanh(\log n)\) and \(a(mn)=(a(m)+a(n))/(1+a(m)a(n))\). Here \(K(n)=k\operatorname{artanh}(a(n))\). These are exactly equivalent coordinate descriptions; the signed unbounded axis eliminates the nonlinear coordinate law and the artificial endpoint identification. Neither creates new arithmetic information.

A shifted representation \(1+k\log n\) keeps unity at the quaternion 1, but is not multiplicative under ordinary quaternion multiplication. The exponential \(e^{k\log n}\) *is* multiplicative, but periodic and noninjective. These tradeoffs cannot be ignored.

## Prime valuations and von Mangoldt weights

For any positive rational \(r=\prod_p p^{v_p(r)}\), \(K(r)=k\sum_p v_p(r)\log p\). In particular
\[
K(79/2)=k(\log79-\log2)=k\log39.5.
\]
The rational \(39.5=79/2\) remains prime in \(\mathbb Z[1/2]\); 79, not 39.5, is the conventional prime index in the von Mangoldt formula.

The von Mangoldt distribution in the log coordinate \(t\) is supported on \(\log(p^j)=j\log p\), with weights \(\Lambda(p^j)=\log p\). Its reciprocal reflection is at \(-j\log p\). On the signed k-axis these are simply opposite positions. This is a faithful pushforward of existing arithmetic, not a new operator or a zero-exclusion condition.

## Tests and next gate

The associated Python script verifies multiplication, inversion, mixed rational prime valuations, and the failure of ordinary quaternion multiplication for the shifted representation. It also verifies that normalizing \(1+k\log n\) onto \(S^3\) changes the operation.

The next meaningful gate is not coordinate algebra: derive an independently motivated quaternionic *operator* with noncommuting directions and full completed Weil coefficients, then test against the Chapter 24 off-axis-zero control. The signed k-axis itself is a real one-dimensional subgroup of the **additive** quaternion algebra and cannot generate noncommutativity by itself.

**Verdict:** The signed k-axis is algebraically cleaner and respects the user's distinction between \(+k\) and \(-k\). It does not, on its own, add a new RH constraint.
