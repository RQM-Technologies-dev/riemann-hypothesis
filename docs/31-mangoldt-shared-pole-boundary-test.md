# 31 — Two-sided pole matching test: raw Mangoldt field versus completed xi

**Date:** 2026-11-08
**Research question:** With \(x>0\), \(t=\log x\), and \(Q_L(x,u)=(L+ut)/(L-ut)\), does the shared \(x\to0^+\), \(x\to+\infty\) quaternionic pole force the reciprocal von Mangoldt arithmetic to match, and does that impose a zero-location constraint on Riemann xi?

**Verdict:** No, not from pole identification or smooth matching alone. The raw Mangoldt harmonics fail continuity at the pole; the completed xi field is smooth and infinitely flat, but a controlled even positive-theta perturbation with explicit off-line zeros has precisely the same smooth pole matching. This establishes a rigorous obstruction to the proposed *boundary condition alone* as an RH mechanism. It does not exclude a future arithmetic-specific operator theorem.

## 1. Exact Cayley identification of the two ends

For \(L>0\) and \(u^2=-1\), define \(t=\log x\) and
\[
Q_L(x,u)=\frac{L+ut}{L-ut}
=\exp(u\theta),\qquad \theta=2\arctan(t/L).
\]
Then \(Q_L(1/x,u)=\overline{Q_L(x,u)}\) and
\[
\lim_{x\to0^+}Q_L(x,u)=\lim_{x\to\infty}Q_L(x,u)=-1.
\]
The circle is a fixed complex slice of \(S^3\). **The two limits are identified in the coordinate; field values require a separate limit proof.**

## 2. Raw reciprocal-prime distribution fails continuous pole matching

For a finite cutoff \(N\), define the paired von Mangoldt field (Chapter 30)
\[
F_N(t)=2\sum_{n=2}^N\frac{\Lambda(n)}{\sqrt n}\cos(t\log n).
\]
It is even: \(F_N(-t)=F_N(t)\). This identity compares values at finite opposite heights, but does not imply a limit at either infinity.

For \(N=2\), \(F_2(t)=\sqrt2\log2\cos(t\log2)\). Set
\[
t_k=\frac{2\pi k}{\log2},\qquad
t'_k=\frac{(2k+1)\pi}{\log2}.
\]
Both approach \(+\infty\), and hence \(Q_L(e^{t_k},u)\), \(Q_L(e^{t'_k},u)\to-1\), yet
\[
F_2(t_k)=+\sqrt2\log2,\qquad F_2(t'_k)=-\sqrt2\log2.
\]
No continuous extension to the shared pole exists even in the one-prime case.

This remains an obstruction for an **absolutely convergent infinite weighted sum**. For \(\sigma>1\), let
\[
F_\sigma(t)=2\sum_{n\ge2}\Lambda(n)n^{-\sigma}\cos(t\log n).
\]
The series converges uniformly and absolutely. If \(F_\sigma(t)\to c\) as \(t\to+\infty\), the time mean \(T^{-1}\int_0^T F_\sigma(t)e^{-it\log2}dt\to0\). However, termwise averaging is justified by absolute convergence, and orthogonality of distinct frequencies makes that limit precisely \(\Lambda(2)2^{-\sigma}>0\). Contradiction. Thus even the regular Dirichlet half-plane version has no pole limit. At \(\sigma=1/2\), the unsmoothed series is not ordinarily convergent and must not be used as a function.

Quaternionic fixed-slice exponentials \(e^{ut\log n}\) similarly wind without a limit. Pairing them with their conjugates produces the scalar cosine field, not a noncommutative new boundary constraint.

## 3. Completed xi has smooth, infinitely flat pole closure

Let \(X(t)=\xi(\tfrac12+it)\). Gamma-factor exponential damping, polynomial bounds for zeta on vertical lines and corresponding fixed-order derivative bounds imply for every \(k\) an exponential-times-polynomial decay of \(X^{(k)}(t)\) at \(|t|\to\infty\). Therefore the polar field
\[
\mathfrak X(\theta)=X(L\tan(\theta/2)),\quad \mathfrak X(\pi)=0
\]
extends \(C^\infty\) and satisfies \(\mathfrak X^{(k)}(\pi)=0\) for all \(k\ge0\). This was already established in Chapter 04. The quaternion-valued companion \(\Psi(\theta,u)=\mathfrak X(\theta)e^{u\theta}\) also has smooth conjugate return.

This pole matching is **not** the RH assertion: it follows from the classical functional equation and Gamma damping without assuming the zero-location hypothesis.

## 4. Decisive negative control: the *same* smooth pole, with off-axis zeros

Use the Chapter 24 positive-even shifted-kernel construction
\[
\Xi_\varepsilon(z)=\Xi(z)\bigl(1+0.98\cos z\bigr),
\quad \Xi(z)=\xi(\tfrac12+iz).
\]
For real \(t\), \(|1+0.98\cos t|\le1.98\) and all fixed-order derivatives of this factor are bounded. Hence \(X_\varepsilon(t)=X(t)(1+0.98\cos t)\) also has exponential-times-polynomial decay with derivatives, and its compactified field is smooth and infinitely flat at the very same shared pole.

But the additional factor has explicit nonreal zeros
\[
z=(2k+1)\pi\pm ib,\quad
b=\operatorname{arcosh}(1/0.98)\approx0.201688487798836053.
\]
Under \(s=\tfrac12+iz\), these give off-critical zeros \(s=\tfrac12\mp b+i(2k+1)\pi\) inside the critical strip. They are zeros of the **modified** Xi, not known or alleged zeros of the Riemann Xi function. The modified kernel retains positive-even Fourier-kernel properties but not the exact original Jacobi-theta arithmetic coefficients.

**Rigorous conclusion:** Smooth matching of a completed, conjugate-returning field at the shared zero/infinity pole does not imply that all zeros are on the critical line. This is an explicit counterexample to the proposed boundary-only proof route.

## 5. Universal smoothing also demonstrates nonselectivity

For \(\sigma>1,\varepsilon>0\), the artificially damped field \(e^{-\varepsilon t^2}F_\sigma(t)\) extends smoothly and infinitely flat under the Cayley compactification because all \(t\)-derivatives of \(F_\sigma\) are bounded. Its identical pole limits are thus created by choosing a damping envelope; they cannot constrain zero locations without an independent arithmetic principle. This is a negative control, **not** an alternative arithmetic completion of zeta.

## 6. Numeric diagnostics and proof priority

Sample \(F_2\) sequences (amplitude \(\sqrt2\log2=0.980258143468547\ldots\)) remain separated by \(1.960516\ldots\) as the mapped angle approaches \(\pi\). On the true critical line, \(|\Xi(t)|\) at \(t=10,20,40,80\) is approximately \(0.03796785,3.665543\cdot10^{-5},2.117622\cdot10^{-11},2.434263\cdot10^{-24}\). The perturbed field also decays.

**Necessary future ingredient:** a boundary or spectral condition tied to the *exact original theta/von Mangoldt coefficients* and impossible for the Chapter 24 perturbed kernel. Mere pole identification, parity, quaternionic conjugation, continuity, flatness, and a fixed-slice representation cannot prove Weil positivity/RH.

The user’s separate arithmetic objective remains rigorously true: \(39.5=79/2\) is prime in \(\mathbb Z[1/2]\); it is not a newly inserted prime index in Riemann theta.
