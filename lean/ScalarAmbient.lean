import Formalism.MirabolicMackeyTheory.MirabolicMackeyProofs.ThreeForms
import Formalism.SharpRestriction.GenusPolyhedralBounds.RelativeIndexClassSets.LengthLeOfSemilinear

noncomputable section
open Module Formalism.EigenvalueLevelCeiling Formalism.EigenvalueLevelCeiling.ThreeFormsAlt

namespace ScalarPassage

variable {R V W : Type} [CommRing R] [AddCommGroup V] [AddCommGroup W] [Module R V] [Module R W]

theorem scalar_image (f : V →ₗ[R] W) (M : Submodule R V) (a : R) :
    (M.map (a • LinearMap.id)).map f = (M.map f).map (a • LinearMap.id) := by
  ext x
  constructor
  · rintro ⟨_, ⟨y, hy, rfl⟩, rfl⟩
    exact ⟨f y, ⟨y, hy, rfl⟩, (f.map_smul a y).symm⟩
  · rintro ⟨_, ⟨y, hy, rfl⟩, rfl⟩
    exact ⟨a • y, ⟨y, hy, rfl⟩, f.map_smul a y⟩

theorem scalar_length_image [IsDedekindDomain R] (f : V →ₗ[R] W) (hf : Function.Injective f)
    (M N : Submodule R V) (a : R) :
    qlen ((M.map f).map (a • LinearMap.id) ⊔ N.map f) (N.map f) =
    qlen (M.map (a • LinearMap.id) ⊔ N) N := by
  rw [← scalar_image, ← Submodule.map_sup]
  exact idxRules_len_map f hf _ _

theorem associated_scalar_image {a b : R} (h : Associated a b) (M : Submodule R V) :
    M.map (a • LinearMap.id) = M.map (b • LinearMap.id) := by
  obtain ⟨u, rfl⟩ := h
  ext x
  constructor
  · rintro ⟨y, hy, rfl⟩
    refine ⟨(↑u⁻¹ : R) • y, M.smul_mem _ hy, ?_⟩
    simp [smul_smul, mul_comm, mul_assoc]
  · rintro ⟨y, hy, rfl⟩
    refine ⟨(u : R) • y, M.smul_mem _ hy, ?_⟩
    simp [smul_smul, mul_comm]

/-- Compare a quotient measured in a coordinate subspace with its ambient
completed quotient, allowing an associated choice of uniformizer power. -/
theorem scalar_length_comap [IsDedekindDomain R] (f : V →ₗ[R] W) (hf : Function.Injective f)
    (M N : Submodule R W) (hM : M ≤ LinearMap.range f) (hN : N ≤ LinearMap.range f)
    {a b : R} (hab : Associated a b) :
    qlen ((M.comap f).map (a • LinearMap.id) ⊔ N.comap f) (N.comap f) =
    qlen (M.map (b • LinearMap.id) ⊔ N) N := by
  rw [← scalar_length_image f hf (M.comap f) (N.comap f) a,
    Submodule.map_comap_eq, Submodule.map_comap_eq,
    inf_eq_right.mpr hM, inf_eq_right.mpr hN, associated_scalar_image hab]

end ScalarPassage
#print axioms ScalarPassage.scalar_length_comap
