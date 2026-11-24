import Formalism.LocalToGlobal.IndefiniteForms.IndefiniteTree.ExampleSatisfiesConditionsAtFive
import Formalism.MirabolicMackeyTheory.MirabolicMackeyProofs.ThreeForms

noncomputable section
open Module NumberField IsDedekindDomain
open Formalism.DivisionValues Formalism.EigenvalueLevelCeiling Formalism.L2.Indef
namespace Formalism.L2.Indef.Tree

variable {K : Type} [Field K] [NumberField K] [StarRing K] {Bs : DefBase K}
  {Df : DefSide Bs} {S : IndefData Df} {P : Type} [Group P] [Finite P] {c : OnConst}

/-- Convert the paired output of the arithmetic runs in place. The place selector,
both weighted budgets, the depth and the original row object stay fixed. -/
theorem depth_of_run_bounds (O : OnObj S P c) (sup : LeafSup O) (stable : LeafLemmaS O)
    (bounds : LatticeIndexBoundAtPairs O) : LatticeIndexBoundAtPairs O true := by
  refine ⟨?_, bounds.2⟩
  have one (v : HeightOneSpectrum (𝓞 K)) (j : Bs.J)
      (hM : IsLatIn ⊤ (O.Th1 v j)) (hT : O.Th1 v j ≤ O.Th v j)
      (hA : O.a v j ≠ 0) (hv : vw v (O.a v j) = (O.E v j : ℤ))
      (hcut : ∀ W : Submodule K (Fin (O.nZ j) → K),
        (lix v (cut W (O.Ms j)) (cut W (O.Th1 v j)) : ℝ) ≤
          (O.E v j : ℝ) * (finrank K W : ℝ) + O.r v j)
      (hsub : O.Th v j ≤ O.Ms j) :
      (lix v (sc (O.a v j) (O.Ms j) ⊔ O.Th1 v j) (O.Th1 v j) : ℝ) ≤ O.r v j := by
    have inc := hT.trans hsub
    rw [three_forms_sum K _ v _ _ (sup j).1 hM inc _ hA (hv ▸ Int.natCast_nonneg _)]
    exact (three_forms K _ v _ _ (sup j).1 hM inc _ _ _ hA hv).mp hcut
  intro w hw
  constructor <;> intro j
  · obtain ⟨hm, ht, ha, hv, hc⟩ := (bounds.1 w hw).1 j
    exact ⟨hm, ht, ha, hv, one _ _ hm ht ha hv hc ((stable w hw).1 j).1⟩
  · obtain ⟨hm, ht, ha, hv, hc⟩ := (bounds.1 w hw).2 j
    exact ⟨hm, ht, ha, hv, one _ _ hm ht ha hv hc ((stable w hw).2 j).1⟩

end Formalism.L2.Indef.Tree
end
