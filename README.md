# Riemann Hypothesis — Quaternionic Polar Closure

**Status:** exploratory mathematical research, not a proof of the Riemann Hypothesis.  
**Updated:** 2026-11-02  
**Scope:** a complex harmonic series, its completed zeta function, and a four-real-dimensional *geometric model*; no physical time or particle-mass claim.

## Core hypothesis

The critical line `s=1/2+it` can be mapped by **one global inverse stereographic/Cayley transformation** into a closed quaternionic polar meridian. Positive zeta-zero ordinates occur on the outward traversal, their conjugates on the return traversal, and infinity is a common pole. All mapped points lie at the same ambient four-dimensional radius `R`; the different zero ordinates become different **angular locations**, not individually normalized radii.

The strongest question is not whether this mapping is possible (it is), but whether a **new, independently defined harmonic closure law** can require zeta zeros to occupy the critical-line meridian.

## Current primary research direction — w-distance saturation criterion (2026-11-02)

**Read first:** [09 — The positive w-distance sum rule and its exact RH equivalence](docs/09-w-distance-rh-equivalence.md). This is now the preferred mathematical test of the polar-closure hypothesis.

On one unit four-dimensional hypersphere, the 3D latitude radius changes with the fourth coordinate \(w\). Use **one** global scale \(L=20\) to bend the whole critical line:

\[
w(t)=\frac{400-t^2}{400+t^2},\qquad
d_w(t)=1+w(t)=\frac{800}{400+t^2}.
\]

The exact conditional-exhaustion test is

\[
\boxed{\displaystyle
\mathrm{RH}\ \Longleftrightarrow\
\sum_{\substack{\gamma>0\\\zeta(1/2+i\gamma)=0}}
d_w(\gamma)
=
20\,\frac{\xi'(20.5)}{\xi(20.5)}
=13.330990477997002487\ldots
}
\]

The sum runs over **all** positive-height critical-line zeros, with multiplicity. The right side is independently evaluable using the completed zeta function on the real axis. The inequality “left side \(\le\) right side” holds unconditionally, and the *difference equals a sum of strictly positive contributions from off-line zeros*. Therefore equality at the infinite limit is **equivalent** to RH; it has **not** been proved. A finite partial sum being smaller is expected even if RH is true.

The distance \(d_w\) is a **difference along the w-coordinate to the infinity pole**, not hyperspherical geodesic distance. The quaternionic geometry provides a new way to organize the question, not a proof by itself.

- [Full proof, meaning of every term, numerical table, and falsification limits](docs/09-w-distance-rh-equivalence.md)
- [Executable 40-digit test with 200 verified-on-line zero heights](experiments/w_distance_rh_criterion.py)
- [Saved numerical output](results/w_distance_rh_criterion_L20.json) and [seven new regression tests](tests/test_w_distance_rh_criterion.py)

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
10. [Executable experiment](experiments/compactified_return.py), [regression tests](tests/test_compactified_return.py), [sample results](results/compactified_return.json); plus [S³ projection experiment](experiments/s3_spectral_projection.py) and [its numerical coefficients](results/s3_spectral_projection.json); plus [Riemann–Siegel polar balance](experiments/riemann_siegel_polar.py), [verification data](results/riemann_siegel_polar.json), and [its tests](tests/test_riemann_siegel_polar.py); plus [exact theta-kernel latitude solver](experiments/theta_kernel_w_roots.py), [first eight w-roots](results/theta_kernel_w_roots_first8.json) and [new tests](tests/test_theta_kernel_w_roots.py).

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
- **Unproved hypothesis:** a unique resonance selection law or independently derived operator that forces exactly the critical-line zeros. The new **w-distance saturation equality is equivalent to RH and remains unproved.** No RH proof is claimed.

Run locally:

```bash
python -m pip install mpmath numpy
python -m unittest discover -s tests -v
python experiments/compactified_return.py --digits 60 --zeros 8 --scale 20
python experiments/s3_spectral_projection.py
python experiments/riemann_siegel_polar.py
python experiments/theta_kernel_w_roots.py --count 3
python experiments/w_distance_rh_criterion.py --scale 20 --count 200 --digits 40
```

We preserve the difference between coordinate geometry, an analytic identity, and a predictive theorem.
