import logging
import re
from typing import Container, Iterator, List, Optional, Union

from pip._vendor.packaging.version import LegacyVersion, Version

from pip._internal.utils.misc import stdlib_pkgs  # TODO: Move definition here.

DistributionVersion = Union[LegacyVersion, Version]

logger = logging.getLogger(__name__)


class BaseDistribution:
    @property
    def location(self):
        # type: () -> Optional[str]
        """Where the distribution is loaded from.

        A string value is not necessarily a filesystem path, since distributions
        can be loaded from other sources, e.g. arbitrary zip archives. ``None``
        means the distribution is created in-memory.
        """
        raise NotImplementedError()

    @property
    def metadata_version(self):
        # type: () -> Optional[str]
        """Value of "Metadata-Version:" in the distribution, if available."""
        raise NotImplementedError()

    @property
    def canonical_name(self):
        # type: () -> str
        raise NotImplementedError()

    @property
    def version(self):
        # type: () -> DistributionVersion
        raise NotImplementedError()

    @property
    def installer(self):
        # type: () -> str
        raise NotImplementedError()

    @property
    def editable(self):
        # type: () -> bool
        raise NotImplementedError()

    @property
    def local(self):
        # type: () -> bool
        raise NotImplementedError()

    @property
    def in_usersite(self):
        # type: () -> bool
        raise NotImplementedError()


class BaseEnvironment:
    """An environment containing distributions to introspect."""

    @classmethod
    def default(cls):
        # type: () -> BaseEnvironment
        raise NotImplementedError()

    @classmethod
    def from_paths(cls, paths):
        # type: (Optional[List[str]]) -> BaseEnvironment
        raise NotImplementedError()

    def get_distribution(self, name):
        # type: (str) -> Optional[BaseDistribution]
        """Given a requirement name, return the installed distributions."""
        raise NotImplementedError()

    def _iter_distributions(self):
        # type: () -> Iterator[BaseDistribution]
        """Iterate through installed distributions.

        This function should be implemented by subclass, but never called
        directly. Use the public ``iter_distribution()`` instead, which
        implements additional logic to make sure the distributions are valid.
        """
        raise NotImplementedError()

    def iter_distributions(self):
        # type: () -> Iterator[BaseDistribution]
        """Iterate through installed distributions."""
        for dist in self._iter_distributions():
            # Make sure the distribution actually comes from a valid Python
            # packaging distribution. Pip's AdjacentTempDirectory leaves folders
            # e.g. ``~atplotlib.dist-info`` if cleanup was interrupted. The
            # valid project name pattern is taken from PEP 508.
            project_name_valid = re.match(
                r"^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$",
                dist.canonical_name,
                flags=re.IGNORECASE,
            )
            if not project_name_valid:
                logger.warning(
                    "Ignoring invalid distribution %s (%s)",
                    dist.canonical_name,
                    dist.location,
                )
                continue
            yield dist

    def iter_installed_distributions(
        self,
        local_only=True,  # type: bool
        skip=stdlib_pkgs,  # type: Container[str]
        include_editables=True,  # type: bool
        editables_only=False,  # type: bool
        user_only=False,  # type: bool
    ):
        # type: (...) -> Iterator[BaseDistribution]
        """Return a list of installed distributions.

        :param local_only: If True (default), only return installations
        local to the current virtualenv, if in a virtualenv.
        :param skip: An iterable of canonicalized project names to ignore;
            defaults to ``stdlib_pkgs``.
        :param include_editables: If False, don't report editables.
        :param editables_only: If True, only report editables.
        :param user_only: If True, only report installations in the user
        site directory.
        """
        it = self.iter_distributions()
        if local_only:
            it = (d for d in it if d.local)
        if not include_editables:
            it = (d for d in it if not d.editable)
        if editables_only:
            it = (d for d in it if d.editable)
        if user_only:
            it = (d for d in it if d.in_usersite)
        return (d for d in it if d.canonical_name not in skip)
