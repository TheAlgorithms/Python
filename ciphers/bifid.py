#!/usr/bin/env python3

"""
The Bifid Cipher uses a Polybius Square to encipher a message in a way that
makes it fairly difficult to decipher without knowing the secret.

https://www.braingle.com/brainteasers/codes/bifid.php
"""

import numpy as np


class BifidCipher:
    def __init__(self) -> None:
        SQUARE = [  # noqa: N806
            ["a", "b", "c", "d", "e"],
            ["f", "g", "h", "i", "k"],
            ["l", "m", "n", "o", "p"],
            ["q", "r", "s", "t", "u"],
            ["v", "w", "x", "y", "z"],
        ]
        self.SQUARE = np.array(SQUARE)

    def letter_to_numbers(self, letter: str) -> np.ndarray:
        """
        Return the pair of numbers that represents the given letter in the
        polybius square

        >>> np.array_equal(BifidCipher().letter_to_numbers('a'), [1,1])
        True

        >>> np.array_equal(BifidCipher().letter_to_numbers('u'), [4,5])
        True
        """
        index1, index2 = np.where(self.SQUARE == letter)
        indexes = np.concatenate([index1 + 1, index2 + 1])
        return indexes

    def numbers_to_letter(self, index1: int, index2: int) -> str:
        """
        Return the letter corresponding to the position [index1, index2] in
        the polybius square

        >>> BifidCipher().numbers_to_letter(4, 5) == "u"
        True

        >>> BifidCipher().numbers_to_letter(1, 1) == "a"
        True
        """
        letter = self.SQUARE[index1 - 1, index2 - 1]
        return letter

    def encode(self, message: str) -> str:
        """
        Return the encoded version of message according to the polybius cipher

        >>> BifidCipher().encode('testmessage') == 'qtltbdxrxlk'
        True

        >>> BifidCipher().encode('Test Message') == 'qtltbdxrxlk'
        True

        >>> BifidCipher().encode('test j') == BifidCipher().encode('test i')
        True
        """
        message = message.lower()
        message = message.replace(" ", "")
        message = message.replace("j", "i")

        first_step = np.empty((2, len(message)))
        for letter_index in range(len(message)):
            numbers = self.letter_to_numbers(message[letter_index])

            first_step[0, letter_index] = numbers[0]
            first_step[1, letter_index] = numbers[1]

        second_step = first_step.reshape(2 * len(message))
        encoded_message = ""
        for numbers_index in range(len(message)):
            index1 = int(second_step[numbers_index * 2])
            index2 = int(second_step[(numbers_index * 2) + 1])
            letter = self.numbers_to_letter(index1, index2)
            encoded_message = encoded_message + letter

        return encoded_message

    def decode(self, message: str) -> str:
        """
        Return the decoded version of message according to the polybius cipher

        >>> BifidCipher().decode('qtltbdxrxlk') == 'testmessage'
        True
        """
        message = message.lower()
        message.replace(" ", "")
        first_step = np.empty(2 * len(message))
        for letter_index in range(len(message)):
            numbers = self.letter_to_numbers(message[letter_index])
            first_step[letter_index * 2] = numbers[0]
            first_step[letter_index * 2 + 1] = numbers[1]

        second_step = first_step.reshape((2, len(message)))
        decoded_message = ""
        for numbers_index in range(len(message)):
            index1 = int(second_step[0, numbers_index])
            index2 = int(second_step[1, numbers_index])
            letter = self.numbers_to_letter(index1, index2)
            decoded_message = decoded_message + letter

        return decoded_message
