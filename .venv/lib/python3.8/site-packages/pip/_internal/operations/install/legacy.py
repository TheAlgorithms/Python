"""Legacy installation process, i.e. `setup.py install`.
"""

import logging
import os
import sys
from distutils.util import change_root
from typing import List, Optional, Sequence

from pip._internal.build_env import BuildEnvironment
from pip._internal.exceptions import InstallationError
from pip._internal.models.scheme import Scheme
from pip._internal.utils.logging import indent_log
from pip._internal.utils.misc import ensure_dir
from pip._internal.utils.setuptools_build import make_setuptools_install_args
from pip._internal.utils.subprocess import runner_with_spinner_message
from pip._internal.utils.temp_dir import TempDirectory

logger = logging.getLogger(__name__)


class LegacyInstallFailure(Exception):
    def __init__(self):
        # type: () -> None
        self.parent = sys.exc_info()


def install(
    install_options,  # type: List[str]
    global_options,  # type: Sequence[str]
    root,  # type: Optional[str]
    home,  # type: Optional[str]
    prefix,  # type: Optional[str]
    use_user_site,  # type: bool
    pycompile,  # type: bool
    scheme,  # type: Scheme
    setup_py_path,  # type: str
    isolated,  # type: bool
    req_name,  # type: str
    build_env,  # type: BuildEnvironment
    unpacked_source_directory,  # type: str
    req_description,  # type: str
):
    # type: (...) -> bool

    header_dir = scheme.headers

    with TempDirectory(kind="record") as temp_dir:
        try:
            record_filename = os.path.join(temp_dir.path, 'install-record.txt')
            install_args = make_setuptools_install_args(
                setup_py_path,
                global_options=global_options,
                install_options=install_options,
                record_filename=record_filename,
                root=root,
                prefix=prefix,
                header_dir=header_dir,
                home=home,
                use_user_site=use_user_site,
                no_user_config=isolated,
                pycompile=pycompile,
            )

            runner = runner_with_spinner_message(
                f"Running setup.py install for {req_name}"
            )
            with indent_log(), build_env:
                runner(
                    cmd=install_args,
                    cwd=unpacked_source_directory,
                )

            if not os.path.exists(record_filename):
                logger.debug('Record file %s not found', record_filename)
                # Signal to the caller that we didn't install the new package
                return False

        except Exception:
            # Signal to the caller that we didn't install the new package
            raise LegacyInstallFailure

        # At this point, we have successfully installed the requirement.

        # We intentionally do not use any encoding to read the file because
        # setuptools writes the file using distutils.file_util.write_file,
        # which does not specify an encoding.
        with open(record_filename) as f:
            record_lines = f.read().splitlines()

    def prepend_root(path):
        # type: (str) -> str
        if root is None or not os.path.isabs(path):
            return path
        else:
            return change_root(root, path)

    for line in record_lines:
        directory = os.path.dirname(line)
        if directory.endswith('.egg-info'):
            egg_info_dir = prepend_root(directory)
            break
    else:
        message = (
            "{} did not indicate that it installed an "
            ".egg-info directory. Only setup.py projects "
            "generating .egg-info directories are supported."
        ).format(req_description)
        raise InstallationError(message)

    new_lines = []
    for line in record_lines:
        filename = line.strip()
        if os.path.isdir(filename):
            filename += os.path.sep
        new_lines.append(
            os.path.relpath(prepend_root(filename), egg_info_dir)
        )
    new_lines.sort()
    ensure_dir(egg_info_dir)
    inst_files_path = os.path.join(egg_info_dir, 'installed-files.txt')
    with open(inst_files_path, 'w') as f:
        f.write('\n'.join(new_lines) + '\n')

    return True
