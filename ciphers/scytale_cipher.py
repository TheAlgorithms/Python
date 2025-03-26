def encrypt_scytale_cipher(message: str, key: int) -> str:
    """
    Encrypts a message using the Scytale Cipher.

    :param message: Text to encrypt.
    :param key: Number of rows (key).
    :return: Encrypted message.
    """
    message = message.replace(" ", "")  # Optional: remove spaces
    ciphertext = [""] * key

    # Distribute characters across rows based on the key
    for i in range(len(message)):
        ciphertext[i % key] += message[i]

    return "".join(ciphertext)


def decrypt_scytale_cipher(ciphertext: str, key: int) -> str:
    """
    Decrypts a message encrypted with the Scytale Cipher.

    :param ciphertext: Encrypted text.
    :param key: Number of rows (key).
    :return: Decrypted message.
    """
    num_cols = -(-len(ciphertext) // key)  # Calculate number of columns (round up)
    num_rows = key
    num_shaded_boxes = (num_cols * num_rows) - len(ciphertext)  # Extra unused boxes

    plaintext = [""] * num_cols
    col = 0
    row = 0

    # Rebuild the plaintext row by row
    for char in ciphertext:
        plaintext[col] += char
        col += 1
        # Reset column and move to next row if end of column is reached
        if (col == num_cols) or (
            col == num_cols - 1 and row >= num_rows - num_shaded_boxes
        ):
            col = 0
            row += 1

    return "".join(plaintext)


# Example usage
message = "HELLO WORLD FROM SCYTALE"
key = 5

# Encrypt the message
ciphered = encrypt_scytale_cipher(message, key)
print("Encrypted:", ciphered)

# Decrypt the message
deciphered = decrypt_scytale_cipher(ciphered, key)
print("Decrypted:", deciphered)
