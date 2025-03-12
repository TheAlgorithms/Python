import hashlib


def proof_of_work(difficulty: int) -> int:
    """
    Simulates a Proof of Work mining process.

    The miner must find a nonce such that the hash of the nonce starts
    with a specific number of leading zeros (difficulty).

    Args:
        difficulty (int): The number of leading zeros required in the hash.

    Returns:
        int: The nonce value that solves the puzzle.

    Example:
        >>> result = proof_of_work(2)  # Difficulty of 2 should be fast
        >>> isinstance(result, int)
        True
    """
    prefix = "0" * difficulty
    nonce = 0

    while True:
        hash_result = hashlib.sha256(f"{nonce}".encode()).hexdigest()
        if hash_result.startswith(prefix):
            return nonce
        nonce += 1
