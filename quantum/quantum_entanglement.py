#!/usr/bin/env python3
"""
Build a quantum circuit with pair or group of qubits to perform
quantum entanglement.
Quantum entanglement is a phenomenon observed at the quantum scale
where entangled particles stay connected (in some sense) so that
the actions performed on one of the particles affects the other,
no matter the distance between two particles.
"""

import qiskit


def quantum_entanglement(qubits: int = 2) -> qiskit.result.counts.Counts:
    """
    # >>> quantum_entanglement(2)
    # {'00': 500, '11': 500}
    #      ┌───┐     ┌─┐
    # q_0: ┤ H ├──■──┤M├───
    #      └───┘┌─┴─┐└╥┘┌─┐
    # q_1: ─────┤ X ├─╫─┤M├
    #           └───┘ ║ └╥┘
    # c: 2/═══════════╩══╩═
    #                 0  1
    Args:
        qubits (int): number of quibits to use. Defaults to 2
    Returns:
        qiskit.result.counts.Counts: mapping of states to its counts
    """
    classical_bits = qubits

    # Using Aer's qasm_simulator
    simulator = qiskit.Aer.get_backend("qasm_simulator")

    # Creating a Quantum Circuit acting on the q register
    circuit = qiskit.QuantumCircuit(qubits, classical_bits)

    # Adding a H gate on qubit 0 (now q0 in superposition)
    circuit.h(0)

    for i in range(1, qubits):
        # Adding CX (CNOT) gate
        circuit.cx(i - 1, i)

    # Mapping the quantum measurement to the classical bits
    circuit.measure(list(range(qubits)), list(range(classical_bits)))

    # Now measuring any one qubit would affect other qubits to collapse
    # their super position and have same state as the measured one.

    # Executing the circuit on the qasm simulator
    job = qiskit.execute(circuit, simulator, shots=1000)

    return job.result().get_counts(circuit)


if __name__ == "__main__":
    print(f"Total count for various states are: {quantum_entanglement(3)}")
