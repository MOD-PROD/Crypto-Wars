#!/usr/bin/env python3
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "generated/battle-preview"
target = ROOT / "generated/installable/cryptowars"
if target.exists():
    shutil.rmtree(target)
shutil.copytree(source, target)
config = target / "Content/config"
config.mkdir(parents=True)
units = json.loads((ROOT / "preview/creatures.json").read_text())
for unit in units.values():
    unit["disabled"] = False
    animation = target / "Content/Sprites" / (unit["graphics"]["animation"] + ".json")
    assert animation.is_file(), animation
(config / "creatures.json").write_text(json.dumps(units, indent=2))
manifest = json.loads((ROOT.parent / "Mods/cryptowars/mod.json").read_text())
manifest.update(description="Experimental creature preview; static combat poses; not engine-tested.", creatures=["config/creatures.json"], keepDisabled=True)
(target / "mod.json").write_text(json.dumps(manifest, indent=2))
shutil.make_archive(str(target.parent / "cryptowars-preview"), "zip", target.parent, target.name)
print("Packaged opt-in preview with two creatures")
