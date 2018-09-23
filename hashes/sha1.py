"""
Demonstrates implementation of SHA1 Hash function in a Python class and gives utilities
to find hash of string or hash of text from a file.
Usage: python sha1.py --string "Hello World Welcome to Cryptography"
       pyhton sha1.py --file "hello_world.txt"
       Without any arguments prints the hash of the string "Hello World"
Also contains a Test class to verify that the generated Hash is same as that
returned by the hashlib library

The Algorithm as described in the reference:
First we start with a message. The message is padded and the length of the message
is added to the end. It is then split into blocks of 512 bits. The blocks are then
processed one at a time. Each block must be expanded and compressed.
The value after each compression is added to a 160bit buffer called the current hash
state. After the last block is processed the current hash state is returned as
the final hash.
Reference: https://deadhacker.com/2006/02/21/sha-1-illustrated/
"""

import argparse
import hashlib #hashlib is only used inside the Test class



class SHA1Hash:
    """
    Class to contain the entire pipeline for SHA1 Hashing Algorithm
    """
    
    H0 - 01100111010001010010001100000001
    H1 - 11101111110011011010101110001001
    H2 - 10011000101110101101110011111110
    H3 - 00010000001100100101010001110110
    H4 - 11000011110100101110000111110000

    def __init__(self, data):
        self.data = data
        self.current_hash = ''

    def padding(self):
        return

    def split_block(self):
        return

    def expand_block(self):
        return

    def compress_block(self):
        return

    def final_hash(self):
        return 'This is in my To Do list'

class SHA1HashTest:
    """
    Test class for the SHA1 class
    """
    def __init__(self, data):
        self.data = data

    def calculated_hash(self):
        return SHA1Hash(self.data).final_hash()

    def hashlib_hash(self):
        return hashlib.sha1(self.data.byte_encode()).hexdigest()

    def byte_encode(self):
        return bytes(self.data, 'utf-8')

    def match_hashes(self):
        # self.assertEqual(self.calculated_hash(), self.hashlib_hash())
        return self.calculated_hash() == self.hashlib_hash()

def run_test_case(hash_input = 'Hello World'):
    """
    Pulled this out of main because we probably dont want to run the Test
    each time we want to calculate hash.
    """
    print(SHA1HashTest(hash_input).match_hashes())


def main():
    parser = argparse.ArgumentParser(description='Process some strings or files')
    parser.add_argument('--string', dest='input_string', default='Hello World',
                        help='Hash the string')
    parser.add_argument('--file', dest='input_file', help='Hash contents of a file')
    args = parser.parse_args()
    input_string = args.input_string
    if args.input_file:
        hash_input = open(args.input_file, 'r').read()
    else:
        hash_input = input_string
    print(SHA1Hash(hash_input).final_hash())

if __name__ == '__main__':
    main()
