from typing import List, Tuple


def n31(a: int) -> Tuple[List[int], int]:
    """
    Returns the Collatz sequence and its length of any positive integer.
    >>> n31(4)
    ([4, 2, 1], 3)
    """

    if not isinstance(a, int):
        raise TypeError("Must be int, not {}".format(type(a).__name__))
    if a < 1:
        raise ValueError(f"Given integer must be greater than 1, not {a}")

    path = [a]
    while a != 1:
        if a % 2 == 0:
            a = a // 2
        else:
            a = 3 * a + 1
        path += [a]
    return path, len(path)


def test_n31():
    """
    >>> test_n31()
    """
    assert n31(4) == ([4, 2, 1], 3)
    assert n31(11) == ([11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], 15)
    assert n31(31) == (
        [
            31,
            94,
            47,
            142,
            71,
            214,
            107,
            322,
            161,
            484,
            242,
            121,
            364,
            182,
            91,
            274,
            137,
            412,
            206,
            103,
            310,
            155,
            466,
            233,
            700,
            350,
            175,
            526,
            263,
            790,
            395,
            1186,
            593,
            1780,
            890,
            445,
            1336,
            668,
            334,
            167,
            502,
            251,
            754,
            377,
            1132,
            566,
            283,
            850,
            425,
            1276,
            638,
            319,
            958,
            479,
            1438,
            719,
            2158,
            1079,
            3238,
            1619,
            4858,
            2429,
            7288,
            3644,
            1822,
            911,
            2734,
            1367,
            4102,
            2051,
            6154,
            3077,
            9232,
            4616,
            2308,
            1154,
            577,
            1732,
            866,
            433,
            1300,
            650,
            325,
            976,
            488,
            244,
            122,
            61,
            184,
            92,
            46,
            23,
            70,
            35,
            106,
            53,
            160,
            80,
            40,
            20,
            10,
            5,
            16,
            8,
            4,
            2,
            1,
        ],
        107,
    )


if __name__ == "__main__":
    num = 4
    path, length = n31(num)
    print(f"The Collatz sequence of {num} took {length} steps. \nPath: {path}")
