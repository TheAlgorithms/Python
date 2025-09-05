import os
from collections import defaultdict

def count_python_lines(root_dir):
    dir_line_counts = defaultdict(int)
    total_lines = 0

    for dirpath, _, filenames in os.walk(root_dir):
        dir_total = 0
        for filename in filenames:
            if filename.endswith('.py'):
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = sum(1 for line in f if line.strip())  # Count non-empty lines
                        dir_total += lines
                        total_lines += lines
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
        dir_line_counts[dirpath] = dir_total

    print("\n📁 Lines of Code by Directory:")
    for directory, count in sorted(dir_line_counts.items()):
        print(f"{directory}: {count} lines")

    print(f"\n🧮 Total Lines of Python Code: {total_lines} lines")

# Example usage
if __name__ == "__main__":
    count_python_lines("/Users/uzairmukadam/Projects/TheAlgorithms-Python/data_structures")  # Replace "." with your target root directory
