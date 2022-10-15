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

import numpy


def greatest_common_divisor(a: int, b: int) -> int:
    """
    >>> greatest_common_divisor(4, 8)
    4
    >>> greatest_common_divisor(8, 4)
    4
    >>> greatest_common_divisor(4, 7)
    1
    >>> greatest_common_divisor(0, 10)
    10
    """
    return b if a == 0 else greatest_common_divisor(b % a, a)


class HillCipher:
    key_string = string.ascii_uppercase + string.digits
    # This cipher takes alphanumerics into account
    # i.e. a total of 36 characters

    # take x and return x % len(key_string)
    modulus = numpy.vectorize(lambda x: x % 36)

    to_int = numpy.vectorize(round)

    def __init__(self, encrypt_key: numpy.ndarray) -> None:
        """
        encrypt_key is an NxN numpy array
        """
        self.encrypt_key = self.modulus(encrypt_key)  # mod36 calc's on the encrypt key
        self.check_determinant()  # validate the determinant of the encryption key
        self.break_key = encrypt_key.shape[0]

    def replace_letters(self, letter: str) -> int:
        """
        >>> hill_cipher = HillCipher(numpy.array([[2, 5], [1, 6]]))
        >>> hill_cipher.replace_letters('T')
        19
        >>> hill_cipher.replace_letters('0')
        26
        """
        return self.key_string.index(letter)

    def replace_digits(self, num: int) -> str:
        """
        >>> hill_cipher = HillCipher(numpy.array([[2, 5], [1, 6]]))
        >>> hill_cipher.replace_digits(19)
        'T'
        >>> hill_cipher.replace_digits(26)
        '0'
        """
        return self.key_string[round(num)]

    def check_determinant(self) -> None:
        """
        >>> hill_cipher = HillCipher(numpy.array([[2, 5], [1, 6]]))
        >>> hill_cipher.check_determinant()
        """
        det = round(numpy.linalg.det(self.encrypt_key))

        if det < 0:
            det = det % len(self.key_string)

        req_l = len(self.key_string)
        if greatest_common_divisor(det, len(self.key_string)) != 1:
            raise ValueError(
                f"determinant modular {req_l} of encryption key({det}) is not co prime "
                f"w.r.t {req_l}.\nTry another key."
            )

    def process_text(self, text: str) -> str:
        """
        >>> hill_cipher = HillCipher(numpy.array([[2, 5], [1, 6]]))
        >>> hill_cipher.process_text('Testing Hill Cipher')
        'TESTINGHILLCIPHERR'
        >>> hill_cipher.process_text('hello')
        'HELLOO'
        """
        chars = [char for char in text.upper() if char in self.key_string]

        last = chars[-1]
        while len(chars) % self.break_key != 0:
            chars.append(last)

        return "".join(chars)

    def encrypt(self, text: str) -> str:
        """
        >>> hill_cipher = HillCipher(numpy.array([[2, 5], [1, 6]]))
        >>> hill_cipher.encrypt('testing hill cipher')
        'WHXYJOLM9C6XT085LL'
        >>> hill_cipher.encrypt('hello')
        '85FF00'
        """
        text = self.process_text(text.upper())
        encrypted = ""

        for i in range(0, len(text) - self.break_key + 1, self.break_key):
            batch = text[i : i + self.break_key]
            vec = [self.replace_letters(char) for char in batch]
            batch_vec = numpy.array([vec]).T
            batch_encrypted = self.modulus(self.encrypt_key.dot(batch_vec)).T.tolist()[
                0
            ]
            encrypted_batch = "".join(
                self.replace_digits(num) for num in batch_encrypted
            )
            encrypted += encrypted_batch

        return encrypted

    def make_decrypt_key(self) -> numpy.ndarray:
        """
        >>> hill_cipher = HillCipher(numpy.array([[2, 5], [1, 6]]))
        >>> hill_cipher.make_decrypt_key()
        array([[ 6, 25],
               [ 5, 26]])
        """
        det = round(numpy.linalg.det(self.encrypt_key))

        if det < 0:
            det = det % len(self.key_string)
        det_inv = None
        for i in range(len(self.key_string)):
            if (det * i) % len(self.key_string) == 1:
                det_inv = i
                break

        inv_key = (
            det_inv
            * numpy.linalg.det(self.encrypt_key)
            * numpy.linalg.inv(self.encrypt_key)
        )

        return self.to_int(self.modulus(inv_key))

    def decrypt(self, text: str) -> str:
        """
        >>> hill_cipher = HillCipher(numpy.array([[2, 5], [1, 6]]))
        >>> hill_cipher.decrypt('WHXYJOLM9C6XT085LL')
        'TESTINGHILLCIPHERR'
        >>> hill_cipher.decrypt('85FF00')
        'HELLOO'
        """
        decrypt_key = self.make_decrypt_key()
        text = self.process_text(text.upper())
        decrypted = ""

        for i in range(0, len(text) - self.break_key + 1, self.break_key):
            batch = text[i : i + self.break_key]
            vec = [self.replace_letters(char) for char in batch]
            batch_vec = numpy.array([vec]).T
            batch_decrypted = self.modulus(decrypt_key.dot(batch_vec)).T.tolist()[0]
            decrypted_batch = "".join(
                self.replace_digits(num) for num in batch_decrypted
            )
            decrypted += decrypted_batch

        return decrypted


def main() -> None:
    n = int(input("Enter the order of the encryption key: "))
    hill_matrix = []

    print("Enter each row of the encryption key with space separated integers")
    for _ in range(n):
        row = [int(x) for x in input().split()]
        hill_matrix.append(row)

    hc = HillCipher(numpy.array(hill_matrix))

    print("Would you like to encrypt or decrypt some text? (1 or 2)")
    option = input("\n1. Encrypt\n2. Decrypt\n")
    if option == "1":
        text_e = input("What text would you like to encrypt?: ")
        print("Your encrypted text is:")
        print(hc.encrypt(text_e))
    elif option == "2":
        text_d = input("What text would you like to decrypt?: ")
        print("Your decrypted text is:")
        print(hc.decrypt(text_d))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()
