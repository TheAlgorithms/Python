"""
Build the quantum full adder (QFA) for any sum of
two quantum registers and one carry in. This circuit
is designed using the Qiskit framework. This
experiment run in IBM Q simulator with 1000 shots.
.
References:
https://www.quantum-inspire.com/kbase/full-adder/
"""

import math

import qiskit


def quantum_full_adder(
    input_1: int = 1, input_2: int = 1, carry_in: int = 1
) -> qiskit.result.counts.Counts:
    """
    # >>> q_full_adder(inp_1, inp_2, cin)
    # the inputs can be 0/1 for qubits in define
    # values, or can be in a superposition of both
    # states with hadamard gate using the input value 2.
    # result for default values: {11: 1000}
    qr_0: ──■────■──────────────■──
            │  ┌─┴─┐          ┌─┴─┐
    qr_1: ──■──┤ X ├──■────■──┤ X ├
            │  └───┘  │  ┌─┴─┐└───┘
    qr_2: ──┼─────────■──┤ X ├─────
          ┌─┴─┐     ┌─┴─┐└───┘
    qr_3: ┤ X ├─────┤ X ├──────────
          └───┘     └───┘
    cr: 2/═════════════════════════
    Args:
        input_1: input 1 for the circuit.
        input_2: input 2 for the circuit.
        carry_in: carry in for the circuit.
    Returns:
        qiskit.result.counts.Counts: sum result counts.
    >>> quantum_full_adder(1, 1, 1)
    {'11': 1000}
    >>> quantum_full_adder(0, 0, 1)
    {'01': 1000}
    >>> quantum_full_adder(1, 0, 1)
    {'10': 1000}
    >>> quantum_full_adder(1, -4, 1)
    Traceback (most recent call last):
        ...
    ValueError: inputs must be positive.
    >>> quantum_full_adder('q', 0, 1)
    Traceback (most recent call last):
        ...
    TypeError: inputs must be integers.
    >>> quantum_full_adder(0.5, 0, 1)
    Traceback (most recent call last):
        ...
    ValueError: inputs must be exact integers.
    >>> quantum_full_adder(0, 1, 3)
    Traceback (most recent call last):
        ...
    ValueError: inputs must be less or equal to 2.
    """
    if (type(input_1) == str) or (type(input_2) == str) or (type(carry_in) == str):
        raise TypeError("inputs must be integers.")

    if (input_1 < 0) or (input_2 < 0) or (carry_in < 0):
        raise ValueError("inputs must be positive.")

    if (
        (math.floor(input_1) != input_1)
        or (math.floor(input_2) != input_2)
        or (math.floor(carry_in) != carry_in)
    ):
        raise ValueError("inputs must be exact integers.")

    if (input_1 > 2) or (input_2 > 2) or (carry_in > 2):
        raise ValueError("inputs must be less or equal to 2.")

    # build registers
    qr = qiskit.QuantumRegister(4, "qr")
    cr = qiskit.ClassicalRegister(2, "cr")
    # list the entries
    entry = [input_1, input_2, carry_in]

    quantum_circuit = qiskit.QuantumCircuit(qr, cr)

    for i in range(0, 3):
        if entry[i] == 2:
            quantum_circuit.h(i)  # for hadamard entries
        elif entry[i] == 1:
            quantum_circuit.x(i)  # for 1 entries
        elif entry[i] == 0:
            quantum_circuit.i(i)  # for 0 entries

    # build the circuit
    quantum_circuit.ccx(0, 1, 3)  # ccx = toffoli gate
    quantum_circuit.cx(0, 1)
    quantum_circuit.ccx(1, 2, 3)
    quantum_circuit.cx(1, 2)
    quantum_circuit.cx(0, 1)

    quantum_circuit.measure([2, 3], cr)  # measure the last two qbits

    backend = qiskit.Aer.get_backend("aer_simulator")
    job = qiskit.execute(quantum_circuit, backend, shots=1000)

    return job.result().get_counts(quantum_circuit)


if __name__ == "__main__":
    print(f"Total sum count for state is: {quantum_full_adder(1, 1, 1)}")
