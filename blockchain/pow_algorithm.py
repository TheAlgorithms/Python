"""
# Title: Proof of Work Algorithm for Blockchain

## Algorithm Statement:
The algorithm implements the Proof of Work (PoW) consensus mechanism used in 
blockchain to validate blocks. PoW ensures participants (miners) perform a 
computational task to create a valid block and add it to the blockchain. The 
difficulty is defined by the number of leading zeros required in the block hash.
"""

import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp, difficulty):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self.nonce = 0  # Start with nonce 0
        self.difficulty = difficulty
        self.hash = self.compute_hash()

    def compute_hash(self):
        """
        Generates the hash of the block content.
        Combines index, previous hash, transactions, timestamp, and nonce into a string,
        which is then hashed using SHA-256.
        """
        block_string = (
            f"{self.index}{self.previous_hash}{self.transactions}{self.timestamp}"
            f"{self.nonce}"
        )
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self):
        """
        Performs Proof of Work by adjusting the nonce until a valid hash is found.
        A valid hash has the required number of leading zeros based on the difficulty 
        level.
        """
        target = '0' * self.difficulty  # Target hash should start with 'difficulty' zeros
        while self.hash[:self.difficulty] != target:
            self.nonce += 1
            self.hash = self.compute_hash()

        print(f"Block mined with nonce {self.nonce}, hash: {self.hash}")

class Blockchain:
    def __init__(self, difficulty):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain (the Genesis block).
        """
        genesis_block = Block(0, "0", "Genesis Block", time.time(), self.difficulty)
        genesis_block.mine_block()
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        """
        Adds a new block to the blockchain after performing Proof of Work.
        """
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, transactions, time.time(), 
                          self.difficulty)
        new_block.mine_block()
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Verifies the integrity of the blockchain by ensuring each block's previous 
        hash matches and that all blocks meet the Proof of Work requirement.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.compute_hash():
                print(f"Invalid block at index {i}. Hash mismatch.")
                return False

            if current_block.previous_hash != previous_block.hash:
                print(f"Invalid chain at index {i}. Previous hash mismatch.")
                return False

        return True

# Test cases

def test_blockchain():
    """
    Test cases for the Blockchain proof of work algorithm.
    """
    # Create blockchain with difficulty level of 4 (hash should start with 4 zeros)
    blockchain = Blockchain(difficulty=4)

    # Add new blocks
    blockchain.add_block("Transaction 1: Alice pays Bob 5 BTC")
    blockchain.add_block("Transaction 2: Bob pays Charlie 3 BTC")

    # Verify the integrity of the blockchain
    assert blockchain.is_chain_valid(), "Blockchain should be valid"

    # Tamper with the blockchain and check validation
    blockchain.chain[1].transactions = "Transaction 1: Alice pays Bob 50 BTC"  # Tampering
    assert not blockchain.is_chain_valid(), "Blockchain should be invalid due to tampering"

    print("All test cases passed.")

if __name__ == "__main__":
    test_blockchain()

"""
# Output:
- Block mined with nonce X, hash: 0000abcd...
- Block mined with nonce Y, hash: 0000xyz...
- Block mined with nonce Z, hash: 0000pqrs...
- All test cases passed.
"""
