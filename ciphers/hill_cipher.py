"""

Hill Cipher:
The below defined class 'HillCipher' implements the Hill Cipher algorithm.
The Hill Cipher is an algorithm that implements modern linear algebra techniques
In this algorithm, you have an encryption key matrix. This is what will be used
in encoding and decoding your text.

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
The algorithm implemented in this code considers only alphanumerics in the text.
If the length of the text to be encrypted is not a multiple of the
break key(the length of one batch of letters),the last character of the text
is added to the text until the length of the text reaches a multiple of
the break_key. So the text after decrypting might be a little different than
the original text.

References:
https://apprendre-en-ligne.net/crypto/hill/Hillciph.pdf
https://www.youtube.com/watch?v=kfmNeskzs2o
https://www.youtube.com/watch?v=4RhLNDqcjpA

"""

import numpy


def gcd(a: int, b: int) -> int:
    """
    >>> gcd(4, 8)
    4
    >>> gcd(8, 4)
    4
    >>> gcd(4, 7)
    1
    >>> gcd(0, 10)
    10
    """
    if a == 0:
        return b
    return gcd(b % a, a)


class HillCipher:
    key_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # This cipher takes alphanumerics into account
    # i.e. a total of 36 characters

    # take x and return x % len(key_string)
    modulus = numpy.vectorize(lambda x: x % 36)

    toInt = numpy.vectorize(lambda x: round(x))

    def __init__(self, encrypt_key):
        """
        encrypt_key is an NxN numpy matrix
        """
        self.encrypt_key = self.modulus(encrypt_key)  # mod36 calc's on the encrypt key
        self.check_determinant()  # validate the determinant of the encryption key
        self.decrypt_key = None
        self.break_key = encrypt_key.shape[0]

    def replaceLetters(self, letter: str) -> int:
        """
        >>> hill_cipher = HillCipher(numpy.matrix([[2, 5], [1, 6]]))
        >>> hill_cipher.replaceLetters('T')
        19
        >>> hill_cipher.replaceLetters('0')
        26
        """
        return self.key_string.index(letter)

    def replaceNumbers(self, num: int) -> str:
        """
        >>> hill_cipher = HillCipher(numpy.matrix([[2, 5], [1, 6]]))
        >>> hill_cipher.replaceNumbers(19)
        'T'
        >>> hill_cipher.replaceNumbers(26)
        '0'
        """
        return self.key_string[round(num)]

    def check_determinant(self) -> None:
        """
        >>> hill_cipher = HillCipher(numpy.matrix([[2, 5], [1, 6]]))
        >>> hill_cipher.check_determinant()
        """
        det = round(numpy.linalg.det(self.encrypt_key))

        if det < 0:
            det = det % len(self.key_string)

        req_l = len(self.key_string)
        if gcd(det, len(self.key_string)) != 1:
            raise ValueError(
                f"determinant modular {req_l} of encryption key({det}) is not co prime w.r.t {req_l}.\nTry another key."
            )

    def process_text(self, text: str) -> str:
        """
        >>> hill_cipher = HillCipher(numpy.matrix([[2, 5], [1, 6]]))
        >>> hill_cipher.process_text('Testing Hill Cipher')
        'TESTINGHILLCIPHERR'
        """
        text = list(text.upper())
        chars = [char for char in text if char in self.key_string]

        last = chars[-1]
        while len(chars) % self.break_key != 0:
            chars.append(last)

        return "".join(chars)

    def encrypt(self, text: str) -> str:
        """
        >>> hill_cipher = HillCipher(numpy.matrix([[2, 5], [1, 6]]))
        >>> hill_cipher.encrypt('testing hill cipher')
        'WHXYJOLM9C6XT085LL'
        """
        text = self.process_text(text.upper())
        encrypted = ""

        for i in range(0, len(text) - self.break_key + 1, self.break_key):
            batch = text[i : i + self.break_key]
            batch_vec = [self.replaceLetters(char) for char in batch]
            batch_vec = numpy.matrix([batch_vec]).T
            batch_encrypted = self.modulus(self.encrypt_key.dot(batch_vec)).T.tolist()[
                0
            ]
            encrypted_batch = "".join(
                self.replaceNumbers(num) for num in batch_encrypted
            )
            encrypted += encrypted_batch

        return encrypted

    def make_decrypt_key(self):
        """
        >>> hill_cipher = HillCipher(numpy.matrix([[2, 5], [1, 6]]))
        >>> hill_cipher.make_decrypt_key()
        matrix([[ 6., 25.],
                [ 5., 26.]])
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

        return self.toInt(self.modulus(inv_key))

    def decrypt(self, text: str) -> str:
        """
        >>> hill_cipher = HillCipher(numpy.matrix([[2, 5], [1, 6]]))
        >>> hill_cipher.decrypt('WHXYJOLM9C6XT085LL')
        'TESTINGHILLCIPHERR'
        """
        self.decrypt_key = self.make_decrypt_key()
        text = self.process_text(text.upper())
        decrypted = ""

        for i in range(0, len(text) - self.break_key + 1, self.break_key):
            batch = text[i : i + self.break_key]
            batch_vec = [self.replaceLetters(char) for char in batch]
            batch_vec = numpy.matrix([batch_vec]).T
            batch_decrypted = self.modulus(self.decrypt_key.dot(batch_vec)).T.tolist()[
                0
            ]
            decrypted_batch = "".join(
                self.replaceNumbers(num) for num in batch_decrypted
            )
            decrypted += decrypted_batch

        return decrypted


def main():
    N = int(input("Enter the order of the encryption key: "))
    hill_matrix = []

    print("Enter each row of the encryption key with space separated integers")
    for i in range(N):
        row = list(map(int, input().split()))
        hill_matrix.append(row)

    hc = HillCipher(numpy.matrix(hill_matrix))

    print("Would you like to encrypt or decrypt some text? (1 or 2)")
    option = input(
        """
1. Encrypt
2. Decrypt
"""
    )

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
