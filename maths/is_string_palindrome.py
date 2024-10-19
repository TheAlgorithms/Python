def is_string_palindrome(words: str) -> bool:
    cleaned_phrase = ''.join(words.split()).lower()
    return cleaned_phrase == cleaned_phrase[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()