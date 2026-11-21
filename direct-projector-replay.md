# Direct projector replay

The patch has two entry points. `levelsExcessDesc` is the scalar-output version of the local estimate called by the theta construction. `on_core_excess` is the scalar-input version of the paired-place row assembly. These are separate theorems. Connecting them on the full arithmetic family also requires the global choice of remainders.

## The scalar that passes through the projector

For the stable lattice pair, let Q denote the ambient quotient and B its character-row quotient. Set δ = [P:U]. If sᵢ and tᵢ are the integral coset maps, Mackey orthogonality gives tᵢsⱼ = |U|·1 when i = j and zero otherwise. For any integral scalar a, replace sᵢ by a·sᵢ with codomain aQ. Restrict tᵢ to that codomain. The composite on the i-th diagonal is now a|U|. The image of the assembled map from aQ to the product of rows contains (a|U|B)^δ. Consequently

    δ · length(a|U|B) ≤ length(aQ).

The code uses extended natural lengths, so this inequality also makes sense before a proof of finite length. On a DVR put a = π^e and u = v(|U|). Multiplication by a unit preserves the scalar image. The inequality becomes δ·R_(e+u)(B) ≤ R_e(Q). The concrete theorem `lemmaGG_with_depth` constructs the maps from the submitted representation and the localized lattice pair. The row assembly uses the existing rank-loss comparison to obtain its original budget. The stronger numerical comparison is checked separately in the audit.

## How to read the patch

| Location | Mathematical change |
| --- | --- |
| `LengthLeOfSemilinear` | Expose the finite bound on length((π^e M + Θ)/Θ) in `localStepExcessQ`. Apply the original pole-level and base estimates to get `localStepLevelsExcessQ`. |
| `LevelsQDesc` | `levelsExcessDesc` carries that bound down the base change in which the uniformizer stays irreducible. The numerator π^e M + Θ commutes with extension of scalars. The signed index of this numerator over Θ equals its quotient length. The original `levelsQDesc` can recover any requested cut at its public boundary. |
| `LemmaGG` | `gg_len_depth` and `lemmaGG_with_depth` give the filtered inequality abstractly and on the concrete coset maps. |
| `OnLocal` and the weighted local conditions | `onLocal_excess_of` accepts the scalar bound directly. `excess_of_theta_sum` identifies the sum-quotient index with the inverse-scaled intersection index, then uses monotonicity to enlarge the initial theta lattice to the stable one. |
| `ExampleSatisfiesConditionsAtFive` | `on_core_excess` uses the scalar at both w and its conjugate. It has the original conclusion `ONwith S N O.errOn`. The two existing ON examples are routed through the new theorem with a directly computed scalar input. |
| `DirectProjectorAudit.lean` | Checks axioms, the quaternion-linear specialization over the central ring, the arithmetic comparison of row budgets, and named dependencies with a legacy positive control. |

## Window and error

`AtPair S` quantifies over both places of each pair for w ∈ S.Tw. The new pair input retains the same a, E, r₁, r₂, δ₂ and the same finite weighted-sum inequalities on those remainder functions. The output retains S.Tw, the tuple S.μ w, both index terms, the local allowance 2/plc(w)² and the final N.E1 j. Applying this output to the full family still requires a direct construction of those same remainders.

## Local proof dependencies

Starting at `on_core`, the audit reaches 518 project declarations. From `on_core_excess` it reaches 488. Their intersection has 487 declarations. The original path uniquely reaches 31 and the direct path uniquely reaches one. The walk follows used constants whose names begin with `Formalism`, `Development`, or `_private.Formalism.`, counting each root once. The counts measure the transitive dependencies of these two row entry points in the patched environment. Whole-project dependencies and build time require a replay of the arithmetic entry point. [Executable audit](DirectProjectorAudit.lean)

## Reproduction

The baseline is the November 20 source archive with SHA-256 `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc`. The ten pre-edit sources were also compared byte for byte with mirror revision `712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9`. The replay uses the project's Lean 4.33.1 and Mathlib revision `0df444a360eaa60ab8c11dca51a86af692955474`. Set PROJECTOR to the directory containing the patch and audit file. From the upstream project root run

```sh
git apply --check "$PROJECTOR/direct-projector.patch"
git apply "$PROJECTOR/direct-projector.patch"
export MATHLIB_CACHE_GET_URL=https://cache.mathlib.org/mathlib4
lake exe cache get
row=Formalism.LocalToGlobal.IndefiniteForms.IndefiniteTree.ExampleSatisfiesConditionsAtFive
theta=Formalism.SharpRestriction.GenusPolyhedralBounds.RelativeIndexClassSets.LevelsQDesc
lake build "+$row:olean" "+$theta:olean"
lake env lean "$PROJECTOR/DirectProjectorAudit.lean"
```

Both build targets and the audit file passed. Lean's `leanchecker` also replayed the declarations of all ten changed modules against their imports and exited successfully. This was a targeted replay of the modified proof. The final `Main` build and independent Comparator verification were outside this replay. To repeat the module checks with bounded memory, run

```sh
git apply --numstat "$PROJECTOR/direct-projector.patch" | cut -f3 |
  sed -e 's|^src/||' -e 's|/|.|g' -e 's|\.lean$||' |
  while IFS= read -r module; do lake env leanchecker -v "$module" || exit 1; done
```

 Every declaration queried with `#print axioms` reported `propext`, `Classical.choice` and `Quot.sound`. The dependency walk confirmed that `levelsExcessDesc` reaches `localStepExcessQ` without `index_last_reduction_holds`. It also confirmed that the legacy row reaches `threeForms_of`, the direct row reaches `gg_len_depth` without `threeForms_of`, and both ON examples reach the direct row without `threeForms_of`. These checks compare named proof dependencies in the submitted namespaces. They do not assert an equivalence between the direct producer and the global remainder contract. The two examples have trivial initial excess.

The additive difference between the two row formulas, with normalized place data, is exactly

    (n/δ − d)u + (r − R_e(Q))/δ.

The audit verifies the identity and its sign under δ > 0, u ≥ 0, δd ≤ n and R_e(Q) ≤ r. A strict saving requires the corresponding term to be positive. The source comparison patch adds 492 lines and removes 139 across ten files, including compatibility wrappers and example proofs.

## Where the two ends still meet the original proof

The arithmetic caller `localIdx` still calls the all-subspace wrapper `levelsQDesc`. `WeightAlgebra.Concl` promises one nonnegative, summable remainder function and a uniform estimate for every admissible cut and every admissible integer depth. `LocalGlobalPassage.l2` uses that contract on a cusp subspace after completion. `l5` uses it across a possibly ramified field extension. `hasIndexBound_of_runs` uses these results to synchronize the two runs. The direct input to `on_core_excess` must be constructed for the same two remainders and both members of each pair before the full chain can dispense with that contract.

For the quaternionic specialization, restricting scalars turns quaternion-linear coset maps into central-ring-linear maps with the identical composites. The four-term arithmetic budget and the construction of the coset maps are still required. The patch extends the source to compare both routes, so its total line count increases.

[Baseline source](https://github.com/Deicyde/riemann-hypothesis/tree/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9) · [Geometric caller](https://github.com/Deicyde/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/JWMggWMem.lean#L123) · [Global remainder contract](https://github.com/Deicyde/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Formalism/SharpRestriction/Divisibility/WeightAlgebra.lean#L424)
