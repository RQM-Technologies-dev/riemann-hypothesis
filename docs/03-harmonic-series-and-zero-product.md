# 03 — Complex harmonics, primes, and reconstruction from all zeros

## Central intuition

One analytic object can be described using its arithmetic input (primes), its harmonic phases (integers), and its zero structure (Hadamard reconstruction). These are **different valid representations** with different domains. The purpose of the quaternionic polar picture is to represent the conjugate relation without making any individual zero a separate sphere or individually adjusting its radius.

## 1. Harmonic phase on a complex line

For a positive integer \(n\),
\[
n^{-s}=n^{-\sigma}e^{-it\log n}
=n^{-\sigma}\left(\cos(t\log n)-i\sin(t\log n)\right).
\]

- \(s=\sigma+it\): complex input.
- \(\sigma\): magnitude decay exponent.
- \(t\): imaginary spectral height; not time.
- \(\log n\): angular frequency *with respect to height*.
- \(\cos,\sin\): real and imaginary quadrature components.
- \(n^{-\sigma}\): magnitude of the individual term.
- \(i\): complex imaginary unit.

For \(\sigma>1\), the sum over \(n\ge1\) is \(\zeta(s)\). At \(\sigma=1/2\) the original nonalternating sum **does not converge**. Consequently, “the harmonic terms cancel at each zero” is a heuristic unless one specifies the analytically continued or convergent representation used to define the sum. A concrete alternative for \(\sigma>0\) is the alternating Dirichlet eta function, \(\eta(s)=(1-2^{1-s})\zeta(s)\).

## 2. Reverse phase and conjugation

For a fixed term,
\[
n^{-\sigma-i(-t)}=n^{-\sigma+it}
=\overline{n^{-\sigma-it}}.
\]
For a fixed slice \(\mathbf u^2=-1\), the same holds under the formal replacement \(i\mapsto\mathbf u\):
\[
n^{-\sigma-\mathbf u(-t)}
=\overline{n^{-\sigma-\mathbf u t}}.
\]

This formal quaternionic slice identity changes neither the underlying complex zeta function nor its zero locations.

Take the global angle \(t=L\tan(\theta/2)\). Then
\[
e^{-it\log n}
=
\exp\left[-iL\log n\tan(\theta/2)\right],
\]
and for each \(\theta\ne\pi\):
\[
h_n(2\pi-\theta)=\overline{h_n(\theta)}.
\]

**What this establishes:** the return half is conjugate to the outward half, term by term, at corresponding finite heights.  
**What it does not establish:** that individual phases have a common finite limit at \(\theta=\pi\).

## 3. Prime product is Euler's, not Gamma's

For \(\Re s>1\):
\[
\zeta(s)=\sum_{n\ge1}\frac1{n^s}
=\prod_{p\ {\rm prime}}\frac1{1-p^{-s}}.
\]
Unique prime factorization gives the product. It does not converge as an Euler product on the critical line.

Separately, the Euler **Gamma function** appears in:
\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]
Gamma is an analytic-completion factor implementing the reflection symmetry, not a direct “inverse of the product of all primes.” The reciprocal Gamma function has its own Weierstrass product over positive integers. Confusing these two Euler formulas would silently introduce an invalid equality.

## 4. The exact completed reflection

The completed function is entire and obeys
\[
\xi(s)=\xi(1-s),\qquad \xi(\bar s)=\overline{\xi(s)}.
\]
Let
\[
X(t)=\xi(1/2+it).
\]
Then \(X(t)\in\mathbb R\) and \(X(-t)=X(t)\). So a pair \(\rho=1/2\pm i\gamma\) maps to two angular occurrences of the **same zero** in a fixed oriented meridian:
\[
\theta_\gamma=2\arctan(\gamma/L),\qquad
\theta_{-\gamma}=2\pi-\theta_\gamma.
\]

For all imaginary orientation axes \(\mathbf u\), these become the same (unoriented) two-sphere in \(S^3\). The outward-versus-return distinction requires the extra orientation or parametrization label.

## 5. From the complete zero set back to one equation

For all nontrivial zeros \(\rho\), with multiplicity, the entire function admits a canonical Hadamard product
\[
\xi(s)=e^{A+Bs}\prod_{\rho}
\left(1-\frac{s}{\rho}\right)e^{s/\rho}.
\]
Here:
- \(\rho\): *complex-valued zero*, wherever it lies in the critical strip.
- \(A,B\): constants fixed by normalization/symmetry.
- \(\prod_\rho\): canonical product over the complete zero multiset; factors make convergence rigorous.
- \(e^{s/\rho}\): convergence-correcting factor.
- This product reconstructs \(\xi(s)\) from its zeros and normalization; it **does not derive the zeros independently**.

If (and only if, as a full-family statement) RH holds, all the zeros can be paired by positive real ordinates \(\gamma_n\), and
\[
X(t)=X(0)\prod_{\gamma_n>0}
\left(1-\frac{t^2}{\gamma_n^2}\right).
\]
The corresponding polar expression is
\[
F(\theta)=X(0)\prod_{\gamma_n>0}
\left(1-
\frac{\tan^2(\theta/2)}
     {\tan^2(\theta_n/2)}
\right),
\quad \theta\ne\pi,
\]
again conditional on RH. Each angular zero position is determined by the original zero height, not by independent resonance physics.

## 6. An unconditional, one-equation angular field

No assumption about RH is necessary to define
\[
\boxed{
F(\theta)=\xi\left(\frac12+iL\tan\frac{\theta}{2}\right)
}
\quad(\theta\ne\pi).
\]
This is one scalar field on a compactified meridian with:
\[
F(2\pi-\theta)=F(\theta)\in\mathbb R
\]
and the known critical-line zeros at their corresponding angular coordinates.

The **new proposed research step** is not to place known zeros into an angular product, but to derive a separate operator/functional equation whose admissible angular modes give the same set, without first using \(\xi\) or \(\gamma_n\).

## 7. Why this connects historically to Dirac, without using physical time

The quaternionic unit \(\cos\theta+\mathbf u\sin\theta\) is an element of \(SU(2)\), so a half-meridian gives the central sign \(-1\), followed by \(+1\) after the whole circuit. This is a **representation-theoretic analogy** to spinorial double return. It is not a Dirac-equation explanation of the Riemann zeros.

The harmonic conjugation \(e^{-it\log n}\mapsto e^{+it\log n}\) and the quaternionic sign-return \(+1\to-1\to+1\) are **different transformations** that are compatible in our chosen polar parametrization. A genuine novel theorem would have to link them through an independent analytic, spectral, or arithmetic selection principle.

## References

- NIST DLMF §25.4, completed zeta and reflection: https://dlmf.nist.gov/25.4
- NIST DLMF §5.11, Gamma asymptotics: https://dlmf.nist.gov/5.11
- Perfect Closure archive, quaternionic lift: https://github.com/RQM-Technologies-dev/perfect-closure/blob/main/archive/zeta-critical-line-program/papers/02-perfect-closure-is-quaternionic.md
- Perfect Closure archive, spectral bridge: https://github.com/RQM-Technologies-dev/perfect-closure/blob/main/archive/zeta-critical-line-program/papers/04-zeta-mass-closure-operator.md
