# Import the datetime module for timestamp and hashlib module for SHA-256 hashing
import datetime
from hashlib import sha256

# Create a Block class
class Block:
    # Initialize the Block object with transactions and the previous block's hash
    def __init__(self, transactions, previous_hash):
        # Set the timestamp to the current date and time
        self.time_stamp = datetime.datetime.now()
        self.transactions = transactions  # Store transaction data
        self.previous_hash = previous_hash  # Store the hash of the previous block
        self.nonce = 0  # Initialize the nonce (number used once) to 0
        self.hash = self.generate_hash()  # Compute and store the block's hash

    # Generate a hash for the block
    def generate_hash(self):
        # Create a block header by combining timestamp, transactions, previous hash, and nonce
        block_header = str(self.time_stamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        # Calculate the SHA-256 hash of the block header
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()  # Return the hexadecimal representation of the hash

    # Print the contents of the block
    def print_contents(self):
        print("timestamp:", self.time_stamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())
        print("previous hash:", self.previous_hash)

# This is the end of the Block class definition

# Example usage:
# Create a new block with some sample transactions and a previous block's hash
transactions_data = "Sample transactions go here"
previous_block_hash = "Previous block's hash goes here"
block = Block(transactions_data, previous_block_hash)

# Print the contents of the block
block.print_contents()
