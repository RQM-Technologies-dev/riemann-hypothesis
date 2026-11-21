import Formalism.LocalToGlobal.IndefiniteForms.IndefiniteTree.ExampleSatisfiesConditionsAtFive
import Formalism.SharpRestriction.GenusPolyhedralBounds.RelativeIndexClassSets.LevelsQDesc
import Lean.Util.FoldConsts

open Module
open Formalism.EigenvalueLevelCeiling
namespace DirectProjectorAudit

variable {R : Type*} [CommRing R] {Y Q : Type*} [AddCommGroup Y] [Module R Y] [AddCommGroup Q]
  [Module R Q]

/-- Restricting quaternion-linear maps to the central coefficient ring preserves the estimate. -/
theorem quaternionic_len_depth {ι : Type*} [Fintype ι] [DecidableEq ι]
    [Module (Quaternion R) Y] [Module (Quaternion R) Q]
    [IsScalarTower R (Quaternion R) Y] [IsScalarTower R (Quaternion R) Q]
    (a n : R) (s : ι → Y →ₗ[Quaternion R] Q) (t : ι → Q →ₗ[Quaternion R] Y)
    (hts : ∀ i j y, t i (s j y) = if i = j then n • y else 0) :
    (Fintype.card ι : ℕ∞) * Module.length R
        (LinearMap.range ((a * n) • (LinearMap.id : Y →ₗ[R] Y))) ≤
      Module.length R (LinearMap.range (a • (LinearMap.id : Q →ₗ[R] Q))) :=
  gg_len_depth a n (fun i => (s i).restrictScalars R) (fun i => (t i).restrictScalars R) hts

theorem row_budget (E σ u d δ n r R ε : ℝ)
    (hδ : 0 < δ) (hu : 0 ≤ u) (hd : δ * d ≤ n) (hR : R ≤ r) :
    (E - σ + 2 * u) * d + R / δ + ε ≤
      (E - σ + u) * d + (r + n * u) / δ + ε := by
  field_simp [hδ.ne']
  nlinarith [mul_le_mul_of_nonneg_right hd hu]

theorem row_budget_gap (E σ u d δ n r R ε : ℝ) (hδ : δ ≠ 0) :
    ((E - σ + u) * d + (r + n * u) / δ + ε) -
      ((E - σ + 2 * u) * d + R / δ + ε) =
        (n / δ - d) * u + (r - R) / δ := by
  field_simp [hδ]
  ring

end DirectProjectorAudit

open Formalism.L2.Indef.Tree Formalism.MainNotions.Gaps.T0
#print axioms gg_len_depth
#print axioms lemmaGG_with_depth
#print axioms Formalism.MainNotions.Gaps.EtaleWeightGaps.levelsExcessDesc
#print axioms excess_of_theta_sum
#print axioms localStepExcessQ
#print axioms on_core_excess
#print axioms example_ON
#print axioms example_satisfies_conditions_at_five
#print axioms DirectProjectorAudit.quaternionic_len_depth
#print axioms DirectProjectorAudit.row_budget

open Lean in
private partial def submittedDeps (env : Environment) (todo : List Name) (seen : NameSet) : NameSet := Id.run do
  match todo with
  | [] => return seen
  | n :: rest =>
    if seen.contains n then return submittedDeps env rest seen
    let seen := seen.insert n
    let some ci := env.find? n | return submittedDeps env rest seen
    let deps := ci.getUsedConstantsAsSet.toList.filter fun k =>
      (`Formalism).isPrefixOf k || (`Development).isPrefixOf k || k.toString.startsWith "_private.Formalism."
    return submittedDeps env (deps ++ rest) seen

open Lean in
run_cmd
  let env ← getEnv
  let producer := submittedDeps env [``Formalism.MainNotions.Gaps.EtaleWeightGaps.levelsExcessDesc] {}
  unless producer.contains ``localStepExcessQ do throwError "Direct producer missed the excess bound"
  if producer.contains ``Formalism.IncomingBounds.index_last_reduction_holds then
    throwError "Direct producer still reaches the all-subspace index estimate"
  let detour := ``threeForms_of
  let legacy := submittedDeps env [``on_core] {}
  let direct := submittedDeps env [``on_core_excess] {}
  unless legacy.contains detour do throwError "Legacy positive control did not reach threeForms_of"
  if direct.contains detour then throwError "Direct row still reaches threeForms_of"
  unless direct.contains ``gg_len_depth do throwError "Direct row did not reach the depth lemma"
  for root in [``example_ON, ``example_satisfies_conditions_at_five] do
    let deps := submittedDeps env [root] {}
    unless deps.contains ``on_core_excess do throwError "Example did not use the direct route"
    if deps.contains detour then throwError "Example still reaches threeForms_of"
  logInfo "Both example proofs use the direct row. Only the legacy row reaches threeForms_of."

