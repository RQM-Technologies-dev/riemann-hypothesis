"""Compare the original and depth-based consumers of the concrete two-run output."""
import argparse
import os
from pathlib import Path
import subprocess
import tempfile

from replay_transport import ROW, pinned

HERE = Path(__file__).resolve().parent
PREFIX = "Development.AbelianVarietyTheory."
RANK = PREFIX + "Proofs.FoundationProofs.TraceLatticeLeThetaLatticeAtPlace"
BOUNDS = PREFIX + "Definitions.Divisors.RealisedChainTorusEq"
CALLER = PREFIX + "Proofs.DivisorProofs.TwistedPlacesBoundChainTwoRunChain"


def section(text, start, end):
    return text[text.index(start):text.index(end, text.index(start))]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Full upstream source tree containing src/")
    parser.add_argument("build", type=Path, help="Build tree with the direct projector patch applied")
    parser.add_argument("--original", action="store_true", help="Measure the caller with the unpatched upstream build")
    args = parser.parse_args()
    if args.original:
        row_file = Path("src", *ROW.split(".")).with_suffix(".lean")
        if (args.build / row_file).read_bytes() != (args.source / row_file).read_bytes():
            parser.error("--original requires the original upstream row source in the build directory")
    rank = "".join(pinned(args.source, RANK, "f0df802df2caa1225f05127c69479559e39d809e0910207560cdc6bd2cfb5ffe"))
    bounds = "".join(pinned(args.source, BOUNDS, "d88e0ca6406550550d8274c8762632350d31ffec2953a15c679f9b8fc81dfa8a"))
    caller = "".join(pinned(args.source, CALLER, "864a2038d66397f65fae08885a191b543116914b914eb0f7ea6c22c7b1ab1707"))
    rank_body = section(rank, "section Place", "end Place")
    rank_direct = section(rank_body, "theorem on_core_atPlaces", "hCE tE1\n") + "hCE tE1\n"
    rank_direct = rank_direct.replace("theorem on_core_atPlaces", "theorem on_depth_atPlaces").replace(
        "  on_core N", "  on_core_excess N").replace("hSp hS hT0 hD", "hSp hS (depth_of_run_bounds O hSup hS hT0) hD")
    leaves = section(bounds, "section Leaves", "end Leaves")
    free = section(caller, "section Free", "end Free")
    direct = section(free, "theorem on_of_has_atPlaces", "hCE tE1⟩") + "hCE tE1⟩\n"
    direct = direct.replace("theorem on_of_has_atPlaces", "theorem on_of_depth_atPlaces").replace(
        "TraceClassRank.on_core_atPlaces", "TraceClassRank.on_depth_atPlaces")
    audit = (HERE / "TwoRunAudit.inc").read_text()
    imports = "import TwoRunDepth\n"
    if args.original:
        imports = "import Formalism.LocalToGlobal.IndefiniteForms.IndefiniteTree.ExampleSatisfiesConditionsAtFive\n"
        rank_direct = direct = ""
        audit = audit.split("#print axioms on_of_depth_atPlaces", 1)[0]
    source = (
        imports + "noncomputable section\n"
        "open Module NumberField IsDedekindDomain Formalism.L2.Indef Formalism.L2.Indef.Tree\n"
        "open Formalism.HermitianLatticesTheory (localization₂)\n"
        "namespace GlobalTheory.TraceClassRank\n" + rank_body + rank_direct + "end Place\nend GlobalTheory.TraceClassRank\n"
        "namespace GlobalTheory.BigOn\n" + leaves + "end Leaves\nend GlobalTheory.BigOn\n"
        "namespace GlobalTheory.OnAtPlacesBase\nopen GlobalTheory.BigOn\n" + free + direct +
        "end Free\nend GlobalTheory.OnAtPlacesBase\nend\n" + audit
    )
    root = args.build.resolve()
    lean_path = subprocess.check_output(["lake", "env", "printenv", "LEAN_PATH"], cwd=root, text=True).strip()
    with tempfile.TemporaryDirectory(prefix="two-run-depth-") as tmp:
        env = dict(os.environ, LEAN_PATH=tmp + os.pathsep + lean_path)
        modules = {"TwoRunConsumer": source} if args.original else {
            "TwoRunDepth": (HERE / "TwoRunDepth.lean").read_text(), "TwoRunConsumer": source}
        for name, content in modules.items():
            path = Path(tmp) / (name + ".lean")
            path.write_text(content)
            subprocess.run(["lean", "--root=" + tmp, "-DmaxHeartbeats=4000000", "-o", str(path.with_suffix(".olean")),
                            str(path)], cwd=root, env=env, check=True)
        for name in modules:
            subprocess.run(["leanchecker", "-v", name], cwd=root, env=dict(env, LEAN_NUM_THREADS="1"), check=True)


if __name__ == "__main__":
    main()
