"""Classical simulation of a quantum NOT (Pauli-X) gate.

The Pauli-X gate maps :math:`|0\rangle` to :math:`|1\rangle` and vice-versa.
In this educational module we model qubits as classical bits (0 or 1).

Reference:
- https://en.wikipedia.org/wiki/Quantum_logic_gate#Pauli-X_gate
"""

from __future__ import annotations


def not_gate(qubit: int) -> int:
    """Flip a single qubit represented as 0 or 1.

    Time Complexity: ``O(1)``
    Space Complexity: ``O(1)``

    >>> not_gate(0)
    1
    >>> not_gate(1)
    0
    >>> not_gate(2)
    Traceback (most recent call last):
        ...
    ValueError: qubit must be either 0 or 1
    """
    if qubit not in (0, 1):
        raise ValueError("qubit must be either 0 or 1")
    return 1 - qubit


if __name__ == "__main__":
    import doctest

    doctest.testmod()
