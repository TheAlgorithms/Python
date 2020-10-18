def reverse_letters(input_str: str) -> str:
    """
    Reverses letters in a given string without adjusting the position of the words
    >>> reverse_letters('The cat in the hat')
    'ehT tac ni eht tah'
    >>> reverse_letters('The quick brown fox jumped over the lazy dog.')
    'ehT kciuq nworb xof depmuj revo eht yzal .god'
    >>> reverse_letters('Is this true?')
    'sI siht ?eurt'
    """
    reversed_letters_list = []
    for i in input_str.split(" "):
        reversed_letters_list.append(i[::-1])
    return " ".join(reversed_letters_list)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
