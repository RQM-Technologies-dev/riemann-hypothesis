import ScalarCompletion
import ScalarRamification

noncomputable section
open Module NumberField IsDedekindDomain Formalism.HermitianLatticesTheory
open Formalism.MainNotions.Gaps.LocalGlobalPassage Formalism.DivisionValues Formalism.EigenvalueLevelCeiling
open Formalism.EigenvalueLevelCeiling.ThreeFormsAlt

namespace ScalarPassage

variable {K0 K : Type} [Field K0] [NumberField K0] [StarRing K0] [Field K] [NumberField K] [StarRing K] [Algebra K0 K]
  {Z : Type} [AddCommGroup Z] [Module K0 Z] [FiniteDimensional K0 Z] [Module (𝓞 K0) Z] [IsScalarTower (𝓞 K0) K0 Z] {n : ℕ}

/-- Carry a single completed remainder to a ramified row lattice. -/
theorem completed_to_ramified (ι : Z →ₗ[K0] (Fin n → K))
    (hind : ∀ (m : ℕ) (b : Fin m → Z), LinearIndependent K0 b → LinearIndependent K fun i => ι (b i))
    (htop : Submodule.span K (Set.range ι) = ⊤) (M N : Submodule (𝓞 K0) Z)
    (hM : IsLatIn ⊤ M) (hN : IsLatIn ⊤ N) (hle : N ≤ M)
    (v : HeightOneSpectrum (𝓞 K)) (a0 : 𝓞 K0) (ha0 : (a0 : K0) ≠ 0)
    (hv0 : 0 ≤ vw (v.under (𝓞 K0)) a0)
    (T : Submodule (𝓞 K) (Fin n → K)) (hT : IsLatIn ⊤ T) (hNT : up ι N ≤ T) (hTM : T ≤ up ι M)
    (a : K) (ha : a ≠ 0)
    (hdepth : (v.asIdeal.ramificationIdx (𝓞 K0) : ℤ) * vw (v.under (𝓞 K0)) a0 ≤ vw v a)
    (r : ℝ) :
    let w := v.under (𝓞 K0)
    let C := (locC (K := K0) w M).map ((algebraMap (𝓞 K0) (w.adicCompletionIntegers K0) a0) • LinearMap.id) ⊔ locC w N
    qlen C (locC w N) ≠ ⊤ → ((qlen C (locC w N)).toNat : ℝ) ≤ r →
      (lix v (sc a (up ι M) ⊔ T) T : ℝ) ≤ (v.asIdeal.ramificationIdx (𝓞 K0) : ℝ) * r := by
  intro w C hfin hr
  exact ramified_excess ι hind htop M N hM hN hle v (a0 : K0) ha0 hv0 T hT hNT hTM
    a ha hdepth r (completion_index w M N a0 r hfin hr)

open Formalism.L2.Indef Formalism.L2.Indef.Tree

/-- A completed source lattice for one actual row. The remainder is an index of
the type, so a proof for a different placewise function cannot be substituted. -/
inductive CompletedRow (K0 : Type) [Field K0] [NumberField K0] [StarRing K0]
    {K : Type} [Field K] [NumberField K] [StarRing K] [Algebra K0 K] {n : ℕ}
    (v : HeightOneSpectrum (𝓞 K)) (A T : Submodule (𝓞 K) (Fin n → K)) (a : K) (r : ℝ) : Prop where
  | fromLattices {Z : Type} [AddCommGroup Z] [Module K0 Z] [FiniteDimensional K0 Z]
      [Module (𝓞 K0) Z] [IsScalarTower (𝓞 K0) K0 Z]
      (ι : Z →ₗ[K0] (Fin n → K))
      (hind : ∀ (m : ℕ) (b : Fin m → Z), LinearIndependent K0 b → LinearIndependent K fun i => ι (b i))
      (htop : Submodule.span K (Set.range ι) = ⊤) (M N : Submodule (𝓞 K0) Z)
      (hM : IsLatIn ⊤ M) (hN : IsLatIn ⊤ N) (hle : N ≤ M)
      (hA : up ι M = A) (hNT : up ι N ≤ T) (hT : IsLatIn ⊤ T) (hTA : T ≤ A)
      (a0 : 𝓞 K0) (ha0 : (a0 : K0) ≠ 0) (hv0 : 0 ≤ vw (v.under (𝓞 K0)) (a0 : K0))
      (ha : a ≠ 0)
      (hdepth : (v.asIdeal.ramificationIdx (𝓞 K0) : ℤ) * vw (v.under (𝓞 K0)) (a0 : K0) ≤ vw v a)
      (hcompleted :
        let w := v.under (𝓞 K0)
        let C := (locC (K := K0) w M).map ((algebraMap (𝓞 K0) (w.adicCompletionIntegers K0) a0) • LinearMap.id) ⊔ locC w N
        qlen C (locC w N) ≠ ⊤ ∧ ((qlen C (locC w N)).toNat : ℝ) ≤ r) :
      CompletedRow K0 v A T a r

theorem CompletedRow.transport {v : HeightOneSpectrum (𝓞 K)} {n : ℕ}
    {A T : Submodule (𝓞 K) (Fin n → K)} {a : K} {r : ℝ} (src : CompletedRow K0 v A T a r) :
    IsLatIn ⊤ T ∧ a ≠ 0 ∧ (lix v (sc a A ⊔ T) T : ℝ) ≤ (v.asIdeal.ramificationIdx (𝓞 K0) : ℝ) * r := by
  cases src with
  | fromLattices ι hind htop M N hM hN hle hA hNT hT hTA a0 ha0 hv0 ha hdepth hcompleted =>
    subst A
    exact ⟨hT, ha, completed_to_ramified ι hind htop M N hM hN hle v a0 ha0 hv0 T hT hNT hTA a ha
      hdepth r hcompleted.1 hcompleted.2⟩

variable {Bs : DefBase K} {Df : DefSide Bs} {S : IndefData Df} {P : Type} [Group P] [Finite P] {c : OnConst}

/-- A single implication from completed inputs at both selected places to the original row window. -/
theorem paired_of_completed (O : OnObj S P c)
    (r : Bool → Bs.J → HeightOneSpectrum (𝓞 K0) → ℝ)
    (hn : ∀ k j v, 0 ≤ r k j v)
    (hs : ∀ k j, Summable (fun v => r k j v * Formalism.BasicNotions.lw K0 v))
    (hb : ∀ k j, ∑' v, r k j v * Formalism.BasicNotions.lw K0 v ≤
      (O.nZ j : ℝ) * (O.f * O.m * O.b * O.de2))
    (hr : ∀ k v j, (if k = true then O.r2 v j else O.r1 v j) =
      (v.asIdeal.ramificationIdx (𝓞 K0) : ℝ) * r k j (v.under (𝓞 K0)))
    (hd : 0 ≤ O.de2 ∧ O.de2 ≤ 1)
    (inputs : AtPair S fun v => ∀ j, O.Th1 v j ≤ O.Th v j ∧ vw v (O.a v j) = (O.E v j : ℤ) ∧
      CompletedRow K0 v (O.Ms j) (O.Th1 v j) (O.a v j) (r (decide (plc v = O.pde)) j (v.under (𝓞 K0)))) :
    LatticeIndexBoundAtPairs O true := by
  apply paired_scalar O r hn hs hb hr hd
  have one (v : HeightOneSpectrum (𝓞 K)) (j : Bs.J) (h : O.Th1 v j ≤ O.Th v j ∧
      vw v (O.a v j) = (O.E v j : ℤ) ∧
      CompletedRow K0 v (O.Ms j) (O.Th1 v j) (O.a v j) (r (decide (plc v = O.pde)) j (v.under (𝓞 K0)))) :
      IsLatIn ⊤ (O.Th1 v j) ∧ O.Th1 v j ≤ O.Th v j ∧ O.a v j ≠ 0 ∧
      vw v (O.a v j) = (O.E v j : ℤ) ∧
      (lix v (sc (O.a v j) (O.Ms j) ⊔ O.Th1 v j) (O.Th1 v j) : ℝ) ≤
        (v.asIdeal.ramificationIdx (𝓞 K0) : ℝ) * r (decide (plc v = O.pde)) j (v.under (𝓞 K0)) := by
    obtain ⟨hT, ha, hindex⟩ := h.2.2.transport
    exact ⟨hT, h.1, ha, h.2.1, hindex⟩
  intro w hw
  exact ⟨fun j => one w j ((inputs w hw).1 j), fun j => one _ j ((inputs w hw).2 j)⟩

end ScalarPassage
#print axioms ScalarPassage.completed_to_ramified
#print axioms ScalarPassage.paired_of_completed
