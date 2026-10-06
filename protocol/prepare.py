#!/usr/bin/env python3
"""Firewall step. Renders EXACTLY what a model sees in RuleArena (rule text + per-problem question/forms)
into inputs/, then the upstream repo (answers, structured info, reference implementation, scorer) is sealed.
Only the problem id mapping is kept, inside sealed/."""
import json, re, sys, shutil, os
from pathlib import Path
R = Path(__file__).resolve().parent
U = R / "upstream"
out = R / "inputs"
idx = []
# ---- airline: rules text + question text (prompt template header/footer kept verbatim)
a = out / "airline"; (a / "problems").mkdir(parents=True, exist_ok=True)
shutil.copy(U / "airline/reference_rules.txt", a / "rules.txt")
src = (U / "airline/auto_test.py").read_text()
tpl = re.search(r'prompt_template = """(.*?)"""', src, re.S).group(1)
(a / "prompt_template.txt").write_text(tpl)
for c in range(3):
    for i, line in enumerate(open(U / f"airline/synthesized_problems/comp_{c}.jsonl")):
        pid = f"airline_L{c}_{i:03d}"
        (a / "problems" / f"{pid}.txt").write_text(json.loads(line)["prompt"])
        idx.append({"id": pid, "domain": "airline", "level": c, "index": i})
# ---- nba: rules text + assumptions template + query (team/player/operations) only
n = out / "nba"; (n / "problems").mkdir(parents=True, exist_ok=True)
shutil.copy(U / "nba/reference_rules.txt", n / "rules.txt")
src = (U / "nba/auto_test.py").read_text()
(n / "prompt_template.txt").write_text(re.search(r'prompt_template = """(.*?)"""', src, re.S).group(1))
for c in range(3):
    for i, q in enumerate(json.load(open(U / f"nba/annotated_problems/comp_{c}.json"))):
        pid = f"nba_L{c}_{i:03d}"
        txt = ("Team Situations:\n" + "\n".join(q["team_situations"]) + "\n\nPlayer Situations:\n" + "\n".join(q["player_situations"])
               + "\n\nOperations:\n" + "\n".join(q["operations"]))
        (n / "problems" / f"{pid}.txt").write_text(txt)
        idx.append({"id": pid, "domain": "nba", "level": c, "index": i})
# ---- tax: render the forms exactly as the harness does (default: tabular forms, no distractor, no example)
t = out / "tax"; (t / "problems").mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(U / "tax"))
import prompt as P  # model-facing form templates + instructions
src = (U / "tax/auto_test.py").read_text()
ptpl = re.search(r'prompt_template = """(.*?)"""', src, re.S).group(1)
(t / "prompt_template.txt").write_text(ptpl)
tbd_mark = "[__]"
for c in range(3):
    for i, prob in enumerate(json.load(open(U / f"tax/synthesized_problems/comp_{c}.json"))):
        tp = json.loads(json.dumps(prob["dict"]))
        forms = [P.basic_forms]
        if tp["itemized"]: forms.append(P.itemized_forms)
        if tp["self_employed"]: forms.append(P.self_employ_forms)
        if tp["has_student_loans_or_education_expenses"]: forms.append(P.edu_forms)
        if tp["child_and_dependent"]: forms.append(P.schedule_8812)
        forms = "".join(forms)
        for k, v in tp["data"].items():
            forms = forms.replace("$" + k, "$" + f"{v:,}" if not isinstance(v, str) else v)
        forms = forms.replace("$TBD", tbd_mark)
        p = ptpl.replace("$forms", forms).replace("$example", "")
        for k in ("name", "age", "spouse_age", "blind", "spouse_blind", "filing_status", "itemized", "num_qualifying_children", "num_other_dependents"):
            p = p.replace("$" + k, str(tp[k]))
        pid = f"tax_L{c}_{i:03d}"
        (t / "problems" / f"{pid}.txt").write_text(p)
        idx.append({"id": pid, "domain": "tax", "level": c, "index": i})
(R / "sealed").mkdir(exist_ok=True)
json.dump(idx, open(R / "sealed" / "index.json", "w"), indent=0)
print(len(idx), "problems rendered")
