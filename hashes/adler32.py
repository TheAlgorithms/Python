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
    Return the Adler-32 checksum of a string encoded as UTF-8.

    >>> adler32('Algorithms')
    363791387

    >>> adler32('go adler em all')
    708642122

    >>> adler32('€100')
    196018850

    >>> adler32('日本語テスト')
    2053180537

    >>> adler32('')
    1
    """
    a = 1
    b = 0
    for plain_byte in plain_text.encode("utf-8"):
        a = (a + plain_byte) % MOD_ADLER
        b = (b + a) % MOD_ADLER
    return (b << 16) | a
