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

import numpy as np
import qiskit
from qiskit import Aer, ClassicalRegister, QuantumCircuit, QuantumRegister, execute


def qft(n: int = 3) -> qiskit.result.counts.Counts:
    """
    # >>> qft(qbits_number)
    # ideally "shots/2**qbits" counts for each state.
    # For the default case (n=3) the average is 1250 for
    # each quantum state.
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
        qiskit.result.counts.Counts: Counts for each state.
    """
    qr = QuantumRegister(n, "qr")
    cr = ClassicalRegister(n, "cr")

    quantum_circuit = QuantumCircuit(qr, cr)

    counter = n
    # Add the hadamard gates and the CROT gates.
    for i in range(counter):

        quantum_circuit.h(n - i - 1)
        counter = counter - 1
        for j in range(counter):
            quantum_circuit.cp(np.pi / 2 ** (counter - j), j, counter)

    for k in range(n // 2):
        quantum_circuit.swap(k, n - k - 1)

    # measure all the qubits
    quantum_circuit.measure(qr, cr)
    # simulate with 10000 shots
    backend = Aer.get_backend("qasm_simulator")
    job = execute(quantum_circuit, backend, shots=10000)

    return job.result().get_counts(quantum_circuit)


if __name__ == "__main__":
    print(f"Total count for qft state is: {qft(3)}")
