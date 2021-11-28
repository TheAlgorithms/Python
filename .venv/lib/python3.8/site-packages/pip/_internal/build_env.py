"""Build Environment used for isolation during sdist building
"""

import contextlib
import logging
import os
import pathlib
import sys
import textwrap
import zipfile
from collections import OrderedDict
from sysconfig import get_paths
from types import TracebackType
from typing import TYPE_CHECKING, Iterable, Iterator, List, Optional, Set, Tuple, Type

from pip._vendor.certifi import where
from pip._vendor.pkg_resources import Requirement, VersionConflict, WorkingSet

from pip import __file__ as pip_location
from pip._internal.cli.spinners import open_spinner
from pip._internal.locations import get_platlib, get_prefixed_libs, get_purelib
from pip._internal.utils.subprocess import call_subprocess
from pip._internal.utils.temp_dir import TempDirectory, tempdir_kinds

if TYPE_CHECKING:
    from pip._internal.index.package_finder import PackageFinder

logger = logging.getLogger(__name__)


class _Prefix:

    def __init__(self, path):
        # type: (str) -> None
        self.path = path
        self.setup = False
        self.bin_dir = get_paths(
            'nt' if os.name == 'nt' else 'posix_prefix',
            vars={'base': path, 'platbase': path}
        )['scripts']
        self.lib_dirs = get_prefixed_libs(path)


@contextlib.contextmanager
def _create_standalone_pip() -> Iterator[str]:
    """Create a "standalone pip" zip file.

    The zip file's content is identical to the currently-running pip.
    It will be used to install requirements into the build environment.
    """
    source = pathlib.Path(pip_location).resolve().parent

    # Return the current instance if it is already a zip file. This can happen
    # if a PEP 517 requirement is an sdist itself.
    if not source.is_dir() and source.parent.name == "__env_pip__.zip":
        yield str(source)
        return

    with TempDirectory(kind="standalone-pip") as tmp_dir:
        pip_zip = os.path.join(tmp_dir.path, "__env_pip__.zip")
        with zipfile.ZipFile(pip_zip, "w") as zf:
            for child in source.rglob("*"):
                zf.write(child, child.relative_to(source.parent).as_posix())
        yield os.path.join(pip_zip, "pip")


class BuildEnvironment:
    """Creates and manages an isolated environment to install build deps
    """

    def __init__(self):
        # type: () -> None
        temp_dir = TempDirectory(
            kind=tempdir_kinds.BUILD_ENV, globally_managed=True
        )

        self._prefixes = OrderedDict(
            (name, _Prefix(os.path.join(temp_dir.path, name)))
            for name in ('normal', 'overlay')
        )

        self._bin_dirs = []  # type: List[str]
        self._lib_dirs = []  # type: List[str]
        for prefix in reversed(list(self._prefixes.values())):
            self._bin_dirs.append(prefix.bin_dir)
            self._lib_dirs.extend(prefix.lib_dirs)

        # Customize site to:
        # - ensure .pth files are honored
        # - prevent access to system site packages
        system_sites = {
            os.path.normcase(site) for site in (get_purelib(), get_platlib())
        }
        self._site_dir = os.path.join(temp_dir.path, 'site')
        if not os.path.exists(self._site_dir):
            os.mkdir(self._site_dir)
        with open(os.path.join(self._site_dir, 'sitecustomize.py'), 'w') as fp:
            fp.write(textwrap.dedent(
                '''
                import os, site, sys

                # First, drop system-sites related paths.
                original_sys_path = sys.path[:]
                known_paths = set()
                for path in {system_sites!r}:
                    site.addsitedir(path, known_paths=known_paths)
                system_paths = set(
                    os.path.normcase(path)
                    for path in sys.path[len(original_sys_path):]
                )
                original_sys_path = [
                    path for path in original_sys_path
                    if os.path.normcase(path) not in system_paths
                ]
                sys.path = original_sys_path

                # Second, add lib directories.
                # ensuring .pth file are processed.
                for path in {lib_dirs!r}:
                    assert not path in sys.path
                    site.addsitedir(path)
                '''
            ).format(system_sites=system_sites, lib_dirs=self._lib_dirs))

    def __enter__(self):
        # type: () -> None
        self._save_env = {
            name: os.environ.get(name, None)
            for name in ('PATH', 'PYTHONNOUSERSITE', 'PYTHONPATH')
        }

        path = self._bin_dirs[:]
        old_path = self._save_env['PATH']
        if old_path:
            path.extend(old_path.split(os.pathsep))

        pythonpath = [self._site_dir]

        os.environ.update({
            'PATH': os.pathsep.join(path),
            'PYTHONNOUSERSITE': '1',
            'PYTHONPATH': os.pathsep.join(pythonpath),
        })

    def __exit__(
        self,
        exc_type,  # type: Optional[Type[BaseException]]
        exc_val,  # type: Optional[BaseException]
        exc_tb  # type: Optional[TracebackType]
    ):
        # type: (...) -> None
        for varname, old_value in self._save_env.items():
            if old_value is None:
                os.environ.pop(varname, None)
            else:
                os.environ[varname] = old_value

    def check_requirements(self, reqs):
        # type: (Iterable[str]) -> Tuple[Set[Tuple[str, str]], Set[str]]
        """Return 2 sets:
            - conflicting requirements: set of (installed, wanted) reqs tuples
            - missing requirements: set of reqs
        """
        missing = set()
        conflicting = set()
        if reqs:
            ws = WorkingSet(self._lib_dirs)
            for req in reqs:
                try:
                    if ws.find(Requirement.parse(req)) is None:
                        missing.add(req)
                except VersionConflict as e:
                    conflicting.add((str(e.args[0].as_requirement()),
                                     str(e.args[1])))
        return conflicting, missing

    def install_requirements(
        self,
        finder,  # type: PackageFinder
        requirements,  # type: Iterable[str]
        prefix_as_string,  # type: str
        message  # type: str
    ):
        # type: (...) -> None
        prefix = self._prefixes[prefix_as_string]
        assert not prefix.setup
        prefix.setup = True
        if not requirements:
            return
        with contextlib.ExitStack() as ctx:
            # TODO: Remove this block when dropping 3.6 support. Python 3.6
            # lacks importlib.resources and pep517 has issues loading files in
            # a zip, so we fallback to the "old" method by adding the current
            # pip directory to the child process's sys.path.
            if sys.version_info < (3, 7):
                pip_runnable = os.path.dirname(pip_location)
            else:
                pip_runnable = ctx.enter_context(_create_standalone_pip())
            self._install_requirements(
                pip_runnable,
                finder,
                requirements,
                prefix,
                message,
            )

    @staticmethod
    def _install_requirements(
        pip_runnable: str,
        finder: "PackageFinder",
        requirements: Iterable[str],
        prefix: _Prefix,
        message: str,
    ) -> None:
        args = [
            sys.executable, pip_runnable, 'install',
            '--ignore-installed', '--no-user', '--prefix', prefix.path,
            '--no-warn-script-location',
        ]  # type: List[str]
        if logger.getEffectiveLevel() <= logging.DEBUG:
            args.append('-v')
        for format_control in ('no_binary', 'only_binary'):
            formats = getattr(finder.format_control, format_control)
            args.extend(('--' + format_control.replace('_', '-'),
                         ','.join(sorted(formats or {':none:'}))))

        index_urls = finder.index_urls
        if index_urls:
            args.extend(['-i', index_urls[0]])
            for extra_index in index_urls[1:]:
                args.extend(['--extra-index-url', extra_index])
        else:
            args.append('--no-index')
        for link in finder.find_links:
            args.extend(['--find-links', link])

        for host in finder.trusted_hosts:
            args.extend(['--trusted-host', host])
        if finder.allow_all_prereleases:
            args.append('--pre')
        if finder.prefer_binary:
            args.append('--prefer-binary')
        args.append('--')
        args.extend(requirements)
        extra_environ = {"_PIP_STANDALONE_CERT": where()}
        with open_spinner(message) as spinner:
            call_subprocess(args, spinner=spinner, extra_environ=extra_environ)


class NoOpBuildEnvironment(BuildEnvironment):
    """A no-op drop-in replacement for BuildEnvironment
    """

    def __init__(self):
        # type: () -> None
        pass

    def __enter__(self):
        # type: () -> None
        pass

    def __exit__(
        self,
        exc_type,  # type: Optional[Type[BaseException]]
        exc_val,  # type: Optional[BaseException]
        exc_tb  # type: Optional[TracebackType]
    ):
        # type: (...) -> None
        pass

    def cleanup(self):
        # type: () -> None
        pass

    def install_requirements(
        self,
        finder,  # type: PackageFinder
        requirements,  # type: Iterable[str]
        prefix_as_string,  # type: str
        message  # type: str
    ):
        # type: (...) -> None
        raise NotImplementedError()
