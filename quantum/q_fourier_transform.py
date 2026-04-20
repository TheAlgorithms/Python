import numpy as np
from qiskit import Aer, ClassicalRegister, QuantumCircuit, QuantumRegister, execute


def quantum_fourier_transform(number_of_qubits: int = 3) -> dict:
    """
    Build and simulate the Quantum Fourier Transform (QFT) circuit
    for a given number of qubits using the Qiskit framework.

    Args:
        number_of_qubits (int): The number of qubits for the QFT circuit.

    Returns:
        dict: A dictionary containing the counts of measurement results.

    Raises:
        ValueError: If the number of qubits is less than or equal to 0,
                    greater than 10, or not an integer.
        TypeError: If the input is not an integer.
    """
    if not isinstance(number_of_qubits, int):
        raise TypeError("Number of qubits must be an integer.")
    if number_of_qubits <= 0:
        raise ValueError("Number of qubits must be > 0.")
    if number_of_qubits > 10:
        raise ValueError("Number of qubits too large to simulate (>10).")

    qr = QuantumRegister(number_of_qubits, "qr")
    cr = ClassicalRegister(number_of_qubits, "cr")
    quantum_circuit = QuantumCircuit(qr, cr)

    # Apply the QFT circuit
    for i in range(number_of_qubits):
        quantum_circuit.h(i)
        for j in range(i + 1, number_of_qubits):
            quantum_circuit.cp(np.pi / 2 ** (j - i), j, i)

    # Swap the qubits
    for i in range(number_of_qubits // 2):
        quantum_circuit.swap(i, number_of_qubits - i - 1)

    # Measure all qubits
    quantum_circuit.measure(qr, cr)

    # Simulate the circuit with 10000 shots
    backend = Aer.get_backend("qasm_simulator")
    job = execute(quantum_circuit, backend, shots=10000)
    result = job.result()

    return result.get_counts(quantum_circuit)


if __name__ == "__main__":
    result_counts = quantum_fourier_transform(3)
    print(f"Total count for quantum fourier transform state is: {result_counts}")
