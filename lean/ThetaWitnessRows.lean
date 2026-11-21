import ScalarPassage

noncomputable section
open Module NumberField IsDedekindDomain
open Formalism.DivisionValues Formalism.EigenvalueLevelCeiling Formalism.L2.Indef Formalism.L2.Indef.Tree

namespace ScalarPassage

variable {K0 K : Type} [Field K0] [NumberField K0] [StarRing K0] [Field K] [NumberField K] [StarRing K] [Algebra K0 K]
variable {Bs : DefBase K} {Df : DefSide Bs} {S : IndefData Df} {P : Type} [Group P] [Finite P] {c : OnConst}

/-- Store the two transported witnesses when constructing the row object. -/
def withRemainders (O : OnObj S P c) (r : Bool → Bs.J → HeightOneSpectrum (𝓞 K0) → ℝ) : OnObj S P c :=
  { O with
    r1 := fun v j => (v.asIdeal.ramificationIdx (𝓞 K0) : ℝ) * r false j (v.under (𝓞 K0))
    r2 := fun v j => (v.asIdeal.ramificationIdx (𝓞 K0) : ℝ) * r true j (v.under (𝓞 K0)) }

theorem paired_with_remainders (O : OnObj S P c)
    (r : Bool → Bs.J → HeightOneSpectrum (𝓞 K0) → ℝ)
    (hn : ∀ k j v, 0 ≤ r k j v)
    (hs : ∀ k j, Summable (fun v => r k j v * Formalism.BasicNotions.lw K0 v))
    (hb : ∀ k j, ∑' v, r k j v * Formalism.BasicNotions.lw K0 v ≤
      (O.nZ j : ℝ) * (O.f * O.m * O.b * O.de2))
    (hd : 0 ≤ O.de2 ∧ O.de2 ≤ 1)
    (inputs : AtPair S fun v => ∀ j, O.Th1 v j ≤ O.Th v j ∧ vw v (O.a v j) = (O.E v j : ℤ) ∧
      CompletedRow K0 v (O.Ms j) (O.Th1 v j) (O.a v j) (r (decide (plc v = O.pde)) j (v.under (𝓞 K0)))) :
    LatticeIndexBoundAtPairs (withRemainders O r) true := by
  apply paired_of_completed (withRemainders O r) r hn hs hb _ hd inputs
  intro k v j
  cases k <;> rfl

/-- The two original classes of rational places, including possibly empty classes. -/
def Populated (O : OnObj S P c) (k : Bool) : Prop :=
  ∃ v : HeightOneSpectrum (𝓞 K), decide (plc v = O.pde) = k

open Classical in
def remainderOrZero (O : OnObj S P c)
    (base : ∀ k, Populated O k → Bs.J → HeightOneSpectrum (𝓞 K0) → ℝ)
    (k : Bool) (j : Bs.J) (w : HeightOneSpectrum (𝓞 K0)) : ℝ :=
  if hk : Populated O k then base k hk j w else 0

/-- Select each populated run once and keep its allowance on both members of
every pair. An absent class requires neither a family nor a local estimate. -/
theorem paired_on_occupied (O : OnObj S P c)
    (base : ∀ k, Populated O k → Bs.J → HeightOneSpectrum (𝓞 K0) → ℝ)
    (hn : ∀ k hk j w, 0 ≤ base k hk j w)
    (hs : ∀ k hk j, Summable (fun w => base k hk j w * Formalism.BasicNotions.lw K0 w))
    (hb : ∀ k hk j, ∑' w, base k hk j w * Formalism.BasicNotions.lw K0 w ≤
      (O.nZ j : ℝ) * (O.f * O.m * O.b * O.de2))
    (hzero : ∀ j, 0 ≤ (O.nZ j : ℝ) * (O.f * O.m * O.b * O.de2))
    (hd : 0 ≤ O.de2 ∧ O.de2 ≤ 1)
    (hi : ∀ k (hk : Populated O k), AtPair S fun v => decide (plc v = O.pde) = k → ∀ j,
      O.Th1 v j ≤ O.Th v j ∧ vw v (O.a v j) = (O.E v j : ℤ) ∧
      CompletedRow K0 v (O.Ms j) (O.Th1 v j) (O.a v j) (base k hk j (v.under (𝓞 K0)))) :
    LatticeIndexBoundAtPairs (withRemainders O (remainderOrZero O base)) true := by
  classical
  refine paired_with_remainders O (remainderOrZero O base) ?_ ?_ ?_ hd ?_
  · intro k j w
    by_cases hk : Populated O k
    · simpa [remainderOrZero, hk] using hn k hk j w
    · simp [remainderOrZero, hk]
  · intro k j
    by_cases hk : Populated O k
    · simpa [remainderOrZero, hk] using hs k hk j
    · simp [remainderOrZero, hk]
  · intro k j
    by_cases hk : Populated O k
    · simpa [remainderOrZero, hk] using hb k hk j
    · simpa [remainderOrZero, hk] using hzero j
  · intro w hw
    have left : Populated O (decide (plc w = O.pde)) := ⟨w, rfl⟩
    have right : Populated O (decide (plc (conjPl w) = O.pde)) := ⟨conjPl w, rfl⟩
    exact ⟨by simpa only [remainderOrZero, dif_pos left] using (hi _ left w hw).1 rfl,
      by simpa only [remainderOrZero, dif_pos right] using (hi _ right w hw).2 rfl⟩

end ScalarPassage
#print axioms ScalarPassage.paired_with_remainders
#print axioms ScalarPassage.paired_on_occupied
