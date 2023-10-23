def running_key_encrypt(key: str, plaintext: str) -> str:
    """
    Encrypts the plaintext using the Running Key Cipher.

    :param key: The running key (long piece of text).
    :param plaintext: The plaintext to be encrypted.
    :return: The ciphertext.
    """
    plaintext = plaintext.replace(" ", "").upper()
    key = key.replace(" ", "").upper()
    key_length = len(key)
    ciphertext = []

    for i in range(len(plaintext)):
        p = ord(plaintext[i]) - ord("A")
        k = ord(key[i % key_length]) - ord("A")
        c = (p + k) % 26
        ciphertext.append(chr(c + ord("A")))

    return "".join(ciphertext)


def running_key_decrypt(key: str, ciphertext: str) -> str:
    """
    Decrypts the ciphertext using the Running Key Cipher.

    :param key: The running key (long piece of text).
    :param ciphertext: The ciphertext to be decrypted.
    :return: The plaintext.
    """
    ciphertext = ciphertext.replace(" ", "").upper()
    key = key.replace(" ", "").upper()
    key_length = len(key)
    plaintext = []

    for i in range(len(ciphertext)):
        c = ord(ciphertext[i]) - ord("A")
        k = ord(key[i % key_length]) - ord("A")
        p = (c - k) % 26
        plaintext.append(chr(p + ord("A")))

    return "".join(plaintext)


def test_running_key_encrypt():
    """
    >>> key = "How does the duck know that? said Victor"
    >>> plaintext = "DEFEND THIS"
    >>> ciphertext = running_key_encrypt(key, plaintext)
    >>> decrypted_text = running_key_decrypt(key, ciphertext)
    >>> decrypted_text == "DEFENDTHIS"
    True
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_running_key_encrypt()

    key = "How does the duck know that? said Victor"
    plaintext = input("Enter the plaintext: ").upper()
    encrypted_text = running_key_encrypt(key, plaintext)
    decrypted_text = running_key_decrypt(key, encrypted_text)

    print("\nPlaintext:", plaintext)
    print("Encrypted:", encrypted_text)
    print("Decrypted:", decrypted_text)
