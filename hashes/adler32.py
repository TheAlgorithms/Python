"""
Adler-32 is a checksum algorithm which was invented by Mark Adler in 1995.
Compared to a cyclic redundancy check of the same length, it trades reliability for
speed (preferring the latter).
Adler-32 is more reliable than Fletcher-16, and slightly less reliable than
Fletcher-32.[2]

Adler-32 is defined over a byte stream, so the input text is hashed as its
UTF-8 encoded bytes. This makes the result match every standard
implementation, e.g. `zlib.adler32(text.encode())`, for any input text.

source: https://en.wikipedia.org/wiki/Adler-32
"""

MOD_ADLER = 65521


def adler32(plain_text: str) -> int:
    """
    Function implements adler-32 hash.
    Iterates and evaluates a new value for each byte of the UTF-8 encoded text

    >>> adler32('Algorithms')
    363791387

    >>> adler32('go adler em all')
    708642122

    >>> adler32('€100')
    196018850

    >>> adler32('日本語テスト')
    2053180537

    >>> import zlib
    >>> texts = ('Algorithms', 'go adler em all', 'héllo', '€100', '日本語テスト')
    >>> all(adler32(text) == zlib.adler32(text.encode()) for text in texts)
    True
    """
    a = 1
    b = 0
    for byte in plain_text.encode():
        a = (a + byte) % MOD_ADLER
        b = (b + a) % MOD_ADLER
    return (b << 16) | a


if __name__ == "__main__":
    import doctest

    doctest.testmod()
