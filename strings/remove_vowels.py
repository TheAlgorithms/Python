"""
A vowel is a sound such as the ones represented in writing
by the letters 'a', 'e', 'i', ' o', and 'u',
which you pronounce with your mouth open, allowing the air to flow through it.

This function removes all the vowels present in the given sentence or a word.
returns the modified version of that string.
eg: HEllO World >> HLL Wrld
"""


def remove_vowels(sentence: str) -> str:
    """
    This remove_vowels function removes all the vowels
    from a given sentence or a word

    >>> remove_vowels('Hello world')
    'Hll wrld'
    >>> remove_vowels('Programming is my passion')
    'Prgrmmng s my pssn'
    >>> remove_vowels('I love coding 24 hours')
    ' lv cdng 24 hrs'
    >>> remove_vowels('')
    ''
    """

    # List of all the vowels
    vowel_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    # iterating over a list of vowels
    for vowel in vowel_list:
        # replacing the vowel with blank
        sentence = sentence.replace(vowel, "")

    # returning a updated string
    return sentence


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # passing a string to a function removeVowels and printing the result
    print(remove_vowels("Welcome to HACKTOBERFEST 2022"))
