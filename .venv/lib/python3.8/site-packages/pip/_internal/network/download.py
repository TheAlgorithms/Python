"""Download files with progress indicators.
"""
import cgi
import logging
import mimetypes
import os
from typing import Iterable, Optional, Tuple

from pip._vendor.requests.models import CONTENT_CHUNK_SIZE, Response

from pip._internal.cli.progress_bars import DownloadProgressProvider
from pip._internal.exceptions import NetworkConnectionError
from pip._internal.models.index import PyPI
from pip._internal.models.link import Link
from pip._internal.network.cache import is_from_cache
from pip._internal.network.session import PipSession
from pip._internal.network.utils import HEADERS, raise_for_status, response_chunks
from pip._internal.utils.misc import format_size, redact_auth_from_url, splitext

logger = logging.getLogger(__name__)


def _get_http_response_size(resp):
    # type: (Response) -> Optional[int]
    try:
        return int(resp.headers['content-length'])
    except (ValueError, KeyError, TypeError):
        return None


def _prepare_download(
    resp,  # type: Response
    link,  # type: Link
    progress_bar  # type: str
):
    # type: (...) -> Iterable[bytes]
    total_length = _get_http_response_size(resp)

    if link.netloc == PyPI.file_storage_domain:
        url = link.show_url
    else:
        url = link.url_without_fragment

    logged_url = redact_auth_from_url(url)

    if total_length:
        logged_url = '{} ({})'.format(logged_url, format_size(total_length))

    if is_from_cache(resp):
        logger.info("Using cached %s", logged_url)
    else:
        logger.info("Downloading %s", logged_url)

    if logger.getEffectiveLevel() > logging.INFO:
        show_progress = False
    elif is_from_cache(resp):
        show_progress = False
    elif not total_length:
        show_progress = True
    elif total_length > (40 * 1000):
        show_progress = True
    else:
        show_progress = False

    chunks = response_chunks(resp, CONTENT_CHUNK_SIZE)

    if not show_progress:
        return chunks

    return DownloadProgressProvider(
        progress_bar, max=total_length
    )(chunks)


def sanitize_content_filename(filename):
    # type: (str) -> str
    """
    Sanitize the "filename" value from a Content-Disposition header.
    """
    return os.path.basename(filename)


def parse_content_disposition(content_disposition, default_filename):
    # type: (str, str) -> str
    """
    Parse the "filename" value from a Content-Disposition header, and
    return the default filename if the result is empty.
    """
    _type, params = cgi.parse_header(content_disposition)
    filename = params.get('filename')
    if filename:
        # We need to sanitize the filename to prevent directory traversal
        # in case the filename contains ".." path parts.
        filename = sanitize_content_filename(filename)
    return filename or default_filename


def _get_http_response_filename(resp, link):
    # type: (Response, Link) -> str
    """Get an ideal filename from the given HTTP response, falling back to
    the link filename if not provided.
    """
    filename = link.filename  # fallback
    # Have a look at the Content-Disposition header for a better guess
    content_disposition = resp.headers.get('content-disposition')
    if content_disposition:
        filename = parse_content_disposition(content_disposition, filename)
    ext = splitext(filename)[1]  # type: Optional[str]
    if not ext:
        ext = mimetypes.guess_extension(
            resp.headers.get('content-type', '')
        )
        if ext:
            filename += ext
    if not ext and link.url != resp.url:
        ext = os.path.splitext(resp.url)[1]
        if ext:
            filename += ext
    return filename


def _http_get_download(session, link):
    # type: (PipSession, Link) -> Response
    target_url = link.url.split('#', 1)[0]
    resp = session.get(target_url, headers=HEADERS, stream=True)
    raise_for_status(resp)
    return resp


class Downloader:
    def __init__(
        self,
        session,  # type: PipSession
        progress_bar,  # type: str
    ):
        # type: (...) -> None
        self._session = session
        self._progress_bar = progress_bar

    def __call__(self, link, location):
        # type: (Link, str) -> Tuple[str, str]
        """Download the file given by link into location."""
        try:
            resp = _http_get_download(self._session, link)
        except NetworkConnectionError as e:
            assert e.response is not None
            logger.critical(
                "HTTP error %s while getting %s", e.response.status_code, link
            )
            raise

        filename = _get_http_response_filename(resp, link)
        filepath = os.path.join(location, filename)

        chunks = _prepare_download(resp, link, self._progress_bar)
        with open(filepath, 'wb') as content_file:
            for chunk in chunks:
                content_file.write(chunk)
        content_type = resp.headers.get('Content-Type', '')
        return filepath, content_type


class BatchDownloader:

    def __init__(
        self,
        session,  # type: PipSession
        progress_bar,  # type: str
    ):
        # type: (...) -> None
        self._session = session
        self._progress_bar = progress_bar

    def __call__(self, links, location):
        # type: (Iterable[Link], str) -> Iterable[Tuple[Link, Tuple[str, str]]]
        """Download the files given by links into location."""
        for link in links:
            try:
                resp = _http_get_download(self._session, link)
            except NetworkConnectionError as e:
                assert e.response is not None
                logger.critical(
                    "HTTP error %s while getting %s",
                    e.response.status_code, link,
                )
                raise

            filename = _get_http_response_filename(resp, link)
            filepath = os.path.join(location, filename)

            chunks = _prepare_download(resp, link, self._progress_bar)
            with open(filepath, 'wb') as content_file:
                for chunk in chunks:
                    content_file.write(chunk)
            content_type = resp.headers.get('Content-Type', '')
            yield link, (filepath, content_type)
