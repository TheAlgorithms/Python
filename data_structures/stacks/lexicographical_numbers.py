from collections.abc import Iterator


def lexical_order(max_number: int) -> Iterator[int]:
    """
    Generate numbers in lexical order from 1 to max_number.

    >>> " ".join(map(str, lexical_order(13)))
    '1 10 11 12 13 2 3 4 5 6 7 8 9'
    >>> list(lexical_order(1))
    [1]
    >>> " ".join(map(str, lexical_order(20)))
    '1 10 11 12 13 14 15 16 17 18 19 2 20 3 4 5 6 7 8 9'
    >>> " ".join(map(str, lexical_order(25)))
    '1 10 11 12 13 14 15 16 17 18 19 2 20 21 22 23 24 25 3 4 5 6 7 8 9'
    >>> list(lexical_order(12))
    [1, 10, 11, 12, 2, 3, 4, 5, 6, 7, 8, 9]
    """

    stack = [1]

    while stack:
        num = stack.pop()
        if num > max_number:
            continue

        yield num
        if (num % 10) != 9:
            stack.append(num + 1)

        stack.append(num * 10)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"Numbers from 1 to 25 in lexical order: {list(lexical_order(26))}")
