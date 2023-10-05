def is_disarium(num: int) -> bool:
    """A Disarium number is an integer where the sum of
    each digit raised to the power of its position
    in the number, is equal to the number.

    Example- 175 is a disarium number
    because 1^1 + 7^2 + 5^3 = 1 + 49 + 125 = 175

    Usage examples:
    >>> is_disarium(1)
    True
    >>> is_disarium(89)
    True
    >>> is_disarium(175)
    True
    >>> is_disarium(2427)
    True
    >>> is_disarium(150)
    False
    >>> is_disarium(63)
    False
    >>> is_disarium(2547)
    False

    """

    exponent = 1
    answer = 0
    temp = str(num)
    for i in temp:
        answer += int(i) ** exponent
        exponent += 1
    if answer == num:
        return True
    else:
        return False


if __name__ == "__main__":
    print(f"{is_disarium(2547) = }")
