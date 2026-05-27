"""Columnar Transposition cipher.

This classical cipher writes the plaintext in rows under a keyword and reads
columns in the order of the alphabetical rank of the keyword letters.

Reference: https://en.wikipedia.org/wiki/Transposition_cipher#Columnar_transposition

We keep spaces and punctuation. Key must be alphabetic (case-insensitive).

>>> pt = "WE ARE DISCOVERED. FLEE AT ONCE"
>>> ct = encrypt(pt, "ZEBRAS")
>>> decrypt(ct, "ZEBRAS") == pt
True

Edge cases:
>>> encrypt("HELLO", "A")
'HELLO'
>>> decrypt("HELLO", "A")
'HELLO'
>>> encrypt("HELLO", "HELLO")
'EHLLO'
>>> decrypt("EHLLO", "HELLO")
'HELLO'
>>> encrypt("HELLO", "")
Traceback (most recent call last):
    ...
ValueError: Key must be a non-empty alphabetic string
"""

from __future__ import annotations


def _normalize_key(key: str) -> str:
    k = "".join(ch for ch in key.upper() if ch.isalpha())
    if not k:
        raise ValueError("Key must be a non-empty alphabetic string")
    return k


def _column_order(key: str) -> list[int]:
    # Stable sort by character then original index to handle duplicates
    indexed = list(enumerate(key))
    return [
        i
        for i, _ in sorted(
            indexed, key=lambda indexed_pair: (indexed_pair[1], indexed_pair[0])
        )
    ]


def encrypt(plaintext: str, key: str) -> str:
    """Encrypt using columnar transposition.

    :param plaintext: Input text (any characters)
    :param key: Alphabetic keyword
    :return: Ciphertext
    :raises ValueError: on invalid key
    """
    k = _normalize_key(key)
    cols = len(k)
    if cols == 1:
        return plaintext

    order = _column_order(k)

    # Build ragged rows without padding
    rows = (len(plaintext) + cols - 1) // cols
    grid: list[str] = [plaintext[i * cols : (i + 1) * cols] for i in range(rows)]

    # Read columns in sorted order, skipping missing cells
    out: list[str] = []
    for col in order:
        for r in range(rows):
            if col < len(grid[r]):
                out.append(grid[r][col])
    return "".join(out)


def decrypt(ciphertext: str, key: str) -> str:
    """Decrypt columnar transposition ciphertext.

    :param ciphertext: Encrypted text
    :param key: Alphabetic keyword
    :return: Decrypted plaintext
    :raises ValueError: on invalid key
    """
    k = _normalize_key(key)
    cols = len(k)
    if cols == 1:
        return ciphertext

    order = _column_order(k)
    text_len = len(ciphertext)
    rows = (text_len + cols - 1) // cols
    r = text_len % cols

    # Column lengths based on ragged last row (no padding during encryption)
    col_lengths: list[int] = []
    for c in range(cols):
        if r == 0:
            col_lengths.append(rows)
        else:
            col_lengths.append(rows if c < r else rows - 1)

    # Slice ciphertext into columns following the sorted order
    columns: list[str] = [""] * cols
    idx = 0
    for col in order:
        ln = col_lengths[col]
        columns[col] = ciphertext[idx : idx + ln]
        idx += ln

    # Rebuild plaintext row-wise
    out: list[str] = []
    pointers = [0] * cols
    for _ in range(rows * cols):
        c = len(out) % cols
        if pointers[c] < len(columns[c]):
            out.append(columns[c][pointers[c]])
            pointers[c] += 1
    return "".join(out)


if __name__ == "__main__":  # pragma: no cover
    import doctest

    doctest.testmod()
