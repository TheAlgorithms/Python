import os
import ast
import doctest
import coverage
import importlib
import sys
import io
import subprocess

def has_doctest(file_path):
    """Check if a Python file contains doctest examples."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read(), filename=file_path)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
                docstring = ast.get_docstring(node)
                if docstring and ">>>" in docstring:
                    return True
    except Exception as e:
        print(f"⚠️ Error parsing {file_path}: {e}")
    return False

def run_doctest_with_coverage(file_path, project_root, filename):
    print(f"\n📄 Running doctests in: {file_path}")

    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    rel_path = os.path.relpath(file_path, project_root)
    module_name = rel_path.replace(os.sep, ".").rstrip(".py")

    cov = coverage.Coverage(source=[os.path.dirname(file_path)], include=[file_path])
    cov.start()

    try:
        module = importlib.import_module(module_name)
        result = doctest.testmod(module)
    except Exception as e:
        print(f"❌ Import failed for {file_path}: {e}")
        cov.stop()
        cov.save()
        return {
            "type": "doctest",
            "file": filename,
            "passed": 0,
            "failed": 1,
            "coverage": 0
        }

    cov.stop()
    cov.save()

    try:
        analysis = cov.analysis(file_path)
        covered = len(analysis[1])
        missed = len(analysis[3])
        buffer = io.StringIO()
        percent = cov.report(file=buffer, show_missing=False)
        buffer_output = buffer.getvalue()
        buffer.close()
    except Exception as e:
        print(f"⚠️ Coverage analysis failed for {file_path}: {e}")
        covered = missed = percent = 0

    print(f"✅ Passed: {result.attempted - result.failed}, ❌ Failed: {result.failed}")
    print(f"📊 Coverage: {percent:.1f}%")
    return {
        "type": "doctest",
        "file": filename,
        "passed": result.attempted - result.failed,
        "failed": result.failed,
        "coverage": percent
    }

def run_pytest_with_coverage(pytest_dir, filename):
    print(f"\n🧪 Running pytest in: {pytest_dir}")

    subprocess.run([
        "coverage", "run", "--parallel-mode", "-m", "pytest", pytest_dir,
        "--tb=short", "--disable-warnings"
    ])

    subprocess.run(["coverage", "combine"])

    try:
        report = subprocess.run(
            ["coverage", "report"],
            capture_output=True,
            text=True
        )
        output = report.stdout
        print(output)

        lines = output.strip().splitlines()
        last_line = lines[-1] if lines else ""
        percent = float(last_line.split()[-1].replace("%", "")) if "%" in last_line else 0.0
    except Exception as e:
        print(f"⚠️ Coverage analysis failed for {pytest_dir}: {e}")
        percent = 0.0

    print(f"📊 Coverage: {percent:.1f}%")
    return {
        "type": "pytest",
        "file": filename,
        "passed": "-",
        "failed": "-",
        "coverage": percent
    }

def run_all_tests(doctest_dirs, pytest_dirs, project_root):
    summary = []

    for parent_directory in doctest_dirs:
        for dirpath, _, filenames in os.walk(parent_directory):
            for filename in filenames:
                if filename.endswith(".py"):
                    file_path = os.path.join(dirpath, filename)
                    if has_doctest(file_path):
                        result = run_doctest_with_coverage(file_path, project_root, filename)
                        summary.append(result)

    for test_dir in pytest_dirs:
        result = run_pytest_with_coverage(test_dir, filename)
        summary.append(result)

    print("\n\n\n############# COMBINED SUMMARY REPORT #############\n")
    print_summary(summary)


def print_summary(summary):
    if not summary:
        print("No tests found.")
        return

    # Compute column widths dynamically
    type_width = max(len("Type"), max(len(i["type"]) for i in summary))
    file_width = max(len("File"), max(len(i["file"]) for i in summary))
    passed_width = max(len("Passed"), max(len(str(i["passed"])) for i in summary))
    failed_width = max(len("Failed"), max(len(str(i["failed"])) for i in summary))
    coverage_width = max(len("Coverage"), max(len(f"{i['coverage']:.1f}%") for i in summary))

    # Build border line
    border = (
        f"+{'-' * (type_width+4)}+{'-' * (file_width+2)}+{'-' * (passed_width+6)}+"
        f"{'-' * (failed_width+6)}+{'-' * (coverage_width+6)}+"
    )

    # Header with emojis only in the title
    header = (
        f"| {'Type':<{type_width+3}}"
        f"| {'File':<{file_width+1}}"
        f"| {'Passed':<{passed_width+5}}"
        f"| {'Failed':<{failed_width+5}}"
        f"| {'Coverage':<{coverage_width+5}}|"
    )

    print(border)
    print(header)
    print(border)

    # Initialize totals
    total_passed, total_failed, coverage_values = 0, 0, []

    # Print rows
    for item in summary:
        label = "pytest" if item["type"] == "pytest" else "doctest"
        coverage_str = f"{item['coverage']:.1f}%"
        row = (
            f"| {label:<{type_width+3}}"
            f"| {item['file']:<{file_width+1}}"
            f"| {item['passed']:<{passed_width+5}}"
            f"| {item['failed']:<{failed_width+5}}"
            f"| {coverage_str:<{coverage_width+5}}|"
        )
        print(row)

        # Update totals for average calculation
        if isinstance(item["passed"], int):
            total_passed += item["passed"]
        if isinstance(item["failed"], int):
            total_failed += item["failed"]
        if isinstance(item["coverage"], (int, float)):
            coverage_values.append(item["coverage"])

    print(border)

    # Compute average coverage
    avg_coverage = sum(coverage_values) / len(coverage_values) if coverage_values else 0

    # Totals row
    total_row = (
        f"| {'TOTAL':<{type_width+3}}"
        f"| {'':<{file_width+1}}"
        f"| {total_passed:<{passed_width+5}}"
        f"| {total_failed:<{failed_width+5}}"
        f"| {avg_coverage:.1f}%"
        f"{' ' * (coverage_width+4-len(f'{avg_coverage:.1f}%'))}|"
    )
    print(total_row)
    print(border)


if __name__ == "__main__":
    ## project_root = "/Users/uzairmukadam/Projects/TheAlgorithms-Python"

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    print(project_root)

    doctest_dirs = [
        f"{project_root}/data_structures/",
    ]

    pytest_dirs = [
        f"{project_root}/data_structures/",
    ]

    run_all_tests(doctest_dirs, pytest_dirs, project_root)
