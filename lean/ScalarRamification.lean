import ScalarDepth
import Formalism.SharpRestriction.GenusPolyhedralBounds.RelativeIndexClassSets.WeightParameterMemUnitInterval

noncomputable section
open Module NumberField IsDedekindDomain Formalism.HermitianLatticesTheory
open Formalism.MainNotions.Gaps.LocalGlobalPassage Formalism.DivisionValues Formalism.EigenvalueLevelCeiling
open Formalism.EigenvalueLevelCeiling.ThreeFormsAlt

namespace ScalarPassage

variable {K0 K : Type} [Field K0] [NumberField K0] [StarRing K0] [Field K] [NumberField K] [StarRing K] [Algebra K0 K]
  {Z : Type} [AddCommGroup Z] [Module K0 Z] [FiniteDimensional K0 Z] [Module (𝓞 K0) Z] [IsScalarTower (𝓞 K0) K0 Z] {n : ℕ}

/-- Pass the original scalar through ramification, a later depth, and a larger theta lattice. -/
theorem ramified_excess (ι : Z →ₗ[K0] (Fin n → K))
    (hind : ∀ (m : ℕ) (b : Fin m → Z), LinearIndependent K0 b → LinearIndependent K fun i => ι (b i))
    (htop : Submodule.span K (Set.range ι) = ⊤) (M N : Submodule (𝓞 K0) Z)
    (hM : IsLatIn ⊤ M) (hN : IsLatIn ⊤ N) (hle : N ≤ M)
    (v : HeightOneSpectrum (𝓞 K)) (a0 : K0) (ha0 : a0 ≠ 0)
    (hv0 : 0 ≤ vw (v.under (𝓞 K0)) a0)
    (T : Submodule (𝓞 K) (Fin n → K)) (hT : IsLatIn ⊤ T) (hNT : up ι N ≤ T) (hTM : T ≤ up ι M)
    (a : K) (ha : a ≠ 0)
    (hdepth : (v.asIdeal.ramificationIdx (𝓞 K0) : ℤ) * vw (v.under (𝓞 K0)) a0 ≤ vw v a)
    (r : ℝ) (h : (lix (v.under (𝓞 K0)) (sc a0 M ⊔ N) N : ℝ) ≤ r) :
    (lix v (sc a (up ι M) ⊔ T) T : ℝ) ≤ (v.asIdeal.ramificationIdx (𝓞 K0) : ℝ) * r := by
  let b := algebraMap K0 K a0
  have hb : b ≠ 0 := by dsimp [b]; simpa using ha0
  have hvb : vw v b = (v.asIdeal.ramificationIdx (𝓞 K0) : ℤ) * vw (v.under (𝓞 K0)) a0 := l3a v a0 ha0
  let C := M ⊓ sc a0⁻¹ N
  have hC := latInter K0 Z M N hM hN a0⁻¹ (inv_ne_zero ha0)
  have hML : IsLatIn ⊤ (up ι M) := ⟨up_fg ι hM.1, up_top ι htop hM.2⟩
  have hNL : IsLatIn ⊤ (up ι N) := ⟨up_fg ι hN.1, up_top ι htop hN.2⟩
  have hCL : IsLatIn ⊤ (up ι C) := ⟨up_fg ι hC.1, up_top ι htop hC.2⟩
  have hc : up ι C ≤ up ι M ⊓ sc b⁻¹ (up ι N) := by
    refine le_inf (up_mono ι inf_le_left) (Submodule.span_le.mpr ?_)
    rintro _ ⟨x, hx, rfl⟩
    apply (mem_sc_inv hb _ _).mpr
    change algebraMap K0 K a0 • ι x ∈ up ι N
    rw [algebraMap_smul, ← map_smul]
    exact Submodule.subset_span ⟨_, (mem_sc_inv ha0 _ x).mp hx.2, rfl⟩
  have hidx := idxMono K _ v ⊤ (up ι M) (up ι C) _ hML hCL
    (latInter K _ _ _ hML hNL b⁻¹ (inv_ne_zero hb)) hc
  have hmono := depth_mono v (up ι M) (up ι N) T hML hNL hT hNT b a hb ha (by rw [hvb]; exact hdepth)
  have hl := l3 l3a ι hind htop M C hM.1 hM.2 hC.1 hC.2 v
  change lix v (up ι M) (up ι C) = _ at hl
  rw [three_forms_sum K0 _ _ M N hM hN hle a0 ha0 hv0] at h
  rw [three_forms_sum K _ v _ T hML hT hTM a ha ((mul_nonneg (Int.natCast_nonneg _) hv0).trans hdepth)]
  have hi := hmono.trans hidx
  rw [hl] at hi
  exact (by exact_mod_cast hi : (lix v (up ι M) (up ι M ⊓ sc a⁻¹ T) : ℝ) ≤
    (v.asIdeal.ramificationIdx (𝓞 K0) : ℝ) * (lix (v.under (𝓞 K0)) M C : ℝ)).trans
    (mul_le_mul_of_nonneg_left h (Nat.cast_nonneg _))

end ScalarPassage

open Module NumberField IsDedekindDomain
open Formalism.DivisionValues Formalism.EigenvalueLevelCeiling Formalism.L2.Indef Formalism.L2.Indef.Tree
open Formalism.MainNotions.Gaps.LocalGlobalPassage

namespace ScalarPassage

variable {K0 K : Type} [Field K0] [NumberField K0] [Field K] [NumberField K] [StarRing K] [Algebra K0 K]
  {Bs : DefBase K} {Df : DefSide Bs} {S : IndefData Df} {P : Type} [Group P] [Finite P] {c : OnConst}

/-- Assemble two given base remainders using the actual row selector and budget. -/
theorem paired_scalar (O : OnObj S P c)
    (r : Bool → Bs.J → HeightOneSpectrum (𝓞 K0) → ℝ)
    (hn : ∀ k j v, 0 ≤ r k j v)
    (hs : ∀ k j, Summable (fun v => r k j v * Formalism.BasicNotions.lw K0 v))
    (hb : ∀ k j, ∑' v, r k j v * Formalism.BasicNotions.lw K0 v ≤
      (O.nZ j : ℝ) * (O.f * O.m * O.b * O.de2))
    (hr : ∀ k v j, (if k = true then O.r2 v j else O.r1 v j) =
      (v.asIdeal.ramificationIdx (𝓞 K0) : ℝ) * r k j (v.under (𝓞 K0)))
    (hd : 0 ≤ O.de2 ∧ O.de2 ≤ 1)
    (hl : AtPair S fun v => ∀ j, IsLatIn ⊤ (O.Th1 v j) ∧ O.Th1 v j ≤ O.Th v j ∧
      O.a v j ≠ 0 ∧ vw v (O.a v j) = (O.E v j : ℤ) ∧
      (lix v (sc (O.a v j) (O.Ms j) ⊔ O.Th1 v j) (O.Th1 v j) : ℝ) ≤
        (v.asIdeal.ramificationIdx (𝓞 K0) : ℝ) * r (decide (plc v = O.pde)) j (v.under (𝓞 K0))) :
    LatticeIndexBoundAtPairs O true := by
  have hlocal (v : HeightOneSpectrum (𝓞 K)) (j : Bs.J) :
      O.r v j = (v.asIdeal.ramificationIdx (𝓞 K0) : ℝ) * r (decide (plc v = O.pde)) j (v.under (𝓞 K0)) := by
    simpa [OnObj.r] using hr (decide (plc v = O.pde)) v j
  have hsum (k : Bool) (j : Bs.J) (S' : Finset (HeightOneSpectrum (𝓞 K))) :=
    (l4 (K := K) (r k j) (hn k j) (hs k j) S').trans (hb k j)
  refine ⟨fun w hw => ?_, hd.1, hd.2, fun v j => ?_, fun j S' => ?_⟩
  · obtain ⟨h, h'⟩ := hl w hw
    simpa only [if_true, hlocal] using And.intro h h'
  · constructor
    · simpa using (hr false v j ▸ mul_nonneg (Nat.cast_nonneg _) (hn false j (v.under (𝓞 K0))) :
        0 ≤ (if false = true then O.r2 v j else O.r1 v j))
    · simpa using (hr true v j ▸ mul_nonneg (Nat.cast_nonneg _) (hn true j (v.under (𝓞 K0))) :
        0 ≤ (if true = true then O.r2 v j else O.r1 v j))
  · have h1 (v) : O.r1 v j = _ := hr false v j
    have h2 (v) : O.r2 v j = _ := hr true v j
    constructor
    · simp_rw [h1]
      exact hsum false j S'
    · simp_rw [h2]
      exact hsum true j S'

end ScalarPassage

#print axioms ScalarPassage.ramified_excess
#print axioms ScalarPassage.paired_scalar
