# Reading the Riemann Hypothesis proof with quaternions

RQM Technologies is studying Levent Alpöge’s announced Lean proof and testing whether quaternionic algebra can shorten part of its arithmetic argument. This repository is a reader’s guide and a place to reproduce those tests. Alpöge describes the original work and credits Claude in his [November 20 announcement](https://alpo.ge/remark.pdf). The exact theorem we are reading is in the [pinned Lean source](https://github.com/leanprover-community/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Main.lean).

**Research status · November 20, 2026.** What would count as a shorter proof? A replacement must take the same arithmetic inputs, prove the same estimate at the same places and depths, and let Lean replay the final theorem after a dependency has been removed. Lean checks a direct local route from a bound on the surviving lattice length to a projected row. The experimental patch adds 492 lines and removes 139 across ten upstream files. Its saving so far is one local proof dependency. A shorter end-to-end proof and a saving specific to quaternions remain open.

## Start with a picture

![Two lattices with determinant valuation four. At depths zero through four the first has remaining lengths 4, 3, 2, 1, 0 and the second has 4, 2, 0, 0, 0.](docs/figures/scalar-depth.gif)

Imagine two accounts holding four units apiece. In A all four units sit in one column. In B there are two columns of two. Each multiplication by the local prime removes one unit from every nonempty column. After two rounds, A still has two units and B has none. The determinant records the starting total. A row of a theta lift can see the difference that survives at a particular depth.

The research question is whether we can **carry that surviving length directly to the row**. The animation is an exact finite lattice example. The global proof needs an estimate for a whole family of such lattices simultaneously.

| If you want to… | Start here |
| --- | --- |
| Understand how a question about primes leads to zeros, theta lifts, and local lattices | [A visual reading guide](docs/reading-the-proof.md) |
| See what conjugate places have to do with quaternions | [The animated Gaussian-integer example](docs/reading-the-proof.md#what-quaternions-combine) |
| Inspect the proposed shortening in ordinary mathematics | [Quaternionic descent and the scalar remainder](quaternionic-descent.md) |
| Reproduce the Lean checks and see their scope | [Direct projector replay](direct-projector-replay.md) and [scalar transport](docs/scalar-transport.md) |
| Explore RQM’s earlier independent work on zero-spheres, theta kernels, and prime sums | [Earlier research index](RESEARCH-INDEX.md) |

The visual examples can be regenerated with Python and Pillow using `python3 experiments/render_proof_figures.py`.
