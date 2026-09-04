from pathlib import Path

root_repository = Path(__file__).resolve().parents[2]

print(root_repository)

algorithms = {}
total_files = 0
total_loc = 0

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
    
    # Count of LOC for each file
    loc = 0
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                loc += 1
    
    # Exclude empty Python package initialization files to reduce noise
    if file_path.name == "__init__.py" and loc == 0:
        continue
    
    total_files += 1
    total_loc += loc
                
    if category not in algorithms:
        algorithms[category] = {}
        
    algorithms[category][str(file_name)] = loc
    
    print("Category:", category)
    print("File:", file_name)
    print("LOC:", algorithms[category][str(file_name)])
    print()
    
# Output formatting
col1 = 28
col2 = 8
col3 = 12
dashes = col1 + col2 + col3 + 2

print("-" * dashes)
print(f"{'Category':<{col1}} {'Files':>{col2}} {'LOC':>{col3}}")

for category, files in algorithms.items():
    file_count = len(files)
    category_loc = sum(files.values())
    
    print(f"{category:<{col1}} {file_count:>{col2}} {category_loc:>{col3}}")

print("-" * dashes)
print(f"{len(algorithms):<{col1}} {total_files:>{col2}} {total_loc:>{col3}}")