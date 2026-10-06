#!/usr/bin/env python3
"""Score our fresh-set answers: regenerate each problem's ground truth from its seed with RuleArena's generator and
score it with RuleArena's reference compute_answer. usage: python fresh/score_fresh.py /path/to/RuleArena"""
import json, os, random, sys
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); import _stubs  # noqa: F401
U = Path(sys.argv[1]).resolve() / "airline"
os.chdir(U); sys.path.insert(0, str(U))
from gen_questions import gen_question
from compute_answer import load_checking_fee, compute_answer
T = load_checking_fee(); gold = {}
for c in range(3):
    for i in range(100):
        s = 20261006000 + c * 1000 + i
        random.seed(s); np.random.seed(s % (2**32))
        _, info = gen_question(complexity=c)
        gold[f"fresh_airline_L{c}_{i:03d}"] = (compute_answer(**info, check_base_tables=T)[0], c)
for name, label in (("A_listed", "A, listed bag order (as scored on the official set)"), ("A_policy", "A + customer-favourable policy [PRIMARY]")):
    p = {json.loads(l)["id"]: json.loads(l)["answer"] for l in open(HERE / f"{name}.jsonl")}
    ok = {k: p.get(k) == v[0] for k, v in gold.items()}
    per = [sum(ok[k] for k in ok if gold[k][1] == L) / 100 for L in range(3)]
    print(f"{label:52s} {sum(ok.values())}/300 = {sum(ok.values())/300:.3f}  " + "  ".join(f"L{L} {x:.2f}" for L, x in enumerate(per)))
