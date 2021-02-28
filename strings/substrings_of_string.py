def substrings(string: str) -> list:
    """
    return  all the substrings of string

    >>> substrings("a")
    ['a']
    >>> substrings("abc")
    ['a', 'ab', 'abc', 'b', 'bc', 'c']
    >>> substrings("aaa")
    ['a', 'aa', 'aaa', 'a', 'aa', 'a']
    >>> substrings("ayu")
    ['a', 'ay', 'ayu', 'y', 'yu', 'u']
    >>> substrings("2001")
    ['2', '20', '200', '2001', '0', '00', '001', '0', '01', '1']
    """
    answer = list()
    for _ in range(0, len(string)):
        temp = ""
        for __ in range(_, len(string)):
            temp += string[__]
            answer.append(temp)
    return answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
