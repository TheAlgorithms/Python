"""
Cosine similarity is a metric used to measure how similar two vectors are,
regardless of their magnitude. It calculates the cosine of the angle between
two vectors projected in a multi-dimensional space.

Widely used in information retrieval, text mining, and recommendation systems.
In NLP and AI, cosine similarity is fundamental for comparing document embeddings,
word vectors, and semantic similarity.

https://en.wikipedia.org/wiki/Cosine_similarity

Cosine similarity = (A · B) / (||A|| * ||B||)

Where:
    A · B is the dot product of vectors A and B
    ||A|| is the magnitude (L2 norm) of vector A
    ||B|| is the magnitude (L2 norm) of vector B
"""

import math


def cosine_similarity(vector_a: list[float], vector_b: list[float]) -> float:
    """
    Calculates the cosine similarity between two vectors.

    Parameters:
        vector_a: A non-empty numerical vector.
        vector_b: A non-empty numerical vector of the same dimension as vector_a.

    Returns:
        The cosine similarity between the two vectors, a float in [-1, 1].
        1 means identical direction, 0 means orthogonal, -1 means opposite.

    >>> cosine_similarity([1, 2, 3], [1, 2, 3])
    1.0
    >>> cosine_similarity([1, 2, 3], [-1, -2, -3])
    -1.0
    >>> cosine_similarity([1, 0, 0], [0, 1, 0])
    0.0
    >>> cosine_similarity([1, 1], [1, 1])
    1.0
    >>> round(cosine_similarity([1, 2, 3], [4, 5, 6]), 6)
    0.974632
    >>> round(cosine_similarity([3, 45, 7, 2], [2, 54, 13, 15]), 6)
    0.972583
    >>> cosine_similarity([], [1, 2])
    Traceback (most recent call last):
        ...
    ValueError: Vectors must not be empty.
    >>> cosine_similarity([1, 2], [1, 2, 3])
    Traceback (most recent call last):
        ...
    ValueError: Vectors must have the same dimension.
    >>> cosine_similarity([0, 0, 0], [1, 2, 3])
    Traceback (most recent call last):
        ...
    ValueError: At least one vector has zero magnitude.
    """
    if not vector_a or not vector_b:
        raise ValueError("Vectors must not be empty.")

    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same dimension.")

    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
    magnitude_a = math.sqrt(sum(a * a for a in vector_a))
    magnitude_b = math.sqrt(sum(b * b for b in vector_b))

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("At least one vector has zero magnitude.")

    return dot_product / (magnitude_a * magnitude_b)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
