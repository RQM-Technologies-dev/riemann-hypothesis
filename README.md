# Riemann Hypothesis — Quaternionic Polar Closure

**Status:** exploratory mathematical research, not a proof of the Riemann Hypothesis.  
**Updated:** 2026-10-30  
**Scope:** a complex harmonic series, its completed zeta function, and a four-real-dimensional *geometric model*; no physical time or particle-mass claim.

## Core hypothesis

The critical line `s=1/2+it` can be mapped by **one global inverse stereographic/Cayley transformation** into a closed quaternionic polar meridian. Positive zeta-zero ordinates occur on the outward traversal, their conjugates on the return traversal, and infinity is a common pole. All mapped points lie at the same ambient four-dimensional radius `R`; the different zero ordinates become different **angular locations**, not individually normalized radii.

The strongest question is not whether this mapping is possible (it is), but whether a **new, independently defined harmonic closure law** can require zeta zeros to occupy the critical-line meridian.

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
8. [Executable experiment](experiments/compactified_return.py), [regression tests](tests/test_compactified_return.py), [sample results](results/compactified_return.json); plus [S³ projection experiment](experiments/s3_spectral_projection.py) and [its numerical coefficients](results/s3_spectral_projection.json); plus [Riemann–Siegel polar balance](experiments/riemann_siegel_polar.py), [verification data](results/riemann_siegel_polar.json), and [its tests](tests/test_riemann_siegel_polar.py).

## Historical links

- [Perfect Closure — archived quaternionic lift](https://github.com/RQM-Technologies-dev/perfect-closure/blob/main/archive/zeta-critical-line-program/papers/02-perfect-closure-is-quaternionic.md).
- [Perfect Closure — zero-to-operator bridge](https://github.com/RQM-Technologies-dev/perfect-closure/blob/main/archive/zeta-critical-line-program/papers/04-zeta-mass-closure-operator.md).
- [Completed Zeta Stability](https://github.com/RQM-Technologies-dev/completed-zeta-stability): separate research program; do not conflate its mathematical/IBM tests with a proof.

## Evidence status

- **Exact:** Cayley mapping; its constant radius; conjugate angular reflection; `ξ(s)=ξ(1-s)`; `X(t)=X(-t)`; standard Euler and Hadamard identities in their proper domains.
- **Established analysis, described here:** decay of the completed function on the critical line; smooth but non-real-analytic flat extension of its scalar angular pullback at the infinity pole; individual harmonic phases have no limit there.
- **Numerically checked:** first eight ordinates, conjugate angles, polar norm, critical-line symmetry, pole decay, exact Gamma/Hardy Z identity and Riemann–Siegel conjugate-pair residual. **Ten local regression tests passed.**
- **Unproved hypothesis:** a unique resonance selection law or independently derived operator that forces exactly the critical-line zeros. No RH proof is claimed.

Run locally:

```bash
python -m pip install mpmath numpy
python -m unittest discover -s tests -v
python experiments/compactified_return.py --digits 60 --zeros 8 --scale 20
python experiments/s3_spectral_projection.py
python experiments/riemann_siegel_polar.py
```

We preserve the difference between coordinate geometry, an analytic identity, and a predictive theorem.
