"""Scytale (Skytale) transposition cipher.

A classical transposition cipher used in ancient Greece. The sender wraps a
strip of parchment around a rod (scytale) and writes the message along the rod.
The recipient with a rod of the same diameter can read the message.

Reference: https://en.wikipedia.org/wiki/Scytale

Functions here keep characters as-is (including spaces). The key is a positive
integer representing the circumference count (number of rows).

>>> encrypt("WE ARE DISCOVERED FLEE AT ONCE", 3)
'WA SVEFETNERDCEDL  C EIOR EAOE'
>>> decrypt('WA SVEFETNERDCEDL  C EIOR EAOE', 3)
'WE ARE DISCOVERED FLEE AT ONCE'

Edge cases:
>>> encrypt("HELLO", 1)
'HELLO'
>>> decrypt("HELLO", 1)
'HELLO'
>>> encrypt("HELLO", 5)  # key equals length
'HELLO'
>>> decrypt("HELLO", 5)
'HELLO'
>>> encrypt("HELLO", 0)
Traceback (most recent call last):
    ...
ValueError: Key must be a positive integer
>>> decrypt("HELLO", -2)
Traceback (most recent call last):
    ...
ValueError: Key must be a positive integer
"""

from __future__ import annotations


def encrypt(plaintext: str, key: int) -> str:
    """Encrypt plaintext using Scytale transposition.

    Write characters around a rod with `key` rows, then read off by rows.

    :param plaintext: Input message to encrypt
    :param key: Positive integer number of rows
    :return: Ciphertext string
    :raises ValueError: if key <= 0
    """
    if key <= 0:
        raise ValueError("Key must be a positive integer")
    if key == 1 or len(plaintext) <= key:
        return plaintext

    # Read every key-th character starting from each row offset
    return "".join(plaintext[row::key] for row in range(key))


def decrypt(ciphertext: str, key: int) -> str:
    """Decrypt Scytale ciphertext.

    Reconstruct rows by their lengths and interleave by columns.

    :param ciphertext: Encrypted string
    :param key: Positive integer number of rows
    :return: Decrypted plaintext
    :raises ValueError: if key <= 0
    """
    if key <= 0:
        raise ValueError("Key must be a positive integer")
    if key == 1 or len(ciphertext) <= key:
        return ciphertext

    length = len(ciphertext)
    base = length // key
    extra = length % key

    # Determine each row length
    row_lengths: list[int] = [base + (1 if r < extra else 0) for r in range(key)]

    # Slice ciphertext into rows
    rows: list[str] = []
    idx = 0
    for r_len in row_lengths:
        rows.append(ciphertext[idx : idx + r_len])
        idx += r_len

    # Pointers to current index in each row
    pointers = [0] * key

    # Reconstruct by taking characters column-wise across rows
    result_chars: list[str] = []
    for i in range(length):
        r = i % key
        if pointers[r] < len(rows[r]):
            result_chars.append(rows[r][pointers[r]])
            pointers[r] += 1
    return "".join(result_chars)


if __name__ == "__main__":  # pragma: no cover
    import doctest

    doctest.testmod()
