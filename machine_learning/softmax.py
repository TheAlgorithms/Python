"""Softmax activation function for multiclass classification.

Softmax converts a sequence of scores into probabilities that sum to one.

>>> probabilities = softmax([2.0, 1.0, 0.1])
>>> [round(value, 4) for value in probabilities]
[0.659, 0.2424, 0.0986]
>>> sum(softmax([1.0, 2.0, 3.0]))
1.0
>>> softmax([])
Traceback (most recent call last):
    ...
ValueError: scores must not be empty
"""

import math


def softmax(scores: list[float]) -> list[float]:
    """Return softmax probabilities for a non-empty list of scores.

    Subtracting the maximum score before exponentiation improves numerical
    stability and prevents overflow for large input values.
    """
    if not scores:
        raise ValueError("scores must not be empty")

    max_score = max(scores)
    exponentials = [math.exp(score - max_score) for score in scores]
    total = sum(exponentials)
    return [value / total for value in exponentials]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
