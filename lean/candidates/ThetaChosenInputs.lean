import ThetaFamilyProducer
import Development.AbelianVarietyTheory.Proofs.HeightProofs.ExistsThresholdRunHolds

/- Adapted from the pinned IndexBoundChosenFamilyOfIntrinsicHypotheses and
ExistsThresholdRunHolds modules. The changed conclusion retains the same Qf
on the family G.setZQ and its scalar allowance. -/
noncomputable section
open NumberField IsDedekindDomain Formalism.BasicNotions Formalism.MainNotions Formalism.MainNotions.WeightAlgebra Formalism.MainNotions.DIV.Cons Formalism.MainNotions.Gaps Formalism.MainNotions.Gaps.EtaleWeightGaps Formalism.L2.Pj ReciprocityTheory.ChartRestriction.G ReciprocityTheory.ChartRestriction.G.Geo.Tor GlobalTheory.RunJoin GlobalTheory.RunIn GlobalTheory.FinalJoin

set_option maxHeartbeats 4000000
set_option synthInstance.maxHeartbeats 400000

namespace GlobalTheory.FinalJoin

/-- Build the scalar witness at the point where the theta coefficients and
their local points are chosen, before constructing the all-subspace conclusion. -/
theorem thetaWitnessOfIntrinsic (D : D7) (B : WeightFamilies.Prov D) (P : ModuliIntegralCharts.Prov D)
    (X : Prov D B P) (j : ℕ) (h1 : 1 ≤ j) (h2 : j ≤ D.R.m) (large₂ : SizeData₂ D)
    (K : KAdm) (H : KHyp) (Ch Ah Cq Aq C2 A2 CR CT : ℝ) (S : Scal B) (ka wL wF : WeightFamilies.Wt D j)
    (T nP nW : ℕ) (h0 : ℝ) (nus : HeightOneSpectrum (𝓞 B.KO) → ℝ)
    (hI : InputsR large₂ (X j h1 h2) K H Ch Ah Cq Aq C2 A2 CR CT S ka wL wF T nP nW h0 nus) :
    ∃ (G : GlobalFamilyData (X j h1 h2) ka wL wF) (Qf : ∀ la, LocalPointData G la),
      ThetaAllowance Qf S T K.CRm (cc D large₂ C2 A2 CR wL) nus
        ((X j h1 h2).rk ka (B.Mlat j ka) * D.R.f * D.R.m * large₂.sc.b * large₂.de2) := by
  obtain ⟨⟨hH, hLat, hLAM, hQ, hSub⟩, hSup, hHerm, G, Gc, PH, Prw, Pet, Pd, hLogD,
    ⟨hW, hTh, hEt, hPGd, hPG4, hPGq, hRd, hRho, hRhoP, hPoly, hB, hM⟩, hComb, Qf, hC, hTie, hLift, hHt⟩ := hI
  have hSet := hH.2.1
  have hH2 := hH.2.2.2.2.1
  obtain ⟨hS0, hSK⟩ := shortG_of_scalB hH.2.2.1 hPG4
  have hDT : WeightFamilies.dimY D j ≤ T := hSet.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1
  have hwt : SizeBoundsAlt.wtIter wadd wL ((X j h1 h2).wF0 wL wF) (a0 D j T) = ka := by
    rw [iterated_weight_at_vanishingOrder (X j h1 h2) wL wF T hDT]; exact (ka_eq_addL_of_setC hSet).symm
  obtain ⟨rz, alz, th0, zc, hTZ, hZ⟩ := exists_global_family_zero_choice G S T Gc hwt hS0 hH2.2.2.1
  obtain ⟨th, hTQ⟩ := exists_global_family_quotient_bounded
    ({ G with rz := rz, alz := alz, th0 := th0, zc := zc } : GlobalFamilyData (X j h1 h2) ka wL wF) large₂ S K.CRm T
    (cc D large₂ C2 A2 CR wL) (Gc * ka.size) Ch Ah hSK hH2.2.2.2
    (mul_le_mul_of_nonneg_right hPGq (by linarith [ka.one_le_size]))
  obtain ⟨hR1, -⟩ := GlobalTheory.shareRho_and_shareRhoT_of_shareRhoR D B P j (X j h1 h2) ka wL wF
    (G.setZQ rz alz th0 zc _ th) S T _ Gc hRho hTZ hZ
  have hM' : ∀ la, InContainM (G.setZQ rz alz th0 zc _ th) la K.CRm T (cc D large₂ C2 A2 CR wL) :=
    fun la => inContainM_of _ la S _ T _ (hM la) (hZ la)
  have hLift' : ∀ la, ((Qf la).tr G rz alz th0 zc _ th).InLiftC S Gc Prw T :=
    fun la => tr_InLiftC G rz alz th0 zc _ th (Qf la) S Gc Prw T (hLift la)
  refine ⟨G.setZQ rz alz th0 zc _ th, fun la => (Qf la).tr G rz alz th0 zc _ th, ?_⟩
  exact thetaFamilyWitness large₂ X K H Ch Ah Cq Aq C2 A2 CR CT j h1 h2 S ka wL wF T nP nW h0 nus hH hLat hSup hLAM hQ
    (G.setZQ rz alz th0 zc _ th) Gc PH Prw Pet Pd (fun la => (Qf la).tr G rz alz th0 zc _ th)
    hW hTh hTZ hTQ hEt hHerm hSub hLogD hPGd hRd hR1 hRhoP hPoly hB hC hTie hLift' hZ hM' hComb hHt


/-- Change the archimedean norm and keep the resulting finite-place function. -/
theorem thetaWitnessOfNet {D : D7} {B : WeightFamilies.Prov D} {P : ModuliIntegralCharts.Prov D} (X : WeightAlgebra.Prov D B P) (j : ℕ) (h1 : 1 ≤ j)
    (h2 : j ≤ D.R.m) (large₂ : SizeData₂ D) (CL : ℝ) (H : KHyp) (Cq C2 A2 CT : ℝ) (S : Scal B) (ka wL wF : WeightFamilies.Wt D j)
    (Tn nP nW : ℕ) (h0 : ℝ) (nus : HeightOneSpectrum (𝓞 B.KO) → ℝ)
    (hn : InputsNet large₂ (X j h1 h2) (kR CL) H 1 4 Cq 4 C2 A2 7 CT S ka wL wF Tn nP nW h0 nus) :
    ∃ (n : SecNorm B) (G : GlobalFamilyData (PJ.tol2NormAlt n.N n.h0 n.h1 n.h2 n.h3 n.h4 (X j h1 h2)) ka wL wF)
      (Qf : ∀ la, LocalPointData G la),
      ThetaAllowance Qf (scalarsWithNorm n.N n.h0 n.h1 n.h2 n.h3 n.h4 S) Tn (k4 large₂ CL).CRm
        (cc D large₂ C2 A2 7 wL) nus ((X j h1 h2).rk ka (B.Mlat j ka) * D.R.f * D.R.m * large₂.sc.b * large₂.de2) := by
  obtain ⟨n, hR⟩ := GlobalTheory.T.exists_secNorm_inputsR_of_inputsNet D B P j (X j h1 h2) large₂ (kR CL) H 1 4 Cq 4 C2 A2 7 CT S ka wL wF Tn nP nW h0 nus hn
  have hR' := GlobalTheory.T.indexBoundIntrinsicHypotheses_netBound_degreeTwo D _ P j _ large₂ CL H 1 4 Cq 4 C2 A2 7 CT _ ka wL wF Tn nP nW h0 _ hR
  let Y : WeightAlgebra.Prov D n.base P := fun j h1 h2 => PJ.tol2NormAlt n.N n.h0 n.h1 n.h2 n.h3 n.h4 (X j h1 h2)
  exact ⟨n, thetaWitnessOfIntrinsic D n.base P Y j h1 h2 large₂ (k4 large₂ CL) H 1 4 Cq 4 C2 A2 7 CT
    _ ka wL wF Tn nP nW h0 nus hR'⟩

/-- The fixed-window statement. Reuse the given finite-net witness for this
row, including its chosen constants, places, depth function and size data. -/
theorem thetaRunOnPage {D : D7} {T : Top D} (h : LawsP T) (hinj : Function.Injective D.what₂.OtoLL)
    (EX : ErrX D) (p j : ℕ) (hj : InR D j) (L : SizeData₂ D) (CL Cq : ℝ) (H : KHyp)
    (C2 A2 CT : ℝ) (ka wL wF : WeightFamilies.Wt D j) (Tn nP nW : ℕ) (h0 : ℝ)
    (hn : InputsNet L (recPlus h j hj) (kR CL) H 1 4 Cq 4 C2 A2 7 CT
      (scalOfP (recB h.toLawsCore) hinj EX p ka wL wF Tn) ka wL wF Tn nP nW h0 (nusR h j wL)) :
    ∃ (n : SecNorm (recB h.toLawsCore)) (CRm : ℝ)
      (G : GlobalFamilyData (recPlusN h j hj n) ka wL wF) (Qf : ∀ la, LocalPointData G la),
      ThetaAllowance Qf (scalOfP n.base hinj EX p ka wL wF Tn) Tn CRm (cc D L C2 A2 7 wL) (nusR h j wL)
        ((recPJ h j hj).rk ka ((recB h.toLawsCore).Mlat j ka) * D.R.f * D.R.m * L.sc.b * L.de2) ∧
      ∀ la e, thetaExcess (recPlusN h j hj n) (scalOfP n.base hinj EX p ka wL wF Tn) ka wL wF Tn la e =
        thetaExcess (recPJ h j hj) (scalOfP (recB h.toLawsCore) hinj EX p ka wL wF Tn) ka wL wF Tn la e := by
  obtain ⟨n, G, Qf, hQ⟩ := thetaWitnessOfNet (fun j h1 h2 => recPlus h j ⟨h1, h2⟩) j hj.1 hj.2 L CL H
    Cq C2 A2 CT _ ka wL wF Tn nP nW h0 _ hn
  refine ⟨n, (k4 L CL).CRm, G, Qf, ?_, fun _ _ => rfl⟩
  rw [scalOfP_base]
  exact hQ


/-- Use the original numerical threshold and finite-net hypotheses for every row. -/
theorem exists_theta_run : ∃ x₀ : ℝ → ℝ → ℝ, ∀ (D : D7) (T : Top D) (h : LawsP T)
    (hinj : Function.Injective D.what₂.OtoLL) (EX : ErrX D) (p : ℕ), (∀ j, InR D j → ParOK T EX p j) →
    ∀ (j : ℕ) (hj : InR D j) (L : SizeData₂ D) (H : KHyp) (C2 A2 CT : ℝ) (ka wL wF : WeightFamilies.Wt D j)
      (Tn nP nW : ℕ) (h0 : ℝ), PageRun L (recPJ h j hj) H C2 A2 CT ka wL wF Tn nP nW h0 → x₀ H.CA H.CK ≤ L.sc.x →
    ∃ (n : SecNorm (recB h.toLawsCore)) (CRm : ℝ)
      (G : GlobalFamilyData (recPlusN h j hj n) ka wL wF) (Qf : ∀ la, LocalPointData G la),
      ThetaAllowance Qf (scalOfP n.base hinj EX p ka wL wF Tn) Tn CRm (cc D L C2 A2 7 wL) (nusR h j wL)
        ((recPJ h j hj).rk ka ((recB h.toLawsCore).Mlat j ka) * D.R.f * D.R.m * L.sc.b * L.de2) ∧
      ∀ la e, thetaExcess (recPlusN h j hj n) (scalOfP n.base hinj EX p ka wL wF Tn) ka wL wF Tn la e =
        thetaExcess (recPJ h j hj) (scalOfP (recB h.toLawsCore) hinj EX p ka wL wF Tn) ka wL wF Tn la e := by
  obtain ⟨CL, Cq, Z₀, hrec⟩ := GlobalTheory.T.exists_indexBoundHypothesesWithNet_allValuedPoints
  obtain ⟨x₀, hx⟩ := GlobalTheory.T.runNumericalConditions_of_indexBound_beyond_threshold Z₀
  refine ⟨x₀, fun D T h hinj EX p hpar j hj large₂ H C2 A2 CT ka wL wF Tn nP nW h0 hrun hx0 => ?_⟩
  obtain ⟨hok, hZ⟩ := hx D _ _ j _ large₂ H C2 A2 CT ka wL wF Tn nP nW h0 hj hrun hx0
  obtain ⟨hn, -⟩ := hrec D T h hinj EX p j hj large₂ H C2 A2 CT ka wL wF Tn nP nW h0 (hpar j hj) hok hZ
  exact thetaRunOnPage h hinj EX p j hj large₂ CL (Cq H.CA H.CK) H C2 A2 CT ka wL wF Tn nP nW h0 hn

end GlobalTheory.FinalJoin

#print axioms GlobalTheory.FinalJoin.exists_theta_run
