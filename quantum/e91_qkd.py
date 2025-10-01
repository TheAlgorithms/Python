import math
import random
import numpy as np
import qiskit
from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister
from qiskit_aer import AerSimulator


def e91_protocol(n_bits: int = 2000) -> dict:
    """
    Simulates the E91 QKD protocol for a specified number of bits.

    Args:
        n_bits: The total number of entangled pairs to be generated and
                measured. This determines the potential length of the raw key.

    Returns:
        A dictionary containing the simulation results:
        - "alice_key": Alice's final, sifted secret key.
        - "bob_key": Bob's final, sifted secret key.
        - "s_value": The calculated CHSH inequality parameter 'S'.
        - "eavesdropper_detected": A boolean indicating if |S| <= 2.
        - "key_match": A boolean indicating if Alice's and Bob's keys match.
        - "key_length": The final length of the sifted keys.

    >>> e91_protocol(100) # doctest: +SKIP
    {'alice_key': '1011110', 'bob_key': '1011110', 's_value': 2.73, ...}

    >>> e91_protocol(-10)
    Traceback (most recent call last):
        ...
    ValueError: Number of bits must be > 0.

    >>> e91_protocol('abc')
    Traceback (most recent call last):
        ...
    TypeError: Number of bits must be an integer.

    >>> e91_protocol(10001)
    Traceback (most recent call last):
        ...
    ValueError: Number of bits is too large to simulate efficiently (>10000).
    """
    # --- Input Validation ---
    if not isinstance(n_bits, int):
        raise TypeError("Number of bits must be an integer.")
    if n_bits <= 0:
        raise ValueError("Number of bits must be > 0.")
    if n_bits > 10000:
        raise ValueError("Number of bits is too large to simulate efficiently (>10000).")

    # Define the measurement angles for Alice and Bob's bases as constants.
    # The keys correspond to the basis name, and values are angles in radians.
    ALICE_BASES = {'A1': 0, 'A2': np.pi / 8, 'A3': np.pi / 4}
    BOB_BASES = {'B1': np.pi / 8, 'B2': np.pi / 4, 'B3': 3 * np.pi / 8}

    # Lists to store the choices and results for each bit.
    alice_chosen_bases, bob_chosen_bases = [], []
    alice_results, bob_results = [], []

    # Get the quantum simulator backend.
    backend = AerSimulator()

    for _ in range(n_bits):
        # Alice and Bob randomly choose their measurement bases.
        alice_basis_name = random.choice(list(ALICE_BASES.keys()))
        bob_basis_name = random.choice(list(BOB_BASES.keys()))
        alice_angle = ALICE_BASES[alice_basis_name]
        bob_angle = BOB_BASES[bob_basis_name]

        # Create a quantum circuit for one entangled pair.
        qr = QuantumRegister(2, 'q')
        cr = ClassicalRegister(2, 'c')
        circuit = QuantumCircuit(qr, cr)

        # Create a Bell state |Φ+⟩ = (|00⟩ + |11⟩)/sqrt(2)
        circuit.h(qr[0])
        circuit.cx(qr[0], qr[1])

        # Apply rotations to simulate measurements in the chosen bases.
        circuit.ry(-2 * alice_angle, qr[0])
        circuit.ry(-2 * bob_angle, qr[1])

        # Measure the qubits.
        circuit.measure(qr, cr)

        # Execute the circuit and get the result.
        job = backend.run(circuit, shots=1)
        result = list(job.result().get_counts().keys())[0]

        # Store choices and results. Qiskit's bit order is reversed.
        alice_chosen_bases.append(alice_basis_name)
        bob_chosen_bases.append(bob_basis_name)
        alice_results.append(int(result[1]))
        bob_results.append(int(result[0]))


    # Sift for generating the secret key.
    # The key is formed when Alice and Bob choose compatible bases.
    # Here, compatible means A2/B1 or A3/B2, where angles are identical.
    alice_key, bob_key = [], []
    for i in range(n_bits):
        is_a2b1 = alice_chosen_bases[i] == 'A2' and bob_chosen_bases[i] == 'B1'
        is_a3b2 = alice_chosen_bases[i] == 'A3' and bob_chosen_bases[i] == 'B2'
        if is_a2b1 or is_a3b2:
            alice_key.append(alice_results[i])
            bob_key.append(bob_results[i])

    # Sift for the CHSH inequality test (Eve detection).
    # We use four specific combinations of bases for the test: a = A1, a' = A3  |  b = B1, b' = B3
    chsh_correlations = {'ab': [], 'ab_': [], 'a_b': [], 'a_b_': []}

    for i in range(n_bits):
        # Convert results {0, 1} to {-1, 1} for calculating correlation.
        a_val = 1 if alice_results[i] == 0 else -1
        b_val = 1 if bob_results[i] == 0 else -1
        product = a_val * b_val  # +1 if correlated, -1 if anti-correlated

        alice_basis = alice_chosen_bases[i]
        bob_basis = bob_chosen_bases[i]

        if alice_basis == 'A1' and bob_basis == 'B1':
            chsh_correlations['ab'].append(product)
        elif alice_basis == 'A1' and bob_basis == 'B3':
            chsh_correlations['ab_'].append(product)
        elif alice_basis == 'A3' and bob_basis == 'B1':
            chsh_correlations['a_b'].append(product)
        elif alice_basis == 'A3' and bob_basis == 'B3':
            chsh_correlations['a_b_'].append(product)

    # Calculate the expectation value (average correlation) for each combination.
    E = {}
    for key, values in chsh_correlations.items():
        E[key] = np.mean(values) if values else 0

    # Calculate the S-value: S = E(a,b) - E(a,b') + E(a',b) + E(a',b')
    s_value = E['ab'] - E['ab_'] + E['a_b'] + E['a_b_']

    # Check for eavesdropper: |S| > 2 indicates security.
    eavesdropper_detected = abs(s_value) <= 2

    return {
        "alice_key": "".join(map(str, alice_key)),
        "bob_key": "".join(map(str, bob_key)),
        "s_value": s_value,
        "eavesdropper_detected": eavesdropper_detected,
        "key_match": alice_key == bob_key,
        "key_length": len(alice_key)
    }


if __name__ == "__main__":
    # num_bits is initialized to 2000
    num_bits = 2000
    results = e91_protocol(num_bits)

    print(f"CHSH S-value: {results['s_value']:.4f}")
    print(f"Eavesdropper detected: {results['eavesdropper_detected']}")
    print(f"Final key length: {results['key_length']}")
    print(f"Keys match: {results['key_match']}")

    if not results['eavesdropper_detected'] and results['key_match'] and results['key_length'] > 0:
        print("\nProtocol successful! Secret key generated securely.")
        print(f"  Alice's key: {results['alice_key']}")
        print(f"  Bob's key:   {results['bob_key']}")
    else:
        print("\nProtocol failed or eavesdropper detected. Key discarded.")
