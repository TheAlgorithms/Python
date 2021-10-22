# Author: M. Yathurshan
# Black Formatter: True

"""
Implementation of SHA256 Hash function in a Python class and provides utilities
to find hash of string or hash of text from a file.

Usage: python sha256.py --string "Hello World!!"
       python sha256.py --file "hello_world.txt"
       When run without any arguments, it prints the hash of the string "Hello World!! Welcome to Cryptography"

References:
https://qvault.io/cryptography/how-sha-2-works-step-by-step-sha-256/ --> in detail
https://en.wikipedia.org/wiki/SHA-2 --> Pseudocode
"""

import argparse
import struct
import unittest
import hashlib  # used only inside Test class


class SHA256:
    """
    Class to contain the entire pipeline for SHA1 Hashing Algorithm

    >>> SHA256(bytes('Python', 'utf-8')).hash
    '18885f27b5af9012df19e496460f9294d5ab76128824c6f993787004f6d9a7db'

    >>> SHA256(bytes('hello world', 'utf-8')).hash
    'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'
    """

    def __init__(self, data: bytes) -> None:
        self.data = data

        # fmt: off

        # Initialize hash values
        self.h = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]

        # Initialize round constants
        self.round_constants = [
            0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
            0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
            0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
            0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
            0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
            0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
            0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
            0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
        ]

        # fmt: on

        self.preprocessing()
        self.final_hash()

    def preprocessing(self) -> None:
        padding = b"\x80" + (b"\x00" * (63 - (len(self.data) + 8) % 64))
        big_endian_integer = struct.pack(">Q", (len(self.data) * 8))
        self.preprocessed_data = self.data + padding + big_endian_integer

    def final_hash(self) -> None:
        # Convert into blocks of 64 bytes
        self.blocks = [
            self.preprocessed_data[x : (x + 64)]
            for x in range(0, len(self.preprocessed_data), 64)
        ]

        for block in self.blocks:
            # Convert the given block into a list of 4 byte integers
            words = list(struct.unpack(">16L", block))
            # add 48 0-ed integers
            words += [0] * 48

            a, b, c, d, e, f, g, h = self.h

            for index in range(0, 64):
                if index > 15:
                    # modify the zero-ed indexes at the end of the array
                    s0 = (
                        self.ror(words[index - 15], 7)
                        ^ self.ror(words[index - 15], 18)
                        ^ (words[index - 15] >> 3)
                    )
                    s1 = (
                        self.ror(words[index - 2], 17)
                        ^ self.ror(words[index - 2], 19)
                        ^ (words[index - 2] >> 10)
                    )

                    words[index] = (
                        words[index - 16] + s0 + words[index - 7] + s1
                    ) % 0x100000000

                # Compression
                S1 = self.ror(e, 6) ^ self.ror(e, 11) ^ self.ror(e, 25)
                ch = (e & f) ^ ((~e & (0xFFFFFFFF)) & g)
                temp1 = (
                    h + S1 + ch + self.round_constants[index] + words[index]
                ) % 0x100000000
                S0 = self.ror(a, 2) ^ self.ror(a, 13) ^ self.ror(a, 22)
                maj = (a & b) ^ (a & c) ^ (b & c)
                temp2 = (S0 + maj) % 0x100000000

                h, g, f, e, d, c, b, a = (
                    g,
                    f,
                    e,
                    ((d + temp1) % 0x100000000),
                    c,
                    b,
                    a,
                    ((temp1 + temp2) % 0x100000000),
                )

            mutated_hash_values = [a, b, c, d, e, f, g, h]

            # Modify final values
            self.h = [
                ((element + mutated_hash_values[index]) % 0x100000000)
                for index, element in enumerate(self.h)
            ]

        self.hash = "".join([hex(value)[2:].zfill(8) for value in self.h])

    def ror(self, value: int, rotations: int) -> int:
        """
        Right rotate a given unsigned number by a certain amount of rotations
        """
        return (0xFFFFFFFF & (value << (32 - rotations))) | (value >> rotations)


class SHA256HashTest(unittest.TestCase):
    """
    Test class for the SHA256 class. Inherits the TestCase class from unittest
    """

    def testMatchHashes(self) -> None:
        msg = bytes("Test String", "utf-8")
        self.assertEqual(SHA256(msg).hash, hashlib.sha256(msg).hexdigest())


def main() -> None:
    """
    Provides option 'string' or 'file' to take input
    and prints the calculated SHA-256 hash
    """

    # unittest.main()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--string",
        dest="input_string",
        default="Hello World!! Welcome to Cryptography",
        help="Hash the string",
    )
    parser.add_argument(
        "-f", "--file", dest="input_file", help="Hash contents of a file"
    )

    args = parser.parse_args()

    input_string = args.input_string

    # hash input should be a bytestring
    if args.input_file:
        with open(args.input_file, "rb") as f:
            hash_input = f.read()
    else:
        hash_input = bytes(input_string, "utf-8")

    print(SHA256(hash_input).hash)


if __name__ == "__main__":
    main()

    import doctest

    doctest.testmod()
