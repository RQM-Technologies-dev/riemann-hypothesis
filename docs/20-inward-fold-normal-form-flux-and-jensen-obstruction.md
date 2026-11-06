# 20 — Inward phase-separation audit: fold normal form, zero flux, and the Jensen obstruction

**Date:** 2026-11-06  
**Status:** New-to-this-repository exact derivations, numerical diagnostics, and a proof-strategy obstruction. **No global phase-separation law or RH proof has been found.**

**Research question:** Does the **actual** Jacobi-theta kernel force the two reflected Xi channels to remain separated as the transverse coordinate \(a\) moves continuously from the known outer boundary \(a=\tfrac12\) toward the critical fold \(a=0\)?

**Finding:** The fold has a precise two-channel normal form relating zeros of \(\Xi\) to critical points of \(\Xi\), and the paired system has a quantized zero-counting flux. However, differentiating the Wronskian produces a *known Jensen criterion equivalent to RH* rather than an unconditional sign theorem. Positivity at the fold, even for every real height, is demonstrably insufficient to prevent off-line collisions. The needed all-height theta-specific inequality remains unproved.

Read with [17 — exact Clay objective](17-clay-statement-and-proof-roadmap.md), [18 — mirror channels](18-mirror-channel-folding-and-zero-collision.md), [19 — first inward scan](19-folded-channel-inward-deformation-and-wronskian.md), [15 — signed theta bilinear form](15-higher-moment-growth-certificate.md).

## 1. Variables and exact channel decomposition

\[
\Xi(z)=\xi(\tfrac12+iz)=2\int_0^\infty\Phi(u)\cos(zu)\,du.
\]

Write \(z=t+ia\), where \(t\) is **spectral height** and \(a\) is the distance from the critical fold; \(s=\tfrac12-a+it\). Let

\[
C(t,a)=\int_0^\infty\Phi(u)\cos(tu)\cosh(au)\,du,\quad
S(t,a)=\int_0^\infty\Phi(u)\sin(tu)\sinh(au)\,du.
\]

Then \(\Xi(t+ia)=2(C-iS)\), with \(C(t,-a)=C(t,a)\) and \(S(t,-a)=-S(t,a)\). The Cauchy–Riemann equations give \(C_a=S_t\) and \(S_a=-C_t\).

**The reflection fold does not simply add two zero-spheres.** Away from \(a=0\), a zero requires the **simultaneous** two-channel cancellation \(C(t,a)=S(t,a)=0\). At the fold \(S(t,0)=0\) identically, so a critical-line zero only requires \(C(t,0)=0\).

## 2. Exact fold normal form: the odd channel becomes the derivative

Taylor expand the **same entire function** at real \(t\), uniformly on every compact real-\(t\) set as \(a\to0\):

\[
\begin{aligned}
C(t,a)&=\tfrac12\Xi(t)-\tfrac{a^2}{4}\Xi''(t)
 +\tfrac{a^4}{48}\Xi^{(4)}(t)+O(a^6),\\
S(t,a)&=-\tfrac a2\Xi'(t)+\tfrac{a^3}{12}\Xi'''(t)
 -\tfrac{a^5}{240}\Xi^{(5)}(t)+O(a^7).
\end{aligned}
\]

Therefore

\[
\boxed{C(t,0)=\tfrac12\Xi(t),\qquad
\lim_{a\to0}S(t,a)/a=-\tfrac12\Xi'(t).}
\tag{F1}
\]

**Interpretation:** the two folded cancellation families connect **zeros of \(\Xi\)** to **stationary points of \(\Xi\)**. This is a precise version of the user's superposed/reflected-sphere intuition, not a claim of two quantum wavefunctions interfering in physical time.

### Motion of the two families near the fold

Suppose \(\gamma\) is a simple real zero \(\Xi(\gamma)=0\), \(\Xi'(\gamma)\ne0\). The analytic implicit-function theorem gives a nearby real root of \(C(\cdot,a)\), even in \(a\), satisfying

\[
\boxed{t_C(a)=\gamma+
 \frac{a^2}{2}\frac{\Xi''(\gamma)}{\Xi'(\gamma)}
 +O(a^4).}
\tag{F2}
\]

Suppose \(\tau\) is a nondegenerate real stationary point \(\Xi'(\tau)=0\), \(\Xi''(\tau)\ne0\). The normalized odd channel \(S(t,a)/a\) extends evenly and analytically across \(a=0\). Its nearby real zero is

\[
\boxed{t_S(a)=\tau+
 \frac{a^2}{6}\frac{\Xi'''(\tau)}{\Xi''(\tau)}
 +O(a^4).}
\tag{F3}
\]

These formulas establish **local persistence**, not a common height-independent lower bound on separation. If all Xi zeros were simple and real, familiar derivative interlacing would be available; asserting that everywhere would presuppose the key RH-level property.

**Independent 40-digit finite numerics (not interval certificates):**

\[
\gamma=14.13472514173469379046\ldots,\quad
\tau=15.58570858982934234460\ldots
\]

| \(a\) | \(t_C(a)\) | \(t_S(a)\) | separation \(t_S-t_C\) | residual in (F2) | residual in (F3) |
|---:|---:|---:|---:|---:|---:|
| 0.05 | 14.133275914014705 | 15.585233681898323 | 1.451957767884 | \(-1.51\cdot10^{-7}\) | \(-5.99\cdot10^{-9}\) |
| 0.10 | 14.128926419126499 | 15.583808886273148 | 1.454882467147 | \(-2.42\cdot10^{-6}\) | \(-9.58\cdot10^{-8}\) |
| 0.20 | 14.111501479886300 | 15.578108631388779 | 1.466607151502 | \(-3.84\cdot10^{-5}\) | \(-1.53\cdot10^{-6}\) |

The residuals exhibit the predicted \(O(a^4)\) scaling for these simple roots.

## 3. The Wronskian and why its first derivative is not a new shortcut

Define the phase-current or channel Wronskian

\[
J(t,a)=C S_t-S C_t.
\]

By analyticity,

\[
\boxed{J=CC_a+SS_a=\tfrac18\,\partial_a|\Xi(t+ia)|^2.}
\tag{W1}
\]

A second differentiation gives

\[
\boxed{
\partial_aJ=C_t^2+S_t^2-CC_{tt}-SS_{tt}
=\tfrac14\left(
|\Xi'(z)|^2-\operatorname{Re}(\Xi(z)\overline{\Xi''(z)})
\right),\quad z=t+ia.
}
\tag{W2}
\]

At the fold \(J(t,0)=0\), and

\[
\boxed{\partial_aJ(t,0)=
\tfrac14[\Xi'(t)^2-\Xi(t)\Xi''(t)].}
\tag{W3}
\]

The bracket is the **first real Laguerre inequality**. A more complete expansion is

\[
J(t,a)=
\frac a4(\Xi'^2-\Xi\Xi'')+
\frac{a^3}{24}\bigl(3\Xi''^2+\Xi\Xi^{(4)}-4\Xi'\Xi'''\bigr)
+O(a^5),
\tag{W4}
\]

where all derivatives on the right are evaluated at real \(t\).

### Exact Jensen obstruction

Csordas–Varga (1989), Theorem 2.2 (quoting Jensen), states that for a suitable **real entire function of genus at most one**, membership in the Laguerre–Pólya class is equivalent to

\[
|f'(z)|^2-\operatorname{Re}(f(z)\overline{f''(z)})\ge0
\quad\text{for every complex }z.
\]

Since \(\Xi\) is real entire of genus at most one, requiring the right side of (W2) nonnegative **globally at all \(z\)** is **equivalent to RH**, not a consequence of merely differentiating the theta integral. The restricted all-height condition \(\partial_aJ\ge0\) on \(0<a\le\tfrac12\) would likewise imply RH: integrate from \(J(t,0)=0\) to obtain \(J(t,a)\ge0\); any off-line zero forces \(J(t_0,a)<0\) just below its height \(a_0\) (proved in [19](19-folded-channel-inward-deformation-and-wronskian.md)). Conversely RH implies the global Jensen inequality.

This closes a **proof-strategy loophole**: substituting the complex Jensen inequality for the missing theta sign lemma silently assumes an RH-equivalent assertion.

### A new explicit counterexample to positivity *only at the fold*

Take a real even entire function of order one

\[
f(z)=(z^2+b^2)\cos(kz),\qquad b=\tfrac15,\quad k=8.
\]

It has **off-real zeros** \(z=\pm i/5\), well inside the RH strip \(|\Im z|<1/2\). However for every *real* \(t\),

\[
\boxed{
f'(t)^2-f(t)f''(t)
= k^2(t^2+b^2)^2+2(t^2-b^2)\cos^2(kt)
\ge 0.0224>0.
}
\tag{N1}
\]

The bound follows by splitting \(t^2\ge b^2\) (both summands nonnegative) and \(t^2<b^2\) (first \(\ge k^2 b^4=0.1024\), second \(\ge-2b^2=-0.08\)). This example is **not the original Xi function**, nor is it asserted to arise from a positive theta kernel. It proves that (W3) can hold **strictly at every real height** in the class of real even entire functions of order one **while nonreal zeros exist**.

The fold curvature or infinitesimal phase separation therefore cannot, by itself, settle RH. A theorem controlling the **whole inward deformation \(0<a\le1/2\)** is essential.

## 4. A conserved topological zero flux

Away from Xi zeros define

\[
U(t,a)=\log|\Xi(t+ia)|.
\]

It is harmonic wherever \(\Xi\ne0\). At a zero \(z_\rho=t_\rho+ia_\rho\) of multiplicity \(m_\rho\), the logarithm has the local singularity \(m_\rho\log|z-z_\rho|\). As a distribution,

\[
\boxed{(\partial_t^2+\partial_a^2)U
=2\pi\sum_{\rho}m_\rho\,\delta_{(t_\rho,a_\rho)}.}
\tag{T1}
\]

For any positively oriented rectangle \(R\) whose boundary contains no zero, Stokes' theorem yields

\[
\boxed{
\oint_{\partial R}
\left(U_t\,da-U_a\,dt\right)
=2\pi N_R,
}
\tag{T2}
\]

where \(N_R\in\mathbb Z_{\ge0}\) is **the number of Xi zeros inside, counted with multiplicity**. This is exactly the argument principle expressed as a flux; it is **not a new RH theorem**.

**Meaning for the folded zero-spheres:** every enclosed zero contributes the **same positive integer charge**. Mirror partners do **not** cancel each other as positive and negative vortices. A quartet at \(z=\pm t_0\pm ia_0\) contributes four charges inside a contour surrounding all four; two charges in the upper-half spectral plane. The symmetry determines the pairing, while the *absence* of off-fold charges is still the problem to prove.

The count is invariant under continuous contour deformation **provided no zero crosses the contour**. Starting at a zero-free outer boundary \(a=1/2\) does not establish zero-freeness of every smaller \(a\): zeros inside a newly expanded strip are precisely the undetermined flux.

### In-session diagnostic of topological charges

A numerical argument-principle winding computation (40 digits, 60 samples per edge; **not interval certified**) gave:

| Entire function | Rectangle \((t_{\min},t_{\max})\times(a_{\min},a_{\max})\) | Observed winding |
|---|---|---:|
| Original \(\Xi\) | \([2.4,3.8]\times[0.05,0.45]\) | 0 |
| Modified \(\Xi(z)[1+0.98\cos z]\) | \([2.4,3.8]\times[0.05,0.45]\) | 1 |
| Same modified function | \([-3.8,3.8]\times[0.05,0.45]\) | 2 |
| Same modified function | \([-3.8,3.8]\times[-0.45,0.45]\) | 4 |

The modified factor has explicit nonreal zeros at \(z=(2k+1)\pi\pm i\operatorname{arcosh}(1/0.98)\); the values 1, 2, and 4 test exactly the mirrored contributions. Winding for finite sampled contours is only a diagnostic until a boundary nonvanishing and phase-step enclosure are certified. These extra zeros belong **only to the modified kernel**, not to Riemann Xi.

Source code: [phase/fold/winding experiment](../experiments/folded_channel_flux_and_limits.py). Saved output: [finite numerical JSON](../results/folded_channel_flux_and_limits.json).

## 5. What the theta modular relation does and does not buy us

The Jacobi identity \(\vartheta(x)=x^{-1/2}\vartheta(1/x)\) is essential in constructing the **specific** even kernel \(\Phi(u)\). In logarithmic variables it manifests as reflection symmetry. The equality \(\Phi(u)=\Phi(-u)\) yields channel parity and (F1)–(W4), but those identities also hold for arbitrary even sufficiently decaying kernels. They do **not** establish the sign of \(J\), the full Jensen inequality, or a zero-flux exclusion.

The negative-control kernel \(\Phi_\varepsilon=\Phi+\varepsilon[\Phi(u-1)+\Phi(u+1)]\) remains positive and even (hence the same **log-coordinate reflection** property) while its transform \(\Xi(z)(1+2\varepsilon\cos z)\) has nonreal zeros. It does **not** preserve the exact theta series and coefficient arithmetic of the original kernel.

A new usable lemma must rely on information not shared by this negative control: e.g., a verified inequality derived from the exact theta series/prime-related identities, a genuinely sign-definite modularly paired oscillatory integral, or a rigorous all-height boundary-phase estimate.

## 6. Next proof obligation and experimental gates

**Chosen working target:**

> Find an unconditional theta-specific estimate that controls the *integrated inward phase flux* for all real spectral heights, strong enough to show no interior zeros occur in \(0<a<1/2\). Equivalently, establish strict sign preservation \(J(t,a)>0\) there, or prove all enclosed zero counts in (T2) vanish.

Do **not** relabel the desired result as a new proof merely by imposing \(J_a\ge0\) everywhere: Jensen's theorem identifies that as an RH-equivalent condition.

Next finite work package:

1. Audit the exact \(\Phi\) theta-series normalization, derivative identities, and modular transformation against [08](08-theta-kernel-zero-latitudes.md); distinguish parity consequences from identities requiring the precise \(n^2\) arithmetic series.
2. Derive a candidate **nonlocal, modularly paired** bound for (W1), rather than only the infinitesimal real-axis coefficient (W3). Test it against the explicit order-one counterexample (N1) and against the modified positive kernel from [19].
3. Use the flux identity (T2) to translate a **proved uniform boundary phase estimate** into a zero-count theorem. Do not infer zero count from a finite numerical winding check.
4. Preserve quaternionic interpretation as an output: zero-free off the fold implies the reflected spherical zero sets coincide at \(a=0\); their quartic perfect square is a consequence, not a premise. The separate Cayley \(S^3\) scale \(L>0\) remains symbolic.
5. Record a full failure/counterexample report if no genuinely theta-specific global sign inequality survives.

## 7. Sources

- G. Csordas and R. S. Varga, "Fourier Transforms and the Hermite–Biehler Theorem", *Proc. Amer. Math. Soc.* **107** (1989), 645–652, especially Theorem 2.2 (complex Jensen criterion), Theorem 2.4, Proposition 3.1; https://doi.org/10.2307/2048160.
- J. Sondow and C. Dumitrescu, "A monotonicity property of Riemann's xi function and a reformulation of the Riemann hypothesis", https://arxiv.org/abs/1005.1104.
- DLMF §25.10, zeros of the Riemann zeta function, https://dlmf.nist.gov/25.10.
- [17 — Clay statement](17-clay-statement-and-proof-roadmap.md), [18 — folded two-channel framework](18-mirror-channel-folding-and-zero-collision.md), [19 — initial Wronskian study](19-folded-channel-inward-deformation-and-wronskian.md).

**Conclusion:** There is a rigorous mathematical meaning to the proposed fold: one channel tends to \(\Xi\), the other (after its vanishing factor is removed) tends to \(\Xi'\); global collisions carry positive, quantized topological charge. However the complex-Laguerre/Jensen obstruction shows why the apparent positivity of the phase-current derivative is not an independently proved invariant of the actual theta kernel. The all-height phase-separation law remains unresolved.
