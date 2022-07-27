"""
https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform

The Burrows–Wheeler transform (BWT, also called block-sorting compression)
rearranges a character string into runs of similar characters. This is useful
for compression, since it tends to be easy to compress a string that has runs
of repeated characters by techniques such as move-to-front transform and
run-length encoding. More importantly, the transformation is reversible,
without needing to store any additional data except the position of the first
original character. The BWT is thus a "free" method of improving the efficiency
of text compression algorithms, costing only some extra computation.
"""
from __future__ import annotations

from typing import TypedDict


class BWTTransformDict(TypedDict):
    bwt_string: str
    idx_original_string: int


def all_rotations(s: str) -> list[str]:
    """
    :param s: The string that will be rotated len(s) times.
    :return: A list with the rotations.
    :raises TypeError: If s is not an instance of str.
    Examples:

    >>> all_rotations("^BANANA|") # doctest: +NORMALIZE_WHITESPACE
    ['^BANANA|', 'BANANA|^', 'ANANA|^B', 'NANA|^BA', 'ANA|^BAN', 'NA|^BANA',
    'A|^BANAN', '|^BANANA']
    >>> all_rotations("a_asa_da_casa") # doctest: +NORMALIZE_WHITESPACE
    ['a_asa_da_casa', '_asa_da_casaa', 'asa_da_casaa_', 'sa_da_casaa_a',
    'a_da_casaa_as', '_da_casaa_asa', 'da_casaa_asa_', 'a_casaa_asa_d',
    '_casaa_asa_da', 'casaa_asa_da_', 'asaa_asa_da_c', 'saa_asa_da_ca',
    'aa_asa_da_cas']
    >>> all_rotations("panamabanana") # doctest: +NORMALIZE_WHITESPACE
    ['panamabanana', 'anamabananap', 'namabananapa', 'amabananapan',
    'mabananapana', 'abananapanam', 'bananapanama', 'ananapanamab',
    'nanapanamaba', 'anapanamaban', 'napanamabana', 'apanamabanan']
    >>> all_rotations(5)
    Traceback (most recent call last):
        ...
    TypeError: The parameter s type must be str.
    """
    if not isinstance(s, str):
        raise TypeError("The parameter s type must be str.")

    return [s[i:] + s[:i] for i in range(len(s))]


def bwt_transform(s: str) -> BWTTransformDict:
    """
    :param s: The string that will be used at bwt algorithm
    :return: the string composed of the last char of each row of the ordered
    rotations and the index of the original string at ordered rotations list
    :raises TypeError: If the s parameter type is not str
    :raises ValueError: If the s parameter is empty
    Examples:

    >>> bwt_transform("^BANANA")
    {'bwt_string': 'BNN^AAA', 'idx_original_string': 6}
    >>> bwt_transform("a_asa_da_casa")
    {'bwt_string': 'aaaadss_c__aa', 'idx_original_string': 3}
    >>> bwt_transform("panamabanana")
    {'bwt_string': 'mnpbnnaaaaaa', 'idx_original_string': 11}
    >>> bwt_transform(4)
    Traceback (most recent call last):
        ...
    TypeError: The parameter s type must be str.
    >>> bwt_transform('')
    Traceback (most recent call last):
        ...
    ValueError: The parameter s must not be empty.
    """
    if not isinstance(s, str):
        raise TypeError("The parameter s type must be str.")
    if not s:
        raise ValueError("The parameter s must not be empty.")

    rotations = all_rotations(s)
    rotations.sort()  # sort the list of rotations in alphabetically order
    # make a string composed of the last char of each rotation
    response: BWTTransformDict = {
        "bwt_string": "".join([word[-1] for word in rotations]),
        "idx_original_string": rotations.index(s),
    }
    return response


def reverse_bwt(bwt_string: str, idx_original_string: int) -> str:
    """
    :param bwt_string: The string returned from bwt algorithm execution
    :param idx_original_string: A 0-based index of the string that was used to
    generate bwt_string at ordered rotations list
    :return: The string used to generate bwt_string when bwt was executed
    :raises TypeError: If the bwt_string parameter type is not str
    :raises ValueError: If the bwt_string parameter is empty
    :raises TypeError: If the idx_original_string type is not int or if not
    possible to cast it to int
    :raises ValueError: If the idx_original_string value is lower than 0 or
    greater than len(bwt_string) - 1

    >>> reverse_bwt("BNN^AAA", 6)
    '^BANANA'
    >>> reverse_bwt("aaaadss_c__aa", 3)
    'a_asa_da_casa'
    >>> reverse_bwt("mnpbnnaaaaaa", 11)
    'panamabanana'
    >>> reverse_bwt(4, 11)
    Traceback (most recent call last):
        ...
    TypeError: The parameter bwt_string type must be str.
    >>> reverse_bwt("", 11)
    Traceback (most recent call last):
        ...
    ValueError: The parameter bwt_string must not be empty.
    >>> reverse_bwt("mnpbnnaaaaaa", "asd") # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    TypeError: The parameter idx_original_string type must be int or passive
    of cast to int.
    >>> reverse_bwt("mnpbnnaaaaaa", -1)
    Traceback (most recent call last):
        ...
    ValueError: The parameter idx_original_string must not be lower than 0.
    >>> reverse_bwt("mnpbnnaaaaaa", 12) # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    ValueError: The parameter idx_original_string must be lower than
    len(bwt_string).
    >>> reverse_bwt("mnpbnnaaaaaa", 11.0)
    'panamabanana'
    >>> reverse_bwt("mnpbnnaaaaaa", 11.4)
    'panamabanana'
    """
    if not isinstance(bwt_string, str):
        raise TypeError("The parameter bwt_string type must be str.")
    if not bwt_string:
        raise ValueError("The parameter bwt_string must not be empty.")
    try:
        idx_original_string = int(idx_original_string)
    except ValueError:
        raise TypeError(
            "The parameter idx_original_string type must be int or passive"
            " of cast to int."
        )
    if idx_original_string < 0:
        raise ValueError("The parameter idx_original_string must not be lower than 0.")
    if idx_original_string >= len(bwt_string):
        raise ValueError(
            "The parameter idx_original_string must be lower than" " len(bwt_string)."
        )

    ordered_rotations = [""] * len(bwt_string)
    for x in range(len(bwt_string)):
        for i in range(len(bwt_string)):
            ordered_rotations[i] = bwt_string[i] + ordered_rotations[i]
        ordered_rotations.sort()
    return ordered_rotations[idx_original_string]


if __name__ == "__main__":
    entry_msg = "Provide a string that I will generate its BWT transform: "
    s = input(entry_msg).strip()
    result = bwt_transform(s)
    print(
        f"Burrows Wheeler transform for string '{s}' results "
        f"in '{result['bwt_string']}'"
    )
    original_string = reverse_bwt(result["bwt_string"], result["idx_original_string"])
    print(
        f"Reversing Burrows Wheeler transform for entry '{result['bwt_string']}' "
        f"we get original string '{original_string}'"
    )
