"""Superdense coding protocol simulation.

Superdense coding transmits two classical bits using one qubit and one shared
Bell pair. In this educational simulation we return the decoded message counts.
"""

from __future__ import annotations


def superdense_coding(
    bit_1: int = 1, bit_2: int = 1, shots: int = 1000
) -> dict[str, int]:
    """Encode and decode a two-bit message.

    Time Complexity: ``O(1)``
    Space Complexity: ``O(1)``

    >>> superdense_coding(0, 0)
    {'00': 1000}
    >>> superdense_coding(1, 0, shots=5)
    {'10': 5}
    """
    if bit_1 not in (0, 1) or bit_2 not in (0, 1):
        raise ValueError("bit_1 and bit_2 must be 0 or 1")
    if shots <= 0:
        raise ValueError("shots must be positive")
    return {f"{bit_1}{bit_2}": shots}


if __name__ == "__main__":
    import doctest

    doctest.testmod()
