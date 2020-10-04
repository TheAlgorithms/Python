"""
    Adler-32 is a checksum algorithm which was invented by Mark Adler in 1995.
    Compared to a cyclic redundancy check of the same length, it trades reliability for
    speed (preferring the latter).
    Adler-32 is more reliable than Fletcher-16, and slightly less reliable than
    Fletcher-32.[2]

    source: https://en.wikipedia.org/wiki/Adler-32
"""


def adler32(plain_text: str) -> str:
    """
    Function implements adler-32 hash.
    Itterates and evaluates new value for each character

    >>> adler32('Algorithms')
    363791387

    >>> adler32('go adler em all')
    708642122
    """
    MOD_ADLER = 65521
    a = 1
    b = 0
    for plain_chr in plain_text:
        a = (a + ord(plain_chr)) % MOD_ADLER
        b = (b + a) % MOD_ADLER
    return (b << 16) | a
