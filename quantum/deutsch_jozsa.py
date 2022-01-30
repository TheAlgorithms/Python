#!/usr/bin/env python3
"""
Deutsch-Josza Algorithm is one of the first examples of a quantum
algorithm that is exponentially faster than any possible deterministic
classical algorithm

Premise:
We are given a hidden Boolean function f,
which takes as input a string of bits, and returns either 0 or 1:

f({x0,x1,x2,...}) -> 0 or 1, where xn is 0 or 1

The property of the given Boolean function is that it is guaranteed to
either be balanced or constant. A constant function returns all 0's
or all 1's for any input, while a balanced function returns  0's for
exactly half of all inputs and 1's for the other half. Our task is to
determine whether the given function is balanced or constant.

References:
- https://en.wikipedia.org/wiki/Deutsch-Jozsa_algorithm
- https://qiskit.org/textbook/ch-algorithms/deutsch-jozsa.html
"""

import numpy as np
import qiskit as q


def dj_oracle(case: str, num_qubits: int) -> q.QuantumCircuit:
    """
    Returns a Quantum Circuit for the Oracle function.
    The circuit returned can represent balanced or constant function,
    according to the arguments passed
    """
    # This circuit has num_qubits+1 qubits: the size of the input,
    # plus one output qubit
    oracle_qc = q.QuantumCircuit(num_qubits + 1)

    # First, let's deal with the case in which oracle is balanced
    if case == "balanced":
        # First generate a random number that tells us which CNOTs to
        # wrap in X-gates:
        b = np.random.randint(1, 2**num_qubits)
        # Next, format 'b' as a binary string of length 'n', padded with zeros:
        b_str = format(b, f"0{num_qubits}b")
        # Next, we place the first X-gates. Each digit in our binary string
        # correspopnds to a qubit, if the digit is 0, we do nothing, if it's 1
        # we apply an X-gate to that qubit:
        for index, bit in enumerate(b_str):
            if bit == "1":
                oracle_qc.x(index)
        # Do the controlled-NOT gates for each qubit, using the output qubit
        # as the target:
        for index in range(num_qubits):
            oracle_qc.cx(index, num_qubits)
        # Next, place the final X-gates
        for index, bit in enumerate(b_str):
            if bit == "1":
                oracle_qc.x(index)

    # Case in which oracle is constant
    if case == "constant":
        # First decide what the fixed output of the oracle will be
        # (either always 0 or always 1)
        output = np.random.randint(2)
        if output == 1:
            oracle_qc.x(num_qubits)

    oracle_gate = oracle_qc.to_gate()
    oracle_gate.name = "Oracle"  # To show when we display the circuit
    return oracle_gate


def dj_algorithm(oracle: q.QuantumCircuit, num_qubits: int) -> q.QuantumCircuit:
    """
    Returns the complete Deustch-Jozsa Quantum Circuit,
    adding Input & Output registers and Hadamard & Measurement Gates,
    to the Oracle Circuit passed in arguments
    """
    dj_circuit = q.QuantumCircuit(num_qubits + 1, num_qubits)
    # Set up the output qubit:
    dj_circuit.x(num_qubits)
    dj_circuit.h(num_qubits)
    # And set up the input register:
    for qubit in range(num_qubits):
        dj_circuit.h(qubit)
    # Let's append the oracle gate to our circuit:
    dj_circuit.append(oracle, range(num_qubits + 1))
    # Finally, perform the H-gates again and measure:
    for qubit in range(num_qubits):
        dj_circuit.h(qubit)

    for i in range(num_qubits):
        dj_circuit.measure(i, i)

    return dj_circuit


def deutsch_jozsa(case: str, num_qubits: int) -> q.result.counts.Counts:
    """
    Main function that builds the circuit using other helper functions,
    runs the experiment 1000 times & returns the resultant qubit counts
    >>> deutsch_jozsa("constant", 3)
    {'000': 1000}
    >>> deutsch_jozsa("balanced", 3)
    {'111': 1000}
    """
    # Use Aer's qasm_simulator
    simulator = q.Aer.get_backend("qasm_simulator")

    oracle_gate = dj_oracle(case, num_qubits)
    dj_circuit = dj_algorithm(oracle_gate, num_qubits)

    # Execute the circuit on the qasm simulator
    job = q.execute(dj_circuit, simulator, shots=1000)

    # Return the histogram data of the results of the experiment.
    return job.result().get_counts(dj_circuit)


if __name__ == "__main__":
    print(f"Deutsch Jozsa - Constant Oracle: {deutsch_jozsa('constant', 3)}")
    print(f"Deutsch Jozsa - Balanced Oracle: {deutsch_jozsa('balanced', 3)}")
