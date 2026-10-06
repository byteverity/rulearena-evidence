# ByteVerity Validity: RuleArena evidence

The answers, hashes and scripts behind our [RuleArena](https://github.com/skyriver-2000/RuleArena) results. They let anyone
re-score them with **RuleArena's own reference implementation**, without trusting us. Spec-gap report:
[RuleArena issue #5](https://github.com/SkyRiver-2000/RuleArena/issues/5).

## Results

| Domain | Problems | L0 | L1 | L2 | All |
| --- | --- | --- | --- | --- | --- |
| Tax | 300 | 0.970 | 0.850 | 0.750 | **0.857** |
| NBA | 216 | 0.802 | 0.697 | 0.522 | **0.699** |
| Airline | 300 | 0.760 | 0.730 | 0.600 | **0.697** |
| **Overall (solver A, primary)** | 816 | | | | **617/816 = 0.756** |

These are **zero-label, one-shot** results on the official set. Solver B, the second independent build, scores the same on
airline and tax and 0.694 on NBA.

**Airline follow-ups, labelled:**

| Airline set | Listed bag order | Customer-favourable policy | Status |
| --- | --- | --- | --- |
| Official 300 | 0.697 | 0.943 | **Post-hoc**: the policy was chosen after seeing errors; it does not replace 0.697 |
| Fresh 300 (new seeds, RuleArena's `gen_questions.py`) | 0.760 | **0.903** | **Clean**: pre-registered, never seen by anyone, scored once |

## Verify it yourself

```bash
git clone https://github.com/skyriver-2000/RuleArena && git -C RuleArena checkout 59f60f6
pip install -r requirements.txt
python score.py RuleArena                     # → 617/816 = 0.756, per domain and level as above
python fresh/generate_fresh.py RuleArena      # → regenerates the 300 fresh problems byte-for-byte from the seeds
python fresh/score_fresh.py RuleArena         # → 0.760 listed order, 0.903 with the policy
# optional: download frozen-answers.tar.gz from the Releases page, extract here, then
python verify_answers.py                      # → SHA-256 of each frozen answer file matches ANSWERS.sha256; slim answers match
```

## What is here

| Path | Content |
| --- | --- |
| `predictions/{airline,tax,nba}_{A,B}.jsonl` | Our answer for every problem (`id`, `answer`). Airline/tax answers are numbers (tax: owed > 0, overpaid < 0); NBA is `False` or `True\|<operation>\|<team>` |
| `index.json` | Maps each `id` to RuleArena's domain, level and index |
| `ANSWERS.sha256` | SHA-256 of the full frozen answer files (release asset), recorded before unsealing |
| `PREREGISTRATION.md` | The one-shot scoring plan, written before unsealing; primary = solver A |
| `interpretations/` | Each solver's log of every point the rule text left open: the competing readings, the one chosen, and the sentence it rests on. Written before scoring. The airline logs record the bag-order choice ("…or choose the order that minimizes fees") |
| `policy/` | The customer-favourable policy (exact search over bag-slot assignments, solver unchanged), its hash, pre-registration, and the post-hoc analyses |
| `fresh/` | The 300 fresh problems, seed scheme, generation and scoring scripts, and our answers |
| `protocol/` | `PROTOCOL.md` (how the seal and the checks worked), `prepare.py` (renders exactly what a model sees from RuleArena), `SEAL.sha256` |

## Method in one paragraph

**Proposer:** OpenAI gpt-6-luna via Codex CLI (subscription, $0 API spend; offline sandbox, no web access). It wrote two
independent solver builds per domain from the rule text alone. **Everything that decides an answer is deterministic:**
extraction code, synthesa-decide rule oracles, and the Validity gate. The gate sent exact, label-free residuals each round:
- every value is anchored to its exact place in the question text;
- every rule clause is covered;
- the rule-table oracles are complete and contradiction-free;
- metamorphic relations hold;
- the two independent builds agree.

The answers, reference code and scorer stayed sealed until a single scoring pass. Details are in `protocol/PROTOCOL.md`.
The solver and verifier code is not published here.

## Honest notes

- **Timing.** The pre-registration and answer hashes were recorded locally before unsealing. They were not timestamped by a
  third party, so their timing rests on our word; we publish them as recorded. The fresh-set problems, by contrast, are
  reproducible by anyone from the seeds, and their gold answers come only from RuleArena's code.
- **Shared misreadings pass cross-checks.** The two builds agreed on airline yet both read bag order literally. The
  reference sorts bags by `complementary_gain`, which the rules never state; see issue #5.
- **NBA was admitted with 6 of 216 builds disagreeing**, disclosed. There is no NBA generator, so there is no fresh NBA set.
- **Open:** 14 official airline misses of exactly −$5 are not yet diagnosed.

Contact: Mohit Mahajan, ByteVerity · Validity, mohit@byteverity.com
