from collections.abc import Generator


def ksa(key: bytes) -> list[int]:
    """
    Key Scheduling Algorithm (KSA)
    ==============================

    The KSA initializes the permutation in the array S (S-box) of size 256
    with values from 0 to 255. Then, it shuffles the array using the secret key.

    Parameters:
    -----------
    * `key`: The secret key used for encryption/decryption as a bytes object.

    Returns:
    --------
    * A list of 256 integers representing the permuted S-box.

    Doctests:
    =========
    >>> ksa(b"Key")[:5]
    [75, 51, 132, 157, 192]
    """
    s_box = list(range(256))
    j = 0
    key_length = len(key)
    for i in range(256):
        j = (j + s_box[i] + key[i % key_length]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
    return s_box


def prga(s_box: list[int]) -> Generator[int, None, None]:
    """
    Pseudo-Random Generation Algorithm (PRGA)
    =========================================

    The PRGA generates keystream bytes from the permuted S-box S.
    For each iteration, it modifies the S-box and outputs one byte of the keystream.

    Parameters:
    -----------
    * `s_box`: The permuted state array S-box.

    Yields:
    -------
    * An integer representing the next byte of the pseudo-random keystream.

    Doctests:
    =========
    >>> box = ksa(b"Key")
    >>> stream = prga(box)
    >>> [next(stream) for _ in range(5)]
    [235, 159, 119, 129, 183]
    """
    s = s_box.copy()
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        yield s[(s[i] + s[j]) % 256]


def encrypt(plaintext: bytes, key: bytes) -> bytes:
    """
    Encrypts/Decrypts the plaintext bytes with a key using the RC4 stream cipher.

    Parameters:
    -----------
    * `plaintext`: The input message to encrypt/decrypt (bytes).
    * `key`: The secret key (bytes).

    Returns:
    --------
    * The encrypted/decrypted result (bytes).

    More on RC4:
    ============
    RC4 (Rivest Cipher 4) is a symmetric stream cipher. Because it is symmetric,
    the encryption and decryption operations are identical. The cipher
    generates a pseudorandom stream of bytes (keystream) which is combined with
    the plaintext using bitwise exclusive-or (XOR).

    Warning:
    --------
    RC4 is cryptographically insecure and vulnerable to several attacks (such
    as keystream biases). It should not be used in secure systems today. It is
    implemented here purely for educational purposes.

    Further reading:
    ================
    * https://en.wikipedia.org/wiki/RC4

    Doctests:
    =========
    >>> encrypt(b"Plaintext", b"Key")
    b'\\xbb\\xf3\\x16\\xe8\\xd9@\\xaf\\n\\xd3'
    >>> encrypt(b"pedia", b"Wiki")
    b'\\x10!\\xbf\\x04 '
    >>> encrypt(b"\\x10!\\xbf\\x04 ", b"Wiki")
    b'pedia'
    """
    if not key:
        raise ValueError("Key must not be empty.")

    s_box = ksa(key)
    keystream = prga(s_box)
    return bytes(p ^ next(keystream) for p in plaintext)


def decrypt(ciphertext: bytes, key: bytes) -> bytes:
    """
    Decrypts the ciphertext bytes with a key using the RC4 stream cipher.

    Since RC4 is symmetric, decryption is identical to encryption.

    Parameters:
    -----------
    * `ciphertext`: The input cipher text to decrypt (bytes).
    * `key`: The secret key (bytes).

    Returns:
    --------
    * The decrypted plaintext (bytes).

    Doctests:
    =========
    >>> decrypt(b'\\x10!\\xbf\\x04 ', b"Wiki")
    b'pedia'
    """
    return encrypt(ciphertext, key)


if __name__ == "__main__":
    import sys

    # Check for doctests
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        import doctest
        doctest.testmod()
        sys.exit(0)

    print(f"\n{'-' * 10}\n RC4 Cipher Menu\n{'-' * 10}")
    print("1. Encrypt String")
    print("2. Decrypt Hex String")
    print("3. Quit")

    while True:
        choice = input("\nWhat would you like to do?: ").strip()
        if choice == "3" or not choice:
            print("Goodbye.")
            break
        elif choice == "1":
            plain_str = input("Enter plain text to encrypt: ")
            key_str = input("Enter key: ")
            if not key_str:
                print("Key cannot be empty!")
                continue
            encrypted_bytes = encrypt(plain_str.encode("utf-8"), key_str.encode("utf-8"))
            print(f"Ciphertext (Hex): {encrypted_bytes.hex()}")
        elif choice == "2":
            hex_str = input("Enter hex ciphertext to decrypt: ")
            key_str = input("Enter key: ")
            if not key_str:
                print("Key cannot be empty!")
                continue
            try:
                cipher_bytes = bytes.fromhex(hex_str)
                decrypted_bytes = decrypt(cipher_bytes, key_str.encode("utf-8"))
                print(f"Decrypted text: {decrypted_bytes.decode('utf-8', errors='replace')}")
            except ValueError as e:
                print(f"Invalid input: {e}")
        else:
            print("Invalid choice, please enter 1, 2, or 3.")
