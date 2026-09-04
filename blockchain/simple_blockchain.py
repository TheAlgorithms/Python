"""
A simple blockchain implementation with Proof-of-Work (PoW).

This educational example demonstrates:
- Block structure with index, timestamp, data, previous hash, nonce, and hash
- Mining via Proof-of-Work
- Chain integrity verification

Author: Letitia Gilbert
"""

import hashlib
from time import time


class Block:
    """
    Represents a single block in a blockchain.

    Attributes:
        index (int): Position of the block in the chain.
        timestamp (float): Creation time of the block.
        data (str): Data stored in the block.
        previous_hash (str): Hash of the previous block.
        nonce (int): Number used for mining.
        hash (str): SHA256 hash of the block's content.
    """

    def __init__(
        self, index: int, data: str, previous_hash: str, difficulty: int = 2
    ) -> None:
        self.index = index
        self.timestamp = time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce, self.hash = self.mine_block(difficulty)

    def compute_hash(self, nonce: int) -> str:
        """
        Compute SHA256 hash of the block with given nonce.

        Args:
            nonce (int): Nonce to include in the hash.

        Returns:
            str: Hexadecimal hash string.

        >>> block = Block(0, "Genesis", "0", difficulty=2)
        >>> len(block.compute_hash(0)) == 64
        True
        >>> isinstance(block.compute_hash(0), str)
        True
        """
        block_string = (
            f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{nonce}"
        )
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty: int) -> tuple[int, str]:
        """
        Simple Proof-of-Work mining algorithm.

        Args:
            difficulty (int): Number of leading zeros required in the hash.

        Returns:
            Tuple[int, str]: Valid nonce and resulting hash that satisfies difficulty.

        >>> block = Block(0, "Genesis", "0", difficulty=2)
        >>> block.hash.startswith('00')
        True
        """
        if difficulty < 1:
            raise ValueError("Difficulty must be at least 1")
        nonce = 0
        target = "0" * difficulty
        while True:
            hash_result = self.compute_hash(nonce)
            if hash_result.startswith(target):
                return nonce, hash_result
            nonce += 1


class Blockchain:
    """
    Simple blockchain class maintaining a list of blocks.

    Attributes:
        chain (List[Block]): List of blocks forming the chain.
    """

    def __init__(self, difficulty: int = 2) -> None:
        self.difficulty = difficulty
        self.chain: list[Block] = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the first block in the blockchain.

        Returns:
            Block: Genesis block.

        >>> bc = Blockchain()
        >>> bc.chain[0].index
        0
        >>> bc.chain[0].hash.startswith('00')
        True
        """
        return Block(0, "Genesis Block", "0", self.difficulty)

    def add_block(self, data: str) -> Block:
        """
        Add a new block to the blockchain with given data.

        Args:
            data (str): Data to store in the block.

        Returns:
            Block: Newly added block.

        >>> bc = Blockchain()
        >>> new_block = bc.add_block("Test Data")
        >>> new_block.index
        1
        >>> new_block.previous_hash == bc.chain[0].hash
        True
        >>> new_block.hash.startswith('00')
        True
        >>> bc.is_valid()
        True
        """
        prev_hash = self.chain[-1].hash
        new_block = Block(len(self.chain), data, prev_hash, self.difficulty)
        self.chain.append(new_block)
        return new_block

    def is_valid(self) -> bool:
        """
        Verify the integrity of the blockchain.

        Returns:
            bool: True if chain is valid, False otherwise.

        >>> bc = Blockchain()
        >>> new_block = bc.add_block("Test")
        >>> new_block.index
        1
        >>> new_block.previous_hash == bc.chain[0].hash
        True
        >>> new_block.hash.startswith('00')
        True
        >>> bc.is_valid()
        True
        >>> bc.chain[1].previous_hash = "tampered"
        >>> bc.is_valid()
        False

        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i - 1]
            if current.previous_hash != prev.hash:
                return False
            if not current.hash.startswith("0" * self.difficulty):
                return False
            if current.hash != current.compute_hash(current.nonce):
                return False
        return True
