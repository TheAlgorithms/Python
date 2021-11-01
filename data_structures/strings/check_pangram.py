"""
wiki: https://en.wikipedia.org/wiki/Pangram
"""


def check_pangram(
    input_str: str = "The quick brown fox jumps over the lazy dog",
) -> bool:
    """
    A Pangram String contains all the alphabets at least once.
    >>> check_pangram("The quick brown fox jumps over the lazy dog")
    True
    >>> check_pangram("Waltz, bad nymph, for quick jigs vex.")
    True
    >>> check_pangram("Jived fox nymph grabs quick waltz.")
    True
    >>> check_pangram("My name is Unknown")
    False
    >>> check_pangram("The quick brown fox jumps over the la_y dog")
    False
    >>> check_pangram()
    True
    """
    frequency = set()
    input_str = input_str.replace(
        " ", ""
    )  # Replacing all the Whitespaces in our sentence
    for alpha in input_str:
        if "a" <= alpha.lower() <= "z":
            frequency.add(alpha.lower())

    return True if len(frequency) == 26 else False


def check_pangram_faster(
    input_str: str = "The quick brown fox jumps over the lazy dog",
) -> bool:
    """
    >>> check_pangram_faster("The quick brown fox jumps over the lazy dog")
    True
    >>> check_pangram_faster("Waltz, bad nymph, for quick jigs vex.")
    True
    >>> check_pangram_faster("Jived fox nymph grabs quick waltz.")
    True
    >>> check_pangram_faster("The quick brown fox jumps over the la_y dog")
    False
    >>> check_pangram_faster()
    True
    """
    flag = [False] * 26
    for char in input_str:
        if char.islower():
            flag[ord(char) - 97] = True
        elif char.isupper():
            flag[ord(char) - 65] = True
    return all(flag)


def benchmark() -> None:
    """
    Benchmark code comparing different version.
    """
    from timeit import timeit

    setup = "from __main__ import check_pangram, check_pangram_faster"
    print(timeit("check_pangram()", setup=setup))
    print(timeit("check_pangram_faster()", setup=setup))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
