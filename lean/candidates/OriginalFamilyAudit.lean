import Formalism.SharpRestriction.GenusPolyhedralBounds.RelativeIndexClassSets.TheoremZeroBundledOfLift
import FamilyAuditCounts
open Lean FamilyAudit

run_cmd
  let env ← getEnv
  let deps := reach env [``Formalism.MainNotions.Gaps.EtaleWeightGaps.theorem_zero_of_named_inputs] {}
  logInfo m!"Original family dependencies {deps.toList.length}, nodes {← termSize env deps.toList}"
