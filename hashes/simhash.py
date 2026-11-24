"""
SimHash (Charikar's Locality-Sensitive Hashing for angular/cosine similarity).

Reference:
Moses S. Charikar (2002), "Similarity estimation techniques from rounding algorithms",
STOC '02: Proceedings of the 34th Annual ACM Symposium on Theory of Computing.
https://en.wikipedia.org/wiki/SimHash
"""

from __future__ import annotations

import hashlib
import re
from collections.abc import Iterable

_MAX_BIT_WIDTH = 512


def tokenize(text: str) -> list[str]:
    """
    Extract lowercase alphanumeric tokens from text.

    >>> tokenize("SimHash: Fast, simple LSH!")
    ['simhash', 'fast', 'simple', 'lsh']
    >>> tokenize("")
    []
    """
    return re.findall(r"\w+", text.lower())


def _hash_token(token: str, bit_width: int) -> int:
    # Use blake2b instead of built-in hash() so fingerprints are deterministic
    # across Python processes regardless of PYTHONHASHSEED.
    digest_bytes = (bit_width + 7) // 8
    raw = hashlib.blake2b(token.encode("utf-8"), digest_size=digest_bytes).digest()
    mask = (1 << bit_width) - 1
    return int.from_bytes(raw, "big") & mask


def _validate_bit_width(bit_width: int) -> None:
    if not 1 <= bit_width <= _MAX_BIT_WIDTH:
        msg = f"bit_width must be between 1 and {_MAX_BIT_WIDTH}, got {bit_width}"
        raise ValueError(msg)


def simhash(
    features: Iterable[str | tuple[str, float]],
    bit_width: int = 64,
) -> int:
    """
    Compute the SimHash fingerprint of unweighted or weighted features.

    >>> h1 = simhash(tokenize("the quick brown fox jumps over the lazy dog"))
    >>> h2 = simhash(tokenize("the quick brown fox leaps over the lazy dog"))
    >>> h3 = simhash(tokenize("quantum chromodynamics and lattice gauge theory"))
    >>> hamming_distance(h1, h2) < hamming_distance(h1, h3)
    True
    >>> simhash([("apple", 3.0), ("banana", 1.0)], bit_width=32) < (1 << 32)
    True
    >>> simhash([])
    Traceback (most recent call last):
        ...
    ValueError: features must not be empty
    >>> simhash(["a"], bit_width=0)
    Traceback (most recent call last):
        ...
    ValueError: bit_width must be between 1 and 512, got 0
    """
    _validate_bit_width(bit_width)
    weights = [0.0] * bit_width
    has_features = False

    for item in features:
        has_features = True
        token, weight = (item, 1.0) if isinstance(item, str) else item
        token_hash = _hash_token(token, bit_width)
        for bit_index in range(bit_width):
            if (token_hash >> bit_index) & 1:
                weights[bit_index] += weight
            else:
                weights[bit_index] -= weight

    if not has_features:
        raise ValueError("features must not be empty")

    fingerprint = 0
    for bit_index, total_weight in enumerate(weights):
        if total_weight >= 0.0:
            fingerprint |= 1 << bit_index
    return fingerprint


def hamming_distance(hash_a: int, hash_b: int) -> int:
    """
    Return the Hamming distance between two non-negative integer hashes.

    >>> hamming_distance(0b1010, 0b1100)
    2
    >>> hamming_distance(42, 42)
    0
    >>> hamming_distance(-1, 0)
    Traceback (most recent call last):
        ...
    ValueError: hash values must be non-negative
    """
    if hash_a < 0 or hash_b < 0:
        raise ValueError("hash values must be non-negative")
    return (hash_a ^ hash_b).bit_count()


def similarity(hash_a: int, hash_b: int, bit_width: int = 64) -> float:
    """
    Return normalized SimHash similarity in [0.0, 1.0].

    >>> similarity(0b1010, 0b1010, bit_width=4)
    1.0
    >>> similarity(0b1111, 0b0000, bit_width=4)
    0.0
    >>> similarity(0b1010, 0b1100, bit_width=4)
    0.5
    >>> similarity(16, 0, bit_width=4)
    Traceback (most recent call last):
        ...
    ValueError: hash values must fit within bit_width=4
    """
    _validate_bit_width(bit_width)
    upper_bound = 1 << bit_width
    if not (0 <= hash_a < upper_bound and 0 <= hash_b < upper_bound):
        msg = f"hash values must fit within bit_width={bit_width}"
        raise ValueError(msg)
    return 1.0 - hamming_distance(hash_a, hash_b) / bit_width


if __name__ == "__main__":
    import doctest

    doctest.testmod()
