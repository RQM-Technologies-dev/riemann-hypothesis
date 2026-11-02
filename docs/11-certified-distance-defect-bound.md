# 11 — A rigorous upper bound on the missing \(w\)-distance, from verified RH height and explicit zero counting

**2026-11-02.** Current best *quantitative* complement to the direct Jacobi-theta/Jensen tail bound in [10](10-jacobi-theta-jensen-tail.md). The numerical constants use published zero verification and a published explicit bound on the total zero-counting function. The main inequalities below are theorems **conditional on those cited published inputs**, not a solution of RH. Any finite-precision output is labelled approximate, not interval-certified.

## 1. The exact positive-defect equation

Fix global \(L>1/2\), let \(x_L=L+1/2\) and \(\rho=\beta+i\gamma\) run over nontrivial zeta zeros with \(\gamma>0\) and multiplicity. Define the one-hypersphere coordinate distance
\[
d_L(\gamma)=1+w(\gamma)=\frac{2L^2}{L^2+\gamma^2}.
\]
The exact identity proved in [09](09-w-distance-rh-equivalence.md) reads
\[
T(L)=L\frac{\xi'(x_L)}{\xi(x_L)}
=\sum_{\Im\rho>0}
\frac{2L(x_L-\beta)}{(x_L-\beta)^2+\gamma^2}.
\]
Its on-line subseries is \(S_{\rm line}(L)=\sum_{\Re\rho=1/2,\Im\rho>0}d_L(\gamma)\). Their difference is strictly nonnegative:
\[
\boxed{
D(L)=T(L)-S_{\rm line}(L)
=\sum_{\substack{\Im\rho>0\\\Re\rho\ne1/2}}
\frac{2L(x_L-\beta)}{(x_L-\beta)^2+\gamma^2}\ge0.
}
\]
RH is **equivalent** to \(D(L)=0\); the equality is currently unproved.

## 2. Published external results (read their exact scope)

**Input A — finite-height verification:** Platt and Trudgian, *Bull. London Math. Soc.* (2021), rigorously proved, using interval arithmetic, that **all** nontrivial zeros with \(0<\gamma\le H\), \(H=3\times10^{12}\), lie on the critical line, and are simple. DOI: https://doi.org/10.1112/blms.12460

This rules out off-line zeros *at or below* \(H\), but gives no information about their existence above \(H\).

**Input B — explicit total-zero counting bound:** Bellotti and Wong, *Mathematics of Computation* (published online November 14, 2025), gave for all \(t\ge e\):
\[
\boxed{
|N(t)-M(t)|\le E(t):=a\log t+b\log\log t+c,
}
\]
where
\[
M(t)=\frac{t}{2\pi}\log\frac{t}{2\pi e},\quad
a=0.10076,\ b=0.24460,\ c=8.08344.
\]
Here \(N(t)\) counts **all** nontrivial zeros with \(0<\gamma\le t\), with multiplicities, NOT only those on the critical line. DOI: https://doi.org/10.1090/mcom/4133

We deliberately use the 2025 bound as published. More recent unreviewed claims of slightly different constants are not required.

## 3. An unconditional weighted tail estimate for all zeros

Define the inverse-square zero tail
\[
P(H)=\sum_{\Im\rho>H}\frac1{\gamma^2}.
\]
The Stieltjes identity (valid for \(H\ge e\), with zeros at height \(H\) excluded) is
\[
P(H)=-\frac{N(H)}{H^2}+2\int_H^\infty\frac{N(t)}{t^3}\,dt.
\]
Substitute \(N=M+(N-M)\). The main term has derivative
\[
M'(t)=\frac1{2\pi}\log\frac t{2\pi},
\]
so
\[
\int_H^\infty t^{-2}\,dM(t)
=\frac{\log(H/(2\pi))+1}{2\pi H}.
\]

For the error, \(|N(t)-M(t)|\le E(t)\) gives
\[
\left|-\frac{N(H)-M(H)}{H^2}
+2\int_H^\infty\frac{N(t)-M(t)}{t^3}\,dt\right|
\le \frac{E(H)}{H^2}+2\int_H^\infty\frac{E(t)}{t^3}\,dt.
\]
Use
\[
2\int_H^\infty\frac{\log t}{t^3}dt
=\frac{\log H+1/2}{H^2},
\quad
2\int_H^\infty\frac{\log\log t}{t^3}dt
\le\frac{\log\log H+(2\log H)^{-1}}{H^2}.
\]
Thus the **explicit rigorous bound** is
\[
\boxed{
P(H)\le P_+(H):=
\frac{\log(H/(2\pi))+1}{2\pi H}
+
\frac{
2a\log H+a/2+2b\log\log H+b/(2\log H)+2c
}{H^2}.
}
\]
Every term is known; no unknown zero ordinate appears on the right.

## 4. Rigorous bound on the possible off-line defect

By Input A, every **off-line** zero must have \(\gamma>H\). Since \(0<\beta<1\), \(x_L-\beta<L+1/2\). Therefore each hypothetical off-line contribution obeys
\[
0<
\frac{2L(x_L-\beta)}
{(x_L-\beta)^2+\gamma^2}
<
\frac{2L(L+1/2)}{\gamma^2}.
\]
Sum over all off-line zeros above \(H\):
\[
\boxed{
0\le D(L)\le 2L(L+1/2)P_+(H).
}
\]
Similarly, for critical-line zeros at heights \(>H\),
\[
\boxed{
0\le S_{\rm line}^{>H}(L)\le 2L^2P_+(H).
}
\]

With \(L=20\), \(H=3\times10^{12}\), standard high-precision evaluation gives:
\[
P_+(H)\approx1.47970363091503245\times10^{-12},
\]
\[
\boxed{0\le S_{\rm line}^{>H}(20)<1.184\times10^{-9}},
\]
\[
\boxed{0\le D(20)<1.214\times10^{-9}}.
\]
The decimal upper thresholds are conservatively rounded *above* evaluation of the explicit proved formulas. They are **not** new upper bounds on off-critical-line zero *heights*, and they do **not** imply \(D(20)=0\). No full interval-arithmetic implementation of the numerical evaluation is claimed; rigorous statements can always be read in their exact symbolic \(P_+(H)\) forms.

**Interpretation:** the measured weight of any possible violation of RH, in *this particular \(w\)-distance sum*, is extremely small. This is an immediate consequence of published zero verification plus known total counting, **not** evidence of a newly proven RH statement. The weighting suppresses very-high-height zeros like \(1/\gamma^2\).

## 5. Application to the first 200 spheres

The existing experiment gives, numerically,
\[
T(20)\approx13.33099047799700249,
\quad S_{200}(20)\approx11.68351994129464652,
\]
so
\[
R_{200}=T(20)-S_{200}(20)\approx1.64747053670235597.
\]

Since
\[
R_{200}=D(20)+S_{\rm line}^{>\gamma_{200}}(20),
\]
the rigorous theoretical bound on \(D\) yields the explicit **two-sided inequality**
\[
\boxed{
R_{200}-2L(L+1/2)P_+(H)
\le S_{\rm line}^{>\gamma_{200}}(20)\le R_{200}.
}
\]
With the displayed approximate values, this brackets the true uncounted critical-line contribution very tightly:
\[
1.647470535488\ldots
\ \lesssim S_{\rm line}^{>\gamma_{200}}(20)
\ \lesssim1.647470536703\ldots.
\]
Here the **inequality in terms of exact \(R_{200}\) and \(P_+\) is rigorous**. The decimal endpoints inherit the numerical uncertainty of \`mpmath\` zero ordinates and are *not* themselves certified enclosures until the first-200-zero inputs and real-axis target are interval-verified. This uncertainty is small for ordinary numerical purposes but should never be mislabelled formal proof.

At the cutoff \(\gamma_{200}\approx396.38\), the explicit zero-count upper bound gives
\[
S_{\rm line}^{>\gamma_{200}}(20)
\le 2L^2 P_+(\gamma_{200})\approx1.74576444.
\]
This is weaker than the total-minus-finite-sum upper bound 1.64747054. The **strong two-sided bracket** comes from *the huge externally certified RH verification height*, not from computing a few hundred zeros alone.

## 6. Does this force the infinite sum to exhaust the target?

**No.** It proves only
\[
0\le D(20)<1.214\times10^{-9}.
\]
It does not prove \(D(20)=0\). The kernel's direct Jensen tail bound in [10] converges to zero *as the cutoff tends to infinity*, but we have not verified that **every** zero at every height lies on the critical line.

It is invalid to send \(H\to\infty\) in the inequality for the **one known** certified height \(H=3\times10^{12}\). Such a step would amount to assuming RH.

What would count as the missing theorem:
- A proof from the Jacobi-theta/prime structure that \(\xi(s)\) has no off-line zeros;
- Or an exact on-line zero-counting equality exhausting the *total* count for all \(T\);
- Or an independent functional-analytic positivity theorem forcing \(D(L)=0\).

A very small **positive upper bound** is not a zero upper bound.

## 7. Reproducibility and caveats

- [Computation of \(P_+(H)\), defect bound, and kernel-Jensen comparison](../experiments/theta_tail_and_defect_bound.py).
- [Machine-readable numbers and notes](../results/theta_tail_and_defect_bound_L20.json).
- [Tests for the algebraic and derivative identities](../tests/test_theta_tail_and_defect_bound.py).
- Source of theta-kernel positivity/integral: Dan Romik, https://math.ucdavis.edu/~romik/data/uploads/papers/riemannxi.pdf
- Platt–Trudgian certified-height theorem: https://doi.org/10.1112/blms.12460
- Bellotti–Wong published explicit zero-counting bound: https://doi.org/10.1090/mcom/4133
