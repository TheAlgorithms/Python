"""
Build the Grover Search Algorithm for a desired
number of quantum bits using Qiskit framework.
This experiment runs in IBM Q simulator with 10000 shots.

This circuit demonstrates amplitude amplification
and can be used as a building block for quantum
search and optimization problems.

References:
https://en.wikipedia.org/wiki/Grover%27s_algorithm
https://qiskit.org/textbook/ch-algorithms/grover.html
"""

import math

try:
    import qiskit
    from qiskit import Aer, ClassicalRegister, QuantumCircuit, QuantumRegister, execute

    QISKIT_AVAILABLE = True
except ModuleNotFoundError:
    QISKIT_AVAILABLE = False


def grover_search(number_of_qubits: int = 2):
    """
    Build and simulate Grover's search algorithm.

    The oracle marks the |11...1> state.

    Args:
        number_of_qubits (int): number of qubits

    Returns:
        qiskit.result.counts.Counts: distribution counts.

    Raises:
        TypeError: if input is not integer
        ValueError: if invalid number of qubits
        ModuleNotFoundError: if qiskit is not installed

    >>> if QISKIT_AVAILABLE:  # doctest: +SKIP
    ...     counts = grover_search(2)
    ...     isinstance(counts, dict)
    True
    """
    if not QISKIT_AVAILABLE:
        raise ModuleNotFoundError(
            "qiskit is required for this algorithm. "
            "Install it with: pip install qiskit qiskit-aer"
        )

    if isinstance(number_of_qubits, str):
        raise TypeError("number of qubits must be an integer.")
    if number_of_qubits <= 0:
        raise ValueError("number of qubits must be > 0.")
    if math.floor(number_of_qubits) != number_of_qubits:
        raise ValueError("number of qubits must be exact integer.")
    if number_of_qubits > 10:
        raise ValueError("number of qubits too large to simulate (>10).")

    # Create registers
    qr = QuantumRegister(number_of_qubits, "qr")
    cr = ClassicalRegister(number_of_qubits, "cr")
    quantum_circuit = QuantumCircuit(qr, cr)

    # Step 1: Initialize superposition
    quantum_circuit.h(qr)

    # -------- Oracle (mark |11...1>) --------
    quantum_circuit.h(number_of_qubits - 1)
    quantum_circuit.mcx(list(range(number_of_qubits - 1)), number_of_qubits - 1)
    quantum_circuit.h(number_of_qubits - 1)

    # -------- Diffuser --------
    quantum_circuit.h(qr)
    quantum_circuit.x(qr)

    quantum_circuit.h(number_of_qubits - 1)
    quantum_circuit.mcx(list(range(number_of_qubits - 1)), number_of_qubits - 1)
    quantum_circuit.h(number_of_qubits - 1)

    quantum_circuit.x(qr)
    quantum_circuit.h(qr)

    # Measure all qubits
    quantum_circuit.measure(qr, cr)

    # Run simulator with 10000 shots
    backend = Aer.get_backend("qasm_simulator")
    job = execute(quantum_circuit, backend, shots=10000)

    return job.result().get_counts(quantum_circuit)


if __name__ == "__main__":
    if QISKIT_AVAILABLE:
        print(f"Total count for Grover search state is: {grover_search(3)}")
    else:
        print("qiskit not installed. Install with: pip install qiskit qiskit-aer")
