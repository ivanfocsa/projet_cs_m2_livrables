#!/usr/bin/env python3
"""Generate Yvan FOCSA presentation deliverables.

Outputs:
- PDF versions of the Yvan Markdown support files.
- PNG diagrams for video/soutenance.
- A Draw.io architecture file that can be opened and edited in diagrams.net.
"""

from __future__ import annotations

import html
import re
import textwrap
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    Flowable,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
YVAN = ROOT / "livrables" / "yvan"
PDF_DIR = YVAN / "pdf"
DIAGRAM_DIR = YVAN / "diagrams"


PDF_SOURCES = [
    (
        YVAN / "00_A_LIRE_DOSSIER_YVAN_FINAL.md",
        "00_A_LIRE_DOSSIER_YVAN_FINAL.pdf",
        "Dossier final Yvan FOCSA - a lire en premier",
    ),
    (YVAN / "README_YVAN.md", "00_Dossier_Yvan_Mode_Emploi.pdf", "Dossier Yvan - Mode d'emploi"),
    (YVAN / "01_etat_avancement_yvan.md", "01_Etat_Avancement_Yvan.pdf", "Etat d'avancement - Yvan FOCSA"),
    (YVAN / "02_script_oral_yvan_3_5_min.md", "02_Script_Oral_Yvan.pdf", "Script oral Yvan"),
    (YVAN / "03_supports_a_montrer.md", "03_Supports_A_Montrer.pdf", "Supports a montrer - Yvan"),
    (YVAN / "04_questions_reponses_jury_yvan.md", "04_Questions_Reponses_Jury_Yvan.pdf", "Questions reponses jury - Yvan"),
    (YVAN / "05_checklist_finale_yvan.md", "05_Checklist_Finale_Yvan.pdf", "Checklist finale - Yvan"),
    (YVAN / "06_script_video_yvan_final.md", "06_Script_Video_Yvan_Final.pdf", "Script video final - Yvan"),
    (
        YVAN / "07_stack_technique_concrete_yvan.md",
        "07_Stack_Technique_Concrete_Yvan.pdf",
        "Stack technique concrete - Yvan",
    ),
    (
        YVAN / "supports" / "00_ORDRE_OUVERTURE_SUPPORTS.md",
        "00_Ordre_Ouverture_Supports.pdf",
        "Ordre d'ouverture des supports Yvan",
    ),
    (
        YVAN / "supports" / "Yvan_FOCSA_Cadrage_Architecture_Organisation.md",
        "Yvan_FOCSA_Cadrage_Architecture_Organisation.pdf",
        "Cadrage, architecture et organisation - Yvan",
    ),
    (
        YVAN / "supports" / "Yvan_FOCSA_Script_Video_Demo.md",
        "Yvan_FOCSA_Script_Video_Demo.pdf",
        "Script video demo - Yvan",
    ),
    (
        YVAN / "supports" / "Yvan_FOCSA_rendu_individuel_v1.md",
        "Yvan_FOCSA_Rendu_Individuel_Source.pdf",
        "Rendu individuel source - Yvan",
    ),
    (
        YVAN / "supports" / "09_Matrice_Conformite_Cahier_Charges.md",
        "Matrice_Conformite_Cahier_Charges.pdf",
        "Matrice de conformite au cahier des charges",
    ),
    (
        YVAN / "supports" / "client_onboarding_checklist.md",
        "Checklist_Onboarding_Client.pdf",
        "Checklist onboarding client",
    ),
]


def ensure_dirs() -> None:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    DIAGRAM_DIR.mkdir(parents=True, exist_ok=True)


def clean_inline(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text.replace("&", "&amp;")


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="DocTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=22,
            textColor=colors.HexColor("#2457D6"),
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="H1x",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=15,
            leading=18,
            textColor=colors.HexColor("#172033"),
            spaceBefore=10,
            spaceAfter=7,
        )
    )
    styles.add(
        ParagraphStyle(
            name="H2x",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=15,
            textColor=colors.HexColor("#172033"),
            spaceBefore=8,
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Bodyx",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.4,
            leading=13.2,
            alignment=TA_LEFT,
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Smallx",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=7.4,
            leading=9.2,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Codex",
            parent=styles["Code"],
            fontName="Courier",
            fontSize=7.4,
            leading=9.2,
            backColor=colors.HexColor("#F5F7FB"),
            borderPadding=3,
            spaceAfter=4,
        )
    )
    return styles


def make_table(rows: list[list[str]], styles):
    if not rows:
        return Spacer(1, 0)
    col_count = max(len(row) for row in rows)
    normalized = [row + [""] * (col_count - len(row)) for row in rows]
    width = 180 * mm
    col_widths = [width / col_count] * col_count
    data = [
        [Paragraph(clean_inline(cell.strip()), styles["Smallx"]) for cell in row]
        for row in normalized
    ]
    table = Table(data, colWidths=col_widths, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E7F0FF")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#172033")),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#D9DEE8")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    return table


class Rule(Flowable):
    def __init__(self, width=180 * mm):
        super().__init__()
        self.width = width
        self.height = 1

    def draw(self):
        self.canv.setStrokeColor(colors.HexColor("#D9DEE8"))
        self.canv.line(0, 0, self.width, 0)


def markdown_to_pdf(source: Path, output: Path, title: str) -> None:
    styles = build_styles()
    doc = SimpleDocTemplate(
        str(output),
        pagesize=A4,
        rightMargin=15 * mm,
        leftMargin=15 * mm,
        topMargin=16 * mm,
        bottomMargin=16 * mm,
        title=title,
        author="Yvan FOCSA",
    )

    story = [Paragraph(title, styles["DocTitle"]), Rule(), Spacer(1, 8)]
    lines = source.read_text(encoding="utf-8").replace("\r\n", "\n").split("\n")
    paragraph: list[str] = []
    table_lines: list[str] = []
    code_lines: list[str] = []
    in_code = False

    def flush_paragraph():
        nonlocal paragraph
        if paragraph:
            story.append(Paragraph(clean_inline(" ".join(paragraph)), styles["Bodyx"]))
            paragraph = []

    def flush_code():
        nonlocal code_lines
        if code_lines:
            escaped = "<br/>".join(html.escape(line) or "&nbsp;" for line in code_lines)
            story.append(Paragraph(escaped, styles["Codex"]))
            code_lines = []

    def flush_table():
        nonlocal table_lines
        if table_lines:
            rows = []
            for line in table_lines:
                if re.match(r"^\|\s*-+", line):
                    continue
                cells = line.strip().strip("|").split("|")
                rows.append([cell.strip() for cell in cells])
            story.append(make_table(rows, styles))
            story.append(Spacer(1, 5))
            table_lines = []

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_paragraph()
            flush_table()
            if in_code:
                flush_code()
                in_code = False
            else:
                in_code = True
            continue

        if in_code:
            code_lines.append(line)
            continue

        if not stripped:
            flush_paragraph()
            flush_table()
            continue

        if stripped == "---":
            flush_paragraph()
            flush_table()
            story.append(Spacer(1, 3))
            story.append(Rule())
            story.append(Spacer(1, 6))
            continue

        if stripped.startswith("|"):
            flush_paragraph()
            table_lines.append(stripped)
            continue

        flush_table()

        if stripped.startswith("# "):
            flush_paragraph()
            story.append(Paragraph(clean_inline(stripped[2:]), styles["H1x"]))
        elif stripped.startswith("## "):
            flush_paragraph()
            story.append(Paragraph(clean_inline(stripped[3:]), styles["H1x"]))
        elif stripped.startswith("### "):
            flush_paragraph()
            story.append(Paragraph(clean_inline(stripped[4:]), styles["H2x"]))
        elif stripped.startswith("- [ ]"):
            flush_paragraph()
            story.append(Paragraph("□ " + clean_inline(stripped[5:].strip()), styles["Bodyx"]))
        elif stripped.startswith("- "):
            flush_paragraph()
            story.append(Paragraph("• " + clean_inline(stripped[2:].strip()), styles["Bodyx"]))
        elif re.match(r"^\d+\.\s+", stripped):
            flush_paragraph()
            story.append(Paragraph(clean_inline(stripped), styles["Bodyx"]))
        elif stripped.startswith(">"):
            flush_paragraph()
            quote = stripped.lstrip("> ").strip()
            story.append(Paragraph("<i>" + clean_inline(quote) + "</i>", styles["Bodyx"]))
        else:
            paragraph.append(stripped)

    flush_paragraph()
    flush_table()
    flush_code()
    doc.build(story)


def font(size: int, bold: bool = False):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Helvetica Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Helvetica.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size=size)
        except Exception:
            pass
    return ImageFont.load_default()


FONT_TITLE = font(42, True)
FONT_H = font(26, True)
FONT_M = font(22)
FONT_S = font(18)


def rounded(draw, box, fill, outline="#8FA3BF", width=2, radius=16):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def wrap(draw, text, xy, max_width, fnt, fill="#172033", line_gap=6):
    x, y = xy
    words = text.split()
    line = ""
    for word in words:
        test = f"{line} {word}".strip()
        if draw.textbbox((0, 0), test, font=fnt)[2] <= max_width:
            line = test
        else:
            draw.text((x, y), line, font=fnt, fill=fill)
            y += fnt.size + line_gap
            line = word
    if line:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + line_gap
    return y


def arrow(draw, start, end, fill="#2457D6", width=5):
    draw.line([start, end], fill=fill, width=width)
    x1, y1 = start
    x2, y2 = end
    dx, dy = x2 - x1, y2 - y1
    length = max((dx * dx + dy * dy) ** 0.5, 1)
    ux, uy = dx / length, dy / length
    px, py = -uy, ux
    size = 18
    p1 = (x2, y2)
    p2 = (x2 - ux * size + px * size * 0.55, y2 - uy * size + py * size * 0.55)
    p3 = (x2 - ux * size - px * size * 0.55, y2 - uy * size - py * size * 0.55)
    draw.polygon([p1, p2, p3], fill=fill)


def new_canvas(title: str, subtitle: str):
    img = Image.new("RGB", (1800, 1100), "#F7F9FC")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, 1800, 126], fill="#2457D6")
    draw.text((56, 34), title, font=FONT_TITLE, fill="white")
    draw.text((58, 88), subtitle, font=FONT_S, fill="#DCE7FF")
    return img, draw


def node(draw, xywh, title, body="", fill="#FFFFFF", outline="#9AA8BC"):
    x, y, w, h = xywh
    rounded(draw, (x, y, x + w, y + h), fill, outline)
    draw.text((x + 18, y + 16), title, font=FONT_H, fill="#172033")
    if body:
        wrap(draw, body, (x + 18, y + 54), w - 36, FONT_S, fill="#435169")


def generate_architecture_png():
    img, draw = new_canvas(
        "Architecture SOC externalise - MVP Daylight",
        "3 sites representatifs aujourd'hui, modele industrialisable vers environ 30 centres",
    )
    soc = (1120, 210, 570, 650)
    rounded(draw, (soc[0], soc[1], soc[0] + soc[2], soc[1] + soc[3]), "#E7F0FF", "#2457D6", 3, 24)
    draw.text((soc[0] + 22, soc[1] + 20), "SOC externalise - Prestataire", font=FONT_H, fill="#172033")

    site_boxes = [
        ((80, 190, 760, 190), "Site 1 - Centre principal", "Poste audioprothesiste, serveur interne / AD, application CRM/RDV, pfSense FW-S01."),
        ((80, 455, 760, 160), "Site 2 - Centre secondaire", "Poste utilisateur, pfSense FW-S02, messagerie simulee."),
        ((80, 690, 760, 145), "Site 3 - Centre distant", "Poste utilisateur et logs applicatifs simules."),
    ]
    for box, title, body in site_boxes:
        node(draw, box, title, body, "#FFFFFF", "#AAB4C3")
        arrow(draw, (box[0] + box[2], box[1] + box[3] // 2), (1120, box[1] + box[3] // 2), "#2457D6", 5)

    soc_nodes = [
        ((1170, 305, 450, 95), "Wazuh Manager", "Collecte, analyse et alertes"),
        ((1170, 430, 450, 95), "Wazuh Indexer", "Stockage et recherche"),
        ((1170, 555, 450, 95), "Wazuh Dashboard", "Interface web SOC"),
        ((1170, 680, 450, 95), "Playbooks / Reporting", "Qualification, reponse, preuves"),
    ]
    for box, title, body in soc_nodes:
        node(draw, box, title, body, "#FFFFFF", "#7C99D8")

    for y in [400, 525, 650]:
        arrow(draw, (1395, y), (1395, y + 30), "#7C99D8", 4)

    draw.text((90, 900), "Flux principaux : agents Wazuh, syslog pfSense, logs applicatifs, logs messagerie.", font=FONT_M, fill="#172033")
    draw.text((90, 942), "Securisation production : filtrage reseau, RBAC, retention, sauvegardes et supervision de sante.", font=FONT_M, fill="#172033")
    img.save(DIAGRAM_DIR / "architecture_soc_externalise.png", quality=95)


def generate_flux_png():
    img, draw = new_canvas(
        "Flux de collecte SOC",
        "De la source de log jusqu'a l'alerte et au playbook",
    )
    stages = [
        ("Sources", "Postes, serveurs, pfSense FW-S01/FW-S02, application, messagerie"),
        ("Collecte", "Agent Wazuh, syslog, fichier log, API si besoin"),
        ("Wazuh Manager", "Normalisation, correlation, regles"),
        ("Indexer", "Stockage, recherche, historique"),
        ("Dashboard", "Vues supervision, analyste, admin"),
        ("Reponse", "Playbook, qualification, preuve, REX"),
    ]
    x = 70
    y = 390
    w = 220
    h = 180
    step = 275
    for i, (title, body) in enumerate(stages):
        node(draw, (x, y, w, h), title, body, "#FFFFFF", "#AAB4C3")
        if i < len(stages) - 1:
            arrow(draw, (x + w + 10, y + h // 2), (x + step - 15, y + h // 2), "#2457D6", 5)
        x += step
    draw.text((80, 735), "Point cle Yvan : expliquer les chemins techniques sans entrer dans le detail des regles Wazuh.", font=FONT_M, fill="#172033")
    draw.text((80, 780), "En production, les flux seraient filtres, journalises et limites au strict necessaire.", font=FONT_M, fill="#172033")
    img.save(DIAGRAM_DIR / "flux_collecte_logs.png", quality=95)


def generate_topologie_png():
    img, draw = new_canvas(
        "Topologie MVP et passage a l'echelle",
        "Le schema montre 3 sites MVP, pas les 30 centres reels",
    )
    node(draw, (650, 250, 500, 210), "Zone SOC centralisee", "Wazuh Manager, Indexer, Dashboard, regles, alertes et playbooks", "#E7F0FF", "#2457D6")
    sites = [
        ((90, 650, 430, 170), "Site 1", "Centre complet : poste, serveur, pfSense, application"),
        ((685, 650, 430, 170), "Site 2", "Centre secondaire : poste, pfSense, messagerie"),
        ((1280, 650, 430, 170), "Site 3", "Centre leger : poste et logs applicatifs"),
    ]
    for box, title, body in sites:
        node(draw, box, title, body, "#FFFFFF", "#AAB4C3")
        arrow(draw, (box[0] + box[2] // 2, box[1]), (900, 460), "#2457D6", 5)
    draw.text((160, 900), "Ces 3 sites prouvent le modele. La checklist onboarding permet de repeter le deploiement vers les autres centres.", font=FONT_M, fill="#172033")
    draw.text((160, 944), "Message oral : 30 centres = besoin cible ; 3 sites = perimetre MVP ; templates = passage a l'echelle.", font=FONT_M, fill="#172033")
    img.save(DIAGRAM_DIR / "topologie_sites_mvp.png", quality=95)


def generate_incident_png():
    img, draw = new_canvas(
        "Processus incident SOC",
        "Collecter, detecter, qualifier, repondre, documenter",
    )
    stages = [
        ("Evenement", "Log collecte"),
        ("Alerte", "Regle SIEM"),
        ("Qualification", "Analyste SOC"),
        ("Decision", "Faux positif ou incident"),
        ("Reponse", "Playbook"),
        ("REX", "Preuve et amelioration"),
    ]
    x = 100
    y = 390
    w = 220
    h = 150
    step = 275
    for i, (title, body) in enumerate(stages):
        node(draw, (x, y, w, h), title, body, "#FFFFFF", "#AAB4C3")
        if i < len(stages) - 1:
            arrow(draw, (x + w + 10, y + h // 2), (x + step - 15, y + h // 2), "#2457D6", 5)
        x += step
    draw.text((90, 720), "A defendre : le SOC ne se limite pas a recevoir des logs, il transforme un evenement en decision documentee.", font=FONT_M, fill="#172033")
    img.save(DIAGRAM_DIR / "processus_incident_soc.png", quality=95)


def add_mx_cell(root, cell_id, value="", style="", vertex="0", edge="0", parent="1", geometry=None, source=None, target=None):
    attrib = {"id": cell_id}
    if value:
        attrib["value"] = value
    if style:
        attrib["style"] = style
    if vertex == "1":
        attrib["vertex"] = "1"
    if edge == "1":
        attrib["edge"] = "1"
    attrib["parent"] = parent
    if source:
        attrib["source"] = source
    if target:
        attrib["target"] = target
    cell = ET.SubElement(root, "mxCell", attrib)
    if geometry:
        geo = ET.SubElement(cell, "mxGeometry", geometry)
        geo.set("as", "geometry")
    return cell


def generate_drawio():
    mxfile = ET.Element("mxfile", {"host": "app.diagrams.net", "modified": "2026-06-22T00:00:00.000Z", "agent": "Codex", "version": "24.7.17"})
    diagram = ET.SubElement(mxfile, "diagram", {"id": "architecture-yvan", "name": "Architecture SOC MVP"})
    model = ET.SubElement(
        diagram,
        "mxGraphModel",
        {
            "dx": "1400",
            "dy": "900",
            "grid": "1",
            "gridSize": "10",
            "guides": "1",
            "tooltips": "1",
            "connect": "1",
            "arrows": "1",
            "fold": "1",
            "page": "1",
            "pageScale": "1",
            "pageWidth": "1600",
            "pageHeight": "1000",
            "math": "0",
            "shadow": "0",
        },
    )
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})
    box_style = "rounded=1;whiteSpace=wrap;html=1;strokeColor=#8FA3BF;fillColor=#FFFFFF;fontSize=16;"
    soc_style = "rounded=1;whiteSpace=wrap;html=1;strokeColor=#2457D6;fillColor=#E7F0FF;fontSize=16;fontStyle=1;"
    edge_style = "endArrow=block;html=1;rounded=0;strokeColor=#2457D6;strokeWidth=2;"
    nodes = {
        "s1": ("Site 1 - Centre principal<br/>Poste, serveur/AD, application, pfSense FW-S01", 70, 140, 360, 110, box_style),
        "s2": ("Site 2 - Centre secondaire<br/>Poste, pfSense FW-S02, messagerie", 70, 310, 360, 100, box_style),
        "s3": ("Site 3 - Centre distant<br/>Poste et logs applicatifs", 70, 470, 360, 90, box_style),
        "wazuh": ("Wazuh Manager / SIEM<br/>Collecte et detection", 660, 190, 300, 100, soc_style),
        "index": ("Wazuh Indexer / OpenSearch<br/>Stockage et recherche", 1040, 190, 300, 100, soc_style),
        "dash": ("Wazuh Dashboard<br/>Supervision / Analyste / Admin", 1040, 360, 300, 100, soc_style),
        "play": ("Playbooks et reporting<br/>Qualification, reponse, REX", 660, 500, 300, 100, soc_style),
    }
    for cell_id, (label, x, y, w, h, style) in nodes.items():
        add_mx_cell(root, cell_id, label, style, vertex="1", geometry={"x": str(x), "y": str(y), "width": str(w), "height": str(h)})
    edges = [
        ("e1", "s1", "wazuh", "Agents Wazuh / syslog pfSense / logs"),
        ("e2", "s2", "wazuh", "Agents + syslog pfSense"),
        ("e3", "s3", "wazuh", "Logs applicatifs"),
        ("e4", "wazuh", "index", "Indexation"),
        ("e5", "index", "dash", "Recherche"),
        ("e6", "wazuh", "play", "Alertes"),
        ("e7", "dash", "play", "Investigation"),
    ]
    for edge_id, src, dst, label in edges:
        add_mx_cell(root, edge_id, label, edge_style, edge="1", source=src, target=dst, geometry={"relative": "1"})
    out = DIAGRAM_DIR / "architecture_soc_externalise.drawio"
    tree = ET.ElementTree(mxfile)
    ET.indent(tree, space="  ")
    tree.write(out, encoding="utf-8", xml_declaration=True)


def generate_pdfs():
    for source, filename, title in PDF_SOURCES:
        if source.exists():
            markdown_to_pdf(source, PDF_DIR / filename, title)
            print(f"PDF {filename}")
        else:
            print(f"SKIP missing {source}")


def main():
    ensure_dirs()
    generate_pdfs()
    generate_architecture_png()
    generate_flux_png()
    generate_topologie_png()
    generate_incident_png()
    generate_drawio()
    print(f"Generated Yvan pack under {YVAN}")


if __name__ == "__main__":
    main()
