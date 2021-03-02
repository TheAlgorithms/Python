def decimal_to_binary(number: int) -> str:
    """
    Return a binary string
    >>> decimal_to_binary(0)
    '0'
    >>> decimal_to_binary(1)
    '1'
    >>> decimal_to_binary(8)
    '1000'
    >>> decimal_to_binary(110)
    '1101110'
    >>> decimal_to_binary(-20)
    '-10100'
    >>> decimal_to_binary("abc")
    Traceback (most recent call last):
        ...
    ValueError: Input is not valid
    >>> decimal_to_binary([])
    Traceback (most recent call last):
        ...
    ValueError: Input is not valid
    """
    if not isinstance(number, int):
        raise ValueError("Input is not valid")
    if number == 0:
        return "0"
    flag = 0
    if number < 0:
        number *= -1
        flag = 1
    answer = ""
    while number:
        answer += str(number % 2)
        number = number // 2
    answer = answer[-1::-1]
    if flag:
        answer = "-" + answer
    return answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
