"""BB84 key distribution simulation without external quantum dependencies.

The simulation models basis choices and bit transmission in a classical way:
when Alice and Bob choose different bases, Bob's bit is random.
"""

from __future__ import annotations

import random


def bb84(key_len: int = 8, seed: int | None = None) -> str:
    """Generate a BB84-style shared key.

    Time Complexity: ``O(key_len)``
    Space Complexity: ``O(key_len)``

    >>> bb84(8, seed=0)
    '11100000'
    >>> len(bb84(16, seed=2))
    16
    """
    if key_len <= 0:
        raise ValueError("key_len must be positive")

    rng = random.Random(seed)
    key_bits: list[str] = []

    while len(key_bits) < key_len:
        alice_basis = rng.randint(0, 1)
        alice_bit = rng.randint(0, 1)
        bob_basis = rng.randint(0, 1)

        measured = alice_bit if alice_basis == bob_basis else rng.randint(0, 1)

        if alice_basis == bob_basis:
            key_bits.append(str(measured))

    return "".join(key_bits)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
