import Formalism.SharpRestriction.GenusPolyhedralBounds.RelativeIndexClassSets.ExistsIrreducibleLocToCompl
import Formalism.PeriodIntegrals.UnitaryGroupMassFormula.LatticeIndexDeterminant.NegLogValuation

noncomputable section
open Module NumberField IsDedekindDomain Formalism.DivisionValues
open Formalism.MainNotions.Gaps.EtaleWeightGaps

namespace ScalarPassage

/-- One integral representative works at every depth at the given place. -/
theorem integral_depths {K : Type} [Field K] [NumberField K] [StarRing K]
    (v : HeightOneSpectrum (𝓞 K)) (b : v.adicCompletionIntegers K) (hb : Irreducible b) :
    ∃ π : 𝓞 K, ∀ e : ℕ,
      ((π ^ e : 𝓞 K) : K) ≠ 0 ∧ vw v ((π ^ e : 𝓞 K) : K) = (e : ℤ) ∧
      Associated (b ^ e) (algebraMap (𝓞 K) (v.adicCompletionIntegers K) (π ^ e)) := by
  obtain ⟨π, hπ⟩ := v.intValuation_exists_uniformizer
  have hne : π ≠ 0 := by
    intro h
    rw [h, map_zero] at hπ
    exact WithZero.exp_ne_zero hπ.symm
  have hassoc := IsDiscreteValuationRing.associated_of_irreducible _ hb (irreducible_algebraMap_int K v hπ)
  refine ⟨π, fun e => ?_⟩
  have hn : ((π ^ e : 𝓞 K) : K) ≠ 0 := by exact_mod_cast pow_ne_zero e hne
  refine ⟨hn, ?_, ?_⟩
  swap
  · obtain ⟨u, hu⟩ := hassoc
    refine ⟨u ^ e, ?_⟩
    rw [map_pow, ← hu, mul_pow, Units.val_pow_eq_pow_val]
  change FractionalIdeal.count K v _ = _
  rw [← PI.LatIdxDetW.neg_log_valuation v hn]
  change -WithZero.log (v.valuation K (algebraMap (𝓞 K) K (π ^ e))) = _
  rw [HeightOneSpectrum.valuation_of_algebraMap, map_pow, hπ]
  simp

end ScalarPassage
#print axioms ScalarPassage.integral_depths
