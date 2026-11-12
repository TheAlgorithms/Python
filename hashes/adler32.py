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

    Args:
        data: Byte data to calculate the hash for

    Returns:
        Adler-32 checksum as a 32-bit integer

    Raises:
        TypeError: If data is not of type bytes

    >>> import zlib
    >>> adler32(b'Algorithms') == zlib.adler32(b'Algorithms')
    True

    >>> adler32(b'go adler em all') == zlib.adler32(b'go adler em all')
    True

    >>> data = bytes([226, 130, 172, 49, 48, 48])
    >>> adler32(data) == zlib.adler32(data)
    True

    >>> adler32(b'') == zlib.adler32(b'')
    True

    >>> adler32('not bytes')
    Traceback (most recent call last):
      ...
    TypeError: data must be bytes, not str
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
