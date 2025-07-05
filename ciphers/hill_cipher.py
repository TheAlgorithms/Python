"""
Hill Cipher Implementation with Exact Integer Arithmetic

This implementation uses integer-only calculations to avoid floating-point errors
and ensure cryptographic correctness. All matrix operations are performed using
exact integer arithmetic.
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
        encrypt_key (np.ndarray): Encryption key matrix
        break_key (int): Size of the encryption key matrix (N x N)
    """

    key_string = string.ascii_uppercase + string.digits
    modulus = np.vectorize(lambda x: x % 36)

    def __init__(self, encrypt_key: np.ndarray) -> None:
        """
        Initialize Hill Cipher with encryption key matrix.

        Args:
            encrypt_key: Square matrix used for encryption

        Raises:
            ValueError: If encryption key is invalid
        """
        self.encrypt_key = self.modulus(encrypt_key).astype(int)
        self.check_determinant()
        self.break_key = encrypt_key.shape[0]

    def replace_letters(self, letter: str) -> int:
        """
        Convert character to its numerical equivalent.
        """
        return self.key_string.index(letter)

    def replace_digits(self, num: int) -> str:
        """
        Convert numerical value to its character equivalent.
        """
        return self.key_string[num]
    def integer_determinant(self, matrix: np.ndarray) -> int:
        """
        Calculate determinant of an integer matrix using exact arithmetic.
        """
        n = matrix.shape[0]
        
        # Base case for 1x1 matrix
        if n == 1:
            return matrix[0, 0]
        
        # Base case for 2x2 matrix
        if n == 2:
            return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
        
        det = 0
        for j in range(n):
            # Create minor matrix by removing first row and j-th column
            minor = matrix[1:, :]
            minor = np.delete(minor, j, axis=1)
            
            # Recursively calculate determinant of minor
            minor_det = self.integer_determinant(minor)
            
            # Calculate cofactor with sign
            sign = (-1) ** j
            det += sign * matrix[0, j] * minor_det
            
        return det

    def check_determinant(self) -> None:
        """
        Validate encryption key determinant.

        The determinant must be coprime with 36 for the key to be valid.

        Raises:
            ValueError: If determinant is not coprime with 36
        """
        det = self.integer_determinant(self.encrypt_key)
        
        # Ensure positive modulo value
        det_mod = det % len(self.key_string)
        if det_mod == 0:
            det_mod = len(self.key_string)

        if greatest_common_divisor(det_mod, len(self.key_string)) != 1:
            msg = (
                f"determinant modular {len(self.key_string)} of encryption key({det}) "
                f"is not co prime w.r.t {len(self.key_string)}. Try another key."
            )
            raise ValueError(msg)

    def process_text(self, text: str) -> str:
        """
        Prepare text for encryption/decryption.
        """
        chars = [char for char in text.upper() if char in self.key_string]
        
        if not chars:
            return ""
            
        last = chars[-1]
        while len(chars) % self.break_key != 0:
            chars.append(last)
            
        return "".join(chars)

    def encrypt(self, text: str) -> str:
        """
        Encrypt plaintext using Hill Cipher.
        """
        text = self.process_text(text.upper())
        if not text:
            return ""
            
        encrypted = ""

        for i in range(0, len(text), self.break_key):
            batch = text[i:i+self.break_key]
            vec = [self.replace_letters(char) for char in batch]
            batch_vec = np.array(vec).reshape(-1, 1)
            
            product = self.encrypt_key @ batch_vec
            batch_encrypted = self.modulus(product).flatten().astype(int)
            
            encrypted_batch = "".join(
                self.replace_digits(num) for num in batch_encrypted
            )
            encrypted += encrypted_batch

        return encrypted

    def make_decrypt_key(self) -> np.ndarray:
        """
        Compute decryption key matrix from encryption key.
        """
        n = self.break_key
        det = self.integer_determinant(self.encrypt_key)
        modulus = len(self.key_string)
        
        # Find modular inverse of determinant
        det_mod = det % modulus
        det_inv = None
        for i in range(1, modulus):
            if (det_mod * i) % modulus == 1:
                det_inv = i
                break

        if det_inv is None:
            raise ValueError("Modular inverse does not exist")

        # Compute adjugate matrix
        adjugate = np.zeros((n, n), dtype=int)
        
        for i in range(n):
            for j in range(n):
                minor = np.delete(self.encrypt_key, i, axis=0)
                minor = np.delete(minor, j, axis=1)
                minor_det = self.integer_determinant(minor)
                sign = (-1) ** (i + j)
                adjugate[j, i] = sign * minor_det  # Transposed assignment

        # Apply modular inverse and mod operation
        inv_key = (det_inv * adjugate) % modulus
        return inv_key

    def decrypt(self, text: str) -> str:
        """
        Decrypt ciphertext using Hill Cipher.
        """
        text = self.process_text(text.upper())
        if not text:
            return ""
            
        decrypt_key = self.make_decrypt_key()
        decrypted = ""

        for i in range(0, len(text), self.break_key):
            batch = text[i:i+self.break_key]
            vec = [self.replace_letters(char) for char in batch]
            batch_vec = np.array(vec).reshape(-1, 1)
            
            product = decrypt_key @ batch_vec
            batch_decrypted = self.modulus(product).flatten().astype(int)
            
            decrypted_batch = "".join(
                self.replace_digits(num) for num in batch_decrypted
            )
            decrypted += decrypted_batch

        return decrypted



def main() -> None:
    """
    Command-line interface for Hill Cipher operations.
    """
    n = int(input("Enter the order of the encryption key: "))
    hill_matrix = []

    print("Enter each row of the encryption key with space separated integers")
    for i in range(n):
        row = [int(x) for x in input(f"Row {i+1}: ").split()]
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
