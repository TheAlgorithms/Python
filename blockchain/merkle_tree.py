"""
Merkle Tree Construction and Verification

This module implements the construction of a Merkle Tree and
verification of inclusion proofs for blockchain data integrity.

Each leaf is a SHA-256 hash of a transaction, and internal nodes are
computed by hashing the concatenation of their child nodes.

References:
https://en.wikipedia.org/wiki/Merkle_tree
"""

import hashlib


def sha256(data: str) -> str:
    """Compute SHA-256 hash of a string."""
    return hashlib.sha256(data.encode()).hexdigest()


def build_merkle_tree(leaves: list[str]) -> list[list[str]]:
    """
    Build a Merkle Tree from the given leaf nodes.

    Args:
        leaves: List of data strings (transactions).

    Returns:
        A list of lists representing tree levels,
        with the last level containing the Merkle root.

    >>> len(build_merkle_tree(["a", "b", "c", "d"])[-1][0])
    64
    """
    if not leaves:
        raise ValueError("Leaf list cannot be empty.")

    current_level = [sha256(x) for x in leaves]
    tree = [current_level]

    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i + 1] if i + 1 < len(current_level) else left
            next_level.append(sha256(left + right))
        current_level = next_level
        tree.append(current_level)

    return tree


def merkle_root(leaves: list[str]) -> str:
    """
    Return the Merkle root hash for a given list of data.

    >>> r = merkle_root(["tx1", "tx2", "tx3"])
    >>> isinstance(r, str)
    True
    """
    return build_merkle_tree(leaves)[-1][0]


def verify_proof(leaf: str, proof: list[str], root: str) -> bool:
    """
    Verify inclusion of a leaf using a Merkle proof.

    Args:
        leaf: Original data string.
        proof: List of sibling hashes up the path.
        root: Expected Merkle root hash.

    Returns:
        True if proof is valid, else False.

    >>> data = ["a", "b", "c", "d"]
    >>> tree = build_merkle_tree(data)
    >>> root = tree[-1][0]
    >>> leaf = "a"
    >>> proof = [sha256("b"), sha256(sha256("c") + sha256("d"))]
    >>> verify_proof(leaf, proof, root)
    True
    """
    computed_hash = sha256(leaf)
    for sibling in proof:
        combined = sha256(computed_hash + sibling)
        computed_hash = combined
    return computed_hash == root


if __name__ == "__main__":
    import doctest

    doctest.testmod()
