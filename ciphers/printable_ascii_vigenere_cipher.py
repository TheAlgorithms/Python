"""
This program encrypts or decrypts messages using a modified Vigenere cipher
that operates on all printable ASCII characters (from 32-126) instead of just letters.
Each character in the message is shifted by a value derived from the corresponding
character in the key. When the end of the key is reached, it repeats cyclically.

Algorithm summary:
- For each printable character:
    * Convert both the message and key characters to their ASCII codes.
    * During encryption: add the key's ASCII value to the message character.
    * During decryption: subtract the key's ASCII value from the message character.
    * Wrap the result within the printable ASCII range using modulo arithmetic.
- Non-printable characters are left unchanged.
- The key repeats automatically to match the message length.

Reference: https://stackoverflow.com/questions/28182091/ascii-vigenere-cipher-implementation-in-java
"""

PRINTABLE_START = 32
PRINTABLE_END = 126
PRINTABLE_RANGE = PRINTABLE_END - PRINTABLE_START + 1


def encrypt_message(key: str, message: str) -> str:
    """
    Encrypts a message using printable ASCII Vigenere cipher.

    >>> encrypt_message('key', 'Hello!')
    "Tk'xu;"
    >>> encrypt_message('SUpeR$eCR3t_KEY', 'This is a message to encrypt.')
    'H^zyr.ycTS#e_Y[[[1zbDkRVF/p`s'
    """
    return translate_message(key, message, "encrypt")


def decrypt_message(key: str, message: str) -> str:
    """
    Decrypts a message using printable ASCII Vigenere cipher.

    >>> decrypt_message('key', "Tk'xu;")
    'Hello!'
    >>> decrypt_message('SUpeR$eCR3t_KEY', 'H^zyr.ycTS#e_Y[[[1zbDkRVF/p`s')
    'This is a message to encrypt.'
    """
    return translate_message(key, message, "decrypt")


def translate_message(key: str, message: str, mode: str) -> str:
    """
    Translates (encrypts or decrypts) a message using the given key.

    >>> translate_message('key', 'Hello!', 'encrypt')
    "Tk'xu;"
    >>> translate_message('key', "Tk'xu;", 'decrypt')
    'Hello!'
    """
    translated = []
    key_index = 0
    key_bytes = [ord(ch) for ch in key]

    for symbol in message:
        sym_val = ord(symbol)

        if PRINTABLE_START <= sym_val <= PRINTABLE_END:
            key_val = key_bytes[key_index]

            if mode == "encrypt":
                new_val = (
                    sym_val - PRINTABLE_START + key_val
                ) % PRINTABLE_RANGE + PRINTABLE_START
            elif mode == "decrypt":
                new_val = (
                    sym_val - PRINTABLE_START - key_val
                ) % PRINTABLE_RANGE + PRINTABLE_START
            else:
                raise ValueError("Mode must be 'encrypt' or 'decrypt'")

            translated.append(chr(new_val))

            key_index = (key_index + 1) % len(key_bytes)
        else:
            translated.append(symbol)

    return "".join(translated)


if __name__ == "__main__":
    message = input("Enter message: ")
    key = input("Enter secret key: ")
    mode = input("Encrypt/Decrypt [e/d]: ")

    if mode.lower().startswith("e"):
        mode = "encrypt"
        translated = encrypt_message(key, message)

        print(f"Encrypted message: {translated}")
    elif mode.lower().startswith("d"):
        mode = "decrypt"
        translated = decrypt_message(key, message)

        print(f"Decrypted message: {translated}")
    else:
        print("Invalid mode. Use 'e' or 'd'.")
