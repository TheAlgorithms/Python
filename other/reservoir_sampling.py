"""
reservoir_sampling.py

An implementation of Reservoir Sampling — a random algorithm to
select `k` items from a stream of unknown or very large size with equal probability.

Reference:
https://en.wikipedia.org/wiki/Reservoir_sampling

Example:
>>> data_stream = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> len(reservoir_sampling(data_stream, 3))
3
>>> all(isinstance(i, int) for i in reservoir_sampling(data_stream, 3))
True
"""

import random
from typing import Iterable, List, TypeVar

T = TypeVar("T")


def reservoir_sampling(stream: Iterable[T], k: int) -> List[T]:
    """
    Return a random sample of size `k` from the given data stream.

    :param stream: An iterable data stream (e.g., list, generator)
    :param k: Number of elements to sample
    :return: A list of `k` randomly selected items

    >>> data = [10, 20, 30, 40, 50]
    >>> len(reservoir_sampling(data, 2))
    2
    >>> isinstance(reservoir_sampling(data, 3), list)
    True
    >>> try:
    ...     reservoir_sampling([], 1)
    ... except ValueError:
    ...     print("Error")
    Error
    """
    if k <= 0:
        raise ValueError("Sample size k must be greater than zero")

    reservoir = []
    for i, item in enumerate(stream):
        if i < k:
            reservoir.append(item)
        else:
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = item

    if len(reservoir) < k:
        raise ValueError("Stream has fewer elements than the requested sample size")

    return reservoir


if __name__ == "__main__":
    # Example usage
    data_stream = range(1, 100)
    sample = reservoir_sampling(data_stream, 5)
    print("Random sample from stream:", sample)
