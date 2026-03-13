"""
xxHash Algorithm

This module implements the xxHash32 algorithm, an extremely fast non-cryptographic
hash function designed to operate at RAM speed limits.

xxHash is known for:
- Extreme speed: One of the fastest hash algorithms available
- Excellent distribution: Passes SMHasher test suite
- Portability: Identical output across all platforms
- Simplicity: Compact implementation with good performance

Common uses:
- Zstandard compression (Facebook's compression algorithm)
- LZ4 compression
- rsync file synchronization
- Database indexing and deduplication
- Hash tables requiring high performance

The algorithm uses carefully selected prime numbers and processes data in 16-byte
stripes using four parallel accumulators for maximum speed.

Note: xxHash is NOT cryptographically secure. Use SHA-256 or similar for security.

References:
- https://github.com/Cyan4973/xxHash
- https://xxhash.com/
- https://github.com/Cyan4973/xxHash/blob/dev/doc/xxhash_spec.md
"""


def _rotl32(value: int, amount: int) -> int:
    """
    Rotate a 32-bit integer left by the specified amount.

    Args:
        value: 32-bit integer to rotate
        amount: Number of bits to rotate (0-31)

    Returns:
        Rotated 32-bit integer

    >>> _rotl32(0x12345678, 8)
    878082066
    >>> _rotl32(0xFFFFFFFF, 1)
    4294967295
    """
    return ((value << amount) | (value >> (32 - amount))) & 0xFFFFFFFF


def xxhash32(data: bytes, seed: int = 0) -> int:
    """
    Calculate the xxHash32 hash of byte data.

    xxHash32 is extremely fast and has excellent distribution properties.
    It processes data in 16-byte chunks using four parallel accumulators.

    Args:
        data: Byte data to hash
        seed: Optional seed value (default: 0) for hash initialization

    Returns:
        32-bit hash value (0 to 4,294,967,295)

    Raises:
        TypeError: If data is not bytes
        ValueError: If seed is negative or > 32-bit max

    >>> xxhash32(b"")
    46947589

    >>> xxhash32(b"hello")
    4211111929

    >>> xxhash32(b"Hello")
    4060533391

    >>> xxhash32(b"world")
    413819571

    >>> xxhash32(b"The quick brown fox jumps over the lazy dog")
    3898516702

    >>> xxhash32(b"a")
    1426945110

    >>> xxhash32(b"abc")
    852579327

    >>> xxhash32(b"Python")
    1196663540

    >>> xxhash32(b"xxHash")
    2929943677

    >>> xxhash32(b"\\x00\\x00\\x00\\x00")
    148298089

    >>> xxhash32(b"test" * 100) != xxhash32(b"test" * 101)
    True

    >>> xxhash32(b"hello", seed=42)
    1292028262

    >>> xxhash32(b"hello", seed=0) != xxhash32(b"hello", seed=1)
    True
    """
    if not isinstance(data, bytes):
        msg = f"data must be bytes, not {type(data).__name__}"
        raise TypeError(msg)

    if seed < 0 or seed > 0xFFFFFFFF:
        msg = f"seed must be between 0 and {0xFFFFFFFF}"
        raise ValueError(msg)

    prime1 = 0x9E3779B1
    prime2 = 0x85EBCA77
    prime3 = 0xC2B2AE3D
    prime4 = 0x27D4EB2F
    prime5 = 0x165667B1

    length = len(data)
    index = 0

    if length >= 16:
        limit = length - 16

        acc1 = (seed + prime1 + prime2) & 0xFFFFFFFF
        acc2 = (seed + prime2) & 0xFFFFFFFF
        acc3 = seed & 0xFFFFFFFF
        acc4 = (seed - prime1) & 0xFFFFFFFF

        while index <= limit:
            lane1 = int.from_bytes(data[index : index + 4], byteorder="little")
            lane2 = int.from_bytes(data[index + 4 : index + 8], byteorder="little")
            lane3 = int.from_bytes(data[index + 8 : index + 12], byteorder="little")
            lane4 = int.from_bytes(data[index + 12 : index + 16], byteorder="little")

            acc1 = _rotl32((acc1 + lane1 * prime2) & 0xFFFFFFFF, 13)
            acc1 = (acc1 * prime1) & 0xFFFFFFFF

            acc2 = _rotl32((acc2 + lane2 * prime2) & 0xFFFFFFFF, 13)
            acc2 = (acc2 * prime1) & 0xFFFFFFFF

            acc3 = _rotl32((acc3 + lane3 * prime2) & 0xFFFFFFFF, 13)
            acc3 = (acc3 * prime1) & 0xFFFFFFFF

            acc4 = _rotl32((acc4 + lane4 * prime2) & 0xFFFFFFFF, 13)
            acc4 = (acc4 * prime1) & 0xFFFFFFFF

            index += 16

        hash_value = (
            _rotl32(acc1, 1) + _rotl32(acc2, 7) + _rotl32(acc3, 12) + _rotl32(acc4, 18)
        )
        hash_value &= 0xFFFFFFFF
    else:
        hash_value = (seed + prime5) & 0xFFFFFFFF

    hash_value = (hash_value + length) & 0xFFFFFFFF

    while index + 4 <= length:
        lane = int.from_bytes(data[index : index + 4], byteorder="little")
        hash_value = (hash_value + lane * prime3) & 0xFFFFFFFF
        hash_value = _rotl32(hash_value, 17)
        hash_value = (hash_value * prime4) & 0xFFFFFFFF
        index += 4

    while index < length:
        lane = data[index]
        hash_value = (hash_value + lane * prime5) & 0xFFFFFFFF
        hash_value = _rotl32(hash_value, 11)
        hash_value = (hash_value * prime1) & 0xFFFFFFFF
        index += 1

    hash_value ^= hash_value >> 15
    hash_value = (hash_value * prime2) & 0xFFFFFFFF
    hash_value ^= hash_value >> 13
    hash_value = (hash_value * prime3) & 0xFFFFFFFF
    hash_value ^= hash_value >> 16

    return hash_value


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    test_data = b"Hello, xxHash!"
    print(f"xxHash32 of '{test_data.decode()}': {xxhash32(test_data)}")
    print(f"xxHash32 with seed=42: {xxhash32(test_data, seed=42)}")
