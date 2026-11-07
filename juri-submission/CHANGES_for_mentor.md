# Changes from the mentor's version to the final submission files

Compared: `Bardeen_JURI_Final.docx` (the mentor's version; byte-identical to the file first given to the AI assistant) against `Bardeen_JURI_FINAL_main_BLIND.docx` plus `Bardeen_JURI_FINAL_supplement_BLIND.docx`.

**What did not change:** every equation is the same mathematics, renumbered only; every number, table value, figure and result is the same; every citation is kept. The results were recomputed independently and match: Table 1, Table 2, Eq. (23), the orderings, ϵ꜀ = 0.0809218378978111 and the crossing radii.

To see every edit inside Word: **Review → Compare → Compare documents**, with the mentor's file as *Original* and the final main file as *Revised*.

## Why the changes were made
JURI requirements found on the journal's website and in the submission system:
- the listed sections (Literature Review with a research gap, Methodology, Results and Discussion, limitations in the Conclusions, Acknowledgments),
- a Conflict of Interest statement,
- Nature reference style,
- the Word template's layout (Times New Roman 12 pt, double spacing),
- a limit of **15 pages**,
- anonymous files for review.

In the template's layout the mentor's version runs to 20 pages.

## 1. Structure
| Mentor's version | Final |
|---|---|
| 1. Introduction (6 paragraphs, including the literature) | 1. Introduction (4 paragraphs) + **2. Literature Review** (the 4 literature paragraphs, moved unchanged) |
| 2. Geometry and geodesic equations | **3. Methodology**: Geometry and geodesic equations, plus **3.4 Numerical procedure** (moved from old 4.1) |
| 3. Perturbative results and metric truncation | **4. Results and Discussion**, 4.1 (subsections 4.1.1–4.1.6) |
| 4. Numerical validation and physical interpretation | 4.2 (subsections 4.2.1–4.2.3) |
| — | **Acknowledgments**, **Conflict of Interest** (new) |
| Equations (1)–(35) | (1)–(26) in the main text, (S1)–(S10) in the supplement |
| Figures 1–4, Tables 1–3 | Figs. 1–2 (old Figs. 3 and 4), Tables 1–2 (old Tables 1 and 3); Figs. S1–S2 and Table S1 in the supplement |

## 2. Moved to the supplement (the text itself is unchanged)
- **Note S1:** the extremality-bound paragraph (old §3.1).
- **Note S2:** the first-order derivation steps for the capture radius (old Eqs. 18–21) and the efficiency (old Eqs. 23–26).
- **Note S3:** the full numerical procedure (old §4.1, two paragraphs).
- **Note S4:** old Figs. 1–2 (now Figs. S1–S2), old Table 2 and its paragraph (now Table S1).
- **Note S5:** the crossover parameterization (old Eq. 34) and the root-count paragraph; the worked example at ϵ = 0.10.

## 3. Removed (repetition, signposting, or required by JURI)
- **Introduction**, four result-summary sentences. JURI: the Introduction must not summarise the results.
  - "The second-order coefficients yield five explicit limiting ratios…"
  - "For the horizon, we locate a unique point…"
  - "The separate error budget explains…"
  - "These results extend the cited geodesic and shadow expansions…"
- **Literature Review:** "The existence of charge-dependent orbital radii is therefore established."
- **§3.3:** "Both Eq. (19) and Eq. (21) concern the background metric."
- **§3.6:** "This establishes a local improvement for these particular quantities and metrics." (merged with the next sentence)
- **§4.2:**
  - "Their similar quadratic onset does not make them interchangeable." (from the Fig. 3 caption)
  - "The next subsection determines where that ordering changes for the horizon."
  - "The shaded region is the smaller benchmark interval used for all five quantities." (the figure legend shows it)
- **§4.4:**
  - "The nominal efficiency also omits disk stresses and radiation-transfer corrections.⁵˒⁶"
  - "The numerical range tested here is a benchmark interval, not a universal validity bound…"

  Both are now in the Conclusions' limitations sentence, and refs 5 and 6 are still cited in the Introduction.
- **Conclusions:**
  - "The established geodesic relations and optical expansions provide the starting point and consistency checks."
  - "The coefficient test and the unique crossover are the specific results of the comparison."
  - "Electromagnetic predictions in the NLED interpretation require its optical geometry and radiation transport."
- **Fig. 1 caption:** "Solid curves show the full Bardeen metric, dashed curves… dotted curves…" (the legend shows it)
- **References:** all DOIs (Nature style does not print them); "(1)" changed to "1."; "-" changed to "–" in page ranges.

## 4. New sentences written with AI help (verbatim; please check each)
These restate the authors' own content or replace moved material. They contain no new results, except item 13, which writes out a polynomial the paper already described.

1. **Introduction:** "We quantify how the first omitted metric term affects the accuracy of both predictions and, for the horizon, determine whether this accuracy ordering changes within the common black-hole domain."
2. **Literature Review:** "Rezzolla and Zhidenko developed a general parametrization for comparing spherical black holes,¹⁶…" (two sentences merged)
3. **Research gap, end of the Literature Review:** "These studies do not, however, separate the error introduced by truncating the metric from the error introduced by expanding the orbital solution to first order, nor do they determine which of the two approximations lies closer to the full Bardeen values. This gap motivates the present comparison." ⚠ Please confirm this is fair to Kobialko & Gal'tsov (ref. 19), who treat both inverse-power deformations and the full Bardeen metric.
4. **§3.4:** "We solve the original metric-based equations by bisection, rather than using the first-order expressions to generate comparison data, on a grid of 1,001 equally spaced values of ϵ from 0 to 0.05, and confirm the results with independent 70-digit calculations. Supplementary Note S3 gives the root brackets, stopping rules and admissibility checks." and "The numerical curves are shown in Supplementary Figs. S1 and S2, and a dimensional example for an illustrative mass is given in Supplementary Table S1."
5. **§4.1.1:** "Both metrics also have exact extremality bounds on the charge (Supplementary Note S1). At these bounds the local expansion parameter is no longer small, so first-order orbital formulas should not be extrapolated to them."
6. **§4.1.3:** "Solving Eq. (12) for the truncated function and evaluating the capture radius with the stationary-value argument gives the first-order null-orbit radius and critical impact parameter in Table 1; Supplementary Note S2 gives the steps."
7. **§4.1.4:** "Because the specific energy is stationary along the circular-orbit family at the ISCO, the first-order shift of the efficiency follows from the explicit charge dependence of the truncated-metric energy alone, giving the efficiency coefficients in Table 1 (Supplementary Note S2)."
8. **§4.1.6:** "This local result does not guarantee the ordering at larger charge." and "The algebra and independent numerical checks are available from the corresponding author on request."
9. **§4.2.2:** "Combining Eq. (25) with a parameterization of the full horizon equation reduces the crossover condition to a degree-sixteen polynomial. After an exact rational transformation, Descartes' rule of signs shows that this polynomial has exactly one root on the common outer-horizon branch (Supplementary Note S5). The crossover lies at" and "Supplementary Note S5 gives a worked example at a larger deformation."
10. **Conclusions:** "The study has three main limitations: it concerns only neutral massive particles and background-metric null rays, its numerical error bounds hold only on the sampled benchmark interval, and the nominal efficiency omits disk stresses and radiation-transfer corrections."
11. **Acknowledgments / Conflict of Interest:** "This research received no external funding." and "The authors declare no conflict of interest."
12. **Data and Code Availability:** "Supplementary Notes S1–S5 accompany this article. The authors’ detailed derivation notes (the full accuracy-ratio algebra, the horizon-crossover calculation and a comparison with the closest literature), together with the scripts and data that reproduce all reported values and figures, are available from the corresponding author on reasonable request; no observational data were analysed."
13. **Supplement:**
    - The opening note.
    - The Note headings.
    - "Figs. S1 and S2 show the numerical results on the benchmark grid of Note S3…"
    - "This note gives the steps behind the single crossover stated in Section 4.2.2, starting from Eq. (25)."
    - **Eq. (S10): the explicit polynomial P(u)**, followed by the root-count paragraph: "The substitution u = (9 + 10t)/(10 + 10t) maps t > 0 onto 9/10 < u < 1. The coefficients of (10 + 10t)¹⁶ P(u) … change sign exactly once, and P(9/10) > 0 > P(1) = −24, so P has exactly one root …, u꜀ = 0.968910490219146 …" ⚠ This is the one piece of new mathematics. It was derived from Eqs. (14), (25) and (S9), and checked symbolically and by solving the horizon equations directly. It reproduces ϵ꜀ to all 16 digits. Please compare it with your own Note S2 / scripts.
    - S5.2: "The first-order horizon is therefore the closer of the two at this deformation, consistent with the single crossover reported in Section 4.2.2 of the main text."

## 5. Formatting
- **Template layout:**
  - Times New Roman 12 pt, double spacing, the template's margins and heading styles.
  - Captions in italic, "Fig. N".
- **Size changes:**
  - Figures 13.5 cm wide at 600 dpi.
  - Tables at 10 pt.
- **Anonymity:** author names and affiliations removed from the upload files (journal rule), and kept in the `_named` copies.

## 6. The mentor's original notes
Your version referred to **existing supplementary files**: "Supplementary Notes S1 and S2 give the accuracy-ratio and horizon-crossover calculations, and Note S3 compares their scope with the closest literature", plus the Python code. The final supplement was rebuilt from material in the paper and **reuses the names S1–S5 with different content**. If your original notes exist, the supplement should be merged with them, or replaced by them, before submission.

**Decision (author, 2026-11-07):** the original notes are not submitted. The Data and Code Availability statement now says they are available on request, described by their content (not as "S1–S3", to avoid clashing with the supplement's Notes S1–S5). Please keep them ready in case a reviewer asks.
