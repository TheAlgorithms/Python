"""MinHash signatures for estimating Jaccard similarity.

MinHash uses the minimum value produced by several independent hash functions
to turn a set into a compact signature. The fraction of equal positions in two
signatures is an unbiased estimator of their Jaccard similarity.

References:
    https://en.wikipedia.org/wiki/MinHash
    https://www.cs.princeton.edu/courses/archive/spring13/cos598C/broder.pdf
"""

from __future__ import annotations

import hashlib
from collections.abc import Iterable, Sequence


def _token_hash(token: str, seed: int, permutation: int) -> int:
    """Return a deterministic 64-bit hash for one token and permutation."""
    payload = f"{seed}:{permutation}:{token}".encode()
    return int.from_bytes(hashlib.blake2b(payload, digest_size=8).digest(), "big")


def min_hash(
    tokens: Iterable[str], num_perm: int = 128, seed: int = 0
) -> tuple[int, ...]:
    """Build a MinHash signature for an iterable of tokens.

    ``tokens`` is treated as a set: repeated tokens do not affect the
    signature. ``num_perm`` controls the accuracy/size trade-off.

    >>> first = min_hash({"a", "b", "c"}, num_perm=64)
    >>> second = min_hash({"a", "b", "d"}, num_perm=64)
    >>> len(first) == len(second) == 64
    True
    >>> 0.0 <= estimated_jaccard(first, second) <= 1.0
    True
    >>> min_hash({"a", "b"}, num_perm=8) == min_hash({"a", "b"}, num_perm=8)
    True
    """
    if num_perm <= 0:
        raise ValueError("num_perm must be positive")

    unique_tokens = set(tokens)
    if not unique_tokens:
        raise ValueError("tokens must contain at least one item")

    return tuple(
        min(_token_hash(token, seed, permutation) for token in unique_tokens)
        for permutation in range(num_perm)
    )


def estimated_jaccard(first: Sequence[int], second: Sequence[int]) -> float:
    """Estimate Jaccard similarity from two MinHash signatures.

    >>> estimated_jaccard((1, 2, 3), (1, 4, 3))
    0.6666666666666666
    >>> estimated_jaccard((1, 2), (1,))
    Traceback (most recent call last):
        ...
    ValueError: signatures must have the same length
    """
    if len(first) != len(second):
        raise ValueError("signatures must have the same length")
    if not first:
        raise ValueError("signatures must not be empty")

    return sum(left == right for left, right in zip(first, second)) / len(first)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
