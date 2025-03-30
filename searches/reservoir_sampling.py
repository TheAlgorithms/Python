"""
Reservoir Sampling Algorithm

Use Case:
Efficient for selecting k random items from a data stream of unknown size,
or when the entire dataset cannot fit into memory.

Time Complexity:
- O(n), where n is the total number of items
- Space Complexity: O(k)

Author: Michael Alexander Montoya
"""

import random

def reservoir_sampling(stream, k):
    """
    Performs reservoir sampling on a stream of items.

    Args:
        stream: An iterable data stream.
        k: Number of items to sample.

    Returns:
        A list containing k randomly sampled items from the stream.
    """

    reservoir = []

    for i, item in enumerate(stream):
        if i < k:
            reservoir.append(item)
        else:
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = item

    return reservoir


# Example usage
if __name__ == "__main__":
    stream_data = range(1, 1001)  # Simulate a stream of numbers from 1 to 1000
    sample_size = 10

    sample = reservoir_sampling(stream_data, sample_size)
    print(f"Random sample of {sample_size} items from stream: {sample}")
