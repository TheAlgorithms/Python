def substrings(string: str) -> list[str]:
    """
    Return a list of substrings of given string

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
    # iterate for every characters of the string
    for index1 in range(0, len(string)):
        temp = ""
        # substrings relative to each character of string
        for index2 in range(index1, len(string)):
            temp += string[index2]
            answer.append(temp)
    return answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
