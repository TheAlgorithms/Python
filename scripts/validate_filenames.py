#!python
import os

try:
    from .build_directory_md import good_file_paths
except ImportError:
    from build_directory_md import good_file_paths  # type: ignore[no-redef]

filepaths = list(good_file_paths())
assert filepaths, "good_file_paths() failed!"

if upper_files := [file for file in filepaths if file != file.lower()]:
    print(f"{len(upper_files)} files contain uppercase characters:")
    print("\n".join(upper_files) + "\n")

if space_files := [file for file in filepaths if " " in file]:
    print(f"{len(space_files)} files contain space characters:")
    print("\n".join(space_files) + "\n")

if hyphen_files := [
    file for file in filepaths if "-" in file and "/site-packages/" not in file
]:
    print(f"{len(hyphen_files)} files contain hyphen characters:")
    print("\n".join(hyphen_files) + "\n")

if nodir_files := [file for file in filepaths if os.sep not in file]:
    print(f"{len(nodir_files)} files are not in a directory:")
    print("\n".join(nodir_files) + "\n")

if bad_files := len(upper_files + space_files + hyphen_files + nodir_files):
    import sys

    sys.exit(bad_files)
