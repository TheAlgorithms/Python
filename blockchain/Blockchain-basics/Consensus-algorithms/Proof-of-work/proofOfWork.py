# Import the Block class from block.py
from block import Block

# Create a Blockchain class
class Blockchain:
    # Constructor to initialize the blockchain
    def __init__(self):
        self.chain = []  # List to hold blocks in the blockchain
        self.all_transactions = []  # List to store all transactions across blocks
        self.genesis_block()  # Create the genesis block to start the blockchain

    # Create the genesis block (the first block in the blockchain)
    def genesis_block(self):
        transactions = {}  # Transactions are empty for the genesis block
        genesis_block = Block(transactions, "0")  # Create a new Block object for the genesis block
        self.chain.append(genesis_block)  # Add the genesis block to the blockchain
        return self.chain

    # Function to print the contents of all blocks in the blockchain
    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_contents()  # Call the print_contents() method of the Block class to print block details

    # Function to add a new block to the blockchain
    def add_block(self, transactions):
        previous_block_hash = self.chain[len(self.chain) - 1].hash  # Get the hash of the previous block
        new_block = Block(transactions, previous_block_hash)  # Create a new Block with the provided transactions
        self.chain.append(new_block)  # Add the new block to the blockchain

    # Function to validate the integrity of the blockchain
    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if (current.hash != current.generate_hash()):
                print("The current hash of the block does not equal the generated hash of the block.")
                return False
            if (current.previous_hash != previous.generate_hash()):
                print("The previous block's hash does not equal the previous hash value stored in the current block.")
                return False
        return True

    # Function to perform proof of work (mining)
    def proof_of_work(self, block, difficulty=2):
        self.proof = block.generate_hash()  # Calculate the hash of the block
        while self.proof[:difficulty] != '0' * difficulty:
            block.nonce += 1  # Increment the nonce value
            self.proof = block.generate_hash()  # Recalculate the hash
        block.nonce = 0  # Reset the nonce value
        return self.proof

# This is the end of the Blockchain class definition
