# Following one remainder through the arithmetic argument

Take a finite place $w$ of the base number field $K_0$, full lattices $N\subseteq M$, and an integral scalar $a_0$. In the completed space, set

$$D_w=\operatorname{length}\big((a_0\widehat M+\widehat N)/\widehat N\big).$$

Suppose $D_w$ is finite and $D_w\le r(w)$. The local transport result keeps this particular function $r$. At a place $v$ over $w$ with ramification index $h_v$, it gives

$$\operatorname{length}_v\big((a M_K+T)/T\big)\le h_v\,r(w).$$

Here $M_K$ is the extended lattice, the coordinate embedding preserves independent families and spans the target, $N_K\subseteq T\subseteq M_K$ is a full lattice, and $v(a)\ge h_v w(a_0)$. All lengths use their own ring’s units. For instance, a factor of length three at the base has length six after a totally ramified quadratic extension. Forgetting the factor two would already fail for a rank-one lattice.

## Why the transport works

1. Completion carries $a_0 M+N$ to $a_0\widehat M+\widehat N$. Applying the upstream localization-to-completion comparison to this numerator and denominator, in the whole ambient space, bounds their localized quotient length by $D_w$. Finiteness matters when Lean converts extended naturals to naturals. [ScalarCompletion.lean](../lean/ScalarCompletion.lean)
2. Put $C=M\cap a_0^{-1}N$. Multiplication by $a_0$ identifies $M/C$ with $(a_0 M+N)/N$. Under extension of number fields, the signed local index of $(M,C)$ multiplies by $h_v$. The extended $C$ lies inside $M_K\cap a_0^{-1}N_K$. Increasing the valuation to $v(a)$ and enlarging $N_K$ to $T$ only decrease the remaining length. This uses the scalar identity and lattice monotonicity. [ScalarDepth.lean](../lean/ScalarDepth.lean) · [ScalarRamification.lean](../lean/ScalarRamification.lean) · [composed statement](../lean/ScalarPassage.lean)
3. Write $\ell_K(v)=\log N(v)/[K:\mathbb Q]$. For each base place, $\sum_{v\mid w}e_v f_v=[K:K_0]$. Thus $\sum_{v\mid w}\ell_K(v)e_v=\ell_{K_0}(w)$. For a finite subset upstairs and a nonnegative remainder, the weighted sum can only decrease. Upstream lemma `l4` proves the finite-subset inequality against the summable base series. [Pinned transport source](https://github.com/leanprover-community/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/WeightParameterMemUnitInterval.lean#L964)

## The two runs

The row object stores two remainder functions. At the distinguished rational place it selects the second. Elsewhere it selects the first. The theorem `paired_scalar` checks this selection at each place and its conjugate in the original `AtPair` window. It proves the exact scalar input `LatticeIndexBoundAtPairs O true`, including the two original finite-sum budgets. Its hypotheses identify each stored function pointwise with its transported witness and supply the local scalar estimate for the selected run. The budget is applied separately to each run. [Row assembly](../lean/ScalarRamification.lean)

The composed theorem `paired_of_completed` goes one step further. Its local input is a completed quotient bound for the selected base lattice, together with the embedding, depth, and lattice containments. It derives the ramified inequality and produces the exact input accepted by `on_core_excess`. Lean reports only `propext`, `Classical.choice`, and `Quot.sound` for this theorem. The caller still supplies the two base functions and their pointwise identification with the row object. [Composed theorem](../lean/ScalarPassage.lean)

## What remains open in the submitted family

- **Geometric producer.** The candidate applies `levelsExcessDesc` to the actual local lattices `T0.MW` and `T0.ThW`, using the original depth, four loss terms, and `rLa`. It is a draft. Its owning geometric module and this specialization still need a successful replay. The completed bound must also be identified with the cusp-lattice quotient for an integral scalar at the prescribed valuation. The [ambient-image lemmas](../lean/ScalarAmbient.lean) handle injective coordinate maps and associated scalars. [Geometric candidate](../lean/candidates/ThetaScalar.lean)
- **Both arithmetic branches.** The interior construction supplies a family of local points and sums its explicit `rLa`. The terminal index invokes a separate `ConclAtM` construction. A direct scalar conclusion and the corresponding weighted witness are needed through each branch. [Interior and terminal split](https://github.com/leanprover-community/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/TheoremZeroOfRefinedInputs.lean#L11) · [Terminal construction](https://github.com/leanprover-community/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/TheoremZeroOfInputs.lean#L47)
- **Witness choice.** The concrete constructor chooses two functions from an existential statement quantified over every subspace. The abstract `TheoremZeroData.r_le` and `r_ok` also use that contract. To remove the detour one must construct the row data from the scalar witnesses or establish the required pointwise comparisons independently. Equal aggregate budgets do not imply equal values at a given place. [Concrete two-run choice](https://github.com/leanprover-community/riemann-hypothesis/blob/712a6aef8fe265fb6f3a5fa1f3101a017aec8fe9/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasIndexBoundOfRuns.lean#L176)
- **Final replay.** The patched arithmetic family has no end-to-end replay. A direct invocation of the original `Main.lean` in the targeted environment stopped at its missing `Statements.olean` import. It never reached the RH theorem. Even a successful replay of the untouched original entry point would leave the replacement dependency to be checked.

## Reproduce the targeted experiment

Apply the [direct projector patch and toolchain instructions](../direct-projector-replay.md) to the pinned source. Then run the following command from this repository with the patched project as the argument.

```sh
python3 lean/replay_transport.py /path/to/patched/upstream
```

The small replay selects complete definitions and proofs from two checksum-verified upstream files, including the proofs of the completion comparison, index ramification formula, and weighted sum. It compiles those declarations with their dependencies, checks the RQM modules, and runs Lean’s independent kernel checker on the new modules. The ordinary source files import the upstream owning module. The targeted driver substitutes the extracted import so the unrelated arithmetic interfaces need not be rebuilt. The candidate geometric file and the global entry point are outside this target.
