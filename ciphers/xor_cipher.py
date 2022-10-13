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

class XORCipher:
    def __init__(self, key: int = 0):
        """
        simple constructor that receives a key or uses
        default key = 0
        """

        # private field
        self.__key = key

    def encrypt(self, content: str, key: int, type_: int) -> list[str]|str:
        """
        input: 'content' of type string and 'key' of type int
        output: encrypted string 'content' as a list of chars
        if key not passed the method uses the key by the constructor.
        otherwise key = 1
        if type is 0,the result will be a list[str].
        if type is 1,the result will be a str.
        """

        # precondition
        assert isinstance(key, int) and isinstance(content, str)

        key = key or self.__key or 1

        # make sure key is an appropriate size
        key %= 255
        
        result_list = [chr(ord(ch) ^ key) for ch in content]
        if type_ == 0:
            return result_list
        else:
            string = ''
            for i in result_list:
                string.append(i)
                return string

    def decrypt(self, content: str, key: int, type_: int) -> list[str]:
        """
        input: 'content' of type list and 'key' of type int
        output: decrypted string 'content' as a list of chars
        if key not passed the method uses the key by the constructor.
        otherwise key = 1
        """

        # precondition
        assert isinstance(key, int) and isinstance(content, list)

        key = key or self.__key or 1

        # make sure key is an appropriate size
        key %= 255

        result_list = [chr(ord(ch) ^ key) for ch in content]
        if type_ == 0:
            return result_list
        else:
            string = ''
            for i in result_list:
                string.append(i)
                return string

    def encrypt_file(self, file: str, key: int = 0) -> bool:
        """
        input: filename (str) and a key (int)
        output: returns true if encrypt process was
        successful otherwise false
        if key not passed the method uses the key by the constructor.
        otherwise key = 1
        """

        # precondition
        assert isinstance(file, str) and isinstance(key, int)

        try:
            with open(file) as fin:
                with open("encrypt.out", "w+") as fout:

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
        assert isinstance(file, str) and isinstance(key, int)

        try:
            with open(file) as fin:
                with open("decrypt.out", "w+") as fout:

                    # actual encrypt-process
                    for line in fin:
                        fout.write(self.decrypt_string(line, key))

        except OSError:
            return False

        return True


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
