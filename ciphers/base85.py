"""
Base85 (Ascii85) encoding and decoding

https://en.wikipedia.org/wiki/Ascii85
"""


def _base10_to_85(d: int) -> str:
    res = []
    for _ in range(5):
        res.append(chr(d % 85 + 33))
        d //= 85
    return "".join(res)


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
    >>> ascii85_encode("héllo".encode())
    b'BZ$fcCi9'
    """
    if not data:
        return b""
    binary_data = "".join(bin(byte)[2:].zfill(8) for byte in data)
    remainder = len(binary_data) % 32
    null_bits = (32 - remainder) % 32
    binary_data = binary_data + "0" * null_bits
    null_bytes = null_bits // 8

    b85_chunks = [
        int(binary_data[i : i + 32], 2) for i in range(0, len(binary_data), 32)
    ]
    result = "".join(_base10_to_85(chunk)[::-1] for chunk in b85_chunks)
    return bytes(result[:-null_bytes] if null_bytes > 0 else result, "utf-8")


def ascii85_decode(data: bytes) -> bytes:
    """
    >>> ascii85_decode(b"")
    b''
    >>> ascii85_decode(b"0etOA2#")
    b'12345'
    >>> ascii85_decode(b"@UX=h+?24")
    b'base 85'
    >>> ascii85_decode(b'BZ$fcCi9').decode()
    'héllo'
    """
    if not data:
        return b""
    s = data.decode("ascii")
    null_values = (5 - (len(s) % 5)) % 5
    binary_data = s + "u" * null_values
    b85_chunks = [binary_data[i : i + 5] for i in range(0, len(binary_data), 5)]
    b85_segments = [[ord(c) - 33 for c in chunk] for chunk in b85_chunks]
    results = [bin(_base85_to_10(chunk))[2:].zfill(32) for chunk in b85_segments]
    byte_chunks = [[int(r[j : j + 8], 2) for j in range(0, 32, 8)] for r in results]
    raw_bytes = bytes(b for chunk in byte_chunks for b in chunk)
    return raw_bytes[:-null_values] if null_values > 0 else raw_bytes


if __name__ == "__main__":
    import doctest

    doctest.testmod()
