def remove_duplicates(sentence: str) -> str:
    """
    Remove duplicate words from sentence and return sorted unique words.

    Note: The output words are sorted alphabetically, not in original order.

    >>> remove_duplicates("Python is great and Java is also great")
    'Java Python also and great is'
    >>> remove_duplicates("Python   is      great and Java is also great")
    'Java Python also and great is'
    """
    return " ".join(sorted(set(sentence.split())))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
