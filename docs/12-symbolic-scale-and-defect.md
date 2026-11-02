# 12 — Keep \(L\) symbolic: a scale-covariant closure criterion

**2026-11-02. Status:** exact derivations from the completed zeta function and its Hadamard product, with cited finite-height verification where stated. **Not a proof of the Riemann hypothesis.**

## 1. \(L\) is a freely chosen coordinate scale, not a zero location

For **every** \(L>0\), write the unit quaternion meridian as
\[
Q_L(t,\mathbf u)=\frac{L+\mathbf u t}{L-\mathbf u t}
=\cos\theta_L(t)+\mathbf u\sin\theta_L(t),\qquad \mathbf u^2=-1,
\]
\[
\theta_L(t)=2\arctan(t/L)\pmod{2\pi},\quad
w_L(t)=\cos\theta_L(t)=\frac{L^2-t^2}{L^2+t^2},\quad
d_L(t)=1+w_L(t)=\frac{2L^2}{L^2+t^2}.
\]
Thus \(Q_L\bar Q_L=1\) for **all** finite \(t\) and \(L>0\). The latitude \(S^2\) at \(w_L\) has radius \(\sqrt{1-w_L^2}\) in the three imaginary coordinates. This is a single map of the entire line, never one normalization per root.

The nontrivial zeta ordinates \(\gamma_n\) are *properties of \(\zeta\)* and are **independent of \(L\)**. Only the polar coordinates of a known zero vary:
\[
\theta_n(L)=2\arctan(\gamma_n/L),\quad
\frac{d\theta_n}{dL}=-\frac{2\gamma_n}{L^2+\gamma_n^2},\quad
\frac{dw_n}{dL}=\frac{4L\gamma_n^2}{(L^2+\gamma_n^2)^2}.
\]

The scale limits are coordinate degenerations, not new zero theorems:
- \(L\to0^+\): every **fixed** positive height maps toward the infinity pole \(\theta\to\pi,\ w\to-1\).
- \(L\to\infty\): every **fixed** finite height maps toward the north pole \(\theta\to0,\ w\to+1\).
No property of \(\zeta\) changes when the picture is reparametrized.

## 2. The complete \(L\)-family of weighted sums

Let \(\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\), and define
\[
T(L)=L\frac{\xi'(\frac12+L)}{\xi(\frac12+L)},\qquad
S_{\mathrm{line}}(L)=
\sum_{\substack{\gamma>0\\\xi(\frac12+i\gamma)=0}}
\frac{2L^2}{L^2+\gamma^2},
\]
\[
\boxed{D(L)=T(L)-S_{\mathrm{line}}(L).}
\]
Zeros are counted with multiplicity and the on-line sum is over **all** positive real ordinates, not a finite list.

The Jacobi-theta Fourier kernel \(\Phi(v)>0\) gives, for every \(L>0\),
\[
\boxed{
T(L)=L
\frac{\int_0^\infty v\Phi(v)\sinh(Lv)\,dv}
{\int_0^\infty\Phi(v)\cosh(Lv)\,dv}.}
\]
This fixes the total independently of any zero table; the denominator is strictly positive.

The existing proof in [09](09-w-distance-rh-equivalence.md) established positivity of every individual zero contribution for \(L\ge1/2\). The next section extends **the complete paired sum** to all \(L>0\) without falsely claiming each separate off-axis zero term must be positive for small \(L\).

## 3. An unconditional **off-line quartet factor** for every \(L>0\)

Let \(\rho=1/2+\delta+i\gamma\) be an off-critical-line nontrivial zero, where \(0<\delta<1/2\), \(\gamma>0\). Reflection/conjugation produces the complete quartet
\[
\frac12\pm\delta\pm i\gamma
\]
with equal multiplicities. Define \(a=\gamma^2,\ b=\delta^2,\ u=L^2\). The centered, even Hadamard product gives one positive real factor per quartet:
\[
\begin{aligned}
A_{\delta,\gamma}(L)
&=\left|1-\frac{L^2}{(\delta+i\gamma)^2}\right|^2\\
&=\boxed{1+\frac{2(\gamma^2-\delta^2)L^2+L^4}
{(\gamma^2+\delta^2)^2}.}
\end{aligned}
\]

It is a known, rigorously verified fact that the first nontrivial zeta zero has imaginary ordinate approximately \(14.134725\); **every** nontrivial zero has \(\gamma>14\), whereas \(|\delta|<1/2\). Therefore \(\gamma^2-\delta^2>0\), so
\[
A_{\delta,\gamma}(L)>1\qquad\text{for all }L>0
\]
if any off-line quartet exists. We use only the established finite-height zero-free information, not RH.

The exact separated product is
\[
\boxed{
\frac{\xi(\frac12+L)}{\xi(\frac12)}
=
\underbrace{\prod_{\substack{\gamma>0\\\xi(\frac12+i\gamma)=0}}
\left(1+\frac{L^2}{\gamma^2}\right)}_{\text{all critical-line pairs}}
\underbrace{\prod_{\delta>0,\gamma>0\text{ off line}}
A_{\delta,\gamma}(L)}_{\text{all off-line quartets}},
}
\]
with multiplicities and absolute convergence of the centered paired products.

Define the **integrated closure defect**
\[
\boxed{
G(L)=\log\frac{\xi(\frac12+L)}{\xi(\frac12)}
-\sum_{\substack{\gamma>0\\\xi(\frac12+i\gamma)=0}}
\log\left(1+\frac{L^2}{\gamma^2}\right)
=\sum_{\text{off-line quartets}}\log A_{\delta,\gamma}(L)\ge0.
}
\]
Then
\[
\boxed{D(L)=L\,G'(L).}
\]
Each quartet contributes to the derivative
\[
\boxed{
D_{\delta,\gamma}(L)
=
\frac{4L^2(L^2+\gamma^2-\delta^2)}
{((L-\delta)^2+\gamma^2)((L+\delta)^2+\gamma^2)}
>0\quad(L>0).
}
\]
This yields the **all-scale RH equivalence**:
\[
\boxed{\mathrm{RH}\iff G(L_0)=0\iff D(L_0)=0
\quad\text{for one (hence every) }L_0>0.}
\]
The fact that the criterion holds symbolically for all scales does **not** establish that it is satisfied.

## 4. Why sending \(L\to0\) is a trap — and a better scale-free limit

If any off-line quartet exists, \(D(L)>0\) for all \(L>0\), **but nevertheless**
\[
\lim_{L\to0^+}D(L)=0
\]
because every term is \(O(L^2)\). Thus taking the limit of the *unnormalized* distance defect cannot prove RH.

Normalize it *before* taking the limit:
\[
\boxed{
\mathcal E:=\lim_{L\to0^+}\frac{D(L)}{L^2}
=\frac{\xi''(\frac12)}{\xi(\frac12)}
-2\sum_{\substack{\gamma>0\\\xi(\frac12+i\gamma)=0}}\frac1{\gamma^2}.
}
\]
The sum over all critical-line zeros converges. In terms of hypothetical off-line quartets,
\[
\boxed{
\mathcal E=\sum_{\delta>0,\gamma>0\text{ off line}}
\frac{4(\gamma^2-\delta^2)}{(\gamma^2+\delta^2)^2}\ge0.
}
\]
Again every term is strictly positive if an off-line zero exists, hence
\[
\boxed{\mathrm{RH}\iff\mathcal E=0.}
\]
This has **no \(L\) left at all**. It is a valid scale-free *equivalent criterion*, not a proof of the equality.

For reference, direct differentiation gives
\[
\frac{\xi''(\frac12)}{\xi(\frac12)}
\approx 0.0462099862308379415778676208607,
\]
independently of all zero locations. The remaining inverse-square zero sum is the unknown to be shown exhaustive.

## 5. A sharper uniform defect bound from published finite-height verification

The finite-height theorem of Platt and Trudgian proves all nontrivial zeros with \(0<\gamma\le H\), \(H=3\times10^{12}\), are on the critical line. The Bellotti–Wong explicit total-zero count supplies the inverse-square tail bound \(P(H)\le P_+(H)\) derived in [11](11-certified-distance-defect-bound.md).

For an off-line quartet beyond \(H\), put \(a=\gamma^2,\ b=\delta^2,\ u=L^2\). Since \(a\ge2b\), the elementary inequality
\[
\begin{aligned}
&\big((u+a+b)^2-4ub\big)-a(u+a-b)\\
&\qquad=u^2+(a-2b)u+3ab+b^2\ge0
\end{aligned}
\]
implies
\[
\boxed{
0<\frac{D_{\delta,\gamma}(L)}{L^2}
\le\frac{4}{\gamma^2}.
}
\]
Two upper-half-plane roots belong to each off-line quartet, so summing yields the **scale-uniform normalized inequality**
\[
\boxed{
0\le\frac{D(L)}{L^2}
\le2\sum_{\substack{\rho\ \text{off line}\\\Im\rho>H}}\frac1{(\Im\rho)^2}
\le2P_+(H),\qquad L>0.
}
\]

At the fixed external verified height, the published counting bound in [11] yields numerically
\[
P_+(H)\approx1.47970363091503245\times10^{-12},
\]
hence
\[
\boxed{
0\le\frac{D(L)}{L^2}<2.960\times10^{-12}
\quad\text{for EVERY }L>0.
}
\]
The symbolic inequality is rigorous assuming the stated published results; decimal thresholds are rounded conservatively above numerical evaluation, not computed in interval arithmetic.

At the **illustrative** \(L=20\), this improves the earlier bound \(D(20)<1.214\times10^{-9}\) from [11] to
\[
0\le D(20)<1.184\times10^{-9}.
\]
This improvement comes from quartet symmetry, not from a new proof of RH. The uniform normalized bound remains positive and cannot force \(\mathcal E=0\).

## 6. What varying \(L\) can and cannot accomplish

**Can do:** expose an entire positive real-analytic parameter family \(G(L),D(L)\), test the same hidden off-line contribution at multiple scales, show exact invariance of the RH **truth value**, and derive \(L\)-independent moment criteria as above.

**Cannot do:** eliminate an off-line zero simply by choosing a scale, by taking \(L\to0\) without normalization, or by observing high numerical agreement for finitely many \(L\). A hypothetical quartet contributes positive analytic factors at every scale, but those contributions are not guaranteed to vanish.

**Specific new proof target:** use the *special arithmetic structure of the actual Jacobi-theta kernel* to show \(\mathcal E=0\) (or \(G(L_0)=0\) at some fixed \(L_0>0\)) **without assuming** the completeness of real/critical-line zeros. This is equivalent to RH and remains unsolved.

## References and computational assets

- NIST DLMF §25.10: https://dlmf.nist.gov/25.10
- Platt and Trudgian, rigorous verification through \(3\times10^{12}\): https://doi.org/10.1112/blms.12460
- Bellotti and Wong, explicit zero counting: https://doi.org/10.1090/mcom/4133
- Jacobi-theta and Jensen: [10](10-jacobi-theta-jensen-tail.md)
- Previous fixed-scale example: [09](09-w-distance-rh-equivalence.md), [11](11-certified-distance-defect-bound.md)
- [Symbolic-scale numerical diagnostics](../experiments/symbolic_scale_family.py), [test suite](../tests/test_symbolic_scale_family.py), and [example output](../results/symbolic_scale_family.json).
