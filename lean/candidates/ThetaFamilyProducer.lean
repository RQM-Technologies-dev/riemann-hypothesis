import ThetaScalar
import Formalism.SharpRestriction.GenusPolyhedralBounds.RelativeIndexClassSets.TheoremZeroBundledOfLift

/- The same chosen local points supply the depth bound and the weighted sum. -/
noncomputable section
open Formalism.MainNotions.WeightAlgebra Formalism.BasicNotions NumberField IsDedekindDomain Module
namespace Formalism.MainNotions.Gaps.EtaleWeightGaps
variable {D : D7} {B : WeightFamilies.Prov D} {P : ModuliIntegralCharts.Prov D}

/-- Pointwise simplification of the actual allowance at the terminal index. -/
theorem terminal_rLa {j : ℕ} {X : PJ D B P j} {ka wL wF : WeightFamilies.Wt D j} {G : GlobalFamilyData X ka wL wF}
    {la : HeightOneSpectrum (𝓞 B.KO)} (Q : LocalPointData G la) (CRm : ℝ) (T : ℕ) (c : ℝ) (hj : D.R.m ≤ j) :
    rLa Q CRm T c =
      (Nat.choose (T - 1) (WeightFamilies.dimY D j) : ℝ) * Q.Ila.toNat +
        (Formalism.MainNotions.Gaps.SizeBoundsAlt.gaussC (B.Mlat j ka) G.zc la : ℝ) := by
  have hq := lenQ_of_ge G hj CRm T c la
  unfold lenQ at hq
  simp [rLa, if_neg (not_lt.mpr hj), hq]

/-- One family's allowance at all permitted places and depths. -/
def ThetaAllowance {j : ℕ} {X : PJ D B P j} {ka wL wF : WeightFamilies.Wt D j}
    {G : GlobalFamilyData X ka wL wF} (Qf : ∀ la, LocalPointData G la) (S : Scal B)
    (T : ℕ) (CRm c : ℝ) (nus : HeightOneSpectrum (𝓞 B.KO) → ℝ) (budget : ℝ) : Prop :=
  let r := fun la => rLa (Qf la) CRm T c
  (∀ la, 0 ≤ r la) ∧ Summable (fun la => r la * X.lN la) ∧
    (∑' la, r la * X.lN la) ≤ budget ∧
    ∀ la (e : ℕ), (T : ℝ) * nus la ≤ (e : ℝ) →
      thetaExcess X S ka wL wF T la e ≠ ⊤ ∧
        ((thetaExcess X S ka wL wF T la e).toNat : ℝ) ≤ r la

/-- Keep Qf explicit through the local length estimate and the global sum. -/
theorem thetaFamilyWitness :
  ∀ (large₂ : SizeData₂ D) (X : Prov D B P) (K : KAdm) (H : KHyp) (Ch Ah Cq Aq C2 A2 CR CT : ℝ),
    ∀ j (h1 : 1 ≤ j) (h2 : j ≤ D.R.m) (S : Scal B) (ka wL wF : WeightFamilies.Wt D j) (T nP nW : ℕ) (h0 : ℝ)
      (nus : HeightOneSpectrum (𝓞 B.KO) → ℝ),
    HypC large₂ (X j h1 h2) H C2 A2 CR 0 CT S ka wL wF T nP nW h0 nus →
    LatAt B j ka → SupBoundByL2AtWeight large₂ B j ka K.CG K.AG → LAMwAt large₂ B j ka K.CL K.AL →
    (j < D.R.m → QAt large₂ B j ka K.CRm H.CK Ch Ah Cq Aq T (cc D large₂ C2 A2 CR wL)) →
    ∀ (G : GlobalFamilyData (X j h1 h2) ka wL wF) (Gc PH Prw Pet Pd : ℝ) (Qf : ∀ la, LocalPointData G la),
    G.TiedW S Gc Prw → G.TiedTh S Gc → G.TiedZ S T Gc →
    G.TiedQ large₂ S K.CRm T (cc D large₂ C2 A2 CR wL) Ch Ah → G.TiedEt large₂ K.Cf K.Af →
    DeepHerm (X j h1 h2) ka → DeepSubMul (X j h1 h2) → DeepLogD (X j h1 h2) ka Pd →
    PageGd (X j h1 h2) ka large₂ K.CG K.AG Pd →
    ShareRd (D := D) (j := j) T G.del ((X j h1 h2).rk ka (B.Mlat j ka)) →
    ShareRho (D := D) (j := j) T G.rz ((X j h1 h2).rk ka (B.Mlat j ka)) →
    ShareRhoP (D := D) (j := j) T G.rq ((X j h1 h2).rk ka (B.Mlat j ka)) →
    PolyDom (j := j) D B large₂ K H C2 A2 CR Ch Ah Cq Aq Gc PH Prw Pet Pd ka →
    (∀ la, InBasis G la) → (∀ la, (Qf la).InCurve) → (∀ la, (Qf la).InTie S) → (∀ la, (Qf la).InLiftC S Gc Prw T) →
    (∀ la, InContainZ G la S T) → (∀ la, InContainM G la K.CRm T (cc D large₂ C2 A2 CR wL)) →
    CombBound G S (cc D large₂ C2 A2 CR wL) nus →
    Heights Qf Gc PH Prw Pet →
    ThetaAllowance Qf S T K.CRm (cc D large₂ C2 A2 CR wL) nus
      ((X j h1 h2).rk ka (B.Mlat j ka) * D.R.f * D.R.m * large₂.sc.b * large₂.de2) := by
  intro large₂ X K H Ch Ah Cq Aq C2 A2 CR CT j h1 h2 S ka wL wF T nP nW h0 nus hH lA sA mA qA G Gc PH Prw Pet Pd Qf
    tW tTh tZ tQ tEt dH dS dL pG sRd sRho sRhoP hP iB iC iT iLf iZ iM hB hHt
  obtain ⟨hrs, hrb⟩ := sumC large₂ X K H Ch Ah Cq Aq C2 A2 CR CT j h1 h2 S ka wL wF T nP nW h0 nus hH lA sA mA qA
    G Gc PH Prw Pet Pd tW tTh tZ tQ tEt dH dS dL pG sRd sRho sRhoP hP hB Qf hHt
  refine ⟨fun la => rLa_nonneg_comb hB (Qf la) _ _ _, hrs, hrb, ?_⟩
  intro la e he
  let Q := Qf la
  have hLift := iLf la tW (iC la) (iT la)
  have hIla := hHt.1 la
  have hΘ := theta_le_msup_of_hypC (X j h1 h2) S hH
  have hspK := (span_Thc_of_hypC hH).2.2
  obtain ⟨-, hSet, -, -, hH2, -⟩ := hH
  have hka := ka_eq_addL_of_setC hSet
  obtain ⟨-, -, -, -, -, -, -, -, -, -, -, -, -, -, -, -, -, hT0, hDT, -⟩ := hSet
  have hok : Q.Ok S K.CRm T (cc D large₂ C2 A2 CR wL) := ⟨iB la, iC la, iT la, iZ la, iM la⟩
  have hw : ∀ k, G.w k ∈ (X j h1 h2).WWc S.sW wL := by
    intro k
    rw [← tW.1]
    exact Submodule.subset_span ⟨k, rfl⟩
  have hth'M : ∀ i, G.th' i ∈ B.Mlat j wF := fun i => hH2.2.1 (tTh i).1
  refine ⟨thetaExcess_finite _ _ _ _ _ _ _ _ lA hΘ hspK, ?_⟩
  exact localThetaBudget G la Q S K.CRm (cc D large₂ C2 A2 CR wL) e (nus la) hka lA hΘ hspK hT0 hDT hw tW.2.1
    (fun i => (tTh i).1) hth'M
    (fun k => (tZ.1 k).1) (fun k => (tZ.1 k).2.1) (fun k => (tZ.1 k).2.2.2) tZ.2.1 tZ.2.2
    tQ.2.1 tQ.2.2.1 (iB la) (iC la) (iT la) (iM la)
    (fun ζ => vEt_nonneg_comb hB Q ζ) (fun ζ => nu_le_comb hB Q (iT la) ζ) he
    (lenBase_all j (X j h1 h2) ka wL wF G la Q S K.CRm T (cc D large₂ C2 A2 CR wL) hok hth'M hw hIla)
    (lenPoleL_all j (X j h1 h2) ka wL wF G la Q S K.CRm T e (cc D large₂ C2 A2 CR wL) hok hLift hw)


end Formalism.MainNotions.Gaps.EtaleWeightGaps
#print axioms Formalism.MainNotions.Gaps.EtaleWeightGaps.thetaFamilyWitness
