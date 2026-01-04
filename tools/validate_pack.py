#!/usr/bin/env python3
import hashlib
import json
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
        print("Usage: tools/validate_pack.py <pack_dir>", file=sys.stderr)
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

    got_vsha = sha256_file(vectors_path)
    exp_vsha = manifest.get("vectors_sha256")
    exp_pack = manifest.get("pack_id")

    if exp_vsha != got_vsha:
        raise SystemExit(f"vectors_sha256 mismatch: manifest={exp_vsha} actual={got_vsha}")
    if exp_pack != got_vsha:
        raise SystemExit(f"pack_id mismatch (MVP expects pack_id==vectors_sha256): manifest={exp_pack} actual={got_vsha}")

    # Validate vectors.jsonl minimally
    ids = set()
    count = 0
    with vectors_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            count += 1
            v = json.loads(line)
            vid = v.get("id")
            if not isinstance(vid, str) or not vid:
                raise SystemExit(f"Vector missing id at line {count}")
            if vid in ids:
                raise SystemExit(f"Duplicate vector id: {vid}")
            ids.add(vid)

            for k in ["scheme", "surface", "chain_profile", "security_equiv_bits", "expected"]:
                if k not in v:
                    raise SystemExit(f"Vector {vid} missing required field: {k}")

    exp_count = int(manifest.get("vector_count", -1))
    if exp_count != count:
        raise SystemExit(f"vector_count mismatch: manifest={exp_count} actual={count}")

    print(f"OK: {pack_dir.name} vectors={count} pack_id={got_vsha}")

if __name__ == "__main__":
    main()
