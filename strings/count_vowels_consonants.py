def count_vowels_and_consonants(text: str) -> tuple[int, int]:
    """
        Count the number of vowels and consonants in a given string.

        This function ignores non-alphabetic characters.

        Args:
            text (str): Input string.

        Returns:
            tuple[int, int]: A tuple containing (vowel_count,
    consonant_count).
     Examples:
        >>> count_vowels_and_consonants("Hello World")
        (3, 7)
        >>> count_vowels_and_consonants("AEIOU")
        (5, 0)
        >>> count_vowels_and_consonants("bcdf")
        (0, 4)
        >>> count_vowels_and_consonants("")
        (0, 0)
    """
    vowels = set("aeiouAEIOU")
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count
