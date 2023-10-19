"""
RC4 (Rivest Cipher 4) Algorithm:
The 'RC4' class below implements the RC4 stream cipher algorithm, also known as the Rivest Cipher 4.
RC4 generates a pseudorandom stream of bits (keystream) based on an initial secret key.
It is used for both encryption and decryption by XORing the plaintext with the keystream.

Algorithm:
1. Key Scheduling: Initialize the S-box (state array) based on the secret key.
2. Stream Generation: Generate the keystream based on the S-box.
3. Encryption: XOR the plaintext with the keystream to produce the ciphertext.
4. Decryption: Decryption is the same as encryption, as RC4 is a symmetric cipher.

References:
https://en.wikipedia.org/wiki/RC4
https://tools.ietf.org/html/rfc6229
"""


class RC4:
    def __init__(self, key: bytes):
        """
        Initialize the RC4 cipher with a secret key.

        Args:
            key (bytes): The secret key.

        Example:
        >>> key = b"SecretKey"
        >>> rc4 = RC4(key)
        """
        self.S = list(range(256))
        self.j = 0
        self.key_setup(key)

    def key_setup(self, key: bytes):
        """
        Key Scheduling: Initialize the S-box based on the secret key.

        Args:
            key (bytes): The secret key.

        Example:
        >>> key = b"SecretKey"
        >>> rc4 = RC4(key)
        >>> rc4.key_setup(key)
        """
        key_length = len(key)
        for i in range(256):
            self.j = (self.j + self.S[i] + key[i % key_length]) % 256
            self.S[i], self.S[self.j] = self.S[self.j], self.S[i]

    def generate_keystream(self, message_length: int) -> list[int]:
        """
        Generate the keystream for encryption/decryption.

        Args:
            message_length (int): Length of the message.

        Returns:
            list[int]: List of keystream values.

        Example:
        >>> key = b"SecretKey"
        >>> rc4 = RC4(key)
        >>> keystream = rc4.generate_keystream(10)
        """
        keystream = []
        i = 0
        j = 0
        for _ in range(message_length):
            i = (i + 1) % 256
            j = (j + self.S[i]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]
            k = self.S[(self.S[i] + self.S[j]) % 256]
            keystream.append(k)
        return keystream

    def encrypt(self, message: str) -> bytes:
        """
        Encrypt a message using the RC4 algorithm.

        Args:
            message (str): The plaintext message to be encrypted.

        Returns:
            bytes: The encrypted message.

        Example:
        >>> key = b"SecretKey"
        >>> rc4 = RC4(key)
        >>> plaintext = "Hello, RC4!"
        >>> encrypted = rc4.encrypt(plaintext)
        """
        keystream = self.generate_keystream(len(message))
        encrypted_message = []
        for i in range(len(message)):
            encrypted_char = ord(message[i]) ^ keystream[i]
            encrypted_message.append(encrypted_char)
        return bytes(encrypted_message)

    def decrypt(self, encrypted_message: bytes) -> str:
        """
        Decrypt an encrypted message using the RC4 algorithm.

        Args:
            encrypted_message (bytes): The encrypted message.

        Returns:
            str: The decrypted plaintext message.

        Example:
        >>> key = b"SecretKey"
        >>> rc4 = RC4(key)
        >>> plaintext = "Hello, RC4!"
        >>> encrypted = rc4.encrypt(plaintext)
        >>> decrypted = rc4.decrypt(encrypted)
        """
        return self.encrypt(
            encrypted_message
        )  # RC4 decryption is the same as encryption


def main():
    key = b"SecretKey"  # Replace with your secret key
    plaintext = "Hello, RC4!"  # Replace with your message

    rc4 = RC4(key)

    encrypted = rc4.encrypt(plaintext)
    decrypted = rc4.decrypt(encrypted)

    print("Original message:", plaintext)
    print("Encrypted message:", encrypted)
    print("Decrypted message:", decrypted.decode("utf-8"))


if __name__ == "__main__":
    main()
