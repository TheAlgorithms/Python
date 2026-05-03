"""
Automated Bug Triage Tool
This script scans markdown bug reports, classifies them by severity based on
keywords, and generates a summarized triage report in Markdown format.
"""

import glob
import os
from datetime import UTC, datetime
from pathlib import Path

# Configuration: Adjust these paths based on your local environment
BASE_DIR = Path(__file__).parent
BUG_PATH = str(BASE_DIR / "production" / "qa" / "bugs" / "*.md")
OUTPUT_PATH = str(BASE_DIR / "production" / "qa")


def classify_severity(content: str) -> str:
    """
    Classifies bug severity based on specific keywords found in the content.
    Returns S1 (Critical) through S4 (Minor).
    >>> classify_severity("The application had a fatal crash on startup.")
    'S1'
    >>> classify_severity("The UI is a bit slow today.")
    'S3'
    """
    content = content.lower()
    if any(k in content for k in ["crash", "data loss", "cannot start", "fatal"]):
        return "S1"
    if any(k in content for k in ["broken", "not working", "fail"]):
        return "S2"
    if any(k in content for k in ["slow", "incorrect", "glitch"]):
        return "S3"
    return "S4"


def classify_priority(severity: str) -> str:
    """
    Maps the technical severity level to a business priority level.
    >>> classify_priority("S1")
    'P1'
    >>> classify_priority("S4")
    'P4'
    """
    priority_map = {"S1": "P1", "S2": "P2", "S3": "P3"}
    return priority_map.get(severity, "P4")


def read_bugs() -> list[dict]:
    """
    Reads all markdown files in the BUG_PATH and extracts metadata.
    >>> read_bugs()
    []
    """
    files = glob.glob(BUG_PATH)
    bugs = []

    for i, file_path in enumerate(sorted(files)):
        try:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            severity = classify_severity(content)
            priority = classify_priority(severity)

            bugs.append({
                "id": f"BUG-{i+1:03}",
                "file": file_path,
                "severity": severity,
                "priority": priority,
                "summary": content.strip().split("\n")[0][:80]
            })
        except OSError as e:
            print(f"⚠️ Could not read file {file_path}: {e}")

    return bugs


def generate_report(bugs: list[dict]) -> None:
    """
    Groups bugs by priority and writes a summarized Markdown report.
    >>> generate_report([])
    ❌ No bugs to report.
    """
    if not bugs:
        print("❌ No bugs to report.")
        return

    date = datetime.now(UTC).strftime("%Y-%m-%d")

    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)

    output_file = os.path.join(OUTPUT_PATH, f"bug-triage-{date}.md")

    p1 = [b for b in bugs if b["priority"] == "P1"]
    p2 = [b for b in bugs if b["priority"] == "P2"]
    p3 = [b for b in bugs if b["priority"] == "P3"]
    p4 = [b for b in bugs if b["priority"] == "P4"]

    report_content = [
        "# Bug Triage Report",
        f"**Date**: {date}  ",
        f"**Open bugs processed**: {len(bugs)}",
        "\n---\n",
        "## Triage Summary\n",
        "| Priority | Count |",
        "|----------|-------|",
        f"| P1       | {len(p1)} |",
        f"| P2       | {len(p2)} |",
        f"| P3       | {len(p3)} |",
        f"| P4       | {len(p4)} |",
        "\n---\n",
        "## P1 Bugs (Critical)"
    ]

    for b in p1:
        report_content.append(f"- {b['id']} | {b['severity']} | {b['summary']}")

    report_content.append("\n## P2 Bugs (High)")
    for b in p2:
        report_content.append(f"- {b['id']} | {b['severity']} | {b['summary']}")

    report_content.append("\n## Backlog (P3/P4)")
    for b in p3 + p4:
        report_content.append(f"- {b['id']} | {b['severity']} | {b['summary']}")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(report_content))

    print(f"✅ Report successfully generated at: {output_file}")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    extracted_bugs = read_bugs()
    generate_report(extracted_bugs)
