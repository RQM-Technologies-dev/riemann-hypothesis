# 09 — The \(w\)-distance sum rule: a positive RH-equivalent criterion

**Research note: 2026-11-02.** This is the preferred next direction for the quaternionic polar-closure program. The criterion below is an exact reformulation of the Riemann Hypothesis, **not a proof** and not a claim of a novel independently derived theorem. It follows from classical Hadamard factorization and symmetry of the completed zeta function.

## 1. One hypersphere, one globally fixed scale

The four-real-coordinate hypersphere is
\[
w^2+x^2+y^2+z^2=1.
\]
Parametrize it in a chosen imaginary quaternionic direction \(\mathbf u^2=-1\):
\[
q=e^{\mathbf u\theta}=\cos\theta+\mathbf u\sin\theta.
\]
Choose \(L>0\) **once**, independently of zero index, and map complex critical-line height \(t\) into
\[
\theta(t)=2\arctan(t/L)\quad (t\ge0),\qquad
w(t)=\cos\theta(t)=\frac{L^2-t^2}{L^2+t^2}.
\]
The three-dimensional latitude sphere at \(w\) has intrinsic radius \(\sqrt{1-w^2}\), while every point has the same **ambient four-dimensional radius** \(1\).

The infinity pole is \(w=-1\). Its **coordinate separation along the \(w\)-axis** (not the geodesic distance on \(S^3\)) is
\[
\boxed{d_w(t)=1+w(t)=\frac{2L^2}{L^2+t^2}
=2\cos^2\!\frac{\theta(t)}2.}
\]
Thus \(d_w\to0\) as \(t\to+\infty\), and the \(\gamma_n\) become distinct latitude positions without per-zero normalization. The half-angle identity is mathematically compatible with spinorial polar geometry, but \(t\) is a **spectral height, not time** and no physical Dirac mechanism is claimed.

## 2. What the completed function knows

Define the entire completed zeta function
\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]
Its zeros \(\rho=\beta+i\gamma\) (all \(0<\beta<1\)) are precisely the nontrivial zeta zeros, counted with multiplicity. It satisfies
\[
\xi(s)=\xi(1-s),\qquad
\xi(\bar s)=\overline{\xi(s)}.
\]
For a scale \(L\ge\tfrac12\), let
\[
x_L=\tfrac12+L\ge1,\quad
T(L)=L\,\frac{\xi'(x_L)}{\xi(x_L)}.
\]
The derivative is with respect to the *complex argument* \(s\), evaluated at the real number \(x_L\). It is **not a time derivative**. There is no zero at this real argument, so the quotient is well-defined.

The classical centered, even Hadamard product is, with zeros paired by \(z\leftrightarrow-z\),
\[
\frac{\xi(1/2+z)}{\xi(1/2)}
=\prod_{\Im\rho>0}
\left(1-\frac{z^2}{(\rho-1/2)^2}\right).
\]
This converges in the specified paired sense because \(\sum_\rho|\rho-1/2|^{-2}<\infty\).
Differentiating the logarithm at real \(z=L\) gives
\[
\frac{\xi'(x_L)}{\xi(x_L)}
=\sum_{\Im\rho>0}
\frac{2L}{L^2-(\rho-1/2)^2}.
\]
Individual terms may be complex; combining an off-axis pair \(\rho=1/2+\delta+i\gamma\) and \(\rho'=1/2-\delta+i\gamma\) gives a real number.

Equivalently, organizing all positive-imaginary roots (including the reflection partners when off-line) yields the **exact, real, absolutely convergent sum**
\[
\boxed{
T(L)=
\sum_{\substack{\rho=\beta+i\gamma\\ \gamma>0}}
\frac{2L\,(x_L-\beta)}
{(x_L-\beta)^2+\gamma^2}.
}
\]
Every summand is **strictly positive** because \(x_L\ge1\) and \(0<\beta<1\). There are no cancellation terms that could hide an off-critical-line root.

## 3. On-line distances and the exact RH equivalence

When a positive-imaginary root is on the line, \(\rho=\tfrac12+i\gamma\), its contribution is
\[
\frac{2L\,(x_L-\frac12)}
{(x_L-\frac12)^2+\gamma^2}
=\frac{2L^2}{L^2+\gamma^2}
=1+w(\gamma)=d_w(\gamma).
\]
Let \(\mathcal Z_{\rm line}^+\) denote *all* positive-height critical-line zeros, counted with multiplicity, and set
\[
S_{\rm line}(L)=\sum_{\gamma\in\mathcal Z_{\rm line}^+}
\frac{2L^2}{L^2+\gamma^2}.
\]

Subtracting yields the *exact nonnegative missing contribution*,
\[
\boxed{
D(L):=T(L)-S_{\rm line}(L)
=\sum_{\substack{\rho=\beta+i\gamma,\ \gamma>0\\\beta\ne1/2}}
\frac{2L\,(x_L-\beta)}
{(x_L-\beta)^2+\gamma^2}
\ge0.
}
\]

Because each off-line term is **strictly positive**:
\[
\boxed{
\mathrm{RH}\quad\Longleftrightarrow\quad D(L)=0
\quad\Longleftrightarrow\quad
\sum_{\gamma\in\mathcal Z_{\rm line}^+}(1+w(\gamma))
=L\,\frac{\xi'(\frac12+L)}{\xi(\frac12+L)},
\qquad L\ge\tfrac12.
}
\]

This is the central rigorous interpretation: **does the sum of all on-sphere, on-line latitudes exhaust the total?** A hypothetical off-line quartet contributes a positive defect. The geometry does not, by itself, show that the defect vanishes.

It is enough to prove \(D(L)=0\) at one fixed \(L\ge\tfrac12\), because a single off-line zero would create a strictly positive contribution at *every* such \(L\). This statement makes no assumption of RH in constructing \(D\).

## 4. Working numerical scale \(L=20\)

Choose \(L=20\) globally; then \(x_L=20.5\) and
\[
d_w(\gamma)=\frac{800}{400+\gamma^2}.
\]
The target can be evaluated **without any zero input** using
\[
\frac{\xi'(s)}{\xi(s)}
=\frac1s+\frac1{s-1}-\frac12\log\pi
+\frac12\psi(s/2)+\frac{\zeta'(s)}{\zeta(s)},
\]
where \(\psi(z)=\Gamma'(z)/\Gamma(z)\) is the digamma function. At \(s=20.5\):
\[
\boxed{T(20)=13.33099047799700248726506126097\ldots}
\]
(Mpmath working precision: 40 decimal digits. The constant is computed from Gamma, zeta, and their derivatives, *not* a sum of preselected zeros.)

The first \(N\) confirmed critical-line zeros give monotone lower bounds:

| First \(N\) zeros | Last height included | Partial \(\sum d_w\) | Remaining \(T(20)-\text{partial}\) |
|---:|---:|---:|---:|
| 1 | 14.134725 | 1.333799151945 | 11.997191326052 |
| 2 | 21.022040 | 2.284001256315 | 11.046989221682 |
| 4 | 30.424876 | 3.667542843754 | 9.663447634243 |
| 8 | 43.327073 | 5.384658881691 | 7.946331596306 |
| 16 | 67.079811 | 7.165884367325 | 6.165106110672 |
| 40 | 122.946829 | 9.270771201486 | 4.060219276511 |
| 100 | 236.524230 | 10.847344387409 | 2.483646090588 |
| 200 | 396.381854 | 11.683519941295 | 1.647470536702 |

**Do not call the final column “off-line mass”**: for finite \(N\) it contains the contributions of *all unenumerated on-line zeros*, plus any hypothetical off-line roots. These finite calculations provide no evidence for or against RH by themselves.

## 5. Off-line quartet control

For a test zero pair at \(s=1/2\pm\delta+i\gamma\), reflection and complex conjugation produce the four roots
\[
1/2+\delta\pm i\gamma,\qquad 1/2-\delta\pm i\gamma.
\]
Their total contribution to \(T(L)\) is
\[
2L\!\left[
\frac{L-\delta}{(L-\delta)^2+\gamma^2}
+
\frac{L+\delta}{(L+\delta)^2+\gamma^2}
\right]>0,\qquad L\ge\tfrac12,\ |\delta|<\frac12.
\]
Thus mirror symmetry allows reciprocal radii under the full Cayley transform, but cannot cancel the **positive log-derivative defect**. This is a stronger arithmetic constraint than simply noticing conjugate symmetry. It still does **not** prove such off-line quartets do not exist.

## 6. What this result is and what remains

**Exact established ingredients:** zeta functional equation; zero symmetries; Hadamard factorization; absolute convergence of the paired log-derivative sum at real \(x_L\); positivity for \(x_L\ge1\); the coordinate \(w\)-distance identity.

**Derived consequence:** the displayed criterion \(D(L)=0\) is equivalent to RH, at any fixed \(L\ge1/2\). This equivalence is a restatement of established theory, not an independent proof of the unknown condition.

**Unproved step:** establishing that the sum over *every* critical-line zero converges to exactly \(T(L)\), without assuming that no off-line zeros exist. Numerical confirmation of finitely many zeros or showing the residual is small cannot prove the required exact equality.

**Most promising mathematical next question:** can we derive an independent bound for the uncounted *on-line tail* using the Jacobi-theta kernel from [08](08-theta-kernel-zero-latitudes.md), then prove the residual vanishes? Any such bound must avoid accidentally inserting the total Riemann–von Mangoldt count as though it counted only on-line zeros; that equality is precisely what's unknown. A successful proof must show the off-line defect vanishes globally.

## 7. Reproducibility

- [Script](../experiments/w_distance_rh_criterion.py): high-precision target from \(\xi'/\xi\), first-\(N\) on-line contributions, off-line quartet countercheck.
- [JSON output](../results/w_distance_rh_criterion_L20.json): target, partial sums, remaining residuals, and a deliberately hypothetical off-axis quartet.
- [Regression tests](../tests/test_w_distance_rh_criterion.py): metric identity, completed-derivative identity, positivity, monotonic bounds, quartet test, and zero-free evaluation point.

Run:
\`\`\`bash
python -m pip install mpmath
python experiments/w_distance_rh_criterion.py --scale 20 --count 200 --digits 40
python -m unittest discover -s tests -v
\`\`\`

## Classical references

- NIST DLMF §§[25.4](https://dlmf.nist.gov/25.4), [25.10](https://dlmf.nist.gov/25.10) on reflection and critical-strip zeros.
- [Harvard notes on Hadamard products and logarithmic derivatives](https://people.math.harvard.edu/~elkies/M259.02/zeta2.pdf).
- [Earlier quaternionic polar embedding](01-polar-quaternionic-geometry.md), [one theta-kernel zero-latitude equation](08-theta-kernel-zero-latitudes.md).


## 8. Follow-on conclusion (2026-11-02): the tail *is* bounded; saturation is still unknown

The next two investigations sharpen this RH-equivalent formulation, without assuming the conclusion:

1. [10 — Jacobi-theta and Jensen](10-jacobi-theta-jensen-tail.md): the positive Jacobi kernel supplies the exact target as a hyperbolic moment, and Jensen's formula gives an **unconditional** upper bound on the remaining critical-line tail above height \(T\), tending to zero at rate \(O(\log T/T)\). This does not establish that the off-line defect \(D(L)\) vanishes. A positive-even-kernel countermodel shows why this is a serious distinction.
2. [11 — Verified-height defect bound](11-certified-distance-defect-bound.md): Platt–Trudgian's certified RH verification to \(3\times10^{12}\) plus Bellotti–Wong's published total-zero bound implies \(0\le D(20)<1.214\times10^{-9}\). This does not give exact equality \(D(20)=0\), but it tightly brackets the uncounted on-line contribution after the first 200 computed zeros.

**Current proof obligation:** produce an independent arithmetic theorem that forces \(D(L)=0\), not merely an estimate \(D(L)<\varepsilon\) for a fixed positive \(\varepsilon\). Neither the round hyperspherical geometry nor plain positivity/evenness of the Fourier kernel has that consequence.
