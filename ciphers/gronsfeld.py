def gronsfeld_encrypt(plaintext, key):
    """
    Encrypts a plaintext using the Gronsfeld cipher.

    Parameters:
    plaintext (str): The message to be encrypted.
    key (str): A numeric key used for encryption (e.g., "31415").

    Returns:
    str: The encrypted message.
    """
    ciphertext = ""
    key = [int(k) for k in key]
    key_length = len(key)

    for i, letter in enumerate(plaintext):
        if letter.isalpha():
            shift = key[i % key_length]
            base = ord("A") if letter.isupper() else ord("a")
            # Shift and wrap around the alphabet
            ciphertext += chr((ord(letter) - base + shift) % 26 + base)
        else:
            ciphertext += letter

    return ciphertext


def gronsfeld_decrypt(ciphertext, key):
    """
    Decrypts a ciphertext using the Gronsfeld cipher.

    Parameters:
    ciphertext (str): The message to be decrypted.
    key (str): A numeric key used for decryption (e.g., "31415").

    Returns:
    str: The decrypted message.
    """
    plaintext = ""
    key = [int(k) for k in key]
    key_length = len(key)

    for i, letter in enumerate(ciphertext):
        if letter.isalpha():
            shift = key[i % key_length]
            base = ord("A") if letter.isupper() else ord("a")
            # Reverse the shift to decrypt
            plaintext += chr((ord(letter) - base - shift) % 26 + base)
        else:
            plaintext += letter

    return plaintext


# Example usage:
plaintext = input("Enter a message to encrypt: ")
key = input("Enter a key (e.g., 31415): ")

encrypted_message = gronsfeld_encrypt(plaintext, key)
print(f"Encrypted: {encrypted_message}")

decrypted_message = gronsfeld_decrypt(encrypted_message, key)
print(f"Decrypted: {decrypted_message}")
