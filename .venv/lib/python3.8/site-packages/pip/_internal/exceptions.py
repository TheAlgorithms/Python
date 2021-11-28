"""Exceptions used throughout package"""

import configparser
from itertools import chain, groupby, repeat
from typing import TYPE_CHECKING, Dict, List, Optional

from pip._vendor.pkg_resources import Distribution
from pip._vendor.requests.models import Request, Response

if TYPE_CHECKING:
    from hashlib import _Hash

    from pip._internal.req.req_install import InstallRequirement


class PipError(Exception):
    """Base pip exception"""


class ConfigurationError(PipError):
    """General exception in configuration"""


class InstallationError(PipError):
    """General exception during installation"""


class UninstallationError(PipError):
    """General exception during uninstallation"""


class NoneMetadataError(PipError):
    """
    Raised when accessing "METADATA" or "PKG-INFO" metadata for a
    pip._vendor.pkg_resources.Distribution object and
    `dist.has_metadata('METADATA')` returns True but
    `dist.get_metadata('METADATA')` returns None (and similarly for
    "PKG-INFO").
    """

    def __init__(self, dist, metadata_name):
        # type: (Distribution, str) -> None
        """
        :param dist: A Distribution object.
        :param metadata_name: The name of the metadata being accessed
            (can be "METADATA" or "PKG-INFO").
        """
        self.dist = dist
        self.metadata_name = metadata_name

    def __str__(self):
        # type: () -> str
        # Use `dist` in the error message because its stringification
        # includes more information, like the version and location.
        return (
            'None {} metadata found for distribution: {}'.format(
                self.metadata_name, self.dist,
            )
        )


class UserInstallationInvalid(InstallationError):
    """A --user install is requested on an environment without user site."""

    def __str__(self):
        # type: () -> str
        return "User base directory is not specified"


class InvalidSchemeCombination(InstallationError):
    def __str__(self):
        # type: () -> str
        before = ", ".join(str(a) for a in self.args[:-1])
        return f"Cannot set {before} and {self.args[-1]} together"


class DistributionNotFound(InstallationError):
    """Raised when a distribution cannot be found to satisfy a requirement"""


class RequirementsFileParseError(InstallationError):
    """Raised when a general error occurs parsing a requirements file line."""


class BestVersionAlreadyInstalled(PipError):
    """Raised when the most up-to-date version of a package is already
    installed."""


class BadCommand(PipError):
    """Raised when virtualenv or a command is not found"""


class CommandError(PipError):
    """Raised when there is an error in command-line arguments"""


class PreviousBuildDirError(PipError):
    """Raised when there's a previous conflicting build directory"""


class NetworkConnectionError(PipError):
    """HTTP connection error"""

    def __init__(self, error_msg, response=None, request=None):
        # type: (str, Response, Request) -> None
        """
        Initialize NetworkConnectionError with  `request` and `response`
        objects.
        """
        self.response = response
        self.request = request
        self.error_msg = error_msg
        if (self.response is not None and not self.request and
                hasattr(response, 'request')):
            self.request = self.response.request
        super().__init__(error_msg, response, request)

    def __str__(self):
        # type: () -> str
        return str(self.error_msg)


class InvalidWheelFilename(InstallationError):
    """Invalid wheel filename."""


class UnsupportedWheel(InstallationError):
    """Unsupported wheel."""


class MetadataInconsistent(InstallationError):
    """Built metadata contains inconsistent information.

    This is raised when the metadata contains values (e.g. name and version)
    that do not match the information previously obtained from sdist filename
    or user-supplied ``#egg=`` value.
    """
    def __init__(self, ireq, field, f_val, m_val):
        # type: (InstallRequirement, str, str, str) -> None
        self.ireq = ireq
        self.field = field
        self.f_val = f_val
        self.m_val = m_val

    def __str__(self):
        # type: () -> str
        template = (
            "Requested {} has inconsistent {}: "
            "filename has {!r}, but metadata has {!r}"
        )
        return template.format(self.ireq, self.field, self.f_val, self.m_val)


class InstallationSubprocessError(InstallationError):
    """A subprocess call failed during installation."""
    def __init__(self, returncode, description):
        # type: (int, str) -> None
        self.returncode = returncode
        self.description = description

    def __str__(self):
        # type: () -> str
        return (
            "Command errored out with exit status {}: {} "
            "Check the logs for full command output."
        ).format(self.returncode, self.description)


class HashErrors(InstallationError):
    """Multiple HashError instances rolled into one for reporting"""

    def __init__(self):
        # type: () -> None
        self.errors = []  # type: List[HashError]

    def append(self, error):
        # type: (HashError) -> None
        self.errors.append(error)

    def __str__(self):
        # type: () -> str
        lines = []
        self.errors.sort(key=lambda e: e.order)
        for cls, errors_of_cls in groupby(self.errors, lambda e: e.__class__):
            lines.append(cls.head)
            lines.extend(e.body() for e in errors_of_cls)
        if lines:
            return '\n'.join(lines)
        return ''

    def __nonzero__(self):
        # type: () -> bool
        return bool(self.errors)

    def __bool__(self):
        # type: () -> bool
        return self.__nonzero__()


class HashError(InstallationError):
    """
    A failure to verify a package against known-good hashes

    :cvar order: An int sorting hash exception classes by difficulty of
        recovery (lower being harder), so the user doesn't bother fretting
        about unpinned packages when he has deeper issues, like VCS
        dependencies, to deal with. Also keeps error reports in a
        deterministic order.
    :cvar head: A section heading for display above potentially many
        exceptions of this kind
    :ivar req: The InstallRequirement that triggered this error. This is
        pasted on after the exception is instantiated, because it's not
        typically available earlier.

    """
    req = None  # type: Optional[InstallRequirement]
    head = ''
    order = -1  # type: int

    def body(self):
        # type: () -> str
        """Return a summary of me for display under the heading.

        This default implementation simply prints a description of the
        triggering requirement.

        :param req: The InstallRequirement that provoked this error, with
            its link already populated by the resolver's _populate_link().

        """
        return f'    {self._requirement_name()}'

    def __str__(self):
        # type: () -> str
        return f'{self.head}\n{self.body()}'

    def _requirement_name(self):
        # type: () -> str
        """Return a description of the requirement that triggered me.

        This default implementation returns long description of the req, with
        line numbers

        """
        return str(self.req) if self.req else 'unknown package'


class VcsHashUnsupported(HashError):
    """A hash was provided for a version-control-system-based requirement, but
    we don't have a method for hashing those."""

    order = 0
    head = ("Can't verify hashes for these requirements because we don't "
            "have a way to hash version control repositories:")


class DirectoryUrlHashUnsupported(HashError):
    """A hash was provided for a version-control-system-based requirement, but
    we don't have a method for hashing those."""

    order = 1
    head = ("Can't verify hashes for these file:// requirements because they "
            "point to directories:")


class HashMissing(HashError):
    """A hash was needed for a requirement but is absent."""

    order = 2
    head = ('Hashes are required in --require-hashes mode, but they are '
            'missing from some requirements. Here is a list of those '
            'requirements along with the hashes their downloaded archives '
            'actually had. Add lines like these to your requirements files to '
            'prevent tampering. (If you did not enable --require-hashes '
            'manually, note that it turns on automatically when any package '
            'has a hash.)')

    def __init__(self, gotten_hash):
        # type: (str) -> None
        """
        :param gotten_hash: The hash of the (possibly malicious) archive we
            just downloaded
        """
        self.gotten_hash = gotten_hash

    def body(self):
        # type: () -> str
        # Dodge circular import.
        from pip._internal.utils.hashes import FAVORITE_HASH

        package = None
        if self.req:
            # In the case of URL-based requirements, display the original URL
            # seen in the requirements file rather than the package name,
            # so the output can be directly copied into the requirements file.
            package = (self.req.original_link if self.req.original_link
                       # In case someone feeds something downright stupid
                       # to InstallRequirement's constructor.
                       else getattr(self.req, 'req', None))
        return '    {} --hash={}:{}'.format(package or 'unknown package',
                                            FAVORITE_HASH,
                                            self.gotten_hash)


class HashUnpinned(HashError):
    """A requirement had a hash specified but was not pinned to a specific
    version."""

    order = 3
    head = ('In --require-hashes mode, all requirements must have their '
            'versions pinned with ==. These do not:')


class HashMismatch(HashError):
    """
    Distribution file hash values don't match.

    :ivar package_name: The name of the package that triggered the hash
        mismatch. Feel free to write to this after the exception is raise to
        improve its error message.

    """
    order = 4
    head = ('THESE PACKAGES DO NOT MATCH THE HASHES FROM THE REQUIREMENTS '
            'FILE. If you have updated the package versions, please update '
            'the hashes. Otherwise, examine the package contents carefully; '
            'someone may have tampered with them.')

    def __init__(self, allowed, gots):
        # type: (Dict[str, List[str]], Dict[str, _Hash]) -> None
        """
        :param allowed: A dict of algorithm names pointing to lists of allowed
            hex digests
        :param gots: A dict of algorithm names pointing to hashes we
            actually got from the files under suspicion
        """
        self.allowed = allowed
        self.gots = gots

    def body(self):
        # type: () -> str
        return '    {}:\n{}'.format(self._requirement_name(),
                                    self._hash_comparison())

    def _hash_comparison(self):
        # type: () -> str
        """
        Return a comparison of actual and expected hash values.

        Example::

               Expected sha256 abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde
                            or 123451234512345123451234512345123451234512345
                    Got        bcdefbcdefbcdefbcdefbcdefbcdefbcdefbcdefbcdef

        """
        def hash_then_or(hash_name):
            # type: (str) -> chain[str]
            # For now, all the decent hashes have 6-char names, so we can get
            # away with hard-coding space literals.
            return chain([hash_name], repeat('    or'))

        lines = []  # type: List[str]
        for hash_name, expecteds in self.allowed.items():
            prefix = hash_then_or(hash_name)
            lines.extend(('        Expected {} {}'.format(next(prefix), e))
                         for e in expecteds)
            lines.append('             Got        {}\n'.format(
                         self.gots[hash_name].hexdigest()))
        return '\n'.join(lines)


class UnsupportedPythonVersion(InstallationError):
    """Unsupported python version according to Requires-Python package
    metadata."""


class ConfigurationFileCouldNotBeLoaded(ConfigurationError):
    """When there are errors while loading a configuration file
    """

    def __init__(self, reason="could not be loaded", fname=None, error=None):
        # type: (str, Optional[str], Optional[configparser.Error]) -> None
        super().__init__(error)
        self.reason = reason
        self.fname = fname
        self.error = error

    def __str__(self):
        # type: () -> str
        if self.fname is not None:
            message_part = f" in {self.fname}."
        else:
            assert self.error is not None
            message_part = f".\n{self.error}\n"
        return f"Configuration file {self.reason}{message_part}"
