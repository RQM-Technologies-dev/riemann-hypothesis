# 38 — Theta-kernel positive definiteness is not zero-location positivity

**Date:** 2026-11-08. **Question:** Can the exact Jacobi-theta kernel, reciprocal von Mangoldt harmonics, and quaternionic k-axis yield a positivity theorem that forces all zeros onto the critical line?

## 1. Genuine theta positivity

Write \(\Xi(t)=\xi(1/2+it)=\int_{\mathbb R}\Phi(v)e^{itv}dv\), with the usual normalization and an even nonnegative rapidly decreasing Riemann theta kernel \(\Phi\). For any real \(t_1,\dots,t_m\) and complex \(c_1,\dots,c_m\),
\[
\sum_{j,l}c_j\overline{c_l}\Xi(t_j-t_l)
=\int_{\mathbb R}\Phi(v)\left|\sum_j c_j e^{it_jv}\right|^2dv\ge0.
\]
This is positive definiteness in the sense of Bochner. It is an exact theorem and uses positivity of the genuine theta kernel. Its quaternionic fixed-slice analogue follows by replacing complex \(i\) with a fixed imaginary unit \(k\); the result remains a real nonnegative scalar for slice coefficients. This is **not** the RH-equivalent Weil positivity criterion.

## 2. Strong negative control from the existing positive theta perturbation

Let \(0<\varepsilon<1/2\), and set
\[
\Phi_\varepsilon(v)=\Phi(v)+\varepsilon\bigl(\Phi(v-1)+\Phi(v+1)\bigr).
\]
Because \(\Phi\ge0\), also \(\Phi_\varepsilon\ge0\), and it is even. Therefore \(\Xi_\varepsilon(t)=\Xi(t)(1+2\varepsilon\cos t)\) is likewise positive definite by exactly the same proof.

Take \(\varepsilon=0.49\). Then \(1+0.98\cos z\) has off-real zeros
\[
z=(2m+1)\pi\pm i b,\qquad b=\operatorname{arcosh}(1/0.98)>0.
\]
Consequently \(\Xi_\varepsilon\) is positive definite on the real line yet has off-real complex zeros. In \(s=1/2+iz\), these become off-critical zeros of the **modified** completed function, not of the original xi.

Thus **positive definiteness of the theta transform, evenness, reciprocal reflection, and a smooth compactified pole do not imply RH**. This control preserves theta-kernel positivity, but not the exact original theta arithmetic and modular identities.

## 3. Why this is a more discriminating test

The prime-translation Laplacian of Chapter 34 is positive for arbitrary positive coefficients; that positivity was nonselective. Here even the *true* theta Fourier representation gives a positive-definite function, but the off-axis control still passes. A proposed quaternionic proof cannot rely only on (i) nonnegative theta kernel, (ii) Fourier positive definiteness, (iii) reflection, or (iv) compactified-pole smoothness.

The remaining candidate input is an **arithmetic-specific** constraint of the *unmodified* Jacobi theta lattice, e.g. its exact Poisson/modular relation together with the complete Weil formula. However, their established identities do not presently provide an unconditional proof of the RH-equivalent Weil positivity criterion. Rewriting them in the k-coordinate is a unitary coordinate change, not a new theorem.

## 4. Next research gate

Find a property \(P\) of the exact original theta kernel that is (a) provable independently from its integer-square coefficients and Poisson summation, (b) not shared by \(\Phi_\varepsilon\), and (c) mathematically sufficient to force the *complete* Weil quadratic form nonnegative for all admissible tests. Demonstrating (a) and (b) alone is insufficient: (c) is the unsolved part. A rigorous proof must address arbitrary spectral height, not finitely many Gaussian checks.

**Status:** Strong negative-control result; no RH proof or new zero-exclusion theorem.

**Arithmetic goal retained:** \(39.5=79/2\) is prime in \(\mathbb Z[1/2]\), not a new Euler-product prime index.
