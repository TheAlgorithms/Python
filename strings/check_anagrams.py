"""
wiki: https://en.wikipedia.org/wiki/Anagram
"""


def check_anagrams(first_str: str, second_str: str) -> bool:
    """
    Two strings are anagrams if they are made up of the same letters but are
    arranged differently (ignoring the case).
    >>> check_anagrams('Silent', 'Listen')
    True
    >>> check_anagrams('This is a string', 'Is this a string')
    True
    >>> check_anagrams('This is    a      string', 'Is     this a string')
    True
    >>> check_anagrams('There', 'Their')
    False
    """
    return (
        "".join(sorted(first_str.lower())).strip()
        == "".join(sorted(second_str.lower())).strip()
    )


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    input_A = input("Enter the first string ").strip()
    input_B = input("Enter the second string ").strip()

    status = check_anagrams(input_A, input_B)
    print(f"{input_A} and {input_B} are {'' if status else 'not '}anagrams.")
