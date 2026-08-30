"""
Build the quantum Fourier transform (QFT) for a desired
number of qubits using the Qiskit framework.

This circuit can be used as a building block to design
Shor's algorithm in quantum computing, as well as
quantum phase estimation, among others.

The circuit is simulated with Qiskit's built-in, pure-Python
``BasicSimulator`` (no compiled ``qiskit-aer`` backend required),
so it runs anywhere Qiskit itself installs.

References:
https://en.wikipedia.org/wiki/Quantum_Fourier_transform
https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.QFT
"""

import math

import numpy as np
import qiskit
from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister, transpile
from qiskit.providers.basic_provider import BasicSimulator


def quantum_fourier_transform(number_of_qubits: int = 3) -> qiskit.result.counts.Counts:
    """
    Build and simulate the quantum Fourier transform applied to the all-zero
    state ``|0...0>``.  The QFT maps ``|0...0>`` to a uniform superposition, so
    every computational-basis outcome is (up to shot noise) equally likely.

    # quantum circuit for number_of_qubits = 3:
                                               ┌───┐
    qr_0: ──────■──────────────────────■───────┤ H ├─X─
                │                ┌───┐ │P(π/2) └───┘ │
    qr_1: ──────┼────────■───────┤ H ├─■─────────────┼─
          ┌───┐ │P(π/4)  │P(π/2) └───┘               │
    qr_2: ┤ H ├─■────────■───────────────────────────X─
          └───┘
    cr: 3/═════════════════════════════════════════════

    Args:
        number_of_qubits : number of qubits

    Returns:
        qiskit.result.counts.Counts: measurement counts over 10000 shots.

    The simulation is seeded, so the set of observed outcomes is reproducible:

    >>> counts = quantum_fourier_transform(2)
    >>> sorted(counts)
    ['00', '01', '10', '11']
    >>> sum(counts.values())
    10000
    >>> quantum_fourier_transform(-1)
    Traceback (most recent call last):
        ...
    ValueError: number of qubits must be > 0.
    >>> quantum_fourier_transform('a')
    Traceback (most recent call last):
        ...
    TypeError: number of qubits must be a integer.
    >>> quantum_fourier_transform(100)
    Traceback (most recent call last):
        ...
    ValueError: number of qubits too large to simulate(>10).
    >>> quantum_fourier_transform(0.5)
    Traceback (most recent call last):
        ...
    ValueError: number of qubits must be exact integer.
    """
    if isinstance(number_of_qubits, str):
        raise TypeError("number of qubits must be a integer.")
    if number_of_qubits <= 0:
        raise ValueError("number of qubits must be > 0.")
    if math.floor(number_of_qubits) != number_of_qubits:
        raise ValueError("number of qubits must be exact integer.")
    if number_of_qubits > 10:
        raise ValueError("number of qubits too large to simulate(>10).")

    qr = QuantumRegister(number_of_qubits, "qr")
    cr = ClassicalRegister(number_of_qubits, "cr")

    quantum_circuit = QuantumCircuit(qr, cr)

    counter = number_of_qubits

    for i in range(counter):
        quantum_circuit.h(number_of_qubits - i - 1)
        counter -= 1
        for j in range(counter):
            quantum_circuit.cp(np.pi / 2 ** (counter - j), j, counter)

    for k in range(number_of_qubits // 2):
        quantum_circuit.swap(k, number_of_qubits - k - 1)

    # measure all the qubits
    quantum_circuit.measure(qr, cr)

    # simulate with 10000 shots on the pure-Python BasicSimulator; seed the run
    # so the observed outcomes are reproducible for the doctest above.
    backend = BasicSimulator()
    transpiled_circuit = transpile(quantum_circuit, backend)
    job = backend.run(transpiled_circuit, shots=10000, seed_simulator=42)

    return job.result().get_counts(quantum_circuit)


if __name__ == "__main__":
    print(
        f"Total count for quantum fourier transform state is: \
    {quantum_fourier_transform(3)}"
    )
