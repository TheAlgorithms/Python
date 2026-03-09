#!/usr/bin/env python3
"""
Simulation of the Quantum Key Distribution (QKD) protocol called BB84,
created by Charles Bennett and Gilles Brassard in 1984.

BB84 is a key-distribution protocol that ensures secure key distribution
using qubits instead of classical bits. The generated key is the result
of simulating a quantum circuit. Our algorithm to construct the circuit
is as follows:

Alice generates two binary strings. One encodes the basis for each qubit:

 - 0 -> {0,1} basis.
 - 1 -> {+,-} basis.

The other encodes the state:

 - 0 -> |0> or |+>.
 - 1 -> |1> or |->.

Bob also generates a binary string and uses the same convention to choose
a basis for measurement. Based on the following results, we follow the
algorithm below:

X|0> = |1>

H|0> = |+>

HX|0> = |->

1. Whenever Alice wants to encode 1 in a qubit, she applies an
X (NOT) gate to the qubit. To encode 0, no action is needed.

2. Wherever she wants to encode it in the {+,-} basis, she applies
an H (Hadamard) gate. No action is necessary to encode a qubit in
the {0,1} basis.

3. She then sends the qubits to Bob (symbolically represented in
this circuit using wires).

4. Bob measures the qubits according to his binary string for
measurement. To measure a qubit in the {+,-} basis, he applies
an H gate to the corresponding qubit and then performs a measurement.

References:
https://en.wikipedia.org/wiki/BB84
https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
"""
import numpy as np
import qiskit


def bb84(key_len: int = 8, seed: int | None = None) -> str:
    """
    Performs the BB84 protocol using a key made of `key_len` bits.
    The two parties in the key distribution are called Alice and Bob.
    Args:
        key_len: The length of the generated key in bits. The default is 8.

        seed: Seed for the random number generator.
        Mostly used for testing. Default is None.

    Returns:
        key: The key generated using BB84 protocol.

    >>> bb84(16, seed=0)
    '0111110111010010'

    >>> bb84(8, seed=0)
    '10110001'
    """
    # Set up the random number generator.
    rng = np.random.default_rng(seed=seed)

    # Roughly 25% of the qubits will contribute to the key.
    # So we take more than we need.
    num_qubits = 6 * key_len
    # Measurement basis for Alice's qubits.
    alice_basis = rng.integers(2, size=num_qubits)
    # The set of states Alice will prepare.
    alice_state = rng.integers(2, size=num_qubits)
    # Measurement basis for Bob's qubits.
    bob_basis = rng.integers(2, size=num_qubits)

    # Quantum Circuit to simulate BB84
    bb84_circ = qiskit.QuantumCircuit(num_qubits, name="BB84")

    # Alice prepares her qubits according to rules above.
    for index, _ in enumerate(alice_basis):
        if alice_state[index] == 1:
            bb84_circ.x(index)
        if alice_basis[index] == 1:
            bb84_circ.h(index)
    bb84_circ.barrier()

    # Bob measures the received qubits according to rules above.
    for index, _ in enumerate(bob_basis):
        if bob_basis[index] == 1:
            bb84_circ.h(index)

    bb84_circ.barrier()
    bb84_circ.measure_all()

    # Simulate the quantum circuit.
    sim = qiskit.Aer.get_backend("aer_simulator")
    # We only need to run one shot because the key is unique.
    # Multiple shots will produce the same key.
    job = qiskit.execute(bb84_circ, sim, shots=1, seed_simulator=seed)
    # Returns the result of measurement.
    result = job.result().get_counts(bb84_circ).most_frequent()

    # Extracting the generated key from the simulation results.
    # Only keep measurement results where Alice and Bob chose the same basis.
    gen_key = "".join(
        [
            result_bit
            for alice_basis_bit, bob_basis_bit, result_bit in zip(
                alice_basis, bob_basis, result
            )
            if alice_basis_bit == bob_basis_bit
        ]
    )

    # Get final key. Pad with 0 if too short, otherwise truncate.
    key = gen_key[:key_len] if len(gen_key) >= key_len else gen_key.ljust(key_len, "0")
    return key


if __name__ == "__main__":
    print(f"The generated key is : {bb84(8, seed=0)}")
    from doctest import testmod

    testmod()
