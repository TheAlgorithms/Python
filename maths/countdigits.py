def count_digits_recursive(n: int) -> int:
    ''' divide each digit by 10 so remainder will be that number '''
    if n//10 == 0:
        return 1
    return count_digits_recursive(int(n / 10)) + 1


def count_digits(n: int) -> int:
    ''' non-recursive way of digit count '''
    count = 0
    while n > 0:
        n = int(n / 10)
        count += 1
    return count


if __name__ == "__main__":
    n = 1568468461984216484351648351648864306186431654986465151846135
    print(count_digits_recursive(n))
    print(count_digits(n))
    import doctest

    doctest.testmod()
