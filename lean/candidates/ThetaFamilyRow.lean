import ThetaFamilyProducer
import ThetaRowInput

set_option maxHeartbeats 200000
noncomputable section
open Formalism.MainNotions.WeightAlgebra Formalism.BasicNotions NumberField IsDedekindDomain Module
namespace Formalism.MainNotions.Gaps.EtaleWeightGaps
variable {D : D7} {B : WeightFamilies.Prov D} {P : ModuliIntegralCharts.Prov D}

open ScalarPassage Formalism.EigenvalueLevelCeiling Formalism.DivisionValues
open Formalism.MainNotions.Gaps.LocalGlobalPassage

section
variable {j : ℕ} (X : PJ D B P j) (S : Scal B) (ka wL wF : WeightFamilies.Wt D j) (T : ℕ)

private abbrev thetaPre :=
  (X.Theta S ka wL wF T).comap ((X.inc ka).restrictScalars (𝓞 B.KO))

private theorem thetaPre_le (hΘ : X.Theta S ka wL wF T ≤ X.Msup ka) :
    thetaPre X S ka wL wF T ≤ B.Mlat j ka :=
  preimage_le_of_theta_image ((X.inc ka).restrictScalars (𝓞 B.KO)) (X.inc_inj ka)
    (B.Mlat j ka) (X.Theta S ka wL wF T) hΘ

private theorem infTheta_lattice (hM : Submodule.IsLattice B.KO (B.Mlat j ka))
    (hΘ : X.Theta S ka wL wF T ≤ X.Msup ka)
    (hspan : Submodule.span B.KO (X.Thc S.sK ka : Set (B.Cusp j ka)) = ⊤) :
    IsLatIn (K := B.KO) ⊤ (B.Mlat j ka ⊓ thetaPre X S ka wL wF T) := by
  refine ⟨hM.fg.of_le inf_le_left, top_unique ?_⟩
  rw [← hspan]
  apply Submodule.span_mono
  intro x hx
  have hinc : X.emb ka (X.Thc S.sK ka) ≤ X.Theta S ka wL wF T := le_sup_right
  have ht : x ∈ thetaPre X S ka wL wF T := hinc ⟨x, hx, rfl⟩
  exact ⟨thetaPre_le X S ka wL wF T hΘ ht, ht⟩
end

private theorem up_mono {K₀ K F : Type} [Field K₀] [NumberField K₀] [Field K] [NumberField K]
    [Algebra K₀ K] [AddCommGroup F] [Module K₀ F] [Module (𝓞 K₀) F] {n : ℕ}
    (ι : F →ₗ[K₀] (Fin n → K)) {M N : Submodule (𝓞 K₀) F} (h : M ≤ N) :
    up ι M ≤ up ι N := Submodule.span_mono (Set.image_mono h)

/-- The two coordinate presentations compute definitionally equal lengths. Build
`Eq.refl` on the displayed left side and let the kernel check conversion. -/
private theorem theta_coordinate_excess {j : ℕ} (X : PJ D B P j) (S : Scal B) (ka wL wF : WeightFamilies.Wt D j)
    (T : ℕ) (w : HeightOneSpectrum (𝓞 B.KO)) (e : ℕ) :
    let A := (B.Mlat j ka).map ((X.inc ka).restrictScalars (𝓞 B.KO))
    let W := Submodule.span (w.adicCompletion B.KO) (bcC (K := B.KO) w '' (A : Set X.Forms))
    let g := W.subtype.restrictScalars (w.adicCompletionIntegers B.KO)
    let M := (locC (K := B.KO) w A).comap g
    let Θ := (locC (K := B.KO) w (X.Theta S ka wL wF T)).comap g
    Formalism.EigenvalueLevelCeiling.ThreeFormsAlt.qlen (M.map ((unif X w ^ e) • LinearMap.id) ⊔ Θ) Θ =
      thetaExcess X S ka wL wF T w e := by
  intro A W g M N
  run_tac Lean.Elab.Tactic.withMainContext do
    let some (_, lhs, _) := (← Lean.Elab.Tactic.getMainTarget).eq? | throwError "expected equality"
    (← Lean.Elab.Tactic.getMainGoal).assign (← Lean.Meta.mkEqRefl lhs)

/-- Use the scalar bound on the original model, allowing the allowance to come
from points on a norm-adjusted model with the same scalar length. -/
theorem rowOfFamily {j : ℕ} {X : PJ D B P j} {ka wL wF : WeightFamilies.Wt D j}
    (S : Scal B) (T e : ℕ) (r : ℝ)
    {K : Type} [Field K] [NumberField K] [StarRing K] [StarRing B.KO] [Algebra B.KO K]
    (v : HeightOneSpectrum (𝓞 K)) {n : ℕ}
    (ι : B.Cusp j ka →ₗ[B.KO] (Fin n → K))
    (hind : ∀ (m : ℕ) (b : Fin m → B.Cusp j ka), LinearIndependent B.KO b → LinearIndependent K fun i => ι (b i))
    (htop : Submodule.span K (Set.range ι) = ⊤)
    (hM : Submodule.IsLattice B.KO (B.Mlat j ka)) (hΘ : X.Theta S ka wL wF T ≤ X.Msup ka)
    (hspan : Submodule.span B.KO (X.Thc S.sK ka : Set (B.Cusp j ka)) = ⊤)
    (L : Submodule (𝓞 K) (Fin n → K)) (hL : IsLatIn ⊤ L)
    (htie : L = up ι ((X.Theta S ka wL wF T).comap ((X.inc ka).restrictScalars (𝓞 B.KO))))
    (a : K) (ha : a ≠ 0)
    (hdepth : (v.asIdeal.ramificationIdx (𝓞 B.KO) : ℤ) * e ≤ vw v a)
    (hbound : ((thetaExcess X S ka wL wF T (v.under (𝓞 B.KO)) e).toNat : ℝ) ≤ r) :
    CompletedRow B.KO v (up ι (B.Mlat j ka)) L a r := by
  let w := v.under (𝓞 B.KO)
  let M := B.Mlat j ka
  let Θ := X.Theta S ka wL wF T
  let pre := thetaPre X S ka wL wF T
  have hm : IsLatIn (K := B.KO) ⊤ M := ⟨hM.fg, hM.span_eq_top⟩
  have hn : IsLatIn (K := B.KO) ⊤ (M ⊓ pre) := infTheta_lattice X S ka wL wF T hM hΘ hspan
  have hnt : up ι (M ⊓ pre) ≤ L := htie.symm ▸ up_mono ι (show M ⊓ pre ≤ pre from inf_le_right)
  have htm : L ≤ up ι M := htie.symm ▸ up_mono ι (thetaPre_le X S ka wL wF T hΘ)
  let b := unif X w
  have hb : Irreducible b := unif_irreducible X w
  have hfin := thetaExcess_finite X S ka wL wF T w e hM hΘ hspan
  have stage := row_of_theta_length (K0 := B.KO) (K := K) (F := B.Cusp j ka) (V := X.Forms) (n := n)
    ι hind htop (X.inc ka) (X.inc_inj ka) M Θ hΘ hm hn L hL hnt htm v e a ha hdepth r b hb
  apply stage
  rw [theta_coordinate_excess X S ka wL wF T w e]
  exact ⟨hfin, hbound⟩

end Formalism.MainNotions.Gaps.EtaleWeightGaps
#print axioms Formalism.MainNotions.Gaps.EtaleWeightGaps.rowOfFamily
