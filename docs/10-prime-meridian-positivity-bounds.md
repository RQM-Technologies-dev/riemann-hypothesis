# Prime Meridian: what can be proved about the signs of the Li coefficients?

**Status: partial mathematical results; not a proof of RH.** No zero locations, zero verification, quadrature, or hypothesis about the zeros enter the two bounds below. The values of the low-order coefficients and the broader asymptotic theory are known. The purpose of these arguments is to test the specific moment approach in note 09, not to claim priority for those facts. Here $n$ is harmonic order, not an index of a zero.

## 1. A finite positivity certificate from the arithmetic value at 4

Use the even, positive Jacobi kernel $\Phi$ in Romik (1.6)–(1.11). The tilted probability distribution $p(v)=e^{v/2}\Phi(v)/\xi(1)$ has moment generating function $M(h)=\xi(1+h)/\xi(1)$. Write $a_j=\mathbb E[V^j]/j!$. Every $a_j$ is strictly positive: after folding the integral onto $v>0$, its extra weight is $2\cosh(v/2)$ for even $j$ and $2\sinh(v/2)$ for odd $j$. Its power series is entire because of the kernel's decay.

Let $G(z)=M(z/(1-z))=1+U(z)$ and $U(z)=\sum_{n\ge1}g_n z^n$. The series for $G$ converges in the open unit disk, irrespective of RH; initially the series for $\log G$ is asserted only near zero. The coefficients are

$$g_n=\sum_{j=1}^n {n-1\choose j-1}a_j,\qquad S_m:=\sum_{k=1}^m g_k=\sum_{j=1}^m {m\choose j}a_j.$$

In particular $g_n$ is positive and nondecreasing. At $h=3$ the actual theta transform gives

$$\sum_{j\ge1}3^j a_j= M(3)-1=2\xi(4)-1=2\pi^2/15-1,$$

using $\xi(1)=1/2$ and $\zeta(4)=\pi^4/90$. Since $\max_{1\le j\le8}{8\choose j}/3^j=28/9$ (attained at $j=2$),

$$S_8\le \tfrac{28}{9}(2\pi^2/15-1)<\tfrac{932}{945}<1.$$

The rational upper bound follows simply from $\pi<22/7$. Define $\log G(z)=\sum_{n\ge1}(\lambda_n/n)z^n$. Then $G'=G(\log G)'$ gives

$$\lambda_n=n g_n-\sum_{j=1}^{n-1}\lambda_j g_{n-j}.$$

Starting with $\lambda_1=g_1$, suppose $0<\lambda_j\le jg_j$ for preceding orders. Then $\lambda_n\le ng_n$, and

$$\lambda_n\ge ng_n-\frac n2\sum_{j=1}^{n-1}g_jg_{n-j}\ge ng_n(1-S_{\lfloor n/2\rfloor}).$$

For the first inequality, pair the weights $j$ and $n-j$ in the convolution. For the second, use $g_{n-j}\le g_n$ on the first half and symmetry for the second half; when $n$ is even this overcounts the middle term, in the safe direction. This proves

$$\lambda_n>\tfrac{13}{945}\,n g_n>0\qquad(1\le n\le17).$$

These seventeen signs are an analytic certificate, not seventeen new numerical measurements. The endpoint 17 is where this certificate stops, not a place where the actual coefficients change sign.

## 2. Positive coefficients at arbitrarily high orders

Write $F=\log G$ for its analytic germ at zero, continued along $[0,1)$ on its real branch; $G(r)>0$ throughout this interval. With $s=(1-r)^{-1}$, the exact completion formula, $\zeta(s)=1+O(2^{-s})$ on the positive real axis as $s\to\infty$, and Stirling give

$$F(r)=\tfrac12s\log s+O(s).$$

Let $H_n=1+1/2+\cdots+1/n$. The coefficient of $z^n$ in $P(z)=\log(1/(1-z))/(1-z)$ is $H_n$. If for some $0<c<1/2$ we had $\lambda_n/n\le cH_n$ for all sufficiently large $n$, the coefficients of $cP-F$ would be eventually nonnegative. By Pringsheim's theorem (after a finite polynomial correction) its Taylor series must have radius at least one: otherwise there would be a singularity at a positive real point below 1, where both $P$ and the real branch of $F$ are analytic. Hence on $0\le r<1$ the function $cP(r)-F(r)$ is bounded below by a fixed polynomial's lower bound. But it equals $(c-1/2)s\log s+O(s)$, which tends to minus infinity. Contradiction.

Consequently $\limsup_{n\to\infty}\lambda_n/(n\log n)\ge1/2$. In particular infinitely many coefficients are strictly positive. This conclusion is consistent with either outcome of RH, and follows also from the stronger asymptotic alternative studied by Voros. It is not a lower bound valid for every sufficiently large order.

## 3. Why the absolute moment estimate cannot deliver all orders

Coefficientwise in a neighborhood of zero, the logarithm splits into odd and even powers of $U$:

$$F=P_+-P_-,\qquad P_+=\tfrac12\log\tfrac{1+U}{1-U},\qquad P_-=-\tfrac12\log(1-U^2).$$

Both $P_\pm$ have nonnegative coefficients, since $U$ does. The coefficient of $P_-$ bounds the negative part of $\lambda_n/n$. But there is a unique $r_*\in(0,1)$ with $G(r_*)=2$: $G(0)=1$, its positive coefficients make it strictly increasing, and it tends to infinity. Exactly, $G(5/6)=4\pi^3/63<2$, whereas $G(7/8)=8\pi^4/225>2$. At $r_*$ the two separate series both diverge logarithmically although $F(r_*)=\log 2$ is regular. Positivity also gives $|U(z)|\le U(|z|)<1$ for $|z|<r_*$. Thus the Taylor radii of $P_\pm$ are exactly $r_*$, and by Cauchy–Hadamard the exponential rate of this negative-part majorant is $r_*^{-1}>1$. Illustratively, solving $2\xi(s_*)=2$ gives $s_*\approx6.064647181$, $r_*=1-1/s_*\approx0.8351099462$, and $1/r_*\approx1.1974471201$. No proof relies on these decimals. They describe the discarded-cancellation estimate, not the true growth of the Li coefficients.

Even the lower estimate $n[z^n](U-U^2/2)$ in the induction cannot be nonnegative at all orders: on $r\uparrow1$ the function $U(r)-U(r)^2/2$ tends to minus infinity. Its Taylor series converges for every $r<1$; with only finitely many negative coefficients it would be bounded below there. Thus the simple inductive lower estimate is negative at arbitrarily high orders, regardless of the true signs.

## 4. The all-orders estimate still missing

Bombieri–Lagarias show it would be enough to establish: for every $\varepsilon>0$ there is a finite $C_\varepsilon$ such that $\lambda_n\ge-C_\varepsilon e^{\varepsilon n}$ for every $n$. A quick analytic explanation: under this bound the generating series of the negative parts of $\lambda_n/n$ converges in the unit disk. Add it to $F$; the resulting germ has nonnegative coefficients and continues along the entire positive radius below 1. Pringsheim's theorem then guarantees Taylor radius at least one. Subtract the negative-part series: $F$ is holomorphic in the disk, so its exponential $G$ is zero-free there. The map $s=1/(1-z)$ maps this disk onto $\Re s>1/2$; reflection excludes zeros on the other side. Li's theorem yields all the desired signs. This paragraph proves the implication, not its hypothesis. A bound with the fixed rate $1.1974\ldots$ does not suffice.

The required missing input is a uniform estimate of the signed difference, not of either positive series separately. Neither the finite certificate nor the positive subsequence supplies it.

## Sources

- Dan Romik, *Orthogonal Polynomial Expansions for the Riemann Xi Function*, §1.1, especially (1.6)–(1.11): https://arxiv.org/abs/1902.06330
- NIST DLMF: completed function https://dlmf.nist.gov/25.4 ; exact even zeta values https://dlmf.nist.gov/25.6 ; Stirling asymptotics https://dlmf.nist.gov/5.11 .
- E. Bombieri and J. C. Lagarias, *Complements to Li's criterion for the Riemann hypothesis*, Theorem 1 and its corollary: https://websites.umich.edu/~lagarias/doc/bombieri.pdf
- Flajolet and Sedgewick, *Analytic Combinatorics*, Theorem IV.6 (Pringsheim): https://algo.inria.fr/flajolet/Publications/book.pdf
- A. Voros, *Sharpenings of Li's criterion for the Riemann hypothesis*: https://arxiv.org/abs/math/0506326
