#!/usr/bin/env python3
"""Re-score our frozen RuleArena answers with RuleArena's OWN reference implementation and correctness rules.
usage: python score.py /path/to/RuleArena            (tested at RuleArena commit 59f60f6)"""
import json, os, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); import _stubs  # noqa: F401
import numpy as np
U = Path(sys.argv[1]).resolve()
idx = json.load(open(HERE / "index.json"))
truth = {}
os.chdir(U / "airline"); sys.path.insert(0, str(U / "airline"))
from compute_answer import load_checking_fee, compute_answer as air  # airline: correct iff value == fee
T = load_checking_fee()
rows = {c: [json.loads(l) for l in open(f"synthesized_problems/comp_{c}.jsonl")] for c in range(3)}
for e in idx:
    if e["domain"] == "airline":
        truth[e["id"]] = air(**rows[e["level"]][e["index"]]["info"], check_base_tables=T)[0]
sys.path.pop(0); os.chdir(U / "tax"); sys.path.insert(0, str(U / "tax"))
import importlib
me, sf = importlib.import_module("micro_evaluation"), importlib.import_module("structured_forms")  # tax: np.isclose
tp = {c: json.load(open(f"synthesized_problems/comp_{c}.json")) for c in range(3)}
for e in idx:
    if e["domain"] == "tax":
        truth[e["id"]] = me.compute_answer(sf.TaxPayer(**tp[e["level"]][e["index"]]["pydantic"]))[0]
os.chdir(U / "nba")                                                                                   # nba: exact target
nb = {c: json.load(open(f"annotated_problems/comp_{c}.json")) for c in range(3)}
for e in idx:
    if e["domain"] == "nba":
        q = nb[e["level"]][e["index"]]
        truth[e["id"]] = "False" if not q["answer"] else f"True|{q['illegal_operation']}|{q['problematic_team']}"
def ok(dom, p, g):
    if p is None: return False
    if dom == "airline": return isinstance(p, (int, float)) and p == g
    if dom == "tax": return isinstance(p, (int, float)) and bool(np.isclose(p, g))
    return p == g
lvl = {e["id"]: e["level"] for e in idx}
tot = 0
for dom in ("airline", "tax", "nba"):
    for side in "AB":
        pred = {json.loads(l)["id"]: json.loads(l)["answer"] for l in open(HERE / "predictions" / f"{dom}_{side}.jsonl")}
        res = {e["id"]: ok(dom, pred.get(e["id"]), truth[e["id"]]) for e in idx if e["domain"] == dom}
        per = [sum(v for k, v in res.items() if lvl[k] == L) / sum(1 for k in res if lvl[k] == L) for L in range(3)]
        print(f"{dom:8s} {side}  {sum(res.values())}/{len(res)} = {sum(res.values())/len(res):.3f}   " + "  ".join(f"L{L} {p:.3f}" for L, p in enumerate(per)))
        if side == "A": tot += sum(res.values())
print(f"PRIMARY (solver A) overall: {tot}/816 = {tot/816:.3f}")
