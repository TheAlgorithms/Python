"""
CRC32 (Cyclic Redundancy Check 32-bit) Hash Algorithm

This module implements the CRC32 hash algorithm, a non-cryptographic hash function
widely used for error detection and data integrity verification.

CRC32 is commonly used in:
- ZIP file format for data integrity
- Ethernet frame check sequences
- PNG image format for chunk verification
- Gzip compression

The algorithm uses the IEEE 802.3 polynomial (0xEDB88320 in reversed bit order)
and produces a 32-bit hash value.

Note: CRC32 is NOT suitable for cryptographic purposes. It's designed for
error detection, not security. For cryptographic hashing, use SHA-256 or similar.

Reference:
- https://en.wikipedia.org/wiki/Cyclic_redundancy_check
- https://www.rfc-editor.org/rfc/rfc1952.html (GZIP specification)
"""


def _generate_crc32_table() -> list[int]:
    """
    Generate the CRC32 lookup table for optimized calculation.

    Uses the IEEE 802.3 polynomial: 0xEDB88320 (reversed bit order)

    >>> table = _generate_crc32_table()
    >>> len(table)
    256
    >>> hex(table[0])
    '0x0'
    >>> hex(table[128])
    '0xedb88320'
    """
    polynomial = 0xEDB88320
    table = []

    for i in range(256):
        crc = i
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ polynomial
            else:
                crc >>= 1
        table.append(crc)

    return table


CRC32_TABLE = _generate_crc32_table()


def crc32(data: bytes) -> int:
    """
    Calculate the CRC32 hash of byte data.

    Args:
        data: Byte data to calculate the hash for

    Returns:
        CRC32 hash as a 32-bit integer (0 to 4294967295)

    Raises:
        TypeError: If data is not of type bytes

    >>> crc32(b"Hello World")
    1243066710

    >>> crc32(b"")
    0

    >>> crc32(b"The quick brown fox jumps over the lazy dog")
    1095738169

    >>> crc32(b"a")
    3904355907

    >>> crc32(b"abc")
    891568578

    >>> crc32(b"123456789")
    3421780262

    >>> crc32(b"Python")
    2742599054

    >>> crc32(b"Algorithms")
    3866870335

    >>> crc32(b"CRC32")
    4128576900

    >>> crc32(b"\\x00\\x00\\x00\\x00")
    558161692

    >>> import zlib
    >>> test_data = b"Verify with zlib"
    >>> crc32(test_data) == zlib.crc32(test_data)
    True
    """
    if not isinstance(data, bytes):
        msg = f"data must be bytes, not {type(data).__name__}"
        raise TypeError(msg)

    crc = 0xFFFFFFFF

    for byte in data:
        table_index = (crc ^ byte) & 0xFF
        crc = (crc >> 8) ^ CRC32_TABLE[table_index]

    return crc ^ 0xFFFFFFFF


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(f"CRC32 of 'Hello World': {crc32(b'Hello World')}")
    print(f"CRC32 of empty bytes: {crc32(b'')}")
