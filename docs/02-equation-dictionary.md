# 02 — Equation dictionary: every symbol and its meaning

This ledger is intended to let a reader reconstruct the full argument *one term at a time*. “Exact” means a mathematical identity in its stated domain, not that an interpretation of that identity has been proved. No symbol here denotes time or mass unless explicitly stated otherwise.

## A. Complex starting point

\[
s=\sigma+it,\qquad s=\tfrac12+it\text{ on the critical line}.
\]

| Term | Definition and interpretation |
| --- | --- |
| \(s\) | Complex argument of the zeta function. |
| \(\sigma=\operatorname{Re}s\) | Real part of \(s\), the horizontal coordinate. |
| \(t=\operatorname{Im}s\) | Real-valued *spectral height*, the vertical coordinate (not time). |
| \(i\) | Complex imaginary unit, \(i^2=-1\). |
| \(\tfrac12\) | The critical-line real coordinate; a number, not a spin quantum number here. |
| \(\delta=\sigma-\tfrac12\) | Displacement from the critical line. RH says every nontrivial zero has \(\delta=0\). |

## B. The quaternionic polar field

\[
\mathbf u=\sin\alpha\cos\beta\,\mathbf i+
\sin\alpha\sin\beta\,\mathbf j+\cos\alpha\,\mathbf k,
\quad
Q=R(\cos\theta+\mathbf u\sin\theta).
\]

| Term | Definition and interpretation |
| --- | --- |
| \(\mathbb H\) | Quaternions, a four-real-dimensional division algebra. |
| \(a,b,c,d\) | Real coordinates of \(q=a+b\mathbf i+c\mathbf j+d\mathbf k\). |
| \(\mathbf i,\mathbf j,\mathbf k\) | Quaternion imaginary basis with \(\mathbf i^2=\mathbf j^2=\mathbf k^2=-1\), \(\mathbf i\mathbf j=\mathbf k\). \(\mathbf i\) in quaternion notation plays the same role as complex \(i\) in a chosen slice; these are distinguished typographically. |
| \(\mathbf u\) | A pure imaginary **unit** quaternion; \(\mathbf u^2=-1\). Axis of one complex slice. |
| \(\alpha,\beta\) | Ordinary spherical angles parametrizing \(\mathbf u\in S^2\); independent of \(t\). |
| \(\theta\) | Polar angular coordinate of the compactified spectral meridian; **not time**. |
| \(R>0\) | One shared Euclidean radius in the four-real-dimensional target space; arbitrary coordinate parameter. |
| \(S^3_R\) | The three-sphere \(\{Q\in\mathbb H:|Q|=R\}\), not ordinary 3D solid space. |
| \(\overline Q\) | Quaternionic conjugate; reverses the imaginary components of \(Q\). |
| \(|Q|^2=Q\overline Q\) | Ordinary positive Euclidean norm squared in four real coordinates. |
| \(\cos,\sin\) | Ordinary trigonometric functions, angles in radians. |
| \(e^{\mathbf u\theta}\) | Quaternionic exponential restricted to one complex slice; equals \(\cos\theta+\mathbf u\sin\theta\). |

**Always distinguish:** a fixed-\(\theta\) *latitude two-sphere* has intrinsic radius \(R|\sin\theta|\), while all latitude spheres have the same **ambient four-dimensional distance** \(R\) from the origin.

## C. One transformation, not zero-by-zero scaling

\[
Q(t,\mathbf u)=R\,(L+\mathbf u t)(L-\mathbf u t)^{-1},
\quad
\theta(t)=2\arctan(t/L)\pmod{2\pi}.
\]

| Term | Definition and interpretation |
| --- | --- |
| \(L>0\) | Fixed scale converting spectral height to an angle. Chosen *once*, not separately for each zero. |
| \((L-\mathbf u t)^{-1}\) | Quaternionic multiplicative inverse, valid for real finite \(t\) since its norm squared is \(L^2+t^2>0\). |
| \(\arctan\) | Inverse tangent, branch in \((-\pi/2,\pi/2)\); modulo \(2\pi\) selects the return branch for negative heights. |
| \(Q(t,\mathbf u)\) | Single Cayley/inverse-stereographic map of the entire critical-line height coordinate. |
| \(\lim_{t\to+\infty}Q=\lim_{t\to-\infty}Q=-R\) | Same geometric infinity pole, reached from opposite directions. |
| \(Q(-t,\mathbf u)=\overline{Q(t,\mathbf u)}\) | Exact conjugate-return identity in a fixed slice. |
| \(\theta(-t)=2\pi-\theta(t)\) | Angular conjugate relation for \(t>0\). |

For off-axis points \(w=\delta+\mathbf u t\):
\[
\frac{|Q(w)|^2}{R^2}=
\frac{(L+\delta)^2+t^2}{(L-\delta)^2+t^2}.
\]
The numerator/denominator are squared norms of \(L+w\) and \(L-w\). Hence radius \(R\) occurs iff \(\delta=0\). This *encodes* the critical line; it doesn't prove all zeros lie there.

## D. The original complex harmonic series

\[
\zeta(s)=\sum_{n=1}^\infty n^{-s}
=\sum_{n=1}^\infty n^{-\sigma}e^{-it\log n}
\quad\textbf{only for }\sigma>1\textbf{ as this Dirichlet series}.
\]

| Term | Definition and interpretation |
| --- | --- |
| \(\zeta(s)\) | Riemann zeta function: a meromorphic continuation of the original series. |
| \(n\) | Positive integer indexing harmonic terms, not a zeta-zero index. |
| \(n^{-\sigma}\) | Magnitude of the \(n\)-th harmonic term. |
| \(e^{-it\log n}\) | Complex phase of the \(n\)-th harmonic at height \(t\). |
| \(\log n\) | Natural logarithm of \(n\); mathematical frequency in the *height parameter*, not a physical time frequency. |
| \(n^{-s}=\exp(-s\log n)\) | Definition of the complex power for positive \(n\). |

For critical-line analysis, use the analytic continuation, or the **alternating eta series**:
\[
\eta(s)=\sum_{n=1}^\infty(-1)^{n-1}n^{-s},\quad
\zeta(s)=\frac{\eta(s)}{1-2^{1-s}}.
\]
This alternating series converges for \(\sigma>0\) (not necessarily absolutely). The denominator does not vanish at \(\sigma=1/2\). Terms of the original *nonalternating* series cannot simply be summed there.

## E. Prime product, Gamma factor, and entire completion

\[
\zeta(s)=\prod_{p\ {\rm prime}}(1-p^{-s})^{-1},\qquad \sigma>1.
\]
Here \(p\) runs over prime integers; this is Euler's prime product, not the inverse Gamma function.

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

| Term | Definition and interpretation |
| --- | --- |
| \(\xi(s)\) | Entire, completed zeta function; its zeros are exactly the nontrivial zeros of \(\zeta\). |
| \(\Gamma(z)\) | Euler Gamma function, \(\Gamma(z)=\int_0^\infty x^{z-1}e^{-x}\,dx\) for \(\Re z>0\), with continuation elsewhere. |
| \(\pi^{-s/2}\) | Completion factor for the functional equation. |
| \(s(s-1)\) | Cancels apparent/polar behavior at \(s=0\) and \(s=1\) in the completed expression; together with other factors gives an entire function. |
| \(X(t)=\xi(\tfrac12+it)\) | Real-valued, even function for real \(t\), by the functional equation and conjugation. |
| \(\xi(s)=\xi(1-s)\) | Exact functional equation (not RH). |
| \(\xi(\bar s)=\overline{\xi(s)}\) | Exact complex-conjugation identity (not RH). |

## F. Zero locations and reverse construction

\[
\rho_n=\tfrac12+i\gamma_n
\quad\text{when a zero lies on the critical line}.
\]
Here \(\rho_n\) is the zero in the complex plane, and \(\gamma_n>0\) its height; **all** nontrivial zeros are known to satisfy this only if RH is true. Their angular positions are
\[
\theta_n=2\arctan(\gamma_n/L),\quad
\theta_n^*=2\pi-\theta_n.
\]
The pairing of nontrivial zeros is always true; that *all* nontrivial zero heights are real critical-line heights is unproved.

Hadamard reconstruction of the entire completed function:
\[
\xi(s)=e^{A+Bs}\prod_{\rho}
  \left(1-\frac{s}{\rho}\right)e^{s/\rho}.
\]
The product is over all nontrivial zeros \(\rho\), with multiplicity, with convergence as an entire canonical product. \(A,B\) are normalization constants. This is an exact mathematical reconstruction, not an operator that discovers the zeros.

**Only assuming RH**, the real-even critical-line function can be written in paired form:
\[
X(t)=X(0)\prod_{\gamma_n>0}
\left(1-\frac{t^2}{\gamma_n^2}\right).
\]
When transformed into angles, replace \(t\) by \(L\tan(\theta/2)\). The real-only product should not be asserted unconditionally.

## G. Pole and spinorial return

\[
U(0)=1,\qquad U(\pi)=-1,\qquad U(2\pi)=1.
\]
The \(-1\) is the central element of \(SU(2)\). The analogy with the \(360^\circ/720^\circ\) spinor sign is mathematical; neither \(\gamma_n\) nor \(\theta\) represents Dirac time, energy, or mass.

For a fixed integer \(n>1\):
\[
h_n(t)=n^{-1/2}e^{-it\log n}.
\]
The conjugate identity \(h_n(-t)=\overline{h_n(t)}\) is exact, but **\(h_n(t)\) has no limit as \(t\to\pm\infty\)**, so it does not continuously pass through the pole by itself.

In contrast, the completed function decays exponentially:
\[
|X(t)|\le C(1+|t|)^M e^{-\pi |t|/4}
\]
for sufficiently large \(|t|\), some positive \(C,M\). This follows from Stirling's formula for \(\Gamma\) and polynomial growth bounds for \(\zeta\) on fixed vertical lines. Precise polynomial exponents are not needed here.

## H. The new compactified amplitude

Define
\[
F(\theta)=X\!\left(L\tan\frac{\theta}{2}\right),\quad
\theta\ne\pi;\qquad F(\pi)=0.
\]
Then \(F(2\pi-\theta)=F(\theta)\). In fact \(F\) extends to a **smooth, infinitely flat** real function at \(\theta=\pi\), but is not real analytic there. See [04](04-infinity-pole-and-spinorial-return.md).

A quaternion-valued **constructed return field** is
\[
\Psi(\theta,\mathbf u)=F(\theta)e^{\mathbf u\theta}.
\]
It has:
\[
\Psi(2\pi-\theta,\mathbf u)=\overline{\Psi(\theta,\mathbf u)},\
\Psi(\pi,\mathbf u)=0,\
\Psi(0,\mathbf u)=\Psi(2\pi,\mathbf u)=X(0).
\]
These are rigorous compatibility identities for a *defined* field, not a derivation of RH.

## Status discipline

**Proved geometry:** all unit-radius and conjugate-return identities.  
**Established analytic inputs:** Gamma asymptotic, completed-zeta reflection, known zero counting, infinitely many critical-line zeros.  
**Our derived consequence:** \(F\) has an infinitely flat, nonanalytic pole and a smooth quaternionic return field \(\Psi\).  
**Hypothesis:** a non-tautological arithmetic/chiral closure equation that selects precisely the zeta-zero latitudes.

Sources: [DLMF zeta reflection/completion](https://dlmf.nist.gov/25.4), [DLMF Gamma asymptotics](https://dlmf.nist.gov/5.11), and [Perfect Closure archived program](https://github.com/RQM-Technologies-dev/perfect-closure).
