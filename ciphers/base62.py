import string


def base62_encode(num: int) -> str:
    """
    Encodes a positive integer into a base62 string.
    """
    if num == 0:
        return "0"

    arr = []
    base = 62
    charset = string.digits + string.ascii_lowercase + string.ascii_uppercase
    while num:
        num, rem = divmod(num, base)
        arr.append(charset[rem])
    arr.reverse()
    return "".join(arr)


def base62_decode(string_val: str) -> int:
    """
    Decodes a base62 string into a positive integer.
    """
    base = 62
    charset = string.digits + string.ascii_lowercase + string.ascii_uppercase
    strlen = len(string_val)
    num = 0

    for idx, char in enumerate(string_val):
        power = strlen - (idx + 1)
        num += charset.index(char) * (base**power)
    return num


def test_base62() -> None:
    """
    Tests for base62_encode and base62_decode.
    """
    assert base62_encode(0) == "0"
    assert base62_encode(123) == "1z"
    assert base62_encode(1000000) == "4C92"
    assert base62_decode("0") == 0
    assert base62_decode("1z") == 123
    assert base62_decode("4C92") == 1000000


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_base62()
