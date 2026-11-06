# Riemann Hypothesis — Quaternionic Polar Closure

**Status:** exploratory mathematical research, not a proof of the Riemann Hypothesis.  
**Updated:** 2026-11-06  
**Scope:** a complex harmonic series, its completed zeta function, and a four-real-dimensional *geometric model*; no physical time or particle-mass claim.

## First Clay-aligned investigation completed — modular inversion no-go (2026-11-06)

**[18 — Exact modular-inversion obstruction and averaged theta growth](docs/18-modular-inversion-obstruction-and-averaged-growth.md).** We constructed an explicit positive, even, fast-decaying perturbation of the actual Jacobi-theta kernel with the same weight-\(\tfrac12\) inversion symmetry, whose Fourier transform is
\[
\widehat\Psi(z)=\Xi(z)\bigl(1+0.98\cos z\bigr).
\]
It has **explicit nonreal auxiliary zeros** at \(z=\pi\pm0.2016884878\ldots i\) (inside the RH strip), showing that **inversion, positivity and decay alone cannot force RH**. These are **not** zeros of the original Riemann Xi function. A separate compactly supported positive perturbation proves that even preserving the original theta **tails exactly** is insufficient without further arithmetic structure.

A genuine unconditional positive theorem also follows by Plancherel:
\[
E(y)=\int_{\mathbb R}|\Xi(x+iy)|^2dx
=4\pi\int_0^\infty\Phi(u)^2\cosh(2yu)du,
\quad
E'(y)=8\pi\int_0^\infty u\Phi(u)^2\sinh(2yu)du>0\ (y>0).
\]
This is **averaged**, not **pointwise**, growth; it does not settle RH. Moreover, \(\partial_y|\Xi(x+iy)|^2\to0\) at large \(|x|\), so any *height-independent positive margin* is impossible.

The next lemma must use the **exact Jacobi \(n^2\)-arithmetic structure** beyond inversion, generic positivity, kernel tails or first Laguerre inequalities. See [experiment](experiments/modular_symmetry_obstruction.py), [six tests](tests/test_modular_symmetry_obstruction.py), and [numerical results](results/modular_symmetry_obstruction.json). These were locally checked, not interval-certified or a proof of RH.

## Governing objective — Clay Millennium Prize statement (2026-11-06)

**Start here:** [17 — Exact Clay problem statement and prioritized proof roadmap](docs/17-clay-statement-and-proof-roadmap.md), then [16 — Two-fold zero-spheres and theta positivity](docs/16-two-fold-zero-spheres-and-theta-positivity.md).

Enrico Bombieri's official [Clay Mathematics Institute problem statement](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf), §I, p. 1, requires **every nontrivial zero \(\rho\) of \(\zeta(s)\) to satisfy \(\Re\rho=\tfrac12\)**. Equivalently, every zero of the completed critical-line function \(\Xi(z)=\xi(\tfrac12+iz)\) must be real. Analytic continuation of zeta is already established; higher-dimensional representations alone are not proofs of the required zero exclusion.

**Primary proof obligation:** obtain unconditionally from the *specific* Jacobi-theta kernel an all-height strict outward growth law
\[
\boxed{\partial_y|\Xi(x+iy)|^2>0,\quad x\in\mathbb R,\ 0<y\le\tfrac12.}
\]
Alternatively, prove infinite-order Toeplitz total nonnegativity for its theta-moment coefficients or construct an exact self-adjoint spectral correspondence to **every** Xi zero. These are RH-equivalent proof targets, **not established results**. Local inequalities, finite verified zeros, positive kernel amplitudes, and self-adjoint *overlap* representations do not suffice.

**Priority order:** (A) theta-specific modular control of the signed oscillatory growth integral, uniformly at all spectral heights; (B) an all-orders Toeplitz factorization; (C) theta heat deformation / de Bruijn–Newman boundary as a distinct exploratory track. The reflection-quartet and paired quaternionic zero-sphere geometry serve as interpretation and hypothesis-generation tools, not substitutes for a new global analytic theorem. Keep the separate Cayley \(S^3\) coordinate scale \(L>0\) symbolic.

**Status:** research roadmap only. **RH remains unsolved.**

## First folded-channel investigation — inward deformation and phase collision (2026-11-06)

**New primary working note:** [19 — Phase/Wronskian, Hermite–Biehler boundary and inward deformation](docs/19-folded-channel-inward-deformation-and-wronskian.md). Starting from \(\Xi(t+ia)=2(C-iS)\), analyticity gives the exact cross-channel Wronskian \(J=CS_t-SC_t=\frac18\partial_a|\Xi|^2\), and \(\partial_t\arg\Xi=-J/(C^2+S^2)\). A second identity gives
\[
\partial_aJ=C_t^2+S_t^2-CC_{tt}-SS_{tt}
=\tfrac14\bigl(|\Xi'|^2-\Re(\Xi\overline{\Xi''})\bigr).
\]
At any hypothetical **simple off-line zero**, \(J=0\) and \(\partial_aJ=|\Xi'|^2/4>0\); every off-line zero, including higher multiplicities, forces a local sign reversal of \(J\) when crossing its spectral latitude. These are exact identities, **not a proof that such zeros are absent**.

Csordas–Varga's 1989 Hermite–Biehler result supplies an **unconditional outer boundary**: the two theta channels have real-zero structure for shifts \(a\ge1/2\). The open research question is whether the **specific** Jacobi-theta kernel preserves this noncollision condition as \(a\) decreases toward 0 at **all** heights.

A 45-digit [finite numerical experiment](experiments/folded_channel_collision_scan.py) with [saved results](results/folded_channel_collision_scan.json) and [new tests](tests/test_folded_channel_collision_scan.py) followed the two channels on heights \(8\le t\le45\). At shifts \(a=0.50,0.49,0.20,0.05\), eight C and eight S roots were found per shift, alternating in the sampled range. A deliberately modified positive kernel with nonreal zeros reproduced the predicted Wronskian sign reversal. These scans are **not certified exhaustive** and **cannot settle RH**. The next task is a theta-modular *uniform inward-preservation lemma* with explicit counterexample/failure gates.

## Mirror-channel hypothesis refinement (2026-11-06)

**Read [18 — Mirror-channel folding, superposition and zero collision](docs/18-mirror-channel-folding-and-zero-collision.md).** The user's hypothesis is **not** that conjugation symmetry alone proves RH; it is that the paired quaternionic zero-spheres may be manifestations of *analytically coupled* mirror channels, and that understanding their folded superposition may reveal a theta-specific restriction on zero locations.

For real spectral height \(t\) and transverse displacement \(a\), the actual Jacobi-theta Fourier representation gives \(\Xi(t+ia)=2[C(t,a)-iS(t,a)]\), with \(C\) even and \(S\) odd under \(a\mapsto-a\). At the fold \(a=0\), \(S(t,0)=0\) identically; off the fold, a zero requires **simultaneous** cancellation \(C=S=0\). The refined proof target is to derive from the special theta kernel a global no-common-zero/interlacing constraint for all \(0<a\le1/2\), without assuming RH. The 1989 Hermite–Biehler research of Csordas and Varga already uses the same cosine/sine channels, so it is essential prior art. This is an **RH-equivalent target**, not a result proved by the decomposition itself.

## Core hypothesis

The critical line `s=1/2+it` can be mapped by **one global inverse stereographic/Cayley transformation** into a closed quaternionic polar meridian. Positive zeta-zero ordinates occur on the outward traversal, their conjugates on the return traversal, and infinity is a common pole. All mapped points lie at the same ambient four-dimensional radius `R`; the different zero ordinates become different **angular locations**, not individually normalized radii.

The strongest question is not whether this mapping is possible (it is), but whether a **new, independently defined harmonic closure law** can require zeta zeros to occupy the critical-line meridian.

## New chapter — two-fold zero-spheres and theta-kernel positivity (2026-11-06)

[16 — Two folds, quaternionic zero-spheres and theta positivity](docs/16-two-fold-zero-spheres-and-theta-positivity.md) collects the recent research discussion into one complete, carefully qualified note. It derives the zeta zero quartet and its quartic, the intrinsic slice-regular lift into paired \(S^2\) zero-spheres, and the exact criterion that both spheres coincide precisely when a zero lies on the critical line. It also distinguishes these zero-spheres from the earlier common \(S^3\) Cayley-coordinate model and keeps the map scale \(L\) arbitrary.

The note compares three potential analytic mechanisms: (1) **strict outward Xi-modulus growth** from the Jacobi-theta Fourier kernel, (2) **infinite-order Toeplitz total nonnegativity** of its positive even theta-moment coefficients, and (3) a **self-adjoint unitary-overlap representation**. The first two are RH-equivalent and **unproved globally**; the third is an exact construction but is not sufficient to prove RH. It includes counterexamples showing that two reflections or positive spectral measures alone cannot rule out off-line zeros.

Reproducibility: [moment/quartic experiment](experiments/two_fold_theta_positivity.py), [unit tests](tests/test_two_fold_theta_positivity.py), and [saved finite numerical diagnostics](results/two_fold_theta_positivity.json). These finite examples do not prove RH or establish all infinite Toeplitz minors. For the prior rigorous partial bounds, see [13](docs/13-theta-kernel-local-growth-certificate.md), [14](docs/14-higher-moment-cosine-certificate.md), and [15](docs/15-higher-moment-growth-certificate.md).

## Supporting research direction — symbolic-scale closure (2026-11-02)

**For this supporting line of work:** read [12 — Keep \(L\) symbolic: scale-covariant closure criterion](docs/12-symbolic-scale-and-defect.md), then [09 — The positive \(w\)-distance RH equivalence](docs/09-w-distance-rh-equivalence.md).

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


### Latest: higher-order theta moment certificates (2026-11-02)

The kernel-only attempt at the scale-free \(\mathcal E=0\) exhaustion theorem **does not yet prove RH**. Instead, the exact global cosine minorant \(\cos z\ge P_{4m+2}(z)\), combined with moment monotonicity of the **actual Jacobi-theta kernel**, gives two rigorous families of *local sufficient conditions*:

- [14 — Higher cosine moments](docs/14-higher-moment-cosine-certificate.md): unconditional zero-free condition \(\Re\Xi(x+iy)>0\) wherever an explicitly defined exact polynomial \(B_n(x)\) is positive for \(|y|\le1/2\). Ninth-order numerical first-root estimate: \(\approx9.913\).
- [15 — Higher bilinear growth moments](docs/15-higher-moment-growth-certificate.md): the more relevant strict-growth condition \(\partial_y|\Xi(x+iy)|^2>0\) wherever the exact polynomial \(H_n(x)\) is positive for \(0<y\le1/2\). Ninth-order numerical first-root estimate: \(\approx7.184\), extending the previous approximate \(4.821\) threshold.

These root **decimals are not interval-certified**; the theorem is the symbolic inequality with its exact theta-moment integrals. Every fixed finite-order minorant eventually turns negative, so the method cannot itself establish positivity at all heights or \(\mathcal E=0\). **All stereographic scales \(L>0\) remain symbolic:** these results constrain the analytic zeta-height coordinate, not the mapping scale.

- [Zero-free experiment](experiments/higher_moment_cosine_certificate.py) and [tests](tests/test_higher_moment_cosine_certificate.py).
- [Growth experiment](experiments/higher_moment_growth_certificate.py) and [tests](tests/test_higher_moment_growth_certificate.py).
- [Numerical zero-free diagnostics](results/higher_moment_cosine_certificate.json) and [growth diagnostics](results/higher_moment_growth_certificate.json).


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

**Current proof-oriented entry point:** [17 — Clay statement and roadmap](docs/17-clay-statement-and-proof-roadmap.md) → [18 — modular inversion obstruction](docs/18-modular-inversion-obstruction-and-averaged-growth.md) → [15 — signed theta-growth integral](docs/15-higher-moment-growth-certificate.md) → [16 — two folds and zero-spheres](docs/16-two-fold-zero-spheres-and-theta-positivity.md). The numbered list preserves the historical research lineage.

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
14. [14 — Higher theta cosine moments](docs/14-higher-moment-cosine-certificate.md): exact polynomial zero-free criteria and their finite-order obstruction.
15. [15 — Higher theta growth moments](docs/15-higher-moment-growth-certificate.md): exact bilinear strict-growth criteria with larger local range, still not RH.
16. [16 — Two folds, zero-spheres, and theta positivity](docs/16-two-fold-zero-spheres-and-theta-positivity.md): complete symmetry/quartic derivation, slice-regular (S^2) lift, growth and total-nonnegativity equivalences, self-adjoint counterexample, and open proof task.
17. [17 — Official Clay proof target and roadmap](docs/17-clay-statement-and-proof-roadmap.md): exact statement, all-height theta-positivity and all-orders alternatives, investigation tracks, and proof acceptance criteria.
18. [18 — Folded mirror channels and zero-collision obstruction](docs/18-mirror-channel-folding-and-zero-collision.md): cosine/sine theta channels, quartic splitting, precise noncollision criterion, Hermite–Biehler prior art, and research tests.
19. [19 — Folded-channel phase, Wronskian and inward deformation](docs/19-folded-channel-inward-deformation-and-wronskian.md): exact C/S phase law, 1989 Hermite–Biehler outer boundary, finite high-precision alternating roots, collision sign test, and next theta-modular lemma.
18. [18 — Modular inversion no-go and averaged growth](docs/18-modular-inversion-obstruction-and-averaged-growth.md): exact off-axis counterexample, compact-tail-preserving obstruction, global L2 average growth, and the next theta-arithmetic lemma.
20. [Executable experiment](experiments/compactified_return.py), [regression tests](tests/test_compactified_return.py), [sample results](results/compactified_return.json); plus [S³ projection experiment](experiments/s3_spectral_projection.py) and [its numerical coefficients](results/s3_spectral_projection.json); plus [Riemann–Siegel polar balance](experiments/riemann_siegel_polar.py), [verification data](results/riemann_siegel_polar.json), and [its tests](tests/test_riemann_siegel_polar.py); plus [exact theta-kernel latitude solver](experiments/theta_kernel_w_roots.py), [first eight w-roots](results/theta_kernel_w_roots_first8.json) and [new tests](tests/test_theta_kernel_w_roots.py).

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
python experiments/higher_moment_cosine_certificate.py --digits 40
python experiments/higher_moment_growth_certificate.py --nodes 220
# add --count 200 to repeat the longer 200-zero calculation
```

We preserve the difference between coordinate geometry, an analytic identity, and a predictive theorem.
