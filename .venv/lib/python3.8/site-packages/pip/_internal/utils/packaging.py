import logging
from email.message import Message
from email.parser import FeedParser
from typing import Optional, Tuple

from pip._vendor import pkg_resources
from pip._vendor.packaging import specifiers, version
from pip._vendor.pkg_resources import Distribution

from pip._internal.exceptions import NoneMetadataError
from pip._internal.utils.misc import display_path

logger = logging.getLogger(__name__)


def check_requires_python(requires_python, version_info):
    # type: (Optional[str], Tuple[int, ...]) -> bool
    """
    Check if the given Python version matches a "Requires-Python" specifier.

    :param version_info: A 3-tuple of ints representing a Python
        major-minor-micro version to check (e.g. `sys.version_info[:3]`).

    :return: `True` if the given Python version satisfies the requirement.
        Otherwise, return `False`.

    :raises InvalidSpecifier: If `requires_python` has an invalid format.
    """
    if requires_python is None:
        # The package provides no information
        return True
    requires_python_specifier = specifiers.SpecifierSet(requires_python)

    python_version = version.parse(".".join(map(str, version_info)))
    return python_version in requires_python_specifier


def get_metadata(dist):
    # type: (Distribution) -> Message
    """
    :raises NoneMetadataError: if the distribution reports `has_metadata()`
        True but `get_metadata()` returns None.
    """
    metadata_name = "METADATA"
    if isinstance(dist, pkg_resources.DistInfoDistribution) and dist.has_metadata(
        metadata_name
    ):
        metadata = dist.get_metadata(metadata_name)
    elif dist.has_metadata("PKG-INFO"):
        metadata_name = "PKG-INFO"
        metadata = dist.get_metadata(metadata_name)
    else:
        logger.warning("No metadata found in %s", display_path(dist.location))
        metadata = ""

    if metadata is None:
        raise NoneMetadataError(dist, metadata_name)

    feed_parser = FeedParser()
    # The following line errors out if with a "NoneType" TypeError if
    # passed metadata=None.
    feed_parser.feed(metadata)
    return feed_parser.close()


def get_requires_python(dist):
    # type: (pkg_resources.Distribution) -> Optional[str]
    """
    Return the "Requires-Python" metadata for a distribution, or None
    if not present.
    """
    pkg_info_dict = get_metadata(dist)
    requires_python = pkg_info_dict.get("Requires-Python")

    if requires_python is not None:
        # Convert to a str to satisfy the type checker, since requires_python
        # can be a Header object.
        requires_python = str(requires_python)

    return requires_python


def get_installer(dist):
    # type: (Distribution) -> str
    if dist.has_metadata("INSTALLER"):
        for line in dist.get_metadata_lines("INSTALLER"):
            if line.strip():
                return line.strip()
    return ""
