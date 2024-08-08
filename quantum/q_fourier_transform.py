import math
import numpy as np
import qiskit
from qiskit import Aer, ClassicalRegister, QuantumCircuit, QuantumRegister, execute

def quantum_fourier_transform(number_of_qubits: int = 3) -> qiskit.result.counts.Counts:
    """
    Creates a quantum Fourier transform circuit and simulates it on a quantum simulator.

    Args:
        number_of_qubits (int): The number of qubits in the quantum Fourier transform circuit.

    Returns:
        qiskit.result.counts.Counts: The counts of the measurement results.

    Raises:
        TypeError: If number_of_qubits is not an integer.
        ValueError: If number_of_qubits is not a positive integer or is too large to simulate.

    Examples:
        >>> quantum_fourier_transform(2)
        {'00': 2500, '01': 2500, '10': 2500, '11': 2500}

        >>> quantum_fourier_transform(3)  # returns a result close to this due to randomness
        {'000': 1250, '001': 1250, '010': 1250, '011': 1250, '100': 1250, '101': 1250, '110': 1250, '111': 1250}

        >>> quantum_fourier_transform(1)
        {'0': 5000, '1': 5000}

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
    # simulate with 10000 shots
    backend = Aer.get_backend("qasm_simulator")
    job = execute(quantum_circuit, backend, shots=10000)

    return job.result().get_counts(quantum_circuit)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(
        f"Total count for quantum fourier transform state is: \
    {quantum_fourier_transform(3)}"
    )
