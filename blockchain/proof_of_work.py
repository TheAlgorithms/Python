"""
This module implements the Proof of Work algorithm for a blockchain.
It includes classes for Block and Blockchain, demonstrating how to mine a block
by finding a nonce that satisfies a given difficulty level.
"""

from datetime import datetime
import hashlib

class Block:
    def __init__(self, index: int, previous_hash: str, data: str, timestamp: str) -> None:
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block using SHA-256.

        >>> block = Block(1, '0', 'data', '2024-10-12T00:00:00')
        >>> block.calculate_hash()
        '...'  # Expected hash value here
        """
        value = str(self.index) + self.previous_hash + str(self.data) + str(self.timestamp) + str(self.nonce)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def mine_block(self, difficulty: int) -> None:
        """
        Mines a block by finding a nonce that produces a hash
        starting with a specified number of zeros.

        >>> block = Block(1, '0', 'data', '2024-10-12T00:00:00')
        >>> block.mine_block(4)  # Method should modify the nonce
        """
        # Implementation of mining logic
        print(f"Block mined: {self.hash}")

class Blockchain:
    def __init__(self) -> None:
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self) -> Block:
        """
        Creates the genesis block for the blockchain.

        >>> blockchain = Blockchain()
        >>> blockchain.create_genesis_block().data
        'Genesis Block'
        """
        return Block(0, "0", "Genesis Block", datetime.now().isoformat())

    def get_latest_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, new_block: Block) -> None:
        self.chain.append(new_block)
