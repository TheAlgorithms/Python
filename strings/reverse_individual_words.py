def reverse_individual_words(input_str: str) -> str:
    """
    Reverses words in a given string
    >>> reverse_individual_words("This is a text")
    'sihT si a txet'
    >>> reverse_individual_words("Another 1234 text")
    'rehtonA 4321 txet'
    >>> reverse_individual_words("A sentence with full stop.")
    'A ecnetnes htiw lluf pots.'
    """
    individual_reverse_string = []
    for word in input_str.split(" "):
        if word[-1] in [".", "!", "?"]:
            individual_reverse_string.append(word[-2::-1] + word[-1])
        else:
            individual_reverse_string.append(word[::-1])

    return " ".join(individual_reverse_string)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
