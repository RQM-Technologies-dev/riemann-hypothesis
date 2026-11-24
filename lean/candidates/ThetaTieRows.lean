import ThetaRunRows
import ThetaTieParameters
import Development.AbelianVarietyTheory.Proofs.DivisorProofs.HasIndexBoundOfRuns
set_option autoImplicit false

noncomputable section

open NumberField IsDedekindDomain Module
open Formalism.BasicNotions Formalism.MainNotions Formalism.MainNotions.DIV.Cons Formalism.L2.Pj Formalism.DivisionValues Formalism.EigenvalueLevelCeiling Formalism.L2.DIV Formalism.L2.Indef Formalism.L2.Indef.Tree Formalism.IndefR Formalism.IndefR.Links
open Formalism.IndefR.Cx Formalism.IndefR.FWT Formalism.BasicNotions.TH Formalism.MainNotions.GlobalTheoryTheory.GenusMassVolumes Formalism.L2.Theta
open GlobalTheory.OntoChain GlobalTheory.RealIndexBound GlobalTheory.OnTies GlobalTheory.FormTies GlobalTheory.BigOn
attribute [local instance] Formalism.BasicNotions.Host.cmStar
open scoped TensorProduct

open Formalism.MainNotions.WeightAlgebra Formalism.MainNotions.Gaps.EtaleWeightGaps
namespace GlobalTheory.BigOn

private theorem row_at_tie {D : D7} {B : WeightFamilies.Prov D} {P6 : ModuliIntegralCharts.Prov D}
    {j : ℕ} (X : PJ D B P6 j) (hinj : Function.Injective D.what₂.OtoLL) (EX : ErrX D) (p : ℕ)
    (ka wL wF : WeightFamilies.Wt D j) (T : ℕ) (nus base : HeightOneSpectrum (𝓞 B.KO) → ℝ)
    {K : Type} [Field K] [NumberField K] [StarRing K] [StarRing B.KO] [Algebra B.KO K]
    {Bs : DefBase K} {Df : DefSide Bs} {S : IndefData Df} {U : Type} [Group U] [Finite U] {oc : OnConst}
    {O : OnObj S U oc} {v : HeightOneSpectrum (𝓞 K)} {i : Bs.J}
    {z : (Fin (O.nZ i) → K) ≃ₗ[K] K ⊗[B.KO] B.Cusp j ka} {act : U → B.Cusp j ka → B.Cusp j ka}
    (tie : FormTieK X hinj EX p ka wL wF T O v i z act)
    (rows : FamilyRowBound X (scalOfP B hinj EX p ka wL wF T) ka wL wF T nus base)
    (hM : Submodule.IsLattice B.KO (B.Mlat j ka))
    (hΘ : X.Theta (scalOfP B hinj EX p ka wL wF T) ka wL wF T ≤ X.Msup ka)
    (hspan : Submodule.span B.KO (X.Thc (scalOfP B hinj EX p ka wL wF T).sK ka : Set (B.Cusp j ka)) = ⊤)
    (hL : IsLatIn (K := K) ⊤ (O.Th v i)) (a : K) (ha : a ≠ 0) (e : ℕ)
    (he : (T : ℝ) * nus (v.under (𝓞 B.KO)) ≤ e)
    (hval : (v.asIdeal.ramificationIdx (𝓞 B.KO) : ℤ) * e ≤ vw v a) :
    (lix v (sc a (O.Ms i) ⊔ O.Th v i) (O.Th v i) : ℝ) ≤
      (v.asIdeal.ramificationIdx (𝓞 B.KO) : ℝ) * base (v.under (𝓞 B.KO)) := by
  rw [tie.Ms_eq]
  exact rows v (coordMap z) (coordMap_linearIndependent z) (coordMap_span z) hM hΘ hspan
    _ hL tie.Th_eq a ha e he hval

private theorem rank_of_row {D : D7} {B : WeightFamilies.Prov D} {P : ModuliIntegralCharts.Prov D}
    {j : ℕ} (X : PJ D B P j) (ka : WeightFamilies.Wt D j) {K : Type} [Field K] [NumberField K] [Algebra B.KO K]
    {n : ℕ} (z : (Fin n → K) ≃ₗ[K] K ⊗[B.KO] B.Cusp j ka) (L : Submodule (𝓞 K) (Fin n → K))
    (ht : L = spanK z (B.Mlat j ka : Set (B.Cusp j ka))) (hL : IsLatIn (K := K) ⊤ L) :
    Submodule.IsLattice B.KO (B.Mlat j ka) ∧ X.rk ka (B.Mlat j ka) = n := by
  subst L
  have hm := isLattice_of_spanK z (B.Mlat j ka) hL
  refine ⟨hm, ?_⟩
  unfold PJ.rk
  rw [hm.span_eq_top, finrank_top]
  have hz := z.finrank_eq
  rw [Module.finrank_baseChange, Module.finrank_fin_fun] at hz
  exact hz.symm

theorem rem_of_rows {D : D7} {B : WeightFamilies.Prov D} {P6 : ModuliIntegralCharts.Prov D}
    {j : ℕ} {X : PJ D B P6 j} {hinj : Function.Injective D.what₂.OtoLL} {EX : ErrX D} {p : ℕ}
    {ka wL wF : WeightFamilies.Wt D j} {T : ℕ} {nus : HeightOneSpectrum (𝓞 B.KO) → ℝ} {b₁ b₂ b₃ b₄ : ℝ}
    {K : Type} [Field K] [NumberField K] [StarRing K] [Algebra B.KO K]
    {Bs : DefBase K} {Df : DefSide Bs} {S : IndefData Df} {U : Type} [Group U] [Finite U] {oc : OnConst}
    {O : OnObj S U oc} {v₁ : HeightOneSpectrum (𝓞 K)} {i : Bs.J}
    {z : (Fin (O.nZ i) → K) ≃ₗ[K] K ⊗[B.KO] B.Cusp j ka} {act : U → B.Cusp j ka → B.Cusp j ka}
    (ht : FormTieK X hinj EX p ka wL wF T O v₁ i z act) (hS : IsLatIn (K := K) ⊤ (O.Ms i))
    [StarRing B.KO] (base : HeightOneSpectrum (𝓞 B.KO) → ℝ) (h0 : ∀ w, 0 ≤ base w)
    (hs : Summable (fun w => base w * X.lN w))
    (hb : ∑' w, base w * X.lN w ≤ X.rk ka (B.Mlat j ka) * b₁ * b₂ * b₃ * b₄)
    (rows : FamilyRowBound X (scalOfP B hinj EX p ka wL wF T) ka wL wF T nus base)
    (hΘ : X.Theta (scalOfP B hinj EX p ka wL wF T) ka wL wF T ≤ X.Msup ka)
    (hspan : Submodule.span B.KO (X.Thc (scalOfP B hinj EX p ka wL wF T).sK ka : Set (B.Cusp j ka)) = ⊤) :
    let ρ := fun (v : HeightOneSpectrum (𝓞 K)) => (v.asIdeal.ramificationIdx (𝓞 B.KO) : ℝ) * base (v.under (𝓞 B.KO))
    (∀ v, 0 ≤ ρ v) ∧ (∀ places : Finset _, ∑ v ∈ places, Formalism.DivisionValues.lw v * ρ v ≤
      (O.nZ i : ℝ) * (b₁ * b₂ * b₃ * b₄)) ∧
    ∀ v, FormTieK X hinj EX p ka wL wF T O v i z act → IsLatIn (K := K) ⊤ (O.Th v i) →
      ∀ a : K, a ≠ 0 → ∀ e : ℕ, (T : ℝ) * nus (v.under (𝓞 B.KO)) ≤ e →
      (v.asIdeal.ramificationIdx (𝓞 B.KO) : ℤ) * e ≤ vw v a →
      (lix v (sc a (O.Ms i) ⊔ O.Th v i) (O.Th v i) : ℝ) ≤ ρ v := by
  obtain ⟨hM, hrank⟩ := rank_of_row X ka z (O.Ms i) ht.Ms_eq hS
  refine ⟨fun _ => mul_nonneg (Nat.cast_nonneg _) (h0 _), ?_, ?_⟩
  · intro places
    apply (Formalism.MainNotions.Gaps.LocalGlobalPassage.l4 base h0 hs places).trans
    apply hb.trans
    rw [hrank]
    exact le_of_eq (by ring)
  · intro v tie hL a ha e he hval
    exact row_at_tie X hinj EX p ka wL wF T nus base tie rows hM hΘ hspan hL a ha e he hval

end GlobalTheory.BigOn
end
#print axioms GlobalTheory.BigOn.rem_of_rows
