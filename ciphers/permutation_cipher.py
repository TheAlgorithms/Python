"""
The Permutation Cipher, implemented above, is a simple encryption
technique that rearranges the characters in a message based on a secret key.
It divides the message into blocks and applies a permutation to the characters
within each block according to the key. The key is a sequence of unique integers
that determine the order of character rearrangement. For more info read:-
https://www.nku.edu/~christensen/1402%20permutation%20ciphers.pdf

"""
import random


def generate_valid_block_size(message_length) -> int:
    """
    Generate a valid block size that is a factor of the message length.

    Args:
        message_length (int): The length of the message.

    Returns:
        int: A valid block size.

    Example:
        generate_valid_block_size(12)

    """
    while True:
        block_size = random.randint(2, message_length)
        if message_length % block_size == 0:
            return block_size


def generate_permutation_key(block_size) -> list:
    """
    Generate a random permutation key of a specified block size.

    Args:
        block_size (int): The size of each permutation block.

    Returns:
        list[int]: A list containing a random permutation of digits.

    Example:
        generate_permutation_key(4)

    """
    digits = list(range(1, block_size + 1))
    random.shuffle(digits)
    key = digits
    return key


def encrypt(message, key, block_size) -> str:
    """
    Encrypt a message using a permutation cipher with block rearrangement using a key.

    Args:
        message (str): The plaintext message to be encrypted.

    Returns:
        str: The encrypted message.
        list[int]: The encryption key.

    Example:
        >>> encrypted_message, key = encrypt("HELLO WORLD")
        >>> decrypted_message = decrypt(encrypted_message, key)
        >>> decrypted_message
        'HELLO WORLD'
    """
    message = message.upper()
    message_length = len(message)
    encrypted_message = ""

    for i in range(0, message_length, block_size):
        block = message[i : i + block_size]
        rearranged_block = [block[digit - 1] for digit in key]
        encrypted_message += "".join(rearranged_block)

    return encrypted_message


def decrypt(encrypted_message, key) -> str:
    """
    Decrypt an encrypted message using a permutation cipher with block rearrangement.

    Args:
        encrypted_message (str): The encrypted message.
        key (list[int]): The permutation key for decryption.

    Returns:
        str: The decrypted plaintext message.

    Example:
        >>> encrypted_message, key = encrypt("HELLO WORLD")
        >>> decrypted_message = decrypt(encrypted_message, key)
        >>> decrypted_message
        'HELLO WORLD'
    """
    key_length = len(key)
    decrypted_message = ""

    for i in range(0, len(encrypted_message), key_length):
        block = encrypted_message[i : i + key_length]
        original_block = [""] * key_length
        for j, digit in enumerate(key):
            original_block[digit - 1] = block[j]
        decrypted_message += "".join(original_block)

    return decrypted_message


def main() -> None:
    message = "HELLO WORLD"

    block_size = generate_valid_block_size(len(message))
    key = generate_permutation_key(block_size)
    encrypted_message = encrypt(message, key, block_size)
    print(f"Encrypted message: {encrypted_message}")

    decrypted_message = decrypt(encrypted_message, key)
    print(f"Decrypted message: {decrypted_message}")


if __name__ == "__main__":
    main()
