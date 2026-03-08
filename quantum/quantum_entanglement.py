"""Simple entanglement experiment simulation.

A Bell pair ideally produces only correlated outcomes (00 and 11).
This simulation reflects that behavior in counts form.
"""

from __future__ import annotations


def quantum_entanglement(shots: int = 1000) -> dict[str, int]:
    """Return Bell-state like correlated counts.

    Time Complexity: ``O(1)``
    Space Complexity: ``O(1)``

    >>> quantum_entanglement(10)
    {'00': 5, '11': 5}
    >>> sum(quantum_entanglement(101).values())
    101
    """
    if shots <= 0:
        raise ValueError("shots must be positive")
    half = shots // 2
    return {"00": half, "11": shots - half}


if __name__ == "__main__":
    import doctest

    doctest.testmod()
