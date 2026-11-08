# 34 — Direct Weil factorization attempt: finite zero-block signature obstruction

**Date:** 2026-11-08. **Status:** rigorous finite-dimensional algebraic obstruction and explicit falsification diagnostic, **not a proof of RH**. Continues [33](33-weil-operator-factorization-proof-gate.md). The earlier 39.5 dyadic-prime example is historical motivation only, **not an ongoing research objective**.

## 1. Exact object to factor

Use the standard Weil criterion in a suitable admissible Mellin test-function class with the complete explicit-formula regularization. The zero-side sesquilinear form is schematically
\[
W(g,h)=\sum_\rho \widehat g(\rho)\overline{\widehat h(1-\overline\rho)}
\]
with zeros counted with multiplicity. Exact choice of Mellin convention, test class, pole terms and zero-sum regularization must be fixed before claiming an operator identity. The full Weil form equals the prime-power **plus archimedean and pole** expression. RH is equivalent to its positivity on all admissible tests; it is not established.

We attempted to factor the zero-side form into a sum of squares **without** assuming zeros lie on the critical line. This gives an immediate structural obstruction.

## 2. Finite off-line reflection block is indefinite

Let \(\rho=\beta+i\gamma\), with \(\beta\ne1/2\), and define its reflection partner \(\rho^\#=1-\overline\rho=1-\beta+i\gamma\). Suppose a test transform takes values \(v_1=\widehat g(\rho)\) and \(v_2=\widehat g(\rho^\#)\). The contribution of this pair to the diagonal zero form is
\[
W_{\rm pair}(v)=v_1\overline{v_2}+v_2\overline{v_1}
=2\Re(v_1\overline{v_2})
=v^*\begin{pmatrix}0&1\\1&0\end{pmatrix}v.
\]
The matrix has eigenvalues \(+1\) and \(-1\). For \(v=(1,-1)\), the block is \(-2\), whereas for \(v=(1,1)\) it is \(+2\). If \(\beta=1/2\), the two reflected locations coincide and the contribution instead is \(|\widehat g(\rho)|^2\ge0\) (counted with multiplicity).

Thus an off-line reflection pair **cannot itself** be factored as \(B^*B\) on an unrestricted two-dimensional value space. This is the algebraic reason why a naive quaternionic Gram factorization cannot make the entire Weil form positive by symmetry alone.

**Scope:** The pair calculation is exact algebra; it does not by itself produce an admissible test function whose *complete* Weil sum is negative. Turning it into the global RH-equivalent contradiction requires a localization/interpolation theorem for admissible Mellin transforms and control of all other zeros. Such localization is part of the classical proof of Weil's equivalence and must not be assumed from this toy block.

## 3. Quaternionic extension does not repair the signature

On a right quaternionic vector space \(\mathbb H^2\), the same Hermitian matrix \(J=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\) has \(J(1,1)^T=(1,1)^T\) and \(J(1,-1)^T=-(1,-1)^T\). Its quadratic form is \(2\Re(\overline v_1v_2)\), so the negative direction persists. Conjugating by a quaternionic unitary cannot change the signs of its eigenvalues. An invertible congruence also preserves inertia of a finite Hermitian form. Hence **a quaternionic change of coordinates cannot turn an indefinite off-line block into a positive norm-square**.

This does **not** rule out a genuinely new arithmetic operator whose exact completed form has an independently established positive structure; it rules out obtaining positivity by a bare quaternionic basis change or a sum-of-squares assertion for unrestricted off-line values.

## 4. Exact negative control and research implication

Chapter 24's modified entire function \(F_\epsilon(s)=\xi(s)[1+0.98\cosh(s-\tfrac12)]\) has explicit extra off-line zeros \(s=\tfrac12\pm b+i(2k+1)\pi\), \(b=\operatorname{arcosh}(1/0.98)\). Their reflected evaluation blocks have the same \(+1,-1\) signature. A putative universal “all even positive theta kernels have positive Weil form” claim would fail this algebraic test. This negative control is **not** a counterexample to RH for the genuine zeta function.

## 5. What a genuinely new factorization would require

An exact identity \(W_\xi(g,g)=\|Ag\|^2\) on all admissible tests, independently derived from the **original** theta/von Mangoldt coefficients, would imply RH. The preceding algebra shows why such an identity cannot arise from a generic symmetry argument: it would have to prove that the actual zero distribution has **no off-line reflection blocks**, or derive an independent structural property equivalent to that exclusion.

The next productive technical gate is not another finite matrix positivity check. It is an independently proved theta-arithmetic coercivity/interpolation bound for the *complete* Weil functional that survives all admissible tests, including high-frequency localization, and fails for the Chapter 24 control. A finite family of positive Gram matrices, an arbitrary positive jump operator, or a quaternionic similarity transform is insufficient.

**Outcome:** Direct finite-block Gram factorization fails for hypothetical off-line zeros; quaternionic scalar extension preserves that failure. The full all-test Weil positivity for xi remains open.

## 6. References

- Weil's positivity criterion as summarized in Chapter 33 and the cited Lagarias review.
- Chapter 24's explicit shifted-kernel control.
- Chapter 17's original theta growth and Toeplitz proof obligations.
