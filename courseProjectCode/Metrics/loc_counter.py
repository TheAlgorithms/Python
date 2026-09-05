import csv
from pathlib import Path

root_repository = Path(__file__).resolve().parents[2]

print(root_repository)

algorithms = {}
total_files = 0
total_loc = 0
total_comments = 0

# Recursively find all files ending with .py
for file_path in root_repository.rglob("*.py"):
    relative_path = file_path.relative_to(root_repository)

    # Add the category of the algorithm to the dictionary
    category = relative_path.parts[0]

    # Ignore metrics code
    if category == "courseProjectCode":
        continue

    # Extract file name including its relative path to project, this accounts for files under sub-folder in their categories
    file_name = Path(*relative_path.parts[1:])

    # Count of LOC and Comments for each file
    loc = 0
    comments = 0

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                loc += 1

            if line.strip().startswith("#"):
                comments += 1

    # Exclude empty Python package initialization files to reduce noise
    if file_path.name == "__init__.py" and loc == 0:
        continue

    total_files += 1
    total_loc += loc
    total_comments += comments

    if category not in algorithms:
        algorithms[category] = {}

    algorithms[category][str(file_name)] = {
        "loc": loc,
        "comments": comments,
        "comment_density": comments / loc if loc > 0 else 0,
    }

    # Can enable in the future with command and switch
    # print("Category:", category)
    # print("File:", file_name)
    # print("LOC:", algorithms[category][str(file_name)])
    # print("Comments:", comments)
    # print("Comments Density:", algorithms[category][str(file_name)]["comment_density"])
    # print()

# Output formatting
col1 = 28
col2 = 8
col3 = 12
dashes = col1 + col2 + col3 + col3 + col3 + 3

print("-" * dashes)
print(
    f"{'Category':<{col1}} {'Files':>{col2}} {'LOC':>{col3}} {'Comments':>{col3}}{'> Density %':>{col3}}"
)
print("-" * dashes)

for category, files in algorithms.items():
    file_count = len(files)

    # Get the values of loc for each file
    category_loc = sum(metrics["loc"] for metrics in files.values())
    category_comments = sum(metrics["comments"] for metrics in files.values())
    category_comment_density = (
        category_comments / category_loc if category_loc > 0 else 0
    )

    print(
        f"{category:<{col1}} {file_count:>{col2}} {category_loc:>{col3}} {category_comments:>{col3}}{category_comment_density * 100:>{col3}.2f}"
    )

print("-" * dashes)

# Calculate Total Comments Density
total_comment_density = total_comments / total_loc if total_loc > 0 else 0

print(
    f"{f'Total ({len(algorithms)} categories)':<{col1}} {total_files:>{col2}} {total_loc:>{col3}} {total_comments:>{col3}}{total_comment_density * 100:>{col3}.2f}\n"
)

# Write results to a csv file
output_file = Path(__file__).resolve().parent / "loc_results.csv"

print("Saving results to file...")
with open(output_file, "w", encoding="utf-8", newline="") as csv_file:
    writer = csv.writer(csv_file)

    # Insert the header
    writer.writerow(["Category", "File", "LOC", "Comments", "Comments Density %"])

    # Insert data rows
    for (
        category,
        files,
    ) in algorithms.items():
        for file_name, metrics in files.items():
            writer.writerow(
                [
                    category,
                    file_name,
                    metrics["loc"],
                    metrics["comments"],
                    metrics["comment_density"] * 100,
                ]
            )

print()
print(f"Results saved to: {output_file.name}")
