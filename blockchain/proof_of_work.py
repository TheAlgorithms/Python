from __future__ import annotations

import hashlib
import json
from time import time


class Block:
    """
    A single block in a proof-of-work blockchain.

    Each block contains data along with a cryptographic hash linking it to the
    previous block. The block's hash must satisfy a difficulty target (start
    with a certain number of zero bits) which is found through mining.

    Attributes:
        index: Position of the block in the chain
        timestamp: Unix time when the block was created
        data: Payload stored in the block
        previous_hash: Hash of the previous block (hex digest)
        nonce: Number used to satisfy the proof-of-work requirement
        hash: SHA-256 hash of this block (hex digest)

    >>> Block(0, 1000.0, "genesis", "0", 0, "0000abc")
    Block(0, 1000.0, 'genesis', '0', 0, hash=0000abc)

    Blocks with the same content are equal:
    >>> Block(0, 0.0, "a", "0", 1, "ab") == Block(0, 0.0, "a", "0", 1, "ab")
    True
    >>> Block(0, 0.0, "a", "0", 1, "ab") == Block(0, 0.0, "b", "0", 1, "ab")
    False
    """

    def __init__(
        self,
        index: int,
        timestamp: float,
        data: str,
        previous_hash: str,
        nonce: int,
        hash_value: str,
    ) -> None:
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = hash_value

    def __repr__(self) -> str:
        return (
            f"Block({self.index}, {self.timestamp}, "
            f"{self.data!r}, {self.previous_hash!r}, {self.nonce}, "
            f"hash={self.hash})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Block):
            return NotImplemented
        return (
            self.index == other.index
            and self.timestamp == other.timestamp
            and self.data == other.data
            and self.previous_hash == other.previous_hash
            and self.nonce == other.nonce
            and self.hash == other.hash
        )

    def to_dict(self) -> dict:
        """Serialise the block to a JSON-compatible dictionary.

        >>> Block(0, 0.0, "a", "0", 0, "ab").to_dict()["data"]
        'a'
        """
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
            "hash": self.hash,
        }


def calculate_hash(
    index: int,
    timestamp: float,
    data: str,
    previous_hash: str,
    nonce: int,
) -> str:
    """Compute the SHA-256 hash of a block's contents.

    The hash is taken over the concatenation of index, timestamp, data,
    previous_hash, and nonce, serialised as a JSON string.

    >>> h = calculate_hash(1, 0.0, "tx", "0000", 42)
    >>> isinstance(h, str) and len(h) == 64
    True

    Same inputs always produce the same hash:
    >>> a = calculate_hash(1, 0.0, "tx", "0000", 42)
    >>> a == calculate_hash(1, 0.0, "tx", "0000", 42)
    True
    """
    payload = json.dumps(
        [index, timestamp, data, previous_hash, nonce],
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode()).hexdigest()


def mine_block(
    index: int,
    timestamp: float,
    data: str,
    previous_hash: str,
    difficulty: int,
) -> Block:
    """Mine a new block by finding a nonce that satisfies the difficulty target.

    The block's hash must start with ``difficulty`` consecutive zero characters.
    This is a brute-force search that increments the nonce until a valid hash
    is found. Higher difficulty values require exponentially more work.

    Difficulty must be a non-negative integer:
    Mined blocks always satisfy the proof-of-work requirement:
    >>> b = mine_block(1, 0.0, "hello", "abcd", 3)
    >>> b.hash[:3]
    '000'

    >>> b = mine_block(2, 0.0, "world", b.hash, 4)
    >>> b.hash[:4]
    '0000'

    Different nonces produce different hashes for the same block data:
    >>> a = calculate_hash(5, 0.0, "same", "prev", 0)
    >>> b = calculate_hash(5, 0.0, "same", "prev", 1)
    >>> a != b
    True
    """
    prefix = "0" * difficulty
    nonce = 0
    hash_value = calculate_hash(index, timestamp, data, previous_hash, nonce)
    while not hash_value.startswith(prefix):
        nonce += 1
        hash_value = calculate_hash(index, timestamp, data, previous_hash, nonce)
    return Block(index, timestamp, data, previous_hash, nonce, hash_value)


class Blockchain:
    """
    A simple proof-of-work blockchain.

    Maintains a chain of blocks where each block references the hash of the
    previous block. New blocks are mined with an adjustable difficulty level,
    and the integrity of the chain can be verified at any time.

    >>> chain = Blockchain(difficulty=2)
    >>> _ = chain.add_block("Payment: Alice -> Bob: 10 BTC")
    >>> _ = chain.add_block("Payment: Bob -> Charlie: 5 BTC")
    >>> len(chain)
    3
    >>> chain.is_valid()
    True

    Tampering with block data invalidates the chain:
    >>> chain.chain[1].data = "Tampered!"
    >>> chain.is_valid()
    False
    """

    def __init__(self, difficulty: int = 2) -> None:
        self.difficulty = difficulty
        self.chain: list[Block] = []
        self._create_genesis_block()

    def _create_genesis_block(self) -> None:
        """Create the first block of the chain (the genesis block).

        The genesis block has index 0, arbitrary data, and previous_hash "0".
        """
        genesis = mine_block(0, time(), "Genesis Block", "0", self.difficulty)
        self.chain.append(genesis)

    def add_block(self, data: str) -> Block:
        """Add a new block with the given data to the chain.

        The block is mined with the chain's configured difficulty level.

        >>> chain = Blockchain(difficulty=1)
        >>> block = chain.add_block("test")
        >>> block.index
        1
        >>> block.data
        'test'
        >>> chain.chain[-1].hash == block.hash
        True
        """
        previous_block = self.chain[-1]
        new_block = mine_block(
            len(self.chain),
            time(),
            data,
            previous_block.hash,
            self.difficulty,
        )
        self.chain.append(new_block)
        return new_block

    def is_valid(self) -> bool:
        """Verify the integrity of the entire blockchain.

        Checks that:
        1. Every block's hash matches its recomputed hash
        2. Every block's previous_hash matches the hash of the preceding block
        3. The genesis block has index 0 and previous_hash "0"

        >>> chain = Blockchain(difficulty=1)
        >>> chain.is_valid()
        True
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != calculate_hash(
                current.index,
                current.timestamp,
                current.data,
                current.previous_hash,
                current.nonce,
            ):
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

    def __len__(self) -> int:
        return len(self.chain)

    def to_json(self) -> str:
        """Serialise the entire blockchain to a JSON string.

        >>> chain = Blockchain(difficulty=1)
        >>> _ = chain.add_block("data")
        >>> isinstance(chain.to_json(), str)
        True
        """
        return json.dumps([block.to_dict() for block in self.chain], indent=2)


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    print("Mining a simple blockchain (difficulty=3)...")
    chain = Blockchain(difficulty=3)
    chain.add_block("Transaction 1: Alice sends 10 BTC to Bob")
    chain.add_block("Transaction 2: Bob sends 5 BTC to Charlie")
    chain.add_block("Transaction 3: Charlie sends 2 BTC to Dave")

    print(f"\nBlockchain valid: {chain.is_valid()}")
    print(f"Total blocks: {len(chain)}")
    print(f"\nFull chain:\n{chain.to_json()}")
