import Lean
open Lean
namespace FamilyAudit
partial def reach (env : Environment) (todo : List Name) (seen : NameSet) : NameSet := Id.run do
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
def termSize (env : Environment) (names : List Name) : Elab.Command.CommandElabM Nat := do
  let mut count := 0
  for n in names do
    let some ci := env.find? n | throwError m!"Missing declaration {n}"
    count := count + (← (ShareCommon.shareCommon' ci.type).numObjs)
    if let some body := ci.value? true then
      count := count + (← (ShareCommon.shareCommon' body).numObjs)
  return count

end FamilyAudit
