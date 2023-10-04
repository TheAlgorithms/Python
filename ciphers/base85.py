"""
Base85 (Ascii85) encoding and decoding

https://en.wikipedia.org/wiki/Ascii85
"""


def _base10_to_85(d: int) -> str:
    return "".join(chr(d % 85 + 33)) + _base10_to_85(d // 85) if d > 0 else ""


def _base85_to_10(digits: list) -> int:
    return sum(char * 85**i for i, char in enumerate(reversed(digits)))


def ascii85_encode(data: bytes) -> bytes:
    """
    >>> ascii85_encode(b"")
    b''
    >>> ascii85_encode(b"12345")
    b'0etOA2#'
    >>> ascii85_encode(b"base 85")
    b'@UX=h+?24'
    """
    binary_data = "".join(bin(ord(d))[2:].zfill(8) for d in data.decode("utf-8"))
    null_values = (32 * ((len(binary_data) // 32) + 1) - len(binary_data)) // 8
    binary_data = binary_data.ljust(32 * ((len(binary_data) // 32) + 1), "0")
    b85_chunks = [int(_s, 2) for _s in map("".join, zip(*[iter(binary_data)] * 32))]
    result = "".join(_base10_to_85(chunk)[::-1] for chunk in b85_chunks)
    return bytes(result[:-null_values] if null_values % 4 != 0 else result, "utf-8")


def ascii85_decode(data: bytes) -> bytes:
    """
    >>> ascii85_decode(b"")
    b''
    >>> ascii85_decode(b"0etOA2#")
    b'12345'
    >>> ascii85_decode(b"@UX=h+?24")
    b'base 85'
    """
    null_values = 5 * ((len(data) // 5) + 1) - len(data)
    binary_data = data.decode("utf-8") + "u" * null_values
    b85_chunks = map("".join, zip(*[iter(binary_data)] * 5))
    b85_segments = [[ord(_s) - 33 for _s in chunk] for chunk in b85_chunks]
    results = [bin(_base85_to_10(chunk))[2::].zfill(32) for chunk in b85_segments]
    char_chunks = [
        [chr(int(_s, 2)) for _s in map("".join, zip(*[iter(r)] * 8))] for r in results
    ]
    result = "".join("".join(char) for char in char_chunks)
    offset = int(null_values % 5 == 0)
    return bytes(result[: offset - null_values], "utf-8")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
