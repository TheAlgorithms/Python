"""
Hill Cipher Implementation

This module provides a complete implementation of the Hill Cipher algorithm,
which uses linear algebra techniques for text encryption and decryption.
The cipher supports alphanumeric characters (A-Z, 0-9) and uses modular
arithmetic with base 36.

Classes:
    HillCipher: Implements the Hill Cipher encryption and decryption operations.

Functions:
    main: Command-line interface for the Hill Cipher operations.

References:
    https://apprendre-en-ligne.net/crypto/hill/Hillciph.pdf
    https://www.youtube.com/watch?v=kfmNeskzs2o
    https://www.youtube.com/watch?v=4RhLNDqcjpA
"""

import string

import numpy as np
from maths.greatest_common_divisor import greatest_common_divisor


class HillCipher:
    """
    Implementation of the Hill Cipher algorithm using matrix operations.

    Attributes:
        key_string (str): String of valid characters (A-Z and 0-9)
        modulus (function): Vectorized function for mod 36 operation
        to_int (function): Vectorized rounding function
        encrypt_key (np.ndarray): Encryption key matrix
        break_key (int): Size of the encryption key matrix (N x N)

    Methods:
        replace_letters: Convert character to numerical value
        replace_digits: Convert numerical value to character
        check_determinant: Validate encryption key determinant
        process_text: Prepare text for encryption/decryption
        encrypt: Encrypt plaintext using Hill Cipher
        make_decrypt_key: Compute decryption key matrix
        decrypt: Decrypt ciphertext using Hill Cipher
    """

    key_string = string.ascii_uppercase + string.digits
    modulus = np.vectorize(lambda x: x % 36)
    to_int = np.vectorize(round)

    def __init__(self, encrypt_key: np.ndarray) -> None:
        """
        Initialize Hill Cipher with encryption key matrix.

        Args:
            encrypt_key: Square matrix used for encryption

        Raises:
            ValueError: If encryption key is invalid

        Examples:
            >>> key = np.array([[2, 5], [1, 6]])
            >>> cipher = HillCipher(key)
            >>> cipher.break_key
            2
        """
        self.encrypt_key = self.modulus(encrypt_key)
        self.check_determinant()
        self.break_key = encrypt_key.shape[0]

    def replace_letters(self, letter: str) -> int:
        """
        Convert character to its numerical equivalent.

        Args:
            letter: Character to convert (A-Z or 0-9)

        Returns:
            Numerical value (0-35)

        Examples:
            >>> key = np.array([[2, 5], [1, 6]])
            >>> cipher = HillCipher(key)
            >>> cipher.replace_letters('A')
            0
            >>> cipher.replace_letters('Z')
            25
            >>> cipher.replace_letters('0')
            26
            >>> cipher.replace_letters('9')
            35
        """
        return self.key_string.index(letter)

    def replace_digits(self, num: int) -> str:
        """
        Convert numerical value to its character equivalent.

        Args:
            num: Numerical value (0-35)

        Returns:
            Character equivalent (A-Z or 0-9)

        Examples:
            >>> key = np.array([[2, 5], [1, 6]])
            >>> cipher = HillCipher(key)
            >>> cipher.replace_digits(0)
            'A'
            >>> cipher.replace_digits(25)
            'Z'
            >>> cipher.replace_digits(26)
            '0'
            >>> cipher.replace_digits(35)
            '9'
        """
        return self.key_string[round(num)]

    def check_determinant(self) -> None:
        """
        Validate encryption key determinant.

        The determinant must be coprime with 36 for the key to be valid.

        Raises:
            ValueError: If determinant is not coprime with 36

        Examples:
            >>> key = np.array([[2, 5], [1, 6]])
            >>> cipher = HillCipher(key)  # Valid key

            >>> invalid_key = np.array([[2, 2], [1, 1]])
            >>> HillCipher(invalid_key)  # Determinant 0
            Traceback (most recent call last):
            ...
            ValueError: determinant modular 36 of encryption key(0) is not co prime
            w.r.t 36. Try another key.

            >>> invalid_key2 = np.array([[4, 2], [6, 3]])
            >>> HillCipher(invalid_key2)  # Determinant 0
            Traceback (most recent call last):
            ...
            ValueError: determinant modular 36 of encryption key(0) is not co prime
            w.r.t 36. Try another key.
        """
        det = round(np.linalg.det(self.encrypt_key))
        det = int(det)  # Convert to int after rounding float

        if det < 0:
            det = det % len(self.key_string)

        req_l = len(self.key_string)
        if greatest_common_divisor(det, req_l) != 1:
            msg = (
                f"determinant modular {req_l} of encryption key({det}) is not co prime "
                f"w.r.t {req_l}.\nTry another key."
            )
            raise ValueError(msg)

    def process_text(self, text: str) -> str:
        """
        Prepare text for encryption/decryption by:
        1. Converting to uppercase
        2. Removing invalid characters
        3. Padding with last character to make length multiple of key size

        Args:
            text: Text to process

        Returns:
            Processed text ready for encryption/decryption

        Examples:
            >>> key = np.array([[2, 5], [1, 6]])
            >>> cipher = HillCipher(key)
            >>> cipher.process_text('Test!123')
            'TEST123'
            >>> cipher.process_text('hello')
            'HELLOO'
            >>> cipher.process_text('a')
            'AA'
            >>> cipher.process_text('abc')
            'ABCC'
        """
        chars = [char for char in text.upper() if char in self.key_string]

        # Handle empty input case
        if not chars:
            return ""

        last = chars[-1]
        while len(chars) % self.break_key != 0:
            chars.append(last)

        return "".join(chars)

    def encrypt(self, text: str) -> str:
        """
        Encrypt plaintext using Hill Cipher.

        Args:
            text: Plaintext to encrypt

        Returns:
            Encrypted ciphertext

        Examples:
            >>> key = np.array([[2, 5], [1, 6]])
            >>> cipher = HillCipher(key)
            >>> cipher.encrypt('Test')
            '4Q6J'
            >>> cipher.encrypt('Hello World')
            '85FF00V4ZAH8'
            >>> cipher.encrypt('ABC')
            'A0K'
            >>> cipher.encrypt('123')
            '0RZ'
            >>> cipher.encrypt('a')
            'PP'
        """
        text = self.process_text(text.upper())
        if not text:
            return ""

        encrypted = ""

        for i in range(0, len(text) - self.break_key + 1, self.break_key):
            # Extract batch of characters
            batch = text[i : i + self.break_key]

            # Convert to numerical vector
            vec = [self.replace_letters(char) for char in batch]
            batch_vec = np.array([vec]).T

            # Matrix multiplication and mod 36
            product = self.encrypt_key.dot(batch_vec)
            batch_encrypted = self.modulus(product).T.tolist()[0]

            # Convert back to characters
            encrypted_batch = "".join(
                self.replace_digits(num) for num in batch_encrypted
            )
            encrypted += encrypted_batch

        return encrypted

    def make_decrypt_key(self) -> np.ndarray:
        """
        Compute decryption key matrix from encryption key.

        Returns:
            Decryption key matrix

        Raises:
            ValueError: If modular inverse doesn't exist

        Examples:
            >>> key = np.array([[2, 5], [1, 6]])
            >>> cipher = HillCipher(key)
            >>> cipher.make_decrypt_key()
            array([[ 6, 25],
                   [ 5, 26]])

            >>> key3x3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
            >>> cipher3 = HillCipher(key3x3)
            >>> cipher3.make_decrypt_key()  # Determinant 0 should be invalid
            Traceback (most recent call last):
            ...
            ValueError: determinant modular 36 of encryption key(0) is not co prime
            w.r.t 36. Try another key.
        """
        det = round(np.linalg.det(self.encrypt_key))
        det = int(det)  # Convert to int after rounding float

        if det < 0:
            det = det % len(self.key_string)

        det_inv: int | None = None
        for i in range(len(self.key_string)):
            if (det * i) % len(self.key_string) == 1:
                det_inv = i
                break

        if det_inv is None:
            raise ValueError("Modular inverse does not exist for decryption key")

        det_float = np.linalg.det(self.encrypt_key)
        inv_key = det_inv * det_float * np.linalg.inv(self.encrypt_key)
        return self.to_int(self.modulus(inv_key))

    def decrypt(self, text: str) -> str:
        """
        Decrypt ciphertext using Hill Cipher.

        Args:
            text: Ciphertext to decrypt

        Returns:
            Decrypted plaintext

        Examples:
            >>> key = np.array([[2, 5], [1, 6]])
            >>> cipher = HillCipher(key)
            >>> cipher.decrypt('4Q6J')
            'TEST'
            >>> cipher.decrypt('85FF00V4ZAH8')
            'HELLOWORLDD'
            >>> cipher.decrypt('A0K')
            'ABCC'
            >>> cipher.decrypt('0RZ')
            '1233'
            >>> cipher.decrypt('PP')
            'AA'
            >>> cipher.decrypt('')
            ''
        """
        text = self.process_text(text.upper())
        if not text:
            return ""

        decrypt_key = self.make_decrypt_key()
        decrypted = ""

        for i in range(0, len(text) - self.break_key + 1, self.break_key):
            # Extract batch of characters
            batch = text[i : i + self.break_key]

            # Convert to numerical vector
            vec = [self.replace_letters(char) for char in batch]
            batch_vec = np.array([vec]).T

            # Matrix multiplication and mod 36
            product = decrypt_key.dot(batch_vec)
            batch_decrypted = self.modulus(product).T.tolist()[0]

            # Convert back to characters
            decrypted_batch = "".join(
                self.replace_digits(num) for num in batch_decrypted
            )
            decrypted += decrypted_batch

        return decrypted


def main() -> None:
    """
    Command-line interface for Hill Cipher operations.

    Steps:
    1. User inputs encryption key size
    2. User inputs encryption key matrix rows
    3. User chooses encryption or decryption
    4. User inputs text to process
    5. Program outputs result
    """
    n = int(input("Enter the order of the encryption key: "))
    hill_matrix = []

    print("Enter each row of the encryption key with space separated integers")
    for i in range(n):
        row = [int(x) for x in input(f"Row {i + 1}: ").split()]
        hill_matrix.append(row)

    hc = HillCipher(np.array(hill_matrix))

    print("\nWould you like to encrypt or decrypt some text?")
    option = input("1. Encrypt\n2. Decrypt\nEnter choice (1/2): ")

    if option == "1":
        text = input("\nEnter text to encrypt: ")
        print("\nEncrypted text:")
        print(hc.encrypt(text))
    elif option == "2":
        text = input("\nEnter text to decrypt: ")
        print("\nDecrypted text:")
        print(hc.decrypt(text))
    else:
        print("Invalid option selected")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("\nRunning sample tests...")
    key = np.array([[2, 5], [1, 6]])
    cipher = HillCipher(key)

    # Test encryption/decryption round trip
    plaintext = "HELLO123"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)

    print(f"\nOriginal text: {plaintext}")
    print(f"Encrypted text: {encrypted}")
    print(f"Decrypted text: {decrypted}")

    # Run CLI interface
    main()
