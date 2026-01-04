#!/usr/bin/env python3
import hashlib
import json
import os
import sys
from pathlib import Path

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    if len(sys.argv) != 2:
        print("Usage: tools/pack_hash.py <pack_dir>", file=sys.stderr)
        sys.exit(2)

    pack_dir = Path(sys.argv[1]).resolve()
    manifest_path = pack_dir / "manifest.json"
    if not manifest_path.exists():
        raise SystemExit(f"Missing manifest: {manifest_path}")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    vectors_file = manifest.get("vectors_file", "vectors.jsonl")
    vectors_path = pack_dir / vectors_file
    if not vectors_path.exists():
        raise SystemExit(f"Missing vectors file: {vectors_path}")

    vsha = sha256_file(vectors_path)

    # MVP rule: pack_id == sha256(vectors.jsonl)
    manifest["vectors_sha256"] = vsha
    manifest["pack_id"] = vsha

    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"OK: vectors_sha256 = {vsha}")
    print(f"OK: pack_id        = {vsha}")

if __name__ == "__main__":
    main()
