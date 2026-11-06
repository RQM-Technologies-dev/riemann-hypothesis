# 18 — Mirror-channel folding, superposition, and zero-collision obstruction

**Date:** 2026-11-06. **Status:** Exact identities, a refined research question, and proposed tests; **not a proof of RH**.  
**User's central distinction:** Do **not** interpret the proposal as "symmetry alone proves RH." Investigate the **coupled interaction** of reflected zero sets: can their folded or superposed structure, together with *the actual Jacobi-theta kernel*, constrain the location where the zero equations can be satisfied?

Continues [16 — two-fold zero-spheres and theta positivity](16-two-fold-zero-spheres-and-theta-positivity.md) and [17 — Clay proof target](17-clay-statement-and-proof-roadmap.md).

## 1. Two reflected spherical channels, not just two mirrors

Let \(w=s-\tfrac12=a+it\) and the intrinsic slice-regular quaternionic extension have the paired zero-spheres

\[
\mathcal S_{a,t}=\{a+ut:u^2=-1\},\qquad \mathcal S_{-a,t}.
\]

Their real spherical factors are

\[
Q_\pm(q)=q^2+(a^2+t^2)\pm2aq.
\]

The quartet factor is

\[
\boxed{P(q)=Q_+(q)Q_-(q)=[q^2+(a^2+t^2)]^2-(2aq)^2.}
\]

This organizes the two factors into a common, mirror-even part \(q^2+a^2+t^2\) and an opposite-sign splitting part \(2aq\). The 2-by-2 algebraic block

\[
M(q)=\begin{pmatrix}q^2+a^2+t^2&2aq\\2aq&q^2+a^2+t^2\end{pmatrix}
\]

has determinant \(P(q)\) and diagonalizes into the two mirror-parity channels \(Q_\pm\). This is a **formal algebraic channel model**, not an independently defined physical Hamiltonian or proof-generating self-adjoint operator. The coefficient \(a\) is already the putative zero's displacement; inserting it into \(M\) does not explain why it vanishes.

At \(a=0\), the splitting disappears:

\[
Q_+=Q_-=q^2+t^2,\qquad P(q)=(q^2+t^2)^2.
\]

Equivalently, if \(Y=q^2\), the two roots \(Y_\pm=-(t^2-a^2)\pm2iat\) have discriminant

\[
\boxed{\Delta_Y=-16a^2t^2.}
\]

For nontrivial zeros \(t\ne0\), the algebraic collision \(\Delta_Y=0\) is equivalent to \(a=0\). **The difficult problem is deriving that collision from the actual xi function without pre-assuming the zero location.**

**Do not confuse "superposition" with literal addition of two arbitrary zero-spheres:** adding the two factors, multiplying them, or identifying them in a quotient does not make the originals coincide. Physical wavefunction superposition is an analogy; the two-channel equations below give a more precise mathematical implementation.

## 2. An exact *theta-kernel* folded-channel decomposition

Define the completed critical-line xi entire function

\[
\Xi(z)=\xi(\tfrac12+iz)
=2\int_0^\infty\Phi(u)\cos(zu)\,du,
\]

with the original even positive Jacobi-theta kernel \(\Phi\) used in [08](08-theta-kernel-zero-latitudes.md).

For real \(t,a\), set

\[
C(t,a)=\int_0^\infty\Phi(u)\cos(tu)\cosh(au)\,du,
\]

\[
S(t,a)=\int_0^\infty\Phi(u)\sin(tu)\sinh(au)\,du.
\]

Then, by direct expansion of \(\cos((t+ia)u)\),

\[
\boxed{\Xi(t+ia)=2[C(t,a)-iS(t,a)],\quad
\Xi(t-ia)=2[C(t,a)+iS(t,a)].}
\]

The channels obey \(C(t,-a)=C(t,a)\), \(S(t,-a)=-S(t,a)\). Their mirror-paired product is

\[
\boxed{\Xi(t+ia)\Xi(t-ia)=4[C(t,a)^2+S(t,a)^2]\ge0.}
\tag{1}
\]

This is an **exact nonnegative real expression** for real \(t,a\), not a newly proved strictly positive bound. It can vanish **only if both channels vanish**:

\[
\Xi(t+ia)=0\quad\Longleftrightarrow\quad
C(t,a)=S(t,a)=0.
\tag{2}
\]

The imaginary Xi height coordinate has a sign reversal relative to the original centered \(w=a+it\): \(\Xi(t+ia)=\xi(\tfrac12-a+it)\). By the functional equation, this does **not** change the paired-zero argument. Keep the two coordinate conventions distinct.

### Why the fold matters

At the critical fold \(a=0\),

\[
S(t,0)=0\quad\text{identically},\qquad
C(t,0)=\tfrac12\Xi(t).
\]

Thus an on-line zero requires only the cosine-channel cancellation \(C(t,0)=0\). Off the fold \(a>0\), an off-line zero requires the **simultaneous collision** of both cosine/hyperbolic and sine/hyperbolic channels.

This is the researchable interpretation of the user's "folded superposition": seek a theta-specific reason why the two channels cannot cancel **simultaneously** away from the fold. This is stronger conceptual structure than merely restating reflection invariance, though (2) itself is still an RH-equivalent zero criterion.

### Cauchy–Riemann coupling

Analyticity relates the two channels:

\[
\boxed{\partial_a C=\partial_t S,\qquad
\partial_t C=-\partial_a S.}
\tag{3}
\]

The channels are not independent arbitrary functions. This coupling may support phase-orientation, root-interlacing, or winding arguments. However analyticity alone does not forbid common zeros away from the fold.

Near \(a=0\), Taylor expansion gives

\[
S(t,a)=-a\,\partial_t C(t,0)+O(a^3),\qquad
C(t,a)=C(t,0)+O(a^2).
\tag{4}
\]

Consequently at a **simple** critical-line zero \(t=\gamma\), the odd channel is nonzero for sufficiently small \(a>0\), since \(\partial_t C(\gamma,0)\ne0\). This is a **local analytic observation**, not a global exclusion or an assertion that every xi zero is simple.

## 3. A more direct zero-collision proof target than global modulus growth

The prior roadmap [17](17-clay-statement-and-proof-roadmap.md) uses outward modulus monotonicity
\(\partial_a|\Xi(t+ia)|^2>0\), a sufficient and RH-equivalent global criterion.

The folded-channel framework suggests testing a potentially more targeted property:

\[
\boxed{
\text{For every }a\in(0,\tfrac12],\quad
C(t,a)=0\ \Longrightarrow\ S(t,a)\ne0
\quad\text{for all }t\in\mathbb R.
}
\tag{FC}
\]

This is **exactly an alternative restatement of RH**, because (2) shows a common zero of \(C,S\) iff xi has an off-real zero in the critical strip (including boundary, which is known zero-free). We have **not** proved (FC); calling it a proof without a separate mechanism would be circular.

A stronger candidate lemma could establish that, for fixed \(a>0\), the real zeros of \(C(\cdot,a)\) and \(S(\cdot,a)\) are strictly separated or interlace, with no common roots and a justified global treatment of multiplicities and unbounded heights. Such an interlacing theorem would imply (FC), but it is **not asserted here** as already true or automatically sufficient without proof.

### Hermite–Biehler connection

Csordas and Varga (1989), *Fourier Transforms and the Hermite–Biehler Theorem*, already study exactly the decomposition of shifted Fourier transforms into

\[
P_\mu(x)=2\int_0^\infty K(u)\cosh(\mu u)\cos(xu)\,du,\quad
Q_\mu(x)=2\int_0^\infty K(u)\sinh(\mu u)\sin(xu)\,du.
\]

These are **\(2C\) and \(2S\)** for our theta kernel. Their theorem and corollary yield an RH-equivalent Laguerre/Hermite–Biehler-style criterion on a signed double integral, and provide a serious prior-art starting point. See *Proceedings of the American Mathematical Society* 107 (1989), pp. 645–651, especially Theorem 3.4 and Corollary 3.5: https://www.ams.org/journals/proc/1989-107-03/S0002-9939-1989-0984799-1/ (verify link before using); accessible copy: https://scispace.com/pdf/fourier-transforms-and-the-hermite-biehler-theorem-2zumw94gvz.pdf

**Novelty guardrail:** The mere \(C,S\) decomposition and Hermite–Biehler approach are **not new**. What could be new is a valid theta-specific *mechanism* establishing noncollision/interlacing globally, or a new quaternionic operator yielding that implication without assuming it.

## 4. Proposed investigation sequence

**Task F1 — exact coordinate and parity map.** Derive the \(w\)-plane and \(z\)-plane reflection actions side-by-side, recording how the quaternionic \(S^2\) pairs project to cosine and sine channels. Validate equations (1)–(4) algebraically and with independent high-precision checks. The earlier Cayley \(S^3\) embedding remains distinct and its scale \(L>0\) symbolic.

**Task F2 — track the *individual channel zero curves*.** For several fixed \(a>0\), locate the real zeros of \(C(t,a)\) and \(S(t,a)\), plot their separation and signs at each other's crossings, and identify when numerically near-coincident channels arise. Compare against simple known real-zero entire functions (e.g. \(z^2-\gamma^2\)) and deliberate nonreal-zero counterexamples (e.g. \(2+\cos z\)). These are diagnostics; finite scans do not prove (FC).

**Task F3 — formulate a *global noncollision/interlacing* lemma.** Use the theta modular relation, exact kernel derivatives, and Hermite–Biehler/variation-diminishing tools to seek a uniform statement excluding common zeros for every \(a\in(0,\tfrac12]\) and all real \(t\). Explicitly test whether the lemma merely hides a known equivalent RH assumption.

**Task F4 — try a topological/winding certificate.** On rectangles with nonvanishing boundaries, the winding number of \(C-iS\) around zero counts Xi zeros by the argument principle. Investigate whether theta-specific boundary phase control yields a **uniform zero-count exclusion** independent of a finite-height search. A winding identity alone counts zeros and is **not** a proof that the count is zero.

**Task F5 — return to spherical degeneracy.** Translate any genuine analytic noncollision theorem into \(a=0\), \(\Delta_Y=0\), and the merger \(\mathcal S_{a,t}=\mathcal S_{-a,t}\). Do not assume the desired degeneracy as a premise.

**Near-term deliverable:** (i) a checked two-channel parity diagram and numerical diagnostic of zero-curve crossings; (ii) a clearly stated candidate interlacing/noncollision lemma with citations; and (iii) a failed-step/counterexample report if a global proof cannot be obtained.

## 5. Relation to Clay problem

Official RH target: all nontrivial xi zeros correspond to real zeros of \(\Xi(z)\). This chapter does **not** claim the fold/superposition itself proves that target. It reframes the desired mathematical mechanism as preventing **simultaneous cancellation of two analytically coupled theta channels away from the fold**. Proving (FC) from theta-specific structure, rather than assuming it, would settle RH.

**Relevant sources:** NIST DLMF §25.10 https://dlmf.nist.gov/25.10; Dan Romik, *The Riemann xi function* (theta representation), https://math.ucdavis.edu/~romik/data/uploads/papers/riemannxi.pdf; Csordas & Varga 1989, linked above; [16](16-two-fold-zero-spheres-and-theta-positivity.md); [17](17-clay-statement-and-proof-roadmap.md).
