"""Pseudo-quantum random bitstring generator.

In an actual quantum device, superposition + measurement can provide unbiased
randomness. Here, we provide a deterministic-seed educational equivalent.
"""

from __future__ import annotations

import random


def quantum_random(num_bits: int = 8, seed: int | None = None) -> str:
    """Generate a random bitstring.

    Time Complexity: ``O(num_bits)``
    Space Complexity: ``O(num_bits)``

    >>> quantum_random(8, seed=0)
    '11011111'
    >>> len(quantum_random(16, seed=7))
    16
    """
    if num_bits <= 0:
        raise ValueError("num_bits must be positive")

    rng = random.Random(seed)
    return "".join(str(rng.randint(0, 1)) for _ in range(num_bits))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
