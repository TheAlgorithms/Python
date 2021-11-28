import sys
from typing import List, Optional, Sequence

# Shim to wrap setup.py invocation with setuptools
#
# We set sys.argv[0] to the path to the underlying setup.py file so
# setuptools / distutils don't take the path to the setup.py to be "-c" when
# invoking via the shim.  This avoids e.g. the following manifest_maker
# warning: "warning: manifest_maker: standard file '-c' not found".
_SETUPTOOLS_SHIM = (
    "import io, os, sys, setuptools, tokenize; sys.argv[0] = {0!r}; __file__={0!r};"
    "f = getattr(tokenize, 'open', open)(__file__) "
    "if os.path.exists(__file__) "
    "else io.StringIO('from setuptools import setup; setup()');"
    "code = f.read().replace('\\r\\n', '\\n');"
    "f.close();"
    "exec(compile(code, __file__, 'exec'))"
)


def make_setuptools_shim_args(
    setup_py_path,  # type: str
    global_options=None,  # type: Sequence[str]
    no_user_config=False,  # type: bool
    unbuffered_output=False,  # type: bool
):
    # type: (...) -> List[str]
    """
    Get setuptools command arguments with shim wrapped setup file invocation.

    :param setup_py_path: The path to setup.py to be wrapped.
    :param global_options: Additional global options.
    :param no_user_config: If True, disables personal user configuration.
    :param unbuffered_output: If True, adds the unbuffered switch to the
     argument list.
    """
    args = [sys.executable]
    if unbuffered_output:
        args += ["-u"]
    args += ["-c", _SETUPTOOLS_SHIM.format(setup_py_path)]
    if global_options:
        args += global_options
    if no_user_config:
        args += ["--no-user-cfg"]
    return args


def make_setuptools_bdist_wheel_args(
    setup_py_path,  # type: str
    global_options,  # type: Sequence[str]
    build_options,  # type: Sequence[str]
    destination_dir,  # type: str
):
    # type: (...) -> List[str]
    # NOTE: Eventually, we'd want to also -S to the flags here, when we're
    # isolating. Currently, it breaks Python in virtualenvs, because it
    # relies on site.py to find parts of the standard library outside the
    # virtualenv.
    args = make_setuptools_shim_args(
        setup_py_path, global_options=global_options, unbuffered_output=True
    )
    args += ["bdist_wheel", "-d", destination_dir]
    args += build_options
    return args


def make_setuptools_clean_args(
    setup_py_path,  # type: str
    global_options,  # type: Sequence[str]
):
    # type: (...) -> List[str]
    args = make_setuptools_shim_args(
        setup_py_path, global_options=global_options, unbuffered_output=True
    )
    args += ["clean", "--all"]
    return args


def make_setuptools_develop_args(
    setup_py_path,  # type: str
    global_options,  # type: Sequence[str]
    install_options,  # type: Sequence[str]
    no_user_config,  # type: bool
    prefix,  # type: Optional[str]
    home,  # type: Optional[str]
    use_user_site,  # type: bool
):
    # type: (...) -> List[str]
    assert not (use_user_site and prefix)

    args = make_setuptools_shim_args(
        setup_py_path,
        global_options=global_options,
        no_user_config=no_user_config,
    )

    args += ["develop", "--no-deps"]

    args += install_options

    if prefix:
        args += ["--prefix", prefix]
    if home is not None:
        args += ["--install-dir", home]

    if use_user_site:
        args += ["--user", "--prefix="]

    return args


def make_setuptools_egg_info_args(
    setup_py_path,  # type: str
    egg_info_dir,  # type: Optional[str]
    no_user_config,  # type: bool
):
    # type: (...) -> List[str]
    args = make_setuptools_shim_args(setup_py_path, no_user_config=no_user_config)

    args += ["egg_info"]

    if egg_info_dir:
        args += ["--egg-base", egg_info_dir]

    return args


def make_setuptools_install_args(
    setup_py_path,  # type: str
    global_options,  # type: Sequence[str]
    install_options,  # type: Sequence[str]
    record_filename,  # type: str
    root,  # type: Optional[str]
    prefix,  # type: Optional[str]
    header_dir,  # type: Optional[str]
    home,  # type: Optional[str]
    use_user_site,  # type: bool
    no_user_config,  # type: bool
    pycompile,  # type: bool
):
    # type: (...) -> List[str]
    assert not (use_user_site and prefix)
    assert not (use_user_site and root)

    args = make_setuptools_shim_args(
        setup_py_path,
        global_options=global_options,
        no_user_config=no_user_config,
        unbuffered_output=True,
    )
    args += ["install", "--record", record_filename]
    args += ["--single-version-externally-managed"]

    if root is not None:
        args += ["--root", root]
    if prefix is not None:
        args += ["--prefix", prefix]
    if home is not None:
        args += ["--home", home]
    if use_user_site:
        args += ["--user", "--prefix="]

    if pycompile:
        args += ["--compile"]
    else:
        args += ["--no-compile"]

    if header_dir:
        args += ["--install-headers", header_dir]

    args += install_options

    return args
