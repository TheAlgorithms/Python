"""
author: Christian Bender
date: 21.12.2017
class: XORCipher

This class implements the XOR-cipher algorithm and provides
some useful methods for encrypting and decrypting strings and
files.

Overview about methods

- encrypt : list of char
- decrypt : list of char
- encrypt_string : str
- decrypt_string : str
- encrypt_file : boolean
- decrypt_file : boolean
"""

from __future__ import annotations


class XORCipher:
    def __init__(self, key: int = 0):
        """
        simple constructor that receives a key or uses
        default key = 0
        """

        # private field
        self.__key = key

    def encrypt(self, content: str, key: int) -> list[str]:
        """
        input: 'content' of type string and 'key' of type int
        output: encrypted string 'content' as a list of chars
        if key not passed the method uses the key by the constructor.
        otherwise key = 1

        Empty list
        >>> XORCipher().encrypt("", 5)
        []

        One key
        >>> XORCipher().encrypt("hallo welt", 1)
        ['i', '`', 'm', 'm', 'n', '!', 'v', 'd', 'm', 'u']

        Normal key
        >>> XORCipher().encrypt("HALLO WELT", 32)
        ['h', 'a', 'l', 'l', 'o', '\\x00', 'w', 'e', 'l', 't']

        Key greater than 255
        >>> XORCipher().encrypt("hallo welt", 256)
        ['h', 'a', 'l', 'l', 'o', ' ', 'w', 'e', 'l', 't']
        """

        # precondition
        assert isinstance(key, int)
        assert isinstance(content, str)

        key = key or self.__key or 1

        # make sure key is an appropriate size
        key %= 256

        return [chr(ord(ch) ^ key) for ch in content]

    def decrypt(self, content: str, key: int) -> list[str]:
        """
        input: 'content' of type list and 'key' of type int
        output: decrypted string 'content' as a list of chars
        if key not passed the method uses the key by the constructor.
        otherwise key = 1

        Empty list
        >>> XORCipher().decrypt("", 5)
        []

        One key
        >>> XORCipher().decrypt("hallo welt", 1)
        ['i', '`', 'm', 'm', 'n', '!', 'v', 'd', 'm', 'u']

        Normal key
        >>> XORCipher().decrypt("HALLO WELT", 32)
        ['h', 'a', 'l', 'l', 'o', '\\x00', 'w', 'e', 'l', 't']

        Key greater than 255
        >>> XORCipher().decrypt("hallo welt", 256)
        ['h', 'a', 'l', 'l', 'o', ' ', 'w', 'e', 'l', 't']
        """

        # precondition
        assert isinstance(key, int)
        assert isinstance(content, str)

        key = key or self.__key or 1

        # make sure key is an appropriate size
        key %= 256

        return [chr(ord(ch) ^ key) for ch in content]

    def encrypt_string(self, content: str, key: int = 0) -> str:
        """
        input: 'content' of type string and 'key' of type int
        output: encrypted string 'content'
        if key not passed the method uses the key by the constructor.
        otherwise key = 1

        Empty list
        >>> XORCipher().encrypt_string("", 5)
        ''

        One key
        >>> XORCipher().encrypt_string("hallo welt", 1)
        'i`mmn!vdmu'

        Normal key
        >>> XORCipher().encrypt_string("HALLO WELT", 32)
        'hallo\\x00welt'

        Key greater than 255
        >>> XORCipher().encrypt_string("hallo welt", 256)
        'hallo welt'
        """

        # precondition
        assert isinstance(key, int)
        assert isinstance(content, str)

        key = key or self.__key or 1

        # make sure key is an appropriate size
        key %= 256

        # This will be returned
        ans = ""

        for ch in content:
            ans += chr(ord(ch) ^ key)

        return ans

    def decrypt_string(self, content: str, key: int = 0) -> str:
        """
        input: 'content' of type string and 'key' of type int
        output: decrypted string 'content'
        if key not passed the method uses the key by the constructor.
        otherwise key = 1

        Empty list
        >>> XORCipher().decrypt_string("", 5)
        ''

        One key
        >>> XORCipher().decrypt_string("hallo welt", 1)
        'i`mmn!vdmu'

        Normal key
        >>> XORCipher().decrypt_string("HALLO WELT", 32)
        'hallo\\x00welt'

        Key greater than 255
        >>> XORCipher().decrypt_string("hallo welt", 256)
        'hallo welt'
        """

        # precondition
        assert isinstance(key, int)
        assert isinstance(content, str)

        key = key or self.__key or 1

        # make sure key is an appropriate size
        key %= 256

        # This will be returned
        ans = ""

        for ch in content:
            ans += chr(ord(ch) ^ key)

        return ans

    def encrypt_file(self, file: str, key: int = 0) -> bool:
        """
        input: filename (str) and a key (int)
        output: returns true if encrypt process was
        successful otherwise false
        if key not passed the method uses the key by the constructor.
        otherwise key = 1
        """

        # precondition
        assert isinstance(file, str)
        assert isinstance(key, int)

        # make sure key is an appropriate size
        key %= 256

        try:
            with open(file) as fin, open("encrypt.out", "w+") as fout:
                # actual encrypt-process
                for line in fin:
                    fout.write(self.encrypt_string(line, key))

        except OSError:
            return False

        return True

    def decrypt_file(self, file: str, key: int) -> bool:
        """
        input: filename (str) and a key (int)
        output: returns true if decrypt process was
        successful otherwise false
        if key not passed the method uses the key by the constructor.
        otherwise key = 1
        """

        # precondition
        assert isinstance(file, str)
        assert isinstance(key, int)

        # make sure key is an appropriate size
        key %= 256

        try:
            with open(file) as fin, open("decrypt.out", "w+") as fout:
                # actual encrypt-process
                for line in fin:
                    fout.write(self.decrypt_string(line, key))

        except OSError:
            return False

        return True


if __name__ == "__main__":
    from doctest import testmod

    testmod()

# Tests
# crypt = XORCipher()
# key = 67

# # test encrypt
# print(crypt.encrypt("hallo welt",key))
# # test decrypt
# print(crypt.decrypt(crypt.encrypt("hallo welt",key), key))

# # test encrypt_string
# print(crypt.encrypt_string("hallo welt",key))

# # test decrypt_string
# print(crypt.decrypt_string(crypt.encrypt_string("hallo welt",key),key))

# if (crypt.encrypt_file("test.txt",key)):
#       print("encrypt successful")
# else:
#       print("encrypt unsuccessful")

# if (crypt.decrypt_file("encrypt.out",key)):
#       print("decrypt successful")
# else:
#       print("decrypt unsuccessful")
