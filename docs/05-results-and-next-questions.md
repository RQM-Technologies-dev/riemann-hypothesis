# 05 — Numerical findings, evidence boundaries, and next tests

**Date:** 2026-10-30.  
**Precision:** 60 decimal digits via \`mpmath\`; no hardware jobs, no paid computation.  
**Reference implementation:** [experiments/compactified_return.py](../experiments/compactified_return.py).  
**Machine-readable output:** [results/compactified_return.json](../results/compactified_return.json).  
**Tests:** [tests/test_compactified_return.py](../tests/test_compactified_return.py).

## Experiment configuration

- One fixed inverse-stereographic scale \(L=20\) throughout.
- One fixed normalized ambient radius \(R=1\); any \(R>0\) rescales the geometry globally.
- First eight positive nontrivial zeros computed by \`mpmath.zetazero\`.
- Full angular branch: \(\theta(t)=2\arctan(t/L)\) for \(t\ge0\), \(2\pi+2\arctan(t/L)\) for \(t<0\).
- Quaternionic unit phase represented in one arbitrary fixed imaginary slice, \(U=a+\mathbf u b\), so radius is \(a^2+b^2\).
- Completed scalar \(X(t)=\xi(1/2+it)\).

## First eight mapped zero pairs

| Index | Positive height \(\gamma_n\) | Outbound angle \(\theta_n\), degrees | Conjugate return, degrees |
|---|---:|---:|---:|
| 1 | 14.1347251417 | 70.500468 | 289.499532 |
| 2 | 21.0220396388 | 92.854390 | 267.145610 |
| 3 | 25.0108575801 | 102.704654 | 257.295346 |
| 4 | 30.4248761259 | 113.361616 | 246.638384 |
| 5 | 32.9350615877 | 117.463099 | 242.536901 |
| 6 | 37.5861781588 | 123.964177 | 236.035823 |
| 7 | 40.9187190121 | 127.903649 | 232.096351 |
| 8 | 43.3270732809 | 130.443419 | 229.556581 |

This is a numerical check of an algebraic coordinate identity, **not** empirical evidence that this geometry constrains the location of zeros.

## Error checks

At 60-digit working precision, using the specified sample points:

| Invariant | Maximum numerical error |
|---|---:|
| Completed scalar \(X(t)=X(-t)\) | \(1.65\times10^{-62}\) |
| \(\operatorname{Im}X(t)=0\) | \(8.26\times10^{-63}\) |
| Polar unit-radius \(|U|^2=1\) | \(7.78\times10^{-62}\) |
| \(\theta(-t)=2\pi-\theta(t)\), conjugate polar coefficients | exact to computed precision |

All seven regression tests pass:
\`\`\`
python -m unittest discover -s tests -v
Ran 7 tests — OK
\`\`\`

## Evidence of completion-factor damping

| \(|t|\) | \(|X(t)|\) |
|---:|---:|
| 20 | \(3.6655427756\times10^{-5}\) |
| 40 | \(2.1176217079\times10^{-11}\) |
| 80 | \(2.4342633467\times10^{-24}\) |
| 160 | \(5.1723127143\times10^{-51}\) |

These samples illustrate the asymptotic exponential bound, but are not by themselves the proof of smoothness (see [04](04-infinity-pole-and-spinorial-return.md)).

## Constructive counterexample to a harmonic phase crossing the pole

Let \(n=2\), \(m=20\). The heights
\[
t_m=\frac{2\pi m}{\log2}\approx181.2944,\quad
t_m'=\frac{(2m+1)\pi}{\log2}\approx185.8268
\]
both lie on the outward path and approach infinity as \(m\to\infty\). Yet
\[
2^{-1/2-it_m}=+0.70710678\ldots,\quad
2^{-1/2-it_m'}=-0.70710678\ldots
\]
(up to numerical rounding). Thus the individual term has no well-defined value at the common infinity pole. The quaternionic unit phase \(U(\theta)\), which is a *different function*, is smooth at that pole. The completed scalar amplitude \(F(\theta)\) is smooth and flat there.

## Claims matrix

| Statement | Status | Why |
|---|---|---|
| One global polar/Cayley map puts the entire critical line on \(S^3_R\) | Proved | Quaternion norm identity |
| Positive and negative heights are angular conjugates | Proved | \(t\mapsto-t\) and \(\theta\mapsto2\pi-\theta\) |
| Half/full meridian gives \(-1/+1\) spinorial sign pattern | Proved for chosen \(U\) | \(e^{\mathbf u\pi}=-1\), \(e^{2\pi\mathbf u}=1\) |
| Any individual harmonic passes smoothly through infinity | **False** | Explicit two-subsequence counterexample |
| Completed \(X\) smoothly vanishes at compactified infinity | Established from analytic asymptotics | Gamma exponential decay; derivatives |
| Completed polar \(F\) is real analytic at infinity | **False** | Infinite accumulating critical-line zeros |
| \(\Psi=F U\) gives conjugate smooth return | Proved for constructed field | Algebraic definitions |
| This return forces all zeta zeros onto critical line | **Unproved** | Mapping already assumes line; off-axis zeros not excluded |
| Prime product converges on critical line | **False** | Euler product valid for \(\Re s>1\) |
| Zeros determine one entire \(\xi\), with normalization | Established | Hadamard product |
| Novel independent spectral/arithmetic selection law has been found | **Not yet** | Operator not derived |

## Next falsifiable investigation

1. Define an operator on compactified \(S^3\) **without \(\xi\) in its coefficients** and without inputting zero heights.
2. Derive its domain/boundary regularity at the infinity pole. In particular, determine whether the flat nonanalytic scalar state is admissible.
3. Specify the exact involution sending \((\theta,\mathbf u)\mapsto(2\pi-\theta,\mathbf u)\), or equivalently \(\mathbf u\mapsto-\mathbf u\) in the unoriented full \(S^3\).
4. Derive arithmetic \(\log p\) content from a canonical kernel or transfer operator, not a tunable prime correction.
5. Require an out-of-sample zero-ordinate test and negative controls with off-axis zero quartets.
6. A true RH proof would still need an exhaustive argument eliminating every possible off-line zero, not only matching the first few.

## Earlier RQM work, not overwritten

Previous perfect-closure/zeta calibration experiments explicitly recorded **no support** under their benchmark protocols. Their results should not be silently turned into successful evidence here. See [Perfect Closure archive](https://github.com/RQM-Technologies-dev/perfect-closure/tree/main/archive/zeta-critical-line-program/experiments) and [Completed Zeta Stability](https://github.com/RQM-Technologies-dev/completed-zeta-stability).
