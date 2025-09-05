"""Generate a sustainability compliance dashboard for CTRL Environmental.

The script reads inspection data from CSV or Excel files, categorizes findings
into environmental topics, flags non-compliances with traffic light colours,
and exports the results to a styled HTML report. Optional PDF export is
attempted if a suitable backend is available. The layout follows a black,
red, and white palette reminiscent of Berlin poster aesthetics and includes
placeholders for the CTRL logo and report metadata.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd
from jinja2 import Environment

try:
    import pdfkit  # type: ignore[import-not-found]
except ImportError:
    pdfkit = None  # type: ignore[assignment]

try:
    from weasyprint import HTML  # type: ignore[import-not-found]
except ImportError:
    HTML = None  # type: ignore[assignment]

CATEGORY_KEYWORDS = {
    "Waste": ["waste", "trash", "garbage", "recycle"],
    "Water": ["water", "effluent", "sewage", "storm"],
    "Air": ["air", "emission", "dust", "smoke"],
    "Chemicals": ["chemical", "hazard", "solvent", "acid", "alkali"],
    "ESG": ["esg", "governance", "social", "sustainability", "diversity"],
}


@dataclass
class Metadata:
    """Metadata describing the inspection report."""

    site: str
    client: str
    inspector: str
    date: str


def read_inspection_data(path: str) -> pd.DataFrame:
    """Read inspection data from a CSV or Excel file."""

    ext = Path(path).suffix.lower()
    if ext in {".xls", ".xlsx"}:
        return pd.read_excel(path)
    return pd.read_csv(path)


def categorize_finding(text: str) -> str:
    """Return the category that best matches *text*."""

    lowered = text.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(word in lowered for word in keywords):
            return category
    return "Other"


def traffic_light(status: str) -> str:
    """Return a CSS colour for a traffic light style status."""

    lowered = status.lower()
    if any(word in lowered for word in ["non", "major", "fail", "nc"]):
        return "#d50000"  # red
    if any(word in lowered for word in ["minor", "obs", "warning"]):
        return "#ffab00"  # amber
    return "#00c853"  # green


def build_table(df: pd.DataFrame) -> str:
    """Return an HTML table with traffic light styling."""

    styled = (
        df.style.applymap(
            lambda v: f"background-color:{traffic_light(v)}", subset=["Status"]
        )
        .set_table_styles(
            [
                {
                    "selector": "th, td",
                    "props": [("border", "1px solid black"), ("padding", "4px")],
                }
            ]
        )
        .hide_index()
    )
    return styled.to_html()


TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>CTRL Environmental Compliance Report</title>
<style>
body { background: #fff; color: #000; font-family: Arial, sans-serif; }
header { background: #000; color: #fff; padding: 20px; text-align: center; }
h1 { color: #e10600; margin: 0; text-transform: uppercase; }
.meta { margin-top: 10px; }
</style>
</head>
<body>
<header>
  <img src="{{ logo }}" alt="CTRL Logo" style="max-height:80px;" />
  <h1>Compliance Dashboard</h1>
  <div class="meta">
    <strong>Site:</strong> {{ meta.site }} |
    <strong>Client:</strong> {{ meta.client }} |
    <strong>Inspector:</strong> {{ meta.inspector }} |
    <strong>Date:</strong> {{ meta.date }}
  </div>
</header>
<div class="table-container">
{{ table | safe }}
</div>
</body>
</html>
"""


def render_report(
    df: pd.DataFrame, meta: Metadata, logo: str, html_path: str, pdf_path: str | None
) -> None:
    """Render *df* to HTML and optionally PDF."""

    table_html = build_table(df)
    env = Environment(autoescape=True)
    template = env.from_string(TEMPLATE)
    html_content = template.render(table=table_html, meta=meta, logo=logo)
    Path(html_path).write_text(html_content, encoding="utf-8")

    if pdf_path:
        if pdfkit is not None:
            pdfkit.from_string(html_content, pdf_path)  # type: ignore[no-untyped-call]
        elif HTML is not None:
            HTML(string=html_content).write_pdf(pdf_path)  # type: ignore[no-untyped-call]
        else:
            print("PDF output requested but no PDF backend is installed.")


def main() -> None:
    """Command line interface for the compliance dashboard."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="CSV or Excel file containing inspection data")
    parser.add_argument("--html", default="report.html", help="Output HTML report path")
    parser.add_argument("--pdf", help="Optional output PDF path")
    parser.add_argument(
        "--logo", default="logo_placeholder.png", help="Path to CTRL logo image"
    )
    parser.add_argument("--site", default="Unknown Site")
    parser.add_argument("--client", default="Unknown Client")
    parser.add_argument("--inspector", default="Unknown Inspector")
    parser.add_argument("--date", default=datetime.now(tz=UTC).date().isoformat())
    args = parser.parse_args()

    data = read_inspection_data(args.input)
    if "Category" not in data.columns and "Finding" in data.columns:
        data["Category"] = data["Finding"].map(categorize_finding)

    meta = Metadata(args.site, args.client, args.inspector, args.date)
    render_report(data, meta, args.logo, args.html, args.pdf)
    print(f"Report written to {args.html}")


if __name__ == "__main__":
    main()
