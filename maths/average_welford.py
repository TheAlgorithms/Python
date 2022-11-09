def average_welford(values: list) -> float:
    """

    calculates average of all given
    values with high precision

    >>> average_welford([1, 2, 3, 4, 5])
    3.0
    >>> average_welford([1.2329435, 2.209462409, 3.230925, 4.47626462, 5.2938759204])
    3.2886942898799996
    >>> average_welford([-5738.2329, 224.209462, 463.230, 85673.47626, -2436.2938759])
    15637.277789219997

    """

    avg = 0.0
    for index in range(len(values)):
        avg += (values[index] - avg) / (index + 1)
    return avg


if __name__ == "__main__":
    __import__("doctest").testmod()
