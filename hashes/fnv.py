"""
FNV (Fowler-Noll-Vo) Hash Algorithm

This module implements the FNV-1a hash algorithm, a fast non-cryptographic hash
function widely used in hash tables, bloom filters, and checksums.

FNV-1a is known for:
- Simplicity: Very simple implementation (XOR and multiply)
- Speed: Extremely fast computation
- Good distribution: Excellent avalanche properties
- Zero collisions: For short strings, very few collisions

Common uses:
- Hash tables (Python's dict historically used a variant)
- Bloom filters and caches
- Checksums for data structures
- Database indexing

The algorithm uses prime numbers and XOR operations to create well-distributed
hash values. The "1a" variant (used here) processes bytes in a different order
than FNV-1, typically providing better distribution.

Note: FNV is NOT cryptographically secure. Use SHA-256 or similar for security.

References:
- http://www.isthe.com/chongo/tech/comp/fnv/
- https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
"""


def fnv1a_32(data: bytes) -> int:
    """
    Calculate the FNV-1a 32-bit hash of byte data.

    FNV-1a uses XOR-then-multiply instead of multiply-then-XOR,
    providing better avalanche characteristics than FNV-1.

    Args:
        data: Byte data to hash

    Returns:
        32-bit hash value (0 to 4,294,967,295)

    Raises:
        TypeError: If data is not bytes

    >>> fnv1a_32(b"")
    2166136261

    >>> fnv1a_32(b"hello")
    1335831723

    >>> fnv1a_32(b"Hello")
    4116459851

    >>> fnv1a_32(b"world")
    933488787

    >>> fnv1a_32(b"The quick brown fox jumps over the lazy dog")
    76545936

    >>> fnv1a_32(b"a")
    3826002220

    >>> fnv1a_32(b"abc")
    440920331

    >>> fnv1a_32(b"Python")
    3822946231

    >>> fnv1a_32(b"FNV-1a")
    3973616866

    >>> fnv1a_32(b"\\x00\\x00\\x00\\x00")
    1268118805

    >>> fnv1a_32(b"test" * 100) != fnv1a_32(b"test" * 101)
    True
    """
    if not isinstance(data, bytes):
        msg = f"data must be bytes, not {type(data).__name__}"
        raise TypeError(msg)

    fnv_32_prime = 0x01000193
    hash_value = 0x811C9DC5

    for byte in data:
        hash_value ^= byte
        hash_value = (hash_value * fnv_32_prime) & 0xFFFFFFFF

    return hash_value


def fnv1a_64(data: bytes) -> int:
    """
    Calculate the FNV-1a 64-bit hash of byte data.

    The 64-bit variant provides a larger hash space, reducing
    collision probability for large datasets.

    Args:
        data: Byte data to hash

    Returns:
        64-bit hash value (0 to 18,446,744,073,709,551,615)

    Raises:
        TypeError: If data is not bytes

    >>> fnv1a_64(b"")
    14695981039346656037

    >>> fnv1a_64(b"hello")
    11831194018420276491

    >>> fnv1a_64(b"Hello")
    7201466553693376363

    >>> fnv1a_64(b"world")
    5717881983045765875

    >>> fnv1a_64(b"The quick brown fox jumps over the lazy dog")
    17580284887202820368

    >>> fnv1a_64(b"a")
    12638187200555641996

    >>> fnv1a_64(b"abc")
    16654208175385433931

    >>> fnv1a_64(b"Python")
    4148801904339793143

    >>> fnv1a_64(b"FNV-1a")
    15319149270662077890

    >>> fnv1a_64(b"\\x00\\x00\\x00\\x00")
    5558979605539197941

    >>> fnv1a_64(b"test" * 100) != fnv1a_64(b"test" * 101)
    True
    """
    if not isinstance(data, bytes):
        msg = f"data must be bytes, not {type(data).__name__}"
        raise TypeError(msg)

    fnv_64_prime = 0x100000001B3
    hash_value = 0xCBF29CE484222325

    for byte in data:
        hash_value ^= byte
        hash_value = (hash_value * fnv_64_prime) & 0xFFFFFFFFFFFFFFFF

    return hash_value


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    test_data = b"Hello, World!"
    print(f"FNV-1a 32-bit hash of '{test_data.decode()}': {fnv1a_32(test_data)}")
    print(f"FNV-1a 64-bit hash of '{test_data.decode()}': {fnv1a_64(test_data)}")
