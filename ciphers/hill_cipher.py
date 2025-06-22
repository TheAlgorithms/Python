"""
Hill Cipher:
The 'HillCipher' class below implements the Hill Cipher algorithm which uses
modern linear algebra techniques to encode and decode text using an encryption
key matrix.

Algorithm:
Let the order of the encryption key be N (as it is a square matrix).
Your text is divided into batches of length N and converted to numerical vectors
by a simple mapping starting with A=0 and so on.

The key is then multiplied with the newly created batch vector to obtain the
encoded vector. After each multiplication modular 36 calculations are performed
on the vectors so as to bring the numbers between 0 and 36 and then mapped with
their corresponding alphanumerics.

While decrypting, the decrypting key is found which is the inverse of the
encrypting key modular 36. The same process is repeated for decrypting to get
the original message back.

Constraints:
The determinant of the encryption key matrix must be relatively prime w.r.t 36.

Note:
This implementation only considers alphanumerics in the text.  If the length of
the text to be encrypted is not a multiple of the break key(the length of one
batch of letters), the last character of the text is added to the text until the
length of the text reaches a multiple of the break_key. So the text after
decrypting might be a little different than the original text.

References:
https://apprendre-en-ligne.net/crypto/hill/Hillciph.pdf
https://www.youtube.com/watch?v=kfmNeskzs2o
https://www.youtube.com/watch?v=4RhLNDqcjpA
"""

import string
import numpy as np
from maths.greatest_common_divisor import greatest_common_divisor


class HillCipher:
    key_string = string.ascii_uppercase + string.digits  # 36 alphanumeric chars
    modulus = np.vectorize(lambda x: x % 36)  # Mod 36 operation
    to_int = np.vectorize(round)  # Round to nearest integer

    def __init__(self, encrypt_key: np.ndarray) -> None:
        self.encrypt_key = self.modulus(encrypt_key)
        self.check_determinant()  # Validate key determinant
        self.break_key = encrypt_key.shape[0]  # Matrix order

    def replace_letters(self, letter: str) -> int:
        """Map char to index (A=0, Z=25, 0=26, 9=35)"""
        return self.key_string.index(letter)

    def replace_digits(self, num: int) -> str:
        """Map index back to char"""
        return self.key_string[num]

    def check_determinant(self) -> None:
        """Ensure det(key) is coprime with 36"""
        det = round(np.linalg.det(self.encrypt_key))
        if det < 0:
            det %= len(self.key_string)

        error_msg = f"Det {det} not coprime with 36. Try another key."
        if greatest_common_divisor(det, len(self.key_string)) != 1:
            raise ValueError(error_msg)

    def process_text(self, text: str) -> str:
        """Convert to uppercase, remove invalid chars, pad to multiple of break_key"""
        chars = [c for c in text.upper() if c in self.key_string]
        last = chars[-1] if chars else "A"
        while len(chars) % self.break_key != 0:
            chars.append(last)
        return "".join(chars)

    def encrypt(self, text: str) -> str:
        """Encrypt text using Hill cipher"""
        text = self.process_text(text.upper())
        encrypted = ""
        for i in range(0, len(text), self.break_key):
            batch = text[i : i + self.break_key]
            vec = [self.replace_letters(c) for c in batch]
            batch_vec = np.array([vec]).T
            batch_encrypted = self.modulus(self.encrypt_key.dot(batch_vec)).T.tolist()[
                0
            ]
            encrypted += "".join(self.replace_digits(round(n)) for n in batch_encrypted)
        return encrypted

    def make_decrypt_key(self) -> np.ndarray:
        """Calculate decryption key matrix"""
        det = round(np.linalg.det(self.encrypt_key))
        if det < 0:
            det %= len(self.key_string)

        # Find modular inverse of det
        det_inv = next(i for i in range(36) if (det * i) % 36 == 1)

        # Calculate inverse key
        inv_key = (
            det_inv * np.linalg.det(self.encrypt_key) * np.linalg.inv(self.encrypt_key)
        )
        return self.to_int(self.modulus(inv_key))

    def decrypt(self, text: str) -> str:
        """Decrypt text using Hill cipher"""
        decrypt_key = self.make_decrypt_key()
        text = self.process_text(text.upper())
        decrypted = ""
        for i in range(0, len(text), self.break_key):
            batch = text[i : i + self.break_key]
            vec = [self.replace_letters(c) for c in batch]
            batch_vec = np.array([vec]).T
            batch_decrypted = self.modulus(decrypt_key.dot(batch_vec)).T.tolist()[0]
            decrypted += "".join(self.replace_digits(round(n)) for n in batch_decrypted)
        return decrypted


def main() -> None:
    """CLI for Hill Cipher"""
    n = int(input("Enter key order: "))
    print(f"Enter {n} rows of space-separated integers:")
    matrix = [list(map(int, input().split())) for _ in range(n)]

    hc = HillCipher(np.array(matrix))

    option = input("1. Encrypt\n2. Decrypt\nChoose: ")
    text = input("Enter text: ")

    if option == "1":
        print("Encrypted:", hc.encrypt(text))
    elif option == "2":
        print("Decrypted:", hc.decrypt(text))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
