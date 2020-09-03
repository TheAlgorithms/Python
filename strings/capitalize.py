import string

def capitalize(sentence: str) -> str:
    """
    This function will capitalize the first letter of a sentence or a word
    >>> capitalize("hello world")
    'Hello world'
    >>> capitalize("123 hello world")
    '123 hello world'
    >>> capitalize(" hello world")
    ' hello world'
    """
    
    """
    Creates a new dictionary which keys are lowercase letters and the values are their corresponding uppercase letter.
    It gets the first character of the sentence and if that character is a key in the dictionary, it gets the value 
    and use it as the first character of the sentence.
    """
    first_letter = sentence[0]
    lower_upper_dict = dict()
    for lower, upper in zip(string.ascii_lowercase, string.ascii_uppercase): 
        lower_upper_dict[lower] = upper
    if first_letter in lower_upper_dict:
        new_sentence = lower_upper_dict[first_letter] + sentence[1:] 
    else:
        new_sentence = sentence
    return new_sentence


if __name__ == "__main__":
    from doctest import testmod

    testmod()
