"""
Fowler-Noll-Vo (FNV-1a) Hash Algorithm.

This module implements the FNV-1a non-cryptographic hash algorithm in both
32-bit and 64-bit variants. Created by Glenn Fowler, Landon Curt Noll, and
Kiem-Phong Vo, FNV-1a is designed for fast hashing of byte sequences,
making it suitable for hash tables, checksums, and hash-based indexing.

The FNV-1a variant differs from FNV-1 by reversing the order of operations:
in FNV-1a, the data octet is XORed into the hash state *before* multiplying
by the FNV prime. This provides significantly better avalanche behavior
for the least significant bits of short keys.

Note: FNV hashes are non-cryptographic and must not be used for cryptographic
security, password hashing, or digital signatures.

References:
- http://www.isthe.com/chongo/tech/comp/fnv/
- https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
- https://datatracker.ietf.org/doc/html/draft-eastlake-fnv-17
"""

FNV_32_PRIME = 0x01000193
FNV_32_OFFSET_BASIS = 0x811C9DC5
MASK_32 = 0xFFFFFFFF

FNV_64_PRIME = 0x100000001B3
FNV_64_OFFSET_BASIS = 0xCBF29CE484222325
MASK_64 = 0xFFFFFFFFFFFFFFFF


def fnv1a_32(data: bytes | str) -> int:
    """
    Compute the 32-bit Fowler-Noll-Vo (FNV-1a) hash of the input data.

    Parameters:
        data: The input string or byte sequence to be hashed. If a string
              is provided, it is automatically encoded as UTF-8 bytes.

    Returns:
        A 32-bit unsigned integer representing the FNV-1a hash value.

    Raises:
        TypeError: If the input data is not an instance of bytes or str.

    Complexity:
        Time: O(n), where n is the number of bytes in data.
        Space: O(1) auxiliary space.

    Examples:
        >>> fnv1a_32("")
        2166136261
        >>> fnv1a_32(b"")
        2166136261
        >>> fnv1a_32("a")
        3826002220
        >>> fnv1a_32(b"a")
        3826002220
        >>> fnv1a_32("foobar")
        3214735720
        >>> fnv1a_32(b"foobar")
        3214735720
        >>> hex(fnv1a_32("foobar"))
        '0xbf9cf968'
        >>> fnv1a_32("The quick brown fox jumps over the lazy dog")
        76545936
        >>> fnv1a_32(12345)
        Traceback (most recent call last):
            ...
        TypeError: data must be bytes or str, not int
    """
    if isinstance(data, str):
        byte_data: bytes | bytearray = data.encode("utf-8")
    elif isinstance(data, (bytes, bytearray)):
        byte_data = data
    else:
        msg = f"data must be bytes or str, not {type(data).__name__}"
        raise TypeError(msg)

    hash_value = FNV_32_OFFSET_BASIS
    for byte in byte_data:
        hash_value = ((hash_value ^ byte) * FNV_32_PRIME) & MASK_32
    return hash_value


def fnv1a_64(data: bytes | str) -> int:
    """
    Compute the 64-bit Fowler-Noll-Vo (FNV-1a) hash of the input data.

    Parameters:
        data: The input string or byte sequence to be hashed. If a string
              is provided, it is automatically encoded as UTF-8 bytes.

    Returns:
        A 64-bit unsigned integer representing the FNV-1a hash value.

    Raises:
        TypeError: If the input data is not an instance of bytes or str.

    Complexity:
        Time: O(n), where n is the number of bytes in data.
        Space: O(1) auxiliary space.

    Examples:
        >>> fnv1a_64("")
        14695981039346656037
        >>> fnv1a_64(b"")
        14695981039346656037
        >>> fnv1a_64("a")
        12638187200555641996
        >>> fnv1a_64(b"a")
        12638187200555641996
        >>> fnv1a_64("foobar")
        9625390261332436968
        >>> fnv1a_64(b"foobar")
        9625390261332436968
        >>> hex(fnv1a_64("foobar"))
        '0x85944171f73967e8'
        >>> fnv1a_64("The quick brown fox jumps over the lazy dog")
        17580284887202820368
        >>> fnv1a_64(12345)
        Traceback (most recent call last):
            ...
        TypeError: data must be bytes or str, not int
    """
    if isinstance(data, str):
        byte_data: bytes | bytearray = data.encode("utf-8")
    elif isinstance(data, (bytes, bytearray)):
        byte_data = data
    else:
        msg = f"data must be bytes or str, not {type(data).__name__}"
        raise TypeError(msg)

    hash_value = FNV_64_OFFSET_BASIS
    for byte in byte_data:
        hash_value = ((hash_value ^ byte) * FNV_64_PRIME) & MASK_64
    return hash_value


if __name__ == "__main__":
    import doctest

    doctest.testmod()
