# 23 — Positive quaternionic folding penalty: an exact reflected-sphere comparison

**Date:** 2026-11-06  
**Status:** Exact geometric identity, checked by independent finite-precision quadrature. **Not a proof of RH.**  
**Primary direction:** [21 — Quaternionic theta continuation and superposed zero-spheres](21-quaternionic-theta-superposed-zero-spheres.md) and [22 — S³ Jensen second harmonic](22-quaternionic-s3-jensen-second-harmonic.md).  
**Clay requirement:** [17 — Exclude every off-critical-line zero](17-clay-statement-and-proof-roadmap.md).

## 1. The user's mechanism: a real constraint on *folded* spherical zero divisors

The research hypothesis is not "the two reflection symmetries alone imply RH." It is that two reflected \(S^2\) zero-spheres may be organized as a single four-real-dimensional superposition, and that **the actual Jacobi-theta structure** might impose an energy/positivity law forcing their centers to fold together onto the critical hyperplane.

This note constructs one explicit **positive folding penalty** that detects off-axis separation for an individual reflected quartet. The penalty exists as an exact identity. It remains **unknown whether the original theta kernel forces its sum to vanish**. That second step, not the positivity formula itself, would be the RH proof.

## 2. Start with the authentic quaternionic theta extension

The centered completed zeta function
\[
f(z)=\xi(\tfrac12+z)=2\int_0^\infty \Phi(v)\cosh(zv)\,dv
\]
has real even coefficients. Its intrinsic quaternionic extension is
\[
\mathcal X(q)=\sum_{n=0}^\infty c_nq^{2n}
=2\int_0^\infty\Phi(v)\cosh(qv)\,dv,\quad q\in\mathbb H.
\]

For \(q=a+ut\) (\(u^2=-1\)), this becomes
\[
\mathcal X(a+ut)=2[C(t,a)+uS(t,a)].
\]
An off-fold zero requires \(C=S=0\). This condition is satisfied across the full conjugacy \(S^2\) orientation sphere, and symmetry supplies the reflected zero-sphere centered at \(-a\). Quaternionic conjugation \(q\mapsto rqr^{-1}\) can change \(u\) but cannot change \(a\).

The ambient \(S^3_R\) in the next section is an **observation surface of radius \(R\)** in \(\mathbb H\), not the \(S^2\) zero-divisor sphere and not the independent Cayley scale \(L\) used elsewhere in the repo.

## 3. Four-dimensional Jensen observable

Define, for an intrinsic slice-regular polynomial or nonvanishing-on-the-surface entire function \(H\),

\[
\mathcal M_R[H]
=\frac{1}{\operatorname{area}(S^3_R)}
\int_{|q|=R}\log|H(q)|\,d\sigma(q).
\]

Writing \(q=R(\cos\theta+u\sin\theta)\) and using normalized \(d\omega(u)\) on \(S^2\), the four-dimensional surface measure has angular density \(\tfrac2\pi\sin^2\theta\,d\theta\,d\omega(u)\). For intrinsic \(H\), the modulus is independent of \(u\); thus

\[
\boxed{
\mathcal M_R[H]
=\frac2\pi\int_0^\pi\sin^2\theta
\log|h(Re^{i\theta})|\,d\theta,
}
\tag{P1}
\]
where \(h\) is the restriction to a fixed complex slice.

As derived in [22](22-quaternionic-s3-jensen-second-harmonic.md), this average is the usual complex circular Jensen mean **minus its second angular cosine harmonic**. It is an exact four-dimensional observable, not an independent extension of the zero data.

For an individual complex slice bookkeeping factor \(h_w(z)=1-z^2/w^2\), put \(r=|w|\) and
\[
j_w(R):=\frac2\pi\int_0^\pi
\sin^2\theta\log|h_w(Re^{i\theta})|\,d\theta.
\]

By the Fourier series of \(\log|1-\alpha e^{2i\theta}|\) and the orthogonality of \(\sin^2\theta\) to all nonconstant \(e^{2ik\theta}\) except \(k=1\),

\[
\boxed{
j_w(R)=
\begin{cases}
\frac{R^2}{2}\Re(w^{-2}),&0<R<r,\\[5pt]
2\log(R/r)+\frac{\Re(w^2)}{2R^2},&R>r.
\end{cases}
}
\tag{P2}
\]

At \(R=r\), both expressions share the same continuous limit; the logarithmic singularity in the angular integral is integrable. **Only the paired polynomial below**, with real coefficients, is used as a globally intrinsic quaternionic polynomial; the single factor \(h_w\) is merely a computational factor on one complex slice.

## 4. The positive reflected-quartet folding penalty

Let an off-center zero have centered slice location \(w=a+it\), with \(a\in\mathbb R\), \(t>0\), and radial distance \(r^2=a^2+t^2\). Its complete reflected quartet \(\{\pm w,\pm\bar w\}\) is represented by the real-coefficient normalized polynomial

\[
\boxed{
P_{a,t}(q)
=\left(1-\frac{q^2}{w^2}\right)
\left(1-\frac{q^2}{\bar w^2}\right),
}
\tag{P3}
\]

where the product is understood by combining its real coefficients before extending it to \(\mathbb H\). The expression does **not** denote a product of two separately quaternionically defined polynomials with nonreal coefficients.

Compare it with the **explicitly artificial, folded radial reference**

\[
\boxed{P^{\mathrm{fold}}_r(q)=
\left(1+\frac{q^2}{r^2}\right)^2.}
\tag{P4}
\]

This reference keeps the common radius \(r\) and the *four complex roots, counted with multiplicity* of the quartet, but places both conjugate pairs on the imaginary axis. It is **not** asserted to equal the genuine xi zero product.

The two spherical logarithmic means follow from (P2):

\[
\mathcal M_R[P_{a,t}]=2j_w(R),\qquad
\mathcal M_R[P^{\mathrm{fold}}_r]=2j_{ir}(R).
\]

Subtracting them gives an exact identity, for every \(R>0\) (with radial-zero cases understood by continuity):

\[
\boxed{
\mathfrak F_R(a,t)
:=\mathcal M_R[P_{a,t}]
-\mathcal M_R[P^{\mathrm{fold}}_r]
=
\begin{cases}
\frac{2a^2R^2}{(a^2+t^2)^2},&0<R\le r,\\[6pt]
\frac{2a^2}{R^2},&R\ge r.
\end{cases}
}
\tag{P5}
\]

It follows **rigorously** that

\[
\boxed{\mathfrak F_R(a,t)\ge0,\qquad
\mathfrak F_R(a,t)=0
\Longleftrightarrow a=0\quad(R>0).}
\tag{P6}
\]

The positive quantity is proportional to the **square of the real displacement** of the two mirror-sphere centers. This is an exact, geometrically meaningful *folding penalty*.

**But it does not force the actual zeta spheres to fold.** The same identity holds for any even real polynomial with an off-axis quartet. The positivity occurs because we chose a hypothetical coalesced reference, not because the actual theta kernel has been shown to forbid separated spheres. It is a comparison theorem, not a conservation law requiring zero cost.

### Summing over a hypothetical xi off-line divisor

If xi had off-line quartets \((a_k,t_k)\) of multiplicity \(m_k\), define the nonnegative hypothetical total

\[
\boxed{
\mathfrak F_R^{\mathrm{off}}
=\sum_{\mathrm{off\ quartets}}m_k\,
\mathfrak F_R(a_k,t_k).
}
\tag{P7}
\]

For each fixed \(R>0\), this sum converges absolutely, because \(|a_k|<1/2\), the zeta zero count grows at most \(O(T\log T)\), and the outer terms decay as \(O(R^2/r_k^4)\). Furthermore

\[
\mathrm{RH}\quad\Longleftrightarrow\quad
\mathfrak F_R^{\mathrm{off}}=0
\quad\text{for any fixed }R>0.
\tag{P8}
\]

**Warning:** the folded reference needed to calculate \(\mathfrak F_R^{\mathrm{off}}\) depends on the *unknown locations of off-line zeros*. Equations (P7)–(P8) are an RH-equivalent *diagnostic*, not an independently theta-evaluable equality or a proof that the sum vanishes.

At small observation radii, the normalized penalty is

\[
\lim_{R\to0^+}\frac{\mathfrak F_R^{\mathrm{off}}}{R^2}
=2\sum_{\mathrm{off\ quartets}}m_k\frac{a_k^2}{(a_k^2+t_k^2)^2}.
\tag{P9}
\]

This measures a different positive aspect of the same unknown off-axis divisor encoded by the scale-free defect \(\mathcal E\) in [12](12-symbolic-scale-and-defect.md). It cannot be set to zero by coordinate choice or by finite-height numerical tests.

## 5. Direct numerical verification and controls

The script [experiments/quaternionic_fold_penalty.py](../experiments/quaternionic_fold_penalty.py) implements the exact formula and independently computes the normalized \(S^3\) angular integrals for the **real-coefficient quartet polynomial and its centered reference**. It also tests the original centered xi function, at radii within the unconditionally zero-free disk, against the separate exact small-radius mean in [22](22-quaternionic-s3-jensen-second-harmonic.md).

Selected 40-digit mpmath integrations (not interval certified):

| Real displacement \(a\) | Height \(t\) | S³ radius \(R\) | Angular mean difference | Formula (P5) |
|---:|---:|---:|---:|---:|
| 0.25 | 1.5 | 0.8 | 0.01495982468955441928 | 0.01495982468955441928 |
| 0.25 | 1.5 | 2.0 | 0.03125000000000000000 | 0.03125000000000000000 |
| 0.20 | 14.13 | 10 | 0.00020060758083400251 | 0.00020060758083400251 |
| 0.20 | 14.13 | 17 | 0.00027681660899653979 | 0.00027681660899653979 |

For the **actual xi function**, the independent quadrature and theta/xi derivative formula give

\[
\mathcal M_R[\mathcal X]
=\log\xi(\tfrac12)
-\frac{R^2}{4}\frac{\xi''(\tfrac12)}{\xi(\tfrac12)}
\]

for \(R=1,3\), both rigorously inside the known first-zero radius. These checks validate the normalization and quadrature; they do not constrain unknown off-line heights.

The [regression tests](../tests/test_quaternionic_fold_penalty.py) check parity, quartic-to-fold limits, both radial regimes, the sign-definite formula, and an independently calculated xi mean. A generic off-axis polynomial is a necessary **negative control** for any invalid argument that (P6) alone proves RH.

## 6. Next *noncircular* research obligation

**Proposed theorem to investigate, not proved:**

> Starting from the exact **arithmetic Jacobi-theta kernel** of xi, prove a four-dimensional identity or inequality that independently forces the total folding penalty (P7) to be zero, without inserting the true zero locations as assumptions.

A concrete investigation sequence:

1. **Independent theta expression.** Develop a formula for a four-dimensional angular or radial functional using only the exact theta series and its modular transformation, not a hypothetical folded product assembled from unknown zeros.
2. **Comparison mechanism.** Find a *kernel-derived reason* the theta functional must coincide with its radial-folded reference. Merely defining that reference from unknown zero positions will be circular; proving a new equality independent of those positions would be consequential.
3. **Falsification.** Test the proposed equality on (i) real even quartics with off-center zero-spheres and (ii) modified positive even theta kernels with explicit nonreal zeros, as well as (iii) the true xi kernel.
4. **Global criterion.** Prove the equality at one positive radius for all zeros, not only finitely many. The convergence of (P7) would then allow the positive summands to force each \(a_k=0\), settling Clay's RH target.
5. **Rigor gate.** Establish all interchanges of infinite sums/integrals, count multiplicities correctly, and explain what new analytic content is supplied by quaternionic geometry beyond a complex-slice rewriting.

**Current result:** an exact positive fold-separation observable and its complete 4D derivation. **The kernel-imposed vanishing theorem remains unsolved.**

## 7. References

- [21 — authentic intrinsic theta continuation](21-quaternionic-theta-superposed-zero-spheres.md)
- [22 — \(S^3\) second-harmonic Jensen identity](22-quaternionic-s3-jensen-second-harmonic.md)
- [12 — existing scale-free off-line defect](12-symbolic-scale-and-defect.md)
- A. Altavilla and C. Bisi, *Log-biharmonicity and a Jensen formula in the space of quaternions*, 2019, https://arxiv.org/abs/1708.04894.
- A. Perotti, *A four dimensional Jensen formula*, 2020, https://www.rivmat.unipr.it/vols/2020-11-1/07-perotti.html.
- Note: (P1)–(P5) are elementary angular-mean calculations in this special intrinsic setting. They are compatible with the published quaternionic Jensen framework but **are not presented as a new general quaternionic Jensen theorem**.
