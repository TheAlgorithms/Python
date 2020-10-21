"""This script runs mypy on all py files in the given directory.

Author: Shining (Fred) Lou
"""
import os
from subprocess import Popen, PIPE
from typing import List, Tuple


def get_src_file_list(dir: str) -> List[str]:
    """ Get all py files from the given directories
    """
    res = []
    for root, dirs, files in os.walk(dir):
        dirs.sort()
        for file_name in sorted(files):
            if file_name[-3:] != '.py': continue
            full_path = os.path.join(root, file_name)
            res.append(full_path)
    return res


def run_mypy(files: List[str] = [], packages: List[str] = [], modules: List[str] = [], args: List[str] = []) -> Tuple[str, str]:
    """ Call mypy given list of files, packages, modules and arguments
    Output: stdout, stderr
    """
    bash_command = ["mypy"]
    for file in files:
        bash_command.append(file)
    for package in packages:
        raise NotImplementedError
    for module in modules:
        raise NotImplementedError
    for arg in args:
        bash_command.append(arg)

    proc = Popen(bash_command, stdout = PIPE)
    output = proc.communicate()
    out = ''
    if output[0]:
        out = output[0].decode("utf-8")
    err = ''
    if output[1]:
        err = output[1].decode("utf-8")
    return out, err


def main() -> None:
    args = ['--follow-imports', 'silent', '--ignore-missing-imports', '--check-untyped-defs', '--sqlite-cache']

    src_files = get_src_file_list('.')
    _, _ = run_mypy(src_files, [], [], args)


if __name__ == '__main__':
    main()
