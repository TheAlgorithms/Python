"""
Python program for DES (Data Encryption Standard) using Electronic Codebook (ECB) mode.

DES is a symmetric-key block cipher that encrypts data in fixed-size blocks (64 bits).
In ECB mode, the plaintext is divided into 64-bit blocks, and each block is encrypted
independently using the same key. This makes ECB the simplest block cipher mode, but
also one of the least secure, as identical plaintext blocks will produce identical
ciphertext blocks.

This implementation of DES includes key scheduling, encryption, and decryption.
It uses standard DES operations such as initial and final permutations, expansion,
permutation, and S-box lookups. Padding is applied to ensure the plaintext length is
a multiple of 64 bits.

Warning: ECB mode is not secure for most use cases due to its vulnerability to block
repetition analysis. Consider using a more secure mode of operation, such as CBC
(Cipher Block Chaining), for sensitive data encryption.

References:
- Handbook of Applied Cryptography (Algorithm 7.82)
- Handbook of Applied Cryptography (Algorithm 7.83)
- Handbook of Applied Cryptography (Algorithm 9.29)
- https://en.wikipedia.org/wiki/Data_Encryption_Standard
"""

import random

# fmt: off

# Initial Permutation Table
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Final Permutation Table
IP_INV = [40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41, 9, 49, 17, 57, 25]

# Expansion Table
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

# Permutation Table
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

# S-boxes (Substitution Boxes)
S_BOXES = {
    "S1": [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
           [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
           [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
           [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    "S2": [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
           [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
           [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
           [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    "S3": [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
           [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
           [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
           [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    "S4": [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
           [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
           [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
           [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    "S5": [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
           [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
           [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
           [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    "S6": [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
           [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
           [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
           [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    "S7": [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
           [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
           [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
           [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    "S8": [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
           [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
           [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
           [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
}

# Permuted Choice 1 Table
PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

# Permuted Choice 2 Table
PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]
# fmt: on


class Operations:
    @staticmethod
    def string_to_bitset(string: str) -> list:
        """
        Converts a string into a list of binary digits (bitset).

        Args:
            string (str): The input string to be converted.

        Returns:
            list: A list of binary digits representing the string.

        Examples:
            >>> Operations.string_to_bitset('A')
            ['0', '1', '0', '0', '0', '0', '0', '1']
            >>> len(Operations.string_to_bitset('ab'))
            16
            >>> Operations.string_to_bitset(' ')
            ['0', '0', '1', '0', '0', '0', '0', '0']
        """
        return list("".join(format(ord(char), "08b") for char in string))

    @staticmethod
    def pad_right_to_multiple_of_n(bitset: list, length: int) -> list:
        """
        Pads the bitset with zeros on the right until
        its length is a multiple of `length`.

        Args:
            bitset (list): A list of binary digits (as strings) to be padded.

        Returns:
            list: The padded bitset, with a length that is a multiple of n.

        Examples:
            >>> Operations.pad_right_to_multiple_of_n(['1', '0', '1'], 4)
            ['1', '0', '1', '0']
            >>> len(Operations.pad_right_to_multiple_of_n(['1'] * 64, 64)) % 64
            0
            >>> len(Operations.pad_right_to_multiple_of_n(['0'] * 63, 64)) % 64
            0
        """
        if len(bitset) % length != 0:
            bitset += list("0" * (length - len(bitset) % length))
        return bitset

    @staticmethod
    def pad_left_to_multiple_of_n(bitset: list, length: int) -> list:
        """
        Pads the bitset with zeros on the left until
        its length is a multiple of length.

        Args:
            bitset (list): A list of binary digits (as strings) to be padded.

        Returns:
            list: The padded bitset, with a length that is a multiple of n.

        Examples:
            >>> Operations.pad_left_to_multiple_of_n(['1', '0', '1'], 4)
            ['0', '1', '0', '1']
            >>> len(Operations.pad_left_to_multiple_of_n(['1'] * 64, 64)) % 64
            0
            >>> len(Operations.pad_left_to_multiple_of_n(['0'] * 63, 64)) % 64
            0
        """
        if len(bitset) % length != 0:
            bitset = list("0" * (length - len(bitset) % length)) + bitset
        return bitset

    @staticmethod
    def bitset_to_hex(bitset: list) -> str:
        """
        Converts a list of binary digits
        into its 16 digit hexadecimal representation.

        Args:
            bitset (list): A list of binary digits (as strings)\
            representing a binary number.

        Returns:
            str: The 16 digit hexadecimal representation of the binary number.

        Examples:
            >>> Operations.bitset_to_hex(['1', '0', '1', '0', '1', '1', '1', '0'])
            '00000000000000ae'
            >>> Operations.bitset_to_hex(['1', '1', '1', '1'] * 16)
            'ffffffffffffffff'
            >>> Operations.bitset_to_hex(['0'] * 64)
            '0000000000000000'
        """
        return format(int("".join(bitset), 2), "016x")

    @staticmethod
    def hex_to_bitset(hex_string: str, left_pad: int) -> list:
        """
        Converts a hexadecimal string to a bitset
        and pads the bitset to a specified length.

        Args:
            hex_string (str): The hexadecimal string to convert.
            left_pad (int): The length to pad the bitset on the left.

        Returns:
            list: The padded bitset.

        Examples:
            >>> Operations.hex_to_bitset('ae', 8)
            ['1', '0', '1', '0', '1', '1', '1', '0']
            >>> Operations.hex_to_bitset('1f', 10)
            ['0', '0', '0', '0', '0', '1', '1', '1', '1', '1']
        """
        return Operations.pad_left_to_multiple_of_n(
            list(format(int(hex_string, 16), f"0{left_pad}b")), left_pad
        )

    @staticmethod
    def bitset_to_string(bitset: list) -> str:
        """
        Converts a bitset into a string by interpreting every 8 bits as a character.

        Args:
            bitset (list): The list of binary digits (bitset).

        Returns:
            str: The decoded string.

        Examples:
            >>> Operations.bitset_to_string(['0', '1', '0', '0', '0', '0', '0', '1'])
            'A'
            >>> Operations.bitset_to_string(['0', '1', '0', '0', '0', '1',\
'0', '0', '0', '1', '0', '1', '0', '1', '1', '0'])
            'DV'
        """
        return "".join(
            chr(int("".join(bitset[i : i + 8]), 2)) for i in range(0, len(bitset), 8)
        )

    @staticmethod
    def xor(bitset1: list, bitset2: list) -> list:
        """
        Applies a bitwise XOR operation between two bitsets of the same length.

        Args:
            bitset1 (list): The first bitset.
            bitset2 (list): The second bitset.

        Returns:
            list: The result of the XOR operation as a new bitset.

        Examples:
            >>> Operations.xor(['0', '1', '0', '1'], ['1', '0', '1', '1'])
            ['1', '1', '1', '0']
            >>> Operations.xor(['1', '0', '1', '0'], ['0', '0', '0', '1'])
            ['1', '0', '1', '1']
            >>> Operations.xor(['1', '0', '1', '0', '1'], ['0', '0', '0', '1'])
            Traceback (most recent call last):
                ...
            ValueError: Bitsets must be of the same length
            >>> Operations.xor(['1', '0', '1', '0'], ['0', '0', '0', '1', '1'])
            Traceback (most recent call last):
                ...
            ValueError: Bitsets must be of the same length
        """
        if len(bitset1) != len(bitset2):
            raise ValueError("Bitsets must be of the same length")
        return [str(int(bitset1[i]) ^ int(bitset2[i])) for i in range(len(bitset1))]

    @staticmethod
    def shift_left(bitset: list, position: int) -> list:
        """
        Performs a rotated left shift on a bitset by `position` positions.

        Args:
            bitset (list): The bitset to be shifted.
            n (int): The number of positions to shift.

        Returns:
            list: The left-shifted bitset.

        Examples:
            >>> Operations.shift_left(['1', '0', '0', '1'], 2)
            ['0', '1', '1', '0']
            >>> Operations.shift_left(['0', '1', '1', '1'], 1)
            ['1', '1', '1', '0']
            >>> Operations.shift_left(['0', '1', '1', '1'], 7)
            ['1', '0', '1', '1']
        """
        position = position % len(bitset)
        return bitset[position:] + bitset[:position]

    @staticmethod
    def permute(bitset: list, permutation: list) -> list:
        """
        Permutes a bitset according to a given permutation table.

        Args:
            bitset (list): The bitset to be permuted.
            permutation (list): The permutation table specifying the new order.

        Returns:
            list: The permuted bitset.

        Examples:
            >>> Operations.permute(['1', '0', '1', '0', '1', '1'], [6, 5, 4, 3, 2, 1])
            ['1', '1', '0', '1', '0', '1']
            >>> Operations.permute(['0', '1', '1', '0', '1', '0'], [3, 1, 6, 5, 4, 2])
            ['1', '0', '0', '1', '0', '1']
            >>> Operations.permute(['0', '1', '1', '0', '1', '0'], \
[3, 1, 6, 5, 4, 2, 7])
            Traceback (most recent call last):
                ...
            ValueError: Permutation values must be within the range of the bitset
        """
        if not all(0 < i <= len(bitset) for i in permutation):
            raise ValueError(
                "Permutation values must be within the range of the bitset"
            )
        return [bitset[i - 1] for i in permutation]


class Des:
    @staticmethod
    def generate_key() -> str:
        """
        Generates a random hexadecimal key of 16 characters (64 bits).

        Returns:
            str: A random hexadecimal key.

        Examples:
            >>> key = Des.generate_key()
            >>> len(key)  # Check if the key length is correct
            16
            >>> # Ensure key only contains valid hex characters
            >>> all(c in "0123456789abcdef" for c in key)
            True
        """
        return "".join(random.choice("0123456789abcdef") for i in range(16))

    @staticmethod
    def key_schedule(key: str) -> list:
        """
        Generates 16 subkeys (round keys) from a given
        64-bit hexadecimal key using the DES key schedule.

        Args:
            key (str): A 16-character hexadecimal string representing a 64-bit key.

        Returns:
            list: A list of 16 subkeys, each of which is a permuted bitset.

        Examples:
            >>> subkeys = Des.key_schedule('133457799BBCDFF1')
            >>> len(subkeys)  # Check that 16 subkeys are generated
            16
            >>> # Ensure each subkey is 48 bits long
            >>> all(len(subkey) == 48 for subkey in subkeys)
            True
        """
        key_bitset = Operations.hex_to_bitset(key, 64)
        key_permuted = Operations.permute(key_bitset, PC1)

        left_key = key_permuted[:28]
        right_key = key_permuted[28:]

        keys = []

        shift_list = [1, 2, 9, 16]

        for i in range(1, 17):
            if i in shift_list:
                left_key = Operations.shift_left(left_key, 1)
                right_key = Operations.shift_left(right_key, 1)
            else:
                left_key = Operations.shift_left(left_key, 2)
                right_key = Operations.shift_left(right_key, 2)
            keys.append(Operations.permute(left_key + right_key, PC2))

        return keys

    @staticmethod
    def des(keys: list, plain_bitset: list) -> list:
        """
        Encrypts a plain bitset using the provided
        subkeys with DES encryption algorithm.

        Args:
            keys (list): A list of 16 subkeys, each 48 bits long.
            plain_bitset (list): A bitset representing the plain text,\
            which should be divisible into 64-bit blocks.

        Returns:
            list: The encrypted bitset.

        Examples:
            >>> plain_bitset = Operations.string_to_bitset("Test string")
            >>> plain_bitset = Operations.pad_right_to_multiple_of_n(plain_bitset, 64)
            >>> keys = Des.key_schedule(Des.generate_key())
            >>> cipher_bitset = Des.des(keys, plain_bitset)
            >>> # The output length should be the same as the input
            >>> len(cipher_bitset) == len(plain_bitset)
            True
            >>> # Decryption should be the inverse of encryption
            >>> plain_bitset == Des.des(keys[::-1], cipher_bitset)
            True
        """

        no_of_blocks = len(plain_bitset) // 64

        cipher_bitset = []

        for i in range(no_of_blocks):
            block = plain_bitset[i * 64 : (i + 1) * 64]
            initial_permutation = Operations.permute(block, IP)

            left_bits = initial_permutation[:32]
            right_bits = initial_permutation[32:]

            for i in range(16):
                right_expanded = Operations.permute(right_bits, E)
                right_xor_key = Operations.xor(right_expanded, keys[i])
                right_s_box = []
                for j in range(8):
                    s_box_input = right_xor_key[j * 6 : (j + 1) * 6]
                    row = 2 * int(s_box_input[0]) + int(s_box_input[5])
                    col = int("".join(s_box_input[1:5]), 2)
                    s_box_output = format(S_BOXES[f"S{j + 1}"][row][col], "04b")
                    right_s_box += list(s_box_output)

                right_permuted = Operations.permute(right_s_box, P)

                left_bits, right_bits = (
                    right_bits,
                    Operations.xor(left_bits, right_permuted),
                )

            left_bits, right_bits = right_bits, left_bits
            cipher_bitset += Operations.permute(left_bits + right_bits, IP_INV)
        return cipher_bitset

    @staticmethod
    def encrypt(key: str, input_string: str) -> str:
        """
        Encrypts a given input string using the DES encryption algorithm.

        Args:
            key (str): A 16-character hexadecimal string representing a 64-bit key.
            input_string (str): The plain text string to be encrypted.

        Returns:
            str: A hexadecimal string representing the encrypted data.

        Examples:
            >>> key = '133457799BBCDFF1'
            >>> input_string = 'Test string'
            >>> encrypted = Des.encrypt(key, input_string)
            >>> encrypted  # Checking the cipher to ensure consistency
            'c84e3c8fb646872720b224896db4f60'
        """
        plain_bitset = Operations.string_to_bitset(input_string)
        padded_bitset = Operations.pad_right_to_multiple_of_n(plain_bitset, 64)
        keys = Des.key_schedule(key)
        cipher_bitset = Des.des(keys, padded_bitset)
        return Operations.bitset_to_hex(cipher_bitset)

    @staticmethod
    def decrypt(key: str, cipher_text: str) -> str:
        """
        Decrypts the given cipher text using DES decryption.

        Args:
            key (str): A 16-character hexadecimal string representing a 64-bit key.
            cipher_text (str): A hexadecimal string representing the encrypted data.

        Returns:
            str: The decrypted plain text string.

        Examples:
            >>> key = '133457799BBCDFF1'
            >>> encrypted_string = 'c84e3c8fb646872720b224896db4f60'
            >>> decrypted = Des.decrypt(key, encrypted_string)
            >>> decrypted  # Checking the cipher to ensure consistency
            'Test string'
        """
        cipher_bitset = Operations.hex_to_bitset(cipher_text, 64)
        keys = Des.key_schedule(key)[::-1]
        plain_bitset = Des.des(keys, cipher_bitset)
        return Operations.bitset_to_string(plain_bitset).replace("\x00", "")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    while True:
        print()
        print("################ DES Algorithm ################")
        print()
        print("Select an option:")
        print("1. To encrypt a string, enter 'e'")
        print("2. To decrypt a string, enter 'd'")
        print("3. To generate a key, enter 'k'")
        print("4. To Quit, enter 'q'")
        mode = input("Enter the option: ").strip().lower()
        if mode not in ["e", "d", "k", "q"]:
            print("Invalid option. Please try again.")
            continue
        if mode == "q":
            break
        elif mode == "k":
            print(f"Generated key: {Des.generate_key()}")
        elif mode == "e":
            key = input("Enter the key: ").strip()
            if len(key) != 16 and not all(char in "0123456789abcdef" for char in key):
                print("Invalid key. Please try again.")
                continue
            input_string = input("Enter the string to encrypt: ").strip()
            print(f"Encrypted string: {Des.encrypt(key, input_string)}")
        elif mode == "d":
            key = input("Enter the key: ").strip()
            if len(key) != 16 and not all(char in "0123456789abcdef" for char in key):
                print("Invalid key. Please try again.")
                continue
            cipher_text = input("Enter the cipher text to decrypt: ").strip()
            print(f"Decrypted string: {Des.decrypt(key, cipher_text)}")
