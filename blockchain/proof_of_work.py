from datetime import datetime, timezone
import hashlib


class Block:
    def __init__(self, index: int, previous_hash: str, data: str, timestamp: str):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp

    def mine_block(self, difficulty: int) -> None:
        # Implement mining logic here
        pass

    @staticmethod
    def create_genesis_block() -> "Block":
        return Block(0, "0", "Genesis Block", datetime.now(timezone.utc).isoformat())
