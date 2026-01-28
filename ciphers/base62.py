import string
import doctest

CHARSET = string.digits + string.ascii_lowercase + string.ascii_uppercase


def base62_encode(num: int) -> str:
    """
    Encodes a positive integer into a base62 string.
    >>> base62_encode(0)
    '0'
    >>> base62_encode(123)
    '1z'
    >>> base62_encode(1000000)
    '4C92'
    """
    if num == 0:
        return CHARSET[0]

    arr = []
    base = len(CHARSET)
    while num:
        num, rem = divmod(num, base)
        arr.append(CHARSET[rem])
    arr.reverse()
    return "".join(arr)


def base62_decode(string_val: str) -> int:
    """
    Decodes a base62 string into a positive integer.
    >>> base62_decode('0')
    0
    >>> base62_decode('1z')
    123
    >>> base62_decode('4C92')
    1000000
    """
    base = len(CHARSET)
    strlen = len(string_val)
    num = 0

    for idx, char in enumerate(string_val):
        power = strlen - (idx + 1)
        num += CHARSET.index(char) * (base**power)
    return num


if __name__ == "__main__":
    doctest.testmod()
