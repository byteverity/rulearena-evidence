# Protocol

The order of operations, as executed on 2026-10-05/06.

1. **Render model-visible inputs.** `prepare.py` wrote each problem exactly as RuleArena's harness presents it, plus the
   rule text, into `inputs/`. Tax forms use the harness's own template logic.
2. **Seal.** Everything else was moved into a locked directory, unreadable from the model's sandbox (hashes in
   `SEAL.sha256`): the answers, the structured problem data (`info` / `pydantic`), the reference `compute_answer`, the fee
   CSVs and the scorer. The seal was verified intact at unsealing.
3. **Build.** Per domain, two independent offline sandboxes (A, B) each built a solver from the rule text alone:
   - deterministic extraction;
   - rule tables as synthesa-decide oracles;
   - a trace of applied rule clauses;
   - an interpretations log (`../interpretations/`).
4. **Gate, every round.** Every residual was computed without labels:
   - RUN: every problem answered;
   - EXTRACTION: every fact number consumed, every value anchored to its exact span (canonical match: Yes~True, $ and
     thousands separators);
   - COVERAGE: every rule clause mapped to code or justified as not applicable;
   - TABLES: oracles compile complete and contradiction-free, re-verify offline, and contain every rule-table amount;
   - METAMORPHIC: relations written by the verifier's author from the rule text. Airline: ticket +$137 → total +$137;
     removing, lightening or shrinking an item never raises the total. Tax: withholding or estimated payment +$100 → answer
     −$100; a name change → no change. NBA: swapping team labels maps the answer; swapping player labels leaves it unchanged;
   - N-VERSION: disagreement with the other build, located to the first divergent line, step or (operation, team) verdict,
     without revealing the other build's answer.
5. **Prove the gate rejects.** Deliberately broken solvers were run through the gate: 9 of 9 rejected (airline: doubled
   ticket, dropped overweight fee, +$10 offset; tax: uncredited withholding, $50 error on joint filers, rounding to
   dollars; NBA: always False, wrong team, flagging a legal operation).
6. **Admit.** A sealed admission decision table (synthesa-decide) returned: airline `admit`, tax `admit`, NBA
   `admit_with_disclosed_disagreement` (210 of 216 agree).
7. **Freeze and score once.** Fresh base runs of both builds were written and hashed (`../ANSWERS.sha256`), and the plan
   was written (`../PREREGISTRATION.md`, primary = A). The seal was then opened and all 816 problems scored once.
8. **Post-hoc, labelled.** The airline misses were diagnosed as bag ordering. The customer-favourable policy was frozen
   (`../policy/`), then evaluated once on 300 fresh problems generated with new seeds, pre-registered
   (`../policy/PREREGISTRATION_FRESH.md`).
