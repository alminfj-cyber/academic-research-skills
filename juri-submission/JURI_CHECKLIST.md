# JURI Submission Checklist

Journal: **Journal of Undergraduate Research International (JURI)**, KFUPM.
Course: RES200.

Rules were taken from the official pages on 2026-11-07:

- [Guide for Authors](https://www.journalssystem.com/juri/Guide-for-Authors,5291.html) (GA)
- [Authorship Policy](https://www.journalssystem.com/juri/Authorship-Policy,5308.html) (AP)
- [AI Guidelines](https://www.journalssystem.com/juri/AI-Guidelines,5294.html) (AI)
- [Research Ethics Policy](https://www.journalssystem.com/juri/Research-Ethics-Policy,5293.html) (RE)
- [Plagiarism Policy](https://www.journalssystem.com/juri/Plagiarism-Policy,5296.html) (PP)
- [Peer Review Process](https://www.journalssystem.com/juri/Peer-Review-Process,5292.html) (PR)
- [Journal Submission Scope](https://www.journalssystem.com/juri/Journal-Submission-Scope,5315.html) (SC)
- [Open Access](https://www.journalssystem.com/juri/Open-Access,5295.html) (OA)

Each rule has an ID. `PROGRESS.md` records the status of each ID.

## Who checks what

| Code | Checked by |
|---|---|
| **AUTO** | `check_juri.py`, run on your .docx. It finds the problem without changing your file. |
| **CITE** | `/ars-citation-check`, which looks up each reference in Crossref, OpenAlex, Semantic Scholar and arXiv. |
| **REVIEW** | `/ars-reviewer` in **guided** mode. It asks questions and points out problems; you make every fix. |
| **YOU** | Only you can confirm it. Answer the question and the status is recorded. |
| **ASK** | The rule is unclear. Confirm it with your mentor or with juri-dr@kfupm.edu.sa. |

All of these tools only check. None of them rewrites your paper, which keeps you within the AI rule (I1–I4).

---

## R: References (GA, PP)
| ID | Rule | Check |
|---|---|---|
| R1 | Nature style for in-text citations: superscript numbers (¹, ²˒³, ⁴⁻⁶) | AUTO |
| R2 | Citations are numbered in the order they first appear in the text | AUTO |
| R3 | Every reference in the list is cited, and every cited number is in the list | AUTO |
| R4 | Each reference is in Nature format: `Surname, A. B., Surname, C. & Surname, D. Title. *Abbrev. Journal* **vol**, pages (year).` More than 5 authors becomes "First, A. et al." | AUTO (pattern) + YOU |
| R5 | Every reference exists, and its details (DOI, year, volume) are correct | CITE |
| R6 | Every word, piece of data or idea taken from someone else is cited | REVIEW + YOU |
| R7 | Direct quotes are in quotation marks and cited | AUTO (finds quotes) + YOU |
| R8 | The paper cites relevant literature, both directly cited and general works | REVIEW |

## S: Manuscript structure (GA)
| ID | Rule | Check |
|---|---|---|
| S1 | The title is concise, informative and reflects the study's core | REVIEW |
| S2 | The abstract is **250 words or fewer** | AUTO |
| S3 | The abstract covers objectives, methods, key results and conclusions | REVIEW |
| S4 | There are **4–8 keywords**, each technically precise | AUTO (count) + REVIEW |
| S5 | The Introduction gives the objectives and background, with **no** extensive literature review and **no** summary of results | REVIEW |
| S6 | There is a separate **Literature Review / Related Work** section that states the **research gap** | AUTO (section present) + REVIEW (gap) |
| S7 | The Methodology concisely describes the subject, design, tools and procedures | AUTO (present) + REVIEW |
| S8 | Results and Discussion includes the results, critical analysis, and a **comparison with the latest work worldwide** | AUTO (present) + REVIEW |
| S9 | The Conclusions summarize the results and include the **limitations** and **future work** | AUTO (keywords) + REVIEW |
| S10 | The Acknowledgments name contributors and **funding** sources | AUTO (present) + YOU |
| S11 | The sections appear in the order the journal lists them | AUTO |

## F: Figures, tables, equations and units (GA, AI)
| ID | Rule | Check |
|---|---|---|
| F1 | Figures are **designed by you** and not taken or adapted from any source | YOU |
| F2 | Figure resolution is **300–600 dpi** | AUTO (calculated from each image's pixels and printed size) |
| F3 | Figure captions are **below** the figure, concise and short | AUTO |
| F4 | Figures are numbered with Arabic numerals in the **"Fig. 1"** form | AUTO |
| F5 | Table titles are **above** the table, clear and concise | AUTO |
| F6 | Tables are numbered with Arabic numerals in the **"Table 1"** form | AUTO |
| F7 | References in the text use the form **(Fig. 4, Table 1)** | AUTO |
| F8 | Every figure and table is referred to in the text, in numerical order | AUTO |
| F9 | Equations are **editable** (made in Word's equation editor) and **not images** | AUTO |
| F10 | Equations are centred, with consecutive numbers (1), (2) on the right | AUTO (numbering) + YOU (layout) |
| F11 | All units are **SI** | AUTO (flags non-SI units) + YOU |
| F12 | Figures and tables are **embedded** in the text, not uploaded separately | AUTO + YOU |
| F13 | Excel charts are pasted with Paste Special as PNG or SVG | YOU |
| F14 | You can explain every figure, table and finding yourself, without AI | YOU |

## P: Preparation and scope (GA, SC)
| ID | Rule | Check |
|---|---|---|
| P1 | The paper is in English | AUTO |
| P2 | The file is in Word format (.docx) | AUTO |
| P3 | The file follows the journal's Word template | AUTO (leftover template text) + YOU |
| P4 | The paper is **15 pages or fewer** | AUTO (actual pages, from a PDF render) |
| P5 | Anything beyond the page limit goes in a **separate** supplementary file that starts with the title, authors and affiliations | YOU |
| P6 | The article is an **Original Article** presenting new research (empirical, theoretical, technical or analytical) | REVIEW + YOU |
| P7 | The field is on the journal's list of 26 subject areas | YOU |
| P8 | The work is unpublished and **not under review at another journal** | YOU |

## A: Authorship (AP)
| ID | Rule | Check |
|---|---|---|
| A1 | The first author is the undergraduate who did the research and wrote the draft | YOU |
| A2 | The first author is the corresponding author and submits the paper | AUTO (finds the * mark) + YOU |
| A3 | The mentor is **labelled "mentor"** | AUTO |
| A4 | Any other author made a significant contribution | YOU |
| A5 | People who made minor contributions are thanked in the Acknowledgments | YOU |
| A6 | Every author helped write the paper, can explain their part, and approved the submission | YOU |

## E: Ethics and disclosure (GA, RE, PP)
| ID | Rule | Check |
|---|---|---|
| E1 | All conflicts of interest, financial or personal, are disclosed. If there are none, the paper says so. | AUTO (statement present) + YOU |
| E2 | Financial support is clearly acknowledged | AUTO (funding wording) + YOU |
| E3 | If the study involved people or animals, it has institutional approval (KFUPM IRB) | YOU |
| E4 | No data is fabricated, falsified or selectively reported | YOU |
| E5 | No one else's work or data is used improperly | YOU |
| E6 | Any reused table, graphic or long passage has permission and a citation (F1 forbids borrowed figures anyway) | YOU |
| E7 | No self-plagiarism: earlier work of yours, such as a course report, is cited if reused | YOU |

## I: AI use (AI)
| ID | Rule | Check |
|---|---|---|
| I1 | AI was used only to improve readability and fluency | YOU |
| I2 | No ideas, analysis or findings came from AI | YOU |
| I3 | You checked every sentence that AI touched | YOU |
| I4 | No AI-generated text was copied without a citation | YOU + PL1 |
| I5 | RES200's own AI rules are followed (the course, not the journal) | YOU / ASK the instructor |

## PL: Plagiarism (PP)
| ID | Rule | Check |
|---|---|---|
| PL1 | Turnitin similarity is **15% or less**, excluding references and common phrases (15–30% means further review; over 30% means rejection) | YOU (KFUPM Turnitin report) |

## SUB: Submission (GA, PR)
| ID | Rule | Check |
|---|---|---|
| SUB1 | Submit online through the [Editorial System](https://www.editorialsystem.com/juri/) (no fees) | YOU |
| SUB2 | Peer review is **double-anonymized**: check whether the system asks for a blinded file without names, affiliations or acknowledgments | YOU / ASK |
| SUB3 | Any reviewers you suggest have no conflict of interest | YOU |
| SUB4 | The paper passes the Editorial Board's first compliance check (every AUTO item passes) | AUTO summary |
| SUB5 | Every field the submission form asks for is filled. The form couldn't be read in advance; check at login for a cover letter, ORCID, or declarations. | YOU |

## Q: Unclear rules to confirm
| ID | Question |
|---|---|
| Q1 | Keywords: "a maximum of 4-8" is read here as "between 4 and 8". |
| Q2 | Fig. or Figure: the guidelines say "Fig.1" and "(Fig.4, Table 1.)", but the template's sample text uses "Figure 1". The guidelines are followed here. |
| Q3 | Equation layout: "center justified… and right justified" is read here as the equation centred and its number on the right. |
| Q4 | Does a double-anonymized review need a separate anonymized file? (SUB2) |
