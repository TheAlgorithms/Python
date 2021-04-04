import random
import string
from typing import Optional


class ShuffledShiftCipher:
    """
    This algorithm uses the Caesar Cipher algorithm but removes the option to
    use brute force to decrypt the message.

    The passcode is a a random password from the selection buffer of
    1. uppercase letters of the English alphabet
    2. lowercase letters of the English alphabet
    3. digits from 0 to 9

    Using unique characters from the passcode, the normal list of characters,
    that can be allowed in the plaintext, is pivoted and shuffled. Refer to docstring
    of __make_key_list() to learn more about the shuffling.

    Then, using the passcode, a number is calculated which is used to encrypt the
    plaintext message with the normal shift cipher method, only in this case, the
    reference, to look back at while decrypting, is shuffled.

    Each cipher object can possess an optional argument as passcode, without which a
    new passcode is generated for that object automatically.
    cip1 = ShuffledShiftCipher('d4usr9TWxw9wMD')
    cip2 = ShuffledShiftCipher()
    """

    def __init__(self, passcode: Optional[str] = None) -> None:
        """
        Initializes a cipher object with a passcode as it's entity
        Note: No new passcode is generated if user provides a passcode
        while creating the object
        """
        self.__passcode = passcode or self.__passcode_creator()
        self.__key_list = self.__make_key_list()
        self.__shift_key = self.__make_shift_key()

    def __str__(self) -> str:
        """
        :return: passcode of the cipher object
        """
        return "Passcode is: " + "".join(self.__passcode)

    def __neg_pos(self, iterlist: list[int]) -> list[int]:
        """
        Mutates the list by changing the sign of each alternate element

        :param iterlist: takes a list iterable
        :return: the mutated list

        """
        for i in range(1, len(iterlist), 2):
            iterlist[i] *= -1
        return iterlist

    def __passcode_creator(self) -> list[str]:
        """
        Creates a random password from the selection buffer of
        1. uppercase letters of the English alphabet
        2. lowercase letters of the English alphabet
        3. digits from 0 to 9

        :rtype: list
        :return: a password of a random length between 10 to 20
        """
        choices = string.ascii_letters + string.digits
        password = [random.choice(choices) for _ in range(random.randint(10, 20))]
        return password

    def __make_key_list(self) -> list[str]:
        """
        Shuffles the ordered character choices by pivoting at breakpoints
        Breakpoints are the set of characters in the passcode

        eg:
            if, ABCDEFGHIJKLMNOPQRSTUVWXYZ are the possible characters
            and CAMERA is the passcode
            then, breakpoints = [A,C,E,M,R] # sorted set of characters from passcode
            shuffled parts: [A,CB,ED,MLKJIHGF,RQPON,ZYXWVUTS]
            shuffled __key_list : ACBEDMLKJIHGFRQPONZYXWVUTS

        Shuffling only 26 letters of the english alphabet can generate 26!
        combinations for the shuffled list. In the program we consider, a set of
        97 characters (including letters, digits, punctuation and whitespaces),
        thereby creating a possibility of 97! combinations (which is a 152 digit number
        in itself), thus diminishing the possibility of a brute force approach.
        Moreover, shift keys even introduce a multiple of 26 for a brute force approach
        for each of the already 97! combinations.
        """
        # key_list_options contain nearly all printable except few elements from
        # string.whitespace
        key_list_options = (
            string.ascii_letters + string.digits + string.punctuation + " \t\n"
        )

        keys_l = []

        # creates points known as breakpoints to break the key_list_options at those
        # points and pivot each substring
        breakpoints = sorted(set(self.__passcode))
        temp_list: list[str] = []

        # algorithm for creating a new shuffled list, keys_l, out of key_list_options
        for i in key_list_options:
            temp_list.extend(i)

            # checking breakpoints at which to pivot temporary sublist and add it into
            # keys_l
            if i in breakpoints or i == key_list_options[-1]:
                keys_l.extend(temp_list[::-1])
                temp_list.clear()

        # returning a shuffled keys_l to prevent brute force guessing of shift key
        return keys_l

    def __make_shift_key(self) -> int:
        """
        sum() of the mutated list of ascii values of all characters where the
        mutated list is the one returned by __neg_pos()
        """
        num = sum(self.__neg_pos([ord(x) for x in self.__passcode]))
        return num if num > 0 else len(self.__passcode)

    def decrypt(self, encoded_message: str) -> str:
        """
        Performs shifting of the encoded_message w.r.t. the shuffled __key_list
        to create the decoded_message

        >>> ssc = ShuffledShiftCipher('4PYIXyqeQZr44')
        >>> ssc.decrypt("d>**-1z6&'5z'5z:z+-='$'>=zp:>5:#z<'.&>#")
        'Hello, this is a modified Caesar cipher'

        """
        decoded_message = ""

        # decoding shift like Caesar cipher algorithm implementing negative shift or
        # reverse shift or left shift
        for i in encoded_message:
            position = self.__key_list.index(i)
            decoded_message += self.__key_list[
                (position - self.__shift_key) % -len(self.__key_list)
            ]

        return decoded_message

    def encrypt(self, plaintext: str) -> str:
        """
        Performs shifting of the plaintext w.r.t. the shuffled __key_list
        to create the encoded_message

        >>> ssc = ShuffledShiftCipher('4PYIXyqeQZr44')
        >>> ssc.encrypt('Hello, this is a modified Caesar cipher')
        "d>**-1z6&'5z'5z:z+-='$'>=zp:>5:#z<'.&>#"

        """
        encoded_message = ""

        # encoding shift like Caesar cipher algorithm implementing positive shift or
        # forward shift or right shift
        for i in plaintext:
            position = self.__key_list.index(i)
            encoded_message += self.__key_list[
                (position + self.__shift_key) % len(self.__key_list)
            ]

        return encoded_message


def test_end_to_end(msg: str = "Hello, this is a modified Caesar cipher") -> str:
    """
    >>> test_end_to_end()
    'Hello, this is a modified Caesar cipher'
    """
    cip1 = ShuffledShiftCipher()
    return cip1.decrypt(cip1.encrypt(msg))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
