#!/usr/bin/env python3
"""Read-only format checker for a JURI (KFUPM) manuscript in .docx form.

Covers the AUTO items in JURI_CHECKLIST.md. It never modifies the paper.

Usage:
    python3 check_juri.py paper.docx [--out report.md] [--no-pdf]

Exit code: 0 if no FAIL, 1 if any FAIL, 2 on a usage error.
"""
from __future__ import annotations

import argparse
import io
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

try:
    import docx  # python-docx
    from docx.oxml.ns import qn
except ImportError:  # pragma: no cover
    sys.exit("python-docx is required: pip install python-docx")

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    Image = None

EMU_PER_INCH = 914400
SUPERSCRIPT_DIGITS = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
SUPERSCRIPT_CHARS = "⁰¹²³⁴⁵⁶⁷⁸⁹"

# Section names in the order the Guide for Authors lists them.
SECTIONS = [
    ("abstract", r"abstract"),
    ("introduction", r"introduction"),
    ("literature review", r"literature\s+review|related\s+work|review\s+of\s+(the\s+)?literature|state\s+of\s+the\s+art"),
    ("methodology", r"method|materials\s+and\s+methods|experimental\s+(program|work|procedure|setup)|research\s+design"),
    ("results and discussion", r"results?"),
    ("conclusions", r"conclusion"),
    ("acknowledgments", r"acknowledg"),
    ("references", r"references|bibliography"),
]

TEMPLATE_LEFTOVERS = [
    "First Author Name", "Second Author Name", "Sub-section 1", "Sub-section 2",
    "Sub-subsection", "Subsection 1", "Subsection 2", "(e.g.", "e.g. Methodology",
    "A Concise and Informative Title", "keyword 1", "u20*******", "XXXX-XXXX",
    "__________", "[insert", "author.email@", "SMPL-ENG-2025-123",
    "This abstract provides a concise summary",
]
ALT_TEXT_LEFTOVERS = ["Description automatically generated", "AI-generated content may be incorrect"]

NON_SI = re.compile(
    r"\d\s?(?:in\.|inch(?:es)?|ft|feet|foot|psi|ksi|lbs?|lbf|pounds?|kips?|°F|ºF|gal(?:lons?)?|"
    r"mi(?:les?)?|mph|oz|yd|yards?|bbl|BTU|Btu|hp|kcal|cal|atm|mmHg|Torr|°R)\b"
)


@dataclass
class Result:
    rid: str
    status: str  # PASS / FAIL / WARN / INFO / MANUAL
    summary: str
    details: list[str] = field(default_factory=list)


def ptext(p_el) -> str:
    """All visible text of a paragraph element, including field results."""
    return "".join(t.text or "" for t in p_el.iter(qn("w:t")))


def is_heading(par) -> int:
    name = (par.style.name or "") if par.style is not None else ""
    m = re.match(r"Heading\s*(\d)", name, re.I)
    if m:
        return int(m.group(1))
    if name.lower() == "title":
        return 0
    return -1


def has_image(el) -> bool:
    return bool(el.findall(".//" + qn("w:drawing"))) or bool(el.findall(".//" + qn("w:pict")))


def has_math(el) -> bool:
    return bool(el.findall(".//{http://schemas.openxmlformats.org/officeDocument/2006/math}oMath"))


def superscript_runs(p_el):
    """Yield the text of superscript runs (citations) in a paragraph element."""
    for r in p_el.iter(qn("w:r")):
        rpr = r.find(qn("w:rPr"))
        sup = False
        if rpr is not None:
            va = rpr.find(qn("w:vertAlign"))
            if va is not None and va.get(qn("w:val")) == "superscript":
                sup = True
        txt = "".join(t.text or "" for t in r.iter(qn("w:t")))
        if sup:
            yield txt
        elif any(c in SUPERSCRIPT_CHARS for c in txt):
            yield "".join(c for c in txt if c in SUPERSCRIPT_CHARS + "⁻,")


def parse_cite_numbers(s: str) -> list[int]:
    s = s.translate(SUPERSCRIPT_DIGITS).replace("⁻", "-").replace("–", "-").replace("—", "-")
    s = s.replace("˒", ",")
    nums: list[int] = []
    for part in re.split(r"[,;\s]+", s.strip()):
        if not part:
            continue
        m = re.fullmatch(r"(\d+)-(\d+)", part)
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            if a <= b and b - a < 200:
                nums.extend(range(a, b + 1))
        elif part.isdigit():
            nums.append(int(part))
    return nums


class Paper:
    def __init__(self, path: Path):
        self.path = path
        self.doc = docx.Document(str(path))
        self.body = self.doc.element.body
        # Ordered blocks: (kind, element, text, paragraph-or-None)
        self.blocks = []
        par_map = {p._p: p for p in self.doc.paragraphs}
        for el in self.body.iterchildren():
            tag = el.tag.split("}")[1]
            if tag == "p":
                self.blocks.append(("p", el, ptext(el), par_map.get(el)))
            elif tag == "tbl":
                self.blocks.append(("tbl", el, "", None))
        self.zip = zipfile.ZipFile(str(path))

    # --- sections -------------------------------------------------------
    def headings(self):
        out = []
        for i, (kind, el, text, par) in enumerate(self.blocks):
            if kind != "p" or par is None or not text.strip():
                continue
            lvl = is_heading(par)
            if lvl >= 1 or (lvl == -1 and self._looks_like_heading(par, text)):
                out.append((i, max(lvl, 1), text.strip()))
        return out

    @staticmethod
    def _looks_like_heading(par, text) -> bool:
        t = text.strip()
        if len(t) > 60 or t.endswith("."):
            return False
        runs = [r for r in par.runs if r.text.strip()]
        return bool(runs) and all(r.bold for r in runs) and bool(
            re.match(r"^(\d+(\.\d+)*\.?\s+)?[A-Z]", t)
        )

    def top_sections(self):
        """Map canonical section -> (block index, heading text), top-level only."""
        found = {}
        for want in (1, 2):
            for i, lvl, text in self.headings():
                if lvl != want:
                    continue
                clean = re.sub(r"^\d+(\.\d+)*\.?\s*", "", text).lower()
                for key, pat in SECTIONS:
                    if key not in found and re.match(rf"^({pat})", clean):
                        found[key] = (i, text)
                        break
        return found

    def section_range(self, key):
        secs = self.top_sections()
        if key not in secs:
            return None
        start = secs[key][0]
        lvl0 = next(l for i, l, _ in self.headings() if i == start)
        nexts = sorted(i for i, lvl, _ in self.headings() if lvl <= lvl0 and i > start)
        end = nexts[0] if nexts else len(self.blocks)
        return start + 1, end

    def section_text(self, key) -> str:
        rng = self.section_range(key)
        if not rng:
            return ""
        return "\n".join(b[2] for b in self.blocks[rng[0]:rng[1]] if b[0] == "p")

    def extra_text(self) -> str:
        """Footnotes, endnotes, headers, footers (author block often lives there)."""
        chunks = []
        for name in self.zip.namelist():
            if re.match(r"word/(footnotes|endnotes|header\d*|footer\d*)\.xml$", name):
                xml = self.zip.read(name).decode("utf8", "replace")
                chunks.append(" ".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", xml)))
        return "\n".join(chunks)


def check(paper: Paper, render_pdf: bool) -> list[Result]:
    R: list[Result] = []
    secs = paper.top_sections()
    blocks = paper.blocks
    ref_rng = paper.section_range("references")
    body_end = ref_rng[0] - 1 if ref_rng else len(blocks)
    all_text = "\n".join(b[2] for b in blocks if b[0] == "p")

    # P2 ------------------------------------------------------------------
    R.append(Result("P2", "PASS" if paper.path.suffix.lower() == ".docx" else "FAIL",
                    f"File type: {paper.path.suffix}"))

    # P1 English (rough: share of ASCII letters among letters)
    letters = [c for c in all_text if c.isalpha()]
    ascii_share = sum(c.isascii() for c in letters) / max(len(letters), 1)
    R.append(Result("P1", "PASS" if ascii_share > 0.95 else "WARN",
                    f"{ascii_share:.0%} of letters are Latin (English expected)."))

    # S11 / section presence ---------------------------------------------
    missing = [k for k, _ in SECTIONS if k not in secs]
    order = [k for k, _ in SECTIONS if k in secs]
    in_order = [secs[k][0] for k in order] == sorted(secs[k][0] for k in order)
    det = [f"Found: " + ", ".join(f"{k} ← '{secs[k][1]}'" for k in order)]
    if missing:
        det.append("Missing (no top-level heading matched): " + ", ".join(missing))
    R.append(Result("S11", "PASS" if not missing and in_order else "FAIL",
                    "All required sections present and in order" if not missing and in_order
                    else ("Section order differs from the Guide for Authors" if not missing
                          else f"{len(missing)} required section(s) not found"),
                    det))
    for rid, key in [("S6", "literature review"), ("S7", "methodology"),
                     ("S8", "results and discussion"), ("S10", "acknowledgments")]:
        R.append(Result(rid, "PASS" if key in secs else "FAIL",
                        f"'{key}' section {'found' if key in secs else 'NOT found'}"
                        + (" (gap/content is checked in guided review)" if rid in ("S6", "S7", "S8") else "")))

    # S2 abstract ----------------------------------------------------------
    abstract = paper.section_text("abstract")
    abs_paras = [t for t in abstract.split("\n") if t.strip() and not re.match(r"\s*key\s*words?", t, re.I)]
    abs_text = " ".join(abs_paras)
    if not abs_paras:
        # Abstract may be a bold run inside a paragraph: "Abstract: ..."
        m = re.search(r"(?is)\babstract\b[:.\s-]*(.+?)(?:\n\s*key\s*words?|\Z)", all_text)
        abs_text = m.group(1) if m else ""
    words = len(re.findall(r"\S+", abs_text))
    R.append(Result("S2", "PASS" if 0 < words <= 250 else "FAIL",
                    f"Abstract word count: {words} (limit 250)" if words else "Abstract not found"))
    abs_cites = []
    rng = paper.section_range("abstract")
    if rng:
        for b in blocks[rng[0]:rng[1]]:
            if b[0] == "p":
                abs_cites += [s for s in superscript_runs(b[1]) if parse_cite_numbers(s)]
    if re.search(r"\[\d+\]|\(\w+[^()]*\d{4}\)", abs_text):
        abs_cites.append("bracketed/author-year citation")
    R.append(Result("S3", "WARN" if abs_cites else "MANUAL",
                    "Abstract contains citations - avoid citing in the abstract" if abs_cites
                    else "No citations in abstract. Content (objectives/methods/results/conclusions) → guided review."))

    # S4 keywords ------------------------------------------------------------
    kw_line = next((b[2] for b in blocks if b[0] == "p" and re.match(r"\s*key\s*words?\s*[:—–-]", b[2], re.I)), None)
    if kw_line is None:
        R.append(Result("S4", "FAIL", "Keywords line not found (expected 'Keywords: a, b, c, d')"))
    else:
        kws = [k.strip(" .") for k in re.split(r"[;,]", re.sub(r"(?i)^\s*key\s*words?\s*[:—–-]\s*", "", kw_line)) if k.strip(" .")]
        R.append(Result("S4", "PASS" if 4 <= len(kws) <= 8 else "FAIL",
                        f"{len(kws)} keywords (required 4-8)", [", ".join(kws)]))

    # S9 conclusions limitations / future work --------------------------------
    concl = paper.section_text("conclusions").lower()
    if not concl:
        R.append(Result("S9", "FAIL", "Conclusions section not found"))
    else:
        lim = bool(re.search(r"limitation|limited\s+(to|by)|constrain|shortcoming|caveat", concl))
        fut = bool(re.search(r"future\s+(work|research|stud)|further\s+(work|research|stud|investigat)|recommend", concl))
        miss = [n for n, ok in [("limitations", lim), ("future work", fut)] if not ok]
        R.append(Result("S9", "PASS" if not miss else "FAIL",
                        "Conclusions mention limitations and future work" if not miss
                        else "Conclusions do not mention: " + ", ".join(miss)))

    # S10 / E2 funding ; E1 COI -------------------------------------------------
    ack = paper.section_text("acknowledgments").lower()
    pre_ref = "\n".join(b[2] for b in blocks[:body_end] if b[0] == "p").lower()
    funding = bool(re.search(r"\bfund(?:ed|ing|s)?\b|\bgrants?\b|financial(?:ly)? support|supported\s+by|sponsor|project\s+(?:no|number)",
                             ack + "\n" + pre_ref[-3000:] + "\n" + paper.extra_text().lower()))
    R.append(Result("E2", "PASS" if funding else "WARN",
                    "Funding statement found" if funding
                    else "No funding wording found. State the funding source, or write 'This research received no external funding.'"))
    coi = bool(re.search(r"conflicts?\s+of\s+interest|competing\s+interests?|declare\s+no", pre_ref + paper.extra_text(), re.I))
    R.append(Result("E1", "PASS" if coi else "FAIL",
                    "Conflict-of-interest statement found" if coi
                    else "No conflict-of-interest statement. Add e.g. 'The authors declare no conflict of interest.'"))

    # A2 / A3 author block ----------------------------------------------------
    abs_i = secs.get("abstract", (8, ""))[0]
    title_i = next((i for i, b in enumerate(blocks) if b[3] is not None and is_heading(b[3]) == 0), -1)
    front_paras = [b[2].strip() for b in blocks[title_i + 1:abs_i] if b[0] == "p" and b[2].strip()]
    front = "\n".join(front_paras) + "\n" + paper.extra_text()
    R.append(Result("A1", "PASS" if front.strip() else "FAIL",
                    f"Author block found ({len(front_paras)} line(s) between title and abstract)" if front.strip()
                    else "No author names/affiliations between the title and the abstract, and none in footnotes"))
    R.append(Result("A3", "PASS" if re.search(r"\bmentor\b", front, re.I) else "FAIL",
                    "Mentor is designated as 'mentor'" if re.search(r"\bmentor\b", front, re.I)
                    else "The word 'mentor' was not found in the author block/footnotes"))
    corr = bool(re.search(r"[A-Za-z]\s?\*|corresponding\s+author", front, re.I))
    R.append(Result("A2", "PASS" if corr else "WARN",
                    "Corresponding author marked" if corr else "No corresponding-author mark (*) found"))

    # P3 template leftovers / alt text -----------------------------------------
    hits = [s for s in TEMPLATE_LEFTOVERS if s.lower() in (all_text + paper.extra_text()).lower()]
    alts = []
    for dp in paper.body.iter("{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}docPr"):
        d = (dp.get("descr") or "") + " " + (dp.get("title") or "")
        if any(a.lower() in d.lower() for a in ALT_TEXT_LEFTOVERS):
            alts.append(d.strip()[:80])
    doc_xml = paper.zip.read("word/document.xml").decode("utf8", "replace")
    n_ins, n_del = len(re.findall(r"<w:ins ", doc_xml)), len(re.findall(r"<w:del ", doc_xml))
    n_com = len(re.findall(r"<w:comment ", paper.zip.read("word/comments.xml").decode("utf8", "replace"))) \
        if "word/comments.xml" in paper.zip.namelist() else 0
    if n_ins or n_del:
        hits.append(f"{n_ins + n_del} tracked change(s) not accepted")
    if n_com:
        hits.append(f"{n_com} Word comment(s) left in the file")
    normal = paper.doc.styles["Normal"]
    fnt = normal.font.name or "theme default"
    ls = normal.paragraph_format.line_spacing
    R.append(Result("P3b", "INFO",
                    f"Body typography: {fnt}, line spacing {ls if ls else 'default'}. The JURI template uses Arial 12 pt, "
                    "double spacing, margins 2.54/3.17/2.54/1.79 cm - page count changes if you move to the template."))
    R.append(Result("P3", "FAIL" if hits or alts else "PASS",
                    "No template placeholder text left" if not (hits or alts) else "Template leftovers found",
                    [f"placeholder: '{h}'" for h in hits] + [f"auto alt text: '{a}'" for a in alts]))

    # Figures / tables / captions ----------------------------------------------
    cap_re = re.compile(r"^\s*(Figure|Fig\.?|Table)\s*(\d+)?\s*[.:]?", re.I)
    real_cap = re.compile(r"^\s*(Figure|Fig\.?|Table)\s*\d*\s*[.:]\s", re.I)
    misstyled = []
    fig_caps, tab_caps, cap_issues = [], [], []

    def nonempty_neighbor(i, step):
        j = i + step
        while 0 <= j < len(blocks):
            k, el, t, _ = blocks[j]
            if k == "tbl" or t.strip() or has_image(el):
                return j
            j += step
        return None

    for i, (kind, el, text, par) in enumerate(blocks[:body_end]):
        if kind != "p":
            continue
        m = cap_re.match(text)
        if not m or len(text) > 400:
            continue
        style = (par.style.name if par is not None and par.style is not None else "")
        if not real_cap.match(text):
            continue  # an ordinary sentence starting with "Table 1 shows..."
        label, num = m.group(1), m.group(2)
        if label.lower().startswith("tab"):
            nxt = nonempty_neighbor(i, +1)
            above = nxt is not None and blocks[nxt][0] == "tbl" and not has_image(blocks[nxt][1])
            tab_caps.append((num, text.strip()))
            if not above:
                cap_issues.append(("F5", f"'{text.strip()[:60]}' is not directly above a table"))
        else:
            prv = nonempty_neighbor(i, -1)
            below = prv is not None and has_image(blocks[prv][1])
            fig_caps.append((label, num, text.strip()))
            if not below:
                cap_issues.append(("F3", f"'{text.strip()[:60]}' is not directly below a figure"))
            if len(re.findall(r"\S+", text)) > 40:
                cap_issues.append(("F3", f"Caption is long ({len(text.split())} words): '{text.strip()[:50]}...'"))

    for i, (kind, el, text, par) in enumerate(blocks[:body_end]):
        if kind == "p" and par is not None and par.style is not None and par.style.name.lower() == "caption" \
                and text.strip() and not real_cap.match(text):
            misstyled.append(text.strip()[:70])
    R.append(Result("F3b", "FAIL" if misstyled else "PASS",
                    f"{len(misstyled)} body paragraph(s) use the Caption style (Word treats them as captions)"
                    if misstyled else "No body text in Caption style", misstyled))
    n_images = sum(1 for b in blocks[:body_end] if has_image(b[1]) and not has_math(b[1]))
    R.append(Result("F3", "PASS" if fig_caps and not [x for x in cap_issues if x[0] == "F3"] else ("INFO" if not fig_caps else "FAIL"),
                    f"{len(fig_caps)} figure captions; {sum(1 for x in cap_issues if x[0]=='F3')} position/length issue(s)"
                    if fig_caps else "No figure captions detected",
                    [d for r_, d in cap_issues if r_ == "F3"]))
    R.append(Result("F5", "PASS" if not [x for x in cap_issues if x[0] == "F5"] else "FAIL",
                    f"{len(tab_caps)} table titles; {sum(1 for x in cap_issues if x[0]=='F5')} not above their table",
                    [d for r_, d in cap_issues if r_ == "F5"]))

    fig_labels = {lbl for lbl, _, _ in fig_caps}
    fig_nums = [int(n) for _, n, _ in fig_caps if n]
    no_num = [t for _, n, t in fig_caps if not n]
    det = []
    if any(not l.lower().startswith("fig.") and l.lower() != "fig" for l in fig_labels):
        det.append("Captions use 'Figure'; the Guide for Authors shows 'Fig.1' (see Q2)")
    if no_num:
        det.append(f"{len(no_num)} caption(s) without a visible number - check Word caption fields are updated (Ctrl+A, F9)")
    if fig_nums and fig_nums != list(range(1, len(fig_nums) + 1)):
        det.append(f"Figure numbers are not 1..n in order: {fig_nums}")
    R.append(Result("F4", "PASS" if not det else ("FAIL" if "not 1..n" in " ".join(det) else "WARN"),
                    "Figure numbering" + (" OK" if not det else " needs attention"), det))
    tab_nums = [int(n) for n, _ in tab_caps if n]
    tdet = [] if tab_nums == list(range(1, len(tab_nums) + 1)) else [f"Table numbers not 1..n in order: {tab_nums}"]
    if any(not n for n, _ in tab_caps):
        tdet.append("Some table titles show no number - update caption fields")
    R.append(Result("F6", "PASS" if not tdet else "FAIL", "Table numbering" + (" OK" if not tdet else " issues"), tdet))

    # F7 / F8 in-text references to figures and tables ------------------------
    body_paras = [b[2] for b in blocks[:body_end] if b[0] == "p" and not real_cap.match(b[2] or "")]
    body_txt = "\n".join(body_paras)
    long_form = re.findall(r"\bFigures?\s+\d+", body_txt)
    def mentions(pat):
        out = []
        for m in re.finditer(pat + r"\s*(\d+(?:\s*(?:,|and|&|[-–])\s*\d+)*)", body_txt):
            out += parse_cite_numbers(re.sub(r"and|&", ",", m.group(1)))
        return out
    refs_fig = mentions(r"\b(?:Figures?|Figs?\.?)")
    refs_tab = mentions(r"\bTables?")
    f7 = []
    if long_form:
        f7.append(f"{len(long_form)} in-text 'Figure N' mention(s); the guide's format is '(Fig. N)'. e.g. {long_form[:3]}")
    R.append(Result("F7", "PASS" if not f7 else "WARN", "In-text figure/table reference format", f7))
    f8 = []
    for kind_, nums_, total in (("Fig.", refs_fig, len(fig_caps)), ("Table", refs_tab, len(tab_caps))):
        never = [n for n in range(1, total + 1) if n not in nums_]
        if never:
            f8.append(f"{kind_} {never} never referred to in the text")
        first = list(dict.fromkeys(nums_))
        if first and first != sorted(first):
            f8.append(f"{kind_} first mentioned out of order: {first}")
        ghost = sorted({n for n in nums_ if n > total})
        if ghost and total:
            f8.append(f"Text refers to {kind_} {ghost} which have no caption")
    R.append(Result("F8", "PASS" if not f8 else "FAIL", "Every figure/table cited in order", f8))

    # F12 embedded
    R.append(Result("F12", "PASS" if n_images or not fig_caps else "FAIL",
                    f"{n_images} embedded image block(s) in the body"))

    # F2 resolution ------------------------------------------------------------
    rels = paper.doc.part.rels
    dpi_rows = []
    for inline in paper.body.iter(qn("wp:inline"), qn("wp:anchor")):
        ext = inline.find(qn("wp:extent"))
        blip = inline.find(".//{http://schemas.openxmlformats.org/drawingml/2006/main}blip")
        if ext is None or blip is None:
            continue
        rid = blip.get(qn("r:embed"))
        if rid not in rels or Image is None:
            continue
        part = rels[rid].target_part
        name = Path(str(part.partname)).name
        if name.lower().endswith((".svg", ".emf", ".wmf")):
            dpi_rows.append((name, None, "vector (OK)"))
            continue
        try:
            im = Image.open(io.BytesIO(part.blob))
            w_in = int(ext.get("cx")) / EMU_PER_INCH
            dpi = im.size[0] / w_in if w_in else 0
            dpi_rows.append((name, dpi, f"{im.size[0]}x{im.size[1]} px at {w_in*2.54:.1f} cm wide"))
        except Exception as e:  # noqa: BLE001
            dpi_rows.append((name, None, f"unreadable ({e.__class__.__name__})"))
    low = [r for r in dpi_rows if r[1] is not None and r[1] < 295]
    high = [r for r in dpi_rows if r[1] is not None and r[1] > 605]
    R.append(Result("F2", "FAIL" if low else ("WARN" if high else ("PASS" if dpi_rows else "INFO")),
                    (f"{len(dpi_rows)} image(s); {len(low)} below 300 dpi, {len(high)} above 600 dpi "
                     "(guide: 300-600)") if dpi_rows else "No raster images found",
                    [f"{n}: {d:.0f} dpi ({s})" if d else f"{n}: {s}" for n, d, s in dpi_rows]))

    # F9 / F10 equations ---------------------------------------------------------
    eq_num_re = re.compile(r"\((\d+)\)\s*$")
    eq_numbers, img_eqs = [], []
    for kind, el, text, par in blocks[:body_end]:
        units = [el] if kind == "p" else el.findall(".//" + qn("w:tr"))
        for u in units:
            t = ptext(u).strip()
            m = eq_num_re.search(t)
            if not m:
                continue
            short = len(re.sub(r"\(\d+\)\s*$", "", t).strip()) < 120
            if has_math(u):
                eq_numbers.append(int(m.group(1)))
            elif has_image(u) and short:
                img_eqs.append(t[:60])
    R.append(Result("F9", "FAIL" if img_eqs else "PASS",
                    f"{len(img_eqs)} numbered equation(s) appear to be images" if img_eqs
                    else f"{len(eq_numbers)} numbered editable equation(s); none are images", img_eqs))
    R.append(Result("F10", "PASS" if eq_numbers == list(range(1, len(eq_numbers) + 1)) else "FAIL",
                    f"Equation numbers: {eq_numbers or 'none'}"
                    + ("" if eq_numbers == list(range(1, len(eq_numbers) + 1)) else " - not consecutive"),
                    ["Centring and right-aligned numbers: check visually (YOU)"]))

    # F11 SI units ------------------------------------------------------------------
    non_si = sorted(set(m.group(0) for m in NON_SI.finditer(body_txt)))
    R.append(Result("F11", "WARN" if non_si else "PASS",
                    f"{len(non_si)} possible non-SI unit(s)" if non_si else "No common non-SI units found",
                    non_si[:20]))

    # R1-R4 citations -----------------------------------------------------------------
    cited_order = []
    other_styles = []
    for kind, el, text, par in blocks[:body_end]:
        if kind == "p" and cap_re.match(text or "") is None:
            pass
        for s in superscript_runs(el):
            cited_order += parse_cite_numbers(s)
        other_styles += re.findall(r"\[\d+(?:[,–-]\s*\d+)*\]", text or "")
        other_styles += re.findall(r"\([A-Z][A-Za-z-]+(?: et al\.| and [A-Z][a-z]+| & [A-Z][a-z]+)?,? (?:19|20)\d{2}[a-z]?\)", text or "")
    ref_entries = []
    if ref_rng:
        for b in blocks[ref_rng[0]:ref_rng[1]]:
            if b[0] == "p" and b[2].strip():
                ref_entries.append((b[2].strip(), b[1]))
    n_refs = len(ref_entries)
    det = []
    if other_styles:
        det.append(f"Non-Nature citation markers found (use superscript numbers): {sorted(set(other_styles))[:8]}")
    if not cited_order:
        det.append("No superscript citation numbers found in the text")
    R.append(Result("R1", "FAIL" if det else "PASS",
                    f"{len(cited_order)} superscript citation number(s) in the text" if not det else "In-text citation style problems", det))
    first = list(dict.fromkeys(cited_order))
    expected = list(range(1, len(first) + 1))
    R.append(Result("R2", "PASS" if first == expected else "FAIL",
                    "References numbered in order of first citation" if first == expected
                    else "Order of first citation is not 1, 2, 3, ...",
                    [] if first == expected else [f"First-appearance order: {first[:40]}"]))
    uncited = [n for n in range(1, n_refs + 1) if n not in first]
    ghost = sorted({n for n in first if n > n_refs})
    det = []
    if uncited:
        det.append(f"In list but never cited: {uncited}")
    if ghost:
        det.append(f"Cited but not in list (list has {n_refs}): {ghost}")
    if not ref_rng:
        det.append("References section not found")
    R.append(Result("R3", "PASS" if not det else "FAIL", f"{n_refs} reference entries; cross-check with text", det))

    fmt_issues = []
    bold_vol = 0
    paren_numbered = False
    for k, (txt, el) in enumerate(ref_entries, 1):
        if re.match(r"^\s*[\[(]\d+[\])]", txt):
            paren_numbered = True
        t = re.sub(r"^\s*[\[(]?\d+[.)\]]\s*", "", txt)
        probs = []
        if not re.search(r"(?:\(|,\s)(?:1[5-9]|20)\d{2}[a-z]?\)\.?\s*(https?://\S+|doi:\s?\S+)?\s*$", t):
            probs.append("does not end with '(year).'")
        # Author segment ends after the last initial (or "et al.") that precedes the title.
        m_auth = re.match(r"^((?:[^.]*?(?:\b[A-Z]\.|et al\.)[\s-]*)+?)(?=\s*[A-Z0-9][a-z0-9]{1,}\b(?!\.))", t)
        authors_seg = m_auth.group(1) if m_auth else ""
        if re.search(r"\band\b", authors_seg):
            probs.append("uses 'and' between authors (Nature uses '&')")
        n_auth = len(re.findall(r"[A-Z][A-Za-z'’-]+, (?:[A-Z]\.[ -]?)+", t[:400]))
        if n_auth > 5 and "et al." not in t[:200]:
            probs.append(f"{n_auth} authors listed - Nature lists the first author + 'et al.' when there are more than five")
        runs = el.findall(qn("w:r"))
        if any((r.find(qn("w:rPr")) is not None and r.find(qn("w:rPr")).find(qn("w:b")) is not None
                and re.fullmatch(r"\s*\d+\s*", "".join(x.text or "" for x in r.iter(qn("w:t")))))
               for r in runs):
            bold_vol += 1
        if probs:
            fmt_issues.append(f"Ref {k}: " + "; ".join(probs) + f" — '{t[:70]}...'")
    if paren_numbered:
        fmt_issues.insert(0, "Reference list numbered '(1)' / '[1]'; Nature numbers the list '1.', '2.'")
    if ref_entries and bold_vol < len(ref_entries) * 0.5:
        fmt_issues.append(f"Only {bold_vol}/{n_refs} entries have a bold volume number (Nature: **vol**)")
    R.append(Result("R4", "PASS" if not fmt_issues else "WARN",
                    "Reference list pattern looks like Nature style" if not fmt_issues
                    else f"{len(fmt_issues)} reference formatting issue(s) to check", fmt_issues[:40]))

    # R7 quotations --------------------------------------------------------------------
    quotes = re.findall(r"[\"“]([^\"”]{25,})[\"”]", body_txt)
    R.append(Result("R7", "MANUAL" if quotes else "PASS",
                    f"{len(quotes)} direct quotation(s): confirm each is cited" if quotes else "No long direct quotations found",
                    [q[:70] for q in quotes[:10]]))

    # SUB2 anonymization hints ------------------------------------------------------------
    selfref = re.findall(r"(?i)\b(our (?:previous|earlier|prior) (?:work|study|paper)|in our lab|we previously (?:reported|showed))\b", body_txt)
    R.append(Result("SUB2", "INFO",
                    "Double-anonymized review: if a blinded file is required, remove names, affiliations, acknowledgments"
                    + (f"; self-identifying phrases found: {sorted(set(selfref))}" if selfref else "")))

    # P4 page count ------------------------------------------------------------------------
    pages, how = None, ""
    if render_pdf and shutil.which("soffice"):
        with tempfile.TemporaryDirectory() as td:
            try:
                subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", td, str(paper.path)],
                               check=True, capture_output=True, timeout=180)
                pdf = next(Path(td).glob("*.pdf"))
                data = pdf.read_bytes()
                pages = len(re.findall(rb"/Type\s*/Page[^s]", data))
                how = "rendered with LibreOffice (may differ from Word by about ±1 page)"
            except Exception as e:  # noqa: BLE001
                how = f"PDF render failed ({e.__class__.__name__})"
    if pages is None:
        try:
            app = paper.zip.read("docProps/app.xml").decode("utf8", "replace")
            m = re.search(r"<Pages>(\d+)</Pages>", app)
            if m:
                pages, how = int(m.group(1)), "from Word's last-saved page count"
        except KeyError:
            pass
    R.append(Result("P4", "INFO" if pages is None else ("PASS" if pages <= 15 else "FAIL"),
                    f"{pages} pages (limit 15; {how})" if pages else f"Page count unavailable ({how})"))

    return R


ORDER = ["P1", "P2", "P3", "P3b", "P4", "S2", "S3", "S4", "S6", "S7", "S8", "S9", "S10", "S11",
         "R1", "R2", "R3", "R4", "R7", "F2", "F3", "F3b", "F4", "F5", "F6", "F7", "F8", "F9",
         "F10", "F11", "F12", "A1", "A2", "A3", "E1", "E2", "SUB2"]


def render(results: list[Result], paper: Path) -> str:
    results = sorted(results, key=lambda r: ORDER.index(r.rid) if r.rid in ORDER else 99)
    icon = {"PASS": "✅", "FAIL": "❌", "WARN": "⚠️", "INFO": "ℹ️", "MANUAL": "👀"}
    counts = {s: sum(r.status == s for r in results) for s in icon}
    lines = [f"# JURI automated check: {paper.name}", "",
             " · ".join(f"{icon[s]} {s} {n}" for s, n in counts.items() if n), "",
             "| ID | Status | Result |", "|---|---|---|"]
    for r in results:
        lines.append(f"| {r.rid} | {icon[r.status]} {r.status} | {r.summary} |")
    lines += ["", "## Details", ""]
    for r in results:
        if r.details:
            lines.append(f"**{r.rid}**")
            lines += [f"- {d}" for d in r.details]
            lines.append("")
    lines.append("_Read-only check. Items marked YOU/REVIEW/CITE in JURI_CHECKLIST.md are not covered here._")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paper", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--no-pdf", action="store_true", help="skip LibreOffice page-count render")
    ap.add_argument("--blind", action="store_true",
                    help="anonymous submission file: names/affiliations must be ABSENT (JURI mutual anonymity)")
    a = ap.parse_args()
    if not a.paper.is_file():
        print(f"not found: {a.paper}", file=sys.stderr)
        return 2
    paper = Paper(a.paper)
    results = check(paper, render_pdf=not a.no_pdf)
    if a.blind:
        results = [r for r in results if r.rid not in ("A1", "A2", "A3")]
        front = paper.extra_text() + "\n" + "\n".join(b[2] for b in paper.blocks[:6])
        hits = sorted(set(re.findall(r"(?i)\b(?:mentor|corresponding author|e-?mail|orcid|university|department of)\b|@\w", front)))
        props = paper.zip.read("docProps/core.xml").decode("utf8", "replace")
        creator = re.findall(r"<dc:creator>([^<]+)<|<cp:lastModifiedBy>([^<]+)<", props)
        results.append(Result("SUB2", "FAIL" if hits or creator else "PASS",
                              "Anonymous file: no names/affiliations in the front matter or file properties"
                              if not (hits or creator) else "Identifying information found in the anonymous file",
                              [f"text: {h}" for h in hits] + [f"file property: {c}" for c in creator]))
        results = [r for r in results if not (r.rid == "SUB2" and r.status == "INFO")]
    report = render(results, a.paper)
    if a.out:
        a.out.write_text(report, encoding="utf8")
    print(report)
    return 1 if any(r.status == "FAIL" for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
