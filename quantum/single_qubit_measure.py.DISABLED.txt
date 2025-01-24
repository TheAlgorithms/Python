#!/usr/bin/env python3
"""
Build a simple bare-minimum quantum circuit that starts with a single
qubit (by default, in state 0), runs the experiment 1000 times, and
finally prints the total count of the states finally observed.
Qiskit Docs: https://qiskit.org/documentation/getting_started.html
"""

import qiskit


def single_qubit_measure(
    qubits: int, classical_bits: int
) -> qiskit.result.counts.Counts:
    """
    >>> single_qubit_measure(1, 1)
    {'0': 1000}
    """
    # Use Aer's simulator
    simulator = qiskit.Aer.get_backend("aer_simulator")

    # Create a Quantum Circuit acting on the q register
    circuit = qiskit.QuantumCircuit(qubits, classical_bits)

    # Map the quantum measurement to the classical bits
    circuit.measure([0], [0])

    # Execute the circuit on the simulator
    job = qiskit.execute(circuit, simulator, shots=1000)

    # Return the histogram data of the results of the experiment.
    return job.result().get_counts(circuit)


if __name__ == "__main__":
    print(f"Total count for various states are: {single_qubit_measure(1, 1)}")
