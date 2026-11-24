import ThetaRowBound
import ThetaRunSelectors
import Development.AbelianVarietyTheory.Definitions.Divisors.IsDeltaDelAtOwnAt
import Development.AbelianVarietyTheory.Proofs.HeightProofs.ExistsPageRunRecordSubFour
import Development.AbelianVarietyTheory.Proofs.HeightProofs.FieldSmallIffOpo

noncomputable section
open NumberField IsDedekindDomain
open Formalism.BasicNotions Formalism.MainNotions Formalism.L2.Pj Formalism.L2.DIV Formalism.IndefR Formalism.IndefR.Links Formalism.IndefR.FWT
open Formalism.MainNotions.WeightAlgebra Formalism.MainNotions.DIV.Cons Formalism.MainNotions.Gaps Formalism.MainNotions.Gaps.EtaleWeightGaps
open GlobalTheory.RunJoin GlobalTheory.RunIn GlobalTheory.FinalJoin GlobalTheory.FinalJoin2 GlobalTheory.RealIndexBound

open Module ScalarPassage Formalism.EigenvalueLevelCeiling Formalism.DivisionValues Formalism.MainNotions.Gaps.LocalGlobalPassage
namespace GlobalTheory.BigOn.CoreWit
/-- Both run selectors return their weighted base allowance and the ramified row estimate for that allowance. -/
theorem exists_two_run_rows : ∃ x₁ : ℝ, ∀ (D : D7) (G : Type) (J : CoreJ D) (r : TwoRuns J G) (EX : ErrX D) (L : SizeData₂ D)
    (Pm : ParameterChoice' D L) (Tp : ParamsT D L Pm) (hK : DV.KapDef D),
    (∀ v j, InR D j → ParOK (r.used v).full.toTop EX (ownAt D v) j) → PageNum Tp x₁ → FieldSmall D L →
      ∀ v (h : LawsP (r.used v).full.toTop) (hinj : Function.Injective D.what₂.OtoLL) (j : ℕ) (hj : InR D j),
      let X := recPJ h j hj
      let ka := kaR Tp hK j
      let wL := lR Tp hK j
      let wF := fR Tp hK j
      let S := scalOfP (recB h.toLawsCore) hinj EX (ownAt D v) ka wL wF Tp.TO
      ∃ (n : SecNorm (recB h.toLawsCore)) (CRm : ℝ)
        (G : GlobalFamilyData (recPlusN h j hj n) ka wL wF) (Qf : ∀ la, LocalPointData G la),
        let allowance := fun la => rLa (Qf la) CRm Tp.TO (cc D L Tp.CP Tp.eP 7 wL)
        (∀ la, 0 ≤ allowance la) ∧ Summable (fun la => allowance la * X.lN la) ∧
        (∑' la, allowance la * X.lN la) ≤ X.rk ka ((recB h.toLawsCore).Mlat j ka) * D.R.f * D.R.m * L.sc.b * L.de2 ∧
        FamilyRowBound X S ka wL wF Tp.TO (nusR h j wL) allowance := by
  obtain ⟨x₁, hrun⟩ := exists_two_run_depth
  refine ⟨x₁, ?_⟩
  intro D G J r EX L Pm Tp hK hp hn hF v h hinj j hj
  obtain ⟨n, C, fam, pts, h0, hs, hb, hd⟩ := hrun D G J r EX L Pm Tp hK hp hn hF v h hinj j hj
  refine ⟨n, C, fam, pts, h0, hs, hb, ?_⟩
  exact rows_of_depth _ _ _ _ _ _ _ _ hd

end GlobalTheory.BigOn.CoreWit
#print axioms GlobalTheory.BigOn.CoreWit.exists_two_run_rows
