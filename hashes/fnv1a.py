"""
FNV-1a (Fowler-Noll-Vo) is a non-cryptographic hash function created by
Glenn Fowler, Landon Curt Noll, and Kiem-Phong Vo.

The FNV-1a variant provides better avalanche characteristics (bit changes
distribute more uniformly) compared to the original FNV-1.

Key properties:
- Fast computation
- Good distribution
- Non-cryptographic (not suitable for security purposes)
- Widely used in hash tables and checksums

Algorithm:
    hash = FNV_offset_basis
    for each byte in data:
        hash = hash XOR byte
        hash = hash * FNV_prime

FNV-1a 32-bit:
    FNV_offset_basis = 2166136261 (0x811c9dc5)
    FNV_prime = 16777619 (0x01000193)

FNV-1a 64-bit:
    FNV_offset_basis = 14695981039346656037 (0xcbf29ce484222325)
    FNV_prime = 1099511628211 (0x100000001b3)

Source: http://www.isthe.com/chongo/tech/comp/fnv/
"""


def fnv1a_32(data: str) -> int:
    """
    Implementation of 32-bit FNV-1a hash algorithm.

    Args:
        data: Input string to hash

    Returns:
        32-bit hash value as integer

    Examples:
        >>> fnv1a_32('Hello')
        4116459851
        >>> fnv1a_32('World')
        3714116915
        >>> fnv1a_32('Algorithms')
        3235099003
        >>> fnv1a_32('')
        2166136261
        >>> fnv1a_32('The quick brown fox jumps over the lazy dog')
        76545936
        >>> fnv1a_32('a')
        3826002220
        >>> fnv1a_32('ab')
        1294271946
        >>> fnv1a_32('abc')
        440920331

    Test with same input produces same output:
        >>> fnv1a_32('test') == fnv1a_32('test')
        True

    Test different inputs produce different outputs:
        >>> fnv1a_32('test') != fnv1a_32('Test')
        True
    """
    # FNV-1a 32-bit parameters
    fnv_offset_basis = 0x811C9DC5  # 2166136261
    fnv_prime = 0x01000193  # 16777619

    hash_value = fnv_offset_basis

    for byte in data.encode("utf-8"):
        hash_value ^= byte  # XOR with byte
        hash_value *= fnv_prime  # Multiply by FNV prime
        hash_value &= 0xFFFFFFFF  # Keep it 32-bit

    return hash_value


def fnv1a_64(data: str) -> int:
    """
    Implementation of 64-bit FNV-1a hash algorithm.

    Args:
        data: Input string to hash

    Returns:
        64-bit hash value as integer

    Examples:
        >>> fnv1a_64('Hello')
        7201466553693376363
        >>> fnv1a_64('World')
        1088154518318865747
        >>> fnv1a_64('Algorithms')
        2924617064648692923
        >>> fnv1a_64('')
        14695981039346656037
        >>> fnv1a_64('The quick brown fox jumps over the lazy dog')
        17580284887202820368
        >>> fnv1a_64('a')
        12638187200555641996
        >>> fnv1a_64('ab')
        620445648566982762
        >>> fnv1a_64('abc')
        16654208175385433931

    Test with same input produces same output:
        >>> fnv1a_64('test') == fnv1a_64('test')
        True

    Test different inputs produce different outputs:
        >>> fnv1a_64('test') != fnv1a_64('Test')
        True
    """
    # FNV-1a 64-bit parameters
    fnv_offset_basis = 0xCBF29CE484222325  # 14695981039346656037
    fnv_prime = 0x100000001B3  # 1099511628211

    hash_value = fnv_offset_basis

    for byte in data.encode("utf-8"):
        hash_value ^= byte  # XOR with byte
        hash_value *= fnv_prime  # Multiply by FNV prime
        hash_value &= 0xFFFFFFFFFFFFFFFF  # Keep it 64-bit

    return hash_value


if __name__ == "__main__":
    import doctest

    doctest.testmod()
