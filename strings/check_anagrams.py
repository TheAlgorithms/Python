"""
wiki: https://en.wikipedia.org/wiki/Anagram
"""

from collections import defaultdict


def check_anagrams(first_str: str, second_str: str) -> bool:
    """
    Two strings are anagrams if they are made up of the same letters but are
    arranged differently (ignoring the case).
    >>> check_anagrams('This', 'These')
    False
    >>> check_anagrams('Silent', 'Listen')
    True
    >>> check_anagrams('This is a string', 'Is this a string')
    True
    >>> check_anagrams('This is    a      string', 'Is     this a string')
    True
    >>> check_anagrams('There', 'Their')
    False
    """
    first_str = first_str.lower().strip()
    second_str = second_str.lower().strip()

    # Remove whitespace
    first_str = first_str.replace(" ", "")
    second_str = second_str.replace(" ", "")

    # Strings of different lengths are not anagrams
    if len(first_str) != len(second_str):
        return False

    # Default values for count should be 0
    count: defaultdict[str, int] = defaultdict(int)

    # For each character in input strings,
    # increment count in the corresponding
    for i in range(len(first_str)):
        count[first_str[i]] += 1
        count[second_str[i]] -= 1

    return all(_count == 0 for _count in count.values())


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    input_a = input("Enter the first string ").strip()
    input_b = input("Enter the second string ").strip()

    status = check_anagrams(input_a, input_b)
    print(f"{input_a} and {input_b} are {'' if status else 'not '}anagrams.")
