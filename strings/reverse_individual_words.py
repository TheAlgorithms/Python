def reverse_individual_words(input_str: str) -> str:
    """
    Reverses words in a given string
    >>> reverse_individual_words("This is a text")
    'sihT si a txet'
    >>> reverse_individual_words("Another 1234 text")
    'rehtonA 4321 txet'
    """
    individual_reverse_string = []
    for word in input_str.split(" "):
        individual_reverse_string.append(word[::-1])
    
    return " ".join(individual_reverse_string)


if __name__ == "__main__":
    import doctest

    doctest.testmod()