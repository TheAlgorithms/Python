def remove_duplicates(sentence: str) -> str:
    """
    Remove duplicates from sentence and return words in sorted order

    Args:
        sentence: Input string containing words separated by spaces

    Returns:
        String with unique words sorted alphabetically

    Examples:
        Basic functionality:
        >>> remove_duplicates("Python is great and Java is also great")
        'Java Python also and great is'

        Multiple spaces handling:
        >>> remove_duplicates("Python   is      great and Java is also great")
        'Java Python also and great is'

        Edge cases:
        >>> remove_duplicates("")
        ''

        >>> remove_duplicates("   ")
        ''

        >>> remove_duplicates("hello")
        'hello'

        >>> remove_duplicates("hello hello hello")
        'hello'

        Mixed case (case sensitive):
        >>> remove_duplicates("Python python PYTHON")
        'PYTHON Python python'

        Numbers and special characters:
        >>> remove_duplicates("1 2 3 1 2 3")
        '1 2 3'

        >>> remove_duplicates("hello world hello world!")
        'hello world world!'

        Single character words:
        >>> remove_duplicates("a b c a b c")
        'a b c'

        Mixed content:
        >>> remove_duplicates("The quick brown fox jumps over the lazy dog")
        'The brown dog fox jumps lazy over quick the'
    """
    return " ".join(sorted(set(sentence.split())))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
