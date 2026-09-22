"""
Proof of Work (PoW) implementation.
This algorithm is used in blockchain technology
to reach consensus and secure the network
"""

import hashlib


def proof_of_work(
    block_number: int, transactions: str, previous_hash: str, difficulty: int
) -> tuple[int, str]:
    """
    Finds a nonce such that the SHA-256 hash of the block starts with
    a specific number of zeros (difficulty).

    >>> proof_of_work(1, "test", "abc", 1)[1].startswith("0")
    True
    >>> # Consistency check: same input must produce same output
    >>> res1 = proof_of_work(1, "data", "hash", 2)
    >>> res2 = proof_of_work(1, "data", "hash", 2)
    >>> res1 == res2
    True
    >>> # Difficulty 0 should return nonce 0 immediately
    >>> proof_of_work(1, "data", "hash", 0)[0]
    0
    """
    if difficulty < 0:
        raise ValueError("difficulty must be a non-negative integer")

    prefix = "0" * difficulty
    nonce = 0

    while True:
        # Create a single string representing all block data
        text = f"{block_number}{transactions}{previous_hash}{nonce}"

        # Calculate the SHA-256 hash
        current_hash = hashlib.sha256(text.encode()).hexdigest()

        # Check if the hash meets the difficulty requirement
        if current_hash.startswith(prefix):
            return nonce, current_hash

        nonce += 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage:
    example_tx = "Alice sends 1 BTC to Bob"
    prev_h = "00000abcdef1234567890"
    diff = 4

    print(f"Mining block... (Difficulty: {diff})")
    nonce, hash_found = proof_of_work(1, example_tx, prev_h, diff)

    print(f"Success! Nonce: {nonce}")
    print(f"Hash: {hash_found}")
