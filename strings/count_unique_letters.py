def unique_letters(word) -> None:
    """
    >>> unique_letters('abbccc')
    {'a': 1, 'b': 2, 'c': 3}
    >>> unique_letters('mellow')
    {'m': 1, 'e': 1, 'l': 2, 'o': 1, 'w': 1}
    """
    dct = {}
    for i in word:
        if i == " ":
            pass
        else:
            if i in dct.keys():
                dct[i] += 1
            else:
                dct[i] = 1
    print(dct)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    unique_letters(input("enter word: "))
