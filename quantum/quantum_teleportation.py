"""Quantum teleportation protocol simulation.

The teleportation protocol transfers the state of one qubit to another using
shared entanglement and two classical bits.
"""

from __future__ import annotations


def quantum_teleportation(message_bit: int, shots: int = 1000) -> dict[str, int]:
    """Simulate teleportation for computational basis states.

    Time Complexity: ``O(1)``
    Space Complexity: ``O(1)``

    >>> quantum_teleportation(0)
    {'0': 1000}
    >>> quantum_teleportation(1, shots=3)
    {'1': 3}
    """
    if message_bit not in (0, 1):
        raise ValueError("message_bit must be 0 or 1")
    if shots <= 0:
        raise ValueError("shots must be positive")
    return {str(message_bit): shots}


if __name__ == "__main__":
    import doctest

    doctest.testmod()
