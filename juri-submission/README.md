# How your JURI paper gets checked

This folder holds everything needed to check a manuscript for the **Journal of Undergraduate Research International (KFUPM)** before you submit it.

| File | What it is |
|---|---|
| `JURI_CHECKLIST.md` | Every rule from the journal's website, with an ID (R1, S2, F9…) and who checks it |
| `check_juri.py` | An automatic format checker. It reads your .docx and never changes it. |
| `PROGRESS.md` | Status of every rule. It is updated after each stage, so a later session can pick up where the last one stopped. |
| `paper/` | Your manuscript goes here. It is **not committed** to git, so your unpublished paper never leaves this machine. |
| `reports/` | Reports from each run. They are not committed either, because they quote your paper. |

## The flow

Each stage records its result in `PROGRESS.md` before the next one starts. If a session ends partway through, the next session reads `PROGRESS.md` and continues from the first stage that isn't ✅.

```
Stage 0  Intake            → 8 questions about your paper (see below)
Stage 1  Format check      → check_juri.py                  (AUTO items)
Stage 2  References        → /ars-citation-check + R4       (CITE items)
Stage 3  Content review    → /ars-reviewer, guided mode     (REVIEW items)
Stage 4  Your declarations → yes/no answers                 (YOU items)
Stage 5  Plagiarism        → your KFUPM Turnitin %          (PL1)
Stage 6  Fix loop          → you edit; Stages 1-3 rerun on the new version
Stage 7  Final gate        → every ID ✅ or explained, then submit
```

### Stage 0: Intake (asked once)
1. Your field, which must be on the journal's 26-subject list (P7)
2. Did the study involve people or animals? If yes, what is the IRB approval number? (E3)
3. Funding source, or "none" (E2)
4. Authors and their roles: you, your mentor, and anyone else (A1–A6)
5. Has the work been published or submitted anywhere else, including as a course report? (P8, E7)
6. Where AI was used, for what, and on which sections (I1–I5)
7. Are all figures your own design? (F1)
8. Do you have a Turnitin report? (PL1)

### Stage 1: Automatic format check
```bash
python3 check_juri.py paper/<your-paper>.docx --out reports/stage1_v1.md
```
This covers the abstract word count, keywords, required sections and their order, limitations and future work, captions above or below, Fig./Table numbering and in-text form, figure dpi, editable equations and their numbering, non-SI units, citation numbering and cross-checks, the Nature reference pattern, the mentor label, conflict-of-interest and funding statements, leftover template text, and the actual page count.

### Stage 2: References
`/ars-citation-check` looks up every reference and reports any that it can't find or whose details don't match. Nature formatting is checked by R4 together with you, because the skill doesn't support Nature style.

### Stage 3: Content review (guided)
`/ars-reviewer` runs in guided mode, aimed at an undergraduate journal and the checklist's S-items. It asks questions and points out problems. **You write every fix**, as JURI's AI Guidelines require.

### Stages 4–5: Your declarations and Turnitin
Answer the YOU items in `PROGRESS.md`, and paste your Turnitin percentage (excluding references). The target is 15% or less.

### Stage 6: Fix loop
Save each revision as a new version, such as `paper/<name>_v2.docx`. Stages 1–3 run again on that version only. `PROGRESS.md` keeps the history.

### Stage 7: Final gate
Submit only when every ID is ✅ or marked N/A with a reason, and the Q questions are resolved. The SUB items come last: the double-anonymized file, the submission form fields, and suggested reviewers.

## How to resume
In a new session, say: **"Continue my JURI check"**. Claude reads `PROGRESS.md` and picks up at the first stage or ID that isn't done.
