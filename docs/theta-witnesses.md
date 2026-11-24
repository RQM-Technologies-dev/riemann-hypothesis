# The two theta remainders

Fix a row $i$ and a run $k$ (first or second). Choose the run’s theta family $G$ and its family of local points $Q_\lambda$ once. Use that choice for every base place $\lambda$ in both the local and global estimates. The explicit base witness is

$$r_{k,i}(\lambda)=\operatorname{rLa}(Q_\lambda,C_{Rm},T,c).$$

In the following table $H=\binom{T-1}{\dim Y_j}$ and $j$ is the weight index. The terminal index $j=m$ can occur in **either** run. Selecting a run by the rational place is a separate operation.

| Contribution at $\lambda$ | Interior $j<m$ | Terminal $j=m$ |
| --- | --- | --- |
| Base index | $H\,I_\lambda$ | $H\,I_\lambda$ |
| Étale levels | $H\,T\,\max(0,c)\,\mathrm{Net}_\lambda/(2\,\mathrm{iet})$ | $0$ |
| Gauss coefficient | $\mathrm{gaussC}_\lambda$ | $\mathrm{gaussC}_\lambda$ |
| Quotient length | $\mathrm{lenQ}_\lambda$ | $0$ |

Here $I_\lambda$ is Lean’s natural-number value of `Q.Ila`. The height hypotheses prove its finiteness. The definition of `rLa` switches off the étale contribution at the terminal index. The separate lemma `lenQ_of_ge` proves that the quotient contribution vanishes **at each place**. The terminal formula therefore retains two terms, either of which may require a bound. [Definition of rLa](https://github.com/leanprover-community/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/PublishedIntClosHolds.lean#L371) · [Vanishing of lenQ](https://github.com/leanprover-community/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/LenAtEqZeroOfSubsingleton.lean#L146)

## What “exact witness” means

The expression `rLa` is the particular *allowance* used by the upstream proof. The actual surviving lattice length can be smaller. Over a discrete valuation ring $R$ with fraction field $K$, write the invariant factors of $M/\Theta$ as $R/(\pi^{d_t})$. Then

$$R_e(M/\Theta)=\sum_t (d_t-e)_+
=\max_{U\subseteq M\otimes_R K}
\bigl[\operatorname{length}_R((M\cap U)/(\Theta\cap U))-e\dim_K U\bigr].$$

For the upper bound, $D_U=(M\cap U)/(\Theta\cap U)$ injects into $M/\Theta$, hence $\pi^eD_U$ injects into $\pi^e(M/\Theta)$. Also $D_U/\pi^eD_U$ is a quotient of $(M\cap U)/\pi^e(M\cap U)$, of length $e\dim_K U$. Add these two bounds. For equality choose $U$ spanned by the Smith basis vectors with $d_t>e$. Each contributes exactly $d_t-e$. This elementary identity explains why controlling one scalar length can replace the subspace estimate at a fixed depth. The proposed Lean route obtains the allowance from the theta family and sends the scalar length straight to the projectors.

## Where the terminal witness comes from

In the interior, `theorem_zero_of_refined_inputs` takes the local points from `hQf hj` and passes the explicit function to `concl_of_nat`. At the terminal index, `conclAtM_of_atMInputs` opens `AtMInputs` to obtain its own local points, basis, curve, tie, lift, and heights. The terminal depth bound gives `CombBound`. Following `theorem_zero_of_named_inputs` through the split theorem leads to `sumC` and the same explicit `rLa` expression on those terminal points. In the interior, `rLa_tsum_le_comb` supplies summability and the first sum estimate, and `sumGC4` bounds it by the row budget. In both branches the bound takes the form

$$\sum_\lambda r_{k,i}(\lambda)\,\ell(\lambda)
\;\le\;\operatorname{rk}(M_{k,i})\, f m b\,\delta_2.$$

Here $\ell$ is the base-place weight and $\delta_2$ is Lean’s `large₂.de2`. Both the summability proof and the budget use the chosen points. In particular the bound is uniform over the permitted depths $e$ because the expression for $r$ is independent of $e$. [Interior choice](https://github.com/leanprover-community/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/TheoremZeroOfRefinedInputs.lean#L11) · [Terminal choice](https://github.com/leanprover-community/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/TheoremZeroOfInputs.lean#L47) · [Common witness and budget](https://github.com/leanprover-community/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/TheoremZeroSplitOfLocalAndSum.lean#L185)

## Passing the witness to a row

For a place $v$ over $\lambda$, write $h_v$ for the ramification index. Store $h_v r_{0,i}(\lambda)$ in the first row field and $h_v r_{1,i}(\lambda)$ in the second. The selector chooses the second field when the rational place is the distinguished prime and the first elsewhere. Each conjugate place is evaluated by that same rule. Upstream also handles an empty selector class with the identically zero function. The normalized finite-place weights absorb $h_v$ in each run’s sum. [Concrete selector and empty case](https://github.com/leanprover-community/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasIndexBoundOfRuns.lean#L135)

The RQM row constructor installs the two functions **before** invoking `paired_of_completed`. Its field-identification premise then closes by reflexivity for both Boolean values. This proves the direct index statement for the constructed object on the original window. Its pointwise error includes the remainders at $v$ and its conjugate. Identifying that error with the error of a previously constructed object would require additional information. [Row constructor](../lean/ThetaWitnessRows.lean)

The theorem `paired_on_occupied` implements the empty-class convention. Supply a base function and its bounds for each inhabited selector class. At a member of a pair, that very place proves its class inhabited, so the selector retrieves the supplied function. The zero case has zero weighted sum and requires only nonnegativity of the row budget. In particular, the two functions need no pointwise comparison with each other. [Two-run selection](../lean/ThetaWitnessRows.lean)

## Replay boundary

The coordinate calculation starts from an injective cusp embedding $f$ and an ambient theta lattice $\Theta\subseteq f(M)$. Take $N=M\cap f^{-1}(\Theta)$. Then $f(N)=\Theta$, and after completion the embedding remains injective. The length computed inside the completed span of $f(M)$ equals the completed cusp quotient length at an associated scalar. This equality preserves the local remainder pointwise. [Coordinate calculation](../lean/ThetaCoordinates.lean)

At each base place, Lean also constructs one integral uniformizer whose powers realize *every* prescribed nonnegative depth. Its completed power differs from the geometric uniformizer power by a unit. Combining these facts gives `row_of_theta_length`. Its inputs include the coordinate embedding, lattice containments and the finite theta-coordinate length bound. Its output is the `CompletedRow` needed by the paired constructor at the same depth and with the same base allowance. [Uniformizer powers](../lean/ThetaDepth.lean) · [Completed row](../lean/ThetaRowInput.lean)

The checked theorem `thetaFamilyWitness` takes the chosen points along with the family’s lift, containment and height proofs and returns their scalar allowance and weighted sum. The paired assembly still has to select one such package per populated class and identify its rows. The existing `exists_rem_of_tie` receives an existential `Concl` and asks for an index bound for every subspace. Recovering only a witness with the same sum bound leaves its pointwise values undetermined. [Family producer](../lean/candidates/ThetaFamilyProducer.lean) · [Upstream use of Concl](https://github.com/leanprover-community/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasIndexBoundOfRuns.lean#L100)

The concrete field equalities identify $M$ with the ambient span in row coordinates and the row theta lattice with the span of $f^{-1}(\Theta)$. If $x$ belongs to that preimage, then $f(x)\in\Theta\subseteq f(M)$. Choose $y\in M$ with $f(y)=f(x)$. Injectivity gives $y=x$, so $f^{-1}(\Theta)\subseteq M$ and $N=f^{-1}(\Theta)$. Taking the span after field extension supplies the two inclusions used in `rowOfFamily`. The row theorem `paired_of_theta_points` instantiates the paired constructor with both explicit functions when both selector classes are populated and the row data are supplied in common base coordinates. [Concrete lattice equalities](https://github.com/leanprover-community/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Development/AbelianVarietyTheory/Definitions/Jets/EmbShortThLeThetaPlain.lean#L57)

## How to recover the actual chosen family

The upstream `RunsHold` constructor takes `.2` of an earlier `RunHolds` result, retaining `HypC ∧ Concl`. Its discarded `.1` contains `Inputs4` on the norm-adjusted model, including a terminal local-point package. Projecting it back out would still leave the old `ConclAtM` proof in the constructor’s dependency graph. [Inputs4 and RunHolds](https://github.com/leanprover-community/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Development/AbelianVarietyTheory/Definitions/HeightFunctions/ConclOfInputs4.lean#L64) · [Point where the package is dropped](https://github.com/leanprover-community/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Development/AbelianVarietyTheory/Definitions/Divisors/ExistsFrameOfRichRec.lean#L122)

One level earlier, `inputs4_of_inputsR` exposes the actual choice. It chooses the zero generators and the bounded quotient generators, installs them with `G.setZQ`, and transports each local point by `(Qf la).tr` to that family. **The interior and terminal packages in this constructor use exactly that same expression for the local points.** This is a stronger identification than observing that the two expressions have the same weighted sum. [Chosen-family construction](https://github.com/leanprover-community/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Development/AbelianVarietyTheory/Proofs/HeightProofs/IndexBoundChosenFamilyOfIntrinsicHypotheses.lean#L23)

For run $k$ and row $i$, the formula at the upgraded family is therefore $r_{k,i}(\lambda)=\operatorname{rLa}((Q^k_{i,\lambda})^{\mathrm{tr}},C^k_{Rm},T_i^k,c_i^k)$. The superscript records the transport to the selected generators. The two runs can have different local points and constants. The identities above are for one choice of family. Repeating an existential construction separately would require a proof that the newly chosen witnesses agree pointwise with the old ones.

The theorem `thetaWitnessOfIntrinsic` returns that transported family, its points and their scalar allowance immediately, using the original `CombBound` before it is specialized by branch. This bypasses construction of both the bundled all-subspace conclusion and its terminal proof in this function. `thetaWitnessOfNet` carries the result through the norm change. `thetaRunOnPage` takes the particular finite-net hypothesis on the prescribed page as input, so it can reuse a prior choice without choosing a threshold again. `exists_theta_run` uses the original numerical-threshold constructor to supply that input. Lean checks equality of the normalized and original scalar lengths by reflexivity. The two-run specialization below applies the upstream page hypotheses at the selected place. [Normalized run](../lean/candidates/ThetaChosenInputs.lean) · [Upstream normalized run](https://github.com/leanprover-community/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Development/AbelianVarietyTheory/Proofs/HeightProofs/ExistsThresholdRunHolds.lean#L48)

Finally, `on_of_has_atPlaces` opens `HasIndexBound` and passes its fields to `on_core_atPlaces`, which calls the original `on_core`. A successful replacement must carry the direct variant through that caller and replay the modified `Main`. The original targeted replay covers the coordinate, depth and row lemmas. The experiment below checks the caller using the existing two-run output. The direct construction below now produces both allowances. The modified final theorem still requires integration and replay. [Upstream row contract](https://github.com/leanprover-community/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Development/AbelianVarietyTheory/Definitions/Divisors/RealisedChainTorusEq.lean#L77) · [Row caller](https://github.com/leanprover-community/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/TwistedPlacesBoundChainTwoRunChain.lean#L34) · [Kernel replay instructions](scalar-transport.md#reproduce-the-targeted-experiment)

## Direct construction and same-statement comparison

At an allowed depth $e$, multiplication by $\pi^e$ removes the first $e$ layers of each invariant factor of $M/\Theta$. The quotient $(\pi^e M+\Theta)/\Theta$ records exactly what survives. For the actual theta lattices, `localThetaBudget` bounds its length by the chosen local point’s `rLa`. The family theorem separately proves finiteness before using `ENat.toNat`, and applies the upstream `sumC` estimate to the same points. The reciprocal powers suggest the ordering of depths. All arithmetic weights in the Lean argument come from the theta family. [Local bound](../lean/candidates/ThetaScalar.lean) · [Weighted family bound](../lean/candidates/ThetaFamilyProducer.lean)

The theorem `exists_two_run_depth` takes the original `TwoRuns`, page and field hypotheses. For every place $v$ and admissible row it applies the run selected by `r.used v` with parameter `ownAt D v`. One threshold works for all selections. Its witnesses specify the normalized family and its local points. Their allowance bounds the surviving length on the original model at **every** allowed depth, and its weighted sum satisfies the original rank-times-size bound. The families can differ across selectors. The statement makes no choice for an unoccupied selector class. A transitive dependency audit at this two-run theorem finds the direct family bound and `sumC`, and excludes both `runHolds_of_parOK` and `theorem_zero_of_named_inputs`. [Arithmetic specialization](../lean/candidates/ThetaRunSelectors.lean) · [Two-run audit](../lean/candidates/ThetaRunAudit.lean)

To compare identical conclusions, `concl_via_family_depth` returns the upstream type `Conclusion1OfComb`. It uses the scalar bound first and recovers the inequality for an arbitrary subspace only when returning this interface. The counts below use the same project namespaces and expression-sharing convention as the consumer audit below. [Replacement proof](../lean/candidates/ThetaFamilyComparison.lean) · [Counting code](../lean/candidates/FamilyAuditCounts.lean)

| Proof of the family theorem | Reachable project declarations | Type and body expression nodes |
| --- | ---: | ---: |
| Pinned upstream original | 3,034 | 2,492,857 |
| Same original theorem with the projector patch | 3,027 | 2,480,087 |
| Direct family proof with the projector patch | 3,028 | 2,467,109 |

Relative to pinned upstream the combined change saves 25,748 nodes (1.03%) and six declarations. Holding the projector patch fixed, the direct proof saves 12,978 nodes and adds one declaration. The audit of the family producer finds both `levelsExcessDesc` and `sumC`. It finds none of `localIdx`, `qlen_of_idx`, `threeForms_of` or the original family theorem. The replacement calls `qlen_of_idx` at the public boundary to recover the subspace conclusion. These counts measure the closure of one theorem. Downstream theorems can share dependencies through other paths, so the saving for the full RH entry point requires its own measurement. The independent kernel checker replayed the direct producer, normalized run, selector theorem and comparison theorem. The further row specialization `rowOfFamily` timed out in a separate 200,000-heartbeat test. The longer optional row replay was stopped without a result. Neither row test enters the comparison.

Use the Lean 4.33.1 upstream checkouts described in the [projector replay](../direct-projector-replay.md). The two commands run the original audit in the pristine checkout and the family proofs and audits in the patched one.

```sh
python3 lean/replay_transport.py --family-original "$ORIGINAL_BUILD"
python3 lean/replay_transport.py --family-depth "$PATCHED_BUILD"
```

## Testing the existing two-run output

The upstream `hasIndexBound_of_runs` returns `HasIndexBound O`. Opening this
package gives one lattice, one scalar at each place and row, two separate
allowance functions, and their weighted bounds. At each place the package
supplies the subspace inequality for the selected run. This gives a way to
test the depth proposal without making new choices of local points.

The [paired conversion](../lean/TwoRunDepth.lean) uses `three_forms` to turn
the subspace inequality into a bound on the intersection index.
`three_forms_sum` identifies that index with the surviving quotient length,
expressed as the index of `a M + Θ` over `Θ`. The proof does this at both
members of every place pair. It copies the two weighted bounds directly
from the input. In particular, it never takes a pointwise maximum of the
two runs' allowances, which could increase the weighted sum.

The [consumer replay](../lean/replay_two_run_depth.py) extracts the relevant
definitions and consumers from three hash-checked upstream source files.
It compares the original `on_of_has_atPlaces` with a version that opens the
same package and feeds the converted bound to `on_core_excess`. Both take
the upstream `HasIndexBound` as input. The experiment measures the cost of
using an existing pair of arithmetic runs. Constructing their scalar outputs
directly from the theta families is a separate experiment. Both the consumer and
`hasIndexBound_of_runs` appear in the published declaration graph rooted at the
classical RH theorem. [Upstream dependency graph](https://proofsandreasons.io/rh-graph.html)


### Measured at the same consumer

| Source and route | Reachable project declarations | Lean expression nodes |
| --- | ---: | ---: |
| Pinned upstream, original consumer | 508 | 677,821 |
| RQM projector patch, original consumer | 531 | 705,781 |
| RQM projector patch, depth-based consumer | 527 | 708,156 |

The experimental route adds **19 declarations and 30,335 expression nodes**
relative to the pinned upstream baseline. Within the patched environment,
eight declarations drop out and four enter, but the exclusive declarations
grow from 17,239 to 19,614 nodes. Both consumers still reach
`threeForms_of` through the subspace-to-depth conversion.

The audit follows references within the Formalism, Development and GlobalTheory
namespaces, including the corresponding private names. For each reached
declaration it counts the type and available body separately after sharing
identical subexpressions within each. The baseline build's 636 local upstream
source files matched the pinned originals byte for byte. The final RH entry
point, build time and export size were outside this comparison. The gain from
518 to 488 reported elsewhere is for a row in the patched environment with
a scalar bound already supplied.

From this repository, supply the upstream source directory and the patched
build directory from the [projector replay](../direct-projector-replay.md).
A full patched checkout can serve as both arguments.

```sh
python3 lean/replay_two_run_depth.py "$UPSTREAM" "$PATCHED_BUILD"
python3 lean/replay_two_run_depth.py "$UPSTREAM" "$ORIGINAL_BUILD" --original
```

To install this variant in a separate upstream checkout after the direct projector patch, copy [TwoRunDepth.lean](../lean/TwoRunDepth.lean) into `src/Formalism/LocalToGlobal/IndefiniteForms/IndefiniteTree/` and apply the [caller patch](../two-run-depth.patch). The patch retains the original public theorem name and assumptions.
