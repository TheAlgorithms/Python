# https://blog.gitnux.com/code/python-tokenize-string/#:~:text=To%20tokenize%20a%20string%20in%20Python%2C%20you%20can%20use%20the,the%20string%20at%20specific%20characters.

def tokenize_string(input_string: str, delimiter: str = ' ') -> list:
    """
    Tokenize a string based on a specified delimiter.

    Args:
        input_string (str): The input string to be tokenized.
        delimiter (str): The delimiter used for splitting the string. Default is a space.

    Returns:
        list: A list of tokens.

    >>> tokenize_string("This is a sample sentence.")
    ['This', 'is', 'a', 'sample', 'sentence.']
    >>> tokenize_string("Comma,Separated,Values", delimiter=',')
    ['Comma', 'Separated', 'Values']
    >>> tokenize_string("NoDelimiterInThisString")
    ['NoDelimiterInThisString']
    """
    if delimiter == '':
        raise ValueError("Delimiter cannot be an empty string")

    tokens = input_string.split(delimiter)
    return tokens

if __name__ == "__main__":
    import doctest

    doctest.testmod()
