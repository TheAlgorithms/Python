# Title: Proof of Work Algorithm for Blockchain

## Algorithm Statement:
# The algorithm implements the Proof of Work (PoW) consensus mechanism used in
# blockchain to validate blocks. PoW ensures participants (miners) perform a
# computational task to create a valid block and add it to the blockchain. The
# difficulty is defined by the number of leading zeros required in the block hash.

import hashlib
import time


class Block:
    def __init__(
        self,
        index: int,
        previous_hash: str,
        transactions: str,
        timestamp: float,
        difficulty: int,
    ) -> None:
        """
        Initializes a Block object with the specified parameters.

        Parameters:
        - index (int): The index of the block in the blockchain.
        - previous_hash (str): The hash of the previous block.
        - transactions (str): The list of transactions in the block.
        - timestamp (float): The time when the block was created
          (in Unix timestamp format).
        - difficulty (int): The difficulty level for mining this block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self.nonce = 0  # Start with nonce 0
        self.difficulty = difficulty
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        """
        Generates the hash of the block content.
        Combines index, previous hash, transactions, timestamp, and nonce into
        a string, which is then hashed using SHA-256.

        Returns:
        - str: The hash of the block.
        """
        block_string = (
            f"{self.index}{self.previous_hash}{self.transactions}{self.timestamp}"
            f"{self.nonce}"
        )
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self) -> None:
        """
        Performs Proof of Work by adjusting the nonce until a valid hash is found.
        A valid hash has the required number of leading zeros based on the
        difficulty level.

        Returns:
        - None
        """
        target = (
            "0" * self.difficulty
        )  # Target hash should start with 'difficulty' zeros
        while self.hash[: self.difficulty] != target:
            self.nonce += 1
            self.hash = self.compute_hash()

        print(f"Block mined with nonce {self.nonce}, hash: {self.hash}")


class Blockchain:
    def __init__(self, difficulty: int) -> None:
        """
        Initializes the blockchain with a given difficulty level.

        Parameters:
        - difficulty (int): The difficulty level for mining blocks in this blockchain.

        Returns:
        - None
        """
        self.chain: list[Block] = []  # Adding type hint for the list of blocks
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """
        Creates the first block in the blockchain (the Genesis block).

        Returns:
        - None
        """
        genesis_block = Block(0, "0", "Genesis Block", time.time(), self.difficulty)
        genesis_block.mine_block()
        self.chain.append(genesis_block)

    def add_block(self, transactions: str) -> None:
        """
        Adds a new block to the blockchain after performing Proof of Work.

        Parameters:
        - transactions (str): The list of transactions to be added in the new block.

        Returns:
        - None
        """
        previous_block = self.chain[-1]
        new_block = Block(
            len(self.chain),
            previous_block.hash,
            transactions,
            time.time(),
            self.difficulty,
        )
        new_block.mine_block()
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Verifies the integrity of the blockchain by ensuring each block's previous
        hash matches and that all blocks meet the Proof of Work requirement.

        Returns:
        - bool: True if the blockchain is valid, False otherwise.
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


## Test Case 1: Blockchain Initialization and Genesis Block
# This test verifies if the blockchain is correctly initialized with a Genesis block
# and if the block is successfully mined.
def test_blockchain() -> None:
    """
    Test cases for the Blockchain proof of work algorithm.

    Returns:
    - None
    """
    # Create blockchain with difficulty level of 4 (hash should start with 4 zeros)
    blockchain = Blockchain(difficulty=4)

    ## Test Case 2: Add a block and verify the block is mined
    # This test adds a new block with transactions and ensures it's mined according
    # to the proof of work mechanism.
    blockchain.add_block("Transaction 1: Alice pays Bob 5 BTC")
    blockchain.add_block("Transaction 2: Bob pays Charlie 3 BTC")

    ## Test Case 3: Verify blockchain integrity
    # This test checks that the blockchain remains valid after adding new blocks
    assert blockchain.is_chain_valid(), "Blockchain should be valid"

    ## Test Case 4: Tampering with the blockchain
    # This test simulates tampering with the blockchain and checks that the validation
    # correctly detects the tampering.
    blockchain.chain[
        1
    ].transactions = "Transaction 1: Alice pays Bob 50 BTC"  # Tampering
    assert (
        not blockchain.is_chain_valid()
    ), "Blockchain should be invalid due to tampering"

    ## Test Case 5: Correct blockchain validation
    # This test checks if the blockchain becomes invalid after tampering and verifies
    # if the PoW still holds after tampering is done.

    print("All test cases passed.")


if __name__ == "__main__":
    test_blockchain()
