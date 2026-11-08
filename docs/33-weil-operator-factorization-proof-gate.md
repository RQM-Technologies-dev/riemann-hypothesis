# 33 — The next proof gate: exact Weil form, and a Fourier no-go for positive Mangoldt jumps

**Date:** 2026-11-08  
**Status:** rigorous additional operator identity and a limitation; **no Riemann-hypothesis proof**.

## Objective

After Chapter 32's positive quaternionic jump operator, ask whether arithmetic-specific positivity can be promoted to the *complete* Weil form. Do not mistake an arbitrary positive operator for the RH-equivalent form. The actual outstanding problem is an all-test-function inequality for the original prime-plus-archimedean explicit formula.

## 1. A sharper exact identity for the positive jump operator

Let \(A(s)=-\zeta'(s)/\zeta(s)=\sum_{n\ge2}\Lambda(n)n^{-s}\) for \(\Re s>1\). Chapter 32 defines
\[
D_\sigma=\sum_{n\ge2}\Lambda(n)n^{-\sigma}(2I-U_{\log n}-U_{-\log n}),\qquad \sigma>1.
\]
The Fourier symbol satisfies the exact identity
\[
\boxed{m_\sigma(t)=2\left[A(\sigma)-\Re A(\sigma+it)\right]
=2\sum_{n\ge2}\Lambda(n)n^{-\sigma}(1-\cos(t\log n))\ge0.}
\tag{33.1}
\]
This is a *global all-frequency* positivity theorem involving the genuine von Mangoldt coefficients. It is **not new** in substance: it follows termwise from \(1-\cos\ge0\) and absolute convergence. It does not extend to \(\sigma=1/2\) by ordinary summation.

The same argument holds for **any** nonnegative absolutely summable weights \(a_n\), not just the actual \(\Lambda(n)\), and any commuting unitary shifts. Therefore (33.1) is an arithmetic-sensitive identity but its positivity is *arithmetic-insensitive*. It is not an RH criterion.

## 2. A structural no-go for norm-square operator strategies

Suppose a proposed quaternionic operator has the form
\[
D=\sum_n B_n^*B_n
\]
with convergence in quadratic-form sense on a common dense domain. Then \(\langle f,Df\rangle=\sum_n\|B_nf\|^2\ge0\) **for every admissible \(f\)**, regardless of the zero distribution of any particular entire function used to generate \(f\). If the *only* link to xi is substitution of the completed critical-line function as an input vector, this cannot distinguish xi from a modified completed function with explicit off-critical zeros, provided both are in the domain. The Chapter 24 shifted-kernel control is one such example for bounded translation differences.

This no-go is deliberately scoped: a sum-of-squares representation of the **actual complete Weil form**, derived from the original theta arithmetic without assuming RH, *would* be a breakthrough. The obstruction applies to unrelated universally positive forms, not to a hypothetical exact arithmetic factorization of Weil's form.

## 3. Why the full Weil functional is the necessary object

For suitable compactly supported smooth functions on the multiplicative positive reals, the classical explicit formula relates the completed zeta zeros to a prime-power distribution, its reciprocal branch, the archimedean Gamma term and pole contributions. In one conventional normalization, the zero-side pairing is
\[
\mathcal W(g)=\sum_\rho \widehat{g}(\rho)\overline{\widehat{g}(1-\overline{\rho})},
\quad \widehat{g}(s)=\int_0^\infty g(x)x^{s-1}dx,
\tag{33.2}
\]
with the sum interpreted in the standard explicit-formula regularization, and with test-function conventions adjusted so that \(\mathcal W(g)\) equals the complete Weil prime-plus-archimedean expression. Under RH, \(1-\overline\rho=\rho\) and (33.2) is a sum of nonnegative squares. Weil's positivity criterion asserts that \(\mathcal W(g)\ge0\) for **all** admissible \(g\) if and only if RH. We do not assert convergence or a proof without the requisite function class and regularization; consult the standard Weil explicit formula for the precise setup.

The \(\Lambda(n)\) jump energy in (33.1) omits the Gamma and pole terms and is *not equal* to (33.2). An inequality involving only \(\Lambda(n)\ge0\) is not sufficient.

## 4. Practical falsification plan

A candidate quaternionic proof must pass all of:
1. **Exactness:** prove its quadratic form equals the fully normalized Weil form for a specified dense admissible test class, including all prime, reciprocal, Gamma and pole terms.
2. **Arithmetic selectivity:** demonstrate that the construction uses more than generic nonnegative weights or a fixed complex-slice extension.
3. **Negative control:** apply the proposed sign argument to Chapter 24's shifted positive-even kernel; the argument must fail, not falsely certify its known off-axis zeros.
4. **Globality:** prove the sign for every admissible test, not just finite Fourier modes, Gaussian tests, or a finite spectral window.
5. **Noncircularity:** derive positivity from independently established arithmetic or operator properties rather than assuming all xi zeros lie on the critical line.

## 5. Conclusion

The strongest exact new audit outcome is the closed-form symbol (33.1) and the corresponding no-go: the successful positive quaternionic jump operator is a generic Markov/Laplacian-type energy, and cannot imply RH. This **narrows** the next meaningful research direction to a rigorous factorization or independent lower bound for the *complete* Weil functional. The central mathematical obstacle remains unsolved.

References: Chapters 17, 18, 24, 30–32; J. Lagarias, *The Riemann Hypothesis: Arithmetic and Geometry*, Weil positivity criterion; CMI Riemann Hypothesis problem statement.
