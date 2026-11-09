# 37 — Off-critical reciprocal Mangoldt harmonics: hyperbolic growth and a zero-exclusion no-go

**Date:** 2026-11-08. **Status:** Exact finite-mode test; no RH proof.

## Question

Can the reciprocal \(k\)-axis prime-power harmonics, together with the centered xi reflection, force the horizontal displacement \(a=\Re s-1/2\) of every nontrivial zero to vanish?

## 1. Complexified reciprocal pairing

Let \(z=a+it\), \(\ell_n=\log n\), \(c_n=\Lambda(n)/\sqrt n\). For finite cutoff \(N\),
\[
P_N(z)=\sum_{n=2}^N c_n(e^{z\ell_n}+e^{-z\ell_n})
=2\sum_{n=2}^N c_n\cosh(z\ell_n).
\]
This is an **entire even** function, \(P_N(-z)=P_N(z)\), and has real Taylor coefficients. On \(a=0\), \(P_N(it)=2\sum c_n\cos(t\ell_n)\) is real. For \(a\ne0\), each mode satisfies
\[
2\cosh((a+it)\ell)=2\cosh(a\ell)\cos(t\ell)
+2i\sinh(a\ell)\sin(t\ell).
\]
This is the appropriate complex-slice analytic continuation; replacing the commuting imaginary unit \(i\) by fixed quaternionic \(k\) changes notation, not the zeros. The imaginary part can cancel among modes. No termwise sign restriction on \(a\) follows.

The unregularized infinite series is not convergent on the critical line and grows rapidly for \(a\ne0\). Finite cutoffs are diagnostics, not completed zeta.

## 2. Exact off-axis zero counterexample with positive prime-power weights

Evenness and positive coefficients do **not** force zeros to the imaginary axis. Consider the *two-frequency positive reciprocal field*
\[
F(z)=2A\cosh(z\ell)+2B\cosh(2z\ell),\quad A,B>0.
\]
Write \(u=\cosh(z\ell)\), so \(\cosh(2z\ell)=2u^2-1\), and
\[
F(z)/2=2Bu^2+Au-B.
\]
The quadratic roots are \(u_\pm=(-A\pm\sqrt{A^2+8B^2})/(4B)\). The negative root is below \(-1\) precisely when \(A>B\), because \(u_-<-1\iff A>B\) (with equality at \(A=B\)). If \(A>B\), write \(u_-=-\cosh b\) for \(b>0\). Then
\[
z=\frac{\pm b+i(2m+1)\pi}{\ell}
\]
are off-axis zeros. Thus a positive two-mode reciprocal harmonic can have zeros with \(a\ne0\).

A **natural von Mangoldt example** uses the prime 2 and its square 4:
\[
\ell=\log2,\quad A=\frac{\Lambda(2)}{\sqrt2}=\frac{\log2}{\sqrt2},
\quad B=\frac{\Lambda(4)}{\sqrt4}=\frac{\log2}{2}.
\]
Here \(A>B>0\), and the exact off-axis zeros above exist. This counterexample uses **genuine** von Mangoldt weights for the first two prime powers, not arbitrary invented coefficients. They are zeros of the finite model \(F\), **not** of the completed xi function.

This proves that prime-power positivity, reciprocal reflection, and evenness are insufficient for zero exclusion, even with genuine coefficients at finite cutoff.

## 3. Why the full completion remains essential

The completed xi function has the exact reflection \(\xi(1/2+z)=\xi(1/2-z)\) and the exact theta integral. Its zero distribution is governed by the global completion, not any finite reciprocal prime sum. The functional equation permits hypothetical off-axis quartets; it does not exclude them.

The ordinary Dirichlet series \(\zeta(-s)=\sum n^s\) for \(\Re s<-1\) is **not** the same reflection as the xi functional equation \(s\mapsto1-s\). The latter includes Gamma and pole factors.

## 4. Next proof gate

Seek an inequality derived from the **full original theta kernel** or complete Weil distribution, with all prime powers, pole terms and archimedean terms, that fails for (a) the two-term von Mangoldt example above and (b) Chapter 24's positive-even shifted theta kernel. A valid criterion must constrain *all* spectral heights and cannot infer RH from symmetry or positivity of finite weights alone.

**Arithmetic goal:** \(39.5=79/2\) is prime in \(\mathbb Z[1/2]\), but no new Euler factor is introduced at 39.5.
