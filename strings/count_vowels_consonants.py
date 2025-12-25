def count_vowels_and_consonants(text: str) -> tuple[int, int]:
    """
        Count the number of vowels and consonants in a given string.

        This function ignores non-alphabetic characters.

        Args:
            text (str): Input string.

        Returns:
            tuple[int, int]: A tuple containing (vowel_count,
    consonant_count).
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


if _name_ == "_main_":
    print(count_vowels_and_consonants("Hello World"))
