import csv
import functools
import logging
import os
import sys
import sysconfig
from importlib.util import cache_from_source
from typing import Any, Callable, Dict, Iterable, Iterator, List, Optional, Set, Tuple

from pip._vendor import pkg_resources
from pip._vendor.pkg_resources import Distribution

from pip._internal.exceptions import UninstallationError
from pip._internal.locations import get_bin_prefix, get_bin_user
from pip._internal.utils.compat import WINDOWS
from pip._internal.utils.logging import indent_log
from pip._internal.utils.misc import (
    ask,
    dist_in_usersite,
    dist_is_local,
    egg_link_path,
    is_local,
    normalize_path,
    renames,
    rmtree,
)
from pip._internal.utils.temp_dir import AdjacentTempDirectory, TempDirectory

logger = logging.getLogger(__name__)


def _script_names(dist, script_name, is_gui):
    # type: (Distribution, str, bool) -> List[str]
    """Create the fully qualified name of the files created by
    {console,gui}_scripts for the given ``dist``.
    Returns the list of file names
    """
    if dist_in_usersite(dist):
        bin_dir = get_bin_user()
    else:
        bin_dir = get_bin_prefix()
    exe_name = os.path.join(bin_dir, script_name)
    paths_to_remove = [exe_name]
    if WINDOWS:
        paths_to_remove.append(exe_name + '.exe')
        paths_to_remove.append(exe_name + '.exe.manifest')
        if is_gui:
            paths_to_remove.append(exe_name + '-script.pyw')
        else:
            paths_to_remove.append(exe_name + '-script.py')
    return paths_to_remove


def _unique(fn):
    # type: (Callable[..., Iterator[Any]]) -> Callable[..., Iterator[Any]]
    @functools.wraps(fn)
    def unique(*args, **kw):
        # type: (Any, Any) -> Iterator[Any]
        seen = set()  # type: Set[Any]
        for item in fn(*args, **kw):
            if item not in seen:
                seen.add(item)
                yield item
    return unique


@_unique
def uninstallation_paths(dist):
    # type: (Distribution) -> Iterator[str]
    """
    Yield all the uninstallation paths for dist based on RECORD-without-.py[co]

    Yield paths to all the files in RECORD. For each .py file in RECORD, add
    the .pyc and .pyo in the same directory.

    UninstallPathSet.add() takes care of the __pycache__ .py[co].
    """
    r = csv.reader(dist.get_metadata_lines('RECORD'))
    for row in r:
        path = os.path.join(dist.location, row[0])
        yield path
        if path.endswith('.py'):
            dn, fn = os.path.split(path)
            base = fn[:-3]
            path = os.path.join(dn, base + '.pyc')
            yield path
            path = os.path.join(dn, base + '.pyo')
            yield path


def compact(paths):
    # type: (Iterable[str]) -> Set[str]
    """Compact a path set to contain the minimal number of paths
    necessary to contain all paths in the set. If /a/path/ and
    /a/path/to/a/file.txt are both in the set, leave only the
    shorter path."""

    sep = os.path.sep
    short_paths = set()  # type: Set[str]
    for path in sorted(paths, key=len):
        should_skip = any(
            path.startswith(shortpath.rstrip("*")) and
            path[len(shortpath.rstrip("*").rstrip(sep))] == sep
            for shortpath in short_paths
        )
        if not should_skip:
            short_paths.add(path)
    return short_paths


def compress_for_rename(paths):
    # type: (Iterable[str]) -> Set[str]
    """Returns a set containing the paths that need to be renamed.

    This set may include directories when the original sequence of paths
    included every file on disk.
    """
    case_map = {os.path.normcase(p): p for p in paths}
    remaining = set(case_map)
    unchecked = sorted({os.path.split(p)[0] for p in case_map.values()}, key=len)
    wildcards = set()  # type: Set[str]

    def norm_join(*a):
        # type: (str) -> str
        return os.path.normcase(os.path.join(*a))

    for root in unchecked:
        if any(os.path.normcase(root).startswith(w)
               for w in wildcards):
            # This directory has already been handled.
            continue

        all_files = set()  # type: Set[str]
        all_subdirs = set()  # type: Set[str]
        for dirname, subdirs, files in os.walk(root):
            all_subdirs.update(norm_join(root, dirname, d)
                               for d in subdirs)
            all_files.update(norm_join(root, dirname, f)
                             for f in files)
        # If all the files we found are in our remaining set of files to
        # remove, then remove them from the latter set and add a wildcard
        # for the directory.
        if not (all_files - remaining):
            remaining.difference_update(all_files)
            wildcards.add(root + os.sep)

    return set(map(case_map.__getitem__, remaining)) | wildcards


def compress_for_output_listing(paths):
    # type: (Iterable[str]) -> Tuple[Set[str], Set[str]]
    """Returns a tuple of 2 sets of which paths to display to user

    The first set contains paths that would be deleted. Files of a package
    are not added and the top-level directory of the package has a '*' added
    at the end - to signify that all it's contents are removed.

    The second set contains files that would have been skipped in the above
    folders.
    """

    will_remove = set(paths)
    will_skip = set()

    # Determine folders and files
    folders = set()
    files = set()
    for path in will_remove:
        if path.endswith(".pyc"):
            continue
        if path.endswith("__init__.py") or ".dist-info" in path:
            folders.add(os.path.dirname(path))
        files.add(path)

    # probably this one https://github.com/python/mypy/issues/390
    _normcased_files = set(map(os.path.normcase, files))  # type: ignore

    folders = compact(folders)

    # This walks the tree using os.walk to not miss extra folders
    # that might get added.
    for folder in folders:
        for dirpath, _, dirfiles in os.walk(folder):
            for fname in dirfiles:
                if fname.endswith(".pyc"):
                    continue

                file_ = os.path.join(dirpath, fname)
                if (os.path.isfile(file_) and
                        os.path.normcase(file_) not in _normcased_files):
                    # We are skipping this file. Add it to the set.
                    will_skip.add(file_)

    will_remove = files | {
        os.path.join(folder, "*") for folder in folders
    }

    return will_remove, will_skip


class StashedUninstallPathSet:
    """A set of file rename operations to stash files while
    tentatively uninstalling them."""
    def __init__(self):
        # type: () -> None
        # Mapping from source file root to [Adjacent]TempDirectory
        # for files under that directory.
        self._save_dirs = {}  # type: Dict[str, TempDirectory]
        # (old path, new path) tuples for each move that may need
        # to be undone.
        self._moves = []  # type: List[Tuple[str, str]]

    def _get_directory_stash(self, path):
        # type: (str) -> str
        """Stashes a directory.

        Directories are stashed adjacent to their original location if
        possible, or else moved/copied into the user's temp dir."""

        try:
            save_dir = AdjacentTempDirectory(path)  # type: TempDirectory
        except OSError:
            save_dir = TempDirectory(kind="uninstall")
        self._save_dirs[os.path.normcase(path)] = save_dir

        return save_dir.path

    def _get_file_stash(self, path):
        # type: (str) -> str
        """Stashes a file.

        If no root has been provided, one will be created for the directory
        in the user's temp directory."""
        path = os.path.normcase(path)
        head, old_head = os.path.dirname(path), None
        save_dir = None

        while head != old_head:
            try:
                save_dir = self._save_dirs[head]
                break
            except KeyError:
                pass
            head, old_head = os.path.dirname(head), head
        else:
            # Did not find any suitable root
            head = os.path.dirname(path)
            save_dir = TempDirectory(kind='uninstall')
            self._save_dirs[head] = save_dir

        relpath = os.path.relpath(path, head)
        if relpath and relpath != os.path.curdir:
            return os.path.join(save_dir.path, relpath)
        return save_dir.path

    def stash(self, path):
        # type: (str) -> str
        """Stashes the directory or file and returns its new location.
        Handle symlinks as files to avoid modifying the symlink targets.
        """
        path_is_dir = os.path.isdir(path) and not os.path.islink(path)
        if path_is_dir:
            new_path = self._get_directory_stash(path)
        else:
            new_path = self._get_file_stash(path)

        self._moves.append((path, new_path))
        if (path_is_dir and os.path.isdir(new_path)):
            # If we're moving a directory, we need to
            # remove the destination first or else it will be
            # moved to inside the existing directory.
            # We just created new_path ourselves, so it will
            # be removable.
            os.rmdir(new_path)
        renames(path, new_path)
        return new_path

    def commit(self):
        # type: () -> None
        """Commits the uninstall by removing stashed files."""
        for _, save_dir in self._save_dirs.items():
            save_dir.cleanup()
        self._moves = []
        self._save_dirs = {}

    def rollback(self):
        # type: () -> None
        """Undoes the uninstall by moving stashed files back."""
        for p in self._moves:
            logger.info("Moving to %s\n from %s", *p)

        for new_path, path in self._moves:
            try:
                logger.debug('Replacing %s from %s', new_path, path)
                if os.path.isfile(new_path) or os.path.islink(new_path):
                    os.unlink(new_path)
                elif os.path.isdir(new_path):
                    rmtree(new_path)
                renames(path, new_path)
            except OSError as ex:
                logger.error("Failed to restore %s", new_path)
                logger.debug("Exception: %s", ex)

        self.commit()

    @property
    def can_rollback(self):
        # type: () -> bool
        return bool(self._moves)


class UninstallPathSet:
    """A set of file paths to be removed in the uninstallation of a
    requirement."""
    def __init__(self, dist):
        # type: (Distribution) -> None
        self.paths = set()  # type: Set[str]
        self._refuse = set()  # type: Set[str]
        self.pth = {}  # type: Dict[str, UninstallPthEntries]
        self.dist = dist
        self._moved_paths = StashedUninstallPathSet()

    def _permitted(self, path):
        # type: (str) -> bool
        """
        Return True if the given path is one we are permitted to
        remove/modify, False otherwise.

        """
        return is_local(path)

    def add(self, path):
        # type: (str) -> None
        head, tail = os.path.split(path)

        # we normalize the head to resolve parent directory symlinks, but not
        # the tail, since we only want to uninstall symlinks, not their targets
        path = os.path.join(normalize_path(head), os.path.normcase(tail))

        if not os.path.exists(path):
            return
        if self._permitted(path):
            self.paths.add(path)
        else:
            self._refuse.add(path)

        # __pycache__ files can show up after 'installed-files.txt' is created,
        # due to imports
        if os.path.splitext(path)[1] == '.py':
            self.add(cache_from_source(path))

    def add_pth(self, pth_file, entry):
        # type: (str, str) -> None
        pth_file = normalize_path(pth_file)
        if self._permitted(pth_file):
            if pth_file not in self.pth:
                self.pth[pth_file] = UninstallPthEntries(pth_file)
            self.pth[pth_file].add(entry)
        else:
            self._refuse.add(pth_file)

    def remove(self, auto_confirm=False, verbose=False):
        # type: (bool, bool) -> None
        """Remove paths in ``self.paths`` with confirmation (unless
        ``auto_confirm`` is True)."""

        if not self.paths:
            logger.info(
                "Can't uninstall '%s'. No files were found to uninstall.",
                self.dist.project_name,
            )
            return

        dist_name_version = (
            self.dist.project_name + "-" + self.dist.version
        )
        logger.info('Uninstalling %s:', dist_name_version)

        with indent_log():
            if auto_confirm or self._allowed_to_proceed(verbose):
                moved = self._moved_paths

                for_rename = compress_for_rename(self.paths)

                for path in sorted(compact(for_rename)):
                    moved.stash(path)
                    logger.debug('Removing file or directory %s', path)

                for pth in self.pth.values():
                    pth.remove()

                logger.info('Successfully uninstalled %s', dist_name_version)

    def _allowed_to_proceed(self, verbose):
        # type: (bool) -> bool
        """Display which files would be deleted and prompt for confirmation
        """

        def _display(msg, paths):
            # type: (str, Iterable[str]) -> None
            if not paths:
                return

            logger.info(msg)
            with indent_log():
                for path in sorted(compact(paths)):
                    logger.info(path)

        if not verbose:
            will_remove, will_skip = compress_for_output_listing(self.paths)
        else:
            # In verbose mode, display all the files that are going to be
            # deleted.
            will_remove = set(self.paths)
            will_skip = set()

        _display('Would remove:', will_remove)
        _display('Would not remove (might be manually added):', will_skip)
        _display('Would not remove (outside of prefix):', self._refuse)
        if verbose:
            _display('Will actually move:', compress_for_rename(self.paths))

        return ask('Proceed (y/n)? ', ('y', 'n')) == 'y'

    def rollback(self):
        # type: () -> None
        """Rollback the changes previously made by remove()."""
        if not self._moved_paths.can_rollback:
            logger.error(
                "Can't roll back %s; was not uninstalled",
                self.dist.project_name,
            )
            return
        logger.info('Rolling back uninstall of %s', self.dist.project_name)
        self._moved_paths.rollback()
        for pth in self.pth.values():
            pth.rollback()

    def commit(self):
        # type: () -> None
        """Remove temporary save dir: rollback will no longer be possible."""
        self._moved_paths.commit()

    @classmethod
    def from_dist(cls, dist):
        # type: (Distribution) -> UninstallPathSet
        dist_path = normalize_path(dist.location)
        if not dist_is_local(dist):
            logger.info(
                "Not uninstalling %s at %s, outside environment %s",
                dist.key,
                dist_path,
                sys.prefix,
            )
            return cls(dist)

        if dist_path in {p for p in {sysconfig.get_path("stdlib"),
                                     sysconfig.get_path("platstdlib")}
                         if p}:
            logger.info(
                "Not uninstalling %s at %s, as it is in the standard library.",
                dist.key,
                dist_path,
            )
            return cls(dist)

        paths_to_remove = cls(dist)
        develop_egg_link = egg_link_path(dist)
        develop_egg_link_egg_info = '{}.egg-info'.format(
            pkg_resources.to_filename(dist.project_name))
        egg_info_exists = dist.egg_info and os.path.exists(dist.egg_info)
        # Special case for distutils installed package
        distutils_egg_info = getattr(dist._provider, 'path', None)

        # Uninstall cases order do matter as in the case of 2 installs of the
        # same package, pip needs to uninstall the currently detected version
        if (egg_info_exists and dist.egg_info.endswith('.egg-info') and
                not dist.egg_info.endswith(develop_egg_link_egg_info)):
            # if dist.egg_info.endswith(develop_egg_link_egg_info), we
            # are in fact in the develop_egg_link case
            paths_to_remove.add(dist.egg_info)
            if dist.has_metadata('installed-files.txt'):
                for installed_file in dist.get_metadata(
                        'installed-files.txt').splitlines():
                    path = os.path.normpath(
                        os.path.join(dist.egg_info, installed_file)
                    )
                    paths_to_remove.add(path)
            # FIXME: need a test for this elif block
            # occurs with --single-version-externally-managed/--record outside
            # of pip
            elif dist.has_metadata('top_level.txt'):
                if dist.has_metadata('namespace_packages.txt'):
                    namespaces = dist.get_metadata('namespace_packages.txt')
                else:
                    namespaces = []
                for top_level_pkg in [
                        p for p
                        in dist.get_metadata('top_level.txt').splitlines()
                        if p and p not in namespaces]:
                    path = os.path.join(dist.location, top_level_pkg)
                    paths_to_remove.add(path)
                    paths_to_remove.add(path + '.py')
                    paths_to_remove.add(path + '.pyc')
                    paths_to_remove.add(path + '.pyo')

        elif distutils_egg_info:
            raise UninstallationError(
                "Cannot uninstall {!r}. It is a distutils installed project "
                "and thus we cannot accurately determine which files belong "
                "to it which would lead to only a partial uninstall.".format(
                    dist.project_name,
                )
            )

        elif dist.location.endswith('.egg'):
            # package installed by easy_install
            # We cannot match on dist.egg_name because it can slightly vary
            # i.e. setuptools-0.6c11-py2.6.egg vs setuptools-0.6rc11-py2.6.egg
            paths_to_remove.add(dist.location)
            easy_install_egg = os.path.split(dist.location)[1]
            easy_install_pth = os.path.join(os.path.dirname(dist.location),
                                            'easy-install.pth')
            paths_to_remove.add_pth(easy_install_pth, './' + easy_install_egg)

        elif egg_info_exists and dist.egg_info.endswith('.dist-info'):
            for path in uninstallation_paths(dist):
                paths_to_remove.add(path)

        elif develop_egg_link:
            # develop egg
            with open(develop_egg_link) as fh:
                link_pointer = os.path.normcase(fh.readline().strip())
            assert (link_pointer == dist.location), (
                'Egg-link {} does not match installed location of {} '
                '(at {})'.format(
                    link_pointer, dist.project_name, dist.location)
            )
            paths_to_remove.add(develop_egg_link)
            easy_install_pth = os.path.join(os.path.dirname(develop_egg_link),
                                            'easy-install.pth')
            paths_to_remove.add_pth(easy_install_pth, dist.location)

        else:
            logger.debug(
                'Not sure how to uninstall: %s - Check: %s',
                dist, dist.location,
            )

        # find distutils scripts= scripts
        if dist.has_metadata('scripts') and dist.metadata_isdir('scripts'):
            for script in dist.metadata_listdir('scripts'):
                if dist_in_usersite(dist):
                    bin_dir = get_bin_user()
                else:
                    bin_dir = get_bin_prefix()
                paths_to_remove.add(os.path.join(bin_dir, script))
                if WINDOWS:
                    paths_to_remove.add(os.path.join(bin_dir, script) + '.bat')

        # find console_scripts
        _scripts_to_remove = []
        console_scripts = dist.get_entry_map(group='console_scripts')
        for name in console_scripts.keys():
            _scripts_to_remove.extend(_script_names(dist, name, False))
        # find gui_scripts
        gui_scripts = dist.get_entry_map(group='gui_scripts')
        for name in gui_scripts.keys():
            _scripts_to_remove.extend(_script_names(dist, name, True))

        for s in _scripts_to_remove:
            paths_to_remove.add(s)

        return paths_to_remove


class UninstallPthEntries:
    def __init__(self, pth_file):
        # type: (str) -> None
        self.file = pth_file
        self.entries = set()  # type: Set[str]
        self._saved_lines = None  # type: Optional[List[bytes]]

    def add(self, entry):
        # type: (str) -> None
        entry = os.path.normcase(entry)
        # On Windows, os.path.normcase converts the entry to use
        # backslashes.  This is correct for entries that describe absolute
        # paths outside of site-packages, but all the others use forward
        # slashes.
        # os.path.splitdrive is used instead of os.path.isabs because isabs
        # treats non-absolute paths with drive letter markings like c:foo\bar
        # as absolute paths. It also does not recognize UNC paths if they don't
        # have more than "\\sever\share". Valid examples: "\\server\share\" or
        # "\\server\share\folder".
        if WINDOWS and not os.path.splitdrive(entry)[0]:
            entry = entry.replace('\\', '/')
        self.entries.add(entry)

    def remove(self):
        # type: () -> None
        logger.debug('Removing pth entries from %s:', self.file)

        # If the file doesn't exist, log a warning and return
        if not os.path.isfile(self.file):
            logger.warning(
                "Cannot remove entries from nonexistent file %s", self.file
            )
            return
        with open(self.file, 'rb') as fh:
            # windows uses '\r\n' with py3k, but uses '\n' with py2.x
            lines = fh.readlines()
            self._saved_lines = lines
        if any(b'\r\n' in line for line in lines):
            endline = '\r\n'
        else:
            endline = '\n'
        # handle missing trailing newline
        if lines and not lines[-1].endswith(endline.encode("utf-8")):
            lines[-1] = lines[-1] + endline.encode("utf-8")
        for entry in self.entries:
            try:
                logger.debug('Removing entry: %s', entry)
                lines.remove((entry + endline).encode("utf-8"))
            except ValueError:
                pass
        with open(self.file, 'wb') as fh:
            fh.writelines(lines)

    def rollback(self):
        # type: () -> bool
        if self._saved_lines is None:
            logger.error(
                'Cannot roll back changes to %s, none were made', self.file
            )
            return False
        logger.debug('Rolling %s back to previous state', self.file)
        with open(self.file, 'wb') as fh:
            fh.writelines(self._saved_lines)
        return True
