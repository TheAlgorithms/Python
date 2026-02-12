def string_statistics(text: str) -> dict[str, int]:
    """
    Return statistics about a string.

    >>> string_statistics("Hello")
    {'length': 5, 'vowels': 2, 'consonants': 3}

    >>> string_statistics("")
    {'length': 0, 'vowels': 0, 'consonants': 0}
    """
    vowels = "aeiouAEIOU"

    length = len(text)
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)

    return {
        "length": length,
        "vowels": vowel_count,
        "consonants": consonant_count,
    }


if __name__ == "__main__":
    from doctest import testmod

    testmod()
