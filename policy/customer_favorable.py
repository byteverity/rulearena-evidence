#!/usr/bin/env python3
"""Declared policy (general, not airline-specific): where the rule text leaves an assignment UNPINNED and it changes
the customer's cost, resolve it in the customer's favour (contra proferentem) by EXACT bounded search.

Airline instance: which listed items occupy the 1st/2nd/3rd checked-bag slots is unpinned (only slots 1-3 carry
distinct fees/complimentary status; every later bag is priced alike). We enumerate every ordered choice of up to 3
items for the leading positions (P(n,3) <= 336 for n = 8), keep the rest in question order, run the UNCHANGED solver on
each re-listing, and take the minimum total. Every problem where the policy changed the answer is recorded.

usage: customer_favorable.py <solver_ws> <problems_dir> <out.jsonl> [--workers N]"""
import itertools, json, re, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
ITEM = re.compile(r"^(\d+)\. (.+?): (\d+) x (\d+) x (\d+) inches, (\d+) lbs;$", re.M)

def variants(text):
    items = list(ITEM.finditer(text))
    body = [m.group(0) for m in items]
    n, seen = len(body), set()
    for k in range(min(3, n) + 1):
        for lead in itertools.permutations(range(n), k):
            order = list(lead) + [i for i in range(n) if i not in lead]
            key = tuple(order)
            if key in seen: continue
            seen.add(key)
            lines = [re.sub(r"^\d+\.", f"{j+1}.", body[i]) for j, i in enumerate(order)]
            yield "-".join(map(str, order)), text[:items[0].start()] + "\n".join(lines) + text[items[-1].end():]

def main():
    ws, pdir, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 4
    probs = sorted(pdir.glob("*.txt"))
    def one(p):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d); vmap = {}
            for tag, txt in variants(p.read_text()):
                f = d / f"v{len(vmap):05d}.txt"; f.write_text(txt); vmap[f.stem] = tag
            o = d / "o.jsonl"
            subprocess.run([sys.executable, "solver/solve.py", "--all", str(d), str(o)], cwd=ws, capture_output=True)
            rows = [json.loads(l) for l in o.read_text().splitlines()] if o.exists() else []
            ans = {vmap[r["id"]]: r.get("answer") for r in rows if isinstance(r.get("answer"), (int, float))}
        listed = "-".join(map(str, range(len(ITEM.findall(p.read_text())))))
        base = ans.get(listed)
        best_tag = min(ans, key=lambda t: (ans[t], t)) if ans else None
        return {"id": p.stem, "answer": ans[best_tag] if best_tag else None, "listed_order_answer": base,
                "policy_fired": best_tag is not None and base is not None and ans[best_tag] < base,
                "chosen_order": best_tag, "orders_evaluated": len(ans)}
    with ThreadPoolExecutor(workers) as ex, open(out, "w") as f:
        for r in ex.map(one, probs):
            f.write(json.dumps(r) + "\n")

if __name__ == "__main__":
    main()
