import ThetaChosenInputs
import Development.AbelianVarietyTheory.Definitions.Divisors.IsDeltaDelAtOwnAt
import Development.AbelianVarietyTheory.Proofs.HeightProofs.ExistsPageRunRecordSubFour
import Development.AbelianVarietyTheory.Proofs.HeightProofs.FieldSmallIffOpo

noncomputable section
open NumberField IsDedekindDomain
open Formalism.BasicNotions Formalism.MainNotions Formalism.L2.Pj Formalism.L2.DIV Formalism.IndefR Formalism.IndefR.Links Formalism.IndefR.FWT
open Formalism.MainNotions.WeightAlgebra Formalism.MainNotions.DIV.Cons Formalism.MainNotions.Gaps Formalism.MainNotions.Gaps.EtaleWeightGaps
open GlobalTheory.RunJoin GlobalTheory.RunIn GlobalTheory.FinalJoin GlobalTheory.FinalJoin2 GlobalTheory.RealIndexBound

namespace GlobalTheory.BigOn.CoreWit
/-- On the common page window, each occupied selector keeps its chosen local points. -/
theorem exists_two_run_depth : ∃ x₁ : ℝ, ∀ (D : D7) (G : Type) (J : CoreJ D) (r : TwoRuns J G) (EX : ErrX D) (L : SizeData₂ D)
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
        ∀ la e, (Tp.TO : ℝ) * nusR h j wL la ≤ (e : ℕ) →
          thetaExcess X S ka wL wF Tp.TO la e ≠ ⊤ ∧
          ((thetaExcess X S ka wL wF Tp.TO la e).toNat : ℝ) ≤ allowance la := by
  obtain ⟨x₀, hrun⟩ := GlobalTheory.FinalJoin.exists_theta_run
  obtain ⟨CK, hCK⟩ := GlobalTheory.FinalJoin.RecordRun.exists_pageRun_record_sub_four
  refine ⟨max ((10 : ℝ) ^ 60) (x₀ 20 CK), ?_⟩
  rintro D G J r EX L Pm Tp hK hpar ⟨S, hCnW, hg, hC, hCZ, hx⟩ hF v h hinj j hj
  have hP := hCK D L Pm Tp hK S hCnW hg ((le_max_left _ _).trans hx) hC hCZ _ _ j (recPJ h j hj) hj
    ((GlobalTheory.FinalJoin2.fieldSmall_iff_opo D _ h L).1 hF)
  obtain ⟨n, C, G', Qf, hA, hEq⟩ := hrun D _ h hinj EX _ (hpar v) j hj L _ _ _ _ _ _ _ _ _ _ _ hP ((le_max_right _ _).trans hx)
  refine ⟨n, C, G', Qf, hA.1, hA.2.1, hA.2.2.1, ?_⟩
  intro la e he
  rw [← hEq la e]
  exact hA.2.2.2 la e he

end GlobalTheory.BigOn.CoreWit
#print axioms GlobalTheory.BigOn.CoreWit.exists_two_run_depth
