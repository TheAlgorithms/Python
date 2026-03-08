"""Classical simulation of the Deutsch-Jozsa decision problem.

Given an oracle promised to be either constant or balanced, determine which
class it belongs to.
"""

from __future__ import annotations

from collections.abc import Callable


def deutsch_jozsa(oracle: Callable[[str], int], num_qubits: int) -> str:
    """Classify an oracle as ``constant`` or ``balanced``.

    Time Complexity: ``O(2**num_qubits)``
    Space Complexity: ``O(1)`` excluding oracle storage.

    >>> deutsch_jozsa(lambda _: 0, 3)
    'constant'
    >>> deutsch_jozsa(lambda bits: int(bits[0] == '1'), 2)
    'balanced'
    """
    if num_qubits <= 0:
        raise ValueError("num_qubits must be positive")

    ones = 0
    total = 1 << num_qubits
    for value in range(total):
        bitstring = format(value, f"0{num_qubits}b")
        output = oracle(bitstring)
        if output not in (0, 1):
            raise ValueError("oracle outputs must be 0 or 1")
        ones += output

    if ones in (0, total):
        return "constant"
    if ones * 2 == total:
        return "balanced"
    raise ValueError("oracle must be promised constant or balanced")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
