# 35 — Theta autocorrelation versus Weil positivity: a rigorous failure gate

**Date:** 2026-11-08. **Status:** exact operator calculation and negative control, no RH proof. Continues Chapters 17, 18, 24, 33–34.

## Question

Can the exact Jacobi-theta kernel supply the missing nonnegative quadratic form by autocorrelation, Fourier positivity, or a quaternionic Gram factorization? This tests a natural next attempt to exclude the negative directions of the full Weil form.

## 1. Exact positive-definite kernel from the theta transform

Let \(\Phi\) be the real, even, positive, rapidly decreasing Riemann theta Fourier kernel, with
\[
\Xi(t)=\int_{\mathbb R}\Phi(u)e^{itu}\,du.
\]
Define its autocorrelation \(C(v)=\int_{\mathbb R}\Phi(u)\Phi(u+v)\,du\). Since \(\Phi\) is even, \(C=\Phi*\Phi\). With the stated Fourier convention,
\[
\widehat C(t)=\Xi(t)^2=|\Xi(t)|^2\ge0\quad(t\in\mathbb R).
\]
Consequently, for any finite complex or quaternionic coefficients \(q_j\) and real shifts \(t_j\),
\[
\sum_{j,k}\overline{q_j}\,C(t_j-t_k)\,q_k\ge0.
\]
**Correction:** The displayed Gram positivity does *not* follow from \(\widehat C(t)\ge0\) with \(t_j\) interpreted as **frequency shifts** unless \(C\) is being evaluated as a function of the Fourier-dual variable; it does follow by Bochner/Plancherel from \(\widehat C\ge0\). Since \(\widehat C\) is real nonnegative, the quaternionic quadratic form is \(\int \widehat C(\omega)|\sum_j e^{i\omega t_j}q_j|^2\,d\omega/(2\pi)\) for a fixed imaginary unit \(i\). This is nonnegative for any quaternionic \(q_j\) because the real scalar weight is central and the quaternionic norm is positive. This is a true positive kernel, but not Weil's zero-sensitive form.

A second, simpler Gram construction uses \(\Phi(u)\ge0\):
\[
K(t)=\int_{\mathbb R}\Phi(u)e^{itu}\,du=\Xi(t),\quad
\sum_{j,k}\overline{q_j}K(t_j-t_k)q_k
=\int_{\mathbb R}\Phi(u)\left|\sum_j e^{-iut_j}q_j\right|^2du\ge0.
\]
Thus \(\Xi\) is positive-definite on the real line despite the fact that real-line positive-definiteness of an entire Fourier transform does not force all complex zeros to lie on the real line.

## 2. Negative control preserves both Gram positivities but has off-axis zeros

Let \(\Phi_\epsilon(u)=\Phi(u)+0.49[\Phi(u-1)+\Phi(u+1)]\). It remains real, even, strictly positive and rapidly decreasing. Its transform is
\[
\Xi_\epsilon(z)=\Xi(z)[1+0.98\cos z].
\]
The extra zeros at \(z=(2k+1)\pi\pm i\,\operatorname{arcosh}(1/0.98)\) are off the real axis and correspond to off-critical zeros of the modified completed function. Yet the Gram kernel \(\Xi_\epsilon(t)\) remains positive-definite because \(\Phi_\epsilon\ge0\). Its autocorrelation also has nonnegative Fourier transform \(|\Xi_\epsilon(t)|^2\).

**Result:** Theta positivity, ordinary Gram positivity, autocorrelation positivity, and their quaternionic scalar extensions cannot force the real-zero property. A candidate proof that equates these to complete Weil positivity is invalid.

## 3. What is still missing?

The Weil form is a zero-sensitive distributional quadratic form involving **all** prime powers, the reciprocal terms, the Gamma-factor/archimedean distribution, and pole terms. The positive Gram kernels above involve \(\Phi\) or \(\Phi*\Phi\) but do not have the complete Weil explicit-formula identity. They are positive for the shifted negative control, whereas Weil positivity fails for a completed function with off-axis zeros under the appropriate analogous zero criterion.

Any meaningful factorization must prove **both** an exact identity with the fully normalized Weil form and an independent nonnegative representation. Merely applying the word “quaternionic” or the norm-square identity to an arbitrary kernel does not satisfy either condition.

## 4. Next proof target: zero-sensitive arithmetic kernel

Derive the complete Weil form on a fixed compactly supported smooth Mellin test class, including the archimedean distribution, with all conventions and convergence justified. Attempt to decompose it into an explicit candidate positive part plus a signed remainder:
\[
\mathcal W(g)=\mathcal P(g)-\mathcal R(g).
\]
The new mathematical goal is to prove \(\mathcal R(g)\le\mathcal P(g)\) for **every** admissible \(g\), using the exact Jacobi theta arithmetic, and demonstrate failure for the shifted-kernel control. Such an inequality is currently unproved and RH-equivalent in strength. The next deliverable should be an explicit, independently verified remainder formula rather than an asserted factorization.

## Conclusion

A rigorous negative result: two natural theta/quaternionic Gram-factorization attempts are universally positive yet cannot discriminate the off-line-zero control. The mathematical obstacle is now isolated to a *zero-sensitive* arithmetic remainder in the full Weil form. RH remains unsolved.
