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
    # Declare frequency as a set to have unique occurrences of letters
    frequency = set()

    # Replace all the whitespace in our sentence
    input_str = input_str.replace(" ", "")
    for alpha in input_str:
        if "a" <= alpha.lower() <= "z":
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


def benchmark() -> None:
    """
    Benchmark code comparing different version.
    """
    from timeit import timeit

    setup = "from __main__ import is_pangram, is_pangram_faster, is_pangram_fastest"
    print(timeit("is_pangram()", setup=setup))
    print(timeit("is_pangram_faster()", setup=setup))
    print(timeit("is_pangram_fastest()", setup=setup))
    # 5.348480500048026, 2.6477354579837993, 1.8470395830227062
    # 5.036091582966037, 2.644472333951853,  1.8869528750656173


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
