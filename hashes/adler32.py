"""
Adler-32 is a checksum algorithm which was invented by Mark Adler in 1995.
Compared to a cyclic redundancy check of the same length, it trades reliability for
speed (preferring the latter).
Adler-32 is more reliable than Fletcher-16, and slightly less reliable than
Fletcher-32.[2]

source: https://en.wikipedia.org/wiki/Adler-32
"""

MOD_ADLER = 65521


def adler32(plain_text: str | bytes) -> int:
    """
    Function implements adler-32 hash.
    Iterates and evaluates a new value for each byte in the data.
    If a string is passed, it is encoded to UTF-8 bytes per the Adler-32 specification.

    >>> adler32('Algorithms')
    363791387

    >>> adler32('go adler em all')
    708642122

    >>> adler32('€100')
    196018850

    >>> adler32(b'Algorithms')
    363791387

    >>> adler32(b'')
    1

    >>> adler32('')
    1

    >>> import zlib
    >>> adler32('日本語テスト') == zlib.adler32('日本語テスト'.encode())
    True

    >>> adler32(b'\\x00\\xff\\xfe') == zlib.adler32(b'\\x00\\xff\\xfe')
    True

    >>> adler32(123)
    Traceback (most recent call last):
        ...
    TypeError: plain_text must be str or bytes-like, not int
    """
    if not isinstance(plain_text, (str, bytes, bytearray)):
        msg = f"plain_text must be str or bytes-like, not {type(plain_text).__name__}"
        raise TypeError(msg)

    data = plain_text.encode("utf-8") if isinstance(plain_text, str) else plain_text
    a = 1
    b = 0
    for byte in data:
        a = (a + byte) % MOD_ADLER
        b = (b + a) % MOD_ADLER
    return (b << 16) | a


if __name__ == "__main__":
    import doctest

    doctest.testmod()
