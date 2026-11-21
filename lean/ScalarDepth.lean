import Formalism.MirabolicMackeyTheory.MirabolicMackeyProofs.LocalConditionsWeightedConditional
import Formalism.MirabolicMackeyTheory.MirabolicMackeyProofs.ThreeForms

noncomputable section
open Module NumberField IsDedekindDomain
open Formalism.DivisionValues Formalism.DivisionValues.ValuationRepresentative Formalism.EigenvalueLevelCeiling Formalism.HermitianLatticesTheory
open Formalism.EigenvalueLevelCeiling.ThreeFormsAlt

namespace ScalarPassage

variable {K Z : Type} [Field K] [NumberField K] [StarRing K] [AddCommGroup Z]
  [Module K Z] [Module (𝓞 K) Z] [IsScalarTower (𝓞 K) K Z] [FiniteDimensional K Z]

/-- Increasing the valuation and enlarging the denominator can only decrease excess. -/
theorem depth_mono (w : HeightOneSpectrum (𝓞 K)) (M N T : Submodule (𝓞 K) Z)
    (hM : IsLatIn ⊤ M) (hN : IsLatIn ⊤ N) (hT : IsLatIn ⊤ T) (hle : N ≤ T)
    (b a : K) (hb : b ≠ 0) (ha : a ≠ 0) (hv : vw w b ≤ vw w a) :
    lix w M (M ⊓ sc a⁻¹ T) ≤ lix w M (M ⊓ sc b⁻¹ N) := by
  have hratio : a * b⁻¹ ∈ OO w := by
    apply mem_OO_of_vw_nonneg w (mul_ne_zero ha (inv_ne_zero hb))
    rw [vw_mul w _ _ ha (inv_ne_zero hb), vw_inv]
    omega
  have hloc : localization₂ w.asIdeal (M ⊓ sc b⁻¹ N) ≤ localization₂ w.asIdeal (M ⊓ sc a⁻¹ T) := by
    rw [localization_inf, localization_inf, localization_sc _ (inv_ne_zero hb), localization_sc _ (inv_ne_zero ha)]
    apply inf_le_inf_left
    intro x hx
    have hx' := (mem_sc_inv hb _ x).mp hx
    have hxT := locBasic_locS_mono w.asIdeal.primeCompl hle hx'
    have hu := (mem_sc_inv (mul_ne_zero ha (inv_ne_zero hb)) _ _).mp
      (le_sc_inv w T (mul_ne_zero ha (inv_ne_zero hb)) hratio hxT)
    apply (mem_sc_inv ha _ x).mpr
    simpa [smul_smul, mul_assoc, hb] using hu
  have hB := latInter K Z M N hM hN _ (inv_ne_zero hb)
  have hA := latInter K Z M T hM hT _ (inv_ne_zero ha)
  have h := idxMono K Z w ⊤ M _ (M ⊓ sc a⁻¹ T) hM (idxRules_inf_lat hB hA) hA inf_le_right
  rwa [locP w M _ _ hloc] at h

end ScalarPassage
