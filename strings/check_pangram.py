import doctest


def check_pangram(input_str: str) -> bool:
    """
    Check if a string is a pangram (contains every letter of the alphabet).
    >>> check_pangram("The quick brown fox jumps over the lazy dog")
    True
    >>> check_pangram("Hello World")
    False
    >>> check_pangram("")
    False
    """
    return {c for c in input_str.lower() if c.isalpha()} == set(
        "abcdefghijklmnopqrstuvwxyz"
    )


if __name__ == "__main__":
    doctest.testmod()
