import ast
import csv
from pathlib import Path

root_repository = Path(__file__).resolve().parents[2]

total_test_files = 0
total_test_cases = 0

for file_path in root_repository.rglob("*.py"):
    relative_path = file_path.relative_to(root_repository)

    if relative_path.parts[0] == "courseProjectCode":
        continue

    if not file_path.name.startswith("test_"):
        continue

    total_test_files += 1

    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        source = file.read()

    try:
        tree = ast.parse(source)
    except SyntaxError:
        continue

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test_"):
            total_test_cases += 1

        elif isinstance(node, ast.AsyncFunctionDef) and node.name.startswith("test_"):
            total_test_cases += 1

# Output formatting
col1 = 28
col2 = 8
dashes = col1 + col2 + 1

print("-" * dashes)
print(f"{'Test Suites/Files':<{col1}} {total_test_files:<{col2}}")

print(f"{'Test Cases':<{col1}} {total_test_cases:<{col2}}")
print("-" * dashes)

# Write results to a csv file
output_file = Path(__file__).resolve().parent / "test_results.csv"
print("Saving results to file...")

with open(output_file, "w", encoding="utf-8", newline="") as csv_file:
    writer = csv.writer(csv_file)

    # Insert the header
    writer.writerow(["Test Suites/Files", "Test Cases"])

    # Insert test suites and cases data
    writer.writerow([total_test_files, total_test_cases])

print()
print(f"Results saved to: {output_file.name}")
