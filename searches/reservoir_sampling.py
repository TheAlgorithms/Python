"""
Reservoir Sampling Algorithm

Use Case:
Efficient for selecting `sample_size` random items from a data stream of unknown size,
or when the entire dataset cannot fit into memory.

Time Complexity:
- O(n), where n is the total number of items
- Space Complexity: O(sample_size)

Author: Michael Alexander Montoya
"""

import random
from typing import Iterable


def reservoir_sampling(stream: Iterable[int], sample_size: int) -> list[int]:
    """
    Performs reservoir sampling on a stream of items.

    Args:
        stream: An iterable data stream.
        sample_size: Number of items to sample.

    Returns:
        A list containing `sample_size` randomly sampled items from the stream.

    >>> result = reservoir_sampling(range(1, 1001), 10)
    >>> len(result) == 10
    True
    """
    reservoir = []

    for i, item in enumerate(stream):
        if i < sample_size:
            reservoir.append(item)
        else:
            j = random.randint(0, i)
            if j < sample_size:
                reservoir[j] = item

    return reservoir


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    stream_data = range(1, 1001)
    sample = reservoir_sampling(stream_data, 10)
    print(f"Sampled items: {sample}")
