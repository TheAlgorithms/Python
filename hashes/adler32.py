"""
Adler-32 is a checksum algorithm which was invented by Mark Adler in 1995.
Compared to a cyclic redundancy check of the same length, it trades reliability for
speed (preferring the latter).
Adler-32 is more reliable than Fletcher-16, and slightly less reliable than
Fletcher-32.[2]

source: https://en.wikipedia.org/wiki/Adler-32
"""

MOD_ADLER = 65521


def adler32(plain_text: str) -> int:
    """
    Function implements adler-32 hash.
    Adler-32 is defined over a byte stream; this implementation encodes the
    input string as UTF-8 and iterates over the resulting bytes, matching the
    behaviour of ``zlib.adler32`` for all inputs (not just ASCII).

    >>> adler32('Algorithms')
    363791387

    >>> adler32('go adler em all')
    708642122

    >>> import zlib
    >>> adler32('€100') == zlib.adler32('€100'.encode())
    True

    >>> adler32('日本語テスト') == zlib.adler32('日本語テスト'.encode())
    True
    """
    a = 1
    b = 0
    for byte in plain_text.encode("utf-8"):
        a = (a + byte) % MOD_ADLER
        b = (b + a) % MOD_ADLER
    return (b << 16) | a
