# https://github.com/rupansh/QuantumComputing/blob/master/rippleadd.py
# https://en.wikipedia.org/wiki/Adder_(electronics)#Full_adder
# https://en.wikipedia.org/wiki/Controlled_NOT_gate

from qiskit import Aer, QuantumCircuit, execute
from qiskit.providers import Backend


def store_two_classics(val1: int, val2: int) -> tuple[QuantumCircuit, str, str]:
    """
    Generates a Quantum Circuit which stores two classical integers
    Returns the circuit and binary representation of the integers
    """
    x, y = bin(val1)[2:], bin(val2)[2:]  # Remove leading '0b'

    # Ensure that both strings are of the same length
    if len(x) > len(y):
        y = y.zfill(len(x))
    else:
        x = x.zfill(len(y))

    # We need (3 * number of bits in the larger number)+1 qBits
    # The second parameter is the number of classical registers, to measure the result
    circuit = QuantumCircuit((len(x) * 3) + 1, len(x) + 1)

    # We are essentially "not-ing" the bits that are 1
    # Reversed because its easier to perform ops on more significant bits
    for i in range(len(x)):
        if x[::-1][i] == "1":
            circuit.x(i)
    for j in range(len(y)):
        if y[::-1][j] == "1":
            circuit.x(len(x) + j)

    return circuit, x, y


def full_adder(
    circuit: QuantumCircuit,
    input1_loc: int,
    input2_loc: int,
    carry_in: int,
    carry_out: int,
):
    """
    Quantum Equivalent of a Full Adder Circuit
    CX/CCX is like 2-way/3-way XOR
    """
    circuit.ccx(input1_loc, input2_loc, carry_out)
    circuit.cx(input1_loc, input2_loc)
    circuit.ccx(input2_loc, carry_in, carry_out)
    circuit.cx(input2_loc, carry_in)
    circuit.cx(input1_loc, input2_loc)


# The default value for **backend** is the result of a function call which is not
# normally recommended and causes flake8-bugbear to raise a B008 error. However,
# in this case, this is accptable because `Aer.get_backend()` is called when the
# function is defined and that same backend is then reused for all function calls.


def ripple_adder(
    val1: int,
    val2: int,
    backend: Backend = Aer.get_backend("qasm_simulator"),  # noqa: B008
) -> int:
    """
    Quantum Equivalent of a Ripple Adder Circuit
    Uses qasm_simulator backend by default

    Currently only adds 'emulated' Classical Bits
    but nothing prevents us from doing this with hadamard'd bits :)

    Only supports adding positive integers

    >>> ripple_adder(3, 4)
    7
    >>> ripple_adder(10, 4)
    14
    >>> ripple_adder(-1, 10)
    Traceback (most recent call last):
        ...
    ValueError: Both Integers must be positive!
    """

    if val1 < 0 or val2 < 0:
        raise ValueError("Both Integers must be positive!")

    # Store the Integers
    circuit, x, y = store_two_classics(val1, val2)

    """
    We are essentially using each bit of x & y respectively as full_adder's input
    the carry_input is used from the previous circuit (for circuit num > 1)

    the carry_out is just below carry_input because
    it will be essentially the carry_input for the next full_adder
    """
    for i in range(len(x)):
        full_adder(circuit, i, len(x) + i, len(x) + len(y) + i, len(x) + len(y) + i + 1)
        circuit.barrier()  # Optional, just for aesthetics

    # Measure the resultant qBits
    for i in range(len(x) + 1):
        circuit.measure([(len(x) * 2) + i], [i])

    res = execute(circuit, backend, shots=1).result()

    # The result is in binary. Convert it back to int
    return int(list(res.get_counts())[0], 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
