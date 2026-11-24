"""Replay the scalar passage against selected, hash-pinned upstream declarations."""
import argparse
import hashlib
import os
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
OWNER = "Formalism.SharpRestriction.GenusPolyhedralBounds.RelativeIndexClassSets.WeightParameterMemUnitInterval"
UNIFORMIZER = "Formalism.SharpRestriction.GenusPolyhedralBounds.RelativeIndexClassSets.ExistsIrreducibleLocToCompl"
WEIGHT = "Formalism.LocalRingCardinality.DataArith"
ROW = "Formalism.LocalToGlobal.IndefiniteForms.IndefiniteTree.ExampleSatisfiesConditionsAtFive"
SPAN = "Formalism.SharpRestriction.GenusPolyhedralBounds.RelativeIndexClassSets.LengthLeOfSemilinear"
FORMS = "Formalism.MirabolicMackeyTheory.MirabolicMackeyProofs.ThreeForms"
BASIS = "Development.AutomorphicArithmetic.IntegralCasts.CapelliIdentities.ExistsBasisOfPid"
VAL = "Formalism.PeriodIntegrals.UnitaryGroupMassFormula.LatticeIndexDeterminant.NegLogValuation"


def pinned(root, name, digest):
    path = (root / "src").joinpath(*name.split(".")).with_suffix(".lean")
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != digest:
        raise ValueError(f"Source checksum mismatch for {path}")
    return data.decode().splitlines(keepends=True)


def slices(lines, ranges):
    return "".join("".join(lines[start-1:end]) for start, end in ranges)


def imports(*names):
    return "".join(f"import {name}\n" for name in names)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("upstream", type=Path, help="Pinned Lean project (pristine for --family-original)")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--family-original", action="store_true",
                       help="Measure the original family theorem in a pristine upstream checkout")
    modes.add_argument("--family-depth", action="store_true",
                       help="Replay the direct family and two-run theorems and measure the family step")
    modes.add_argument("--family", action="store_true",
                        help="Check the arithmetic candidates with their full upstream modules")
    args = parser.parse_args()
    root = args.upstream.resolve()
    core = pinned(root, OWNER, "e08fa8017b40fc9b07514b91304e38d11382d6586df6e13c15be9366a5470c19")
    weights = pinned(root, WEIGHT, "f9cd7b6481f0f48c1d914de7aa3cdb06e8d3548403e803d7f9a4d0e9a5b8e895")
    uniformizer = pinned(root, UNIFORMIZER, "98378281e1788079559d151c5b5d3c439b181021277d8d9cc7e587e7ac43e58a")
    targets = [ROW, SPAN, FORMS, BASIS, VAL]
    if args.family or args.family_depth:
        targets.extend([OWNER, UNIFORMIZER,
                        "Formalism.SharpRestriction.GenusPolyhedralBounds.RelativeIndexClassSets.TheoremZeroBundledOfLift",
                        "Development.AbelianVarietyTheory.Proofs.HeightProofs.ExistsThresholdRunHolds",
                        "Development.AbelianVarietyTheory.Definitions.Divisors.IsDeltaDelAtOwnAt",
                        "Development.AbelianVarietyTheory.Proofs.HeightProofs.ExistsPageRunRecordSubFour",
                        "Development.AbelianVarietyTheory.Proofs.HeightProofs.FieldSmallIffOpo"])
    if args.family_original:
        targets = ["Formalism.SharpRestriction.GenusPolyhedralBounds.RelativeIndexClassSets.TheoremZeroBundledOfLift"]
    subprocess.run(["lake", "build", *[f"+{n}:olean" for n in targets]], cwd=root, check=True)
    lean_path = subprocess.check_output(["lake", "env", "printenv", "LEAN_PATH"], cwd=root, text=True).strip()
    with tempfile.TemporaryDirectory(prefix="scalar-passage-") as tmp:
        out = Path(tmp)
        env = dict(os.environ, LEAN_PATH=str(out) + os.pathsep + lean_path)
        def check(name, source):
            path = out / f"{name}.lean"
            path.write_text(source)
            subprocess.run(["lean", f"--root={out}", "-j", "2", "-DmaxSynthPendingDepth=3", "-DmaxHeartbeats=4000000",
                            "-o", str(out / f"{name}.olean"), str(path)], cwd=root, env=env, check=True)

        if args.family_original:
            for name in ("FamilyAuditCounts", "OriginalFamilyAudit"):
                check(name, (HERE / "candidates" / f"{name}.lean").read_text())
            return
        if args.family or args.family_depth:
            sources = []
            if args.family:
                sources.extend(["ScalarDepth", "ScalarAmbient", "ScalarCompletion", "ScalarRamification",
                                "ScalarPassage", "ThetaDepth", "ThetaCoordinates", "ThetaRowInput",
                                "ThetaWitnessRows"])
            sources.extend(["candidates/ThetaScalar", "candidates/ThetaFamilyProducer",
                            "candidates/ThetaChosenInputs", "candidates/ThetaRunSelectors",
                            "candidates/ThetaFamilyComparison", "candidates/FamilyAuditCounts",
                            "candidates/OriginalFamilyAudit", "candidates/ThetaFamilyAudit", "candidates/ThetaRunAudit"])
            if args.family:
                sources.append("candidates/ThetaFamilyWitness")
            for source in sources:
                path = HERE / (source + ".lean")
                check(path.stem, path.read_text())
                subprocess.run(["leanchecker", "-v", path.stem], cwd=root, env=env, check=True)
            return

        check("ScalarDepth", (HERE / "ScalarDepth.lean").read_text())
        check("ScalarAmbient", (HERE / "ScalarAmbient.lean").read_text())
        check("CompletionFacts", imports(ROW, FORMS, SPAN, BASIS) +
              "open Module NumberField IsDedekindDomain\nnoncomputable section\nnamespace Formalism.BasicNotions\n" +
              slices(weights, [(37, 40)]) + "end Formalism.BasicNotions\nend\n" + slices(core, [(123, 649)]))
        check("RamUnifiedFacts", imports("CompletionFacts", "ScalarDepth", VAL) +
              slices(core, [(726, 1004), (1144, 1155), (1178, 1206), (1282, 1288)]))
        for name, owner in [("ScalarCompletion", "CompletionFacts"), ("ScalarRamification", "RamUnifiedFacts")]:
            source = (HERE / f"{name}.lean").read_text()
            check(name, source.replace("import " + OWNER + "\n", "import " + owner + "\n"))
        check("ScalarPassage", (HERE / "ScalarPassage.lean").read_text())
        check("UniformizerFacts", imports("Mathlib") + "noncomputable section\nopen Module NumberField IsDedekindDomain\n" +
              "namespace Formalism.MainNotions.Gaps.EtaleWeightGaps\n" + slices(uniformizer, [(12, 24), (49, 94)]) +
              "end Formalism.MainNotions.Gaps.EtaleWeightGaps\n")
        depth = (HERE / "ThetaDepth.lean").read_text().replace("import " + UNIFORMIZER + "\n", "import UniformizerFacts\n")
        check("ThetaDepth", depth)
        for name in ("ThetaCoordinates", "ThetaRowInput", "ThetaWitnessRows"):
            check(name, (HERE / f"{name}.lean").read_text())
        for name in ("ThetaDepth", "ThetaCoordinates", "ThetaRowInput", "ThetaWitnessRows", "ScalarDepth", "ScalarAmbient", "ScalarCompletion", "ScalarRamification", "ScalarPassage"):
            subprocess.run(["leanchecker", "-v", name], cwd=root, env=env, check=True)


if __name__ == "__main__":
    main()
