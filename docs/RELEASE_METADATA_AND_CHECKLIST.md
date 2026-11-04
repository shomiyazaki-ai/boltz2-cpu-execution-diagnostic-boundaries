# Release metadata and author checklist

Status: **UNPUBLISHED CANDIDATE — author reports a Zenodo draft and reserved version DOI `10.5281/zenodo.23934898`. ZIP upload, final saved-draft validation, GitHub repository/release and Zenodo Publish are still pending.** Research STOP is independent of publication preparation.

| Field | Candidate / pending value |
| --- | --- |
| Title | Boltz-2 CPU Execution and Diagnostic Boundaries: A Windows 11 Technical Record |
| Author / affiliation | Sho Miyazaki / Independent researcher, Tokyo, Japan |
| Repository name | `boltz2-cpu-execution-diagnostic-boundaries` |
| Version / planned tag | 1.0.0 / v1.0.0 |
| Actual repository URL / commit / published tag | PENDING / PENDING / PENDING |
| Zenodo type | **Other**; “Technical Record” is a descriptive label, not a verified special subtype |
| Zenodo DOI / publication date | 10.5281/zenodo.23934898 (reserved, unpublished draft) / PENDING (actual publication date not established) |
| Relation to A+B | references 10.5281/zenodo.23910491; separate technical output, no transferred results/MSC |
| Licenses | CC BY 4.0 scoped to original documentation/figures/data curation; MIT scoped to original Python code |

## Metadata and route

Recommended: after explicit author approval, create a **direct Zenodo deposit** with type Other, upload the frozen repository payload as one ZIP, and enter the provided metadata. List **both scoped licenses**, supported by the current mixed-license guidance. The GitHub release remains a fixed code/data snapshot of the same scientific content. No automatic archiving is configured here.

The official GitHub archiving guide describes a **Software record**; it does not establish that automatic release archiving will preserve this desired Other classification. We therefore do not claim automatic support for Other. This is a route choice based on the documented flow, not a live sandbox deposit test.

`.zenodo.json` is supplied as a legacy metadata candidate with Other and **no single-license field**, because a single value would misrepresent the file-scoped CC BY 4.0 / MIT arrangement. **Do not use it as a complete mixed-license import or an automatic-publish instruction.** The direct form-ready plan in `ZENODO_DEPOSIT_METADATA.json` contains both scoped licenses. It is not labelled an API-validated request. In GitHub release archiving, `.zenodo.json` takes precedence over `CITATION.cff`; CFF still serves GitHub citation display. CFF uses its supported dataset type for this data/evidence compendium, not a fictitious technical-record CFF enum.

## Author review before any publication

- Confirm that the public claims, corrections, source selection, funding/conflict/resource declarations, license scope and AI disclosure reflect the author's record and rights.
- Confirm that the 59 selected curated source items are sufficient and the excluded executable/raw inputs need not be distributed.
- Review the two figures, especially the distinction between a last monitoring sample and a stop-event timestamp.
- Approve the exact frozen candidate and the separate GitHub/Zenodo publication actions explicitly. This Work does not seek or assume that approval.
- The author reports DOI `10.5281/zenodo.23934898` reserved in the Zenodo draft. Confirm it remains assigned to this draft after file upload; do not present it as published until Zenodo Publish is complete.
- Set the real publication date, repository URL and release commit after they exist. Do not place a commit hash inside the same commit's content as a circular identity claim; record it in the release metadata or external record.
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

Initial draft UI inspection and DOI reservation are **author-reported DONE**; file-upload acceptance, save-with-file validation, preview after upload, Publish and public download checks remain **NOT RUN**. These expected publication-stage tasks do not imply a scientific-data QC failure.

Publication Gate 5 is **IN PROGRESS**: the author reports that Other, both file-scoped licenses, related A+B DOI, description and DOI reservation were checked in the Zenodo draft UI. ZIP upload/save/preview and public publication are not yet completed. The CFF license field is intentionally omitted due to the OR semantics of arrays under CFF 1.2.0.

## Gate 5 author-reported values (4 November 2026)

- DOI: `10.5281/zenodo.23934898` — **reserved in Zenodo draft, not yet published**.
- Resource type: Other; descriptive label: Technical Record.
- Licenses: CC BY 4.0 and MIT, file-scoped per `LICENSE_SCOPE.md`.
- Copyright field: Copyright © 2026 Sho Miyazaki for author-original materials. Third-party materials retain their respective rights. Licensing is file-specific: CC BY 4.0 applies to author-original prose, figures, and eligible curated materials; MIT applies to author-original code. See LICENSE_SCOPE.md and docs/RIGHTS_AND_ATTRIBUTION.md for details.
- Related work: References `10.5281/zenodo.23910491` (separate C01 A+B record).
- GitHub repository URL, tag and commit: pending.
- The draft UI showed an intended date of `2026-11-04`, which must be checked against the actual publication date before publishing.
- No final public access or DOI resolution has been established.
