"""https://en.wikipedia.org/wiki/Atbash"""

import string
from timeit import timeit  # Moved to top-level as required


def atbash_slow(sequence: str) -> str:
    """
    Atbash cipher implementation using ordinal values.
    Encodes/decodes by reversing the alphabet.

    >>> atbash_slow("ABCDEFG")
    'ZYXWVUT'

    >>> atbash_slow("aW;;123BX")
    'zD;;123YC'
    """
    output = ""
    for char in sequence:
        code = ord(char)
        if 65 <= code <= 90:  # Uppercase A-Z
            output += chr(155 - code)
        elif 97 <= code <= 122:  # Lowercase a-z
            output += chr(219 - code)
        else:  # Non-alphabetic characters
            output += char
    return output


def atbash(sequence: str) -> str:
    """
    Optimized Atbash cipher implementation using string translation.
    More efficient than ordinal-based approach.

    >>> atbash("ABCDEFG")
    'ZYXWVUT'

    >>> atbash("aW;;123BX")
    'zD;;123YC'
    """
    # Create translation tables
    letters = string.ascii_letters
    reversed_letters = string.ascii_lowercase[::-1] + string.ascii_uppercase[::-1]

    # Create translation mapping
    translation = str.maketrans(letters, reversed_letters)

    # Apply translation to each character
    return sequence.translate(translation)


def benchmark() -> None:
    """
    Performance comparison of both Atbash implementations.
    Measures execution time using Python's timeit module.
    """
    print("Running performance benchmarks...")
    setup = "from string import printable; from __main__ import atbash, atbash_slow"
    # Time the slow implementation
    slow_time = timeit("atbash_slow(printable)", setup=setup)
    print(f"> atbash_slow(): {slow_time:.6f} seconds")

    # Time the optimized implementation
    fast_time = timeit("atbash(printable)", setup=setup)
    print(f">      atbash(): {fast_time:.6f} seconds")


if __name__ == "__main__":
    # Test examples
    examples = ("ABCDEFGH", "123GGjj", "testStringtest", "with space")
    for example in examples:
        print(f"{example} encrypted in atbash: {atbash(example)}")

    # Run performance comparison
    benchmark()
