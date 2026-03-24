import secrets


class Onepad:
    @staticmethod
    def encrypt(text: str) -> tuple[list[int], list[int]]:
        """
        Function to encrypt text using cryptographically secure random numbers.

        >>> Onepad().encrypt("")
        ([], [])
        >>> Onepad().encrypt([])
        ([], [])
        >>> c, k = Onepad().encrypt(" ")
        >>> len(c) == 1 and len(k) == 1
        True
        >>> c, k = Onepad().encrypt("Hello")
        >>> len(c) == 5 and len(k) == 5
        True
        >>> Onepad().decrypt(c, k)
        'Hello'
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
            k = secrets.randbelow(300) + 1  # range [1, 300]
            c = (i + k) * k
            cipher.append(c)
            key.append(k)
        return cipher, key

    @staticmethod
    def decrypt(cipher: list[int], key: list[int]) -> str:
        """
        Function to decrypt text using the key produced by encrypt().
        >>> Onepad().decrypt([], [])
        ''
        >>> Onepad().decrypt([35], [])
        ''
        >>> Onepad().decrypt([], [35])
        Traceback (most recent call last):
        ...
        IndexError: list index out of range
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
