# 18 — Modular inversion is insufficient: an explicit off-line counterexample and an exact averaged growth law

**Date:** 2026-11-06.  
**Status:** Three rigorous *obstruction/baseline* theorems and reproducible numerical diagnostics, **not** a proof of the Riemann hypothesis.  
**Implements:** [Clay roadmap — 17](17-clay-statement-and-proof-roadmap.md), priority A1–A4.  
**Relevant prior calculations:** [theta Fourier kernel — 08](08-theta-kernel-zero-latitudes.md), [theta growth integral — 15](15-higher-moment-growth-certificate.md), [two zero-spheres — 16](16-two-fold-zero-spheres-and-theta-positivity.md).

## Executive finding

The Jacobi modular inversion condition, positivity, evenness, and strong kernel decay **do not imply** all Fourier zeros are real. This note gives a completely explicit family built **from the exact Riemann theta kernel** for which those properties survive, but an entire auxiliary factor introduces nonreal zeros **inside** the RH strip \(|\Im z|<1/2\). A second constructive theorem shows that even preserving the *entire tail* of the theta kernel outside a compact interval would not be enough. The actual theta *arithmetic content*—its full special series, not just inversion or tails—must enter any valid global positivity proof.

We also derive an **unconditional positive law after averaging over all spectral heights**. This is a genuine global positivity theorem from the theta kernel, but it is weaker than the *pointwise* positivity required for RH. A separate Riemann–Lebesgue observation rules out any proposed fixed positive lower bound uniform in height.

## 1. Source and normalization audit

Use the completed xi function

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\quad
\Xi(z)=\xi(\tfrac12+iz).
\]

The exact classical Fourier formula (Romik, eqs. (1.6)–(1.11)) is

\[
\Xi(z)=\int_{-\infty}^{\infty}\Phi(u)e^{izu}\,du
=2\int_0^\infty\Phi(u)\cos(zu)\,du,
\]

where

\[
\Phi(u)=\sum_{n\ge1}
\left(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2}\right)
e^{-\pi n^2e^{2u}}.
\]

It is real, even, strictly positive and rapidly decreasing. Let

\[
\Theta(v)=\sum_{n\in\mathbb Z}e^{-\pi n^2v},
\qquad
\omega(v)=v^2\Theta''(v)+\tfrac32v\Theta'(v).
\]

Then \(\Phi(u)=2e^{u/2}\omega(e^{2u})\), and the Jacobi inversion gives

\[
\Theta(1/v)=\sqrt v\,\Theta(v),\qquad
\omega(1/v)=\sqrt v\,\omega(v),\qquad
\Phi(-u)=\Phi(u).
\]

**Normalization warning:** Some literature divides \(\Phi\) by two and writes different front factors. We use the full Fourier normalization above, identical to [08](08-theta-kernel-zero-latitudes.md) and Dan Romik.

Independent 35-digit sample check (8 theta terms on \(u\ge0\)):

\[
2\int_0^\infty\Phi(u)\cos((3.5+0.23i)u)\,du
-\xi\bigl(\tfrac12+i(3.5+0.23i)\bigr)
\approx 0
\]

at the displayed numerical precision. Finite quadrature is not an interval proof; the exact Fourier identity is classical.

## 2. Theorem A — an explicit modular-inversion no-go construction

For any \(b>0\) and \(0<\varepsilon<1/2\), define

\[
\boxed{\Psi_{\varepsilon,b}(u)
=\Phi(u)+\varepsilon[\Phi(u-b)+\Phi(u+b)].}
\]

**Claims, proved directly:**

1. \(\Psi\) is **strictly positive, real, even, \(C^\infty\)** and super-exponentially decreasing in both tails.
2. The associated Mellin kernel
   \[
   \omega_{\varepsilon,b}(v)
   =\tfrac12 v^{-1/4}\Psi_{\varepsilon,b}(\tfrac12\log v)
   \]
   satisfies the **same weight-\(\tfrac12\) inversion law** as the original \(\omega\):
   \[
   \boxed{\omega_{\varepsilon,b}(1/v)
   =\sqrt v\,\omega_{\varepsilon,b}(v),\quad v>0.}
   \]
3. The Fourier transform factors **exactly** by the Fourier shift identity:
   \[
   \boxed{
   \widehat\Psi_{\varepsilon,b}(z)
   =[1+2\varepsilon\cos(bz)]\,\Xi(z).
   }
   \]
4. Regardless of whether RH is true, \(\widehat\Psi\) has the explicit nonreal zeros
   \[
   \boxed{
   z_k^\pm=\frac{(2k+1)\pi}{b}
   \pm\frac{i}{b}\operatorname{arcosh}\!\left(\frac{1}{2\varepsilon}\right),
   \quad k\in\mathbb Z.
   }
   \]

**Proof.** Positivity follows term by term because \(\Phi>0\), and the two shifts preserve smoothness and rapid decay. Evenness is immediate from \(\Phi(-u)=\Phi(u)\). For \(v>0\),

\[
\begin{aligned}
\omega_{\varepsilon,b}(1/v)
&=\tfrac12 v^{1/4}
 \Psi_{\varepsilon,b}(-\tfrac12\log v)\\
&=\tfrac12 v^{1/4}
 \Psi_{\varepsilon,b}(\tfrac12\log v)
=\sqrt v\,\omega_{\varepsilon,b}(v).
\end{aligned}
\]

By translation of Fourier integrals, each shifted copy contributes
\(e^{\pm ibz}\Xi(z)\); their sum gives \(1+2\varepsilon\cos(bz)\). At
\(z=(2k+1)\pi/b+i\eta/b\), \(\cos(bz)=-\cosh\eta\); choosing
\(\eta=\operatorname{arcosh}(1/(2\varepsilon))\) gives an exact zero. The negative-imaginary counterpart follows by conjugation. QED.

**Concrete critical-strip counterexample:**

\[
b=1,\quad\varepsilon=0.49,\quad
\boxed{z=\pi\pm0.201688487798836053004338678586\,i}.
\]

These zeros obey \(0<|\Im z|<1/2\). The new transform is *not* the Riemann \(\Xi\); we have **not** found off-line zeta zeros. The construction refutes any attempted RH argument that uses **only** positivity, evenness, smooth decay and the weight-\(\tfrac12\) inversion equation.

**Scope caution:** \(\omega_{\varepsilon,b}\) obeys the inversion identity, but is **not** the original Jacobi theta derivative series. The construction does not refute a proof that genuinely uses all arithmetic information in \(\Theta(v)=\sum_ne^{-\pi n^2v}\).

## 3. Theorem B — even the complete theta tail and inversion do not suffice

This strengthens the obstruction beyond the large-\(u\) tail, while making no claim about preserving the full theta series.

Choose an even, smooth, nonnegative, nonzero bump \(g\) supported sufficiently close to zero so that its Fourier transform \(\widehat g(z)\) does not vanish at

\[
z_0=\pi+i\operatorname{arcosh}(50/49).
\]

Such a bump exists: as the support shrinks, \(\widehat g(z_0)\) approaches the positive mass \(\int g\) after normalization. Put

\[
h(u)=g(u)+0.49[g(u-1)+g(u+1)].
\]

Then \(h\) is even, \(C^\infty\), nonnegative and compactly supported; its Fourier transform is

\[
\widehat h(z)=\widehat g(z)(1+0.98\cos z).
\]

Thus \(\widehat h\) has a **simple nonreal zero** at \(z_0\), with \(0<\Im z_0<1/2\), since \(\widehat g(z_0)\ne0\) and \(\sin z_0\ne0\).

For \(M>0\), set \(\Psi_M(u)=\Phi(u)+M h(u)\). This is **strictly positive and even**. Furthermore, **outside the compact support of \(h\), \(\Psi_M(u)=\Phi(u)\) exactly**, so all original positive and negative theta tails, not merely their leading asymptotics, are unchanged. Its associated \(\omega_M(v)=\tfrac12v^{-1/4}\Psi_M(\tfrac12\log v)\) still obeys the exact inversion relation.

Pick a small disk \(D\) around \(z_0\) lying strictly inside \(0<\Im z<1/2\), such that \(\widehat h\) has exactly one zero in \(D\) and no boundary zero. On \(\partial D\), \(|\widehat h|\) has a positive minimum and \(|\Xi|\) a finite maximum. For sufficiently large \(M\),

\[
|\Xi(z)|<M|\widehat h(z)|\quad(z\in\partial D).
\]

**Rouché's theorem** now proves that \(\Xi(z)+M\widehat h(z)=\widehat\Psi_M(z)\) also has exactly one nonreal zero in \(D\).

**Conclusion:** No argument resting solely on *positivity + evenness + weight-\(\tfrac12\) inversion + exact agreement with theta tails outside a compact set* can prove RH. The full arithmetic behavior of the **actual** kernel over its entire domain matters.

## 4. Theorem C — a genuine global positivity law, but only on average

Define the **spectrally integrated** squared modulus

\[
\boxed{E(y)=\int_{-\infty}^{\infty}|\Xi(x+iy)|^2\,dx.}
\]

Since
\(\Xi(x+iy)=\int_{\mathbb R}\Phi(u)e^{ixu-yu}\,du\),
Plancherel's identity (Fourier convention as in §1) gives

\[
\boxed{
E(y)=2\pi\int_{\mathbb R}\Phi(u)^2e^{-2yu}\,du
=4\pi\int_0^\infty\Phi(u)^2\cosh(2yu)\,du.
}
\]

Differentiate under the integral (justified by theta super-exponential decay):

\[
\boxed{
E'(y)=8\pi\int_0^\infty u\Phi(u)^2\sinh(2yu)\,du>0
\qquad(y>0),
}
\]

and

\[
\boxed{
E''(y)=16\pi\int_0^\infty u^2\Phi(u)^2\cosh(2yu)\,du>0
\qquad(y\in\mathbb R).
}
\]

Therefore **the aggregate spectral energy is strictly convex and grows away from the critical line**. This is an unconditional theta-kernel positivity theorem, requiring **no RH assumption**.

However, the same averaged positivity holds for the perturbed \(\Psi_{\varepsilon,b}\) and \(\Psi_M\) kernels above, which have explicit nonreal zeros. So **average growth is not a pointwise zero-exclusion theorem**. An attempted proof must control each \(x\), not only its integral.

Numerical theta-quadrature illustrations (35-digit arithmetic, not interval-certified):

| \(y\) | \(E(y)\) | \(E'(y)\) |
| ---: | ---: | ---: |
| 0 | 2.00905988686130880796 | 0 |
| 0.2 | 2.01301423079197293470 | 0.03958059792880788872 |
| 0.5 | 2.03389684916017308159 | 0.09993213309261361358 |

### No uniform positive height-independent margin

For each **fixed** \(y\), the Riemann–Lebesgue lemma gives

\[
\Xi(x+iy)\to0,\qquad
\partial_y\Xi(x+iy)\to0
\quad (|x|\to\infty),
\]

because \(\Phi(u)e^{-yu}\) and \(u\Phi(u)e^{-yu}\) are both integrable. Hence

\[
\boxed{
\partial_y|\Xi(x+iy)|^2\longrightarrow0
\quad (|x|\to\infty)
}
\]

**unconditionally**. Thus no theorem of the form
\(\partial_y|\Xi(x+iy)|^2\ge c(y)>0\) independent of all \(x\) can hold. When we say a target sign estimate is **global in spectral height**, this means **valid at every \(x\)**, not bounded below by an \(x\)-independent positive number.

This provides an explicit **failure gate** for an overly strong candidate lemma in the Clay roadmap.

## 5. Additional obstruction — log-concavity and the first Laguerre inequality are not enough

For a positive normalized Gaussian \(g_\sigma(u)\) of standard deviation \(\sigma\), consider

\[
K(u)=g_\sigma(u)+\varepsilon[g_\sigma(u-1)+g_\sigma(u+1)],
\quad \varepsilon=0.49,\ \sigma=8.
\]

Its Fourier transform is

\[
F(z)=e^{-\sigma^2z^2/2}(1+2\varepsilon\cos z),
\]

so it **also** has nonreal zeros \(z=\pi\pm0.20168848\ldots i\).

Nonetheless, \(K\) is **strictly log-concave**. Factoring out the central Gaussian, the second logarithmic derivative is

\[
(\log K)''(u)
=-\frac1{\sigma^2}+\frac{\operatorname{Var}_{p_u}(\mu)}{\sigma^4},
\quad \mu\in\{-1,0,1\}.
\]

Since the conditional variance of a variable supported on \([-1,1]\) is at most \(1\),

\[
(\log K)''(u)
\le-\frac1{64}+\frac1{4096}
=-\frac{63}{4096}<0.
\]

Even **the first Laguerre inequality** holds strictly for **all real \(x\)**:

\[
L_1[F](x)=F'(x)^2-F(x)F''(x)>0.
\]

Indeed, if \(h(x)=1+2\varepsilon\cos x\), then

\[
L_1[F](x)=e^{-\sigma^2x^2}
\left[(h')^2-hh''+\sigma^2h^2\right].
\]

We have
\((h')^2-hh''=4\varepsilon^2+2\varepsilon\cos x\) and
\(h(x)\ge1-2\varepsilon\). Therefore

\[
e^{\sigma^2x^2}L_1[F](x)
\ge4\varepsilon^2-2\varepsilon+\sigma^2(1-2\varepsilon)^2
=0.006>0.
\]

This underscores that even strict positive curvature of the real-axis modulus, as captured by the **first** Laguerre inequality, does not enforce the full complex zero-location theorem.

**Caveat:** this Gaussian Fourier transform has entire order 2, whereas \(\Xi\) has order 1. The example refutes the proposed bare log-concavity/first-Laguerre mechanism, **not** every argument that additionally requires xi's precise order or theta arithmetic.

For real-entire \(F\), the small-transverse expansion is

\[
\partial_y|F(x+iy)|^2
=2y\bigl[F'(x)^2-F(x)F''(x)\bigr]+O(y^3),
\]

so first-Laguerre positivity controls only a **local** transverse derivative and does not imply positivity for all \(0<y\le1/2\).

## 6. Audit of the existing signed theta-growth expression

With \(C,S\) as in [15](15-higher-moment-growth-certificate.md), the normalization is

\[
\Xi(x+iy)=2(C-iS),\qquad
G(x,y)=CC_y+SS_y=\tfrac18\partial_y|\Xi(x+iy)|^2.
\]

The exact symmetrized double integral is

\[
\begin{aligned}
G(x,y)&=\tfrac14\int_0^\infty\int_0^\infty \Phi(u)\Phi(v)
\left[(u+v)\sinh(y(u+v))\cos(x(u-v))\right.\\
&\hspace{5.3em}\left.+(u-v)\sinh(y(u-v))\cos(x(u+v))\right]du\,dv.
\end{aligned}
\]

The factor \(1/4\) is consistent with the half-line normalization and product-to-sum identities. This identity gives a **signed cosine integral**. Replacing all cosines by \(+1\), inferring that each frequency block is positive, or applying a positive-kernel result without checking Fourier oscillation signs would be invalid.

## 7. What changed in the proof strategy

**Eliminated insufficient ideas:**

1. Two reflection folds, the quartet polynomial, or the quaternionic zero-sphere lift alone.
2. Kernel positivity, evenness and modular inversion alone (Theorem A).
3. Matching theta tails and modular inversion alone (Theorem B).
4. Positivity of the \emph{height-averaged} growth (Theorem C).
5. Log-concavity of a positive even kernel and its first real-axis Laguerre inequality (Gaussian example).
6. Any pointwise lower bound with a strictly positive margin **independent of height**.

**Next research lemma must be genuinely theta-specific.** The original kernel is not an arbitrary positive even transform:

\[
\Phi(u)=\sum_{n=1}^\infty
(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2})
e^{-\pi n^2e^{2u}}.
\]

A useful candidate would derive a sign-controlled expression for the **entire** bilinear growth integral from the discrete \(n^2\) arithmetic/Poisson structure, rather than from just inversion. One possible strategy is to obtain a globally convergent signed series grouped by lattice indices \((m,n)\), then prove the **whole grouped expression** is positive at every spectral height \(x\) and \(0<y\le1/2\). Pairwise nonnegativity is **not** assumed, and no such theorem is known here.

Alternatively, derive a true \(\mathrm{PF}_\infty\) Toeplitz factorization directly from the theta coefficients. This remains a separate RH-equivalent open objective, not something supplied by this note.

**Acceptance conditions for the next lemma:** the derivation must use a property that the shift and compact-bump kernels violate; it must address all real heights without an impossible fixed positive margin; it must account for arbitrary positive \(y\) in the strip; and it cannot assume zero-freeness.

## 8. Reproducibility and sources

- [Experiment](../experiments/modular_symmetry_obstruction.py), [six regression tests](../tests/test_modular_symmetry_obstruction.py), [saved numerical diagnostics](../results/modular_symmetry_obstruction.json). Finite theta sums are evaluated on \(u\ge0\) with **evenness imposed before numerical summation**, avoiding inaccurate truncation on negative \(u\). The exact theorems do not depend on finite truncations.
- Dan Romik, *Orthogonal polynomial expansions for the Riemann xi function*, introduction equations (1.6)–(1.11), https://math.ucdavis.edu/~romik/data/uploads/papers/riemannxi.pdf
- Jonathan Sondow and Cristian Dumitrescu, *A monotonicity property of Riemann's xi function and a reformulation of the Riemann Hypothesis*, https://arxiv.org/abs/1005.1104
- [15 — previous local growth certificates](15-higher-moment-growth-certificate.md)
- [16 — quaternionic symmetry and growth equivalences](16-two-fold-zero-spheres-and-theta-positivity.md)
- [17 — exact Clay statement and roadmap](17-clay-statement-and-proof-roadmap.md)

**Verdict:** the first Clay-aligned research milestone is completed as a **rigorous obstruction report plus an unconditional averaged positivity theorem**, not as an all-height pointwise positivity proof. The next task is to extract a stronger arithmetic sign mechanism from the **exact** Jacobi-theta series.
