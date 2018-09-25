"""
Demonstrates implementation of SHA1 Hash function in a Python class and gives utilities
to find hash of string or hash of text from a file.
Usage: python sha1.py --string "Hello World!!"
       pyhton sha1.py --file "hello_world.txt"
       When run without any arguments, it prints the hash of the string "Hello World!! Welcome to Cryptography"
Also contains a Test class to verify that the generated Hash is same as that
returned by the hashlib library

SHA1 hash or SHA1 sum of a string is a crytpographic function which means it is easy
to calculate forwards but extemely difficult to calculate backwards. What this means
is, you can easily calculate the hash of  a string, but it is extremely difficult to
know the original string if you have its hash. This property is useful to communicate
securely, send encrypted messages and is very useful in payment systems, blockchain
and cryptocurrency etc.
The Algorithm as described in the reference:
First we start with a message. The message is padded and the length of the message
is added to the end. It is then split into blocks of 512 bits or 64 bytes. The blocks
are then processed one at a time. Each block must be expanded and compressed.
The value after each compression is added to a 160bit buffer called the current hash
state. After the last block is processed the current hash state is returned as
the final hash.
Reference: https://deadhacker.com/2006/02/21/sha-1-illustrated/
"""

import argparse
import struct
import hashlib #hashlib is only used inside the Test class
import unittest


class SHA1Hash:
    """
    Class to contain the entire pipeline for SHA1 Hashing Algorithm
    """

    def __init__(self, data):
        """
        Inititates the variables data and h. h is a list of 5 8-digit Hexadecimal
        numbers corresponding to (1732584193, 4023233417, 2562383102, 271733878, 3285377520)
        respectively. We will start with this as a message digest. 0x is how you write
        Hexadecimal numbers in Python
        """
        self.data = data
        self.h = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]

    @staticmethod
    def rotate(n, b):
        """
        Static method to be used inside other methods. Left rotates n by b.
        """
        return ((n << b) | (n >> (32 - b))) & 0xffffffff

    def padding(self):
        """
        Pads the input message with zeros so that padded_data has 64 bytes or 512 bits
        """
        padding = b'\x80' + b'\x00'*(63 - (len(self.data) + 8) % 64)
        padded_data = self.data + padding + struct.pack('>Q', 8 * len(self.data))
        return padded_data

    def split_blocks(self):
        """
        Returns a list of bytestrings each of length 64
        """
        return [self.padded_data[i:i+64] for i in range(0, len(self.padded_data), 64)]

    # @staticmethod
    def expand_block(self, block):
        """
        Takes block of 64 and returns list of length 80.
        It is really a static method but
        we need the rotate method inside, so we will have to use self
        """
        w = list(struct.unpack('>16L', block)) + [0] * 64
        for i in range(16, 80):
            w[i] = self.rotate((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1)
        return w

    def final_hash(self):
        """
        Calls all the other methods to process the input. Returns SHA1 hash
        """
        self.padded_data = self.padding()
        self.blocks = self.split_blocks()
        for block in self.blocks:
            expanded_block = self.expand_block(block)
            a, b, c, d, e = self.h
            for i in range(0, 80):
                if 0 <= i < 20:
                    f = (b & c) | ((~b) & d)
                    k = 0x5A827999
                elif 20 <= i < 40:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif 40 <= i < 60:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                elif 60 <= i < 80:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6
                a, b, c, d, e = self.rotate(a, 5) + f + e + k + expanded_block[i] & 0xffffffff,\
                                a, self.rotate(b, 30), c, d
        self.h = self.h[0] + a & 0xffffffff,\
                 self.h[1] + b & 0xffffffff,\
                 self.h[2] + c & 0xffffffff,\
                 self.h[3] + d & 0xffffffff,\
                 self.h[4] + e & 0xffffffff

        return '%08x%08x%08x%08x%08x' %tuple(self.h)


class SHA1HashTest(unittest.TestCase):
    """
    Test class for the SHA1Hash class. Inherits the TestCase class from unittest
    """
    def testMatchHashes(self):
        msg = bytes("Hello World", 'utf-8')
        self.assertEqual(SHA1Hash(msg).final_hash(), hashlib.sha1(msg).hexdigest())

def run_test():
    """
    Run the unit test. Pulled this out of main because we probably dont want to run
    the test each time.
    """
    unittest.main()

def main():
    """
    Provides option string or file to take input and prints the calculated SHA1 hash
    """
    parser = argparse.ArgumentParser(description='Process some strings or files')
    parser.add_argument('--string', dest='input_string',
                        default='Hello World!! Welcome to Cryptography',
                        help='Hash the string')
    parser.add_argument('--file', dest='input_file', help='Hash contents of a file')
    args = parser.parse_args()
    input_string = args.input_string
    #In any case hash input should be a bytestring
    if args.input_file:
        hash_input = open(args.input_file, 'rb').read()
    else:
        hash_input = bytes(input_string, 'utf-8')
    print(SHA1Hash(hash_input).final_hash())

if __name__ == '__main__':
    main()
