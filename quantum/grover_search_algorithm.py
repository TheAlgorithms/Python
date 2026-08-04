import importlib.util
import math


def grover_search(number_of_qubits: int = 2):
    """
    Build and simulate Grover's search algorithm.
    """

    if importlib.util.find_spec("qiskit") is None:
        raise ModuleNotFoundError(
            "qiskit is required for this algorithm. "
            "Install it with: pip install qiskit qiskit-aer"
        )

    from qiskit import Aer, ClassicalRegister, QuantumCircuit, QuantumRegister, execute

    if isinstance(number_of_qubits, str):
        raise TypeError("number of qubits must be an integer.")
    if number_of_qubits <= 0:
        raise ValueError("number of qubits must be > 0.")
    if math.floor(number_of_qubits) != number_of_qubits:
        raise ValueError("number of qubits must be exact integer.")
    if number_of_qubits > 10:
        raise ValueError("number of qubits too large to simulate (>10).")

    qr = QuantumRegister(number_of_qubits, "qr")
    cr = ClassicalRegister(number_of_qubits, "cr")
    quantum_circuit = QuantumCircuit(qr, cr)

    quantum_circuit.h(qr)

    quantum_circuit.h(number_of_qubits - 1)
    quantum_circuit.mcx(list(range(number_of_qubits - 1)), number_of_qubits - 1)
    quantum_circuit.h(number_of_qubits - 1)

    quantum_circuit.h(qr)
    quantum_circuit.x(qr)

    quantum_circuit.h(number_of_qubits - 1)
    quantum_circuit.mcx(list(range(number_of_qubits - 1)), number_of_qubits - 1)
    quantum_circuit.h(number_of_qubits - 1)

    quantum_circuit.x(qr)
    quantum_circuit.h(qr)

    quantum_circuit.measure(qr, cr)

    backend = Aer.get_backend("qasm_simulator")
    job = execute(quantum_circuit, backend, shots=10000)

    return job.result().get_counts(quantum_circuit)
