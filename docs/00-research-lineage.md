# 00 — Research lineage and what was deliberately retained

This file preserves the conversation's conceptual and mathematical progression leading into the **quaternionic polar-return hypothesis**. It is not a claim that each previous exploratory calculation has been independently rerun in this repository.

## A. Dirac electron and the original intuition

1. Conventional spin-\(\tfrac12\) is represented by \(SU(2)\) spinors. A \(2\pi\) spatial rotation reverses the spinor sign, and a \(4\pi\) spatial rotation restores it. Unit quaternions provide the equivalent polar representation \(q=\cos(\varphi/2)+\mathbf u\sin(\varphi/2)\).
2. The motivating interpretation was **balance as resonance**: if \(q(\theta)=\cos\theta+\mathbf u\sin\theta\), then \(|q|^2=1\), and changing quadrature components preserve that norm.
3. A Dirac-type mass-shell construction using the existing \(S^3\) shell operator \(\hat N=\sqrt{-\Delta_{S^3}+1}\) gave a *compatible* dispersion law \(E^2=p^2c^2+(\varepsilon_C n)^2\). But the energy scale \(\varepsilon_C\) and left/right coupling were imposed, not derived. The simple first-three-shell interpretation of electron/muon/tau masses failed.
4. **Boundary:** the current Riemann-zeta program treats spinorial geometry solely as an \(SU(2)\) mathematical analogy. The complex height \(t\) is NOT time; there is no electron or mass hypothesis in the polar-zero investigation.

## B. Dirac-like zeta representation

The chiral Hermitian two-channel matrix
\[
H_\xi(s)=\begin{pmatrix}0&\xi(s)\\\overline{\xi(s)}&0\end{pmatrix}
\]
has eigenvalues \(\pm|\xi(s)|\). Zeta zeros become zero-energy degeneracies of this constructed matrix. Near a simple critical-line zero, its linearization is Dirac-cone-like in \((\delta,t-\gamma)\), but **all simple zeros would have this local behavior**, including hypothetical off-line ones.

A reflection-invariant polynomial multiplier can introduce an off-line quartet without breaking the completed-function mirror symmetry. Therefore conjugation, chiral block form, local phase winding, and norm closure alone do not force RH. The earlier work also considered the Laguerre differential expression \(X'^2-XX''\), which is a known analytic diagnostic and not a new proof of RH.

## C. Independent spectral model, investigated then set aside

An exploratory half-line chiral operator
\[
\mathcal D_0=
\begin{pmatrix}0&-\partial_x+W(x)\\
\partial_x+W(x)&0\end{pmatrix},
\qquad W(x)=4\pi e^{2x}
\]
was chosen because its leading high-energy counting asymptotics have a \(T\log T\) shape matching Riemann–von Mangoldt. This **does not** mean its eigenvalues are the zero ordinates. Earlier exploratory first-eigenvalue and prime-correction comparisons did not reproduce the individual zeros or outperform null controls. These previous numerical metrics have *not* been independently reproduced inside this new repository.

The current work deliberately does **not** introduce an ad hoc prime-correction fit. See the separate [completed-zeta-stability](https://github.com/RQM-Technologies-dev/completed-zeta-stability) and the archived [Perfect Closure](https://github.com/RQM-Technologies-dev/perfect-closure) material for background.

## D. Geometric reformulation initiated by the user

The next hypothesis was to interpret a complex critical-line zero \(1/2+i\gamma_n\) as an entire quaternionic imaginary-direction family
\[
\{1/2+\gamma_n\mathbf u:\mathbf u^2=-1\}.
\]
These are concentric two-spheres of different Euclidean radii in the three imaginary coordinates. The user explicitly **rejected independently normalizing each sphere**.

The revised goal is a **single global higher-dimensional bending of the entire line**:
\[
Q(t,\mathbf u)=R(L+\mathbf u t)(L-\mathbf u t)^{-1}
=R e^{\mathbf u\theta(t)},\quad\theta(t)=2\arctan(t/L)\bmod2\pi.
\]
Every mapped point lies on one **ambient four-dimensional** radius \(|Q|=R\). Positive ordinates lie on one half of the chosen meridian, their negatives on the conjugate return half, and \(+\infty\) and \(-\infty\) meet at \(Q=-R\). This is a **global coordinate transformation**, not a per-zero scaling law.

The user then proposed: infinity is the pole of the polar circuit; the conjugate zeros occur as the opposite branch after passing that pole. The central question became whether the opposite traversal is more than a coordinate parametrization, particularly for the individual harmonic phases and the completed zeta function.

## E. Euler primes, Gamma, and the inverse problem

The zeta Dirichlet series is the harmonic starting point; Euler's prime product is valid for \(\Re s>1\). The Gamma factor is part of the entire completed \(\xi\), while **Hadamard factorization** reconstructs \(\xi\) from its complete zero multiset and normalization. The existence of this reverse product is established mathematics. It does not itself select the zeros.

The present investigation focuses on a single polar \(\xi\)-field and the singular infinity pole, retaining a precise difference between **a model reproducing a known symmetry** and **a law forcing zero placement**.

## F. New finding in this repo

The raw harmonic \(n^{-1/2-it}\) has no limit at the infinity pole; its phase oscillates forever as \(|t|\to\infty\). Meanwhile, Gamma completion makes \(X(t)=\xi(1/2+it)\) decay exponentially. Its angular pullback \(F(\theta)\) extends smoothly by zero at the pole, is infinitely flat there, and cannot be analytic there because infinitely many critical-line zeros accumulate.

Thus the quaternionic return field
\[
\Psi(\theta,\mathbf u)=F(\theta)e^{\mathbf u\theta}
\]
is **smooth, conjugate-symmetric, and globally returning** as a constructed field—without implying that the individual harmonics traverse the infinity point continuously, or that RH follows.

## Research rules

- All four quaternion coordinates are mathematical coordinates; no physical fourth spatial dimension is asserted.
- No equation may assume time, mass, or an electron when describing zeta heights.
- Never use a different \(R\) or \(L\) for individual zeros.
- Don't present a coordinate reformulation, a zero-containing product, or a \(\xi\)-dependent operator as an independent proof.
- Check off-line zero counterexamples and the whole spectrum, not only the first few known zeros.
