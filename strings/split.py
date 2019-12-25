def split(string: str, seperator: str = " ") -> list:
    """
    Will split the string up into all the values seperated by the seperator (defaults to spaces)
    
    >>> split("apple#banana#cherry#orange",seperator='#')
    ['apple', 'banana', 'cherry', 'orange']
    
    >>> split("Hello there")
    ['Hello', 'there']
    
    >>> split("11/22/63",seperator = '/')
    ['11', '22', '63']
    
    >>> split("12:43:39",seperator = ":")
    ['12', '43', '39']
    """

    split_words = []

    last_index = 0
    for index, char in enumerate(string):
        if char == seperator:
            split_words.append(string[last_index:index])
            last_index = index + 1
        elif index + 1 == len(string):
            split_words.append(string[last_index : index + 1])
    return split_words


if __name__ == "__main__":
    from doctest import testmod

    testmod()
