# JURI check progress

Keys: ⬜ not started · 🔄 in progress · ✅ done/pass · ❌ fails, fix needed · ⚠️ warning, decide · N/A (with a reason)

**Paper file:** `paper/Bardeen_JURI_v1.docx` (local only, not committed)
**Current version:** FINAL. Upload: `paper/Bardeen_JURI_FINAL_main_BLIND.docx` (15 pp) + `paper/Bardeen_JURI_FINAL_supplement_BLIND.docx` (5 pp). Named copies: `..._main_named.docx`, `..._supplement_named.docx`. Built by `paper/final_build.py` from v6 + `paper/blind_v5.py` + `paper/supp_versions.py`
**Next step:** user: open both files in Word (≤15 pages), decide W3–W5, Turnitin ≤15%, form step 3 AUTHORS, upload main + supplement, check generated PDF, submit.

## Stages
| Stage | Status | Version | Date | Notes |
|---|---|---|---|---|
| 0 Intake | 🔄 | v1 | 2026-11-07 | answered: authors, funding, acknowledgments, prior submission, supp. Pending: AI use, figures, Turnitin, mentor dept, COI, supplementary decision |
| 1 Format check (`check_juri.py`) | ✅ | v1 | 2026-11-07 | 11 FAIL, 5 WARN, report reports/stage1_v1.md |
| 2 References (`/ars-citation-check` + R4) | ✅ | v1 | 2026-11-07 | 18/18 DOIs verified; 4 non-DOI classics for you to confirm |
| 3 Content review (guided `/ars-reviewer`) | ✅ | FINAL | 2026-11-07 | quick mode; all numbers recomputed and matching; W1 (methodology lacked numerical procedure) and W2 fixed; W3–W5 author decisions; report reports/stage3_review.md |
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
| R4 | ✅ | v6: DOIs removed (Nature style); endings '(year).' verified |
| R5 | ⚠️ | 18/18 DOIs resolve and match (Crossref). Refs 1, 2, 3, 11 are books/proceedings with no DOI → YOU confirm details (esp. ref 11 page 174, ref 3 pages 343–450) |
| R6 | ⬜ | |
| R7 | ✅ | no long direct quotes |
| R8 | ⬜ | |
| S1 | ⬜ | |
| S2 | ✅ | 195 words |
| S3 | ⬜ | |
| S4 | ✅ | 6 keywords |
| S5 | ✅ | v6: result summary removed from the Introduction (JURI: Introduction must not summarise results) |
| S6 | ✅ | v3: tracked AI edit adds the research-gap paragraph at the end of the Literature Review (restates the author's own claim from the Introduction, bounded to the cited studies) → YOU accept/reject; check it matches your comparison with Kobialko & Gal'tsov |
| S7 | ✅ | numerical procedure now in Methodology §3.4 (Stage 3 W1) |
| S8 | ✅ | Stage 3: results recomputed independently (Tables 1–2, Eq. 23, crossover) and match |
| S9 | ✅ | v3: tracked AI edit states three limitations explicitly (taken from §4.2.4) |
| S10 | ✅ | v2: ACKNOWLEDGMENTS section added |
| S11 | ✅ | v2: all sections present, in order |
| F1 | ✅ | all 4 figures made by the author with own scripts (user, 2026-11-07) |
| F2 | ✅ | 4 images, 584–600 dpi |
| F3 | ⚠️ | Fig. 2 caption 43 words (optional) |
| F4 | ✅ | v2: captions "Fig. N." |
| F5 | ✅ | 3 table titles, all above their tables |
| F6 | ✅ | Tables 1–3 in order |
| F7 | ✅ | v2: in-text "Fig. N" |
| F8 | ✅ | all figures and tables referred to, in order |
| F9 | ✅ | 35 editable equations, none images |
| F10 | ✅ | FINAL main equations renumbered (1)–(26); every "Eq. (n)" reference checked |
| F11 | ✅ | no non-SI units found |
| F12 | ✅ | figures embedded |
| F13 | ⬜ | |
| F14 | ✅ | author made the figures and can explain them (user) |
| P1 | ✅ | English |
| P2 | ✅ | .docx |
| P3 | ⚠️ | v4: all template paragraph styles matched (Normal TNR 12 double, 12 pt before; Title Arial 14; headings Arial bold, H2/H3 italic; captions italic 12 single, 12 pt after; references 12 single); 20 paragraphs with an undefined "BodyText" style set to Normal; equations kept 12 pt like the template; 11 tracked changes to accept |
| P4 | ✅ | FINAL main: 15 pages double-spaced in the template format (measured with equations rendered) |
| P5 | ✅ | supplement: Notes S1–S5, Eqs. (S1)–(S10) incl. the explicit crossover polynomial (verified symbolically and numerically) |
| P6 | ⬜ | |
| P7 | ⬜ | |
| P8 | ✅ | not submitted elsewhere (user) |
| A1 | ✅ | names NOT in the file (mutual anonymity); enter both authors in form step 3 AUTHORS (still grey in the user's screenshot) |
| A2 | 🔄 | set Fajer Almindeel as corresponding author in form step 3 |
| A3 | 🔄 | add the mentor in form step 3 (role: mentor if the form offers it) |
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
| SUB2 | ✅ | FINAL main and supplement BLIND files: nothing identifying in text, footnotes or file properties (verified) |
| SUB3 | ⬜ | |
| SUB4 | ⬜ | |
| SUB5 | 🔄 | form: steps 1, 2, 4–8 done; step 3 AUTHORS not done; step 9 upload the BLIND file; step 10 create PDF and check it; step 11 submit |
| Q1 | ⬜ | keywords 4–8 |
| Q2 | ✅ | followed the Guide for Authors: "Fig. N" |
| Q3 | ⬜ | equation alignment |
| Q4 | ✅ | submission system: one anonymous manuscript-body file |

## Run log
_(each stage appends one line: date · stage · version · result summary)_
- 2026-11-07 · Stage 1 · v1 · format check: 11 FAIL / 5 WARN; checker false results fixed after manual verification (abstract heading level, '*' in 'Sagittarius A*', 'fundamental' ≠ funding, 'Figs. 1 and 2')
- 2026-11-07 · Stage 2 · v1 · Crossref: 18/18 DOIs match; refs 1, 2, 3, 11 unindexed books/proceedings
- 2026-11-07 · Stage 0 · v1 · intake partly answered (no funding, no acknowledgments, not submitted elsewhere, no supp files preferred); personal details kept in local paper/intake.md
- 2026-11-07 · Stage 6 · v2 · compliance edits (structure, author block, statements, typography, Fig./ref formats); wording unchanged except headings/cross-refs (verified by word diff); 229 equations byte-identical; checker 11 → 4 FAIL
- 2026-11-07 · Stage 6 · v3 · fixed v2 bugs (body font Arial→Times New Roman per template; Methodology subsections misnumbered 4.1.x→3.x); tracked AI edits: gap paragraph, limitations, supplementary references; equations byte-identical
- 2026-11-07 · P4 · page counts re-measured with the equation module installed (earlier counts drew equations as blank): v1 12, v3 18, exact template spacing 19
- 2026-11-07 · Stage 6 · v4 · template styles matched; undefined BodyText style fixed; text and equations unchanged (verified); 20 pages strict template; JURI sample template = 16 pages
- 2026-11-07 · P4 · clarified: double spacing is inferred from the template file, not stated on the website; spacing variants measured (13/14/16/20 pages)
- 2026-11-07 · SUB2 · submission screenshots: mutual anonymity, one file; v5 BLIND files built (no names, changes accepted, metadata scrubbed); checker gains --blind
- 2026-11-07 · P4 · v6 length cuts (tracked); equations identical in symbols and structure (only table symbols 10 pt); 20 → 17 pages double-spaced
- 2026-11-07 · FINAL · main 15 pp + supplement 5 pp; content moved, not deleted; equations renumbered and every reference verified; anonymity verified for both files
- 2026-11-07 · Stage 3 · FINAL · quick review; polynomial P(u) added as Eq. (S10); numerical procedure moved to §3.4; main 15 pp, supplement 5 pp
- 2026-11-07 · P5 · author decision: the author's own original Notes S1–S3 not submitted; Data and Code Availability says they are available on request (described by content); main still 15 pp; anonymous check clean
- 2026-11-07 · P5 · Data and Code Availability simplified: further working notes (the author's own) and scripts available on request
- 2026-11-07 · P4 · Word showed 19 pages with gaps: removed 79 keep-with-next chains (kept headings, figure→caption, table title→table) and set body double spacing to exact 24 pt so inline Cambria Math lines are not taller; LibreOffice now 13 pp main, 4 pp supplement; no clipping
- 2026-11-07 · SUB · system PDF checked: latest main paper, 15 system pages (header/footer/line numbers added), anonymous, equations and figures fine; supplement has no upload slot → email to the editorial office. ABSTRACT heading changed to the main-heading style (bold, not italic)
- 2026-11-07 · F · website re-checked: no changes to any JURI page; figures meet the existing rules (own work, 600 dpi, captions below, Fig. N). Tables 1, 2, S1: exact 14 pt line height in every cell so labels and numbers share a baseline; header row one weight
