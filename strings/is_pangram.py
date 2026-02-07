"""
wiki: https://en.wikipedia.org/wiki/Pangram
"""


def is_pangram(
    input_str: str = "The quick brown fox jumps over the lazy dog",
) -> bool:
    """
    A Pangram String contains all the alphabets at least once.
    >>> is_pangram("The quick brown fox jumps over the lazy dog")
    True
    >>> is_pangram("Waltz, bad nymph, for quick jigs vex.")
    True
    >>> is_pangram("Jived fox nymph grabs quick waltz.")
    True
    >>> is_pangram("My name is Unknown")
    False
    >>> is_pangram("The quick brown fox jumps over the la_y dog")
    False
    >>> is_pangram()
    True
    """
    frequency = set()
    input_str = input_str.replace(" ", "")
    for alpha in input_str:
        if alpha.isalpha():
            frequency.add(alpha.lower())
    return len(frequency) == 26


def is_pangram_faster(
    input_str: str = "The quick brown fox jumps over the lazy dog",
) -> bool:
    """
    >>> is_pangram_faster("The quick brown fox jumps over the lazy dog")
    True
    >>> is_pangram_faster("Waltz, bad nymph, for quick jigs vex.")
    True
    >>> is_pangram_faster("Jived fox nymph grabs quick waltz.")
    True
    >>> is_pangram_faster("The quick brown fox jumps over the la_y dog")
    False
    >>> is_pangram_faster()
    True
    """
    flag = [False] * 26
    for char in input_str:
        if char.islower():
            flag[ord(char) - 97] = True
        elif char.isupper():
            flag[ord(char) - 65] = True
    return all(flag)


def is_pangram_fastest(
    input_str: str = "The quick brown fox jumps over the lazy dog",
) -> bool:
    """
    >>> is_pangram_fastest("The quick brown fox jumps over the lazy dog")
    True
    >>> is_pangram_fastest("Waltz, bad nymph, for quick jigs vex.")
    True
    >>> is_pangram_fastest("Jived fox nymph grabs quick waltz.")
    True
    >>> is_pangram_fastest("The quick brown fox jumps over the la_y dog")
    False
    >>> is_pangram_fastest()
    True
    """
    return len({char for char in input_str.lower() if char.isalpha()}) == 26
