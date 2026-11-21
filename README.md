# A quaternionic route through Alpöge’s RH proof

This is RQM Technologies’ experimental fork of the **local projector argument** in Levent Alpöge’s announced Lean proof. The fork is distributed as a patch against a pinned revision. The proposed shortcut is to carry one integer from each theta lattice straight to the projected row. [Alpöge’s announcement](https://alpo.ge/remark.pdf) · [Upstream source](https://github.com/leanprover-community/riemann-hypothesis/tree/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9)

## The shortcut

At a finite place, let $Q=M/\Theta$ measure the difference between the ambient lattice and the theta lattice. After multiplying by a uniformizer $\pi$ to depth $e$, the surviving discrepancy has length $R_e(Q)=\operatorname{length}(\pi^e Q)$.

For a row quotient $B$, let $\delta$ be the number of cosets and $u$ the valuation of the subgroup order. The projector maps give the following bound.

$$\boxed{\displaystyle R_{e+u}(B)\;\le\;\frac{R_e(Q)}{\delta}.}$$

The transfer into one coset followed by projection from another is zero. On the matching coset the composite multiplies by the subgroup order. Together the maps account for $\delta$ copies of the surviving row inside the image of the ambient quotient. This skips the intermediate estimate over every subspace. Lean checks the inequality for quaternion-linear transfers by measuring length over the central ring. [Projector proof and replay](direct-projector-replay.md) · [Quaternion-linear theorem](DirectProjectorAudit.lean)

For example, with three cosets and $R_e(Q)=7$, the surviving length of one row is at most two at depth $e+u$. This is where the factor of three enters the proof. It comes from the three copies fitting inside an image of length at most seven.

![Animation showing the surviving length of two lattice quotients as the uniformizer depth increases](docs/figures/scalar-depth.gif)

## What quaternions contribute

Quaternions compress the bookkeeping at conjugate places. For an invertible matrix $A$ over the quadratic subfield, its quaternionic reduced norm is $\det(A)\overline{\det(A)}$. One norm packages both determinant contributions. The scalar remainder retains the depth information a determinant alone loses. The local proof uses orthogonality over the central ring. Exhibiting a quaternion action on the specific arithmetic rows would give a stronger quaternionic interpretation. [Worked example with animation](docs/reading-the-proof.md#what-quaternions-combine)

## How far the fork reaches

**Checked locally.** The scalar estimate passes through completion and ramification. The two transported remainder functions can be installed in the row object and passed to `paired_of_completed` on its original window. The original row entry point reaches **518** project declarations under the audit’s namespace filter. The direct row reaches **488**. It drops 31 declarations, including `threeForms_of`, and adds one. These counts cover the local row proof. [Reproduce the dependency count](direct-projector-replay.md)

**Open globally.** Both arithmetic branches specify their allowance by the same function `rLa`. At the terminal index it reduces to the base-index term plus the Gauss term. The concrete two-run family still needs a checked Lean connection from those allowances to the row inputs. A replay of the modified `Main` and an end-to-end proof-length or runtime saving remain open. [Exact witnesses and remaining obligations](docs/theta-witnesses.md) · [Reproduce the transport checks](docs/scalar-transport.md)
