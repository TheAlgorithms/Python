"""
The Josephus problem is a famous theoretical problem related to a certain
counting-out game. This module provides functions to solve the Josephus problem
for n people and a step size of k.

The Josephus problem is defined as follows:
- n people are standing in a circle.
- Starting with a specified person, you count around the circle,
  skipping a fixed number of people (k).
- The person at which you stop counting is eliminated from the circle.
- The counting continues until only one person remains.

For more information about the Josephus problem, refer to:
https://en.wikipedia.org/wiki/Josephus_problem
"""


def josephus_recursive(n: int, k: int) -> int:
    """
    Solve the Josephus problem for n people and a step size of k recursively.

    Args:
        n (int): Number of people.
        k (int): Step size for elimination.

    Returns:
        int: The position of the last person remaining.

    Examples:
        >>> josephus_recursive(7, 3)
        3
        >>> josephus_recursive(10, 2)
        4
    """
    if n == 1:
        return 0

    return (josephus_recursive(n - 1, k) + k) % n


def find_winner(n: int, k: int) -> int:
    """
    Find the winner of the Josephus problem for n people and a step size of k.

    Args:
        n (int): Number of people.
        k (int): Step size for elimination.

    Returns:
        int: The position of the last person remaining (1-based index).

    Examples:
        >>> find_winner(7, 3)
        4
        >>> find_winner(10, 2)
        5
    """
    return josephus_recursive(n, k) + 1


def josephus_iterative(n: int, k: int) -> int:
    """
    Solve the Josephus problem for n people and a step size of k iteratively.

    Args:
        n (int): The number of people in the circle.
        k (int): The number of steps to take before eliminating someone.

    Returns:
        int: The position of the last person standing.

    Examples:
        >>> josephus_iterative(5, 2)
        3
        >>> josephus_iterative(7, 3)
        4
    """
    circle = list(range(1, n + 1))
    current = 0

    while len(circle) > 1:
        current = (current + k - 1) % len(circle)
        circle.pop(current)

    return circle[0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
