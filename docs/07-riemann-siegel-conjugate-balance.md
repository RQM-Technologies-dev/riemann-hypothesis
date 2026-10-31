# 07 — The strongest Dirac-inspired bridge: Riemann–Siegel's conjugate harmonic return

**Investigation dated 2026-10-30.** This is a *mathematical* connection, with zeta height \(t\) as a spectral coordinate, **not time**, and \(\mathbf u\) as a chosen quaternionic imaginary axis, **not a physical spin axis**.

## 1. Gamma supplies the balancing phase

Let
\[
s=\tfrac12+it,\qquad t\in\mathbb R.
\]
Define the Riemann–Siegel theta function with a continuous phase branch:
\[
\boxed{
\vartheta(t)=
\arg\Gamma\left(\tfrac14+\tfrac{it}{2}\right)
-\tfrac t2\log\pi.
}
\]
Here \(\Gamma\) is Euler's Gamma function; the argument uses a continuous branch of its phase along the path. Define Hardy's real-valued function
\[
\boxed{Z(t)=e^{i\vartheta(t)}\zeta(\tfrac12+it)\in\mathbb R}.
\]
This is classical mathematics, not a proposal. The Gamma-driven phase removes the varying phase imposed by the zeta functional equation and makes the critical-line expression real.

The completed zeta function is \(\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\). Along the line, \(s(s-1)=-(t^2+1/4)\) is negative real and the Gamma-power factor has phase \(e^{i\vartheta(t)}\). Therefore we get the **exact** identity
\[
\boxed{
X(t):=\xi(\tfrac12+it)=-A(t)\,Z(t)
}
\]
where
\[
\boxed{
A(t)=\frac{t^2+\tfrac14}{2}\pi^{-1/4}
\left|\Gamma\!\left(\tfrac14+\tfrac{it}{2}\right)\right|>0.
}
\]
Every term has a clear role:
- \(X(t)\): real, even completed zeta amplitude;
- \(Z(t)\): real harmonic interference function with the same critical-line zeros;
- \(\vartheta(t)\): **Gamma-controlled phase balance**;
- \(A(t)\): positive Gamma-based amplitude envelope, which decays exponentially at large \(|t|\);
- \(t\): imaginary height, not time.

Because \(A(t)\) never vanishes at finite real \(t\), \(X(t)=0\) if and only if \(Z(t)=0\).

## 2. The conjugate pairs appear explicitly in the Riemann–Siegel formula

For \(t>0\), put
\[
M(t)=\left\lfloor\sqrt{\frac{t}{2\pi}}\right\rfloor,
\qquad
\phi_n(t)=\vartheta(t)-t\log n.
\]
The classical Riemann–Siegel formula is
\[
\boxed{
Z(t)=2\sum_{n=1}^{M(t)}
\frac{\cos\phi_n(t)}{\sqrt n}
+\mathcal R_{\rm RS}(t)
}
\]
with its standard remainder \(\mathcal R_{\rm RS}(t)\), asymptotically \(O(t^{-1/4})\) as \(t\to\infty\). The remainder **must not be silently discarded**, particularly for the first few zero heights.

By Euler's identity, each term is exactly a **pair of conjugate complex waves**:
\[
\frac{2\cos\phi_n}{\sqrt n}
=\frac1{\sqrt n}\left(
e^{i\phi_n}+e^{-i\phi_n}\right).
\]
This is the precise mathematical counterpart of “two phases balancing into one real response.” It is *already a known decomposition*, and it derives from the functional equation and analytic approximation rather than from a quaternionic physical mechanism.

For a chosen quaternionic slice \(\mathbf u\), define the analogous polar pair:
\[
W_M(t,\mathbf u)=
\sum_{n=1}^{M(t)}\frac{e^{\mathbf u\phi_n(t)}}{\sqrt n},
\qquad
B_M=W_M+\overline W_M.
\]
Since \(e^{\mathbf u\phi}=\cos\phi+\mathbf u\sin\phi\),
\[
\boxed{B_M(t)=2\sum_{n=1}^{M(t)}\frac{\cos\phi_n(t)}{\sqrt n}\in\mathbb R.}
\]
The axis \(\mathbf u\) disappears from the scalar sum: all quaternionic slices express the same real balance. The full zeta condition is
\[
\boxed{B_M(t)+\mathcal R_{\rm RS}(t)=0.}
\]
This is an exact zero equation if the Riemann–Siegel remainder is retained, but it is **not a proof of RH** or an independent derivation of zero positions.

## 3. Write the entire balance equation in polar coordinates

Fix \(L>0\) once for all zeros. With
\[
t(\theta)=L\tan\frac{\theta}{2}
\quad(0<\theta<\pi),
\qquad
U(\theta,\mathbf u)=\cos\theta+\mathbf u\sin\theta,
\]
the scalar completed field is
\[
\boxed{
F(\theta)=
-A(t(\theta))\left[
2\sum_{n=1}^{M(t(\theta))}
\frac{\cos(\vartheta(t(\theta))-t(\theta)\log n)}{\sqrt n}
+\mathcal R_{\rm RS}(t(\theta))
\right].
}
\]
Thus one compact angular expression contains:
- *Gamma phase correction* \(\vartheta\);
- *arithmetic logarithmic frequencies* \(\log n\);
- *the positive decay envelope* \(A\);
- *conjugate real pairing* \(2\cos\);
- *the infinity pole* \(\theta\to\pi\).

There are **no zero-by-zero radius normalizations**.

For \(\pi<\theta<2\pi\), extend by the exact completed symmetry \(F(2\pi-\theta)=F(\theta)\); equivalently use \(t<0\) and the same \(X(t)\). The related quaternionic constructed field
\[
\Psi(\theta,\mathbf u)=F(\theta)U(\theta,\mathbf u)
\]
obeys \(\Psi(2\pi-\theta)=\overline{\Psi(\theta)}\).

## 4. New numerical check: the remainder matters

These are 50-digit \`mpmath\` checks with \`siegeltheta\` and \`siegelz\`; values in the table are rounded.

| Height \(t\) | \(M(t)\) | Exact \(Z(t)\) | Conjugate-pair sum \(B_M(t)\) | Required remainder \(Z-B_M\) |
|---:|---:|---:|---:|---:|
| First critical zero \(\approx14.134725\) | 1 | \(\approx0\) | \(-0.314438\) | \(+0.314438\) |
| Second critical zero \(\approx21.022040\) | 1 | \(\approx0\) | \(-0.437581\) | \(+0.437581\) |
| 30 | 2 | \(0.596029\) | \(0.988948\) | \(-0.392920\) |
| 50 | 2 | \(-0.340735\) | \(0.005320\) | \(-0.346055\) |
| 100 | 3 | \(2.692697\) | \(2.239451\) | \(+0.453246\) |
| 200 | 5 | \(5.589784\) | \(5.413960\) | \(+0.175824\) |
| 500 | 8 | \(1.472448\) | \(1.723691\) | \(-0.251244\) |

The pair sum doesn't vanish at a zero by itself. The **full conjugate balance, including the remainder**, vanishes. This is a check of the classical formula; the remainder was evaluated as the exact difference \(Z-B_M\), not predicted independently from an asymptotic expansion.

## 5. What happens at infinity?

Stirling's formula yields
\[
A(t)\sim C\,|t|^{7/4}e^{-\pi|t|/4}
\]
for some fixed \(C>0\); \(|Z(t)|=|\zeta(1/2+it)|\) has at most polynomial growth. Hence \(F(\theta)\to0\) rapidly at the compactified pole.

Meanwhile,
\[
M(t)\sim\sqrt{\frac{|t|}{2\pi}}\to\infty,\quad
\phi_n(t)\text{ continues winding as }|t|\to\infty.
\]
The increasing number of conjugate terms and their individual phase oscillations do **not** have a well-defined termwise limit at infinity; yet the completed total field has a smooth, infinitely flat zero there.

**This is the precise connection to the user's insight:** there is a mathematically exact *paired-wave balance* before and after the same polar infinity pole, but the complete field—not individual waves—is the object with a smooth return.

The Riemann–Siegel cutoff \(M(t)\) changes discontinuously at certain heights; its remainder compensates so the full \(Z(t)\) remains smooth. The decomposition should not be treated as individually smooth terms across those thresholds.

## 6. Why this is more useful than a physical Dirac analogy

The Dirac analogy supplied the language of conjugate components and a spinorial sign-return on the chosen quaternionic meridian. The Riemann–Siegel formula supplies **the actual analytic pairing law for the zeta function**. It requires no physical time, charge, mass, or quantum particle.

But it says only how \(\zeta(1/2+it)\) behaves on the critical line. It does **not** exclude zeros of \(\zeta(\sigma+it)\) for \(\sigma\ne1/2\). Any future “perfect closure proves RH” proposal must establish an independent off-line obstruction.

## Next independent mathematical target

Use the completed theta/Gamma phase and the known arithmetic periods to formulate a fixed, non-fitted operator or positive form on the compact meridian. Its domain must handle the flat nonanalytic infinity pole. The test is not whether the on-line sum can be rewritten (it can), but whether the operator forces *all* zeros onto this balanced meridian **without presupposing that conclusion**.

## References

- DLMF §25.10: Hardy \(Z\), Riemann–Siegel theta and Riemann–Siegel formula: https://dlmf.nist.gov/25.10
- DLMF §25.4: completed zeta and reflection: https://dlmf.nist.gov/25.4
- DLMF §5.11: Gamma asymptotics: https://dlmf.nist.gov/5.11
- DLMF §25.2: original and alternating Dirichlet series: https://dlmf.nist.gov/25.2
