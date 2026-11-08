# 33 — Reciprocal k-axis and the exact multiplicative group law

**Date:** 2026-11-08. **Status:** Exact algebraic result and limitations; no RH proof.

## Corrected geometric choice

The reciprocal number line need not be the real scalar \(w\)-axis. Use the imaginary quaternion \(k\) as the bounded coordinate:
\[
a(n)=\tanh(\log n)=\frac{n^2-1}{n^2+1},\quad
q(n)=\sqrt{1-a(n)^2}+k a(n)=\operatorname{sech}(\log n)+k\tanh(\log n).
\]
Here \(q(n)\in S^3\), lies on the positive-real semicircle of the \(w\)-\(k\) plane, \(q(1)=1\), \(q(1/n)=\overline{q(n)}\), and the distinct limiting poles are \(q(0^+)=-k\) and \(q(+\infty)=+k\). Neither endpoint is attained at finite \(n>0\). The \(k\)-axis is a geometric coordinate, not an additional imaginary basis beyond \(i,j,k\).

## Exact multiplication on reciprocal coordinates

For \(a,b\in(-1,1)\), define
\[
a\oplus b=\frac{a+b}{1+ab}.
\]
The denominator is positive. Since \(\operatorname{artanh}(a\oplus b)=\operatorname{artanh}a+\operatorname{artanh}b\), the law is associative and commutative, has identity \(0\) and inverse \(-a\). Moreover
\[
a(mn)=a(m)\oplus a(n),\quad a(1/n)=-a(n).
\]
Thus \((\mathbb R_{>0},\times)\cong((-1,1),\oplus)\). The coordinate operation is the standard hyperbolic-tangent addition formula, not a new arithmetic theorem.

For points on the selected meridian \(M=\{\sqrt{1-a^2}+ka:-1<a<1\}\), define \(q(a)\star q(b)=q(a\oplus b)\). This is an exact group law on \(M\), transported from multiplication, but **not** ordinary quaternion multiplication.

For example \(a(2)=3/5\), \(a(4)=15/17\). Ordinary quaternion multiplication gives
\[
q(2)^2=(4/5+3k/5)^2=7/25+24k/25,
\]
whereas
\[
q(4)=8/17+15k/17.
\]
These differ. The transported law correctly gives \(q(2)\star q(2)=q(4)\).

## Why a simple quaternion homomorphism is insufficient

The alternative \(U_\kappa(n)=\exp(k\kappa\log n)\) obeys \(U_\kappa(mn)=U_\kappa(m)U_\kappa(n)\) under ordinary quaternion multiplication, but is periodic in \(\log n\), so is not injective on all positive reals for any \(\kappa\ne0\). Thus the compact bounded meridian coordinate gives an injective representation at the cost of transporting the group operation. The original quaternion product gives a continuous homomorphism but loses global injectivity.

The two limiting poles do not form a group extension: the would-be composition \(+1\oplus(-1)\) is undefined, reflecting the indeterminate product \(\infty\cdot0\).

## Prime-power structure

For any positive rational \(r=\prod_p p^{v_p(r)}\),
\[
\operatorname{artanh}a(r)=\sum_p v_p(r)\log p,\quad
a(r)=\bigoplus_p [v_p(r)]_{\oplus}a(p).
\]
This retains exact prime-factorization coordinates, but the scalar \(a(r)\) alone does not provide a *linear* separation of prime valuations without applying \(\operatorname{artanh}\).

The original research example \(39.5=79/2\) is a prime element in \(\mathbb Z[1/2]\), with \(v_{79}=1\) and \(v_2=-1\). It is not an extra ordinary-prime index or Euler factor.

## Critical test for Riemann research

Under the change of variable \(a=\tanh t\), the Haar measure \(dt\) on additive logarithmic coordinates becomes \(da/(1-a^2)\). Consequently, the map
\[
(\mathcal U f)(a)=(1-a^2)^{-1/2} f(\operatorname{artanh}a)
\]
is unitary from \(L^2(\mathbb R,dt)\) to \(L^2((-1,1),da)\). Conjugating an existing operator by \(\mathcal U\) preserves its spectrum and positivity; a coordinate transformation alone cannot prove Weil positivity or RH.

The next nontrivial step must define an **independently justified** operator on the \(k\)-axis (not just a conjugation of the classical Weil functional) with the exact von Mangoldt and archimedean coefficients, and prove a new positivity property. Test it against the off-axis-zero negative control from Chapter 24 and the raw-prime boundary obstruction from Chapter 31.

**Conclusion:** The reciprocal \(k\)-axis multiplication law works exactly. The new geometric choice is mathematically sound, but does not yet impose new zero constraints.
