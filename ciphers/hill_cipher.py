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
    key_string = string.ascii_uppercase + string.digits  # 36 chars
    modulus = np.vectorize(lambda x: x % 36)  # Mod 36
    to_int = np.vectorize(round)  # Round numbers

    def __init__(self, encrypt_key: np.ndarray) -> None:
        self.encrypt_key = self.modulus(encrypt_key)
        self.check_determinant()  # Validate key
        self.break_key = encrypt_key.shape[0]  # Matrix size

    def replace_letters(self, letter: str) -> int:
        """Char to index (A=0, 0=26)"""
        return self.key_string.index(letter)

    def replace_digits(self, num: int) -> str:
        """Index to char"""
        return self.key_string[num]

    def check_determinant(self) -> None:
        """Ensure det(key) coprime with 36"""
        det = round(np.linalg.det(self.encrypt_key))
        if det < 0:
            det %= len(self.key_string)

        error_msg = f"Det {det} not coprime with 36. Try another key."
        if greatest_common_divisor(det, len(self.key_string)) != 1:
            raise ValueError(error_msg)

    def process_text(self, text: str) -> str:
        """Uppercase, filter, pad text"""
        chars = [c for c in text.upper() if c in self.key_string]
        last = chars[-1] if chars else "A"
        while len(chars) % self.break_key != 0:
            chars.append(last)
        return "".join(chars)

    def encrypt(self, text: str) -> str:
        """Encrypt with Hill cipher"""
        text = self.process_text(text.upper())
        encrypted = ""
        for i in range(0, len(text), self.break_key):
            batch = text[i : i + self.break_key]
            vec = [self.replace_letters(c) for c in batch]
            batch_vec = np.array([vec]).T
            product = self.encrypt_key.dot(batch_vec)
            modulated = self.modulus(product)
            batch_encrypted = modulated.T.tolist()[0]
            encrypted_batch = "".join(
                self.replace_digits(round(n)) for n in batch_encrypted
            )
            encrypted += encrypted_batch
        return encrypted

    def make_decrypt_key(self) -> np.ndarray:
        """Create decryption key"""
        det = round(np.linalg.det(self.encrypt_key))
        if det < 0:
            det %= len(self.key_string)

        # Find det modular inverse
        det_inv = next(i for i in range(36) if (det * i) % 36 == 1)

        # Compute inverse key
        inv_key = (
            det_inv * np.linalg.det(self.encrypt_key) * np.linalg.inv(self.encrypt_key)
        )
        return self.to_int(self.modulus(inv_key))

    def decrypt(self, text: str) -> str:
        """Decrypt with Hill cipher"""
        decrypt_key = self.make_decrypt_key()
        text = self.process_text(text.upper())
        decrypted = ""
        for i in range(0, len(text), self.break_key):
            batch = text[i : i + self.break_key]
            vec = [self.replace_letters(c) for c in batch]
            batch_vec = np.array([vec]).T
            product = decrypt_key.dot(batch_vec)
            modulated = self.modulus(product)
            batch_decrypted = modulated.T.tolist()[0]
            decrypted_batch = "".join(
                self.replace_digits(round(n)) for n in batch_decrypted
            )
            decrypted += decrypted_batch
        return decrypted


def main() -> None:
    """Hill Cipher CLI"""
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
