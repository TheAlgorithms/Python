# pig_latin.py


def pig_latin(sentence: str) -> str:
    """Compute the piglatin of a given string.

    Usage examples:
    >>> pig_latin("pig")
    'igpay'
    >>> pig_latin("latin")
    'atinlay'
    >>> pig_latin("banana")
    'ananabay'
    >>> pig_latin("friends")
    'iendsfray'
    >>> pig_latin("smile")
    'ilesmay'
    >>> pig_latin("string")
    'ingstray'
    >>> pig_latin("eat")
    'eatway'
    >>> pig_latin("omelet")
    'omeletway'
    >>> pig_latin("are")
    'areway'

    """

    sentence = sentence.lower()
    length = len(sentence)
    if sentence[0] in "aeiou":
        result = sentence + "way"
    else:
        for i in range(length):
            if sentence[i] in "aeiou":
                break
        result = sentence[i:] + sentence[:i] + "ay"
    return result


statement = input("Enter a string: ")
answer = pig_latin(statement)

print(f'The PIG LATIN of the entered string is "{answer}"')
