# Riemann Hypothesis — Quaternionic Polar Closure

**Status:** exploratory mathematical research, not a proof of the Riemann Hypothesis.  
**Updated:** 2026-11-02  
**Scope:** a complex harmonic series, its completed zeta function, and a four-real-dimensional *geometric model*; no physical time or particle-mass claim.

## Core hypothesis

The critical line `s=1/2+it` can be mapped by **one global inverse stereographic/Cayley transformation** into a closed quaternionic polar meridian. Positive zeta-zero ordinates occur on the outward traversal, their conjugates on the return traversal, and infinity is a common pole. All mapped points lie at the same ambient four-dimensional radius `R`; the different zero ordinates become different **angular locations**, not individually normalized radii.

The strongest question is not whether this mapping is possible (it is), but whether a **new, independently defined harmonic closure law** can require zeta zeros to occupy the critical-line meridian.

## Primary research direction — symbolic-scale closure (2026-11-02)

**Read first:** [12 — Keep \(L\) symbolic: scale-covariant closure criterion](docs/12-symbolic-scale-and-defect.md), then [09 — The positive \(w\)-distance RH equivalence](docs/09-w-distance-rh-equivalence.md).

The inverse-stereographic coordinate choice is valid for **every \(L>0\)**:
\[
\boxed{
\theta_L(t)=2\arctan(t/L),\qquad
w_L(t)=\frac{L^2-t^2}{L^2+t^2},\qquad
d_L(t)=1+w_L(t)=\frac{2L^2}{L^2+t^2}.
}
\]
The zeta-zero ordinates \(\gamma_n\) are **independent of \(L\)**. Varying \(L\) only changes their angular positions on the common hypersphere; it does not move the complex zeros or change the truth of RH.

For any \(L>0\), define the complete weighted deficiency
\[
\boxed{
D(L)=L\,\frac{\xi'(\frac12+L)}{\xi(\frac12+L)}
-\sum_{\substack{\gamma>0\\\xi(\frac12+i\gamma)=0}}
\frac{2L^2}{L^2+\gamma^2}.
}
\]
The entire positive-scale family satisfies
\[
\boxed{\mathrm{RH}\ \Longleftrightarrow\ D(L_0)=0
\quad\text{for any one (hence every) }L_0>0.}
\]
The all-positive-\(L\) positivity proof uses complete off-critical-line conjugate **quartets**, not an incorrect assertion that each individual off-line term is positive for small \(L\).

A *scale-free* alternative is
\[
\boxed{
\mathcal E=\lim_{L\to0^+}\frac{D(L)}{L^2}
=\frac{\xi''(\frac12)}{\xi(\frac12)}
-2\sum_{\substack{\gamma>0\\\xi(\frac12+i\gamma)=0}}\frac1{\gamma^2}
\ge0,\qquad
\mathrm{RH}\Longleftrightarrow\mathcal E=0.
}
\]
Crucially \(D(L)\to0\) automatically as \(L\to0^+\), **even if RH is false**. We must not mistake that coordinate degeneration for proof of complete closure.

**Numerical illustration only:** at \(L=20\) the target is \(T(20)\approx13.330990477997\), as recorded in [09](docs/09-w-distance-rh-equivalence.md). It is not a privileged geometric scale.

The sum runs over **all** positive-height critical-line zeros, with multiplicity. The right side is independently evaluable using the completed zeta function on the real axis. The inequality “left side \(\le\) right side” holds unconditionally, and the *difference equals a sum of strictly positive contributions from off-line zeros*. Therefore equality at the infinite limit is **equivalent** to RH; it has **not** been proved. A finite partial sum being smaller is expected even if RH is true.

The distance \(d_w\) is a **difference along the w-coordinate to the infinity pole**, not hyperspherical geodesic distance. The quaternionic geometry provides a new way to organize the question, not a proof by itself.

- [Full proof, meaning of every term, numerical table, and falsification limits](docs/09-w-distance-rh-equivalence.md)
- [Executable 40-digit test with 200 verified-on-line zero heights](experiments/w_distance_rh_criterion.py)
- [Saved numerical output](results/w_distance_rh_criterion_L20.json) and [seven new regression tests](tests/test_w_distance_rh_criterion.py)


### Latest follow-on: bounded missing contribution (2026-11-02)

The Jacobi-theta positive Fourier kernel supplies the **exact real-axis target**
\[
T(L)=L\frac{\int_0^\infty v\Phi(v)\sinh(Lv)\,dv}
{\int_0^\infty\Phi(v)\cosh(Lv)\,dv},
\]
without entering any zeros. **Jensen's theorem** then gives a genuine unconditional upper bound on all remaining *critical-line* \(w\)-distances at height above \(H\), and proves that tail tends to zero. [Full theorem and positive-kernel counterexample](docs/10-jacobi-theta-jensen-tail.md).

A stronger **uniform normalized** bound follows from published verification through \(H=3\times10^{12}\), published explicit zero counting, and the off-line quartet identity:
\[
\boxed{0\le D(L)/L^2\le2P_+(H)<2.960\times10^{-12}
\quad\text{for all }L>0.}
\]
Here \(P_+(H)\) is an explicit upper bound on \(\sum_{\Im\rho>H}(\Im\rho)^{-2}\). At the illustrative \(L=20\), \(D(20)<1.184\times10^{-9}\), improving the earlier \(1.214\times10^{-9}\) bound. The full [symbolic derivation](docs/12-symbolic-scale-and-defect.md) is now primary; [the earlier derivation and external references](docs/11-certified-distance-defect-bound.md) remain useful.

**This does not prove \(D(20)=0\)**. The finite-height verified range cannot be extended to infinity without a new theorem. The epsilon-sized upper bound is largely a consequence of the \(1/\gamma^2\) weighting of high zeros.

- [Reproducible equations, numerical diagnostics, and counterexample](experiments/theta_tail_and_defect_bound.py)
- [Numerical results and certified-height assumptions](results/theta_tail_and_defect_bound_L20.json)
- [New regression tests](tests/test_theta_tail_and_defect_bound.py) (committed; run with existing test suite)


### Latest mathematical investigation: a theta-only *partial* growth theorem (2026-11-02)

The kernel-only attempt at the proposed scale-free exhaustion equality did **not** establish \(\mathcal E=0\). Instead, [13 — Jacobi-theta local growth certificate](docs/13-theta-kernel-local-growth-certificate.md) rigorously derives two unconditional partial bounds:

\[
\Xi(x+iy)\ne0\quad (|x|<6.545059859\ldots,\ |y|\le1/2),
\]
\[
\partial_y|\Xi(x+iy)|^2>0\quad
(|x|<4.821134613\ldots,\ 0<y\le1/2).
\]

Both follow from **moments of the actual positive Jacobi-theta kernel**, with no zero locations inserted. These are weaker than established finite-height zero-free results. The exact growth expression is a double integral with positive amplitudes but sign-changing cosine factors; controlling those oscillations for **all** real \(x\) remains equivalent to RH (Hinkkanen–Lagarias growth theorem; see Planat 2026).

- [Proof and term-by-term derivation](docs/13-theta-kernel-local-growth-certificate.md).
- [Reproducible moment experiment](experiments/theta_growth_certificate.py), [tests](tests/test_theta_growth_certificate.py), [numerical constants](results/theta_growth_certificate.json).
- Related **preprint** updated 2026-11-02: Suvrit Sra, *On some positivity properties of the Riemann Xi function*, v3, https://suvrit.github.io/papers/riem-xi/ . Its very high **finite-order** positivity results do not imply full RH.

The scale \(L>0\) remains **symbolic** throughout the geometric and exhaustion criteria: the new analytic growth theorem does not require choosing \(L\) at all.


## One-page equation summary

Choose a unit imaginary quaternion `u²=-1`, fixed positive scale `L` and common radius `R`.

```text
s(t) = 1/2 + i t                complex critical line
Q(t,u) = R (L + u t)(L-u t)^(-1)
       = R [cos θ(t) + u sin θ(t)]
θ(t) = 2 arctan(t/L) mod 2π
|Q(t,u)|² = R²                 one ambient S³
θ(+t) + θ(-t) = 2π             conjugate return
Q(0,u)=+R; Q(∞,u)=-R          compactified infinity pole
Q at θ=2π = +R                complete return
```

The completed zeta function is `ξ(s)=½s(s−1)π^(−s/2)Γ(s/2)ζ(s)`. Its real, even critical-line restriction `X(t)=ξ(½+it)` can be pulled back onto the polar meridian. Its zeros occur at angular positions determined by `t = L tan(θ/2)`.

**Important:** every point of the critical line, not only zeros, lands on the sphere. The geometry by itself does not select zeros or establish RH.

## Reading order

0. [00 — Research lineage and prior investigations](docs/00-research-lineage.md): preserves the Dirac, zeta, and Perfect Closure steps that led to this formulation.
1. [01 — Polar quaternionic geometry](docs/01-polar-quaternionic-geometry.md): what a coordinate is, why infinity becomes a pole, fixed radius versus latitude spheres, conjugation, spinorial analogy.
2. [02 — Equation-by-equation dictionary](docs/02-equation-dictionary.md): every term, variable, domain, and prerequisite.
3. [03 — Complex harmonic series, Euler product, and reverse-zero reconstruction](docs/03-harmonic-series-and-zero-product.md): phases, where the series converges, Gamma versus primes, Hadamard product.
4. [04 — Infinity-pole investigation](docs/04-infinity-pole-and-spinorial-return.md): new mathematical findings, local proof, limits, topological limitations, spectral-density prediction.
5. [05 — Numerical results and next tests](docs/05-results-and-next-questions.md): reproducibility, claims matrix, independent-model requirements.
6. [06 — Round S³ spectral test](docs/06-round-s3-spectral-test.md): rigorous single-shell no-go and the infinite zonal expansion.
7. [07 — Riemann–Siegel conjugate wave balance](docs/07-riemann-siegel-conjugate-balance.md): the **exact Gamma-phase/Hardy Z relation** and the known conjugate harmonic sum with its essential remainder.
8. [08 — One exact theta harmonic equation for zero latitudes](docs/08-theta-kernel-zero-latitudes.md): **one global Jacobi-theta cosine integral** directly selects the critical-line hypersphere coordinates w; normalized quaternionic conjugate-phase form, numerical roots, and pole boundaries.
9. [09 — Positive w-distance RH criterion](docs/09-w-distance-rh-equivalence.md): **primary direction**, exact log-derivative identity, strict positivity of off-line contributions, and numeric exhaustion experiment.
10. [10 — Jacobi-theta/Jensen tail theorem](docs/10-jacobi-theta-jensen-tail.md): rigorous unconditional convergence of the uncounted on-line weighted tail, and why positivity alone cannot prove RH.
11. [11 — Verified-height defect bound](docs/11-certified-distance-defect-bound.md): published finite-height verification and explicit total zero-counting give a useful baseline bound.
12. [12 — Symbolic-scale closure and normalized defect](docs/12-symbolic-scale-and-defect.md): **primary current theorem**, proof for all positive L, quartet factors and universal normalized bound.
13. [13 — Jacobi-theta partial growth theorem](docs/13-theta-kernel-local-growth-certificate.md): kernel-only zero-free and strict-growth certificates, with rigorous oscillatory obstruction.
14. [Executable experiment](experiments/compactified_return.py), [regression tests](tests/test_compactified_return.py), [sample results](results/compactified_return.json); plus [S³ projection experiment](experiments/s3_spectral_projection.py) and [its numerical coefficients](results/s3_spectral_projection.json); plus [Riemann–Siegel polar balance](experiments/riemann_siegel_polar.py), [verification data](results/riemann_siegel_polar.json), and [its tests](tests/test_riemann_siegel_polar.py); plus [exact theta-kernel latitude solver](experiments/theta_kernel_w_roots.py), [first eight w-roots](results/theta_kernel_w_roots_first8.json) and [new tests](tests/test_theta_kernel_w_roots.py).

## Historical links

- [Perfect Closure — archived quaternionic lift](https://github.com/RQM-Technologies-dev/perfect-closure/blob/main/archive/zeta-critical-line-program/papers/02-perfect-closure-is-quaternionic.md).
- [Perfect Closure — zero-to-operator bridge](https://github.com/RQM-Technologies-dev/perfect-closure/blob/main/archive/zeta-critical-line-program/papers/04-zeta-mass-closure-operator.md).
- [Completed Zeta Stability](https://github.com/RQM-Technologies-dev/completed-zeta-stability): separate research program; do not conflate its mathematical/IBM tests with a proof.


## Latest: one harmonic equation for all w-latitudes

Using the classical Jacobi-theta Fourier kernel Phi, the critical-line zeros obey **one** exact cosine-integral equation: `C_L(w)=2∫₀∞ Phi(v) cos(L v sqrt((1-w)/(1+w))) dv=0`, for `-1<w<1`. With the single global `L=20`, integral root discovery (not using known zero locations as inputs) reproduces the first eight critical-line zeros and maps them into one common `S³` hypersphere. A normalized weight gives the equivalent **quaternionic conjugate-wave balance**. This is an exact coordinate reformulation of the established Xi transform and **does not exclude off-critical-line zeros** or prove RH. Full details: [08](docs/08-theta-kernel-zero-latitudes.md).

## Evidence status

- **Exact:** Cayley mapping; its constant radius; conjugate angular reflection; `ξ(s)=ξ(1-s)`; `X(t)=X(-t)`; standard Euler and Hadamard identities in their proper domains.
- **Established analysis, described here:** decay of the completed function on the critical line; smooth but non-real-analytic flat extension of its scalar angular pullback at the infinity pole; individual harmonic phases have no limit there.
- **Numerically checked:** first eight ordinates, conjugate angles, polar norm, critical-line symmetry, pole decay, exact Gamma/Hardy Z identity and Riemann–Siegel conjugate-pair residual. **Fourteen earlier regression tests were reported passing; seven additional distance-criterion tests passed locally on 2026-11-02.**
- **Unproved hypothesis:** a unique resonance selection law or independently derived operator that forces exactly the critical-line zeros. The **symbolic-scale saturation equality and scale-free moment criterion are equivalent to RH and remain unproved**, despite the positive uniform bound on the defect. No RH proof is claimed.

Run locally:

```bash
python -m pip install mpmath numpy
python -m unittest discover -s tests -v
python experiments/compactified_return.py --digits 60 --zeros 8 --scale 20
python experiments/s3_spectral_projection.py
python experiments/riemann_siegel_polar.py
python experiments/theta_kernel_w_roots.py --count 3
python experiments/w_distance_rh_criterion.py --scale 20 --count 200 --digits 40
python experiments/theta_tail_and_defect_bound.py --digits 40 --scale 20 --count 8
python experiments/symbolic_scale_family.py --scales 0.1,0.5,1,5,20,100 --count 40
python experiments/theta_growth_certificate.py --digits 45
# add --count 200 to repeat the longer 200-zero calculation
```

We preserve the difference between coordinate geometry, an analytic identity, and a predictive theorem.
