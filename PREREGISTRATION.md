# RuleArena — pre-registered scoring (written before unsealing)

- Scored once, all 816 problems (airline 300, tax 300, NBA 216), RuleArena's own correctness rule per domain:
  airline `value == fee` (compute_answer), tax `np.isclose(value, answer)` (owed > 0 / overpaid < 0 convention),
  NBA exact target string ("Answer: False." / "Answer: True. Illegal Operation: X. Problematic Team: Y.").
- PRIMARY number: solver A (fixed before unsealing — not chosen after seeing scores).
- Also reported: solver B; and accuracy on the A∩B-agreement subset vs the disagreement subset.
- Inputs: final/{airline,tax,nba}_{A,B}.jsonl, frozen by sha256 in final/ANSWERS.sha256 before unsealing.
- Disclosed: NBA did not reach full agreement (210/216 after 12 rounds) → admission = admit_with_disclosed_disagreement.
- After scoring, nothing is re-tuned and re-scored; any later change is a new, separately labelled run.
- Firewall: no answers, structured info, reference implementation or scorer were read or used during development;
  the only labelled signal used is this single scoring pass.
