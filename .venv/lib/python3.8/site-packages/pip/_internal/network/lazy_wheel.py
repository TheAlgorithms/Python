"""Lazy ZIP over HTTP"""

__all__ = ['HTTPRangeRequestUnsupported', 'dist_from_wheel_url']

from bisect import bisect_left, bisect_right
from contextlib import contextmanager
from tempfile import NamedTemporaryFile
from typing import Any, Dict, Iterator, List, Optional, Tuple
from zipfile import BadZipfile, ZipFile

from pip._vendor.pkg_resources import Distribution
from pip._vendor.requests.models import CONTENT_CHUNK_SIZE, Response

from pip._internal.network.session import PipSession
from pip._internal.network.utils import HEADERS, raise_for_status, response_chunks
from pip._internal.utils.wheel import pkg_resources_distribution_for_wheel


class HTTPRangeRequestUnsupported(Exception):
    pass


def dist_from_wheel_url(name, url, session):
    # type: (str, str, PipSession) -> Distribution
    """Return a pkg_resources.Distribution from the given wheel URL.

    This uses HTTP range requests to only fetch the potion of the wheel
    containing metadata, just enough for the object to be constructed.
    If such requests are not supported, HTTPRangeRequestUnsupported
    is raised.
    """
    with LazyZipOverHTTP(url, session) as wheel:
        # For read-only ZIP files, ZipFile only needs methods read,
        # seek, seekable and tell, not the whole IO protocol.
        zip_file = ZipFile(wheel)  # type: ignore
        # After context manager exit, wheel.name
        # is an invalid file by intention.
        return pkg_resources_distribution_for_wheel(zip_file, name, wheel.name)


class LazyZipOverHTTP:
    """File-like object mapped to a ZIP file over HTTP.

    This uses HTTP range requests to lazily fetch the file's content,
    which is supposed to be fed to ZipFile.  If such requests are not
    supported by the server, raise HTTPRangeRequestUnsupported
    during initialization.
    """

    def __init__(self, url, session, chunk_size=CONTENT_CHUNK_SIZE):
        # type: (str, PipSession, int) -> None
        head = session.head(url, headers=HEADERS)
        raise_for_status(head)
        assert head.status_code == 200
        self._session, self._url, self._chunk_size = session, url, chunk_size
        self._length = int(head.headers['Content-Length'])
        self._file = NamedTemporaryFile()
        self.truncate(self._length)
        self._left = []  # type: List[int]
        self._right = []  # type: List[int]
        if 'bytes' not in head.headers.get('Accept-Ranges', 'none'):
            raise HTTPRangeRequestUnsupported('range request is not supported')
        self._check_zip()

    @property
    def mode(self):
        # type: () -> str
        """Opening mode, which is always rb."""
        return 'rb'

    @property
    def name(self):
        # type: () -> str
        """Path to the underlying file."""
        return self._file.name

    def seekable(self):
        # type: () -> bool
        """Return whether random access is supported, which is True."""
        return True

    def close(self):
        # type: () -> None
        """Close the file."""
        self._file.close()

    @property
    def closed(self):
        # type: () -> bool
        """Whether the file is closed."""
        return self._file.closed

    def read(self, size=-1):
        # type: (int) -> bytes
        """Read up to size bytes from the object and return them.

        As a convenience, if size is unspecified or -1,
        all bytes until EOF are returned.  Fewer than
        size bytes may be returned if EOF is reached.
        """
        download_size = max(size, self._chunk_size)
        start, length = self.tell(), self._length
        stop = length if size < 0 else min(start+download_size, length)
        start = max(0, stop-download_size)
        self._download(start, stop-1)
        return self._file.read(size)

    def readable(self):
        # type: () -> bool
        """Return whether the file is readable, which is True."""
        return True

    def seek(self, offset, whence=0):
        # type: (int, int) -> int
        """Change stream position and return the new absolute position.

        Seek to offset relative position indicated by whence:
        * 0: Start of stream (the default).  pos should be >= 0;
        * 1: Current position - pos may be negative;
        * 2: End of stream - pos usually negative.
        """
        return self._file.seek(offset, whence)

    def tell(self):
        # type: () -> int
        """Return the current possition."""
        return self._file.tell()

    def truncate(self, size=None):
        # type: (Optional[int]) -> int
        """Resize the stream to the given size in bytes.

        If size is unspecified resize to the current position.
        The current stream position isn't changed.

        Return the new file size.
        """
        return self._file.truncate(size)

    def writable(self):
        # type: () -> bool
        """Return False."""
        return False

    def __enter__(self):
        # type: () -> LazyZipOverHTTP
        self._file.__enter__()
        return self

    def __exit__(self, *exc):
        # type: (*Any) -> Optional[bool]
        return self._file.__exit__(*exc)

    @contextmanager
    def _stay(self):
        # type: ()-> Iterator[None]
        """Return a context manager keeping the position.

        At the end of the block, seek back to original position.
        """
        pos = self.tell()
        try:
            yield
        finally:
            self.seek(pos)

    def _check_zip(self):
        # type: () -> None
        """Check and download until the file is a valid ZIP."""
        end = self._length - 1
        for start in reversed(range(0, end, self._chunk_size)):
            self._download(start, end)
            with self._stay():
                try:
                    # For read-only ZIP files, ZipFile only needs
                    # methods read, seek, seekable and tell.
                    ZipFile(self)  # type: ignore
                except BadZipfile:
                    pass
                else:
                    break

    def _stream_response(self, start, end, base_headers=HEADERS):
        # type: (int, int, Dict[str, str]) -> Response
        """Return HTTP response to a range request from start to end."""
        headers = base_headers.copy()
        headers['Range'] = f'bytes={start}-{end}'
        # TODO: Get range requests to be correctly cached
        headers['Cache-Control'] = 'no-cache'
        return self._session.get(self._url, headers=headers, stream=True)

    def _merge(self, start, end, left, right):
        # type: (int, int, int, int) -> Iterator[Tuple[int, int]]
        """Return an iterator of intervals to be fetched.

        Args:
            start (int): Start of needed interval
            end (int): End of needed interval
            left (int): Index of first overlapping downloaded data
            right (int): Index after last overlapping downloaded data
        """
        lslice, rslice = self._left[left:right], self._right[left:right]
        i = start = min([start]+lslice[:1])
        end = max([end]+rslice[-1:])
        for j, k in zip(lslice, rslice):
            if j > i:
                yield i, j-1
            i = k + 1
        if i <= end:
            yield i, end
        self._left[left:right], self._right[left:right] = [start], [end]

    def _download(self, start, end):
        # type: (int, int) -> None
        """Download bytes from start to end inclusively."""
        with self._stay():
            left = bisect_left(self._right, start)
            right = bisect_right(self._left, end)
            for start, end in self._merge(start, end, left, right):
                response = self._stream_response(start, end)
                response.raise_for_status()
                self.seek(start)
                for chunk in response_chunks(response, self._chunk_size):
                    self._file.write(chunk)
