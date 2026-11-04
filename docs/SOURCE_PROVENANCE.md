# Sources, identities and curation

The provided PACK 04 SHA256 is `4fffa17308754c8dba615ec093d21781b78e9e29ed5c08f677b65f4f63d46dbe`; PACK 05 is `290e51c5863d6fc1f5146ee286f67af05977ebc0a25650fdc72a698a5320aa2a`. Their new attachment suffixes `(3)` versus the request's `(2)` do not denote changed bytes. Both CRC checks passed. The separate assessment Markdown matches the copy in its archive; all assessment checksums passed. These facts validate input identity, not scientific correctness.

All 306 PACK provenance rows resolve to matching Evidence Index entries, source-register identities and SHA256 content. The PACKs store 131 and 74 unique evidence items respectively; cross-PACK duplicates remain possible. The 205-row selection evaluates within-PACK unique contents and lists provenance aliases. The public manifest selects 59 source items and records exactly how each became a public file. No entire private PACK or audit package is redistributed.

The full C01 Evidence Index has 650 entries / 490 unique hashes. The supplied Source Register contains 72 entries, with **67 ZIP + 1 MD + 2 JSON + 2 TXT** by actual file type. This corrects the request's “70 ZIP + two TXT”. The two unattached protocol TXT entries and PACKs 01–03 were not dynamically/materially revalidated here; their index identities are historical metadata only. Underlying source-archive hashes are cross-checked against the supplied register, not recomputed from absent archives.

The 2 November independent assessment is an important secondary interpretation source. The present technical claims use the original saved run/test/decision files as primary evidence. That earlier assessment's PASS labels are not substituted for dynamic Windows evidence. The present preparation/QC is also one Work, not external peer review.

## Boltz-2 official sources (v2.2.1)

| File | Recorded Git blob SHA1 | Official source |
| --- | --- | --- |
| trunkv2.py | ebd7a2ec6160307076b226b0d7d3ef1bfb376c29 | https://github.com/jwohlwend/boltz/blob/v2.2.1/src/boltz/model/modules/trunkv2.py |
| transition.py | 8bab809375efe56fb8397af341db5af7cc39a071 | https://github.com/jwohlwend/boltz/blob/v2.2.1/src/boltz/model/layers/transition.py |
| outer_product_mean.py | 9a4a607d0f2da30539eb8a9bcf3a6d5b3f90f9db | https://github.com/jwohlwend/boltz/blob/v2.2.1/src/boltz/model/layers/outer_product_mean.py |

Official code retrieved on 4 November 2026 was inspected for the existing chunking branches and final-projection initialization calls. The Git blob hashes match the historical fingerprints when preserving the official single trailing newline; a text-tool-added extra terminal newline is a presentation artifact and is not called an exact downloaded source blob. The official `final_init_` calls and historical author-method excerpts identify why Step 3 zero outputs are insufficient and why Step 4 substituted test-only final weights. No official implementation is included in the public payload. License: https://github.com/jwohlwend/boltz/blob/v2.2.1/LICENSE (MIT).

## Microsoft semantics

- https://learn.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-jobobject_extended_limit_information — JobMemoryLimit and peak counters.
- https://learn.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-jobobject_basic_limit_information — job-wide committed-memory limit and kill-on-close flags.

The API definitions do not convert the small-worker saved tests into a production safety guarantee. The observed peak-counter/cap difference remains explicit.

## Quality references actually inspected

- https://github.com/shomiyazaki-ai/sampl8-pka-reference-sensitivity — source/claim/reproduction/citation boundaries.
- https://github.com/shomiyazaki-ai/bioemu-filter-sensitivity-ntbe-x2-omega — verification levels, archival versus maintained identities.
- https://github.com/shomiyazaki-ai/hpacker-stagewise-proximity-x4 — at-a-glance results and correction boundaries.
- https://github.com/shomiyazaki-ai/boltz2-mpc-reference-structure-comparison — evidence links, limitations, distinct A+B scope.

Their current default-branch READMEs were fetched on 4 November 2026 as quality references. An old pending-publication phrase on a reference README is not treated as proof of current archive publication status. No reference's figure count, publication genre or MSC assessment is copied into C+D.
