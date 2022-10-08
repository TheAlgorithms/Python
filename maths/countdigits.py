def count_digits_recursive(num: int) -> int:
    """divide each digit by 10 so remainder will be that number"""
    if num // 10 == 0:
        return 1
    return count_digits_recursive(int(num / 10)) + 1


def count_digits(num: int) -> int:
    """non-recursive way of digit count"""
    count = 0
    while num > 0:
        num = int(num / 10)
        count += 1
    return count


def count_using_conversion(num: int) -> int:
    """by conversion integer to string and get length of string"""
    return len(str(num))


if __name__ == "__main__":
    num = 1568468461984216484351648351648864306186431654986465151846135
    print(count_digits_recursive(num))
    print(count_digits(num))
    print(count_using_conversion(num))
    import doctest

    doctest.testmod()
