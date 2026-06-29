#!/usr/bin/env python3
"""Build the visual white paper for the dotnet-service template."""

from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "docs" / "dotnet-service-template-white-paper.pdf"
W, H = A4

NAVY = HexColor("#152238")
INK = HexColor("#1F2937")
CREAM = HexColor("#FFF8EE")
PAPER = HexColor("#FFFDF9")
CORAL = HexColor("#F4775C")
MINT = HexColor("#7CCDB5")
GOLD = HexColor("#F5BE62")
BLUE = HexColor("#6E8DD5")
SECONDARY = HexColor("#667085")
PALE_BLUE = HexColor("#E9EEF9")
PALE_MINT = HexColor("#E7F5F0")
PALE_CORAL = HexColor("#FCEAE5")
WHITE = HexColor("#FFFFFF")

MARGIN = 18 * mm


def para(c, text, x, y_top, width, size=10, leading=None, color=INK,
         font="Helvetica", align=TA_LEFT):
    """Draw a paragraph and return its height."""
    leading = leading or size * 1.28
    style = ParagraphStyle(
        "inline",
        fontName=font,
        fontSize=size,
        leading=leading,
        textColor=color,
        alignment=align,
        spaceAfter=0,
    )
    p = Paragraph(text, style)
    _, height = p.wrap(width, H)
    p.drawOn(c, x, y_top - height)
    return height


def rounded(c, x, y, width, height, fill, radius=10, stroke=None, line=1):
    c.setFillColor(fill)
    c.setStrokeColor(stroke or fill)
    c.setLineWidth(line)
    c.roundRect(x, y, width, height, radius, fill=1, stroke=1 if stroke else 0)


def label(c, text, x, y, fill, text_color=NAVY, width=None):
    size = 7.2
    pad = 7
    width = width or stringWidth(text, "Helvetica-Bold", size) + pad * 2
    rounded(c, x, y, width, 18, fill, radius=9)
    c.setFillColor(text_color)
    c.setFont("Helvetica-Bold", size)
    c.drawCentredString(x + width / 2, y + 6, text)
    return width


def page_header(c, kicker, title, subtitle=None, dark=False):
    fg = WHITE if dark else NAVY
    sub = HexColor("#CBD5E1") if dark else SECONDARY
    c.setFillColor(CORAL if dark else BLUE)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(MARGIN, H - 28 * mm, kicker.upper())
    para(c, title, MARGIN, H - 35 * mm, W - 2 * MARGIN, 25, 28, fg, "Helvetica-Bold")
    if subtitle:
        para(c, subtitle, MARGIN, H - 57 * mm, W - 2 * MARGIN, 10, 13, sub)


def footer(c, page, dark=False):
    color = HexColor("#CBD5E1") if dark else SECONDARY
    c.setFillColor(color)
    c.setFont("Helvetica", 7)
    c.drawString(MARGIN, 13 * mm, "DOTNET-SERVICE TEMPLATE  /  WHITE PAPER")
    c.drawRightString(W - MARGIN, 13 * mm, f"{page:02d}")


def arrow(c, x1, y1, x2, y2, color=BLUE, width=2):
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(width)
    c.line(x1, y1, x2, y2)
    c.saveState()
    c.translate(x2, y2)
    c.rotate(0 if x2 >= x1 else 180)
    c.line(0, 0, -7, 4)
    c.line(0, 0, -7, -4)
    c.restoreState()


def icon_contract(c, cx, cy, scale=1, color=NAVY):
    c.setStrokeColor(color)
    c.setLineWidth(2 * scale)
    c.roundRect(cx - 16 * scale, cy - 19 * scale, 32 * scale, 38 * scale,
                4 * scale, fill=0, stroke=1)
    for offset, length in [(9, 18), (2, 23), (-5, 15)]:
        c.line(cx - 10 * scale, cy + offset * scale,
               cx + (length - 10) * scale, cy + offset * scale)
    c.circle(cx + 9 * scale, cy - 11 * scale, 3 * scale, fill=0, stroke=1)


def icon_filter(c, cx, cy, scale=1, color=NAVY):
    c.setStrokeColor(color)
    c.setLineWidth(2 * scale)
    c.line(cx - 19 * scale, cy + 16 * scale, cx + 19 * scale, cy + 16 * scale)
    c.line(cx - 19 * scale, cy + 16 * scale, cx - 6 * scale, cy)
    c.line(cx + 19 * scale, cy + 16 * scale, cx + 6 * scale, cy)
    c.line(cx - 6 * scale, cy, cx - 6 * scale, cy - 15 * scale)
    c.line(cx + 6 * scale, cy, cx + 6 * scale, cy - 15 * scale)
    c.line(cx - 6 * scale, cy - 15 * scale, cx + 6 * scale, cy - 9 * scale)


def icon_service(c, cx, cy, scale=1, color=NAVY):
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(2 * scale)
    for y in (10, 0, -10):
        c.roundRect(cx - 20 * scale, cy + (y - 4) * scale, 40 * scale,
                    8 * scale, 2 * scale, fill=0, stroke=1)
        c.circle(cx - 13 * scale, cy + y * scale, 1.5 * scale, fill=1, stroke=0)


def cover(c):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # A visual pipeline: choices enter, a contract filters, one clean service leaves.
    c.setFillColor(PAPER)
    c.rect(0, H * 0.47, W, H * 0.53, fill=1, stroke=0)
    c.setStrokeColor(HexColor("#D6DCE8"))
    c.setLineWidth(1)
    for x in (80, 145, 210):
        c.line(x, H - 105, 282, H - 220)
    for x, y, fill, text in [
        (62, H - 92, CORAL, "API"),
        (128, H - 122, MINT, "DATA"),
        (194, H - 84, GOLD, "AUTH"),
        (95, H - 176, BLUE, "CI"),
        (187, H - 190, PALE_CORAL, "OBS"),
    ]:
        rounded(c, x, y, 49, 26, fill, radius=13)
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawCentredString(x + 24.5, y + 9, text)

    # Contract and output.
    rounded(c, 251, H - 265, 92, 116, NAVY, radius=15)
    icon_contract(c, 297, H - 201, 1.2, WHITE)
    c.setFillColor(MINT)
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(297, H - 242, "CONTRACT")
    arrow(c, 350, H - 207, 410, H - 207, CORAL, 3)
    rounded(c, 421, H - 270, 105, 126, PALE_MINT, radius=15,
            stroke=MINT, line=1.5)
    icon_service(c, 473, H - 196, 1.25, NAVY)
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(473, H - 238, "STANDALONE APP")
    c.setFillColor(SECONDARY)
    c.setFont("Helvetica", 7)
    c.drawCentredString(473, H - 252, "owns its next move")

    c.setFillColor(NAVY)
    c.rect(0, 0, W, H * 0.47, fill=1, stroke=0)
    label(c, ".NET", MARGIN, H * 0.47 - 38, MINT)
    label(c, "TEMPLATE CONTRACT", MARGIN + 50, H * 0.47 - 38, CORAL)
    para(c, "Blueprint.<br/>Not framework.", MARGIN, H * 0.47 - 68,
         W - 2 * MARGIN, 31, 35, WHITE, "Helvetica-Bold")
    para(c,
         "Designing an option-driven .NET service template with explicit contracts, isolated output, and honest release gates.",
         MARGIN, H * 0.47 - 155, W - 2 * MARGIN, 12, 16, MINT,
         "Helvetica-Bold")
    para(c,
         "The clever part is not how much code the template can add. It is how clearly the template says what it will add, what it will reject, and when it is done.",
         MARGIN, H * 0.47 - 205, W - 2 * MARGIN, 9.5, 13,
         HexColor("#D7DEE9"))
    c.setFillColor(CORAL)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(MARGIN, 20 * mm, "ARCHITECTURE  /  CONTRACTS  /  DELIVERY")
    footer(c, 1, True)
    c.showPage()


def outcome_card(c, x, y, width, height, number, title, proof, fill, accent):
    rounded(c, x, y, width, height, fill, radius=12)
    c.setFillColor(accent)
    c.setFont("Helvetica-Bold", 27)
    c.drawString(x + 15, y + height - 36, number)
    para(c, title, x + 15, y + height - 49, width - 30, 10, 12,
         NAVY, "Helvetica-Bold")
    para(c, proof, x + 15, y + height - 78, width - 30, 8.2, 11,
         SECONDARY)


def outcomes(c):
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    page_header(c, "Win at a glance", "The contract is visible - and countable.",
                "The current repository turns variation into a machine-readable agreement, then checks generated output at milestone boundaries.")
    gap = 12
    card_w = (W - 2 * MARGIN - gap) / 2
    card_h = 121
    top_y = H - 112 * mm
    outcome_card(c, MARGIN, top_y, card_w, card_h, "19",
                 "explicit options",
                 "Runtime, API, data, security, integration, testing, and delivery choices live in one versioned contract.",
                 PALE_BLUE, BLUE)
    outcome_card(c, MARGIN + card_w + gap, top_y, card_w, card_h, "13",
                 "compatibility rules",
                 "6 normalize, 5 require, 2 warn. Invalid intent is corrected, blocked, or surfaced before generation.",
                 PALE_CORAL, CORAL)
    outcome_card(c, MARGIN, top_y - card_h - gap, card_w, card_h, "5",
                 "milestone test entrypoints",
                 "M4 through M8 cover generation, data, capabilities, production readiness, and adoption checks.",
                 PALE_MINT, MINT)
    outcome_card(c, MARGIN + card_w + gap, top_y - card_h - gap, card_w,
                 card_h, "2",
                 "target frameworks",
                 ".NET 8 and .NET 10 are represented in the option contract and framework-specific generation paths.",
                 HexColor("#FFF2D9"), GOLD)

    rounded(c, MARGIN, 31 * mm, W - 2 * MARGIN, 92, NAVY, radius=13)
    c.setFillColor(MINT)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(MARGIN + 17, 31 * mm + 67, "THE RESULT")
    para(c,
         "A choice is no longer a README suggestion. It becomes input, a rule, generated output, and evidence.",
         MARGIN + 17, 31 * mm + 56, W - 2 * MARGIN - 34, 14, 18,
         WHITE, "Helvetica-Bold")
    c.setFillColor(HexColor("#B6C0D0"))
    c.setFont("Helvetica", 7)
    c.drawRightString(W - MARGIN - 17, 31 * mm + 13,
                      "Counts verified from config/template-options.json and tests/m4-m8")
    footer(c, 2)
    c.showPage()


def before_after(c):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    page_header(c, "Before / after", "From starter-code folklore to a contract.",
                "The shift is organizational as much as technical: decisions become explicit before files appear.")

    col_w = (W - 2 * MARGIN - 40) / 2
    y = 78 * mm
    height = 148 * mm
    rounded(c, MARGIN, y, col_w, height, WHITE, radius=14,
            stroke=HexColor("#E6DCD0"))
    rounded(c, MARGIN + col_w + 40, y, col_w, height, NAVY, radius=14)

    label(c, "BEFORE", MARGIN + 16, y + height - 31, PALE_CORAL, CORAL)
    para(c, "A pile of defaults", MARGIN + 16, y + height - 53,
         col_w - 32, 18, 22, NAVY, "Helvetica-Bold")
    before_items = [
        ("Hidden choices", "Packages and files imply decisions that nobody selected."),
        ("Soft warnings", "Incompatible combinations fail later - often during build or runtime."),
        ("Sticky ownership", "Generated code still feels coupled to the starter repository."),
    ]
    item_y = y + height - 105
    for idx, (title, body) in enumerate(before_items, 1):
        c.setFillColor(CORAL)
        c.circle(MARGIN + 28, item_y + 5, 10, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(MARGIN + 28, item_y + 2, str(idx))
        para(c, title, MARGIN + 46, item_y + 16, col_w - 62, 9.5, 12,
             NAVY, "Helvetica-Bold")
        para(c, body, MARGIN + 46, item_y, col_w - 62, 8, 10.5, SECONDARY)
        item_y -= 75

    ax = MARGIN + col_w + 20
    arrow(c, ax - 10, y + height / 2, ax + 10, y + height / 2, CORAL, 3)

    right_x = MARGIN + col_w + 40
    label(c, "AFTER", right_x + 16, y + height - 31, MINT, NAVY)
    para(c, "A deliberate snapshot", right_x + 16, y + height - 53,
         col_w - 32, 18, 22, WHITE, "Helvetica-Bold")
    steps = [
        ("01", "Select", "Only requested capabilities enter."),
        ("02", "Validate", "Rules normalize or reject intent."),
        ("03", "Generate", "Unselected scaffolding stays out."),
        ("04", "Own", "The application becomes independent."),
    ]
    sy = y + height - 114
    for num, title, body in steps:
        c.setFillColor(MINT)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(right_x + 18, sy, num)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(right_x + 48, sy, title)
        c.setFillColor(HexColor("#C7D0DE"))
        c.setFont("Helvetica", 7.8)
        c.drawString(right_x + 48, sy - 13, body)
        if num != "04":
            c.setStrokeColor(HexColor("#3A4961"))
            c.line(right_x + 23, sy - 21, right_x + 23, sy - 42)
        sy -= 69

    rounded(c, MARGIN, 31 * mm, W - 2 * MARGIN, 60, CORAL, radius=12)
    para(c,
         "The template ends at generation. The generated application begins there.",
         MARGIN + 16, 31 * mm + 42, W - 2 * MARGIN - 32, 12, 15,
         WHITE, "Helvetica-Bold", TA_CENTER)
    footer(c, 3)
    c.showPage()


def flow(c):
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    page_header(c, "What ships", "Five moves. One standalone service.",
                "The template is a creation-time tool, not a runtime dependency or upgrade mechanism.")

    xs = [MARGIN + 35 + i * 106 for i in range(5)]
    cy = H - 88 * mm
    colors = [BLUE, GOLD, CORAL, MINT, NAVY]
    names = ["Install", "Choose", "Validate", "Generate", "Own"]
    descs = ["dotnet new", "needed capabilities", "contract rules",
             "isolated source", "normal app lifecycle"]
    for i, (x, fill, name, desc) in enumerate(zip(xs, colors, names, descs)):
        c.setFillColor(fill)
        c.circle(x, cy, 25, fill=1, stroke=0)
        c.setFillColor(WHITE if fill != GOLD else NAVY)
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(x, cy - 4, str(i + 1))
        para(c, name, x - 42, cy - 36, 84, 9, 11, NAVY,
             "Helvetica-Bold", TA_CENTER)
        para(c, desc, x - 47, cy - 52, 94, 7.2, 9, SECONDARY,
             "Helvetica", TA_CENTER)
        if i < 4:
            arrow(c, x + 31, cy, xs[i + 1] - 31, cy, HexColor("#BCC6D6"), 1.5)

    rounded(c, MARGIN, 74 * mm, W - 2 * MARGIN, 160, NAVY, radius=14)
    c.setFillColor(MINT)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(MARGIN + 18, 74 * mm + 135, "CAPABILITIES INCLUDED ONLY WHEN SELECTED")
    capabilities = [
        ("API", "Controllers / Minimal / None", CORAL),
        ("DATA", "EF Core / PostgreSQL / SQL Server / SQLite", MINT),
        ("SECURITY", "JWT / OIDC / Policy", GOLD),
        ("INTEGRATION", "HTTP / Messaging / Hybrid", BLUE),
        ("DELIVERY", "Containers / GitHub Actions / Azure DevOps", CORAL),
        ("OPERATIONS", "Health / OpenTelemetry / Cache / Jobs", MINT),
    ]
    for i, (name, text, accent) in enumerate(capabilities):
        row = i // 2
        col = i % 2
        x = MARGIN + 18 + col * 242
        yy = 74 * mm + 103 - row * 38
        c.setFillColor(accent)
        c.circle(x + 4, yy + 4, 4, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(x + 16, yy + 1, name)
        c.setFillColor(HexColor("#C7D0DE"))
        c.setFont("Helvetica", 7.4)
        c.drawString(x + 16, yy - 11, text)

    rounded(c, MARGIN, 30 * mm, W - 2 * MARGIN, 78, PALE_CORAL, radius=12)
    c.setFillColor(CORAL)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(MARGIN + 16, 30 * mm + 55, "EXPLICITLY OUTSIDE THE TARGET")
    para(c,
         "Desktop and client UI, Razor Pages, MVC UI, games, Azure Functions, Kubernetes provisioning, and legacy .NET Framework applications.",
         MARGIN + 16, 30 * mm + 43, W - 2 * MARGIN - 32, 9, 12, NAVY)
    footer(c, 4)
    c.showPage()


def reality(c):
    c.setFillColor(NAVY)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    page_header(c, "Reality check", "A green build is not a broker test.",
                "The repository separates what generates and compiles from what has durable infrastructure evidence.", True)

    rounded(c, MARGIN, H - 129 * mm, W - 2 * MARGIN, 116, HexColor("#21314A"), radius=14)
    para(c, "generation + build", MARGIN + 22, H - 93 * mm,
         145, 15, 18, WHITE, "Helvetica-Bold", TA_CENTER)
    c.setFillColor(CORAL)
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(W / 2, H - 99 * mm, "!=")
    para(c, "integration evidence", W - MARGIN - 167, H - 93 * mm,
         145, 15, 18, MINT, "Helvetica-Bold", TA_CENTER)
    para(c,
         "Compilation proves structure. Production claims need behavior under real infrastructure, failure, retry, and recovery.",
         MARGIN + 40, H - 117 * mm, W - 2 * MARGIN - 80, 8.5, 11,
         HexColor("#C7D0DE"), "Helvetica", TA_CENTER)

    left = MARGIN
    top = H - 146 * mm
    box_w = (W - 2 * MARGIN - 14) / 2
    rounded(c, left, 70 * mm, box_w, 118, PALE_MINT, radius=12)
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(left + 15, 70 * mm + 93, "CURRENTLY PRODUCTION-CAPABLE")
    para(c,
         "API<br/>EF Core persistence<br/>Health checks<br/>OpenTelemetry wiring<br/>Container options",
         left + 15, 70 * mm + 78, box_w - 30, 9, 16, INK)

    right = left + box_w + 14
    rounded(c, right, 70 * mm, box_w, 118, PALE_CORAL, radius=12)
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(right + 15, 70 * mm + 93, "STILL NEEDS DURABLE EVIDENCE")
    para(c,
         "Broker adapters<br/>Outbox and inbox-outbox dispatch<br/>Hangfire storage and recovery<br/>Telemetry export assertion",
         right + 15, 70 * mm + 78, box_w - 30, 8.8, 16, INK)

    rounded(c, MARGIN, 31 * mm, W - 2 * MARGIN, 72, CORAL, radius=12)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(MARGIN + 16, 31 * mm + 49, "LOCAL CONSTRAINT, HONESTLY ROUTED")
    para(c,
         ".NET 10 and Docker smoke checks remain CI-owned on this machine. The gate stays; only its execution venue changes.",
         MARGIN + 16, 31 * mm + 35, W - 2 * MARGIN - 32, 9, 12, WHITE)
    footer(c, 5, True)
    c.showPage()


def takeaways(c):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    page_header(c, "Takeaways", "Five rules for templates that age well.",
                "A durable template behaves less like a code dump and more like a small, testable product contract.")

    rules = [
        ("01", "Contract before content", "Make every supported choice, default, and incompatibility explicit before generating files.", BLUE),
        ("02", "Exclude what was not chosen", "Optional capability means absent code and packages - not dormant scaffolding.", CORAL),
        ("03", "End cleanly", "Generated output must build and evolve without referencing the template repository.", MINT),
        ("04", "Match proof to the claim", "Generation tests prove shape; runtime and infrastructure tests prove behavior.", GOLD),
        ("05", "Keep upgrades application-owned", "Do not regenerate over a live service. Adopt changes through normal review and migration.", BLUE),
    ]
    start_y = H - 86 * mm
    card_h = 57
    for i, (num, title, body, accent) in enumerate(rules):
        y = start_y - i * 67
        rounded(c, MARGIN, y, W - 2 * MARGIN, card_h, WHITE, radius=11,
                stroke=HexColor("#E8DED2"))
        rounded(c, MARGIN, y, 53, card_h, accent, radius=11)
        c.setFillColor(NAVY if accent == GOLD else WHITE)
        c.setFont("Helvetica-Bold", 15)
        c.drawCentredString(MARGIN + 26.5, y + 21, num)
        para(c, title, MARGIN + 68, y + 43, 160, 10, 12, NAVY,
             "Helvetica-Bold")
        para(c, body, MARGIN + 230, y + 42, W - MARGIN - (MARGIN + 246),
             8.3, 11, SECONDARY)

    rounded(c, MARGIN, 28 * mm, W - 2 * MARGIN, 77, NAVY, radius=13)
    c.setFillColor(MINT)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(MARGIN + 17, 28 * mm + 55, "THE SHORT VERSION")
    para(c,
         "Build a funnel, not a cage: constrain the creation decision, then let the application go.",
         MARGIN + 17, 28 * mm + 43, W - 2 * MARGIN - 34, 12, 15,
         WHITE, "Helvetica-Bold")
    footer(c, 6)
    c.showPage()


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUTPUT), pagesize=A4)
    c.setTitle("Blueprint, Not Framework - dotnet-service Template White Paper")
    c.setSubject("An evidence-led white paper about the option-driven dotnet-service template contract")
    c.setAuthor("dotnet-template contributors")
    c.setCreator("dotnet-template white paper build script")
    cover(c)
    outcomes(c)
    before_after(c)
    flow(c)
    reality(c)
    takeaways(c)
    c.save()
    print(OUTPUT)


if __name__ == "__main__":
    build()
