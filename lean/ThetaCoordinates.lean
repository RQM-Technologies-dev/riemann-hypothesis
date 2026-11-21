import ScalarAmbient
import ScalarCompletion

noncomputable section
open Module IsDedekindDomain Formalism.EigenvalueLevelCeiling.ThreeFormsAlt
open Formalism.MainNotions.Gaps.LocalGlobalPassage

namespace ScalarPassage

variable {R K F V : Type} [CommRing R] [IsDedekindDomain R] [Field K] [Algebra R K] [IsFractionRing R K]
  [AddCommGroup F] [Module R F] [Module K F] [IsScalarTower R K F]
  [AddCommGroup V] [Module R V] [Module K V] [IsScalarTower R K V]

/-- Completion commutes with the image of a lattice under the cusp inclusion. -/
theorem locC_map (v : HeightOneSpectrum R) (f : F →ₗ[K] V) (M : Submodule R F) :
    (locC (K := K) v M).map ((f.baseChange (v.adicCompletion K)).restrictScalars (v.adicCompletionIntegers K)) =
      locC v (M.map (f.restrictScalars R)) := by
  unfold locC
  rw [Submodule.map_span]
  congr 1
  ext y
  constructor
  · rintro ⟨_, ⟨x, hx, rfl⟩, rfl⟩
    exact ⟨f x, ⟨x, hx, rfl⟩, rfl⟩
  · rintro ⟨_, ⟨x, hx, rfl⟩, rfl⟩
    exact ⟨bcC v x, ⟨x, hx, rfl⟩, rfl⟩

/-- Identify the quotient in the ambient forms with the quotient of the
completed cusp lattices. Theta can be supplied as a sublattice of the image. -/
theorem cusp_length (v : HeightOneSpectrum R) (f : F →ₗ[K] V) (hf : Function.Injective f)
    (M : Submodule R F) (Θ : Submodule R V) (hΘ : Θ ≤ M.map (f.restrictScalars R))
    (a : v.adicCompletionIntegers K) :
    let N := M ⊓ Θ.comap (f.restrictScalars R)
    qlen ((locC (K := K) v (M.map (f.restrictScalars R))).map (a • LinearMap.id) ⊔ locC v Θ) (locC v Θ) =
      qlen ((locC (K := K) v M).map (a • LinearMap.id) ⊔ locC v N) (locC v N) := by
  intro N
  have hN : N.map (f.restrictScalars R) = Θ := by
    apply le_antisymm
    · rintro _ ⟨x, hx, rfl⟩
      exact hx.2
    · intro y hy
      obtain ⟨x, hx, rfl⟩ := hΘ hy
      exact ⟨x, ⟨hx, hy⟩, rfl⟩
  let g := (f.baseChange (v.adicCompletion K)).restrictScalars (v.adicCompletionIntegers K)
  have hg : Function.Injective g := Module.Flat.lTensor_preserves_injective_linearMap f hf
  have h := scalar_length_image g hg (locC (K := K) v M) (locC v N) a
  dsimp only [g] at h
  rwa [locC_map, locC_map, hN] at h


/-- On the full span of the embedded integral forms, the geometric length
equals the completed cusp length at any associated integral scalar. -/
theorem theta_coordinate_length (v : HeightOneSpectrum R) (f : F →ₗ[K] V) (hf : Function.Injective f)
    (M : Submodule R F) (Θ : Submodule R V) (hΘ : Θ ≤ M.map (f.restrictScalars R))
    (b : v.adicCompletionIntegers K) (a : R) (hab : Associated b (algebraMap R (v.adicCompletionIntegers K) a)) :
    let A := M.map (f.restrictScalars R)
    let W := Submodule.span (v.adicCompletion K) (bcC (K := K) v '' (A : Set V))
    let g := W.subtype.restrictScalars (v.adicCompletionIntegers K)
    let N := M ⊓ Θ.comap (f.restrictScalars R)
    qlen (((locC v A).comap g).map (b • LinearMap.id) ⊔ (locC v Θ).comap g) ((locC v Θ).comap g) =
      qlen ((locC (K := K) v M).map ((algebraMap R (v.adicCompletionIntegers K) a) • LinearMap.id) ⊔ locC v N) (locC v N) := by
  intro A W g N
  have hr (L : Submodule R V) (hle : L ≤ A) : locC (K := K) v L ≤ LinearMap.range g := by
    refine Submodule.span_le.mpr ?_
    rintro _ ⟨x, hx, rfl⟩
    exact ⟨⟨_, Submodule.subset_span ⟨x, hle hx, rfl⟩⟩, rfl⟩
  exact (scalar_length_comap g Subtype.val_injective _ _ (hr A le_rfl) (hr Θ hΘ) hab).trans
    (cusp_length v f hf M Θ hΘ _)

end ScalarPassage
#print axioms ScalarPassage.cusp_length

#print axioms ScalarPassage.theta_coordinate_length
