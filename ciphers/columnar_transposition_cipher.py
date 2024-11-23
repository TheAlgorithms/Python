import math


def encrypt_columnar_cipher(message: str, key: str) -> str:
    """
    Encrypts a message using the Columnar Transposition Cipher.

    :param message: Text to encrypt.
    :param key: String key used to define column order.
    :return: Encrypted message.
    """
    # Remove spaces and calculate dimensions
    message = message.replace(" ", "")
    num_cols = len(key)
    num_rows = math.ceil(len(message) / num_cols)

    # Fill the grid with characters
    grid = [""] * num_cols
    for i, char in enumerate(message):
        grid[i % num_cols] += char

    # Sort columns based on the key order
    sorted_key_indices = sorted(range(len(key)), key=lambda k: key[k])
    ciphertext = "".join([grid[i] for i in sorted_key_indices])

    return ciphertext


def decrypt_columnar_cipher(ciphertext: str, key: str) -> str:
    """
    Decrypts a message encrypted with the Columnar Transposition Cipher.

    :param ciphertext: Encrypted text.
    :param key: String key used to define column order.
    :return: Decrypted message.
    """
    num_cols = len(key)
    num_rows = math.ceil(len(ciphertext) / num_cols)
    num_shaded_boxes = (num_cols * num_rows) - len(ciphertext)

    # Sort columns based on the key order
    sorted_key_indices = sorted(range(len(key)), key=lambda k: key[k])
    col_lengths = [num_rows] * num_cols
    for i in range(num_shaded_boxes):
        col_lengths[sorted_key_indices[-(i + 1)]] -= 1

    # Distribute ciphertext into columns based on the sorted key
    grid = []
    start = 0
    for col_length in col_lengths:
        grid.append(ciphertext[start : start + col_length])
        start += col_length

    # Rebuild plaintext row by row
    plaintext = ""
    for i in range(num_rows):
        for j in range(num_cols):
            if i < len(grid[sorted_key_indices[j]]):
                plaintext += grid[sorted_key_indices[j]][i]

    return plaintext


# Example usage
message = "HELLO WORLD FROM COLUMNAR"
key = "3412"

# Encrypt the message
encrypted = encrypt_columnar_cipher(message, key)
print("Encrypted:", encrypted)

# Decrypt the message
decrypted = decrypt_columnar_cipher(encrypted, key)
print("Decrypted:", decrypted)
