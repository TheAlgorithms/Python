from __future__ import annotations
from string import ascii_letters


def encrypt(input_string: str, key: int, alphabet: str | None = None) -> str:
    """
    Encrypts a given string with the Caesar cipher and returns the encoded message.

    Parameters
    ----------
    input_string : str
        The plain-text that needs to be encoded.
    key : int
        The number of letters to shift the message by.
    alphabet : str | None, optional
        The alphabet used to encode the cipher.
        If not specified, the standard English alphabet (a-z, A-Z) is used.

    Returns
    -------
    str
        A string containing the encoded cipher-text.

    Raises
    ------
    TypeError
        If input_string is not a string or key is not an integer.

    Examples
    --------
    >>> encrypt('The quick brown fox jumps over the lazy dog', 8)
    'Bpm yCqks jzwEv nwF rCuxA wDmz Bpm tiHG lwo'
    >>> encrypt('a lowercase alphabet', 5, 'abcdefghijklmnopqrstuvwxyz')
    'f qtbjwhfxj fqumfgjy'
    """
    if not isinstance(input_string, str):
        raise TypeError("input_string must be a string.")
    if not isinstance(key, int):
        raise TypeError("key must be an integer.")

    alpha = alphabet or ascii_letters
    result = []

    for character in input_string:
        if character not in alpha:
            result.append(character)
        else:
            new_index = (alpha.index(character) + key) % len(alpha)
            result.append(alpha[new_index])

    return "".join(result)


def decrypt(input_string: str, key: int, alphabet: str | None = None) -> str:
    """
    Decodes a Caesar cipher text using the provided key.

    Parameters
    ----------
    input_string : str
        The cipher-text that needs to be decoded.
    key : int
        The number of letters to shift backward.
    alphabet : str | None, optional
        The alphabet used to decode the cipher.

    Returns
    -------
    str
        The decoded plain-text.

    Examples
    --------
    >>> decrypt('Bpm yCqks jzwEv nwF rCuxA wDmz Bpm tiHG lwo', 8)
    'The quick brown fox jumps over the lazy dog'
    """
    return encrypt(input_string, -key, alphabet)


def brute_force(input_string: str, alphabet: str | None = None) -> dict[int, str]:
    """
    Attempts to brute-force all possible Caesar cipher keys.

    Parameters
    ----------
    input_string : str
        The cipher-text to attempt decoding.
    alphabet : str | None, optional
        The alphabet used to decode the cipher.

    Returns
    -------
    dict[int, str]
        A dictionary mapping each key to its decoded message.

    Examples
    --------
    >>> brute_force("jFyuMy xIH'N vLONy zILwy Gy!")[20]
    "Please don't brute force me!"
    """
    if not isinstance(input_string, str):
        raise TypeError("input_string must be a string.")

    alpha = alphabet or ascii_letters
    results = {}

    for key in range(1, len(alpha) + 1):
        results[key] = decrypt(input_string, key, alpha)

    return results
