"""
CRC-32 is a cyclic redundancy check algorithm that produces a 32-bit checksum.
It is widely used for error detection in network transmissions and file integrity
checks (ZIP, PNG, gzip, etc.). This implementation uses the reflected polynomial
0xEDB88320 with a precomputed 256-entry lookup table.

Reference: https://en.wikipedia.org/wiki/Cyclic_redundancy_check
"""


def _generate_crc32_table() -> list[int]:
    """
    Build a 256-entry lookup table for CRC-32 using the reflected
    polynomial 0xEDB88320.

    >>> table = _generate_crc32_table()
    >>> len(table)
    256
    >>> hex(table[0])
    '0x0'
    >>> hex(table[1])
    '0x77073096'
    """
    table: list[int] = []
    for byte in range(256):
        crc = byte
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xEDB88320
            else:
                crc >>= 1
        table.append(crc)
    return table


_CRC32_TABLE = _generate_crc32_table()


def crc32(data: bytes) -> int:
    """
    Compute the CRC-32 checksum for the given bytes.

    The output matches Python's ``zlib.crc32()`` for the same input.

    >>> crc32(b'')
    0
    >>> hex(crc32(b'hello'))
    '0x3610a686'
    >>> crc32(b'hello world')
    222957957
    >>> hex(crc32(b'The quick brown fox jumps over the lazy dog'))
    '0x414fa339'

    Verify against zlib:
    >>> import zlib
    >>> crc32(b'hello world') == zlib.crc32(b'hello world')
    True
    >>> crc32(b'\\x00\\xff\\x55\\xaa') == zlib.crc32(b'\\x00\\xff\\x55\\xaa')
    True
    """
    crc = 0xFFFFFFFF
    for byte in data:
        lookup_index = (crc ^ byte) & 0xFF
        crc = (crc >> 8) ^ _CRC32_TABLE[lookup_index]
    return crc ^ 0xFFFFFFFF


if __name__ == "__main__":
    import doctest

    doctest.testmod()
