# Post-hoc policy + fresh-problem evaluation — pre-registered before generating or scoring

- Policy (frozen, sha256 in policy/POLICY.sha256): "where the rule text leaves an assignment unpinned and it changes the
  customer's cost, resolve it in the customer's favour (contra proferentem) by exact bounded search". Adopted AFTER seeing
  official airline errors → every number on the official set using it is labelled POST-HOC / LABEL-INFORMED.
- Solver: airline solver A, unchanged (frozen answers final/airline_A.jsonl; solver code as at the one-shot score).
- Fresh set: 300 NEW airline problems (100 per level) from RuleArena's own airline/gen_questions.py with seeds
  20261006000 + i (random and numpy.random), rendered exactly as the harness does; gold from the reference compute_answer.
  Never seen by anyone before scoring. Scored ONCE.
- Report: fresh-set accuracy for (a) solver A as scored (listed order) and (b) solver A + policy. PRIMARY = (b).
- No further changes after the fresh score; any later change is a new labelled run.
