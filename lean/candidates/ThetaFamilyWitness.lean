import ThetaFamilyProducer
import ThetaFamilyRow
import ThetaWitnessRows

noncomputable section
open Formalism.MainNotions.WeightAlgebra Formalism.BasicNotions NumberField IsDedekindDomain Module
namespace Formalism.MainNotions.Gaps.EtaleWeightGaps
variable {D : D7} {B : WeightFamilies.Prov D} {P : ModuliIntegralCharts.Prov D}

open ScalarPassage Formalism.EigenvalueLevelCeiling Formalism.DivisionValues
open Formalism.MainNotions.Gaps.LocalGlobalPassage

/-- The base-place allowance for each occupied run and row, with its own local points. -/
def twoThetaRemainders {J : Type} (idx : Bool → J → ℕ)
    (X : ∀ k i, PJ D B P (idx k i)) (ka wL wF : ∀ k i, WeightFamilies.Wt D (idx k i))
    (G : ∀ k i, GlobalFamilyData (X k i) (ka k i) (wL k i) (wF k i))
    (Q : ∀ k i la, LocalPointData (G k i) la) (CRm c : Bool → J → ℝ) (T : Bool → J → ℕ) :
    Bool → J → HeightOneSpectrum (𝓞 B.KO) → ℝ :=
  fun k i la => rLa (Q k i la) (CRm k i) (T k i) (c k i)

/-- Both occupied selectors, in common base coordinates. The remaining local
premise ties the selected family's completed lattice to the actual row. -/
theorem paired_of_theta_points
    {K : Type} [Field K] [NumberField K] [StarRing K] [StarRing B.KO] [Algebra B.KO K]
    {Bs : Formalism.L2.Indef.DefBase K} {Df : Formalism.L2.Indef.DefSide Bs}
    {S : Formalism.L2.Indef.IndefData Df} {U : Type} [Group U] [Finite U]
    {oc : Formalism.L2.Indef.Tree.OnConst} (O : Formalism.L2.Indef.Tree.OnObj S U oc)
    (idx : Bool → Bs.J → ℕ) (X : ∀ k i, PJ D B P (idx k i))
    (ka wL wF : ∀ k i, WeightFamilies.Wt D (idx k i))
    (G : ∀ k i, GlobalFamilyData (X k i) (ka k i) (wL k i) (wF k i))
    (Q : ∀ k i la, LocalPointData (G k i) la) (CRm c : Bool → Bs.J → ℝ) (T : Bool → Bs.J → ℕ)
    (scal : Bool → Bs.J → Scal B) (nus : Bool → Bs.J → HeightOneSpectrum (𝓞 B.KO) → ℝ)
    (hA : ∀ k i, ThetaAllowance (Q k i) (scal k i) (T k i) (CRm k i) (c k i) (nus k i)
      ((O.nZ i : ℝ) * (O.f * O.m * O.b * O.de2)))
    (hd : 0 ≤ O.de2 ∧ O.de2 ≤ 1) :
    let r := twoThetaRemainders idx X ka wL wF G Q CRm c T
    Formalism.L2.Indef.Tree.AtPair S (fun v => ∀ i, O.Th1 v i ≤ O.Th v i ∧ vw v (O.a v i) = (O.E v i : ℤ) ∧
      CompletedRow B.KO v (O.Ms i) (O.Th1 v i) (O.a v i) (r (decide (plc v = O.pde)) i (v.under (𝓞 B.KO)))) →
      Formalism.L2.Indef.Tree.LatticeIndexBoundAtPairs (withRemainders O r) true := by
  intro r inputs
  refine paired_with_remainders O r ?_ ?_ ?_ hd inputs
  · exact fun k i => (hA k i).1
  · exact fun k i => (hA k i).2.1
  · exact fun k i => (hA k i).2.2.1

end Formalism.MainNotions.Gaps.EtaleWeightGaps

#print axioms Formalism.MainNotions.Gaps.EtaleWeightGaps.thetaFamilyWitness
#print axioms Formalism.MainNotions.Gaps.EtaleWeightGaps.paired_of_theta_points
