#!/usr/bin/env python3
"""Extract source frames without modifying the original character assets."""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageSequence

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=ROOT / 'generated' / 'frames')
    parser.add_argument('--faction', action='append')
    args = parser.parse_args()
    assets = ROOT / 'assets'
    manifest = json.loads((assets / 'manifest.json').read_text())
    known = {entry['id'] for entry in manifest}
    if args.faction and set(args.faction) - known:
        parser.error('Unknown faction')
    for entry in manifest:
        faction = entry['id']
        if args.faction and faction not in args.faction:
            continue
        target = args.output / faction
        target.mkdir(parents=True, exist_ok=True)
        frames = []
        with Image.open(assets / entry['original']) as source:
            if source.n_frames != entry['frames'] or list(source.size) != entry['size']:
                raise ValueError(f'{faction}: source differs from manifest')
            for index, frame in enumerate(ImageSequence.Iterator(source)):
                name = f'{index:03d}.png'
                frame.convert('RGBA').save(target / name)
                frames.append({'file': name, 'durationMs': frame.info.get('duration', 100)})
        (target / 'frames.json').write_text(json.dumps({'faction': faction, 'status': 'source-frames-only', 'frames': frames}, indent=2) + '\n')
        print(f'{faction}: {len(frames)} frames')

if __name__ == '__main__':
    main()
