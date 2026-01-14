"""
Grover's Search Algorithm implementation using Qiskit.

Grover's algorithm is a quantum algorithm for searching an unsorted database
with quadratic speedup over classical algorithms.

Wikipedia:
https://en.wikipedia.org/wiki/Grover%27s_algorithm
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def grover_search(shots: int = 1024) -> dict[str, int]:
    """
    Runs Grover's search algorithm for 2 qubits and returns measurement results.

    The oracle marks the |11> state.

    Args:
        shots (int): Number of simulation shots.

    Returns:
        dict[str, int]: Measurement counts.

    Example:
    >>> result = grover_search(100)
    >>> isinstance(result, dict)
    True
    """

    n = 2
    qc = QuantumCircuit(n, n)

    # Initialize superposition
    qc.h(range(n))

    # Oracle marking |11>
    qc.cz(0, 1)

    # Diffuser
    qc.h(range(n))
    qc.x(range(n))
    qc.h(1)
    qc.cx(0, 1)
    qc.h(1)
    qc.x(range(n))
    qc.h(range(n))

    # Measurement
    qc.measure(range(n), range(n))

    # Run on simulator
    backend = AerSimulator()
    compiled = transpile(qc, backend)
    result = backend.run(compiled, shots=shots).result()
    counts = result.get_counts()

    return counts


if __name__ == "__main__":
    print(grover_search())
