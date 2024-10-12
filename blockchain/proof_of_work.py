"""
Proof of Work Module
"""

from datetime import datetime, timezone
import hashlib

class Block:
    def __init__(self, index: int, previous_hash: str, data: str, timestamp: str):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp

    def calculate_hash(self) -> str:
        value = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}"
        return hashlib.sha256(value.encode("utf-8")).hexdigest()

    def mine_block(self, difficulty: int) -> None:
        """
        Mines a block by finding a nonce that produces a hash
        """
        pass  # Implement mining logic here

    def get_block(self) -> str:
        """
        Returns a formatted string of the block
        """
        return f"Block {self.index}:\nHash: {self.calculate_hash()}\nData: {self.data}\n"

def create_genesis_block() -> Block:
    """
    Creates the first block in the blockchain
    """
    return Block(0, "0", "Genesis Block", datetime.now(timezone.utc).isoformat())

def get_latest_block() -> Block:
    """
    Returns the latest block in the blockchain
    """
    pass  # Implement logic to return the latest block

# Further implementation here...
