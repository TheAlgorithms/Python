"""
Endianness Conversion Algorithm

This module implements endianness (byte order) conversion utilities for converting
between big-endian and little-endian representations of multi-byte integers.

Endianness refers to the order of bytes in a multi-byte data type:
- Big-endian: Most significant byte first (e.g., 0x12345678 → [0x12, 0x34, 0x56, 0x78])
- Little-endian: Least significant byte first
  (e.g., 0x12345678 → [0x78, 0x56, 0x34, 0x12])

Common uses:
- Network protocols (TCP/IP uses big-endian for multi-byte fields)
- File format parsing (PNG, JPEG headers specify endianness)
- Cryptographic algorithms (MD5 uses little-endian, SHA-256 uses big-endian)
- Binary data serialization (Protocol Buffers, MessagePack)
- Hardware interfacing (ARM is bi-endian, x86 is strictly little-endian)
- Cross-platform data exchange

Real-world examples:
- IP addresses are transmitted in big-endian (network byte order)
- Modern ARM and x86 processors typically operate in little-endian mode
- Java class files use big-endian format
- Bitcoin uses little-endian for block hashes
- USB and PCI protocols use little-endian

References:
- https://en.wikipedia.org/wiki/Endianness
- RFC 1700 (Network Byte Order)
- https://tools.ietf.org/html/rfc1700
"""


def swap_endianness_16(value: int) -> int:
    """
    Swap the byte order of a 16-bit integer.

    Args:
        value: 16-bit integer (0 to 65,535)

    Returns:
        Integer with swapped byte order

    Raises:
        ValueError: If value is negative or exceeds 16-bit range

    >>> swap_endianness_16(0x1234)
    13330

    >>> hex(swap_endianness_16(0x1234))
    '0x3412'

    >>> swap_endianness_16(0xABCD)
    52651

    >>> hex(swap_endianness_16(0xABCD))
    '0xcdab'

    >>> swap_endianness_16(0)
    0

    >>> swap_endianness_16(0xFFFF)
    65535
    """
    if value < 0 or value > 0xFFFF:
        msg = f"value must be between 0 and {0xFFFF}"
        raise ValueError(msg)

    return ((value & 0xFF) << 8) | ((value & 0xFF00) >> 8)


def swap_endianness_32(value: int) -> int:
    """
    Swap the byte order of a 32-bit integer.

    Args:
        value: 32-bit integer (0 to 4,294,967,295)

    Returns:
        Integer with swapped byte order

    Raises:
        ValueError: If value is negative or exceeds 32-bit range

    >>> swap_endianness_32(0x12345678)
    2018915346

    >>> hex(swap_endianness_32(0x12345678))
    '0x78563412'

    >>> swap_endianness_32(0xDEADBEEF)
    4022250974

    >>> hex(swap_endianness_32(0xDEADBEEF))
    '0xefbeadde'

    >>> swap_endianness_32(0)
    0

    >>> swap_endianness_32(0xFFFFFFFF)
    4294967295

    >>> swap_endianness_32(0x01020304)
    67305985
    """
    if value < 0 or value > 0xFFFFFFFF:
        msg = f"value must be between 0 and {0xFFFFFFFF}"
        raise ValueError(msg)

    return (
        ((value & 0x000000FF) << 24)
        | ((value & 0x0000FF00) << 8)
        | ((value & 0x00FF0000) >> 8)
        | ((value & 0xFF000000) >> 24)
    )


def swap_endianness_64(value: int) -> int:
    """
    Swap the byte order of a 64-bit integer.

    Args:
        value: 64-bit integer (0 to 18,446,744,073,709,551,615)

    Returns:
        Integer with swapped byte order

    Raises:
        ValueError: If value is negative or exceeds 64-bit range

    >>> swap_endianness_64(0x0123456789ABCDEF)
    17279655951921914625

    >>> hex(swap_endianness_64(0x0123456789ABCDEF))
    '0xefcdab8967452301'

    >>> swap_endianness_64(0xFEDCBA9876543210)
    1167088121787636990

    >>> hex(swap_endianness_64(0xFEDCBA9876543210))
    '0x1032547698badcfe'

    >>> swap_endianness_64(0)
    0

    >>> swap_endianness_64(0xFFFFFFFFFFFFFFFF)
    18446744073709551615
    """
    if value < 0 or value > 0xFFFFFFFFFFFFFFFF:
        msg = f"value must be between 0 and {0xFFFFFFFFFFFFFFFF}"
        raise ValueError(msg)

    return (
        ((value & 0x00000000000000FF) << 56)
        | ((value & 0x000000000000FF00) << 40)
        | ((value & 0x0000000000FF0000) << 24)
        | ((value & 0x00000000FF000000) << 8)
        | ((value & 0x000000FF00000000) >> 8)
        | ((value & 0x0000FF0000000000) >> 24)
        | ((value & 0x00FF000000000000) >> 40)
        | ((value & 0xFF00000000000000) >> 56)
    )


def bytes_to_int_little(data: bytes) -> int:
    """
    Convert bytes to integer using little-endian byte order.

    Args:
        data: Byte sequence to convert (1-8 bytes)

    Returns:
        Integer representation in little-endian order

    Raises:
        TypeError: If data is not bytes
        ValueError: If data is empty or exceeds 8 bytes

    >>> bytes_to_int_little(b'\\x78\\x56\\x34\\x12')
    305419896

    >>> hex(bytes_to_int_little(b'\\x78\\x56\\x34\\x12'))
    '0x12345678'

    >>> bytes_to_int_little(b'\\x01\\x02')
    513

    >>> bytes_to_int_little(b'\\xff')
    255

    >>> bytes_to_int_little(b'\\x00\\x00\\x00\\x01')
    16777216
    """
    if not data or len(data) > 8:
        msg = "data must be between 1 and 8 bytes"
        raise ValueError(msg)

    return int.from_bytes(data, byteorder="little")


def bytes_to_int_big(data: bytes) -> int:
    """
    Convert bytes to integer using big-endian byte order.

    Args:
        data: Byte sequence to convert (1-8 bytes)

    Returns:
        Integer representation in big-endian order

    Raises:
        TypeError: If data is not bytes
        ValueError: If data is empty or exceeds 8 bytes

    >>> bytes_to_int_big(b'\\x12\\x34\\x56\\x78')
    305419896

    >>> hex(bytes_to_int_big(b'\\x12\\x34\\x56\\x78'))
    '0x12345678'

    >>> bytes_to_int_big(b'\\x01\\x02')
    258

    >>> bytes_to_int_big(b'\\xff')
    255

    >>> bytes_to_int_big(b'\\x00\\x00\\x00\\x01')
    1
    """
    if not data or len(data) > 8:
        msg = "data must be between 1 and 8 bytes"
        raise ValueError(msg)

    return int.from_bytes(data, byteorder="big")


def int_to_bytes_little(value: int, num_bytes: int) -> bytes:
    """
    Convert integer to bytes using little-endian byte order.

    Args:
        value: Integer to convert (non-negative)
        num_bytes: Number of bytes in output (1-8)

    Returns:
        Bytes representation in little-endian order

    Raises:
        ValueError: If value is negative, num_bytes invalid, or value too large

    >>> int_to_bytes_little(0x12345678, 4)
    b'xV4\\x12'

    >>> int_to_bytes_little(513, 2)
    b'\\x01\\x02'

    >>> int_to_bytes_little(255, 1)
    b'\\xff'

    >>> int_to_bytes_little(16777216, 4)
    b'\\x00\\x00\\x00\\x01'
    """
    if value < 0:
        msg = "value must be non-negative"
        raise ValueError(msg)

    if num_bytes < 1 or num_bytes > 8:
        msg = "num_bytes must be between 1 and 8"
        raise ValueError(msg)

    if value >= (1 << (num_bytes * 8)):
        msg = f"value {value} too large for {num_bytes} bytes"
        raise ValueError(msg)

    return value.to_bytes(num_bytes, byteorder="little")


def int_to_bytes_big(value: int, num_bytes: int) -> bytes:
    """
    Convert integer to bytes using big-endian byte order.

    Args:
        value: Integer to convert (non-negative)
        num_bytes: Number of bytes in output (1-8)

    Returns:
        Bytes representation in big-endian order

    Raises:
        ValueError: If value is negative, num_bytes invalid, or value too large

    >>> int_to_bytes_big(0x12345678, 4)
    b'\\x124Vx'

    >>> int_to_bytes_big(258, 2)
    b'\\x01\\x02'

    >>> int_to_bytes_big(255, 1)
    b'\\xff'

    >>> int_to_bytes_big(1, 4)
    b'\\x00\\x00\\x00\\x01'
    """
    if value < 0:
        msg = "value must be non-negative"
        raise ValueError(msg)

    if num_bytes < 1 or num_bytes > 8:
        msg = "num_bytes must be between 1 and 8"
        raise ValueError(msg)

    if value >= (1 << (num_bytes * 8)):
        msg = f"value {value} too large for {num_bytes} bytes"
        raise ValueError(msg)

    return value.to_bytes(num_bytes, byteorder="big")


if __name__ == "__main__":
    import doctest

    _ = doctest.testmod()

    print("Endianness Conversion Examples:")
    print(f"16-bit: 0x1234 → {hex(swap_endianness_16(0x1234))}")
    print(f"32-bit: 0x12345678 → {hex(swap_endianness_32(0x12345678))}")
    print(f"64-bit: 0x0123456789ABCDEF → {hex(swap_endianness_64(0x0123456789ABCDEF))}")
    print(f"Bytes to int (little): {bytes_to_int_little(b'\x78\x56\x34\x12'):#x}")
    print(f"Bytes to int (big): {bytes_to_int_big(b'\x12\x34\x56\x78'):#x}")
