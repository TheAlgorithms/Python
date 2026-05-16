"""
Each character on a computer is assigned a unique code and the preferred standard is
ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then
XOR each byte with a given value, taken from a secret key. The advantage with the
XOR function is that using the same encryption key on the cipher text, restores
the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and
the key is made up of random bytes. The user would keep the encrypted message and the
encryption key in different locations, and without both "halves", it is impossible to
decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is
to use a password as a key. If the password is shorter than the message, which is
likely, the key is repeated cyclically throughout the message. The balance for this
method is using a sufficiently long password key for security, but short enough to
be memorable.

Your task has been made easy, as the encryption key consists of three lower case
characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a
file containing the encrypted ASCII codes, and the knowledge that the plain text
must contain common English words, decrypt the message and find the sum of the ASCII
values in the original text.
"""

from __future__ import annotations

import string
from itertools import cycle, product
from pathlib import Path

VALID_CHARS: str = (
    string.ascii_letters + string.digits + string.punctuation + string.whitespace
)
LOWERCASE_INTS: list[int] = [ord(letter) for letter in string.ascii_lowercase]
VALID_INTS: set[int] = {ord(char) for char in VALID_CHARS}

COMMON_WORDS: list[str] = ["the", "be", "to", "of", "and", "in", "that", "have"]


def try_key(ciphertext: list[int], key: tuple[int, ...]) -> str | None:
    """
    Given an encrypted message and a possible 3-character key, decrypt the message.
    If the decrypted message contains a invalid character, i.e. not an ASCII letter,
    a digit, punctuation or whitespace, then we know the key is incorrect, so return
    None.
    >>> try_key([0, 17, 20, 4, 27], (104, 116, 120))
    'hello'
    >>> try_key([68, 10, 300, 4, 27], (104, 116, 120)) is None
    True
    """
    decoded: str = ""
    keychar: int
    cipherchar: int
    decodedchar: int

    for keychar, cipherchar in zip(cycle(key), ciphertext):
        decodedchar = cipherchar ^ keychar
        if decodedchar not in VALID_INTS:
            return None
        decoded += chr(decodedchar)

    return decoded


def filter_valid_chars(ciphertext: list[int]) -> list[str]:
    """
    Given an encrypted message, test all 3-character strings to try and find the
    key. Return a list of the possible decrypted messages.
    >>> from itertools import cycle
    >>> text = "The enemy's gate is down"
    >>> key = "end"
    >>> encoded = [ord(k) ^ ord(c) for k,c in zip(cycle(key), text)]
    >>> text in filter_valid_chars(encoded)
    True
    """
    possibles: list[str] = []
    for key in product(LOWERCASE_INTS, repeat=3):
        encoded = try_key(ciphertext, key)
        if encoded is not None:
            possibles.append(encoded)
    return possibles


def filter_common_word(possibles: list[str], common_word: str) -> list[str]:
    """
    Given a list of possible decoded messages, narrow down the possibilities
    for checking for the presence of a specified common word. Only decoded messages
    containing common_word will be returned.
    >>> filter_common_word(['asfla adf', 'I am here', '   !?! #a'], 'am')
    ['I am here']
    >>> filter_common_word(['athla amf', 'I am here', '   !?! #a'], 'am')
    ['athla amf', 'I am here']
    """
    return [possible for possible in possibles if common_word in possible.lower()]


def solution(filename: str = "p059_cipher.txt") -> int:
    """
    Test the ciphertext against all possible 3-character keys, then narrow down the
    possibilities by filtering using common words until there's only one possible
    decoded message.
    >>> solution("test_cipher.txt")
    3000
    """
    ciphertext: list[int]
    possibles: list[str]
    common_word: str
    decoded_text: str
    data: str = Path(__file__).parent.joinpath(filename).read_text(encoding="utf-8")

    ciphertext = [int(number) for number in data.strip().split(",")]

    possibles = filter_valid_chars(ciphertext)
    for common_word in COMMON_WORDS:
        possibles = filter_common_word(possibles, common_word)
        if len(possibles) == 1:
            break

    decoded_text = possibles[0]
    return sum(ord(char) for char in decoded_text)


if __name__ == "__main__":
    print(f"{solution() = }")
