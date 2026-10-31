# 01 — Quaternionic polar geometry without per-zero normalization

**Research status:** exact coordinate geometry; its application as a zero-selection mechanism is conjectural.

## Four real coordinates, no time

Take the quaternion algebra \(\mathbb H\), with
\[
q=a+b\mathbf i+c\mathbf j+d\mathbf k,\quad
\mathbf i^2=\mathbf j^2=\mathbf k^2=\mathbf i\mathbf j\mathbf k=-1.
\]
The four components \((a,b,c,d)\) are real **geometric coordinates**, not \(3+1\) spacetime coordinates. Nothing in this model assumes a physically existing fourth spatial dimension.

For angles \(\alpha\in[0,\pi]\) and \(\beta\in[0,2\pi)\), put
\[
\mathbf u(\alpha,\beta)=
(\sin\alpha\cos\beta)\mathbf i+
(\sin\alpha\sin\beta)\mathbf j+
(\cos\alpha)\mathbf k,\qquad
\mathbf u^2=-1,\quad|\mathbf u|=1.
\]
The unit quaternion polar form is
\[
U(\theta,\mathbf u)=e^{\mathbf u\theta}
=\cos\theta+\mathbf u\sin\theta,
\quad
Q(\theta,\mathbf u)=R\,U(\theta,\mathbf u).
\]
As a point in \(\mathbb R^4\), \(|Q|^2=R^2\), defining \(S^3_R\).

**Important distinction:** \(Q=R\,U\) lies at radius \(R\) from the four-dimensional origin, while fixing a polar angle \(\theta\in(0,\pi)\) and varying \(\mathbf u\) gives a two-sphere of intrinsic radius \(R\sin\theta\). The distinct zero latitude spheres do *not* all have the same intrinsic two-dimensional radius. They all belong to the *same ambient \(S^3_R\)*.

## One global inverse stereographic mapping

Let the usual zeta complex variable be \(s=\sigma+it\). On the critical line, \(\sigma=1/2\); here \(t\) is a real spectral height, **not time**. Fix constants \(L>0\) and \(R>0\), once for the entire line. Define
\[
Q(t,\mathbf u)
=R\,(L+\mathbf u t)(L-\mathbf u t)^{-1}.
\]
The factors live in the commutative slice \(\mathbb C_{\mathbf u}\), so division is unambiguous. Direct expansion gives
\[
Q(t,\mathbf u)
=R\left[\frac{L^2-t^2}{L^2+t^2}
+\mathbf u\frac{2Lt}{L^2+t^2}\right].
\]
Let
\[
\theta(t)=
\begin{cases}
2\arctan(t/L),& t\ge0,\\
2\pi+2\arctan(t/L),& t<0.
\end{cases}
\]
Then \(Q(t,\mathbf u)=R[\cos\theta(t)+\mathbf u\sin\theta(t)]\).
The identity
\[
(L^2-t^2)^2+(2Lt)^2=(L^2+t^2)^2
\]
proves **without any individual zero normalization** that \(|Q(t,\mathbf u)|=R\) for all real \(t\).

The return coordinates follow:
\[
\theta(-t)=2\pi-\theta(t)\quad(t>0);
\qquad Q(-t,\mathbf u)=\overline{Q(t,\mathbf u)}.
\]
The poles and stages:
\[
t=0\leftrightarrow\theta=0\leftrightarrow Q=R;
\quad t\to+\infty\leftrightarrow\theta\to\pi^-\leftrightarrow Q=-R;
\]
\[
t\to-\infty\leftrightarrow\theta\to\pi^+\leftrightarrow Q=-R;
\quad t=0\text{ after return}\leftrightarrow\theta=2\pi\leftrightarrow Q=R.
\]
Thus the *one-point compactification of the real spectral line* is an angular circle along any **fixed** imaginary unit \(\mathbf u\).

## What happens when all imaginary axes vary?

For fixed \(t>0\), \(\mathbf u\in S^2\) sweeps out
\[
\mathcal S_t=
\{R(\cos\theta(t)+\mathbf u\sin\theta(t)):\mathbf u^2=-1\}.
\]
This is a latitude two-sphere in the ambient \(S^3_R\).

Because
\[
Q(-t,\mathbf u)=Q(+t,-\mathbf u),
\]
the *unoriented full spherical sets* for \(+t\) and \(-t\) are identical. They only become distinguishable as *oriented traversals* if we keep the chosen slice/meridian label \(\mathbf u\). Allowing all \(\mathbf u\) and a full \(0\le\theta\le2\pi\) redundantly parametrizes \(S^3\); it is not a new four-dimensional degree of freedom.

## Spinorial sign-return analogy

The quaternionic path obeys
\[
U(0)=+1,\qquad U(\pi)=-1,\qquad U(2\pi)=+1.
\]
Under the ordinary quaternion-to-spatial-rotation map, a spinorial phase angle \(\theta\) corresponds to a spatial rotation angle \(2\theta\). Consequently, the first half of this **chosen** meridian resembles a \(360^\circ\) spinor sign reversal and the full circuit resembles a \(720^\circ\) return.

This identity follows from \(SU(2)\cong S^3\) and from our coordinate choice. It **does not mean** a zeta zero is a fermion, that \(\theta\) is time, that any zeta ordinate is determined, or that a physical spinor dynamics has been derived.

## Extending off the critical line: test of radius constraint

Let \(w=\delta+\mathbf u t\), with \(\delta=\sigma-1/2\). Set
\[
Q(w)=R\,(L+w)(L-w)^{-1}.
\]
Whenever \(L-w\) is invertible,
\[
\frac{|Q(w)|^2}{R^2}
=\frac{(L+\delta)^2+t^2}{(L-\delta)^2+t^2}.
\]
For \(L>0\), \(|Q(w)|=R\) if and only if \(\delta=0\). Thus the unit-radius condition is **equivalent to being on the critical line**, by design.

The statement “all nontrivial zeros lie on \(S^3_R\) under this map” is therefore **exactly a reformulation of RH**, not its proof. Any analytic or physical criterion selecting the sphere over off-sphere zeros must be derived independently.

## Questions this geometry does not yet answer

1. Why should zeros, as opposed to arbitrary critical-line points, be selected?
2. Which operator or action fixes \(L\) or makes it non-arbitrary?
3. Can a globally well-defined complex/quaternionic amplitude pass through the compactified pole?
4. Can a derived arithmetic law (not a fitted zero list) pick out the angular latitudes?

See [equation dictionary](02-equation-dictionary.md), [harmonic series](03-harmonic-series-and-zero-product.md), and [infinity-pole result](04-infinity-pole-and-spinorial-return.md).
