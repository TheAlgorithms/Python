def capitalize(str: sentence) -> str:
    """
    This function will capitalize the first word of a sentence
    >>> capitalize("hello world")
        Hello world
    >>> capitalize("123 hello world)
        123 hello world
    """

    sentence = sentence.lsplit()
    firstChar = sentence[0]
    if isalpha(firstChar):
        upperCaseChar = str.upper(firstChar)
        sentence[0] = str.upper(firstChar)
    print(sentence)


capitalize("hello world")
