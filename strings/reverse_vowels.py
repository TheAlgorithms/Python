"""
Author: J. Samuel
"""

vowels = {"a", "e", "i", "o", "u"}


def is_vowel(letter: str) -> bool:
    """
    >>> is_vowel('a')
    True
    >>> is_vowel('b')
    False

    Return true if letter is a vowel, otherwise false
    """
    return letter in vowels


def swap_letters(idx1: int, idx2: int, word_list: list):
    """
    Swaps the letters at index idx1 and idx2 in word_list
    """
    word_list[idx1], word_list[idx2] = word_list[idx2], word_list[idx1]


def reverse_vowels(word: str) -> str:
    """
    >>> reverse_vowels('beautiful')
    'buiutafel'
    >>> reverse_vowels('banana')
    'banana'

    Reverses the vowels in an English word and returns it (O(n)).

    Args:
        word (str): given word/string
    """
    # Split word into list of characters
    word_list = [word[i] for i in range(len(word))]
    idx1, idx2 = 0, len(word_list) - 1

    while idx1 < idx2:

        is_left_char_vowel = is_vowel(word_list[idx1].lower())
        is_right_char_vowel = is_vowel(word_list[idx2].lower())

        # Both characters not vowels so move pointers
        if not is_left_char_vowel and not is_right_char_vowel:
            idx1 += 1
            idx2 -= 1

        # Both characters are vowels so swap them and move pointers
        elif is_left_char_vowel and is_right_char_vowel:
            swap_letters(idx1, idx2, word_list)
            idx1 += 1
            idx2 -= 1

        # Right character is not a vowel so move pointer left
        elif not is_right_char_vowel:
            idx2 -= 1

        # Left character is not a vowel so move pointer right
        else:
            idx1 += 1

    return "".join(word_list)


def main():
    words = []
    words.append("hello world")
    words.append("steph cUrry")
    words.append("lebron james")
    words.append("aeuOi")
    words.append("aeio")
    words.append("potatO")
    words.append("leGoAt")
    words.append("finger guns")
    words.append("beautiful")
    words.append("banana")
    words.append("soiree")

    for word in words:
        word_reversed = reverse_vowels(word)
        print(word, "=>", word_reversed)
        assert word == reverse_vowels(word_reversed)
        print(word_reversed, "=>", reverse_vowels(word_reversed), "\n")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
