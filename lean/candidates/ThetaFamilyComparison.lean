import ThetaFamilyProducer

noncomputable section
open Formalism.MainNotions.WeightAlgebra Formalism.BasicNotions NumberField IsDedekindDomain Module
namespace Formalism.MainNotions.Gaps.EtaleWeightGaps
variable {D : D7} {B : WeightFamilies.Prov D} {P : ModuliIntegralCharts.Prov D}

theorem concl_via_family_depth : Conclusion1OfComb (D := D) (B := B) (P := P) := by
  intro large₂ X K H Ch Ah Cq Aq C2 A2 CR CT j h1 h2 S ka wL wF T nP nW h0 nus hH lA sA mA qA G Gc PH Prw Pet Pd Qf
    tW tTh tZ tQ tEt dH dS dL pG sRd sRho sRhoP hP iB iC iT iLf iZ iM hB hHt
  obtain ⟨hn, hs, hb, hl⟩ := thetaFamilyWitness large₂ X K H Ch Ah Cq Aq C2 A2 CR CT j h1 h2 S ka wL wF T
    nP nW h0 nus hH lA sA mA qA G Gc PH Prw Pet Pd Qf tW tTh tZ tQ tEt dH dS dL pG sRd sRho sRhoP
    hP iB iC iT iLf iZ iM hB hHt
  apply concl_of_nat _ _ _ _ _ _ _ _ _ hH.2.2.2.1.1 hn hs hb
  intro la e he V hV
  have hΘ := theta_le_msup_of_hypC (X j h1 h2) S hH
  have hLat := inLat_of (X j h1 h2) S ka wL wF T la lA hΘ (span_Thc_of_hypC hH).2.2
  letI := T0.finDim_of_isLat _ hLat.1
  apply qlen_of_idx _ _ _ _ _ _ _ hLat hΘ e _ _ V hV
  exact T0.subspace_bound_of_excess (K := (X j h1 h2).Kl la) (unif _ la)
    (unif_irreducible _ la) _ _ hLat.1 hLat.2 e _ (hl la e he).2

end Formalism.MainNotions.Gaps.EtaleWeightGaps
