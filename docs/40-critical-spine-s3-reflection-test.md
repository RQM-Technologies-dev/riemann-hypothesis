# 40 — Critical spine S² inside S³: reflection and off-spine negative control

**Date:** 2026-11-08. **Status:** Exact geometric theorem and numerically checked counterexample to geometry-only zero exclusion. **RH not proved.**

## Geometry and distinction between S³ and full quaternion space

Write \(q=a+xi+yj+zk\in\mathbb H\). The reflection \(R(q)=-a+xi+yj+zk=-\bar q\) is an orthogonal involution of the underlying real 4-space. Its fixed locus in \(\mathbb H\) is the three-dimensional imaginary hyperplane \(a=0\); its intersection with the unit \(S^3\) is an \(S^2\), \(a=0,\ x^2+y^2+z^2=1\). The map \(R\) is **not** a unital quaternion-algebra automorphism; it is a real-linear geometric isometry. On each radius \(r>0\), the fixed set is \(S^2_r\).

Center the completed zeta function: \(f(z)=\xi(1/2+z)\), even and real on the real axis. Its intrinsic slice extension \(F(q)\) has spherical zero sets \(\{a+u t:u^2=-1\}\) for nonreal complex zeros \(a+it\). The functional equation gives the reflected sphere at \(-a\). RH says all nontrivial zeta zeros have \(a=0\); geometrically every such zero sphere lies in the imaginary fixed hyperplane. **The fixed \(S^2\) on the unit sphere is only a normalized directional cross-section**: it is not the complete set of zeros, nor does it contain zeros at all radii.

## The direct negative-control test

Use the positive-even theta-kernel perturbation of Chapter 24:
\[
f_\varepsilon(z)=f(z)\bigl(1+0.98\cosh z\bigr).
\]
The multiplicative factor is even and real on the real axis, so it preserves the same reflection symmetry and intrinsic quaternionic lift. Yet its additional zeros occur at
\[
z=\pm b+i(2m+1)\pi,\qquad b=\operatorname{arcosh}(1/0.98)=0.201688487798836053\ldots
\]
together with complex conjugates, yielding reflected off-spine zero spheres at \(a=\pm b\). For the *modified* completed function these correspond to off-critical-line zeros at \(s=1/2\pm b+i(2m+1)\pi\); **these are not zeros of the original xi function**.

At \(m=0,1\), high-precision evaluation gave absolute residuals approximately \(1.10\times10^{-37}\) and \(9.28\times10^{-37}\) for \(1+0.98\cosh(b+it)\). The exact positive folding deficit introduced by the perturbation is
\[
\Delta\mathcal D_0=
\frac{\tanh(b/2)}{4b}-\frac{\operatorname{sech}^2(b/2)}8
=0.00084061113274389191045\ldots>0.
\]
The original Chapter 24 proof supplies this identity. Consequently the same critical spine, conjugate return and positive-even shifted kernel permit strictly off-spine zeros. Reflection alone does not force the folding deficit to vanish.

## Is the quaternionic spine adding independent information?

Not yet. For an intrinsic slice-regular extension, the location of zero spheres is determined by the original complex zero locations. Reflection of the scalar coordinate and passage from complex conjugate pairs to quaternionic 2-spheres is a faithful geometric restatement. An independent theorem would need a **theta-specific** operator or inequality, valid at every height, that forces \(\mathcal D_0=0\) and demonstrably fails for the shifted-kernel control. The spine topology by itself is insufficient.

## Reproducibility

\`experiments/critical_spine_s3_test.py\` checks involution, fixed-locus geometry, the off-spine roots and the positive deficit. Numerical checks supplement, but do not replace, the exact algebraic arguments.

**Next gate:** Seek a canonical quaternionic coupling of theta-derived arithmetic modes across noncommuting axes that is *not* equivalent to the intrinsic slice extension. Demand a proved compatibility with original xi and a genuine zero-exclusion inequality; otherwise retain the spine as useful geometry, not a proof.

**Prior chapters:** 21–24, 32–39. **Dyadic arithmetic:** 39.5=79/2 remains prime in \(\mathbb Z[1/2]\), but is not an additional ordinary zeta Euler factor.
