def countAndSay(n: int) -> str:
    """
    Generate the n-th term of the count-and-say sequence.

    The count-and-say sequence is a series of number strings that follows
    a recursive formula. To get the next number in the sequence, you "say"
    the previous number and then convert it into a new number string.

	Examples:
        >>> countAndSay(1)
        '1'
        >>> countAndSay(4)
        '1211'
        >>> countAndSay(5)
        '111221'
        >>> countAndSay(6)
        '312211'
    """
    if n == 1:
        return "1"
    
    prev = countAndSay(n - 1)
    result = ""
    count = 1
    
    for i in range(len(prev)):
        if i + 1 < len(prev) and prev[i] == prev[i + 1]:
            count += 1
        else:
            result += str(count) + prev[i]
            count = 1
    
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
