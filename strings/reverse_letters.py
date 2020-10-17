def reverse_letters(input_str: str) -> str:
    '''
    Reverses letters in a given string without adjusting the postion of the words
    >>> reverse_letters('The cat in the hat')
    'ehT tac ni eht tah'
    >>> reverse_letters('The quick brown fox jumped over the lazy dog.')
    'ehT kciuq nworb xof depmuj revo eht yzal .god'
    >>> reverse_letters('Is this true?')
    'sI siht ?eurt'
    '''
    arr = []  # create an empty list
    for i in input_str.split(' '):  # Runs a for loop in a list of the string separated by space
        arr.append(i[::-1])  # Appends reversed letter of a single word
    return ' '.join(arr) # returns the arr joined with spaces


if __name__ == '__main__':
    import doctest

    doctest.testmod()
