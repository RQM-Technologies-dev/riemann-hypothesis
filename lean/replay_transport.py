"""Replay the scalar passage against selected, hash-pinned upstream declarations."""
import argparse
import hashlib
import os
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
OWNER = "Formalism.SharpRestriction.GenusPolyhedralBounds.RelativeIndexClassSets.WeightParameterMemUnitInterval"
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
    parser.add_argument("upstream", type=Path, help="Patched, pinned Lean project")
    root = parser.parse_args().upstream.resolve()
    core = pinned(root, OWNER, "e08fa8017b40fc9b07514b91304e38d11382d6586df6e13c15be9366a5470c19")
    weights = pinned(root, WEIGHT, "f9cd7b6481f0f48c1d914de7aa3cdb06e8d3548403e803d7f9a4d0e9a5b8e895")
    subprocess.run(["lake", "build", *[f"+{n}:olean" for n in (ROW, SPAN, FORMS, BASIS, VAL)]], cwd=root, check=True)
    lean_path = subprocess.check_output(["lake", "env", "printenv", "LEAN_PATH"], cwd=root, text=True).strip()
    with tempfile.TemporaryDirectory(prefix="scalar-passage-") as tmp:
        out = Path(tmp)
        env = dict(os.environ, LEAN_PATH=str(out) + os.pathsep + lean_path)
        def check(name, source):
            path = out / f"{name}.lean"
            path.write_text(source)
            subprocess.run(["lean", f"--root={out}", "-j", "2", "-DmaxSynthPendingDepth=3", "-DmaxHeartbeats=4000000",
                            "-o", str(out / f"{name}.olean"), str(path)], cwd=root, env=env, check=True)

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
        for name in ("ScalarDepth", "ScalarAmbient", "ScalarCompletion", "ScalarRamification", "ScalarPassage"):
            subprocess.run(["leanchecker", name], cwd=root, env=env, check=True)


if __name__ == "__main__":
    main()
