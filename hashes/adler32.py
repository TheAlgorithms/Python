"""
Adler-32 is a checksum algorithm which was invented by Mark Adler in 1995.
Compared to a cyclic redundancy check of the same length, it trades reliability for
speed (preferring the latter).
Adler-32 is more reliable than Fletcher-16, and slightly less reliable than
Fletcher-32.[2]

source: https://en.wikipedia.org/wiki/Adler-32
"""

MOD_ADLER = 65521


def adler32(data: bytes) -> int:
    """
    Function implements adler-32 hash.
    Iterates and evaluates a new value for each byte of the input.

    Unlike the former str API, this function requires bytes. Encode text explicitly
    (for example, with text.encode("utf-8")) before calling it.

    Args:
        data: Byte data to calculate the hash for

    Returns:
        Adler-32 checksum as a 32-bit integer

    Raises:
        TypeError: If data is not of type bytes

    >>> adler32(b'Algorithms')
    363791387

    >>> adler32(b'Wikipedia') == 0x11E60398
    True

    >>> import zlib

    >>> adler32(b'go adler em all') == zlib.adler32(b'go adler em all')
    True

    The previous implementation summed Unicode code points instead of UTF-8 bytes.

    >>> data = '€100'.encode('utf-8')
    >>> adler32(data) == zlib.adler32(data)
    True

    >>> adler32(b'') == zlib.adler32(b'')
    True

    >>> adler32('not bytes')
    Traceback (most recent call last):
      ...
    TypeError: data must be bytes, not str

    >>> adler32(123)
    Traceback (most recent call last):
      ...
    TypeError: data must be bytes, not int
    """
    if not isinstance(data, bytes):
        msg = f"data must be bytes, not {type(data).__name__}"
        raise TypeError(msg)

    a = 1
    b = 0
    for byte in data:
        a = (a + byte) % MOD_ADLER
        b = (b + a) % MOD_ADLER
    return (b << 16) | a
