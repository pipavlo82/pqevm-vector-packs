# PQEVM Vector Packs (canonical test vectors + calldata)

This repository hosts **canonical vector packs** for post-quantum (and related)
signature verification on EVM.

Goal:
- make benchmarks comparable across implementations by pinning:
  - vector semantics
  - calldata packing (when applicable)
  - expected outcomes (status / magic)
  - provenance metadata

Packs live under `packs/*`, each pack contains:
- `manifest.json` (metadata + hashes)
- `vectors.jsonl` (JSON Lines, one vector per line)

---

## Quick start

Validate a pack:

```bash
python3 tools/validate_pack.py packs/mldsa65_fips204
```

Compute / refresh manifest hashes:

```bash
python3 tools/pack_hash.py packs/mldsa65_fips204
```

---

## Repo layout

- `packs/` — canonical vector packs
- `schema/` — JSON schemas
- `tools/` — validators + hash utilities
