import random


class Onepad:
    @staticmethod
    def encrypt(text: str) -> tuple[list[int], list[int]]:
        """
        Function to encrypt text using pseudo-random numbers
        >>> Onepad().encrypt("")
        ([], [])
        >>> Onepad().encrypt([])
        ([], [])
        >>> random.seed(1)
        >>> Onepad().encrypt(" ")
        ([6969], [69])
        >>> random.seed(1)
        >>> Onepad().encrypt("Hello")
        ([9729, 114756, 4653, 31309, 10492], [69, 292, 33, 131, 61])
        >>> Onepad().encrypt(1)
        Traceback (most recent call last):
        ...
        TypeError: 'int' object is not iterable
        >>> Onepad().encrypt(1.1)
        Traceback (most recent call last):
        ...
        TypeError: 'float' object is not iterable
        """
        plain = [ord(i) for i in text]
        key = []
        cipher = []
        for i in plain:
            k = random.randint(1, 300)
            c = (i + k) * k
            cipher.append(c)
            key.append(k)
        return cipher, key

    @staticmethod
    def decrypt(cipher: list[int], key: list[int]) -> str:
        """
        Function to decrypt text using pseudo-random numbers.
        >>> Onepad().decrypt([], [])
        ''
        >>> Onepad().decrypt([35], [])
        ''
        >>> Onepad().decrypt([], [35])
        Traceback (most recent call last):
        ...
        IndexError: list index out of range
        >>> random.seed(1)
        >>> Onepad().decrypt([9729, 114756, 4653, 31309, 10492], [69, 292, 33, 131, 61])
        'Hello'
        """
        plain = []
        for i in range(len(key)):
            p = int((cipher[i] - (key[i]) ** 2) / key[i])
            plain.append(chr(p))
        return "".join(plain)


if __name__ == "__main__":
    c, k = Onepad().encrypt("Hello")
    print(c, k)
    print(Onepad().decrypt(c, k))
