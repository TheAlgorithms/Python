"""
Build the quantum fourier transform (qft) for a desire
number of quantum bits using Qiskit framework. This
experiment run in IBM Q simulator with 10000 shots.
This circuit can be use as a building block to design
the Shor's algorithm in quantum computing. As well as,
quantum phase estimation among others.
.
References:
https://en.wikipedia.org/wiki/Quantum_Fourier_transform
https://qiskit.org/textbook/ch-algorithms/quantum-fourier-transform.html
"""

import math

import numpy as np
import qiskit
from qiskit import Aer, ClassicalRegister, QuantumCircuit, QuantumRegister, execute


def quantum_fourier_transform(number_of_qubits: int = 3) -> qiskit.result.counts.Counts:
    """
    # >>> quantum_fourier_transform(2)
    # {'00': 2500, '01': 2500, '11': 2500, '10': 2500}
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
        n : number of qubits
    Returns:
        qiskit.result.counts.Counts: distribute counts.

    >>> quantum_fourier_transform(2)
    {'00': 2500, '01': 2500, '10': 2500, '11': 2500}
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
    if type(number_of_qubits) == str:
        raise TypeError("number of qubits must be a integer.")
    if not number_of_qubits > 0:
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
    # simulate with 10000 shots
    backend = Aer.get_backend("qasm_simulator")
    job = execute(quantum_circuit, backend, shots=10000)

    return job.result().get_counts(quantum_circuit)


if __name__ == "__main__":
    print(
        f"Total count for quantum fourier transform state is: \
    {quantum_fourier_transform(3)}"
    )
