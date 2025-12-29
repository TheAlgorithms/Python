"""
Merkle Tree (Hash Tree) Implementation

A Merkle tree is a tree data structure where every leaf node is labeled with the
cryptographic hash of a data block, and every non-leaf node is labeled with the
hash of its child nodes. This allows efficient and secure verification of large
data structures.

How it works:
1. Hash each data block to create leaf nodes
2. Pair adjacent hashes and hash them together to create parent nodes
3. Repeat until a single root hash remains
4. If odd number of nodes, duplicate the last one

Use cases:
- Bitcoin and Blockchain: Verify transactions in blocks efficiently
- Git: Verify repository integrity and commit history
- IPFS: Content-addressed distributed file system
- Certificate Transparency: SSL/TLS certificate verification logs
- Apache Cassandra: Anti-entropy for data synchronization
- BitTorrent: Verify pieces of downloaded files

Time Complexity:
- Build tree: O(n) where n is number of data blocks
- Generate proof: O(log n)
- Verify proof: O(log n)

Space Complexity: O(n)

References:
- https://en.wikipedia.org/wiki/Merkle_tree
- https://bitcoin.org/bitcoin.pdf (Section 7: Reclaiming Disk Space)
- https://tools.ietf.org/html/rfc9162 (Certificate Transparency)
"""

from hashlib import sha256


class MerkleTree:
    """
    Merkle tree implementation for efficient data verification.

    >>> tree = MerkleTree([b"a", b"b", b"c", b"d"])
    >>> root = tree.get_root()
    >>> len(root)
    64

    >>> tree = MerkleTree([b"hello", b"world"])
    >>> proof = tree.get_proof(0)
    >>> len(proof) > 0
    True

    >>> tree = MerkleTree([b"data"])
    >>> root = tree.get_root()
    >>> len(root)
    64
    """

    def __init__(self, data_blocks: list[bytes]) -> None:
        if not data_blocks:
            msg = "Cannot create Merkle tree from empty data"
            raise ValueError(msg)
        self.leaves = [sha256(block).hexdigest() for block in data_blocks]
        self.tree = self._build_tree()

    def _build_tree(self) -> list[list[str]]:
        tree = [self.leaves[:]]
        current_level = self.leaves[:]
        while len(current_level) > 1:
            current_level = [
                (
                    sha256(
                        (current_level[i] + current_level[i + 1]).encode()
                    ).hexdigest()
                    if i + 1 < len(current_level)
                    else sha256(
                        (current_level[i] + current_level[i]).encode()
                    ).hexdigest()
                )
                for i in range(0, len(current_level), 2)
            ]
            tree.append(current_level)
        return tree

    def get_root(self) -> str:
        """
        Get the Merkle root hash.

        >>> tree = MerkleTree([b"a", b"b", b"c", b"d"])
        >>> root = tree.get_root()
        >>> isinstance(root, str)
        True

        >>> tree = MerkleTree([b"single"])
        >>> root = tree.get_root()
        >>> len(root)
        64
        """
        return self.tree[-1][0]

    def get_proof(self, index: int) -> list[tuple[str, str]]:
        """
        Generate a Merkle proof for a data block at the given index.

        Returns list of (hash, position) tuples where position is 'left' or 'right'.

        >>> tree = MerkleTree([b"a", b"b", b"c", b"d"])
        >>> proof = tree.get_proof(0)
        >>> len(proof) > 0
        True

        >>> tree = MerkleTree([b"a", b"b"])
        >>> proof = tree.get_proof(0)
        >>> all(isinstance(p, tuple) and len(p) == 2 for p in proof)
        True

        >>> tree = MerkleTree([b"only_one"])
        >>> proof = tree.get_proof(0)
        >>> len(proof)
        0
        """
        if index < 0 or index >= len(self.leaves):
            msg = f"Index {index} out of range"
            raise ValueError(msg)
        proof = []
        for level in self.tree[:-1]:
            sibling_index = index ^ 1
            if sibling_index < len(level):
                position = "left" if index % 2 == 1 else "right"
                proof.append((level[sibling_index], position))
            index //= 2
        return proof

    @staticmethod
    def verify_proof(
        leaf_hash: str, proof: list[tuple[str, str]], root_hash: str
    ) -> bool:
        """
        Verify a Merkle proof.

        >>> tree = MerkleTree([b"a", b"b", b"c", b"d"])
        >>> root = tree.get_root()
        >>> leaf = sha256(b"a").hexdigest()
        >>> proof = tree.get_proof(0)
        >>> MerkleTree.verify_proof(leaf, proof, root)
        True

        >>> MerkleTree.verify_proof(leaf, proof, "wrong_root")
        False

        >>> tree = MerkleTree([b"x", b"y", b"z"])
        >>> root = tree.get_root()
        >>> leaf = sha256(b"y").hexdigest()
        >>> proof = tree.get_proof(1)
        >>> MerkleTree.verify_proof(leaf, proof, root)
        True

        >>> wrong_leaf = sha256(b"wrong").hexdigest()
        >>> MerkleTree.verify_proof(wrong_leaf, proof, root)
        False
        """
        current_hash = leaf_hash
        for sibling_hash, position in proof:
            current_hash = (
                sha256((sibling_hash + current_hash).encode()).hexdigest()
                if position == "left"
                else sha256((current_hash + sibling_hash).encode()).hexdigest()
            )
        return current_hash == root_hash


if __name__ == "__main__":
    import doctest

    _ = doctest.testmod()

    print("Merkle Tree Example:")
    data = [b"Transaction 1", b"Transaction 2", b"Transaction 3", b"Transaction 4"]
    tree = MerkleTree(data)
    print(f"Root hash: {tree.get_root()}")
    print(f"Proof for index 0: {tree.get_proof(0)}")
    leaf = sha256(data[0]).hexdigest()
    proof = tree.get_proof(0)
    is_valid = MerkleTree.verify_proof(leaf, proof, tree.get_root())
    print(f"Proof valid: {is_valid}")
