import hashlib
import time
from datetime import datetime

class Block:
    def __init__(self, index: int, previous_hash: str, data: str, timestamp: str):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        value = (str(self.index) + str(self.previous_hash) + 
                 str(self.data) + str(self.timestamp) + str(self.nonce))
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def mine_block(self, difficulty: int) -> None:
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self) -> Block:
        return Block(0, "0", "Genesis Block", datetime.now().isoformat())

    def get_latest_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, new_block: Block) -> None:
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

# Example usage
blockchain = Blockchain()
blockchain.add_block(Block(1, "", "Block 1 Data", datetime.now().isoformat()))
blockchain.add_block(Block(2, "", "Block 2 Data", datetime.now().isoformat()))

# Display the blockchain
for block in blockchain.chain:
    print(f"Block {block.index} - Hash: {block.hash} - Data: {block.data}")
