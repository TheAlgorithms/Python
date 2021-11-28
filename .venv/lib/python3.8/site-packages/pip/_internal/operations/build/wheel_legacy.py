import logging
import os.path
from typing import List, Optional

from pip._internal.cli.spinners import open_spinner
from pip._internal.utils.setuptools_build import make_setuptools_bdist_wheel_args
from pip._internal.utils.subprocess import (
    LOG_DIVIDER,
    call_subprocess,
    format_command_args,
)

logger = logging.getLogger(__name__)


def format_command_result(
    command_args,  # type: List[str]
    command_output,  # type: str
):
    # type: (...) -> str
    """Format command information for logging."""
    command_desc = format_command_args(command_args)
    text = f'Command arguments: {command_desc}\n'

    if not command_output:
        text += 'Command output: None'
    elif logger.getEffectiveLevel() > logging.DEBUG:
        text += 'Command output: [use --verbose to show]'
    else:
        if not command_output.endswith('\n'):
            command_output += '\n'
        text += f'Command output:\n{command_output}{LOG_DIVIDER}'

    return text


def get_legacy_build_wheel_path(
    names,  # type: List[str]
    temp_dir,  # type: str
    name,  # type: str
    command_args,  # type: List[str]
    command_output,  # type: str
):
    # type: (...) -> Optional[str]
    """Return the path to the wheel in the temporary build directory."""
    # Sort for determinism.
    names = sorted(names)
    if not names:
        msg = (
            'Legacy build of wheel for {!r} created no files.\n'
        ).format(name)
        msg += format_command_result(command_args, command_output)
        logger.warning(msg)
        return None

    if len(names) > 1:
        msg = (
            'Legacy build of wheel for {!r} created more than one file.\n'
            'Filenames (choosing first): {}\n'
        ).format(name, names)
        msg += format_command_result(command_args, command_output)
        logger.warning(msg)

    return os.path.join(temp_dir, names[0])


def build_wheel_legacy(
    name,  # type: str
    setup_py_path,  # type: str
    source_dir,  # type: str
    global_options,  # type: List[str]
    build_options,  # type: List[str]
    tempd,  # type: str
):
    # type: (...) -> Optional[str]
    """Build one unpacked package using the "legacy" build process.

    Returns path to wheel if successfully built. Otherwise, returns None.
    """
    wheel_args = make_setuptools_bdist_wheel_args(
        setup_py_path,
        global_options=global_options,
        build_options=build_options,
        destination_dir=tempd,
    )

    spin_message = f'Building wheel for {name} (setup.py)'
    with open_spinner(spin_message) as spinner:
        logger.debug('Destination directory: %s', tempd)

        try:
            output = call_subprocess(
                wheel_args,
                cwd=source_dir,
                spinner=spinner,
            )
        except Exception:
            spinner.finish("error")
            logger.error('Failed building wheel for %s', name)
            return None

        names = os.listdir(tempd)
        wheel_path = get_legacy_build_wheel_path(
            names=names,
            temp_dir=tempd,
            name=name,
            command_args=wheel_args,
            command_output=output,
        )
        return wheel_path
