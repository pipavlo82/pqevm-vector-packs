# Licensing scope

The Apache License, Version 2.0, reproduced in [LICENSE](LICENSE), applies to
Pavlo-authored repository material within the scope below, to the extent Pavlo
owns or is authorized to license the relevant rights.

Copyright 2026 Pavlo Tvardovskyi

Existing third-party copyright, license, patent, attribution and trademark
notices remain applicable. For mixed or adapted material, the new grant covers
only Pavlo's original additions. Imported source, external contributions,
quoted specifications, captures and other third-party material are not
relicensed by this grant. Inclusion in this repository or a missing license
does not itself supply permission. Existing grants are not withdrawn or narrowed.

| Material | Applicable boundary |
| --- | --- |
| `README.md`, `schema/**`, `tools/**` and Pavlo's original pack packaging/metadata contributions | Apache-2.0 for Pavlo-authored material. |
| `packs/mldsa65_fips204/vectors.jsonl` | Imported public-key/signature/message operands from `ml-dsa-65-ethereum-verification/test_vectors/vector_001.json`, as recorded in each vector's notes. Their original source rights remain applicable; authorship of the underlying operands is not established by the pack's repository owner. |
| `packs/mldsa65_fips204/manifest.json` | Original packaging metadata is distinguishable from the referenced external/source operands. The existing empty `source_commit`, vector hash, `pack_id`, count and provenance are preserved exactly; this legal change does not repair or infer missing provenance. |

No license is newly granted for unconfirmed third-party vector material. Source
repositories are references only and are not relicensed. A successful pack
validator establishes the unchanged container hash/count contract, not signature
validity, FIPS conformance or vector provenance completeness.
