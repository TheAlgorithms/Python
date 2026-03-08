"""Single-qubit measurement simulation.

This module starts from the default :math:`|0\rangle` state and measures it.
Without any gate applied first, all measurements produce ``0``.
"""

from __future__ import annotations


def single_qubit_measure(
    qubits: int = 1, classical_bits: int = 1, shots: int = 1000
) -> dict[str, int]:
    """Return measurement counts for an unmodified qubit state.

    Time Complexity: ``O(1)``
    Space Complexity: ``O(classical_bits)``

    >>> single_qubit_measure(1, 1)
    {'0': 1000}
    >>> single_qubit_measure(1, 2, shots=5)
    {'00': 5}
    """
    if qubits < 1 or classical_bits < 1 or shots < 1:
        raise ValueError("qubits, classical_bits and shots must be positive")
    return {"0" * classical_bits: shots}


if __name__ == "__main__":
    import doctest

    doctest.testmod()
