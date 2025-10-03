"""
Build the quantum fourier transform (QFT) for a desired
number of quantum bits using the Qiskit framework. This
experiment runs in the IBM Q simulator with 10000 shots.
This circuit can be used as a building block to design
Shor's algorithm in quantum computing, as well as
quantum phase estimation among others.

References:
https://en.wikipedia.org/wiki/Quantum_Fourier_transform
https://qiskit.org/textbook/ch-algorithms/quantum-fourier-transform.html
"""

import math
import numpy as np
import qiskit
from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister
from qiskit_aer import AerSimulator

def quantum_fourier_transform(number_of_qubits: int = 3) -> qiskit.result.counts.Counts:
    """
    Build a quantum fourier transform circuit for a given number of qubits and simulate it.

    Args:
        number_of_qubits (int): Number of qubits for the QFT.

    Returns:
        qiskit.result.counts.Counts: The measurement result counts from the quantum circuit simulation.

    Examples:
    >>> result = quantum_fourier_transform(2)
    >>> total_counts = sum(result.values())
    >>> total_counts == 10000
    True
    >>> set(result.keys()) == {'00', '01', '10', '11'}
    True

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

    # Apply the quantum Fourier transform
    for i in range(number_of_qubits):
        # Apply Hadamard gate to qubit i
        quantum_circuit.h(i)
        
        # Apply controlled rotation gates
        for j in range(i + 1, number_of_qubits):
            angle = np.pi / (2 ** (j - i))
            quantum_circuit.cp(angle, j, i)

    # Apply SWAP gates to reverse the order of qubits
    for i in range(number_of_qubits // 2):
        quantum_circuit.swap(i, number_of_qubits - i - 1)

    # Measure all the qubits
    quantum_circuit.measure(qr, cr)
    
    # Simulate with 10000 shots using AerSimulator
    simulator = AerSimulator()
    job = simulator.run(quantum_circuit, shots=10000)
    
    return job.result().get_counts(quantum_circuit)


if __name__ == "__main__":
    print(
        f"Total count for quantum fourier transform state is: \
    {quantum_fourier_transform(3)}"
    )