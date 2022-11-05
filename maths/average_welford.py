def average_welford(values: list) -> float:
    """

    calculates average of all given
    values with high precision

    >>> average_welford([1, 2, 3, 4, 5])
    3.0
    >>> average_welford([1.2329435, 2.209462409, 3.230925, 4.47626462, 5.2938759204])
    3.2886942898799996
    >>> average_welford([-57386462.2329435, 2246262.209462409, 4632463.230925, 856737354.47626462, -243664265.2938759204])
    112513070.4779665

    """

    avg = 0.0
    for index in range(0, len(values)):
        avg += (values[index] - avg) / (index + 1)
    return avg


if __name__ == "__main__":
    __import__("doctest").testmod()
