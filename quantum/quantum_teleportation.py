#!/usr/bin/env python3
"""
Build quantum teleportation circuit using three quantum bits
and 1 classical bit. The main idea is to send one qubit from
Alice to Bob using the entanglement properties. This experiment
run in IBM Q simulator with 1000 shots.
.
References:
https://en.wikipedia.org/wiki/Quantum_teleportation
https://qiskit.org/textbook/ch-algorithms/teleportation.html
"""

import numpy as np
import qiskit
from qiskit import Aer, ClassicalRegister, QuantumCircuit, QuantumRegister, execute


def quantum_teleportation(
    theta: float = np.pi / 2, phi: float = np.pi / 2, lam: float = np.pi / 2
) -> qiskit.result.counts.Counts:

    """
    # >>> quantum_teleportation()
    #{'00': 500, '11': 500} # ideally
    #      ┌─────────────────┐          ┌───┐
    #qr_0: ┤  U(π/2,π/2,π/2) ├───────■──┤ H ├─■─────────
    #      └──────┬───┬──────┘     ┌─┴─┐└───┘ │
    #qr_1: ───────┤ H ├─────────■──┤ X ├──────┼───■─────
    #             └───┘       ┌─┴─┐└───┘      │ ┌─┴─┐┌─┐
    #qr_2: ───────────────────┤ X ├───────────■─┤ X ├┤M├
    #                         └───┘             └───┘└╥┘
    #cr: 1/═══════════════════════════════════════════╩═
    Args:
        theta (float): Single qubit rotation U Gate theta parameter. Default to np.pi/2
        phi (float): Single qubit rotation U Gate phi parameter. Default to np.pi/2
        lam (float): Single qubit rotation U Gate lam parameter. Default to np.pi/2
    Returns:
        qiskit.result.counts.Counts: Teleported qubit counts.
    """

    qr = QuantumRegister(3, "qr")  # Define the number of quantum bits
    cr = ClassicalRegister(1, "cr")  # Define the number of classical bits

    quantum_circuit = QuantumCircuit(qr, cr)  # Define the quantum circuit.

    # Build the circuit
    quantum_circuit.u(theta, phi, lam, 0)  # Quantum State to teleport
    quantum_circuit.h(1)  # add hadamard gate
    quantum_circuit.cx(
        1, 2
    )  # add control gate with qubit 1 as control and 2 as target.
    quantum_circuit.cx(0, 1)
    quantum_circuit.h(0)
    quantum_circuit.cz(0, 2)  # add control z gate.
    quantum_circuit.cx(1, 2)

    quantum_circuit.measure([2], [0])  # measure the qubit.

    # Simulate the circuit using qasm simulator
    backend = Aer.get_backend("qasm_simulator")
    job = execute(quantum_circuit, backend, shots=1000)

    return job.result().get_counts(quantum_circuit)


if __name__ == "__main__":
    print(
        "Total count for teleported state is: "
        f"{quantum_teleportation(np.pi/2, np.pi/2, np.pi/2)}"
    )
