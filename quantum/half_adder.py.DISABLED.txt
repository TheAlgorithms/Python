# DISABLED!!
#!/usr/bin/env python3
"""
Build a half-adder quantum circuit that takes two bits as input,
encodes them into qubits, then runs the half-adder circuit calculating
the sum and carry qubits, observed over 1000 runs of the experiment
.

References:
https://en.wikipedia.org/wiki/Adder_(electronics)
https://qiskit.org/textbook/ch-states/atoms-computation.html#4.2-Remembering-how-to-add-
"""

import qiskit


def half_adder(bit0: int, bit1: int) -> qiskit.result.counts.Counts:
    """
    >>> half_adder(0, 0)
    {'00': 1000}
    >>> half_adder(0, 1)
    {'01': 1000}
    >>> half_adder(1, 0)
    {'01': 1000}
    >>> half_adder(1, 1)
    {'10': 1000}
    """
    # Use Aer's simulator
    simulator = qiskit.Aer.get_backend("aer_simulator")

    qc_ha = qiskit.QuantumCircuit(4, 2)
    # encode inputs in qubits 0 and 1
    if bit0 == 1:
        qc_ha.x(0)
    if bit1 == 1:
        qc_ha.x(1)
    qc_ha.barrier()

    # use cnots to write XOR of the inputs on qubit2
    qc_ha.cx(0, 2)
    qc_ha.cx(1, 2)

    # use ccx / toffoli gate to write AND of the inputs on qubit3
    qc_ha.ccx(0, 1, 3)
    qc_ha.barrier()

    # extract outputs
    qc_ha.measure(2, 0)  # extract XOR value
    qc_ha.measure(3, 1)  # extract AND value

    # Execute the circuit on the qasm simulator
    job = qiskit.execute(qc_ha, simulator, shots=1000)

    # Return the histogram data of the results of the experiment
    return job.result().get_counts(qc_ha)


if __name__ == "__main__":
    counts = half_adder(1, 1)
    print(f"Half Adder Output Qubit Counts: {counts}")
