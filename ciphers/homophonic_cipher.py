#!/usr/bin/env python3
"""
# pmhsc - poor man's homophonic substitution cipher

"""
import argparse
import os
import pickle
import random
import sys
import time

from itertools import product
from string import ascii_lowercase


CHARS = ascii_lowercase + ' '


def generate_maps():
    start_time = time.time()

    # get 7 random non-repeating letters and space
    letters = random.sample(CHARS, 8)

    # get the 16,777,216 permutations with repetitions and shuffle them
    perms = [''.join(_) for _ in product(letters, repeat=8)]
    random.shuffle(perms)

    perm_dict = {}
    for l in CHARS:
        l_index = CHARS.index(l)
        perm_dict[l] = perms[621378*l_index:621378*(l_index+1)]

    with open('mapping.p', 'wb') as f:
        pickle.dump(perm_dict, f)

    print('Mapping completed in {0:.2f} seconds.'.format(time.time() - start_time))


def check_file(f_name):
    if not os.path.isfile(f_name):
        print('{}: No such file.'.format(f_name))
        sys.exit(1)


def read_map(map_file):
    if not os.path.isfile(map_file):
        print('Unable to find mapping file, use --genmaps to generate one.')
        sys.exit(1)

    with open(map_file, 'rb') as f:
        return pickle.loads(f.read())


def encrypt(map_file, input_file, output_file):
    check_file(input_file)

    start_time = time.time()

    mapping = read_map(map_file)

    with open(input_file) as f:
        plaintext = f.read()

    with open(output_file, 'w') as f:
        for i in plaintext:
            if i.isalpha() or (i == ' '):
                i = i.lower()
                f.write(random.choice(mapping[i]))

    print('Encryption completed in {0:.2f} seconds.'.format(time.time() - start_time))


def decrypt(map_file, input_file, output_file):
    check_file(input_file)

    start_time = time.time()

    mapping = read_map(map_file)

    def search_mapping(s):
        for k, vals in mapping.items():
            for v in vals:
                if v == s:
                    return k

    with open(input_file) as f:
        ciphertext = f.read()

    plaintext = ''
    enc_letters = [ciphertext[x:x+8] for x in range(0, len(ciphertext), 8)]
    for l in enc_letters:
        plaintext += search_mapping(l)

    with open(output_file, 'w') as f:
        f.write(plaintext+'\n')

    print('Decryption completed in {0:.2f} seconds.'.format(time.time() - start_time))


def get_parser():
    parser = argparse.ArgumentParser(description='poor man\'s homophonic substitution cipher')
    parser.add_argument('-g', '--genmaps',
                        help='generate mapping file', action='store_true')
    parser.add_argument('-e', '--encrypt',
                        help='encrypt a file', action='store_true')
    parser.add_argument('-d', '--decrypt',
                        help='decrypt a file', action='store_true')
    parser.add_argument('-m', '--mapping',
                        help='specify a mapping file to use (default: mapping.p)',
                        type=str, default='mapping.p')
    parser.add_argument('-i', '--input',
                        help='input file', type=str)
    parser.add_argument('-o', '--output',
                        help='output file', type=str)

    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    if not (args['genmaps'] or args['encrypt'] or args['decrypt']):
        parser.print_help()
        return

    if args['genmaps']:
        generate_maps()
        return

    if not args['input']:
        print('Input file not supplied.')
        return
    if not args['output']:
        print('Output file not supplied.')
        return

    if args['encrypt']:
        encrypt(args['mapping'], args['input'], args['output'])
        return
    if args['decrypt']:
        decrypt(args['mapping'], args['input'], args['output'])
        return


if __name__ == '__main__':
    main()