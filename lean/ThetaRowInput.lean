import ThetaCoordinates
import ThetaDepth
import ScalarPassage

noncomputable section
open Module NumberField IsDedekindDomain Formalism.DivisionValues Formalism.EigenvalueLevelCeiling
open Formalism.MainNotions.Gaps.LocalGlobalPassage Formalism.EigenvalueLevelCeiling.ThreeFormsAlt

namespace ScalarPassage

/-- The preimage that occurs in the row tie already lies in the ambient lattice. -/
theorem preimage_le_of_theta_image {R F V : Type*} [CommRing R] [AddCommGroup F] [Module R F]
    [AddCommGroup V] [Module R V] (f : F →ₗ[R] V) (hf : Function.Injective f)
    (M : Submodule R F) (Θ : Submodule R V) (hΘ : Θ ≤ M.map f) : Θ.comap f ≤ M := by
  intro x hx
  obtain ⟨y, hy, hxy⟩ := hΘ hx
  exact hf hxy ▸ hy

/-- Feed the length in theta coordinates at depth e to the row constructor
using a base integral representative of exactly that depth. -/
theorem row_of_theta_length {K0 K F V : Type} [Field K0] [NumberField K0] [StarRing K0]
    [Field K] [NumberField K] [StarRing K] [Algebra K0 K] [AddCommGroup F] [Module K0 F]
    [Module (𝓞 K0) F] [IsScalarTower (𝓞 K0) K0 F] [FiniteDimensional K0 F]
    [AddCommGroup V] [Module K0 V] [Module (𝓞 K0) V] [IsScalarTower (𝓞 K0) K0 V]
    {n : ℕ} (ι : F →ₗ[K0] (Fin n → K))
    (hind : ∀ (m : ℕ) (b : Fin m → F), LinearIndependent K0 b → LinearIndependent K fun i => ι (b i))
    (htop : Submodule.span K (Set.range ι) = ⊤) (f : F →ₗ[K0] V) (hf : Function.Injective f)
    (M : Submodule (𝓞 K0) F) (Θ : Submodule (𝓞 K0) V) (hΘ : Θ ≤ M.map (f.restrictScalars (𝓞 K0)))
    (hM : IsLatIn ⊤ M) (hN : IsLatIn ⊤ (M ⊓ Θ.comap (f.restrictScalars (𝓞 K0))))
    (T : Submodule (𝓞 K) (Fin n → K)) (hT : IsLatIn ⊤ T)
    (hNT : up ι (M ⊓ Θ.comap (f.restrictScalars (𝓞 K0))) ≤ T) (hTM : T ≤ up ι M)
    (v : HeightOneSpectrum (𝓞 K)) (e : ℕ) (a : K) (ha : a ≠ 0)
    (hdepth : (v.asIdeal.ramificationIdx (𝓞 K0) : ℤ) * e ≤ vw v a) (r : ℝ) :
    let w := v.under (𝓞 K0)
    ∀ b : w.adicCompletionIntegers K0, Irreducible b →
    let A := M.map (f.restrictScalars (𝓞 K0))
    let W := Submodule.span (w.adicCompletion K0) (bcC (K := K0) w '' (A : Set V))
    let g := W.subtype.restrictScalars (w.adicCompletionIntegers K0)
    let d := qlen (((locC w A).comap g).map ((b ^ e) • LinearMap.id) ⊔ (locC w Θ).comap g) ((locC w Θ).comap g)
    d ≠ ⊤ ∧ (d.toNat : ℝ) ≤ r → CompletedRow K0 v (up ι M) T a r := by
  intro w b hb A W g d hd
  obtain ⟨π, hπ⟩ := integral_depths w b hb
  obtain ⟨hne, hv, hassoc⟩ := hπ e
  refine CompletedRow.fromLattices ι hind htop M _ hM hN inf_le_left rfl hNT hT hTM
    (π ^ e) hne (hv ▸ Int.natCast_nonneg e) ha (by rw [hv]; exact hdepth) ?_
  have heq := theta_coordinate_length w f hf M Θ hΘ (b ^ e) (π ^ e) hassoc
  change d = _ at heq
  rw [heq] at hd
  exact hd

end ScalarPassage
#print axioms ScalarPassage.row_of_theta_length
