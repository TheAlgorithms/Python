"""Orchestrator for building wheels from InstallRequirements.
"""

import logging
import os.path
import re
import shutil
from typing import Any, Callable, Iterable, List, Optional, Tuple

from pip._vendor.packaging.utils import canonicalize_name, canonicalize_version
from pip._vendor.packaging.version import InvalidVersion, Version

from pip._internal.cache import WheelCache
from pip._internal.exceptions import InvalidWheelFilename, UnsupportedWheel
from pip._internal.metadata import get_wheel_distribution
from pip._internal.models.link import Link
from pip._internal.models.wheel import Wheel
from pip._internal.operations.build.wheel import build_wheel_pep517
from pip._internal.operations.build.wheel_legacy import build_wheel_legacy
from pip._internal.req.req_install import InstallRequirement
from pip._internal.utils.logging import indent_log
from pip._internal.utils.misc import ensure_dir, hash_file, is_wheel_installed
from pip._internal.utils.setuptools_build import make_setuptools_clean_args
from pip._internal.utils.subprocess import call_subprocess
from pip._internal.utils.temp_dir import TempDirectory
from pip._internal.utils.urls import path_to_url
from pip._internal.vcs import vcs

logger = logging.getLogger(__name__)

_egg_info_re = re.compile(r'([a-z0-9_.]+)-([a-z0-9_.!+-]+)', re.IGNORECASE)

BinaryAllowedPredicate = Callable[[InstallRequirement], bool]
BuildResult = Tuple[List[InstallRequirement], List[InstallRequirement]]


def _contains_egg_info(s):
    # type: (str) -> bool
    """Determine whether the string looks like an egg_info.

    :param s: The string to parse. E.g. foo-2.1
    """
    return bool(_egg_info_re.search(s))


def _should_build(
    req,  # type: InstallRequirement
    need_wheel,  # type: bool
    check_binary_allowed,  # type: BinaryAllowedPredicate
):
    # type: (...) -> bool
    """Return whether an InstallRequirement should be built into a wheel."""
    if req.constraint:
        # never build requirements that are merely constraints
        return False
    if req.is_wheel:
        if need_wheel:
            logger.info(
                'Skipping %s, due to already being wheel.', req.name,
            )
        return False

    if need_wheel:
        # i.e. pip wheel, not pip install
        return True

    # From this point, this concerns the pip install command only
    # (need_wheel=False).

    if req.editable or not req.source_dir:
        return False

    if req.use_pep517:
        return True

    if not check_binary_allowed(req):
        logger.info(
            "Skipping wheel build for %s, due to binaries "
            "being disabled for it.", req.name,
        )
        return False

    if not is_wheel_installed():
        # we don't build legacy requirements if wheel is not installed
        logger.info(
            "Using legacy 'setup.py install' for %s, "
            "since package 'wheel' is not installed.", req.name,
        )
        return False

    return True


def should_build_for_wheel_command(
    req,  # type: InstallRequirement
):
    # type: (...) -> bool
    return _should_build(
        req, need_wheel=True, check_binary_allowed=_always_true
    )


def should_build_for_install_command(
    req,  # type: InstallRequirement
    check_binary_allowed,  # type: BinaryAllowedPredicate
):
    # type: (...) -> bool
    return _should_build(
        req, need_wheel=False, check_binary_allowed=check_binary_allowed
    )


def _should_cache(
    req,  # type: InstallRequirement
):
    # type: (...) -> Optional[bool]
    """
    Return whether a built InstallRequirement can be stored in the persistent
    wheel cache, assuming the wheel cache is available, and _should_build()
    has determined a wheel needs to be built.
    """
    if req.editable or not req.source_dir:
        # never cache editable requirements
        return False

    if req.link and req.link.is_vcs:
        # VCS checkout. Do not cache
        # unless it points to an immutable commit hash.
        assert not req.editable
        assert req.source_dir
        vcs_backend = vcs.get_backend_for_scheme(req.link.scheme)
        assert vcs_backend
        if vcs_backend.is_immutable_rev_checkout(req.link.url, req.source_dir):
            return True
        return False

    assert req.link
    base, ext = req.link.splitext()
    if _contains_egg_info(base):
        return True

    # Otherwise, do not cache.
    return False


def _get_cache_dir(
    req,  # type: InstallRequirement
    wheel_cache,  # type: WheelCache
):
    # type: (...) -> str
    """Return the persistent or temporary cache directory where the built
    wheel need to be stored.
    """
    cache_available = bool(wheel_cache.cache_dir)
    assert req.link
    if cache_available and _should_cache(req):
        cache_dir = wheel_cache.get_path_for_link(req.link)
    else:
        cache_dir = wheel_cache.get_ephem_path_for_link(req.link)
    return cache_dir


def _always_true(_):
    # type: (Any) -> bool
    return True


def _verify_one(req, wheel_path):
    # type: (InstallRequirement, str) -> None
    canonical_name = canonicalize_name(req.name or "")
    w = Wheel(os.path.basename(wheel_path))
    if canonicalize_name(w.name) != canonical_name:
        raise InvalidWheelFilename(
            "Wheel has unexpected file name: expected {!r}, "
            "got {!r}".format(canonical_name, w.name),
        )
    dist = get_wheel_distribution(wheel_path, canonical_name)
    dist_verstr = str(dist.version)
    if canonicalize_version(dist_verstr) != canonicalize_version(w.version):
        raise InvalidWheelFilename(
            "Wheel has unexpected file name: expected {!r}, "
            "got {!r}".format(dist_verstr, w.version),
        )
    metadata_version_value = dist.metadata_version
    if metadata_version_value is None:
        raise UnsupportedWheel("Missing Metadata-Version")
    try:
        metadata_version = Version(metadata_version_value)
    except InvalidVersion:
        msg = f"Invalid Metadata-Version: {metadata_version_value}"
        raise UnsupportedWheel(msg)
    if (metadata_version >= Version("1.2")
            and not isinstance(dist.version, Version)):
        raise UnsupportedWheel(
            "Metadata 1.2 mandates PEP 440 version, "
            "but {!r} is not".format(dist_verstr)
        )


def _build_one(
    req,  # type: InstallRequirement
    output_dir,  # type: str
    verify,  # type: bool
    build_options,  # type: List[str]
    global_options,  # type: List[str]
):
    # type: (...) -> Optional[str]
    """Build one wheel.

    :return: The filename of the built wheel, or None if the build failed.
    """
    try:
        ensure_dir(output_dir)
    except OSError as e:
        logger.warning(
            "Building wheel for %s failed: %s",
            req.name, e,
        )
        return None

    # Install build deps into temporary directory (PEP 518)
    with req.build_env:
        wheel_path = _build_one_inside_env(
            req, output_dir, build_options, global_options
        )
    if wheel_path and verify:
        try:
            _verify_one(req, wheel_path)
        except (InvalidWheelFilename, UnsupportedWheel) as e:
            logger.warning("Built wheel for %s is invalid: %s", req.name, e)
            return None
    return wheel_path


def _build_one_inside_env(
    req,  # type: InstallRequirement
    output_dir,  # type: str
    build_options,  # type: List[str]
    global_options,  # type: List[str]
):
    # type: (...) -> Optional[str]
    with TempDirectory(kind="wheel") as temp_dir:
        assert req.name
        if req.use_pep517:
            assert req.metadata_directory
            assert req.pep517_backend
            if global_options:
                logger.warning(
                    'Ignoring --global-option when building %s using PEP 517', req.name
                )
            if build_options:
                logger.warning(
                    'Ignoring --build-option when building %s using PEP 517', req.name
                )
            wheel_path = build_wheel_pep517(
                name=req.name,
                backend=req.pep517_backend,
                metadata_directory=req.metadata_directory,
                tempd=temp_dir.path,
            )
        else:
            wheel_path = build_wheel_legacy(
                name=req.name,
                setup_py_path=req.setup_py_path,
                source_dir=req.unpacked_source_directory,
                global_options=global_options,
                build_options=build_options,
                tempd=temp_dir.path,
            )

        if wheel_path is not None:
            wheel_name = os.path.basename(wheel_path)
            dest_path = os.path.join(output_dir, wheel_name)
            try:
                wheel_hash, length = hash_file(wheel_path)
                shutil.move(wheel_path, dest_path)
                logger.info('Created wheel for %s: '
                            'filename=%s size=%d sha256=%s',
                            req.name, wheel_name, length,
                            wheel_hash.hexdigest())
                logger.info('Stored in directory: %s', output_dir)
                return dest_path
            except Exception as e:
                logger.warning(
                    "Building wheel for %s failed: %s",
                    req.name, e,
                )
        # Ignore return, we can't do anything else useful.
        if not req.use_pep517:
            _clean_one_legacy(req, global_options)
        return None


def _clean_one_legacy(req, global_options):
    # type: (InstallRequirement, List[str]) -> bool
    clean_args = make_setuptools_clean_args(
        req.setup_py_path,
        global_options=global_options,
    )

    logger.info('Running setup.py clean for %s', req.name)
    try:
        call_subprocess(clean_args, cwd=req.source_dir)
        return True
    except Exception:
        logger.error('Failed cleaning build dir for %s', req.name)
        return False


def build(
    requirements,  # type: Iterable[InstallRequirement]
    wheel_cache,  # type: WheelCache
    verify,  # type: bool
    build_options,  # type: List[str]
    global_options,  # type: List[str]
):
    # type: (...) -> BuildResult
    """Build wheels.

    :return: The list of InstallRequirement that succeeded to build and
        the list of InstallRequirement that failed to build.
    """
    if not requirements:
        return [], []

    # Build the wheels.
    logger.info(
        'Building wheels for collected packages: %s',
        ', '.join(req.name for req in requirements),  # type: ignore
    )

    with indent_log():
        build_successes, build_failures = [], []
        for req in requirements:
            cache_dir = _get_cache_dir(req, wheel_cache)
            wheel_file = _build_one(
                req, cache_dir, verify, build_options, global_options
            )
            if wheel_file:
                # Update the link for this.
                req.link = Link(path_to_url(wheel_file))
                req.local_file_path = req.link.file_path
                assert req.link.is_wheel
                build_successes.append(req)
            else:
                build_failures.append(req)

    # notify success/failure
    if build_successes:
        logger.info(
            'Successfully built %s',
            ' '.join([req.name for req in build_successes]),  # type: ignore
        )
    if build_failures:
        logger.info(
            'Failed to build %s',
            ' '.join([req.name for req in build_failures]),  # type: ignore
        )
    # Return a list of requirements that failed to build
    return build_successes, build_failures
