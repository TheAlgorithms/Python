"""Handles all VCS (version control) support"""

import logging
import os
import shutil
import sys
import urllib.parse
from typing import (
    Any,
    Dict,
    Iterable,
    Iterator,
    List,
    Mapping,
    Optional,
    Tuple,
    Type,
    Union,
)

from pip._internal.cli.spinners import SpinnerInterface
from pip._internal.exceptions import BadCommand, InstallationError
from pip._internal.utils.misc import (
    HiddenText,
    ask_path_exists,
    backup_dir,
    display_path,
    hide_url,
    hide_value,
    rmtree,
)
from pip._internal.utils.subprocess import CommandArgs, call_subprocess, make_command
from pip._internal.utils.urls import get_url_scheme

__all__ = ['vcs']


logger = logging.getLogger(__name__)

AuthInfo = Tuple[Optional[str], Optional[str]]


def is_url(name):
    # type: (str) -> bool
    """
    Return true if the name looks like a URL.
    """
    scheme = get_url_scheme(name)
    if scheme is None:
        return False
    return scheme in ['http', 'https', 'file', 'ftp'] + vcs.all_schemes


def make_vcs_requirement_url(repo_url, rev, project_name, subdir=None):
    # type: (str, str, str, Optional[str]) -> str
    """
    Return the URL for a VCS requirement.

    Args:
      repo_url: the remote VCS url, with any needed VCS prefix (e.g. "git+").
      project_name: the (unescaped) project name.
    """
    egg_project_name = project_name.replace("-", "_")
    req = f'{repo_url}@{rev}#egg={egg_project_name}'
    if subdir:
        req += f'&subdirectory={subdir}'

    return req


def find_path_to_setup_from_repo_root(location, repo_root):
    # type: (str, str) -> Optional[str]
    """
    Find the path to `setup.py` by searching up the filesystem from `location`.
    Return the path to `setup.py` relative to `repo_root`.
    Return None if `setup.py` is in `repo_root` or cannot be found.
    """
    # find setup.py
    orig_location = location
    while not os.path.exists(os.path.join(location, 'setup.py')):
        last_location = location
        location = os.path.dirname(location)
        if location == last_location:
            # We've traversed up to the root of the filesystem without
            # finding setup.py
            logger.warning(
                "Could not find setup.py for directory %s (tried all "
                "parent directories)",
                orig_location,
            )
            return None

    if os.path.samefile(repo_root, location):
        return None

    return os.path.relpath(location, repo_root)


class RemoteNotFoundError(Exception):
    pass


class RevOptions:

    """
    Encapsulates a VCS-specific revision to install, along with any VCS
    install options.

    Instances of this class should be treated as if immutable.
    """

    def __init__(
        self,
        vc_class,  # type: Type[VersionControl]
        rev=None,  # type: Optional[str]
        extra_args=None,  # type: Optional[CommandArgs]
    ):
        # type: (...) -> None
        """
        Args:
          vc_class: a VersionControl subclass.
          rev: the name of the revision to install.
          extra_args: a list of extra options.
        """
        if extra_args is None:
            extra_args = []

        self.extra_args = extra_args
        self.rev = rev
        self.vc_class = vc_class
        self.branch_name = None  # type: Optional[str]

    def __repr__(self):
        # type: () -> str
        return f'<RevOptions {self.vc_class.name}: rev={self.rev!r}>'

    @property
    def arg_rev(self):
        # type: () -> Optional[str]
        if self.rev is None:
            return self.vc_class.default_arg_rev

        return self.rev

    def to_args(self):
        # type: () -> CommandArgs
        """
        Return the VCS-specific command arguments.
        """
        args = []  # type: CommandArgs
        rev = self.arg_rev
        if rev is not None:
            args += self.vc_class.get_base_rev_args(rev)
        args += self.extra_args

        return args

    def to_display(self):
        # type: () -> str
        if not self.rev:
            return ''

        return f' (to revision {self.rev})'

    def make_new(self, rev):
        # type: (str) -> RevOptions
        """
        Make a copy of the current instance, but with a new rev.

        Args:
          rev: the name of the revision for the new object.
        """
        return self.vc_class.make_rev_options(rev, extra_args=self.extra_args)


class VcsSupport:
    _registry = {}  # type: Dict[str, VersionControl]
    schemes = ['ssh', 'git', 'hg', 'bzr', 'sftp', 'svn']

    def __init__(self):
        # type: () -> None
        # Register more schemes with urlparse for various version control
        # systems
        urllib.parse.uses_netloc.extend(self.schemes)
        super().__init__()

    def __iter__(self):
        # type: () -> Iterator[str]
        return self._registry.__iter__()

    @property
    def backends(self):
        # type: () -> List[VersionControl]
        return list(self._registry.values())

    @property
    def dirnames(self):
        # type: () -> List[str]
        return [backend.dirname for backend in self.backends]

    @property
    def all_schemes(self):
        # type: () -> List[str]
        schemes = []  # type: List[str]
        for backend in self.backends:
            schemes.extend(backend.schemes)
        return schemes

    def register(self, cls):
        # type: (Type[VersionControl]) -> None
        if not hasattr(cls, 'name'):
            logger.warning('Cannot register VCS %s', cls.__name__)
            return
        if cls.name not in self._registry:
            self._registry[cls.name] = cls()
            logger.debug('Registered VCS backend: %s', cls.name)

    def unregister(self, name):
        # type: (str) -> None
        if name in self._registry:
            del self._registry[name]

    def get_backend_for_dir(self, location):
        # type: (str) -> Optional[VersionControl]
        """
        Return a VersionControl object if a repository of that type is found
        at the given directory.
        """
        vcs_backends = {}
        for vcs_backend in self._registry.values():
            repo_path = vcs_backend.get_repository_root(location)
            if not repo_path:
                continue
            logger.debug('Determine that %s uses VCS: %s',
                         location, vcs_backend.name)
            vcs_backends[repo_path] = vcs_backend

        if not vcs_backends:
            return None

        # Choose the VCS in the inner-most directory. Since all repository
        # roots found here would be either `location` or one of its
        # parents, the longest path should have the most path components,
        # i.e. the backend representing the inner-most repository.
        inner_most_repo_path = max(vcs_backends, key=len)
        return vcs_backends[inner_most_repo_path]

    def get_backend_for_scheme(self, scheme):
        # type: (str) -> Optional[VersionControl]
        """
        Return a VersionControl object or None.
        """
        for vcs_backend in self._registry.values():
            if scheme in vcs_backend.schemes:
                return vcs_backend
        return None

    def get_backend(self, name):
        # type: (str) -> Optional[VersionControl]
        """
        Return a VersionControl object or None.
        """
        name = name.lower()
        return self._registry.get(name)


vcs = VcsSupport()


class VersionControl:
    name = ''
    dirname = ''
    repo_name = ''
    # List of supported schemes for this Version Control
    schemes = ()  # type: Tuple[str, ...]
    # Iterable of environment variable names to pass to call_subprocess().
    unset_environ = ()  # type: Tuple[str, ...]
    default_arg_rev = None  # type: Optional[str]

    @classmethod
    def should_add_vcs_url_prefix(cls, remote_url):
        # type: (str) -> bool
        """
        Return whether the vcs prefix (e.g. "git+") should be added to a
        repository's remote url when used in a requirement.
        """
        return not remote_url.lower().startswith(f'{cls.name}:')

    @classmethod
    def get_subdirectory(cls, location):
        # type: (str) -> Optional[str]
        """
        Return the path to setup.py, relative to the repo root.
        Return None if setup.py is in the repo root.
        """
        return None

    @classmethod
    def get_requirement_revision(cls, repo_dir):
        # type: (str) -> str
        """
        Return the revision string that should be used in a requirement.
        """
        return cls.get_revision(repo_dir)

    @classmethod
    def get_src_requirement(cls, repo_dir, project_name):
        # type: (str, str) -> str
        """
        Return the requirement string to use to redownload the files
        currently at the given repository directory.

        Args:
          project_name: the (unescaped) project name.

        The return value has a form similar to the following:

            {repository_url}@{revision}#egg={project_name}
        """
        repo_url = cls.get_remote_url(repo_dir)

        if cls.should_add_vcs_url_prefix(repo_url):
            repo_url = f'{cls.name}+{repo_url}'

        revision = cls.get_requirement_revision(repo_dir)
        subdir = cls.get_subdirectory(repo_dir)
        req = make_vcs_requirement_url(repo_url, revision, project_name,
                                       subdir=subdir)

        return req

    @staticmethod
    def get_base_rev_args(rev):
        # type: (str) -> List[str]
        """
        Return the base revision arguments for a vcs command.

        Args:
          rev: the name of a revision to install.  Cannot be None.
        """
        raise NotImplementedError

    def is_immutable_rev_checkout(self, url, dest):
        # type: (str, str) -> bool
        """
        Return true if the commit hash checked out at dest matches
        the revision in url.

        Always return False, if the VCS does not support immutable commit
        hashes.

        This method does not check if there are local uncommitted changes
        in dest after checkout, as pip currently has no use case for that.
        """
        return False

    @classmethod
    def make_rev_options(cls, rev=None, extra_args=None):
        # type: (Optional[str], Optional[CommandArgs]) -> RevOptions
        """
        Return a RevOptions object.

        Args:
          rev: the name of a revision to install.
          extra_args: a list of extra options.
        """
        return RevOptions(cls, rev, extra_args=extra_args)

    @classmethod
    def _is_local_repository(cls, repo):
        # type: (str) -> bool
        """
           posix absolute paths start with os.path.sep,
           win32 ones start with drive (like c:\\folder)
        """
        drive, tail = os.path.splitdrive(repo)
        return repo.startswith(os.path.sep) or bool(drive)

    @classmethod
    def get_netloc_and_auth(cls, netloc, scheme):
        # type: (str, str) -> Tuple[str, Tuple[Optional[str], Optional[str]]]
        """
        Parse the repository URL's netloc, and return the new netloc to use
        along with auth information.

        Args:
          netloc: the original repository URL netloc.
          scheme: the repository URL's scheme without the vcs prefix.

        This is mainly for the Subversion class to override, so that auth
        information can be provided via the --username and --password options
        instead of through the URL.  For other subclasses like Git without
        such an option, auth information must stay in the URL.

        Returns: (netloc, (username, password)).
        """
        return netloc, (None, None)

    @classmethod
    def get_url_rev_and_auth(cls, url):
        # type: (str) -> Tuple[str, Optional[str], AuthInfo]
        """
        Parse the repository URL to use, and return the URL, revision,
        and auth info to use.

        Returns: (url, rev, (username, password)).
        """
        scheme, netloc, path, query, frag = urllib.parse.urlsplit(url)
        if '+' not in scheme:
            raise ValueError(
                "Sorry, {!r} is a malformed VCS url. "
                "The format is <vcs>+<protocol>://<url>, "
                "e.g. svn+http://myrepo/svn/MyApp#egg=MyApp".format(url)
            )
        # Remove the vcs prefix.
        scheme = scheme.split('+', 1)[1]
        netloc, user_pass = cls.get_netloc_and_auth(netloc, scheme)
        rev = None
        if '@' in path:
            path, rev = path.rsplit('@', 1)
            if not rev:
                raise InstallationError(
                    "The URL {!r} has an empty revision (after @) "
                    "which is not supported. Include a revision after @ "
                    "or remove @ from the URL.".format(url)
                )
        url = urllib.parse.urlunsplit((scheme, netloc, path, query, ''))
        return url, rev, user_pass

    @staticmethod
    def make_rev_args(username, password):
        # type: (Optional[str], Optional[HiddenText]) -> CommandArgs
        """
        Return the RevOptions "extra arguments" to use in obtain().
        """
        return []

    def get_url_rev_options(self, url):
        # type: (HiddenText) -> Tuple[HiddenText, RevOptions]
        """
        Return the URL and RevOptions object to use in obtain(),
        as a tuple (url, rev_options).
        """
        secret_url, rev, user_pass = self.get_url_rev_and_auth(url.secret)
        username, secret_password = user_pass
        password = None  # type: Optional[HiddenText]
        if secret_password is not None:
            password = hide_value(secret_password)
        extra_args = self.make_rev_args(username, password)
        rev_options = self.make_rev_options(rev, extra_args=extra_args)

        return hide_url(secret_url), rev_options

    @staticmethod
    def normalize_url(url):
        # type: (str) -> str
        """
        Normalize a URL for comparison by unquoting it and removing any
        trailing slash.
        """
        return urllib.parse.unquote(url).rstrip('/')

    @classmethod
    def compare_urls(cls, url1, url2):
        # type: (str, str) -> bool
        """
        Compare two repo URLs for identity, ignoring incidental differences.
        """
        return (cls.normalize_url(url1) == cls.normalize_url(url2))

    def fetch_new(self, dest, url, rev_options):
        # type: (str, HiddenText, RevOptions) -> None
        """
        Fetch a revision from a repository, in the case that this is the
        first fetch from the repository.

        Args:
          dest: the directory to fetch the repository to.
          rev_options: a RevOptions object.
        """
        raise NotImplementedError

    def switch(self, dest, url, rev_options):
        # type: (str, HiddenText, RevOptions) -> None
        """
        Switch the repo at ``dest`` to point to ``URL``.

        Args:
          rev_options: a RevOptions object.
        """
        raise NotImplementedError

    def update(self, dest, url, rev_options):
        # type: (str, HiddenText, RevOptions) -> None
        """
        Update an already-existing repo to the given ``rev_options``.

        Args:
          rev_options: a RevOptions object.
        """
        raise NotImplementedError

    @classmethod
    def is_commit_id_equal(cls, dest, name):
        # type: (str, Optional[str]) -> bool
        """
        Return whether the id of the current commit equals the given name.

        Args:
          dest: the repository directory.
          name: a string name.
        """
        raise NotImplementedError

    def obtain(self, dest, url):
        # type: (str, HiddenText) -> None
        """
        Install or update in editable mode the package represented by this
        VersionControl object.

        :param dest: the repository directory in which to install or update.
        :param url: the repository URL starting with a vcs prefix.
        """
        url, rev_options = self.get_url_rev_options(url)

        if not os.path.exists(dest):
            self.fetch_new(dest, url, rev_options)
            return

        rev_display = rev_options.to_display()
        if self.is_repository_directory(dest):
            existing_url = self.get_remote_url(dest)
            if self.compare_urls(existing_url, url.secret):
                logger.debug(
                    '%s in %s exists, and has correct URL (%s)',
                    self.repo_name.title(),
                    display_path(dest),
                    url,
                )
                if not self.is_commit_id_equal(dest, rev_options.rev):
                    logger.info(
                        'Updating %s %s%s',
                        display_path(dest),
                        self.repo_name,
                        rev_display,
                    )
                    self.update(dest, url, rev_options)
                else:
                    logger.info('Skipping because already up-to-date.')
                return

            logger.warning(
                '%s %s in %s exists with URL %s',
                self.name,
                self.repo_name,
                display_path(dest),
                existing_url,
            )
            prompt = ('(s)witch, (i)gnore, (w)ipe, (b)ackup ',
                      ('s', 'i', 'w', 'b'))
        else:
            logger.warning(
                'Directory %s already exists, and is not a %s %s.',
                dest,
                self.name,
                self.repo_name,
            )
            # https://github.com/python/mypy/issues/1174
            prompt = ('(i)gnore, (w)ipe, (b)ackup ',  # type: ignore
                      ('i', 'w', 'b'))

        logger.warning(
            'The plan is to install the %s repository %s',
            self.name,
            url,
        )
        response = ask_path_exists('What to do?  {}'.format(
            prompt[0]), prompt[1])

        if response == 'a':
            sys.exit(-1)

        if response == 'w':
            logger.warning('Deleting %s', display_path(dest))
            rmtree(dest)
            self.fetch_new(dest, url, rev_options)
            return

        if response == 'b':
            dest_dir = backup_dir(dest)
            logger.warning(
                'Backing up %s to %s', display_path(dest), dest_dir,
            )
            shutil.move(dest, dest_dir)
            self.fetch_new(dest, url, rev_options)
            return

        # Do nothing if the response is "i".
        if response == 's':
            logger.info(
                'Switching %s %s to %s%s',
                self.repo_name,
                display_path(dest),
                url,
                rev_display,
            )
            self.switch(dest, url, rev_options)

    def unpack(self, location, url):
        # type: (str, HiddenText) -> None
        """
        Clean up current location and download the url repository
        (and vcs infos) into location

        :param url: the repository URL starting with a vcs prefix.
        """
        if os.path.exists(location):
            rmtree(location)
        self.obtain(location, url=url)

    @classmethod
    def get_remote_url(cls, location):
        # type: (str) -> str
        """
        Return the url used at location

        Raises RemoteNotFoundError if the repository does not have a remote
        url configured.
        """
        raise NotImplementedError

    @classmethod
    def get_revision(cls, location):
        # type: (str) -> str
        """
        Return the current commit id of the files at the given location.
        """
        raise NotImplementedError

    @classmethod
    def run_command(
        cls,
        cmd,  # type: Union[List[str], CommandArgs]
        show_stdout=True,  # type: bool
        cwd=None,  # type: Optional[str]
        on_returncode='raise',  # type: str
        extra_ok_returncodes=None,  # type: Optional[Iterable[int]]
        command_desc=None,  # type: Optional[str]
        extra_environ=None,  # type: Optional[Mapping[str, Any]]
        spinner=None,  # type: Optional[SpinnerInterface]
        log_failed_cmd=True,  # type: bool
        stdout_only=False,  # type: bool
    ):
        # type: (...) -> str
        """
        Run a VCS subcommand
        This is simply a wrapper around call_subprocess that adds the VCS
        command name, and checks that the VCS is available
        """
        cmd = make_command(cls.name, *cmd)
        try:
            return call_subprocess(cmd, show_stdout, cwd,
                                   on_returncode=on_returncode,
                                   extra_ok_returncodes=extra_ok_returncodes,
                                   command_desc=command_desc,
                                   extra_environ=extra_environ,
                                   unset_environ=cls.unset_environ,
                                   spinner=spinner,
                                   log_failed_cmd=log_failed_cmd,
                                   stdout_only=stdout_only)
        except FileNotFoundError:
            # errno.ENOENT = no such file or directory
            # In other words, the VCS executable isn't available
            raise BadCommand(
                f'Cannot find command {cls.name!r} - do you have '
                f'{cls.name!r} installed and in your PATH?')
        except PermissionError:
            # errno.EACCES = Permission denied
            # This error occurs, for instance, when the command is installed
            # only for another user. So, the current user don't have
            # permission to call the other user command.
            raise BadCommand(
                f"No permission to execute {cls.name!r} - install it "
                f"locally, globally (ask admin), or check your PATH. "
                f"See possible solutions at "
                f"https://pip.pypa.io/en/latest/reference/pip_freeze/"
                f"#fixing-permission-denied."
            )

    @classmethod
    def is_repository_directory(cls, path):
        # type: (str) -> bool
        """
        Return whether a directory path is a repository directory.
        """
        logger.debug('Checking in %s for %s (%s)...',
                     path, cls.dirname, cls.name)
        return os.path.exists(os.path.join(path, cls.dirname))

    @classmethod
    def get_repository_root(cls, location):
        # type: (str) -> Optional[str]
        """
        Return the "root" (top-level) directory controlled by the vcs,
        or `None` if the directory is not in any.

        It is meant to be overridden to implement smarter detection
        mechanisms for specific vcs.

        This can do more than is_repository_directory() alone. For
        example, the Git override checks that Git is actually available.
        """
        if cls.is_repository_directory(location):
            return location
        return None
