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
    return len(set(c for c in input_str.lower() if c.isalpha())) == 26


if __name__ == "__main__":
    import doctest

    doctest.testmod()
