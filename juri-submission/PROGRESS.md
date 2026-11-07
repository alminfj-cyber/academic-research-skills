# JURI check progress

Keys: ⬜ not started · 🔄 in progress · ✅ done/pass · ❌ fails, fix needed · ⚠️ warning, decide · N/A (with a reason)

**Paper file:** `paper/Bardeen_JURI_v1.docx` (local only, not committed)
**Current version:** v1
**Next step:** Stage 0 answers (8 intake questions) → then Stage 3 guided content review on v1, or fix the Stage 1 ❌ items first and send v2.

## Stages
| Stage | Status | Version | Date | Notes |
|---|---|---|---|---|
| 0 Intake | 🔄 | v1 | 2026-11-07 | paper received; 8 questions awaiting answers |
| 1 Format check (`check_juri.py`) | ✅ | v1 | 2026-11-07 | 11 FAIL, 5 WARN, report reports/stage1_v1.md |
| 2 References (`/ars-citation-check` + R4) | ✅ | v1 | 2026-11-07 | 18/18 DOIs verified; 4 non-DOI classics for you to confirm |
| 3 Content review (guided `/ars-reviewer`) | ⬜ | | | |
| 4 Your declarations | ⬜ | | | |
| 5 Turnitin (PL1) | ⬜ | | | |
| 6 Fix loop | ⬜ | | | |
| 7 Final gate | ⬜ | | | |

## Rule status (IDs from JURI_CHECKLIST.md)
| ID | Status | Note |
|---|---|---|
| R1 | ✅ | 34 superscript citation numbers |
| R2 | ✅ | numbered in order of first citation |
| R3 | ✅ | 22 refs, all cited, none missing |
| R4 | ⚠️ | Nature pattern otherwise correct (italic journal, bold volume, (year)). Fix: list numbered "(1)" → "1."; page ranges use "-" → en dash "–" |
| R5 | ⚠️ | 18/18 DOIs resolve and match (Crossref). Refs 1, 2, 3, 11 are books/proceedings with no DOI → YOU confirm details (esp. ref 11 page 174, ref 3 pages 343–450) |
| R6 | ⬜ | |
| R7 | ✅ | no long direct quotes |
| R8 | ⬜ | |
| S1 | ⬜ | |
| S2 | ✅ | 195 words |
| S3 | ⬜ | |
| S4 | ✅ | 6 keywords |
| S5 | ⬜ | |
| S6 | ❌ | no Literature Review section; earlier studies are inside the Introduction (intro paragraphs 3–6) |
| S7 | ❌ | no Methodology section; method content is in §2 and §4.1 |
| S8 | ❌ | no "Results and Discussion" heading; results are in §3–§4 |
| S9 | ⚠️ | future work present; limitations implied ("concerns neutral massive particles…") but not stated as limitations; §4.4 has them |
| S10 | ❌ | no Acknowledgments section |
| S11 | ❌ | missing: Literature Review, Methodology, Results and Discussion, Acknowledgments |
| F1 | ⬜ | |
| F2 | ✅ | 4 images, 584–600 dpi |
| F3 | ❌ | captions below figures OK; but 2 body paragraphs ("Table 2 gives…", "Table 3 reports…") use the Caption style; Fig. 1 (42 words) and Fig. 4 (56 words) captions long vs "concise and short" |
| F4 | ⚠️ | captions use "Figure N."; guide shows "Fig. 1" (Q2) |
| F5 | ✅ | 3 table titles, all above their tables |
| F6 | ✅ | Tables 1–3 in order |
| F7 | ⚠️ | "Figure 3 shows", "Figure 4 shows" → guide format "(Fig. 3)" |
| F8 | ✅ | all figures and tables referred to, in order |
| F9 | ✅ | 35 editable equations, none images |
| F10 | ⚠️ | numbers (1)–(35) consecutive; YOU confirm centred with number right |
| F11 | ✅ | no non-SI units found |
| F12 | ✅ | figures embedded |
| F13 | ⬜ | |
| F14 | ⬜ | |
| P1 | ✅ | English |
| P2 | ✅ | .docx |
| P3 | ❌ | not in template typography: Times New Roman, ~1.08 spacing, A4 margins 2.16/2.16/2.54/1.79 cm. Template: Arial 12, double spacing, 2.54/3.17/2.54/1.79 cm. No comments/tracked changes left |
| P4 | ⚠️ | 10 pages as is; ~17 pages when set in the template typography (LibreOffice simulation) → over the 15-page limit |
| P5 | ⬜ | Data & Code Availability mentions supplementary files/Notes S1–S3 → YOU confirm file exists and starts with title, authors, affiliations |
| P6 | ⬜ | |
| P7 | ⬜ | |
| P8 | ⬜ | |
| A1 | ❌ | no author names or affiliations anywhere in the file |
| A2 | ❌ | no corresponding author marked |
| A3 | ❌ | no mentor listed |
| A4 | ⬜ | |
| A5 | ⬜ | |
| A6 | ⬜ | |
| E1 | ❌ | no conflict-of-interest statement |
| E2 | ❌ | no funding statement (write the source or "no external funding") |
| E3 | ⬜ | |
| E4 | ⬜ | |
| E5 | ⬜ | |
| E6 | ⬜ | |
| E7 | ⬜ | |
| I1 | ⬜ | |
| I2 | ⬜ | |
| I3 | ⬜ | |
| I4 | ⬜ | |
| I5 | ⬜ | |
| PL1 | ⬜ | |
| SUB1 | ⬜ | |
| SUB2 | ⬜ | |
| SUB3 | ⬜ | |
| SUB4 | ⬜ | |
| SUB5 | ⬜ | |
| Q1 | ⬜ | keywords 4–8 |
| Q2 | ⬜ | Fig. vs Figure |
| Q3 | ⬜ | equation alignment |
| Q4 | ⬜ | anonymized file? |

## Run log
_(each stage appends one line: date · stage · version · result summary)_
- 2026-11-07 · Stage 1 · v1 · format check: 11 FAIL / 5 WARN; checker false results fixed after manual verification (abstract heading level, '*' in 'Sagittarius A*', 'fundamental' ≠ funding, 'Figs. 1 and 2')
- 2026-11-07 · Stage 2 · v1 · Crossref: 18/18 DOIs match; refs 1, 2, 3, 11 unindexed books/proceedings
