# 26 — Two-sided harmonic arithmetic, fractional primes, and the quaternionic no-go theorem

**Date:** 2026-11-08
**Objective:** retain the user's target that 39.5 be rigorously prime, while studying multiplication outward from 1 and division inward toward 0 as complementary number-line constructions.

## A. Two distinct algebraic systems

**Reciprocal monoid:** \(M_-=\{1/n:n\in\mathbb N_{>0}\}\) with ordinary multiplication and identity 1. Its irreducibles are precisely \(1/p\) for integer primes \(p\): \(1/n=(1/a)(1/b)\iff n=ab\). Every \(1/n\) has unique factorization into reciprocal primes. Note that \(M_-\) is a *monoid*, not a ring (not closed under addition).

**Dyadic ring:** \(A=\mathbb Z[1/2]\) with units \(\{\pm2^k:k\in\mathbb Z\}\). Every nonzero nonunit is, up to a unit, a product of odd rational primes. Thus \(79/2=39.5\) is a prime element: \(A/(79/2)\cong\mathbb F_{79}\). Conversely \(39=3\cdot13\) is composite. In \(A\), \(1/79\) is not an element.

These two systems cannot simply be merged while keeping 79 (and hence 39.5) prime: **if a unital ring contains both 79 and 1/79, then 79 is a unit**; if it also contains 1/2, then 39.5 is a unit. Units are not prime elements. This is a precise obstruction to demanding all reciprocal primes and 39.5 simultaneously be prime in one ring under ordinary multiplication. A monoid or graded/multisorted construction can keep distinct prime notions, but must label them.

## B. One harmonic coordinate for both directions

For positive real \(x\), define \(t=\log x\). Then \(x=n\) corresponds to \(t=\log n\), while \(x=1/n\) corresponds to \(t=-\log n\). The involution \(x\leftrightarrow1/x\) becomes \(t\leftrightarrow-t\).

Fix \(L>0\) and a unit imaginary quaternion \(u^2=-1\). The compactified Cayley coordinate
\[
Q_L(x,u)=\frac{L+u\log x}{L-u\log x}
=\cos(2\arctan(\log x/L))+u\sin(2\arctan(\log x/L))
\]
satisfies \(|Q_L|=1\), \(Q_L(1/x,u)=\overline{Q_L(x,u)}\), and \(Q_L(1,u)=1\). The two tails \(x\to0^+\) and \(x\to+\infty\) meet at the compactified pole \(-1\). This is exact coordinate geometry, not a new prime theorem. The map is generally **not** multiplicative: \(Q_L(xy)\ne Q_L(x)Q_L(y)\).

A multiplicative alternative is \(U_\kappa(x,u)=\exp(u\kappa\log x)\), for \(\kappa\in\mathbb R\). It obeys \(U_\kappa(xy)=U_\kappa(x)U_\kappa(y)\) and \(U_\kappa(1/x)=\overline{U_\kappa(x)}\), but is not injective globally because angles are periodic. Both constructions use a fixed complex slice and do not introduce independent quaternionic noncommutative arithmetic.

**Commutativity obstruction:** the image of a commutative multiplicative system under any multiplicative map into nonzero quaternions must consist of mutually commuting quaternions. A nonreal commuting family lies in a common complex slice. Therefore assigning independent noncommuting quaternionic axes to primes cannot preserve the ordinary multiplication law without changing the operation or abandoning homomorphism.

## C. Analytic bridge and negative controls

For \(\Re s>1\), Euler's product reindexed by odd dyadic prime representatives \(x=p/2\) is
\[
\zeta(s)=(1-2^{-s})^{-1}\prod_{x=p/2,\ p\ {\rm odd\ prime}}(1-(2x)^{-s})^{-1}.
\]
The factor \(2^{-s}\) is mandatory. This is reindexing, not a new continuation or proof about zeros.

The reciprocal prime Dirichlet series \(P(s)=\sum_p p^{-s}\) converges for \(\Re s>1\), whereas \(\sum_p1/p\) diverges. The scaled odd-prime series \(F(s)=\sum_{p\ {\rm odd}}(2/p)^s=2^s(P(s)-2^{-s})\) converges for \(\Re s>1\). At \(s=2\), \(F(2)\approx0.80898968\). None is the original Jacobi theta series \(\sum_{n\in\mathbb Z}e^{-\pi n^2y}\).

A slice-valued prime phase series \(\sum_{p\ {\rm odd}}(2/p)^s\exp(-u\log(p/2))\) is absolutely convergent for real \(s>1\), but has no demonstrated new theta modular symmetry or xi zero constraint.

## D. Conclusions and research gate

1. **Proved:** 39.5 is a prime element in \(\mathbb Z[1/2]\).
2. **Proved:** \(1/p\) are precisely the irreducibles of the reciprocal-integer multiplicative monoid.
3. **Proved no-go:** one unital ring containing both 1/79 and 79 cannot keep 79 nonunit prime.
4. **Proved:** inversion maps exactly to quaternionic conjugation under the fixed-axis log-Cayley representation.
5. **Proved no-go:** a multiplicative quaternionic representation of ordinary commutative arithmetic cannot acquire genuinely noncommuting prime axes.
6. **Open:** any independent arithmetic/theta property forcing a new Riemann zero restriction.

**Next research:** consider a *two-sorted* arithmetic model (dyadic ring prime elements and reciprocal monoid irreducibles, with an inversion correspondence as a relation rather than a ring isomorphism), then test a theta-specific operator that is not merely a slice reparameterization. Avoid calling \(1/79\) and \(79/2\) primes in the same ordinary ring.
