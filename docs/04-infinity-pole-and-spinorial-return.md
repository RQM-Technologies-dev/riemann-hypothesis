# 04 — Investigation: what really crosses the infinity pole?

**2026-10-30 — Research note.** The goal is to make the user's polar-return hypothesis precise **without equating the zeta height with time or treating zeta as a literal electron**. All results below are mathematical consequences of standard analytic facts and the explicitly chosen coordinate map. No RH proof is claimed.

## Result A — Geometry closes; the phases of individual harmonics do not

Fix \(L>0\), one pure imaginary unit \(\mathbf u^2=-1\), and \(R>0\). Define
\[
U(\theta,\mathbf u)=e^{\mathbf u\theta},\quad Q=R U,\qquad
t=L\tan(\theta/2)\quad(\theta\ne\pi).
\]
The fixed-\(\mathbf u\) meridian is a circle. Along it:
\[
Q(0)=+R,\quad Q(\pi)=-R,\quad Q(2\pi)=+R.
\]
The two real infinity ends of \(t\) have become *one geometric point*, \(Q=-R\).

For a single harmonic from the original zeta Dirichlet series:
\[
h_n(t)=n^{-1/2}e^{-it\log n},\qquad n>1.
\]
For every finite \(t\):
\[
h_n(-t)=\overline{h_n(t)}.
\]
**However**, \(h_n\) has no limit as \(t\to+\infty\). A proof for \(n=2\) is explicit:
\[
t_m=\frac{2\pi m}{\log2}\to\infty,\qquad
t_m'=\frac{(2m+1)\pi}{\log2}\to\infty.
\]
At these two sequences,
\[
h_2(t_m)=2^{-1/2},\qquad h_2(t_m')=-2^{-1/2}.
\]
Both map to \(\theta\to\pi^-\), but their values differ. There is no limiting harmonic phase at infinity, let alone a continuous reversal through it.

This *does not contradict* \(h_n(-t)=\overline{h_n(t)}\): conjugate matching of finite pairs is not the same as a continuous traversal of a singular endpoint.

## Result B — The completed zeta scalar *does* admit a smooth polar return

The completed zeta function is
\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]
Set
\[
X(t)=\xi(\tfrac12+it),\quad t\in\mathbb R.
\]
The functional equation and complex conjugation give:
\[
X(t)\in\mathbb R,\qquad X(-t)=X(t).
\]

Now define the compactified field
\[
F(\theta)=
\begin{cases}
X\!\left(L\tan\frac{\theta}{2}\right),&\theta\ne\pi,\\
0,&\theta=\pi.
\end{cases}
\]
Because \(t(2\pi-\theta)=-t(\theta)\), we have
\[
F(2\pi-\theta)=F(\theta).
\]

**Decay argument.** On \(s=1/2+it\), Stirling gives
\[
\left|\Gamma\!\left(\tfrac14+\tfrac{it}{2}\right)\right|
\sim\sqrt{2\pi}\left(\tfrac{|t|}{2}\right)^{-1/4}
e^{-\pi|t|/4}.
\]
Multiplying by \(\tfrac12s(s-1)\pi^{-s/2}\) and using polynomial growth of \(\zeta\) on fixed vertical lines gives, for suitable constants \(C,M>0\),
\[
|X(t)|\le C(1+|t|)^M e^{-\pi|t|/4}
\quad (|t|\text{ large}).
\]
Analogous polynomial-times-exponential bounds hold for every fixed-order \(t\)-derivative of \(X\) (different constants/exponents for each order).

Write \(\varepsilon=|\theta-\pi|\). Near the pole,
\[
|t|=L\cot(\varepsilon/2)
=\frac{2L}{\varepsilon}+O(\varepsilon).
\]
Hence
\[
|F(\pi\pm\varepsilon)|\le
C'\varepsilon^{-M'}\exp\left(-\frac{\pi L}{2\varepsilon}+O(\varepsilon)\right).
\]
The same type of bound holds for all \(\theta\)-derivatives by the chain rule. Thus \(F\) extends to a \(C^\infty\) (smooth) function at \(\pi\), and
\[
\boxed{F^{(k)}(\pi)=0\quad\text{for every integer }k\ge0.}
\]
This is called an **infinitely flat pole**.

**Interpretation:** the original individual harmonic phases keep winding faster, while the **completed** zeta function has a collectively damped scalar value approaching zero. Its polar continuation is smooth as a *real-angle function*, not a holomorphic continuation of \(\xi\) through complex infinity.

## Result C — The pole is smooth but cannot be real analytic

The completed function \(X\) is not identically zero (for example \(X(0)\ne0\)). It is a theorem (Hardy) that \(\zeta\) has infinitely many zeros on the critical line. Therefore \(F\) has infinitely many distinct real zeros approaching \(\theta=\pi\).

If \(F\) had a real-analytic extension to a neighborhood of \(\pi\), its infinitely many zeros accumulating there would force it to vanish identically in a neighborhood (identity theorem for real-analytic functions). This contradicts the nonzero behavior of \(X\).

Thus:
\[
\boxed{F\text{ is smooth and infinitely flat at }\pi,\quad
       F\text{ is NOT real analytic there}.}
\]
This conclusion does **not** assume RH. It uses only the known infinitely many critical-line zeros.

## Result D — A continuous quaternion-valued return field exists

Define the unit quaternion phase
\[
U(\theta,\mathbf u)=\cos\theta+\mathbf u\sin\theta
\]
and the **constructed** quaternionic field
\[
\boxed{\Psi(\theta,\mathbf u)=F(\theta)\,U(\theta,\mathbf u).}
\]
Since \(F\) is real and even about \(\pi\):
\[
\Psi(2\pi-\theta,\mathbf u)
=\overline{\Psi(\theta,\mathbf u)}.
\]
It satisfies:
\[
\Psi(0,\mathbf u)=X(0),\quad
\Psi(\pi,\mathbf u)=0,\quad
\Psi(2\pi,\mathbf u)=X(0).
\]
Therefore \(\Psi\) is a **well-defined smooth, globally returning mathematical field along the meridian**, notwithstanding the lack of a limit for the individual harmonic phases.

The quaternionic factor \(U\) provides the \(+1\to-1\to+1\) double-return geometry. The completed factor \(F\) provides the scalar zero structure, including its infinite accumulation at the pole. Both are required for this particular construction.

But \(\Psi\) is *defined using \(\xi\)*. It does not independently determine its zeros. Multiplying an arbitrary scalar field by \(U\) would give an analogous conjugate geometry. Do not confuse the existence of \(\Psi\) with a proof of RH.

A normalized phase \(F/|F|\) is *not* continuous across a simple zero; at \(\pi\) no global unit-phase limit is recovered from the scalar amplitude. The amplitude's vanishing is what permits the smooth **unnormalized** field \(\Psi\) to pass the pole.

## Result E — The new geometry predicts an accumulation law only if RH is assumed

For \(t\gg1\),
\[
\varepsilon=\pi-\theta(t)\sim\frac{2L}{t}.
\]
The **total** number \(N(T)\) of nontrivial zeta zeros up to height \(T\) obeys Riemann–von Mangoldt:
\[
N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T).
\]
Under **RH**, this is also the count of critical-line zeros up to \(T\), and their angular accumulation at the pole is therefore
\[
\boxed{
N_{\rm angle}(\varepsilon)\sim
\frac{L}{\pi\varepsilon}\log\frac{L}{\pi\varepsilon}
\quad(\varepsilon\downarrow0,\ \textbf{assuming RH}).
}
\]
Without RH, infinitely many such angular zeros are known, but the stated full counting asymptotic does not automatically apply to their subset. If one claimed it unconditionally, one would be smuggling RH into the argument.

The leading angular zero density (under RH) scales like
\[
\frac{L}{\pi\varepsilon^2}
\log\frac{L}{\pi\varepsilon}.
\]
This is a *coordinate translation of an existing counting law*, not a novel prediction of a dynamical model.

## What really seems promising

Our strongest **new formulation of a standard fact** is the contrast:
- **Unbounded phase winding** for each raw harmonic near the pole;
- **smooth infinite-order scalar vanishing** for the Gamma-completed ensemble at the same pole;
- **exact conjugate angular return** for the completed scalar field and constructed quaternionic companion.

This creates a precise mathematical target for “perfect closure”: find a new action, transfer operator, positive form, or boundary condition that forces a particular scalar completion instead of writing it by hand.

## Open obstructions

1. Every point of the critical line lies on \(S^3_R\); zero selectivity is missing.
2. The \(\xi\)-based return field is constructed from known analytic structure, so cannot independently prove RH.
3. Ordinary \(SU(2)\) double-return topology does not constrain scalar zeros.
4. The Euler product does not converge on the critical line, and termwise harmonic limits do not exist at the infinity pole.
5. A true RH argument must rule out nontrivial off-line zeros, not just model the known on-line ones.
6. A global quaternionic extension must specify a slice-regular or other precise function class; changing the imaginary axis alone does not create new zeros.

## Next step: a falsifiable model

Seek a **single arithmetic kernel** \(K\), specified independently of known zeta-zero heights, acting on the compactified polar coordinate, with a fixed domain and an involution \(J\) implementing \(J:\theta\mapsto2\pi-\theta\). Prove nonnegativity/self-adjointness or another off-axis obstruction **from the kernel**, then compare its selected eigenangles to held-out known ordinates.

No ad hoc per-zero radii, per-zero parameters, or fitted phase jumps. Baseline controls must include even analytic functions with off-critical-line zeros, because reflection symmetry alone admits them.

## References and prior art

- DLMF §25.4, completed zeta/reflection: https://dlmf.nist.gov/25.4
- DLMF §5.11, Gamma asymptotic: https://dlmf.nist.gov/5.11
- DLMF §25.10, Hardy real zeta zeros and Riemann–Siegel \(Z\): https://dlmf.nist.gov/25.10
- Perfect Closure: https://github.com/RQM-Technologies-dev/perfect-closure
