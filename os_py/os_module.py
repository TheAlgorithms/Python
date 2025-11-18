import os

# -------------------------------
# 📂 1. DIRECTORY OPERATIONS
# -------------------------------
print("Current Working Directory:", os.getcwd())

# Create a new folder
os.mkdir("demo_folder")
print("\nAfter creating 'demo_folder':", os.listdir())

# Rename folder
os.rename("demo_folder", "renamed_folder")
print("After renaming:", os.listdir())

# Change directory
os.chdir("renamed_folder")
print("Now inside directory:", os.getcwd())

# Go back to parent directory
os.chdir("..")

# Remove directory
os.rmdir("renamed_folder")
print("After removing folder:", os.listdir())

# -------------------------------
# 🧭 2. PATH HANDLING
# -------------------------------
print("\n--- Path Operations ---")
path = os.getcwd()

print("Absolute Path:", os.path.abspath(path))
print("Is Directory:", os.path.isdir(path))
print("Is File:", os.path.isfile(__file__))
print("File Name:", os.path.basename(__file__))
print("Directory Name:", os.path.dirname(__file__))
print("Path Exists:", os.path.exists(path))
print("Joined Path:", os.path.join(path, "sample.txt"))

# -------------------------------
# 🌍 3. ENVIRONMENT VARIABLES
# -------------------------------
print("\n--- Environment Variables ---")
print("OS Name:", os.name)
print("Home Directory:", os.getenv("HOME") or os.getenv("USERPROFILE"))
print("Python Path:", os.getenv("PATH").split(";")[0])  # Show first path

# Setting and unsetting an environment variable
os.putenv("MY_VAR", "User_name")
print("MY_VAR (after putenv):", os.getenv("MY_VAR"))

os.unsetenv("MY_VAR")
print("MY_VAR (after unsetenv):", os.getenv("MY_VAR"))

# -------------------------------
# ⚙️ 4. SYSTEM COMMANDS
# -------------------------------
print("\n--- System Commands ---")
# Example: list files using OS command
os.system("dir" if os.name == "nt" else "ls")

# -------------------------------
# 🧱 5. PROCESS INFORMATION
# -------------------------------
print("\n--- Process Info ---")
print("Process ID:", os.getpid())
print("CPU Count:", os.cpu_count())

# -------------------------------
# 🔐 6. FILE ACCESS & PERMISSIONS
# -------------------------------
print("\n--- File Access & Permissions ---")
filename = "testfile.txt"
with open(filename, "a+") as f:
    f.write("This is a test file for os module demo.\n")

print("File Created:", filename)
print("File Size:", os.path.getsize(filename), "bytes")
print("Has Read Access:", os.access(filename, os.R_OK))
print("Has Write Access:", os.access(filename, os.W_OK))

# -------------------------------
# 🧩 7. CLEANUP
# -------------------------------
os.remove(filename)
print("\nFile Removed:", filename)

# print("\n✅ All OS operations completed successfully!")
