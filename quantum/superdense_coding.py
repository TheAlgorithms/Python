"""
Build the superdense coding protocol. This quantum
circuit can send two classical bits using one quantum
bit. This circuit is designed using the Qiskit
framework. This experiment run in IBM Q simulator
with 1000 shots.
.
References:
https://qiskit.org/textbook/ch-algorithms/superdense-coding.html
https://en.wikipedia.org/wiki/Superdense_coding
"""

import math

import qiskit
from qiskit import Aer, ClassicalRegister, QuantumCircuit, QuantumRegister, execute


def superdense_coding(bit_1: int = 1, bit_2: int = 1) -> qiskit.result.counts.Counts:
    """
    The input refer to the classical message
    that you wants to send. {'00','01','10','11'}
    result for default values: {11: 1000}
               ┌───┐          ┌───┐
    qr_0: ─────┤ X ├──────────┤ X ├─────
          ┌───┐└─┬─┘┌───┐┌───┐└─┬─┘┌───┐
    qr_1: ┤ H ├──■──┤ X ├┤ Z ├──■──┤ H ├
          └───┘     └───┘└───┘     └───┘
    cr: 2/══════════════════════════════
    Args:
        bit_1: bit 1 of classical information to send.
        bit_2: bit 2 of classical information to send.
    Returns:
        qiskit.result.counts.Counts: counts of send state.
    >>> superdense_coding(0,0)
    {'00': 1000}
    >>> superdense_coding(0,1)
    {'01': 1000}
    >>> superdense_coding(-1,0)
    Traceback (most recent call last):
        ...
    ValueError: inputs must be positive.
    >>> superdense_coding(1,'j')
    Traceback (most recent call last):
        ...
    TypeError: inputs must be integers.
    >>> superdense_coding(1,0.5)
    Traceback (most recent call last):
        ...
    ValueError: inputs must be exact integers.
    >>> superdense_coding(2,1)
    Traceback (most recent call last):
        ...
    ValueError: inputs must be less or equal to 1.
    """
    if (type(bit_1) == str) or (type(bit_2) == str):
        raise TypeError("inputs must be integers.")
    if (bit_1 < 0) or (bit_2 < 0):
        raise ValueError("inputs must be positive.")
    if (math.floor(bit_1) != bit_1) or (math.floor(bit_2) != bit_2):
        raise ValueError("inputs must be exact integers.")
    if (bit_1 > 1) or (bit_2 > 1):
        raise ValueError("inputs must be less or equal to 1.")

    # build registers
    qr = QuantumRegister(2, "qr")
    cr = ClassicalRegister(2, "cr")

    quantum_circuit = QuantumCircuit(qr, cr)

    # entanglement the qubits
    quantum_circuit.h(1)
    quantum_circuit.cx(1, 0)

    # send the information
    c_information = str(bit_1) + str(bit_2)

    if c_information == "11":
        quantum_circuit.x(1)
        quantum_circuit.z(1)
    elif c_information == "10":
        quantum_circuit.z(1)
    elif c_information == "01":
        quantum_circuit.x(1)
    else:
        quantum_circuit.i(1)

    # unentangled the circuit
    quantum_circuit.cx(1, 0)
    quantum_circuit.h(1)

    # measure the circuit
    quantum_circuit.measure(qr, cr)

    backend = Aer.get_backend("qasm_simulator")
    job = execute(quantum_circuit, backend, shots=1000)

    return job.result().get_counts(quantum_circuit)


if __name__ == "__main__":
    print(f"Counts for classical state send: {superdense_coding(1,1)}")
