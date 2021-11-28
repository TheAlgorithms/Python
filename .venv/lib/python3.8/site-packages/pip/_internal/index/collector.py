"""
The main purpose of this module is to expose LinkCollector.collect_sources().
"""

import cgi
import collections
import functools
import html
import itertools
import logging
import os
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree
from optparse import Values
from typing import (
    Callable,
    Iterable,
    List,
    MutableMapping,
    NamedTuple,
    Optional,
    Sequence,
    Union,
)

from pip._vendor import html5lib, requests
from pip._vendor.requests import Response
from pip._vendor.requests.exceptions import RetryError, SSLError

from pip._internal.exceptions import NetworkConnectionError
from pip._internal.models.link import Link
from pip._internal.models.search_scope import SearchScope
from pip._internal.network.session import PipSession
from pip._internal.network.utils import raise_for_status
from pip._internal.utils.filetypes import is_archive_file
from pip._internal.utils.misc import pairwise, redact_auth_from_url
from pip._internal.vcs import vcs

from .sources import CandidatesFromPage, LinkSource, build_source

logger = logging.getLogger(__name__)

HTMLElement = xml.etree.ElementTree.Element
ResponseHeaders = MutableMapping[str, str]


def _match_vcs_scheme(url):
    # type: (str) -> Optional[str]
    """Look for VCS schemes in the URL.

    Returns the matched VCS scheme, or None if there's no match.
    """
    for scheme in vcs.schemes:
        if url.lower().startswith(scheme) and url[len(scheme)] in '+:':
            return scheme
    return None


class _NotHTML(Exception):
    def __init__(self, content_type, request_desc):
        # type: (str, str) -> None
        super().__init__(content_type, request_desc)
        self.content_type = content_type
        self.request_desc = request_desc


def _ensure_html_header(response):
    # type: (Response) -> None
    """Check the Content-Type header to ensure the response contains HTML.

    Raises `_NotHTML` if the content type is not text/html.
    """
    content_type = response.headers.get("Content-Type", "")
    if not content_type.lower().startswith("text/html"):
        raise _NotHTML(content_type, response.request.method)


class _NotHTTP(Exception):
    pass


def _ensure_html_response(url, session):
    # type: (str, PipSession) -> None
    """Send a HEAD request to the URL, and ensure the response contains HTML.

    Raises `_NotHTTP` if the URL is not available for a HEAD request, or
    `_NotHTML` if the content type is not text/html.
    """
    scheme, netloc, path, query, fragment = urllib.parse.urlsplit(url)
    if scheme not in {'http', 'https'}:
        raise _NotHTTP()

    resp = session.head(url, allow_redirects=True)
    raise_for_status(resp)

    _ensure_html_header(resp)


def _get_html_response(url, session):
    # type: (str, PipSession) -> Response
    """Access an HTML page with GET, and return the response.

    This consists of three parts:

    1. If the URL looks suspiciously like an archive, send a HEAD first to
       check the Content-Type is HTML, to avoid downloading a large file.
       Raise `_NotHTTP` if the content type cannot be determined, or
       `_NotHTML` if it is not HTML.
    2. Actually perform the request. Raise HTTP exceptions on network failures.
    3. Check the Content-Type header to make sure we got HTML, and raise
       `_NotHTML` otherwise.
    """
    if is_archive_file(Link(url).filename):
        _ensure_html_response(url, session=session)

    logger.debug('Getting page %s', redact_auth_from_url(url))

    resp = session.get(
        url,
        headers={
            "Accept": "text/html",
            # We don't want to blindly returned cached data for
            # /simple/, because authors generally expecting that
            # twine upload && pip install will function, but if
            # they've done a pip install in the last ~10 minutes
            # it won't. Thus by setting this to zero we will not
            # blindly use any cached data, however the benefit of
            # using max-age=0 instead of no-cache, is that we will
            # still support conditional requests, so we will still
            # minimize traffic sent in cases where the page hasn't
            # changed at all, we will just always incur the round
            # trip for the conditional GET now instead of only
            # once per 10 minutes.
            # For more information, please see pypa/pip#5670.
            "Cache-Control": "max-age=0",
        },
    )
    raise_for_status(resp)

    # The check for archives above only works if the url ends with
    # something that looks like an archive. However that is not a
    # requirement of an url. Unless we issue a HEAD request on every
    # url we cannot know ahead of time for sure if something is HTML
    # or not. However we can check after we've downloaded it.
    _ensure_html_header(resp)

    return resp


def _get_encoding_from_headers(headers):
    # type: (ResponseHeaders) -> Optional[str]
    """Determine if we have any encoding information in our headers.
    """
    if headers and "Content-Type" in headers:
        content_type, params = cgi.parse_header(headers["Content-Type"])
        if "charset" in params:
            return params['charset']
    return None


def _determine_base_url(document, page_url):
    # type: (HTMLElement, str) -> str
    """Determine the HTML document's base URL.

    This looks for a ``<base>`` tag in the HTML document. If present, its href
    attribute denotes the base URL of anchor tags in the document. If there is
    no such tag (or if it does not have a valid href attribute), the HTML
    file's URL is used as the base URL.

    :param document: An HTML document representation. The current
        implementation expects the result of ``html5lib.parse()``.
    :param page_url: The URL of the HTML document.
    """
    for base in document.findall(".//base"):
        href = base.get("href")
        if href is not None:
            return href
    return page_url


def _clean_url_path_part(part):
    # type: (str) -> str
    """
    Clean a "part" of a URL path (i.e. after splitting on "@" characters).
    """
    # We unquote prior to quoting to make sure nothing is double quoted.
    return urllib.parse.quote(urllib.parse.unquote(part))


def _clean_file_url_path(part):
    # type: (str) -> str
    """
    Clean the first part of a URL path that corresponds to a local
    filesystem path (i.e. the first part after splitting on "@" characters).
    """
    # We unquote prior to quoting to make sure nothing is double quoted.
    # Also, on Windows the path part might contain a drive letter which
    # should not be quoted. On Linux where drive letters do not
    # exist, the colon should be quoted. We rely on urllib.request
    # to do the right thing here.
    return urllib.request.pathname2url(urllib.request.url2pathname(part))


# percent-encoded:                   /
_reserved_chars_re = re.compile('(@|%2F)', re.IGNORECASE)


def _clean_url_path(path, is_local_path):
    # type: (str, bool) -> str
    """
    Clean the path portion of a URL.
    """
    if is_local_path:
        clean_func = _clean_file_url_path
    else:
        clean_func = _clean_url_path_part

    # Split on the reserved characters prior to cleaning so that
    # revision strings in VCS URLs are properly preserved.
    parts = _reserved_chars_re.split(path)

    cleaned_parts = []
    for to_clean, reserved in pairwise(itertools.chain(parts, [''])):
        cleaned_parts.append(clean_func(to_clean))
        # Normalize %xx escapes (e.g. %2f -> %2F)
        cleaned_parts.append(reserved.upper())

    return ''.join(cleaned_parts)


def _clean_link(url):
    # type: (str) -> str
    """
    Make sure a link is fully quoted.
    For example, if ' ' occurs in the URL, it will be replaced with "%20",
    and without double-quoting other characters.
    """
    # Split the URL into parts according to the general structure
    # `scheme://netloc/path;parameters?query#fragment`.
    result = urllib.parse.urlparse(url)
    # If the netloc is empty, then the URL refers to a local filesystem path.
    is_local_path = not result.netloc
    path = _clean_url_path(result.path, is_local_path=is_local_path)
    return urllib.parse.urlunparse(result._replace(path=path))


def _create_link_from_element(
    anchor,    # type: HTMLElement
    page_url,  # type: str
    base_url,  # type: str
):
    # type: (...) -> Optional[Link]
    """
    Convert an anchor element in a simple repository page to a Link.
    """
    href = anchor.get("href")
    if not href:
        return None

    url = _clean_link(urllib.parse.urljoin(base_url, href))
    pyrequire = anchor.get('data-requires-python')
    pyrequire = html.unescape(pyrequire) if pyrequire else None

    yanked_reason = anchor.get('data-yanked')
    if yanked_reason:
        yanked_reason = html.unescape(yanked_reason)

    link = Link(
        url,
        comes_from=page_url,
        requires_python=pyrequire,
        yanked_reason=yanked_reason,
    )

    return link


class CacheablePageContent:
    def __init__(self, page):
        # type: (HTMLPage) -> None
        assert page.cache_link_parsing
        self.page = page

    def __eq__(self, other):
        # type: (object) -> bool
        return (isinstance(other, type(self)) and
                self.page.url == other.page.url)

    def __hash__(self):
        # type: () -> int
        return hash(self.page.url)


def with_cached_html_pages(
    fn,    # type: Callable[[HTMLPage], Iterable[Link]]
):
    # type: (...) -> Callable[[HTMLPage], List[Link]]
    """
    Given a function that parses an Iterable[Link] from an HTMLPage, cache the
    function's result (keyed by CacheablePageContent), unless the HTMLPage
    `page` has `page.cache_link_parsing == False`.
    """

    @functools.lru_cache(maxsize=None)
    def wrapper(cacheable_page):
        # type: (CacheablePageContent) -> List[Link]
        return list(fn(cacheable_page.page))

    @functools.wraps(fn)
    def wrapper_wrapper(page):
        # type: (HTMLPage) -> List[Link]
        if page.cache_link_parsing:
            return wrapper(CacheablePageContent(page))
        return list(fn(page))

    return wrapper_wrapper


@with_cached_html_pages
def parse_links(page):
    # type: (HTMLPage) -> Iterable[Link]
    """
    Parse an HTML document, and yield its anchor elements as Link objects.
    """
    document = html5lib.parse(
        page.content,
        transport_encoding=page.encoding,
        namespaceHTMLElements=False,
    )

    url = page.url
    base_url = _determine_base_url(document, url)
    for anchor in document.findall(".//a"):
        link = _create_link_from_element(
            anchor,
            page_url=url,
            base_url=base_url,
        )
        if link is None:
            continue
        yield link


class HTMLPage:
    """Represents one page, along with its URL"""

    def __init__(
        self,
        content,                  # type: bytes
        encoding,                 # type: Optional[str]
        url,                      # type: str
        cache_link_parsing=True,  # type: bool
    ):
        # type: (...) -> None
        """
        :param encoding: the encoding to decode the given content.
        :param url: the URL from which the HTML was downloaded.
        :param cache_link_parsing: whether links parsed from this page's url
                                   should be cached. PyPI index urls should
                                   have this set to False, for example.
        """
        self.content = content
        self.encoding = encoding
        self.url = url
        self.cache_link_parsing = cache_link_parsing

    def __str__(self):
        # type: () -> str
        return redact_auth_from_url(self.url)


def _handle_get_page_fail(
    link,  # type: Link
    reason,  # type: Union[str, Exception]
    meth=None  # type: Optional[Callable[..., None]]
):
    # type: (...) -> None
    if meth is None:
        meth = logger.debug
    meth("Could not fetch URL %s: %s - skipping", link, reason)


def _make_html_page(response, cache_link_parsing=True):
    # type: (Response, bool) -> HTMLPage
    encoding = _get_encoding_from_headers(response.headers)
    return HTMLPage(
        response.content,
        encoding=encoding,
        url=response.url,
        cache_link_parsing=cache_link_parsing)


def _get_html_page(link, session=None):
    # type: (Link, Optional[PipSession]) -> Optional[HTMLPage]
    if session is None:
        raise TypeError(
            "_get_html_page() missing 1 required keyword argument: 'session'"
        )

    url = link.url.split('#', 1)[0]

    # Check for VCS schemes that do not support lookup as web pages.
    vcs_scheme = _match_vcs_scheme(url)
    if vcs_scheme:
        logger.warning('Cannot look at %s URL %s because it does not support '
                       'lookup as web pages.', vcs_scheme, link)
        return None

    # Tack index.html onto file:// URLs that point to directories
    scheme, _, path, _, _, _ = urllib.parse.urlparse(url)
    if (scheme == 'file' and os.path.isdir(urllib.request.url2pathname(path))):
        # add trailing slash if not present so urljoin doesn't trim
        # final segment
        if not url.endswith('/'):
            url += '/'
        url = urllib.parse.urljoin(url, 'index.html')
        logger.debug(' file: URL is directory, getting %s', url)

    try:
        resp = _get_html_response(url, session=session)
    except _NotHTTP:
        logger.warning(
            'Skipping page %s because it looks like an archive, and cannot '
            'be checked by a HTTP HEAD request.', link,
        )
    except _NotHTML as exc:
        logger.warning(
            'Skipping page %s because the %s request got Content-Type: %s.'
            'The only supported Content-Type is text/html',
            link, exc.request_desc, exc.content_type,
        )
    except NetworkConnectionError as exc:
        _handle_get_page_fail(link, exc)
    except RetryError as exc:
        _handle_get_page_fail(link, exc)
    except SSLError as exc:
        reason = "There was a problem confirming the ssl certificate: "
        reason += str(exc)
        _handle_get_page_fail(link, reason, meth=logger.info)
    except requests.ConnectionError as exc:
        _handle_get_page_fail(link, f"connection error: {exc}")
    except requests.Timeout:
        _handle_get_page_fail(link, "timed out")
    else:
        return _make_html_page(resp,
                               cache_link_parsing=link.cache_link_parsing)
    return None


class CollectedSources(NamedTuple):
    find_links: Sequence[Optional[LinkSource]]
    index_urls: Sequence[Optional[LinkSource]]


class LinkCollector:

    """
    Responsible for collecting Link objects from all configured locations,
    making network requests as needed.

    The class's main method is its collect_sources() method.
    """

    def __init__(
        self,
        session,       # type: PipSession
        search_scope,  # type: SearchScope
    ):
        # type: (...) -> None
        self.search_scope = search_scope
        self.session = session

    @classmethod
    def create(cls, session, options, suppress_no_index=False):
        # type: (PipSession, Values, bool) -> LinkCollector
        """
        :param session: The Session to use to make requests.
        :param suppress_no_index: Whether to ignore the --no-index option
            when constructing the SearchScope object.
        """
        index_urls = [options.index_url] + options.extra_index_urls
        if options.no_index and not suppress_no_index:
            logger.debug(
                'Ignoring indexes: %s',
                ','.join(redact_auth_from_url(url) for url in index_urls),
            )
            index_urls = []

        # Make sure find_links is a list before passing to create().
        find_links = options.find_links or []

        search_scope = SearchScope.create(
            find_links=find_links, index_urls=index_urls,
        )
        link_collector = LinkCollector(
            session=session, search_scope=search_scope,
        )
        return link_collector

    @property
    def find_links(self):
        # type: () -> List[str]
        return self.search_scope.find_links

    def fetch_page(self, location):
        # type: (Link) -> Optional[HTMLPage]
        """
        Fetch an HTML page containing package links.
        """
        return _get_html_page(location, session=self.session)

    def collect_sources(
        self,
        project_name: str,
        candidates_from_page: CandidatesFromPage,
    ) -> CollectedSources:
        # The OrderedDict calls deduplicate sources by URL.
        index_url_sources = collections.OrderedDict(
            build_source(
                loc,
                candidates_from_page=candidates_from_page,
                page_validator=self.session.is_secure_origin,
                expand_dir=False,
                cache_link_parsing=False,
            )
            for loc in self.search_scope.get_index_urls_locations(project_name)
        ).values()
        find_links_sources = collections.OrderedDict(
            build_source(
                loc,
                candidates_from_page=candidates_from_page,
                page_validator=self.session.is_secure_origin,
                expand_dir=True,
                cache_link_parsing=True,
            )
            for loc in self.find_links
        ).values()

        if logger.isEnabledFor(logging.DEBUG):
            lines = [
                f"* {s.link}"
                for s in itertools.chain(find_links_sources, index_url_sources)
                if s is not None and s.link is not None
            ]
            lines = [
                f"{len(lines)} location(s) to search "
                f"for versions of {project_name}:"
            ] + lines
            logger.debug("\n".join(lines))

        return CollectedSources(
            find_links=list(find_links_sources),
            index_urls=list(index_url_sources),
        )
