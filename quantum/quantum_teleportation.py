#!/usr/bin/env python3
"""
Build quantum teleportation circuit using three quantum bits
and 1 classical bit. The main idea is to send one qubit from
Alice to Bob using the entanglement propertie. This experiment
run in IBM Q simulator with 1000 shots.
.
References:
https://en.wikipedia.org/wiki/Quantum_teleportation
https://qiskit.org/textbook/ch-algorithms/teleportation.html
"""

import numpy as np
from qiskit import Aer, ClassicalRegister, QuantumCircuit, QuantumRegister, execute


def quantum_teleportation(
    theta: float = np.pi / 2, phi: float = np.pi / 2, lam: float = np.pi / 2
):

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
        theta (float): Single qubit rotation U Gate theta parameter. Defaults to np.pi/2
        phi (float): Single qubit rotation U Gate phi parameter. Defaul to np.pi/2
        lam (float): Single qubit rotation U Gate lam parameter. Defaul to np.pi/2
    Returns:
        qiskit.result.counts.Counts: Teleported qubit counts.
    """

    qr = QuantumRegister(3, "qr")  # Define the number of quantum bits
    cr = ClassicalRegister(1, "cr")  # Define the number of classical bits

    qc = QuantumCircuit(qr, cr)  # Define the quantum circuit.

    # Build the circuit
    qc.u(theta, phi, lam, 0)  # Quantum State to teleport
    qc.h(1)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.h(0)
    qc.cz(0, 2)
    qc.cx(1, 2)

    qc.measure([2], [0])

    # Simulate the circuit using qasm simulator
    backend = Aer.get_backend("qasm_simulator")
    job = execute(qc, backend, shots=1000)

    return job.result().get_counts(qc)


if __name__ == "__main__":
    print(
        f"Total count for teleported state is: {quantum_teleportation(np.pi/2, np.pi/2, np.pi/2)}"
    )
