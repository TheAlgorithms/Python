"""
Calculate the minimum waiting time using a greedy algorithm.
reference: https://www.youtube.com/watch?v=Sf3eiO12eJs

For doctests run following command:
python -m doctest -v minimum_waiting_time.py

The minimum_waiting_time function uses a greedy algorithm to calculate the minimum
time for queries to complete. It sorts the list in non-decreasing order, calculates
the waiting time for each query by multiplying its position in the list with the
sum of all remaining query times, and returns the total waiting time. A doctest
ensures that the function produces the correct output.
"""


def minimum_waiting_time(queries: list[int]) -> int:
    """
    This function takes a list of query times and returns the minimum waiting time
    for all queries to be completed.

    Args:
        queries: A list of queries measured in picoseconds

    Returns:
        total_waiting_time: Minimum waiting time measured in picoseconds

    Examples:
    >>> minimum_waiting_time([3, 2, 1, 2, 6])
    17
    >>> minimum_waiting_time([3, 2, 1])
    4
    >>> minimum_waiting_time([1, 2, 3, 4])
    10
    >>> minimum_waiting_time([5, 5, 5, 5])
    30
    >>> minimum_waiting_time([])
    0
    """
    n = len(queries)
    if n in (0, 1):
        return 0
    return sum(query * (n - i - 1) for i, query in enumerate(sorted(queries)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
