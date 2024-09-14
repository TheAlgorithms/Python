import hashlib
import json
from time import time
from uuid import uuid4

class Blockchain:
    def __init__(self):
        # Initialize blockchain as an empty list and pending transactions
        self.chain = []
        self.current_transactions = []

        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Creates a new block and adds it to the chain.
        :param proof: The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) Hash of previous block
        :return: New Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined block.
        :param sender: Address of the sender
        :param recipient: Address of the recipient
        :param amount: Amount of the transaction
        :return: The index of the block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a block.
        :param block: Block
        :return: Hash as a hex string
        """
        # Ensure the dictionary is ordered to avoid inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """
        Returns the last block in the chain.
        :return: Last Block
        """
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work algorithm:
        - Find a number p' such that hash(pp') contains leading 4 zeroes
        - p is the previous proof, and p' is the new proof
        :param last_proof: Previous proof
        :return: New proof
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
            
            # Add the mining reward here
        self.new_transaction(
            sender="0",  # System or network
            recipient="Miner1",  # Replace with the miner's address
            amount=1  # Reward amount
        )
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: Previous proof
        :param proof: Current proof
        :return: True if correct, False if not.
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

# Create a new blockchain instance
blockchain = Blockchain()

# Example usage: Add a new transaction and mine a new block
blockchain.new_transaction(sender="Alice", recipient="Bob", amount=50)
last_proof = blockchain.last_block['proof']
proof = blockchain.proof_of_work(last_proof)
block = blockchain.new_block(proof)

print(f"New block created: {block}")
