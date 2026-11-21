import ThetaScalar
import ThetaRowInput
import ThetaWitnessRows
import Formalism.SharpRestriction.GenusPolyhedralBounds.RelativeIndexClassSets.TheoremZeroBundledOfLift

/- Arithmetic specialization against the pinned theta-family definitions.
See docs/theta-witnesses.md for the checked targets and the replay boundary. -/
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

/-- Use the scalar bound on the original model, allowing the allowance to come
from points on a norm-adjusted model with the same scalar length. -/
theorem rowOfFamily {j : ℕ} {X : PJ D B P j} {ka wL wF : WeightFamilies.Wt D j}
    (S : Scal B) (T e : ℕ) (r : ℝ)
    {K : Type} [Field K] [NumberField K] [StarRing K] [StarRing B.KO] [Algebra B.KO K]
    (v : HeightOneSpectrum (𝓞 K)) {n : ℕ}
    (ι : B.Cusp j ka →ₗ[B.KO] (Fin n → K))
    (hind : ∀ (m : ℕ) (b : Fin m → B.Cusp j ka), LinearIndependent B.KO b → LinearIndependent K fun i => ι (b i))
    (htop : Submodule.span K (Set.range ι) = ⊤)
    (hM : Submodule.IsLattice B.KO (B.Mlat j ka)) (hΘ : X.Theta S ka wL wF T ≤ X.Msup ka)
    (hspan : Submodule.span B.KO (X.Thc S.sK ka : Set (B.Cusp j ka)) = ⊤)
    (L : Submodule (𝓞 K) (Fin n → K)) (hL : IsLatIn ⊤ L)
    (htie : L = up ι ((X.Theta S ka wL wF T).comap ((X.inc ka).restrictScalars (𝓞 B.KO))))
    (a : K) (ha : a ≠ 0)
    (hdepth : (v.asIdeal.ramificationIdx (𝓞 B.KO) : ℤ) * e ≤ vw v a)
    (hbound : ((thetaExcess X S ka wL wF T (v.under (𝓞 B.KO)) e).toNat : ℝ) ≤ r) :
    CompletedRow B.KO v (up ι (B.Mlat j ka)) L a r := by
  let N := (B.Mlat j ka) ⊓ (X.Theta S ka wL wF T).comap ((X.inc ka).restrictScalars (𝓞 B.KO))
  have hpre := preimage_le_of_theta_image ((X.inc ka).restrictScalars (𝓞 B.KO)) (X.inc_inj ka) (B.Mlat j ka) _ hΘ
  have hNL : up ι N ≤ L := by rw [htie]; exact Submodule.span_mono (Set.image_mono inf_le_right)
  have hLM : L ≤ up ι (B.Mlat j ka) := by rw [htie]; exact Submodule.span_mono (Set.image_mono hpre)
  have hN : IsLatIn ⊤ N := by
    refine ⟨hM.fg.of_le (show N ≤ B.Mlat j ka from inf_le_left), top_unique ?_⟩
    rw [← hspan]
    apply Submodule.span_mono
    intro x hx
    have ht : X.inc ka x ∈ X.Theta S ka wL wF T :=
      (show X.emb ka (X.Thc S.sK ka) ≤ X.Theta S ka wL wF T from le_sup_right) ⟨x, hx, rfl⟩
    exact ⟨hpre ht, ht⟩
  exact row_of_theta_length ι hind htop (X.inc ka) (X.inc_inj ka) (B.Mlat j ka) _ hΘ
    ⟨hM.fg, hM.span_eq_top⟩ hN L hL hNL hLM v e a ha hdepth r
    (unif X _) (unif_irreducible X _) ⟨thetaExcess_finite _ _ _ _ _ _ _ _ hM hΘ hspan, hbound⟩

end Formalism.MainNotions.Gaps.EtaleWeightGaps

#print axioms Formalism.MainNotions.Gaps.EtaleWeightGaps.thetaFamilyWitness
#print axioms Formalism.MainNotions.Gaps.EtaleWeightGaps.paired_of_theta_points
