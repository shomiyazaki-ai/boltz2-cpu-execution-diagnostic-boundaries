# Release metadata and author checklist

Status: **UNPUBLISHED PRE-RELEASE CANDIDATE — Zenodo DOI `10.5281/zenodo.23934898` is reserved. The author-provided five-page Zenodo Preview confirms the initial ZIP upload/save and correct draft metadata; the initial uploaded ZIP is now superseded by the Windows-verifier correction. The replacement ZIP upload/preview, final GitHub release/tag and Zenodo Publish remain pending. The GitHub repository is private and contains initial staging commit `16cd45cffe05e8a7c2b6dd16ac4211db31cd7035`.** Research STOP is independent of publication preparation.

| Field | Candidate / pending value |
| --- | --- |
| Title | Boltz-2 CPU Execution and Diagnostic Boundaries: A Windows 11 Technical Record |
| Author / affiliation | Sho Miyazaki / Independent researcher, Tokyo, Japan |
| Repository name | `boltz2-cpu-execution-diagnostic-boundaries` |
| Version / planned tag | 1.0.0 / v1.0.0 |
| GitHub repository / initial staging commit / final release commit / published tag | `https://github.com/shomiyazaki-ai/boltz2-cpu-execution-diagnostic-boundaries` (private) / `16cd45cffe05e8a7c2b6dd16ac4211db31cd7035` (verified) / PENDING / PENDING |
| Zenodo type | **Other**; “Technical Record” is a descriptive label, not a verified special subtype |
| Zenodo DOI / publication date | 10.5281/zenodo.23934898 (reserved, unpublished draft) / PENDING (actual publication date not established) |
| Relation to A+B | references 10.5281/zenodo.23910491; separate technical output, no transferred results/MSC |
| Licenses | CC BY 4.0 scoped to original documentation/figures/data curation; MIT scoped to original Python code |

## Metadata and route

An existing **direct Zenodo draft** already has resource type Other and validated metadata. **Before publication, replace the superseded initial ZIP** with the new fully checked ZIP containing the Windows-compatible verifier and updated state notes, retaining all Zenodo UI metadata as already previewed. List **both scoped licenses**, supported by the current mixed-license guidance. The GitHub release remains a fixed code/data snapshot of the same scientific content. No automatic archiving is configured here.

The official GitHub archiving guide describes a **Software record**; it does not establish that automatic release archiving will preserve this desired Other classification. We therefore do not claim automatic support for Other. This is a route choice based on the documented flow, not a live sandbox deposit test.

`.zenodo.json` is supplied as a legacy metadata candidate with Other and **no single-license field**, because a single value would misrepresent the file-scoped CC BY 4.0 / MIT arrangement. **Do not use it as a complete mixed-license import or an automatic-publish instruction.** The direct form-ready plan in `ZENODO_DEPOSIT_METADATA.json` contains both scoped licenses. It is not labelled an API-validated request. In GitHub release archiving, `.zenodo.json` takes precedence over `CITATION.cff`; CFF still serves GitHub citation display. CFF uses its supported dataset type for this data/evidence compendium, not a fictitious technical-record CFF enum.

## Author review before any publication

- Confirm that the public claims, corrections, source selection, funding/conflict/resource declarations, license scope and AI disclosure reflect the author's record and rights.
- Confirm that the 59 selected curated source items are sufficient and the excluded executable/raw inputs need not be distributed.
- Review the two figures, especially the distinction between a last monitoring sample and a stop-event timestamp.
- Approve the exact frozen candidate and the separate GitHub/Zenodo publication actions explicitly. This Work does not seek or assume that approval.
- The author-provided Zenodo Preview confirms DOI `10.5281/zenodo.23934898` in an unpublished draft with its initial ZIP. Confirm the same DOI remains assigned after **replacement ZIP** upload and save; do not present it as published until Zenodo Publish is complete.
- The GitHub repository exists at `https://github.com/shomiyazaki-ai/boltz2-cpu-execution-diagnostic-boundaries`. Initial staging commit `16cd45cffe05e8a7c2b6dd16ac4211db31cd7035` is a historical record, **not** a claim to be the final release commit. Fix the final release commit and tag externally after the last content change. Do not place a final commit hash inside that same commit's content (circular identity). Set actual publication date at publication.
- Regenerate affected internal checksums after any approved edits, rerun V1/QC, and rebuild matching GitHub and Zenodo payloads. ZIP byte hashes and extracted file hashes are distinct.

## Post-publication checks (not performed)

Resolve the real version DOI; check title/type/version/creator/affiliation/licenses and related-work relation; download the public ZIP and verify its SHA256 and internal checksums against the approved release; verify figure/evidence links and GitHub tag/commit; preserve correction history. Create no duplicate “scientific results” from the two hosting locations. Ledger/SNS updates are outside this Work.

## Official sources checked 4 November 2026 JST

- https://help.zenodo.org/docs/github/
- https://help.zenodo.org/docs/github/archive-software/github-upload/ — describes Software records.
- https://help.zenodo.org/docs/github/describe-software/zenodo-json/ — JSON precedence over CFF.
- https://help.zenodo.org/docs/deposit/about-records/ — draft/record/version distinction.
- https://help.zenodo.org/docs/deposit/describe-records/resource-type/ — choose a principal type for mixed objects.
- https://help.zenodo.org/docs/deposit/describe-records/licenses/ — mixed-license uploads supported.
- https://developers.zenodo.org/ — legacy `upload_type=other`; legacy single-license field is not the full current multi-license form.

The author supplied a five-page Zenodo Preview PDF dated 4 November 2026: initial ZIP upload, draft Preview, DOI, resource type Other, both licenses, copyright and related DOI are **CHECKED IN THE SUPPLIED PREVIEW**. The initially uploaded ZIP is superseded by the Windows verifier correction; replacement ZIP upload/save/preview, Publish and public download checks are **NOT RUN**. These expected publication-stage tasks do not imply a scientific-data QC failure.

Publication Gate 5 draft metadata and the **initial ZIP** were preview-checked; **replacement ZIP** upload/save/preview and publication remain pending. The author-provided preview checked Other, both scoped licenses, copyright, related A+B DOI, Description and the version DOI. The CFF license field is intentionally omitted due to the OR semantics of arrays under CFF 1.2.0.

## Gate 5 author-reported values (4 November 2026)

- DOI: `10.5281/zenodo.23934898` — **reserved in Zenodo draft, not yet published**.
- Resource type: Other; descriptive label: Technical Record.
- Licenses: CC BY 4.0 and MIT, file-scoped per `LICENSE_SCOPE.md`.
- Copyright field: Copyright © 2026 Sho Miyazaki for author-original materials. Third-party materials retain their respective rights. Licensing is file-specific: CC BY 4.0 applies to author-original prose, figures, and eligible curated materials; MIT applies to author-original code. See LICENSE_SCOPE.md and docs/RIGHTS_AND_ATTRIBUTION.md for details.
- Related work: References `10.5281/zenodo.23910491` (separate C01 A+B record).
- GitHub repository `https://github.com/shomiyazaki-ai/boltz2-cpu-execution-diagnostic-boundaries`: private; initial staging commit `16cd45cffe05e8a7c2b6dd16ac4211db31cd7035` verified. Final release commit and tag: pending.
- The draft UI showed an intended date of `2026-11-04`, which must be checked against the actual publication date before publishing.
- No final public access or published DOI resolution has been established. The existing Zenodo preview is not proof of publication.
- Windows-compatible `verification/verify_record.py` and refreshed SHA256SUMS must appear in the replacement Zenodo ZIP; the initial Zenodo ZIP does not contain this fix.
- Metadata fields confirmed by the author-provided preview must not be changed when replacing the ZIP; verify the same description, both licenses, copyright, and related DOI afterward.
