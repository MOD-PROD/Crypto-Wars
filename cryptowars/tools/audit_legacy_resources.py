#!/usr/bin/env python3
"""Static inventory, not a proof of standalone compatibility."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[2]
pattern = re.compile(r'"([^"\n]+\.(?:txt|def|pcx|lod|snd|vid|h3m|wav|mp3|fnt))"', re.I)
results = {}
for folder in ("client", "clientsdl2", "lib", "launcher", "config"):
    for path in sorted((root / folder).rglob("*")):
        if path.suffix not in (".cpp", ".h", ".json"):
            continue
        for n, line in enumerate(path.read_text(errors="replace").splitlines(), 1):
            for match in pattern.finditer(line):
                results.setdefault(match.group(1).upper(), []).append({"file": str(path.relative_to(root)), "line": n})
output = root / "cryptowars/generated/legacy-resource-audit.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(results, indent=2))
print(f"{len(results)} distinct literal resource references; dynamic references not covered")
