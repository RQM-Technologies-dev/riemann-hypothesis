import ThetaFamilyComparison
import FamilyAuditCounts
open Lean FamilyAudit

run_cmd
  let env ← getEnv
  let deps := reach env [``Formalism.MainNotions.Gaps.EtaleWeightGaps.concl_via_family_depth] {}
  logInfo m!"Replacement family dependencies {deps.toList.length}, nodes {← termSize env deps.toList}"
run_cmd
  let names := (reach (← getEnv) [``Formalism.MainNotions.Gaps.EtaleWeightGaps.thetaFamilyWitness] {}).toList
  for leaf in ["levelsExcessDesc", "sumC", "index_last_reduction_holds", "localIdx", "qlen_of_idx", "localBound", "threeForms_of", "theorem_zero_of_named_inputs"] do
    let hits := names.filter fun n => n.toString.endsWith ("." ++ leaf)
    logInfo m!"thetaFamilyWitness reaches {leaf}: {!hits.isEmpty}"
