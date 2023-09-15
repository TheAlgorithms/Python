"""Proof of Work (PoW) is a consensus algorithm used in blockchain systems
like Bitcoin. In PoW, network participants (miners) solve complex mathematical
puzzles to validate transactions and add new blocks to the blockchain.
This resource-intensive process ensures the security and integrity of
the network by requiring computational work and discouraging malicious actors."""


import hashlib
import random
import string

# Define the difficulty target (number of leading zeros)
difficulty = 4


def generate_random_string(length):
    # Generate a random string of given length
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


def proof_of_work(difficulty):
    # Create a target with the specified number of leading zeros
    target = "0" * difficulty

    # Initialize a nonce
    nonce = 0

    while True:
        # Generate a random string for the data (you can replace this with your data)
        data = generate_random_string(16)

        # Concatenate the data and nonce
        combined_data = data + str(nonce)

        # Calculate the hash of the combined data using SHA-256
        sha256_hash = hashlib.sha256(combined_data.encode()).hexdigest()

        # Check if the hash meets the difficulty target
        if sha256_hash[:difficulty] == target:
            print(f"Nonce found: {nonce}")
            print(f"Hash: {sha256_hash}")
            break

        # Increment the nonce for the next iteration
        nonce += 1


# Run the Proof of Work with the specified difficulty
proof_of_work(difficulty)

"""In this code:

'difficulty'  specifies the number of leading zeros that the resulting hash must have to be considered a valid solution.

'generate_random_string(length)' generates a random string of the specified length. You can replace this with your actual data.

'proof_of_work(difficulty)' is the main function that performs the PoW.
It generates random data, concatenates it with a nonce, calculates the SHA-256 hash,
and checks if the hash meets the difficulty target. If not, it increments the nonce
and continues until a valid hash is found.
"""
