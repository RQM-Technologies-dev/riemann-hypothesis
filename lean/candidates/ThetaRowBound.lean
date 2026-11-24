import ThetaFamilyRow
noncomputable section
open NumberField IsDedekindDomain
open Formalism.BasicNotions Formalism.MainNotions Formalism.MainNotions.WeightAlgebra
open Module ScalarPassage Formalism.EigenvalueLevelCeiling Formalism.DivisionValues Formalism.MainNotions.Gaps.LocalGlobalPassage
namespace Formalism.MainNotions.Gaps.EtaleWeightGaps

/-- All rows tied to this family at an admissible depth, with the same base allowance. -/
def FamilyRowBound {D : D7} {B : WeightFamilies.Prov D} {P : ModuliIntegralCharts.Prov D} {j : ℕ}
    (X : PJ D B P j) (S : Scal B) (ka wL wF : WeightFamilies.Wt D j) (T : ℕ)
    (nus allowance : HeightOneSpectrum (𝓞 B.KO) → ℝ) : Prop :=
  ∀ {K : Type} [Field K] [NumberField K] [StarRing K] [StarRing B.KO]
    [Algebra B.KO K] (u : HeightOneSpectrum (𝓞 K)) {m : ℕ}
    (ι : B.Cusp j ka →ₗ[B.KO] (Fin m → K)),
    (∀ t (b : Fin t → B.Cusp j ka), LinearIndependent B.KO b →
      LinearIndependent K fun l => ι (b l)) → Submodule.span K (Set.range ι) = ⊤ →
    Submodule.IsLattice B.KO (B.Mlat j ka) →
    X.Theta S ka wL wF T ≤ X.Msup ka →
    Submodule.span B.KO (X.Thc S.sK ka : Set (B.Cusp j ka)) = ⊤ →
    ∀ (Lθ : Submodule (𝓞 K) (Fin m → K)), IsLatIn (K := K) ⊤ Lθ →
    Lθ = up ι ((X.Theta S ka wL wF T).comap ((X.inc ka).restrictScalars (𝓞 B.KO))) →
    ∀ (a : K), a ≠ 0 → ∀ e : ℕ, (T : ℝ) * nus (u.under (𝓞 B.KO)) ≤ e →
    (u.asIdeal.ramificationIdx (𝓞 B.KO) : ℤ) * e ≤ vw u a →
    (lix u (sc a (up ι (B.Mlat j ka)) ⊔ Lθ) Lθ : ℝ) ≤
      (u.asIdeal.ramificationIdx (𝓞 B.KO) : ℝ) * allowance (u.under (𝓞 B.KO))

theorem rows_of_depth {D : D7} {B : WeightFamilies.Prov D} {P : ModuliIntegralCharts.Prov D} {j : ℕ}
    (X : PJ D B P j) (S : Scal B) (ka wL wF : WeightFamilies.Wt D j) (T : ℕ)
    (nus allowance : HeightOneSpectrum (𝓞 B.KO) → ℝ)
    (hd : ∀ w e, (T : ℝ) * nus w ≤ (e : ℕ) → thetaExcess X S ka wL wF T w e ≠ ⊤ ∧
      ((thetaExcess X S ka wL wF T w e).toNat : ℝ) ≤ allowance w) :
    FamilyRowBound X S ka wL wF T nus allowance := by
  intro K _ _ _ _ _ u m ι hi htop hM hΘ hspan Lθ hL ht a ha e he hval
  exact (rowOfFamily (X := X) S T e _ u ι hi htop hM hΘ hspan Lθ hL ht a ha hval
    (hd _ e he).2).transport.2.2

end Formalism.MainNotions.Gaps.EtaleWeightGaps
