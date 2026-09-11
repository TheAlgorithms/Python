from __future__ import annotations

import math


def cosine_similarity(vector_a: list[float], vector_b: list[float]) -> float:
    """
    Finds the cosine similarity between two multi-dimensional vectors.
    The result ranges from -1 (exactly opposite) to 1 (exactly the same).

    https://en.wikipedia.org/wiki/Cosine_similarity

    >>> cosine_similarity([1, 2, 3], [1, 2, 3])
    1.0
    >>> cosine_similarity([1, 0], [0, 1])
    0.0
    >>> cosine_similarity([1, 2, 3], [-1, -2, -3])
    -1.0
    """
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must be of the same length")

    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))

    magnitude_a = math.sqrt(sum(a * a for a in vector_a))
    magnitude_b = math.sqrt(sum(b * b for b in vector_b))

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Cannot compute similarity with a zero-vector")

    return dot_product / (magnitude_a * magnitude_b)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
