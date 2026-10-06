#!/usr/bin/env python3
"""Regenerate the 300 fresh airline problems with RuleArena's own generator and the published seeds, and check them
byte-for-byte against fresh/problems/. usage: python fresh/generate_fresh.py /path/to/RuleArena"""
import hashlib, json, os, random, sys
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent
U = Path(sys.argv[1]).resolve() / "airline"
os.chdir(U); sys.path.insert(0, str(U))
from gen_questions import gen_question
bad = 0
for c in range(3):
    for i in range(100):
        s = 20261006000 + c * 1000 + i
        random.seed(s); np.random.seed(s % (2**32))
        prompt, _ = gen_question(complexity=c)
        pub = (HERE / "problems" / f"fresh_airline_L{c}_{i:03d}.txt").read_text()
        bad += prompt != pub
print("regenerated 300 fresh problems;", "ALL IDENTICAL to the published set" if bad == 0 else f"{bad} DIFFER")
