open Lean GlobalTheory.OnAtPlacesBase
private partial def reach (env : Environment) (todo : List Name) (seen : NameSet) : NameSet := Id.run do
  match todo with
  | [] => return seen
  | n :: rest =>
    if seen.contains n then return reach env rest seen
    let some ci := env.find? n | return reach env rest (seen.insert n)
    let deps := ci.getUsedConstantsAsSet.toList.filter fun k =>
      [`Formalism, `Development, `GlobalTheory].any (·.isPrefixOf k) ||
        ["_private.Formalism.", "_private.Development.", "_private.GlobalTheory."].any (fun pre : String => k.toString.startsWith pre)
    return reach env (deps ++ rest) (seen.insert n)

/-- Count type and body nodes separately, sharing common subexpressions within each. -/
private def termSize (env : Environment) (names : List Name) : Elab.Command.CommandElabM Nat := do
  let mut count := 0
  for n in names do
    let some ci := env.find? n | throwError m!"Missing declaration {n}"
    count := count + (← (ShareCommon.shareCommon' ci.type).numObjs)
    if let some body := ci.value? true then
      count := count + (← (ShareCommon.shareCommon' body).numObjs)
  return count

run_cmd
  let env ← getEnv
  let original := reach env [``on_of_has_atPlaces] {}
  logInfo m!"Baseline declarations {original.toList.length}, type/body nodes {← termSize env original.toList}."

#print axioms on_of_depth_atPlaces
run_cmd
  let env ← getEnv
  let baseline := reach env [``on_of_has_atPlaces] {}
  let trial := reach env [``on_of_depth_atPlaces] {}
  let detour := ``Formalism.EigenvalueLevelCeiling.threeForms_of
  unless baseline.contains detour && trial.contains detour do throwError "Missing subspace-to-depth dependency"
  unless trial.contains ``Formalism.L2.Indef.Tree.depth_of_run_bounds &&
      trial.contains ``Formalism.L2.Indef.Tree.on_core_excess do throwError "Missing experimental path"
  let removed := baseline.toList.filter fun n => !trial.contains n
  let added := trial.toList.filter fun n => !baseline.contains n
  logInfo m!"consumer dependencies: original {baseline.toList.length}, adapted {trial.toList.length}, removed {removed.length}, added {added.length}"
  let before ← termSize env removed
  let after ← termSize env added
  logInfo m!"Exclusive declaration type/body expression nodes: original {before}, adapted {after}."
  logInfo m!"Adapted type/body nodes {← termSize env trial.toList}."
