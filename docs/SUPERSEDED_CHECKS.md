# Failed and superseded checks

1. **Step 6 Job test:** `step6_job_summary.json` reports normal PASS but `step6_normal_parent_done.json` reports child exit 1. Cleanup observations alone did not establish a normally completed child.
2. **Old S3:** source `C01_S3_Result_002/summary.json` has `all_pass=true`; normal/unlimited terminal event is `WORKER_EXCEPTION` with worker exit 0. The separately preserved case JSONL confirms the contradiction. These are retained source observations, not accepted normal-path success.
3. **Final S3 v1.2:** source `C01_S3_Result_003/summary.json` and its case records establish the limited corrected normal/unlimited `NORMAL_COMPLETE`/0 observations, overlimit `MEMORY_ERROR_OBSERVED`/42, and injected exception `WORKER_EXCEPTION`/1. Both summaries share schema version `C01_S3_DYNAMIC_V1`; use the source directory and original SHA256 to distinguish them.

The source v1.2 README attributes the misleading exception handling to catching `BaseException` around `sys.exit`; narrowing to `Exception` was recorded as the revision. This is historical explanation, not a new dynamic verification. Earlier static guard-string failure also preceded the final run. Those development details do not broaden the final test's scope.

Original source bytes remain privately unchanged. Curated copies preserve PASS flags, contrary events and exits together. No silent repair is applied. Final S3 does not establish whole-model numerical equivalence, system safety or a valid production memory cap. B1 remains NO-GO, and real-model diagnostics remain NOT RUN.
