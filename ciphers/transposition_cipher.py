import math

"""
In cryptography, the TRANSPOSITION cipher is a method of encryption where the
positions of plaintext are shifted a certain number (determined by the key) that
follows a regular system that results in the permuted text, known as the encrypted
text. The type of transposition cipher demonstrated under is the ROUTE cipher.
"""

def main() -> None:
    message = input("Enter message: ").strip()
    if not message:
        print("Message cannot be empty.")
        return

    try:
        key = int(input(f"Enter key [2-{len(message) - 1}]: "))
        if key < 2 or key >= len(message):
            raise ValueError
    except ValueError:
        print("Invalid key. Please enter an integer within the specified range.")
        return

    mode = input("Encryption/Decryption [e/d]: ").strip().lower()
    if mode not in ['e', 'd']:
        print("Invalid mode. Please enter 'e' for encryption or 'd' for decryption.")
        return

    if mode == "e":
        text = encrypt_message(key, message)
    else:
        text = decrypt_message(key, message)

    # Append pipe symbol (vertical bar) to identify spaces at the end.
    print(f"Output:\n{text + '|'}")

def encrypt_message(key: int, message: str) -> str:
    """
    >>> encrypt_message(6, 'Harshil Darji')
    'Hlia rDsahrij'
    """
    cipher_text = [""] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipher_text[col] += message[pointer]
            pointer += key
    return "".join(cipher_text)

def decrypt_message(key: int, message: str) -> str:
    """
    >>> decrypt_message(6, 'Hlia rDsahrij')
    'Harshil Darji'
    """
    num_cols = math.ceil(len(message) / key)
    num_rows = key
    num_shaded_boxes = (num_cols * num_rows) - len(message)
    plain_text = [""] * num_cols
    col = 0
    row = 0

    for symbol in message:
        plain_text[col] += symbol
        col += 1

        if (
            (col == num_cols)
            or (col == num_cols - 1)
            and (row >= num_rows - num_shaded_boxes)
        ):
            col = 0
            row += 1

    return "".join(plain_text)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()