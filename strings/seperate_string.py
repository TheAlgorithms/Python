"""
https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/

An algorith that seperates the characers in a string and sorts them into a list.
This can also append the characters into a provided list.
"""


def seperate(text, provided_list=None) -> list:
    """ This seperates each character of a string and sorts them into a new list or a provided list.
        >>> test_text = "hello"
        >>> test_list = ['t', 'e', 's', 't', ' ']
        >>> print(seperate(test_text, test_list))
        ['t', 'e', 's', 't', ' ', 'h', 'e', 'l', 'l', 'o']
        >>> print(seperate(test_text))
        ['h', 'e', 'l', 'l', 'o']
    """

    if provided_list is None:
        seperated_text = []
    
    else:
        seperated_text = provided_list

    for x in text:
        seperated_text.append(x)
    
    # Returns a list with each character of the inputed text seperated
    return seperated_text

if __name__ == '__main__':
    import doctest
    doctest.testmod()
