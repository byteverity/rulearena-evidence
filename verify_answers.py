#!/usr/bin/env python3
"""Check that the slim predictions/ match the frozen full answer files whose SHA-256 were recorded before unsealing.
Download frozen-answers.tar.gz from the GitHub release, extract it here (creates final/), then run this."""
import hashlib, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
want = dict(reversed(l.split()) for l in open(HERE / "ANSWERS.sha256"))
for path, h in sorted(want.items()):
    f = HERE / path
    got = hashlib.sha256(f.read_bytes()).hexdigest()
    slim = {json.loads(l)["id"]: json.loads(l)["answer"] for l in open(HERE / "predictions" / f.name)}
    full = {json.loads(l)["id"]: json.loads(l).get("answer") for l in open(f)}
    print(f"{path}: sha256 {'OK' if got == h else 'MISMATCH'}; slim answers {'match' if slim == full else 'DIFFER'}")
