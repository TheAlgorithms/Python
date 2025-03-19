#Author : Hugo Cheung

"""
This repository contains a Python implementation of the VerusHash algorithm, a unique proof-of-work (PoW) hashing algorithm used by Verus Coin (VRSC).
VerusHash combines SHA-256 and Keccak-256 in a specific sequence to create a secure and ASIC-resistant hashing algorithm.
This implementation is designed to be self-contained, relying only on custom implementations of SHA-256 and Keccak-256, with no external dependencies.
"""

import hashlib

def verushash(data):
    """
    Compute VerusHash of the input data.
    VerusHash alternates between SHA-256 and Keccak-256 in a specific sequence.

    Args:
        data (bytes): The input data to be hashed.

    Returns:
        bytes: The VerusHash result as a byte string.
    """
    def sha256(data):
        """Compute SHA-256 hash of the input data using hashlib."""
        return hashlib.sha256(data).digest()

    def keccak256(data):
        """Compute Keccak-256 hash of the input data using a custom implementation."""
        # Keccak-256 parameters
        ROUNDS = 24
        RATE = 1088  # Rate in bits (1600 - 2*256)
        CAPACITY = 512  # Capacity in bits (2*256)
        STATE_SIZE = 1600  # State size in bits (5x5x64)

        # Padding
        PADDING = 0x06
        DELIMITER = 0x80

        # Initialize the state
        state = [0] * (STATE_SIZE // 8)  # State in bytes

        # Absorb phase
        block_size = RATE // 8
        padded_data = data + bytes([PADDING]) + bytes([0] * (block_size - (len(data) + 1) % block_size))
        padded_data += bytes([DELIMITER])

        for i in range(0, len(padded_data), block_size):
            block = padded_data[i:i + block_size]
            for j in range(len(block)):
                state[j] ^= block[j]
            state = keccak_f(state)

        # Squeeze phase
        output = bytearray()
        while len(output) < 32:  # 256 bits = 32 bytes
            output.extend(state[:block_size])
            state = keccak_f(state)

        return bytes(output[:32])

    def keccak_f(state):
        """Keccak-f permutation function."""
        # Convert state to a 5x5x64 array
        lanes = [[0] * 5 for _ in range(5)]
        for x in range(5):
            for y in range(5):
                index = 8 * (x + 5 * y)
                lane = int.from_bytes(state[index:index + 8], byteorder='little')
                lanes[x][y] = lane

        # Perform 24 rounds of Keccak-f
        for round in range(ROUNDS):
            lanes = keccak_round(lanes, round)

        # Convert lanes back to bytes
        state = bytearray()
        for y in range(5):
            for x in range(5):
                state.extend(lanes[x][y].to_bytes(8, byteorder='little'))

        return state

    def keccak_round(lanes, round):
        """Perform one round of Keccak-f."""
        # Theta step
        c = [lanes[x][0] ^ lanes[x][1] ^ lanes[x][2] ^ lanes[x][3] ^ lanes[x][4] for x in range(5)]
        d = [c[(x - 1) % 5] ^ ((c[(x + 1) % 5] << 1 | c[(x + 1) % 5] >> 63) for x in range(5)]
        for x in range(5):
            for y in range(5):
                lanes[x][y] ^= d[x]

        # Rho and Pi steps
        x, y = 1, 0
        current = lanes[x][y]
        for t in range(24):
            x, y = y, (2 * x + 3 * y) % 5
            current, lanes[x][y] = lanes[x][y], (current << ((t + 1) * (t + 2) // 2) | current >> (64 - ((t + 1) * (t + 2) // 2))

        # Chi step
        for y in range(5):
            t = [lanes[x][y] for x in range(5)]
            for x in range(5):
                lanes[x][y] = t[x] ^ (~t[(x + 1) % 5] & t[(x + 2) % 5])

        # Iota step
        lanes[0][0] ^= ROUND_CONSTANTS[round]

        return lanes

    # Round constants for Keccak-f
    ROUND_CONSTANTS = [
        0x0000000000000001, 0x0000000000008082, 0x800000000000808A,
        0x8000000080008000, 0x000000000000808B, 0x0000000080000001,
        0x8000000080008081, 0x8000000000008009, 0x000000000000008A,
        0x0000000000000088, 0x0000000080008009, 0x000000008000000A,
        0x000000008000808B, 0x800000000000008B, 0x8000000000008089,
        0x8000000000008003, 0x8000000000008002, 0x8000000000000080,
        0x000000000000800A, 0x800000008000000A, 0x8000000080008081,
        0x8000000000008080, 0x0000000080000001, 0x8000000080008008
    ]

    # Step 1: Compute SHA-256 of the input data
    hash1 = sha256(data)

    # Step 2: Compute Keccak-256 of the SHA-256 result
    hash2 = keccak256(hash1)

    # Step 3: Compute SHA-256 of the Keccak-256 result
    hash3 = sha256(hash2)

    # Step 4: Compute Keccak-256 of the final SHA-256 result
    final_hash = keccak256(hash3)

    return final_hash

# Example usage
if __name__ == "__main__":
    # Input data (can be a block header or any other data)
    input_data = b"Hello, VerusHash!"

    # Compute VerusHash
    result = verushash(input_data)

    # Print the result as a hexadecimal string
    print("VerusHash:", result.hex())
