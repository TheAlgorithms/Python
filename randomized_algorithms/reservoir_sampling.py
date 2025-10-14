import random
from typing import List, Iterator, TypeVar

T = TypeVar("T")


def reservoir_sampling(stream: Iterator[T], k: int) -> List[T]:
    """
    Randomly select k items from a stream of unknown length using reservoir sampling.

    Args:
        stream (Iterator[T]): Input data stream.
        k (int): Number of items to sample.

    Returns:
        List[T]: List of k randomly sampled items.

    Examples:
    >>> stream = iter(range(1, 11))
    >>> len(reservoir_sampling(stream, 5))
    5
    """
    reservoir: List[T] = []
    for i, item in enumerate(stream):
        if i < k:
            reservoir.append(item)
        else:
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = item
    return reservoir


if __name__ == "__main__":
    import doctest

    doctest.testmod()
