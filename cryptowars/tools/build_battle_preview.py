#!/usr/bin/env python3
"""Generate experimental animation layouts; source poses are not combat actions."""
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'generated' / 'frames'
OUTPUT = ROOT / 'generated' / 'battle-preview' / 'Content' / 'Sprites' / 'cryptowars'
# IDs from client/battle/BattleConstants.h. Only melee preview groups.
GROUPS = {0:'moving',1:'mouseon',2:'holding',3:'hitted',4:'defence',5:'death',7:'turn_l',8:'turn_r',11:'attack_up',12:'attack_front',13:'attack_down',20:'move_start',21:'move_end',22:'dead'}

def main():
    for faction in ('ton', 'btc'):
        source = SOURCE / faction
        metadata = json.loads((source / 'frames.json').read_text())
        target = OUTPUT / faction
        target.mkdir(parents=True, exist_ok=True)
        names = []
        for entry in metadata['frames']:
            name = entry['file']
            with Image.open(source / name) as im:
                im.convert('RGBA').save(target / name)
            names.append(name)
        # Use a static original pose for unsupported actions, not a fake attack.
        sequences = [{'group': group, 'frames': [names[0]]} for group in GROUPS]
        layout = {'basepath': f'cryptowars/{faction}/', 'sequences': sequences}
        (OUTPUT / f'{faction}.json').write_text(json.dumps(layout, indent=2) + '\n')
        print(f'{faction}: {len(sequences)} placeholder groups; not playable art')

if __name__ == '__main__':
    main()
