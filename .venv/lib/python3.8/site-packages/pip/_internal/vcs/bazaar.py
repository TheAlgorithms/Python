import logging
from typing import List, Optional, Tuple

from pip._internal.utils.misc import HiddenText, display_path
from pip._internal.utils.subprocess import make_command
from pip._internal.utils.urls import path_to_url
from pip._internal.vcs.versioncontrol import (
    AuthInfo,
    RemoteNotFoundError,
    RevOptions,
    VersionControl,
    vcs,
)

logger = logging.getLogger(__name__)


class Bazaar(VersionControl):
    name = 'bzr'
    dirname = '.bzr'
    repo_name = 'branch'
    schemes = (
        'bzr+http', 'bzr+https', 'bzr+ssh', 'bzr+sftp', 'bzr+ftp',
        'bzr+lp', 'bzr+file'
    )

    @staticmethod
    def get_base_rev_args(rev):
        # type: (str) -> List[str]
        return ['-r', rev]

    def fetch_new(self, dest, url, rev_options):
        # type: (str, HiddenText, RevOptions) -> None
        rev_display = rev_options.to_display()
        logger.info(
            'Checking out %s%s to %s',
            url,
            rev_display,
            display_path(dest),
        )
        cmd_args = (
            make_command('branch', '-q', rev_options.to_args(), url, dest)
        )
        self.run_command(cmd_args)

    def switch(self, dest, url, rev_options):
        # type: (str, HiddenText, RevOptions) -> None
        self.run_command(make_command('switch', url), cwd=dest)

    def update(self, dest, url, rev_options):
        # type: (str, HiddenText, RevOptions) -> None
        cmd_args = make_command('pull', '-q', rev_options.to_args())
        self.run_command(cmd_args, cwd=dest)

    @classmethod
    def get_url_rev_and_auth(cls, url):
        # type: (str) -> Tuple[str, Optional[str], AuthInfo]
        # hotfix the URL scheme after removing bzr+ from bzr+ssh:// readd it
        url, rev, user_pass = super().get_url_rev_and_auth(url)
        if url.startswith('ssh://'):
            url = 'bzr+' + url
        return url, rev, user_pass

    @classmethod
    def get_remote_url(cls, location):
        # type: (str) -> str
        urls = cls.run_command(
            ['info'], show_stdout=False, stdout_only=True, cwd=location
        )
        for line in urls.splitlines():
            line = line.strip()
            for x in ('checkout of branch: ',
                      'parent branch: '):
                if line.startswith(x):
                    repo = line.split(x)[1]
                    if cls._is_local_repository(repo):
                        return path_to_url(repo)
                    return repo
        raise RemoteNotFoundError

    @classmethod
    def get_revision(cls, location):
        # type: (str) -> str
        revision = cls.run_command(
            ['revno'], show_stdout=False, stdout_only=True, cwd=location,
        )
        return revision.splitlines()[-1]

    @classmethod
    def is_commit_id_equal(cls, dest, name):
        # type: (str, Optional[str]) -> bool
        """Always assume the versions don't match"""
        return False


vcs.register(Bazaar)
