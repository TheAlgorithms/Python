from functools import lru_cache


@lru_cache
def bell_number(number_of_partitions: int) -> int:
    """
    Calculate the Bell Number for a given number of partitions.
    :param number_of_partitions: The number of partitions for which to calculate the Bell Number.
    :return: The Bell Number for the given number of partitions.
    >>> bell_number(5)
    52
    >>> bell_number(0)
    1
    >>> bell_number(-1)
    Traceback (most recent call last):
        ...
    ValueError: Number of partitions should not be negative.
    """
    if number_of_partitions < 0:
        raise ValueError("Number of partitions should not be negative.")
    if number_of_partitions == 0:
        return 1
    # Initialize the Bell Number for n=1
    bell_n = [0] * (number_of_partitions + 1)
    bell_n[0] = 1
    for i in range(1, number_of_partitions + 1):
        bell_n[i] = 0
        for j in range(i):
            bell_n[i] += bell_n[j]
    return bell_n[number_of_partitions]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
