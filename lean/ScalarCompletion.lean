import Formalism.SharpRestriction.GenusPolyhedralBounds.RelativeIndexClassSets.LengthLeOfSemilinear
import Formalism.SharpRestriction.GenusPolyhedralBounds.RelativeIndexClassSets.WeightParameterMemUnitInterval

noncomputable section
open Module NumberField IsDedekindDomain Formalism.HermitianLatticesTheory
open Formalism.MainNotions.Gaps.LocalGlobalPassage
open Formalism.EigenvalueLevelCeiling.ThreeFormsAlt
open Formalism.MainNotions.Gaps.T0 (excess_span_image)

namespace ScalarPassage

section Completion

variable {R K F : Type} [CommRing R] [IsDedekindDomain R] [Field K] [Algebra R K] [IsFractionRing R K]
    [AddCommGroup F] [Module K F] [Module R F] [IsScalarTower R K F] (v : HeightOneSpectrum R)

theorem completed_scalar_sum (M T : Submodule R F) (a : R) :
    locC (K := K) v (M.map (a • LinearMap.id) ⊔ T) =
    (locC (K := K) v M).map ((algebraMap R (v.adicCompletionIntegers K) a) • LinearMap.id) ⊔ locC v T := by
  let j : F →ₛₗ[algebraMap R (v.adicCompletionIntegers K)] TensorProduct K (v.adicCompletion K) F :=
    { toFun := bcC v, map_add' := (bcC (K := K) v).map_add,
      map_smul' := bc_smulR v }
  exact excess_span_image j a M T

/-- A finite completed scalar defect controls the local defect at the same depth. -/
theorem completion_excess (M T : Submodule R F) (a : R) :
    let A := M.map (a • LinearMap.id) ⊔ T
    let C := (locC (K := K) v M).map ((algebraMap R (v.adicCompletionIntegers K) a) • LinearMap.id) ⊔ locC v T
    qlen C (locC v T) ≠ ⊤ →
    qlen (localization₂ v.asIdeal A) (localization₂ v.asIdeal T) ≤ qlen C (locC v T) := by
  intro A C hfin
  have hwhole (L : Submodule R F) : locC (K := K) v L ≤ (locKC v (⊤ : Submodule K F)).restrictScalars (v.adicCompletionIntegers K) := by
    refine Submodule.span_le.mpr ?_
    rintro _ ⟨x, _, rfl⟩
    exact Submodule.subset_span ⟨x, trivial, rfl⟩
  have hC : locC (K := K) v A = C := completed_scalar_sum v M T a
  have h := l1 (K := K) (F := F) v A T ⊤
  rw [inf_eq_left.mpr (hwhole A), inf_eq_left.mpr (hwhole T), hC,
    Submodule.restrictScalars_top, inf_top_eq, inf_eq_right.mpr (show T ≤ A from le_sup_right)] at h
  exact h hfin

end Completion
end ScalarPassage

#print axioms ScalarPassage.completion_excess

open Formalism.EigenvalueLevelCeiling
namespace ScalarPassage

/-- The completed bound is converted to the signed index used by field extension. -/
theorem completion_index {K F : Type} [Field K] [NumberField K] [StarRing K]
    [AddCommGroup F] [Module K F] [Module (𝓞 K) F] [IsScalarTower (𝓞 K) K F]
    (v : HeightOneSpectrum (𝓞 K)) (M N : Submodule (𝓞 K) F) (a : 𝓞 K) (r : ℝ) :
    let C := (locC (K := K) v M).map ((algebraMap (𝓞 K) (v.adicCompletionIntegers K) a) • LinearMap.id) ⊔ locC v N
    qlen C (locC v N) ≠ ⊤ → ((qlen C (locC v N)).toNat : ℝ) ≤ r →
      (lix v (sc (a : K) M ⊔ N) N : ℝ) ≤ r := by
  intro C hfin hr
  have hs : sc (a : K) M = M.map (a • LinearMap.id) := by
    unfold sc
    congr 1
    ext x
    exact algebraMap_smul K a x
  rw [hs]
  unfold lix
  rw [lidx_of_le v.asIdeal (le_sup_right : N ≤ M.map (a • LinearMap.id) ⊔ N)]
  have h := ENat.toNat_le_toNat (completion_excess (K := K) v M N a hfin) hfin
  exact le_trans (by exact_mod_cast h) hr

end ScalarPassage
#print axioms ScalarPassage.completion_index
