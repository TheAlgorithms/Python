"""Cache Management
"""

import hashlib
import json
import logging
import os
from typing import Any, Dict, List, Optional, Set

from pip._vendor.packaging.tags import Tag, interpreter_name, interpreter_version
from pip._vendor.packaging.utils import canonicalize_name

from pip._internal.exceptions import InvalidWheelFilename
from pip._internal.models.format_control import FormatControl
from pip._internal.models.link import Link
from pip._internal.models.wheel import Wheel
from pip._internal.utils.temp_dir import TempDirectory, tempdir_kinds
from pip._internal.utils.urls import path_to_url

logger = logging.getLogger(__name__)


def _hash_dict(d):
    # type: (Dict[str, str]) -> str
    """Return a stable sha224 of a dictionary."""
    s = json.dumps(d, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha224(s.encode("ascii")).hexdigest()


class Cache:
    """An abstract class - provides cache directories for data from links


        :param cache_dir: The root of the cache.
        :param format_control: An object of FormatControl class to limit
            binaries being read from the cache.
        :param allowed_formats: which formats of files the cache should store.
            ('binary' and 'source' are the only allowed values)
    """

    def __init__(self, cache_dir, format_control, allowed_formats):
        # type: (str, FormatControl, Set[str]) -> None
        super().__init__()
        assert not cache_dir or os.path.isabs(cache_dir)
        self.cache_dir = cache_dir or None
        self.format_control = format_control
        self.allowed_formats = allowed_formats

        _valid_formats = {"source", "binary"}
        assert self.allowed_formats.union(_valid_formats) == _valid_formats

    def _get_cache_path_parts(self, link):
        # type: (Link) -> List[str]
        """Get parts of part that must be os.path.joined with cache_dir
        """

        # We want to generate an url to use as our cache key, we don't want to
        # just re-use the URL because it might have other items in the fragment
        # and we don't care about those.
        key_parts = {"url": link.url_without_fragment}
        if link.hash_name is not None and link.hash is not None:
            key_parts[link.hash_name] = link.hash
        if link.subdirectory_fragment:
            key_parts["subdirectory"] = link.subdirectory_fragment

        # Include interpreter name, major and minor version in cache key
        # to cope with ill-behaved sdists that build a different wheel
        # depending on the python version their setup.py is being run on,
        # and don't encode the difference in compatibility tags.
        # https://github.com/pypa/pip/issues/7296
        key_parts["interpreter_name"] = interpreter_name()
        key_parts["interpreter_version"] = interpreter_version()

        # Encode our key url with sha224, we'll use this because it has similar
        # security properties to sha256, but with a shorter total output (and
        # thus less secure). However the differences don't make a lot of
        # difference for our use case here.
        hashed = _hash_dict(key_parts)

        # We want to nest the directories some to prevent having a ton of top
        # level directories where we might run out of sub directories on some
        # FS.
        parts = [hashed[:2], hashed[2:4], hashed[4:6], hashed[6:]]

        return parts

    def _get_candidates(self, link, canonical_package_name):
        # type: (Link, str) -> List[Any]
        can_not_cache = (
            not self.cache_dir or
            not canonical_package_name or
            not link
        )
        if can_not_cache:
            return []

        formats = self.format_control.get_allowed_formats(
            canonical_package_name
        )
        if not self.allowed_formats.intersection(formats):
            return []

        candidates = []
        path = self.get_path_for_link(link)
        if os.path.isdir(path):
            for candidate in os.listdir(path):
                candidates.append((candidate, path))
        return candidates

    def get_path_for_link(self, link):
        # type: (Link) -> str
        """Return a directory to store cached items in for link.
        """
        raise NotImplementedError()

    def get(
        self,
        link,            # type: Link
        package_name,    # type: Optional[str]
        supported_tags,  # type: List[Tag]
    ):
        # type: (...) -> Link
        """Returns a link to a cached item if it exists, otherwise returns the
        passed link.
        """
        raise NotImplementedError()


class SimpleWheelCache(Cache):
    """A cache of wheels for future installs.
    """

    def __init__(self, cache_dir, format_control):
        # type: (str, FormatControl) -> None
        super().__init__(cache_dir, format_control, {"binary"})

    def get_path_for_link(self, link):
        # type: (Link) -> str
        """Return a directory to store cached wheels for link

        Because there are M wheels for any one sdist, we provide a directory
        to cache them in, and then consult that directory when looking up
        cache hits.

        We only insert things into the cache if they have plausible version
        numbers, so that we don't contaminate the cache with things that were
        not unique. E.g. ./package might have dozens of installs done for it
        and build a version of 0.0...and if we built and cached a wheel, we'd
        end up using the same wheel even if the source has been edited.

        :param link: The link of the sdist for which this will cache wheels.
        """
        parts = self._get_cache_path_parts(link)
        assert self.cache_dir
        # Store wheels within the root cache_dir
        return os.path.join(self.cache_dir, "wheels", *parts)

    def get(
        self,
        link,            # type: Link
        package_name,    # type: Optional[str]
        supported_tags,  # type: List[Tag]
    ):
        # type: (...) -> Link
        candidates = []

        if not package_name:
            return link

        canonical_package_name = canonicalize_name(package_name)
        for wheel_name, wheel_dir in self._get_candidates(
            link, canonical_package_name
        ):
            try:
                wheel = Wheel(wheel_name)
            except InvalidWheelFilename:
                continue
            if canonicalize_name(wheel.name) != canonical_package_name:
                logger.debug(
                    "Ignoring cached wheel %s for %s as it "
                    "does not match the expected distribution name %s.",
                    wheel_name, link, package_name,
                )
                continue
            if not wheel.supported(supported_tags):
                # Built for a different python/arch/etc
                continue
            candidates.append(
                (
                    wheel.support_index_min(supported_tags),
                    wheel_name,
                    wheel_dir,
                )
            )

        if not candidates:
            return link

        _, wheel_name, wheel_dir = min(candidates)
        return Link(path_to_url(os.path.join(wheel_dir, wheel_name)))


class EphemWheelCache(SimpleWheelCache):
    """A SimpleWheelCache that creates it's own temporary cache directory
    """

    def __init__(self, format_control):
        # type: (FormatControl) -> None
        self._temp_dir = TempDirectory(
            kind=tempdir_kinds.EPHEM_WHEEL_CACHE,
            globally_managed=True,
        )

        super().__init__(self._temp_dir.path, format_control)


class CacheEntry:
    def __init__(
        self,
        link,  # type: Link
        persistent,  # type: bool
    ):
        self.link = link
        self.persistent = persistent


class WheelCache(Cache):
    """Wraps EphemWheelCache and SimpleWheelCache into a single Cache

    This Cache allows for gracefully degradation, using the ephem wheel cache
    when a certain link is not found in the simple wheel cache first.
    """

    def __init__(self, cache_dir, format_control):
        # type: (str, FormatControl) -> None
        super().__init__(cache_dir, format_control, {'binary'})
        self._wheel_cache = SimpleWheelCache(cache_dir, format_control)
        self._ephem_cache = EphemWheelCache(format_control)

    def get_path_for_link(self, link):
        # type: (Link) -> str
        return self._wheel_cache.get_path_for_link(link)

    def get_ephem_path_for_link(self, link):
        # type: (Link) -> str
        return self._ephem_cache.get_path_for_link(link)

    def get(
        self,
        link,            # type: Link
        package_name,    # type: Optional[str]
        supported_tags,  # type: List[Tag]
    ):
        # type: (...) -> Link
        cache_entry = self.get_cache_entry(link, package_name, supported_tags)
        if cache_entry is None:
            return link
        return cache_entry.link

    def get_cache_entry(
        self,
        link,            # type: Link
        package_name,    # type: Optional[str]
        supported_tags,  # type: List[Tag]
    ):
        # type: (...) -> Optional[CacheEntry]
        """Returns a CacheEntry with a link to a cached item if it exists or
        None. The cache entry indicates if the item was found in the persistent
        or ephemeral cache.
        """
        retval = self._wheel_cache.get(
            link=link,
            package_name=package_name,
            supported_tags=supported_tags,
        )
        if retval is not link:
            return CacheEntry(retval, persistent=True)

        retval = self._ephem_cache.get(
            link=link,
            package_name=package_name,
            supported_tags=supported_tags,
        )
        if retval is not link:
            return CacheEntry(retval, persistent=False)

        return None
