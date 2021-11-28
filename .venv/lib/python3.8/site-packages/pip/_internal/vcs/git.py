import logging
import os.path
import re
import urllib.parse
import urllib.request
from typing import List, Optional, Tuple

from pip._vendor.packaging.version import _BaseVersion
from pip._vendor.packaging.version import parse as parse_version

from pip._internal.exceptions import BadCommand, InstallationError
from pip._internal.utils.misc import HiddenText, display_path, hide_url
from pip._internal.utils.subprocess import make_command
from pip._internal.vcs.versioncontrol import (
    AuthInfo,
    RemoteNotFoundError,
    RevOptions,
    VersionControl,
    find_path_to_setup_from_repo_root,
    vcs,
)

urlsplit = urllib.parse.urlsplit
urlunsplit = urllib.parse.urlunsplit


logger = logging.getLogger(__name__)


HASH_REGEX = re.compile('^[a-fA-F0-9]{40}$')


def looks_like_hash(sha):
    # type: (str) -> bool
    return bool(HASH_REGEX.match(sha))


class Git(VersionControl):
    name = 'git'
    dirname = '.git'
    repo_name = 'clone'
    schemes = (
        'git+http', 'git+https', 'git+ssh', 'git+git', 'git+file',
    )
    # Prevent the user's environment variables from interfering with pip:
    # https://github.com/pypa/pip/issues/1130
    unset_environ = ('GIT_DIR', 'GIT_WORK_TREE')
    default_arg_rev = 'HEAD'

    @staticmethod
    def get_base_rev_args(rev):
        # type: (str) -> List[str]
        return [rev]

    def is_immutable_rev_checkout(self, url, dest):
        # type: (str, str) -> bool
        _, rev_options = self.get_url_rev_options(hide_url(url))
        if not rev_options.rev:
            return False
        if not self.is_commit_id_equal(dest, rev_options.rev):
            # the current commit is different from rev,
            # which means rev was something else than a commit hash
            return False
        # return False in the rare case rev is both a commit hash
        # and a tag or a branch; we don't want to cache in that case
        # because that branch/tag could point to something else in the future
        is_tag_or_branch = bool(
            self.get_revision_sha(dest, rev_options.rev)[0]
        )
        return not is_tag_or_branch

    def get_git_version(self):
        # type: () -> _BaseVersion
        VERSION_PFX = 'git version '
        version = self.run_command(
            ['version'], show_stdout=False, stdout_only=True
        )
        if version.startswith(VERSION_PFX):
            version = version[len(VERSION_PFX):].split()[0]
        else:
            version = ''
        # get first 3 positions of the git version because
        # on windows it is x.y.z.windows.t, and this parses as
        # LegacyVersion which always smaller than a Version.
        version = '.'.join(version.split('.')[:3])
        return parse_version(version)

    @classmethod
    def get_current_branch(cls, location):
        # type: (str) -> Optional[str]
        """
        Return the current branch, or None if HEAD isn't at a branch
        (e.g. detached HEAD).
        """
        # git-symbolic-ref exits with empty stdout if "HEAD" is a detached
        # HEAD rather than a symbolic ref.  In addition, the -q causes the
        # command to exit with status code 1 instead of 128 in this case
        # and to suppress the message to stderr.
        args = ['symbolic-ref', '-q', 'HEAD']
        output = cls.run_command(
            args,
            extra_ok_returncodes=(1, ),
            show_stdout=False,
            stdout_only=True,
            cwd=location,
        )
        ref = output.strip()

        if ref.startswith('refs/heads/'):
            return ref[len('refs/heads/'):]

        return None

    @classmethod
    def get_revision_sha(cls, dest, rev):
        # type: (str, str) -> Tuple[Optional[str], bool]
        """
        Return (sha_or_none, is_branch), where sha_or_none is a commit hash
        if the revision names a remote branch or tag, otherwise None.

        Args:
          dest: the repository directory.
          rev: the revision name.
        """
        # Pass rev to pre-filter the list.
        output = cls.run_command(
            ['show-ref', rev],
            cwd=dest,
            show_stdout=False,
            stdout_only=True,
            on_returncode='ignore',
        )
        refs = {}
        # NOTE: We do not use splitlines here since that would split on other
        #       unicode separators, which can be maliciously used to install a
        #       different revision.
        for line in output.strip().split("\n"):
            line = line.rstrip("\r")
            if not line:
                continue
            try:
                ref_sha, ref_name = line.split(" ", maxsplit=2)
            except ValueError:
                # Include the offending line to simplify troubleshooting if
                # this error ever occurs.
                raise ValueError(f'unexpected show-ref line: {line!r}')

            refs[ref_name] = ref_sha

        branch_ref = f'refs/remotes/origin/{rev}'
        tag_ref = f'refs/tags/{rev}'

        sha = refs.get(branch_ref)
        if sha is not None:
            return (sha, True)

        sha = refs.get(tag_ref)

        return (sha, False)

    @classmethod
    def _should_fetch(cls, dest, rev):
        # type: (str, str) -> bool
        """
        Return true if rev is a ref or is a commit that we don't have locally.

        Branches and tags are not considered in this method because they are
        assumed to be always available locally (which is a normal outcome of
        ``git clone`` and ``git fetch --tags``).
        """
        if rev.startswith("refs/"):
            # Always fetch remote refs.
            return True

        if not looks_like_hash(rev):
            # Git fetch would fail with abbreviated commits.
            return False

        if cls.has_commit(dest, rev):
            # Don't fetch if we have the commit locally.
            return False

        return True

    @classmethod
    def resolve_revision(cls, dest, url, rev_options):
        # type: (str, HiddenText, RevOptions) -> RevOptions
        """
        Resolve a revision to a new RevOptions object with the SHA1 of the
        branch, tag, or ref if found.

        Args:
          rev_options: a RevOptions object.
        """
        rev = rev_options.arg_rev
        # The arg_rev property's implementation for Git ensures that the
        # rev return value is always non-None.
        assert rev is not None

        sha, is_branch = cls.get_revision_sha(dest, rev)

        if sha is not None:
            rev_options = rev_options.make_new(sha)
            rev_options.branch_name = rev if is_branch else None

            return rev_options

        # Do not show a warning for the common case of something that has
        # the form of a Git commit hash.
        if not looks_like_hash(rev):
            logger.warning(
                "Did not find branch or tag '%s', assuming revision or ref.",
                rev,
            )

        if not cls._should_fetch(dest, rev):
            return rev_options

        # fetch the requested revision
        cls.run_command(
            make_command('fetch', '-q', url, rev_options.to_args()),
            cwd=dest,
        )
        # Change the revision to the SHA of the ref we fetched
        sha = cls.get_revision(dest, rev='FETCH_HEAD')
        rev_options = rev_options.make_new(sha)

        return rev_options

    @classmethod
    def is_commit_id_equal(cls, dest, name):
        # type: (str, Optional[str]) -> bool
        """
        Return whether the current commit hash equals the given name.

        Args:
          dest: the repository directory.
          name: a string name.
        """
        if not name:
            # Then avoid an unnecessary subprocess call.
            return False

        return cls.get_revision(dest) == name

    def fetch_new(self, dest, url, rev_options):
        # type: (str, HiddenText, RevOptions) -> None
        rev_display = rev_options.to_display()
        logger.info('Cloning %s%s to %s', url, rev_display, display_path(dest))
        self.run_command(make_command('clone', '-q', url, dest))

        if rev_options.rev:
            # Then a specific revision was requested.
            rev_options = self.resolve_revision(dest, url, rev_options)
            branch_name = getattr(rev_options, 'branch_name', None)
            if branch_name is None:
                # Only do a checkout if the current commit id doesn't match
                # the requested revision.
                if not self.is_commit_id_equal(dest, rev_options.rev):
                    cmd_args = make_command(
                        'checkout', '-q', rev_options.to_args(),
                    )
                    self.run_command(cmd_args, cwd=dest)
            elif self.get_current_branch(dest) != branch_name:
                # Then a specific branch was requested, and that branch
                # is not yet checked out.
                track_branch = f'origin/{branch_name}'
                cmd_args = [
                    'checkout', '-b', branch_name, '--track', track_branch,
                ]
                self.run_command(cmd_args, cwd=dest)

        #: repo may contain submodules
        self.update_submodules(dest)

    def switch(self, dest, url, rev_options):
        # type: (str, HiddenText, RevOptions) -> None
        self.run_command(
            make_command('config', 'remote.origin.url', url),
            cwd=dest,
        )
        cmd_args = make_command('checkout', '-q', rev_options.to_args())
        self.run_command(cmd_args, cwd=dest)

        self.update_submodules(dest)

    def update(self, dest, url, rev_options):
        # type: (str, HiddenText, RevOptions) -> None
        # First fetch changes from the default remote
        if self.get_git_version() >= parse_version('1.9.0'):
            # fetch tags in addition to everything else
            self.run_command(['fetch', '-q', '--tags'], cwd=dest)
        else:
            self.run_command(['fetch', '-q'], cwd=dest)
        # Then reset to wanted revision (maybe even origin/master)
        rev_options = self.resolve_revision(dest, url, rev_options)
        cmd_args = make_command('reset', '--hard', '-q', rev_options.to_args())
        self.run_command(cmd_args, cwd=dest)
        #: update submodules
        self.update_submodules(dest)

    @classmethod
    def get_remote_url(cls, location):
        # type: (str) -> str
        """
        Return URL of the first remote encountered.

        Raises RemoteNotFoundError if the repository does not have a remote
        url configured.
        """
        # We need to pass 1 for extra_ok_returncodes since the command
        # exits with return code 1 if there are no matching lines.
        stdout = cls.run_command(
            ['config', '--get-regexp', r'remote\..*\.url'],
            extra_ok_returncodes=(1, ),
            show_stdout=False,
            stdout_only=True,
            cwd=location,
        )
        remotes = stdout.splitlines()
        try:
            found_remote = remotes[0]
        except IndexError:
            raise RemoteNotFoundError

        for remote in remotes:
            if remote.startswith('remote.origin.url '):
                found_remote = remote
                break
        url = found_remote.split(' ')[1]
        return url.strip()

    @classmethod
    def has_commit(cls, location, rev):
        # type: (str, str) -> bool
        """
        Check if rev is a commit that is available in the local repository.
        """
        try:
            cls.run_command(
                ['rev-parse', '-q', '--verify', "sha^" + rev],
                cwd=location,
                log_failed_cmd=False,
            )
        except InstallationError:
            return False
        else:
            return True

    @classmethod
    def get_revision(cls, location, rev=None):
        # type: (str, Optional[str]) -> str
        if rev is None:
            rev = 'HEAD'
        current_rev = cls.run_command(
            ['rev-parse', rev],
            show_stdout=False,
            stdout_only=True,
            cwd=location,
        )
        return current_rev.strip()

    @classmethod
    def get_subdirectory(cls, location):
        # type: (str) -> Optional[str]
        """
        Return the path to setup.py, relative to the repo root.
        Return None if setup.py is in the repo root.
        """
        # find the repo root
        git_dir = cls.run_command(
            ['rev-parse', '--git-dir'],
            show_stdout=False,
            stdout_only=True,
            cwd=location,
        ).strip()
        if not os.path.isabs(git_dir):
            git_dir = os.path.join(location, git_dir)
        repo_root = os.path.abspath(os.path.join(git_dir, '..'))
        return find_path_to_setup_from_repo_root(location, repo_root)

    @classmethod
    def get_url_rev_and_auth(cls, url):
        # type: (str) -> Tuple[str, Optional[str], AuthInfo]
        """
        Prefixes stub URLs like 'user@hostname:user/repo.git' with 'ssh://'.
        That's required because although they use SSH they sometimes don't
        work with a ssh:// scheme (e.g. GitHub). But we need a scheme for
        parsing. Hence we remove it again afterwards and return it as a stub.
        """
        # Works around an apparent Git bug
        # (see https://article.gmane.org/gmane.comp.version-control.git/146500)
        scheme, netloc, path, query, fragment = urlsplit(url)
        if scheme.endswith('file'):
            initial_slashes = path[:-len(path.lstrip('/'))]
            newpath = (
                initial_slashes +
                urllib.request.url2pathname(path)
                .replace('\\', '/').lstrip('/')
            )
            after_plus = scheme.find('+') + 1
            url = scheme[:after_plus] + urlunsplit(
                (scheme[after_plus:], netloc, newpath, query, fragment),
            )

        if '://' not in url:
            assert 'file:' not in url
            url = url.replace('git+', 'git+ssh://')
            url, rev, user_pass = super().get_url_rev_and_auth(url)
            url = url.replace('ssh://', '')
        else:
            url, rev, user_pass = super().get_url_rev_and_auth(url)

        return url, rev, user_pass

    @classmethod
    def update_submodules(cls, location):
        # type: (str) -> None
        if not os.path.exists(os.path.join(location, '.gitmodules')):
            return
        cls.run_command(
            ['submodule', 'update', '--init', '--recursive', '-q'],
            cwd=location,
        )

    @classmethod
    def get_repository_root(cls, location):
        # type: (str) -> Optional[str]
        loc = super().get_repository_root(location)
        if loc:
            return loc
        try:
            r = cls.run_command(
                ['rev-parse', '--show-toplevel'],
                cwd=location,
                show_stdout=False,
                stdout_only=True,
                on_returncode='raise',
                log_failed_cmd=False,
            )
        except BadCommand:
            logger.debug("could not determine if %s is under git control "
                         "because git is not available", location)
            return None
        except InstallationError:
            return None
        return os.path.normpath(r.rstrip('\r\n'))


vcs.register(Git)
