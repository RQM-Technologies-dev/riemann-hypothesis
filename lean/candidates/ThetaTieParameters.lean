import ThetaRunSelectors
import Development.AbelianVarietyTheory.Proofs.HeightProofs.ParametersOkOfLaws
set_option autoImplicit false

open NumberField IsDedekindDomain Module
open Formalism.BasicNotions Formalism.MainNotions Formalism.MainNotions.DIV.Cons Formalism.L2.Pj Formalism.DivisionValues Formalism.EigenvalueLevelCeiling Formalism.L2.DIV Formalism.L2.Indef Formalism.L2.Indef.Tree Formalism.IndefR Formalism.IndefR.Links
open Formalism.IndefR.Cx Formalism.IndefR.FWT Formalism.BasicNotions.TH Formalism.MainNotions.GlobalTheoryTheory.GenusMassVolumes Formalism.L2.Theta
open GlobalTheory.OntoChain GlobalTheory.RealIndexBound GlobalTheory.OnTies GlobalTheory.FormTies GlobalTheory.BigOn
attribute [local instance] Formalism.BasicNotions.Host.cmStar

open GlobalTheory.RunJoin GlobalTheory.RunIn GlobalTheory.FinalJoin GlobalTheory.FinalJoin2
namespace GlobalTheory.BigOn

theorem selector_parameters_of_ties : ∀ (D : D7) (G : Type) [Group G] [Fintype G] (Pl0 T0 : Type) (A : FamIn D.what₂.LL G Pl0 T0 D.R.m) (J : CoreJ D) [Algebra J.Q.c.F D.what₂.LL] (R : RealDat D A J.Q.c.F) (F : Face D A) (κ : ∀ i : Fin D.R.m, WeightFamilies.Wt D ((i : ℕ) + 1)) (v₀ : ∀ (i : Fin D.R.m) (σ : D.what₂.LL →+* ℂ), (R.MW i σ).Vec) (fw : FWTie J R κ v₀) (L : SizeData₂ D) (Pm : ParameterChoice' D L) (Tp : ParamsT D L Pm) (hK : DV.KapDef D) (EX : ErrX D) (r : TwoRuns J G), CoreTies L EX J R → RunsOk fw r → OwnPin r → ∀ v j, InR D j → ParOK (r.used v).full.toTop EX (ownAt D v) j := by
  intro D G _ _ Pl0 T0 A J _ R F κ v₀ fw L Pm Tp hK EX r hc ok hown v
  let h := (ok.laws v).p
  have hl := ok.laws v
  have hF : GlobalTheory.FinalJoin2.FieldOK0 D (ownAt D v) := by
    unfold ownAt
    split_ifs
    · exact hc.field₂
    · exact hc.field₁
  refine GlobalTheory.FinalJoin2.liftIndexParameterConditions_of_coreAndShortLaws D J _ EX _ hl.j h hl.sh rfl hc.canon hF hc.halfEX ?_
  intro j hj n
  exact ⟨hl.lvA j hj n, hown v j n hj⟩

end GlobalTheory.BigOn
