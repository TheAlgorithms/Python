def reverse_letters(input_str: str) -> str:
    """
    Reverses letters in a given string without adjusting the position of the words
    >>> reverse_letters('The cat in the hat')
    'ehT tac ni eht tah'
    >>> reverse_letters('The quick brown fox jumped over the lazy dog.')
    'ehT kciuq nworb xof depmuj revo eht yzal .god'
    >>> reverse_letters('Is this true?')
    'sI siht ?eurt'
    >>> reverse_letters("I   love       Python")
    'I evol nohtyP'
    """
    return " ".join([word[::-1] for word in input_str.split()])
#reverse string without using[::-1] & reverse function
def reverse_str_letter(input_str: str) -> str:
    rev=""
    for i in input_str:
        rev=rev+i
    return rev


if __name__ == "__main__":
    import doctest

    doctest.testmod()
