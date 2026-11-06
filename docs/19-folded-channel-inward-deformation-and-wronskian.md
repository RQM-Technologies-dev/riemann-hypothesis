# 19 — From the critical-strip boundary to the fold: phase, Wronskian, and channel collision

**Date:** 2026-11-06. **Status:** audited identities, finite numerical experiment, a constructed collision diagnostic, and a focused next lemma. **Not a proof of RH.**

**Research motivation:** The user's model is *not* “two mirror symmetries prove RH.” It asks whether the two mirrored quaternionic zero-spheres encode a deeper *folded-superposition constraint* — an analytic rule that makes **simultaneous destructive interference** of two theta channels possible only on the centered fold. We investigate that mechanism using the actual Riemann Xi Fourier transform.

**Lineage:** [16 — quartets and S² zero-spheres](16-two-fold-zero-spheres-and-theta-positivity.md), [17 — Clay's exact zero-exclusion goal](17-clay-statement-and-proof-roadmap.md), [18 — theta mirror channels](18-mirror-channel-folding-and-zero-collision.md), [15 — signed theta double integral](15-higher-moment-growth-certificate.md).

## 1. Exact definitions and which fold is which

Write \(\Xi(z)=\xi(\tfrac12+iz)\). For real \(t,a\),

\[
\begin{aligned}
C(t,a)&=\int_0^\infty\Phi(u)\cos(tu)\cosh(au)\,du,\\
S(t,a)&=\int_0^\infty\Phi(u)\sin(tu)\sinh(au)\,du,\\
\Xi(t+ia)&=2[C(t,a)-iS(t,a)],\\
\Xi(t-ia)&=2[C(t,a)+iS(t,a)].
\end{aligned}
\]

Here \(\Phi\) is the *specific* even Jacobi-theta kernel used throughout this repository, not an arbitrary positive kernel. The spectral coordinate \(t\) is not physical time. The original s-coordinate is \(s=\tfrac12-a+it\) for \(z=t+ia\), so the sign of \(a\) reverses between these coordinate systems.

The two channels are **analytically coupled**, not two independent wavefunctions:

\[
C(t,-a)=C(t,a),\quad S(t,-a)=-S(t,a),
\]

\[
\boxed{C_a=S_t,\quad S_a=-C_t;\qquad
C_{aa}=-C_{tt},\quad S_{aa}=-S_{tt}.}
\tag{1}
\]

On the critical fold \(a=0\), the odd channel \(S(t,0)\) vanishes identically. An actual Xi zero must also satisfy \(C=0\). Away from the fold, a Xi zero requires **both** \(C(t,a)=S(t,a)=0\); the fold removes one of these cancellation conditions.

At a simple real Xi zero \(t=\gamma\),

\[
S(t,a)=-a C_t(t,0)+O(a^3),\quad
C(t,a)=C(t,0)+O(a^2),
\]

so the odd channel is locally nonzero at and near that *particular simple* critical-line root for sufficiently small positive \(a\). This local observation does not exclude distant off-line roots, nor does it prove global simplicity.

## 2. The phase/Wronskian identity — a rigorous bridge

Define the channel Wronskian

\[
\boxed{J(t,a):=C(t,a)S_t(t,a)-S(t,a)C_t(t,a).}
\tag{2}
\]

Using (1), the identity from the established outward Xi-growth program is

\[
\boxed{
J=CC_a+SS_a=\frac18\,\partial_a|\Xi(t+ia)|^2.
}
\tag{3}
\]

Where \(\Xi\ne0\), write \(\theta(t,a)=\arg\Xi(t+ia)\), with any local continuous branch of the argument. Then

\[
\boxed{
\partial_t\theta
=-\frac{J}{C^2+S^2}
=-\frac12\partial_a\log|\Xi(t+ia)|^2.
}
\tag{4}
\]

Thus **phase rotation, outward modulus growth, and preservation of the alternating mirror channels are linked by the same sign**. Proving \(J>0\) for all real \(t\) and \(0<a\le\tfrac12\) would prove the Clay RH statement. Equation (4) is exact but **does not establish that sign**.

There is a second exact derivative identity, obtained from (1):

\[
\boxed{
\begin{aligned}
\partial_aJ
&=C_t^2+S_t^2-CC_{tt}-SS_{tt}\\
&=\mathcal L(C)+\mathcal L(S)\\
&=\tfrac14\left(|\Xi'(z)|^2-
\operatorname{Re}(\Xi(z)\overline{\Xi''(z)})\right),
\quad z=t+ia,
\end{aligned}}
\tag{5}
\]

where \(\mathcal L(f)=f_t^2-ff_{tt}\) denotes the classical Laguerre expression. This is closely related to the **Jensen/Laguerre inequalities and Hermite–Biehler approach already studied** in Csordas–Varga (1989), especially their Lemma 3.3 and Theorem 3.4. This is not claimed as a new theorem.

At \(a=0\), \(J(t,0)=0\) for every \(t\). If one could prove \(\partial_aJ\ge0\) with sufficient strictness for all \(0<a\le\tfrac12\), then integrating (5) would give \(J>0\). However, a universal sign for the right side of (5) is again essentially the outstanding RH-level property. It is **not** a free consequence of positive \(\Phi\).

## 3. What an actual collision must do to phase

Suppose \(\Xi(z_0)=0\), where \(z_0=t_0+ia_0\), \(0<a_0<\tfrac12\). At that point,

\[
C(t_0,a_0)=S(t_0,a_0)=J(t_0,a_0)=0.
\]

If the zero is simple (\(\Xi'(z_0)\ne0\)), (5) yields the **exact local collision identity**

\[
\boxed{
\partial_aJ(t_0,a_0)=\frac{|\Xi'(z_0)|^2}{4}>0.
}
\tag{6}
\]

Hence for \(a\) sufficiently close to \(a_0\), holding \(t=t_0\) fixed, \(J(t_0,a)<0\) just inward and \(J(t_0,a)>0\) just outward. This is a genuine sign reversal, not merely a vanishing point.

More generally, if the off-line zero has multiplicity \(m\) and
\(\Xi(z)=b(z-z_0)^m+O((z-z_0)^{m+1})\) with \(b\ne0\), then

\[
\boxed{
J(t_0,a)=\frac{m|b|^2}{4}(a-a_0)^{2m-1}
+O((a-a_0)^{2m}).
}
\tag{7}
\]

Thus **every** off-line zero, regardless of multiplicity, creates a local sign change in \(J\). For \(m>1\) the first derivative \(\partial_aJ\) can vanish at the collision; equation (6) is only for simple zeros.

This supplies a useful counterfactual prediction for the folded-sphere model: an off-center spherical zero pair would carry paired phase-vortex signatures. Symmetry forces the *pairing* of these signatures, **not** their absence. What would rule them out is a **global no-sign-reversal theorem** derived from theta-specific structure.

## 4. An unconditional outer boundary from Hermite–Biehler theory

The original nontrivial zeta zeros lie in \(0<\Re s<1\), so all Xi zeros lie within \(|\Im z|<\tfrac12\) unconditionally. The Riemann Xi Fourier kernel satisfies the admissibility assumptions used by **G. Csordas and R. S. Varga, "Fourier transforms and the Hermite–Biehler theorem," Proc. AMS 107 (1989), 645–652**.

Their **Proposition 3.1**, under an established zero strip \(|\Im z|<\tau\), shows that the cosine–cosh and sine–sinh channels \(P_\mu=2C(\cdot,\mu)\) and \(Q_\mu=2S(\cdot,\mu)\) are Laguerre–Pólya entire functions for \(\mu\ge\tau\). The Hermite–Biehler argument also provides real-rootedness of their real linear combinations and a nonnegative Wronskian for these outer shifts. In particular, at \(\mu=\tfrac12\), the original Xi function has no zeros on that boundary and \(C,S\) share no real zero.

**This is our unconditional starting point**: a separated, well-structured pair of channel-zero families at \(a=\tfrac12\).

**The question changes from "why are there twins?" to "can the Hermite–Biehler structure of the actual theta kernel be continued *inward*, for every \(0<a<\tfrac12\), without a channel collision?"** The inward preservation is exactly the difficult RH-level step and is not provided by the 1989 theorem.

Primary source: Csordas & Varga (1989), https://doi.org/10.2307/2048160, notably Proposition 3.1, Theorem 2.5, Lemma 3.3 and Theorem 3.4. Also https://www.mdpi.com/2073-8994/18/8/1283 for a 2026 theta-kernel growth discussion.

## 5. Reproducible first finite-height experiment

Scripts and saved output:

- [experiments/folded_channel_collision_scan.py](../experiments/folded_channel_collision_scan.py)
- [tests/test_folded_channel_collision_scan.py](../tests/test_folded_channel_collision_scan.py)
- [results/folded_channel_collision_scan.json](../results/folded_channel_collision_scan.json)

**Method.** Compute \(C=\Re\Xi/2,\ S=-\Im\Xi/2\) from the analytic continuation with mpmath, and check three sample points against independent Jacobi-theta quadrature. Use 45-digit arithmetic. Search sign brackets with step \(0.25\) in \(8\le t\le45\), refine roots numerically, and compare channel zero locations. Numerical sign-bracket scans **can miss tangent roots or narrow root pairs**, so this is neither an exhaustive enumeration nor a certified no-common-zero theorem.

| \(a\) | C roots found | S roots found | C/S alternation in scanned range | smallest sampled C-to-S root gap |
|---:|---:|---:|---|---:|
| 0.50 | 8 | 8 | yes | 0.9601307537 |
| 0.49 | 8 | 8 | yes | 0.9548395564 |
| 0.20 | 8 | 8 | yes | 0.8338004695 |
| 0.05 | 8 | 8 | yes | 0.8085993923 |

Examples for \(a=0.20\): the first three C cancellation locations are \(14.1115014798863,\ 20.9917875534091,\ 24.9874690682859\); the first three S cancellations are \(15.5781086313888,\ 22.0883879752191,\ 26.2641289459225\). Thus the two channels appear to alternate in this finite window.

Selected independent theta-integral/xi differences were of order \(10^{-48}\) to \(10^{-50}\) at the chosen quadrature precision. These are **numerical cross-checks, not interval error bounds**.

### Deliberately constructed collision as a negative control

Let \(\varepsilon=0.49\) and define a *different* positive even kernel

\[
\Phi_\varepsilon(u)=
\Phi(u)+\varepsilon[\Phi(u-1)+\Phi(u+1)].
\]

Its Fourier transform is

\[
\Xi_\varepsilon(z)=\Xi(z)[1+2\varepsilon\cos z],
\]

with extra nonreal zeros at

\[
z=\pi\pm i\,\operatorname{arcosh}(1/0.98)
=\pi\pm 0.201688487798836\ldots i.
\]

At \(t=\pi\), its Wronskian changes sign across the collision: approximately \(J=-2.58\cdot10^{-6}\) at \(a=0.20\) and \(J=+1.37\cdot10^{-5}\) at \(a=0.21\). This confirms the collision prediction for a valid positive even *perturbed* kernel. The perturbed kernel does **not** satisfy the full special theta construction defining the original Riemann Xi function; it is **not a counterexample to RH**.

## 6. The next mathematical lemma to attempt

**Inward Hermite–Biehler preservation lemma (CONJECTURAL):** for the original Jacobi-theta kernel, show the two entire real functions
\[
P_a(t)=2C(t,a),\qquad Q_a(t)=2S(t,a)
\]
retain a strict, orientation-consistent separation as \(a\) decreases from \(1/2\) to any positive value, without a common zero at any real height \(t\).

A suitable all-height theorem would imply RH. To avoid hiding RH in a reformulation, attempt the following *specific supporting step* first:

> Derive from the Jacobi modular transformation and its differentiated kernel identities a **uniform sign-preserving deformation estimate** for the cross-channel Wronskian
> \[
> J(t,a)=\frac18\partial_a|\Xi(t+ia)|^2
> \]
> that is valid for **all** real \(t\) and \(0<a\le 1/2\) and does not assume real-rootedness of Xi.

Possible avenues, **not proofs**:

1. **Modular structure:** express \(\partial_aJ=\mathcal L(C)+\mathcal L(S)\) as a theta-double-integral and seek a modularly paired sign cancellation not true for \(\Phi_\varepsilon\).
2. **Deformation:** start from the unconditional Hermite–Biehler boundary at \(a=1/2\). Seek an independently proved differential inequality preventing \(J\) from becoming zero under inward continuation.
3. **Phase winding:** compute the winding of \(\Xi(t+ia)\) on finite rectangles using the argument principle, then identify what additional **uniform boundary estimate** would prohibit nonreal zero-pairs at arbitrarily high height. A winding number without this step only counts zeros.
4. **Spherical translation after proof:** a proved analytic noncollision law would force \(\mathcal S_{a,t}=\mathcal S_{-a,t}\) for each nontrivial zero in the slice-regular quaternionic lift. The independent Cayley \(S^3\) coordinate scale \(L\) remains symbolic.

**Failure gates:**
- A proof that simply uses positive \(\Phi\) or evenness is invalid (the explicit \(\Phi_\varepsilon\) destroys it).
- A proof that uses Hermite–Biehler on every \(a>0\) as a hypothesis is circular.
- Eight observed roots per channel, however well computed, cannot establish the global interlacing law.
- Local signs of \(J_a\) and phase slopes do not imply a global sign over unbounded \(t\).
- Never advertise a new RH proof until the uniform all-height theorem has a correct independent derivation and serious mathematical review.

**Conclusion:** The folded-superposition idea now has an explicit dynamical formulation: begin with a proven outer-strip Hermite–Biehler separation, deform the coupled theta channels inward, and seek a special modular obstruction to the sign reversal that necessarily accompanies any off-line zero. That is a research mechanism, not merely a visual analogy, but the decisive inward-preservation estimate remains unproved.
