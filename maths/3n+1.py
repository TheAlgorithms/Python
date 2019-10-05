from typing import Tuple, List


def n31(a: int) -> Tuple[List[int], int]:
    """
    Returns the Collatz sequence and its length of any postiver integer.
    >>> n31(4)
    ([4, 2, 1], 3)
    """

    if not isinstance(a, int):
        raise TypeError("Must be int, not {0}".format(type(a).__name__))
    if a < 1:
        raise ValueError("Given integer must be greater than 1, not {0}".format(a))

    path = [a]
    while a != 1:
        if a % 2 == 0:
            a = a // 2
        else:
            a = 3 * a + 1
        path += [a]
    return path, len(path)


def main():
    num = 4
    path, length = n31(num)
    print(
        "The Collatz sequence of {0} took {1} steps. \nPath: {2}".format(
            num, length, path
        )
    )


if __name__ == "__main__":
    main()
