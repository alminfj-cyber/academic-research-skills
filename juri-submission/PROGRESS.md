# JURI check progress

Keys: ⬜ not started · 🔄 in progress · ✅ done/pass · ❌ fails, fix needed · ⚠️ warning, decide · N/A (with a reason)

**Paper file:** `paper/Bardeen_JURI_v1.docx` (local only, not committed)
**Current version:** v3 (`paper/Bardeen_JURI_v3.docx`; built by local `paper/build_base.py` + `paper/edits_v3.py`; preview `preview/Bardeen_JURI_v3_preview.html`)
**Next step:** page-limit decision (≈19 Word pages vs 15) → condense or ask the journal; YOU review and accept the tracked edits; answer the figures question; then Stage 3 guided review and Turnitin.

## Stages
| Stage | Status | Version | Date | Notes |
|---|---|---|---|---|
| 0 Intake | 🔄 | v1 | 2026-11-07 | answered: authors, funding, acknowledgments, prior submission, supp. Pending: AI use, figures, Turnitin, mentor dept, COI, supplementary decision |
| 1 Format check (`check_juri.py`) | ✅ | v1 | 2026-11-07 | 11 FAIL, 5 WARN, report reports/stage1_v1.md |
| 2 References (`/ars-citation-check` + R4) | ✅ | v1 | 2026-11-07 | 18/18 DOIs verified; 4 non-DOI classics for you to confirm |
| 3 Content review (guided `/ars-reviewer`) | ⬜ | | | |
| 4 Your declarations | ⬜ | | | |
| 5 Turnitin (PL1) | ⬜ | | | |
| 6 Fix loop | 🔄 | v2 | 2026-11-07 | mechanical/compliance fixes done; author-only items marked as Word comments |
| 7 Final gate | ⬜ | | | |

## Rule status (IDs from JURI_CHECKLIST.md)
| ID | Status | Note |
|---|---|---|
| R1 | ✅ | 34 superscript citation numbers |
| R2 | ✅ | numbered in order of first citation |
| R3 | ✅ | 22 refs, all cited, none missing |
| R4 | ✅ | v2: list "1." numbering; page ranges en dash |
| R5 | ⚠️ | 18/18 DOIs resolve and match (Crossref). Refs 1, 2, 3, 11 are books/proceedings with no DOI → YOU confirm details (esp. ref 11 page 174, ref 3 pages 343–450) |
| R6 | ⬜ | |
| R7 | ✅ | no long direct quotes |
| R8 | ⬜ | |
| S1 | ⬜ | |
| S2 | ✅ | 195 words |
| S3 | ⬜ | |
| S4 | ✅ | 6 keywords |
| S5 | ⬜ | |
| S6 | ✅ | v3: tracked AI edit adds the research-gap paragraph at the end of the Literature Review (restates the author's own claim from the Introduction, bounded to the cited studies) → YOU accept/reject; check it matches your comparison with Kobialko & Gal'tsov |
| S7 | ✅ | v2: "3. METHODOLOGY: GEOMETRY AND GEODESIC EQUATIONS" |
| S8 | ✅ | v2: "4. RESULTS AND DISCUSSION" (old §3 → 4.1, old §4 → 4.2); 4 cross-references renumbered |
| S9 | ✅ | v3: tracked AI edit states three limitations explicitly (taken from §4.2.4) |
| S10 | ✅ | v2: ACKNOWLEDGMENTS section added |
| S11 | ✅ | v2: all sections present, in order |
| F1 | ⬜ | |
| F2 | ✅ | 4 images, 584–600 dpi |
| F3 | ⚠️ | v2: Caption-style body text fixed; Fig. 1 (42 w) and Fig. 4 (56 w) captions still long → YOU shorten or keep |
| F4 | ✅ | v2: captions "Fig. N." |
| F5 | ✅ | 3 table titles, all above their tables |
| F6 | ✅ | Tables 1–3 in order |
| F7 | ✅ | v2: in-text "Fig. N" |
| F8 | ✅ | all figures and tables referred to, in order |
| F9 | ✅ | 35 editable equations, none images |
| F10 | ⚠️ | numbers (1)–(35) consecutive; YOU confirm centred with number right |
| F11 | ✅ | no non-SI units found |
| F12 | ✅ | figures embedded |
| F13 | ⬜ | |
| F14 | ⬜ | |
| P1 | ✅ | English |
| P2 | ✅ | .docx |
| P3 | ⚠️ | v3: correct template typography (Times New Roman 12 double-spaced body, Arial headings, template margins); 11 tracked changes must be accepted before submission |
| P4 | ❌ | measured with equations rendered (libreoffice-math installed; original = 12 pages, same as the author's Word): margins +1 → 13, double spacing +4 → 17, added sections/edits +1 → v3 = 18; with the template's exact paragraph spacing (12 pt before, 0 after) = 19 → over 15 |
| P5 | ✅ | v3: no supplementary file (user choice); 4 references changed to "available from the corresponding author on request" (tracked) |
| P6 | ⬜ | |
| P7 | ⬜ | |
| P8 | ✅ | not submitted elsewhere (user) |
| A1 | ✅ | v2: author line + affiliation footnotes; mentor verified on ORCID (Assistant Professor, Physics, KFUPM) and KFUPM Physics faculty list ("Abdallah M. Al-Zahrani") |
| A2 | ✅ | v2: Fajer Almindeel marked * corresponding, email in footnote |
| A3 | ✅ | v2: "Research Mentor" in footnote 2 |
| A4 | ✅ | two authors only (user) |
| A5 | ✅ | no minor contributors (user, 2026-11-07) |
| A6 | ⬜ | |
| E1 | ✅ | v2: "The authors declare no conflict of interest." (user: no conflicts) |
| E2 | ✅ | v2: "This research received no external funding." |
| E3 | ⬜ | |
| E4 | ⬜ | |
| E5 | ⬜ | |
| E6 | ⬜ | |
| E7 | ✅ | no prior submission/publication (user) |
| I1 | ⚠️ | user states AI use for organizing; v3 AI edits are tracked and limited to organization/language of the author's own content → keep a record, inform mentor |
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
| Q2 | ✅ | followed the Guide for Authors: "Fig. N" |
| Q3 | ⬜ | equation alignment |
| Q4 | ⬜ | anonymized file? |

## Run log
_(each stage appends one line: date · stage · version · result summary)_
- 2026-11-07 · Stage 1 · v1 · format check: 11 FAIL / 5 WARN; checker false results fixed after manual verification (abstract heading level, '*' in 'Sagittarius A*', 'fundamental' ≠ funding, 'Figs. 1 and 2')
- 2026-11-07 · Stage 2 · v1 · Crossref: 18/18 DOIs match; refs 1, 2, 3, 11 unindexed books/proceedings
- 2026-11-07 · Stage 0 · v1 · intake partly answered (no funding, no acknowledgments, not submitted elsewhere, no supp files preferred); personal details kept in local paper/intake.md
- 2026-11-07 · Stage 6 · v2 · compliance edits (structure, author block, statements, typography, Fig./ref formats); wording unchanged except headings/cross-refs (verified by word diff); 229 equations byte-identical; checker 11 → 4 FAIL
- 2026-11-07 · Stage 6 · v3 · fixed v2 bugs (body font Arial→Times New Roman per template; Methodology subsections misnumbered 4.1.x→3.x); tracked AI edits: gap paragraph, limitations, supplementary references; equations byte-identical
- 2026-11-07 · P4 · page counts re-measured with the equation module installed (earlier counts drew equations as blank): v1 12, v3 18, exact template spacing 19
