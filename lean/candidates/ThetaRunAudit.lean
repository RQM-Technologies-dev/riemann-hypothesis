import ThetaRunSelectors
import FamilyAuditCounts

open Lean FamilyAudit
open Formalism.MainNotions.Gaps.EtaleWeightGaps

run_cmd
  let reached := reach (← getEnv) [``GlobalTheory.BigOn.CoreWit.exists_two_run_depth] {}
  for expected in [``thetaFamilyWitness, ``localThetaBudget, ``sumC] do
    unless reached.contains expected do throwError m!"Missing arithmetic dependency {expected}"
  for bypassed in [``theorem_zero_of_named_inputs, ``GlobalTheory.FinalJoin.runHolds_of_parOK] do
    if reached.contains bypassed then throwError m!"Unexpected legacy run dependency {bypassed}"
  logInfo "Both run selectors reach the direct family bound and its weighted sum."
