import os
import posixpath
import re
import urllib.parse
from typing import TYPE_CHECKING, Optional, Tuple, Union

from pip._internal.utils.filetypes import WHEEL_EXTENSION
from pip._internal.utils.hashes import Hashes
from pip._internal.utils.misc import (
    redact_auth_from_url,
    split_auth_from_netloc,
    splitext,
)
from pip._internal.utils.models import KeyBasedCompareMixin
from pip._internal.utils.urls import path_to_url, url_to_path

if TYPE_CHECKING:
    from pip._internal.index.collector import HTMLPage


class Link(KeyBasedCompareMixin):
    """Represents a parsed link from a Package Index's simple URL
    """

    __slots__ = [
        "_parsed_url",
        "_url",
        "comes_from",
        "requires_python",
        "yanked_reason",
        "cache_link_parsing",
    ]

    def __init__(
        self,
        url,                   # type: str
        comes_from=None,       # type: Optional[Union[str, HTMLPage]]
        requires_python=None,  # type: Optional[str]
        yanked_reason=None,    # type: Optional[str]
        cache_link_parsing=True,  # type: bool
    ):
        # type: (...) -> None
        """
        :param url: url of the resource pointed to (href of the link)
        :param comes_from: instance of HTMLPage where the link was found,
            or string.
        :param requires_python: String containing the `Requires-Python`
            metadata field, specified in PEP 345. This may be specified by
            a data-requires-python attribute in the HTML link tag, as
            described in PEP 503.
        :param yanked_reason: the reason the file has been yanked, if the
            file has been yanked, or None if the file hasn't been yanked.
            This is the value of the "data-yanked" attribute, if present, in
            a simple repository HTML link. If the file has been yanked but
            no reason was provided, this should be the empty string. See
            PEP 592 for more information and the specification.
        :param cache_link_parsing: A flag that is used elsewhere to determine
                                   whether resources retrieved from this link
                                   should be cached. PyPI index urls should
                                   generally have this set to False, for
                                   example.
        """

        # url can be a UNC windows share
        if url.startswith('\\\\'):
            url = path_to_url(url)

        self._parsed_url = urllib.parse.urlsplit(url)
        # Store the url as a private attribute to prevent accidentally
        # trying to set a new value.
        self._url = url

        self.comes_from = comes_from
        self.requires_python = requires_python if requires_python else None
        self.yanked_reason = yanked_reason

        super().__init__(key=url, defining_class=Link)

        self.cache_link_parsing = cache_link_parsing

    def __str__(self):
        # type: () -> str
        if self.requires_python:
            rp = f' (requires-python:{self.requires_python})'
        else:
            rp = ''
        if self.comes_from:
            return '{} (from {}){}'.format(
                redact_auth_from_url(self._url), self.comes_from, rp)
        else:
            return redact_auth_from_url(str(self._url))

    def __repr__(self):
        # type: () -> str
        return f'<Link {self}>'

    @property
    def url(self):
        # type: () -> str
        return self._url

    @property
    def filename(self):
        # type: () -> str
        path = self.path.rstrip('/')
        name = posixpath.basename(path)
        if not name:
            # Make sure we don't leak auth information if the netloc
            # includes a username and password.
            netloc, user_pass = split_auth_from_netloc(self.netloc)
            return netloc

        name = urllib.parse.unquote(name)
        assert name, f'URL {self._url!r} produced no filename'
        return name

    @property
    def file_path(self):
        # type: () -> str
        return url_to_path(self.url)

    @property
    def scheme(self):
        # type: () -> str
        return self._parsed_url.scheme

    @property
    def netloc(self):
        # type: () -> str
        """
        This can contain auth information.
        """
        return self._parsed_url.netloc

    @property
    def path(self):
        # type: () -> str
        return urllib.parse.unquote(self._parsed_url.path)

    def splitext(self):
        # type: () -> Tuple[str, str]
        return splitext(posixpath.basename(self.path.rstrip('/')))

    @property
    def ext(self):
        # type: () -> str
        return self.splitext()[1]

    @property
    def url_without_fragment(self):
        # type: () -> str
        scheme, netloc, path, query, fragment = self._parsed_url
        return urllib.parse.urlunsplit((scheme, netloc, path, query, None))

    _egg_fragment_re = re.compile(r'[#&]egg=([^&]*)')

    @property
    def egg_fragment(self):
        # type: () -> Optional[str]
        match = self._egg_fragment_re.search(self._url)
        if not match:
            return None
        return match.group(1)

    _subdirectory_fragment_re = re.compile(r'[#&]subdirectory=([^&]*)')

    @property
    def subdirectory_fragment(self):
        # type: () -> Optional[str]
        match = self._subdirectory_fragment_re.search(self._url)
        if not match:
            return None
        return match.group(1)

    _hash_re = re.compile(
        r'(sha1|sha224|sha384|sha256|sha512|md5)=([a-f0-9]+)'
    )

    @property
    def hash(self):
        # type: () -> Optional[str]
        match = self._hash_re.search(self._url)
        if match:
            return match.group(2)
        return None

    @property
    def hash_name(self):
        # type: () -> Optional[str]
        match = self._hash_re.search(self._url)
        if match:
            return match.group(1)
        return None

    @property
    def show_url(self):
        # type: () -> str
        return posixpath.basename(self._url.split('#', 1)[0].split('?', 1)[0])

    @property
    def is_file(self):
        # type: () -> bool
        return self.scheme == 'file'

    def is_existing_dir(self):
        # type: () -> bool
        return self.is_file and os.path.isdir(self.file_path)

    @property
    def is_wheel(self):
        # type: () -> bool
        return self.ext == WHEEL_EXTENSION

    @property
    def is_vcs(self):
        # type: () -> bool
        from pip._internal.vcs import vcs

        return self.scheme in vcs.all_schemes

    @property
    def is_yanked(self):
        # type: () -> bool
        return self.yanked_reason is not None

    @property
    def has_hash(self):
        # type: () -> bool
        return self.hash_name is not None

    def is_hash_allowed(self, hashes):
        # type: (Optional[Hashes]) -> bool
        """
        Return True if the link has a hash and it is allowed.
        """
        if hashes is None or not self.has_hash:
            return False
        # Assert non-None so mypy knows self.hash_name and self.hash are str.
        assert self.hash_name is not None
        assert self.hash is not None

        return hashes.is_hash_allowed(self.hash_name, hex_digest=self.hash)


# TODO: Relax this comparison logic to ignore, for example, fragments.
def links_equivalent(link1, link2):
    # type: (Link, Link) -> bool
    return link1 == link2
