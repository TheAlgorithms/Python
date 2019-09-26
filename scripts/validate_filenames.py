#!/usr/bin/env python3

import os
from build_directory_md import good_filepaths

filepaths = list(good_filepaths())
assert filepaths, "good_filepaths() failed!"


upper_files = [file for file in filepaths if file != file.lower()]
if upper_files:
    print(f"{len(upper_files)} files contain uppercase characters:")
    print("\n".join(upper_files) + "\n")

space_files = [file for file in filepaths if " " in file]
if space_files:
    print(f"{len(space_files)} files contain space characters:")
    print("\n".join(space_files) + "\n")

nodir_files = [file for file in filepaths if os.sep not in file]
if nodir_files:
    print(f"{len(nodir_files)} files are not in a directory:")
    print("\n".join(nodir_files) + "\n")

bad_files = len(upper_files + space_files + nodir_files)
if bad_files:
    import sys
    sys.exit(bad_files)
