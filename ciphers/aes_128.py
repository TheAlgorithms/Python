import base64
from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad



'''
AES (Advanced Encryption Standard) is a symmetric encryption algorithm used 
    for secure data encryption. AES-128 uses a 128-bit key to encrypt and decrypt 
    data blocks of 128 bits. This implementation uses Cipher Block Chaining (CBC) mode 
    with PKCS7 padding for encrypting messages.

    For more details, visit: 
    https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
'''



def aes_encrypt(plaintext: str, key: str) -> str:
    """
    AES-128 Encryption using CBC mode and PKCS7 padding.

    :param plaintext: The plaintext message to be encrypted.
    :param key: The encryption key (16 characters = 128 bits).
    :return: Encrypted message (Base64 encoded).

    >>> msg = "This is a secret message."
    >>> key = "thisisaverysecret"
    >>> enc = aes_encrypt(msg, key)
    >>> dec = aes_decrypt(enc, key)
    >>> aes_decrypt(enc, key) == msg
    True
    """
    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode("utf-8"), AES.block_size))
    return base64.b64encode(cipher.iv + ciphertext).decode("utf-8")


def aes_decrypt(ciphertext: str, key: str) -> str:
    """
    AES-128 Decryption using CBC mode and PKCS7 padding.

    :param ciphertext: The Base64 encoded encrypted message.
    :param key: The decryption key (16 characters = 128 bits).
    :return: Decrypted plaintext message.

    >>> msg = "This is a secret message."
    >>> key = "thisisaverysecret"
    >>> enc = aes_encrypt(msg, key)
    >>> dec = aes_decrypt(enc, key)
    >>> dec == msg
    True
    """
    raw = base64.b64decode(ciphertext)
    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv=raw[: AES.block_size])
    return unpad(cipher.decrypt(raw[AES.block_size :]), AES.block_size).decode("utf-8")


def main() -> None:
    key = input("Enter 16-character key (AES-128): ")
    if len(key) != 16:
        raise ValueError("Key must be 16 characters long!")

    message = input("Enter message: ")

    # Encryption
    encrypted_message = aes_encrypt(message, key)
    print("Encrypted message:", encrypted_message)

    # Decryption
    decrypted_message = aes_decrypt(encrypted_message, key)
    print("Decrypted message:", decrypted_message)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
