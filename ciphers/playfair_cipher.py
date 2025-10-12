"""
https://en.wikipedia.org/wiki/Playfair_cipher#Description

The Playfair cipher was developed by Charles Wheatstone in 1854
It's use was heavily promotedby Lord Playfair, hence its name

Some features of the Playfair cipher are:

1) It was the first literal diagram substitution cipher
2) It is a manual symmetric encryption technique
3) It is a multiple letter encryption cipher

The implementation in the code below encodes alphabets only.
It removes spaces, special characters and numbers from the
code.

Playfair is no longer used by military forces because of known
insecurities and of the advent of automated encryption devices.
This cipher is regarded as insecure since before World War I.
"""

import itertools
import string
from collections.abc import Generator, Iterable


def chunker(seq: Iterable[str], size: int) -> Generator[tuple[str, ...]]:
    it = iter(seq)
    while True:
        chunk = tuple(itertools.islice(it, size))
        if not chunk:
            return
        yield chunk


def prepare_input(dirty: str) -> str:
    """
    Prepare the plaintext by up-casing it
    and separating repeated letters with X's
    """

    dirty = "".join([c.upper() for c in dirty if c in string.ascii_letters])
    clean = ""

    if len(dirty) < 2:
        return dirty

    for i in range(len(dirty) - 1):
        clean += dirty[i]

        if dirty[i] == dirty[i + 1]:
            clean += "X"

    clean += dirty[-1]

    if len(clean) & 1:
        clean += "X"

    return clean


def generate_table(key: str) -> list[str]:
    # I and J are used interchangeably to allow
    # us to use a 5x5 table (25 letters)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # we're using a list instead of a '2d' array because it makes the math
    # for setting up the table and doing the actual encoding/decoding simpler
    table = []

    # copy key chars into the table if they are in `alphabet` ignoring duplicates
    for char in key.upper():
        if char not in table and char in alphabet:
            table.append(char)

    # fill the rest of the table in with the remaining alphabet chars
    for char in alphabet:
        if char not in table:
            table.append(char)

    return table


def encode(plaintext: str, key: str) -> str:
    """
    Encode the given plaintext using the Playfair cipher.
    Takes the plaintext and the key as input and returns the encoded string.

    >>> encode("Hello", "MONARCHY")
    'CFSUPM'
    >>> encode("attack on the left flank", "EMERGENCY")
    'DQZSBYFSDZFMFNLOHFDRSG'
    >>> encode("Sorry!", "SPECIAL")
    'AVXETX'
    >>> encode("Number 1", "NUMBER")
    'UMBENF'
    >>> encode("Photosynthesis!", "THE SUN")
    'OEMHQHVCHESUKE'
    """

    table = generate_table(key)
    plaintext = prepare_input(plaintext)
    ciphertext = ""

    for char1, char2 in chunker(plaintext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)

        if row1 == row2:
            ciphertext += table[row1 * 5 + (col1 + 1) % 5]
            ciphertext += table[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += table[((row1 + 1) % 5) * 5 + col1]
            ciphertext += table[((row2 + 1) % 5) * 5 + col2]
        else:  # rectangle
            ciphertext += table[row1 * 5 + col2]
            ciphertext += table[row2 * 5 + col1]

    return ciphertext


def decode(ciphertext: str, key: str) -> str:
    """
    Decode the input string using the provided key.

    >>> decode("BMZFAZRZDH", "HAZARD")
    'FIREHAZARD'
    >>> decode("HNBWBPQT", "AUTOMOBILE")
    'DRIVINGX'
    >>> decode("SLYSSAQS", "CASTLE")
    'ATXTACKX'
    """

    table = generate_table(key)
    plaintext = ""

    for char1, char2 in chunker(ciphertext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)

        if row1 == row2:
            plaintext += table[row1 * 5 + (col1 - 1) % 5]
            plaintext += table[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            plaintext += table[((row1 - 1) % 5) * 5 + col1]
            plaintext += table[((row2 - 1) % 5) * 5 + col2]
        else:  # rectangle
            plaintext += table[row1 * 5 + col2]
            plaintext += table[row2 * 5 + col1]

    return plaintext


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Encoded:", encode("BYE AND THANKS", "GREETING"))
    print("Decoded:", decode("CXRBANRLBALQ", "GREETING"))
