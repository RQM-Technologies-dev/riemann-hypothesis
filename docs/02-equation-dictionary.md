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

## I. The w-distance sum rule (current priority)

The point on the unit hypersphere is \(q=\cos\theta+\mathbf u\sin\theta\), with \(w=\cos\theta\). For one global \(L>0\),
\[
w(t)=\frac{L^2-t^2}{L^2+t^2},
\qquad
d_w(t)=1+w(t)=\frac{2L^2}{L^2+t^2}.
\]

| Term | Definition and meaning |
| --- | --- |
| \(w\) | Fourth (scalar) coordinate on the unit hypersphere \(w^2+x^2+y^2+z^2=1\). |
| \(r_{xyz}=\sqrt{1-w^2}\) | Radius of the two-sphere latitude in the other three coordinates; varies with \(w\), unlike the fixed ambient radius. |
| \(w=-1\) | The **infinity pole** of the globally compactified critical-line meridian. |
| \(d_w=1+w\) | Difference in the **w-coordinate** from a point to that pole; it is *not* intrinsic/geodesic distance along the hypersphere. |
| \(L>0\) | Single Cayley coordinate scale chosen for the **whole** line and for every zero, not fitted by zero index. |
| \(\gamma>0\) | Positive imaginary height of a critical-line zero \(s=1/2+i\gamma\). |
| \(d_w(\gamma)=2L^2/(L^2+\gamma^2)\) | Positive w-distance associated with one on-line zero, with multiplicity. |
| \(\rho=\beta+i\gamma\) | A general nontrivial zero of the completed zeta function, including hypothetical off-line zeros. |
| \(\beta\in(0,1)\) | Real part of a general nontrivial zero. RH states that every \(\beta=1/2\). |
| \(\delta=\beta-1/2\) | Horizontal displacement of a zero from the critical line. |
| \(x_L=1/2+L\) | Real evaluation point. Require \(L\ge1/2\) to guarantee strict positivity of every zero contribution; the numerical direct formula uses \(L>1/2\). |
| \(\xi'(x_L)\) | Complex derivative \(d\xi/ds\) evaluated at real \(s=x_L\). Not a derivative in physical time. |
| \(\xi'(x_L)/\xi(x_L)\) | Logarithmic derivative of the completed zeta function at a real, zero-free argument. |
| \(T(L)=L\,\xi'(x_L)/\xi(x_L)\) | Unconditional **total** weighted contribution from *all* nontrivial zeta zeros. |
| \(S_{\rm line}(L)\) | Sum of all on-line positive-height w-distances, counting multiplicities; not available in closed form without solving the infinite problem. |
| \(D(L)=T(L)-S_{\rm line}(L)\) | Nonnegative defect equal to contributions from **off-critical-line** zeros. RH iff \(D(L)=0\). |
| \(\psi(z)=\Gamma'(z)/\Gamma(z)\) | Digamma function, used to calculate \(T(L)\) directly without zero input. |

The exact identity is
\[
T(L)=\sum_{\substack{\rho=\beta+i\gamma\\\gamma>0}}
\frac{2L(x_L-\beta)}{(x_L-\beta)^2+\gamma^2}.
\]
For \(L\ge1/2\), **every term is strictly positive**, and the terms corresponding to \(\beta=1/2\) equal \(d_w(\gamma)\). Hence
\[
\boxed{\displaystyle
\mathrm{RH}\iff
\sum_{\gamma\in\mathcal Z_{\rm line}^{+}}(1+w(\gamma))
=L\frac{\xi'(1/2+L)}{\xi(1/2+L)}
\quad(L\ge1/2).}
\]
At the demonstration scale \(L=20\), the right side is \(13.330990477997002487\ldots\). This is an **RH-equivalent criterion derived from established Hadamard-product identities**, not a solved proof of equality.

**Crucial warning:** the deficit after a **finite** sum is the contribution of all *unlisted on-line zeros plus any off-line zeros*. It is **not** a measurable amount of off-line contribution. Only the limit over *all* on-line zeros can test \(D(L)=0\).

See [09 — full proof, numerical checks, and limitations](09-w-distance-rh-equivalence.md).

## J. Theta-kernel tail theorem and certified-height defect bound (2026-11-02)

The positive even arithmetic kernel \(\Phi(v)\) determines the completed function:
\[
X(z)=\xi(\tfrac12+iz)=2\int_0^\infty\Phi(v)\cos(zv)\,dv.
\]
At imaginary argument \(z=-iL\), the real-axis target becomes
\[
T(L)=
L\frac{\int_0^\infty v\Phi(v)\sinh(Lv)\,dv}
{\int_0^\infty\Phi(v)\cosh(Lv)\,dv}.
\]

| Term | Exact meaning |
| --- | --- |
| \(v\ge0\) | Mathematical integration coordinate of the Jacobi-theta Fourier kernel; **not time**. |
| \(\Phi(v)\) | Classical positive, even, rapidly decaying arithmetic kernel built from derivatives of Jacobi's theta series. |
| \(X(z)=\xi(1/2+iz)\) | Entire Riemann Xi function, now allowing complex parameter \(z\), whose real zeros are the critical-line zeta ordinates. |
| \(\sinh,\cosh\) | Hyperbolic sine and cosine resulting from analytic substitution \(z=-iL\), unrelated to physical hyperbolic time. |
| \(N_{\rm line}(T)\) | Number of **positive real zeros** of \(X\) up to height \(T\), with multiplicity; not presumed to count all zeta zeros. |
| \(J(T)\) | Upper bound \(\frac{1}{2\log2}\log\frac{\xi(1/2+2T)}{\xi(1/2)}\) for \(N_{\rm line}(T)\), obtained using positivity and Jensen's formula. |
| \(S_{\rm line}^{>T}(L)\) | Total remaining \(w\)-coordinate distances of the **on-line zeros above cutoff \(T\)**. |
| \(B_\Theta(T,L)\) | Explicit theta-Jensen integral giving an unconditional upper bound on \(S_{\rm line}^{>T}\); it decays like \(O(\log T/T)\) for fixed \(L\). |
| \(N_{\rm all}(T)\) | Number of *all* nontrivial zeta zeros with \(0<\Im\rho\le T\), including any hypothetical off-line zeros. |
| \(M(T)\) | Leading term \(\frac{T}{2\pi}\log\frac{T}{2\pi e}\) in the Riemann–von Mangoldt zero count. |
| \(a,b,c\) | Published Bellotti–Wong explicit counting-error coefficients \(0.10076,0.24460,8.08344\). |
| \(E(T)\) | Upper bound \(a\log T+b\log\log T+c\) on \(|N_{\rm all}(T)-M(T)|\), valid for \(T\ge e\). |
| \(P_+(H)\) | Analytically evaluated upper bound on \(\sum_{\Im\rho>H}1/(\Im\rho)^2\), from explicit zero counting. |
| \(H=3\times10^{12}\) | Height through which published interval arithmetic verified all zeta zeros are on-line; **finite**, not infinite. |
| \(D(L)\) | Nonnegative RH-equivalent off-line defect from Section I. A small strictly positive bound is not a proof of \(D(L)=0\). |

The rigorous theta-Jensen tail inequality is
\[
0\le S_{\rm line}^{>T}(L)\le
\boxed{B_\Theta(T,L)=\frac{2L^2}{\log2}
\int_T^\infty
\frac{t}{(L^2+t^2)^2}
\log\frac{\xi(\tfrac12+2t)}{\xi(\tfrac12)}\,dt}.
\]

The independently obtained **external-verification-dependent** off-line bound is
\[
\boxed{0\le D(L)\le2L(L+\tfrac12)P_+(H)},
\quad
P_+(H)=\frac{\log(H/(2\pi))+1}{2\pi H}
+\frac{2a\log H+a/2+2b\log\log H+b/(2\log H)+2c}{H^2}.
\]
At \(L=20,H=3\times10^{12}\): \(0\le D(20)<1.214\times10^{-9}\).

**Do not confuse \(S_{\rm line}^{>T}\) with \(D(L)\):** the first accounts for uncounted *on-line* zeros and tends to zero as the cutoff rises; the second accounts for potentially *off-line* zeros and is exactly zero if and only if RH is true.

See [10](10-jacobi-theta-jensen-tail.md) and [11](11-certified-distance-defect-bound.md) for proof steps and citations.

## K. Symbolic \(L>0\): the scale covariant closure family

**2026-11-02 update:** the critical-line embedding is valid for *every* \(L>0\), and the RH-equivalent closure criterion is now proved valid for every positive \(L\) by **pairing off-line conjugate zeros**. Earlier sections used \(L\ge1/2\) to make each *individual* off-line term positive; that restriction is not necessary for the *complete quartet contribution*.

| Term | Definition and role |
| --- | --- |
| \(L>0\) | Arbitrary, globally fixed stereographic coordinate scale; **not** a fitted zero and **not** a physical parameter. |
| \(\gamma_n\) | Actual zeta-zero height, independent of any choice of \(L\). |
| \(\theta_n(L)=2\arctan(\gamma_n/L)\) | Changed angular position of the **same** zero as the coordinate scale varies. |
| \(d_L(\gamma)=2L^2/(L^2+\gamma^2)\) | Changed \(w\)-coordinate distance to the infinity pole; not intrinsic geodesic distance. |
| \(G(L)\) | Integrated positive off-line defect: \(\log[\xi(1/2+L)/\xi(1/2)]-\sum_{\mathrm{line}}\log(1+L^2/\gamma^2)\). |
| \(D(L)=LG'(L)\) | Derivative defect. If off-line roots exist it is strictly positive at every \(L>0\); if RH is true it vanishes identically. |
| \(\delta>0,\gamma>0\) | Real offset and positive height of one hypothetical off-axis quartet \(1/2\pm\delta\pm i\gamma\). |
| \(A_{\delta,\gamma}(L)\) | Positive real quartet factor \(1+[2(\gamma^2-\delta^2)L^2+L^4]/(\gamma^2+\delta^2)^2\), strictly greater than 1 for zeta zeros at any \(L>0\). |
| \(\mathcal E=\lim_{L\to0^+}D(L)/L^2\) | \(L\)-free weighted off-axis moment; nonnegative, and zero iff RH. |
| \(P_+(H)\) | Published-count-based bound on the upper inverse-square zero tail. Enables \(D(L)/L^2\le2P_+(H)\) uniformly across all \(L>0\), not zero. |

The **symbolic** product form is
\[
\frac{\xi(\frac12+L)}{\xi(\frac12)}
=\prod_{\gamma\ \mathrm{on\ line}}\left(1+\frac{L^2}{\gamma^2}\right)
\prod_{\delta,\gamma\ \mathrm{off\ quartet}}
\left[1+\frac{2(\gamma^2-\delta^2)L^2+L^4}{(\gamma^2+\delta^2)^2}\right].
\]

The **scale-free** (but still unproved) exhaustion condition is
\[
\boxed{\mathcal E=\frac{\xi''(\frac12)}{\xi(\frac12)}
-2\sum_{\gamma\ \mathrm{on\ line}}\gamma^{-2}=0.}
\]
The total \(\xi''(1/2)/\xi(1/2)\) is directly evaluable from the Jacobi-theta function and equals approximately \(0.04620998623083794158\). The infinite sum over *all* line-zero reciprocal squares remains the unknown. A strictly positive uniform bound on \(\mathcal E\) is NOT a proof it is zero.

See [full derivation](12-symbolic-scale-and-defect.md) and the [multi-scale demonstration](../experiments/symbolic_scale_family.py).

## Status discipline

**Proved geometry:** all unit-radius and conjugate-return identities.  
**Established analytic inputs:** Gamma asymptotic, completed-zeta reflection, known zero counting, infinitely many critical-line zeros.  
**Our derived consequence:** \(F\) has an infinitely flat, nonanalytic pole and a smooth quaternionic return field \(\Psi\).  
**Hypothesis:** a non-tautological arithmetic/chiral closure equation that selects precisely the zeta-zero latitudes.

Sources: [DLMF zeta reflection/completion](https://dlmf.nist.gov/25.4), [DLMF Gamma asymptotics](https://dlmf.nist.gov/5.11), and [Perfect Closure archived program](https://github.com/RQM-Technologies-dev/perfect-closure).
